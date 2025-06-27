from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0597",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Mafioso",                # 5
        "Garcia",                 # 6
        "Don Marconi",            # 7
        "Regenenkopf",            # 8
        "Mustang",                # 9
        "Mustang",                # 10
        "Randy",                  # 11
        "Elie",                   # 12
        "Tio",                    # 13
        "Detective Dudley",       # 14
        "bc0510",                 # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 13, 180)
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
        "BattleInfo_E4", 0x0012, 34, 6, 180, 0, 0, 0, 0, "bc0510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68200.dat", "ms68300.dat", "ms68300.dat", 0, 0, 0, "ms68300.dat", 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00300.itc",                   # 00
        "chr/ch00100.itc",                   # 01
        "chr/ch00200.itc",                   # 02
        "chr/ch00900.itc",                   # 03
        "chr/ch00000.itc",                   # 04
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
        "monster/ch68250.itc",               # 10
        "monster/ch68251.itc",               # 11
        "monster/ch68350.itc",               # 12
        "monster/ch68350.itc",               # 13
    ))

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
    DeclNpc(-6599,   0,       112099,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       106000,  90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3019,   29,      111360,  90,   389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6699,    0,       101599,  90,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclEvent(0x0000, 0, 13,  0.0,                   48.0,                  -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -16.0,                 0.20000000298023224,   1.0])

    DeclActor(0,       0,       114800,  1200,    0,       1100,    116500,  0x007C, 0,  6,  0x0000)
    DeclActor(7700,    0,       113500,  1200,    7700,    1500,    113500,  0x007C, 0,  17, 0x0000)
    DeclActor(6000,    0,       6000,    1200,    6000,    1500,    6000,    0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  20, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_478",          # 00, 0
        "Function_1_530",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_56B",          # 03, 3
        "Function_4_5BD",          # 04, 4
        "Function_5_656",          # 05, 5
        "Function_6_756",          # 06, 6
        "Function_7_970",          # 07, 7
        "Function_8_B24",          # 08, 8
        "Function_9_D83",          # 09, 9
        "Function_10_101E",        # 0A, 10
        "Function_11_1227",        # 0B, 11
        "Function_12_2240",        # 0C, 12
        "Function_13_2E42",        # 0D, 13
        "Function_14_3ACA",        # 0E, 14
        "Function_15_4005",        # 0F, 15
        "Function_16_4A33",        # 10, 16
        "Function_17_4A88",        # 11, 17
        "Function_18_4AE6",        # 12, 18
        "Function_19_4D4A",        # 13, 19
        "Function_20_744A",        # 14, 20
        "Function_21_77D7",        # 15, 21
    ))


    def Function_0_478(): pass

    label("Function_0_478")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B8"),
        (1, "loc_4C4"),
        (2, "loc_4D0"),
        (3, "loc_4DC"),
        (4, "loc_4E8"),
        (5, "loc_4F4"),
        (6, "loc_500"),
        (SWITCH_DEFAULT, "loc_50C"),
    )


    label("loc_4B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_4C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_4D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_4DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_4E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_4F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_500")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_50C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_518")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_518")

    label("loc_52F")

    Return()

    # Function_0_478 end

    def Function_1_530(): pass

    label("Function_1_530")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_530")

    label("loc_54E")

    Return()

    # Function_1_530 end

    def Function_2_54F(): pass

    label("Function_2_54F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56A")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_54F")

    label("loc_56A")

    Return()

    # Function_2_54F end

    def Function_3_56B(): pass

    label("Function_3_56B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_585")
    Event(0, 15)

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_599")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)
    Jump("loc_5BC")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_5AD")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 12)
    Jump("loc_5BC")

    label("loc_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_5BC")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 14)

    label("loc_5BC")

    Return()

    # Function_3_56B end

    def Function_4_5BD(): pass

    label("Function_4_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_5D2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_5D2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_608")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_615")
    OP_70(0x11, 0xA)

    label("loc_615")

    SetMapObjFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_633")
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x10, 0x10)
    Jump("loc_63D")

    label("loc_633")

    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x10, 0x10)

    label("loc_63D")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    OP_1B(0x2, 0x0, 0x15)

    label("loc_655")

    Return()

    # Function_4_5BD end

    def Function_5_656(): pass

    label("Function_5_656")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_739")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_739")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_755")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_755")

    Return()

    # Function_5_656 end

    def Function_6_756(): pass

    label("Function_6_756")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1000, 116100, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 0, 115100, 0)
    OP_0D()
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The chest is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_851")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use Treasure Chest Key\x01",      # 0
            "Cancel\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_82C"),
        (1, "loc_834"),
        (SWITCH_DEFAULT, "loc_84C"),
    )


    label("loc_82C")

    Call(0, 19)
    Jump("loc_84C")

    label("loc_834")

    SetChrPos(0x0, 0, 0, 114700, 180)
    EventEnd(0x5)
    Jump("loc_84C")

    label("loc_84C")

    Jump("loc_96F")

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8BA")

    ChrTalk(
        0x101,
        (
            "#4300435V#0001F#11P(I'll need a key to open this...\x01",
            "Should I try searching the room?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_956")

    label("loc_8BA")


    ChrTalk(
        0x101,
        (
            "#4300433V#0003F#11P(I don't think I'll be able to unlock this\x01",
            "with a lockpick.)\x02\x03",
            "#4300434V#0000F(So that means...\x01",
            "Should I try searching the room?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_956")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 114700, 180)
    SetScenarioFlags(0xC6, 3)
    EventEnd(0x5)

    label("loc_96F")

    Return()

    # Function_6_756 end

    def Function_7_970(): pass

    label("Function_7_970")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A44")

    ChrTalk(
        0xFE,
        (
            "#4300426V#0306FThese guys look like they've busted their\x01",
            "asses to gather all the latest toys, from\x01",
            "Reinford to Verne...\x02\x03",
            "#4300427V#0301FHell if I know how much mira\x01",
            "all this stuff costs.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    Jump("loc_B20")

    label("loc_A44")


    ChrTalk(
        0xFE,
        (
            "#4300423V#0308FFile here talks about Revache's\x01",
            "arms smuggling routes...\x02\x03",
            "#4300424V#0303FThey even control all the routes\x01",
            "I knew about...\x02\x03",
            "#4300425V#0300FI'd bet they're makin' use of Garcia's\x01",
            "jaeger connections.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B20")

    TalkEnd(0xFE)
    Return()

    # Function_7_970 end

    def Function_8_B24(): pass

    label("Function_8_B24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BFC")

    ChrTalk(
        0x13,
        (
            "#4300421V#0105FThey apparently went through great pains\x01",
            "preparing a catalog for this year's auction.\x02\x03",
            "#4300422V#0106FI admittedly feel a hint of guilt, but I suppose\x01",
            "they reap what they sow.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 1)
    Jump("loc_D7F")

    label("loc_BFC")


    ChrTalk(
        0x13,
        (
            "#4300417V#0108FLooks like they even prepared a catalog of\x01",
            "merchandise for the Schwarze Auction...\x02\x03",
            "#4300418VFrom means of acquisition to contracts,\x01",
            "it's all summarized in detail right here...\x02\x03",
            "#4300419V#0106FTo think that they even acquired a\x01",
            "masterpiece stolen by Phantom Thief B...\x02\x03",
            "#4300420V#0101FIf this info became public, it could possibly\x01",
            "cause an international uproar...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_D7F")

    TalkEnd(0xFE)
    Return()

    # Function_8_B24 end

    def Function_9_D83(): pass

    label("Function_9_D83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(
        0x14,
        (
            "#4300431V#0205FAh, even the names of Republican Faction diet\x01",
            "members and the commissioner of the CPD are\x01",
            "listed here...\x02\x03",
            "#4300432V#0206FThat is an apt explanation for the pressure placed\x01",
            "on the First Division.\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    Jump("loc_101A")

    label("loc_E6E")


    ChrTalk(
        0x14,
        (
            "#4300428V#0208FI found a list of Crossbell's most influential political\x01",
            "and business figures engaged in acts of bribery.\x02\x03",
            "#4300429V#0203FIt includes not only the speaker, but also several\x01",
            "Imperial Faction diet members, the CGF commander,\x01",
            "and other directors of various organizations.\x02\x03",
            "#4300430V#0211FAccording to this, they receive vast sums of mira\x01",
            "from enterprises in return for silencing matters\x01",
            "involving Revache...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_101A")

    TalkEnd(0xFE)
    Return()

    # Function_9_D83 end

    def Function_10_101E(): pass

    label("Function_10_101E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10C1")

    ChrTalk(
        0xFE,
        (
            "#4300415V#0603FWhat we've found constitutes\x01",
            "conclusive evidence of smuggling...\x02\x03",
            "#4300416V#0610FDamn it!\x01",
            "If only we had a search warrant!\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    Jump("loc_1223")

    label("loc_10C1")


    ChrTalk(
        0xFE,
        (
            "#4300412V#0608FSo, we've managed to find files directly\x01",
            "tying Revache to illegal smuggling.\x02\x03",
            "#4300413V#0606FI thought I had an idea of what they\x01",
            "were doing, but to think the scale of\x01",
            "their operation was this massive.\x02\x03",
            "#4300414V#0610FDamn it, if only we had a search warrant...\x01",
            "This is enough evidence to put them\x01",
            "behind bars for a whole century!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1223")

    TalkEnd(0xFE)
    Return()

    # Function_10_101E end

    def Function_11_1227(): pass

    label("Function_11_1227")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    OP_68(150, 930, 108140, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(26500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1800, 30, 106500, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -2700, 30, 108400, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -3000, 20, 107100, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 30, 105400, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -1500, 30, 108200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 900, 30, 108000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Bold Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2100001VYou bastards.\x01",
            "To think you had the nerve to return...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Giant Man in Suit")

    AnonymousTalk(
        0xFF,
        (
            "#2100002VDo you have any idea how much mira\x01",
            "we wasted bailing you out?\x02\x03",
            "#2100003VIt's not exactly a walk in the park\x01",
            "to go and bribe diet members.\x01",
            "You know that, right?\x02",
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
        0xB,
        "#2100004V#6PW-We're sorry, Boss...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2100005V#6PWe weren't expecting the police to\x01",
            "show from outta nowhere.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        (
            "#2100006V#11P#3103FHmph, no matter.\x01",
            "Those guys called themselves the\x01",
            "'Special Support Section'?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        (
            "#2100007V#5P#3100FFabio, Moran.\x02\x03",
            "#2100008VAre those rookies responsible for causing\x01",
            "your dumb-asses to screw up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100009V#6PY-Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100010V#12PUmm... Those brats in the Downtown District\x01",
            "seemed to be cooperating with them.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        (
            "#2100011V#5P#3104FHuh? I heard they were nothing more\x01",
            "than a team of incompetent children.\x02\x03",
            "#2100012V#3100FAnd you all...managed to lose to them?\x01",
            "You're utter failures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100013V#6PN-No!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100014V#12PW-We'll get our revenge on 'em.\x01",
            "We swear it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#2100015V#6PI've heard those damn kids use that run-down\x01",
            "office building over in Central Square as their\x01",
            "headquarters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#2100016V#6PJust say the word, and we'll raze\x01",
            "their building, Boss!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        "#2100017V#11P#3107F#4SYOU DUMBASSES!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#2100018V#6PEek!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        (
            "#2100019V#11P#3107FDoes it look like I give a damn about\x01",
            "some brats from the CPD?\x02\x03",
            "#2100020VThe only ones we need to focus on\x01",
            "crushing are Heiyue...\x02\x03",
            "#2100021VThose damn Eastern Quarter pricks think they\x01",
            "can waltz in here and take what Revache owns!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#2100022V#6PW-Well...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Fat Man",
        (
            "#2100023V#3004F#1PNow, now, Garcia. There's no need\x01",
            "to get so worked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1B6A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B6A)
    WaitChrThread(0xD, 2)

    def lambda_1B7B():
        OP_96(0xFE, 0x12C, 0x1E, 0x1A900, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B7B)
    OP_68(-200, 930, 110500, 2000)
    Sleep(50)

    def lambda_1BA9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1BA9)

    def lambda_1BB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BB6)
    Sleep(50)

    def lambda_1BC6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1BC6)

    def lambda_1BD3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1BD3)
    Sleep(50)

    def lambda_1BE3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1BE3)
    WaitChrThread(0xD, 1)
    OP_6F(0x1)

    ChrTalk(
        0xD,
        "#2100024V#2P#3101FDon...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xE,
        (
            "#2100025VWe may have lost a vital route\x01",
            "to the Republic due to their\x01",
            "interference the other day.\x02\x03",
            "#2100026VWhat Heiyue doesn't know is\x01",
            "that we have connections with\x01",
            "Speaker Hartmann.\x02\x03",
            "#2100027VOur stranglehold on Crossbell\x01",
            "is airtight.\x02",
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
        0xD,
        (
            "#2100028V#2P#3107FListen to me, Don... One of their men could\x01",
            "be a serious threat!\x02\x03",
            "#2100029VWe need to do something about that man\x01",
            "dressed in black!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2100030V#3002F#5PHaha... That little assassin of theirs\x01",
            "that you had some fun with, eh?\x02\x03",
            "#2100031VI imagine he's quite dextrous if he\x01",
            "managed to handle a veteran jaeger.\x02\x03",
            "#2100032VI have no doubt in mind that Cao\x01",
            "spent a fortune hiring him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100033V#2P#3101FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2100034V#3004F#5PNot to worry, Garcia. We've already begun\x01",
            "planning countermeasures to deal with Heiyue.\x02\x03",
            "#2100035VWe've received a rough estimate on the\x01",
            "war hounds. We'll be victorious next time.\x02\x03",
            "#2100036V#3001FWe have more pressing concerns, like\x01",
            "next month's fast-approaching auction.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#2100037V#2P#3103FI understand, Don.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#2100038V#3003F#5PI don't give a damn how much of a nuisance\x01",
            "they are. We absolutely CANNOT let them\x01",
            "interfere with this year's auction!\x02\x03",
            "#2100039V#3001FWe can ignore the police and guild.\x01",
            "Neither of them can touch us, anyway.\x02\x03",
            "#2100040VRevache must organize and plan, so that\x01",
            "we don't get caught off guard yet again by\x01",
            "Heiyue's goddamned assassin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#2100041V#2P#3101FUnderstood!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1227 end

    def Function_12_2240(): pass

    label("Function_12_2240")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis159.itp")
    OP_68(-200, 1530, 110500, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -1500, 20, 108400, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 700, 20, 108400, 0)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -200, 30, 108900, 0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    Sound(818, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        "#3601141V#4SWhat a goddamn disgrace!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-200, 1030, 110500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xE,
        (
            "#3601142V#5P#3007FTo think that we've been forced into striking\x01",
            "a deal with the CPD of all people!\x02\x03",
            "#3601143VDamn it all... This is all because you're\x01",
            "utterly incompetent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3601144V#11P#3103F...I have nothing to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3601145V#6PB-But, didn't you get that doll yourself,\x01",
            "Don?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3601146V#5P#3001FWhat the hell did you just say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3601147V#3103F#11PKeep your mouth shut.\x02\x03",
            "#3601148V#3101FIt doesn't matter. The responsibility lies with us.\x01",
            "It was our duty to not let any intruders in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3601149V#6PY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3601150V#5P#3001FHmph. Whatever.\x02\x03",
            "#3601151V#3003FSpeaker Hartmann has completely cut\x01",
            "contact with us ever since then.\x02\x03",
            "#3601152VNot only that, but goddamn Heiyue\x01",
            "is getting more aggressive!\x02\x03",
            "#3601153VD-Damn it all! At this rate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3601154V#11P#3104FPlease relax, Don.\x02\x03",
            "#3601155V#3100FOur stranglehold on Crossbell\x01",
            "is as firm as ever.\x02\x03",
            "#3601156VIf we can fend off Heiyue's onslaught,\x01",
            "I'm sure even Speaker Hartm--\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        (
            "#3601157V#5P#3007FGarcia! Where the hell is the guarantee\x01",
            "that we can even hold out against them?!\x02\x03",
            "#3601158VYou haven't even managed to take the\x01",
            "head of a single measly assassin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3601159V#11P#3103FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3601160V#5P#3001FDamn it! At this rate, we won't be able to rely\x01",
            "on Hartmann's assistance anymore.\x02\x03",
            "#3601161V#3003FGrr... What should we do?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#3601162V#5P#3004FAnything is fair game at this point...\x02\x03",
            "#3601163V#3002FI've decided. It's time we pull out our trump card.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#3601164V#12POur trump card?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3601165V#6PY-You don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3601166V#11P#3105FAre you sure, Don?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3601167V#5P#3002FHaha... Why so surprised, Garcia?\x02\x03",
            "#3601168VThat sort of insurance was made\x01",
            "for times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3601169V#11P#3107FB-But... It's way too risky!\x02\x03",
            "#3601170VForget the police. This is going to get the\x01",
            "Bracer Guild on our asses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3601171V#5P#3004FThe answer is simple: Crush Heiyue like the\x01",
            "bugs they are before the guild even finds out.\x02\x03",
            "#3601172VThis seems like the perfect time to conduct\x01",
            "a test run of our distribution network.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#3601173V#3002FWe'll never hand over the reins of Crossbell's\x01",
            "underworld to some goddamn outsiders!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x48, 0x4, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x25, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFA")
    OP_29(0x25, 0x4, 0x40)

    label("loc_2CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D18")
    OP_29(0x26, 0x4, 0x40)
    Jump("loc_2D2A")

    label("loc_2D18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2A")
    OP_29(0x26, 0x4, 0x40)

    label("loc_2D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D48")
    OP_29(0x27, 0x4, 0x40)
    Jump("loc_2D5A")

    label("loc_2D48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D5A")
    OP_29(0x27, 0x4, 0x40)

    label("loc_2D5A")

    SubItemNumber(0x358, 1)
    Sleep(1000)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2240 end

    def Function_13_2E42(): pass

    label("Function_13_2E42")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    LoadEffect(0x0, "event\\ev502_00.eff")
    OP_68(0, 1130, 51000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 30, 48000, 0)
    SetChrPos(0x102, -100, 30, 46300, 0)
    SetChrPos(0x104, 900, 30, 45800, 0)
    SetChrPos(0x103, -1200, 30, 46500, 0)
    SetChrPos(0x10A, 1300, 30, 47800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)

    def lambda_2F66():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F66)

    def lambda_2F80():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2F80)
    Sleep(50)

    def lambda_2F9D():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F9D)

    def lambda_2FB7():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FB7)
    Sleep(50)

    def lambda_2FD4():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FD4)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1130, 62000, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#4300360V#0005FYou guys think this is Marconi's office?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300361V#0300FConsiderin' how pointlessly decked out\x01",
            "the place is, I'm gonna go with yeah.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(740, 1130, 51250, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19360, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#4300362V#0603F#11PEnough standing around. Let's go inside.\x02\x03",
            "#4300363V#0601FWe may be able to find clues regarding the\x01",
            "whereabouts of the missing people.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300364V\x07\x05",
            "#40WIntruders detected.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#4300365V\x07\x05",
            "Exiting standby mode.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        "#4300366V#0605F#11PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300367V#12P#0201FEveryone, get back!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 2430, 55000, 0)
    MoveCamera(25, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(14500, 0)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xF, 0x100)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 1000, 55000, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    MoveCamera(45, 21, 0, 3500)
    SetCameraDistance(15500, 3500)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0xF, 0x40, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_33FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_33FA)
    Sound(202, 0, 100, 0)
    WaitChrThread(0xF, 2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_68(0, 1430, 55000, 300)

    def lambda_342E():
        OP_9D(0xFE, 0x0, 0x0, 0xD6D8, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_342E)

    def lambda_344B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_344B)
    Sleep(50)

    def lambda_3468():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3468)
    Sleep(50)

    def lambda_3485():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3485)
    Sleep(50)

    def lambda_34A2():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34A2)
    Sleep(50)

    def lambda_34BF():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34BF)
    WaitChrThread(0xF, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19500, 1500)
    OP_82(0x0, 0x2BC, 0xBB8, 0x5DC)
    Sound(813, 0, 80, 0)
    Sound(944, 0, 100, 0)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    OP_68(0, 1430, 51300, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    CancelBlur(0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4300368V#0011F#12P...?!\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x102,
        "#4300369V#0105F#12PA-A robot?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300370V#0307F#12PThe mother of all machines is\x01",
            "crashin' the party?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 3, 0, 1)
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 70, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300371V\x07\x05",
            "Switching to interception mode...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#4300372V\x07\x05",
            "Five targets identified.\x01",
            "Weapon diagnostics complete.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#4300373V\x07\x05",
            "'Mustang' activated.\x01",
            "Initiating interception...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 2600, 0, 53500, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    BeginChrThread(0x10, 3, 0, 2)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, -2600, 0, 53500, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    BeginChrThread(0x11, 3, 0, 2)
    OP_82(0x96, 0x96, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0x10, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x11, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_3811():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3811)

    def lambda_3822():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3822)
    Sound(202, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)

    ChrTalk(
        0x103,
        "#4300374V#0207F#12P#NRemotely-controlled attack units!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#4300375V#0607F#12PLook alive, everyone!\x02\x03",
            "#4300376VLet's send this hunk of metal back to the\x01",
            "scrapyard where it belongs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300377V#0007F#12PGot it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xF, 0x3)
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x1)
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)

    def lambda_3A33():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3A33)
    WaitChrThread(0xF, 2)
    SetChrFlags(0xF, 0x20)
    Sound(947, 0, 100, 0)
    BlurSwitch(0x15E, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(30, 15, 0, 350)
    SetCameraDistance(14500, 350)

    def lambda_3A81():
        OP_96(0xFE, 0x0, 0x0, 0xB798, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3A81)
    Sleep(50)
    SetChrSubChip(0xF, 0x2)
    Sleep(300)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Call(0, 14)
    Return()

    # Function_13_2E42 end

    def Function_14_3ACA(): pass

    label("Function_14_3ACA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00056.itc", 0x1E)
    LoadChrToIndex("chr/ch00156.itc", 0x1F)
    LoadChrToIndex("chr/ch00256.itc", 0x20)
    LoadChrToIndex("chr/ch00356.itc", 0x21)
    LoadChrToIndex("chr/ch00953.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    OP_68(440, 1130, 51170, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 0, 30, 51000, 0)
    SetChrPos(0x102, -100, 30, 49300, 0)
    SetChrPos(0x104, 900, 30, 48800, 0)
    SetChrPos(0x103, -1200, 30, 49500, 0)
    SetChrPos(0x10A, 1300, 30, 50800, 0)
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
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x3)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_68(440, 1130, 50170, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4300378V#0006F#5P*pant*...*pant*...\x01",
            "That was way harder than any of the\x01",
            "other archaisms we've fought so far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300379V#0306F#11PNo kiddin'... How hasn't Heiyue had\x01",
            "this beast of a machine sicced on\x01",
            "'em yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300380V#6P#0206FI am certain that controlling a machine\x01",
            "of this nature is exceedingly difficult.\x02\x03",
            "#4300381V#0211FThere is a strong possibility it would go\x01",
            "on a rampage without a skilled engineer\x01",
            "handling it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300382V#12P#0106FI'm just glad we didn't have to fight it\x01",
            "in the middle of the city. It would have\x01",
            "been much harder for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300383V#11P#0606FYeah, seriously...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(
        0x10A,
        (
            "#4300384V#11P#0603FOkay...\x01",
            "We've cleared the final obstacle.\x02\x03",
            "#4300385V#0601FLet us examine the room!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F1C():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3F1C)
    Sleep(150)

    def lambda_3F2C():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3F2C)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    ChrTalk(
        0x101,
        "#4300386V#6P#0000FRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_37()
    OP_68(0, 1280, 51000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, 30, 51000, 0)
    SetChrPos(0x1, 0, 30, 51000, 0)
    SetChrPos(0x2, 0, 30, 51000, 0)
    SetChrPos(0x3, 0, 30, 51000, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC6, 1)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_3ACA end

    def Function_15_4005(): pass

    label("Function_15_4005")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 111500, 0)
    MoveCamera(47, 30, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 300, 0, 99000, 0)
    SetChrPos(0x102, -500, 0, 99000, 0)
    SetChrPos(0x104, -500, 0, 99000, 0)
    SetChrPos(0x103, 300, 0, 99000, 0)
    SetChrPos(0x10A, 800, 0, 99000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1100, 104500, 6000)
    MoveCamera(27, 17, 0, 6000)
    SetCameraDistance(19500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_410C():
        OP_96(0xFE, 0x1F4, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_410C)

    def lambda_4126():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4126)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 16)
    Sleep(500)

    def lambda_4143():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4143)

    def lambda_415D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_415D)
    Sleep(500)

    def lambda_4171():
        OP_96(0xFE, 0x1F4, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4171)

    def lambda_418B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_418B)
    Sleep(500)

    def lambda_419F():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_419F)

    def lambda_41B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_41B9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(780, 1000, 102610, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(17950, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_42BF")

    ChrTalk(
        0x102,
        (
            "#4300387V#6P#0101FWow, this office is absolutely stunning...\x02\x03",
            "#4300388V#0103FIt's still not quite at the level of Speaker\x01",
            "Hartmann's home, but regardless...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_441B")

    label("loc_42BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4392")

    ChrTalk(
        0x103,
        (
            "#4300389V#12P#0201FThis is the office of a man who clearly\x01",
            "indulges himself in luxury.\x02\x03",
            "#4300390V#0203FIt still does not reach the same level of absurdity\x01",
            "as Speaker Hartmann's home, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_441B")

    label("loc_4392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_441B")

    ChrTalk(
        0x104,
        (
            "#4300391V#6P#0302FWhew...\x01",
            "One helluva room, ain't it?\x02\x03",
            "#4300392V#0309FMarconi and Hartmann both have\x01",
            "some fancy-ass cribs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441B")


    ChrTalk(
        0x101,
        (
            "#4300393V#11P#0012FYeah, I guess the two of them are pretty similar.\x02\x03",
            "#4300394V#0011FHey!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_44C7():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44C7)

    def lambda_44D4():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_44D4)

    def lambda_44E1():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_44E1)

    def lambda_44EE():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_44EE)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_456E")

    ChrTalk(
        0x102,
        "#4300395V#6P#0108FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300396V#6P#0306FNot your finest moment, Mademois-Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4645")

    label("loc_456E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_45D8")

    ChrTalk(
        0x103,
        "#4300397V#12P#0205FAh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300398V#6P#0306FA stupid move for a smart lady, Tio Tot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4645")

    label("loc_45D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4645")

    ChrTalk(
        0x104,
        "#4300399V#6P#0305FWhoops. My bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300400V#12P#0211FA less than intelligent move, Randy.\x02",
    )

    CloseMessageWindow()

    label("loc_4645")

    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#4300401V#11P#0604FHah.\x01",
            "Why the sudden silence?\x02\x03",
            "#4300402V#0602FI've been well aware of what you two\x01",
            "pulled at the Schwarze Auction.\x02\x03",
            "#4300403VThe First Division has been trying to\x01",
            "put a stop to their illegal activities for\x01",
            "a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300404V#0012F#6PO-Oh, haha...\x02\x03",
            "#4300405V#0003FRegardless, this definitely seems like\x01",
            "it's Marconi's office.\x02\x03",
            "#4300406V#0001FI think we've scoped out Revache's\x01",
            "entire headquarters, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300407V#11P#0608FYeah... Neither the mafia members\x01",
            "nor the missing people are here.\x02\x03",
            "#4300408V#0603FIf there really are any clues lying around,\x01",
            "odds are they're in this office.\x02\x03",
            "#4300409V#0601FTime is precious...\x01",
            "Let's split up and search the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300410V#0013F#6PYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300411V#3P#0103F#6PI'm sure we'll find something\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    RemoveParty(0x9, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_68(0, 1200, 101500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, 0, 0, 101500, 0)
    SetMapFlags(0x2000)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xC6, 2)
    OP_29(0x4C, 0x1, 0x1A)
    OP_1B(0x2, 0x0, 0x15)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_4005 end

    def Function_16_4A33(): pass

    label("Function_16_4A33")


    def lambda_4A38():
        OP_96(0xFE, 0x320, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4A38)

    def lambda_4A52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4A52)
    WaitChrThread(0x10A, 1)

    def lambda_4A67():
        OP_95(0xFE, 2000, 0, 102400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4A67)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    Return()

    # Function_16_4A33 end

    def Function_17_4A88(): pass

    label("Function_17_4A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9E")
    Call(0, 18)
    Jump("loc_4AE5")

    label("loc_4A9E")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The cabinet has a wide selection of vintage alcohol.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_4AE5")

    Return()

    # Function_17_4A88 end

    def Function_18_4AE6(): pass

    label("Function_18_4AE6")

    EventBegin(0x0)
    Fade(1000)
    OP_68(7700, 1200, 113000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6700, 0, 113000, 90)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The cabinet has a wide selection of vintage alcohol.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#4300436V#0005F#6P(Not sure why I was expecting to find anything\x01",
            "other than fancy wine here.)\x02\x03",
            "#4300437V#0000F(Actually... I have an idea.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd lifted each bottle, one by one.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#4300438V#0002F#6P(Bingo!)\x02",
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
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x32F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32F, 1)

    ChrTalk(
        0x101,
        (
            "#4300439V#0004F#6P(I don't think any of his subordinates would\x01",
            "ever dare touch this cabinet.)\x02\x03",
            "#4300440V#0000F(Not a bad hiding place, Marconi.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6700, 0, 113000, 90)
    SetScenarioFlags(0xC6, 4)
    EventEnd(0x5)
    Return()

    # Function_18_4AE6 end

    def Function_19_4D4A(): pass

    label("Function_19_4D4A")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis092.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis093.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    Sound(809, 0, 100, 0)
    Sleep(600)
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#4300441V#0000F#11P(Okay, looks like I managed to open it.)\x02\x03",
            "#4300442V#0008F(These look like files... I should flip\x01",
            "through them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x331, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x332),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x332, 1)

    AnonymousTalk(
        0x101,
        (
            "#4300443V#0005F(There it is!)\x02\x03",
            "#4300444V#0003F(It's as we thought... They're responsible\x01",
            "for distributing the drugs.)\x02\x03",
            "#4300445V(And it looks like that cult is behind\x01",
            "the production of Gnosis.)\x02\x03",
            "#4300446V#0013F(What kind of relationship do they have?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#4300447V#0001F#11P(Hold on, there's something sitting in\x01",
            "the corner of the chest.)\x02\x03",
            "#4300448V(Is this a CPD badge?)\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x333),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x333, 1)

    AnonymousTalk(
        0x101,
        "#4300449V#0005F(...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_C9(0x3, 0x0, 0xFFFDF0A8, 0xFFFDF0A8, 0x0)
    OP_C9(0x3, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(0, 0, -1)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0xBB8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    OP_68(0, 900, 110000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -200, 20, 107400, 0)
    SetChrPos(0x102, -1900, 30, 108500, 0)
    SetChrPos(0x103, -1500, 30, 107700, 0)
    SetChrPos(0x104, 1200, 30, 108100, 330)
    SetChrPos(0x10A, 0, 20, 109200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFrame(0xFF, "sakebin", 0x0, 0x1)
    ClearMapObjFlags(0x13, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7122", 0)
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x10A,
        (
            "#4300450V#0603F#11PEach and every missing person is\x01",
            "written on this list.\x02\x03",
            "#4300451VWe've found our decisive evidence that the\x01",
            "mafia is responsible for spreading the drugs.\x02\x03",
            "#4300452V#0601FWe've also managed to confirm that Gnosis\x01",
            "was concocted by that terrible cult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300453V#12P#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300454V#12P#0106FHow was the mafia able to get their\x01",
            "hands on something like this?\x02\x03",
            "#4300455V#0108FAccording to the shipment inventory,\x01",
            "it looks like somebody's been supplying\x01",
            "it to them.\x02\x03",
            "#4300456V#0101FDoes Marconi really have this strong\x01",
            "a tie to the cult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300457V#12P#0003FIs there any other way to look at it?\x02\x03",
            "#4300458V#0001FAccording to the documents, his contact was\x01",
            "an acquaintance he made a few years back.\x02\x03",
            "#4300459VHe prescribed the drugs to some war hounds\x01",
            "and even provided a surefire method of\x01",
            "easily manipulating them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300460V#0306FDamn, man. It takes jaegers a long-ass\x01",
            "time to train those canines.\x02\x03",
            "#4300461V#0301FHow many of them they had in their\x01",
            "arsenal never did sit well with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300462V#0603F#11PDoes that mean a member of the cult\x01",
            "has been in cahoots with them?\x02\x03",
            "#4300463V#0608FBut, who could it be?\x02\x03",
            "#4300464VWe can deduce that it's someone living\x01",
            "in Crossbell, judging by how frequently\x01",
            "they're in contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300465V#12P#0003FI don't know the answer.\x02\x03",
            "#4300466V#0013FWhat I do know is, regarding the location of\x01",
            "the missing people and the reason behind\x01",
            "the sudden disappearance of the entire mafia...\x02\x03",
            "#4300467VMy intuition tells me that this mystery\x01",
            "contact is the man behind the curtain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300468V#12P#0206FI agree with Lloyd.\x02\x03",
            "#4300469V#0208FThose blue pills are likely an enhanced version\x01",
            "of the original Gnosis from six years ago.\x02\x03",
            "#4300470V#0201FThat monster managed to perfect the formula\x01",
            "and is now supplying the mafia with it...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A43():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A43)
    WaitChrThread(0x103, 2)
    Sleep(300)

    def lambda_5A63():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A63)
    Sleep(50)

    def lambda_5A73():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A73)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x102,
        "#4300471V#5P#0101FTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300472V#0004F#11PIt's all right, Tio... We're with you.\x02\x03",
            "#4300473V#0000FNever again... We'll never let them\x01",
            "touch you again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#4300541V#6P#0202FLloyd...\x02",
    )

    CloseMessageWindow()

    def lambda_5B53():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5B53)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#4300475V#0304FWhoever this guy is, he seems like\x01",
            "a real piece of shit. I'm gonna enjoy\x01",
            "kickin' his slimy ass.\x02\x03",
            "#4300476V#0301FThe real problem is, how are we going\x01",
            "to lure him outta his hiding place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300477V#5P#0108FRight... We're lacking in numbers.\x02\x03",
            "#4300478VWe already have to deal with the vanished\x01",
            "mafia, the search for the missing persons,\x01",
            "and the bomb threat at the airport, too...\x02\x03",
            "#4300479V#0106FIf the higher-ups weren't putting so much\x01",
            "pressure on the force, we could do\x01",
            "something about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300480V#0606F#11PDamn it... To think that the commissioner was\x01",
            "completely won over by petty bribery.\x02\x03",
            "#4300481VIf it weren't for that, we'd be able to mobilize\x01",
            "the entire CPD and work on countermeasures.\x02\x03",
            "#4300482V#0610FHas he no shame?! He's a blight on the name\x01",
            "of the CPD!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E8F():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E8F)
    Sleep(50)

    def lambda_5E9F():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5E9F)
    Sleep(50)

    def lambda_5EAF():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5EAF)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    ChrTalk(
        0x101,
        "#4300483V#12P#0005FHey, Dudley...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4300484V#12P#0003FI have a suggestion.\x02\x03",
            "#4300485V#0001FWhy don't we request the help of the bracers?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    MoveCamera(43, 21, 0, 1200)
    OP_68(250, 900, 108770, 1200)

    def lambda_5FF8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5FF8)
    Sleep(100)

    def lambda_6008():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6008)
    Sleep(50)

    def lambda_6018():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6018)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#4300486V#5P#0100FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300487V#11P#0302FGood thinkin', pal! They'd be a colossal help\x01",
            "right about now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300488V#0607F#5PTh-Think before you speak, Bannings!\x02\x03",
            "#4300489VThe widespread corruption within\x01",
            "the CPD would be exposed to the\x01",
            "guild if we did that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300490V#12P#0006FCorruption is corruption, no matter its origin...\x01",
            "It's a price the whole force will have to pay.\x02\x03",
            "#4300491VAll of us will have to bear the responsibility\x01",
            "of sweeping it under the rug.\x02\x03",
            "#4300492V#0013FIsn't it best to embrace the embarrassment and\x01",
            "accept consequences, in order to move forward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300493V#0610F#5PTch...\x02",
    )

    CloseMessageWindow()

    def lambda_629E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_629E)
    Sleep(50)

    def lambda_62AE():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_62AE)
    Sleep(50)

    def lambda_62BE():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62BE)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4300494V#6P#0211FWe cannot be sure what will happen to the\x01",
            "missing people if we continue to waste time,\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300495V#12P#0300FNot only that, but we still don't have a\x01",
            "damn clue what the mafia's main\x01",
            "objective is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300496V#6P#0101FThis isn't an appropriate time to persist\x01",
            "in holding on to your pride, Dudley.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x10A,
        "#4300497V#0603F#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10A)
    Sleep(100)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    ChrTalk(
        0x10A,
        (
            "#4300498V#0604F#5PHmph. So these are the kinds of people\x01",
            "Sergei has gathered for himself.\x02\x03",
            "#4300499V#0600FVery well. I understand. I'll leave you all\x01",
            "in charge of contacting the guild.\x02\x03",
            "#4300500VI'll go and secure the First Division's help\x01",
            "behind the top brass' back.\x02\x03",
            "#4300501V#0603FI may even be able to enlist help from the\x01",
            "Second Division, depending on the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300502V#12P#0002FDudley...\x02\x03",
            "#4300503V#0004FThank you.\x01",
            "I appreciate you giving us a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300504V#0602F#5PHmph. Don't misunderstand me.\x02\x03",
            "#4300505VIt just so happens that we have no other\x01",
            "choice in these circumstances.\x02\x03",
            "#4300506V#0603FMore importantly... Bannings.\x02\x03",
            "#4300507V#0601FAre you fine holding on to that badge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300508V#12P#0008FOh...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x102,
        "#4300509V#0108FIt's a damaged CPD badge...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#4300510V#0301FYou sure that's your brother's old badge?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#4300511V#0006FYeah, I'm almost positive it is.\x02\x03",
            "#4300512V#0000FTio, do you remember seeing this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#4300513V#0204FYes...\x02\x03",
            "#4300514VI imagine it was damaged during\x01",
            "one of the raids on the cult lodges...\x02\x03",
            "#4300515V#0202FHe told me it was his 'badge of honor.'\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x10A,
        (
            "#4300516V#0606FI see...\x02\x03",
            "#4300517V#0608FNo wonder he didn't bother to exchange it for\x01",
            "a new one, despite my constant pestering.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#4300518V#12P#0000FDudley, you...and my brother worked together, right?\x02\x03",
            "#4300519VSince my brother transferred to the First Division\x01",
            "and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300520V#0603F#5PYeah, I suppose...\x02\x03",
            "#4300521V#0601FTo be frank, he wasn't the type of man to\x01",
            "mesh well with the First Division.\x02\x03",
            "#4300522VOverbearing and reckless, always acting\x01",
            "independently... He stood out like a sore thumb.\x02\x03",
            "#4300523VHe hardly cooperated with anyone, especially me.\x01",
            "We were constantly at odds during every case.\x02\x03",
            "#4300524V#0604FHowever, everyone in the First Division\x01",
            "acknowledged him for the detective he was.\x02\x03",
            "#4300525VMyself included, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300526V#12P#0005FDudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300527V#0606F#5PWhen he was killed in the line of duty, it\x01",
            "hit all of us in the First Division much harder\x01",
            "than we ever could have imagined.\x02\x03",
            "#4300528VAlthough we never really saw eye-to-eye with\x01",
            "Guy...perhaps, somewhere inside us, we all\x01",
            "envied that eternal enthusiasm he carried...\x02\x03",
            "#4300529V#0608FWe all desperately searched for the culprit,\x01",
            "but in the end, we were at a loss...\x02\x03",
            "#4300530V#0603FMy apologies, Bannings. I didn't intend to\x01",
            "drag up painful memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300531V#12P#0011FD-Don't worry about it. It's okay.\x02\x03",
            "#4300532V#0006FMy brother definitely had a problem of running\x01",
            "off to investigate cases on his own...\x02\x03",
            "#4300533V#0002FHonestly, just hearing about your reaction\x01",
            "to Guy's death is more than enough for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300534V#0602F#5PI see...\x02\x03",
            "#4300535V#0603FHowever, here we are on the verge of\x01",
            "a breakthrough. We finally have a lead\x01",
            "on who the culprit is.\x02\x03",
            "#4300536VThat being said, this is something the\x01",
            "First Division suspected from the start.\x02\x03",
            "#4300537V#0601FYou might be able to settle your\x01",
            "brother's old score for--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300538V#12P#0004FNo. I'll worry about my brother later...\x02\x03",
            "#4300539V#0008FWe've got a mountain of pressing issues\x01",
            "to handle right in front of us already.\x02\x03",
            "#4300540V#0000FI'll worry about Guy once we've solved these.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7127():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7127)
    Sleep(50)

    def lambda_7137():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7137)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x103,
        "#4300474V#6P#0202FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300542V#6P#0104FYou really ought to take it down a notch, Lloyd.\x01",
            "You can get too serious at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300543V#11P#0309FLloyd will be Lloyd.\x01",
            "You just gotta love the guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300544V#0604F#5PVery well, Bannings.\x02\x03",
            "#4300545V#0602FLet us both set out to do what we must.\x02\x03",
            "#4300546VWe can't have that annoyingly optimistic\x01",
            "man outdo us from beyond the grave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300547V#12P#0000FRight!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis161.itp")
    OP_29(0x4C, 0x4, 0x10)
    SubItemNumber(0x32F, 1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x28, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x9)
    RemoveParty(0x9, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    ReplaceBGM("ed7000", "ed7000")
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t3010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4D4A end

    def Function_20_744A(): pass

    label("Function_20_744A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -1400, 30, 60500, 0)
    SetChrPos(0x104, -1400, 30, 59400, 0)
    SetChrPos(0x103, -100, 30, 59400, 0)
    SetChrPos(0x10A, 1000, 30, 61000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0003F(We've finally made it to the don's office.)\x02\x03",
            "#0008F(We'll be going beyond the point of no return\x01",
            "in multiple ways if we enter this room.)\x02\x03",
            "#0013F(What should we do?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Upon entering, you may no longer freely\x01",
            "explore outside of Crossbell City.\x02\x03",
            "Remaining quests labeled with a short\x01",
            "term will expire. Proceed with caution.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Unlock door and go inside.]\x01",      # 0
            "[Leave for now.]\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76B3"),
        (1, "loc_7781"),
        (SWITCH_DEFAULT, "loc_77D4"),
    )


    label("loc_76B3")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    FadeToDark(1000, 0, -1)

    def lambda_76D7():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76D7)
    Sleep(100)

    def lambda_76F4():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_76F4)
    Sleep(100)

    def lambda_7711():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7711)
    Sleep(100)

    def lambda_772E():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_772E)
    Sleep(100)

    def lambda_774B():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_774B)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_65(0x3, 0x1)
    Call(0, 15)
    Jump("loc_77D4")

    label("loc_7781")

    SetChrPos(0x0, 0, 30, 61800, 180)
    SetChrPos(0x1, 0, 30, 61800, 180)
    SetChrPos(0x2, 0, 30, 61800, 180)
    SetChrPos(0x3, 0, 30, 61800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_77D4")

    label("loc_77D4")

    EventEnd(0x5)
    Return()

    # Function_20_744A end

    def Function_21_77D7(): pass

    label("Function_21_77D7")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0013FThis is no time to be leaving...\x01",
            "I have to keep searching this room!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 100500, 0)
    EventEnd(0x4)
    Return()

    # Function_21_77D7 end

    SaveToFile()

Try(main)
