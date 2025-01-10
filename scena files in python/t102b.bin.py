from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t102b.bin",                # FileName
        "t102b",                    # MapName
        "t102b",                    # Location
        0x0095,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 149, 0, 2, 0, 3],
    )

    BuildStringList((
        "t102b",                  # 0
        "Elise",                  # 1
        "James",                  # 2
        "Nikita",                 # 3
        "Young Man",              # 4
        "Woman",                  # 5
        "Girl",                   # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Clerk",                  # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Mafioso",                # 12
        "Mafioso",                # 13
        "Mafioso",                # 14
        "犬１",                   # 15
        "犬２",                   # 16
        "SE制御",                 # 17
        "bt102b",                 # 18
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 10, 12, 180)
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
        "BattleInfo_E4", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt102b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms31102.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50363.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch32300.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch27800.itc",                   # 04
        "chr/ch26800.itc",                   # 05
        "chr/ch21100.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch24400.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch23600.itc",                   # 0B
        "chr/ch25900.itc",                   # 0C
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

    DeclNpc(12250,   0,       11149,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-24909,  0,       5570,    90,   385,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-23729,  0,       5570,    270,  385,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(100139,  0,       18219,   0,    385,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-23930,  0,       11470,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-22840,  0,       10689,   315,  401,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3279,    0,       2970,    225,  385,  0x0, 0,   9,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2539,    0,       2380,    45,   385,  0x0, 0,   10,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-18940,  0,       12609,   180,  385,  0x0, 0,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 15,  -11.0,                 8.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.6666667461395264,    -0.800000011920929,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  -19.030000686645508,   11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.515000343322754,     -7.53164529800415,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 34,  100.1500015258789,     23.260000228881836,    -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -12.518750190734863,   -11.630000114440918,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 36,  19.0,                  11.899999618530273,    -1.0,                  2.4964001178741455,    [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.6329113841056824,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  -7.53164529800415,     0.20000000298023224,   1.0])

    DeclActor(27660,   0,       10070,   1200,    27660,   1500,    10070,   0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_5BC",          # 00, 0
        "Function_1_674",          # 01, 1
        "Function_2_69F",          # 02, 2
        "Function_3_6E6",          # 03, 3
        "Function_4_76E",          # 04, 4
        "Function_5_813",          # 05, 5
        "Function_6_882",          # 06, 6
        "Function_7_912",          # 07, 7
        "Function_8_AB3",          # 08, 8
        "Function_9_B50",          # 09, 9
        "Function_10_B9D",         # 0A, 10
        "Function_11_BF6",         # 0B, 11
        "Function_12_C63",         # 0C, 12
        "Function_13_D63",         # 0D, 13
        "Function_14_E0C",         # 0E, 14
        "Function_15_13BA",        # 0F, 15
        "Function_16_1A9E",        # 10, 16
        "Function_17_1AE4",        # 11, 17
        "Function_18_1B2A",        # 12, 18
        "Function_19_1B69",        # 13, 19
        "Function_20_1BD5",        # 14, 20
        "Function_21_1C3A",        # 15, 21
        "Function_22_1CA6",        # 16, 22
        "Function_23_1D12",        # 17, 23
        "Function_24_1DB5",        # 18, 24
        "Function_25_1DE4",        # 19, 25
        "Function_26_1E13",        # 1A, 26
        "Function_27_1E2F",        # 1B, 27
        "Function_28_1E4E",        # 1C, 28
        "Function_29_1E73",        # 1D, 29
        "Function_30_1EA1",        # 1E, 30
        "Function_31_2443",        # 1F, 31
        "Function_32_2495",        # 20, 32
        "Function_33_24E7",        # 21, 33
        "Function_34_2598",        # 22, 34
        "Function_35_2599",        # 23, 35
        "Function_36_268B",        # 24, 36
        "Function_37_26A7",        # 25, 37
        "Function_38_26C1",        # 26, 38
    ))


    def Function_0_5BC(): pass

    label("Function_0_5BC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5FC"),
        (1, "loc_608"),
        (2, "loc_614"),
        (3, "loc_620"),
        (4, "loc_62C"),
        (5, "loc_638"),
        (6, "loc_644"),
        (SWITCH_DEFAULT, "loc_650"),
    )


    label("loc_5FC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_608")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_614")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_620")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_62C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_638")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_644")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_650")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_65C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_673")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_65C")

    label("loc_673")

    Return()

    # Function_0_5BC end

    def Function_1_674(): pass

    label("Function_1_674")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69E")
    OP_94(0xFE, 0x17D0E, 0x3F0C, 0x19154, 0x47A4, 0x3E8)
    Sleep(150)
    Jump("Function_1_674")

    label("loc_69E")

    Return()

    # Function_1_674 end

    def Function_2_69F(): pass

    label("Function_2_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B2")
    Jump("loc_6E5")

    label("loc_6B2")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0xB, 0, 0, 1)

    label("loc_6E5")

    Return()

    # Function_2_69F end

    def Function_3_6E6(): pass

    label("Function_3_6E6")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_END)), "loc_70A")
    Call(0, 13)

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_713")

    label("loc_713")

    ModifyEventFlags(0, 2, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_736")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_736")

    OP_1B(0x5, 0xFF, 0xFFFF)
    OP_1B(0x7, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    ClearMapObjFlags(0x3, 0x10)
    OP_1B(0x5, 0x0, 0x23)
    OP_1B(0x7, 0x0, 0x25)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_76D")

    Return()

    # Function_3_6E6 end

    def Function_4_76E(): pass

    label("Function_4_76E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, is it about time for the tourists\x01",
            "to head on back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... I wonder why all those people\x01",
            "were heading to the residential area.\x01",
            "A party, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_76E end

    def Function_5_813(): pass

    label("Function_5_813")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's almost time to head to the\x01",
            "speaker's mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha... Tonight will be one\x01",
            "to remember.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_813 end

    def Function_6_882(): pass

    label("Function_6_882")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "My man here claims he's going to win\x01",
            "me something beautiful at the auction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And his poor wife doesn't\x01",
            "know a thing...hehehe.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_882 end

    def Function_7_912(): pass

    label("Function_7_912")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A20")

    ChrTalk(
        0xFE,
        "Aaaaah, this day couldn't get better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of all the park's goodness, I even managed\x01",
            "to give Mishy a good kick! That's basically the heart\x01",
            "of the Mishelam Wonderland experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It did nearly get me thrown out of the park, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AAF")

    label("loc_A20")


    ChrTalk(
        0xFE,
        (
            "Kicking Mishy is something only kids\x01",
            "are allowed to do, but I still went for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All in all, this was a good day.\x01",
            "I have no regrets!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAF")

    TalkEnd(0xFE)
    Return()

    # Function_7_912 end

    def Function_8_AB3(): pass

    label("Function_8_AB3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Sure, the theme park was enjoyable...but\x01",
            "I really wanted to go into the jewelry store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Why does that stupid rule\x01",
            "have to be a thing?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_AB3 end

    def Function_9_B50(): pass

    label("Function_9_B50")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Mama... The ship is going to leave\x01",
            "without us if we don't hurry!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_B50 end

    def Function_10_B9D(): pass

    label("Function_10_B9D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Man, today was the best day of my life!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Happy 70th birthday, Crossbell!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_B9D end

    def Function_11_BF6(): pass

    label("Function_11_BF6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Haha, I'm not sure if one day was enough to take\x01",
            "in everything here. I'd like to come back soon.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_BF6 end

    def Function_12_C63(): pass

    label("Function_12_C63")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_D46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D62")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_D62")

    Return()

    # Function_12_C63 end

    def Function_13_D63(): pass

    label("Function_13_D63")

    SetChrChipByIndex(0x13, 0x0)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x40)
    ClearChrFlags(0x13, 0x1)
    SetChrPos(0x13, -170, 0, 10700, 225)
    SetChrChipByIndex(0x14, 0x0)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0x14, 0x1)
    SetChrPos(0x14, 3010, 0, 7590, 270)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x1)
    SetChrPos(0x15, 1980, 0, 4930, 315)
    Return()

    # Function_13_D63 end

    def Function_14_E0C(): pass

    label("Function_14_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3A")
    EventBegin(0x1)
    Call(0, 38)
    Sleep(50)
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)
    Jump("loc_13B9")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1322")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-19000, 1000, 11800, 0)
    SetChrPos(0x101, -19330, 0, 8810, 0)
    SetChrPos(0x102, -17960, 0, 8810, 0)
    SetChrPos(0x103, -20760, 0, 10150, 45)
    SetChrPos(0x104, -16940, 0, 9380, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF")
    SetChrPos(0x151, -18610, 0, 7180, 0)

    label("loc_EBF")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -19000, 0, 12900, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)

    def lambda_EFF():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x2C2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EFF)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    WaitChrThread(0x10, 1)

    ChrTalk(
        0x101,
        "#5005F#3PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PWelcome to Diamante Jewelers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PPardon me, sir. By any chance, do you\x01",
            "have a letter of introduction?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1005")

    ChrTalk(
        0x102,
        (
            "#0105F#6POh, umm... I assume it's necessary\x01",
            "in order to shop here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_1005")


    ChrTalk(
        0x102,
        (
            "#5305F#6POh, umm... I assume it's necessary\x01",
            "in order to shop here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104D")


    ChrTalk(
        0x10,
        "#11PIndeed. Store policy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11PThis store only serves members, so I must insist\x01",
            "that you refrain from trying to enter from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PNow, then, if you would...\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(100)

    def lambda_110C():
        OP_96(0xFE, 0xFFFFB5C8, 0x0, 0x3264, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_110C)
    Sleep(300)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
    WaitChrThread(0x10, 1)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x10, 0x80)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E6")

    ChrTalk(
        0x103,
        "#0203FNo mercy for first-time shoppers, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1219")

    label("loc_11E6")


    ChrTalk(
        0x103,
        "#5403FNo mercy for first-time shoppers, then?\x02",
    )

    CloseMessageWindow()

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1259")

    ChrTalk(
        0x104,
        "#0310F#12PWh-What the hell's up with that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_128A")

    label("loc_1259")


    ChrTalk(
        0x104,
        "#5610F#12PWh-What the hell's up with that?!\x02",
    )

    CloseMessageWindow()

    label("loc_128A")


    ChrTalk(
        0x101,
        (
            "#5003F#3PThat guy doesn't seem to eager for us to\x01",
            "return, so let's ignore this place for now.\x01",
            "Wouldn't want security called on us.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xAE, 1)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Jump("loc_13B9")

    label("loc_1322")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#5000FThe store's employee told us it's limited\x01",
            "to members only. There's no point in\x01",
            "trying to force our way inside, now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -18610, 0, 9950, 180)
    EventEnd(0x4)

    label("loc_13B9")

    Return()

    # Function_14_E0C end

    def Function_15_13BA(): pass

    label("Function_15_13BA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x98, 0xFF, 0xFF)
    AddParty(0x99, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("chr/ch31050.itc", 0x25)
    LoadChrToIndex("chr/ch31051.itc", 0x26)
    LoadChrToIndex("chr/ch31053.itc", 0x27)
    LoadChrToIndex("chr/ch31150.itc", 0x28)
    LoadChrToIndex("chr/ch31151.itc", 0x29)
    LoadChrToIndex("chr/ch31153.itc", 0x2A)
    LoadChrToIndex("chr/ch00000.itc", 0x2B)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x199, 0x80)
    SetChrBattleFlags(0x199, 0x8000)
    SetChrFlags(0x19A, 0x80)
    SetChrBattleFlags(0x19A, 0x8000)
    SetChrPos(0x101, -9430, 0, 7730, 90)
    SetChrPos(0x102, -10930, 0, 7250, 90)
    SetChrPos(0x103, -11440, 0, 9330, 90)
    SetChrPos(0x104, -13560, 0, 9140, 90)
    SetChrPos(0x105, -13830, 0, 7790, 90)
    SetChrPos(0x133, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x13, 30, 0, 27560, 180)
    SetChrPos(0x14, -1600, 0, -5300, 0)
    SetChrPos(0x16, 1200, 0, -5300, 0)
    SetChrPos(0x15, 18000, 0, 7400, 270)
    SetChrPos(0x17, 18000, 0, 9200, 270)
    SetChrPos(0x11, 17000, 0, 7400, 270)
    SetChrPos(0x12, 17000, 0, 8600, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xB, 0, 0, 20560, 180)
    SetChrPos(0xC, 16500, 0, 6300, 270)
    SetChrPos(0xD, 14000, 0, 10400, 270)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    OP_68(-9750, 1600, 8000, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18190, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(17190, 1000)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(9000, 1000, 8000, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24710, 0)
    OP_68(-1000, 1000, 8000, 5000)
    SetCameraDistance(15940, 5000)
    Sound(928, 0, 100, 0)
    Sound(919, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 21)
    BeginChrThread(0x12, 3, 0, 22)
    BeginChrThread(0xB, 3, 0, 23)
    BeginChrThread(0xC, 3, 0, 24)
    BeginChrThread(0xD, 3, 0, 25)
    BeginChrThread(0x13, 3, 0, 16)
    Sleep(1500)
    BeginChrThread(0x14, 3, 0, 17)
    BeginChrThread(0x15, 3, 0, 18)
    BeginChrThread(0x16, 3, 0, 19)
    BeginChrThread(0x17, 3, 0, 20)
    BeginChrThread(0x18, 1, 0, 29)
    Sleep(300)

    def lambda_1844():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1844)

    def lambda_1859():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1859)

    def lambda_186E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_186E)

    def lambda_1883():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1883)

    def lambda_1898():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1898)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    EndChrThread(0x18, 0x1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3501789V#0007F#5PStop! Are you insane...?!\x01",
            "Don't involve bystanders!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#3501790V#6PHah! Who gives a damn?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#3501791V#12PAt this point, I don't care if a few people\x01",
            "get hurt if it means we don't take the heat!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x133, -3840, 0, 8710, 90)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(12940, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_E4", 0x30200011, 0x0, 0x0, 0x16, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    Return()

    # Function_15_13BA end

    def Function_16_1A9E(): pass

    label("Function_16_1A9E")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1AAB():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AAB)

    def lambda_1AC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AC0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_1A9E end

    def Function_17_1AE4(): pass

    label("Function_17_1AE4")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1AF1():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1AF1)

    def lambda_1B06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B06)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_17_1AE4 end

    def Function_18_1B2A(): pass

    label("Function_18_1B2A")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1B37():
        OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B37)

    def lambda_1B4C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B4C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_18_1B2A end

    def Function_19_1B69(): pass

    label("Function_19_1B69")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_1B87():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1B87)

    def lambda_1B9C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B9C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_19_1B69 end

    def Function_20_1BD5(): pass

    label("Function_20_1BD5")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 26)

    def lambda_1BF3():
        OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1BF3)

    def lambda_1C08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C08)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_20_1BD5 end

    def Function_21_1C3A(): pass

    label("Function_21_1C3A")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1C51():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C51)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_1C71():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1C71)
    WaitChrThread(0xFE, 1)

    def lambda_1C8A():
        OP_A6(0xFE, 0x0, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C8A)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_21_1C3A end

    def Function_22_1CA6(): pass

    label("Function_22_1CA6")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1CBD():
        OP_9B(0x0, 0xFE, 0x0, 0x4268, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CBD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_1CDD():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1CDD)
    WaitChrThread(0xFE, 1)

    def lambda_1CF6():
        OP_A6(0xFE, 0x0, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1CF6)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_22_1CA6 end

    def Function_23_1D12(): pass

    label("Function_23_1D12")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1D29():
        OP_95(0xFE, -160, 0, 17680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D29)
    WaitChrThread(0xFE, 1)

    def lambda_1D47():
        OP_95(0xFE, -5000, 0, 14360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D47)
    WaitChrThread(0xFE, 1)

    def lambda_1D65():
        OP_95(0xFE, -7030, 1240, 16610, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D65)
    WaitChrThread(0xFE, 1)

    def lambda_1D83():
        OP_95(0xFE, -7110, 1710, 17620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1D83)

    def lambda_1D9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D9D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_64(0xFE)
    Return()

    # Function_23_1D12 end

    def Function_24_1DB5(): pass

    label("Function_24_1DB5")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1DCC():
        OP_9B(0x0, 0xFE, 0x0, 0x7148, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DCC)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_24_1DB5 end

    def Function_25_1DE4(): pass

    label("Function_25_1DE4")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1DFB():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DFB)
    WaitChrThread(0xFE, 1)
    OP_64(0xFE)
    Return()

    # Function_25_1DE4 end

    def Function_26_1E13(): pass

    label("Function_26_1E13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E2E")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_26_1E13")

    label("loc_1E2E")

    Return()

    # Function_26_1E13 end

    def Function_27_1E2F(): pass

    label("Function_27_1E2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E4D")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_27_1E2F")

    label("loc_1E4D")

    Return()

    # Function_27_1E2F end

    def Function_28_1E4E(): pass

    label("Function_28_1E4E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_28_1E4E end

    def Function_29_1E73(): pass

    label("Function_29_1E73")

    Sleep(1500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Sleep(500)
    Sound(925, 0, 100, 0)
    Return()

    # Function_29_1E73 end

    def Function_30_1EA1(): pass

    label("Function_30_1EA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x98, 0xFF)
    RemoveParty(0x99, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -2410, 0, 7740, 90)
    SetChrPos(0x102, -3820, 0, 9270, 90)
    SetChrPos(0x103, -3820, 0, 7190, 90)
    SetChrPos(0x104, -5680, 0, 9660, 90)
    SetChrPos(0x105, -6650, 0, 8520, 90)
    SetChrPos(0x133, -5070, 0, 6600, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Call(0, 13)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x11, -4750, 0, 12450, 135)
    SetChrPos(0x12, -4019, 0, 13570, 135)
    OP_68(2410, 1600, 7740, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(15510, 0)
    FadeToBright(1000, 0)
    OP_68(-2410, 1600, 7740, 3000)
    OP_6F(0x1)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_2050():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2050)

    def lambda_205D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_205D)
    Sleep(100)

    def lambda_206D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_206D)

    def lambda_207A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_207A)
    Sleep(100)

    def lambda_208A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_208A)

    def lambda_2097():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_2097)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)

    ChrTalk(
        0x101,
        "#3501792V#0001F#6PAre you two all right?\x02",
    )

    CloseMessageWindow()

    def lambda_20EA():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_20EA)

    def lambda_20F7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_20F7)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2124")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214B")

    label("loc_2124")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2141")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214B")

    label("loc_2141")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_214B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2167"),
        (1, "loc_21C9"),
        (2, "loc_2220"),
        (SWITCH_DEFAULT, "loc_2290"),
    )


    label("loc_2167")

    OP_2C(0x47, 0x3)

    ChrTalk(
        0x11,
        "#3501793V#11PY-Yeah...! Never better!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#3501794V#11PWho WERE those people...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2290")

    label("loc_21C9")

    OP_2C(0x47, 0x1)

    ChrTalk(
        0x11,
        "#3501797V#11PWhat a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#3501796V#11PWho were those people...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2290")

    label("loc_2220")


    ChrTalk(
        0x11,
        "#3501795V#11PWhat a mess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3501798V#11POh, what's with those people?!\x01",
            "I demand an explanation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2290")

    label("loc_2290")


    ChrTalk(
        0x102,
        (
            "#3501799V#0101F#6PThere's no time! Please, go take\x01",
            "shelter in the hotel!\x02\x03",
            "#3501800VYou should be safe in there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3501801V#11PO-Okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#3501802V#11PTh-This is the worst day of my life!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3501803V#11PI should have never come to this\x01",
            "horrifying place...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x11, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x12, 3, 0, 32)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    SetChrPos(0x0, -3910, 0, 7710, 90)
    SetScenarioFlags(0xA7, 5)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_30_1EA1 end

    def Function_31_2443(): pass

    label("Function_31_2443")


    def lambda_2448():
        OP_95(0xFE, -6640, 1090, 16630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2448)
    WaitChrThread(0xFE, 1)

    def lambda_2466():
        OP_95(0xFE, -6850, 1750, 17950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2466)

    def lambda_2480():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2480)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_31_2443 end

    def Function_32_2495(): pass

    label("Function_32_2495")


    def lambda_249A():
        OP_95(0xFE, -6640, 1090, 16630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_249A)
    WaitChrThread(0xFE, 1)

    def lambda_24B8():
        OP_95(0xFE, -6850, 1750, 17950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24B8)

    def lambda_24D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24D2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_2495 end

    def Function_33_24E7(): pass

    label("Function_33_24E7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The area past this point is under construction.\x01",
            "Please refrain from trespassing.\x01",
            "      - Mishelam Development Division\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_33_24E7 end

    def Function_34_2598(): pass

    label("Function_34_2598")

    Return()

    # Function_34_2598 end

    def Function_35_2599(): pass

    label("Function_35_2599")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0008F(We don't really have time to waste,\x01",
            "but should we take a quick breather?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2631"),
        (SWITCH_DEFAULT, "loc_2666"),
    )


    label("loc_2631")

    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_2674")

    label("loc_2666")

    FadeToBright(300, 0)
    Jump("loc_2674")

    label("loc_2674")

    Sleep(50)
    SetChrPos(0x0, -5150, 0, 14030, 135)
    EventEnd(0x4)
    Return()

    # Function_35_2599 end

    def Function_36_268B(): pass

    label("Function_36_268B")

    EventBegin(0x1)
    Call(0, 38)
    Sleep(50)
    SetChrPos(0x0, 19600, 0, 9770, 180)
    EventEnd(0x4)
    Return()

    # Function_36_268B end

    def Function_37_26A7(): pass

    label("Function_37_26A7")

    EventBegin(0x1)
    Call(0, 38)
    OP_5A()
    SetChrPos(0x0, 40, 0, 17030, 180)
    EventEnd(0x4)
    Return()

    # Function_37_26A7 end

    def Function_38_26C1(): pass

    label("Function_38_26C1")


    ChrTalk(
        0x101,
        (
            "#0013FThere's no time for detours! We have\x01",
            "to get this girl to the dock, now!\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_38_26C1 end

    SaveToFile()

Try(main)
