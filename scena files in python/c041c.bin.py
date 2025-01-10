from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c041c.bin",                # FileName
        "c041c",                    # MapName
        "c041c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 1, 0, 2],
    )

    BuildStringList((
        "c041c",                  # 0
        "Ilya",                   # 1
        "Rixia",                  # 2
        "Manager Balsamo",        # 3
        "Receptionist Rowland",   # 4
        "Eugene",                 # 5
        "Theodor",                # 6
        "Plie",                   # 7
        "Selene",                 # 8
        "Karelia",                # 9
        "Troupe Leader Avan",     # 10
        "Guest",                  # 11
        "Guest",                  # 12
        "Guest",                  # 13
        "Guest",                  # 14
        "Guest",                  # 15
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch25800.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch28700.itc",                   # 05
        "chr/ch28800.itc",                   # 06
        "chr/ch36900.itc",                   # 07
        "chr/ch37000.itc",                   # 08
        "chr/ch27500.itc",                   # 09
    ))

    DeclNpc(-91550,  0,       1679,    180,  405,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-90209,  0,       1070,    225,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-2250,   2500,    15000,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(6969,    0,       3480,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-91199,  0,       -870,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-121580, 0,       1669,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-121709, 0,       3109,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-91300,  0,       4960,    90,   389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-121709, 0,       3109,    90,   277,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3240,   0,       4179,    180,  389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 25,  9.0,                   14.0,                  2.5,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -4.5,                  -2.799999713897705,    -0.4999999701976776,   1.0])

    DeclActor(6500,    0,       3480,    1200,    6970,    1500,    3480,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4EE",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_A1D",          # 04, 4
        "Function_5_A21",          # 05, 5
        "Function_6_DFD",          # 06, 6
        "Function_7_ED8",          # 07, 7
        "Function_8_12C8",         # 08, 8
        "Function_9_15CF",         # 09, 9
        "Function_10_177D",        # 0A, 10
        "Function_11_18DF",        # 0B, 11
        "Function_12_19AF",        # 0C, 12
        "Function_13_1A70",        # 0D, 13
        "Function_14_1BB5",        # 0E, 14
        "Function_15_1E77",        # 0F, 15
        "Function_16_215B",        # 10, 16
        "Function_17_2483",        # 11, 17
        "Function_18_26C4",        # 12, 18
        "Function_19_29C2",        # 13, 19
        "Function_20_2C03",        # 14, 20
        "Function_21_3BE5",        # 15, 21
        "Function_22_3C2B",        # 16, 22
        "Function_23_3C71",        # 17, 23
        "Function_24_3C9D",        # 18, 24
        "Function_25_3D42",        # 19, 25
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_430")
    Event(0, 19)
    Jump("loc_4A7")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_4A7")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_454")
    Event(0, 18)
    Jump("loc_4A7")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46A")
    Event(0, 17)
    Jump("loc_4A7")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_495")
    SetChrPos(0xA, -3460, 0, 2440, 0)
    ClearChrFlags(0x11, 0x80)

    label("loc_495")

    Jump("loc_4A7")

    label("loc_49A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    Event(0, 16)

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4ED")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x10, -90300, 0, 4960, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_4ED")
    SetChrFlags(0x9, 0x10)

    label("loc_4ED")

    Return()

    # Function_1_404 end

    def Function_2_4EE(): pass

    label("Function_2_4EE")

    OP_1B(0x3, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_510")
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x3, 0x0, 0x18)

    label("loc_510")

    Return()

    # Function_2_4EE end

    def Function_3_511(): pass

    label("Function_3_511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_69B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5A9")

    ChrTalk(
        0xA,
        (
            "I don't believe he's hiding\x01",
            "inside of the theater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll be sure to inform the police\x01",
            "immediately if we spot him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696")

    label("loc_5A9")


    ChrTalk(
        0xA,
        (
            "I've heard everything, Detective Bannings.\x01",
            "You're searching for a young boy, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't believe he's hiding\x01",
            "inside of the theater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please, don't worry.\x01",
            "We'll be sure to inform the police\x01",
            "immediately if we spot him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_696")

    Jump("loc_A19")

    label("loc_69B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE")

    ChrTalk(
        0xFE,
        (
            "To think that the stalker\x01",
            "was a young girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we're currently processing\x01",
            "Ilya's sudden request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't take issue with her joining the\x01",
            "troupe, if Ilya insists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, Rixia joined us under\x01",
            "strikingly similar circumstances.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8B1")

    label("loc_7BE")


    ChrTalk(
        0xFE,
        (
            "Ilya waltzed in here one day,\x01",
            "dragging Rixia along with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The troupe leader was initially\x01",
            "getting fed up with her mistakes,\x01",
            "but Rixia eventually began to shine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya's eyes never make a mistake.\x01",
            "In fact, they're a huge help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1")

    Jump("loc_A19")

    label("loc_8B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95F")

    ChrTalk(
        0xFE,
        "Have you heard the news?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ilya is having a bit of an issue regarding\x01",
            "a stalker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Could I ask you all\x01",
            "for your help?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_98E")

    label("loc_95F")


    ChrTalk(
        0xFE,
        (
            "*sigh* Could I ask you all\x01",
            "for your help?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E")

    Jump("loc_A19")

    label("loc_993")


    ChrTalk(
        0xA,
        (
            "Oh, hello everyone.\x01",
            "Welcome to Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Are you here to visit Ilya? She's in\x01",
            "the hall with the troupe leader\x01",
            "and Rixia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    TalkEnd(0xFE)
    Return()

    # Function_3_511 end

    def Function_4_A1D(): pass

    label("Function_4_A1D")

    Call(0, 5)
    Return()

    # Function_4_A1D end

    def Function_5_A21(): pass

    label("Function_5_A21")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_ADB")

    ChrTalk(
        0xB,
        (
            "We conducted a search and were unable to\x01",
            "find the little boy you were looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'll pay closer attention after the\x01",
            "evening performance has begun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBB")

    label("loc_ADB")


    ChrTalk(
        0xB,
        (
            "I kept a close eye on all of the\x01",
            "customers that came through the lobby...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I believe any child that walked through our doors\x01",
            "was accompanied by their guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm really sorry I couldn't be any more help.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_BBB")

    Jump("loc_DF9")

    label("loc_BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CA8")

    ChrTalk(
        0xB,
        (
            "*sigh* I'm not sure how it happened, but\x01",
            "the troupe is apparently taking on\x01",
            "another member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "How does Ilya go and scout out new talent\x01",
            "while she has to worry about a stalker?\x01",
            "She has to be a genius, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D5C")

    ChrTalk(
        0xB,
        (
            "Oh, by the way. I noticed Ilya and Rixia\x01",
            "speaking with the troupe leader after\x01",
            "last night's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't help but wonder what they were\x01",
            "discussing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_D5C")


    ChrTalk(
        0xB,
        "Today's actually Arc en Ciel's day off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That didn't stop Ilya and Rixia\x01",
            "from showing up for practice,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Those two live for the arts.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_DF9")

    TalkEnd(0xB)
    Return()

    # Function_5_A21 end

    def Function_6_DFD(): pass

    label("Function_6_DFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_ED1")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "#1700FRixia's finally getting a hang of the\x01",
            "performance's tempo.\x02\x03",
            "#1709FWe just need to keep up this pace. It's time to\x01",
            "go full force for this last bit of rehearsal!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_ED4")

    label("loc_ED1")

    Call(0, 7)

    label("loc_ED4")

    TalkEnd(0xFE)
    Return()

    # Function_6_DFD end

    def Function_7_ED8(): pass

    label("Function_7_ED8")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Rixia's immense rate of improvement\x01",
            "has been remarkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1709FYeah, no kidding. I'd say today's\x01",
            "performance was our magnum opus.\x02\x03",
            "#1702FIt helps that everybody's refined the\x01",
            "heck outta their acting. Not only that...\x02\x03",
            "...but doesn't it seem like Rixia's grasped\x01",
            "the performance's tempo, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1809FPerforming the play twice in one day was much\x01",
            "more demanding than I had anticipated...\x02\x03",
            "#1802FBut, I agree. Our last performance felt\x01",
            "amazing. I feel much lighter on my feet\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1709FYes! That's it, Rixia! Make sure you\x01",
            "treasure that feeling!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(
        0x160,
        (
            "#3305F(This is the famed Ilya Platiere?\x01",
            "Hmm, she doesn't seem too special.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F(Not special?)\x02\x03",
            "#0000F(You know people consider her to be\x01",
            "a genius, right? Though, I guess that\x01",
            "only applies to her stage presence.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3304F(If you insist. What an interesting 'genius.')\x02\x03",
            "#3302F(That Eastern girl has more to her\x01",
            "than she lets on...)\x02\x03",
            "(Perhaps I should watch an\x01",
            "Arc en Ciel play to observe her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B8")

    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_7_ED8 end

    def Function_8_12C8(): pass

    label("Function_8_12C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 4)), scpexpr(EXPR_END)), "loc_13BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13B4")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "#1810FTomorrow's the last day of\x01",
            "the Anniversary Festival.\x02\x03",
            "#1804FOkay. I'd better do what I can\x01",
            "to maintain peak physical condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(Poor girl. She must be exhausted.)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_13B7")

    label("loc_13B4")

    Call(0, 7)

    label("loc_13B7")

    Jump("loc_15CB")

    label("loc_13BC")


    ChrTalk(
        0x9,
        (
            "#1805FOh, hello, Lloyd.\x02\x03",
            "Have you had any luck\x01",
            "finding that boy?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_14AB")

    ChrTalk(
        0x101,
        (
            "#0006FNot yet, unfortunately.\x02\x03",
            "#0000FI'm sure we'll find him in no time once\x01",
            "we've gathered all of the testimonies.\x01",
            "I wouldn't worry about it, Rixia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1519")

    label("loc_14AB")


    ChrTalk(
        0x101,
        (
            "#0006FNo, not yet...\x02\x03",
            "#0000FWe haven't finished the investigation\x01",
            "yet, so don't let it worry you, Rixia.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1519")


    ChrTalk(
        0x9,
        (
            "#1806FOkay, if you say so.\x02\x03",
            "#1810FI'm so sorry, Lloyd. I would have been able\x01",
            "to help you with the search if I didn't have\x01",
            "a performance scheduled so soon...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0xB2, 4)

    label("loc_15CB")

    TalkEnd(0xFE)
    Return()

    # Function_8_12C8 end

    def Function_9_15CF(): pass

    label("Function_9_15CF")

    TalkBegin(0xFE)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_165B")

    ChrTalk(
        0xC,
        (
            "I must say, this bitter green tea the\x01",
            "Republic exports is most exquisite.\x01",
            "I feel the fatigue dissipating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176D")

    label("loc_165B")


    ChrTalk(
        0xC,
        "*sips*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Aaaah... Oh, marvelous.\x01",
            "I feel rejuvenated already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Fantastic job, Rixia. I can always count\x01",
            "on you Easterners to have interesting\x01",
            "herbal remedies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1704FWhoa, no kidding. This is great stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1809FThank you. I'm glad you're enjoying it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_176D")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_9_15CF end

    def Function_10_177D(): pass

    label("Function_10_177D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 6)), scpexpr(EXPR_END)), "loc_17CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17C5")

    ChrTalk(
        0xD,
        "Our troupe maintains a seniority system.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17C8")

    label("loc_17C5")

    Call(0, 12)

    label("loc_17C8")

    Jump("loc_18DB")

    label("loc_17CD")


    ChrTalk(
        0xD,
        "The girls are looking for some kid, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You want me in on the search, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FI think we're good already, but thanks.\x01",
            "I appreciate the offer.\x02\x03",
            "I think we'll find him in due time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yeah? All right, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I hope you find him soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 6)

    label("loc_18DB")

    TalkEnd(0xFE)
    Return()

    # Function_10_177D end

    def Function_11_18DF(): pass

    label("Function_11_18DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 7)), scpexpr(EXPR_END)), "loc_1935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(
        0xE,
        (
            "*munch* *munch*\x01",
            "Mmm... I live for pastries. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1930")

    label("loc_192D")

    Call(0, 12)

    label("loc_1930")

    Jump("loc_19AB")

    label("loc_1935")


    ChrTalk(
        0xE,
        (
            "Oh, you mean the little boy\x01",
            "Ilya was in a huff about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm sorry, but I don't think\x01",
            "I've seen him around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 7)

    label("loc_19AB")

    TalkEnd(0xFE)
    Return()

    # Function_11_18DF end

    def Function_12_19AF(): pass

    label("Function_12_19AF")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)

    ChrTalk(
        0xD,
        (
            "I think you should calm down on the\x01",
            "pastries after you've changed, Plie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Theodor, my dear... Mind your\x01",
            "own damn business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "My apologies, madame.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_19AF end

    def Function_13_1A70(): pass

    label("Function_13_1A70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1ADC")

    ChrTalk(
        0xF,
        (
            "I-I can't believe I got praised by Ilya.\x01",
            "This is the best day of my life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "... ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BB1")

    label("loc_1ADC")


    ChrTalk(
        0xF,
        "Hey, do you mind hearing me out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "You're not going to believe this! Ilya\x01",
            "finally praised my acting today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "This is the first time Lad-- Ahem!\x01",
            "I mean...Ilya, has praised me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1BB1")

    TalkEnd(0xFE)
    Return()

    # Function_13_1A70 end

    def Function_14_1BB5(): pass

    label("Function_14_1BB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1DAB")
    OP_4B(0x10, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1C4C")

    ChrTalk(
        0x10,
        (
            "Anyhow, you'll have to bear with using\x01",
            "this one for the night scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Your usual one is getting patched up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D9E")

    label("loc_1C4C")


    ChrTalk(
        0x10,
        (
            "Okay, let's take a look...\x01",
            "Yep. You pull it off well.\x01",
            "How is it? Any discomfort?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "No, this'll do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It was a loose costume to\x01",
            "begin with, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "Y-Yeah, it was. I figured making it\x01",
            "loose would help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Don't worry about it! It's a wonderful\x01",
            "costume, loose or not!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1D9E")

    OP_4C(0x10, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_1E73")

    label("loc_1DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(
        0x10,
        (
            "It's our duty to clean the building on\x01",
            "days we don't hold any performances.\x01",
            "Sheesh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E73")

    label("loc_1E14")


    ChrTalk(
        0x10,
        (
            "You can't just keep eating pastries\x01",
            "in here, Plie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Into the trash they go!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_1E73")

    TalkEnd(0xFE)
    Return()

    # Function_14_1BB5 end

    def Function_15_1E77(): pass

    label("Function_15_1E77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2049")

    ChrTalk(
        0xFE,
        (
            "Hey, I heard you guys managed to\x01",
            "settle everything in one piece!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, fortunately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe situation did proceed\x01",
            "in an unexpected manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, no kidding. Ilya's always been\x01",
            "the forceful type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reminds me of back when Rixia\x01",
            "joined the troupe, and Ilya...\x01",
            "*endlessly grumbling*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FHah. Gone full chatterbox mode, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThe troupe leader seems to\x01",
            "frequently butt heads with Ilya...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 2)
    Jump("loc_2157")

    label("loc_2049")


    ChrTalk(
        0xFE,
        (
            "Regardless, you have my thanks.\x01",
            "Now we may proceed with the\x01",
            "performance without any worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We wish to express our gratitude, so\x01",
            "may we send you tickets later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FOh, hell yeah! You didn't even\x01",
            "need to ask, my friend!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSomebody's excited...\x02",
    )

    CloseMessageWindow()

    label("loc_2157")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E77 end

    def Function_16_215B(): pass

    label("Function_16_215B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Welcome, everybody.\x01",
            "We appreciate you coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Thank you for your assistance with the\x01",
            "private performance. Allow me to express\x01",
            "my utmost gratitude once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FIt's all a part of the job, sir.\x02\x03",
            "#0000FIt sounds like you're in the middle of a performance.\x01",
            "I'm glad Arc en Ciel can continue to provide everyone\x01",
            "with fantastic shows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Of course, and it's all thanks to the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, that reminds me... We're taking a\x01",
            "day off from performing tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We'll all be here anyway, so feel\x01",
            "free to stop by for a visit, if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThank you. We'll make it a point to\x01",
            "visit you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB8, 7)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_215B end

    def Function_17_2483(): pass

    label("Function_17_2483")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Welcome, everybody.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, I regret to inform you that Ilya\x01",
            "and Rixia are currently occupied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe should be the ones apologizing.\x01",
            "Everybody's getting prepared, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, not like we had much to do here, eh?\x01",
            "We can drop by here another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI agree. We should leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FOur apologies for the disturbance.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2483 end

    def Function_18_26C4(): pass

    label("Function_18_26C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    LoadChrToIndex("chr/ch21800.itc", 0x1E)
    LoadChrToIndex("chr/ch21900.itc", 0x1F)
    LoadChrToIndex("chr/ch20800.itc", 0x20)
    LoadChrToIndex("chr/ch21200.itc", 0x21)
    LoadChrToIndex("chr/ch21300.itc", 0x22)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrChipByIndex(0x14, 0x20)
    SetChrChipByIndex(0x15, 0x21)
    SetChrChipByIndex(0x16, 0x22)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x12, 3540, 0, -2890, 315)
    SetChrPos(0x13, 2540, 0, -1890, 135)
    SetChrPos(0x14, 5100, 0, 3030, 89)
    SetChrPos(0x15, -1210, 0, -1120, 225)
    SetChrPos(0x16, -2410, 0, -2320, 45)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0005FWow, this place is packed. I'm pretty\x01",
            "sure the show was scheduled to end\x01",
            "before the parade, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI think most people's excitement\x01",
            "from the performance hasn't\x01",
            "worn down yet.\x02\x03",
            "I think it's safe to assume the theater\x01",
            "will be congested for a while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FRetreating is recommended. I would\x01",
            "not like to risk bothering them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FGuess we'll make ourselves scarce, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 1)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_26C4 end

    def Function_19_29C2(): pass

    label("Function_19_29C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(0, 1450, -4360, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 500, 0, -3230, 0)
    SetChrPos(0x102, -500, 0, -3430, 0)
    SetChrPos(0x103, 500, 0, -4730, 0)
    SetChrPos(0x104, -500, 0, -4930, 0)
    SetChrPos(0xA, 0, 0, -1760, 180)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Welcome, everybody.\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, I regret to inform you that Ilya\x01",
            "and Rixia are currently occupied...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWe should be the ones apologizing.\x01",
            "Everybody's getting prepared, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, not like we had much to do here, eh?\x01",
            "We can drop by here another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI agree. We should leave.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FOur apologies for the disturbance.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0xB9, 2)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_29C2 end

    def Function_20_2C03(): pass

    label("Function_20_2C03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, -2000, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 0, 0, -7000, 0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -5100, 0, 3000, 135)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -6000, 0, 2400, 135)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10000000)
    MoveCamera(45, 21, 0, 3000)
    SetCameraDistance(19000, 3000)

    def lambda_2CCA():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CCA)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(500)
    OP_6F(0x50)

    ChrTalk(
        0x101,
        (
            "#3400239V#0005FWhoa, you hardly see the place this empty.\x02\x03",
            "#3400240V#0000FI bet the afternoon show's already ended.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x9,
        "Girl's Voice",
        "#3400241V#2PLloyd? Is that you?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Woman's Voice",
        "#3400242V#2POh, something going on again?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-860, 1100, -1110, 2500)
    MoveCamera(10, 21, 0, 2500)
    SetCameraDistance(18000, 2500)

    def lambda_2E43():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E43)

    def lambda_2E50():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E50)
    Sleep(100)

    def lambda_2E6D():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E6D)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F8B")

    ChrTalk(
        0x101,
        "#3400246V#12P#0005FHello, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400244V#5P#1702FWhat's up? Didja come to hang out\x01",
            "with your favorite gals again?\x02\x03",
            "#3400260V#1709FWe still have some time to chill out before\x01",
            "the evening show. Wanna join us for tea?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33EB")

    label("loc_2F8B")


    ChrTalk(
        0x101,
        (
            "#3400243V#12P#0005FHey, you two.\x02\x03",
            "#3400247V#0002FIt's been a while. Let me just say,\x01",
            "everybody's been talking about\x01",
            "your new play, nonstop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400248V#5P#1702FHaha. Well, obviously! It's only\x01",
            "natural for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3400249V#1809F#5PI actually noticed that you came to watch\x01",
            "us on our opening day, Lloyd.\x02\x03",
            "#3400250V#1802FI hope you enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400251V#12P#0012FWeeeell, I only came because I was\x01",
            "accompanying Cecile.\x02\x03",
            "#3400252V#0002FBut still, the play was phenomenal!\x02\x03",
            "#3400253V#0009FI've always known Ilya was amazing, but\x01",
            "I've become your fan as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3400254V#1810F#5PO-Oh, please... You're embarrassing me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400255V#1705F#5POh, my, what do we have here?\x02\x03",
            "#3400256V#1709FMaybe I should let Cecile know her lil'\x01",
            "bro is putting the moves on my co-star.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3400257V#12P#0011FOh, come on! You clearly know\x01",
            "you're fudging the truth!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "#3400258V#1801F#6PG-Geez, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400259V#5P#1702FOkay, but seriously. What's up?\x01",
            "Do you need something from us?\x02\x03",
            "#3400245VWe still have some time to chill out before\x01",
            "the evening show. Wanna join us for tea?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33E3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_33E3)

    label("loc_33EB")


    ChrTalk(
        0x101,
        (
            "#3400261V#12P#0008FSorry, no can do. I'm here on some\x01",
            "work-related business.\x02\x03",
            "#3400262V#0001FYou see...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained to Ilya and Rixia that\x01",
            "he is searching for a lost little boy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        "#3400263V#1801F#5POh, no... That's terrible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400264V#5P#1706FWell, it's definitely true that the kiddies\x01",
            "love to come watch our shows.\x02\x03",
            "#3400265VI guess there's a chance one mighta\x01",
            "snuck in during a performance.\x02\x03",
            "#3400266V#1702FMind holding on for a minute, Lloyd?\x02\x03",
            "#3400267VI'll check with the folks on break to see\x01",
            "if they noticed him.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 21)
    Sleep(100)

    def lambda_3632():

        label("loc_3632")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_3632")

    QueueWorkItem2(0x9, 2, lambda_3632)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3400268V#12P#0005FW-Wait...\x02\x03",
            "#3400269V#0006FI don't need you to go that far for me...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x2)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        (
            "#3400270V#1804F#5POnce Ilya has her mind set on something,\x01",
            "there's no stopping her.\x02\x03",
            "#3400271V#1802FI'll help her take a look around, too.\x01",
            "I'll be back in a bit, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    BeginChrThread(0x9, 3, 0, 22)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x9, 0x3)
    SetChrPos(0x8, -1100, 0, 600, 135)
    SetChrPos(0x9, -2000, 0, 0, 135)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrSubChip(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3400272V#5P#1706FWell, doesn't look like he's hiding around\x01",
            "the theater right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3400273V#1806F#5PI'm sorry, I wish I could be more helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400274V#12P#0002FIt's okay, I appreciate the help regardless.\x01",
            "I should be apologizing for bothering you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3400275V#5P#1702FDon't sweat it, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3400276V#1800F#5PI'll be sure to notify the troupe leader and\x01",
            "the manager about the child.\x02\x03",
            "#3400277VShould we contact the police in the\x01",
            "event that we find him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400278V#12P#0004FYeah, that would be perfect.\x02\x03",
            "#3400279V#0002FThanks again, you two. I'm sure you'll\x01",
            "perform flawlessly tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3400280V#5P#1709FYou know it, my favorite lil' guy! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3400281V#1802F#5PThank you for stopping by, Lloyd.\x01",
            "You're always welcome here.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_3ACA():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ACA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BB0")
    StopBGM(0x7D0)
    WaitBGM()

    AnonymousTalk(
        0x101,
        (
            "#0003F(All right, that's a wrap on the Entertainment\x01",
            "District's investigation.)\x02\x03",
            "#0001F(Looks like the Back Alley is next...\x01",
            "Let's continue the investigation there!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3BB0")

    SetScenarioFlags(0xA1, 7)
    OP_29(0x46, 0x1, 0x1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD9")
    OP_29(0x46, 0x1, 0x2)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 3)

    label("loc_3BD9")

    EventEnd(0x5)
    NewScene("c040C", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_20_2C03 end

    def Function_21_3BE5(): pass

    label("Function_21_3BE5")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_3BF7():
        OP_95(0xFE, -5500, 0, 5000, 3500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BF7)
    WaitChrThread(0xFE, 1)

    def lambda_3C15():
        OP_95(0xFE, -10500, 0, 5000, 3500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C15)
    Return()

    # Function_21_3BE5 end

    def Function_22_3C2B(): pass

    label("Function_22_3C2B")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_3C3D():
        OP_95(0xFE, -5500, 0, 5000, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C3D)
    WaitChrThread(0xFE, 1)

    def lambda_3C5B():
        OP_95(0xFE, -10500, 0, 5000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C5B)
    Return()

    # Function_22_3C2B end

    def Function_23_3C71(): pass

    label("Function_23_3C71")

    OP_92(0xFE, 0xFFFFE69C, 0xBB8, 0x1F4)

    def lambda_3C83():
        OP_95(0xFE, -6500, 0, 5000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C83)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3C71 end

    def Function_24_3C9D(): pass

    label("Function_24_3C9D")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0000FLooks like these are the second floor seats.\x02\x03",
            "Wouldn't want to bother people by wandering\x01",
            "around, so I'll refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8260, 2500, 14010, 90)
    EventEnd(0x4)
    Return()

    # Function_24_3C9D end

    def Function_25_3D42(): pass

    label("Function_25_3D42")

    EventBegin(0x1)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#0000FLooks like these are the second floor seats.\x02\x03",
            "Wouldn't want to bother people by wandering\x01",
            "around, so I'll refrain from entering.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5760, 2500, 13790, 270)
    EventEnd(0x4)
    Return()

    # Function_25_3D42 end

    SaveToFile()

Try(main)
