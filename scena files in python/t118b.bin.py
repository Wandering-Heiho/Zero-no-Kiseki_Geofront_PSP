from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t118b.bin",                # FileName
        "t118b",                    # MapName
        "t118b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 4, 0, 5],
    )

    BuildStringList((
        "t118b",                  # 0
        "Invitee",                # 1
        "Invitee",                # 2
        "Invitee",                # 3
        "Invitee",                # 4
        "Invitee",                # 5
        "Doven Kaiser 1",         # 6
        "Doven Kaiser 2",         # 7
        "bt113b",                 # 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch21802.itc",                   # 00
        "chr/ch21900.itc",                   # 01
        "chr/ch33002.itc",                   # 02
        "chr/ch21702.itc",                   # 03
        "chr/ch33100.itc",                   # 04
        "monster/ch67151.itc",               # 05
    ))

    DeclNpc(3829,    150,     -64919,  180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(70,      0,       -69059,  180,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-46529,  150,     32020,   180,  469,  0x0, 0,   2,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-46529,  150,     27889,   0,    469,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-19,     0,       -11449,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_234",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_317",          # 02, 2
        "Function_3_342",          # 03, 3
        "Function_4_35E",          # 04, 4
        "Function_5_3B7",          # 05, 5
        "Function_6_405",          # 06, 6
        "Function_7_68B",          # 07, 7
        "Function_8_884",          # 08, 8
        "Function_9_A4E",          # 09, 9
        "Function_10_C22",         # 0A, 10
        "Function_11_CFA",         # 0B, 11
    ))


    def Function_0_234(): pass

    label("Function_0_234")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_274"),
        (1, "loc_280"),
        (2, "loc_28C"),
        (3, "loc_298"),
        (4, "loc_2A4"),
        (5, "loc_2B0"),
        (6, "loc_2BC"),
        (SWITCH_DEFAULT, "loc_2C8"),
    )


    label("loc_274")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_280")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_28C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_298")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D4")

    label("loc_2EB")

    Return()

    # Function_0_234 end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_316")
    OP_94(0xFE, 0xFFFFF9CA, 0xFFFEEAE4, 0x456, 0xFFFEFC6E, 0x3E8)
    Sleep(300)
    Jump("Function_1_2EC")

    label("loc_316")

    Return()

    # Function_1_2EC end

    def Function_2_317(): pass

    label("Function_2_317")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_341")
    OP_94(0xFE, 0xFFFFFB82, 0xFFFFBE42, 0x3DE, 0xFFFFF16E, 0x3E8)
    Sleep(300)
    Jump("Function_2_317")

    label("loc_341")

    Return()

    # Function_2_317 end

    def Function_3_342(): pass

    label("Function_3_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35D")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_342")

    label("loc_35D")

    Return()

    # Function_3_342 end

    def Function_4_35E(): pass

    label("Function_4_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_36C")
    Jump("loc_3B6")

    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 2)
    Jump("loc_3B6")

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_393")
    Jump("loc_3B6")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3B6")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_3B6")

    Return()

    # Function_4_35E end

    def Function_5_3B7(): pass

    label("Function_5_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_3C0")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3CE")
    Jump("loc_404")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_END)), "loc_404")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_404")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_404")
    Event(0, 11)

    label("loc_404")

    Return()

    # Function_5_3B7 end

    def Function_6_405(): pass

    label("Function_6_405")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_499")
    Jump("loc_4E3")

    label("loc_499")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E3")

    label("loc_4B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E3")

    label("loc_4D9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")

    ChrTalk(
        0xFE,
        (
            "Rumors say that the highlight of the auction\x01",
            "is going to be an exquisite doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I hear that, all I can think of is that\x01",
            "doll workshop, Rosenberg Studio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I can't wait until this finally starts.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_683")

    label("loc_5F2")


    ChrTalk(
        0xFE,
        (
            "Rosenberg dolls are extremely fascinating.\x01",
            "They're so finely crafted that they look alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I can't wait until this finally starts.\x02",
    )

    CloseMessageWindow()

    label("loc_683")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_405 end

    def Function_7_68B(): pass

    label("Function_7_68B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790")

    ChrTalk(
        0xFE,
        (
            "My husband is extremely fond of dolls,\x01",
            "and everything like them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Dolls? Isn't that a bit childish?' is what I\x01",
            "thought at first, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...since then, I've come to truly appreciate\x01",
            "their beauty. They really are quite lovely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_880")

    label("loc_790")


    ChrTalk(
        0xFE,
        (
            "Ever since I came to appreciate the beauty\x01",
            "of dolls, it's been my life's goal to collect as\x01",
            "many as I can with my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We will find and procure dolls, no matter\x01",
            "how much mira it may take... That's the\x01",
            "power of a doll's charm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880")

    TalkEnd(0xFE)
    Return()

    # Function_7_68B end

    def Function_8_884(): pass

    label("Function_8_884")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_918")
    Jump("loc_962")

    label("loc_918")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_938")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_962")

    label("loc_938")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_958")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_962")

    label("loc_958")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_962")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I appreciate them throwing a dinner party\x01",
            "and all, but I have no plans to attend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will only eat my meals when they are\x01",
            "served to me by maids. I assure you,\x01",
            "there's no better way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_884 end

    def Function_9_A4E(): pass

    label("Function_9_A4E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE2")
    Jump("loc_B2C")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B02")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2C")

    label("loc_B02")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B22")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B2C")

    label("loc_B22")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I managed to get an invitation from an\x01",
            "acquaintance of mine, though I'm not sure\x01",
            "if I belong in this kind of environment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'm just going to wait here until the\x01",
            "actual auction starts.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_A4E end

    def Function_10_C22(): pass

    label("Function_10_C22")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, oh, dear. I decided to go on a\x01",
            "self-guided tour of the mansion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...but I think I'm lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is quite the dilemma... If I don't\x01",
            "find my way back soon, the auction\x01",
            "will start without me.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_C22 end

    def Function_11_CFA(): pass

    label("Function_11_CFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D37")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_D58")

    label("loc_D37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D52")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_D58")

    label("loc_D52")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_D58")

    LoadChrToIndex("chr/ch00450.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 1, 0, 3)
    Sleep(50)
    BeginChrThread(0xE, 1, 0, 3)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E81")
    OP_68(0, 1200, -6000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xEF, -750, 0, -7000, 0)
    SetChrPos(0x105, 750, 0, -7750, 0)
    SetChrPos(0x133, 0, 0, -9000, 0)
    SetChrPos(0xD, 0, 0, 0, 180)
    SetChrPos(0xE, 1250, 0, 1000, 180)
    Jump("loc_F15")

    label("loc_E81")

    OP_68(0, 1200, -16000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -16000, 0)
    SetChrPos(0xEF, -750, 0, -17000, 0)
    SetChrPos(0x105, 750, 0, -17750, 0)
    SetChrPos(0x133, 0, 0, -19000, 0)
    SetChrPos(0xD, 0, 0, -10000, 180)
    SetChrPos(0xE, 1250, 0, -9000, 180)

    label("loc_F15")


    def lambda_F1A():
        OP_98(0xD, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F1A)
    Sleep(50)

    def lambda_F37():
        OP_98(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_F37)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xD, 2)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1031")
    OP_68(0, 1200, -6000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0xEF, 0, 0, -6000, 0)
    SetChrPos(0x105, 0, 0, -6000, 0)
    Jump("loc_1092")

    label("loc_1031")

    OP_68(0, 1200, -16000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -16000, 0)
    SetChrPos(0xEF, 0, 0, -16000, 0)
    SetChrPos(0x105, 0, 0, -16000, 0)

    label("loc_1092")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_CFA end

    SaveToFile()

Try(main)
