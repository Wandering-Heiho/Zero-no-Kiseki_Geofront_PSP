from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "Old Man Mors",           # 1
        "Old Man Mors",           # 2
        "Parla",                  # 3
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(-2160,   100,     6829,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)

    ScpFunction((
        "Function_0_110",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_346",          # 03, 3
        "Function_4_399",          # 04, 4
        "Function_5_27C0",         # 05, 5
        "Function_6_2C3B",         # 06, 6
    ))


    def Function_0_110(): pass

    label("Function_0_110")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_150"),
        (1, "loc_15C"),
        (2, "loc_168"),
        (3, "loc_174"),
        (4, "loc_180"),
        (5, "loc_18C"),
        (6, "loc_198"),
        (SWITCH_DEFAULT, "loc_1A4"),
    )


    label("loc_150")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_15C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_168")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_174")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_180")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_18C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_198")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1C7")

    Return()

    # Function_0_110 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_221")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2200, 30, 8350, 135)
    SetChrFlags(0xA, 0x10)
    Jump("loc_345")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22F")
    Jump("loc_345")

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_23D")
    Jump("loc_345")

    label("loc_23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24B")
    Jump("loc_345")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_259")
    Jump("loc_345")

    label("loc_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26C")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_292")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BD")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_345")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D0")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_345")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    Jump("loc_345")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_345")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_345")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_345")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_345")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_33C")
    Jump("loc_345")

    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_345")

    label("loc_345")

    Return()

    # Function_2_1F3 end

    def Function_3_346(): pass

    label("Function_3_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_365")

    label("loc_35F")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_398")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_398")

    Return()

    # Function_3_346 end

    def Function_4_399(): pass

    label("Function_4_399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF5")
    TurnDirection(0x8, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_544")

    ChrTalk(
        0xFE,
        (
            "Oh, you're that lad that we sat with on\x01",
            "the train, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FOh, you're that old man from back then!\x01",
            "Haha. It's been a while, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Indeed it has! A couple months, I believe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to remember you reporting in\x01",
            "to your first day of work that day.\x01",
            "How's that been treating you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIt's hard, but I'm scraping by.\x01",
            "I feel like I'm getting used to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795")

    label("loc_544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6D9")

    ChrTalk(
        0xFE,
        (
            "Oh, you're that lad that we sat with on\x01",
            "the train, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FOh, you're that old man from back then!\x01",
            "Haha. It's been a while, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Indeed it has! A couple months, I believe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to remember you reporting in\x01",
            "to your first day of day of work that day.\x01",
            "How's that been treating you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FIt's hard, but I'm scraping by.\x01",
            "I feel like I'm getting used to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_795")

    label("loc_6D9")


    ChrTalk(
        0xFE,
        (
            "Oh, you're that lad that we sat with on\x01",
            "the train, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How was your first day at work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FThank you for asking. I feel like I'm\x01",
            "really starting to get the hang of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_795")


    ChrTalk(
        0xFE,
        (
            "Hoho! Are these your colleagues? It's nice to\x01",
            "see a group of young people working together\x01",
            "towards a better tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know how much I can help, but feel\x01",
            "free to drop by and chat if you want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Back in my day, I was a merchant. I'm lucky\x01",
            "to have a few connections around the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, wow. I never knew that.\x02\x03",
            "#0000FWho are you acquainted with, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Let me think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's the mayor of Crossbell, and there's a\x01",
            "certain association of merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, a good friend of mine is also the\x01",
            "director of St. Ursula Hospital.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        "#0303FUh, Lloyd? Isn't this guy kind of a big deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FUm, sir, what do you do for a living?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I'm glad you asked! I am the\x01",
            "sitting chairman of Crossbell's\x01",
            "Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't go getting all nervous now.\x01",
            "It's not that big of a deal, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(His appearance does not play the part, though.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104F(So this is Chairman Mors of the Business\x01",
            "Owners' Association?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 4)
    Jump("loc_27BC")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_27BC")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE7")

    ChrTalk(
        0xFE,
        (
            "There was already an incident yesterday,\x01",
            "but now there's another problem down\x01",
            "at the airport?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's with all the occurrences lately?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The diet's probably too busy to give them any mind.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D6A")

    label("loc_CE7")


    ChrTalk(
        0xFE,
        (
            "Us merchants are a bit more sensitive to\x01",
            "what's happening around us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All these accidents recently are\x01",
            "making me worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6A")

    Jump("loc_27BC")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E4D")

    ChrTalk(
        0xFE,
        (
            "The latest issue of the Crossbell Times\x01",
            "didn't get delivered this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I asked my wife if she knew anything,\x01",
            "but she's just as clueless as I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, no... Has the paper been put\x01",
            "on hiatus?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BC")

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(
        0xFE,
        (
            "To no one's surprise, the diet\x01",
            "meeting has been extended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The longer they delay it, the longer it'll\x01",
            "take for the budget to get enforced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't those stubborn fools shut up and\x01",
            "decide already? If they keep it up, it'll\x01",
            "start causing problems for the rest of us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1013")

    label("loc_F7D")


    ChrTalk(
        0xFE,
        (
            "Right. I was expecting Speaker Hartmann\x01",
            "to refuse to compromise on his position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, the diet continues to\x01",
            "extend the budget meeting...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1013")

    Jump("loc_27BC")

    label("loc_1018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1AD2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1450")

    ChrTalk(
        0xFE,
        (
            "Ah, it's Lloyd and his friends. I appreciate\x01",
            "your help during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_125A")

    ChrTalk(
        0x101,
        (
            "#0000FNot at all, sir. It's only natural for officers to\x01",
            "give a helping hand to those in need.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(
        0x102,
        "#0100FI'm just glad we were able to resolve the issue.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1224")

    label("loc_1161")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C1")

    ChrTalk(
        0x103,
        (
            "#0204FBut also, we were able to display our true\x01",
            "potential as a team.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1224")

    label("loc_11C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1224")

    ChrTalk(
        0x104,
        (
            "#0304FThat's what you'd expect from the renowned\x01",
            "Special Support Section, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1224")


    ChrTalk(
        0xFE,
        (
            "Well, aren't you youngsters\x01",
            "full of energy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CB")

    label("loc_125A")


    ChrTalk(
        0x101,
        "#0006FI apologize for failing to help you...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12CA")

    ChrTalk(
        0x102,
        "#0103FWe're sorry for worrying you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_12CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1307")

    ChrTalk(
        0x103,
        "#0203FOur failure was unfortunate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_134A")

    label("loc_1307")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134A")

    ChrTalk(
        0x104,
        "#0306FDon't got much for excuses to offer ya.\x02",
    )

    CloseMessageWindow()

    label("loc_134A")


    ChrTalk(
        0xFE,
        (
            "No, no. What matters is that you tried your\x01",
            "hardest with the investigation. All of the locals\x01",
            "appreciate your efforts, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CB")


    ChrTalk(
        0xFE,
        (
            "Oh, by the way. You all seem to have brought\x01",
            "a child with you today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you taking her down to the police station?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1511")

    label("loc_1450")


    ChrTalk(
        0xFE,
        (
            "Oh, well if it isn't Lloyd! I haven't\x01",
            "seen you in a while, lad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, what's this? You seem to have brought\x01",
            "a small child with you today.\x01",
            "Are you taking her down to the police station?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1511")


    ChrTalk(
        0x101,
        (
            "#0000FSomething along those lines. We're trying to\x01",
            "uncover her identity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, really? Well, good luck with that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Excuse me, young lady. You'd better look both\x01",
            "ways before crossing the street, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And make sure you don't run out onto the road!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111FDo. Not. Run. Onto. Road...\x02\x03",
            "#1109FOkay, I got it! I won't run onto any roads!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hoho. She's a sharp one!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 7)
    Jump("loc_1ACD")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1D")

    ChrTalk(
        0xFE,
        (
            "The diet plans to reconvene,\x01",
            "starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I imagine the Imperial and Republican factions\x01",
            "plan to bicker the entire time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I fully sympathize with Mayor MacDowell's struggles\x01",
            "as he attempts to herd those groups of man-children.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A15")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(
        0x101,
        (
            "#0003F(He seems pretty worried about your\x01",
            "grandfather, Elie.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Well, they've been friends for a long time,\x01",
            "so I'm not exactly surprised.)\x02\x03",
            "#0108F(I'm the same, to be honest. I'm worried\x01",
            "for how the diet will proceed.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A15")

    label("loc_18B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1967")

    ChrTalk(
        0x103,
        (
            "#0203F(The chairman is showing signs of\x01",
            "unease regarding Elie's grandfather.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yeah, well, according to Elie, those\x01",
            "two are longtime friends.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A15")

    label("loc_1967")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(
        0x104,
        (
            "#0303F(The chairman is sweatin' real hard over\x01",
            "Mademois-Elie's grandad, eh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yeah, well, according to Elie, those two\x01",
            "are longtime friends.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A15")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACD")

    label("loc_1A1D")


    ChrTalk(
        0xFE,
        (
            "Bah, Mayor MacDowell is the only honest\x01",
            "politician you'll find in this crooked pit of\x01",
            "a government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The diet won't make it easy, but all we\x01",
            "can do is watch over him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACD")

    Jump("loc_27BC")

    label("loc_1AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1AE0")
    Jump("loc_27BC")

    label("loc_1AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1AEE")
    Jump("loc_27BC")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1CFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C30")

    ChrTalk(
        0xFE,
        (
            "Are you all excited for next month's\x01",
            "Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to focus on the fact that the\x01",
            "Crossbell Diet meets one week after\x01",
            "it ends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a crucial meeting responsible for deciding\x01",
            "the city's yearly budget... I must make sure\x01",
            "the members don't act out of self-interest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CF9")

    label("loc_1C30")


    ChrTalk(
        0xFE,
        (
            "I'll have to prepare for the diet's budget meeting\x01",
            "after the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor is neutral to either faction, so\x01",
            "this will be a do-or-die moment for him.\x01",
            "Us merchants will be wary, as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF9")

    Jump("loc_27BC")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    ChrTalk(
        0xFE,
        (
            "Those Revache members got bailed\x01",
            "out, eh? The fact they can get\x01",
            "off scot-free gets on my nerves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I decided to not get involved in politics,\x01",
            "and that's why I get so antsy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E6B")

    label("loc_1DD0")


    ChrTalk(
        0xFE,
        (
            "Crossbell politics have long been\x01",
            "corrupted by mira and foreign interests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Give me a break... Day after day,\x01",
            "the diet never fails to disappoint.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6B")

    Jump("loc_27BC")

    label("loc_1E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2057")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB3")

    ChrTalk(
        0xFE,
        (
            "Dinz should be having a big sale on\x01",
            "vegetables in the marketplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've helped him out a few times before, so now\x01",
            "he stops by to check up on me occasionally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see that he's still the honest merchant I know\x01",
            "and respect. I hope all of our young merchants\x01",
            "can be just as successful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2052")

    label("loc_1FB3")


    ChrTalk(
        0xFE,
        (
            "As an elderly, retired merchant, it falls on\x01",
            "my shoulders to help the youngsters out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's important that he's able to continue\x01",
            "being an honest man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2052")

    Jump("loc_27BC")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D1")

    ChrTalk(
        0xFE,
        "I must leave for tonight's meeting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to arrange general meetings\x01",
            "and provide financial statements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival's nearing, so I'll\x01",
            "need to get in touch with the mayor soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha... Yeah, I figured you'd be really\x01",
            "busy, Chairman Mors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course. I may be old, but I'm still\x01",
            "working all the time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2240")

    label("loc_21D1")


    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association is meeting tonight,\x01",
            "so it falls in my court to make preparations for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2240")

    Jump("loc_27BC")

    label("loc_2245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238A")

    ChrTalk(
        0xFE,
        (
            "Despite what you may think, the merchants\x01",
            "of Crossbell actually do more than butt heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There has been a network of merchants\x01",
            "here in East Street for a long time, so\x01",
            "we've come to help each other out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And before we knew it, we came to\x01",
            "be the Crossbell Business Owners'\x01",
            "Association.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2440")

    label("loc_238A")


    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association was\x01",
            "born right here on East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While the association has grown to cover all of\x01",
            "Crossbell, its roots were planted in this very street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2440")

    Jump("loc_27BC")

    label("loc_2445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_25D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255F")

    ChrTalk(
        0xFE,
        (
            "I have arrangements to meet with\x01",
            "an old friend of mine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An old merchant friend, mind you.\x01",
            "Now that we've retired, we like to engage\x01",
            "in the occasional friendly debate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho. Passion runs deep within the\x01",
            "veins of East Street merchants!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25CD")

    label("loc_255F")


    ChrTalk(
        0xFE,
        (
            "I have arrangements to meet with\x01",
            "an old friend of mine today. I think\x01",
            "it's about time I start preparing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25CD")

    Jump("loc_27BC")

    label("loc_25D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_27BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2736")

    ChrTalk(
        0xFE,
        (
            "While I may be the chairman of the Business\x01",
            "Owners' Association now, I ran my own stall\x01",
            "on the streets back when I was a young lad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd wager the connections I've fostered since\x01",
            "my early days have saved me numerous times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't hesitate to come to me with your issues.\x01",
            "It'd be my pleasure to work as your adviser!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27BC")

    label("loc_2736")


    ChrTalk(
        0xFE,
        (
            "Meeting you must be the work of fate,\x01",
            "so if you have any problems, come to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It'd be my pleasure to work as your adviser!\x02",
    )

    CloseMessageWindow()

    label("loc_27BC")

    TalkEnd(0xFE)
    Return()

    # Function_4_399 end

    def Function_5_27C0(): pass

    label("Function_5_27C0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2854")
    Jump("loc_289E")

    label("loc_2854")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2874")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_289E")

    label("loc_2874")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2894")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_289E")

    label("loc_2894")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_289E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C3")

    ChrTalk(
        0xFE,
        "It seems the diet has finally adjourned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only heard a rumor of the final budget,\x01",
            "but it sounded fairly reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Imperial Faction kept opposing the Republican\x01",
            "Faction, while Mayor MacDowell fought bravely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2A56")

    label("loc_29C3")


    ChrTalk(
        0xFE,
        "It seems the diet has finally adjourned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering our current faction-based system,\x01",
            "Mayor MacDowell fought bravely to keep the peace.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A56")

    Jump("loc_2C33")

    label("loc_2A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB7")

    ChrTalk(
        0xFE,
        (
            "Thanks to the IBC, Crossbell boasts\x01",
            "the continent's largest international bank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. None of the merchants' achievements\x01",
            "even compare to the IBC's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC has always been helmed by\x01",
            "intelligent CEOs who possess great\x01",
            "intuition and perseverance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us, the IBC is one of the many\x01",
            "prides of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2C33")

    label("loc_2BB7")


    ChrTalk(
        0xFE,
        "The IBC is the world's largest international bank.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's safe to say that it's one of\x01",
            "Crossbell's prides and joys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C33")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_27C0 end

    def Function_6_2C3B(): pass

    label("Function_6_2C3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E55")
    TurnDirection(0xFE, 0x101, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Oh, dear. We meet again.\x01",
            "If I recall correctly, we sat across from\x01",
            "each other on the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FO-Oh! You're the kind lady from back then.\x02\x03",
            "That's right. You said your house was on\x01",
            "East Street. This must be it, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember how you offered\x01",
            "to carry our luggage for us. You're an\x01",
            "admirable man for your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way, my husband is upstairs,\x01",
            "if you'd like to talk to him. I'm sure he'd\x01",
            "be pleased to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSure, I'd be happy to.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 5)
    Jump("loc_4D9E")

    label("loc_2E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(
        0xFE,
        (
            "Now, dear, don't lose your breath\x01",
            "with all of this politics talk.\x01",
            "Hurry and eat up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_304F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FBB")

    ChrTalk(
        0xFE,
        (
            "I've heard rumors from merchants that\x01",
            "many of the traders they've been\x01",
            "negotiating with have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Surely it can't be coincidence, right?\x01",
            "Maybe they've all left to take their\x01",
            "business to other foreign markets?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_304A")

    label("loc_2FBB")


    ChrTalk(
        0xFE,
        (
            "I've heard from the merchants that\x01",
            "they're generally punctual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The fact that they've all gone and\x01",
            "disappeared is peculiar, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304A")

    Jump("loc_4D9E")

    label("loc_304F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3104")

    ChrTalk(
        0xFE,
        (
            "My husband is always fussing about\x01",
            "what is going on in the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why, if the latest Crossbell\x01",
            "Times isn't delivered, he gets\x01",
            "all restless and unruly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_3104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_32F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323C")

    ChrTalk(
        0xFE,
        (
            "Look at my husband. He can't\x01",
            "take his eyes away from that\x01",
            "newspaper, can he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter the year, he always gets\x01",
            "like this while the diet is in session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't want to be forced to hear\x01",
            "constant barrages of political stories,\x01",
            "it's best not to get too close to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32F2")

    label("loc_323C")


    ChrTalk(
        0xFE,
        (
            "My husband ALWAYS gets like\x01",
            "this, no matter the year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't want to be forced to hear\x01",
            "constant barrages of political stories,\x01",
            "it's best not to get too close to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F2")

    Jump("loc_4D9E")

    label("loc_32F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_3922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3679")

    ChrTalk(
        0xFE,
        (
            "Oh, what do we have here?\x01",
            "What an adorable little visitor\x01",
            "you've brought today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FHi, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, isn't she just full of energy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThis cute bundle of joy is KeA. The SSS\x01",
            "will be looking after her for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh? Well, I'm sure you have your reasons.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Oh, I have an idea! Take this with you,\x01",
            "KeA. Okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We used to sell liquor, so this is about\x01",
            "as much juice as we have.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1CF, 1)

    ChrTalk(
        0x153,
        "#1105FWow, can I really have this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course you can, sweetie! It'll perk you\x01",
            "right up when you're tired.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35E0")

    ChrTalk(
        0x102,
        (
            "#0100FShow the nice lady your good manners\x01",
            "and thank her, KeA.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_35E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3620")

    ChrTalk(
        0x103,
        "#0200FWe appreciate your hospitality.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3656")

    label("loc_3620")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3656")

    ChrTalk(
        0x104,
        "#0300FHaha. Appreciate the gift.\x02",
    )

    CloseMessageWindow()

    label("loc_3656")


    ChrTalk(
        0x153,
        "#1109FThanks, Granny!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_391D")

    label("loc_3679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3882")

    ChrTalk(
        0xFE,
        (
            "Oh, that reminds me... Well, if it's\x01",
            "you guys, I'm sure you've already heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, there was some big hullabaloo\x01",
            "over at Mishelam on the last day of the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard some monsters appeared in the\x01",
            "Mishelam Center, but unfortunately,\x01",
            "I don't know all the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope no poor souls were harmed during\x01",
            "the attacks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHahaha...\x01",
            "(It looks like the coverage restrictions have prevented\x01",
            "most of the details from getting out...for now.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_391D")

    label("loc_3882")


    ChrTalk(
        0xFE,
        (
            "You would think that monsters appearing in\x01",
            "Mishelam would be a huge story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose it's entirely possible that it's\x01",
            "just an overblown rumor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_391D")

    Jump("loc_3BB4")

    label("loc_3922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CF")

    ChrTalk(
        0xFE,
        (
            "Oh, what do we have here?\x01",
            "What an adorable little visitor\x01",
            "you've brought today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to relax here, as my\x01",
            "husband's already back from work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_3BB4")

    label("loc_39CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B19")

    ChrTalk(
        0xFE,
        (
            "Apparently, there was some big hullabaloo\x01",
            "over at Mishelam on the last day of the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard some monsters appeared in the\x01",
            "Mishelam Center, but unfortunately, I don't\x01",
            "know the details of what happened after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't heard much for conversation\x01",
            "regarding the incident, either.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BB4")

    label("loc_3B19")


    ChrTalk(
        0xFE,
        (
            "You would think that monsters appearing in\x01",
            "Mishelam would be a huge story...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose it's entirely possible that it's\x01",
            "just an overblown rumor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB4")

    Jump("loc_4D9E")

    label("loc_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3C36")

    ChrTalk(
        0xFE,
        "Oh, are you all leaving already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take care out there, everyone. The\x01",
            "city is awfully congested today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3D8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBA")

    ChrTalk(
        0xFE,
        (
            "Roy and Meiling have matured\x01",
            "so much recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They could have just stayed at\x01",
            "our place today.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3D88")

    label("loc_3CBA")


    ChrTalk(
        0xFE,
        (
            "It's hard to describe the joy I feel when I'm able\x01",
            "to see my grandchildren every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll have my grandchildren stay over tonight\x01",
            "so they can spend some quality time with us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D88")

    Jump("loc_4D9E")

    label("loc_3D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E15")

    ChrTalk(
        0xFE,
        "The big parade is today, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was thinking about preparing\x01",
            "something refreshing to drink...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3EB8")

    label("loc_3E15")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll make enough for the members\x01",
            "of the Business Owners' Association as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much time passes,\x01",
            "those people will always be spoiled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB8")

    Jump("loc_4D9E")

    label("loc_3EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_401A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9A")

    ChrTalk(
        0xFE,
        (
            "My husband is at the Business Owners'\x01",
            "Association tent today as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think he's worried about some of the junior\x01",
            "members... Not that he'd ever admit it.\x01",
            "Utterly hopeless, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4015")

    label("loc_3F9A")


    ChrTalk(
        0xFE,
        (
            "I'll have to bring him a delicious\x01",
            "boxed lunch later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he's engrossed in negotiations,\x01",
            "as he usually is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4015")

    Jump("loc_4D9E")

    label("loc_401A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4109")

    ChrTalk(
        0xFE,
        (
            "My husband has already left,\x01",
            "if you're looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He had a meeting at the Business Owners' Association.\x01",
            "The Anniversary Festival has them in a tizzy, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's fairly energetic\x01",
            "for his age, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_4109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_42F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4240")

    ChrTalk(
        0xFE,
        "While we're on the topic of the IBC...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe Mr. Crois was good friends\x01",
            "with Mayor MacDowell's son-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mayor's son-in-law was a politician\x01",
            "a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to recall them both having daughters.\x01",
            "I imagine those two girls are as\x01",
            "close as sisters.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_42F1")

    label("loc_4240")


    ChrTalk(
        0xFE,
        (
            "I believe Mr. Crois is good friends\x01",
            "with Mayor MacDowell's son-in-law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I seem to recall them both having daughters.\x01",
            "I imagine those two girls are as\x01",
            "close as sisters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42F1")

    Jump("loc_4D9E")

    label("loc_42F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_44A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442A")

    ChrTalk(
        0xFE,
        (
            "Crossbell's newest bracer duo is always\x01",
            "running around taking care of requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I recall correctly, their names were\x01",
            "Estelle and Joshua... They're basically\x01",
            "celebrities here on East Street!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's so delightful watching young people\x01",
            "work so hard at what they love.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_44A1")

    label("loc_442A")


    ChrTalk(
        0xFE,
        (
            "Those new bracers seem to be trying\x01",
            "really hard to help out the locals. I think\x01",
            "I've even seen them in magazines!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A1")

    Jump("loc_4D9E")

    label("loc_44A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B6")

    ChrTalk(
        0xFE,
        (
            "Now that the Anniversary Festival is almost\x01",
            "here, the streets are buzzing with excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every store is eager to make mira during the festival.\x01",
            "We're also quite ready for it to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My heart is almost jumping in anticipation!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4654")

    label("loc_45B6")


    ChrTalk(
        0xFE,
        (
            "Now that the Anniversary Festival is almost\x01",
            "here, the streets are buzzing with excitement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This time of the year is always\x01",
            "an enjoyable experience.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4654")

    Jump("loc_4D9E")

    label("loc_4659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4742")

    ChrTalk(
        0xFE,
        (
            "My back has been killing me since this morning, so\x01",
            "I asked some of my merchant friends if they would\x01",
            "pick up my groceries for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess my husband's connections\x01",
            "come in handy occasionally, wouldn't you say?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D9E")

    label("loc_4742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488C")

    ChrTalk(
        0xFE,
        (
            "It's nice to see you again, but oh, my!\x01",
            "You look exhausted. What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FAhaha... Don't worry about us, we're fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FRight. We managed to survive.\x01",
            "Had we not taken that break, though...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_4884")

    ChrTalk(
        0x101,
        (
            "#0000FThank you for the lemonade, Mrs. Parla.\x01",
            "It definitely came in handy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4884")

    SetScenarioFlags(0x0, 1)
    Jump("loc_48FD")

    label("loc_488C")


    ChrTalk(
        0xFE,
        (
            "Well, if you get tired again, just let me know!\x01",
            "I'll gladly treat you to another tall glass of my\x01",
            "lemonade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FD")

    Jump("loc_4D9E")

    label("loc_4902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B64")

    ChrTalk(
        0xFE,
        (
            "What a nice group of youthful people\x01",
            "we've got here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you all going out on a trip?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYes, ma'am. We've got some business to\x01",
            "take care of at Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My, my, that's quite the journey.\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Oh, I have an idea. Why don't you take\x01",
            "this all with you?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x336),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x336, 1)

    ChrTalk(
        0x101,
        (
            "#0000FIsn't this the same iced lemonade you\x01",
            "gave me on the train?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed it is! Remember to drink some while\x01",
            "you're on the road if you feel dehydrated, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHaha. Roger that, madam.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 7)
    Jump("loc_4BB5")

    label("loc_4B64")


    ChrTalk(
        0xFE,
        (
            "Hurry along, now! You've got to get out\x01",
            "there while the day is still young!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB5")

    Jump("loc_4D9E")

    label("loc_4BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C81")

    ChrTalk(
        0xFE,
        (
            "The streets in the area can get a bit\x01",
            "too rowdy at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once you get used to it, you start to feel\x01",
            "a little lonely when it becomes quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't it ironic?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4CD6")

    label("loc_4C81")


    ChrTalk(
        0xFE,
        (
            "I start to feel a little lonely when it becomes\x01",
            "quiet outside. Isn't it ironic?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD6")

    Jump("loc_4D9E")

    label("loc_4CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4D9E")

    ChrTalk(
        0xFE,
        (
            "I love getting to know our\x01",
            "city's promising youths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're always welcome to come back here.\x01",
            "Just say the word, and I'll be sure to prepare\x01",
            "you something especially delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9E")

    TalkEnd(0xFE)
    Return()

    # Function_6_2C3B end

    SaveToFile()

Try(main)
