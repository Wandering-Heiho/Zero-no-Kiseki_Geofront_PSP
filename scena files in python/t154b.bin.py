from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t154b.bin",                # FileName
        "t154b",                    # MapName
        "t154b",                    # Location
        0x0051,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 81, 0, 2, 0, 3],
    )

    BuildStringList((
        "t154b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Medical Intern Gwen",    # 5
        "Nurse Lan",              # 6
        "Inpatient",              # 7
        "Inpatient",              # 8
        "Inpatient",              # 9
        "Nurse Ada",              # 10
        "Doctor Belldine",        # 11
        "Inpatient",              # 12
        "Inpatient",              # 13
        "Inpatient",              # 14
        "bt154b",                 # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_B4", 11, 1, 0)
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

    # event battle count: 2

    BattleInfo(
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch29500.itc",                   # 02
        "chr/ch29700.itc",                   # 03
        "chr/ch29800.itc",                   # 04
        "chr/ch29300.itc",                   # 05
        "apl/ch50133.itc",                   # 06
        "apl/ch50137.itc",                   # 07
        "apl/ch50141.itc",                   # 08
        "apl/ch50135.itc",                   # 09
        "apl/ch50139.itc",                   # 0A
        "apl/ch50143.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-1000,   0,       55279,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4309,   0,       55029,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4000,   699,     57029,   270,  341,  0x0, 0,   6,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4949,    699,     57029,   270,  341,  0x0, 0,   7,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4949,    699,     52029,   270,  341,  0x0, 0,   8,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4940,    0,       -54380,  0,    261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4269,    0,       -53810,  0,    261,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4150,   699,     -52060,  270,  341,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-4150,   699,     -56970,  270,  341,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(4849,    699,     -52060,  270,  341,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)

    DeclEvent(0x0000, 0, 18,  26.5,                  -11.0,                 -1.0,                  110.25,                [0.1428571492433548,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.7857143878936768,   3.6666667461395264,    0.20000000298023224,   1.0])

    DeclActor(29820,   0,       -12440,  1200,    29820,   1500,    -12440,  0x007C, 0,  21, 0x0000)

    ScpFunction((
        "Function_0_404",          # 00, 0
        "Function_1_4BC",          # 01, 1
        "Function_2_4E7",          # 02, 2
        "Function_3_53D",          # 03, 3
        "Function_4_5DA",          # 04, 4
        "Function_5_60B",          # 05, 5
        "Function_6_6BD",          # 06, 6
        "Function_7_811",          # 07, 7
        "Function_8_939",          # 08, 8
        "Function_9_AAA",          # 09, 9
        "Function_10_C07",         # 0A, 10
        "Function_11_D0E",         # 0B, 11
        "Function_12_E77",         # 0C, 12
        "Function_13_FC1",         # 0D, 13
        "Function_14_1148",        # 0E, 14
        "Function_15_1304",        # 0F, 15
        "Function_16_1637",        # 10, 16
        "Function_17_16B2",        # 11, 17
        "Function_18_1DDF",        # 12, 18
        "Function_19_20B7",        # 13, 19
        "Function_20_2132",        # 14, 20
        "Function_21_28B3",        # 15, 21
    ))


    def Function_0_404(): pass

    label("Function_0_404")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_444"),
        (1, "loc_450"),
        (2, "loc_45C"),
        (3, "loc_468"),
        (4, "loc_474"),
        (5, "loc_480"),
        (6, "loc_48C"),
        (SWITCH_DEFAULT, "loc_498"),
    )


    label("loc_444")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_450")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_45C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_468")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_474")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_480")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_498")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4A4")

    label("loc_4BB")

    Return()

    # Function_0_404 end

    def Function_1_4BC(): pass

    label("Function_1_4BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E6")
    OP_94(0xFE, 0xFFFFFAF6, 0xCFEE, 0x4D8, 0xD99E, 0x3E8)
    Sleep(400)
    Jump("Function_1_4BC")

    label("loc_4E6")

    Return()

    # Function_1_4BC end

    def Function_2_4E7(): pass

    label("Function_2_4E7")

    BeginChrThread(0xC, 0, 0, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50C")
    Event(0, 20)
    Jump("loc_53C")

    label("loc_50C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B")
    Event(0, 17)
    Jump("loc_53C")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53C")
    Event(0, 15)

    label("loc_53C")

    Return()

    # Function_2_4E7 end

    def Function_3_53D(): pass

    label("Function_3_53D")

    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED06", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    Call(0, 16)

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB")
    Call(0, 19)

    label("loc_5BB")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D3")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_3_53D end

    def Function_4_5DA(): pass

    label("Function_4_5DA")

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

    # Function_4_5DA end

    def Function_5_60B(): pass

    label("Function_5_60B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We will stay here and comfort the patients.\x01",
            "It would be terrible if their conditions\x01",
            "worsened because of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Lloyd, everyone. Please save the others!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_60B end

    def Function_6_6BD(): pass

    label("Function_6_6BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")

    ChrTalk(
        0xFE,
        (
            "O-Okay, I need to pull myself together. In\x01",
            "situations like this, you need resolve more\x01",
            "than medical skills!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just have to perk up and give the\x01",
            "patients a hopeful smile!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80D")

    label("loc_786")


    ChrTalk(
        0xFE,
        "Calm down... Just calm down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Argh! This is impossible! The more\x01",
            "I try to calm down, the more I freak\x01",
            "out about everything!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    TalkEnd(0xFE)
    Return()

    # Function_6_6BD end

    def Function_7_811(): pass

    label("Function_7_811")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A5")
    Jump("loc_8EF")

    label("loc_8A5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8C5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EF")

    label("loc_8C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EF")

    label("loc_8E5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "It's past my bedtime...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_811 end

    def Function_8_939(): pass

    label("Function_8_939")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CD")
    Jump("loc_A17")

    label("loc_9CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A17")

    label("loc_9ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A17")

    label("loc_A0D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A17")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Was that really gunfire going off earlier...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Th-That's preposterous. I must have misheard.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_939 end

    def Function_9_AAA(): pass

    label("Function_9_AAA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B3E")
    Jump("loc_B88")

    label("loc_B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_B5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_B7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Wh-What's with all this noise?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This can't be normal! It just can't be!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_AAA end

    def Function_10_C07(): pass

    label("Function_10_C07")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We're so lucky Doctor Belldine is here with us.\x01",
            "I doubt the nurses and I would have been\x01",
            "able to calm down the patients ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be honest, I'd like to check how things\x01",
            "are in the other rooms, but...I'd only end\x01",
            "up getting hurt, wouldn't I?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_C07 end

    def Function_11_D0E(): pass

    label("Function_11_D0E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDA")

    ChrTalk(
        0xFE,
        (
            "Until this starts to turn around, I plan to give\x01",
            "the patients my undivided attention. Hopefully\x01",
            "I can be a bright spot in this dim situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't do anything crazy, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E73")

    label("loc_DDA")

    TurnDirection(0xFE, 0x15, 0)

    ChrTalk(
        0xFE,
        (
            "Come, now, take deeeeep breaths. If you\x01",
            "move too much, the stitches will come loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you stay still, you'll be perfectly fine, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_E73")

    TalkEnd(0xFE)
    Return()

    # Function_11_D0E end

    def Function_12_E77(): pass

    label("Function_12_E77")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F0B")
    Jump("loc_F55")

    label("loc_F0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F2B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F55")

    label("loc_F2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F55")

    label("loc_F4B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F55")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Oh, dear... Sonny, is the hospital\x01",
            "going to be all right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_E77 end

    def Function_13_FC1(): pass

    label("Function_13_FC1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1055")
    Jump("loc_109F")

    label("loc_1055")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1075")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_109F")

    label("loc_1075")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1095")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_109F")

    label("loc_1095")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_109F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Thank the Goddess this didn't happen\x01",
            "while my mother-in-law was visiting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is the situation really that intense?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_FC1 end

    def Function_14_1148(): pass

    label("Function_14_1148")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11DC")
    Jump("loc_1226")

    label("loc_11DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11FC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1226")

    label("loc_11FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_121C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1226")

    label("loc_121C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1226")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "H-Hey! Wait a second! I'm still\x01",
            "recuperating, so walking isn't\x01",
            "exactly the easiest thing for me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Owww... Wh-What do I do? There's\x01",
            "no way I could run away like this!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_1148 end

    def Function_15_1304(): pass

    label("Function_15_1304")

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
    OP_68(3750, 1000, 2800, 0)
    MoveCamera(35, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2800, 0, 3450, 90)
    SetChrPos(0x102, 2800, 0, 2150, 90)
    SetChrPos(0x103, 1500, 0, 3450, 90)
    SetChrPos(0x104, 1500, 0, 2150, 90)
    SetChrPos(0x106, 200, 0, 2800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 9600, 0, 3440, 270)
    SetChrPos(0x9, 9450, 0, 1840, 270)
    FadeToBright(1000, 0)
    OP_68(4750, 1000, 2800, 1000)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5100540V#0201F#1PThat was quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100541V#0307F#5PLet's show 'em what we're made of!\x02",
    )

    CloseMessageWindow()
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
    OP_68(4250, 1000, 2800, 850)
    SetCameraDistance(17500, 850)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1587():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1587)

    def lambda_159C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_159C)
    Sleep(350)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(400)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 16)
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
    SetChrPos(0x0, 4000, 0, 3000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE1, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_1304 end

    def Function_16_1637(): pass

    label("Function_16_1637")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x1)
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
    SetChrPos(0x8, 6570, 0, 1270, 90)
    SetChrPos(0x9, 5480, 0, 3900, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_16_1637 end

    def Function_17_16B2(): pass

    label("Function_17_16B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-100, 1000, 54020, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -600, 0, 49400, 0)
    SetChrPos(0x102, 600, 0, 49400, 0)
    SetChrPos(0x103, -600, 0, 48100, 0)
    SetChrPos(0x104, 600, 0, 48100, 0)
    SetChrPos(0x106, 0, 0, 46800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, -2500, 0, 55150, 180)
    SetChrPos(0xC, -2500, 0, 53950, 0)
    FadeToBright(1000, 0)
    OP_68(-870, 1000, 54870, 3000)

    def lambda_17C9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17C9)
    Sleep(50)

    def lambda_17E1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17E1)
    Sleep(50)

    def lambda_17F9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17F9)
    Sleep(50)

    def lambda_1811():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1811)
    Sleep(50)

    def lambda_1829():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1829)
    Sleep(200)

    def lambda_1841():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1841)
    Sleep(50)

    def lambda_1855():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1855)
    Sleep(500)

    def lambda_1869():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1869)
    Sleep(50)

    def lambda_187D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_187D)
    Sleep(500)

    def lambda_1891():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1891)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_18AA():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18AA)

    def lambda_18B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18B7)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_18CC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18CC)

    def lambda_18D9():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18D9)
    WaitChrThread(0x106, 1)

    def lambda_18EA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_18EA)
    OP_4B(0xD, 0xFF)
    EndChrThread(0xC, 0xFF)
    SetChrSubChip(0xC, 0x0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1939():
        OP_93(0xFE, 0x5A, 0x258)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1939)
    Sleep(50)

    def lambda_1949():
        OP_93(0xFE, 0x5A, 0x258)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1949)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xC,
        "#5100542V#6PWait, I recognize you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100543V#6PRandy and...Cecile's little brother?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100544V#0302F#11PLan! Good to see you're safe and\x01",
            "sound, girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100545V#0000F#11PGood to see you, Lan. Are all the patients\x01",
            "here present and accounted for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100546V#6PWell, all of the ones assigned to this\x01",
            "room are, but as for the rest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5100547V#6PHey! Are the mafia still prowling the halls?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100548V#0206F#11PThey still occupy the premises, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100549V#0103F#11PWe're trying to locate St. Ursula staff and\x01",
            "patients, currently. Of course, we've been\x01",
            "suppressing mafiosos we run across.\x02\x03",
            "#5100550V#0101FI'm sorry, but it's still extremely dangerous\x01",
            "out there. Please continue to hide here for\x01",
            "the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5100551V#6PF-Fine, if we have to.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D27")

    ChrTalk(
        0xD,
        (
            "#5100552V#6PAda, Philia, and Cecile should still be\x01",
            "somewhere in the hospital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100553V#6PPlease find them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100554V#0013F#11PJust leave it to us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D79")

    label("loc_1D27")


    ChrTalk(
        0xD,
        "#5100555V#6PBe careful out there, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100556V#0000F#11PWill do!\x02",
    )

    CloseMessageWindow()

    label("loc_1D79")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 10, 0, 50670, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xD, -4310, 0, 55030, 0)
    SetChrPos(0xC, -1000, 0, 55280, 180)
    OP_4C(0xD, 0xFF)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xE2, 0)
    OP_29(0x4D, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_16B2 end

    def Function_18_1DDF(): pass

    label("Function_18_1DDF")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
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
    OP_68(26750, 1200, -11250, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 27250, 0, -11320, 180)
    SetChrPos(0x102, 26090, 0, -11300, 180)
    SetChrPos(0x103, 27290, 0, -9930, 180)
    SetChrPos(0x104, 26110, 0, -9930, 180)
    SetChrPos(0x106, 26710, 0, -8580, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xA, 26550, 0, -17660, 0)
    SetChrPos(0xB, 27830, 0, -18140, 0)
    FadeToBright(1000, 0)
    OP_68(26750, 1200, -13750, 1500)
    Sleep(1300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
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
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)

    def lambda_1FE8():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1FE8)

    def lambda_1FFD():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1FFD)
    OP_68(26750, 1200, -12500, 800)
    SetCameraDistance(18000, 800)
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    Call(0, 19)
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
    SetChrPos(0x0, 26650, 0, -14270, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE2, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_1DDF end

    def Function_19_20B7(): pass

    label("Function_19_20B7")

    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xA, 26350, 0, -17110, 0)
    SetChrPos(0xB, 27830, 0, -18140, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_19_20B7 end

    def Function_20_2132(): pass

    label("Function_20_2132")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1710, 1100, -53910, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -550, 0, -49650, 180)
    SetChrPos(0x102, 550, 0, -49650, 180)
    SetChrPos(0x103, -550, 0, -48450, 180)
    SetChrPos(0x104, 550, 0, -48450, 180)
    SetChrPos(0x106, 0, 0, -47250, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -2700, 0, -53930, 180)
    SetChrPos(0x12, -2700, 0, -55100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x3)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(-890, 1100, -55040, 3000)

    def lambda_229D():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_229D)
    Sleep(50)

    def lambda_22B5():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22B5)
    Sleep(50)

    def lambda_22CD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22CD)
    Sleep(50)

    def lambda_22E5():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22E5)
    Sleep(50)

    def lambda_22FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_22FD)
    Sleep(200)

    def lambda_2315():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2315)

    def lambda_2326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2326)
    Sleep(100)

    def lambda_233A():

        label("loc_233A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_233A")

    QueueWorkItem2(0x11, 1, lambda_233A)

    def lambda_234C():

        label("loc_234C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_234C")

    QueueWorkItem2(0x12, 1, lambda_234C)
    Sleep(400)

    def lambda_2361():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2361)

    def lambda_2372():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2372)
    Sleep(500)

    def lambda_2386():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2386)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_239F():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_239F)

    def lambda_23AC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23AC)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_23C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23C1)

    def lambda_23CE():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23CE)
    WaitChrThread(0x106, 1)

    def lambda_23DF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_23DF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    Sound(107, 0, 100, 0)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)

    ChrTalk(
        0x12,
        "#5100557V#6PThe Special Support Section...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5100558V#6PLloyd? Randy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100559V#0002F#11PAda! I'm glad you're safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100560V#0304F#11PGot some patients with ya, too, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5100561V#6PIf you're here, does that mean those\x01",
            "mafia goons have cleared out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100562V#0003F#11PNo, not yet.\x02\x03",
            "#5100563V#0001FRight now, we're just making sure\x01",
            "everyone's all right, restraining the\x01",
            "mafia as we see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5100564V#6PIf that's the case, you'd rather us\x01",
            "stay put, right? I assume it would\x01",
            "be too dangerous to move now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100565V#0202F#11PThat would be for the best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100566V#0100F#11PPlease, stay here for a little longer.\x01",
            "At least until we've found everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5100567V#6PVery well. And thanks, everyone.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D9")

    ChrTalk(
        0x11,
        (
            "#5100568V#6PI think there's one other patient left\x01",
            "in one of the rooms on the third floor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5100569V#6PCecile and Philia should be with him.\x01",
            "Please, keep them safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282F")

    label("loc_27D9")


    ChrTalk(
        0x11,
        (
            "#5100570V#6PThere's no need to worry about us.\x01",
            "We'll be as cautious as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_282F")


    ChrTalk(
        0x101,
        "#5100571V#0000F#11PThanks!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 0, 0, -54000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x11, 4940, 0, -54380, 0)
    SetChrPos(0x12, 4270, 0, -53810, 0)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0xE2, 2)
    OP_29(0x4D, 0x1, 0x9)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_2132 end

    def Function_21_28B3(): pass

    label("Function_21_28B3")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Orbal power is offline.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_28B3 end

    SaveToFile()

Try(main)
