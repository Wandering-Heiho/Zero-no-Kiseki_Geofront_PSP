from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4000.bin",                # FileName
        "t4000",                    # MapName
        "t4000",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 3, 0, 4],
    )

    BuildStringList((
        "t4000",                  # 0
        "Father Roland",          # 1
        "Sister Juju",            # 2
        "Tamil",                  # 3
        "Hamil",                  # 4
        "Estelle",                # 5
        "Joshua",                 # 6
        "Bracer Lynn",            # 7
        "Bracer Aeolia",          # 8
        "Tourist Von Tienne",     # 9
        "Mainz Mountain Path",    # 10
    ))

    AddCharChip((
        "chr/ch25400.itc",                   # 00
        "chr/ch25500.itc",                   # 01
        "chr/ch23800.itc",                   # 02
        "chr/ch00600.itc",                   # 03
        "chr/ch00700.itc",                   # 04
        "chr/ch32000.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch32400.itc",                   # 07
    ))

    DeclNpc(-2630,   0,       9369,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2299,    0,       14270,   180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5780,   0,       14529,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5780,   0,       13680,   0,    385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(21059,   0,       40569,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(20940,   0,       44159,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-9,      0,       5010,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(1200,    0,       4199,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1940,   9,       19950,   0,    385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-10390,  500,     13820,   1200,    -10390,  2000,    13820,   0x007C, 0,  18, 0x0000)

    PlaceName(5.0, -0.0, -35.0, 0x0000, 0x0000, "Mainz Mountain Path")

    ScpFunction((
        "Function_0_234",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_49E",          # 03, 3
        "Function_4_621",          # 04, 4
        "Function_5_634",          # 05, 5
        "Function_6_1431",         # 06, 6
        "Function_7_2BB4",         # 07, 7
        "Function_8_2ECC",         # 08, 8
        "Function_9_3280",         # 09, 9
        "Function_10_3337",        # 0A, 10
        "Function_11_3679",        # 0B, 11
        "Function_12_3812",        # 0C, 12
        "Function_13_3C52",        # 0D, 13
        "Function_14_3D4B",        # 0E, 14
        "Function_15_3DBA",        # 0F, 15
        "Function_16_3F2F",        # 10, 16
        "Function_17_4BDA",        # 11, 17
        "Function_18_50EB",        # 12, 18
    ))


    def Function_0_234(): pass

    label("Function_0_234")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_274"),
        (1, "loc_280"),
        (2, "loc_28C"),
        (3, "loc_298"),
        (4, "loc_2A4"),
        (5, "loc_2B0"),
        (6, "loc_2BC"),
        (SWITCH_DEFAULT, "loc_2C8"),
    )


    label("loc_274")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_280")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_28C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_298")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2EB")

    Return()

    # Function_0_234 end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, -2510, 0, 14270, 2000, 0x0)
    OP_95(0xFE, -2510, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 11020, 0, 12920, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 20000, 2000, 0x0)
    OP_95(0xFE, 18830, 0, 24520, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 31740, 2000, 0x0)
    OP_95(0xFE, 26350, 0, 46780, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 51110, 2000, 0x0)
    OP_95(0xFE, 23030, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 54060, 2000, 0x0)
    OP_95(0xFE, 21080, 0, 48950, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 44720, 2000, 0x0)
    OP_95(0xFE, 25050, 0, 34580, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 27090, 2000, 0x0)
    OP_95(0xFE, 17430, 0, 21180, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 14270, 2000, 0x0)
    Jump("Function_1_2EC")

    label("loc_43C")

    Return()

    # Function_1_2EC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49D")
    OP_95(0xFE, 23000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 42000, 6000, 0x0)
    OP_95(0xFE, 19000, 0, 39000, 6000, 0x0)
    OP_95(0xFE, 23000, 0, 39000, 6000, 0x0)
    Jump("Function_2_43D")

    label("loc_49D")

    Return()

    # Function_2_43D end

    def Function_3_49E(): pass

    label("Function_3_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_5DB")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4DC")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EA")
    Jump("loc_5DB")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_4F8")
    Jump("loc_5DB")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_510")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_528")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5DB")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 23000, 0, 41500, 0)
    SetChrPos(0xB, 23000, 0, 39000, 0)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_5DB")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_586")
    Jump("loc_5DB")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_59E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_5DB")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5DB")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_5DB")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5C8")
    Jump("loc_5DB")

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DB")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_5DB")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC")
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_60D")

    label("loc_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D")
    Event(0, 17)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_620")
    ClearChrFlags(0x10, 0x80)

    label("loc_620")

    Return()

    # Function_3_49E end

    def Function_4_621(): pass

    label("Function_4_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_633")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_633")

    Return()

    # Function_4_621 end

    def Function_5_634(): pass

    label("Function_5_634")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6FB")

    ChrTalk(
        0xFE,
        (
            "As the sun sets, so too does one's\x01",
            "field of vision. Please keep an eye\x01",
            "out for any lurking monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please make sure to be careful if you're\x01",
            "heading out onto the highway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_77C")

    ChrTalk(
        0xFE,
        (
            "Sergeant Major Seeker of the CGF has\x01",
            "come to visit us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what the nature of her visit is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_83E")

    ChrTalk(
        0xFE,
        (
            "Lately, I've felt that Crossbell has become\x01",
            "more dangerous than in past years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We must protect the cathedral and the\x01",
            "children attending Sunday School with\x01",
            "all our might.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8E2")

    ChrTalk(
        0xFE,
        (
            "Good day to you all. Welcome\x01",
            "to the Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunday School is in session right now,\x01",
            "so please try not to disturb their lessons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_965")

    ChrTalk(
        0xFE,
        "Oh, are you leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come again any time, and may the\x01",
            "blessings of the Goddess go with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4D")

    ChrTalk(
        0xFE,
        (
            "Good day, everyone. Welcome\x01",
            "to the Crossbell Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FHi there! My name's KeA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha... Brimming with energy, I see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_C45")

    ChrTalk(
        0x101,
        (
            "#0000FSorry, but is Sister Marble in today?\x02\x03",
            "We were wanting to ask her something\x01",
            "about this girl, if possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, I see. So that's what brought you here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sister Marble is currently preparing for her\x01",
            "lesson in the Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, of course. Thanks for the help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B6E")

    ChrTalk(
        0x102,
        "#0104FThank goodness she's here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BB8")

    ChrTalk(
        0x103,
        "#0200FIt sounds like she is quite devoted to her work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BF9")

    ChrTalk(
        0x104,
        (
            "#0300FGood thing we didn't catch her on\x01",
            "a day off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF9")


    ChrTalk(
        0x101,
        "#0000FAgreed. Want to head inside and find her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FLet's gooo!\x02",
    )

    CloseMessageWindow()

    label("loc_C45")

    SetScenarioFlags(0x0, 0)
    Jump("loc_CFF")

    label("loc_C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(
        0xFE,
        (
            "Sister Marble is currently occupied with her\x01",
            "lesson in the Sunday School classroom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFF")

    label("loc_CB4")


    ChrTalk(
        0xFE,
        (
            "Haha. It always fills my heart with joy\x01",
            "to see such a lively child...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFF")

    Jump("loc_142D")

    label("loc_D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBE")

    ChrTalk(
        0xFE,
        (
            "During the Anniversary Festival, Mass\x01",
            "will be held in the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is the final day of the festival...\x01",
            "It's time to mentally prepare myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E2F")

    label("loc_DBE")


    ChrTalk(
        0xFE,
        (
            "Today is the last day of the festival...\x01",
            "I'm going to have to focus if I want to\x01",
            "stay on top of guard duty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E2F")

    Jump("loc_142D")

    label("loc_E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_EEC")

    ChrTalk(
        0xFE,
        (
            "Our cathedral will be busy for the duration\x01",
            "of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me, security gets hard to maintain when\x01",
            "there's a lot of people crawling around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FAD")

    ChrTalk(
        0xFE,
        (
            "During the Anniversary Festival, Mass\x01",
            "will be held in the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From the looks of things, tourists have\x01",
            "started to take an interest in the beauty\x01",
            "of the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_109D")

    ChrTalk(
        0xFE,
        (
            "During the Anniversary Festival, Mass\x01",
            "will be held in the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you wish to attend, please make your\x01",
            "way inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, we're handing out candy to the\x01",
            "children, but feel free to have some if\x01",
            "you'd like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1141")

    ChrTalk(
        0xFE,
        (
            "Another accident-free day. Thank you,\x01",
            "Aidios, for blessing us with luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How lovely it would be if every day\x01",
            "was as uneventful as this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_133F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(
        0xFE,
        (
            "Sunday School is in session\x01",
            "in the cathedral's classroom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Currently, it falls on my shoulders to keep\x01",
            "anyone suspicious from interfering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're...with the police, correct? Please,\x01",
            "feel free to enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_133A")

    label("loc_1234")


    ChrTalk(
        0xFE,
        (
            "Given that this institution watches over\x01",
            "the well-being of Crossbell's children, I\x01",
            "take guard duty very seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially now, with so many incidents occurring\x01",
            "throughout Crossbell. Just take those monster\x01",
            "attacks from the other day for example...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133A")

    Jump("loc_142D")

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_142D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FC")

    ChrTalk(
        0xFE,
        (
            "Archbishop Eralda, the head of our parish,\x01",
            "shares the teachings of Aidios with all who\x01",
            "desire to hear them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, remain quiet while on the premises.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_142D")

    label("loc_13FC")


    ChrTalk(
        0xFE,
        "Please, remain quiet while on the premises.\x02",
    )

    CloseMessageWindow()

    label("loc_142D")

    TalkEnd(0xFE)
    Return()

    # Function_5_634 end

    def Function_6_1431(): pass

    label("Function_6_1431")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_161B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1577")

    ChrTalk(
        0xFE,
        (
            "It's been almost half a year since I\x01",
            "started my life as a sister here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the past months, I've met many\x01",
            "citizens and children, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...compared to Sister Marble, I can't\x01",
            "help but feel like a mere amateur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that someday I will become\x01",
            "a worthy sister, just like her...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1616")

    label("loc_1577")


    ChrTalk(
        0xFE,
        (
            "It's been almost half a year since I\x01",
            "started my life as a sister here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that someday I will become a\x01",
            "worthy sister, just like Sister Marble...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1616")

    Jump("loc_2BB0")

    label("loc_161B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1712")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CB")

    ChrTalk(
        0xFE,
        (
            "That girl from the CGF came to pray\x01",
            "again today. She's been doing that\x01",
            "ever since she was a private.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Noel truly is a polite and kind soul.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_170D")

    label("loc_16CB")


    ChrTalk(
        0xFE,
        (
            "She's been stopping by to pray ever\x01",
            "since she was a private.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_170D")

    Jump("loc_2BB0")

    label("loc_1712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_178A")

    ChrTalk(
        0xFE,
        (
            "Tamil and Hamil come here to play\x01",
            "quite often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The sad thing is...I still can't tell who's who.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_178A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F3")

    ChrTalk(
        0xFE,
        (
            "Children from East Street should be\x01",
            "stopping by the cathedral today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, the children of today are\x01",
            "wise beyond their years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, Couta always knows\x01",
            "exactly what's on sale in all of the\x01",
            "city's stores. It's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since he told me about all the latest deals,\x01",
            "I'll probably go do some shopping later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_199F")

    label("loc_18F3")


    ChrTalk(
        0xFE,
        (
            "Children from East Street should be\x01",
            "stopping by the cathedral today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The children of today are wise beyond\x01",
            "their years. Fortunately, that keeps me\x01",
            "sharp as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_199F")

    Jump("loc_2BB0")

    label("loc_19A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D0C")
    TurnDirection(0xFE, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7F")

    ChrTalk(
        0xFE,
        (
            "By the way...does this fine young\x01",
            "lady attend our Sunday School?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111FS-cool? Is that why you brought\x01",
            "me here, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FUm... It's sort of hard to explain.\x01",
            "She's got her own special set of\x01",
            "circumstances, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, no... Please allow me to apologize\x01",
            "for asking such a personal question.\x01",
            "That was insensitive of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, we would love to have her in the\x01",
            "class if she's ever able to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm positive that the other children would\x01",
            "be overjoyed to make a new friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FSure, if I feel like it!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1C15")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1C5C")

    label("loc_1C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1C3B")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1C5C")

    label("loc_1C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1C5C")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1C5C")

    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D07")

    label("loc_1C7F")


    ChrTalk(
        0xFE,
        (
            "Excuse me, KeA. Please feel free to join\x01",
            "Sunday School whenever you feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'll make sure to give you a warm welcome!\x02",
    )

    CloseMessageWindow()

    label("loc_1D07")

    Jump("loc_2BB0")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E68")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, my... Aren't you a cutie pie?\x01",
            "What's your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FIt's KeA! K-e-A!\x02\x03",
            "#1109FHmmm... Why are you wearing\x01",
            "those funny clothes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "F-Funny? This is normal attire\x01",
            "for us sisters, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FSis-ter? Like siblings?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Does she really not know anything\x01",
            "about the Septian Church...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FC3")

    label("loc_1E68")


    ChrTalk(
        0xFE,
        "Funny? Is that really true...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be... Could my outfit be the\x01",
            "reason the children can never take\x01",
            "me seriously?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1F26")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1F6D")

    label("loc_1F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1F4C")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_1F6D")

    label("loc_1F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1F6D")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1F6D")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006FI...wouldn't worry too much about\x01",
            "the fashion advice of a girl her age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC3")

    Jump("loc_2BB0")

    label("loc_1FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2095")

    ChrTalk(
        0xFE,
        (
            "I overheard someone mentioning\x01",
            "a young boy getting lost in the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...and you were going around the\x01",
            "city, asking if people had seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How admirable of you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20FA")

    label("loc_2095")


    ChrTalk(
        0xFE,
        (
            "You performed a meritorious deed yesterday.\x01",
            "To think you found a lost child in this vast state.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20FA")

    Jump("loc_2BB0")

    label("loc_20FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225B")

    ChrTalk(
        0xFE,
        (
            "I spoke to Sister Marble about how\x01",
            "to deal with the children's teasing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but she just told me that it's a sign\x01",
            "of affection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What did she mean by that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How in the world does messing with\x01",
            "my skirt mean they like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I just don't follow. Perhaps it's\x01",
            "because I'm still new to the job...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_232F")

    label("loc_225B")


    ChrTalk(
        0xFE,
        (
            "Children often attack me, flip up\x01",
            "my skirt, and things of that nature...\x01",
            "But does that mean they like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll finally understand it after\x01",
            "I've been a part of the church as\x01",
            "long as Sister Marble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232F")

    Jump("loc_2BB0")

    label("loc_2334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_256E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D8")

    ChrTalk(
        0xFE,
        (
            "For some reason, I get the feeling that\x01",
            "the children like making fun of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In today's Mass, for example, one of the\x01",
            "boys suddenly kicked my rear end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must admit that chasing after him was\x01",
            "quite fun. We even had a good laugh\x01",
            "once it was all said and done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I want to adopt a smarter, more mature\x01",
            "attitude. One that's appropriate for a sister\x01",
            "of the Septian Church.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2569")

    label("loc_24D8")


    ChrTalk(
        0xFE,
        (
            "For some reason, I get the feeling that\x01",
            "the children like making fun of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Maybe I should ask Sister Marble\x01",
            "for some advice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2569")

    Jump("loc_2BB0")

    label("loc_256E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F9")

    ChrTalk(
        0xFE,
        (
            "It was bustling around here yesterday.\x01",
            "We had an unprecedented amount of\x01",
            "visitors come with their children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regrettably, we had no way of knowing this.\x01",
            "We hadn't baked enough cookies to go around,\x01",
            "so some of them went home in tears...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My heart nearly broke in two when I saw\x01",
            "that, so I decided to stay up all night,\x01",
            "baking sheet after sheet of cookies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_275C")

    label("loc_26F9")


    ChrTalk(
        0xFE,
        (
            "There weren't enough cookies yesterday,\x01",
            "but I'll make sure we'll have more than\x01",
            "enough today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275C")

    Jump("loc_2BB0")

    label("loc_2761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27F3")

    ChrTalk(
        0xFE,
        (
            "Sunday School is not scheduled for today.\x01",
            "Instead, we're holding Mass for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We would love it if you could attend.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BB0")

    label("loc_27F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E9")

    ChrTalk(
        0xFE,
        (
            "I consider myself a capable cook, so\x01",
            "I treat the children to lunch when they\x01",
            "make it to Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I fear more and more children\x01",
            "are starting to become picky eaters...\x01",
            "Well, I'll show them what I'm made of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll casually mix in their least favorite food\x01",
            "with their favorites. That way, their taste\x01",
            "buds will slowly get used to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And when I finally reveal what they stuffed\x01",
            "their faces with... Oh, now THAT will be\x01",
            "something to behold. ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A3F")

    label("loc_29E9")


    ChrTalk(
        0xFE,
        (
            "Heehee. I'm already looking forward to\x01",
            "getting rid of their pesky eating habits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3F")

    Jump("loc_2BB0")

    label("loc_2A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1A")

    ChrTalk(
        0xFE,
        (
            "Oh, hello. Have you come to visit\x01",
            "the cathedral?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or perhaps you're here to pay your\x01",
            "respects to someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you follow the road off to the side,\x01",
            "you'll reach the cemetery.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BB0")

    label("loc_2B1A")


    ChrTalk(
        0xFE,
        (
            "If you're wanting to reach the cemetery,\x01",
            "please just follow that side road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The souls resting there will undoubtedly\x01",
            "appreciate your visit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1431 end

    def Function_7_2BB4(): pass

    label("Function_7_2BB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2C0E")

    ChrTalk(
        0xA,
        (
            "Whoa, it's already this late? Mom'll\x01",
            "be mad if we don't hurry home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C1C")
    Jump("loc_2EC8")

    label("loc_2C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CBE")

    ChrTalk(
        0xA,
        (
            "Mom lets us play here on the days\x01",
            "we're off from Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Plus, it's kind of a waste to have a\x01",
            "playground like this and not use it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CCC")
    Jump("loc_2EC8")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE7")
    Call(0, 10)
    Jump("loc_2DBA")

    label("loc_2CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2D68")
    TurnDirection(0xA, 0x153, 0)

    ChrTalk(
        0xA,
        (
            "Aw, you're going home already?\x01",
            "We'll have to play next time, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1100FOkay! Sounds good to me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DBA")

    label("loc_2D68")


    ChrTalk(
        0xA,
        (
            "(Are you seriously getting this excited\x01",
            "because she's kinda cute, Hamil...?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBA")

    Jump("loc_2EC8")

    label("loc_2DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E10")

    ChrTalk(
        0xA,
        "Apparently, this lady's a bracer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Pffft! I don't buy it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E1E")
    Jump("loc_2EC8")

    label("loc_2E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E2C")
    Jump("loc_2EC8")

    label("loc_2E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E3A")
    Jump("loc_2EC8")

    label("loc_2E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E48")
    Jump("loc_2EC8")

    label("loc_2E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2E56")
    Jump("loc_2EC8")

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2EC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E71")
    Call(0, 9)
    Jump("loc_2EC8")

    label("loc_2E71")


    ChrTalk(
        0xA,
        (
            "Hamil and I are supposed to be\x01",
            "identical twins, but his reflexes\x01",
            "are sooo slow...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC8")

    TalkEnd(0xFE)
    Return()

    # Function_7_2BB4 end

    def Function_8_2ECC(): pass

    label("Function_8_2ECC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F32")

    ChrTalk(
        0xB,
        (
            "Having a curfew really sucks, but since\x01",
            "I'm starving, we might as well go back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327C")

    label("loc_2F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2F40")
    Jump("loc_327C")

    label("loc_2F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FC8")

    ChrTalk(
        0xB,
        "Hey, Tamil, what's the plan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All this running around is making me tired,\x01",
            "so let's go chat with that one sister!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327C")

    label("loc_2FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2FD6")
    Jump("loc_327C")

    label("loc_2FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF1")
    Call(0, 10)
    Jump("loc_312F")

    label("loc_2FF1")

    TurnDirection(0xB, 0x153, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_30CD")

    ChrTalk(
        0xB,
        (
            "Oh, you're leaving... Would you like to read\x01",
            "a book with me next time you're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1109FHeehee, sure! Reading is one of my favorite\x01",
            "things in the whooole wide world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(S-So...cute...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_312F")

    label("loc_30CD")


    ChrTalk(
        0xB,
        " (*sigh* She's an angel...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1105FHuh? You say something...?\x02",
    )

    CloseMessageWindow()

    label("loc_312F")

    Jump("loc_327C")

    label("loc_3134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_31CE")

    ChrTalk(
        0xB,
        (
            "Haaahhh... I think I'm getting\x01",
            "tired of playing, Tamil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If all you're going to do is mess with\x01",
            "that girl, we should just go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327C")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_31DC")
    Jump("loc_327C")

    label("loc_31DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_31EA")
    Jump("loc_327C")

    label("loc_31EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31F8")
    Jump("loc_327C")

    label("loc_31F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3206")
    Jump("loc_327C")

    label("loc_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3214")
    Jump("loc_327C")

    label("loc_3214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_327C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322F")
    Call(0, 9)
    Jump("loc_327C")

    label("loc_322F")


    ChrTalk(
        0xB,
        (
            "Haaaahhh...haaaahhh... How the heck...\x01",
            "does he have...this much energy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_327C")

    TalkEnd(0xFE)
    Return()

    # Function_8_2ECC end

    def Function_9_3280(): pass

    label("Function_9_3280")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xA,
        "All right, Hamil! What's next?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "J-Just...wait a second, Tamil.\x01",
            "I need a break before we do\x01",
            "anything else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huh? You're ALREADY tired?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_9_3280 end

    def Function_10_3337(): pass

    label("Function_10_3337")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)

    ChrTalk(
        0xA,
        "What's up next, Hamil? Tag?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Well, I kinda wanted to go home...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105FWhoa! You two have the same face!\x01",
            "That's soooo cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x153, 400)
    TurnDirection(0xB, 0x153, 400)
    Sleep(400)

    ChrTalk(
        0xA,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "(W-Wow, she's cute...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FHow the heck does that even happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "U-Um...'cause we're twins?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Th-That's right. Pretty crazy, huh?\x01",
            "They say we're 'identical twins.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FTa-wins...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F(Kids really are able to become\x01",
            "friends in a heartbeat.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3561")

    ChrTalk(
        0x102,
        "#0100F(It's hard to deny her charm.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_365F")

    label("loc_3561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_35AA")

    ChrTalk(
        0x103,
        (
            "#0203F(Being sociable is one of KeA's innate\x01",
            "traits.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365F")

    label("loc_35AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_365F")

    ChrTalk(
        0x104,
        (
            "#0300F(Watch it, kids. If you stare too much\x01",
            "at our precious girl, you'll find yourself\x01",
            "experiencing the wrath of Lloyd.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Why choose me of all people...?)\x02",
    )

    CloseMessageWindow()

    label("loc_365F")

    SetScenarioFlags(0xAE, 0)
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xB, 0xA, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_3337 end

    def Function_11_3679(): pass

    label("Function_11_3679")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_380E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3799")

    ChrTalk(
        0xC,
        "#0802FListen up, kiddos! C'mon, single file line!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#0801FThey aren't listening. At. All.\x02\x03",
            "#0809FWell, if that's the case... If you can't beat\x01",
            "them, join them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0109F(Oh, Estelle...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0309F(Someone's havin' fun.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_380E")

    label("loc_3799")


    ChrTalk(
        0xC,
        (
            "#0809FIf you don't cut it out, I'll unleash my\x01",
            "most powerful move! Tickle barrage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hahahaha!\x02",
    )

    CloseMessageWindow()

    label("loc_380E")

    TalkEnd(0xFE)
    Return()

    # Function_11_3679 end

    def Function_12_3812(): pass

    label("Function_12_3812")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3C4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4F")

    ChrTalk(
        0x101,
        (
            "#0002FHey there, Joshua. Come here\x01",
            "to wind down a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#0902FWell, we came to deliver something to\x01",
            "the archbishop, but...\x02\x03",
            "As you can see, the children awakened\x01",
            "Estelle's inner kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FShe looks really happy, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FThey're clearly very fond of Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#0904FAgreed. She's had that special\x01",
            "connection with kids for as long\x01",
            "as I can remember.\x02\x03",
            "#0900FHonestly, you could probably put\x01",
            "that under her long list of talents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    ChrTalk(
        0xD,
        (
            "#0903FThank you so much for yesterday.\x02\x03",
            "Both Estelle and I felt like we were\x01",
            "carrying the weight of the world on\x01",
            "our shoulders for a while there.\x02\x03",
            "#0902FSo...thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FI-It was nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHey, you can thank us by makin' sure\x01",
            "to catch that devilish little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#0909FHaha. We'll do our best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 0)
    Jump("loc_3C4E")

    label("loc_3B4F")


    ChrTalk(
        0xD,
        (
            "#0904FThe festival is finally coming to a close...\x02\x03",
            "#0900FFortunately, today's not as crazy as yesterday,\x01",
            "so let's give it our all, guys.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4B")

    ChrTalk(
        0x101,
        (
            "#0002FY-Yeah. Definitely.\x02\x03",
            "#0003F(This probably isn't the best time\x01",
            "to bring up the auction.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4B")

    SetScenarioFlags(0x0, 4)

    label("loc_3C4E")

    TalkEnd(0xFE)
    Return()

    # Function_12_3812 end

    def Function_13_3C52(): pass

    label("Function_13_3C52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D47")

    ChrTalk(
        0xFE,
        (
            "We came here to deliver the medicinal\x01",
            "herbs requested by the archbishop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were done in no time thanks to\x01",
            "Aeolia, who knew exactly what we\x01",
            "were looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Her doctor's license isn't just for show,\x01",
            "that much I know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D47")

    TalkEnd(0xFE)
    Return()

    # Function_13_3C52 end

    def Function_14_3D4B(): pass

    label("Function_14_3D4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DB6")

    ChrTalk(
        0xFE,
        "Herbs...berries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that's it! Shall we deliver\x01",
            "everything to the archbishop?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB6")

    TalkEnd(0xFE)
    Return()

    # Function_14_3D4B end

    def Function_15_3DBA(): pass

    label("Function_15_3DBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E79")

    ChrTalk(
        0xFE,
        (
            "The Crossbell Cathedral truly is an extraordinary\x01",
            "feat of architecture, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's easily twice the size of the chapel\x01",
            "I've been attending thus far.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F2B")

    label("loc_3E79")


    ChrTalk(
        0xFE,
        (
            "The Crossbell Cathedral truly is an extraordinary\x01",
            "feat of architecture, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would even say it's comparable to\x01",
            "the High Seat in the Holy City of Arteria.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2B")

    TalkEnd(0xFE)
    Return()

    # Function_15_3DBA end

    def Function_16_3F2F(): pass

    label("Function_16_3F2F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(13460, 3600, 9960, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, 600, 0, -6100, 0)
    SetChrPos(0x153, 0, 0, -4500, 0)
    SetChrPos(0xEF, -600, 0, -6100, 0)
    FadeToBright(1000, 0)
    OP_68(13460, 10600, 9960, 10000)
    PlaceName2(100, 40, "c_plac33", 0x0, 4000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_11(0xA0, 0xDC, 0xDC, 0x3C, 0x64, 0x0)
    OP_68(0, 900, -4500, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17900, 0)
    OP_0D()

    ChrTalk(
        0x153,
        (
            "#3600452V#1105F#5PWooooowie...\x02\x03",
            "#3600453V#1110FThis building is the biggest building I've\x01",
            "ever seen! Is this the church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600454V#0004F#6PSure is. This is the Crossbell Cathedral, KeA.\x02\x03",
            "#3600455V#0001FI'm sure you've probably gone somewhere\x01",
            "similar to pray with your family before, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0xB4, 0x1F4)

    ChrTalk(
        0x153,
        "#3600456V#1100F#11PHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4233")

    ChrTalk(
        0x102,
        (
            "#3600457V#0106F#5PI don't think your average town's chapel\x01",
            "is quite as large as this one...\x02\x03",
            "#3600458V#0100FThis might not be the best spot to help\x01",
            "her remember her past.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A2")

    label("loc_4233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_42F1")

    ChrTalk(
        0x103,
        (
            "#3600459V#0206F#5PChapels in the average town or city are\x01",
            "considerably smaller.\x02\x03",
            "#3600460V#0200FSo this place might not be all that helpful\x01",
            "in KeA regaining her memories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A2")

    label("loc_42F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_43A2")

    ChrTalk(
        0x104,
        (
            "#3600461V#0306F#5PI dunno about this, Lloyd. Ain't most\x01",
            "chapels tiny compared to this place?\x02\x03",
            "#3600462V#0300FNot sure if this'll be the trigger we're\x01",
            "looking for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A2")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 3)), scpexpr(EXPR_END)), "loc_46A2")

    ChrTalk(
        0x101,
        (
            "#3600472V#0006F#12PThat's a good point.\x02\x03",
            "#3600464V#0000FFor now, let's just meet up with Sister Marble.\x02\x03",
            "#3600465VShe might even be able to introduce us to\x01",
            "a specialist within the church.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4521")

    ChrTalk(
        0x102,
        (
            "#3600466V#0104F#5PActually, I wouldn't be surprised if she did,\x01",
            "knowing her.\x02\x03",
            "#3600467V#0102FShe should still be in the Sunday School\x01",
            "classroom. Shall we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469A")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_45DB")

    ChrTalk(
        0x103,
        (
            "#3600468V#0202F#5PSister Marble is that Sunday School\x01",
            "teacher you mentioned before, right?\x02\x03",
            "#3600486VThat means she might still be in the\x01",
            "classroom. Let us go, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469A")

    label("loc_45DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_469A")

    ChrTalk(
        0x104,
        (
            "#3600470V#0302F#5PSister Marble's the one you and Mademois-Elie\x01",
            "have brought up a couple times now, right?\x02\x03",
            "#3600489VLet's give the Sunday School classroom a shot,\x01",
            "then. C'mon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469A")

    OP_57(0x0)
    OP_5A()
    Jump("loc_4BBD")

    label("loc_46A2")


    ChrTalk(
        0x101,
        (
            "#3600463V#0006F#12PThat's a good point.\x02\x03",
            "#3600473V#0000FBut first, I'd like to consult with someone\x01",
            "I know here.\x02\x03",
            "#3600474VIt's one of the Sunday School instructors\x01",
            "who used to look after me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4A4E")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#3600475V#0105F#5POh...? Are you referring to Sister Marble,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600476V#0005F#12PI am, but how did you...?\x02\x03",
            "#3600477V#0004FOh, duh. You went to the same Sunday\x01",
            "School, right?\x02\x03",
            "#3600478V#0000FWe must've had class on different days.\x01",
            "That'd explain why we never met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600479V#0102F#5PI suppose it would. After I finished\x01",
            "Sunday School, I left to study abroad.\x02\x03",
            "#3600480V#0106FHmm. I can't help but wonder if things would\x01",
            "move quicker if we had met as kids...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600481V#0005F#12PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600482V#0112F#5PN-Never mind!\x02\x03",
            "#3600483V#0104FA-Anyway, let's see if Sister Marble\x01",
            "is somewhere around here.\x02\x03",
            "#3600484V#0100FShe's probably still teaching Sunday\x01",
            "School right about now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BBA")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4B1E")

    ChrTalk(
        0x103,
        (
            "#3600485V#0202F#5PI see. Having a connection to someone\x01",
            "in the church may prove beneficial.\x02\x03",
            "#3600469VShould we try visiting the classroom?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600490V#0000F#12PYeah, it's right inside.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BBA")

    label("loc_4B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4BBA")

    ChrTalk(
        0x104,
        (
            "#3600488V#0300F#5PAll righty, then.\x02\x03",
            "#3600471VLet's give the Sunday School\x01",
            "classroom a shot, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600487V#0000F#12PYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    label("loc_4BBA")

    OP_57(0x0)
    OP_5A()

    label("loc_4BBD")

    SetChrPos(0x0, 0, 0, -4500, 0)
    SetScenarioFlags(0xA8, 1)
    OP_29(0x48, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_16_3F2F end

    def Function_17_4BDA(): pass

    label("Function_17_4BDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_68(-200, 2950, 35510, 0)
    MoveCamera(325, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24530, 0)
    SetChrPos(0x101, -500, 2000, 37440, 180)
    SetChrPos(0x153, 870, 2000, 38370, 180)
    SetChrPos(0xEF, -370, 2000, 39460, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    OP_79(0x0)
    OP_68(-200, 2950, 31510, 4500)

    def lambda_4CB0():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CB0)

    def lambda_4CC5():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4CC5)

    def lambda_4CDA():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4CDA)

    def lambda_4CEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CEF)
    Sleep(300)

    def lambda_4D03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_4D03)
    Sleep(300)

    def lambda_4D17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_4D17)
    Sleep(1500)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)

    def lambda_4D4A():
        TurnDirection(0xFE, 0xEF, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D4A)
    WaitChrThread(0x153, 1)

    def lambda_4D5B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4D5B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 2)
    WaitChrThread(0x153, 2)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3600640V#0000F#6PNext up, St. Ursula Hospital.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(100)
    TurnDirection(0xEF, 0x153, 500)

    ChrTalk(
        0x101,
        (
            "#3600641V#0001F#5PThat's not exactly next door, is it?\x01",
            "KeA, are you getting tired?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600642V#1110F#12PI'm A-OK!\x02\x03",
            "#3600643V#1109FWalking around with everyone is the\x01",
            "best! I love it, hehehe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600644V#0012F#5PHaha, I wish I could always be as\x01",
            "energetic as you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4F65")

    ChrTalk(
        0x102,
        (
            "#3600645V#0109F#5PShall we head to the south exit, then?\x02\x03",
            "#3600646V#0102FIf we take the bus, we should\x01",
            "get there in no time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5095")

    label("loc_4F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5008")

    ChrTalk(
        0x103,
        (
            "#3600647V#0202F#5PShould we proceed to the city's\x01",
            "south exit, Lloyd?\x02\x03",
            "#3600648V#0204FThe bus will be the most time-efficient\x01",
            "option, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5095")

    label("loc_5008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5095")

    ChrTalk(
        0x104,
        (
            "#3600649V#0304F#5PHaha, well, then...to the south exit?\x02\x03",
            "#3600650V#0302FIf we catch the bus, we'll be there\x01",
            "before we know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5095")

    OP_93(0x153, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x153,
        "#3600651V#1110F#12PYeah! Let's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 2000, 32200, 180)
    SetScenarioFlags(0xA8, 3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_17_4BDA end

    def Function_18_50EB(): pass

    label("Function_18_50EB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "- Crossbell Cathedral Parsonage -\x01",
            "   Those who have come to pray\x01",
            "   are welcome in the cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_50EB end

    SaveToFile()

Try(main)
