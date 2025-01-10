from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0320.bin",                # FileName
        "c0320",                    # MapName
        "c0320",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0320",                  # 0
        "Representative Campbell",# 1
        "Republican Representative",# 2
        "Republican Representative",# 3
        "Carla",                  # 4
        "Marsha",                 # 5
    ))

    AddCharChip((
        "chr/ch27702.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch27802.itc",                   # 02
        "chr/ch33200.itc",                   # 03
        "chr/ch34500.itc",                   # 04
    ))

    DeclNpc(0,       250,     46110,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2490,   0,       48869,   45,   389,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(2299,    250,     43630,   270,  341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(43490,   59,      3440,    135,  389,  0x0, 0,   3,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-44409,  0,       10199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(45950,   60,      1790,    1500,    46410,   1000,    1270,    0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_248",          # 01, 1
        "Function_2_273",          # 02, 2
        "Function_3_29E",          # 03, 3
        "Function_4_311",          # 04, 4
        "Function_5_383",          # 05, 5
        "Function_6_9B1",          # 06, 6
        "Function_7_BDB",          # 07, 7
        "Function_8_1761",         # 08, 8
        "Function_9_1C0C",         # 09, 9
        "Function_10_1FAD",        # 0A, 10
        "Function_11_33A2",        # 0B, 11
        "Function_12_3F02",        # 0C, 12
        "Function_13_4AEC",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1D0"),
        (1, "loc_1DC"),
        (2, "loc_1E8"),
        (3, "loc_1F4"),
        (4, "loc_200"),
        (5, "loc_20C"),
        (6, "loc_218"),
        (SWITCH_DEFAULT, "loc_224"),
    )


    label("loc_1D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_1F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_200")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_20C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_224")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_230")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_230")

    label("loc_247")

    Return()

    # Function_0_190 end

    def Function_1_248(): pass

    label("Function_1_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_272")
    OP_94(0xFE, 0xFFFFF57E, 0xC1DE, 0xFFFFEFFC, 0xB4AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_248")

    label("loc_272")

    Return()

    # Function_1_248 end

    def Function_2_273(): pass

    label("Function_2_273")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29D")
    OP_94(0xFE, 0xAE56, 0xD70, 0xA320, 0x67C, 0x3E8)
    Sleep(300)
    Jump("Function_2_273")

    label("loc_29D")

    Return()

    # Function_2_273 end

    def Function_3_29E(): pass

    label("Function_3_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_2B9")
    ClearChrFlags(0xC, 0x80)

    label("loc_2B9")

    Jump("loc_2FE")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DB")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_2FE")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x8, 0x80)
    SetChrSubChip(0xA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0xC, 0x80)

    label("loc_2FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)

    label("loc_310")

    Return()

    # Function_3_29E end

    def Function_4_311(): pass

    label("Function_4_311")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C")
    OP_66(0x0, 0x1)

    label("loc_34C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_365")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_36B")

    label("loc_365")

    OP_10(0x0, 0x1)
    OP_10(0x7, 0x0)

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_382")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_382")

    label("loc_382")

    Return()

    # Function_4_311 end

    def Function_5_383(): pass

    label("Function_5_383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD")
    Call(0, 10)
    Return()

    label("loc_3AD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441")
    Jump("loc_48B")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_461")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_461")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_481")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B")

    label("loc_481")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_60E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_549")

    ChrTalk(
        0xFE,
        (
            "I offer you my thanks for returning\x01",
            "my foolish daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe I've said my piece.\x01",
            "Please leave immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_609")

    label("loc_549")


    ChrTalk(
        0xFE,
        (
            "Hmph. I knew this city's police force\x01",
            "was comprised of buffoons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter. I have her contact address,\x01",
            "so I will make her come back by force.\x01",
            "Her complaints will fall on deaf ears.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_609")

    Jump("loc_9A9")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886")

    ChrTalk(
        0xFE,
        (
            "Between the diet meeting and the Heiyue incident,\x01",
            "this morning was absolutely exhausting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had even more appointments in the afternoon,\x01",
            "so I came to rest at home for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I did, I couldn't find my daughter\x01",
            "or her maid anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I became suspicious when I saw a note\x01",
            "she left behind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(
        0x104,
        "#0301F(Guess she's the defiant type.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I doubt he'd have any idea as\x01",
            "to where she would go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x2D, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(
        0x103,
        (
            "#0200F(Now that we have information, shall we\x01",
            "return to Carla's room and continue to\x01",
            "analyze for further clues?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Yeah. Good plan, Tio.)\x02",
    )

    CloseMessageWindow()

    label("loc_87E")

    SetScenarioFlags(0x0, 0)
    Jump("loc_9A9")

    label("loc_886")


    ChrTalk(
        0xFE,
        (
            "My daughter and maid were nowhere to be found\x01",
            "upon my return home this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm relying on you to find her for me. I cannot\x01",
            "allow the Imperial Faction to use this as\x01",
            "ammunition against me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(Is...is he more concerned for his career\x01",
            "than his daughter's well-being?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_383 end

    def Function_6_9B1(): pass

    label("Function_6_9B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B16")

    ChrTalk(
        0xFE,
        (
            "Allegations of bribery against that diet member's\x01",
            "secretary, or that inexplicable incident at the\x01",
            "speaker's estate...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Which one would be a more effective\x01",
            "attack against the Imperial Faction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The budget meeting is almost over. I'll have\x01",
            "to quickly decide which course of action will\x01",
            "best support Representative Campbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BD7")

    label("loc_B16")


    ChrTalk(
        0xFE,
        (
            "While Representative Campbell is fighting in\x01",
            "the diet, I'm fighting out here, working to\x01",
            "uncover valuable information beneficial to us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As always, the diet is a war of information.\x02",
    )

    CloseMessageWindow()

    label("loc_BD7")

    TalkEnd(0xFE)
    Return()

    # Function_6_9B1 end

    def Function_7_BDB(): pass

    label("Function_7_BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C05")
    Call(0, 10)
    Return()

    label("loc_C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F32")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CA2")
    Jump("loc_CEC")

    label("loc_CA2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CC2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEC")

    label("loc_CC2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEC")

    label("loc_CE2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")

    ChrTalk(
        0xFE,
        "The diet has adjourned for the year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I must say, this year's diet was\x01",
            "certainly drawn-out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, the Republican Faction was\x01",
            "able to stand strong thanks to the delays.\x01",
            "Hahaha...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F26")

    label("loc_DED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_E9B")

    ChrTalk(
        0xFE,
        (
            "Ahem... Anyway, I'm relieved\x01",
            "the representative's daughter\x01",
            "has returned home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was unable to have my daily cup of tea\x01",
            "while the maid was absent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F26")

    label("loc_E9B")


    ChrTalk(
        0xFE,
        (
            "And with that being said...why has\x01",
            "my tea not arrived?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have not seen the maid in quite\x01",
            "some time... What exactly is\x01",
            "she doing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F26")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1760")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1760")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FD2")
    Jump("loc_101C")

    label("loc_FD2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FF2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_101C")

    label("loc_FF2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1012")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_101C")

    label("loc_1012")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_101C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1364")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(
        0xFE,
        (
            "It is truly a relief. The Imperial Faction no longer\x01",
            "has any ammunition to use against us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heh. Not to worry. I am hard at work\x01",
            "preparing countermeasures for the diet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11B1")

    label("loc_111E")


    ChrTalk(
        0xFE,
        (
            "I have to say, Representative Campbell\x01",
            "was unusually agitated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe he's actually been worried about\x01",
            "his daughter? Pfft, as if! Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_135F")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")

    ChrTalk(
        0xFE,
        (
            "So...you were unable to retrieve\x01",
            "the representative's daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some help you are. No matter. If the\x01",
            "Imperial Faction catches wind of this,\x01",
            "we'll handle it fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Between Heiyue and issues with the diet,\x01",
            "we have much to deal with at the moment.\x01",
            "Could you refrain from bothering us?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_135F")

    label("loc_12F0")


    ChrTalk(
        0xFE,
        (
            "Between Heiyue and issues with the diet,\x01",
            "we have much to deal with at the moment.\x01",
            "Make yourselves scarce.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135F")

    Jump("loc_1759")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167B")

    ChrTalk(
        0xFE,
        (
            "Representative Campbell runs a\x01",
            "strict household.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For instance, he'll enforce small rules like\x01",
            "everybody having to eat breakfast together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's actually quite obvious that his daughter\x01",
            "despises such trivialities.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1673")

    ChrTalk(
        0x103,
        "#0203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His suffocating nature could be the\x01",
            "reasoning behind their discord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And despite that, she still adhered to his\x01",
            "rule and joined him for breakfast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How am I privy to such knowledge?\x01",
            "I ate breakfast with them, of course!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(
        0x103,
        (
            "#0200F(Now that we have information, shall we\x01",
            "return to Carla's room and continue to\x01",
            "analyze for further clues?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Yeah. Good plan, Tio.)\x02",
    )

    CloseMessageWindow()

    label("loc_166D")

    OP_29(0x2D, 0x1, 0x3)

    label("loc_1673")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1759")

    label("loc_167B")


    ChrTalk(
        0xFE,
        (
            "Between Heiyue and issues with the diet,\x01",
            "we have much to deal with at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Proceed with the investigation as you would.\x01",
            "I urge you to pursue the matter discreetly,\x01",
            "so as to not alert the Imperial Faction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1759")

    SetChrSubChip(0xFE, 0x2)
    TalkEnd(0xFE)

    label("loc_1760")

    Return()

    # Function_7_BDB end

    def Function_8_1761(): pass

    label("Function_8_1761")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183C")

    ChrTalk(
        0xFE,
        (
            "It appears the diet's budget meeting has concluded.\x01",
            "I suppose Father will be arriving home sooner than\x01",
            "anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no other choice. I shall attend\x01",
            "family dinner with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_18D4")

    label("loc_183C")


    ChrTalk(
        0xFE,
        (
            "I'm attending today not because of orders,\x01",
            "but because I genuinely want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, I don't truly hate Father\x01",
            "from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D4")

    Jump("loc_1C08")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1999")

    ChrTalk(
        0xFE,
        "I plan to shop with Marsha later in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father has yet to yell at me today.\x01",
            "Is this what freedom feels like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You have my gratitude, everyone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A17")

    label("loc_1999")


    ChrTalk(
        0xFE,
        "I plan to shop with Marsha later in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My Father has yet to yell at me today.\x01",
            "Is this the feeling of freedom?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A17")

    Jump("loc_1C08")

    label("loc_1A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B84")

    ChrTalk(
        0xFE,
        "It's true. Nothing compares to home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank you, everyone. You've truly helped me\x01",
            "in ways nobody could understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt's okay. We were only doing what's right.\x01",
            "On that note, could you please try and\x01",
            "speak with your father a little more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is the plan. You've given me the\x01",
            "confidence to give it an attempt.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C08")

    label("loc_1B84")


    ChrTalk(
        0xFE,
        (
            "Thank you, everyone. You've truly helped me\x01",
            "in ways nobody could understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I would love for you to visit me once again.\x02",
    )

    CloseMessageWindow()

    label("loc_1C08")

    TalkEnd(0xFE)
    Return()

    # Function_8_1761 end

    def Function_9_1C0C(): pass

    label("Function_9_1C0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1C88")

    ChrTalk(
        0xFE,
        (
            "I am preparing the most delightful\x01",
            "feast tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope my lady and the master\x01",
            "will be pleased.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA9")

    label("loc_1C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D8C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(
        0xFE,
        (
            "I've noticed my lady smiling a lot\x01",
            "more recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What can I say? I am most looking forward\x01",
            "to our shopping adventure today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D87")

    label("loc_1D2A")


    ChrTalk(
        0xFE,
        "My lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I cannot believe she ran away from\x01",
            "home... Will she be okay on her own?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D87")

    Jump("loc_1FA9")

    label("loc_1D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FA9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_1F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(
        0xFE,
        (
            "I don't know how I can thank you\x01",
            "for your help, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am truly relieved to have consulted\x01",
            "you, instead of following my lady\x01",
            "like I had originally intended to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNot a problem, ma'am. The SSS will always\x01",
            "welcome your requests with open arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O-Okay. I'll be sure to remember that!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F2E")

    label("loc_1EEA")


    ChrTalk(
        0xFE,
        (
            "Thank you very much, everyone.\x01",
            "I'm glad I summoned my courage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2E")

    Jump("loc_1FA9")

    label("loc_1F33")


    ChrTalk(
        0xFE,
        "I've neglected all of my work for the day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must begin preparing the meal, or it\x01",
            "won't be ready on time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA9")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C0C end

    def Function_10_1FAD(): pass

    label("Function_10_1FAD")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(440, 1000, 42830, 0)
    MoveCamera(54, 20, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, 500, 0, 40660, 0)
    SetChrPos(0x102, -500, 0, 40660, 0)
    SetChrPos(0x103, -500, 60, 39200, 0)
    SetChrPos(0x104, 500, 60, 39200, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PUnbelievable! What a foolish thing to do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe must find a way to retrieve her,\x01",
            "Representative Campbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, gentlemen. We're here\x01",
            "regarding the support request.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    SetChrSubChip(0xA, 0x1)
    Fade(300)
    SetChrPos(0xA, 1900, 60, 43630, 270)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_95(0xA, 2029, 60, 42410, 1000, 0x0)
    OP_93(0xA, 0xE1, 0x190)

    ChrTalk(
        0xA,
        (
            "#5PAh, you're the CPD's Something-Or-Other\x01",
            "Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWhat a relief! We were becoming so desperate that\x01",
            "we'd be willing to scrape the bottom of the barrel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PJust a moment. Are you not Elie,\x01",
            "Mayor MacDowell's granddaughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWhy have you come with them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FIt's been some time, Representative.\x02\x03",
            "#0100FAs it stands, I am currently employed\x01",
            "by the CPD. I visit you as a detective\x01",
            "of the SSS today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI-Is that the case? So be it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHmm... I suppose the mayor is neutral.\x01",
            "Nothing to be concerned about, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PBut, Representative! The Imperial Faction's\x01",
            "cunning members rely on underhanded tactics.\x01",
            "What if they catch wind of this incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300F(Guessin' this could blow up into a major\x01",
            "political fallout, eh, Mademois-Elie?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106F(It's possible... Talking to diet members\x01",
            "always makes me feel uncomfortable.)\x02\x03",
            "#0101FExcuse me, Representative Campbell.\x01",
            "Could you describe the situation to us\x01",
            "in great detail?\x02\x03",
            "You have a troubled look on your face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI seem to recall the support request seeking\x01",
            "assistance in searching for an important person.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x8,
        "#5PRight you are. I've run into a bit of a snag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI suppose I have no choice but to explain\x01",
            "the situation to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut let me make one thing clear to you:\x01",
            "This is a politically sensitive matter!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThe Republican Faction has been\x01",
            "placed into a difficult situation.\x01",
            "This must remain strictly confidential!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FUnderstood. We'll promise to keep this\x01",
            "under wraps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe swear to remain silent about the\x01",
            "investigation, Representative.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PVery well, then. Listen up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PA certain member of our faction has\x01",
            "disappeared.\x02",
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
        0x103,
        "#12P#0205FCould you elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PIt so happens to be my very own daughter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PShe has run away from home, along\x01",
            "with our maid.\x02",
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
        (
            "#12P#0306F(This dude's still actin' pompous after\x01",
            "his daughter peaced out?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FBy daughter, are you referring to Carla?\x01",
            "We were classmates in Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAh, really? Well, the representative\x01",
            "and his daughter have never been on\x01",
            "particularly good terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PTheir relationship seems to be entirely\x01",
            "comprised of petty arguments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHowever, the timing couldn't be worse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POur main supporter, Heiyue, was raided\x01",
            "this morning. Dealing with the aftermath\x01",
            "has been cumbersome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHmph. That utterly foolish daughter of mine.\x01",
            "I would normally leave her to her own devices\x01",
            "during a hectic period like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, recent reports have shown the\x01",
            "mafias' spats becoming more dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt's far too dangerous to leave two girls\x01",
            "wandering around on their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah, I'd be worried about your daughter's\x01",
            "well-being if I were you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNot only that, but if this were to become\x01",
            "publicized, the Imperial Faction could use\x01",
            "it as ammunition against me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou can't put your guard down during the diet,\x01",
            "so I would prefer to avoid any scandals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnd with that, I request you, the SSS,\x01",
            "to discreetly apprehend and return\x01",
            "my daughter to me.\x02",
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
        0x103,
        (
            "#12P#0203F(It all comes down to protecting his\x01",
            "reputation, then.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306F(S'pose that's how these bigwigs think.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0103F(I already assumed as much...)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_2F57():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F57)
    Sleep(50)

    def lambda_2F67():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F67)

    def lambda_2F74():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F74)

    def lambda_2F81():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F81)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#6P#0101FWell, it's clear that he's concerned for her.\x01",
            "There's a fair chance she might be in\x01",
            "harm's way, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0003FAgreed.\x02",
    )

    CloseMessageWindow()

    def lambda_3021():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3021)

    def lambda_302E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_302E)

    def lambda_303B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_303B)

    def lambda_3048():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3048)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#12P#0001FWe understand the situation, sir. We accept\x01",
            "your request to search for your daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5POh, thank Aidios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PBring her back immediately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FI can't promise we'll be able to do it quickly...\x02\x03",
            "#0001F...but, we'll locate your daughter and provide\x01",
            "protection until we've safely brought her home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PVery well. I suppose I'll rely on you for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PProceed however you like.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PI believe his daughter left a note in her room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThat note may prove useful to\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3278():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3278)

    def lambda_3285():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3285)

    def lambda_3292():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3292)

    def lambda_329F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_329F)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#0101FThank you for letting us know.\x01",
            "We'll take a look at it, then.\x02",
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
            "[Search for an Important Person]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 30, 0, 40130, 180)
    SetChrPos(0xA, 2300, 250, 43630, 270)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x2)
    OP_29(0x2D, 0x1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1FAD end

    def Function_11_33A2(): pass

    label("Function_11_33A2")

    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 135)
    SetChrPos(0x102, 45340, 60, 3250, 135)
    SetChrPos(0x103, 43820, 60, 3620, 135)
    SetChrPos(0x104, 44820, 60, 4220, 135)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0005FLooks like she left her message\x01",
            "in this notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x102, 45710, 60, 2120, 1000, 0x0)
    OP_93(0x102, 0x5A, 0x190)

    ChrTalk(
        0x102,
        (
            "#11P#0103FLet's see what it says...\x02\x03",
            "'I've had enough of you and your\x01",
            "insistence on only doing as you please.'\x02\x03",
            "'So, now I shall do as I please. Goodbye!\x01",
            "                                                 - Carla'\x02\x03",
            "'P.S. I've brought the maid with me.\x01",
            "If you're bothered that your meals will\x01",
            "no longer be made for you, then I'm glad!'\x02",
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
        0x101,
        "#12P#0006FWh-Where do we even begin...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0306FClassic case of the apple not falling far from\x01",
            "the tree. She's not any less selfish than him.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x190)
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#11P#0108FRepresentative Campbell is the type to put\x01",
            "his work ahead of his home life.\x02\x03",
            "And now that I think about it, Carla would often\x01",
            "complain about her father in Sunday School...\x02\x03",
            "#0103FI wouldn't be surprised if a sudden falling out\x01",
            "caused her to run away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FHowever, the notebook fails to provide a clue\x01",
            "about where we should begin the search.\x02\x03",
            "#0200FThe only detail given was that she ran away\x01",
            "from home by her own volition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FHmm... Based on her note, I think it'd be\x01",
            "fair of us to assume something.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Suddenly ran away from home]\x01",        # 0
            "[Planned to run away from home]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF4")
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0003FShe must have run away unexpectedly.\x02\x03",
            "As Elie mentioned, a sudden falling out\x01",
            "may have caused her to run away.\x02\x03",
            "#0001FShe was pretty angry, too, based\x01",
            "on the note.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FI would consider that a reasonable deduction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FI figure if she planned this whole thing\x01",
            "out, the note woulda been longer and\x01",
            "filled with more resentment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 1)
    Jump("loc_3CA6")

    label("loc_3AF4")


    ChrTalk(
        0x101,
        "#12P#0003FHer running away must have been premeditated.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#0305FYou sure, man? Wouldn't the letter have been\x01",
            "more clearly thought out if it was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FRight. I am sure she would have written the\x01",
            "note more cleverly to express her feelings\x01",
            "of resentment towards her father.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0006FO-Oh, yeah. I guess that does make sense.\x02\x03",
            "This looks hastily scribbled, so she probably\x01",
            "took off suddenly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA6")


    ChrTalk(
        0x102,
        (
            "#11P#0101FHow long ago do you think she ran away\x01",
            "from home?\x02\x03",
            "#0108FI hope it hasn't been too long. Our search\x01",
            "will be much more difficult if she's gone far.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EF3")
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0003FWell, it's impossible for us to tell with\x01",
            "the information we have at this time.\x02\x03",
            "#0001FLet's try to get some more information from\x01",
            "the representative before we come to any\x01",
            "conclusions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FLet's get out our shovels, 'cause\x01",
            "we're about to dig up some dirt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FShall we return here to summarize the\x01",
            "details once we have finished?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x4)
    EventEnd(0x5)
    Jump("loc_3F01")

    label("loc_3EF3")

    TurnDirection(0x101, 0x102, 400)
    Sleep(300)
    Call(0, 12)
    Return()

    label("loc_3F01")

    Return()

    # Function_11_33A2 end

    def Function_12_3F02(): pass

    label("Function_12_3F02")


    ChrTalk(
        0x101,
        (
            "#12P#0003FGood question. Going by what the\x01",
            "representative told us, they probably\x01",
            "left...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Yesterday]\x01",         # 0
            "[This morning]\x01",      # 1
            "[Just now]\x01",          # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#11P#0103FShe was present for breakfast, but she\x01",
            "had left by the afternoon.\x02\x03",
            "#0101FI think it's safe to conclude that she\x01",
            "departed sometime in the morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4266")

    label("loc_407B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4171")

    ChrTalk(
        0x102,
        (
            "#11P#0105FOh, but I thought she was present for\x01",
            "breakfast this morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FWhoops, think I messed that one up. He noticed\x01",
            "her disappearance in the afternoon, so I think\x01",
            "it's safe to say she left this morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4266")

    label("loc_4171")


    ChrTalk(
        0x102,
        (
            "#11P#0105FOh, but I thought the representative noticed\x01",
            "her disappearance in the afternoon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FWhoops, think I messed that one up. He noticed\x01",
            "her disappearance in the afternoon, so I think\x01",
            "it's safe to say she left this morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4266")


    ChrTalk(
        0x103,
        "#6P#0200FWe should still be able to catch up with her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0301FStill dunno where the hell she ran off to, though.\x02\x03",
            "#0303FThink we should ask her friends 'bout it?\x01",
            "Maybe they got a clue or two for us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(
        0x101,
        (
            "#12P#0003FNo, I don't think we have the time for that.\x02\x03",
            "#0001FIf we consider the circumstances, there's\x01",
            "definitely a place she would have visited.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe know she left this morning without\x01",
            "having planned to.\x02\x03",
            "Considering that, there's one place in\x01",
            "particular she likely had to visit first.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Crossbell Cathedral]\x01",      # 0
            "[City Hall]\x01",                # 1
            "[The IBC]\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46CF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#12P#0000FThe IBC, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FMakes sense to me. Our escapee probably\x01",
            "needed some dough for her getaway.\x02\x03",
            "S'pose that's the most logical step\x01",
            "she would take, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FIf she suddenly left, then she wouldn't\x01",
            "have had much time to pack.\x01",
            "The IBC is certainly a possibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FShall we depart for the IBC, then?\x01",
            "She may still be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYeah, let's get there ASAP!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AAC")

    label("loc_46CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B8")

    ChrTalk(
        0x101,
        (
            "#12P#0000FMy theory is she made her way to the cathedral.\x02\x03",
            "If she's a person of faith, then she\x01",
            "may have wanted to offer a prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0108FI don't seem to recall Carla being\x01",
            "particularly pious, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4877")

    label("loc_47B8")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI think she went to City Hall.\x02\x03",
            "She may have wanted to file a\x01",
            "change in residency or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0108FWell... I doubt Carla was thinking that\x01",
            "clearly when she left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4877")

    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#6P#0203FWe have concluded that she ran away\x01",
            "suddenly...\x02\x03",
            "#0200FIs it not probable that she was carrying a\x01",
            "scarce amount of mira on her person?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_495F():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_495F)

    def lambda_496C():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_496C)

    def lambda_4979():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4979)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0005FGood point, Tio. She might have gone to\x01",
            "the IBC to withdraw funds for her journey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303FY'know, now that I think about... That's\x01",
            "probably the most logical course of action.\x02\x03",
            "#0300FLet's jet on over to the IBC!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FYes, let's make our way to\x01",
            "the IBC with haste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC4")
    OP_2C(0x2D, 0x2)

    label("loc_4AC4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 45270, 60, 2680, 152)
    OP_29(0x2D, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_3F02 end

    def Function_13_4AEC(): pass

    label("Function_13_4AEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C8C")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I've had enough of you and your\x01",
            "insistence on only doing as you please.\x01",
            "So, now I shall do as I please. Goodbye!\x01",
            "                                                 - Carla\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P.S. I've brought the maid with me.\x01",
            "If you're bothered that your meals will\x01",
            "no longer be made for you, then I'm glad!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_4DBA")

    label("loc_4C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_4DB7")
    EventBegin(0x0)
    Fade(800)
    OP_68(44280, 1560, 2580, 0)
    MoveCamera(56, 25, 0, 0)
    OP_6E(390, 0)
    SetCameraDistance(21530, 0)
    SetChrPos(0x101, 44280, 60, 2500, 0)
    SetChrPos(0x102, 45340, 60, 3250, 270)
    SetChrPos(0x103, 43820, 60, 3620, 90)
    SetChrPos(0x104, 44820, 60, 4220, 180)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#11P#0108FHow long ago do you think she ran away\x01",
            "from home?\x02\x03",
            "I hope it hasn't been too long. Our search\x01",
            "will be much more difficult if she's gone far.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_4DBA")

    label("loc_4DB7")

    Call(0, 11)

    label("loc_4DBA")

    Return()

    label("loc_4DBB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I've had enough of you and your\x01",
            "insistence on only doing as you please.\x01",
            "So, now I shall do as I please. Goodbye!\x01",
            "                                                 - Carla\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P.S. I've brought the maid with me.\x01",
            "If you're bothered that your meals will\x01",
            "no longer be made for you, then I'm glad!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_13_4AEC end

    SaveToFile()

Try(main)
