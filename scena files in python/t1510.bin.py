from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1510.bin",                # FileName
        "t1510",                    # MapName
        "t1510",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1510",                  # 0
        "Superintendent Kirsch",  # 1
        "Medical Intern Flora",   # 2
        "Medical Intern Lytton",  # 3
        "Cecile",                 # 4
        "Bracer Lynn",            # 5
        "Bracer Aeolia",          # 6
        "Tourist Thuiller",       # 7
        "Tourist Pastel",         # 8
    ))

    AddCharChip((
        "chr/ch24300.itc",                   # 00
        "chr/ch29502.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch32002.itc",                   # 03
        "chr/ch32102.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch23900.itc",                   # 06
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

    DeclNpc(-4809,   0,       11600,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-12069,  150,     14399,   180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-12069,  150,     11050,   0,    469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-12319,  150,     3630,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4690,    3750,    15430,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 17,  9.0,                   11.0,                  3.25,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -5.5,                  -0.6500000357627869,   1.0])

    DeclActor(-6100,   0,       10440,   1000,    -4810,   1500,    11600,   0x007E, 0,  3,  0x0000)
    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  11, 0x0000)
    DeclActor(5830,    0,       11730,   1200,    5830,    1500,    11730,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_42C",          # 02, 2
        "Function_3_4D1",          # 03, 3
        "Function_4_4D5",          # 04, 4
        "Function_5_1BCD",         # 05, 5
        "Function_6_1D21",         # 06, 6
        "Function_7_34E2",         # 07, 7
        "Function_8_3647",         # 08, 8
        "Function_9_3795",         # 09, 9
        "Function_10_3B48",        # 0A, 10
        "Function_11_4271",        # 0B, 11
        "Function_12_42DA",        # 0C, 12
        "Function_13_4516",        # 0D, 13
        "Function_14_4641",        # 0E, 14
        "Function_15_5D7B",        # 0F, 15
        "Function_16_6E0D",        # 10, 16
        "Function_17_74A0",        # 11, 17
        "Function_18_7554",        # 12, 18
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3CA")
    Jump("loc_3D8")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D8")
    ClearChrFlags(0xA, 0x80)

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F0")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)
    Jump("loc_413")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_413")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 15)

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42B")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_42B")

    Return()

    # Function_1_3BC end

    def Function_2_42C(): pass

    label("Function_2_42C")

    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_4D0")

    Return()

    # Function_2_42C end

    def Function_3_4D1(): pass

    label("Function_3_4D1")

    Call(0, 4)
    Return()

    # Function_3_4D1 end

    def Function_4_4D5(): pass

    label("Function_4_4D5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_542")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_542")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_572")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_561")
    OP_AF(0x5D)
    Jump("loc_563")

    label("loc_561")

    OP_AF(0x5C)

    label("loc_563")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC4")

    label("loc_572")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_592")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BC4")

    label("loc_592")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6")
    Jump("loc_1BC4")

    label("loc_5A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_630")

    ChrTalk(
        0x8,
        "Welcome, y'all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I bet the hospital is preparing for the\x01",
            "day right about now, same as us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_83E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(
        0x8,
        (
            "It's almost time for the nurses\x01",
            "to come get a spot of dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our meals have been quite the hit\x01",
            "with the patients as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Gable of the diet irritated me a while ago\x01",
            "when he said, 'Your food lacks elegance!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But since then, I've worked on improving the\x01",
            "menu, and apparently it has been a welcome\x01",
            "change. Maybe he wasn't wrong, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_839")

    label("loc_7B8")


    ChrTalk(
        0x8,
        (
            "Our meals have been quite the hit\x01",
            "with the patients as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe I owe that rude Mr. Gable an\x01",
            "apology, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839")

    Jump("loc_1BC4")

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_912")

    ChrTalk(
        0x8,
        (
            "Word is that those people who were carried\x01",
            "into the hospital this morning were all assaulted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, dear, I hope the hospital doesn't\x01",
            "get caught up in something shady\x01",
            "because of all this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9B6")

    ChrTalk(
        0x8,
        (
            "That lady bracer is always helping\x01",
            "out the hospital with this or that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Maybe I can repay some of the debt\x01",
            "we owe her by cooking up a feast.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_9B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_A4D")

    ChrTalk(
        0x8,
        "Where'd that girl of yours run off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What? You've lost her?! *sigh*\x01",
            "What the heck are you doing, talking\x01",
            "to me? Go find her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF")

    ChrTalk(
        0x8,
        (
            "Oh, I overheard your story, missy.\x01",
            "You're Cecile's niece, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1105FHuh? Really? Am I REALLY, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FN-No! This is a huge misunderstanding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha! Just a bit of teasing! Don't\x01",
            "take everything so seriously, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FI'm confused.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F*sigh* Geez...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BF9")

    ChrTalk(
        0x102,
        (
            "#0102F(I knew he was susceptible to these kinds\x01",
            "of things, but he really is hopeless, isn't he?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA7")

    label("loc_BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C69")

    ChrTalk(
        0x103,
        (
            "#0202F(Lloyd reminds me of the typical comic relief\x01",
            "archetype in these kinds of situations.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA7")

    label("loc_C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_CA7")

    ChrTalk(
        0x104,
        "#0309F(Poor guy. Lloyd will be Lloyd, I guess.)\x02",
    )

    CloseMessageWindow()

    label("loc_CA7")

    SetScenarioFlags(0x0, 0)
    Jump("loc_CFD")

    label("loc_CAF")


    ChrTalk(
        0x8,
        "Hahaha. You'll have to forgive me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Please, make yourselves at home.\x02",
    )

    CloseMessageWindow()

    label("loc_CFD")

    Jump("loc_1BC4")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(
        0x8,
        "Nice to see you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I appreciate you making the trip out here\x01",
            "during the craziness of the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5B")

    ChrTalk(
        0x8,
        (
            "All the ingredients used for our meals\x01",
            "are bought from Mr. Hayworth, a local\x01",
            "trader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's a lifesaver. Fresh and healthy\x01",
            "ingredients like these are hard to get\x01",
            "at a fair price.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EAC")

    label("loc_E5B")


    ChrTalk(
        0x8,
        (
            "The ingredients we use in our meals are\x01",
            "all purchased through Mr. Hayworth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAC")

    Jump("loc_1BC4")

    label("loc_EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(
        0x8,
        (
            "Have you met my niece, Marone? She's\x01",
            "a lifesaver, cleaning the dormitories as\x01",
            "thoroughly as she does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Once I heard about how much free time\x01",
            "she had, I offered her a job here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keeping things neat and tidy is one of\x01",
            "her finest qualities, so making her one\x01",
            "of my cleaners was a no-brainer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")

    ChrTalk(
        0x8,
        (
            "Having to stay in bed during the whole Anniversary\x01",
            "Festival must be a shame, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want to go above and beyond with my cooking\x01",
            "the next few days, just so the patients\x01",
            "don't feel like they're missing too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But I still have to make sure I don't go too\x01",
            "crazy. If you can't strike a good balance,\x01",
            "the whole thing will come tumbling down...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1224")

    label("loc_1178")


    ChrTalk(
        0x8,
        (
            "During the Anniversary Festival,\x01",
            "I want to push the quality of my\x01",
            "meals to the limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you try the tofu burger I put\x01",
            "into yesterday's menu? Tasty\x01",
            "AND healthy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1224")

    Jump("loc_1BC4")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_139B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC")

    ChrTalk(
        0x8,
        (
            "The interns are unbelievably passionate.\x01",
            "They even study while eating, if you can\x01",
            "believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Study while you're young and you'll live\x01",
            "a long, happy life. That's what I say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1396")

    label("loc_12FC")


    ChrTalk(
        0x8,
        (
            "Maybe I should create a menu full of\x01",
            "food known to stimulate the brain. That'd\x01",
            "probably help the medical interns' studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How about fish eyes?\x02",
    )

    CloseMessageWindow()

    label("loc_1396")

    Jump("loc_1BC4")

    label("loc_139B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_145C")

    ChrTalk(
        0x8,
        (
            "Earlier, some visitors were discussing\x01",
            "Arc en Ciel's new show over lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's called 'Golden Sun, Silver Moon,'\x01",
            "isn't it? My, I'd love to be able to go\x01",
            "see it someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_145C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1478")
    Call(0, 5)
    Jump("loc_16A9")

    label("loc_1478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C1")

    ChrTalk(
        0x8,
        (
            "I make meals for all the patients, too,\x01",
            "but it doesn't always go well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For example, yesterday, Mr. Gable spouted\x01",
            "some nonsense in that private room of his.\x01",
            "'Give me a steak! Medium rare!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So, I accidentally blurted out that he should\x01",
            "go to an actual restaurant if he wants\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A9")

    label("loc_15C1")


    ChrTalk(
        0x8,
        (
            "Yesterday, Mr. Gable spouted some\x01",
            "nonsense in that private room of his.\x01",
            "'Give me a steak! Medium rare!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I always pay attention to the nutritional\x01",
            "value of my meals, so people like him\x01",
            "aren't the easiest to get along with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A9")

    Jump("loc_1BC4")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_17CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CA")
    Call(0, 5)
    Jump("loc_17C5")

    label("loc_16CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")

    ChrTalk(
        0x8,
        (
            "Now that the lunchtime rush is over, things\x01",
            "have gotten quiet in the dormitories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Later, I think I'll go give Marone a hand\x01",
            "with the cleaning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17C5")

    label("loc_1775")


    ChrTalk(
        0x8,
        (
            "Oh, right. If you want to order something,\x01",
            "go ahead and let me know, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C5")

    Jump("loc_1BC4")

    label("loc_17CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1A47")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E6")
    Call(0, 5)
    Jump("loc_1A42")

    label("loc_17E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D6")

    ChrTalk(
        0x8,
        (
            "Are you going back already, Cecile?\x01",
            "You still have some time until your\x01",
            "break is over, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure you're aware it's hard to find\x01",
            "time to rest, even when the hospital\x01",
            "is in the middle of a lull.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1302FYou worry too much, Kirsch. Trust me,\x01",
            "seeing Lloyd wiped away all of my\x01",
            "exhaustion.\x02\x03",
            "#1300FAnd as always, thank you for allowing\x01",
            "us to stay in the dormitories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, what's gotten into you? You're\x01",
            "one of my boarders, so there's no\x01",
            "need to thank me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A42")

    label("loc_19D6")


    ChrTalk(
        0x8,
        (
            "Listen, you all. Don't go pushing\x01",
            "Cecile around too much, all right?\x01",
            "She's a very busy lady, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A42")

    Jump("loc_1BC4")

    label("loc_1A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A63")
    Call(0, 5)
    Jump("loc_1BC4")

    label("loc_1A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B15")

    ChrTalk(
        0x8,
        (
            "Hello, you four. Welcome to St. Ursula's\x01",
            "cafeteria and dormitories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Some of the staff are exhausted from\x01",
            "the night shift, so try not to disturb them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC4")

    label("loc_1B15")


    ChrTalk(
        0x8,
        (
            "Our rooms and cafeteria are open to\x01",
            "visitors, just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're feeling hungry, just let me\x01",
            "know. I'll work my magic and cook\x01",
            "something wonderful for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC4")

    Jump("loc_4E2")

    label("loc_1BC9")

    TalkEnd(0x8)
    Return()

    # Function_4_4D5 end

    def Function_5_1BCD(): pass

    label("Function_5_1BCD")


    ChrTalk(
        0x8,
        (
            "Here at St. Ursula, we put a lot of\x01",
            "consideration into the nutritional\x01",
            "value of our meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One of our specialty meals is our\x01",
            "homemade beef stew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would you like to learn how\x01",
            "to make it for yourself?\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
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
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x5)
    Return()

    # Function_5_1BCD end

    def Function_6_1D21(): pass

    label("Function_6_1D21")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DB5")
    Jump("loc_1DFF")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DD5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFF")

    label("loc_1DD5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFF")

    label("loc_1DF5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DFF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC5")

    ChrTalk(
        0xFE,
        "That book...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, thank goodness you found it.\x01",
            "I'm sorry that my negligence caused\x01",
            "so much trouble for you all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F7C")

    label("loc_1EC5")


    ChrTalk(
        0xFE,
        (
            "I bet it was difficult to find that one book\x01",
            "amongst all the giant bookshelves, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm impressed that you found it so quickly.\x01",
            "What'd you do, a full-on frontal assault?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2109")

    ChrTalk(
        0xFE,
        (
            "You see, I like to grab medical textbooks\x01",
            "from the research ward's reference room\x01",
            "and study here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But from the looks of it, I must have mixed\x01",
            "up the library book and textbooks when I\x01",
            "was returning them to the reference room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm very sorry about this, but do you mind\x01",
            "searching the reference room for it? I'm\x01",
            "afraid I'm quite busy right now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_2109")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212A")
    Call(0, 16)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_212A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2244")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F8")

    ChrTalk(
        0xFE,
        (
            "Now that that's over with, it's time to\x01",
            "dive back into the books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's still a bit too early for lunch...\x01",
            "Well, I'm sure time will fly by if I\x01",
            "read one of my textbooks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_223F")

    label("loc_21F8")


    ChrTalk(
        0xFE,
        (
            "Personally, I think this cafeteria is the\x01",
            "perfect place to study.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223F")

    Jump("loc_34DA")

    label("loc_2244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2308")

    ChrTalk(
        0xFE,
        (
            "Today's lecture was a breeze for me.\x01",
            "Reading my medical textbooks everywhere\x01",
            "I go must finally be paying off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Lytton kept up with the lecture\x01",
            "as well as I did?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_2308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_23C3")

    ChrTalk(
        0xFE,
        (
            "I'm in the middle of studying for our next\x01",
            "exam. Could you please leave me alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The exam is still quite far away, but it's\x01",
            "always best to start preparing early.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_23C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(
        0xFE,
        "*sigh* I knew it. Surgeries really are amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's still so many undiscovered techniques,\x01",
            "which makes the field that much more exciting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_246B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2514")

    ChrTalk(
        0xFE,
        (
            "Huh? A little girl, you say? I don't\x01",
            "believe I saw one pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she made her way into the cafeteria,\x01",
            "I assure you, I would have noticed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_2514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_27A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275B")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FOooh, are you reading a book? Whatever\x01",
            "it is, it looks super complicated, miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FA book about autopsies, huh...?\x02\x03",
            "#0011FW-Wait! You're way too young to be\x01",
            "reading stuff like that, KeA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1106FAw... That stinks.\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_26B7")
    Jump("loc_2701")

    label("loc_26B7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26D7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2701")

    label("loc_26D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26F7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2701")

    label("loc_26F7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2701")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "You...guys...are...irritating...me.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_279B")

    label("loc_275B")


    ChrTalk(
        0xFE,
        (
            "Unbelievable. Can't you see that\x01",
            "I'm trying to study here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279B")

    Jump("loc_34DA")

    label("loc_27A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2815")

    ChrTalk(
        0xFE,
        (
            "Since I'm always up to my nose\x01",
            "in books, I make sure to treasure\x01",
            "our practical training sessions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28BF")

    ChrTalk(
        0xFE,
        (
            "I just remembered, the professors won't\x01",
            "be available tomorrow because of the\x01",
            "faculty meeting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I better go ask questions while\x01",
            "I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_28BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DA")
    Call(0, 8)
    Jump("loc_2981")

    label("loc_28DA")


    ChrTalk(
        0xFE,
        (
            "*munch* *munch* If I followed standard\x01",
            "eating times, I'd never get anything done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This has become my way of life ever\x01",
            "since I was able to observe surgeries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2981")

    Jump("loc_34DA")

    label("loc_2986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A90")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival? Sorry, but\x01",
            "I can't say I'm interested in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite what you may think, I came to\x01",
            "Crossbell for purely academic reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You won't see me crying over a lack of\x01",
            "free time, unlike the other interns.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B21")

    label("loc_2A90")


    ChrTalk(
        0xFE,
        (
            "Besides, it's the 'Crossbell' Anniversary\x01",
            "Festival, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Correct me if I'm wrong, but that has\x01",
            "nothing to do with a Remiferian like me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B21")

    Jump("loc_34DA")

    label("loc_2B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C29")

    ChrTalk(
        0xFE,
        (
            "I've still got some time before our surgery\x01",
            "lecture, so I think I'll grab a bite to eat\x01",
            "while brushing up on the chapter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm often told that doing so is bad\x01",
            "manners, but I can't help but feel that\x01",
            "not multitasking is a waste of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_2C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2E30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA6")

    ChrTalk(
        0xFE,
        (
            "I usually carry around this book about\x01",
            "autopsies... Is that weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was having lunch with Lytton,\x01",
            "he threw a big fit and told me not to\x01",
            "read it while eating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FPersonally, I would lose my appetite if I saw\x01",
            "the book's illustrations, as well. Especially if\x01",
            "I was eating meat or the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Maybe, but it doesn't faze me at all.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E2B")

    label("loc_2DA6")


    ChrTalk(
        0xFE,
        (
            "Is carrying around this book really\x01",
            "that weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was convenient. Now I can\x01",
            "study wherever and whenever I want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2B")

    Jump("loc_34DA")

    label("loc_2E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2EBE")

    ChrTalk(
        0xFE,
        "Oh, is it time already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll stop by the reference room\x01",
            "for a bit of last minute studying before\x01",
            "the lecture.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DA")

    label("loc_2EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_30D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF6")

    ChrTalk(
        0xFE,
        "Lytton is from Remiferia, just like me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not the most gifted student,\x01",
            "so he had to study like a madman\x01",
            "in order to get accepted here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really don't think he's all there in the head...\x01",
            "Even though he was attacked by monsters,\x01",
            "he doesn't seem fazed in the slightest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30CE")

    label("loc_2FF6")


    ChrTalk(
        0xFE,
        (
            "Something tells me Lytton isn't all there in\x01",
            "the head... He was attacked by monsters,\x01",
            "but isn't the slightest bit freaked out about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he sure is lucky. I need to make\x01",
            "sure to thank Aidios for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30CE")

    Jump("loc_34DA")

    label("loc_30D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_32F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3276")

    ChrTalk(
        0xFE,
        (
            "I usually end up losing track of time in the\x01",
            "cafeteria because it's so comfy. As long as\x01",
            "I can make progress studying, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1302FFlora, it's always so refreshing to see\x01",
            "your passion for reading in action.\x02\x03",
            "#1304FHowever, just make sure you're not so\x01",
            "engrossed reading a book that you end\x01",
            "up arriving late to lecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You sound like my mom every once in\x01",
            "a while, Cecile.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32F4")

    label("loc_3276")


    ChrTalk(
        0xFE,
        (
            "But, now that you mention it, I think it's\x01",
            "almost time for a lecture. I suppose I'll\x01",
            "head on to the research ward, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F4")

    Jump("loc_34DA")

    label("loc_32F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34DA")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3487")

    ChrTalk(
        0xFE,
        "Hmm, I see... So that turns into that, and...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh! That makes sense!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Is she studying in the middle of eating?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(I believe so. It looks like a biology\x01",
            "textbook, judging by all the photos\x01",
            "of dissections...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(Ugh. That's nasty.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(Something tells me I would not\x01",
            "want to read something like that\x01",
            "while eating a meal.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34DA")

    label("loc_3487")


    ChrTalk(
        0xFE,
        (
            "There's no time that isn't study time!\x01",
            "Oh, isn't surgery just so fascinating?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1D21 end

    def Function_7_34E2(): pass

    label("Function_7_34E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3576")
    Jump("loc_35C0")

    label("loc_3576")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3596")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C0")

    label("loc_3596")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35B6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C0")

    label("loc_35B6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F7")
    Call(0, 8)
    Jump("loc_363F")

    label("loc_35F7")


    ChrTalk(
        0xFE,
        (
            "*sigh* How is she able to stomach\x01",
            "her food, looking at that stuff?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_34E2 end

    def Function_8_3647(): pass

    label("Function_8_3647")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "Hey, Flora. I got a question about\x01",
            "one of the last lecture points...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...What the heck?! Don't read that\x01",
            "kinda stuff while eating!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Why? It'd be a waste of time to not study a\x01",
            "bit while eating... Mmm, tasty. *munch*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I mean, sure, but looking at autopsy photos\x01",
            "while eating? I think I'm going to be sick.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_3647 end

    def Function_9_3795(): pass

    label("Function_9_3795")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3829")
    Jump("loc_3873")

    label("loc_3829")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3849")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3873")

    label("loc_3849")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3869")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3873")

    label("loc_3869")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3873")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3925")

    ChrTalk(
        0xFE,
        "Were you able to put together a nice present?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aeolia and I were planning to go\x01",
            "visit Shizuku a bit later, anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B40")

    label("loc_3925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3A9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A18")

    ChrTalk(
        0xFE,
        (
            "What'd you say? You're collecting\x01",
            "stuff so Shizuku can make a gift?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'd be more than happy to\x01",
            "help you guys out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But unfortunately, I don't think I have\x01",
            "anything on me that'd be that useful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 4)
    Jump("loc_3A96")

    label("loc_3A18")


    ChrTalk(
        0xFE,
        (
            "Unfortunately, I don't think I have anything\x01",
            "on me that would work as a gift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sorry I couldn't be of any more help.\x02",
    )

    CloseMessageWindow()

    label("loc_3A96")

    Jump("loc_3B40")

    label("loc_3A9B")


    ChrTalk(
        0xFE,
        (
            "'Cause of a big emergency, Aeolia and I\x01",
            "had to hightail it over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought we'd be a little less busy after\x01",
            "the festival, but looks like I was wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B40")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_3795 end

    def Function_10_3B48(): pass

    label("Function_10_3B48")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BDC")
    Jump("loc_3C26")

    label("loc_3BDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BFC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C26")

    label("loc_3BFC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C1C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C26")

    label("loc_3C1C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C26")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D11")

    ChrTalk(
        0xFE,
        (
            "Poor Shizuku has been hospitalized\x01",
            "here for such a long time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I have no choice but to give\x01",
            "her lots of cuddles, for Arios' sake! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Snap out of it, Aeolia.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4269")

    label("loc_3D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_40F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4006")

    ChrTalk(
        0xFE,
        "Oh? Shizuku wants to make a present?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see here... I might have\x01",
            "just the thing...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xFE,
        "Here it is! Would this work?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Aeolia took out a sapphirl crystal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        (
            "How about this? Some Imperial merchant\x01",
            "gave me this as a reward a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This would definitely make Shizuku's day,\x01",
            "don't you think? Make sure she gets it. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FTh-That's WAY too nice!\x02\x03",
            "Besides, Shizuku would probably get\x01",
            "in trouble if she used something this\x01",
            "expensive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FAlso, this would likely go against her\x01",
            "request of collecting simple materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, you think so? But I don't really\x01",
            "have anything else on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I just wanted to be able to help\x01",
            "sweet, sweet Shizuku...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 5)
    Jump("loc_40EE")

    label("loc_4006")


    ChrTalk(
        0xFE,
        (
            "*sigh* I just wanted to be able to help\x01",
            "sweet, sweet Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got it! If the sapphirl crystal is no good,\x01",
            "what about this goldia one...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FWe already established that we can't\x01",
            "take anything like that, Aeolia!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EE")

    Jump("loc_4269")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F0")

    ChrTalk(
        0xFE,
        (
            "The guy who was just carried into the\x01",
            "hospital was attacked by monsters on\x01",
            "the highway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it just me, or are monsters becoming\x01",
            "stronger than usual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I'm just glad he was able\x01",
            "to make it out of that alive.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4269")

    label("loc_41F0")


    ChrTalk(
        0xFE,
        "Actually, I helped out with his surgery.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's times like these that I'm really glad\x01",
            "I have my medical license.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4269")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_3B48 end

    def Function_11_4271(): pass

    label("Function_11_4271")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "3F: Women's Dormitory→\x01\x01",
            "← 2F: Men's Dormitory\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_4271 end

    def Function_12_42DA(): pass

    label("Function_12_42DA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_436E")
    Jump("loc_43B8")

    label("loc_436E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_438E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43B8")

    label("loc_438E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43AE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43B8")

    label("loc_43AE")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43B8")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4469")

    ChrTalk(
        0xE,
        "*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huh. I thought this hospital food was\x01",
            "going to be light and unappetizing,\x01",
            "but boy, was I wrong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_450E")

    label("loc_4469")


    ChrTalk(
        0xE,
        (
            "Hmm... I'm having a hard time coming\x01",
            "up with any complaints about the food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's honestly about a hundred times\x01",
            "better than the junk food I usually eat...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_450E")

    SetChrSubChip(0xE, 0x0)
    TalkEnd(0xE)
    Return()

    # Function_12_42DA end

    def Function_13_4516(): pass

    label("Function_13_4516")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BB")

    ChrTalk(
        0xFE,
        (
            "This building is where all the doctors\x01",
            "and nurses live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Living together with all your coworkers\x01",
            "sounds like a blast, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_463D")

    label("loc_45BB")


    ChrTalk(
        0xFE,
        (
            "This building is where all the doctors\x01",
            "and nurses live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet living with a bunch of strangers\x01",
            "is a fun change of pace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463D")

    TalkEnd(0xFE)
    Return()

    # Function_13_4516 end

    def Function_14_4641(): pass

    label("Function_14_4641")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch05300.itc", 0x23)
    OP_68(-6830, 1000, 10260, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
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
    SetChrPos(0x101, -13400, 200, 6850, 180)
    SetChrPos(0x102, -13700, 200, 3600, 0)
    SetChrPos(0x103, -12800, 200, 3600, 0)
    SetChrPos(0x104, -11900, 200, 3600, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12300, 200, 6850, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    FadeToBright(1000, 0)
    OP_68(-12750, 1000, 5380, 6000)
    OP_0D()
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xB,
        (
            "#1101104VI'm Cecile Neues.\x01",
            "Nice to meet you all.\x02\x03",
            "#1101105VSo, you three are Lloyd's\x01",
            "coworkers, right?\x02",
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
        "#1101106V#0102F#6PY-Yes. My name is Elie MacDowell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101107V#0203F#12PTio Plato. Pleasure to make your\x01",
            "acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101108V#0309F#2PRandy Orlando's the name!\x01",
            "The pleasure's all mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101109V#1302F#5PIt's nice to meet all of you.\x02\x03",
            "#1101110V#1306F*sigh* I'm such a scatterbrain.\x02\x03",
            "#1101111VAnd here I was, thinking that Lloyd\x01",
            "came here to show his girlfriends\x01",
            "around the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1101112V#0011F#1PE-Excuse me, WHAT?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#1101113V#1309F#11PI mean, you've been gone for almost\x01",
            "three years, right?\x02\x03",
            "#1101114VI had hoped that you'd make a girlfriend\x01",
            "or two that you'd introduce me to.\x02\x03",
            "#1101115V#1305FOh! Are you actually dating one of them,\x01",
            "but using this whole coworker thing as\x01",
            "a disguise...?\x02\x03",
            "#1101116V#1308FI-I'm sorry, Lloyd. I shouldn't be making\x01",
            "assumptions like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101117V#0006F#1PC-Cecile, listen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101118V#1309F#11PSo, which one is it?\x02\x03",
            "#1101119VElie? Tio? Oh, my, you aren't dating both\x01",
            "of them at the same time, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101120V#0001F#1PCecile! I'm! Not! Dating! Them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101121V#1305F#11PD-Does that mean you're dating him...?\x02\x03",
            "#1101122V#1306FHmm, well, I've always tried to be an\x01",
            "understanding big sister to you...\x02\x03",
            "#1101123V#1301FDon't worry! You've got my full support!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101124V#0012F#1PNo! I do NOT swing that way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101125V#0109F#6PHe denies it so vehemently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101126V#0202F#12PShe is quite the unique woman,\x01",
            "is she not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101127V#0309F#2POoooh, I love me an airhead...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        (
            "#1101128V#0003F#1PAhem! Back to the topic at hand...\x02\x03",
            "#1101129V#0001FCecile, we're actually here about\x01",
            "the recent monster attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101130V#1303F#11PYes, that's right.\x02\x03",
            "#1101131V#1300FI already received permission from\x01",
            "the head nurse to tell you everything.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0xB,
        (
            "#1101132V#1303F#5P...It happened exactly one week ago.\x02\x03",
            "#1101133VThat night, one of our interns, Lytton,\x01",
            "was assaulted by some monsters.\x02\x03",
            "#1101134V#1301FHowever, something about it was weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101135V#0201F#12PThe CGF report mentions the possibility of it\x01",
            "being a misunderstanding on the injured's part.\x01",
            "Is that what you are referring to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101136V#1306F#5PExactly right. It seems that the CGF\x01",
            "left the investigation unconvinced.\x02\x03",
            "#1101137V#1301FNow, I don't know the specifics...but I\x01",
            "heard Lytton was attacked on the roof.\x02",
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
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1101138V#0005F#1PThe roof?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101139V#0101F#6PHow is that possible...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101140V#1300F#5PWell, you see, the hospital roof is both\x01",
            "a terrace and a garden.\x02\x03",
            "#1101141VThe entrance to the research ward\x01",
            "is up there, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101142V#0301F#2PGot'cha... So to sum it up, it ain't a\x01",
            "place you'd ever expect monsters to\x01",
            "show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101143V#1306F#5PYes. That's the conclusion that the\x01",
            "CGF ended up leaning towards.\x02\x03",
            "#1101144V#1308FBut I can't accept that.\x02\x03",
            "#1101145V#1301FThat's why I would like you guys to\x01",
            "keep investigating the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101146V#0006F#1PI don't know, Cecile...\x02\x03",
            "#1101147V#0008FHonestly, I wouldn't expect that much\x01",
            "from us, if I were you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#1101148V#1302F#11PAlways so modest, Lloyd.\x02\x03",
            "#1101149VI read the Crossbell Times, you know.\x01",
            "The Special Support Section started\x01",
            "off strong, didn't they?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#1101150V#0005F#1POh... Are you talking about the\x01",
            "case downtown?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_5680")

    ChrTalk(
        0x102,
        (
            "#1101151V#0105F#6PI didn't think the recent articles stated\x01",
            "that we were the ones that resolved\x01",
            "the incident...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D4")

    label("loc_5680")


    ChrTalk(
        0x104,
        (
            "#1101152V#0302F#12PAre ya sayin' they actually wrote\x01",
            "somethin' nice about us?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D4")

    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#1101153V#1304F#5PThey might not have flat-out said it,\x01",
            "but the message was clear.\x02\x03",
            "#1101154V#1302FOn top of that, a couple of those boys\x01",
            "wrapped up in the mess were hospitalized\x01",
            "at St. Ursula...\x02\x03",
            "#1101155VI heard a bit about the situation while\x01",
            "their friends came to visit them.\x02\x03",
            "#1101156V#1309FBelieve it or not, they kept mentioning\x01",
            "that they owed you four big-time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1101157V#0000F#1PDid they really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101158V#0102F#6PWhat a coincidence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101159V#0309F#2PC'mon, I'm gonna blush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101160V#0203F#12PI do not remember you playing too\x01",
            "important a role, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#1101161V#1303F#5PLet me think...\x02\x03",
            "#1101162V#1300FAn interview with Lytton is probably a\x01",
            "good place to start your investigation,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101163V#0003F#1PYeah. If you could introduce us,\x01",
            "that'd be great.\x02\x03",
            "#1101164V#0001FAlso, I'd like to investigate the\x01",
            "actual crime scene, if possible.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#1101165V#1302F#11PI don't think that will be a problem.\x01",
            "I'll show you around the hospital.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -12300, 0, 6400, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1101166V#0005F#1PAre you sure you have the time\x01",
            "for that, Cecile?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#1101167V#1300F#11POh, yes. I'm on break, right now.\x01",
            "Don't worry about it, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#1101168V#1309F#5PFirst, we'll head to the second\x01",
            "floor of the hospital.\x02\x03",
            "#1101169VFollow me, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101170V#0102F#6PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101171V#0204F#12PWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1101172V#0309F#2POff we go!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#1101173V#0012F#5P(I'm glad to see everyone's\x01",
            "really hit it off with Cecile.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
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
    SetChrFlags(0xB, 0x80)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    AddParty(0x35, 0xFF, 0xFF)
    SetChrPos(0x0, -10400, 0, 6500, 90)
    SetScenarioFlags(0x62, 0)
    OP_29(0x3F, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_14_4641 end

    def Function_15_5D7B(): pass

    label("Function_15_5D7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch08202.itc", 0x23)
    OP_68(-9140, 1000, 9070, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23610, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_5DFC")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_5E23")

    label("loc_5DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5E12")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_5E23")

    label("loc_5E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5E23")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_5E23")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x23)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrPos(0x153, -13350, 300, 3500, 0)
    SetChrPos(0x101, -12350, 200, 3500, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12350, 200, 6850, 180)
    SetChrPos(0xEF, -13350, 200, 6850, 180)
    FadeToBright(1000, 0)
    OP_68(-12880, 1200, 5390, 5000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#3600760V#1309F#5PI might have been too quick to\x01",
            "draw conclusions.\x02\x03",
            "#3600761V#1302FAfter all, you're 18 and KeA looks\x01",
            "around 9. It's impossible that you\x01",
            "could be the father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600762V#0006F#12P*sigh* That goes without saying...\x02\x03",
            "#3600763V#0001FWhere did you even get the idea that\x01",
            "she was my daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600764V#1306F#5PI mean, you two struck me as family\x01",
            "the moment I saw you together...\x02\x03",
            "#3600765V#1300FBecause of that, I was convinced that\x01",
            "you were her father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600766V#0011F#12PWhat?\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x2)

    ChrTalk(
        0x153,
        (
            "#3600767V#1105F#6PYou're my dad, Lloyd?!\x02\x03",
            "#3600768V#1110FI had no idea!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        "#3600769V#0012F#11PNo, I'm not!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(150)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_62AA")

    ChrTalk(
        0xB,
        (
            "#3600770V#1302F#11PHeehee. Hey, Elie...\x02\x03",
            "#3600779VLook at them sitting there. They DO\x01",
            "give off that impression, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3600772V#0105F#5PHuh... Now that you mention it, I'm\x01",
            "starting to see it, too.\x02\x03",
            "#3600773V#0104FSure, they don't look alike at all, but\x01",
            "the way they interact with each other...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6526")

    label("loc_62AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_63FA")

    ChrTalk(
        0xB,
        (
            "#3600774V#1302F#11PHeehee. Hey, Tio...\x02\x03",
            "#3600775VLook at them, standing there. They DO\x01",
            "give off that impression, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3600776V#0205F#5PNow that you mention it, I have to agree.\x02\x03",
            "#3600777V#0204FThey don't share any physical characteristics,\x01",
            "but their interactions very much remind me of\x01",
            "father and child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6526")

    label("loc_63FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6526")

    ChrTalk(
        0xB,
        (
            "#3600778V#1302F#11PHeehee. Hey, Randy...\x02\x03",
            "#3600771VLook at them, standing there. They DO\x01",
            "give off that impression, don't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3600780V#0305F#5PY'know, you might be on to somethin'.\x02\x03",
            "#3600781V#0309FSure, they look nothin' alike, but those\x01",
            "two definitely act like they're related.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6526")


    ChrTalk(
        0x101,
        "#3600782V#0011F#12PA-Are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#3600783V#1104F#6PHehehe... Lloyd is my dad, huh?\x02\x03",
            "#3600784V#1100FCan I call you Dad, now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3600785V#0012F#11PCan't we just stick with Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600786V#1103F#6PHmm, I guess.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x0)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#3600787V#1110F#12PAnyway, Cecile, you're super nice!\x02\x03",
            "#3600788V#1109FYup, I like you a lot!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#3600789V#1309F#5PHeehee. And I like you, KeA.\x02\x03",
            "#3600790VI'd say our personalities mesh\x01",
            "pretty well, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#3600791V#1109F#12PDefinitely!\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_679A")

    ChrTalk(
        0x102,
        "#3600792V#0102F#5P(They've become friends in no time.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_684D")

    label("loc_679A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_67FB")

    ChrTalk(
        0x103,
        (
            "#3600793V#0202F#5P(It did not take long for them to\x01",
            "be good friends, did it?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_684D")

    label("loc_67FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_684D")

    ChrTalk(
        0x104,
        (
            "#3600794V#0300F#5P(Haha. KeA's charm must've gotten\x01",
            "to Cecile, eh?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684D")


    ChrTalk(
        0x101,
        (
            "#3600795V#0006F#12P(*sigh* These two are a handful,\x01",
            "that's for sure...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3600796V#1303F#5PSo, Lloyd...about KeA's memories...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    ChrTalk(
        0x101,
        (
            "#3600797V#0003F#12PYeah, I think we gave you the gist of\x01",
            "the situation earlier.\x02\x03",
            "#3600798V#0001FWe were planning to take KeA to the\x01",
            "Neurology Department.\x02\x03",
            "#3600799VDo you know who we should talk to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600800V#1304F#5PI do, but I think you may have already\x01",
            "met him.\x02\x03",
            "#3600801V#1300FDoctor Joachim Guenter is his name.\x02",
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
        (
            "#3600802V#0005F#12PWait, what? Doctor Guenter specializes\x01",
            "in neurology?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6B21")
    SetChrSubChip(0x102, 0x1)

    ChrTalk(
        0x102,
        "#3600803V#0105F#6PThat's what he does at St. Ursula...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BAC")

    label("loc_6B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6B6B")
    SetChrSubChip(0x103, 0x1)

    ChrTalk(
        0x103,
        "#3600804V#0205F#6PSo, that is what he practices...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BAC")

    label("loc_6B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6BAC")
    SetChrSubChip(0x104, 0x1)

    ChrTalk(
        0x104,
        "#3600805V#0305F#6PHuh. Didn't see that comin'.\x02",
    )

    CloseMessageWindow()

    label("loc_6BAC")


    ChrTalk(
        0xB,
        (
            "#3600806V#1302F#5PWell, at first glance, you just see a carefree\x01",
            "fisherman, but...\x02\x03",
            "#3600807VI've heard that he actually made amazing\x01",
            "breakthroughs at a foreign medical institution.\x02\x03",
            "#3600808VHere at St. Ursula, he manages the Pharmacology\x01",
            "and Neurology departments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600809V#0000F#12PThat's pretty impressive.\x02\x03",
            "#3600810VSo you think talking about KeA's condition\x01",
            "with him would be a safe bet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3600811V#1304F#5PI do. I have no doubt that he'll\x01",
            "be able to help in some fashion.\x02\x03",
            "#3600812V#1302FWe should stop by the reception\x01",
            "desk and see if he's available.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21610, 3000)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_5D7B end

    def Function_16_6E0D(): pass

    label("Function_16_6E0D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-10080, 1000, 14190, 0)
    MoveCamera(53, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19140, 0)
    SetChrPos(0x101, -10300, 0, 13500, 270)
    SetChrPos(0x102, -10300, 0, 14700, 270)
    SetChrPos(0x103, -9100, 0, 13500, 270)
    SetChrPos(0x104, -9100, 0, 14700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EB6")
    SetChrPos(0x109, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_6EE1")

    label("loc_6EB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EE1")
    SetChrPos(0x10A, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_6EE1")

    SetChrSubChip(0x9, 0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0000FExcuse me. Are you Flora?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PThat's right. Do you have\x01",
            "some sort of business with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FWe're from the Crossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "We actually came to collect your\x01",
            "overdue library book, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#6POh, so that's what this is about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PHmm, the thing is, I DO want to\x01",
            "return it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    ChrTalk(
        0x102,
        "#11P#0105FAre you implying you can't...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PYes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYou see, I like to grab medical textbooks\x01",
            "from the research ward's reference room\x01",
            "and study here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PBut from the looks of it, I must have mixed\x01",
            "up the library book and textbooks when I\x01",
            "was returning them to the reference room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PBy the time I realized that, I kind of forgot\x01",
            "where I put it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0203F...Brilliant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FWell, guess that leaves us no choice.\x02\x03",
            "#0300FI feel for her, though. I always lose\x01",
            "track of where I put my mags.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0211FI feel like that is the type of reading material\x01",
            "that people make sure NOT to lose, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FKnock it off, you two... Anyway, the overdue book\x01",
            "should be on one of the reference room shelves,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes, I'm sure of it. I'm sorry about this,\x01",
            "but do you mind finding it for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYou can find the research ward\x01",
            "on the hospital's roof, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FDon't worry, we know the place.\x02\x03",
            "#0000FReady, everyone?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7486")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7486")

    SetChrPos(0x0, -10220, 0, 13340, 270)
    OP_29(0x28, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_16_6E0D end

    def Function_17_74A0(): pass

    label("Function_17_74A0")

    EventBegin(0x1)

    ChrTalk(
        0x103,
        "#0205FLloyd, this way leads to the cafeteria.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, oops.\x02\x03",
            "#0001FWe should take a closer look at those\x01",
            "boxes and containers stacked outside.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9230, 3750, 13010, 0)
    EventEnd(0x4)
    Return()

    # Function_17_74A0 end

    def Function_18_7554(): pass

    label("Function_18_7554")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　       Visitor and Outpatient Lodgings　　\x01",
            "Speak with the superintendent prior to use of rooms.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_7554 end

    SaveToFile()

Try(main)
