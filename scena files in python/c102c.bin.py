from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c102c.bin",                # FileName
        "c102c",                    # MapName
        "c102c",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c102c",                  # 0
        "Branch Manager Cerdan",  # 1
        "Kopan",                  # 2
        "Peter",                  # 3
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24200.itc",                   # 02
    ))

    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7230,    0,       6780,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(-3170,   0,       51750,   1200,    -2860,   1500,    52600,   0x007C, 0,  9,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  15, 0x0000)

    ScpFunction((
        "Function_0_1A0",          # 00, 0
        "Function_1_258",          # 01, 1
        "Function_2_2D9",          # 02, 2
        "Function_3_316",          # 03, 3
        "Function_4_31A",          # 04, 4
        "Function_5_1052",         # 05, 5
        "Function_6_1DD7",         # 06, 6
        "Function_7_20C4",         # 07, 7
        "Function_8_22D8",         # 08, 8
        "Function_9_2FD1",         # 09, 9
        "Function_10_3BD5",        # 0A, 10
        "Function_11_3BF1",        # 0B, 11
        "Function_12_3DBE",        # 0C, 12
        "Function_13_3E68",        # 0D, 13
        "Function_14_6C2A",        # 0E, 14
        "Function_15_6EBD",        # 0F, 15
    ))


    def Function_0_1A0(): pass

    label("Function_0_1A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E0"),
        (1, "loc_1EC"),
        (2, "loc_1F8"),
        (3, "loc_204"),
        (4, "loc_210"),
        (5, "loc_21C"),
        (6, "loc_228"),
        (SWITCH_DEFAULT, "loc_234"),
    )


    label("loc_1E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_204")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_210")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_21C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_234")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_257")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_257")

    Return()

    # Function_0_1A0 end

    def Function_1_258(): pass

    label("Function_1_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26B")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2BF")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_279")
    Jump("loc_2BF")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_287")
    Jump("loc_2BF")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_295")
    Jump("loc_2BF")

    label("loc_295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2AC")
    SetChrFlags(0x8, 0x80)
    Jump("loc_2BF")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BF")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D8")
    Event(0, 8)

    label("loc_2D8")

    Return()

    # Function_1_258 end

    def Function_2_2D9(): pass

    label("Function_2_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EF")
    OP_65(0x0, 0x1)

    label("loc_2EF")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_315")
    OP_66(0x1, 0x1)

    label("loc_315")

    Return()

    # Function_2_2D9 end

    def Function_3_316(): pass

    label("Function_3_316")

    Call(0, 4)
    Return()

    # Function_3_316 end

    def Function_4_31A(): pass

    label("Function_4_31A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A6")

    ChrTalk(
        0x8,
        (
            "Hey there, Lloyd. Are you aware of\x01",
            "the Rank Certification Exam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our guild grants ranks that correspond\x01",
            "to how skilled of an angler you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! If you become an ace angler,\x01",
            "I bet you'd be legendary in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, kid. If your young brain doesn't\x01",
            "understand anything, feel free to ask me.\x01",
            "I'll give you a thorough explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8D7")

    ChrTalk(
        0x8,
        "Welcome to the Fisherman's Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're our newest member, Lloyd, right?\x01",
            "I've heard the stories about you, kid!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kopan went and invited you to\x01",
            "our guild, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nice to meet you, Lloyd. The name's\x01",
            "Cerdan, and I'm the Fisherman's Guild\x01",
            "Manager here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FO-Oh, thanks...\x02\x03",
            "#0005FWait, what? When the heck did\x01",
            "I join the Fisherman's Guild?!\x02\x03",
            "#0003FI mean, sure, I DID accept that\x01",
            "fishing rod earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahahaha! Don't sweat the details, kid!\x01",
            "You're already our comrade in rods!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I don't think I'm escaping this one...)\x02\x03",
            "#0000F(Eh, looks like they all share a love\x01",
            "for fishing. I'm willing to bet Cerdan\x01",
            "could talk about it for hours on end...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right! Have you heard about the\x01",
            "Rank Certification Exam, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our guild grants ranks that correspond\x01",
            "to how skilled of an angler you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! If you become an ace angler,\x01",
            "I bet you'd be legendary in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, kid. If your young brain doesn't\x01",
            "understand anything, feel free to ask me.\x01",
            "I'll give you a thorough explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_8D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E11")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A2B")

    ChrTalk(
        0x8,
        (
            "Congrats! Looks like you've finally become\x01",
            "a member of our fine guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, Kopan sure snatched you up quick.\x01",
            "I was going to personally invite you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FOh, you were?\x02\x03",
            "#0005FWait when the heck did I\x01",
            "join the Fisherman's Guild?!\x02\x03",
            "#0003FI mean, sure, I DID accept that\x01",
            "fishing rod earlier...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B97")

    label("loc_A2B")


    ChrTalk(
        0x8,
        (
            "Congrats on joining the guild, kid!\x01",
            "I've been looking forward to meeting\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The name's Cerdan, and I'm the Fisherman's\x01",
            "Guild Manager here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "A pleasure to meet you, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FHaha, thanks...\x02\x03",
            "#0005FWait, what? When the heck did\x01",
            "I join the Fisherman's Guild?!\x02\x03",
            "#0003FI mean, sure, I DID accept that\x01",
            "fishing rod earlier...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B97")


    ChrTalk(
        0x8,
        (
            "Bwahahaha! Don't sweat the details, kid!\x01",
            "You're already our comrade in rods!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I don't think I'm escaping this one...)\x02\x03",
            "#0000F(Still, it looks like they all share a love\x01",
            "for fishing. I'm willing to bet Cerdan\x01",
            "could talk about it for hours on end...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right! Have you heard about the\x01",
            "Rank Certification Exam, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our guild grants ranks that correspond\x01",
            "to how skilled of an angler you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! If you become an ace angler,\x01",
            "I bet you'd be legendary in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, kid. If your young brain doesn't\x01",
            "understand anything, feel free to ask me.\x01",
            "I'll give you a thorough explanation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_E11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_1044")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103F")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED8")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E83")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA3")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ED3")

    label("loc_EA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB7")
    Jump("loc_ED3")

    label("loc_EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_ED3")

    Jump("loc_103A")

    label("loc_ED8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FB7")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",            # 0
            "Check Rank\x01",      # 1
            "Shop\x01",            # 2
            "Leave\x01",           # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F29")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4D")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB2")

    label("loc_F4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F71")
    OP_AF(0x36)
    Jump("loc_F73")

    label("loc_F71")

    OP_AF(0x37)

    label("loc_F73")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB2")

    label("loc_F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F96")
    Jump("loc_FB2")

    label("loc_F96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_FB2")

    Jump("loc_103A")

    label("loc_FB7")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",            # 0
            "Check Rank\x01",      # 1
            "Leave\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100A")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_103A")

    label("loc_100A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101E")
    Jump("loc_103A")

    label("loc_101E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_103A")

    Jump("loc_E24")

    label("loc_103F")

    Jump("loc_1047")

    label("loc_1044")

    Call(0, 5)

    label("loc_1047")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_31A end

    def Function_5_1052(): pass

    label("Function_5_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1692")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124D")

    ChrTalk(
        0x8,
        "Hey there, kid. You hear about this before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Legend has it, a fabled fish known only as\x01",
            "the serpenthead lives in Crossbell's waters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thing's apparently hiding in the depths of Lake Elm.\x01",
            "It's a mighty fierce one, too. Used to strike fear\x01",
            "into the hearts of any fisherman back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the blasted thing hasn't been spotted\x01",
            "for the last ten or so years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd wager we'd have to award you a medal\x01",
            "if you manage to fish that thing up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1336")

    label("loc_124D")


    ChrTalk(
        0x8,
        (
            "The serpenthead is truly the Guardian of\x01",
            "Lake Elm... Fishing the thing up has been\x01",
            "our dream for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though it hasn't been spotted in ten or so\x01",
            "years, a Master Fisher like yourself\x01",
            "might stand a chance against it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1336")

    Jump("loc_168D")

    label("loc_133B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B6")

    ChrTalk(
        0x8,
        (
            "You're every bit the man I expected you to be, Lloyd.\x01",
            "You've attained the rank of Divine Angler, yet you\x01",
            "manage to remain humble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! I'm a fan of ya, Lloyd! Why don't we\x01",
            "gather some of the boys and go do a bit of night\x01",
            "fishing sometime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our branch likes to go night fishing every\x01",
            "once in a while as a social event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FSorry, Cerdan. Tonight's not a great night.\x02\x03",
            "I'd love to go fishing with you all when\x01",
            "I have the time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Bwahaha! You even managed to humbly reject me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All right then, kid! Just lemme know when you're good\x01",
            "to go. We'll even throw a contest to celebrate!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_168D")

    label("loc_15B6")


    ChrTalk(
        0x8,
        (
            "After all, how are we not gonna rejoice at your\x01",
            "feat of reaching the rank of Divine Angler?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm going to have you recount the whole tale\x01",
            "of how you managed to take down the\x01",
            "mighty serpenthead. Bwahahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168D")

    Jump("loc_1DD6")

    label("loc_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1735")

    ChrTalk(
        0x8,
        (
            "I think I'll go and enjoy myself\x01",
            "a good ol' fishin' session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "City's been a bit too noisy for my liking,\x01",
            "so I'm thinkin' Mainz sounds good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD6")

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(
        0x8,
        (
            "The master of Crossbellan waters still\x01",
            "lurks somewhere out there. A fish so\x01",
            "immense, no one's caught it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But anyway, you should be able to find some\x01",
            "other big ones, like the electric eel, and\x01",
            "the demon catfish, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_188C")

    ChrTalk(
        0x8,
        (
            "If any of those strike your fancy, then you\x01",
            "should try and catch 'em, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_188C")


    ChrTalk(
        0x8,
        (
            "If you've got any interest in making it to the\x01",
            "next level, then keep challengin' yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EC")

    Jump("loc_1DD6")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0C")

    ChrTalk(
        0x8,
        (
            "The president of the Fisherman's Guild\x01",
            "is a man known as the Fishing Baron.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I shot him an invite to join us in Crossbell for the\x01",
            "Anniversary Festival, but the man couldn't find\x01",
            "time in his schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Can't blame him, though. He's a busy man.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB7")

    label("loc_1A0C")


    ChrTalk(
        0x8,
        (
            "The Fishing Baron's trying to establish branches\x01",
            "in all the major countries across Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's an extremely busy man, so he\x01",
            "sadly had to refuse my invitation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB7")

    Jump("loc_1DD6")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B46")

    ChrTalk(
        0x8,
        "You got some real nice catches yesterday!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you continue tryin' to reach the\x01",
            "next level, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C12")

    label("loc_1B46")


    ChrTalk(
        0x8,
        (
            "I know it's the Anniversary Festival, but\x01",
            "don't cast aside your fishin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you neglect training in the way of the rod,\x01",
            "you'll get real rusty. Try to reel in at least\x01",
            "one fish a day, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C12")

    Jump("loc_1DD6")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4A")

    ChrTalk(
        0x8,
        (
            "Hey, Lloyd. You busy with all your\x01",
            "police work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, it's the height of the Anniversary\x01",
            "Festival, so we're saddled with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah? Well, I just heard somethin'\x01",
            "odd, is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't worry about it, though. Just focus\x01",
            "on your work and fish in your downtime!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DD6")

    label("loc_1D4A")


    ChrTalk(
        0x8,
        (
            "Don't worry about us, Lloyd. Your job's\x01",
            "your top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That being said, don't forget to fish\x01",
            "for a bit when you have a break!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD6")

    Return()

    # Function_5_1052 end

    def Function_6_1DD7(): pass

    label("Function_6_1DD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2040")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        "Right, I tried talking about it to Estelle, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not too surprised our full-time working members\x01",
            "are up the creek without a paddle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's the guild's style to fish without harmin'\x01",
            "our day jobs. It's a shame, but let's cast 'em\x01",
            "an invite a little bit earlier next time, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha... He insisted that he's going to\x01",
            "attend, and there's no stoppin' him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even told us he'd take a few vacation days.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Man, I'm lookin' forward to this. Been too\x01",
            "long since we've all been this excited!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What's he even talking about?)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_20C0")

    label("loc_2040")


    ChrTalk(
        0xFE,
        "Man, I'm lookin' forward to this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This event's been in the works for over a\x01",
            "month, so let's make it a good one, yeah?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1DD7 end

    def Function_7_20C4(): pass

    label("Function_7_20C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_22D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2174")

    ChrTalk(
        0xFE,
        (
            "Apparently, Peter and that Master\x01",
            "Fisherman guy went to fish at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lame. I wanted to challenge 'em\x01",
            "to another fishing showdown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22D4")

    label("loc_2174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2240")

    ChrTalk(
        0xFE,
        (
            "I dunno what you guys do, but the police\x01",
            "are havin' some trouble, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, don't worry about me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, I've got some free time, so I figure\x01",
            "I'll go get some fishin' done.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22D4")

    label("loc_2240")


    ChrTalk(
        0xFE,
        (
            "Apparently, Peter and that Master\x01",
            "Fisherman guy went to fish at Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got some free time, so I figure I'll\x01",
            "go fishin' somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D4")

    TalkEnd(0xFE)
    Return()

    # Function_7_20C4 end

    def Function_8_22D8(): pass

    label("Function_8_22D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1500, 1400, 700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22440, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 11910, 1670, 7920, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2100, 1400, 1510, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22440, 3000)

    def lambda_23D9():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23D9)

    def lambda_23F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23F3)
    Sleep(300)

    def lambda_2407():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2407)

    def lambda_2421():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2421)
    Sleep(300)

    def lambda_2435():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2435)

    def lambda_244F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_244F)
    Sleep(300)

    def lambda_2463():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2463)

    def lambda_247D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_247D)
    Sleep(3000)

    ChrTalk(
        0x101,
        "#5P#0000FExcuse us...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x0, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x2D, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5P#0003FLooks like nobody's in.\x02\x03",
            "#0001FI figured we'd be able to find a clue about\x01",
            "Doctor Guenter if we came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FThose fishin' freaks head out to their\x01",
            "tournament, or whatever it was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FIf they have, then our would-be clue\x01",
            "has already left the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWait a moment, please. I still sense\x01",
            "a presence somewhere inside.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Young Man's Voice",
        "O-Oh, crap! I'm late!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_26B1():

        label("loc_26B1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_26B1")

    QueueWorkItem2(0x0, 1, lambda_26B1)

    def lambda_26C3():

        label("loc_26C3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_26C3")

    QueueWorkItem2(0x1, 1, lambda_26C3)

    def lambda_26D5():

        label("loc_26D5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_26D5")

    QueueWorkItem2(0x2, 1, lambda_26D5)

    def lambda_26E7():

        label("loc_26E7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_26E7")

    QueueWorkItem2(0x3, 1, lambda_26E7)
    Fade(500)
    OP_68(9180, 1400, 3560, 0)
    OP_0D()

    def lambda_2710():
        OP_95(0xFE, 11480, 0, 3930, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2710)
    Sleep(100)
    OP_68(2630, 1400, 2250, 2700)
    WaitChrThread(0x9, 1)

    def lambda_2742():
        OP_95(0xFE, 3740, 0, 3740, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2742)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "#11PWell, if it isn't Detective Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FGreat timing, Kopan. You got a second\x01",
            "to answer a quick question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSorry, man! I don't have time to sit here\x01",
            "and chitchat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI gotta hurry to the Fisher Cup out on\x01",
            "Ursula Road's sandbar! Based on the\x01",
            "time, it probably just started!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105FThe...Fisher Cup?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FThat the fishin' tournament?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh, so you guys already knew about it.\x01",
            "I shoulda known. Nothin' gets past an angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Fisher Cup is a tournament held in honor\x01",
            "of the Fisherman's Guild president, Mr. Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWait! I just said that I don't have\x01",
            "time to sit around chitchatting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf I don't hurry my rear out there, all the\x01",
            "older guys will snag the best spots!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0011FJ-Just one thing! One more thing!\x02\x03",
            "#0000FAmong those attending the Fisher\x01",
            "Cup, is there a doctor with glasses,\x01",
            "blue hair, and a white labcoat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHmmmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYou talkin' about Joachim?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'm pretty sure he was comin' today, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FBingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh, you guys all participating\x01",
            "in the tournament?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIn that case, take this!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x34),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34, 1)

    ChrTalk(
        0x101,
        "#6P#0005FWh-What?! Why are you giving me this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#11PI'm givin' it to you as a memento for competin'\x01",
            "in the Fisher Cup. It's a participation prize,\x01",
            "so to speak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006F(I don't ever recall committing to this tournament,\x01",
            "so...is this really okay?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWait, damn it! I forgot I was running late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSorry guys, gotta jet! You'd better get\x01",
            "movin' if you wanna make it!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(940, 1400, 910, 1000)
    OP_95(0x9, -1250, 0, -1260, 7000, 0x0)

    def lambda_2DDF():
        OP_95(0xFE, -3050, 0, -3060, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2DDF)

    def lambda_2DF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2DF9)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#11P#0105FFor someone in a hurry, he\x01",
            "really went out of his way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FY-Yeah...\x02\x03",
            "#0000FAnyway, we know Doctor Guenter should\x01",
            "be headed to the sandbar on Ursula Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FWe must hurry and reel him in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FCaught his enthusiasm, eh, Tio Tot?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FSilence.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_68(1210, 1400, 1210, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_29(0x16, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_22D8 end

    def Function_9_2FD1(): pass

    label("Function_9_2FD1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(-2830, 1100, 51870, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3450, 0, 51000, 0)
    SetChrPos(0x102, -3450, 0, 49640, 0)
    SetChrPos(0x103, -2510, 0, 51000, 0)
    SetChrPos(0x104, -2510, 0, 49640, 0)
    SetChrPos(0x9, -1490, 0, 45300, 315)
    SetChrFlags(0x9, 0x40)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    LoadEffect(0x7, "event\\eva00_00.eff")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#6P#0105FOh, this tank of water is enormous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0202FThe fish appear to be swimming peacefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FActually, now that I've taken a better look, their\x01",
            "scales look like they reflect light and sparkle.\x02\x03",
            "#0000FAn 'oasis of pristine water'... I think this\x01",
            "might be our next target.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(860, 0, 100, 0)
    PlayEffect(0x7, 0x7, 0xFF, 0x0, -3230, 1000, 53150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    StopEffect(0x7, 0x2)
    Sleep(500)
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
        "#6P#0005FDid you guys see that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FIt's inside the friggin' tank?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Young Man's Voice",
        "What's the matter, you guys?\x02",
    )

    CloseMessageWindow()
    OP_68(-3020, 1400, 49800, 1800)
    BeginChrThread(0x9, 1, 0, 10)
    Sleep(300)

    def lambda_3334():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3334)

    def lambda_3341():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3341)

    def lambda_334E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_334E)

    def lambda_335B():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_335B)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0100FOh, sorry to disturb you. It's actually\x01",
            "a bit of a long story, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000F...to make it short, an important card of\x01",
            "ours fell into this tank. Do you mind getting\x01",
            "it out for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PThe heck?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#12PLooks like it'd be kinda challenging...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PYou'd probably have to snag it with\x01",
            "a hook to get it outta there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PNot a chance I'm diving in there to grab it.\x02",
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
        0x103,
        "#11P#0200FThat much is a given.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FGuess we'll need a pretty experienced\x01",
            "fisherman to get that baby outta there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PMeh. I'm already here. I'll fish the blasted\x01",
            "thing out for you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3150, 1200, 49570, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3080, 0, 49720, 0)
    SetChrPos(0x102, -3880, 0, 47530, 0)
    SetChrPos(0x103, -2670, 0, 48590, 0)
    SetChrPos(0x104, -2670, 0, 47530, 0)
    SetChrPos(0x9, -3010, 0, 51090, 180)
    Sleep(1200)
    Sound(11, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5PPiece of cake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0012FW-Wow. You made that look easy.\x02\x03",
            "#0000FSorry to make you do our dirty work, Kopan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PNo biggie. I do stuff like this all the time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PSo, uh...what's up with the card?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FW-Well... You're going to be standing here for\x01",
            "a long time, if you really want to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHmm? Eh, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0301FYo, Lloyd. Hurry up and read that sucker.\x02",
    )

    CloseMessageWindow()

    def lambda_3879():

        label("loc_3879")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_3879")

    QueueWorkItem2(0x102, 1, lambda_3879)

    def lambda_388B():

        label("loc_388B")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_388B")

    QueueWorkItem2(0x104, 1, lambda_388B)

    def lambda_389D():

        label("loc_389D")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_389D")

    QueueWorkItem2(0x103, 1, lambda_389D)
    OP_95(0x101, -3920, 0, 48810, 1000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_38CF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38CF)

    def lambda_38DC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38DC)

    def lambda_38E9():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38E9)

    def lambda_38F6():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_38F6)
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#0105FOkay. Let's see what we have here...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　9-7-14-9-19\x01",
            "　Examine the central box\x01",
            "　that rudely resounds!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#0301FThe hell are these numbers for? You think\x01",
            "I'm some kinda orbal computer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FPerhaps some kind of code?\x02\x03",
            "#0203FFor example, it is entirely possible these\x01",
            "numbers correspond to letters...maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FYeah, that makes sense to me. Let's keep\x01",
            "that in our minds while we search.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2910, 0, 49460, 0)
    SetChrPos(0x9, -520, 0, 43310, 90)
    ClearChrFlags(0x9, 0x40)
    OP_4C(0x9, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x1, 0x1)
    OP_29(0x22, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_2FD1 end

    def Function_10_3BD5(): pass

    label("Function_10_3BD5")

    OP_95(0x9, -3370, 0, 47470, 1500, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Return()

    # Function_10_3BD5 end

    def Function_11_3BF1(): pass

    label("Function_11_3BF1")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C72")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_3D9A")

    label("loc_3C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CE4")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3D9A")

    label("loc_3CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D56")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3D9A")

    label("loc_3D56")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_3D9A")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_11_3BF1 end

    def Function_12_3DBE(): pass

    label("Function_12_3DBE")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DDC")
    Jump("loc_3E16")

    label("loc_3DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF9")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_3E16")

    label("loc_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E16")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_3E16")

    label("loc_3E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E29")
    Jump("loc_3E46")

    label("loc_3E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E3C")
    Jump("loc_3E46")

    label("loc_3E3C")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_3E46")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_12_3DBE end

    def Function_13_3E68(): pass

    label("Function_13_3E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42A8")

    ChrTalk(
        0x8,
        (
            "First, let me explain. The Fisherman's Guild seeks\x01",
            "to spread fishing enthusiasm and administers the\x01",
            "Rank Certification Exam to increase one's fishing rank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For each promotion in rank you achieve, we'll\x01",
            "award you with different titles and prizes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You just joined the guild, so your current rank\x01",
            "is Amateur Fisher, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_413B")

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least four unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You can look at your Fishing Notebook to\x01",
            "see what kinds of fish you've already caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Come back and report to us once you've\x01",
            "caught four unique kinds, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Isn't fishin' just the best? Just gotta plan out a\x01",
            "strategy and bag yourself some big ones.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A0")

    label("loc_413B")


    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least four unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, what's this now? You've already managed\x01",
            "to catch four unique kinds of fish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure. Just fork over that Fishing Notebook of\x01",
            "yours for a second so I can check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ask me to check your rank again any time and\x01",
            "I'll give you your much deserved promotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A0")

    SetScenarioFlags(0x69, 6)
    Jump("loc_6C29")

    label("loc_42A8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_46C0")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Wow, Lloyd. Managed to catch yourself\x01",
            "some real beauts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good work, kid. Starting today, you are\x01",
            "now a Hobbyist Fisher!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Achieved the rank of Hobbyist Fisher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x5A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " as a prize.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x5A, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "This thing's my prized straw hat you see.\x01",
            "Better catch you wearin' it the next time\x01",
            "you go fishin', got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wear this hat and work towards your next\x01",
            "big catch, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FOh, this is standard fishing paraphernalia\x01",
            "isn't it? I'll wear it with pride, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You still have a long way to go, but the boys and\x01",
            "I thought we'd prepare this nice medal for you\x01",
            "to celebrate ranking up to Hobbyist Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But more importantly, I think you're ready to hear\x01",
            "the next challenge you need to tackle to rank up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "eight unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Plan out a strategy and bag yourself some big ones.\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_4807")

    label("loc_46C0")


    ChrTalk(
        0x8,
        "Your current rank is Amateur Fisher, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least four unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You can look at your Fishing Notebook to\x01",
            "see what kinds of fish you've already caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Be sure to come back to me if you\x01",
            "catch some more. I'll see if you've earned\x01",
            "a promotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4807")

    Jump("loc_6C29")

    label("loc_480C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E84")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Wow, Lloyd. Managed to catch yourself\x01",
            "some real beauts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good work, kid. Starting today, you are\x01",
            "now a Professional Fisher!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Achieved the rank of Professional Fisher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x9E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " as a prize.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x9E, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "I remember the day I reached Professional\x01",
            "Fisher as clear as a river stream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd always been an avid fisherman, but I had to stop\x01",
            "in Liberl for a business trip. During that trip, I met\x01",
            "with the founder of the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Needless to say, this man was the legendary angler\x01",
            "himself, Mr. Fisher, who's now my boss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, cue some more fishing, and then it happened.\x01",
            "I was granted the rank of Professional Fisher.\x01",
            "Maaaaan, that sure takes me back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FH-Haha, it must have been quite the struggle.\x01",
            "(It's another one of Cerdan's stories...\x01",
            "It's going to be a long one, I can feel it.)\x02\x03",
            "#0000FBut, wait. Why'd you stop in Liberl for work?\x01",
            "Were you some kind of trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! No, no, not at all! I was there\x01",
            "on behalf of my father, who was a businessman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure, I may have business acumen, but I\x01",
            "pride myself in being a branch manager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FYeah, I can see that...\x01",
            "(I figured he lived for his hobby, but\x01",
            "this just confirms it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whoops, almost forgot. I still gotta tell you\x01",
            "about the requirements to advance to the\x01",
            "next rank!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least twelve unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'll really need to pull out all the stops\x01",
            "for this one, but just try your best!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_4F7A")

    label("loc_4E84")


    ChrTalk(
        0x8,
        (
            "Your current rank is Hobbyist\x01",
            "Fisher, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least eight unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Be sure to come back to me if you\x01",
            "catch some more. I'll see if you've earned\x01",
            "yourself a promotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7A")

    Jump("loc_6C29")

    label("loc_4F7F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_562C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_552C")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Wow, Lloyd. Managed to catch yourself\x01",
            "some real beauts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Good work, kid. Starting today, you are\x01",
            "now a 2nd Class Fisher!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Achieved the rank of 2nd Class Fisher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x33E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " as a prize.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33E, 1)
    AddItemNumber(0xA4, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "You did it, Lloyd. Congrats!\x01",
            "Y'know, I actually had some struggles managing\x01",
            "to become a 2nd Class Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Didn't know how to handle it, so I hid away\x01",
            "in the mountains to find my inner angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Managed to get in touch with Mother Nature, which\x01",
            "sharpened my senses. Next thing I know, I catch the\x01",
            "elusive pearlglass and BOOM... Promotion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure you had your fair share of hardships, too,\x01",
            "which is exactly why this is a momentous occasion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that you've managed to make it this far,\x01",
            "I'm expecting great things from you, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHaha. I'll try to live up to your expectations, sir.\x02\x03",
            "#0000FBy the way, if I'm currently a 2nd Class Fisher,\x01",
            "does that mean the next rank is 1st Class Fisher?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right you are, kid. The next rank is indeed\x01",
            "1st Class Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In order to advance to 1st Class Fisher, you\x01",
            "must catch at least 16 unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At long last, you're counted among the ranks\x01",
            "of the high-ranked anglers in the guild.\x01",
            "Bwahaha! I'm looking forward to your next feat!\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_5627")

    label("loc_552C")


    ChrTalk(
        0x8,
        (
            "Your current rank is Professional\x01",
            "Fisher, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least twelve unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Be sure to come back to me if you\x01",
            "catch some more. I'll see if you've earned\x01",
            "yourself a promotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5627")

    Jump("loc_6C29")

    label("loc_562C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5D37")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Wow, Lloyd. Managed to somehow catch\x01",
            "even more rare beauts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Amazing job, Lloyd. Starting today,\x01",
            "you are now a 1st Class Fisher!\x01",
            "Phenomenal work as always, Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Achieved the rank of 1st Class Fisher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33F, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "You've finally reached the rank of 1st Class\x01",
            "Fisher. Man, you work quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Think I made it to that rank five or six years\x01",
            "ago, and that was the final push needed to\x01",
            "convince me to start up this branch in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I remember it clearly... The tears of joy pouring\x01",
            "from Mr. Fisher's eyes when I proposed my plan...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Well, never mind that.\x01",
            "Lloyd, I might as well tell you one\x01",
            "more thing while you're here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a 1st Class Fisher, you now have the\x01",
            "ability to purchase the Deluxe Dumplings\x01",
            "here at the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is an all-purpose, high-quality\x01",
            "bait, developed by yours truly.\x01",
            "All kinds of different fish will bite it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWell, it would be nice to have some new bait.\x02\x03",
            "#0008FAnd, it's definitely true that changing your bait\x01",
            "will attract different types of fish. Maybe I'll use\x01",
            "this as a chance to try some new techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Bwahaha! You never let me down, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're damn right! Change your bait at the\x01",
            "usual fishing holes, and it's like you're in\x01",
            "a whole new world!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And I can't forget... I need to tell you the\x01",
            "requirement to advance to the next rank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's finally time for you to advance to the\x01",
            "rank known as Master Fisher. You'll need\x01",
            "to catch 23 unique kinds of fish this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This one's going to push you beyond your limits,\x01",
            "but you're going to have to deal with it, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_5E9A")

    label("loc_5D37")


    ChrTalk(
        0x8,
        (
            "Your current rank is 2nd Class Fisher,\x01",
            "Lloyd. That's already an incredible feat in itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Your conditions for ranking up are to catch\x01",
            "at least 16 unique kinds of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure you'll pull it off if you change up your\x01",
            "bait and locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. Be sure to come back to me if you\x01",
            "catch some more. I'll see if you've earned\x01",
            "a promotion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9A")

    Jump("loc_6C29")

    label("loc_5E9F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_654F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_63D4")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "Holy carp! You've managed to fish up\x01",
            "the ever-elusive noble carp, and even\x01",
            "the gold salmon?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is unreal, Lloyd. Starting today,\x01",
            "you are now a Master Fisher!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Achieved the rank of Master Fisher!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x340),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x37),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x340, 1)
    AddItemNumber(0x37, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "Ya did it, kid. You managed to ascend\x01",
            "to my level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We can finally discuss the gold salmon's\x01",
            "glorious tail fin...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And the feeling of the noble carp's\x01",
            "powerful tug on your line...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a fellow Master Fisher, I can definitely\x01",
            "say that you're a fishin' sage now. Pretty stoked\x01",
            "to have another friend reach this level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Afraid I've got nothing left to teach you, Lloyd.\x01",
            "It's up to you to figure it out from here, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHahaha... Wow, this feels like a dream.\x01",
            "Thank you for everything, Cerdan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's just one more thing... There hides\x01",
            "a mythical Guardian of Crossbell's waters.\x01",
            "A fish so immense, no one's caught it before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's rumored that the Aqua Wizard I just gave\x01",
            "you has the strength to reel that bad boy in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever feel like you're up to the task, then\x01",
            "challenge yourself to finally capture this legend\x01",
            "of the deep.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_654A")

    label("loc_63D4")


    ChrTalk(
        0x8,
        (
            "Your current rank is 1st Class Fisher, Lloyd.\x01",
            "It's amazing you've come so far in such little time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, the rank of Master Fisher still awaits\x01",
            "you. You have to catch 23 unique kinds\x01",
            "of fish to qualify.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This'll be your toughest challenge yet.\x01",
            "You must catch a noble carp and a\x01",
            "gold salmon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you manage to catch any more\x01",
            "kinds of fish, come show me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_654A")

    Jump("loc_6C29")

    label("loc_654F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C29")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6AEA")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cerdan examined Lloyd's Fishing Notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "G-GLORIOUS! You ACTUALLY managed to\x01",
            "catch the Guardian of the lake itself, the\x01",
            "serpenthead?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I-I can't believe my eyes... You've gone\x01",
            "and done it now, Lloyd! I think I might\x01",
            "even start crying! Bwahahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FY-Yeah, I figured it was that insane fish\x01",
            "you told me about...\x02\x03",
            "#0003FI was totally shocked by how large\x01",
            "this thing was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That legendary fish's been the Crossbell\x01",
            "branch's arch nemesis for YEARS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But now that you've caught it, it can\x01",
            "only mean one thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's time I bestowed upon you\x01",
            "a special title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And that title is known as the 'Divine Angler.'\x01",
            "This renowned title has only ever been\x01",
            "awarded to one person in one branch!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Received the title of Divine Angler!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x60),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x60, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x8,
        (
            "Never woulda expected you to surpass me\x01",
            "and become a Divine Angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you never stop doin' what you're\x01",
            "doin', Crossbell's very own Divine Angler!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FUh... This is incredibly embarrassing.\x02\x03",
            "#0000FBut, you've supported me in more ways than\x01",
            "I can count. I'll keep relying on you for all\x01",
            "matters fishing. Sound good, Cerdan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see you're still a humble kid despite\x01",
            "all you've accomplished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! Wouldn't have it any other way!\x01",
            "Bwahahahahaha!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_6C29")

    label("loc_6AEA")


    ChrTalk(
        0x8,
        "Your current rank is Master Fisher, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We unfortunately don't award any ranks\x01",
            "higher than that at the Crossbell branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, if it's you... I'm sure there'll\x01",
            "always be bigger fish to fry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! Be sure to show your pal,\x01",
            "Cerdan, if you catch anything new!\x01",
            "I'd love to take a gander at it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C29")

    Return()

    # Function_13_3E68 end

    def Function_14_6C2A(): pass

    label("Function_14_6C2A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C4F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C6A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C85")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CA0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CBB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CD6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CF1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D0C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D27")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D42")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D5D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D78")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D93")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DAE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DC9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DE4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DFF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E35")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E50")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E6B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E86")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EA1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EBC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EBC")

    Return()

    # Function_14_6C2A end

    def Function_15_6EBD(): pass

    label("Function_15_6EBD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Easy Fish Dishes is on the shelf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_6F84")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F84")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x8)

    label("loc_6F84")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_15_6EBD end

    SaveToFile()

Try(main)
