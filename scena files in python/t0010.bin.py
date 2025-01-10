from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0010.bin",                # FileName
        "t0010",                    # MapName
        "t0010",                    # Location
        0x0038,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 56, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0010",                  # 0
        "Chief Tolta",            # 1
        "Ena",                    # 2
        "Millia",                 # 3
        "Donald",                 # 4
        "Ange",                   # 5
        "Harold",                 # 6
    ))

    AddCharChip((
        "chr/ch23702.itc",                   # 00
        "chr/ch24002.itc",                   # 01
        "chr/ch24100.itc",                   # 02
        "chr/ch24202.itc",                   # 03
        "chr/ch24300.itc",                   # 04
        "chr/ch24302.itc",                   # 05
        "chr/ch24102.itc",                   # 06
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

    DeclNpc(-38479,  180,     -1779,   90,   341,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-88830,  0,       -1460,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(519,     180,     -1850,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(38409,   180,     540,     180,  469,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(33700,   0,       -2619,   204,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(73630,   0,       670,     1200,    73630,   1000,    670,     0x007C, 0,  4,  0x0000)
    DeclActor(75750,   0,       3060,    1200,    75750,   1000,    3060,    0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_240",          # 00, 0
        "Function_1_2F8",          # 01, 1
        "Function_2_4CA",          # 02, 2
        "Function_3_520",          # 03, 3
        "Function_4_540",          # 04, 4
        "Function_5_6B7",          # 05, 5
        "Function_6_1F70",         # 06, 6
        "Function_7_2EA0",         # 07, 7
        "Function_8_3B12",         # 08, 8
        "Function_9_51A9",         # 09, 9
        "Function_10_51AA",        # 0A, 10
        "Function_11_5B50",        # 0B, 11
        "Function_12_5C79",        # 0C, 12
        "Function_13_6735",        # 0D, 13
        "Function_14_6D2A",        # 0E, 14
        "Function_15_A1AE",        # 0F, 15
        "Function_16_A9A5",        # 10, 16
    ))


    def Function_0_240(): pass

    label("Function_0_240")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_280"),
        (1, "loc_28C"),
        (2, "loc_298"),
        (3, "loc_2A4"),
        (4, "loc_2B0"),
        (5, "loc_2BC"),
        (6, "loc_2C8"),
        (SWITCH_DEFAULT, "loc_2D4"),
    )


    label("loc_280")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_28C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_298")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2E0")

    label("loc_2F7")

    Return()

    # Function_0_240 end

    def Function_1_2F8(): pass

    label("Function_1_2F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_310")
    Event(0, 13)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_363")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, 38320, 180, -2250, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x4)
    Jump("loc_4AA")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_37B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3BF")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, -38500, 150, -3230, 90)
    Jump("loc_4AA")

    label("loc_3BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3D7")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_3D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_402")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_41A")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_437")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_454")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_484")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_49C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4AA")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0xA, 0x80)

    label("loc_4AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C9")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_4C9")

    Return()

    # Function_1_2F8 end

    def Function_2_4CA(): pass

    label("Function_2_4CA")

    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA")
    OP_70(0x0, 0x0)
    Jump("loc_4FE")

    label("loc_4FA")

    OP_70(0x0, 0x1E)

    label("loc_4FE")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51C")
    OP_66(0x1, 0x1)

    label("loc_51C")

    Call(0, 3)
    Return()

    # Function_2_4CA end

    def Function_3_520(): pass

    label("Function_3_520")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_53F")

    label("loc_539")

    ClearMapObjFlags(0x0, 0x4)

    label("loc_53F")

    Return()

    # Function_3_520 end

    def Function_4_540(): pass

    label("Function_4_540")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x103, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62A")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x85, 1)"), scpexpr(EXPR_END)), "loc_5C0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x103, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_625")

    label("loc_5C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_625")

    Jump("loc_6AB")

    label("loc_62A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You're really going to take that EP Cut 1?\x01",
            "Haven't the Armoricans been through enough?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6AB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_540 end

    def Function_5_6B7(): pass

    label("Function_5_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D9")
    Call(0, 12)
    Return()

    label("loc_6D9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_76D")
    Jump("loc_7B7")

    label("loc_76D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_78D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B7")

    label("loc_78D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B7")

    label("loc_7AD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(
        0xFE,
        (
            "Armorica Village, as it stands, is in its\x01",
            "most natural form. One which was\x01",
            "created by Aidios Herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm certain that by seeking unnecessary\x01",
            "development, something similar to that\x01",
            "monster attack is bound to happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not like I don't understand where\x01",
            "Derek is coming from.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9B2")

    label("loc_921")


    ChrTalk(
        0xFE,
        (
            "I know that Derek wants the villagers\x01",
            "to be able to live an abundant life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even so, as the village chief, this issue is nonnegotiable.\x02",
    )

    CloseMessageWindow()

    label("loc_9B2")

    Jump("loc_1F68")

    label("loc_9B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AA9")

    ChrTalk(
        0xFE,
        (
            "It's a fool's errand to compare Armorica\x01",
            "Village to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell City is Crossbell City, and\x01",
            "Armorica Village is Armorica Village...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Both have their forms that are given\x01",
            "by nature and by our Goddess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF6")

    ChrTalk(
        0xFE,
        (
            "I tried speaking with Derek about\x01",
            "this village's future yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, he continues to insist that\x01",
            "the village must modernize, no matter\x01",
            "the costs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bringing in so many tourists to try\x01",
            "and achieve his silly dream has\x01",
            "caused us a lot of problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What am I going to do with Derek?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C72")

    label("loc_BF6")


    ChrTalk(
        0xFE,
        (
            "For some reason, he can't accept my\x01",
            "determination to preserve this village\x01",
            "and its culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aidios, what do I do?\x02",
    )

    CloseMessageWindow()

    label("loc_C72")

    Jump("loc_1F68")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")

    ChrTalk(
        0xFE,
        (
            "Hmm... It looks like all the tourists have\x01",
            "more or less returned to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was it really such a good idea\x01",
            "to set up a food stall to attract tourists?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While it's true the village did benefit from it,\x01",
            "I can't just ignore the fact that people ended\x01",
            "up wandering onto the Ancient Battlefield, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Derek comes back, we're going to\x01",
            "sit down and have a serious conversation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB8")

    label("loc_E1F")


    ChrTalk(
        0xFE,
        (
            "Tourism brought profit to Armorica, but\x01",
            "not without trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When Derek comes back, we're going to\x01",
            "sit down and have a serious conversation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB8")

    Jump("loc_1F68")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9E")

    ChrTalk(
        0xFE,
        (
            "This year's Anniversary Festival brought in\x01",
            "many more tourists than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Derek's plan was a success, but to what end?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was this all connected to his desire to\x01",
            "modernize the village?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104C")

    label("loc_F9E")


    ChrTalk(
        0xFE,
        (
            "We'll most likely be seeing more tourists\x01",
            "today than the rest of the festival combined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could this have been connected to Derek's\x01",
            "modernization plans all along...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104C")

    Jump("loc_1F68")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A5")

    ChrTalk(
        0xFE,
        (
            "It's good to see the village so lively with\x01",
            "tourists, but how long will it actually last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, they're just tourists. Once the\x01",
            "festival comes to a close, they're all going\x01",
            "to gradually leave, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, they're a disturbance to our farmers.\x01",
            "I knew that this plan wasn't without its flaws.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1270")

    label("loc_11A5")


    ChrTalk(
        0xFE,
        (
            "The village may become livelier for a time...\x01",
            "but I have the feeling it will only be temporary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, tourists are a disturbance to our farmers.\x01",
            "I knew that this plan wasn't without its flaws.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1270")

    Jump("loc_1F68")

    label("loc_1275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(
        0xFE,
        (
            "According to Derek, the food stall has been\x01",
            "quite a hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the chief of Armorica Village and a\x01",
            "long-time producer of honey, I couldn't\x01",
            "be prouder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13C6")

    label("loc_132E")


    ChrTalk(
        0xFE,
        (
            "Apparently, our food stall has been a hit.\x01",
            "I suppose I was justified, letting Derek\x01",
            "take care of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As village chief, I couldn't be prouder.\x02",
    )

    CloseMessageWindow()

    label("loc_13C6")

    Jump("loc_1F68")

    label("loc_13CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AA")

    ChrTalk(
        0xFE,
        (
            "Derek's food stall plan seems to be\x01",
            "going smoothly so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The villagers are looking forward\x01",
            "to it as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe putting Derek in charge of it was\x01",
            "the right decision, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1534")

    label("loc_14AA")


    ChrTalk(
        0xFE,
        (
            "We'll see what happens when the Anniversary\x01",
            "Festival arrives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With so many tourists, I hope nothing\x01",
            "bad happens to the village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1534")

    Jump("loc_1F68")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A1D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1625")

    ChrTalk(
        0xFE,
        "Ah, my friends from the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, when I first met you four,\x01",
            "I never would have imagined that I'd\x01",
            "come to rely on the police so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be counting on you if something\x01",
            "else ever happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_1625")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_16FE")

    ChrTalk(
        0xFE,
        (
            "The private property that the monsters\x01",
            "are trespassing on is a gated area to\x01",
            "the southeast of the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to use whatever you find\x01",
            "in there, if it helps you resolve this\x01",
            "matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A18")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(
        0xFE,
        (
            "My son gave me a long village renewal\x01",
            "proposal earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think it's wise to go overboard,\x01",
            "forgetting our modest way of living in\x01",
            "the process...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If a food stall for the Anniversary Festival is all\x01",
            "he wants, I'm more than happy for him to run it.\x01",
            "Besides, it won't be the first time we've ran one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am curious as to what the results\x01",
            "of all this will be...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A18")

    label("loc_188E")


    ChrTalk(
        0xFE,
        (
            "Considering the current state of Crossbell City,\x01",
            "it's clear that modernizations is not always a\x01",
            "good thing. At least, that's what I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that Armorica Village will be all right,\x01",
            "continuing in its frugal nature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son, Derek, is stubbornly against\x01",
            "that idea, for whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I am curious as to what the results\x01",
            "of the Anniversary Festival will be...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A18")

    Jump("loc_1F68")

    label("loc_1A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1A")

    ChrTalk(
        0xFE,
        (
            "Since our conversation yesterday,\x01",
            "I've told the villagers they should be\x01",
            "more careful for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The beasts remain at large, correct?\x01",
            "Until they are stopped, I don't think\x01",
            "the village can truly be at peace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B92")

    label("loc_1B1A")


    ChrTalk(
        0xFE,
        (
            "The beasts remain at large, correct?\x01",
            "I reminded the villagers to remain wary\x01",
            "yesterday. I suggest you do the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B92")

    Jump("loc_1F68")

    label("loc_1B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAD")

    ChrTalk(
        0xFE,
        "Hmm, so you haven't figured anything out yet...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it DID happen nearly three weeks ago.\x01",
            "I can't blame you for having trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there have been attacks outside\x01",
            "Armorica Village, the culprits may\x01",
            "possess some level of intelligence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D54")

    label("loc_1CAD")


    ChrTalk(
        0xFE,
        (
            "Oh, and don't let the legend about the\x01",
            "divine wolves bother you. That's all\x01",
            "it is: a mere legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't let everything we talked about\x01",
            "throw you off-course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D54")

    Jump("loc_1F68")

    label("loc_1D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EAD")

    ChrTalk(
        0xFE,
        (
            "Still, an investigation? Here? Maybe I haven't\x01",
            "given the CPD enough credit. You may be a\x01",
            "match for the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The only thing I'm certain of is that it\x01",
            "took place in the dead of night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know whether you'll find relevant\x01",
            "information, but you're free to ask around\x01",
            "the village for any details.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F68")

    label("loc_1EAD")


    ChrTalk(
        0xFE,
        (
            "Most of our farmers should be home\x01",
            "by now, or at least on their way back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Quite a few of them like to eat lunch\x01",
            "at the Ash Tree Inn, by the river. Why\x01",
            "don't you go there first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F68")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_6B7 end

    def Function_6_1F70(): pass

    label("Function_6_1F70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2067")

    ChrTalk(
        0xFE,
        (
            "Tolta and Derek ended up having another\x01",
            "passionate argument yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're father and son... Why can't they\x01",
            "come to some mutual understanding?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't look like they have any\x01",
            "intention to stop any time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9C")

    label("loc_2067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_20F3")

    ChrTalk(
        0xFE,
        (
            "Tolta and Derek always get into\x01",
            "heated arguments due to their\x01",
            "conflicting ideals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They never turn out well, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E9C")

    label("loc_20F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21AB")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        (
            "The villagers always end up being worried\x01",
            "whenever my husband and son argue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you don't mind, could you please watch\x01",
            "over Derek whenever you're here?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    Jump("loc_2E9C")

    label("loc_21AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CC")

    ChrTalk(
        0xFE,
        (
            "My husband and son each have their own\x01",
            "methods, but I know both of them only have\x01",
            "the village's best interests at heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Differing opinions and ideas are always\x01",
            "going to clash to an extent, but I can't help\x01",
            "but feel conflicted about the whole thing...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2373")

    label("loc_22CC")


    ChrTalk(
        0xFE,
        (
            "As a wife and mother, I wish those two\x01",
            "would just shake hands and get along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe nothing can be done for those\x01",
            "two, given their vastly different mindsets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2373")

    Jump("loc_2E9C")

    label("loc_2378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_24EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248F")

    ChrTalk(
        0xFE,
        (
            "My husband has been rife with worry,\x01",
            "poring over the pros and cons of doing\x01",
            "this Anniversary Festival food stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought everything would be all right this\x01",
            "time, but it looks like he's going to end up\x01",
            "arguing with Derek again. Silly me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E9")

    label("loc_248F")


    ChrTalk(
        0xFE,
        (
            "I'm conflicted whenever I hear Tolta and\x01",
            "Derek arguing about something or\x01",
            "another...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E9")

    Jump("loc_2E9C")

    label("loc_24EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A9")

    ChrTalk(
        0xFE,
        (
            "On one hand, I understand my husband's\x01",
            "worries about tourists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but on the other, I am so happy that Derek is\x01",
            "trying to improve Armorica Village.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_264F")

    label("loc_25A9")


    ChrTalk(
        0xFE,
        (
            "Whatever happens, I know that Derek\x01",
            "has the qualifications and zeal to become\x01",
            "the next village chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that, in my opinion, is something to\x01",
            "be proud of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264F")

    Jump("loc_2E9C")

    label("loc_2654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2731")

    ChrTalk(
        0xFE,
        (
            "We still have four more days of the festival\x01",
            "to enjoy, and it looks to me like the crowd\x01",
            "of tourists will continue to grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should make sure and ask Gofan to give\x01",
            "them a warm welcome at the inn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9C")

    label("loc_2731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_28BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F0")

    ChrTalk(
        0xFE,
        (
            "It's been a long time since I've seen\x01",
            "Derek so passionate about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son has his own ideas\x01",
            "and plans for when he becomes the\x01",
            "next village chief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B7")

    label("loc_27F0")


    ChrTalk(
        0xFE,
        (
            "Whenever I look at how Derek is set\x01",
            "on developing the village for the better,\x01",
            "I can't help but feel relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son has his own ideas\x01",
            "and plans for when he becomes the\x01",
            "next village chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B7")

    Jump("loc_2E9C")

    label("loc_28BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A5F")

    ChrTalk(
        0xFE,
        (
            "Derek and Tolta don't get along too\x01",
            "well, nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As the current village chief, my husband\x01",
            "cherishes Armorica and is determined to\x01",
            "protect it from any unnecessary changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But as his successor, Derek wants to modernize\x01",
            "Armorica in order to give the villagers an easier,\x01",
            "more convenient life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Neither of them are technically in the\x01",
            "wrong, so it's been a difficult issue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B2A")

    label("loc_2A5F")


    ChrTalk(
        0xFE,
        (
            "I swear, those two would rather keep fighting\x01",
            "than try to understand each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Is there a good way to mediate between\x01",
            "a bickering father and son? If there is, I would\x01",
            "love to hear it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2A")

    Jump("loc_2E9C")

    label("loc_2B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0xFE,
        (
            "I heard that the wolf-like monsters have\x01",
            "attacked other places, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They could even return here and attack\x01",
            "our village again. Just the thought sends\x01",
            "shivers down my spine. *shudder*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C6A")

    label("loc_2C0B")


    ChrTalk(
        0xFE,
        (
            "After all, they might end up attacking one\x01",
            "of the villagers... We'll have to be cautious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6A")

    Jump("loc_2E9C")

    label("loc_2C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_2D17")

    ChrTalk(
        0xFE,
        (
            "The attack was quite disturbing for\x01",
            "most of the villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something like this almost never happens\x01",
            "in Armorica Village, so I can't fault them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9C")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0F")

    ChrTalk(
        0xFE,
        (
            "Just like my husband, I was fast asleep\x01",
            "while the beasts attacked. I'm sorry.\x01",
            "I wish I could be of more help to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have an idea. Why don't you ask\x01",
            "the people who live near where the\x01",
            "brunt of the damage was?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E9C")

    label("loc_2E0F")


    ChrTalk(
        0xFE,
        (
            "We mainly suffered damages to the\x01",
            "apiary, livestock, and crops...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I recommend you ask the people in\x01",
            "charge of those more about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9C")

    TalkEnd(0xFE)
    Return()

    # Function_6_1F70 end

    def Function_7_2EA0(): pass

    label("Function_7_2EA0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F34")
    Jump("loc_2F7E")

    label("loc_2F34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7E")

    label("loc_2F54")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F74")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7E")

    label("loc_2F74")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F7E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_30B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3079")

    ChrTalk(
        0xFE,
        (
            "We harvested a bit too many veggies\x01",
            "yesterday, so Elkin and I are going to\x01",
            "try to sell them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't get many chances to ride in the\x01",
            "truck, so I'm pretty excited, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30B4")

    label("loc_3079")


    ChrTalk(
        0xFE,
        (
            "Still, Elkin is taking forever to check on\x01",
            "the truck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B4")

    Jump("loc_3B0A")

    label("loc_30B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3164")

    ChrTalk(
        0xFE,
        (
            "Hmm... Should I make lunch before\x01",
            "heading to work today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotten tired of eating at the Ash Tree Inn\x01",
            "every day, so something new would be fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0A")

    label("loc_3164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_32EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3264")

    ChrTalk(
        0xFE,
        (
            "My brother Elkin cannot control his\x01",
            "accent whenever he gets excited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That accent used to be pretty prevalent\x01",
            "in Armorica in the past, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nowadays, old man Donald and Elkin\x01",
            "are the only ones that really use it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32EA")

    label("loc_3264")


    ChrTalk(
        0xFE,
        (
            "When Elkin was a kid, he'd always\x01",
            "be hanging out with Donald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess Elkin picked up his speech\x01",
            "patterns without noticing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EA")

    Jump("loc_3B0A")

    label("loc_32EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32FD")
    Jump("loc_3B0A")

    label("loc_32FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_330B")
    Jump("loc_3B0A")

    label("loc_330B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3319")
    Jump("loc_3B0A")

    label("loc_3319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3327")
    Jump("loc_3B0A")

    label("loc_3327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_33DC")

    ChrTalk(
        0xFE,
        (
            "The village has really started getting\x01",
            "their festival preparations going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, wait, that includes me, too. Guess\x01",
            "I should go find something I can help with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0A")

    label("loc_33DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_34DD")

    ChrTalk(
        0xFE,
        (
            "My brother Elkin's true weakness is his\x01",
            "love for orbal vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He basically keeps the village's truck to\x01",
            "himself, even though the villagers all pitched\x01",
            "in to buy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, no one ever complains about it,\x01",
            "so I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0A")

    label("loc_34DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_367E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3604")

    ChrTalk(
        0xFE,
        (
            "Did you see all those boxes lined up\x01",
            "in the apiary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those are artificial beehives. Plop a\x01",
            "group of bees in there and you'll have\x01",
            "a hive and sweet honey in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try not to mess around with them, though.\x01",
            "It's not my fault if you end up getting stung.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3679")

    label("loc_3604")


    ChrTalk(
        0xFE,
        (
            "You'll find a nasty swarm of bees inside\x01",
            "our artificial beehives. Don't go touching\x01",
            "them all willy-nilly, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3679")

    Jump("loc_3B0A")

    label("loc_367E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_37EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377F")

    ChrTalk(
        0xFE,
        (
            "Derek, who works the apiaries, is\x01",
            "kinda...well, he's a good guy, but way\x01",
            "too serious sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since he's the chief's son, I guess he\x01",
            "feels some sense of responsibility, but\x01",
            "he could really stand to loosen up a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37E6")

    label("loc_377F")


    ChrTalk(
        0xFE,
        (
            "Armorica Village is a quiet place. I think\x01",
            "we should take things slowly and live a\x01",
            "relaxing life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E6")

    Jump("loc_3B0A")

    label("loc_37EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_397B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E7")

    ChrTalk(
        0xFE,
        (
            "Farm work requires love and dedication.\x01",
            "We make sure to treat every single crop\x01",
            "like it was a child of ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When our fields were hit by the attack...\x01",
            "I'm sure you can imagine how much that\x01",
            "hurt the village, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3976")

    label("loc_38E7")


    ChrTalk(
        0xFE,
        (
            "Our little crops that we worked\x01",
            "so hard to raise, destroyed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To us, it was like finding out our very\x01",
            "own children had gotten hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3976")

    Jump("loc_3B0A")

    label("loc_397B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A77")

    ChrTalk(
        0xFE,
        (
            "The magnificent views you can find\x01",
            "here are, in my opinion, some of the\x01",
            "best treats Armorica has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whew, I'm getting sleepy. I wonder if\x01",
            "anyone would notice if I snuck into the\x01",
            "barn and took a quick nap...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B0A")

    label("loc_3A77")


    ChrTalk(
        0xFE,
        (
            "Maybe I'll sneak into the barn and take\x01",
            "a short nap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If Derek found out, he'd probably\x01",
            "end up scolding me, so maybe it's\x01",
            "not worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_2EA0 end

    def Function_8_3B12(): pass

    label("Function_8_3B12")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BA6")
    Jump("loc_3BF0")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BC6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BF0")

    label("loc_3BC6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BE6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BF0")

    label("loc_3BE6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BF0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CCD")

    ChrTalk(
        0xFE,
        "You found the book, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Losin' someone else's property\x01",
            "is a lack of consideration on my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be more careful next time, I swear.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DFD")

    ChrTalk(
        0xFE,
        (
            "I lost track of the book in the apiary's shed,\x01",
            "near the front of Chief Tolta's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Last time I saw it, I was readin' in there,\x01",
            "but I haven't the foggiest idea as to when\x01",
            "it coulda disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm real sorry, folks. Would ya mind\x01",
            "searchin' for it, anyway?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E1E")
    Call(0, 15)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_3E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3F98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F42")
    SetChrSubChip(0xB, 0x0)

    ChrTalk(
        0xB,
        "Ange, dear, I can't thank ya enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're the greatest momma ever, always\x01",
            "watchin' the kids like you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Now where did that come from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You can leave the kids to me, dear. All you\x01",
            "need to focus on is doing your absolute\x01",
            "best at work, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F93")

    label("loc_3F42")


    ChrTalk(
        0xFE,
        (
            "'Cause Ange looks after our two kids,\x01",
            "I'm able to work without any worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F93")

    Jump("loc_51A1")

    label("loc_3F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B3")

    ChrTalk(
        0xFE,
        (
            "Derek, the chief's son, is tryin' his\x01",
            "damnedest to modernize the village\x01",
            "or whatever, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...to me, Armorica Village is perfect\x01",
            "just the way she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't it be downright depressin'\x01",
            "if Armorica Village became a copy\x01",
            "of Crossbell City?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4153")

    label("loc_40B3")


    ChrTalk(
        0xFE,
        (
            "In my eyes, Armorica Village is perfect\x01",
            "just the way she is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wouldn't it be downright depressin'\x01",
            "if Armorica Village became a copy\x01",
            "of Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4153")

    Jump("loc_51A1")

    label("loc_4158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41EF")

    ChrTalk(
        0xFE,
        (
            "Harvest was plentiful this year,\x01",
            "I'm happy to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet this is our reward for those\x01",
            "divine wolf imposters gettin' caught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_42AB")

    ChrTalk(
        0xFE,
        (
            "Just like most years, I worked and\x01",
            "worked and worked, and the Anniversary\x01",
            "Festival passed me by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's the life of a farmer,\x01",
            "so it don't bother me too much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_42AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4379")

    ChrTalk(
        0xFE,
        (
            "Work is done for the day, so I guess\x01",
            "I'll walk on down to the Ash Tree Inn\x01",
            "and have a few drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it's the Anniversary Festival.\x01",
            "I think I can treat myself to a lil' bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A1")

    label("loc_4379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_458D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44CF")

    ChrTalk(
        0xFE,
        (
            "It's swell and everything that the village\x01",
            "is gettin' more and more excitin' with\x01",
            "each busload of tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That said, it'd probably be best to warn 'em\x01",
            "away from the more dangerous places near\x01",
            "Armorica.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I 'specially don't want any folks goin' onto the\x01",
            "Ancient Battlefield, off of Old Armorica Road.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4588")

    label("loc_44CF")


    ChrTalk(
        0xFE,
        (
            "We gotta warn tourists to watch themselves\x01",
            "and not enter any dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I 'specially don't want any folks goin' onto the\x01",
            "Ancient Battlefield, off of Old Armorica Road.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4588")

    Jump("loc_51A1")

    label("loc_458D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BC")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I've only learned it from hearsay, but 'parently,\x01",
            "the new Arc en Ciel show was somethin' else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I got my mitts on some tickets, I woulda taken\x01",
            "a sick day and gone to see 'em in a heartbeat.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        "Is that right?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xFE,
        "Just a joke, dear.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    OP_93(0xC, 0xCC, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_475B")

    label("loc_46BC")


    ChrTalk(
        0xFE,
        "W-Well, that didn't go over well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I think that no matter who ya\x01",
            "are, as long as ya live in Crossbell,\x01",
            "you're gonna be a fan of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_475B")

    Jump("loc_51A1")

    label("loc_4760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4872")

    ChrTalk(
        0xFE,
        (
            "Once the Anniversary Festival starts,\x01",
            "tourists will begin visiting the village,\x01",
            "little by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, considerin' we're doin' a food stall\x01",
            "this year, there might be more than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, somethin' 'bout that makes me nervous.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48FF")

    label("loc_4872")


    ChrTalk(
        0xFE,
        (
            "Tourists and traders stop by every now and\x01",
            "then, but never more than one or two. We might\x01",
            "have to mentally prepare ourselves this year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FF")

    Jump("loc_51A1")

    label("loc_4904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A0C")

    ChrTalk(
        0xFE,
        (
            "By the way, y'know that bridge that's sealed\x01",
            "off on Old Armorica Road?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Past that is the Ancient Battlefield.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That place has got a weird feelin' to it, but\x01",
            "ya gotta be careful with all those monsters\x01",
            "prowlin' around there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4B00")

    label("loc_4A0C")


    ChrTalk(
        0xFE,
        (
            "The Ancient Battlefield is a weird place,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most people avoid it 'cause of the monsters,\x01",
            "but I think you folks should be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, ya can't get there now, but if ya ever\x01",
            "get the opportunity, I would take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B00")

    Jump("loc_51A1")

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C90")

    ChrTalk(
        0xFE,
        (
            "The whole village pitched in mira to buy that\x01",
            "orbal truck parked near the village gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was real pricey, but we had to have a\x01",
            "way to transport crops to Crossbell City\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. They say stuff like that gets\x01",
            "cheaper as it becomes more common,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the time my boy can buy one for\x01",
            "himself, they had better be a bit more\x01",
            "affordable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D52")

    label("loc_4C90")


    ChrTalk(
        0xFE,
        (
            "Orbal luxuries such as cars and the like\x01",
            "are supposed to get cheaper as they\x01",
            "become more widespread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, they'll be more affordable by\x01",
            "the time my boy is old enough to buy one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D52")

    Jump("loc_51A1")

    label("loc_4D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_4F9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EBF")

    ChrTalk(
        0xFE,
        (
            "When ya think of a trader, ya usually think\x01",
            "of a guy who travels from country to country...\x01",
            "but Mr. Hayworth doesn't work that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy stays in Crossbell, doing what\x01",
            "he can to build up his business. And he's\x01",
            "a hard worker, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These days, it's not easy to find a smart\x01",
            "trader who's also a good man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F9A")

    label("loc_4EBF")


    ChrTalk(
        0xFE,
        (
            "Mr. Hayworth and I get along well enough.\x01",
            "I sometimes ask him 'bout business and\x01",
            "that kinda stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Earnin' the respect and trust of a place,\x01",
            "little by little... Traders who work like\x01",
            "that don't come by often.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F9A")

    Jump("loc_51A1")

    label("loc_4F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FC")

    ChrTalk(
        0xFE,
        (
            "Recently, our fields were ravaged by some\x01",
            "monsters. To top it off, even our livestock\x01",
            "didn't come out unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We found paw prints of some kind of canine,\x01",
            "but, whatever it is, it's not from around these\x01",
            "parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe they really were those divine wolves,\x01",
            "like the chief mentioned.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F4")
    SetScenarioFlags(0x68, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F4")

    SetScenarioFlags(0x0, 3)
    Jump("loc_5193")

    label("loc_50FC")


    ChrTalk(
        0xFE,
        (
            "Whatever kinda wolf attacked our fields isn't\x01",
            "from around these parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe they really were those divine wolves,\x01",
            "like the chief mentioned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5193")

    Jump("loc_51A1")

    label("loc_5198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_51A1")

    label("loc_51A1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_3B12 end

    def Function_9_51A9(): pass

    label("Function_9_51A9")

    Return()

    # Function_9_51A9 end

    def Function_10_51AA(): pass

    label("Function_10_51AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5321")
    TurnDirection(0xC, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5289")

    ChrTalk(
        0xFE,
        (
            "Stefan came by early in the morning\x01",
            "and he's been playing with Camille and\x01",
            "Pully ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure he'll end up eating here, too, so I'll\x01",
            "need to make more food than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_531C")

    label("loc_5289")


    ChrTalk(
        0xFE,
        (
            "Stefan and my kids get extra rowdy when\x01",
            "they all play together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to thank his mother for raising such\x01",
            "a good friend to my kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531C")

    Jump("loc_5B4C")

    label("loc_5321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_532F")
    Jump("loc_5B4C")

    label("loc_532F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53DF")

    ChrTalk(
        0xFE,
        (
            "Aretha's son, Stefan, has been playing\x01",
            "with my kids all the time recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope my kids don't get him wrapped up\x01",
            "in something silly and get him hurt.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B4C")

    label("loc_53DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5495")

    ChrTalk(
        0xFE,
        (
            "I wanted to take the kids to the Anniversary\x01",
            "Festival, but it didn't end up panning out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose it's better to be busy with work\x01",
            "than to have none at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B4C")

    label("loc_5495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_55A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5551")

    ChrTalk(
        0xFE,
        (
            "I wanted to take my kids to the festival,\x01",
            "but it didn't work out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I should have more time to rest\x01",
            "next year, so I'll work my hardest\x01",
            "until then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55A3")

    label("loc_5551")


    ChrTalk(
        0xFE,
        (
            "Next year, I'll definitely be able to take\x01",
            "them to the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A3")

    Jump("loc_5B4C")

    label("loc_55A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_55B6")
    Jump("loc_5B4C")

    label("loc_55B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5709")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5682")

    ChrTalk(
        0xFE,
        (
            "Farm work is keeping me busy, so I won't\x01",
            "be able to make the trip to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aretha and Stefan are going, since it's a\x01",
            "good opportunity to visit their old home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5704")

    label("loc_5682")


    ChrTalk(
        0xFE,
        (
            "Aretha and Stefan are going to the festival,\x01",
            "since it's a good opportunity to visit their\x01",
            "old home. Haha, I'm quite jealous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5704")

    Jump("loc_5B4C")

    label("loc_5709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_58C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5725")
    Call(0, 11)
    Jump("loc_58C1")

    label("loc_5725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5824")

    ChrTalk(
        0xFE,
        (
            "I checked with a friend who lives in\x01",
            "Crossbell City, and guess what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets for Arc en Ciel's new show are already\x01",
            "booked for the next two months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* City folks' passion for Arc en Ciel\x01",
            "is on a whole different level.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_58C1")

    label("loc_5824")


    ChrTalk(
        0xFE,
        (
            "Buying a ticket two months in advance?\x01",
            "Patience is a virtue, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All this just shows how much Arc en Ciel\x01",
            "means to the people of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C1")

    Jump("loc_5B4C")

    label("loc_58C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5B19")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58E2")
    Call(0, 11)
    Jump("loc_5B14")

    label("loc_58E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A39")

    ChrTalk(
        0xFE,
        (
            "Now that the monsters have been dealt with,\x01",
            "I can let the kids play outside by themselves\x01",
            "again without worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a farmer, I don't have the time or\x01",
            "luxury to travel outside the village\x01",
            "very often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Camille always pesters me to take\x01",
            "him and Pully to the Anniversary Festival...\x01",
            "It's a bit hard to deal with.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5B14")

    label("loc_5A39")


    ChrTalk(
        0xFE,
        (
            "As a farmer, I don't have the time or\x01",
            "luxury to be able to travel outside the\x01",
            "village with my kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Camille always pesters me to take\x01",
            "him and Pully to the Anniversary Festival...\x01",
            "It's a bit hard to deal with.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B14")

    Jump("loc_5B4C")

    label("loc_5B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5B27")
    Jump("loc_5B4C")

    label("loc_5B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 0)), scpexpr(EXPR_END)), "loc_5B35")
    Jump("loc_5B4C")

    label("loc_5B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 6)), scpexpr(EXPR_END)), "loc_5B43")
    Jump("loc_5B4C")

    label("loc_5B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5B4C")

    label("loc_5B4C")

    TalkEnd(0xFE)
    Return()

    # Function_10_51AA end

    def Function_11_5B50(): pass

    label("Function_11_5B50")


    ChrTalk(
        0xFE,
        (
            "I'm in the middle of making a carbonara.\x01",
            "My entire family can't get enough of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should try making one for yourself\x01",
            "sometime. Here, try memorizing this.\x02",
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1AC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xA)
    Return()

    # Function_11_5B50 end

    def Function_12_5C79(): pass

    label("Function_12_5C79")

    EventBegin(0x0)
    Fade(500)
    OP_68(-39840, 1950, -2730, 0)
    MoveCamera(325, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23700, 0)
    SetChrPos(0x101, -41000, 0, -1800, 90)
    SetChrPos(0x102, -41500, 0, -2800, 90)
    SetChrPos(0x103, -42500, 0, -800, 90)
    SetChrPos(0x104, -43250, 0, -1800, 90)
    SetChrPos(0x8, -39300, 180, -1800, 270)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#0000FLong time no see, Chief Tolta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAh, the Special Support Section!\x01",
            "Thanks for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PNews of your success in solving the monster\x01",
            "attacks reached Armorica the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PI even managed to convince some of\x01",
            "the other villagers that the police aren't\x01",
            "all bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309F'Preciate it, man.\x02\x03",
            "#0301FThis ain't the time to be singin'\x01",
            "our praises, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FIf you don't mind, could you run us\x01",
            "through the details of your request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12POhoh, I almost forgot! Before that,\x01",
            "allow me to thank you once more\x01",
            "for dealing with those beasts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PNow, then... I'll cut straight to the\x01",
            "heart of the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FThe support request mentioned something\x01",
            "about monsters trespassing onto Armorica\x01",
            "private property?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PIndeed they have.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PYou likely saw the place as you were\x01",
            "heading here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAlong Old Armorica Road, we own a\x01",
            "stretch of property that serves as a\x01",
            "storehouse for materials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PThere's been a pack of monsters that stormed\x01",
            "in recently and made the place their new nest.\x01",
            "It's caused us a whole slew of problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FA pack? I can see how that's\x01",
            "an issue for the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FAny injuries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PNot at the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHowever, we store many of our farming tools\x01",
            "over there, so we cannot continue to ignore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAnd given how well you dealt with our previous run-in\x01",
            "with monsters, I was more than happy to submit a\x01",
            "support request, rather than ask the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309FSounds like our stock is finally starting\x01",
            "to go up.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#5P#0203FWhile we should be happy about that,\x01",
            "we should probably focus on the task at hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0304FGeez, I know that... All righty, let's go\x01",
            "show these trespassers who's boss!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#5P#0001FYeah, it'd be best to finish\x01",
            "this quickly.\x02\x03",
            "Wait too long, and this pack could\x01",
            "get out of hand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6455():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6455)
    Sleep(50)

    def lambda_6465():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6465)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x8,
        (
            "#12POh, so you'll do it? I knew asking\x01",
            "the SSS for help was the right call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PHere. Take this with you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33A, 1)

    ChrTalk(
        0x8,
        (
            "#12PThat's your key to unlocking the\x01",
            "property's gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHead southeast on the old road,\x01",
            "and you'll find the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHeck, riding the bus halfway down\x01",
            "the path would save you time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PIf you find anything useful in the area,\x01",
            "I don't mind you using it. Please, just\x01",
            "take care of this for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FUnderstood. Leave it to us, Chief Tolta.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Old Road Property Monster Extermination]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -41000, 0, -1800, 90)
    OP_29(0xD, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_5C79 end

    def Function_13_6735(): pass

    label("Function_13_6735")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-39840, 1950, -2730, 0)
    MoveCamera(325, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24700, 0)
    SetChrPos(0x101, -41000, 0, -1800, 90)
    SetChrPos(0x102, -41500, 0, -2800, 90)
    SetChrPos(0x103, -42500, 0, -800, 90)
    SetChrPos(0x104, -43250, 0, -1800, 90)
    SetChrPos(0x8, -39300, 180, -1800, 270)
    SetCameraDistance(23700, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#12PI see. No more worrying about them, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PLooks like we can finally get back\x01",
            "to tending our fields in peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PIt seems I owe you my thanks once again,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0309FIt was no biggie. Stuff like that is nothin' for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0106FHonestly, you're all talk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FThere's something else, Chief Tolta. Since that property is\x01",
            "on the road, you should put up a warning sign so people\x01",
            "don't accidentally wander inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHmm, I'm sure that can be arranged. Besides,\x01",
            "I want just our villagers to enter that place\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PHowever, I can't help but notice that this\x01",
            "all started after the wolf attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PIt's almost been a month since then,\x01",
            "and yet this still happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0203FA correlation has not been confirmed,\x01",
            "but it is quite probable.\x02\x03",
            "#0200FWith our extermination, I do not think any\x01",
            "more monsters will attempt to trespass onto\x01",
            "the storehouse grounds again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12PYou think? Hearing that is music to my ears.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PAnyway, thank you. As always, I'll make sure\x01",
            "to call you if something else pops up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FYou can count on us, sir. Call us, and\x01",
            "we'll come running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FWell, if you'll excuse us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Old Road Property Monster Extermination]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -41000, 0, -1800, 90)
    OP_29(0xD, 0x1, 0x3)
    OP_29(0xD, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_13_6735 end

    def Function_14_6D2A(): pass

    label("Function_14_6D2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09300.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("apl/ch50014.itc", 0x24)
    OP_68(-44120, 1200, -2790, 0)
    MoveCamera(318, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, -40600, 0, -2700, 0)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -40600, 0, -1200, 180)
    SetChrPos(0x101, -46400, 0, -1800, 90)
    SetChrPos(0x102, -46400, 0, -3000, 90)
    SetChrPos(0x103, -47800, 0, -3000, 90)
    SetChrPos(0x104, -47800, 0, -1800, 90)
    FadeToBright(1000, 0)
    OP_68(-42120, 1200, -2790, 3000)
    OP_6F(0x1)
    OP_0D()

    NpcTalk(
        0xD,
        "Kind-Looking Man",
        (
            "#1100410V#3609F#6PIt was a pleasure doing business with you.\x02\x03",
            "#1100411V#3600FThank you for your continued support.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        "#1100412V#11PYes, and same to you.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        (
            "#1100413V#11PThough... Are you sure that price\x01",
            "is good for your business?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        (
            "#1100414V#11PIt's 20 percent more than what\x01",
            "other traders paid.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Kind-Looking Man",
        (
            "#1100415V#3604F#6PI assure you, they're well worth the price.\x01",
            "Given the praises sung about Armorica's\x01",
            "goods, I think they'll prove quite profitable.\x02\x03",
            "#1100416V#3600FThere's no need to fret over my endeavors.\x01",
            "I'll break even, somehow.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        (
            "#1100417V#11PConfident as ever. Always a pleasure to\x01",
            "work with you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        (
            "#1100418V#11PPlease, bring your beautiful wife and son\x01",
            "with you to the village next time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        "#1100419V#11PThey're more than welcome here.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Kind-Looking Man",
        (
            "#1100420V#3609F#6PHaha. I think I'll do just that.\x02\x03",
            "#1100421V#3600FTake care. I'll be sure to come again.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        "#1100422V#11PYes, until next time.\x02",
    )

    CloseMessageWindow()

    def lambda_7233():

        label("loc_7233")

        TurnDirection(0x8, 0xD, 500)
        Yield()
        Jump("loc_7233")

    QueueWorkItem2(0x8, 1, lambda_7233)
    OP_93(0xD, 0x10E, 0x12C)
    OP_68(-44550, 1200, -2490, 2000)

    def lambda_725D():
        OP_95(0xFE, -43890, 0, -1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_725D)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0xD,
        "Kind-Looking Man",
        "#1100423V#3605FOh, pardon me...\x02",
    )

    CloseMessageWindow()
    OP_68(-45790, 1200, -1120, 3000)

    def lambda_72D7():
        OP_96(0xFE, 0xFFFF498A, 0x0, 0xFFFFFD08, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72D7)

    def lambda_72F1():
        OP_96(0xFE, 0xFFFF461A, 0x0, 0xFFFFF9C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72F1)

    def lambda_730B():
        OP_96(0xFE, 0xFFFF41D8, 0x0, 0xFFFFF434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_730B)

    def lambda_7325():
        OP_96(0xFE, 0xFFFF4296, 0x0, 0xFFFFF966, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7325)

    def lambda_733F():

        label("loc_733F")

        TurnDirection(0x101, 0xD, 500)
        Yield()
        Jump("loc_733F")

    QueueWorkItem2(0x101, 1, lambda_733F)

    def lambda_7351():

        label("loc_7351")

        TurnDirection(0x102, 0xD, 500)
        Yield()
        Jump("loc_7351")

    QueueWorkItem2(0x102, 1, lambda_7351)

    def lambda_7363():

        label("loc_7363")

        TurnDirection(0x103, 0xD, 500)
        Yield()
        Jump("loc_7363")

    QueueWorkItem2(0x103, 1, lambda_7363)

    def lambda_7375():

        label("loc_7375")

        TurnDirection(0x104, 0xD, 500)
        Yield()
        Jump("loc_7375")

    QueueWorkItem2(0x104, 1, lambda_7375)
    OP_68(-47580, 1200, -1450, 2000)

    def lambda_7398():
        OP_95(0xFE, -46980, 0, -3680, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7398)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0xB4, 0x1F4)
    Sound(103, 0, 100, 0)

    def lambda_73C3():
        OP_95(0xFE, -47000, 0, -4530, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_73C3)

    def lambda_73DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_73DD)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    Sleep(300)
    Sound(104, 0, 100, 0)
    Sleep(700)

    ChrTalk(
        0x101,
        "#1100424V#0005F#11PThat man just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100425V#0100F#5PHe had the air of a trader about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100426V#0300F#5PSure did. He musta had some business\x01",
            "with Armorica's head honcho.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_74F5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_74F5)
    WaitChrThread(0x8, 1)

    NpcTalk(
        0x8,
        "Old Man's Voice",
        "#1100427V#1PYou all are...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7582():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7582)

    def lambda_758F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_758F)

    def lambda_759C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_759C)

    def lambda_75A9():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75A9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(-44030, 1200, -1870, 2500)

    def lambda_75D7():
        OP_96(0xFE, 0xFFFF59DE, 0x0, 0xFFFFF862, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_75D7)
    Sleep(800)

    def lambda_75F4():
        OP_96(0xFE, 0xFFFF5420, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75F4)
    Sleep(50)

    def lambda_7611():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFFB82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7611)
    Sleep(50)

    def lambda_762E():
        OP_96(0xFE, 0xFFFF4F3E, 0x0, 0xFFFFF542, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_762E)
    Sleep(50)

    def lambda_764B():
        OP_96(0xFE, 0xFFFF4A5C, 0x0, 0xFFFFF862, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_764B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1100428V#0000F#5PApologies for interrupting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100429V#0100F#5PWe're looking for the chief of the village.\x01",
            "Are you him, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        "#1100430V#2PIndeed I am.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Old Man",
        "#1100431V#2PI'm Tolta. Are you folks tourists?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100432V#0003FNo, sir.\x02\x03",
            "#1100433V#0001FWe're here to investigate the recent\x01",
            "monster attack in the village.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1100434V#2POh, I understand!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100435V#2PThe folks over at the Guardian Force\x01",
            "have stopped by a few times already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100436V#2PUnfortunately, they couldn't find any conclusive\x01",
            "leads. I'm full of confidence now that you all are\x01",
            "on the job!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x103,
        "#1100437V#0206F#5P(This optimism is strange.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100438V#5P#0306F(Yup. Same misunderstanding as usual.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100439V#5P#0106F(I've moved past the point of being\x01",
            "surprised now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100440V#0006F#5PSorry, sir. I should have been more clear.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        "#1100441V#2PHmm? What's this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100442V#0003F#5PDespite what you're probably thinking,\x01",
            "we aren't from the Bracer Guild.\x02\x03",
            "#1100443V#0000FWe're from the Crossbell Police Department,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    OP_68(-36090, 2400, -2550, 0)
    MoveCamera(327, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -38500, 200, -1500, 90)
    SetChrPos(0x102, -38500, 200, -2800, 90)
    SetChrPos(0x103, -34300, 200, -1700, 270)
    SetChrPos(0x104, -34300, 200, -3000, 270)
    SetChrPos(0x8, -36300, 200, 100, 180)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(-36090, 1400, -2550, 3000)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#1100444V#11PI see. The Crossbell police wouldn't\x01",
            "have been my first guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100445V#11PI apologize for the misunderstanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100446V#11PThe police rarely visit this village,\x01",
            "so I wasn't really expecting this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100447V#11POn the other hand, bracers are always\x01",
            "coming and going, thanks to Arios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100448V#5P#0006FY-You don't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100449V#6P#0306FHow can one dude be so popular,\x01",
            "yet so dedicated to his job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100450V#0103F#6PBracers aside, Chief Tolta...\x02\x03",
            "#1100451V#0101FCan we get back to the reason\x01",
            "why we're here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100452V#5P#0001FIf you don't mind, could you give\x01",
            "us a rundown of the attack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100453V#11PHmm. Sure, I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100454V#11PIt happened about three weeks ago,\x01",
            "on the night of a new moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100455V#11PA pack of monsters snuck into our village,\x01",
            "laying waste to any crops they could find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100456V#11PFruit, wheat...even our livestock was hit.\x01",
            "Every household in the village was affected\x01",
            "by it, to some degree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100457V#5P#0001FAnd there were no eyewitnesses, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100458V#11PYes. Unlike the rowdy city folk, people\x01",
            "here tend to go to sleep earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100459V#11PAfter all, we get up when the rooster crows.\x01",
            "Because of that, we were all fast asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100460V#11PBy the time everyone woke up, the paw\x01",
            "prints and damage left by the monsters\x01",
            "were clear as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100461V#5P#0003FI thought as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100462V#12P#0200FCould you further expound upon why you\x01",
            "think they are wolf-like in nature...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100463V#11PAh, right. You see, the paw prints left all around\x01",
            "the village were from some kind of canine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100464V#11PFunny thing is, some CGF members were\x01",
            "scheduled to patrol the Armorica area later\x01",
            "that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100465V#11POnce we informed them about the attack,\x01",
            "they conducted a search of the perimeter,\x01",
            "just to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100466V#0103F#6PBut not a single trace of the canines was\x01",
            "found anywhere...\x02\x03",
            "#1100467V#0101FHis statement seems to line up with what\x01",
            "the CGF report described.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100468V#11PHmm, that's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100469V#11PLike I said, it's been three weeks since\x01",
            "that mess. By the Goddess' protection,\x01",
            "we haven't been hit again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100470V#11PTo be honest, I thought this was a\x01",
            "one-time issue...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100471V#11PI'm sorry to hear that other locations\x01",
            "have been attacked, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100472V#5P#0003FIt's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100473V#6P#0300FYo, I got a question. It's pretty awesome to see\x01",
            "the villagers so chill after an attack like that.\x01",
            "It's like the whole fiasco didn't faze 'em at all.\x02\x03",
            "#1100474VWeren't your losses pretty heavy?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)

    ChrTalk(
        0x8,
        "#1100475V#11PNo, it isn't as bad as you think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100476V#11PIf you count the losses per household,\x01",
            "they were relatively light.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#1100477V#5P#0005FI thought it was much worse.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#1100478V#11PThis is merely a rough estimate, but I'd wager\x01",
            "the total loss was around 100,000 mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100479V#11PStill, no matter how much I try to downplay it,\x01",
            "a loss is still a loss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100480V#11PIt was a stressful time for the village.\x01",
            "Thankfully, we were able to strike a\x01",
            "business deal that'll help us recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100481V#11PI'm happy to say most of our losses\x01",
            "have been accounted for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100482V#5P#0005FA business deal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100483V#12P#0205FWas it with the guest that just left?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100484V#11PIndeed. He's a trader from Crossbell City.\x01",
            "Over the past few years, we've maintained\x01",
            "a healthy business relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100485V#11PAfter hearing about the damages, he increased\x01",
            "his offers by a wide margin. Bless his soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100486V#11PYou don't see that kind of generosity\x01",
            "too often in people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100487V#0100F#6PHe sounds like a kind man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100488V#6P#0300FA trader, eh? No wonder he was in that\x01",
            "fancy getup. Gotta look the part and all,\x01",
            "y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100489V#11PYes, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100490V#11PConsidering the shape Crossbell is in, these\x01",
            "damages are the least of our worries...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100491V#5P#0005FPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100492V#0101F#6PSorry, could you explain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100493V#11PSorry. That may have been inappropriate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100494V#11PApologies, folks. Forget all that nonsense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100495V#6P#0306FGeez, you can't just tease a man like that.\x02\x03",
            "#1100496V#0301FThat's like lowerin' a slab of meat in front\x01",
            "of a dog and takin' it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100497V#0203F#12PAgreed. I do not appreciate being\x01",
            "left in the dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100498V#11PHahaha, my sincerest apologies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100499V#11PThe ramblings of an old man aren't too\x01",
            "interesting. But, are you still curious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100500V#5P#0003FYes, sir. Please, tell us everything you know.\x02\x03",
            "#1100501V#0001FAt this point, we'll take any lead we can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100502V#11PHmm... Well, if you insist.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7202", 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#1100503V#11PHave you folks ever heard of\x01",
            "the 'divine wolves'?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100504V#5P#0005FDivine...wolves?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100505V#0105F#6PAs in, holy wolves?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100506V#0200F#12PI do not believe such a term\x01",
            "exists in the database.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100507V#11PJust as I thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100508V#11PThis legend must be long lost in the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100509V#11PA shame, really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100510V#5P#0001FSorry, but what exactly is a divine wolf?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100511V#11PThe divine wolves are an ancient species\x01",
            "of beasts that reside within Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100512V#11PStories describe them as wolves with\x01",
            "fur as white as snow.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100513V#5P#0005FYou don't mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100514V#0205F#12PCould these divine wolves be the culprits\x01",
            "behind the village's damages?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100515V#11POf course, there's no evidence saying that\x01",
            "they're the culprits. But, personally, I would\x01",
            "not be surprised if they were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100516V#11PYou see, the old legends mention that these\x01",
            "divine wolves are not regular wolves, but\x01",
            "Holy Beasts, sent by Aidios Herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100517V#11PLong ago, this land of Crossbell was a\x01",
            "bloody place, rife with conflict...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100518V#11PWhile watching over the foolishness of man,\x01",
            "they would occasionally help the weak, if\x01",
            "they so desired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100519V#11PAt least, that's how the legend goes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100520V#0101F#6PI can't believe I had never heard this before...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100521V#5P#0008FSomething about this sounds familiar.\x01",
            "I think I read a fairy tale about a white\x01",
            "wolf when I was a little kid.\x02\x03",
            "#1100522V#0003FI'm pretty sure I borrowed the book from\x01",
            "the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100523V#11PYes. I'm sure the legend of the divine wolves\x01",
            "serves as the basis for that particular fairy tale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100524V#11PAs I'm sure you are all aware, Crossbell has undergone\x01",
            "drastic changes in the past few decades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100525V#11POnce it became the center of trade in Zemuria--\x01",
            "being influenced by both the Empire and Republic--\x01",
            "Crossbell began to leave its history in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100526V#11PAnd, with that...the divine wolves slowly vanished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100527V#0208F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100528V#6P#0306FHuh. Guess they were just fed up with\x01",
            "man bein' dumb as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100529V#11PWell said. Those are my thoughts exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100530V#11PI believe that's why the divine wolves\x01",
            "disappeared over the course of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100531V#11PAnd if they have finally decided to return...\x01",
            "I can only think that this is an omen of\x01",
            "things to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100532V#5P#0001FWhy would you think that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100533V#11PIt may be out of my place to say...but I feel\x01",
            "that Crossbell City has been expanding too\x01",
            "rapidly and too aggressively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100534V#11PLast time I rode a bus down to visit, all\x01",
            "those changes left my jaw on the floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100535V#11PIt's as if people are so caught up living in\x01",
            "the moment, they've forgotten to remember\x01",
            "the past...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100536V#11PThat's how I see it, anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100537V#5P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100538V#0106F#6PI don't know what to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100539V#11POh, dear. I wasn't intending to lambaste\x01",
            "you folks with a sermon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100540V#11PI just think it's possible that this attack\x01",
            "might have been a warning from the\x01",
            "returning divine wolves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100541V#11PI suppose if you interpret it that way,\x01",
            "everything would make sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x8,
        (
            "#1100542V#11PBut it looks to me like you all took\x01",
            "the story a bit too seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100543V#11PPlease, ignore me. Those were nothing\x01",
            "more than the ramblings of an old man\x01",
            "who doesn't know when to stop talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100544V#5P#0004FI wouldn't dismiss yourself like that...\x01",
            "That was all valuable information, sir.\x02\x03",
            "#1100545V#0000FI think I may even be able to tackle\x01",
            "this case from a new angle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100546V#11PHmm, I guess it was worth it, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100547V#11PWell, back to the subject at hand. You came here to\x01",
            "conduct an investigation, right? Is there anything\x01",
            "I can do to assist you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100548V#5P#0000FYes, actually...\x02\x03",
            "#1100549VMay we have your permission to ask\x01",
            "the villagers about the incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100550V#11PIf it's just you four, it shouldn't\x01",
            "be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100551V#11PNoon, isn't it? Perfect. Most people should be\x01",
            "getting back from farm work right about this time.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    SetChrPos(0x0, -41820, 0, -1890, 270)
    SetChrPos(0x8, -38480, 180, -1780, 90)
    OP_4C(0x8, 0xFF)
    SetMapObjFrame(0xFF, "kage03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x1, 0x1)
    SetScenarioFlags(0x60, 5)
    OP_29(0x3F, 0x1, 0x3)
    ClearMapFlags(0x10000000)
    PlayBGM("ed7120", 0)
    EventEnd(0x5)
    Return()

    # Function_14_6D2A end

    def Function_15_A1AE(): pass

    label("Function_15_A1AE")

    EventBegin(0x0)
    Fade(500)
    OP_68(40430, 1500, -580, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23400, 0)
    SetChrPos(0x101, 40500, 0, 0, 270)
    SetChrPos(0x102, 40500, 0, 1200, 270)
    SetChrPos(0x103, 41700, 0, 0, 270)
    SetChrPos(0x104, 41700, 0, 1200, 270)
    SetChrSubChip(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A25B")
    SetChrPos(0x109, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A286")

    label("loc_A25B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A286")
    SetChrPos(0x10A, 41100, 0, -1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_A286")

    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me. Are you Donald, by any\x01",
            "chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYup, that's me. Need somethin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe're from the Crossbell Police Department.\x01",
            "Do you have a minute?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that they were collecting overdue books.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#5PHmm, so ya came about that thing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIf that's the case, you ain't gonna like\x01",
            "what I have to say.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A477")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_A477")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0005FOh. Oh, no. Surely not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FSub-sub-sub-subleasing?!\x02\x03",
            "#0306FWhat is the DEAL with people these\x01",
            "days?! Just return the damn book!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PErr, I didn't exactly lend it out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI would read it durin' downtime on the\x01",
            "farm, but my memory is kinda foggy\x01",
            "as to where I left the darn thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PI mighta lost it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A65B")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_A65B")

    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#0105FN-No way... After all this searching...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6F8")

    ChrTalk(
        0x109,
        (
            "#6P#0506FWe thought subleasing was bad,\x01",
            "but it somehow got even worse...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A765")

    label("loc_A6F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A765")

    ChrTalk(
        0x10A,
        (
            "#6P#0601F(This is why rules are made, people!\x01",
            "Follow them! It's not a foreign concept!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A765")


    ChrTalk(
        0x103,
        (
            "#12P#0200FDo you have any idea where you could\x01",
            "have left it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POh, yeah. I last had it in the shed over\x01",
            "by the apiary. The one right in front of\x01",
            "the village chief's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PI was all relaxed, readin' that book there.\x01",
            "Next time I looked for it, I couldn't find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PI'm sorry for the trouble, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FNothing we can do about it now.\x02\x03",
            "#0000FIf that book is going to be anywhere, that\x01",
            "shed is our best bet. Let's go check it out\x01",
            "and put an end to this wild goose chase.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A987")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_A987")

    SetChrPos(0x0, 40500, 0, 0, 270)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_15_A1AE end

    def Function_16_A9A5(): pass

    label("Function_16_A9A5")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x2DA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2DA, 1)
    EventBegin(0x0)
    Fade(500)
    OP_68(76390, 1500, -1840, 0)
    MoveCamera(340, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23510, 0)
    SetChrPos(0x101, 75420, 0, -450, 135)
    SetChrPos(0x102, 76950, 0, -530, 225)
    SetChrPos(0x103, 75550, 0, -1930, 45)
    SetChrPos(0x104, 77080, 0, -2020, 315)
    SetChrSubChip(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA9E")
    SetChrPos(0x109, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_AAC9")

    label("loc_AA9E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAC9")
    SetChrPos(0x10A, 76640, 0, -2920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_AAC9")

    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FThere's the library's stamp.\x01",
            "This must be our overdue book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0106FPhew, that turned into quite the search.\x02\x03",
            "#0105FI can't say I was expecting it to end up\x01",
            "being an Arc en Ciel fan book, though...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABE1")

    ChrTalk(
        0x109,
        "#6P#0500FIt certainly seems in demand.\x02",
    )

    CloseMessageWindow()

    label("loc_ABE1")


    ChrTalk(
        0x104,
        (
            "#12P#0306FHey, we can't control what people want\x01",
            "to read or not. If that thing has photos in\x01",
            "it, I ESPECIALLY can't blame 'em.\x02\x03",
            "#0309FHell, I almost want to take it and give\x01",
            "it a read myself.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD03")

    ChrTalk(
        0x10A,
        "#6P#0601F*glare*...Orlando.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FC'mon. Learn to take a joke.\x02",
    )

    CloseMessageWindow()

    label("loc_AD03")


    ChrTalk(
        0x103,
        (
            "#6P#0206FYou are free to check it out...AFTER\x01",
            "we have returned it to the library.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD7F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_AD7F")

    SetChrPos(0x0, 76380, 0, -1420, 180)
    SetChrSubChip(0xB, 0x0)
    OP_29(0x28, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADBD")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_ADBD")

    OP_65(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_16_A9A5 end

    SaveToFile()

Try(main)
