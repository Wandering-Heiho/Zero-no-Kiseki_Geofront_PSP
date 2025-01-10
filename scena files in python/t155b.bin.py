from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t155b.bin",                # FileName
        "t155b",                    # MapName
        "t155b",                    # Location
        0x0052,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 82, 0, 1, 0, 2],
    )

    BuildStringList((
        "t155b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Nurse Philia",           # 3
        "Medical Intern Lytton",  # 4
        "Janitor Dyson",          # 5
        "Representative Gable",   # 6
        "Representative Gable",   # 7
        "Cecile",                 # 8
        "Michael",                # 9
        "Doctor Lago",            # 10
        "Doctor Gailey",          # 11
        "Chief Ursuline",         # 12
        "bt154b",                 # 13
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 8, 14, 180)
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

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31103.dat", "ms31003.dat", "ms31003.dat", "ms67101.dat", 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
        "apl/ch50363.itc",                   # 01
        "chr/ch29900.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "apl/ch50153.itc",                   # 04
        "chr/ch33602.itc",                   # 05
        "chr/ch05300.itc",                   # 06
        "apl/ch50144.itc",                   # 07
        "chr/ch29202.itc",                   # 08
        "chr/ch32702.itc",                   # 09
        "chr/ch32900.itc",                   # 0A
        "chr/ch33600.itc",                   # 0B
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-55169,  0,       -50069,  0,    261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-55930,  0,       -49529,  0,    261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-55549,  379,     -47700,  90,   342,  0x0, 1,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(54200,   -300,    -2799,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-54500,  250,     -52330,  270,  468,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(6519,    0,       -48889,  0,    389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6150,    400,     -47400,  0,    468,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-102150, 250,     -4730,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-102150, 250,     -7550,   0,    469,  0x0, 0,   9,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-100489, 0,       -6130,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)

    DeclEvent(0x0000, 0, 15,  -1.5,                  9.0,                   -1.0,                  110.25,                [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.5,                   -1.2857143878936768,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  -9.0,                  21.0,                  0.0,                   110.25,                [0.1428571492433548,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.2857143878936768,    -7.0,                  -0.0,                  1.0])

    DeclActor(-6230,   0,       14490,   1200,    -6230,   1500,    14490,   0x007C, 0,  28, 0x0000)
    DeclActor(5240,    0,       -48080,  1200,    6340,    1500,    -47750,  0x007E, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_528",          # 01, 1
        "Function_2_5D9",          # 02, 2
        "Function_3_67E",          # 03, 3
        "Function_4_6AF",          # 04, 4
        "Function_5_86E",          # 05, 5
        "Function_6_9A3",          # 06, 6
        "Function_7_9BE",          # 07, 7
        "Function_8_9D0",          # 08, 8
        "Function_9_D59",          # 09, 9
        "Function_10_10C4",        # 0A, 10
        "Function_11_13F5",        # 0B, 11
        "Function_12_145D",        # 0C, 12
        "Function_13_1730",        # 0D, 13
        "Function_14_19AA",        # 0E, 14
        "Function_15_1B6C",        # 0F, 15
        "Function_16_1F52",        # 10, 16
        "Function_17_1FCD",        # 11, 17
        "Function_18_2D25",        # 12, 18
        "Function_19_31DD",        # 13, 19
        "Function_20_323B",        # 14, 20
        "Function_21_3299",        # 15, 21
        "Function_22_32F7",        # 16, 22
        "Function_23_3355",        # 17, 23
        "Function_24_33B3",        # 18, 24
        "Function_25_3401",        # 19, 25
        "Function_26_416A",        # 1A, 26
        "Function_27_4212",        # 1B, 27
        "Function_28_47B5",        # 1C, 28
        "Function_29_47E0",        # 1D, 29
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4B0"),
        (1, "loc_4BC"),
        (2, "loc_4C8"),
        (3, "loc_4D4"),
        (4, "loc_4E0"),
        (5, "loc_4EC"),
        (6, "loc_4F8"),
        (SWITCH_DEFAULT, "loc_504"),
    )


    label("loc_4B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_504")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_510")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_527")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_510")

    label("loc_527")

    Return()

    # Function_0_470 end

    def Function_1_528(): pass

    label("Function_1_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_53B")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_540")

    label("loc_53B")

    ClearChrFlags(0xD, 0x80)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_553")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_END)), "loc_56B")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_56B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58B")
    SetScenarioFlags(0xE6, 6)
    Jump("loc_5C9")

    label("loc_58B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AF")
    Event(0, 18)
    Jump("loc_5C9")

    label("loc_5AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 17)

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5D8")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)

    label("loc_5D8")

    Return()

    # Function_1_528 end

    def Function_2_5D9(): pass

    label("Function_2_5D9")

    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_606")
    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)

    label("loc_606")

    SetMapObjFrame(0xFF, "BED03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED04", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_649")
    Call(0, 16)

    label("loc_649")

    ClearMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_660")
    OP_66(0x1, 0x1)

    label("loc_660")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67D")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_67D")

    Return()

    # Function_2_5D9 end

    def Function_3_67E(): pass

    label("Function_3_67E")

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

    # Function_3_67E end

    def Function_4_6AF(): pass

    label("Function_4_6AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A4")

    ChrTalk(
        0xFE,
        "Mr. Gable finally came back, thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was certain he'd get mad at me for\x01",
            "giving away his bed, but he looks a\x01",
            "little down in the dumps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's kinda pitiful, seeing him mope around\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_81B")

    label("loc_7A4")


    ChrTalk(
        0xFE,
        (
            "Ever since he came back to his room,\x01",
            "Mr. Gable has been moping nonstop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something scare him, or what...?\x02",
    )

    CloseMessageWindow()

    label("loc_81B")

    Jump("loc_86A")

    label("loc_820")


    ChrTalk(
        0xFE,
        (
            "Where in the world could Mr. Gable have\x01",
            "gone to at a time like this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    TalkEnd(0xFE)
    Return()

    # Function_4_6AF end

    def Function_5_86E(): pass

    label("Function_5_86E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_END)), "loc_911")

    ChrTalk(
        0xFE,
        (
            "I wish I could give Mr. Dyson the\x01",
            "treatment he needs, but look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This room doesn't have close to the\x01",
            "amount of supplies I need...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_911")


    ChrTalk(
        0xFE,
        (
            "At least he's managed to calm down.\x01",
            "Though, the fever isn't encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's going to be in a lot of pain for\x01",
            "a while. Poor guy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F")

    TalkEnd(0xFE)
    Return()

    # Function_5_86E end

    def Function_6_9A3(): pass

    label("Function_6_9A3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Ugh... *groan*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_9A3 end

    def Function_7_9BE(): pass

    label("Function_7_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CF")
    Call(0, 25)

    label("loc_9CF")

    Return()

    # Function_7_9BE end

    def Function_8_9D0(): pass

    label("Function_8_9D0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A64")
    Jump("loc_AAE")

    label("loc_A64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AAE")

    label("loc_A84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AAE")

    label("loc_AA4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AAE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C44")

    ChrTalk(
        0xFE,
        (
            "O-Oh, Goddess... What do I do?\x01",
            "Run? Fight? Stay and hide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If he was so bold to send an assassin\x01",
            "after me, where could I even run to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(His delusions have broken him.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(Considering he's likely well acquainted\x01",
            "with Speaker Hartmann's two-facedness,\x01",
            "I can fully understand his reaction...)\x02\x03",
            "#0108F(What a sad, sad man.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D51")

    label("loc_C44")


    ChrTalk(
        0xFE,
        (
            "Damn it all! If you want war, Hartmann,\x01",
            "I'll give you war! It's time for revolution!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I expose this assassination plot, the\x01",
            "public will no doubt side with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then again, that wouldn't work. By\x01",
            "the time I act, Hartmann would have\x01",
            "covered his tracks...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D51")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_9D0 end

    def Function_9_D59(): pass

    label("Function_9_D59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6E")
    Call(0, 10)
    Jump("loc_10C0")

    label("loc_D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1C")

    ChrTalk(
        0xF,
        (
            "#1302FExcuse me... You're helping Lloyd\x01",
            "and the others, right?\x02\x03",
            "#1309FI wanted to thank you for earlier.\x01",
            "Without you, I don't know how\x01",
            "we would have made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702FHeh. I only assisted because things\x01",
            "happened to unfold that way.\x02\x03",
            "If you wish to give thanks, give it to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1305F(Huh? Have I met this person before?\x01",
            "Something about his voice...)\x02\x03",
            "#1300F(Hmm, must be my imagination.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 0)
    Jump("loc_10C0")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1027")

    ChrTalk(
        0xF,
        (
            "#1301FI understand, Lloyd, but...\x02\x03",
            "I just can't accept that Doctor Guenter\x01",
            "would be a part of something so appalling.\x02\x03",
            "#1303FSure, he likes to play hooky to indulge in\x01",
            "his hobbies, but he was always such a\x01",
            "kind doctor who loved his patients...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10C0")

    label("loc_1027")


    ChrTalk(
        0xF,
        (
            "#1303FI just can't accept that Doctor Guenter\x01",
            "would be a part of something so appalling...\x02\x03",
            "#1308FWas his entire persona at St. Ursula just\x01",
            "an act?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C0")

    TalkEnd(0xFE)
    Return()

    # Function_9_D59 end

    def Function_10_10C4(): pass

    label("Function_10_10C4")

    EventBegin(0x0)
    Fade(500)
    OP_68(5950, 1000, -48900, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 5000, 0, -48900, 45)
    SetChrPos(0x102, 4130, 0, -49060, 45)
    SetChrPos(0x103, 3790, 0, -48130, 90)
    SetChrPos(0x104, 3320, 0, -47550, 90)
    SetChrPos(0x106, 5890, 0, -50380, 0)
    OP_93(0xF, 0x0, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#1302FPhew. It looks like the medicine is finally\x01",
            "kicking in. Michael's sleeping like a baby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThat's great to hear, Cecile.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xF, 400)

    ChrTalk(
        0x101,
        (
            "#0005F(Oh, right. I found Guy's badge...)\x02\x03",
            "#0008F(I should tell her that I finally found a\x01",
            "memento of him, shouldn't I?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0006F(No, what am I thinking?)\x02\x03",
            "(Her plate is full as is. Laying that on her\x01",
            "now would be an unnecessary burden.)\x02\x03",
            "#0008F(I'm sorry, Cecile. We'll have a long chat\x01",
            "after this is all over and done with.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 400)

    ChrTalk(
        0xF,
        "#1305FLloyd, is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDon't worry about me. I'm just thinking.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 5000, 0, -48900, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xEC, 7)
    EventEnd(0x5)
    Return()

    # Function_10_10C4 end

    def Function_11_13F5(): pass

    label("Function_11_13F5")

    TalkBegin(0x10)

    ChrTalk(
        0x10,
        "Zzz... Zzz...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Michael is sleeping soundly, thanks to the medicine\x01",
            "Cecile procured.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_11_13F5 end

    def Function_12_145D(): pass

    label("Function_12_145D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F1")
    Jump("loc_153B")

    label("loc_14F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1511")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_153B")

    label("loc_1511")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1531")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_153B")

    label("loc_1531")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_153B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")

    ChrTalk(
        0xFE,
        (
            "It's true. There are quite a few parts of\x01",
            "Doctor Guenter's personal history that\x01",
            "have been concealed from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We know he's Remiferian. He's proven himself\x01",
            "an expert in pharmacology and neurology...\x01",
            "But what else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, we really don't\x01",
            "know anything about him, do we?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1728")

    label("loc_16A1")


    ChrTalk(
        0xFE,
        "His outward personality, his medical prowess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We might have only scratched the surface of\x01",
            "the man that is Joachim Guenter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1728")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_145D end

    def Function_13_1730(): pass

    label("Function_13_1730")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17C4")
    Jump("loc_180E")

    label("loc_17C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180E")

    label("loc_17E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1804")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_180E")

    label("loc_1804")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1923")

    ChrTalk(
        0xFE,
        (
            "What in Aidios' name was that stagnant air\x01",
            "that filled the research ward? Is the AC not\x01",
            "functioning properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Either way, I hope it's contained. If it reaches the\x01",
            "hospital, the patients' conditions could worsen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_19A2")

    label("loc_1923")


    ChrTalk(
        0xFE,
        "What in Aidios' name was that stagnant air...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We may do research all day, but we don't know\x01",
            "everything, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_1730 end

    def Function_14_19AA(): pass

    label("Function_14_19AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB8")

    ChrTalk(
        0xFE,
        (
            "The guy with the monsters was heading\x01",
            "up to the research ward's fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He wasn't wearing a gaudy, black suit,\x01",
            "so I don't think he was mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing someone walk among monsters without\x01",
            "even breaking a sweat is just too weird...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B68")

    label("loc_1AB8")


    ChrTalk(
        0xFE,
        (
            "I don't think that guy who went up to the\x01",
            "fourth floor was a part of the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing someone walk among monsters without\x01",
            "even breaking a sweat is just too weird...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B68")

    TalkEnd(0xFE)
    Return()

    # Function_14_19AA end

    def Function_15_1B6C(): pass

    label("Function_15_1B6C")

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
    OP_68(-9000, 1000, 9000, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -4800, 0, 9600, 270)
    SetChrPos(0x102, -4800, 0, 8300, 270)
    SetChrPos(0x103, -3500, 0, 8300, 270)
    SetChrPos(0x104, -3500, 0, 9600, 270)
    SetChrPos(0x106, -2200, 0, 8950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -8430, 0, 21350, 180)
    SetChrPos(0x9, -9590, 0, 21100, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 3000)

    def lambda_1CBB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CBB)
    Sleep(50)

    def lambda_1CD3():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CD3)
    Sleep(50)

    def lambda_1CEB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CEB)
    Sleep(50)

    def lambda_1D03():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D03)
    Sleep(50)

    def lambda_1D1B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1D1B)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1DB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DB5)
    Sleep(50)

    def lambda_1DC5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1DC5)
    Sleep(50)

    def lambda_1DD5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DD5)
    Sleep(50)

    def lambda_1DE5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DE5)
    Sleep(50)

    def lambda_1DF5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DF5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Fade(500)
    OP_68(-8850, 1000, 16000, 0)
    OP_68(-8850, 1000, 10500, 1500)
    SetCameraDistance(25500, 0)
    SetCameraDistance(19500, 1500)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_1E65():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E65)

    def lambda_1E7A():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E7A)
    Sleep(500)
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
    Sleep(500)
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
    SetChrPos(0x0, -8500, 0, 8500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE2, 3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_1B6C end

    def Function_16_1F52(): pass

    label("Function_16_1F52")

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
    SetChrPos(0x8, -8580, 0, 14110, 315)
    SetChrPos(0x9, -11600, 0, 11420, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_16_1F52 end

    def Function_17_1FCD(): pass

    label("Function_17_1FCD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-52500, 1000, -50000, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -49550, 50, -49660, 270)
    SetChrPos(0x102, -49550, 50, -50640, 270)
    SetChrPos(0x103, -48250, 50, -50640, 270)
    SetChrPos(0x104, -48250, 50, -49660, 270)
    SetChrPos(0x106, -46950, 50, -50160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, -56730, 0, -50110, 0)
    SetChrPos(0xB, -55580, 0, -49500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_68(-54000, 1000, -50000, 3000)

    def lambda_2138():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2138)
    Sleep(50)

    def lambda_2150():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2150)
    Sleep(50)

    def lambda_2168():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2168)
    Sleep(50)

    def lambda_2180():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2180)
    Sleep(50)

    def lambda_2198():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2198)
    Sleep(200)

    def lambda_21B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21B0)

    def lambda_21C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21C1)
    Sleep(100)

    def lambda_21D5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21D5)
    Sleep(50)

    def lambda_21E5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_21E5)
    Sleep(350)

    def lambda_21F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_21F5)

    def lambda_2206():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2206)
    Sleep(500)

    def lambda_221A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_221A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xA,
        "#5100572V#3POh! It's Randy and Cecile's little brother!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100573V#0302F#11PHaha. Glad to see you're safe,\x01",
            "my beautiful Philia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100574V#6PYou're the CPD, aren't you?\x01",
            "Is everything okay now?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100575V#0003F#11PUnfortunately, there are still intruders\x01",
            "moving around in the hospital.\x02\x03",
            "#5100576V#0013FHey, isn't that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100577V#3PYes. The janitor, Mr. Dyson.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100578V#3PHe suffered a serious laceration during\x01",
            "the commotion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100579V#6PI patched it up as well as I could with the\x01",
            "first aid kit, so he's not in any immediate\x01",
            "danger, I don't think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100580V#6PStill, I don't want to take my eyes off him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100581V#0006F#11PThank goodness he's stable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100582V#0105F#11PSpeaking of the injured, where's the\x01",
            "patient that was staying here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100583V#3PRepresentative Gable was being treated in\x01",
            "this room, but he's nowhere to be found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100584V#3PHmm, where could he have run off to...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100585V#3POh, well. He was faking whatever he claimed\x01",
            "he had, anyway. I don't think we need\x01",
            "to worry about him too much.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5100586V#0003F#11PO-Oh. Well, we'll try and confirm\x01",
            "his safety, just in case.\x02\x03",
            "#5100587V#0005FThat reminds me, Philia.\x02\x03",
            "#5100588V#0001FDo you know where Cecile is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100589V#3PHuh? Cecile?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100590V#3PBefore the mafia showed up, I could have\x01",
            "sworn she was in the nurses' station with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100591V#6PWait, didn't Miss Neues go to check on\x01",
            "Room 301? The one Michael's in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5100592V#6PI remember her mentioning that she was\x01",
            "going to read him a picture book, since\x01",
            "he was all alone after Shizuku left...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_2B93")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    ChrTalk(
        0x103,
        (
            "#5100593V#0205F#11PWe entered Room 301 on our way\x01",
            "here, did we not...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100594V#0301F#11PYep. Place was as empty as could be.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#5100595V#3PS-Seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100596V#6PThen where the heck is she...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100597V#0008F#11PWe'll continue searching for Cecile and\x01",
            "Michael, since they're probably together.\x02\x03",
            "#5100598V#0013FYou two focus on treating the wounded,\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100599V#6PS-Sure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100600V#3PDon't get caught by those crazy people!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CC6")

    label("loc_2B93")


    ChrTalk(
        0x103,
        (
            "#5100601V#0205F#11PI believe Room 301 was one of the\x01",
            "rooms we saw on our way here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100602V#0006F#11PYeah, we walked right past it.\x02\x03",
            "#5100603V#0000FWe'll see if she's there. You two focus\x01",
            "on treating the wounded, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100604V#6PSure thing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100605V#3PYep, just leave it to us!\x02",
    )

    CloseMessageWindow()

    label("loc_2CC6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -53190, 0, -50010, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xA, -55170, 0, -50070, 0)
    SetChrPos(0xB, -55930, 0, -49530, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE2, 4)
    OP_29(0x4D, 0x1, 0xA)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_1FCD end

    def Function_18_2D25(): pass

    label("Function_18_2D25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3300, 1000, -50000, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -800, 0, -50000, 90)
    SetChrPos(0x102, -800, 0, -50000, 90)
    SetChrPos(0x103, -800, 0, -50000, 90)
    SetChrPos(0x104, -800, 0, -50000, 90)
    SetChrPos(0x106, -800, 0, -50000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(4700, 1000, -50000, 3000)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(600)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 21)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(600)
    BeginChrThread(0x106, 3, 0, 23)
    WaitChrThread(0x101, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 6)), scpexpr(EXPR_END)), "loc_2EC2")

    ChrTalk(
        0x101,
        "#5100606V#0001F#6PEmpty like we thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100611V#0106F#6PThey aren't hiding under the bed,\x01",
            "are they...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB9")

    label("loc_2EC2")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5100608V#0005F#6PW-Wait, where are they...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100609V#0301F#6PThis is Room 301, ain't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100610V#0101F#6PI don't get it. They should be here...\x02\x03",
            "#5100607V#0108FThey aren't hiding under the bed,\x01",
            "are they...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB9")


    ChrTalk(
        0x103,
        (
            "#5100612V#0201F#6PI think we would have noticed, if\x01",
            "that was the case.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x106)
    OP_68(5790, 1000, -49750, 2500)
    BeginChrThread(0x106, 3, 0, 24)
    WaitChrThread(0x106, 3)
    OP_6F(0x1)
    Sound(820, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        (
            "#5100613V\x07\x03",
            "#0700F#11PThe air's still warm.\x02\x03",
            "#5100614VThe occupant was here not too long ago...\x02\x03",
            "#5100615V...with that nurse, as well. Cecile, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100616V\x07\x00",
            "#0013F#6PDamn! Come on, let's keep searching\x01",
            "for them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100617V#0307F#6PYou got it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    OP_68(3000, 1000, -50000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 3000, 0, -50000, 90)
    SetChrPos(0x1, 3000, 0, -50000, 90)
    SetChrPos(0x2, 3000, 0, -50000, 90)
    SetChrPos(0x3, 3000, 0, -50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE2, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_2D25 end

    def Function_19_31DD(): pass

    label("Function_19_31DD")


    def lambda_31E2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31E2)

    def lambda_31F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31F7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3210():
        OP_95(0xFE, 3090, 0, -49370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3210)
    WaitChrThread(0x101, 1)

    def lambda_322E():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_19_31DD end

    def Function_20_323B(): pass

    label("Function_20_323B")


    def lambda_3240():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3240)

    def lambda_3255():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3255)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_326E():
        OP_95(0xFE, 2350, 0, -51300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_326E)
    WaitChrThread(0xFE, 1)

    def lambda_328C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_328C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_323B end

    def Function_21_3299(): pass

    label("Function_21_3299")


    def lambda_329E():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_329E)

    def lambda_32B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32B3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_32CC():
        OP_95(0xFE, 2420, 0, -48520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32CC)
    WaitChrThread(0xFE, 1)

    def lambda_32EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32EA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_3299 end

    def Function_22_32F7(): pass

    label("Function_22_32F7")


    def lambda_32FC():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32FC)

    def lambda_3311():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3311)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_332A():
        OP_95(0xFE, 1330, 0, -48080, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_332A)
    WaitChrThread(0xFE, 1)

    def lambda_3348():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3348)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_32F7 end

    def Function_23_3355(): pass

    label("Function_23_3355")


    def lambda_335A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_335A)

    def lambda_336F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_336F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_3388():
        OP_95(0xFE, 1320, 50, -50150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3388)
    WaitChrThread(0xFE, 1)

    def lambda_33A6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33A6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_3355 end

    def Function_24_33B3(): pass

    label("Function_24_33B3")


    def lambda_33B8():
        OP_95(0xFE, 4950, 0, -50540, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33B8)
    WaitChrThread(0xFE, 1)

    def lambda_33D6():
        OP_95(0xFE, 5950, 0, -48890, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33D6)
    WaitChrThread(0xFE, 1)

    def lambda_33F4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_33B3 end

    def Function_25_3401(): pass

    label("Function_25_3401")

    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    Fade(1000)
    OP_68(54550, 1300, -1040, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 54580, 0, -1490, 180)
    SetChrPos(0x102, 54860, 0, -360, 180)
    SetChrPos(0x103, 54100, 0, 400, 180)
    SetChrPos(0x104, 54810, 0, 1280, 180)
    SetChrPos(0x106, 54100, 0, 2190, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xD, 54620, 0, -2970, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100618V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9C(0xD, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#5100619V#2PE-Eeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100620V#2PPlease, spare me! I beg of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100621V#0301F#5PThe hell is this guy's problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100622V#0106F#5PRepresentative Gable, of the Imperial Faction.\x01",
            "The same one Philia mentioned a moment ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xD)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#5100623V#2PWh-Who are you ruffians?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100624V#2PAre you with the mafia?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100625V#0003F#5PNo, sir. We're with the Crossbell Police\x01",
            "Department, Special Support Section.\x02\x03",
            "#5100626V#0001FMr. Gable, what are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100627V#2PA-Are you blind, boy?! I'm hiding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100628V#2PThe mafia must have come to get\x01",
            "rid of me once and for all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100629V#2PSpeaker Hartmann, you coward...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#5100630V#0008F#5P(Elie, what do you think?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100631V#0106F#5P(Absolutely paranoid, no doubt about it.)\x02\x03",
            "#5100632V#0111F(The speaker clearly couldn't care less\x01",
            "about him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100633V#0206F#5P(What a shock.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100634V#2PA-Anyway, the police, you say? I order you\x01",
            "to take me with you and get me out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100635V#2PI'd rather not die today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100636V#0003F#5PI'm sorry, sir. We haven't completed our\x01",
            "sweep of the hospital yet. There are still\x01",
            "unconfirmed people out there.\x02\x03",
            "#5100637V#0001FWe have to make sure they're safe\x01",
            "before conducting any evacuations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100638V#0100F#5PFor now, could you return to your room\x01",
            "and wait for us?\x02\x03",
            "#5100639VWe've taken out the mafia in this area,\x01",
            "so you should be able to move safely,\x01",
            "if you're quick about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100640V#2PWh-Who...who do you think I am?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100641V#2PI am one of the MOST important representatives\x01",
            "of the Crossbell Diet! I am irreplaceable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100642V\x07\x03",
            "#0700F#5PWhat an annoying, sniveling man. Would you\x01",
            "object to me putting him to sleep?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#5100643V#2PE-Excuse me? Who are you to...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100644V#2PWait, that black outfit... Haven't I heard\x01",
            "about you from somewhere...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100645V\x07\x03",
            "#0702F#5PHeh. Where indeed?\x02\x03",
            "#5100646VWas it not the little rumor drifting around\x01",
            "the government, relating to Heiyue? Or\x01",
            "am I mistaken?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xD,
        "#5100647V#2P*gasp* It can't be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100648V#0006F#5PEnough teasing, Yin.\x02\x03",
            "#5100649V#0013FMr. Gable. This is a state of emergency.\x02\x03",
            "#5100650VNow, please cooperate. Go take shelter\x01",
            "in your room and stay there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100651V#2PF-F-Fine. Have it your way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100652V#2PJust drive those mafia loons away at once!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(56620, 500, 2080, 0)
    MoveCamera(70, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    SetCameraDistance(27000, 2500)
    SetChrPos(0x101, 54770, 0, 2600, 270)
    SetChrPos(0x102, 55470, 0, 3170, 270)
    SetChrPos(0x103, 55830, 0, 2100, 270)
    SetChrPos(0x104, 56450, 0, 2800, 270)
    SetChrPos(0x106, 57130, 0, 2110, 270)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0xD, 3, 0, 26)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#5100653V#0300F#5PWhew. For a hospital patient, he's got\x01",
            "some legs, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100654V#0211F#11PMiss Philia DID say he was admitted\x01",
            "under false pretenses, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A5")

    ChrTalk(
        0x101,
        (
            "#5100655V#0006F#5PWe've wasted enough time with him.\x01",
            "Let's keep searching for Cecile and\x01",
            "Michael.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4104")

    label("loc_40A5")


    ChrTalk(
        0x101,
        (
            "#5100656V#0006F#5PWe've wasted enough time with him.\x01",
            "Let's hurry up to the research ward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4104")


    ChrTalk(
        0x102,
        "#5100657V#0101F#5PRight!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 50910, 0, 110, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetScenarioFlags(0xE2, 6)
    OP_29(0x4D, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_3401 end

    def Function_26_416A(): pass

    label("Function_26_416A")

    SetChrPos(0xFE, 54490, 0, 1290, 225)

    def lambda_4180():
        OP_95(0xFE, 53490, 0, 2450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4180)
    WaitChrThread(0xFE, 1)

    def lambda_419E():
        OP_95(0xFE, 51600, 0, 2360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_419E)
    WaitChrThread(0xFE, 1)

    def lambda_41BC():
        OP_95(0xFE, 51080, 0, 40, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41BC)
    WaitChrThread(0xFE, 1)

    def lambda_41DA():
        OP_95(0xFE, 48880, 0, 20, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41DA)
    Sound(107, 0, 100, 0)
    Sleep(200)

    def lambda_41FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41FD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_416A end

    def Function_27_4212(): pass

    label("Function_27_4212")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(5290, 2000, -50030, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21610, 0)
    SetChrPos(0x101, 4600, 0, -50000, 90)
    SetChrPos(0x102, 3600, 0, -49400, 90)
    SetChrPos(0x103, 3600, 0, -50600, 90)
    SetChrPos(0x104, 2200, 0, -49400, 90)
    SetChrPos(0x106, 2200, 0, -50600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    SetChrPos(0xF, 6200, 0, -50000, 270)
    FadeToBright(1000, 0)
    OP_68(5290, 1000, -50030, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#5100694V#1306F#11PThat's everything that's happened, is it?\x02\x03",
            "#5100695V#1308FI can't believe Doctor Guenter would...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100696V#0006F#6PWell, we aren't 100 percent sure of his involvement.\x02\x03",
            "#5100697V#0001FDo you know if he's still in the research ward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5100698V#1303F#11PI don't know...\x02\x03",
            "#5100699V#1301FIt's possible that he's still there,\x01",
            "along with the other doctors.\x02\x03",
            "#5100700VI'm pretty sure the mafia was only able to\x01",
            "drag out some of the interns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100701V#0003F#6PThere's our next lead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100702V#0301F#6PAin't we forgetting something? What was\x01",
            "up with those monsters just now?\x02\x03",
            "#5100703VThey sure as hell weren't normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100704V#0208F#6PI feel the same.\x02\x03",
            "#5100705VI had the feeling there was something\x01",
            "amiss about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100706V#0101F#6PThey must be the mafia's doing, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5100707V#1306F#11PI'm not sure, but they first appeared\x01",
            "in the research ward.\x02\x03",
            "#5100708V#1301FIn a matter of seconds, we were\x01",
            "surrounded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100709V\x07\x03",
            "#0700F#6PThis research ward appears to\x01",
            "hold the answers we seek.\x02\x03",
            "#5100710VTime is fleeting. Shall we?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#5100711V\x07\x00",
            "#0013F#11PLet's go!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3670, 0, -50220, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0xF, 6520, 0, -48890, 0)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0xE2, 7)
    OP_29(0x4D, 0x1, 0xC)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_4212 end

    def Function_28_47B5(): pass

    label("Function_28_47B5")

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

    # Function_28_47B5 end

    def Function_29_47E0(): pass

    label("Function_29_47E0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4820")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_4820")


    ChrTalk(
        0x103,
        (
            "#0200FHold on, Lloyd. I am detecting someone\x01",
            "in the room on the left-side of the hall.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_489D")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_489D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_48BE")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_48BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_48DF")
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_48DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4900")
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_4900")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4925")

    def lambda_4917():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4917)

    label("loc_4925")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4947")

    def lambda_4939():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4939)

    label("loc_4947")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4969")

    def lambda_495B():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_495B)

    label("loc_4969")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_498B")

    def lambda_497D():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_497D)

    label("loc_498B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49AD")

    def lambda_499F():
        OP_92(0xFE, 0xFFFFBB86, 0x22B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_499F)

    label("loc_49AD")

    Sleep(1000)
    Fade(500)
    OP_68(-16780, 1000, 8490, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0005FGood catch, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101FWe should investigate before proceeding.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A8A")

    label("loc_4A3C")


    ChrTalk(
        0x101,
        (
            "#0001FAccording to Tio, there's someone\x01",
            "in Room 302. Let's check it out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8A")

    Jump("loc_4AC8")

    label("loc_4A8F")


    ChrTalk(
        0x101,
        (
            "#0001FCecile should be in Room 301, so\x01",
            "let's hurry!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AC8")

    Sleep(50)
    SetChrPos(0x0, -8930, 0, 17770, 180)
    EventEnd(0x4)
    Return()

    # Function_29_47E0 end

    SaveToFile()

Try(main)
