from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c045c.bin",                # FileName
        "c045c",                    # MapName
        "c045c",                    # Location
        0x0024,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 4, 0, 5],
    )

    BuildStringList((
        "c045c",                  # 0
        "Receptionist Kyle",      # 1
        "Doris",                  # 2
        "Aeron",                  # 3
        "Manager Leticia",        # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Kilika",                 # 8
    ))

    AddCharChip((
        "chr/ch07300.itc",                   # 00
        "chr/ch21800.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22300.itc",                   # 03
        "chr/ch25700.itc",                   # 04
        "chr/ch27500.itc",                   # 05
        "chr/ch27900.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   4,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   5,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(112779,  0,       57889,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(116599,  0,       58169,   225,  261,  0x0, 0,   3,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(155360,  0,       59509,   135,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(114040,  0,       5860,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  6,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_364",          # 03, 3
        "Function_4_38F",          # 04, 4
        "Function_5_3F4",          # 05, 5
        "Function_6_3F5",          # 06, 6
        "Function_7_3F9",          # 07, 7
        "Function_8_D91",          # 08, 8
        "Function_9_D95",          # 09, 9
        "Function_10_193D",        # 0A, 10
        "Function_11_1DDF",        # 0B, 11
        "Function_12_21FF",        # 0C, 12
        "Function_13_259B",        # 0D, 13
        "Function_14_27C4",        # 0E, 14
        "Function_15_2A7A",        # 0F, 15
        "Function_16_3226",        # 10, 16
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_338")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_2D8")

    label("loc_338")

    Return()

    # Function_1_2D8 end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_363")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_339")

    label("loc_363")

    Return()

    # Function_2_339 end

    def Function_3_364(): pass

    label("Function_3_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38E")
    OP_94(0xFE, 0x1C200, 0xDFAC, 0x1CB9C, 0xE8B2, 0x3E8)
    Sleep(300)
    Jump("Function_3_364")

    label("loc_38E")

    Return()

    # Function_3_364 end

    def Function_4_38F(): pass

    label("Function_4_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39D")
    Jump("loc_3F3")

    label("loc_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C6")
    SetChrPos(0xF, 63400, 0, 59930, 90)
    ClearChrFlags(0xF, 0x80)

    label("loc_3C6")

    Jump("loc_3F3")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D9")
    Jump("loc_3F3")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3F3")
    ClearChrFlags(0xF, 0x80)

    label("loc_3F3")

    Return()

    # Function_4_38F end

    def Function_5_3F4(): pass

    label("Function_5_3F4")

    Return()

    # Function_5_3F4 end

    def Function_6_3F5(): pass

    label("Function_6_3F5")

    Call(0, 7)
    Return()

    # Function_6_3F5 end

    def Function_7_3F9(): pass

    label("Function_7_3F9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F")

    ChrTalk(
        0xB,
        "Welcome to Hotel Millennium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We provide only the finest quality of\x01",
            "service at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We make for the perfect place to rest in Crossbell,\x01",
            "the entertainment capital of Zemuria!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_57F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FA")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D88")

    label("loc_5FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E")
    Jump("loc_D88")

    label("loc_60E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D88")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_733")

    ChrTalk(
        0xB,
        (
            "Now that we've reached the final day of the\x01",
            "festival, it is my sworn duty to bid farewell to\x01",
            "our guests while wearing the brightest smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We'll be waiting in anticipation for them to\x01",
            "do the honor of visiting us next time they're\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_854")

    ChrTalk(
        0xB,
        (
            "I heard the parade passing through\x01",
            "here earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm used to hearing the parade ever since\x01",
            "I was a child, so rehearing it always fills\x01",
            "me with a sense of nostalgia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While I may take on the role of a manager,\x01",
            "my blood will always be that of a true\x01",
            "Crossbellan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 4)), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(
        0xB,
        (
            "I am terribly sorry. I don't believe\x01",
            "he was in our lobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I make sure to greet all of our guests,\x01",
            "and I haven't seen him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B")

    label("loc_8EF")


    ChrTalk(
        0x101,
        (
            "#0000F(Yeah, this person might\x01",
            "know something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "Oh, he's such a cutie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My apologies, but I don't recall him\x01",
            "coming to our lobby before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThat's unfortunate. Thank you\x01",
            "for cooperating, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_A4B")

    Jump("loc_D88")

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B71")

    ChrTalk(
        0xB,
        (
            "I heard the parade passing through\x01",
            "here earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm used to hearing the parade ever since\x01",
            "I was a child, so rehearing it always fills\x01",
            "me with a sense of nostalgia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "While I may take on the role of a manager,\x01",
            "my blood will always be that of a true\x01",
            "Crossbellan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C2F")

    ChrTalk(
        0xB,
        (
            "Today's parade route will be passing\x01",
            "underneath our top floor's deluxe rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Our rooms are generally booked in\x01",
            "advance around this time, so a\x01",
            "vacancy is quite rare.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CD4")

    ChrTalk(
        0xB,
        (
            "There's supposedly an event going\x01",
            "on at City Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And not to brag, but many of the attendees\x01",
            "have reserved their hotel rooms with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D88")

    label("loc_CD4")


    ChrTalk(
        0xB,
        (
            "Our hotel has been massively popular\x01",
            "ever since the festival began.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And if I'm not mistaken, the Entertainment\x01",
            "District has built up quite the reputation\x01",
            "among tourists.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D88")

    Jump("loc_589")

    label("loc_D8D")

    TalkEnd(0xB)
    Return()

    # Function_7_3F9 end

    def Function_8_D91(): pass

    label("Function_8_D91")

    Call(0, 9)
    Return()

    # Function_8_D91 end

    def Function_9_D95(): pass

    label("Function_9_D95")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F03")

    ChrTalk(
        0x8,
        "Good day. Welcome to Hotel Millenium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you've currently booked a room with us,\x01",
            "then please contact the front reception\x01",
            "desk if you are in need of assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetScenarioFlags(0x4B, 4)

    label("loc_F03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1939")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F5E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7E")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1934")

    label("loc_F7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F92")
    Jump("loc_1934")

    label("loc_F92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1934")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(
        0x8,
        (
            "The hotel is emptying out now that the\x01",
            "festival is coming to its end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Feel free to book a room if you need\x01",
            "one. We have plenty of vacancies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1934")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_10CA")

    ChrTalk(
        0x8,
        (
            "A little worrying to hear about a lost\x01",
            "boy, wouldn't you say? I'll be sure\x01",
            "to keep an eye out for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1934")

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 5)), scpexpr(EXPR_END)), "loc_1190")

    ChrTalk(
        0x8,
        (
            "The district's been packed with tourists,\x01",
            "so I can't really say if I saw him or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can at least state with full confidence\x01",
            "that he is NOT a guest at this hotel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1361")

    label("loc_1190")


    ChrTalk(
        0x101,
        (
            "#0000F(This receptionist might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "A missing child? Pretty troubling.\x01",
            "Let me think for a sec...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm. Can't really state with full confidence\x01",
            "if I saw him or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Considering how packed it is outside,\x01",
            "everybody just sort of blends together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, fair enough. Thank you for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAA, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_1361")

    Jump("loc_1934")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1444")

    ChrTalk(
        0x8,
        (
            "Now that the Anniversary Festival is almost\x01",
            "over, many of the tourists are preparing to\x01",
            "return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We believe our quality of service will warrant\x01",
            "their continued patronage in the future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1541")

    label("loc_1444")


    ChrTalk(
        0x8,
        (
            "Miss Rouran informed me that she will be\x01",
            "leaving Crossbell in two days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I presume she'll be returning home the day\x01",
            "after the festival has concluded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We believe our quality of service will warrant\x01",
            "her continued patronage in the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1541")

    Jump("loc_1934")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1688")

    ChrTalk(
        0x8,
        (
            "A lady by the name of Miss Rouran is\x01",
            "currently staying with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe she had a ticket for Arc en Ciel,\x01",
            "so she's out for the day to enjoy the show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She's supposedly involved in the entertainment\x01",
            "industry. In all honesty, I'm not too shocked.\x01",
            "Take a look at her. She's absolutely stunning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1934")

    label("loc_1688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1760")

    ChrTalk(
        0x8,
        (
            "We strive to provide the finest service, so we\x01",
            "make it a point to remember each and every\x01",
            "one of our guests' names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'd be surprised by how many famous\x01",
            "foreign dignitaries have stayed here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1934")

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_184D")

    ChrTalk(
        0x8,
        (
            "I mistook one of our guests for another one\x01",
            "staying here... Keep it a secret from the\x01",
            "manager, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A lot of people came and went from the\x01",
            "hotel over the last day, so it seems like\x01",
            "I still have a ways to go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1934")

    label("loc_184D")


    ChrTalk(
        0x8,
        "Did you forget something, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh. Excuse me, sir. To think I would\x01",
            "confuse one guest with another...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A lot of people coming and going from\x01",
            "the hotel over the last day, so it seems\x01",
            "like I still have a ways to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1934")

    Jump("loc_F0D")

    label("loc_1939")

    TalkEnd(0x8)
    Return()

    # Function_9_D95 end

    def Function_10_193D(): pass

    label("Function_10_193D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A03")

    ChrTalk(
        0xA,
        (
            "Once a guest has checked out, we must\x01",
            "ready the room as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We're tasked with cleaning the rooms with\x01",
            "haste so that our guests do not have to\x01",
            "wait on us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDB")

    label("loc_1A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A6B")

    ChrTalk(
        0xA,
        (
            "Doris managed to clean that room\x01",
            "properly this time around. Good.\x01",
            "Very good, indeed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDB")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B5A")

    ChrTalk(
        0xA,
        (
            "Our rooms must look flawless in order to give\x01",
            "our patrons the true Hotel Millennium experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Anniversary Festival is no good reason to\x01",
            "ease up on the work. I'll have to pay close\x01",
            "attention to Doris.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C2F")

    label("loc_1B5A")


    ChrTalk(
        0xA,
        (
            "The hallways are looking a little sloppier\x01",
            "than they normally do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our rooms must look flawless in order to give\x01",
            "our patrons the true Hotel Millennium experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I must make this clear to Doris.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C2F")

    Jump("loc_1DDB")

    label("loc_1C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D26")

    ChrTalk(
        0xA,
        (
            "People who tend to stay at the hotel in Mishelam\x01",
            "during the Anniversary Festival are generally\x01",
            "on the wealthier side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Such a feat would be nigh impossible for\x01",
            "an ordinary citizen like myself.\x01",
            "I WISH I could... Hahaha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDB")

    label("loc_1D26")


    ChrTalk(
        0xA,
        (
            "Our deluxe suites are fully booked during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They typically remain vacant, but special occasions\x01",
            "like the Anniversary Festival tend to change that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDB")

    TalkEnd(0xFE)
    Return()

    # Function_10_193D end

    def Function_11_1DDF(): pass

    label("Function_11_1DDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E30")

    ChrTalk(
        0x9,
        (
            "Okay, let's see... Gotta replace the bath\x01",
            "set, and then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FB")

    label("loc_1E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(
        0x9,
        (
            "Aeron pointed out how poorly I've been\x01",
            "cleaning the rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I finally managed to redo it all...\x01",
            "I suppose just because I'm busy\x01",
            "doesn't mean I should cut corners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FB")

    label("loc_1EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F9D")

    ChrTalk(
        0x9,
        (
            "*sigh* I can feel the fatigue starting\x01",
            "to set in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've still got one more day of the Anniversary\x01",
            "Festival to get through. Here's to hoping\x01",
            "I'll survive...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FB")

    label("loc_1F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2067")

    ChrTalk(
        0x9,
        (
            "I need to fold the sheets for this room, bring\x01",
            "them over to the linen closet, and then make\x01",
            "the beds for this other room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Argh, I need to hurry! The guests\x01",
            "are returning soon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FB")

    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_20F3")

    ChrTalk(
        0x9,
        (
            "I thankfully finished making all the beds\x01",
            "on this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anybody that gives me a tip sure knows\x01",
            "how to make my day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FB")

    label("loc_20F3")


    ChrTalk(
        0x9,
        (
            "I thankfully finished making all the beds\x01",
            "on this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "People these days have been leaving tips\x01",
            "under their pillow. I suppose it's a popular\x01",
            "new fad...not that I'm complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "P-Pardon me!\x01",
            "That was unbecoming of me to say\x01",
            "in front of a guest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_21FB")

    TalkEnd(0xFE)
    Return()

    # Function_11_1DDF end

    def Function_12_21FF(): pass

    label("Function_12_21FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2277")

    ChrTalk(
        0xC,
        (
            "Arc en Ciel's show just ended, so I\x01",
            "plan to relax with my daughter for\x01",
            "the rest of this fine day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2597")

    label("loc_2277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2312")

    ChrTalk(
        0xC,
        (
            "I watched Arc en Ciel's show with my\x01",
            "daughter earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She was so impressed by them that\x01",
            "she's been in a daze the whole day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2597")

    label("loc_2312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_23DB")

    ChrTalk(
        0xC,
        (
            "I'm going to watch Arc en Ciel perform\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My daughter doesn't seem to be interested,\x01",
            "but I'm sure she'll come to understand their\x01",
            "magnificence after having watched them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2597")

    label("loc_23DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_247A")

    ChrTalk(
        0xC,
        (
            "There's nothing better than watching Arc en Ciel\x01",
            "perform. I hope to savor the bewilderment on\x01",
            "my daughter's face once she experiences them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2597")

    label("loc_247A")


    ChrTalk(
        0xC,
        (
            "We came to enjoy the Anniversary Festival,\x01",
            "and getting to watch Arc en Ciel perform\x01",
            "is the icing on the cake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's been three long years since I last watched\x01",
            "Arc en Ciel perform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Now that they've announced a new production,\x01",
            "I brought my daughter to watch it with me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2597")

    TalkEnd(0xFE)
    Return()

    # Function_12_21FF end

    def Function_13_259B(): pass

    label("Function_13_259B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2629")

    ChrTalk(
        0xD,
        (
            "I'm going to look around the Entertainment\x01",
            "District with my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I wonder if I can find any Ilya merchandise...\x02",
    )

    CloseMessageWindow()
    Jump("loc_27C0")

    label("loc_2629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2676")

    ChrTalk(
        0xD,
        "Ohhh, Lady Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "*sigh* She was absolutely stunning!\x02",
    )

    CloseMessageWindow()
    Jump("loc_27C0")

    label("loc_2676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2726")

    ChrTalk(
        0xD,
        (
            "Crossbell's Entertainment District is amazing!\x01",
            "It has all kinds of fun things to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I'll go out and have some more fun after\x01",
            "a bit of a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C0")

    label("loc_2726")


    ChrTalk(
        0xD,
        (
            "My father keeps rambling about how amazing\x01",
            "Arc en Ciel is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's just a play... How amazing could it be?\x01",
            "I doubt it's going to be life-changing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C0")

    TalkEnd(0xFE)
    Return()

    # Function_13_259B end

    def Function_14_27C4(): pass

    label("Function_14_27C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(
        0xE,
        (
            "Well, I think I've learned a good lesson here.\x01",
            "Going to a casino is sure to make you lose\x01",
            "your mira in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Better watch my wallet. It's too dangerous\x01",
            "in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A76")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2938")

    ChrTalk(
        0xE,
        "I tried my luck at the casino yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Boy, what a thrill that was... I think I can\x01",
            "finally relate to all of the people who\x01",
            "get hooked on it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A76")

    label("loc_2938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29C4")

    ChrTalk(
        0xE,
        (
            "It was pretty painful to get to Crossbell, so\x01",
            "I figured, why not live a little?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Maybe I'll try my hand at gambling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A76")

    label("loc_29C4")


    ChrTalk(
        0xE,
        (
            "Thank Aidios I was able to reserve a room\x01",
            "at such an elegant hotel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If I'm being honest, I wasn't looking forward\x01",
            "to staying at that dingy old inn over on\x01",
            "East Street.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A76")

    TalkEnd(0xFE)
    Return()

    # Function_14_27C4 end

    def Function_15_2A7A(): pass

    label("Function_15_2A7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2BA6")

    ChrTalk(
        0xF,
        (
            "#3400FAn Arc en Ciel tour of Calvard... An\x01",
            "attractive prospect, wouldn't you say?\x02\x03",
            "Should it happen, it's inevitable that the\x01",
            "troupe's popularity would blaze across\x01",
            "the country.\x02\x03",
            "Will they realize that, though? Who can say?\x01",
            "All I've done is lay the offer on the table.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5C")

    label("loc_2BA6")


    ChrTalk(
        0xF,
        (
            "#3400FI will admit that they're just as\x01",
            "spectacular as I've been told.\x02\x03",
            "The performance left me speechless.\x01",
            "And I trust that you will believe me\x01",
            "when I say that hardly happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou sound like every other person that just\x01",
            "saw Arc en Ciel for the first time. So, were\x01",
            "you able to make an appointment with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400FQuite easily. I laid my offer at their feet. I now\x01",
            "have to wait and see if they decline or accept.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_2D5C")

    Jump("loc_3222")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 5)), scpexpr(EXPR_END)), "loc_2EE9")

    ChrTalk(
        0xF,
        (
            "#3400FThere are many matters I still must investigate\x01",
            "for my job now.\x02\x03",
            "How I proceed will entirely depend\x01",
            "on how they respond to my offer.\x02\x03",
            "There is much to think about... After all,\x01",
            "being prepared for any situation trumps\x01",
            "one's own ability every time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(It's like she's playing a game of chess. I wouldn't\x01",
            "want to get on her bad side, that's for sure.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3222")

    label("loc_2EE9")


    ChrTalk(
        0xF,
        (
            "#3400FHello there. I don't believe that I had the\x01",
            "opportunity to thank you for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, Kilika? Not a problem. We were just doing\x01",
            "our jobs. So, are you staying in this hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FFancy place for an equally fancy lady.\x01",
            "Makes sense to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FSo this is the power of show business...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400FOh, don't misunderstand. I couldn't\x01",
            "care less about the quality of my lodgings.\x02\x03",
            "It just so happens that this is the ideal location\x01",
            "for my business dealings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOh, of course. It's right beside Arc en Ciel,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400FRight you are. Though, I will admit the view\x01",
            "is an added benefit.\x02\x03",
            "I have no doubt that tomorrow's performance will\x01",
            "be as riveting as their last one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I don't think you have to worry about\x01",
            "anything there. It was nice seeing you again,\x01",
            "Kilika.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB7, 5)

    label("loc_3222")

    TalkEnd(0xFE)
    Return()

    # Function_15_2A7A end

    def Function_16_3226(): pass

    label("Function_16_3226")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32EB")
    OP_29(0x46, 0x1, 0x2)

    ChrTalk(
        0x101,
        (
            "#0000F(All right, that's a wrap on the Entertainment\x01",
            "District's investigation.)\x02\x03",
            "(Looks like the Back Alley is next...\x01",
            "Let's continue the investigation there!)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_32EB")

    Return()

    # Function_16_3226 end

    SaveToFile()

Try(main)
