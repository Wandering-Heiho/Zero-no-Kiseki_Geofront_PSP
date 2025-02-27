from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
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
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(7530,    0,       6780,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_3DC",          # 02, 2
        "Function_3_410",          # 03, 3
        "Function_4_414",          # 04, 4
        "Function_5_117D",         # 05, 5
        "Function_6_3505",         # 06, 6
        "Function_7_3BE4",         # 07, 7
        "Function_8_4B61",         # 08, 8
        "Function_9_4EB0",         # 09, 9
        "Function_10_5941",        # 0A, 10
        "Function_11_5B0E",        # 0B, 11
        "Function_12_5BCB",        # 0C, 12
        "Function_13_8980",        # 0D, 13
        "Function_14_8C13",        # 0E, 14
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_178 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26A")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_290")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_3B5")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C4")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D7")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_3B5")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_317")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_3B5")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_37E")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_379")

    Jump("loc_3B5")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_3B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_3DB")

    Return()

    # Function_1_230 end

    def Function_2_3DC(): pass

    label("Function_2_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_40F")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_40F")

    Return()

    # Function_2_3DC end

    def Function_3_410(): pass

    label("Function_3_410")

    Call(0, 4)
    Return()

    # Function_3_410 end

    def Function_4_414(): pass

    label("Function_4_414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_43E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5CA")

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

    label("loc_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A01")

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
            "manager here in Crossbell.\x02",
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

    label("loc_A01")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B56")

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
            "#0005FWait, when the heck did I\x01",
            "join the Fisherman's Guild?!\x02\x03",
            "#0003FI mean, sure, I DID accept that\x01",
            "fishing rod earlier...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC2")

    label("loc_B56")


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
            "Guild manager here in Crossbell.\x02",
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

    label("loc_CC2")


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

    label("loc_F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_116F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116A")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1003")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCE")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FFE")

    label("loc_FCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FE2")
    Jump("loc_FFE")

    label("loc_FE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_FFE")

    Jump("loc_1165")

    label("loc_1003")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E2")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1054")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1078")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10DD")

    label("loc_1078")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AD")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109C")
    OP_AF(0x36)
    Jump("loc_109E")

    label("loc_109C")

    OP_AF(0x37)

    label("loc_109E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10DD")

    label("loc_10AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C1")
    Jump("loc_10DD")

    label("loc_10C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_10DD")

    Jump("loc_1165")

    label("loc_10E2")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1135")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1165")

    label("loc_1135")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1149")
    Jump("loc_1165")

    label("loc_1149")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1165")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_1165")

    Jump("loc_F4F")

    label("loc_116A")

    Jump("loc_1172")

    label("loc_116F")

    Call(0, 5)

    label("loc_1172")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_414 end

    def Function_5_117D(): pass

    label("Function_5_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(
        0x8,
        (
            "There's an apartment complex by the name\x01",
            "of Acacia two buildings down to the left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pretty sure there was a vacant room in there.\x01",
            "That's what you're looking for, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_188A")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1438")

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
    Jump("loc_1521")

    label("loc_1438")


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

    label("loc_1521")

    Jump("loc_1885")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AE")

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
            "I'll be sure to happily go fishing with you all\x01",
            "when I have the time, though.\x02",
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
            "All right, then, kid! Just lemme know when you're good\x01",
            "to go. We'll even throw a contest to celebrate!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1885")

    label("loc_17AE")


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

    label("loc_1885")

    Jump("loc_3504")

    label("loc_188A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1962")

    ChrTalk(
        0x8,
        (
            "The sun's already setting.\x01",
            "Maybe I'll try my luck at some of the\x01",
            "ponds out on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have a real gut feeling that I'm going to\x01",
            "catch myself a whopper during tonight's\x01",
            "fishing session.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_1962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(
        0x8,
        (
            "Odd... I can't seem to contact\x01",
            "Joachim...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He promised me last night that we'd\x01",
            "go night fishing today, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(...He's probably too engrossed in\x01",
            "researching the drug's composition.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Given how Doc acts, I bet you're\x01",
            "right on the money, Lloyd.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B87")

    ChrTalk(
        0x8,
        (
            "Y'know, gold salmon are kinda like phantoms.\x01",
            "Heard they only swim around the waters in the\x01",
            "Mainz area, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Their flowing, sleek figure and\x01",
            "those shining, golden scales...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The gold salmon truly IS\x01",
            "the salmon to end all salmon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D28")

    ChrTalk(
        0x8,
        "Big news, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This morning, Joachim fought hard and\x01",
            "managed to catch the biggest, most\x01",
            "impressive noble carp I've ever seen!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "His achievement has earned him the rank\x01",
            "of Master Fisher. He sure caught up to me\x01",
            "quick, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI do not think Doctor Guenter has changed\x01",
            "one bit since we first met him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. That sounds like a good story to tell\x01",
            "Cecile later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DA8")

    label("loc_1D28")


    ChrTalk(
        0x8,
        "Joachim has been promoted to Master Fisher.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I might have to start calling him\x01",
            "Master Joachim from now on, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA8")

    Jump("loc_3504")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1E4D")

    ChrTalk(
        0x8,
        (
            "Hey, Lloyd. I haven't seen you\x01",
            "pop in here much lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You better be fishing at least once a\x01",
            "day so those skills don't get rusty, kid!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_1E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_20D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2014")

    ChrTalk(
        0x8,
        (
            "Truth be told, I'm thinking of hosting a\x01",
            "fishing competition during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was thinking of calling in a Master Fisherman\x01",
            "from Liberl here to help out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "Oh, right! Your name's also Lloyd, isn't it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! Truly a great name for\x01",
            "great anglers alike!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FH-Huh? What are you laughing about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't worry about it, kid. I haven't decided\x01",
            "if I want to do it yet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20CF")

    label("loc_2014")


    ChrTalk(
        0x8,
        (
            "I was considering calling up a Master\x01",
            "Fisherman from Liberl here to help host\x01",
            "a competition during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We'll make him our special guest.\x01",
            "Bwahaha! I'm getting excited!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CF")

    Jump("loc_3504")

    label("loc_20D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BA")

    ChrTalk(
        0x8,
        (
            "I'd recommend casting your line over on\x01",
            "Ursula Road around this time of the year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "One of our comrades in rods actually works\x01",
            "at St. Ursula Medical College, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He keeps telling me about how he ditches\x01",
            "work to go up the road and catch some fish.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0005FThere's someone who loves to fish that\x01",
            "much at St. Ursula Medical College?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FDude, you think it's him?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2360")

    label("loc_22BA")


    ChrTalk(
        0x8,
        (
            "I'd recommend casting your line over on\x01",
            "Ursula Road around this time of the year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you want to test your mettle, Lloyd,\x01",
            "try catching the fish over there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2360")

    Jump("loc_3504")

    label("loc_2365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_242A")

    ChrTalk(
        0x8,
        (
            "If you aren't reeling in what you want,\x01",
            "try changing your rod and bait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That'll drastically change what fish you catch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "It does require some trial and error, mind you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_242A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263F")

    ChrTalk(
        0x8,
        "Welcome to the Fisherman's Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How have your fish-scapades been going,\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIt's been so-so, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, yeah? I guess I have heard that the\x01",
            "CPD likes to keep you detectives busy.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D6")

    ChrTalk(
        0x8,
        (
            "Well, if you manage to make any fine catches,\x01",
            "don't forget to bring 'em to me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do enough work to earn a promotion,\x01",
            "I'll award you a wonderful prize, believe me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2637")

    label("loc_25D6")


    ChrTalk(
        0x8,
        (
            "If you manage to snag any whoppers,\x01",
            "come report 'em to me. I'll be waiting\x01",
            "in anticipation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2637")

    SetScenarioFlags(0x0, 0)
    Jump("loc_274B")

    label("loc_263F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26FF")

    ChrTalk(
        0x8,
        (
            "The requirement to pass the\x01",
            "Rank Certification Exam is to\x01",
            "catch a certain number of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you manage to make any fine catches,\x01",
            "don't forget to bring 'em to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274B")

    label("loc_26FF")


    ChrTalk(
        0x8,
        (
            "Hey, Lloyd. If you manage to snag any\x01",
            "whoppers, come report 'em to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274B")

    Jump("loc_3504")

    label("loc_2750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEF")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(
        0xA,
        "You hear the news, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our guild managed to reel us in\x01",
            "another member yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, really? Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, this lass is quite the angler.\x01",
            "Might already be as good as me!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xA,
        (
            "Her name's Estelle, and she's a\x01",
            "famous bracer. Haven't you seen\x01",
            "her in any magazines before?\x02",
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
        0x8,
        (
            "I got invited to go fishing with her once--she\x01",
            "was a real pro. All that bracer work must\x01",
            "have really sharpened her reflexes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha... A formidable enemy\x01",
            "stands in your way, eh, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FShe already was one BEFORE\x01",
            "this little revelation...\x01",
            "(Are you kidding me? She fishes, too?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FEstelle doesn't have any brakes on\x01",
            "her at all, does she?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_2BFF")

    label("loc_2AEF")


    ChrTalk(
        0x8,
        (
            "Well, I've heard Estelle's had a knack\x01",
            "for fishing even back when she was\x01",
            "growing up in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And hey, speaking of Liberl, that's where\x01",
            "the Fisherman's Guild was founded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, Lloyd, just because you're busy doesn't\x01",
            "mean you can start neglecting fishing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFF")

    Jump("loc_3504")

    label("loc_2C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_30B4")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(
        0x8,
        (
            "The Fisherman's Guild is a prestigious\x01",
            "organization created in order to spread\x01",
            "the culture and greatness of fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Due to our strong sense of purpose and calling,\x01",
            "our guild established the Rank Certification Exam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, kid. If your young brain doesn't\x01",
            "understand anything, then ask your old pal!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AF")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD8")

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
            "All right, then, kid! Just lemme know when you're good\x01",
            "to go. We'll even throw a contest to celebrate!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_30AF")

    label("loc_2FD8")


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

    label("loc_30AF")

    Jump("loc_3504")

    label("loc_30B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_31DF")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x8,
        (
            "Sounds like Kopan's gone and bagged\x01",
            "himself another big one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We gotta put a stop to this man, Peter.\x01",
            "He keeps making us look like chumps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "For sure. I'm already getting antsy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hahaha. Shall we unleash our\x01",
            "true power during tonight's\x01",
            "fishing session?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_3504")

    label("loc_31DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BF")

    ChrTalk(
        0x8,
        (
            "Peter, you know I can hardly refuse\x01",
            "when it comes to showing off my\x01",
            "master techniques!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! How about we hold ourselves a\x01",
            "tournament near the stream, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105F(Who are these people?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3504")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3406")

    ChrTalk(
        0x8,
        (
            "The Fisherman's Guild is always\x01",
            "trying to reel in new recruits.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "Any interest, kid? You want to be\x01",
            "our comrade in rods?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We welcome people of all experience\x01",
            "levels to come and join our ranks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSorry, I'm kind of in the middle of working.\x01",
            "(There's no way I'd have time for this.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3504")

    label("loc_3406")


    ChrTalk(
        0x8,
        (
            "The Fisherman's Guild is always\x01",
            "trying to reel in new recruits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you think we're baiting you, then maybe\x01",
            "you should join and see for yourself!\x02",
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

    label("loc_3504")

    Return()

    # Function_5_117D end

    def Function_6_3505(): pass

    label("Function_6_3505")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_35A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3565")

    ChrTalk(
        0xFE,
        "Here's your food, ya beauts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eat till you're full!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_35A3")

    label("loc_3565")


    ChrTalk(
        0xFE,
        (
            "Still a few red flies left over,\x01",
            "but that's all for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A3")

    Jump("loc_3BE0")

    label("loc_35A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_35B6")
    Jump("loc_3BE0")

    label("loc_35B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_375E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367D")

    ChrTalk(
        0xFE,
        "Ah, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you looking for the branch manager?\x01",
            "He's downstairs if you wanna talk to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't hurt to ask about the\x01",
            "Rank Certification Exam, y'know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_3759")

    label("loc_367D")


    ChrTalk(
        0xFE,
        (
            "Dependin' on the kind of bait you use,\x01",
            "you'll have a different pool of fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're havin' trouble reelin' in the fish\x01",
            "you want, try switchin' your bait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's all just a simple game of trial and error.\x02",
    )

    CloseMessageWindow()

    label("loc_3759")

    Jump("loc_3BE0")

    label("loc_375E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A4")

    ChrTalk(
        0xFE,
        "Huh, did you guys return by bus, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess we weren't on the same bus, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I already let the branch manager know the news.\x01",
            "He's downstairs, so go to him if you got any\x01",
            "questions or concerns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't hurt to ask about the\x01",
            "Rank Certification Exam, y'know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_395F")

    label("loc_38A4")


    ChrTalk(
        0xFE,
        "Howdy there, folks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm here pretty often, so don't be afraid to\x01",
            "come to me if ya got any questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a sweet deal, I'll let ya know about\x01",
            "our recommended fishin' spots.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395F")

    Jump("loc_3BE0")

    label("loc_3964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3972")
    Jump("loc_3BE0")

    label("loc_3972")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3D")

    ChrTalk(
        0xFE,
        (
            "Why do I always get stuck cleanin'\x01",
            "the fish tank?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* This is so lame. What a drag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FThat's one massive fish tank...\x01",
            "(What the heck IS this place?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AA9")

    label("loc_3A3D")


    ChrTalk(
        0xFE,
        (
            "You impressed? This tank was\x01",
            "custom made by Genten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's 'cause our branch manager's pretty rich.\x02",
    )

    CloseMessageWindow()

    label("loc_3AA9")

    Jump("loc_3BE0")

    label("loc_3AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B74")

    ChrTalk(
        0xFE,
        (
            "Our branch of the Fisherman's Guild is for\x01",
            "all of Crossbell's fishing enthusiasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're lookin' at one of 'em right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Member No. 3, Kopan.\x01",
            "Rank, Master Fisher.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BE0")

    label("loc_3B74")


    ChrTalk(
        0xFE,
        (
            "I'm also a member, but I'm not the\x01",
            "best catch, if you know what I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Pretty lame of me, right?\x02",
    )

    CloseMessageWindow()

    label("loc_3BE0")

    TalkEnd(0xFE)
    Return()

    # Function_6_3505 end

    def Function_7_3BE4(): pass

    label("Function_7_3BE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C0E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_3C0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3EAC")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2D")

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd. You plannin' on getting\x01",
            "some fishin' in tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hope you catch some big ones!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a feelin' you could go places, Lloyd.\x01",
            "Might just be a gut feeling, but I think you could\x01",
            "even surpass the rank of Master Fisher.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DBB")

    label("loc_3D2D")


    ChrTalk(
        0xFE,
        (
            "I have a feelin' you might someday surpass\x01",
            "being a Master Fisher, Lloyd. Anyway, I hope\x01",
            "you reel in some good ones during night fishing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBB")

    Jump("loc_3EA7")

    label("loc_3DC0")


    ChrTalk(
        0xFE,
        "I always knew ya had it in ya, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't believe you managed to become a\x01",
            "Divine Angler so quickly after joinin' us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Let's keep doin' everything we can to\x01",
            "improve this branch, eh, Mr. Divine Angler\x01",
            "of Water?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA7")

    Jump("loc_4B5D")

    label("loc_3EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3FB8")

    ChrTalk(
        0xFE,
        (
            "The guest we brought in from Liberl\x01",
            "went back home last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sad to see him go. My match with him was\x01",
            "a great experience for my fishin' career.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like I'm going to have to keep honin' my\x01",
            "skills if I want to stand my ground next time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5D")

    label("loc_3FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_40A2")

    ChrTalk(
        0xFE,
        (
            "I'm planning to go out and practice\x01",
            "casting my line for a few hours today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like Estelle's been provin' her\x01",
            "worth around Crossbell's regular\x01",
            "fishin' spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. I can't let her show me up\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5D")

    label("loc_40A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_422C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417B")

    ChrTalk(
        0xFE,
        (
            "Hey, Lloyd. You tried fishin' on\x01",
            "the West Crossbell Highway yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I'm lovin' all these extra orbal buses\x01",
            "in Crossbell. It's so much easier to go fishing\x01",
            "wherever you want now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4227")

    label("loc_417B")


    ChrTalk(
        0xFE,
        (
            "Oh, apparently, Kopan's out on the\x01",
            "Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd bet he's at that waterfall near\x01",
            "the bus stop along the road.\x01",
            "It's actually his favorite fishin' spot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4227")

    Jump("loc_4B5D")

    label("loc_422C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E3")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    ChrTalk(
        0xA,
        "You hear the news, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our guild managed to reel us in\x01",
            "another member yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, really? Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, this lass is quite the angler.\x01",
            "Might already be as good as me!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xA,
        (
            "Her name's Estelle, and she's a\x01",
            "famous bracer. Haven't you seen\x01",
            "her in any magazines before?\x02",
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
        0x8,
        (
            "I got invited to go fishing with her once, and she\x01",
            "was a real pro. All that time as a bracer must\x01",
            "have sharpened her reflexes nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha... A formidable enemy\x01",
            "stands in your way, eh, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FShe already was one BEFORE\x01",
            "this little revelation...\x01",
            "(Are you kidding me? She fishes, too?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FEstelle doesn't have any brakes on\x01",
            "her at all, does she?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_46B7")

    label("loc_45E3")


    ChrTalk(
        0xFE,
        (
            "Rumor has it that Estelle was a\x01",
            "high-ranking fisher back in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know you're pretty busy with your job, but\x01",
            "you should try and stop by sometime for\x01",
            "a fishing challenge. Gotta try it at least once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B7")

    Jump("loc_4B5D")

    label("loc_46BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4A19")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B0")

    ChrTalk(
        0xFE,
        "I heard about it from Kopan!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I'm so pumped that we got ourselves\x01",
            "another new member.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd better tell us whenever you\x01",
            "make some great catches, okay?!\x01",
            "We'll be lookin' forward to it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_481C")

    label("loc_47B0")


    ChrTalk(
        0xFE,
        (
            "You'd better tell us whenever you\x01",
            "make some great catches, okay?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'll be lookin' forward to it!\x02",
    )

    CloseMessageWindow()

    label("loc_481C")

    Jump("loc_4A14")

    label("loc_4821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4972")

    ChrTalk(
        0xFE,
        (
            "Congrats on earning the title of\x01",
            "Divine Angler, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Fisherman's Guild has a branch both\x01",
            "in Liberl and Crossbell, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...there's only ever been two people to\x01",
            "earn the title of Divine Angler, and\x01",
            "that's including you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Divine Angler in Liberl is supposedly\x01",
            "some female bracer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A14")

    label("loc_4972")


    ChrTalk(
        0xFE,
        (
            "Lloyd, congrats on earning the\x01",
            "title of Divine Angler!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Let's keep doin' everything we can to\x01",
            "improve this branch, eh, Mr. Divine Angler\x01",
            "of Water?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A14")

    Jump("loc_4B5D")

    label("loc_4A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4A2A")
    Call(0, 4)
    Jump("loc_4B5D")

    label("loc_4A2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF4")

    ChrTalk(
        0xFE,
        (
            "Heh. Fishing by the streams up\x01",
            "on Mainz Mountain Path, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm super excited just thinking about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(I think they're busy discussing\x01",
            "fishing with each other...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B5D")

    label("loc_4AF4")


    ChrTalk(
        0xFE,
        (
            "Come back to the Fisherman's Guild\x01",
            "whenever you've got the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We'd be glad to welcome ya.\x02",
    )

    CloseMessageWindow()

    label("loc_4B5D")

    TalkEnd(0xFE)
    Return()

    # Function_7_3BE4 end

    def Function_8_4B61(): pass

    label("Function_8_4B61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(470, 1400, 310, 0)
    MoveCamera(45, 33, 0, 0)
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
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(1850, 1400, 1760, 3000)
    MoveCamera(45, 34, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20100, 3000)

    def lambda_4C52():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C52)

    def lambda_4C6C():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C6C)

    def lambda_4C86():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C86)

    def lambda_4CA0():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4CA0)

    def lambda_4CBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4CBA)

    def lambda_4CCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4CCB)

    def lambda_4CDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4CDC)

    def lambda_4CED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4CED)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#5P#0005FThis is the building directly to the right of\x01",
            "the Bracer Guild... Wasn't it supposed to be\x01",
            "vacant, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(3480, 1400, 3380, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_0D()
    Sleep(700)

    ChrTalk(
        0x103,
        (
            "#5P#0200FIt does not display any signs of vacancy\x01",
            "at all. Quite the opposite, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FWe should probably bug reception\x01",
            "to see what the deal is.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    ClearMapFlags(0x10000000)
    OP_29(0x3, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_8_4B61 end

    def Function_9_4EB0(): pass

    label("Function_9_4EB0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_68(5760, 1300, 6920, 0)
    MoveCamera(19, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22710, 0)
    SetChrPos(0x101, 4560, 0, 6480, 45)
    SetChrPos(0x102, 5370, 0, 5660, 45)
    SetChrPos(0x103, 3590, 0, 5480, 45)
    SetChrPos(0x104, 4390, 0, 4680, 45)
    OP_93(0x8, 0x87, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#11PMan, I wanna go on another\x01",
            "fishin' trip sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBwahaha! I bet you would, wouldn't ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FExcuse us, sir. We're with the--\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#11POh, you kids all interested in joining?\x01",
            "Bwahaha! I'll gladly accept you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PWelcome to the Fisherman's Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PBoy, am I glad to see younger\x01",
            "fishing enthusiasts joining us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        "#6P#0305FJoinin' the...Fisherman's Guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0006FPardon me, sir, but what exactly is this place?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh, sorry about that, kid. This is the gathering\x01",
            "grounds of fishing enthusiasts--the Crossbell\x01",
            "branch of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHey, kid with the blue and white jacket there.\x01",
            "You look like you've handled a few rods before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can sniff out talent from a selge away.\x01",
            "How 'bout it, kid? Lookin' to get your bait on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FWhat? I-I mean, sure, I used to go fishing\x01",
            "back when I was a kid...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#0011FNo, snap out of it! We're currently on duty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0109F(I'm impressed at how easily he could\x01",
            "tell Lloyd has fishing experience.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203F(These old men mystify me.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(*sigh* Man, that caught me off guard.)\x02\x03",
            "#0000FAnyway, this might go without saying,\x01",
            "but this building isn't vacant, right?\x02\x03",
            "Because according to the records from\x01",
            "City Hall, this place should be unoccupied...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PWhat? Of course it's not. That's impossible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PAs you can see, we're in the process\x01",
            "of planning our next fishing event!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHmm, while we're on the topic of vacancies...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11PThere's an apartment complex by the name\x01",
            "of Acacia down the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PPretty sure there was a vacant room in there.\x01",
            "That's what you're looking for, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou'll find the Acacia directly to the left\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
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

    def lambda_57A4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57A4)

    def lambda_57B1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57B1)

    def lambda_57BE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57BE)

    def lambda_57CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_57CB)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#0303F#12PThe actual vacancy's two buildings away?\x01",
            "You're tellin' me the records were botched?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FThat seems to be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FIn that case, we should head there and\x01",
            "confirm it so that City Hall can update\x01",
            "their records.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0x0, 4780, 0, 5260, 225)
    SetChrPos(0x1, 4780, 0, 5260, 225)
    SetChrPos(0x2, 4780, 0, 5260, 225)
    SetChrPos(0x3, 4780, 0, 5260, 225)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_29(0x3, 0x1, 0x4)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_9_4EB0 end

    def Function_10_5941(): pass

    label("Function_10_5941")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59C2")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_5AEA")

    label("loc_59C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A34")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_5AEA")

    label("loc_5A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA6")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_5AEA")

    label("loc_5AA6")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_5AEA")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_10_5941 end

    def Function_11_5B0E(): pass

    label("Function_11_5B0E")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2C")
    Jump("loc_5B66")

    label("loc_5B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B49")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_5B66")

    label("loc_5B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B66")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_5B66")

    label("loc_5B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B79")
    Jump("loc_5BA9")

    label("loc_5B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8C")
    Jump("loc_5BA9")

    label("loc_5B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9F")
    Jump("loc_5BA9")

    label("loc_5B9F")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_5BA9")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_11_5B0E end

    def Function_12_5BCB(): pass

    label("Function_12_5BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_600C")

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
            "With each promotion in rank you achieve, we'll\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E9F")

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
    Jump("loc_6004")

    label("loc_5E9F")


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

    label("loc_6004")

    SetScenarioFlags(0x69, 6)
    Jump("loc_897F")

    label("loc_600C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_656F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6423")
    Call(0, 10)
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
            "Achieved the rank of Hobbyist Fisher!\x02",
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
            "This thing's my prized straw hat, you see.\x01",
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
    Call(0, 11)
    Jump("loc_656A")

    label("loc_6423")


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

    label("loc_656A")

    Jump("loc_897F")

    label("loc_656F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6BE5")
    Call(0, 10)
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
            "Achieved the rank of Professional Fisher!\x02",
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
            "(It's another one of Cerdan's stories... It's going\x01",
            "to be a long one. I can feel it.)\x02\x03",
            "#0000FBut, wait. Why'd you stop in Liberl for work?\x01",
            "Were you some kind of trader?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bwahaha! No, no, not at all! I was there on\x01",
            "behalf of my father, himself a businessman.\x02",
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
    Call(0, 11)
    Jump("loc_6CDB")

    label("loc_6BE5")


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

    label("loc_6CDB")

    Jump("loc_897F")

    label("loc_6CE0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7383")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7283")
    Call(0, 10)
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
            "Y'know, I actually had some struggles\x01",
            "becoming a 2nd Class Fisher.\x02",
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
    Call(0, 11)
    Jump("loc_737E")

    label("loc_7283")


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

    label("loc_737E")

    Jump("loc_897F")

    label("loc_7383")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7A8D")
    Call(0, 10)
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
    Call(0, 11)
    Jump("loc_7BF0")

    label("loc_7A8D")


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

    label("loc_7BF0")

    Jump("loc_897F")

    label("loc_7BF5")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_812A")
    Call(0, 10)
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
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_82A0")

    label("loc_812A")


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
            "you. You have to catch 23 unique kinds of fish\x01",
            "to qualify.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This'll be your toughest challenge yet.\x01",
            "You must catch a noble carp and\x01",
            "a gold salmon.\x02",
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

    label("loc_82A0")

    Jump("loc_897F")

    label("loc_82A5")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8840")
    Call(0, 10)
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
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_897F")

    label("loc_8840")


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

    label("loc_897F")

    Return()

    # Function_12_5BCB end

    def Function_13_8980(): pass

    label("Function_13_8980")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89A5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89C0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89DB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_89F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_89F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A11")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A2C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A62")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A7D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A98")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AB3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8ACE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ACE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AE9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B1F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B3A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B55")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B70")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B8B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BA6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BC1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BDC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C12")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C12")

    Return()

    # Function_13_8980 end

    def Function_14_8C13(): pass

    label("Function_14_8C13")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_8CDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CDA")
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

    label("loc_8CDA")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_14_8C13 end

    SaveToFile()

Try(main)
