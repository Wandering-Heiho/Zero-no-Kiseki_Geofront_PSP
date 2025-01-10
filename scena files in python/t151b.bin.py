from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t151b.bin",                # FileName
        "t151b",                    # MapName
        "t151b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t151b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Marone",                 # 3
        "Bus Passenger",          # 4
        "Bus Passenger",          # 5
        "Bus Passenger",          # 6
        "Bus Passenger",          # 7
        "Bus Passenger",          # 8
        "Head Nurse Martha",      # 9
        "Superintendent Kirsch",  # 10
        "Security Guard Tony",    # 11
        "Bus Driver",             # 12
        "Outpatient",             # 13
        "Outpatient",             # 14
        "bt152b",                 # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 2, 13, 180)
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
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch21000.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch20300.itc",                   # 09
        "chr/ch29600.itc",                   # 0A
        "chr/ch24300.itc",                   # 0B
        "apl/ch50155.itc",                   # 0C
        "apl/ch50154.itc",                   # 0D
        "chr/ch20000.itc",                   # 0E
        "chr/ch22802.itc",                   # 0F
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(55459,   0,       -2079,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(55909,   0,       1330,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(59330,   449,     -3049,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(59130,   0,       -5159,   225,  261,  0x0, 0,   7,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(57900,   0,       -6389,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(52869,   0,       -4570,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(52490,   0,       51650,   0,    261,  0x0, 0,   10,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(60090,   0,       55479,   180,  261,  0x0, 0,   11,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(59909,   449,     53849,   90,   343,  0x0, 1,   12,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(52569,   449,     53849,   90,   343,  0x0, 1,   13,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(58209,   0,       50250,   270,  261,  0x0, 0,   14,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(52270,   449,     56560,   180,  341,  0x0, 0,   15,  0,   255, 255, 0,   15,  255,  0)

    DeclEvent(0x0000, 0, 22,  6.0,                   4.0,                   -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -1.3333333730697632,   0.10000000894069672,   1.0])

    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_408",          # 00, 0
        "Function_1_4C0",          # 01, 1
        "Function_2_515",          # 02, 2
        "Function_3_5A8",          # 03, 3
        "Function_4_5D9",          # 04, 4
        "Function_5_6E4",          # 05, 5
        "Function_6_73E",          # 06, 6
        "Function_7_8C7",          # 07, 7
        "Function_8_978",          # 08, 8
        "Function_9_9CE",          # 09, 9
        "Function_10_A38",         # 0A, 10
        "Function_11_EEB",         # 0B, 11
        "Function_12_107C",        # 0C, 12
        "Function_13_1203",        # 0D, 13
        "Function_14_1293",        # 0E, 14
        "Function_15_12F6",        # 0F, 15
        "Function_16_1430",        # 10, 16
        "Function_17_1499",        # 11, 17
        "Function_18_19BD",        # 12, 18
        "Function_19_1FD4",        # 13, 19
        "Function_20_204F",        # 14, 20
        "Function_21_2932",        # 15, 21
        "Function_22_3235",        # 16, 22
    ))


    def Function_0_408(): pass

    label("Function_0_408")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_448"),
        (1, "loc_454"),
        (2, "loc_460"),
        (3, "loc_46C"),
        (4, "loc_478"),
        (5, "loc_484"),
        (6, "loc_490"),
        (SWITCH_DEFAULT, "loc_49C"),
    )


    label("loc_448")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_454")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_460")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_46C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_478")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_484")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_490")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_49C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_4A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A8")

    label("loc_4BF")

    Return()

    # Function_0_408 end

    def Function_1_4C0(): pass

    label("Function_1_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DB")
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_514")

    label("loc_4DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 20)
    Jump("loc_514")

    label("loc_4FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_514")
    Event(0, 21)

    label("loc_514")

    Return()

    # Function_1_4C0 end

    def Function_2_515(): pass

    label("Function_2_515")

    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED07", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED08", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    Call(0, 19)

    label("loc_58A")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5A7")

    Return()

    # Function_2_515 end

    def Function_3_5A8(): pass

    label("Function_3_5A8")

    TalkBegin(0xFE)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafioso is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_5A8 end

    def Function_4_5D9(): pass

    label("Function_4_5D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")

    ChrTalk(
        0xFE,
        (
            "We haven't been able to contact\x01",
            "anyone in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really hope Kirsch, Sera, and\x01",
            "everyone else are safe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6E0")

    label("loc_66A")


    ChrTalk(
        0xFE,
        (
            "We haven't been able to contact\x01",
            "anyone in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Kirsch and the\x01",
            "others are doing okay...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E0")

    TalkEnd(0xFE)
    Return()

    # Function_4_5D9 end

    def Function_5_6E4(): pass

    label("Function_5_6E4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Damn it, I have a friend who's in the\x01",
            "hospital. How do I know he's all right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_6E4 end

    def Function_6_73E(): pass

    label("Function_6_73E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D2")
    Jump("loc_81C")

    label("loc_7D2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7F2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81C")

    label("loc_7F2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_812")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81C")

    label("loc_812")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "I'm so glad you're all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't help but think about what might\x01",
            "happen if we're kept locked up like this...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_73E end

    def Function_7_8C7(): pass

    label("Function_7_8C7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Th-Those guys in the black suits...\x01",
            "Did you get a good look at their eyes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like they aren't human. There's no\x01",
            "life in them, just an unsettling calmness...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_8C7 end

    def Function_8_978(): pass

    label("Function_8_978")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Crap... Why did this have to happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What did I do to deserve this?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_978 end

    def Function_9_9CE(): pass

    label("Function_9_9CE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The bus driver is being treated in the\x01",
            "next room over...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I sure hope he'll pull through.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_9CE end

    def Function_10_A38(): pass

    label("Function_10_A38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_END)), "loc_B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B11")

    ChrTalk(
        0xFE,
        (
            "Oh, you found it! That's the key\x01",
            "those men took from me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With it, you should be able to\x01",
            "unlock the door to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hold on to it and go save Cecile\x01",
            "and the patients!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B94")

    label("loc_B11")


    ChrTalk(
        0xFE,
        (
            "With that key, you should be able to\x01",
            "unlock the door to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hold on to it and go save Cecile\x01",
            "and the patients!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B94")

    Jump("loc_EE7")

    label("loc_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_END)), "loc_DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAE")

    ChrTalk(
        0xFE,
        (
            "What? The hospital entrance\x01",
            "was locked...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Those buffoons have shut us out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I usually have the key to the\x01",
            "hospital on me, but those men\x01",
            "snatched it from me earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll have to find the one holding\x01",
            "the key and take it back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 1)
    SetScenarioFlags(0x0, 1)
    Jump("loc_D9C")

    label("loc_CAE")


    ChrTalk(
        0xFE,
        (
            "The hospital key I always have\x01",
            "was stolen by one of those men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They went up the stairs to the\x01",
            "dormitories, so I think they might\x01",
            "still be in the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only thing you can do is track\x01",
            "them down and take back the key.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C")

    Jump("loc_EE7")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E98")

    ChrTalk(
        0xFE,
        (
            "Those men used force against\x01",
            "the staff and the patients...\x01",
            "That's unforgivable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I resisted like a madwoman, but\x01",
            "they easily overpowered me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll leave the hospital to you four.\x01",
            "Now go save Cecile and the patients!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EE7")

    label("loc_E98")


    ChrTalk(
        0xFE,
        (
            "I'll leave the hospital to you four.\x01",
            "Now go save Cecile and the patients!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE7")

    TalkEnd(0xFE)
    Return()

    # Function_10_A38 end

    def Function_11_EEB(): pass

    label("Function_11_EEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAD")
    TurnDirection(0xFE, 0x12, 0)

    ChrTalk(
        0xFE,
        "Stay with me, Tony!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember: Because you intervened,\x01",
            "the bus driver wasn't shot a second\x01",
            "time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're both still with us, so you have\x01",
            "to stay strong!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1078")

    label("loc_FAD")


    ChrTalk(
        0xFE,
        (
            "What a mess. Since there's no medical\x01",
            "equipment here in the inn, the best I can\x01",
            "give him is general first aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The other man has already broken into\x01",
            "a fiery fever, and I only have two hands...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1078")

    TalkEnd(0xFE)
    Return()

    # Function_11_EEB end

    def Function_12_107C(): pass

    label("Function_12_107C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(
        0xFE,
        (
            "H-Hey... Guess you're running low\x01",
            "on luck, too, seeing as you came to\x01",
            "the hospital at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bus driver and I tried to fight\x01",
            "back and, in return, got shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Damn it! Some security guard I am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_11FF")

    label("loc_116E")


    ChrTalk(
        0xFE,
        (
            "I'm supposed to be St. Ursula's security\x01",
            "guard, but they were able to easily break\x01",
            "through my line...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't deserve this position...\x02",
    )

    CloseMessageWindow()

    label("loc_11FF")

    TalkEnd(0xFE)
    Return()

    # Function_12_107C end

    def Function_13_1203(): pass

    label("Function_13_1203")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Argh... I didn't think I was actually\x01",
            "going to get shot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When that guy raised his gun towards\x01",
            "me, I thought it was all over.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1203 end

    def Function_14_1293(): pass

    label("Function_14_1293")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I just had a checkup scheduled for\x01",
            "this evening. Then I got wrapped\x01",
            "up in all of this.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1293 end

    def Function_15_12F6(): pass

    label("Function_15_12F6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_138A")
    Jump("loc_13D4")

    label("loc_138A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D4")

    label("loc_13AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13CA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D4")

    label("loc_13CA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13D4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "This is all a dream... Y-Yeah, a dream...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_12F6 end

    def Function_16_1430(): pass

    label("Function_16_1430")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "3F: Women's Dormitory→\x01\x01",
            "← 2F: Men's Dormitory\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_1430 end

    def Function_17_1499(): pass

    label("Function_17_1499")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(-7450, 1000, 12750, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 0, 0, -1300, 0)
    SetChrPos(0x102, 600, 50, -2800, 0)
    SetChrPos(0x103, -600, 50, -2800, 0)
    SetChrPos(0x104, -600, 0, -4300, 0)
    SetChrPos(0x106, 600, 0, -4300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 6500, 0, 9500, 180)
    SetChrPos(0x9, 4500, 0, 9500, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_68(1750, 1000, 4550, 7000)
    Sleep(3000)

    def lambda_161D():
        OP_95(0xFE, 0, 0, 3700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_161D)

    def lambda_1637():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1637)
    Sleep(50)

    def lambda_164B():
        OP_95(0xFE, 600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_164B)

    def lambda_1665():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1665)
    Sleep(50)

    def lambda_1679():
        OP_95(0xFE, -600, 50, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1679)

    def lambda_1693():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1693)
    Sleep(50)

    def lambda_16A7():
        OP_95(0xFE, -600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16A7)

    def lambda_16C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_16C1)
    Sleep(50)

    def lambda_16D5():
        OP_95(0xFE, 600, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_16D5)

    def lambda_16EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_16EF)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1739():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1739)
    Sleep(50)

    def lambda_1749():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_1749)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_1772():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1772)

    def lambda_177F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_177F)

    def lambda_178C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_178C)
    Sleep(100)

    def lambda_179C():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_179C)

    def lambda_17A9():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_17A9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100435V#0013F#6PTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100436V#0301F#6PWell, that didn't take long!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100437V\x07\x02",
            "#5P...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5100438V\x07\x02",
            "#5P...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x106,
        (
            "#5100439V\x07\x03",
            "#0702F#12PNo point in complaining, Orlando.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5100440V\x07\x00",
            "#0107F#6PEveryone, look out!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)

    def lambda_1953():
        OP_95(0xFE, 3650, 0, 6040, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1953)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1975():
        OP_95(0xFE, 2009, 0, 6190, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1975)
    Sleep(500)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_1499 end

    def Function_18_19BD(): pass

    label("Function_18_19BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    OP_68(-280, 1100, 3650, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x101, -440, 0, 5250, 90)
    SetChrPos(0x102, -1750, 0, 5720, 90)
    SetChrPos(0x103, -2900, 0, 3020, 90)
    SetChrPos(0x104, -1020, 0, 3310, 90)
    SetChrPos(0x106, -3540, 0, 4380, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Call(0, 19)
    FadeToBright(1000, 0)
    SetCameraDistance(26500, 2000)
    OP_6F(0x10)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        "#5100441V#0303F#6PJust as tough as the other ones, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100442V#0203F#6POnce again, I detected almost no\x01",
            "flux in their emotional states.\x02\x03",
            "#5100443V#0208FI think it is possible that they are not\x01",
            "moving of their own volition.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C1A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C1A)
    Sleep(50)

    def lambda_1C2A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C2A)
    Sleep(50)

    def lambda_1C3A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C3A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#5100444V#0105F#5PC-Could you explain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100445V#0013F#5PYou mean...they're being controlled?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#5100446V#0206F#6PEssentially. Though, I cannot confirm\x01",
            "this hypothesis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100447V\x07\x03",
            "#0700F#6PIn the East, there are things known as\x01",
            "'puppet techniques,' which incorporate\x01",
            "the power of drugs and hypnosis...\x02\x03",
            "#5100448VYour hypothesis isn't an impossibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100449V#0106F#5PThat's not what I wanted to hear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100450V#0306F#11PThat'd be a real pain in the ass, man.\x02\x03",
            "#5100451V#0301FBut, mind control? That ain't Garcia's\x01",
            "style, no matter how much I think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100452V#0003F#5PI was thinking the same thing.\x02\x03",
            "#5100453V#0013FFor now, confirming the safety of\x01",
            "everyone at St. Ursula takes priority.\x02\x03",
            "#5100454VWhile we're here, let's try searching\x01",
            "the dormitories for anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100455V#0101F#5PAll right!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    SetChrPos(0x0, 0, 0, 4000, 0)
    SetScenarioFlags(0xE0, 4)
    EventEnd(0x5)
    Return()

    # Function_18_19BD end

    def Function_19_1FD4(): pass

    label("Function_19_1FD4")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 2940, 0, 3630, 225)
    SetChrPos(0x9, 2480, 0, 5210, 315)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_19_1FD4 end

    def Function_20_204F(): pass

    label("Function_20_204F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(57230, 1100, -1820, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19870, 0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrPos(0x101, 47720, 0, 0, 90)
    SetChrPos(0x102, 46520, 0, 600, 90)
    SetChrPos(0x103, 46520, 0, -600, 90)
    SetChrPos(0x104, 45320, 0, -600, 90)
    SetChrPos(0x106, 45320, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(55230, 1100, -1820, 4000)

    def lambda_2145():
        OP_95(0xFE, 52720, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2145)

    def lambda_215F():
        OP_95(0xFE, 51520, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_215F)

    def lambda_2179():
        OP_95(0xFE, 51520, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2179)

    def lambda_2193():
        OP_95(0xFE, 50320, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2193)

    def lambda_21AD():
        OP_95(0xFE, 50320, 0, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_21AD)
    Sleep(1000)

    def lambda_21CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21CA)
    Sleep(500)

    def lambda_21DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21DE)

    def lambda_21EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_21EF)
    Sleep(500)

    def lambda_2203():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2203)

    def lambda_2214():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2214)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_22F4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22F4)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    def lambda_2308():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2308)

    def lambda_2315():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2315)
    Sleep(50)

    def lambda_2325():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2325)

    def lambda_2332():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2332)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xA, 1)

    NpcTalk(
        0xB,
        "Young Man",
        "#5100456V#5PL-L-Look out!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Middle-Aged Man",
        "#5100457V#11PWh-Who are you?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DF")

    ChrTalk(
        0x101,
        "#5100458V#0005F#6PAren't you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2429")

    label("loc_23DF")


    ChrTalk(
        0x101,
        (
            "#5100459V#0002F#6PThank goodness. I'm glad to see\x01",
            "you guys are safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2429")

    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#5100460V#11PAren't you...those police officers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100461V#0003F#6PThat's right. We're with the CPD.\x02\x03",
            "#5100462V#0000FOnce we realized something was wrong,\x01",
            "we came to check on everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0xC,
        "Young Woman",
        "#5100463V#5PW-We're saved! Thank you, Aidios!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man in Suit",
        (
            "#5100464V#11PI started to assume the worst when\x01",
            "they dragged us away from the bus...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100465V#0301F#6P#NHold on. You guys were initially on\x01",
            "that bus that's parked on the road?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xD,
        "#5100466V#11PWe were, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100467V#11POn our way here, a bunch of those\x01",
            "mafia guys stood in the bus' way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100468V#5PAfter that, they held us at gunpoint\x01",
            "and made us walk the rest of the way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100469V#5POh, our driver! He tried to fight back,\x01",
            "but ended up getting shot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100470V#0106F#6PSo that's how it happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100471V#0003F#6PEveryone, please wait here for just\x01",
            "a little while longer.\x02\x03",
            "#5100472V#0001FI promise that we'll come back to\x01",
            "take you somewhere safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100473V#5PO-Okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5100474V#5PThank you so much!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x0, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_93(0xE, 0x2D, 0x0)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xE0, 5)
    OP_29(0x4D, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_20_204F end

    def Function_21_2932(): pass

    label("Function_21_2932")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(56470, 700, 54520, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23870, 0)
    SetChrPos(0x101, 48100, 0, 50000, 90)
    SetChrPos(0x102, 46900, 0, 50600, 90)
    SetChrPos(0x103, 46900, 0, 49400, 90)
    SetChrPos(0x104, 45700, 0, 50600, 90)
    SetChrPos(0x106, 45700, 0, 49400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 56000, 0, 54040, 180)
    SetChrPos(0x11, 56000, 0, 52770, 0)
    FadeToBright(1000, 0)
    OP_68(54450, 700, 52500, 3000)
    Sleep(150)

    def lambda_2A46():
        OP_95(0xFE, 53100, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A46)

    def lambda_2A60():
        OP_95(0xFE, 51900, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A60)

    def lambda_2A7A():
        OP_95(0xFE, 51900, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A7A)

    def lambda_2A94():
        OP_95(0xFE, 50700, 0, 50600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A94)

    def lambda_2AAE():
        OP_95(0xFE, 50700, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2AAE)
    Sleep(1000)

    def lambda_2ACB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ACB)
    Sleep(500)

    def lambda_2ADF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2ADF)

    def lambda_2AF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2AF0)
    Sleep(500)

    def lambda_2B04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B04)

    def lambda_2B15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2B15)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    def lambda_2B3A():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B3A)

    def lambda_2B47():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2B47)

    def lambda_2B54():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_2B54)
    Sleep(100)

    def lambda_2B64():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_2B64)

    def lambda_2B71():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_2B71)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2C21():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C21)
    Sleep(30)

    def lambda_2C31():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C31)
    Sleep(300)

    ChrTalk(
        0x10,
        "#5100475V#5PGood heavens!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5100476V#11PIt's the police!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100477V#0002F#12PHead Nurse...Martha, right?\x01",
            "I'm glad you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100478V#0202F#12PThere is some good news.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5100479V#5PWhy are you youngsters here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5100480V#5PH-Have you taken back the hospital already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100481V#0106F#6PNot yet. We've only just arrived.\x02\x03",
            "#5100482V#0101FWe're checking whether everyone is\x01",
            "safe and accounted for at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5100483V#5POkay. I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100484V#0301F#6PSo, some folks sustained injuries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5100485V#5PUnfortunately so. Our security\x01",
            "guard and the bus driver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5100486V#5PThe mafia put a bullet in each of them,\x01",
            "so I immediately administered first aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100487V#0006F#12PGood thing you were around.\x02\x03",
            "#5100488V#0001FIs Cecile working in the hospital now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5100489V#5PI believe so. Due to the hospital being\x01",
            "packed lately, we've been needing every\x01",
            "set of hands we can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5100490V#5PI was in the middle of taking my\x01",
            "break when I walked over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5100491V#5PI should be there with everyone in\x01",
            "the hospital during a crisis like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100492V#0208F#12PMartha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100493V#0003F#12PYou don't have anything to worry about.\x02\x03",
            "#5100494V#0013FWe're going to save Cecile and the rest of\x01",
            "the patients, no matter what!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100495V#0101F#6PPlease keep watching over the\x01",
            "injured's conditions, Martha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5100496V#5POf course. Thank you, everyone!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 50500, 0, 50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10, 52490, 0, 51650, 0)
    SetChrPos(0x11, 60090, 0, 55480, 180)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0xE0, 6)
    OP_29(0x4D, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_21_2932 end

    def Function_22_3235(): pass

    label("Function_22_3235")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32CD")

    ChrTalk(
        0x101,
        (
            "#0001FThe mafia was definitely guarding\x01",
            "something on the first floor.\x02\x03",
            "Let's see if we can't find out who\x01",
            "or what it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3332")

    label("loc_32CD")


    ChrTalk(
        0x101,
        (
            "#0001FThere should be another room\x01",
            "on the first floor. Let's give it a\x01",
            "sweep before moving out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3332")

    Sleep(50)
    SetChrPos(0x0, 4059, 0, 3600, 270)
    EventEnd(0x4)
    Return()

    # Function_22_3235 end

    SaveToFile()

Try(main)
