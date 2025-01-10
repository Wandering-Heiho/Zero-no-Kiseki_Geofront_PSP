from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t111b.bin",                # FileName
        "t111b",                    # MapName
        "t111b",                    # Location
        0x0047,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 71, 0, 2, 0, 3],
    )

    BuildStringList((
        "t111b",                  # 0
        "Guide Berkeley",         # 1
        "Nikita",                 # 2
        "Evelyn",                 # 3
        "James",                  # 4
        "Man in Suit",            # 5
        "Man in Suit",            # 6
        "Invitee",                # 7
        "Invitee",                # 8
        "Invitee",                # 9
        "Invitee",                # 10
        "Invitee",                # 11
        "Invitee",                # 12
        "Man in Suit",            # 13
        "Man in Suit",            # 14
        "Man in Suit",            # 15
        "Mafioso",                # 16
        "Mafioso",                # 17
        "Mafioso",                # 18
        "Garcia",                 # 19
        "Mariabell",              # 20
        "Don Marconi",            # 21
        "Speaker Hartmann",       # 22
        "bt111b",                 # 23
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

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
        "BattleInfo_E4", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt111b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "chr/ch36100.itc",                   # 02
        "chr/ch33300.itc",                   # 03
        "chr/ch33000.itc",                   # 04
        "chr/ch33100.itc",                   # 05
        "chr/ch26800.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch21900.itc",                   # 08
        "chr/ch22000.itc",                   # 09
        "chr/ch27800.itc",                   # 0A
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

    DeclNpc(1909,    500,     19610,   180,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(10149,   500,     22780,   270,  385,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2789,    500,     25229,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2019,    500,     25690,   0,    401,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2240,   500,     27729,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2009,    500,     27729,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6530,   500,     16040,   135,  385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5719,   500,     15300,   315,  385,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6449,    500,     24350,   45,   385,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5719,   500,     15300,   315,  385,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6530,   500,     16040,   135,  385,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(9100,    500,     22780,   90,   385,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_474",          # 00, 0
        "Function_1_52C",          # 01, 1
        "Function_2_52D",          # 02, 2
        "Function_3_673",          # 03, 3
        "Function_4_6BC",          # 04, 4
        "Function_5_8D2",          # 05, 5
        "Function_6_986",          # 06, 6
        "Function_7_A0F",          # 07, 7
        "Function_8_B79",          # 08, 8
        "Function_9_E92",          # 09, 9
        "Function_10_11D9",        # 0A, 10
        "Function_11_1298",        # 0B, 11
        "Function_12_1375",        # 0C, 12
        "Function_13_14BF",        # 0D, 13
        "Function_14_171E",        # 0E, 14
        "Function_15_17CC",        # 0F, 15
        "Function_16_18F9",        # 10, 16
        "Function_17_260E",        # 11, 17
        "Function_18_3E88",        # 12, 18
        "Function_19_5739",        # 13, 19
        "Function_20_5E02",        # 14, 20
        "Function_21_60F2",        # 15, 21
        "Function_22_645E",        # 16, 22
        "Function_23_6AB4",        # 17, 23
        "Function_24_7380",        # 18, 24
        "Function_25_73A1",        # 19, 25
        "Function_26_73D0",        # 1A, 26
    ))


    def Function_0_474(): pass

    label("Function_0_474")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B4"),
        (1, "loc_4C0"),
        (2, "loc_4CC"),
        (3, "loc_4D8"),
        (4, "loc_4E4"),
        (5, "loc_4F0"),
        (6, "loc_4FC"),
        (SWITCH_DEFAULT, "loc_508"),
    )


    label("loc_4B4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4C0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4CC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4D8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4E4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4F0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_508")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_514")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_514")

    label("loc_52B")

    Return()

    # Function_0_474 end

    def Function_1_52C(): pass

    label("Function_1_52C")

    Return()

    # Function_1_52C end

    def Function_2_52D(): pass

    label("Function_2_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_53B")
    Jump("loc_5B0")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_55D")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_5B0")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_589")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_5B0")

    label("loc_589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5B0")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_602")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FA")
    Event(0, 18)
    Jump("loc_5FD")

    label("loc_5FA")

    Event(0, 17)

    label("loc_5FD")

    Jump("loc_613")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_613")
    Event(0, 22)

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_627")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 16)
    Jump("loc_672")

    label("loc_627")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_63B")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 19)
    Jump("loc_672")

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_64F")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 20)
    Jump("loc_672")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_663")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 21)
    Jump("loc_672")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_672")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 23)

    label("loc_672")

    Return()

    # Function_2_52D end

    def Function_3_673(): pass

    label("Function_3_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_67C")

    label("loc_67C")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_694")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_6B5")
    OP_1B(0x0, 0x0, 0x1A)

    label("loc_6B5")

    Sound(124, 1, 80, 0)
    Return()

    # Function_3_673 end

    def Function_4_6BC(): pass

    label("Function_4_6BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_6CD")
    Jump("loc_8CE")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(
        0xFE,
        "Oh, can I be of any service?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If not, please take your seats in the main\x01",
            "hall. It should be starting soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CE")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_75D")
    Jump("loc_8CE")

    label("loc_75D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_8CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859")

    ChrTalk(
        0xFE,
        (
            "The Schwarze Auction will begin promptly\x01",
            "at 9PM and will be held in the main hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until then, please enjoy a few drinks in the\x01",
            "salon over through the door on the left. If you\x01",
            "are hungry, food is available as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8CE")

    label("loc_859")


    ChrTalk(
        0xFE,
        (
            "If you require a room, please let any of the\x01",
            "attendants know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I assure you, we'll see to it straight away.\x02",
    )

    CloseMessageWindow()

    label("loc_8CE")

    TalkEnd(0xFE)
    Return()

    # Function_4_6BC end

    def Function_5_8D2(): pass

    label("Function_5_8D2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh... Do I spy a man with no plus-one?\x01",
            "I may just have to introduce myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "James isn't exactly strapped for mira,\x01",
            "but I wonder how large this man's\x01",
            "wallet is...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_8D2 end

    def Function_6_986(): pass

    label("Function_6_986")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "As a gesture of good faith, my husband\x01",
            "is going to bid on quite a few pieces of\x01",
            "priceless jewelry for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How exciting.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_986 end

    def Function_7_A0F(): pass

    label("Function_7_A0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3B")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xB,
        (
            "Why couldn't you have taken your seat\x01",
            "when the usher approached us earlier?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        "I don't see what you're in a tiff about, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(If I, by a twist of cruel fate, had been assigned\x01",
            "seats next to her and Nikita was with me,\x01",
            "my life would be over...)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_B75")

    label("loc_B3B")


    ChrTalk(
        0xB,
        (
            "D-Don't mind me. Should we go\x01",
            "on and find our seats?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B75")

    TalkEnd(0xFE)
    Return()

    # Function_7_A0F end

    def Function_8_B79(): pass

    label("Function_8_B79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B8A")
    Jump("loc_E8E")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D1F")

    ChrTalk(
        0xFE,
        "Dear guests, is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please don't roam around too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101F(It doesn't look like they're aware of\x01",
            "the situation yet...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#5703F(That's quite convenient for us. If you\x01",
            "intend to investigate, you should do it\x01",
            "before things get out of hand.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101F(Good point. Let's take this opportunity to walk\x01",
            "around the mansion while we still can.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D9D")

    label("loc_D1F")


    ChrTalk(
        0xFE,
        "Did you forget something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The auction will not be postponed\x01",
            "for any minor issues. Please hurry\x01",
            "and take your seats.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9D")

    Jump("loc_E8E")

    label("loc_DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_E25")

    ChrTalk(
        0xFE,
        (
            "The Schwarze Auction will begin soon.\x01",
            "Please head inside the main hall and\x01",
            "take your seats as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8E")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(
        0xFE,
        (
            "The security team has everything\x01",
            "under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please rest easy and enjoy the event.\x02",
    )

    CloseMessageWindow()

    label("loc_E8E")

    TalkEnd(0xFE)
    Return()

    # Function_8_B79 end

    def Function_9_E92(): pass

    label("Function_9_E92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_EA3")
    Jump("loc_11D5")

    label("loc_EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_F8E")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "Auction staff have prepared plenty of seats\x01",
            "for our guests. Please sit in whichever open\x01",
            "seat you would like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you wish, you can stand and participate,\x01",
            "but seats on the second floor are also available.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D5")

    label("loc_F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_112E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BE")

    ChrTalk(
        0xFE,
        (
            "You must be Miss Mariabell and her\x01",
            "acquaintances, correct? I've heard\x01",
            "about you from the guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He will be waiting for you inside\x01",
            "the hall. We've prepared a row\x01",
            "of seats at the back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2900FWhy, thank you. Come along, now.\x01",
            "Let's not waste any time and go inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1129")

    label("loc_10BE")


    ChrTalk(
        0xFE,
        (
            "You must be Miss Mariabell and her\x01",
            "acquaintances, correct? Seats have\x01",
            "been prepared in the very back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1129")

    Jump("loc_11D5")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_11D5")

    ChrTalk(
        0xFE,
        (
            "We're in the process of making the final\x01",
            "preparations inside the main hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you would please wait a bit longer,\x01",
            "it would be greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D5")

    TalkEnd(0xFE)
    Return()

    # Function_9_E92 end

    def Function_10_11D9(): pass

    label("Function_10_11D9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "This is the first time my husband has brought\x01",
            "me along to the speaker's mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The anticipation for this auction is killing me.\x01",
            "I do hope we will be able to win something.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_11D9 end

    def Function_11_1298(): pass

    label("Function_11_1298")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My wife is usually extremely shy.\x01",
            "In order to break her out of her\x01",
            "shell, I decided to bring her along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to have her learn how to\x01",
            "behave in high society if she wants\x01",
            "to keep accompanying me places.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1298 end

    def Function_12_1375(): pass

    label("Function_12_1375")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(
        0xFE,
        (
            "My mansion back in the Empire is nothing\x01",
            "to scoff at, but this place blows mine out of\x01",
            "the water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now THIS is what you call luxurious...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_14BB")

    label("loc_141D")


    ChrTalk(
        0xFE,
        (
            "My mansion back in the Empire is nothing\x01",
            "to scoff at, but compared to this place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's just say, I wish I was born\x01",
            "as lucky as Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14BB")

    TalkEnd(0xFE)
    Return()

    # Function_12_1375 end

    def Function_13_14BF(): pass

    label("Function_13_14BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(
        0xFE,
        "The curtains are about to open...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll show all those naysayers. That Rosenberg\x01",
            "Studio doll is as good as mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x138,
        (
            "#2905FWhat's this...? It looks to me like tonight's\x01",
            "rival has finally made his appearance.\x02\x03",
            "#2900FYou aren't the only one with eyes for that\x01",
            "doll. And I assure you, I won't lose it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    ChrTalk(
        0xFE,
        (
            "Hohoh...? You have guts, young lady.\x01",
            "Please, try to go easy on me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_171A")

    label("loc_166D")


    ChrTalk(
        0xFE,
        (
            "I do not intend to let something so close\x01",
            "within my grasp slip away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x138, 500)

    ChrTalk(
        0xFE,
        "Try to go easy on me, young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#2900FHehe... As long as you do the same to me.\x02",
    )

    CloseMessageWindow()

    label("loc_171A")

    TalkEnd(0xFE)
    Return()

    # Function_13_14BF end

    def Function_14_171E(): pass

    label("Function_14_171E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, it seems like my dear husband is finding\x01",
            "it hard to contain his enthusiasm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once we're seated, I'll need him to cool his\x01",
            "head before the auction starts.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_171E end

    def Function_15_17CC(): pass

    label("Function_15_17CC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "(Since I've been talking to this woman for\x01",
            "a while now, I decided that, heck, I should\x01",
            "just invite her to the auction.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Well, I also had an ulterior motive. It wouldn't reflect\x01",
            "well on me if I came without a partner. Thank Aidios\x01",
            "for placing a convenient woman like her in my life.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_17CC end

    def Function_16_18F9(): pass

    label("Function_16_18F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 500, 500, 6800, 0)
    SetChrPos(0xEF, -500, 500, 6800, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    OP_68(-4530, 2300, 17580, 0)
    MoveCamera(326, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19400, 0)
    OP_68(5540, 2300, 24020, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(0, 2300, 11200, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16760, 0)
    OP_4B(0x8, 0xFF)

    def lambda_1A00():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A00)
    Sleep(200)

    def lambda_1A18():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A18)

    def lambda_1A2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A2D)

    def lambda_1A3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_1A3E)
    OP_68(0, 2300, 12950, 4000)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 2)
    OP_0D()

    ChrTalk(
        0x101,
        "#3500796V#5105F#12PWhat kind of place did we step into...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1B3D")

    ChrTalk(
        0x102,
        (
            "#3500797V#5301F#6PSpeaker Hartmann's mansion...\x02\x03",
            "#3500798VI've heard the rumors, but I didn't\x01",
            "expect it to be this grand...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C89")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1BFA")

    ChrTalk(
        0x103,
        (
            "#3500799V#5406F#6PThe overall atmosphere reminds me\x01",
            "more of a castle than a mansion...\x02\x03",
            "#3500800V#5401FI cannot fathom how much mira it\x01",
            "must cost to maintain this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C89")

    label("loc_1BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1C89")

    ChrTalk(
        0x104,
        (
            "#3500801V#5605F#6PHot damn!\x02\x03",
            "#3500802V#5601FI bet Erebonian nobles can't waltz in here\x01",
            "without feelin' a lil' depressed, y'know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C89")


    ChrTalk(
        0x101,
        (
            "#3500803V#5106F#12PThis exceeds every possible expectation\x01",
            "I had, that's for sure...\x02\x03",
            "#3500804V#5108F(Speaker Hartmann and Revache...)\x02\x03",
            "#3500805V#5113F(They're more influential than I initially thought.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        "#3500806V#11PDear guests...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1DB3():
        OP_95(0xFE, 0, 500, 14060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1DB3)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "#3500807V#5PWelcome to the Schwarze Auction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500808V#5PIs this your first time attending?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500809V#5100F#12PThat's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500810V#5PThe auction is scheduled to begin at 9PM\x01",
            "inside the main hall, straight ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500811V#5PThere is a banquet being held inside the\x01",
            "salon to your left. Please have a few drinks\x01",
            "and dine to your heart's content.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500812V#5PIf you don't mind me asking, are you\x01",
            "planning on staying the night with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500813V#5105F#12POh, we aren't.\x02\x03",
            "#3500814V#5104FYou see, we've already booked a room\x01",
            "at Hotel Delphinia and have friends\x01",
            "waiting for us there.\x02\x03",
            "#3500815V#5100FWe appreciate the offer, but we'll have\x01",
            "to pass this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500816V#5PVery well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500817V#5PIf you change your mind, please do not\x01",
            "hesitate to inform one of the attendants.\x01",
            "We'll prepare a room straight away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500818V#5PAlso, you are more than welcome to stroll\x01",
            "around the estate as much as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500819V#5PHowever, please be aware that there are\x01",
            "a few restricted areas. We apologize for\x01",
            "the inconvenience in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500820V#5100F#12PThat shouldn't be an issue.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2296")

    ChrTalk(
        0x102,
        (
            "#3500821V#5302F#6PThank you for the explanation.\x01",
            "We will heed your words.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2303")

    ChrTalk(
        0x103,
        (
            "#3500822V#5402F#6PThank you for informing us. We will\x01",
            "make sure not to cause any trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_2303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2344")

    ChrTalk(
        0x104,
        "#3500823V#5609F#6PThanks for lettin' us know, man.\x02",
    )

    CloseMessageWindow()

    label("loc_2344")


    ChrTalk(
        0x8,
        (
            "#3500824V#5PMy pleasure. If you need anything or have\x01",
            "any complaints, please make sure to inform\x01",
            "me or one of the other attendants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500825V#5PNow, if you'll excuse me...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)

    def lambda_2406():
        OP_95(0xFE, 1910, 500, 19610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2406)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#3500826V#5103F#2P(We have roughly two hours before\x01",
            "the auction gets underway.)\x02\x03",
            "#3500827V#5101F(Let's scope out the mansion for now.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2529")

    ChrTalk(
        0x102,
        (
            "#3500828V#5301F#1P(Of course. We should gather information\x01",
            "while we have the chance.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_2529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_255C")

    ChrTalk(
        0x103,
        "#3500829V#5401F#1P(Roger that.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_25C7")

    ChrTalk(
        0x104,
        (
            "#3500830V#5600F#1P(Sounds like a plan. We can even grab\x01",
            "a bite to eat while lookin' around.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C7")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 500, 12000, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 0)
    OP_29(0x47, 0x1, 0x9)
    OP_1B(0x0, 0x0, 0x1A)
    EventEnd(0x5)
    Return()

    # Function_16_18F9 end

    def Function_17_260E(): pass

    label("Function_17_260E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36100.itc", 0x1E)
    LoadChrToIndex("chr/ch02200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -4010, 500, 25720, 180)
    OP_68(0, 1600, 19000, 0)
    MoveCamera(325, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1A, 0, 500, 15000, 0)
    SetChrPos(0x15, 0, 500, 13500, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1B, 0, 500, 12000, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -14500, 500, 20600, 90)
    SetChrPos(0xEF, -14500, 500, 19400, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 2500)

    def lambda_27AA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_27AA)

    def lambda_27BF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_27BF)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x1A, 0xB4, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1A,
        (
            "#3501099VHmph. I wasn't expecting this.\x02\x03",
            "#3501100VI was sure they'd try to pull something\x01",
            "stupid by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x15,
        "#3501101V#6PNothin' out of the ordinary so far, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3501102V#6PBesides, I doubt even Heiyue could pull\x01",
            "off somethin' big enough to ruin Speaker\x01",
            "Hartmann's rep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501103V#3103F#11PDon't underestimate 'em, dumbass.\x02\x03",
            "#3501104V#3101FForget Yin. I've heard stories that this Cao\x01",
            "guy's even got Heiyue's old guard on edge.\x02\x03",
            "#3501105VYou're as good as dead if you leave your\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501106V#6PS-Sorry, Boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501107V#3103F#11PAnyway, something just feels off with\x01",
            "this year's auction...\x02\x03",
            "#3501108VI have a feeling that someone besides\x01",
            "Heiyue is messing with us...\x02\x03",
            "#3501109V#3101FThat's what my gut says, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501110V#6PR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501111V#6PIs that your jaeger instincts talkin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501112V#3104F#11PSure, something like that.\x02\x03",
            "#3501113V#3102FHeh. I must be gettin' old.\x02\x03",
            "#3501114VI'd love it if everything went off without\x01",
            "a hitch, but...this anxiety ain't going away.\x02\x03",
            "#3501115VI almost feel that excitement I'd get before\x01",
            "going on a hunt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501116V#6PH-Hahaha...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-12460, 1600, 21220, 0)
    MoveCamera(325, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-1910, 1600, 19760, 4500)

    def lambda_2CFE():
        OP_95(0xFE, -4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CFE)
    Sleep(100)

    def lambda_2D1B():
        OP_95(0xFE, -4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D1B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501117V#5105F#5PHe's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2DC5")

    ChrTalk(
        0x102,
        "#3501118V#5301F#5P(...Garcia Rossi!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E41")

    label("loc_2DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2E06")

    ChrTalk(
        0x103,
        "#3501119V#5401F#5P(...the mafia's underboss!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E41")

    label("loc_2E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E41")

    ChrTalk(
        0x104,
        "#3501120V#5607F#5P(...the Killing Bear, eh?)\x02",
    )

    CloseMessageWindow()

    label("loc_2E41")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E7E")

    def lambda_2E76():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E76)

    label("loc_2E7E")


    def lambda_2E83():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2E83)
    Sleep(50)

    def lambda_2E93():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E93)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    ChrTalk(
        0x1A,
        (
            "#3501121V#3104F#12PApologies.\x02\x03",
            "#3501122V#3100FMy name is Garcia Rossi. I'm in charge\x01",
            "of tonight's security detail.\x02\x03",
            "#3501123VAs a part of that, I make sure to patrol\x01",
            "this area every so often. Please forgive\x01",
            "me for any inconvenience that may cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501124V#5112F#5PIt's fine. You all are doing a great job.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3034")

    ChrTalk(
        0x102,
        "#3501125V#5308F#5P(If we keep talking to him, he's bound to...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_30D7")

    label("loc_3034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3086")

    ChrTalk(
        0x103,
        "#3501126V#5408F#5P(We have to find some excuse to leave or...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_30D7")

    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_30D7")

    ChrTalk(
        0x104,
        "#3501127V#5608F#5P(Kinda stuck between a rock and a hard place...)\x02",
    )

    CloseMessageWindow()

    label("loc_30D7")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-3300, 1600, 20000, 2500)

    def lambda_3102():
        OP_95(0xFE, -2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3102)
    Sleep(300)
    Sound(1856, 255, 100, 0)
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#3501128V#3105F#12PSir, something tells me that we may\x01",
            "have met somewhere before...\x02\x03",
            "#3501129V#3101FHmm...?\x02",
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
        (
            "#3501130V#5104F#5PAren't you simply imagining things?\x02\x03",
            "#3501131V#5100FI doubt I'd forget meeting a mountain\x01",
            "of a man such as yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3503001V#3109F#12PHaha! You make a good point.\x02\x03",
            "#3501132V#3100FStill...just to be safe, do you mind\x01",
            "telling me your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501133V#5103F#5PSure, I don't see why not.\x02\x03",
            "#3501134V#5100FGuy Bannings. Pleased to meet you, Mr. Rossi.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "#3501135V#3105F#12PGuy...?\x02\x03",
            "#3501136VSomething about that rings a bell...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_33F9")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#3501137V#3101F#12PAnd who might your friend be...?\x02",
    )

    CloseMessageWindow()

    label("loc_33F9")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    ChrTalk(
        0x101,
        "#3501138V#5110F#5P(Crap... Did I screw up?!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_349C")

    ChrTalk(
        0x102,
        "#3501139V#5301F#5P(What should we do, Lloyd...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3521")

    label("loc_349C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_34DE")

    ChrTalk(
        0x103,
        "#3501140V#5401F#5P(Things are looking grim...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3521")

    label("loc_34DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3521")

    ChrTalk(
        0x104,
        "#3501141V#5610F#5P(Well, if worse comes to worst...)\x02",
    )

    CloseMessageWindow()

    label("loc_3521")


    NpcTalk(
        0x1B,
        "Woman's Voice",
        "#3501142V#11PHehe. Looks like I'm late.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_35AC():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35AC)

    def lambda_35B9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_35B9)
    Sleep(100)

    def lambda_35C9():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_35C9)

    def lambda_35D6():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_35D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_35F3():

        label("loc_35F3")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_35F3")

    QueueWorkItem2(0x15, 1, lambda_35F3)
    OP_68(-2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_3621():
        OP_95(0xFE, -1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3621)
    WaitChrThread(0x1B, 1)
    OP_6F(0x1)
    EndChrThread(0x15, 0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501143V#5105F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_36C6")

    ChrTalk(
        0x102,
        "#3501144V#5305F#5PB-Bell...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_36C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_36FA")

    ChrTalk(
        0x103,
        "#3501145V#5405F#5PMariabell...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_372F")

    label("loc_36FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_372F")

    ChrTalk(
        0x104,
        "#3501146V#5605F#5PWhoa, Mariabell...?!\x02",
    )

    CloseMessageWindow()

    label("loc_372F")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1B,
        (
            "#3501147VGood evening, 'Guy.'\x02\x03",
            "#3501148VFancy meeting you here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#3501149V#5112F#5PY-Yeah, you, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_383F")

    ChrTalk(
        0x102,
        "#3501150V#5306F#5PYes... Quite unexpected.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_383F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3881")

    ChrTalk(
        0x103,
        "#3501151V#5406F#5PI did not anticipate this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BE")

    label("loc_3881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_38BE")

    ChrTalk(
        0x104,
        "#3501152V#5606F#5PFunny thing, coincidences...\x02",
    )

    CloseMessageWindow()

    label("loc_38BE")


    ChrTalk(
        0x1A,
        "#3501153V#3100F#11PHmm...? And who might you be, madam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501154V#2904F#6PI'm Mariabell Crois.\x02\x03",
            "#3501155V#2902FThe pleasure's all mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        "#3501156V#11PCrois? She's the IBC's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501157V#3104F#11PYou have my sincerest apologies, Ms. Crois.\x01",
            "I assure you, I'm well aware of who you are.\x02\x03",
            "#3501158V#3100FI take it you finally decided to accept our\x01",
            "invitation this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501159V#2904F#6PHehe, I thought it would paint me in a bad\x01",
            "light if I kept on refusing your kind offers.\x02\x03",
            "#3501160V#2900FAlso, these two guests are dear friends\x01",
            "of mine...\x02\x03",
            "#3501161VDo you have some problem with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501162V#3104F#11POh, of course not.\x02\x03",
            "#3501163V#3100FAllow me the privilege of welcoming you\x01",
            "to the Schwarze Auction one more time.\x02\x03",
            "#3501164VWould you like me to show you to where\x01",
            "Speaker Hartmann is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501165V#2904F#6PI will pay our beloved speaker a visit later.\x02\x03",
            "#3501166V#2902FIn the meantime, could you have a room\x01",
            "prepared for me?\x02\x03",
            "#3501167VI've been in a business meeting a good\x01",
            "portion of the day and would love to get\x01",
            "a bit of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#3501168V#3104F#11PAbsolutely.\x02",
    )

    CloseMessageWindow()
    OP_68(-3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#3501169V#3100F#6PYou heard her. Ms. Crois would like\x01",
            "a room prepared.\x02\x03",
            "#3501170VYou better get your act together and\x01",
            "treat her with respect, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x1A, 500)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#3501171V#11PY-Yes, sir. Please, Ms. Crois, allow me\x01",
            "to show you to your room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x37, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("t117B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_260E end

    def Function_18_3E88(): pass

    label("Function_18_3E88")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36100.itc", 0x1E)
    LoadChrToIndex("chr/ch02200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 4010, 500, 25720, 180)
    OP_68(0, 1600, 19000, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1A, 0, 500, 15000, 0)
    SetChrPos(0x15, 0, 500, 13500, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1B, 0, 500, 12000, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 14500, 500, 20600, 90)
    SetChrPos(0xEF, 14500, 500, 19400, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    FadeToBright(1000, 0)
    SetCameraDistance(19000, 2500)

    def lambda_4024():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4024)

    def lambda_4039():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4039)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x1A, 0xB4, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x1A,
        (
            "#3501099VHmph. I wasn't expecting this.\x02\x03",
            "#3501100VI was sure they'd try to pull something\x01",
            "stupid by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x15,
        "#3501101V#12PNothin' out of the ordinary so far, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3501102V#12PBesides, I doubt even Heiyue could pull\x01",
            "off somethin' big enough to ruin Speaker\x01",
            "Hartmann's rep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501103V#3103F#5PDon't underestimate 'em, dumbass.\x02\x03",
            "#3501104V#3101FForget Yin. I've heard stories sayin' that Cao\x01",
            "guy can get the Heiyue leaders to bend over\x01",
            "backwards for him. He's that good.\x02\x03",
            "#3501105VYou're as good as dead if you leave your\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501106V#12PS-Sorry, boss. Won't happen again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501107V#3103F#5PAnyway, something just feels off with\x01",
            "this year's auction...\x02\x03",
            "#3501108VI have a feeling that someone besides\x01",
            "Heiyue is messing with us...\x02\x03",
            "#3501109V#3101FThat's what my gut says, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501110V#12PR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501111V#12PIs that your jaeger instincts talkin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501112V#3104F#5PSure, something like that.\x02\x03",
            "#3501113V#3102FHeh. I must be gettin' old.\x02\x03",
            "#3501114VI'd love it if everything went on\x01",
            "without a hitch, but...\x01",
            "This anxiety ain't going away.\x02\x03",
            "#3501115VI almost feel that excitement I'd\x01",
            "get before going on a hunt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#3501116V#12PHahaha...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(12460, 1600, 21220, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(1910, 1600, 19760, 4500)

    def lambda_45B3():
        OP_95(0xFE, 4000, 500, 20600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_45B3)
    Sleep(100)

    def lambda_45D0():
        OP_95(0xFE, 4000, 500, 19400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_45D0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501117V#5105F#11PHe's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_467C")

    ChrTalk(
        0x102,
        "#3501118V#5301F#11P(...Garcia Rossi!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_46F5")

    label("loc_467C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_46B9")

    ChrTalk(
        0x103,
        "#3501119V#5401F#11P(...the mafia's boss!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_46F5")

    label("loc_46B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_46F5")

    ChrTalk(
        0x104,
        "#3501120V#5607F#11P(...the Killing Bear, eh?)\x02",
    )

    CloseMessageWindow()

    label("loc_46F5")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4732")

    def lambda_472A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_472A)

    label("loc_4732")


    def lambda_4737():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4737)
    Sleep(50)

    def lambda_4747():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4747)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    ChrTalk(
        0x1A,
        (
            "#3501121V#3104F#6PApologies.\x02\x03",
            "#3501122V#3100FMy name is Garcia Rossi. I'm in charge\x01",
            "of tonight's security detail.\x02\x03",
            "#3501123VAs a part of that, I make sure to patrol\x01",
            "this area every so often. Please forgive\x01",
            "me of any inconvenience that may cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501124V#5112F#11PIt's fine. You all are doing a great job.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_48E8")

    ChrTalk(
        0x102,
        "#3501125V#5308F#11P(If we keep talking to him, he's bound to...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_498D")

    label("loc_48E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_493B")

    ChrTalk(
        0x103,
        "#3501126V#5408F#11P(We have to find some excuse to leave or...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_498D")

    label("loc_493B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_498D")

    ChrTalk(
        0x104,
        "#3501127V#5608F#11P(Kinda stuck between a rock and a hard place...)\x02",
    )

    CloseMessageWindow()

    label("loc_498D")

    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3300, 1600, 20000, 2500)

    def lambda_49B8():
        OP_95(0xFE, 2500, 500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_49B8)
    Sleep(300)
    Sound(1856, 255, 100, 0)
    WaitChrThread(0x1A, 1)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#3501128V#3105F#6PSir, something tells me that we may\x01",
            "have met somewhere before...\x02\x03",
            "#3501129V#3101FHmm...?\x02",
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
        (
            "#3501130V#5104F#11PAren't you simply imagining things?\x02\x03",
            "#3501131V#5100FI doubt I'd forget meeting a mountain\x01",
            "like yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3503001V#3109F#6PHaha! You make a good point.\x02\x03",
            "#3501132V#3100FStill...just to be safe, do you mind\x01",
            "telling me your name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501133V#5103F#11PSure, I don't see why not.\x02\x03",
            "#3501134V#5100FGuy Bannings. Pleased to meet you, Mr. Rossi.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A,
        (
            "#3501135V#3105F#6PGuy...?\x02\x03",
            "#3501136VSomething about that rings a bell...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4CA1")
    TurnDirection(0x1A, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#3501137V#3101F#6PAnd who might your friend be...?\x02",
    )

    CloseMessageWindow()

    label("loc_4CA1")

    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0xEF)

    ChrTalk(
        0x101,
        "#3501138V#5110F#11P(Crap... Did I screw up?!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4D46")

    ChrTalk(
        0x102,
        "#3501139V#5301F#11P(What should we do, Lloyd...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCD")

    label("loc_4D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4D89")

    ChrTalk(
        0x103,
        "#3501140V#5401F#11P(Things are looking grim...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DCD")

    label("loc_4D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4DCD")

    ChrTalk(
        0x104,
        "#3501141V#5610F#11P(Well, if worse comes to worst...)\x02",
    )

    CloseMessageWindow()

    label("loc_4DCD")


    NpcTalk(
        0x1B,
        "Woman's Voice",
        "#3501142V#5PHehe. Looks like I'm late.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4E57():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E57)

    def lambda_4E64():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4E64)
    Sleep(100)

    def lambda_4E74():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4E74)

    def lambda_4E81():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4E81)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x15, 1)

    def lambda_4E9E():

        label("loc_4E9E")

        TurnDirection(0x15, 0x1B, 500)
        Yield()
        Jump("loc_4E9E")

    QueueWorkItem2(0x15, 1, lambda_4E9E)
    OP_68(2700, 1600, 19140, 3000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_4ECC():
        OP_95(0xFE, 1820, 500, 17630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4ECC)
    WaitChrThread(0x1B, 1)
    OP_6F(0x1)
    EndChrThread(0x15, 0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501143V#5105F#11PHuh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4F73")

    ChrTalk(
        0x102,
        "#3501144V#5305F#11PB-Bell...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FDE")

    label("loc_4F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4FA8")

    ChrTalk(
        0x103,
        "#3501145V#5405F#11PMariabell...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FDE")

    label("loc_4FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4FDE")

    ChrTalk(
        0x104,
        "#3501146V#5605F#11PWhoa, Mariabell...?!\x02",
    )

    CloseMessageWindow()

    label("loc_4FDE")

    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x1B,
        (
            "#3501147VGood evening, 'Guy.'\x02\x03",
            "#3501148VFancy meeting you here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        "#3501149V#5112F#11PY-Yeah, you, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_50F0")

    ChrTalk(
        0x102,
        "#3501150V#5306F#11PYes... Quite unexpected.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5171")

    label("loc_50F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5133")

    ChrTalk(
        0x103,
        "#3501151V#5406F#11PI did not anticipate this...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5171")

    label("loc_5133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5171")

    ChrTalk(
        0x104,
        "#3501152V#5606F#11PFunny thing, coincidences...\x02",
    )

    CloseMessageWindow()

    label("loc_5171")


    ChrTalk(
        0x1A,
        "#3501153V#3105F#5PHmm...? And who might you be, madam?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501154V#2904F#12PI'm Mariabell Crois.\x02\x03",
            "#3501155V#2902FThe pleasure's all mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        "#3501156V#5PCrois? She's the IBC's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501157V#3104F#5PYou have my sincerest apologies, Ms. Crois.\x01",
            "I assure you, I'm well aware of who you are.\x02\x03",
            "#3501158V#3100FI take it you finally decided to accept our\x01",
            "invitation this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501159V#2904F#12PHehe, I thought it would paint me in a bad\x01",
            "light if I kept on refusing your kind offers.\x02\x03",
            "#3501160V#2900FAlso, these two guests are dear friends\x01",
            "of mine...\x02\x03",
            "#3501161VDo you have some problem with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501162V#3104F#5POh, of course not.\x02\x03",
            "#3501163V#3100FAllow me the privilege of welcoming you\x01",
            "to the Schwarze Auction one more time.\x02\x03",
            "#3501164VWould you like me to show you to where\x01",
            "Speaker Hartmann is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#3501165V#2904F#12PI will pay our beloved Speaker a visit later.\x02\x03",
            "#3501166V#2902FIn the meantime, could you have a room\x01",
            "prepared for me?\x02\x03",
            "#3501167VI've been in a business meeting a good\x01",
            "portion of the day and would love to get\x01",
            "a bit of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#3501168V#3104F#5PAbsolutely.\x02",
    )

    CloseMessageWindow()
    OP_68(3030, 1600, 20130, 1200)
    OP_93(0x1A, 0x0, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x1A,
        (
            "#3501169V#3100F#12PYou heard her. Ms. Crois would like\x01",
            "a room prepared.\x02\x03",
            "#3501170VYou better get your act together and\x01",
            "treat her with respect, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x1A, 500)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#3501171V#5PY-Yes, sir. Please, Ms. Crois, allow me\x01",
            "to show you to your room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    AddParty(0x37, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("t117B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3E88 end

    def Function_19_5739(): pass

    label("Function_19_5739")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-80, 1800, 19610, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 500, 25200, 180)
    SetChrPos(0xEF, 600, 500, 25200, 180)
    SetChrPos(0x151, 0, 500, 24000, 180)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    FadeToBright(1000, 0)
    SetCameraDistance(17000, 3000)

    def lambda_57DB():
        OP_95(0xFE, 0, 500, 19000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_57DB)
    Sleep(100)

    def lambda_57F8():
        OP_95(0xFE, -600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57F8)
    Sleep(50)

    def lambda_5815():
        OP_95(0xFE, 600, 500, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5815)

    def lambda_582F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_582F)

    def lambda_5840():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_5840)

    def lambda_5851():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_5851)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x151, 0x0, 0x1F4)

    ChrTalk(
        0x151,
        (
            "#3501375V#5703F#12P(The guard dogs they put in the\x01",
            "courtyard are all fast asleep...)\x02\x03",
            "#3501376V#5702F(Now, what could that mean?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501377V#5103F#5P(Considering the situation...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does the dogs falling asleep mean?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[There's an intruder]\x01",                # 0
            "[It's a trap laid by the mafia]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59E2"),
        (1, "loc_5B71"),
        (SWITCH_DEFAULT, "loc_5C71"),
    )


    label("loc_59E2")

    OP_2C(0x47, 0x1)

    ChrTalk(
        0x101,
        (
            "#3501378V#5113F#5P(I think it's likely that there is an\x01",
            "intruder in our midst.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5A7E")

    ChrTalk(
        0x102,
        "#3501379V#5301F#5P(I think so, too.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AE2")

    label("loc_5A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5AB8")

    ChrTalk(
        0x103,
        "#3501380V#5401F#5P(That seems likely.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AE2")

    label("loc_5AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5AE2")

    ChrTalk(
        0x104,
        "#3501381V#5601F#5P(Agreed.)\x02",
    )

    CloseMessageWindow()

    label("loc_5AE2")


    ChrTalk(
        0x151,
        (
            "#3501382V#5704F#12P(In any case, something is definitely\x01",
            "happening behind the scenes...)\x02\x03",
            "#3501383V#5702F(That's our only absolute.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C71")

    label("loc_5B71")


    ChrTalk(
        0x101,
        (
            "#3501384V#5108F#5P(It might be a trap laid by the mafia,\x01",
            "in order to trip us up...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501385V#5706F#12P(Forgive me, but I think you're\x01",
            "overthinking things.)\x02\x03",
            "#3501386V#5702F(In any case, something is\x01",
            "definitely happening behind\x01",
            "the scenes.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C71")

    label("loc_5C71")


    ChrTalk(
        0x101,
        (
            "#3501387V#5101F#5P(Let's make one more lap around\x01",
            "the mansion, just to be sure.)\x02\x03",
            "#3501388V(We might notice something different.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xE1, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5D30")

    ChrTalk(
        0x102,
        "#3501389V#5301F#5P(Let's go!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DA0")

    label("loc_5D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5D63")

    ChrTalk(
        0x103,
        "#3501390V#5401F#5P(Understood!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DA0")

    label("loc_5D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5DA0")

    ChrTalk(
        0x104,
        "#3501391V#5601F#5P(I hear you loud and clear.)\x02",
    )

    CloseMessageWindow()

    label("loc_5DA0")


    ChrTalk(
        0x151,
        (
            "#3501392V#5709F#12P(Be a friend and let me tag\x01",
            "along, okay?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 500, 18770, 180)
    SetScenarioFlags(0xA6, 2)
    OP_29(0x47, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_19_5739 end

    def Function_20_5E02(): pass

    label("Function_20_5E02")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch31900.itc", 0x20)
    LoadChrToIndex("chr/ch02200.itc", 0x21)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 2000, 500, 18000, 270)
    SetChrPos(0x14, -1000, 500, 19600, 90)
    SetChrPos(0x15, -1000, 500, 18000, 90)
    SetChrPos(0x16, -1000, 500, 16400, 90)
    SetChrPos(0x17, -2400, 500, 19600, 90)
    SetChrPos(0x18, -2400, 500, 18000, 90)
    SetChrPos(0x19, -2400, 500, 16400, 90)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(4059, 1700, 17050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_68(60, 1700, 18000, 2500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#3501582V#3104F#11PHeh... So the mice have finally decided to\x01",
            "come out and play, eh?\x02\x03",
            "#3501583V#3107FIt's time for the hunt to begin!\x02\x03",
            "#3501584VKeep the guests in the main hall and seal off\x01",
            "all exits!\x02\x03",
            "#3501585VNone of them are escaping, you hear?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(80, 140, -1, -1)
    SetChrName("Mafiosos")
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)

    AnonymousTalk(
        0xFF,
        "#3501586V#4SUnderstood, Boss!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xA6, 7)
    OP_29(0x47, 0x1, 0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("t119B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5E02 end

    def Function_21_60F2(): pass

    label("Function_21_60F2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch31900.itc", 0x20)
    LoadChrToIndex("chr/ch02200.itc", 0x21)
    LoadChrToIndex("chr/ch06200.itc", 0x22)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 0, 500, 19500, 180)
    SetChrPos(0x1A, 0, 500, 17500, 0)
    SetChrPos(0x14, 0, 500, 16000, 0)
    SetChrPos(0x15, 1500, 500, 16000, 0)
    SetChrPos(0x16, -1500, 500, 16000, 0)
    OP_52(0x1A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-4990, 1700, 17500, 0)
    MoveCamera(325, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1700, 17500, 2500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x1C,
        (
            "#3501602V#3007F#11PDamn it...! You still haven't found\x01",
            "the intruders?!\x02\x03",
            "#3501603VThe guests are about to start a\x01",
            "riot in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#3501604V#3103F#6PYou have to be patient.\x02\x03",
            "#3501605V#3100FThe mansion has been completely sealed off. Those\x01",
            "pests are nothing more than a bunch of scared mice\x01",
            "now, desperately lookin' for a way out of their cage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#3501606V#3003F#11PDamn it... If this keeps up, Speaker Hartmann\x01",
            "is going to...\x02\x03",
            "#3501607V#3007FJust hurry up and find them!\x02\x03",
            "#3501608VKill those brats if you have to!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xA7, 1)
    SetScenarioFlags(0x5C, 1)
    NewScene("t119B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_60F2 end

    def Function_22_645E(): pass

    label("Function_22_645E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00450.itc", 0x26)
    LoadChrToIndex("chr/ch00451.itc", 0x27)
    LoadChrToIndex("chr/ch31000.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_64D0")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_64F7")

    label("loc_64D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_64E6")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_64F7")

    label("loc_64E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_64F7")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_64F7")

    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrChipByIndex(0x17, 0x28)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x17, 0, 500, 19600, 180)
    SetChrPos(0x18, 0, 500, 18000, 0)
    SetChrPos(0x101, -10780, 500, 16940, 90)
    SetChrPos(0xEF, -10780, 500, 16940, 90)
    SetChrPos(0x105, -10780, 500, 16940, 90)
    SetChrPos(0x133, -10780, 500, 16940, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x133, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-1500, 1600, 19000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, 19000, 2500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501705V#0000F#2P(Yes! There's not many of them!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6686")

    ChrTalk(
        0x102,
        "#3501706V#0100F#2P(Let's force our way through!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6710")

    label("loc_6686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_66CE")

    ChrTalk(
        0x103,
        "#3501707V#0202F#2P(We can break through their line!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6710")

    label("loc_66CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_6710")

    ChrTalk(
        0x104,
        "#3501708V#0300F#2P(Time to smash up their defense!)\x02",
    )

    CloseMessageWindow()

    label("loc_6710")


    ChrTalk(
        0x105,
        "#3501709V#0400F#2P(Shall we?!)\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6760():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6760)
    Sleep(50)

    def lambda_6770():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6770)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)

    ChrTalk(
        0x17,
        "#3501710V#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3501711V#11PWhat in the world...?\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(-2130, 1400, 19140, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22800, 0)
    SetCameraDistance(19800, 2000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x133, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -9740, 500, 18820, 90)
    SetChrPos(0xEF, -11480, 500, 18040, 90)
    SetChrPos(0x105, -11140, 500, 19670, 90)
    SetChrPos(0x133, -12980, 500, 18940, 90)

    def lambda_6870():
        OP_95(0xFE, -4740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6870)
    Sleep(50)

    def lambda_688D():
        OP_95(0xFE, -6480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_688D)
    Sleep(50)

    def lambda_68AA():
        OP_95(0xFE, -6140, 500, 19670, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_68AA)
    Sleep(100)

    def lambda_68C7():
        OP_95(0xFE, -7980, 500, 18940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_68C7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        "#3501712V#11PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#3501713V#11PWeren't they outside?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_699D")

    ChrTalk(
        0x102,
        "#3501714V#0107F#6PYou're too slow!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_699D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_69E9")

    ChrTalk(
        0x103,
        "#3501715V#0207F#6PYou should work on your reaction time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A1E")

    label("loc_69E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_6A1E")

    ChrTalk(
        0x104,
        "#3501716V#0307F#3PHeads-up, slowpokes!\x02",
    )

    CloseMessageWindow()

    label("loc_6A1E")

    SetCameraDistance(15800, 300)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_6A3E():
        OP_95(0xFE, -740, 500, 18820, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A3E)

    def lambda_6A58():
        OP_95(0xFE, -2480, 500, 18040, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6A58)

    def lambda_6A72():
        OP_95(0xFE, -2980, 500, 19260, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6A72)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 23)
    Return()

    # Function_22_645E end

    def Function_23_6AB4(): pass

    label("Function_23_6AB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00450.itc", 0x26)
    LoadChrToIndex("chr/ch00451.itc", 0x27)
    LoadChrToIndex("chr/ch31000.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31053.itc", 0x2A)
    LoadChrToIndex("chr/ch31153.itc", 0x2B)
    LoadChrToIndex("chr/ch06200.itc", 0x2C)
    LoadChrToIndex("chr/ch06500.itc", 0x2D)
    LoadChrToIndex("chr/ch05500.itc", 0x2E)
    LoadChrToIndex("chr/ch00000.itc", 0x2F)
    LoadChrToIndex("apl/ch50364.itc", 0x30)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x3)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x3)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x17, 3470, 500, 19830, 270)
    SetChrPos(0x18, 2770, 500, 17960, 270)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x2D)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1B, 0x2E)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1D, 0x8000)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1B, 0x8000)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1C, 0, 4000, 33000, 180)
    SetChrPos(0x1D, 600, 500, 28500, 180)
    SetChrPos(0x1B, 0, 1500, 32500, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6C11")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_6C38")

    label("loc_6C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_6C27")
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_6C38")

    label("loc_6C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_6C38")
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    label("loc_6C38")

    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -50, 500, 18760, 90)
    SetChrPos(0xEF, -950, 500, 19580, 90)
    SetChrPos(0x105, -1080, 500, 17400, 90)
    SetChrPos(0x133, -2650, 500, 18280, 90)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    OP_68(0, 1400, 19000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18750, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18000, 1500)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(100)

    def lambda_6CFD():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CFD)

    def lambda_6D0A():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6D0A)
    Sleep(100)

    def lambda_6D1A():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6D1A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    Sleep(100)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)

    NpcTalk(
        0x1C,
        "Man's Voice",
        (
            "#3501717V#4PQuiet down, you lot! Have you\x01",
            "still not fou--\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x133, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6DEE():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DEE)

    def lambda_6DFB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6DFB)
    Sleep(100)

    def lambda_6E0B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E0B)

    def lambda_6E18():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_6E18)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)
    Sleep(100)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1C, -600, 500, 28500, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Fade(500)
    OP_68(-560, 1600, 22180, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18650, 0)

    def lambda_6E91():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6E91)
    WaitChrThread(0x1C, 1)
    OP_0D()
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#3501718V#3005F#5PWh-Who the hell are you people?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3501719V#5805F#12P#NWooow! He's even rounder up close!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6F6D")

    ChrTalk(
        0x102,
        "#3501720V#0101F#12PDon Marconi...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FDD")

    label("loc_6F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_6FA2")

    ChrTalk(
        0x103,
        "#3501721V#0201F#12PRevache's don!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FDD")

    label("loc_6FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_6FDD")

    ChrTalk(
        0x104,
        "#3501722V#0307F#12PRevache's head honcho...!\x02",
    )

    CloseMessageWindow()

    label("loc_6FDD")

    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3501723V#0007F#11PForget about him! We need\x01",
            "to keep moving!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_702B():
        OP_95(0xFE, -800, 500, 18640, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_702B)
    WaitChrThread(0x133, 1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x30)
    SetChrSubChip(0x101, 0x5)
    Sound(910, 0, 100, 0)
    Sleep(250)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        "#3501724V#0402F#12PArrivederci!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20650, 2000)
    BeginChrThread(0x105, 3, 0, 24)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(100)
    BeginChrThread(0xEF, 3, 0, 24)
    OP_63(0x1C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x1C)
    Sleep(300)
    OP_63(0x1C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    OP_6F(0x10)

    ChrTalk(
        0x1C,
        "#3501725V#3001F#5PWh-Wh-Wha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x1C,
        (
            "#3501726V#3007F#5P#4SWHAT ARE YOU LYING ON\x01",
            "THE FLOOR FOR?!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1030, 1600, 20870, 1500)
    SetCameraDistance(16780, 1500)
    OP_63(0x1C, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_71C4():
        OP_95(0xFE, 690, 500, 21650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_71C4)
    WaitChrThread(0x1C, 1)
    OP_93(0x1C, 0x87, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x1C,
        (
            "#3501727V#3007F#5PGET UP AND FOLLOW THEM!\x02\x03",
            "#3501728V#3001FWhere the hell is Garcia?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-940, 2500, 27990, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    OP_68(-940, 2500, 29990, 4000)
    Sleep(1500)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    BeginChrThread(0x1B, 3, 0, 25)
    WaitChrThread(0x1B, 3)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x1B,
        (
            "#3501729V#2902F#5P(My, isn't this an interesting turn\x01",
            "of events?)\x02\x03",
            "#3501730V#2905F(But that girl that Lloyd was carrying...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_734C")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_7373")

    label("loc_734C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_7362")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_7373")

    label("loc_7362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7373")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_7373")

    SetScenarioFlags(0x5C, 0)
    NewScene("t110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_6AB4 end

    def Function_24_7380(): pass

    label("Function_24_7380")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_738C():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_738C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_7380 end

    def Function_25_73A1(): pass

    label("Function_25_73A1")


    def lambda_73A6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73A6)

    def lambda_73BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_73BB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_73A1 end

    def Function_26_73D0(): pass

    label("Function_26_73D0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7473")

    ChrTalk(
        0x101,
        (
            "#5101F(It took a lot of effort to sneak in here, so we\x01",
            "shouldn't waste it. Let's check out the mansion\x01",
            "a bit more before the auction starts.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_755D")

    ChrTalk(
        0x138,
        (
            "#2905FOh, aren't you planning on heading to\x01",
            "the auction? It's held in the main hall,\x01",
            "right through those doors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5105FUh, yeah.\x02\x03",
            "#5100FSince we're all here, why don't we\x01",
            "head inside together?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_75DB")

    label("loc_755D")


    ChrTalk(
        0x101,
        (
            "#5101FThe auction is being held in the main\x01",
            "hall straight ahead of us... Trying to\x01",
            "sneak away now would look suspicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_762C")

    ChrTalk(
        0x101,
        (
            "#5101FSomething is off... Let's look around\x01",
            "the mansion some more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_762C")

    Sleep(50)
    SetChrPos(0x0, 0, 0, -1030, 360)
    EventEnd(0x4)
    Return()

    # Function_26_73D0 end

    SaveToFile()

Try(main)
