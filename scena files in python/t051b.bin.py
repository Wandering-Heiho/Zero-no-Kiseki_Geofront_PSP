from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t051b.bin",                # FileName
        "t051b",                    # MapName
        "t051b",                    # Location
        0x003D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 61, 0, 1, 0, 2],
    )

    BuildStringList((
        "t051b",                  # 0
        "Mayor Bickson",          # 1
        "Anna",                   # 2
        "Old Lady Bilma",         # 3
        "Amy",                    # 4
        "Miner Logy",             # 5
        "Miranda",                # 6
        "Alec",                   # 7
        "Mine Chief Hoffmann",    # 8
        "Miner Max",              # 9
        "Lurieda",                # 10
    ))

    AddCharChip((
        "chr/ch23202.itc",                   # 00
        "chr/ch20100.itc",                   # 01
        "chr/ch23700.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch23300.itc",                   # 04
        "chr/ch23000.itc",                   # 05
        "chr/ch26302.itc",                   # 06
        "chr/ch22702.itc",                   # 07
        "apl/ch50130.itc",                   # 08
        "chr/ch24300.itc",                   # 09
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

    DeclNpc(-889,    949,     2640,    90,   341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-6530,   750,     59,      270,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(49209,   0,       4369,    0,    261,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(50959,   0,       1389,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(49689,   0,       1389,    90,   389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(97519,   150,     2130,    180,  469,  0x0, 0,   7,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(98349,   0,       -1129,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(97459,   150,     -1169,   0,    469,  0x0, 0,   6,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(154710,  300,     2500,    315,  471,  0x0, 0,   8,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(147369,  0,       4179,    333,  261,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_421",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_755",          # 04, 4
        "Function_5_7C4",          # 05, 5
        "Function_6_824",          # 06, 6
        "Function_7_8F1",          # 07, 7
        "Function_8_A0A",          # 08, 8
        "Function_9_A81",          # 09, 9
        "Function_10_B6D",         # 0A, 10
        "Function_11_CF4",         # 0B, 11
        "Function_12_E87",         # 0C, 12
        "Function_13_1003",        # 0D, 13
        "Function_14_1118",        # 0E, 14
        "Function_15_121F",        # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_420")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_420")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_346")
    Jump("loc_420")

    label("loc_346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_354")
    Jump("loc_420")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_362")
    Jump("loc_420")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_420")

    label("loc_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_37E")
    Jump("loc_420")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38C")
    Jump("loc_420")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39A")
    Jump("loc_420")

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A8")
    Jump("loc_420")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3B6")
    Jump("loc_420")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_409")
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_3FD")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_404")

    label("loc_3FD")

    TurnDirection(0xE, 0xD, 0)

    label("loc_404")

    Jump("loc_420")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_417")
    Jump("loc_420")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_420")

    label("loc_420")

    Return()

    # Function_1_31C end

    def Function_2_421(): pass

    label("Function_2_421")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_421 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_50B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_501")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50B")

    label("loc_501")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "A monopoly on the septium industry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course, everyone's safety is\x01",
            "my number one priority...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But what about our regular trade partners?\x01",
            "We can't afford to lose their trust...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Mayor Bickson is really under\x01",
            "a lot of stress right now...)\x02\x03",
            "#0001F(I'm sure they'll attack tonight.\x01",
            "Let's get ready and stand by at the inn.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_73B")

    label("loc_6A5")


    ChrTalk(
        0xFE,
        (
            "Oh, it's just you guys...\x01",
            "Are you planning on staying the night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'see, one of our miners was injured,\x01",
            "so you all can never be too careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B")

    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_42D end

    def Function_4_755(): pass

    label("Function_4_755")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Bickson looks beside himself with worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should cook him some treats to\x01",
            "cheer him up?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_755 end

    def Function_5_7C4(): pass

    label("Function_5_7C4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, dear. My grandchildren never fail to\x01",
            "cause a ruckus in the middle of the night.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_7C4 end

    def Function_6_824(): pass

    label("Function_6_824")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_839")
    Call(0, 7)
    Jump("loc_8ED")

    label("loc_839")


    ChrTalk(
        0xFE,
        (
            "Geez, why can't my brother go drink\x01",
            "with his friends like a normal person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Max was mauled by a monster\x01",
            "the other day, so I can't really blame\x01",
            "him for staying home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    TalkEnd(0xFE)
    Return()

    # Function_6_824 end

    def Function_7_8F1(): pass

    label("Function_7_8F1")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)

    ChrTalk(
        0xB,
        (
            "Hey, are you really skipping another\x01",
            "drinking party at the bar...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But the mayor told me to hurry\x01",
            "on home after my shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What's wrong with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You've forced my hand, Logy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You. Are. An. Introvert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Sh-Shut up, Amy!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_8F1 end

    def Function_8_A0A(): pass

    label("Function_8_A0A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1F")
    Call(0, 7)
    Jump("loc_A7D")

    label("loc_A1F")


    ChrTalk(
        0xFE,
        "Tch... I wish she'd mind her own business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Besides, I can't really stomach alcohol.\x02",
    )

    CloseMessageWindow()

    label("loc_A7D")

    TalkEnd(0xFE)
    Return()

    # Function_8_A0A end

    def Function_9_A81(): pass

    label("Function_9_A81")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_AE0")
    TurnDirection(0xFE, 0xF, 0)

    ChrTalk(
        0xFE,
        (
            "Heeey, can't we go ahead and eat?\x01",
            "My stomach is about to implode.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B69")

    label("loc_AE0")


    ChrTalk(
        0xFE,
        (
            "*sigh* I guess I have to wait until\x01",
            "Dad gets home. Just my luck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm about to die of hunger. Surely\x01",
            "he's almost home, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B69")

    TalkEnd(0xFE)
    Return()

    # Function_9_A81 end

    def Function_10_B6D(): pass

    label("Function_10_B6D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C01")
    Jump("loc_C4B")

    label("loc_C01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4B")

    label("loc_C21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C41")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4B")

    label("loc_C41")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C82")
    Call(0, 11)
    Jump("loc_CEC")

    label("loc_C82")


    ChrTalk(
        0xFE,
        (
            "Oh, you guys. I know I gave you permission\x01",
            "to enter the mines, but please try not to get\x01",
            "hurt, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEC")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_B6D end

    def Function_11_CF4(): pass

    label("Function_11_CF4")

    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xD,
        (
            "Max still hasn't recovered from the\x01",
            "monster attack...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah, well, the wound itself wasn't\x01",
            "that deep, but there's another problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's right on his leg. If I pushed him too\x01",
            "hard, it might affect him for life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Ah, okay. I'm worried about him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Be careful, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hahaha, don't worry about me.\x01",
            "I'm the mine chief, after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "No lack of confidence, I see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_11_CF4 end

    def Function_12_E87(): pass

    label("Function_12_E87")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F1B")
    Jump("loc_F65")

    label("loc_F1B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F3B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F65")

    label("loc_F3B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F5B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F65")

    label("loc_F5B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F65")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 2)), scpexpr(EXPR_END)), "loc_FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA5")
    Call(0, 11)
    Jump("loc_FD7")

    label("loc_FA5")


    ChrTalk(
        0xFE,
        (
            "This man is too reckless for\x01",
            "his own good...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD7")

    Jump("loc_FFB")

    label("loc_FDC")


    ChrTalk(
        0xFE,
        "*sigh* Why is he so late?\x02",
    )

    CloseMessageWindow()

    label("loc_FFB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_E87 end

    def Function_13_1003(): pass

    label("Function_13_1003")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1018")
    Call(0, 14)
    Jump("loc_1114")

    label("loc_1018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")

    ChrTalk(
        0xFE,
        (
            "For some reason, I can never sleep\x01",
            "if I don't enter the mine that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dang it. Why did that stupid\x01",
            "monster have to attack me...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1114")

    label("loc_10B6")


    ChrTalk(
        0xFE,
        (
            "*sigh* This sucks. My body is going to wither\x01",
            "away while everyone else has a great life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1114")

    TalkEnd(0xFE)
    Return()

    # Function_13_1003 end

    def Function_14_1118(): pass

    label("Function_14_1118")


    ChrTalk(
        0xFE,
        "Morning can't come soon enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I already finished this book I bought\x01",
            "recently. It was pretty interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Would you like to give it a read?\x01",
            "Here, I hope you enjoy it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C8, 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_14_1118 end

    def Function_15_121F(): pass

    label("Function_15_121F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My husband has been down in the dumps\x01",
            "ever since he ended up bedridden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just hope he gets better soon.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_121F end

    SaveToFile()

Try(main)
