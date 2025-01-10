from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t117b.bin",                # FileName
        "t117b",                    # MapName
        "t117b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t117b",                  # 0
        "Invitee",                # 1
        "Invitee",                # 2
        "Invitee",                # 3
        "Evelyn",                 # 4
        "James",                  # 5
        "Guide",                  # 6
        "Mafioso 1",              # 7
        "Mafioso 2",              # 8
        "bt113b",                 # 9
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
            ("ms31002.dat", "ms31102.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch33002.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "chr/ch33302.itc",                   # 03
        "chr/ch27802.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
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
        "chr/ch31051.itc",                   # 1C
        "chr/ch31151.itc",                   # 1D
    ))

    DeclNpc(-310,    0,       -71709,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(44860,   150,     -13789,  270,  469,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(40840,   150,     -13789,  90,   469,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(44860,   150,     26239,   270,  469,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(40840,   150,     26290,   90,   469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   28,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   29,  0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_2AC",          # 00, 0
        "Function_1_364",          # 01, 1
        "Function_2_3EB",          # 02, 2
        "Function_3_442",          # 03, 3
        "Function_4_574",          # 04, 4
        "Function_5_800",          # 05, 5
        "Function_6_830",          # 06, 6
        "Function_7_B8C",          # 07, 7
        "Function_8_E55",          # 08, 8
        "Function_9_2537",         # 09, 9
        "Function_10_3FA7",        # 0A, 10
    ))


    def Function_0_2AC(): pass

    label("Function_0_2AC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2EC"),
        (1, "loc_2F8"),
        (2, "loc_304"),
        (3, "loc_310"),
        (4, "loc_31C"),
        (5, "loc_328"),
        (6, "loc_334"),
        (SWITCH_DEFAULT, "loc_340"),
    )


    label("loc_2EC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_2F8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_304")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_310")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_31C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_328")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_334")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_34C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_363")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_34C")

    label("loc_363")

    Return()

    # Function_0_2AC end

    def Function_1_364(): pass

    label("Function_1_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_39E")
    ClearScenarioFlags(0x5C, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_381")
    Event(0, 8)
    Jump("loc_39E")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_392")
    Event(0, 9)
    Jump("loc_39E")

    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_39E")
    Event(0, 9)

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_3AC")
    Jump("loc_3EA")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_3BA")
    Jump("loc_3EA")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_3D2")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3EA")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3EA")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_3EA")

    Return()

    # Function_1_364 end

    def Function_2_3EB(): pass

    label("Function_2_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_3F4")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_402")
    Jump("loc_441")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_441")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_441")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_441")
    Event(0, 10)

    label("loc_441")

    Return()

    # Function_2_3EB end

    def Function_3_442(): pass

    label("Function_3_442")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Despite most hiding their real names, the people\x01",
            "invited to this event are all powerful individuals\x01",
            "from both the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Politicians and nobles are quite skilled with\x01",
            "swapping out personas for each and every\x01",
            "circumstance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Of course, that includes me, too. Hehehe...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_442 end

    def Function_4_574(): pass

    label("Function_4_574")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73F")

    ChrTalk(
        0xFE,
        (
            "This auction is the perfect opportunity\x01",
            "to forge new connections with influential\x01",
            "people from all over Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe, my dear, sweet daughter! How\x01",
            "about we find you a good husband while\x01",
            "we're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ohoho. Now, Father, I think you just want\x01",
            "to use me to make some new friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now that I think about it, isn't a political\x01",
            "marriage the only reason you were\x01",
            "adopted into Mother's family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bwahahaha! You caught me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FC")

    label("loc_73F")


    ChrTalk(
        0xFE,
        (
            "If you really stop and consider it, there's\x01",
            "no connection stronger than one forged\x01",
            "by holy matrimony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if the opportunity presents itself,\x01",
            "maybe we should go for it? Bwahaha!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC")

    TalkEnd(0xFE)
    Return()

    # Function_4_574 end

    def Function_5_800(): pass

    label("Function_5_800")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, Father. You DO love your jokes.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_800 end

    def Function_6_830(): pass

    label("Function_6_830")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C4")
    Jump("loc_90E")

    label("loc_8C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_904")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E")

    label("loc_904")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")

    ChrTalk(
        0xFE,
        (
            "'This is it. I'm going to have to file\x01",
            "a divorce, aren't I?' When that's all\x01",
            "I could think about, Wazy told me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'The fact that you can't forgive him\x01",
            "means that you really love him.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I lost sight of what is truly important to\x01",
            "me. I need to thank Wazy for helping\x01",
            "me understand that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With my husband reflecting on his actions,\x01",
            "I think I will be able to forgive him in due time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 1)
    Jump("loc_B84")

    label("loc_AD6")

    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xFE,
        (
            "I'll be forever grateful for Wazy's help tonight.\x01",
            "He honestly saved my entire marriage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Darling, let's go on in. The auction should\x01",
            "be starting any minute now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B84")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_830 end

    def Function_7_B8C(): pass

    label("Function_7_B8C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_C6A")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C40")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6A")

    label("loc_C40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C6A")

    label("loc_C60")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(
        0xFE,
        (
            "That was the first time I've seen\x01",
            "Evelyn that furious. And to tell the\x01",
            "truth...I was petrified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to her extremely docile nature,\x01",
            "I thought I could get away with anything,\x01",
            "and I ended up a womanizer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe she had such an intense\x01",
            "personality hidden away all this time...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 2)
    Jump("loc_E4D")

    label("loc_DD0")


    ChrTalk(
        0xFE,
        (
            "At any rate, I'm just glad we were able to\x01",
            "fix things between us, by some miracle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My life as a womanizer is over.\x02",
    )

    CloseMessageWindow()

    label("loc_E4D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_B8C end

    def Function_8_E55(): pass

    label("Function_8_E55")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0x102, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x138,
        (
            "#3501172V#2904F#11PI think I have a grasp on the situation now.\x02\x03",
            "#3501173V#2902FQuite the bold move, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501174V#5106F#6PYeah, we know.\x02\x03",
            "#3501175V#5108FFrom an outside perspective, I could\x01",
            "see how someone might think we're\x01",
            "being selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501176V#2902F#11PDon't get me wrong, I like your idea.\x02\x03",
            "#3501177V#2909FIf you weren't as determined as you are,\x01",
            "you would be completely unsuited to be\x01",
            "one of Elie's coworkers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#3501178V#5313F#6PB-Bell, please stop...\x02\x03",
            "#3501179V#5301FWhy are you at a place like this, anyway?\x02\x03",
            "#3501180VBased on our earlier conversation, it sounded\x01",
            "like this was your first time attending, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501181V#2902F#11PWell, you see, I receive invitations from\x01",
            "Speaker Hartmann every year, practically\x01",
            "begging me to come.\x02\x03",
            "#3501182V#2903FBut, as I'm sure you know, he's a man who\x01",
            "has connections with a lot of unsavory\x01",
            "individuals.\x02\x03",
            "#3501183VMy father would always come up with\x01",
            "excuse after excuse in order to keep me\x01",
            "from attending.\x02\x03",
            "#3501184V#2901FWith so much to do, I was never really\x01",
            "able to accept their invitations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501185V#5306F#6PThat certainly makes sense.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501186V#5105F#6PSo why could you come this year?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3501187V#5300F#5PI've mentioned it before, but Bell handles\x01",
            "some of the IBC's work for her father.\x02\x03",
            "#3501188VActually, she's the one responsible for all\x01",
            "of Mishelam's current construction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501189V#5111F#6PReally...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501190V#2902F#11PYou say that, but I only really manage\x01",
            "the hotel and theme park.\x02\x03",
            "#3501191V#2906FThat's the reason why I couldn't bear to\x01",
            "decline another invitation from Speaker\x01",
            "Hartmann, who's lived here for so long.\x02\x03",
            "#3501192V#2900FAnd so, I decided that I would attend\x01",
            "this year's Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501193V#5101F#6PSo that's why...\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0x102,
        "#3501194V#5311F#6P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x138,
        (
            "#3501195V#2905F#11PWhat is it, Elie?\x02\x03",
            "#3501196VYou want to say something, right?\x01",
            "Your face gives it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501197V#5303F#6PYes, well...\x02\x03",
            "#3501198V#5300FBell, you wouldn't do something if you weren't\x01",
            "at least the slightest bit interested in it, right?\x02\x03",
            "#3501199VI'm not sure if I buy that you came here\x01",
            "just to pay your respects.\x02\x03",
            "#3501200VDo you really not have some ulterior motive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501201V#2904F#11PHehe. Sharp as always, Elie.\x02\x03",
            "#3501202V#2902FIn reality, I've heard rumors of something in\x01",
            "the auction that piqued my interest.\x02\x03",
            "#3501203VAnd so, because of that certain something,\x01",
            "I decided to attend the auction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501204V#5105F#6PSo...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501205V#5301F#6PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501206V#2904F#11PAn antique doll, crafted during the early\x01",
            "days of the Rosenberg Studio...\x02\x03",
            "#3501207V#2902FAmong doll connoisseurs such as myself, those\x01",
            "particular dolls are said to be the ultimate catch\x01",
            "and sell for an exceptionally high price.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501208V#5105F#6PAn antique doll from that famous studio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501209V#5301F#6PI presume it has quite a colorful\x01",
            "history, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501210V#2904F#11PI don't know if it was stolen or some rich\x01",
            "man has to part with it for some reason...\x02\x03",
            "#3501211V#2902F...but what I do know is that rumors say\x01",
            "it's an absolute masterpiece.\x02\x03",
            "#3501212VAs a collector, I can't let this chance pass\x01",
            "me by, can I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501213V#5306F#6PThat's true. You've been a fan of those\x01",
            "dolls for as long as I can remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501214V#5101F#6PIf you don't mind me asking, how much\x01",
            "does one of these dolls usually go for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501215V#2905F#11PHmm, let me think...\x02\x03",
            "#3501216V#2906FThe studio's earlier works were much\x01",
            "bigger than their ones now, and they\x01",
            "rarely show up on the market anymore.\x02\x03",
            "#3501217VAnd given the fact that the doll maker\x01",
            "doesn't intend to make any like those\x01",
            "again, they've racked up quite the premium.\x02\x03",
            "#3501218V#2900FOne was even sold for approximately\x01",
            "five million mira at an auction in the\x01",
            "Imperial capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501219V#5111F#6POne doll is that much?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501220V#5309F#6PWell, given how passionate the fans are\x01",
            "and how the dolls are truly priceless\x01",
            "works of art, it's not too shocking.\x02\x03",
            "#3501221V#5300FYou're dead set on winning this bid, aren't\x01",
            "you, Bell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501222V#2904F#11PAnd regardless of how it ended up here,\x01",
            "that's hardly the fault of the doll, is it?\x02\x03",
            "#3501223V#2902FOf course, if it turns out it was stolen, I'll make\x01",
            "sure to take the proper countermeasures.\x02\x03",
            "#3501224V#2909FThat includes formally negotiating with the\x01",
            "former owner to officially make it mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501225V#5106F#6PHow...thorough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501226V#5306F#6P*sigh* You're dedicated, that's for sure.\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x138,
        "#3501227V#2905F#11POh...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1500)

    def lambda_2149():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2149)
    Sleep(50)

    def lambda_2159():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2159)
    OP_6F(0x1)

    NpcTalk(
        0xD,
        "Guide's Voice",
        "#3501228V#2SPardon me, Ms. Crois.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Guide's Voice",
        (
            "#3501229V#2SThe auction will be beginning shortly,\x01",
            "just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501230V#2904F#11PWill it? Thank you for letting me know.\x02\x03",
            "#3501231V#2900FI'll head there in just a minute, so please\x01",
            "prepare three seats, preferably in the back,\x01",
            "for us, will you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Guide's Voice",
        "#3501232V#2SIt would be our pleasure.\x02",
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_22FA():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22FA)
    Sleep(50)

    def lambda_230A():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_230A)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#3501233V#5308F#6PUmm, Bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501234V#2902F#11PI know what you're thinking,\x01",
            "and there's no need to worry.\x02\x03",
            "#3501235VI will wait to introduce myself to the speaker\x01",
            "until after the auction. He won't see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501236V#5306F#6PIf that's the case...\x02\x03",
            "#3501237V#5300F...shall we accompany her, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501238V#5104F#6PWell, we might as well go together\x01",
            "since we're all here.\x02\x03",
            "#3501239V#5100FThanks for setting us up with seats,\x01",
            "Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#3501240V#2909F#11POh, it was nothing!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_E55 end

    def Function_9_2537(): pass

    label("Function_9_2537")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0xEF, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x138,
        (
            "#3501241V#2904F#11PI think I have a grasp on the situation now.\x02\x03",
            "#3501242V#2902FQuite the bold move, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501243V#5106F#6PYeah, we know.\x02\x03",
            "#3501244V#5108FFrom an outside perspective, I could\x01",
            "see how someone might think we're\x01",
            "being selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501245V#2902F#11PDon't get me wrong, I like your idea.\x02\x03",
            "#3501246V#2909FIf you weren't as determined as you are,\x01",
            "you would be completely unsuited to be\x01",
            "one of Elie's coworkers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501247V#5112F#6PY-You think so...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(
        0x103,
        "#3501248V#5402F#6PElie is very important to you, correct?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2838")

    label("loc_27EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2838")

    ChrTalk(
        0x104,
        "#3501249V#5602F#6PYou must care a lot about Mademois-Elie, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_2838")


    ChrTalk(
        0x138,
        (
            "#3501250V#2904F#11PWell, yes. It wouldn't be an exaggeration\x01",
            "to say that I love her.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501251V#5111F#6PCome again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501252V#2902F#11PI mean, isn't she just the cutest thing?\x02\x03",
            "#3501253VDespite being blunt, stubborn, and proud,\x01",
            "she still has an elegance and calming aura\x01",
            "about her.\x02\x03",
            "#3501254V#2909FShe's my best friend, and I'm proud of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501255V#5100F#6PShe's definitely all of those things, yeah.\x02\x03",
            "#3501256V#5104FWe're all proud to work alongside her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2AC4")

    ChrTalk(
        0x103,
        (
            "#3501257V#5404F#6PIf Elie heard you say that, I imagine she\x01",
            "would have the world's brightest blush.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B2E")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2B2E")

    ChrTalk(
        0x104,
        (
            "#3501258V#5609F#6PHaha! If she heard you say that, I bet\x01",
            "her face would turn red as a beet!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2E")


    ChrTalk(
        0x138,
        (
            "#3501259V#2906F#11PIt's a shame that Elie wasn't able to\x01",
            "accompany you two.\x02\x03",
            "#3501260V#2900FIf she did, I would have loved to inspect\x01",
            "all the beautiful artwork with her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501261V#5101F#6PActually...is there some specific reason\x01",
            "why you came to the Schwarze Auction?\x02\x03",
            "#3501262VIf our previous conversation is anything to\x01",
            "go by, this is your first time attending.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501263V#2902F#11PWell, you see, I receive invitations from\x01",
            "Speaker Hartmann every year, practically\x01",
            "begging me to come.\x02\x03",
            "#3501264V#2903FBut, as I'm sure you know, he's a man who\x01",
            "has connections with a lot of unsavory\x01",
            "individuals.\x02\x03",
            "#3501265VMy father would always come up with\x01",
            "excuse after excuse in order to keep me\x01",
            "from attending.\x02\x03",
            "#3501266V#2901FWith so much to do, I was never really\x01",
            "able to accept their invitations.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2E92")

    ChrTalk(
        0x103,
        "#3501267V#5400F#6PWhat was different this year?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ECF")

    label("loc_2E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2ECF")

    ChrTalk(
        0x104,
        "#3501268V#5605F#6PSomething turn up this year?\x02",
    )

    CloseMessageWindow()

    label("loc_2ECF")


    ChrTalk(
        0x138,
        (
            "#3501269V#2904F#11PYou see, I'm in charge of all of Mishelam's\x01",
            "current construction projects.\x02\x03",
            "#3501270V#2900FThat's the reason why I couldn't bear to\x01",
            "decline another invitation from Speaker\x01",
            "Hartmann, who's lived here for so long.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_301C")

    ChrTalk(
        0x103,
        "#3501271V#5401F#6PHuh?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_304E")

    label("loc_301C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_304E")

    ChrTalk(
        0x104,
        "#3501272V#5607F#6PWhoa, seriously?!\x02",
    )

    CloseMessageWindow()

    label("loc_304E")


    ChrTalk(
        0x101,
        (
            "#3501273V#5111F#6PThat's right! We heard you're in charge\x01",
            "of several of the IBC's projects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501274V#2904F#11PYes, but I only really manage the\x01",
            "hotel and theme park here.\x02\x03",
            "#3501275V#2902FAlso, I heard rumors of something being\x01",
            "sold in the auction that piqued my interest.\x02\x03",
            "#3501276VAnd yes, because of that certain something,\x01",
            "I decided to attend the auction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501277V#5101F#6PSo...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_323E")

    ChrTalk(
        0x103,
        "#3501278V#5401F#6PWhat is it, exactly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3278")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3278")

    ChrTalk(
        0x104,
        "#3501279V#5602F#6PWanna tell us what it is?\x02",
    )

    CloseMessageWindow()

    label("loc_3278")


    ChrTalk(
        0x138,
        (
            "#3501280V#2904F#11PAn antique doll, crafted during the early\x01",
            "days of the Rosenberg Studio...\x02\x03",
            "#3501281V#2902FAmong doll connoisseurs, such as myself, those\x01",
            "particular dolls are said to be magnum opuses,\x01",
            "fetching exceptionally high prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501282V#5105F#6PAn antique doll from that famous studio...\x02\x03",
            "#3501283V#5101FIt must have quite the history, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501284V#2904F#11PI don't know if it was stolen or some rich\x01",
            "man has to part with it for some reason...\x02\x03",
            "#3501285V...but what I do know is that rumors say\x01",
            "it's an absolute masterpiece.\x02\x03",
            "#3501286V#2902FAs a collector, I can't let this chance pass\x01",
            "me by, can I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501287V#5112F#6PI can't argue with that logic.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(
        0x103,
        (
            "#3501288V#5400F#6PThese dolls... How much do they\x01",
            "usually sell for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35D4")

    label("loc_357B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_35D4")

    ChrTalk(
        0x104,
        (
            "#3501289V#5609F#6PSpeakin' of these dolls, how much\x01",
            "does one usually cost?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D4")


    ChrTalk(
        0x138,
        (
            "#3501290V#2905F#11PHmm, let me think...\x02\x03",
            "#3501291V#2906FThe studio's earlier works were much\x01",
            "bigger than their ones now, and they\x01",
            "rarely show up on the market anymore.\x02\x03",
            "#3501292VAnd given the fact that the doll maker\x01",
            "doesn't intend to make any like those\x01",
            "again, they've racked up quite the premium.\x02\x03",
            "#3501293V#2900FOne was even sold for approximately\x01",
            "five million mira in an auction at the\x01",
            "Erebonian capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501294V#5111F#6POne doll is that much?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3894")

    ChrTalk(
        0x103,
        (
            "#3501295V#5406F#6PYou could buy a top-of-the-line orbal\x01",
            "computer with that kind of mira...\x02\x03",
            "#3501296V#5400FYou must be intending to win it in\x01",
            "tonight's auction, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_3894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3945")

    ChrTalk(
        0x104,
        (
            "#3501297V#5606F#6PYou could buy a freakin' tank with\x01",
            "that kinda mira...\x02\x03",
            "#3501298V#5605FAnd your face is tellin' me that you're\x01",
            "plannin' to win that doll tonight?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3945")


    ChrTalk(
        0x138,
        (
            "#3501299V#2904F#11PIndeed. And regardless of how it ended up\x01",
            "here, that's hardly the fault of the doll, is it?\x02\x03",
            "#3501300V#2902FOf course, if it turns out it was stolen, I'll make\x01",
            "sure to take the proper countermeasures.\x02\x03",
            "#3501301V#2909FThat includes formally negotiating with the\x01",
            "former owner to officially make it mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501302V#5106F#6PHow...thorough.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3AED")

    ChrTalk(
        0x103,
        "#3501303V#5406F#6PVery generous of you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B25")

    label("loc_3AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3B25")

    ChrTalk(
        0x104,
        "#3501304V#5606F#6PGenerous gal, ain't ya?\x02",
    )

    CloseMessageWindow()

    label("loc_3B25")

    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x138,
        "#3501305V#2905F#11POh...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1200)

    def lambda_3B74():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B74)
    Sleep(50)

    def lambda_3B84():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3B84)
    OP_6F(0x1)

    NpcTalk(
        0xD,
        "Guide's Voice",
        "#3501306V#2SPardon me, Ms. Crois.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Guide's Voice",
        (
            "#3501307V#2SThe auction will be beginning shortly,\x01",
            "just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501308V#2909F#11PWill it? Thank you for letting me know.\x02\x03",
            "#3501309V#2900FI'll head there in just a minute, so please\x01",
            "prepare three seats, preferably in the back,\x01",
            "for us, will you?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Guide's Voice",
        "#3501310V#2SIt would be our pleasure.\x02",
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_3D25():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D25)
    Sleep(50)

    def lambda_3D35():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3D35)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3501311V#5108F#6PUh, Mariabell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501312V#2902F#11PI know what you're thinking,\x01",
            "and there's no need to worry.\x02\x03",
            "#3501313VI will introduce myself to the speaker\x01",
            "after the auction, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3E69")

    ChrTalk(
        0x103,
        (
            "#3501314V#5402F#6PIf that is your plan, there should not be\x01",
            "any conflicts, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3EA8")

    ChrTalk(
        0x104,
        "#3501315V#5600F#6PGuess we should be okay, then.\x02",
    )

    CloseMessageWindow()

    label("loc_3EA8")


    ChrTalk(
        0x101,
        (
            "#3501316V#5103F#6POkay. Since we're already here,\x01",
            "we might as well accompany you\x01",
            "to the auction.\x02\x03",
            "#3501317V#5100FThanks for setting us up with seats,\x01",
            "Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#3501318V#2909F#11POh, it was nothing!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_2537 end

    def Function_10_3FA7(): pass

    label("Function_10_3FA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FE4")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_4005")

    label("loc_3FE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FFF")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_4005")

    label("loc_3FFF")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_4005")

    LoadChrToIndex("chr/ch00450.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FB")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, -750, 0, -12500, 0)
    SetChrPos(0x105, 750, 0, -12250, 0)
    SetChrPos(0x133, 0, 0, -14000, 0)
    SetChrPos(0xE, 0, 0, -5000, 180)
    SetChrPos(0xF, -750, 0, -4250, 180)
    Jump("loc_4237")

    label("loc_40FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41A3")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, -750, 0, -20500, 0)
    SetChrPos(0x105, 750, 0, -20250, 0)
    SetChrPos(0x133, 0, 0, -22000, 0)
    SetChrPos(0xE, 0, 0, -13000, 180)
    SetChrPos(0xF, -750, 0, -12250, 180)
    Jump("loc_4237")

    label("loc_41A3")

    OP_68(0, 1200, -22000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -22000, 0)
    SetChrPos(0xEF, -750, 0, -23500, 0)
    SetChrPos(0x105, 750, 0, -23250, 0)
    SetChrPos(0x133, 0, 0, -25000, 0)
    SetChrPos(0xE, 0, 0, -16000, 180)
    SetChrPos(0xF, -750, 0, -15250, 180)

    label("loc_4237")


    def lambda_423C():
        OP_97(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_423C)
    Sleep(50)

    def lambda_4259():
        OP_97(0xF, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4259)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xE, 1)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0xF, 0xFF)
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
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434B")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, 0, 0, -11000, 0)
    SetChrPos(0x105, 0, 0, -11000, 0)
    Jump("loc_4421")

    label("loc_434B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C0")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, 0, 0, -19000, 0)
    SetChrPos(0x105, 0, 0, -19000, 0)
    Jump("loc_4421")

    label("loc_43C0")

    OP_68(0, 1200, -23250, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -23250, 0)
    SetChrPos(0xEF, 0, 0, -23250, 0)
    SetChrPos(0x105, 0, 0, -23250, 0)

    label("loc_4421")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_10_3FA7 end

    SaveToFile()

Try(main)
