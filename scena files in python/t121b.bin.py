from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t121b.bin",                # FileName
        "t121b",                    # MapName
        "t121b",                    # Location
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
        "t121b",                  # 0
        "Butler Coen",            # 1
        "Man in Suit",            # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Mafioso",                # 5
        "Mafioso",                # 6
        "Mafioso",                # 7
        "Mafioso",                # 8
        "Lechter",                # 9
        "Elizabeth",              # 10
        "Voice",                  # 11
        "Yin",                    # 12
        "bt113b",                 # 13
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 8, 14, 180)
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
            ("ms31002.dat", "ms31102.dat", "ms31102.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch25900.itc",                   # 00
        "chr/ch36000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch07400.itc",                   # 05
        "chr/ch39100.itc",                   # 06
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
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-58000,  0,       -49500,  180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(58000,   0,       -49500,  180,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(60700,   0,       2400,    0,    389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(63099,   0,       4000,    315,  389,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -55500,  0,    389,  0x0, 3,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -56500,  0,    389,  0x0, 3,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(58000,   0,       -57500,  0,    389,  0x0, 3,   4,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-54029,  0,       6579,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-52930,  0,       6579,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 14,  58.0,                  -57.5,                 -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.600000381469727,   19.166667938232422,    0.20000000298023224,   1.0])

    DeclActor(55540,   0,       6000,    2500,    55540,   1500,    6000,    0x007C, 0,  8,  0x0000)
    DeclActor(-57850,  0,       4860,    2500,    -57850,  1500,    4860,    0x007C, 0,  8,  0x0000)
    DeclActor(55540,   0,       1500,    2500,    55540,   1500,    1500,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_4A0",          # 00, 0
        "Function_1_558",          # 01, 1
        "Function_2_5EC",          # 02, 2
        "Function_3_726",          # 03, 3
        "Function_4_AB7",          # 04, 4
        "Function_5_AF3",          # 05, 5
        "Function_6_D5E",          # 06, 6
        "Function_7_EFD",          # 07, 7
        "Function_8_F15",          # 08, 8
        "Function_9_FA9",          # 09, 9
        "Function_10_FE6",         # 0A, 10
        "Function_11_109E",        # 0B, 11
        "Function_12_1156",        # 0C, 12
        "Function_13_153F",        # 0D, 13
        "Function_14_1E0A",        # 0E, 14
        "Function_15_24FC",        # 0F, 15
        "Function_16_3545",        # 10, 16
        "Function_17_35A6",        # 11, 17
        "Function_18_3607",        # 12, 18
        "Function_19_3668",        # 13, 19
        "Function_20_3B26",        # 14, 20
        "Function_21_3F28",        # 15, 21
        "Function_22_3F6C",        # 16, 22
        "Function_23_3F92",        # 17, 23
        "Function_24_6087",        # 18, 24
        "Function_25_60DC",        # 19, 25
        "Function_26_6121",        # 1A, 26
        "Function_27_6166",        # 1B, 27
        "Function_28_619D",        # 1C, 28
        "Function_29_61DB",        # 1D, 29
        "Function_30_621F",        # 1E, 30
        "Function_31_6263",        # 1F, 31
        "Function_32_62A7",        # 20, 32
    ))


    def Function_0_4A0(): pass

    label("Function_0_4A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4E0"),
        (1, "loc_4EC"),
        (2, "loc_4F8"),
        (3, "loc_504"),
        (4, "loc_510"),
        (5, "loc_51C"),
        (6, "loc_528"),
        (SWITCH_DEFAULT, "loc_534"),
    )


    label("loc_4E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_4EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_4F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_504")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_510")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_51C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_528")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_534")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_557")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_540")

    label("loc_557")

    Return()

    # Function_0_4A0 end

    def Function_1_558(): pass

    label("Function_1_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_5B7")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_592")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_5B7")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_5A0")
    Jump("loc_5B7")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_5AE")
    Jump("loc_5B7")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_5B7")

    label("loc_5B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D1")
    Event(0, 19)

    label("loc_5D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EB")
    Event(0, 23)

    label("loc_5EB")

    Return()

    # Function_1_558 end

    def Function_2_5EC(): pass

    label("Function_2_5EC")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_609")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_644")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_644")
    Call(0, 9)

    label("loc_644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_667")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_667")
    Call(0, 10)

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_68A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68A")
    Call(0, 11)

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_END)), "loc_6B4")
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    Jump("loc_6D0")

    label("loc_6B4")

    SetMapObjFrame(0xFF, "mado_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x0, 0x1)

    label("loc_6D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_6D9")

    label("loc_6D9")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1")
    OP_1B(0x2, 0x0, 0x20)

    label("loc_6F1")

    SetMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B")
    ClearMapObjFlags(0x8, 0x10)

    label("loc_70B")

    SetMapObjFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_725")
    ClearMapObjFlags(0x9, 0x10)

    label("loc_725")

    Return()

    # Function_2_5EC end

    def Function_3_726(): pass

    label("Function_3_726")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C")
    Call(0, 12)
    Jump("loc_AB6")

    label("loc_73C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_74D")
    Jump("loc_AB3")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_7E6")

    ChrTalk(
        0xFE,
        (
            "Mr. Hartmann is currently putting the final\x01",
            "touches on the auction program with\x01",
            "President Marconi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please keep your voices down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB3")

    label("loc_7E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8A4")

    ChrTalk(
        0xFE,
        (
            "This is the personal room of the mansion's\x01",
            "owner: The wonderful, honorable Speaker\x01",
            "Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please hurry on to the main hall. The\x01",
            "auction will be beginning shortly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB3")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(
        0xFE,
        (
            "This is the personal room of the mansion's\x01",
            "owner, the wonderful, honorable Speaker\x01",
            "Hartmann.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_9F6")

    ChrTalk(
        0xFE,
        (
            "If you are looking for him, I believe he is\x01",
            "greeting guests in the salon, which is on\x01",
            "the left-hand side of the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have any business with him, please\x01",
            "head over there and introduce yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB3")

    label("loc_9F6")


    ChrTalk(
        0xFE,
        (
            "Mr. Hartmann is preparing to go to the salon,\x01",
            "which is on the left-hand side of the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have any business with him, please\x01",
            "head over there and introduce yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB3")

    TalkEnd(0x8)

    label("loc_AB6")

    Return()

    # Function_3_726 end

    def Function_4_AB7(): pass

    label("Function_4_AB7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He is completely unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_4_AB7 end

    def Function_5_AF3(): pass

    label("Function_5_AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B04")
    Jump("loc_D5A")

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B12")
    Jump("loc_D5A")

    label("loc_B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BC2")

    ChrTalk(
        0xFE,
        (
            "I beg your pardon, but if you continue to\x01",
            "stand around, you'll interfere with the\x01",
            "movement of the exhibits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please make your way back to the main hall.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D5A")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_D5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")

    ChrTalk(
        0xFE,
        "Do you need something else, guests?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100FAh, no. Sorry about that.\x02\x03",
            "#5108F(What was that voice...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "The exhibits are under lock and key\x01",
            "until the auction's opening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wait to see them in the auction, please.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D5A")

    label("loc_CDB")


    ChrTalk(
        0xFE,
        (
            "The exhibits are going to remain private\x01",
            "until the start of the event. Please look\x01",
            "forward to seeing them in the auction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5A")

    TalkEnd(0xFE)
    Return()

    # Function_5_AF3 end

    def Function_6_D5E(): pass

    label("Function_6_D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(
        0x10,
        (
            "#3505FThe heck? The intruders from the back\x01",
            "courtyard somehow made it in here.\x02\x03",
            "#3502FYou sure you have time to relax?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#5810F#NSee ya later, weirdo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3504FFare thee well, young one.\x02\x03",
            "#3501FYou know, isn't calling me\x01",
            "a weirdo a little harsh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EF9")

    label("loc_E77")

    OP_4B(0x11, 0xFF)
    TurnDirection(0xFE, 0x11, 0)

    ChrTalk(
        0x10,
        (
            "#3509FYour owner isn't here to be a\x01",
            "killjoy, so let's play, Noire!\x02\x03",
            "#3507FTime for kick the can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Nyaoon?\x02",
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)

    label("loc_EF9")

    TalkEnd(0xFE)
    Return()

    # Function_6_D5E end

    def Function_7_EFD(): pass

    label("Function_7_EFD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Prr, nya-n.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_EFD end

    def Function_8_F15(): pass

    label("Function_8_F15")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8C")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_F8C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA8")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_FA8")

    Return()

    # Function_8_F15 end

    def Function_9_FA9(): pass

    label("Function_9_FA9")

    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    Return()

    # Function_9_FA9 end

    def Function_10_FE6(): pass

    label("Function_10_FE6")

    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 59800, 0, 1810, 0)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xB, 58650, 0, 3490, 45)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 64230, 0, 4180, 315)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)
    Return()

    # Function_10_FE6 end

    def Function_11_109E(): pass

    label("Function_11_109E")

    SetChrChipByIndex(0xD, 0x3)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, 58290, 0, -55060, 45)
    SetChrChipByIndex(0xE, 0x3)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 59250, 0, -56490, 180)
    SetChrChipByIndex(0xF, 0x3)
    SetChrSubChip(0xF, 0x1)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x1)
    SetChrPos(0xF, 56290, 0, -58070, 135)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_11_109E end

    def Function_12_1156(): pass

    label("Function_12_1156")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(-57790, 1200, -50440, 0)
    MoveCamera(315, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18290, 0)
    SetChrPos(0x101, -57400, 0, -51000, 0)
    SetChrPos(0xEF, -58600, 0, -51000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#3501064V#11PExcuse me, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3501065V#11PThis is the owner's personal room.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501066V#5105F#6PYou mean...Speaker Hartmann's?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3501067V#11PQuite so, sir.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 4)), scpexpr(EXPR_END)), "loc_1373")

    ChrTalk(
        0x8,
        "#3501068V#11PUnfortunately, Mr. Hartmann is currently absent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3501069V#11PHe will soon be at the salon, which is on the\x01",
            "left-hand side of the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501070V#5100F#6PYes, I saw him not too long ago.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1480")

    label("loc_1373")


    ChrTalk(
        0x8,
        (
            "#3501071V#11PGiven the time, you should be able to find him\x01",
            "at the salon, which is on the left-hand side of\x01",
            "the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3501072V#11PIf you have business with Mr. Hartmann, I\x01",
            "advise you to hurry along there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501073V#5100F#6PThanks for the help.\x02",
    )

    CloseMessageWindow()

    label("loc_1480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_14BA")

    ChrTalk(
        0x102,
        "#3501074V#5302F#6PIf you'll excuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1521")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_14EA")

    ChrTalk(
        0x103,
        "#3501075V#5404F#6PExcuse us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1521")

    label("loc_14EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(
        0x104,
        "#3501076V#5609F#6PTalk to ya later, pal.\x02",
    )

    CloseMessageWindow()

    label("loc_1521")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -58000, 0, -51500, 180)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 7)
    EventEnd(0x5)
    Return()

    # Function_12_1156 end

    def Function_13_153F(): pass

    label("Function_13_153F")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(1000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 58000, 0, -48500, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(58220, 1100, -52980, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19200, 0)
    SetChrPos(0x101, 57410, 0, -62690, 0)
    SetChrPos(0xEF, 58150, 0, -63610, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    def lambda_15F1():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15F1)

    def lambda_1606():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1606)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(58220, 1100, -53580, 1800)

    def lambda_1642():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1642)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#3501077V#5PYou'll have to forgive us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3501078V#5PThis room is for staff only.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501079V#5106F#12POh, sorry. We got a little overwhelmed by\x01",
            "the size of this place and lost our way.\x02\x03",
            "#3501080V#5108F(So the mafia is guarding this spot...)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -51980, 1800)
    OP_6F(0x1)

    NpcTalk(
        0x12,
        "Man's Voice",
        (
            "#3501081V#2P#2SHey, everything's sorted like it says in\x01",
            "the list, right?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "Man's Voice",
        (
            "#3501082V#5P#2SYeah! It's almost time to carry the goods\x01",
            "for the first half out!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#3501083V#11POh, sonuva...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501084V#5105F#12PBy any chance...are the exhibits being\x01",
            "stored in there?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(58220, 1100, -53580, 1200)
    OP_93(0x9, 0xB4, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        (
            "#3501085V#5PY-Yeah, that's right. We've been keeping\x01",
            "a watchful eye over them so the auction\x01",
            "can run as smooth as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3501086V#5PLook forward to seeing them in the auction.\x01",
            "You won't want to miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501087V#5104F#12POf course. I wouldn't miss it for the world.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3501088V#5100F#5PReady to head back?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1AC7")

    ChrTalk(
        0x102,
        "#3501089V#5302F#11PYes, shall we?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3E")

    label("loc_1AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1B0C")

    ChrTalk(
        0x103,
        "#3501090V#5402F#11PI'm ready if you are, Brother.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B3E")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1B3E")

    ChrTalk(
        0x104,
        "#3501091V#5602F#11PYup, let's move.\x02",
    )

    CloseMessageWindow()

    label("loc_1B3E")


    def lambda_1B43():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B43)

    def lambda_1B50():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1B50)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Fade(1000)
    OP_68(58390, 1100, -58100, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18240, 0)
    OP_68(58390, 1100, -60100, 3000)

    def lambda_1BA9():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BA9)

    def lambda_1BBE():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1BBE)
    Sleep(2000)
    OP_0D()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    SetChrSubChip(0x101, 0x0)

    def lambda_1C3B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1C3B)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    OP_4B(0xEF, 0xFF)
    Sleep(500)
    OP_93(0xEF, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#3501093V#5111F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1CF1")

    ChrTalk(
        0x102,
        "#3501094V#5305F#12P(Lloyd?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D52")

    label("loc_1CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1D20")

    ChrTalk(
        0x103,
        "#3501095V#5405F#12P(Lloyd?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D52")

    label("loc_1D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1D52")

    ChrTalk(
        0x104,
        "#3501096V#5605F#12P(You good, man?)\x02",
    )

    CloseMessageWindow()

    label("loc_1D52")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3501097V#5106F#5P(It's nothing.)\x02\x03",
            "#3501098V#5101F(Let's just hurry and get out of here.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0xA6, 0)
    OP_29(0x47, 0x1, 0xA)
    EventEnd(0x5)
    NewScene("t119B", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_13_153F end

    def Function_14_1E0A(): pass

    label("Function_14_1E0A")

    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch31150.itc", 0x1E)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31050.itc", 0x21)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("apl/ch50364.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31000.itc", 0x27)
    LoadChrToIndex("chr/ch00550.itc", 0x28)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 58810, 0, -53260, 0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 61240, 0, 1290, 0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 63510, 0, 4260, 315)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 60110, 0, 2400, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 60800, 0, 6500, 180)
    SetChrPos(0x101, 58000, 0, -59000, 0)
    SetChrPos(0xEF, 58700, 0, -60000, 0)
    SetChrPos(0x151, 57300, 0, -60500, 0)
    SetChrPos(0x9, 58930, 0, -51280, 0)
    OP_68(57900, 1500, -60140, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    FadeToBright(1000, 0)
    OP_68(57900, 1500, -58090, 1200)
    OP_6F(0x1)
    OP_0D()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(57900, 1300, -52450, 2000)
    SetCameraDistance(17330, 2000)

    def lambda_2009():
        OP_95(0xFE, 58340, 0, -52690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2009)
    Sleep(100)

    def lambda_2026():
        OP_95(0xFE, 59000, 0, -53630, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2026)
    Sleep(100)

    def lambda_2043():
        OP_95(0xFE, 57030, 0, -53980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2043)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#3501393V#5110F#11PNo good. He's out cold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501394V#5700F#12PIt looks like he was taken out with\x01",
            "a single blow. Impressive.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0x102,
        "#3501395V#5301F#12PWho could do something like this...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(
        0x103,
        "#3501396V#5401F#12PWho is capable of something like this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D0")

    label("loc_2196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(
        0x104,
        "#3501397V#5601F#12PCulprit must be a beast.\x02",
    )

    CloseMessageWindow()

    label("loc_21D0")


    ChrTalk(
        0x101,
        "#3501398V#5113F#11PLet's go inside!\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    OP_68(61440, 1200, 3040, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19300, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(1000, 0)
    OP_68(61440, 1200, 5040, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0xA,
        "#3501399V#12PY-You...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3501400V#2PWhen did you get here?!\x02",
    )

    CloseMessageWindow()
    Sound(1628, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x13,
        (
            "#3501401V\x07\x03",
            "Heh. My name is Yin.\x02\x03",
            "#3501402VAnd I can appear anywhere the\x01",
            "moonlight may shine.\x07\x00\x02",
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
        0xA,
        "#3501403V#4PC-Cut the crap...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#3501404V#6PHurry up and die!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#3501405V\x07\x03",
            "#0702F#5PFools.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14300, 400)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_2457():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2457)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)

    def lambda_2474():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2474)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)

    def lambda_2491():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2491)
    Sleep(300)
    Battle(0xFFFFFFFF, 0x30200004, "", 0x30000500, 0x0, 0x0, 0x0, 0x30031100, 0x30031000, 0x30031000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x200, 0x8)
    FadeToDark(0, 0, -1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    Call(0, 15)
    Return()

    # Function_14_1E0A end

    def Function_15_24FC(): pass

    label("Function_15_24FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31151.itc", 0x1F)
    LoadChrToIndex("chr/ch31153.itc", 0x20)
    LoadChrToIndex("chr/ch31051.itc", 0x22)
    LoadChrToIndex("chr/ch31053.itc", 0x23)
    LoadChrToIndex("chr/ch00500.itc", 0x24)
    LoadChrToIndex("chr/ch00501.itc", 0x25)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    LoadChrToIndex("chr/ch00551.itc", 0x27)
    LoadEffect(0x0, "event\\ev307_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xA, 60780, 0, 4520, 0)
    SetChrPos(0xB, 60140, 0, 5260, 45)
    SetChrPos(0xC, 61710, 0, 5140, 315)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 61000, 0, 6300, 180)
    FadeToBright(0, 0)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(834, 0, 100, 0)
    OP_68(61000, 700, 5300, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14530, 0)
    SetCameraDistance(17660, 500)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 17)
    BeginChrThread(0xC, 3, 0, 18)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    OP_6F(0x79)
    CancelBlur(0)

    ChrTalk(
        0xC,
        "#3501406V#12PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3501407V#6PUnbelievable...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    Sound(514, 0, 100, 0)
    Call(0, 10)
    OP_0D()
    Sleep(750)
    SetChrPos(0x101, 58160, 0, -4030, 0)
    SetChrPos(0xEF, 58160, 0, -4030, 0)
    SetChrPos(0x151, 58160, 0, -4030, 0)
    OP_68(61500, 1000, 4019, 2000)
    MoveCamera(42, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(18540, 2000)
    Sleep(200)

    def lambda_270A():
        OP_95(0xFE, 61080, 0, 1250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_270A)
    Sleep(200)

    def lambda_2727():
        OP_95(0xFE, 61590, 0, 160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2727)
    Sleep(200)

    def lambda_2744():
        OP_95(0xFE, 60490, 0, 60, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2744)
    WaitChrThread(0x101, 1)

    def lambda_2762():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2762)
    WaitChrThread(0xEF, 1)

    def lambda_2773():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2773)
    WaitChrThread(0x151, 1)

    def lambda_2784():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_2784)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501408V#5107F#12PWhat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2836")

    ChrTalk(
        0x102,
        "#3501409V#5307F#12PI thought so!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28AB")

    label("loc_2836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2867")

    ChrTalk(
        0x103,
        "#3501410V#5401F#12PI knew it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_28AB")

    label("loc_2867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_28AB")

    ChrTalk(
        0x104,
        "#3501411V#5607F#12PLooks like we got a party crasher!\x02",
    )

    CloseMessageWindow()

    label("loc_28AB")

    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x13)
    Sleep(300)
    Sound(1609, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x13,
        (
            "#3501412V\x07\x03",
            "#0700F#5PI thought I sensed some peculiar presences.\x01",
            "So you snuck in as well, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501413V\x07\x00",
            "#5113F#12PYou...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501414V#5705F#12PI try not to judge books by their cover, but\x01",
            "you look like quite the dangerous person.\x02\x03",
            "#3501415V#5702FAllow me one guess. You must be Yin,\x01",
            "the assassin everyone is yammering about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#3501416V\x07\x03",
            "#0702F#5PRight you are, Wazy Hemisphere,\x01",
            "leader of Crossbell City's Testaments.\x02\x03",
            "#3501417VI see that one of those odd presences\x01",
            "was you.\x02\x03",
            "#3501418VI still sense others as well... Heh. This\x01",
            "auction truly is a lion's den.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501419V\x07\x00",
            "#5704F#12PAn interesting statement there...\x02\x03",
            "#3501420V#5700FNow, do you plan to get rid of us with\x01",
            "your full power, as you did with them?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    Fade(250)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501421V#5111F#12PWait, what?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x13,
        (
            "#3501422V\x07\x03",
            "#0702F#11PDespite it being simpler to deal with you\x01",
            "all, here and now...\x02\x03",
            "#3501423VI think it will prove more entertaining\x01",
            "to watch you fend for yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#3501424V\x07\x00",
            "#5105F#12PWhat do you mean...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x13, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x13,
        (
            "#3501425V\x07\x03",
            "#0702F#11PThe exhibits for the second half of the auction\x01",
            "are all stored in the room over there.\x02\x03",
            "#3501426VAccording to information that was sent to\x01",
            "Heiyue, there's a 'bomb,' so to speak, among\x01",
            "those items.\x02\x03",
            "#3501427VI recommend you confirm it for yourselves.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1614, 255, 100, 0)
    OP_93(0x13, 0x0, 0x190)
    Sleep(1200)
    Fade(500)
    OP_68(61000, 1000, 4500, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18540, 0)
    SetCameraDistance(17540, 1000)
    OP_0D()
    OP_6F(0x79)
    OP_68(61000, 1500, 8000, 1500)
    MoveCamera(0, 7, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(7250, 1500)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    SetChrChip(0x0, 0x13, 0x1E, 0x12C)

    def lambda_2ECC():
        OP_95(0xFE, 61000, 0, 7500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2ECC)
    WaitChrThread(0x13, 1)
    SetChrSubChip(0x13, 0x2)
    SetChrFlags(0x13, 0x4)
    Sleep(200)
    Sound(854, 0, 100, 0)

    def lambda_2EFC():
        OP_9D(0xFE, 0xEE48, 0xFFFFD8F0, 0x2AF8, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2EFC)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 60800, 0, 9000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0x1770, 0x1F4)
    Sound(921, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetMapObjFrame(0xFF, "mado_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mado_b", 0x1, 0x1)
    WaitChrThread(0x13, 1)
    SetChrChip(0x1, 0x13, 0x0, 0x0)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_6F(0x79)
    Sleep(750)
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(61020, 1000, 7200, 0)
    MoveCamera(55, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19540, 0)
    SetCameraDistance(16540, 2000)

    def lambda_2FF8():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FF8)
    Sleep(300)

    def lambda_3010():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3010)
    Sleep(300)

    def lambda_3028():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3028)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x151, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3501428V\x07\x00",
            "#5107F#11PHey, wait!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_30A8")

    ChrTalk(
        0x102,
        "#3501429V#5301F#11PHow is he that fast?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_30A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_30E6")

    ChrTalk(
        0x103,
        "#3501430V#5401F#11PHe is quick. Too quick.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3118")

    label("loc_30E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(
        0x104,
        "#3501431V#5607F#11PWhoa, slow down!\x02",
    )

    CloseMessageWindow()

    label("loc_3118")


    ChrTalk(
        0x151,
        (
            "#3501432V#5706F#12PI see that this Yin is as much a monster\x01",
            "as the rumors painted him to be.\x02\x03",
            "#3501433V#5703FWe should consider it a blessing from\x01",
            "the Goddess we didn't have to fight.\x02\x03",
            "#3501434V#5701FWhat do you intend to do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3501435V#5103F#5PTime's running out. Let's conduct\x01",
            "a sweep of the exhibit room now.\x02\x03",
            "#3501436V#5101FI want to see whether that bomb he\x01",
            "mentioned is actually there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#3501437V#5702F#12PHaha. You never disappoint, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_338C")

    ChrTalk(
        0x102,
        (
            "#3501438V#5306F#12P*sigh* We don't have much choice.\x02\x03",
            "#3501439V#5300FLet's investigate the room with haste.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BF")

    label("loc_338C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3449")

    ChrTalk(
        0x103,
        (
            "#3501440V#5406F#12PGiven the situation, any other choice\x01",
            "would prove inefficient.\x02\x03",
            "#3501441V#5402FAt the very least, we should conduct\x01",
            "a search while we still have time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BF")

    label("loc_3449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_34BF")

    ChrTalk(
        0x104,
        (
            "#3501442V#5606F#12PDamn. Don't have many other options,\x01",
            "do we?\x02\x03",
            "#3501443V#5600FLet's be quick about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BF")


    ChrTalk(
        0x101,
        "#3501444V#5100F#5PLet's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    SetChrPos(0x0, 60190, 0, -200, 180)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xA6, 3)
    OP_29(0x47, 0x1, 0xD)
    OP_1B(0x2, 0x0, 0x20)
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7302", 0)
    ReplaceBGM("ed7125", "ed7302")
    EventEnd(0x5)
    Return()

    # Function_15_24FC end

    def Function_16_3545(): pass

    label("Function_16_3545")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60780, 800, 4520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3581():
        OP_9D(0xFE, 0xE998, 0x0, 0x712, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3581)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_16_3545 end

    def Function_17_35A6(): pass

    label("Function_17_35A6")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 60140, 800, 5260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_35E2():
        OP_9D(0xFE, 0xE51A, 0x0, 0xDA2, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35E2)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_35A6 end

    def Function_18_3607(): pass

    label("Function_18_3607")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 61710, 800, 5140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3643():
        OP_9D(0xFE, 0xFAE6, 0x0, 0x1054, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3643)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_3607 end

    def Function_19_3668(): pass

    label("Function_19_3668")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch31050.itc", 0x23)
    LoadChrToIndex("chr/ch31051.itc", 0x24)
    LoadChrToIndex("chr/ch31150.itc", 0x25)
    LoadChrToIndex("chr/ch31151.itc", 0x26)
    LoadChrToIndex("chr/ch00000.itc", 0x29)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xD, 58100, 0, -73510, 0)
    SetChrPos(0xE, 58900, 0, -74710, 0)
    SetChrPos(0xF, 57170, 0, -75310, 0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 57250, 0, -52700, 90)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(58100, 1200, -68860, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(58100, 1200, -73860, 1500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0xD,
        "#3501564V#11PThere they are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501565V#11PThe intruders!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(58000, 1200, -51840, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501566V#0010F#5PThey found us...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#3501567V#0007F#11PKeA, get back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3501568V#5801F#6POkie dokie!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x133, 3, 0, 21)
    Sleep(200)
    OP_93(0x101, 0xB4, 0x12C)
    WaitChrThread(0x133, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3989")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Jump("loc_39B0")

    label("loc_3989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_399F")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_39B0")

    label("loc_399F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_39B0")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_39B0")

    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_39EE")

    ChrTalk(
        0x102,
        "#3501569V#0107F#5PHere they come!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A58")

    label("loc_39EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3A27")

    ChrTalk(
        0x103,
        "#3501570V#0201F#5PPrepare yourselves!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A58")

    label("loc_3A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3A58")

    ChrTalk(
        0x104,
        "#3501571V#0307F#5PGet ready, guys!\x02",
    )

    CloseMessageWindow()

    label("loc_3A58")

    OP_68(57960, 1200, -53640, 1300)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xD, 58100, 0, -60510, 0)
    SetChrPos(0xE, 58900, 0, -61710, 0)
    SetChrPos(0xF, 57170, 0, -62310, 0)

    def lambda_3AB9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3AB9)
    Sleep(100)

    def lambda_3AD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3AD1)
    Sleep(100)

    def lambda_3AE9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3AE9)
    Sleep(800)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    Call(0, 20)
    Return()

    # Function_19_3668 end

    def Function_20_3B26(): pass

    label("Function_20_3B26")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 57950, 0, -52700, 180)
    SetChrPos(0xEF, 58860, 0, -52240, 180)
    SetChrPos(0x105, 57560, 0, -50980, 180)
    SetChrPos(0x133, 56620, 0, -49950, 180)
    Call(0, 11)
    OP_68(57960, 1200, -53640, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(18290, 2500)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501572V#0010F#5PThey're down!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(58380, 1200, -50320, 1500)
    MoveCamera(38, 19, 0, 1500)

    def lambda_3C59():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C59)

    def lambda_3C66():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3C66)
    Sleep(100)

    def lambda_3C76():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C76)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3501573V#0001F#11PKeA, are you all right?!\x02",
    )

    CloseMessageWindow()

    def lambda_3CC2():

        label("loc_3CC2")

        TurnDirection(0x101, 0x133, 500)
        Yield()
        Jump("loc_3CC2")

    QueueWorkItem2(0x101, 1, lambda_3CC2)

    def lambda_3CD4():

        label("loc_3CD4")

        TurnDirection(0xEF, 0x133, 500)
        Yield()
        Jump("loc_3CD4")

    QueueWorkItem2(0xEF, 1, lambda_3CD4)

    def lambda_3CE6():

        label("loc_3CE6")

        TurnDirection(0x105, 0x133, 500)
        Yield()
        Jump("loc_3CE6")

    QueueWorkItem2(0x105, 1, lambda_3CE6)
    OP_68(58380, 1200, -51450, 1000)
    BeginChrThread(0x133, 3, 0, 22)
    WaitChrThread(0x133, 3)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x133,
        (
            "#3501574V#5810F#6PYeah, I'm great!\x02\x03",
            "#3501575V#5809FI've never been better!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501576V#0002F#11PI'm glad.\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(250)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#3501577V#0404F#5PHaha, quite the brave girl we've got\x01",
            "here.\x02\x03",
            "#3501578V#0400FWith luck, we'll be able to shake them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3E8E")

    ChrTalk(
        0x102,
        "#3501579V#0101F#11PLet's hurry, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFF")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3ECC")

    ChrTalk(
        0x103,
        "#3501580V#0201F#11PTime is of the essence!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFF")

    label("loc_3ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3EFF")

    ChrTalk(
        0x104,
        "#3501581V#0301F#11PNo time to waste!\x02",
    )

    CloseMessageWindow()

    label("loc_3EFF")

    Sleep(150)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    SetChrPos(0x0, 57210, 0, -54060, 180)
    SetScenarioFlags(0xA6, 6)
    EventEnd(0x5)
    Return()

    # Function_20_3B26 end

    def Function_21_3F28(): pass

    label("Function_21_3F28")


    def lambda_3F2D():
        OP_95(0xFE, 56620, 0, -52700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F2D)
    WaitChrThread(0xFE, 1)

    def lambda_3F4B():
        OP_95(0xFE, 56620, 0, -49950, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F4B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_3F28 end

    def Function_22_3F6C(): pass

    label("Function_22_3F6C")


    def lambda_3F71():
        OP_95(0xFE, 57250, 0, -52700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F71)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_22_3F6C end

    def Function_23_3F92(): pass

    label("Function_23_3F92")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("apl/ch50371.itc", 0x20)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -58000, 0, -4970, 0)
    SetChrPos(0xEF, -58350, 0, -4920, 0)
    SetChrPos(0x105, -57990, 0, -6140, 0)
    SetChrPos(0x133, -52560, 0, -2430, 0)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -59700, 0, 8000, 180)
    SetChrFlags(0x10, 0x8000)
    VolumeBGM(0x32, 0x7D0)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, -1480, 4000)

    def lambda_406F():
        OP_95(0xFE, -58000, 0, -1860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_406F)
    Sleep(800)

    def lambda_408C():
        OP_95(0xFE, -58680, 0, -2920, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_408C)
    Sleep(300)

    def lambda_40A9():
        OP_95(0xFE, -57580, 0, -3520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40A9)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FD7")

    ChrTalk(
        0x101,
        "#3501617V#0005F#6PWhat was this place again?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_415E")

    ChrTalk(
        0x102,
        "#3501618V#0101F#6PWasn't it Speaker Hartmann's private quarters?\x02",
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_415E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_41BB")

    ChrTalk(
        0x103,
        (
            "#3501619V#0201F#6PI assume this is Speaker Hartmann's private\x01",
            "quarters...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_421D")

    label("loc_41BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_421D")

    ChrTalk(
        0x104,
        (
            "#3501620V#0305F#1PDidn't they say this was the speaker's\x01",
            "private room or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421D")


    ChrTalk(
        0x105,
        "#3501621V#0402F#6PTalk about an extravagant room.\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#3501622V#0404F#6P...Though it seems someone beat us\x01",
            "to the punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501632V#0005F#6PWazy, what do you mean...?\x02",
    )

    CloseMessageWindow()
    OP_68(-57830, 1200, 4080, 2000)
    OP_6F(0x1)

    NpcTalk(
        0x10,
        "Carefree Voice",
        "#3501624V#11PWhy'd you have to go and notice me?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Carefree Voice",
        (
            "#3501625V#11PI went through a lot of pain to try and\x01",
            "surprise you guys, and now it's ruined.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_43ED():

        label("loc_43ED")

        TurnDirection(0x101, 0x10, 500)
        Yield()
        Jump("loc_43ED")

    QueueWorkItem2(0x101, 1, lambda_43ED)

    def lambda_43FF():

        label("loc_43FF")

        TurnDirection(0xEF, 0x10, 500)
        Yield()
        Jump("loc_43FF")

    QueueWorkItem2(0xEF, 1, lambda_43FF)

    def lambda_4411():

        label("loc_4411")

        TurnDirection(0x105, 0x10, 500)
        Yield()
        Jump("loc_4411")

    QueueWorkItem2(0x105, 1, lambda_4411)

    def lambda_4423():
        OP_95(0xFE, -61300, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4423)
    WaitChrThread(0x10, 1)
    OP_68(-58780, 1200, -1460, 4000)
    OP_93(0x10, 0x87, 0x1F4)

    def lambda_4459():
        OP_96(0xFE, 0xFFFF138E, 0x0, 0x2DA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4459)
    WaitChrThread(0x10, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3501626V#0011F#6PLechter?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_44DB")

    ChrTalk(
        0x102,
        "#3501627V#0105F#6PWh-Why are you here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4557")

    label("loc_44DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4519")

    ChrTalk(
        0x103,
        "#3501628V#0205F#6PWhat are you doing here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4557")

    label("loc_4519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4557")

    ChrTalk(
        0x104,
        "#3501629V#0301F#6PHid yourself pretty well, eh?\x02",
    )

    CloseMessageWindow()

    label("loc_4557")

    OP_68(-58540, 1200, -1840, 1500)

    def lambda_456D():
        OP_95(0xFE, -59360, 0, -570, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_456D)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    ChrTalk(
        0x10,
        (
            "#3501630V#3505F#5POh, would you look at that...\x02\x03",
            "#3501631V#3504FYou guys went and caught yourself a\x01",
            "pretty impressive fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501623V#0005F#6PFish...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#3501633V#5805F#12PBy fish, are you talking about me?\x02\x03",
            "#3501634V#5801FOh, no. Are you going to eat me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501635V#3502F#5PI am! I'm going to gobble you from\x01",
            "head to toe in one bite!\x02\x03",
            "#3501636V#3509FGet ready! Here I come!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A6(0x10, 0x14, 0x14, 0x190, 0x7D0)
    Sleep(300)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x10, 0x0, 0x3E8)
    Sleep(500)
    OP_93(0x10, 0x10E, 0x3E8)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#3501637V#3507F#11PAh, shoot! I got something stuck\x01",
            "in my throat!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#3501638V#5809F#12PHeeheehee! What a weirdo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501639V#0006F#6PA good observation, KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#3501640V#0404F#6PHaha, you all have quite a lot of odd\x01",
            "acquaintances, don't you? That Yin,\x01",
            "the IBC CEO's daughter...\x02\x03",
            "#3501641V#0402FIs the SSS THAT magnetic or what?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48B4():
        TurnDirection(0xFE, 0x105, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48B4)
    Sleep(50)

    def lambda_48C4():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_48C4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#3501642V#0013F#11PI'd prefer it if we weren't, actually...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_497E")

    ChrTalk(
        0x102,
        (
            "#3501643V#0111F#5PYou have just as many strange friends\x01",
            "as us, Wazy. Maybe even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A57")

    label("loc_497E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_49F3")

    ChrTalk(
        0x103,
        (
            "#3501644V#0211F#5PI find his statement ironic when he has\x01",
            "even more outlandish friends than us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A57")

    label("loc_49F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4A57")

    ChrTalk(
        0x104,
        (
            "#3501645V#0306F#5PYou're one to talk, Wazy. You've\x01",
            "got a bunch of weird friends, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A57")

    OP_93(0x10, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x10,
        (
            "#3501646V#3506F#5PGuys, aren't you being a little too\x01",
            "calm right now?\x02\x03",
            "#3501647V#3501FLast time I checked, you guys were\x01",
            "trying to break outta here! Don't you\x01",
            "feel the slightest bit nervous?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_4B5D():
        TurnDirection(0xFE, 0x10, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B5D)

    def lambda_4B6A():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4B6A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        (
            "#3501648V#0012F#6PI really wasn't expecting Lechter to be\x01",
            "the voice of reason in this mess...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-58780, 1200, -2750, 1500)
    OP_6F(0x1)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -57500, -1000, -8000, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0x12,
        "Man's Voice",
        "#3501649V#2P#2SHey, did you find them yet?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4CA9():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CA9)

    def lambda_4CB6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4CB6)
    Sleep(100)

    def lambda_4CC6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4CC6)

    def lambda_4CD3():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4CD3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)

    NpcTalk(
        0x12,
        "Man's Voice",
        (
            "#3501650V#2P#2SI've completely scoured the right wing!\x01",
            "All we have to cover is the left!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x12,
        "Man's Voice",
        "#3501651V#2P#2SMake sure to check the speaker's room, too!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_68(-58780, 1200, -1840, 1000)

    def lambda_4DC1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4DC1)
    Sleep(100)

    def lambda_4DD1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4DD1)

    def lambda_4DDE():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4DDE)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3501652V#0010F#11PWe've got trouble...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501653V#3505F#5PWhat are you guys hanging around here for?\x02\x03",
            "#3501654V#3504FDon't you remember where I was hiding?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 500)

    ChrTalk(
        0x101,
        "#3501655V#0005F#6PLechter...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4F49")

    ChrTalk(
        0x102,
        "#3501656V#0101F#6PThere's no time for hesitation, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FD7")

    label("loc_4F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4F94")

    ChrTalk(
        0x103,
        "#3501657V#0201F#6PWe do not have time to be indecisive!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FD7")

    label("loc_4F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4FD7")

    ChrTalk(
        0x104,
        "#3501658V#0301F#6PNo time to think things over, man!\x02",
    )

    CloseMessageWindow()

    label("loc_4FD7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, -57000, 0, 8000, 180)
    SetChrPos(0xEF, -58000, 0, 8000, 180)
    SetChrPos(0x105, -59000, 0, 8000, 180)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xD, -58000, 0, -5900, 0)
    SetChrPos(0xE, -58000, 0, -5900, 0)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -61000, 0, 4000, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_68(-58000, 1200, 3580, 0)
    MoveCamera(322, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(-58000, 1200, -280, 4000)
    BeginChrThread(0x10, 3, 0, 24)
    Sleep(2000)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x10, 3)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#3501659V#6POh, hello, Mr. Arundel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501660V#3504F#11PYo! Good work patrolling the place, guys.\x02\x03",
            "#3501661V#3500FI heard some kooks broke into the auction.\x01",
            "Catch them yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3501662V#6PNot yet, but it's only a matter of time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3501663V#6PWhat exactly were you doing in\x01",
            "here, Mr. Arundel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501664V#3503F#11POh, me? I just heard some crazy noises\x01",
            "in here and decided to do some snooping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501665V#6PCrazy noises...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3501666V#6PCould that have been the intruders?!\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, 3280, 1500)
    OP_93(0x10, 0x0, 0x12C)
    OP_6F(0x1)

    ChrTalk(
        0x10,
        (
            "#3501667V#3509F#6PHeeeey, c'mon out.\x02\x03",
            "#3501668VThere's no need to be shy, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501669V#0013F#11P(What does he think he's doing...?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_541F")

    ChrTalk(
        0x102,
        (
            "#3501670V#0108F#11P(Did he intend to hand us over from\x01",
            "the start?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F1")

    label("loc_541F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5491")

    ChrTalk(
        0x103,
        (
            "#3501671V#0208F#11P(He must have planned to hand us over\x01",
            "the moment we stepped into the room.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54F1")

    label("loc_5491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_54F1")

    ChrTalk(
        0x104,
        (
            "#3501672V#0310F#11P(Damn it! Did he plan to sell us out from\x01",
            "the very beginnin'?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F1")


    ChrTalk(
        0x105,
        "#3501673V#0404F#5P(No, be patient.)\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(823, 0, 100, 0)
    Sleep(300)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x11, -57150, 0, 2300, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_68(-58000, 1200, 1000, 3500)

    def lambda_5589():

        label("loc_5589")

        TurnDirection(0x10, 0x11, 500)
        Yield()
        Jump("loc_5589")

    QueueWorkItem2(0x10, 1, lambda_5589)

    def lambda_559B():
        OP_95(0xFE, -57000, 0, 1000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_559B)

    def lambda_55B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_55B5)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x11, 2)
    OP_93(0x11, 0x10E, 0x1F4)
    EndChrThread(0x10, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0xD,
        "#3501674V#6PA...cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501675V#3500F#5PHey, Noire! What the heck are you\x01",
            "being a scaredy-cat for?\x02\x03",
            "#3501676VEverything's all right, girl.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x11, -57200, 0, 1000, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrSubChip(0x10, 0x1)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#3501677V#3509F#5PPsst, psst! You must have some bad\x01",
            "memories of being chased by some\x01",
            "big bad dogs, huh?\x02\x03",
            "#3501678V#3507FWell, you can file all your complaints\x01",
            "with these gentlemen here!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    OP_68(-58000, 1200, 0, 1200)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_6F(0x1)
    Sound(823, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#3501679V#6PUgh, false alarm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501680V#6PExcuse us!\x02",
    )

    CloseMessageWindow()

    def lambda_57D0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_57D0)
    Sleep(100)

    def lambda_57E0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_57E0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0x10,
        (
            "#3501681V#3505F#11POh, hold on a second. I just remembered\x01",
            "something important.\x02\x03",
            "#3501682V#3510FI could've sworn I saw some shady people\x01",
            "hanging outside that window just now, but...\x02\x03",
            "#3501683VHmm, I'm not positive if it was the people\x01",
            "you were looking for or not... Maybe it was?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5948():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5948)
    Sleep(50)

    def lambda_5958():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5958)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0xD,
        "#3501684V#6PYou aren't pulling our leg, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501685V#6PCan you describe them?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#3501686V#3503F#11PI THINK that they had a younger girl\x01",
            "with them, but I could be wrong.\x02\x03",
            "#3501687V#3501FDoes that mean the intruders escaped\x01",
            "to the back courtyard?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A76():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A76)
    Sleep(100)

    def lambda_5A86():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5A86)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0xD,
        (
            "#3501688V#11PThat matches witness testimonies\x01",
            "word for word!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3501689V#6PCrap... How and when did they\x01",
            "get outta the mansion?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501690V#6PWe gotta tell the boss about this!\x02",
    )

    CloseMessageWindow()
    OP_68(-58000, 1200, -1500, 2000)
    BeginChrThread(0xE, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 27)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x10, 0x5)
    SetChrSubChip(0x10, 0x0)
    Sound(820, 0, 100, 0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()
    Sleep(1000)
    OP_68(-56670, 1200, 1310, 5000)

    def lambda_5BD5():

        label("loc_5BD5")

        TurnDirection(0x10, 0x101, 500)
        Yield()
        Jump("loc_5BD5")

    QueueWorkItem2(0x10, 1, lambda_5BD5)

    def lambda_5BE7():

        label("loc_5BE7")

        TurnDirection(0x11, 0x101, 500)
        Yield()
        Jump("loc_5BE7")

    QueueWorkItem2(0x11, 1, lambda_5BE7)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0xEF, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 31)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0x105,
        "#3501691V#0402F#12PBravo. A splendid performance.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5CB7")

    ChrTalk(
        0x102,
        (
            "#3501692V#0111F#12PDid you know the cat was there\x01",
            "from the very beginning?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D7D")

    label("loc_5CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5D1B")

    ChrTalk(
        0x103,
        (
            "#3501693V#0211F#12PYou had that cat prepared before\x01",
            "the situation even unfolded?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D7D")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5D7D")

    ChrTalk(
        0x104,
        (
            "#3501694V#0302F#12PAre you tellin' me you banked your\x01",
            "entire lie on a freakin' cat?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D7D")


    ChrTalk(
        0x10,
        (
            "#3501695V#3504F#5PCan't say I know what you're talking about.\x02\x03",
            "#3501696V#3505FHuh? How did the intruders from the\x01",
            "back courtyard get in here?\x02\x03",
            "#3501697V#3509FThe world's a crazy place, I tell ya.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#3501698V#5809F#11PHeeheehee! You really ARE a weirdo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501699V#0012F#12PHaha... You really saved our skins, Lechter.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3501700V#0000F#5PBecause of Lechter's bit of misdirection,\x01",
            "the front door might be short on guards.\x02\x03",
            "#3501701VEveryone, it's now or never! Let's head\x01",
            "for the entrance, ASAP!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5FBA")

    ChrTalk(
        0x102,
        "#3501702V#0100F#12PAll right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_601B")

    label("loc_5FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5FE7")

    ChrTalk(
        0x103,
        "#3501703V#0202F#12PRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_601B")

    label("loc_5FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_601B")

    ChrTalk(
        0x104,
        "#3501704V#0300F#12PLet's get it done!\x02",
    )

    CloseMessageWindow()

    label("loc_601B")

    OP_57(0x0)
    SetCameraDistance(18750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -58000, 0, 0, 180)
    SetChrPos(0x10, -54030, 0, 6580, 90)
    SetChrPos(0x11, -52930, 0, 6580, 270)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0xA7, 2)
    OP_29(0x47, 0x1, 0x11)
    VolumeBGM(0x64, 0xBB8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_3F92 end

    def Function_24_6087(): pass

    label("Function_24_6087")

    SetChrPos(0x10, -61000, 0, 4000, 180)

    def lambda_609D():
        OP_95(0xFE, -61000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_609D)
    WaitChrThread(0xFE, 1)

    def lambda_60BB():
        OP_95(0xFE, -58000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60BB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_24_6087 end

    def Function_25_60DC(): pass

    label("Function_25_60DC")


    def lambda_60E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60E1)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58000, 0, -2240, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_25_60DC end

    def Function_26_6121(): pass

    label("Function_26_6121")


    def lambda_6126():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6126)
    OP_95(0xFE, -57980, 0, -4080, 4000, 0x1)
    OP_95(0xFE, -58360, 0, -3500, 4000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_6121 end

    def Function_27_6166(): pass

    label("Function_27_6166")


    def lambda_616B():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_616B)
    Sleep(500)

    def lambda_6188():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6188)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_6166 end

    def Function_28_619D(): pass

    label("Function_28_619D")

    OP_93(0xFE, 0xB4, 0x320)

    def lambda_61A9():
        OP_95(0xFE, -58000, 0, -5900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A9)
    Sleep(300)

    def lambda_61C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61C6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_619D end

    def Function_29_61DB(): pass

    label("Function_29_61DB")


    def lambda_61E0():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61E0)
    WaitChrThread(0xFE, 1)

    def lambda_61FE():
        OP_95(0xFE, -55680, 0, 1190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61FE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_29_61DB end

    def Function_30_621F(): pass

    label("Function_30_621F")


    def lambda_6224():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6224)
    WaitChrThread(0xFE, 1)

    def lambda_6242():
        OP_95(0xFE, -54290, 0, 200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6242)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_30_621F end

    def Function_31_6263(): pass

    label("Function_31_6263")


    def lambda_6268():
        OP_95(0xFE, -54690, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6268)
    WaitChrThread(0xFE, 1)

    def lambda_6286():
        OP_95(0xFE, -54730, 0, 2230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6286)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_6263 end

    def Function_32_62A7(): pass

    label("Function_32_62A7")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#5103FThere's something about that room...\x02\x03",
            "#5101FWell, we don't have much time. For now,\x01",
            "let's focus on investigating it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 58000, 0, -4000, 0)
    EventEnd(0x4)
    Return()

    # Function_32_62A7 end

    SaveToFile()

Try(main)
