from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2020",                  # 0
        "Warrant Officer Mireille",# 1
        "Guardsman Brood",        # 2
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch23000.itc",                   # 02
    ))

    DeclNpc(-1309,   0,       42250,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(40889,   0,       -30579,  315,  261,  0x0, 0,   1,   0,   0,   2,   0,   8,   255,  0)

    ScpFunction((
        "Function_0_10C",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_24D",          # 02, 2
        "Function_3_278",          # 03, 3
        "Function_4_351",          # 04, 4
        "Function_5_352",          # 05, 5
        "Function_6_551",          # 06, 6
        "Function_7_24D3",         # 07, 7
        "Function_8_26EA",         # 08, 8
        "Function_9_2B66",         # 09, 9
        "Function_10_2CE2",        # 0A, 10
        "Function_11_42DC",        # 0B, 11
        "Function_12_4D2D",        # 0C, 12
    ))


    def Function_0_10C(): pass

    label("Function_0_10C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_10C end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24C")
    OP_95(0xFE, -890, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, -10930, 2000, 0x0)
    OP_95(0xFE, -890, 0, -10930, 2000, 0x0)
    Jump("Function_1_1C4")

    label("loc_24C")

    Return()

    # Function_1_1C4 end

    def Function_2_24D(): pass

    label("Function_2_24D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_94(0xFE, 0x99A2, 0xFFFF838C, 0xA4BA, 0xFFFF8E40, 0x3E8)
    Sleep(300)
    Jump("Function_2_24D")

    label("loc_277")

    Return()

    # Function_2_24D end

    def Function_3_278(): pass

    label("Function_3_278")

    SetMapObjFrame(0xFF, "main03", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29D")
    SetMapObjFrame(0xFF, "main03", 0x1, 0x1)

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1")
    SetChrPos(0x8, -40640, 0, 1570, 135)
    Jump("loc_322")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31D")

    label("loc_2E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_30C")
    SetChrPos(0x8, -35130, 0, 4170, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_31D")

    label("loc_30C")

    SetChrPos(0x8, -40640, 0, 1570, 135)

    label("loc_31D")

    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    SetChrFlags(0x9, 0x80)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Event(0, 12)

    label("loc_350")

    Return()

    # Function_3_278 end

    def Function_4_351(): pass

    label("Function_4_351")

    Return()

    # Function_4_351 end

    def Function_5_352(): pass

    label("Function_5_352")

    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(
        0xFE,
        "W-W-Wait...! Randy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FOh, if it isn't Mireille. How ya been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I see you still haven't learned\x01",
            "any manners...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Besides, I was promoted to warrant\x01",
            "officer! Don't address me so casually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha. Is that so?\x02\x03",
            "#0304FEither way, I'm outta the Guardian Force,\x01",
            "so I don't care too much about ranks and\x01",
            "all that jazz.\x02\x03",
            "#0309FBut, if you insist, I'll address you with the\x01",
            "utmost respect, Warrant Officer Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Enough! Just do whatever you want,\x01",
            "I don't care anymore!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 1)
    Return()

    # Function_5_352 end

    def Function_6_551(): pass

    label("Function_6_551")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F")
    Call(0, 5)
    Jump("loc_824")

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746")

    ChrTalk(
        0xFE,
        (
            "We just had a shipment of supplements\x01",
            "being researched at St. Ursula Medical\x01",
            "College arrive not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Based on everything I've heard, these\x01",
            "particular ones are ground-breaking and\x01",
            "last much longer than our usual stock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSt. Ursula never fails to amaze.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHey, Mireille. Mind sharin' some\x01",
            "of them with yours truly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sorry, Randy. There were only\x01",
            "enough pills for our unit here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FDamn, what a letdown...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_824")

    label("loc_746")


    ChrTalk(
        0xFE,
        (
            "We just had a shipment of supplements\x01",
            "being researched at St. Ursula Medical\x01",
            "College arrive not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have an intense drill planned at\x01",
            "Knox Forest tonight, so I'm hoping\x01",
            "that these will keep us going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_824")

    Jump("loc_24CF")

    label("loc_829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_844")
    Call(0, 5)
    Jump("loc_BF8")

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEC")

    ChrTalk(
        0xFE,
        (
            "Tomorrow night, we're traveling to the Knox\x01",
            "Forest for a combat drill, but we're only\x01",
            "going to use our standard-issue gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Crossbell Guardian Force's standard-issue\x01",
            "weapons consist of stun halberds and assault\x01",
            "rifles. All soldiers are trained in both, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That didn't stop a certain SOMEONE from ignoring\x01",
            "the rules and only practicing with the stun halberds.\x01",
            "*glare*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHahaha. It's not my fault for remembering the\x01",
            "basics of close quarters combat so well, is it?\x02\x03",
            "#0300FY'know, I'm always down to give you a\x01",
            "few pointers. Some say my halberd skills\x01",
            "are faster than a bullet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* There you go again with\x01",
            "that ego of yours...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BF8")

    label("loc_AEC")


    ChrTalk(
        0xFE,
        (
            "The Crossbell Guardian Force's standard-issue\x01",
            "weapons consists of stun halberds and assault\x01",
            "rifles. All soldiers are trained in both, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Randy, if you just participated in the\x01",
            "basic rifle training...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, never mind. What's in the past\x01",
            "is in the past.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF8")

    Jump("loc_24CF")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C18")
    Call(0, 5)
    Jump("loc_109F")

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8C")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        "You're...Sergeant Major Noel Seeker, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard stories about you. Tangram Gate's\x01",
            "bright, up-and-coming guardsman, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503FThat's a bit of an exaggeration.\x02\x03",
            "#0500FI know working directly under the commander\x01",
            "may be discouraging at times, but please keep\x01",
            "doing the CGF proud, Warrant Officer Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha, Mireille's sense of justice is the only\x01",
            "thing she's had over the other guys, I'd say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        "Th-That's it?! Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FCome on, try not to tease the\x01",
            "warrant officer too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304FFine, fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, Randy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    ChrTalk(
        0xFE,
        (
            "Like I was saying, as a superior officer, it's\x01",
            "always reassuring to see a guardsman like\x01",
            "Sergeant Major Seeker make a name for herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, let's both continue to work towards\x01",
            "making the Crossbell Guardian Force\x01",
            "the best it can possibly be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0501FY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 0)
    Jump("loc_109F")

    label("loc_F8C")


    ChrTalk(
        0xFE,
        (
            "I wanted our unit to conduct the investigation\x01",
            "of those ruins, but we can't do anything about\x01",
            "it, since the order came from the commander...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sergeant Major Seeker, Special Support Section...\x01",
            "I'm leaving the investigation in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304FYep, we got this.\x02",
    )

    CloseMessageWindow()

    label("loc_109F")

    Jump("loc_24CF")

    label("loc_10A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1323")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10CE")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E0")
    Call(0, 5)
    Jump("loc_131E")

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126B")

    ChrTalk(
        0xFE,
        (
            "I've been in charge of leading Bellguard Gate\x01",
            "during the festival, but that ends today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With luck, everything will end without any\x01",
            "complications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FY'know, that idiot you call a commander\x01",
            "is probably gonna leave you hangin' after\x01",
            "the Anniversary Festival, too.\x02\x03",
            "#0300FIt's gonna be up to you to lead the troops\x01",
            "at Bellguard Gate, Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, I know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_131E")

    label("loc_126B")


    ChrTalk(
        0xFE,
        (
            "I'm relieved that our inspections have\x01",
            "carried on with few complications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From here on out, it's my duty to make\x01",
            "sure my fellow guardsmen don't lose\x01",
            "their motivation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131E")

    Jump("loc_24CF")

    label("loc_1323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_168E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134D")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_134D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")
    Call(0, 5)
    Jump("loc_1689")

    label("loc_135F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(
        0xFE,
        (
            "As the acting leader of Bellguard Gate, I've had\x01",
            "to sort through passport applications for people\x01",
            "entering and exiting Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, you hardly\x01",
            "ever did any office work, right, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYep. Me and paperwork don't mix too well.\x02\x03",
            "I usually pushed all that fun stuff onto\x01",
            "Carter or Connors, whoever was closer.\x02\x03",
            "#0309FI made sure to reimburse 'em by introducin'\x01",
            "them to some girls I knew from the places\x01",
            "over in the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Those two are in for an interrogation\x01",
            "next time I see them...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1689")

    label("loc_159D")


    ChrTalk(
        0xFE,
        (
            "Randy...please tell me you aren't doing\x01",
            "the same to the rest of the Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHaha! Lloyd wantin' to do my busywork\x01",
            "in exchange for some gals? Good joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FI-I've never done that, for the record!\x02",
    )

    CloseMessageWindow()

    label("loc_1689")

    Jump("loc_24CF")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_198A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B8")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_16B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CA")
    Call(0, 5)
    Jump("loc_1985")

    label("loc_16CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191D")

    ChrTalk(
        0xFE,
        (
            "Phew... I don't particularly dislike\x01",
            "paperwork, but it can be tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FDon't kid yourself. Warrant Officer Mireille\x01",
            "is a warrior, through and through!\x02\x03",
            "#0300FWhen it comes to combat, she's one of the\x01",
            "best Bellguard Gate has to offer. The guys\x01",
            "out here even listen to her orders, y'know.\x02\x03",
            "Sittin' in a chair and fillin' out papers all day\x01",
            "must suck for a gal like you, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aaargh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You make it sound like I'm some\x01",
            "sort of musclehead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FMy bad, Mireille. The compliments\x01",
            "came from the heart, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Can you just leave me alone?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1985")

    label("loc_191D")


    ChrTalk(
        0xFE,
        (
            "*sigh* Despite how things may look,\x01",
            "I'm extremely busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just leave me alone, Randy.\x02",
    )

    CloseMessageWindow()

    label("loc_1985")

    Jump("loc_24CF")

    label("loc_198A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E41")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1ADF")
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7C")

    ChrTalk(
        0xFE,
        (
            "I intend to thoroughly search the\x01",
            "commander's office for the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We weren't the cause of this mess, but\x01",
            "that doesn't make it any less important!\x01",
            "I will do my duty, whatever it may be!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AD3")

    label("loc_1A7C")


    ChrTalk(
        0xFE,
        (
            "I'm going to leave the rest of the investigation\x01",
            "to the SSS. Good luck out there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD3")

    OP_93(0x8, 0x0, 0x0)
    Jump("loc_1E3C")

    label("loc_1ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1AF3")
    Call(0, 10)
    Jump("loc_1E3C")

    label("loc_1AF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B05")
    Call(0, 5)
    Jump("loc_1E3C")

    label("loc_1B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D46")

    ChrTalk(
        0xFE,
        (
            "Now that the Anniversary Festival has\x01",
            "started, I doubt the commander will show\x01",
            "up at the gate until it ends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the highest-ranking officer here,\x01",
            "it's my duty to make sure Bellguard\x01",
            "Gate's security remains top-notch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FI bet you guys will manage just fine\x01",
            "without that bum. The CGF is filled\x01",
            "with the best of the best, ain't it?\x02\x03",
            "#0304FStill, don't overdo it. I don't want\x01",
            "you to go and screw things up like\x01",
            "last time, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Y-You jerk...! I have no need\x01",
            "for your concern!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(I'm afraid to ask what happened last time...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E3C")

    label("loc_1D46")


    ChrTalk(
        0xFE,
        (
            "During the Anniversary Festival, traffic through\x01",
            "the gate always picks up, so we aren't surprised\x01",
            "if one or two mishaps happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the highest-ranking officer here,\x01",
            "it's my duty to make sure Bellguard\x01",
            "Gate's security remains top-notch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3C")

    Jump("loc_24CF")

    label("loc_1E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2388")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5C")
    Call(0, 5)
    Jump("loc_2383")

    label("loc_1E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224B")
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(
        0xFE,
        (
            "Randy... Y-You really shouldn't be\x01",
            "loitering around Bellguard Gate for\x01",
            "too long, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHaha, what's your deal? You worryin' about\x01",
            "me is a special occasion.\x02\x03",
            "#0300FOh, that reminds me. I've heard from more\x01",
            "than one source that you begged and begged\x01",
            "the brass to not fire me way back when.\x02\x03",
            "#0305FMireille, be honest. Do you lov--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "D-Don't say anything you'd regret!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just didn't want to lose a valuable soldier\x01",
            "because of a silly reason like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHmm? 'Silly reason'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FDo you mean Randy's trouble\x01",
            "with the women here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FGetting kicked out of the CGF for being too\x01",
            "much of a womanizer is certainly something\x01",
            "I could see happening to Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Trouble with women...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FC'mon, Mireille! It's nothin' to be\x01",
            "shy about, is it?\x02\x03",
            "#0304FYou were a liiiiiittle in love with the\x01",
            "Orlando, right? I'm sure if ya admit\x01",
            "it, you'd feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* As usual, talking to you gets\x01",
            "us nowhere...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2383")

    label("loc_224B")


    ChrTalk(
        0xFE,
        (
            "I admit it; I was strongly against\x01",
            "Randy's discharge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However! It definitely wasn't due to having...\x01",
            "r-romantic feelings for him. J-Just, thinking\x01",
            "about it logically, I thought--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FBasically, you knew you'd be lonely\x01",
            "without me around, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        "Ugh! Just think what you want, Randy!\x02",
    )

    CloseMessageWindow()

    label("loc_2383")

    Jump("loc_24CF")

    label("loc_2388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_24CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A3")
    Call(0, 5)
    Jump("loc_24CF")

    label("loc_23A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2452")

    ChrTalk(
        0xFE,
        (
            "*sigh* Leaving the CGF hasn't made you\x01",
            "change in the slightest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure you three must have a tough time\x01",
            "dealing with a jerk like Randy, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24CF")

    label("loc_2452")


    ChrTalk(
        0xFE,
        (
            "My only advice is to be careful around him.\x01",
            "If you aren't paying attention, it'll be hard to\x01",
            "get him back on his leash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24CF")

    TalkEnd(0xFE)
    Return()

    # Function_6_551 end

    def Function_7_24D3(): pass

    label("Function_7_24D3")


    ChrTalk(
        0xFE,
        "Oh, it's the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUh, Warrant Officer Mireille...\x02\x03",
            "#0003FI'm sorry that we weren't able to find that\x01",
            "key for you. We had some pressing issues\x01",
            "to take care of, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, don't beat yourselves up over it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After you left, I searched for it until\x01",
            "morning but didn't have any luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FHey, I'm sorry. Seriously.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "Apologizing? To me?\x01",
            "That doesn't suit you, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You were busy and no amount of apologies can\x01",
            "change that. Really, it wasn't a big deal, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 3)
    Return()

    # Function_7_24D3 end

    def Function_8_26EA(): pass

    label("Function_8_26EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27A0")

    ChrTalk(
        0xFE,
        (
            "Schedule says that we have a combat\x01",
            "drill tonight on the forest road...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's always drill after drill--never anything\x01",
            "that actually tests us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27E4")

    label("loc_27A0")


    ChrTalk(
        0xFE,
        (
            "Guess we've got no choice, but still,\x01",
            "how pathetic can we get?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E4")

    Jump("loc_2B62")

    label("loc_27E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_28DF")

    ChrTalk(
        0xFE,
        (
            "When Burrell from Tangram Gate told me\x01",
            "the ruins investigation was over, I nearly\x01",
            "jumped for joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The SSS gave a helping hand to Sergeant\x01",
            "Major Seeker during that ordeal, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Either way, I appreciate what you did.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B62")

    label("loc_28DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29C3")

    ChrTalk(
        0xFE,
        (
            "I recently got my hands on a poster\x01",
            "of Arc en Ciel's new dancer, Rixia Mao,\x01",
            "from my buddy over at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pinned it up right over there if you want to\x01",
            "give her a look. Quite something, ain't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B62")

    label("loc_29C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DE")
    Call(0, 9)
    Jump("loc_2A76")

    label("loc_29DE")


    ChrTalk(
        0xFE,
        (
            "Now that I've worked under the CGF\x01",
            "commander for a while now, I know\x01",
            "without a doubt that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...having a boss like him is the absolute worst.\x02",
    )

    CloseMessageWindow()

    label("loc_2A76")

    Jump("loc_2B62")

    label("loc_2A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B62")

    ChrTalk(
        0xFE,
        (
            "Ever since the commander started to skip out\x01",
            "on work, Warrant Officer Mireille has been our\x01",
            "sort of interim commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a bit unreliable, but I can't deny that she\x01",
            "has drive. Overall, she's a good superior.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B62")

    TalkEnd(0xFE)
    Return()

    # Function_8_26EA end

    def Function_9_2B66(): pass

    label("Function_9_2B66")


    ChrTalk(
        0xFE,
        (
            "Well, it looks like my break is already\x01",
            "over. Time to get back to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I think of Warrant Officer Mireille\x01",
            "as my boss, instead of the commander,\x01",
            "work becomes a lot more bearable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right. I just finished this book while\x01",
            "I was on break, so be a friend and take\x01",
            "it with you, okay?\x02",
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
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CA, 1)
    SetScenarioFlags(0x9C, 4)
    Return()

    # Function_9_2B66 end

    def Function_10_2CE2(): pass

    label("Function_10_2CE2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35280, 900, 2640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24100, 0)
    SetChrPos(0x101, -34000, 0, 1500, 0)
    SetChrPos(0x102, -35300, 0, 1000, 0)
    SetChrPos(0x103, -34000, 0, 500, 0)
    SetChrPos(0x104, -35300, 0, 2000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4260")

    ChrTalk(
        0x8,
        "#11POh, drat... Just where did it run off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PIf I don't find it soon...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_2F64")

    ChrTalk(
        0x104,
        (
            "#6P#0300FYo, Mireille. How's my favorite\x01",
            "CGF soldier doin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FNice to see you again, Warrant Officer.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    ChrTalk(
        0x8,
        (
            "#11PRandy? And the rest of the Special\x01",
            "Support Section? What are you four\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#11POh, right! It's about that support\x01",
            "request I submitted, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI've been in such a rush, I nearly\x01",
            "forgot about it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BD")

    label("loc_2F64")


    ChrTalk(
        0x104,
        (
            "#6P#0300FYo, Mireille. How's my favorite\x01",
            "CGF soldier doin'?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    ChrTalk(
        0x8,
        "#11PRandy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PW-Wait...RANDY?! What are\x01",
            "you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd just who are these three...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FOh, sorry about that. I'm Lloyd Bannings,\x01",
            "of the Crossbell Police Department,\x01",
            "Special Support Section.\x02\x03",
            "#0000FWe came by to ask about the support\x01",
            "request you submitted to us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh? Now that I think about it, Randy did\x01",
            "mention something about a Special\x01",
            "Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe fact that I sent that request to you\x01",
            "all completely slipped my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BD")

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
        0x102,
        (
            "#6P#0109FI'm sure you have your work cut out\x01",
            "for you here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0304FHaha, classic Mireille. She puts on the\x01",
            "serious face, but she's really not all there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PE-Excuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSomeone like YOU has no right\x01",
            "to say that to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FCan we calm down, everyone?\x02\x03",
            "#0001FI know it's sudden, but would you\x01",
            "mind explaining the request to us?\x02\x03",
            "The CGF wouldn't be coming to us\x01",
            "for help unless it really needed it, so\x01",
            "I've been curious to learn the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAhem. Yes, that's correct. I'm sorry\x01",
            "we're a little disorganized right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSo you see, we've accidentally misplaced\x01",
            "something incredibly important to the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNormally, finding it would be our top priority,\x01",
            "but as you can see, we're running short on\x01",
            "manpower during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThat's why we decided to ask for some\x01",
            "assistance in the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FI think I understand the situation.\x02\x03",
            "#0105FSo, what exactly are we looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's the key to the armored car that the\x01",
            "Guardian Force has just deployed. It's\x01",
            "one of the newer models.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FA new model...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI had only heard rumors about it...\x01",
            "So it has finally been deployed?\x02\x03",
            "I fail to understand how you could\x01",
            "have lost something so valuable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0301FLemme guess. The commander?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_37E2():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37E2)

    def lambda_37EF():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37EF)

    def lambda_37FC():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37FC)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11PI suppose that wasn't a hard guess.\x02",
    )

    CloseMessageWindow()

    def lambda_3839():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3839)

    def lambda_3846():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3846)

    def lambda_3853():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3853)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#0005FIt wasn't? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, it started yesterday. The commander\x01",
            "had thrown an exclusive party, celebrating\x01",
            "Crossbell's 70th birthday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAt said party, the commander drank more\x01",
            "alcohol than he probably should have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...and then he had one of the soldiers drive\x01",
            "our new armored car to his party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FMust've been tryin' to win over his guests\x01",
            "by showin' off his new, shiny ride, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FAudacious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POnce the commander returned and had\x01",
            "the car parked inside the gate, the soldier\x01",
            "gave the key back to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd, somehow, he misplaced it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNow that we can't move it, we had\x01",
            "no choice but to put a tarp over it in\x01",
            "a last-ditch effort to conceal it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FI was wondering what that was doing outside.\x02\x03",
            "#0001FBut was that really your best move? The\x01",
            "tarp makes it look more suspicious, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FWell, if they left the car as is, it would\x01",
            "probably raise a lot of questions they\x01",
            "don't wish to answer.\x02\x03",
            "#0103FFor example, why exactly is the CGF's\x01",
            "new heavy-duty armored car actively\x01",
            "deployed inside of the border gate?\x02\x03",
            "#0101FIf the Imperial Army took it as a threat,\x01",
            "I'm not sure we'd be able to reason with\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FYou can't be serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAt the very least, we'd like to avoid any\x01",
            "provocation at all costs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FIs this new model really all that?\x02\x03",
            "#0300FThe armored car we were usin' before\x01",
            "was pretty nice when it came to defense\x01",
            "and mobility, if I remember right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTrust me, it is. The new model is an upgraded,\x01",
            "more combat-oriented version of our old cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's equipped with vulcan cannons,\x01",
            "miniature missile pods, and an\x01",
            "overhaul of its base firepower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you inspected the CGF's entire\x01",
            "arsenal, it would easily come out\x01",
            "on top. No doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0301FGot'cha. I agree with ya, then. Leavin'\x01",
            "that out in the open ain't a good idea.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x104,
        (
            "#6P#0303FSo? Where exactly is that\x01",
            "oh-so wonderful commander\x01",
            "right now anyway?\x02\x03",
            "#0301FThis was his room, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'll get to all that. This morning, the\x01",
            "commander left and told us to 'Find\x01",
            "that blasted key while I'm gone!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAlso, he made sure to inform us that he\x01",
            "absolutely had to use the festival's social\x01",
            "gatherings to his advantage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0303FTch. Sounds like him, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThe more I hear about this commander,\x01",
            "the less I am eager to meet him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnyway, we really want to move\x01",
            "the armored car out of the public\x01",
            "eye ASAP...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWill you help us find the key?\x02",
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1)
    SetScenarioFlags(0x8C, 1)
    Jump("loc_42D8")

    label("loc_4260")

    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11PWe want to move the armored car\x01",
            "out of the public eye ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo, will you help us find the key?\x02",
    )

    CloseMessageWindow()

    label("loc_42D8")

    Call(0, 11)
    Return()

    # Function_10_2CE2 end

    def Function_11_42DC(): pass

    label("Function_11_42DC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_432D"),
        (1, "loc_4BC9"),
        (SWITCH_DEFAULT, "loc_4CEB"),
    )


    label("loc_432D")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#12P#0001FWe'd be happy to help, Warrant Officer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PReally...? Thank you very much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FNow, would you mind helping us\x01",
            "retrace the commander's steps?\x02\x03",
            "Did he mention anything that might\x01",
            "give us any leads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PLet me think... If you'd like to hear what\x01",
            "I was able to get out of him this morning,\x01",
            "I would be more than happy to share.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FThat should suffice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhen the commander returned, he had the\x01",
            "armored car parked right inside of the gate,\x01",
            "and he took the key from the soldier driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PMost likely due to craving a light meal in\x01",
            "an attempt to sober up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSo, he stopped by the mess hall and had\x01",
            "one of the cooks make him some food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAfterwards, he waltzed up to the roof and sung\x01",
            "his heart out for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...and once he finished, he realized that he\x01",
            "had no idea where the key had gone.\x02",
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
        0x103,
        "#6P#0203FHe sounds like a proper drunk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FI think it was a miracle that he made it\x01",
            "to the rooftop at all, given his condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0301FWhat a loser.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FFrom what we just heard, we know for\x01",
            "a fact that the key was lost while he was\x01",
            "gallivanting around the gate.\x02\x03",
            "#0103FAnd if that's the case, we shouldn't have\x01",
            "to worry about searching anywhere other\x01",
            "than Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FI agree, Elie.\x02\x03",
            "#0000FAll right, then. We should perform a\x01",
            "sweep of the general area first.\x02\x03",
            "Who knows? We might find some\x01",
            "clues or, with luck, the key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWarrant Officer Mireille, would you\x01",
            "like to accompany us on our search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo, I'm sorry. I feel like I would just\x01",
            "get in the way if I came along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIn the meantime, I'll search for it by\x01",
            "tearing apart the commander's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0304FSounds good, Mireille. Even in the most\x01",
            "desperate of situations, you can\x01",
            "always count on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGeez, Randy. I AM counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe should go ahead and commence\x01",
            "our search for the key.\x02\x03",
            "Let's start by checking out the armored car\x01",
            "and its surrounding area.\x02",
        )
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
            "[Important Item Retrieval]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x19, 0x1, 0x2)
    Jump("loc_4CFA")

    label("loc_4BC9")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#12P#0006FI feel horrible about this, but we have\x01",
            "other business we have to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PO-Oh. Is that right...? Well, I suppose\x01",
            "I can't fault you for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you have any spare time later, please\x01",
            "come talk to me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI'm counting on you, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CFA")

    label("loc_4CEB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4CFA")

    label("loc_4CFA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -34470, 0, 200, 90)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_42DC end

    def Function_12_4D2D(): pass

    label("Function_12_4D2D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-42850, 900, 590, 0)
    MoveCamera(294, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0x101, -33410, 0, -910, 225)
    SetChrPos(0x102, -32170, 0, 1270, 315)
    SetChrPos(0x103, -33510, 0, 870, 315)
    SetChrPos(0x104, -32220, 0, -420, 270)
    Sleep(500)
    OP_68(-36150, 900, 890, 5000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0005FRandy, you know what this room is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FThis office belongs to His Excellency,\x01",
            "the Crossbell Guardian Force Commander.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#0005FReally? It doesn't look like he's here\x01",
            "right now, though.\x02\x03",
            "Just where is he...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FProbably out partying or somethin'.\x02\x03",
            "Guy rarely does his job. He usually\x01",
            "leaves everything to his subordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIf that's the case, maybe we should\x01",
            "give up on meeting him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FHuh? You wanted to meet him?\x02\x03",
            "#0306FListen, dude. I'd rather not come\x01",
            "face to face with my former boss.\x01",
            "That'd be WAY too awkward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYou might have a point there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FThat aside, this room is clearly\x01",
            "in extremely poor taste.\x02\x03",
            "#0101FImagine the tens of thousands\x01",
            "of mira it took to purchase all of\x01",
            "these antiques on display...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FPersonally, I am having trouble picturing\x01",
            "this as an office in the first place, let alone\x01",
            "the CGF commander's.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        (
            "#0300FI bet he got 'em with all that bribe money\x01",
            "he's built up over the years.\x02\x03",
            "#0306FMan, what a waste. If I had that much mira, I'd\x01",
            "be throwin' it all over the Entertainment District,\x01",
            "livin' it up.\x02\x03",
            "I'd treat some babes to a good time and\x01",
            "spend all night gamblin' away at the casino.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        (
            "#0211FPerhaps you two are not as different\x01",
            "as you might think.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -32220, 0, -420, 270)
    SetScenarioFlags(0x6F, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_4D2D end

    SaveToFile()

Try(main)
