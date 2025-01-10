from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 260000, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "Old Man Quint",          # 1
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
    ))

    DeclNpc(260260,  0,       250,     0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_1A0",          # 01, 1
        "Function_2_1CB",          # 02, 2
        "Function_3_31C",          # 03, 3
        "Function_4_32F",          # 04, 4
        "Function_5_F54",          # 05, 5
        "Function_6_1264",         # 06, 6
        "Function_7_1378",         # 07, 7
        "Function_8_1DA1",         # 08, 8
        "Function_9_23CE",         # 09, 9
        "Function_10_2654",        # 0A, 10
        "Function_11_2687",        # 0B, 11
        "Function_12_26B7",        # 0C, 12
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_128"),
        (1, "loc_134"),
        (2, "loc_140"),
        (3, "loc_14C"),
        (4, "loc_158"),
        (5, "loc_164"),
        (6, "loc_170"),
        (SWITCH_DEFAULT, "loc_17C"),
    )


    label("loc_128")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_134")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_140")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_14C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_158")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_164")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_170")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_17C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_188")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_19F")

    Return()

    # Function_0_E8 end

    def Function_1_1A0(): pass

    label("Function_1_1A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_1A0")

    label("loc_1CA")

    Return()

    # Function_1_1A0 end

    def Function_2_1CB(): pass

    label("Function_2_1CB")

    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9")
    Event(0, 9)

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_209")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204")
    SetChrFlags(0x8, 0x80)

    label("loc_204")

    Jump("loc_31B")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_242")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_23D")

    Jump("loc_31B")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_276")

    Jump("loc_31B")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_28E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B4")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_31B")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_31B")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_31B")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_304")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_31B")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_31B")

    label("loc_31B")

    Return()

    # Function_2_1CB end

    def Function_3_31C(): pass

    label("Function_3_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32E")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_32E")

    Return()

    # Function_3_31C end

    def Function_4_32F(): pass

    label("Function_4_32F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Thanks to you, I was able to give my\x01",
            "friend a worthwhile visit. I can't thank\x01",
            "you enough for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something else ever comes up, I'll\x01",
            "make sure to contact you again.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422")
    Call(0, 8)
    Return()

    label("loc_422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57A")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Double-checking requests gives off an air\x01",
            "of amateurism, but don't let it bother you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've jotted down the locations of the\x01",
            "flowers in your notebook, right? Be sure\x01",
            "to check it before you come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once you've gathered all three flowers,\x01",
            "I'd like you to bring them back to me.\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_593")
    Call(0, 5)
    Return()

    label("loc_593")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7EA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")

    ChrTalk(
        0xFE,
        (
            "You know, I can't help but think of Guy\x01",
            "on nights like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, when you finally become an\x01",
            "adult...let's share a few drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll treat you to some of his favorites.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0004FI'm already looking forward to it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEA, 0)
    Jump("loc_74B")

    label("loc_6A5")


    ChrTalk(
        0xFE,
        (
            "On his days off, Guy would drop by\x01",
            "here from time to time and we'd drink\x01",
            "the night away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, when you finally become an\x01",
            "adult, let's share a few drinks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74B")

    Jump("loc_7E5")

    label("loc_750")


    ChrTalk(
        0xFE,
        (
            "You know, I can't help but think of him\x01",
            "on nights like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, it looks like I got caught up in\x01",
            "some gossip.\x01",
            "You can forget all that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E5")

    Jump("loc_F50")

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_878")

    ChrTalk(
        0xFE,
        "Well, then... Time to start the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I lost most of my family ages ago. Caring\x01",
            "for the graves is all I have left now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F50")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8F9")

    ChrTalk(
        0xFE,
        (
            "Many fellow Crossbellans suffer from\x01",
            "wounds so great, they never mention them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try to keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F50")

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_907")
    Jump("loc_F50")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_915")
    Jump("loc_F50")

    label("loc_915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_923")
    Jump("loc_F50")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A0C")

    ChrTalk(
        0xFE,
        (
            "There was a big crowd of folks at the harbor\x01",
            "while I was doing some grocery shopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were probably heading to Mishelam\x01",
            "to blow off some steam, if I were to guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If only I was a wee bit younger...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F50")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A1A")
    Jump("loc_F50")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(
        0xFE,
        (
            "There was this lady visiting a grave during\x01",
            "the festival, and I suggested that she try\x01",
            "to have some fun instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "In hindsight, that was insensitive of me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F50")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")

    ChrTalk(
        0xFE,
        (
            "Yesterday's Mass was a lot more crowded\x01",
            "than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most of them stopped by the cemetery\x01",
            "afterwards to pay their respects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been 70 years since our state was founded.\x01",
            "I imagine this year in particular will be quite\x01",
            "special for us Crossbellans.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C7D")

    label("loc_BFB")


    ChrTalk(
        0xFE,
        (
            "It's been 70 years since our state was founded.\x01",
            "I imagine this year in particular will be quite\x01",
            "special for us Crossbellans.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7D")

    Jump("loc_F50")

    label("loc_C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C90")
    Jump("loc_F50")

    label("loc_C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5F")

    ChrTalk(
        0xFE,
        (
            "You know, the Anniversary Festival\x01",
            "is coming up next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time really does fly by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps that's because I choose to spend\x01",
            "my days in a secluded place like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE2")

    label("loc_D5F")


    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival is already right\x01",
            "on us, is it...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I still remember last year's festival as if\x01",
            "it was yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE2")

    Jump("loc_F50")

    label("loc_DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_F50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDF")

    ChrTalk(
        0xFE,
        (
            "Crossbell's problematic position between\x01",
            "Erebonia and Calvard means we're often\x01",
            "caught up in their strife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many have already fallen to the raging\x01",
            "turbulence of this era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do offer a prayer for them, please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F50")

    label("loc_EDF")


    ChrTalk(
        0xFE,
        (
            "Many have lost their lives over the\x01",
            "development of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do offer a prayer for them, please.\x02",
    )

    CloseMessageWindow()

    label("loc_F50")

    TalkEnd(0xFE)
    Return()

    # Function_4_32F end

    def Function_5_F54(): pass

    label("Function_5_F54")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FFC")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_FFC")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1175")

    ChrTalk(
        0x101,
        "#12P#0000FMr. Quint? Sorry to bother you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PThe police?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FThat's right, sir. We're from the\x01",
            "Special Support Section, coming\x01",
            "about your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmmm, well, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI want you to bring me three different\x01",
            "kinds of flowers for an offering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PCan you go on and fetch them now?\x02",
    )

    CloseMessageWindow()
    OP_29(0x2E, 0x1, 0x0)
    Jump("loc_1216")

    label("loc_1175")


    ChrTalk(
        0x8,
        (
            "#5PAnything else you need to take\x01",
            "care of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI want you to bring me three different\x01",
            "kinds of flowers for an offering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PCan you do that for me?\x02",
    )

    CloseMessageWindow()

    label("loc_1216")

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    Call(0, 7)

    label("loc_122B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1245")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1245")

    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_F54 end

    def Function_6_1264(): pass

    label("Function_6_1264")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1377")

    ChrTalk(
        0x101,
        (
            "#12P#0006FI'm terribly sorry, but we have some\x01",
            "urgent business to attend to first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThat so? Well, I can wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PLet me know when you're able to start,\x01",
            "and then I'll give the finer details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1377")

    Return()

    # Function_6_1264 end

    def Function_7_1378(): pass

    label("Function_7_1378")


    ChrTalk(
        0x101,
        "#12P#0000FWe can start right away, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PGood deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'll get straight to the point. Got\x01",
            "pen and paper on you? I'll tell you\x01",
            "which flowers you need to collect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PReady for the first one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FYes.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#0000FTio, mind writing it down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203FRoger.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PFirst, the Leevus Flower. You'll find them\x01",
            "blooming near the police academy on\x01",
            "West Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSecond, we have the Requium Flower.\x01",
            "I believe Tallys' General Store on\x01",
            "West Street sells them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PFinally, there's the Fainel Flower.\x01",
            "You know that watchtower near Crossbell's\x01",
            "east exit? They're usually at the foot of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThey tend to bloom near similar flowers, too,\x01",
            "so be careful to not overlook them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POnce you're done, I'd like you to bring them\x01",
            "all to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FNoted.\x02\x03",
            "#0200FMay I ask why you specifically want\x01",
            "these three flowers?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#0100FYellow, blue, and white symbolize the\x01",
            "repose of the soul here in Crossbell.\x02\x03",
            "Flowers of these colors are arranged\x01",
            "into bouquets, which are traditionally\x01",
            "offered during funerals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FIs this that 'language of flowers' thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI believe this is slightly different from\x01",
            "floriography, Randy.\x02\x03",
            "#0200FIt would not be a stretch to claim that these\x01",
            "flowers resemble Crossbell's state colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(I think a tricolored bouquet was\x01",
            "offered at Guy's funeral, too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P...\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FU-Um, sir...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0305FWhat's with the silent treatment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, it's just that I'm a bit disappointed\x01",
            "that your generation is so unaware of\x01",
            "these old traditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut on the other hand, that ignorance should\x01",
            "provide you with a bit of an extra challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FS-Sorry about that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHaha, sorry man. I ain't even from\x01",
            "Crossbell to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmm, fine, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYou know what to do. Off you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FU-Understood!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D29")

    ChrTalk(
        0x10A,
        "#6P#0603F...\x02",
    )

    CloseMessageWindow()

    def lambda_1B83():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B83)
    Sleep(50)

    def lambda_1B93():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B93)
    Sleep(50)

    def lambda_1BA3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BA3)
    Sleep(50)

    def lambda_1BB3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BB3)

    ChrTalk(
        0x101,
        (
            "#11P#0012FUmm, you heard the situation,\x01",
            "Dudley. So...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#0600FHmph. Yes, I heard perfectly clear.\x01",
            "Someone seems to have forgotten that\x01",
            "we're in a tad bit of a hurry.\x02\x03",
            "#0606FWhatever. You can't exactly turn down\x01",
            "the request at this point.\x02\x03",
            "#0600FMake haste, not mistakes so we can\x01",
            "resume our investigation ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FWill do, Mr. First Division!\x02",
    )

    CloseMessageWindow()

    label("loc_1D29")

    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Collecting Flowers for Resting Places]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2E, 0x1, 0x1)
    Return()

    # Function_7_1378 end

    def Function_8_1DA1(): pass

    label("Function_8_1DA1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E52")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1E52")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0000FWe're back, Mr. Quint.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmm. Faster than I expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDid you get the flowers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes. Feel free to give them a look.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x349),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02\x03",
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02\x03",
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x34B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x349, 1)
    SubItemNumber(0x34A, 1)
    SubItemNumber(0x34B, 1)

    ChrTalk(
        0x8,
        "#5PThese are the ones, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYour efforts are much appreciated,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FJust doing our jobs, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FBut man, we ran all over just to pick some\x01",
            "flowers.\x02\x03",
            "Even Tallys' had run out! What are the odds\x01",
            "of that happenin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FWell, we still managed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FSir, may I ask you something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PDepends on the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FIt's not particularly common to gather\x01",
            "these three specific flowers except for\x01",
            "funerals nowadays...\x02\x03",
            "#0100FWhat exactly did you need them for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou're right that there's\x01",
            "no funeral at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, since you helped me pick them, come\x01",
            "with me, and we'll offer them together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYou'll get your answer afterwards.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 11)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 11)
    BeginChrThread(0x104, 3, 0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22B1")
    Sleep(200)

    def lambda_22A9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_22A9)

    label("loc_22B1")

    WaitChrThread(0x8, 3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#0205FWhat is he talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FBeats me.\x02\x03",
            "#0003FI guess we'll see when we get there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23B3")

    ChrTalk(
        0x10A,
        "#6P#0603F(It can't be...)\x02",
    )

    CloseMessageWindow()

    label("loc_23B3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2E, 0x1, 0x7)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1DA1 end

    def Function_9_23CE(): pass

    label("Function_9_23CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2477")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2477")

    OP_93(0x8, 0xB4, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(30720, 3000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PThanks to you, I was able to give my\x01",
            "friend a worthwhile visit. I can't thank\x01",
            "you enough for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf something else ever comes up, I'll\x01",
            "make sure to contact you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FWe'll be waiting. Goodbye, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Collecting Flowers for Resting Places]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_29(0x2E, 0x4, 0x10)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2651")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2651")

    EventEnd(0x5)
    Return()

    # Function_9_23CE end

    def Function_10_2654(): pass

    label("Function_10_2654")


    def lambda_2659():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2659)
    Sleep(2500)

    def lambda_2676():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2676)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_2654 end

    def Function_11_2687(): pass

    label("Function_11_2687")


    def lambda_268C():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_268C)
    WaitChrThread(0xFE, 1)

    def lambda_26AA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26AA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_2687 end

    def Function_12_26B7(): pass

    label("Function_12_26B7")


    def lambda_26BC():
        OP_98(0xFE, 0x12C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26BC)
    WaitChrThread(0xFE, 1)

    def lambda_26DA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26DA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_26B7 end

    SaveToFile()

Try(main)
