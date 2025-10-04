from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c134b.bin",                # FileName
        "c134b",                    # MapName
        "c134b",                    # Location
        0x001D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 29, 0, 1, 0, 3],
    )

    BuildStringList((
        "c134b",                  # 0
        "Mr. Crois",              # 1
        "Mariabell",              # 2
        "KeA",                    # 3
        "Shizuku",                # 4
        "Elie",                   # 5
        "Tio",                    # 6
        "Randy",                  # 7
        "Dolls",                  # 8
        "Dolls",                  # 9
    ))

    AddCharChip((
        "chr/ch05602.itc",                   # 00
        "chr/ch05500.itc",                   # 01
        "apl/ch50512.itc",                   # 02
        "apl/ch50512.itc",                   # 03
        "chr/ch05502.itc",                   # 04
        "apl/ch50093.itc",                   # 05
        "chr/ch00102.itc",                   # 06
        "chr/ch00100.itc",                   # 07
        "chr/ch00200.itc",                   # 08
        "chr/ch00300.itc",                   # 09
    ))

    DeclNpc(55000,   150,     128800,  180,  261,  0x0, 0,   0,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(57799,   29,      126400,  225,  261,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(171500,  200,     123500,  270,  343,  0x0, 1,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(171500,  200,     124400,  270,  343,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(59090,   29,      121360,  0,    341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(172360,  800,     120099,  0,    374,  0x0, 3,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(172360,  800,     120800,  0,    374,  0x0, 4,   5,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  8,  0x0000)
    DeclActor(170460,  0,       122680,  1500,    171500,  1200,    123000,  0x007E, 0,  6,  0x0000)
    DeclActor(170300,  0,       125140,  1500,    171500,  1200,    124000,  0x007E, 0,  4,  0x0000)
    DeclActor(172500,  0,       121000,  1200,    172500,  1500,    121000,  0x007C, 0,  21, 0x0000)
    DeclActor(172500,  0,       120000,  1200,    172500,  1500,    120250,  0x007C, 0,  21, 0x0000)

    ScpFunction((
        "Function_0_2C4",          # 00, 0
        "Function_1_37C",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_487",          # 03, 3
        "Function_4_4CA",          # 04, 4
        "Function_5_4CE",          # 05, 5
        "Function_6_5C6",          # 06, 6
        "Function_7_5CA",          # 07, 7
        "Function_8_62A",          # 08, 8
        "Function_9_62E",          # 09, 9
        "Function_10_9F3",         # 0A, 10
        "Function_11_FBF",         # 0B, 11
        "Function_12_191B",        # 0C, 12
        "Function_13_3EB6",        # 0D, 13
        "Function_14_6683",        # 0E, 14
        "Function_15_9454",        # 0F, 15
        "Function_16_B3CD",        # 10, 16
        "Function_17_B883",        # 11, 17
        "Function_18_D3E7",        # 12, 18
        "Function_19_D41A",        # 13, 19
        "Function_20_D457",        # 14, 20
        "Function_21_D4AB",        # 15, 21
    ))


    def Function_0_2C4(): pass

    label("Function_0_2C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_304"),
        (1, "loc_310"),
        (2, "loc_31C"),
        (3, "loc_328"),
        (4, "loc_334"),
        (5, "loc_340"),
        (6, "loc_34C"),
        (SWITCH_DEFAULT, "loc_358"),
    )


    label("loc_304")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_310")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_31C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_328")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_334")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_340")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_358")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_37B")

    Return()

    # Function_0_2C4 end

    def Function_1_37C(): pass

    label("Function_1_37C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_394")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    Event(0, 17)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 15)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_3CB")
    Jump("loc_47F")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_47F")

    label("loc_448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47F")

    label("loc_466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xE, 0x80)

    label("loc_47F")

    Return()

    # Function_1_37C end

    def Function_2_480(): pass

    label("Function_2_480")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_480 end

    def Function_3_487(): pass

    label("Function_3_487")

    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_487 end

    def Function_4_4CA(): pass

    label("Function_4_4CA")

    Call(0, 5)
    Return()

    # Function_4_4CA end

    def Function_5_4CE(): pass

    label("Function_5_4CE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_578")

    ChrTalk(
        0xB,
        "#1503F#40WZzz... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Oh, thank Aidios. They're safe and sound...)\x02\x03",
            "#0000F(I'm so glad we were able to protect them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C2")

    label("loc_578")


    ChrTalk(
        0xB,
        "#1503F#40WZzz... Zzz...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Shizuku is sleeping gently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_5C2")

    TalkEnd(0xB)
    Return()

    # Function_5_4CE end

    def Function_6_5C6(): pass

    label("Function_6_5C6")

    Call(0, 7)
    Return()

    # Function_6_5C6 end

    def Function_7_5CA(): pass

    label("Function_7_5CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E0")
    Call(0, 16)
    Jump("loc_629")

    label("loc_5E0")

    TalkBegin(0xA)

    ChrTalk(
        0xA,
        "#1113F#40WZzz... Zzz...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "KeA is sleeping gently.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_629")

    Return()

    # Function_7_5CA end

    def Function_8_62A(): pass

    label("Function_8_62A")

    Call(0, 9)
    Return()

    # Function_8_62A end

    def Function_9_62E(): pass

    label("Function_9_62E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C2")
    Jump("loc_70C")

    label("loc_6C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E2")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6E2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_702")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_702")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70C")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A")
    SetScenarioFlags(0xEE, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_816")

    ChrTalk(
        0x8,
        (
            "#2800FYou may go to the first floor and ask the\x01",
            "receptionist to exchange any type of sepith.\x02\x03",
            "Don't forget to rest here while you still can,\x01",
            "Lloyd. I imagine the peace won't last long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB")

    label("loc_816")


    ChrTalk(
        0x8,
        (
            "#2803FLeave everything to the guards. The IBC is fortunate\x01",
            "to have some of the finest security on the continent.\x02\x03",
            "#2800FDon't hesitate to ask the first floor receptionist\x01",
            "if you need to restock any supplies.\x02\x03",
            "#2804FAnd don't forget to rest here while you still can,\x01",
            "Lloyd. I imagine the peace won't last long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FYes, sir. Thank you for your hospitality.\x02\x03",
            "#0003F(Let's stock up on supplies while we still can...\x01",
            "There's no telling what'll happen next.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9EB")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_9_62E end

    def Function_10_9F3(): pass

    label("Function_10_9F3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A87")
    Jump("loc_AD1")

    label("loc_A87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD1")

    label("loc_AA7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AD1")

    label("loc_AC7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AD1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F")
    SetScenarioFlags(0xEF, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B75")

    ChrTalk(
        0x9,
        "#2901F*stare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F...?!\x01",
            "(What the heck did I do this time?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C27")

    label("loc_B75")


    ChrTalk(
        0x9,
        (
            "#2903FI can never be too careful...\x02\x03",
            "#2901FI need to devise a plan to deter them once\x01",
            "this nuisance has been dealt with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(She seems more disturbed than usual...)\x02",
    )

    CloseMessageWindow()

    label("loc_C27")

    Jump("loc_FB7")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D0E")

    ChrTalk(
        0x9,
        (
            "#2904FI've instructed the technology department to restore\x01",
            "the orbal network. We need to have it up and running\x01",
            "as soon as possible.\x02\x03",
            "#2900FIn the meantime, I'll continue to try and make sense\x01",
            "of this mess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_D0E")


    ChrTalk(
        0x9,
        (
            "#2903FI tried to think up a strategy to break the\x01",
            "stalemate we're engaged in...\x02\x03",
            "#2901FIt's no use, though. We don't have enough\x01",
            "options.\x02\x03",
            "We can't make a move without knowing our\x01",
            "enemy's true identity, or their objectives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FWe should assess the situation first...\x02\x03",
            "#0006FAnalyzing their movements and acting\x01",
            "accordingly would be the most efficient\x01",
            "move afterwards...I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2905FStrange as it is, I agree with you.\x02\x03",
            "#2904FRegardless, I've instructed the\x01",
            "technology department to restore\x01",
            "the orbal network.\x02\x03",
            "#2902FI'm fairly certain Tio is helping\x01",
            "with the effort, so why don't you\x01",
            "go down there and check on her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSure. That sounds like a plan.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_FB7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_9F3 end

    def Function_11_FBF(): pass

    label("Function_11_FBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD7")
    Call(0, 12)
    Return()

    label("loc_FD7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_106B")
    Jump("loc_10B5")

    label("loc_106B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_108B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B5")

    label("loc_108B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B5")

    label("loc_10AB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_145A")

    ChrTalk(
        0xC,
        (
            "#0112FAh, Lloyd...?\x02\x03",
            "#0113FD-Don't you think it'd be a good idea for you\x01",
            "to take a bit of a break?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FY-Yeah... I'll take one after I go on another\x01",
            "quick patrol.\x02\x03",
            "#0002FYou've been running around just as much as I have,\x01",
            "so you should get some rest, too, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0102FI will take you up on that offer.\x01",
            "Thank you for your concern.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#2901FSuspicious.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrSubChip(0xC, 0x0)
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        "#0011FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#0112FWhat are you implying, Bell?!\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0xC)

    ChrTalk(
        0x9,
        (
            "#2903FWell, your face turned as bright red as your\x01",
            "friend's hair just now.\x02\x03",
            "#2901FI honestly hope that you aren't taking advantage\x01",
            "of this life-or-death situation to make a move\x01",
            "on my dear Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FTh-That's ridiculous!\x01",
            "(Although, I was about to...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#0113F*blush*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2910F(I. WILL. END. YOU.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1703")

    label("loc_145A")


    ChrTalk(
        0xC,
        (
            "#0108FLloyd...\x01",
            "This has gotten really serious.\x02\x03",
            "#0101FWhat could the cult--no. What could Doctor Guenter's\x01",
            "objective be amidst all this madness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FI don't have an answer for you...\x02\x03",
            "#0006FBut, we've managed to drag everybody here\x01",
            "into this mess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0xC,
        (
            "#0102FHeehee...\x01",
            "Some things never change with you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0104FDon't worry. Uncle Dieter and Mariabell are\x01",
            "both formidable foes. They'll be able to take\x01",
            "care of everyone here just fine.\x02\x03",
            "#0100FI think it's better for us to figure out how we\x01",
            "can keep KeA and Shizuku out of harm's reach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, you're right.\x01",
            "Maybe I'll head out on another patrol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1703")

    SetScenarioFlags(0xE4, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1913")

    label("loc_1717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_1839")

    ChrTalk(
        0xC,
        (
            "#0109FU-Umm...\x01",
            "Can you take care of the supplies and equipment?\x02\x03",
            "#0102FI'll go talk with Bell and the others to come up\x01",
            "with a plan on how we're going to overcome this.\x02\x03",
            "Let's do everything we can, but not to the point\x01",
            "of total exhaustion.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1834")

    ChrTalk(
        0x101,
        "#0000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1834")

    Jump("loc_1913")

    label("loc_1839")


    ChrTalk(
        0xC,
        (
            "#0103FI spoke with Bell about how to proceed.\x01",
            "Unfortunately, we don't have any options right now.\x02\x03",
            "#0108FIf only it were dawn, or if we could at\x01",
            "least contact someone outside the IBC...\x01",
            "Maybe we'd have some hope.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1913")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_FBF end

    def Function_12_191B(): pass

    label("Function_12_191B")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xC, 0xFF)
    LoadChrToIndex("apl/ch50541.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#5200461V#0108F#5P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200456V#0000F#5PElie...\x01",
            "So this is where you've been hiding.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sound(1178, 255, 90, 0)
    Sleep(150)

    AnonymousTalk(
        0xC,
        "#5200457V#40WLloyd...?\x02",
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
        0x101,
        (
            "#5200458V#0006F#5PI know I'm just repeating myself at this point, but\x01",
            "the situation really took a turn for the worse.\x02\x03",
            "#5200459V#0001FI just hope everybody in the city is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200460V#0106F#11P#30WYeah. Me, too.\x02\x03",
            "#5200455V#0108F#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5200462V#0004F#5PHey. Your grandfather will be just fine.\x02\x03",
            "#5200463V#0000FThe one pulling the CGF's strings has no\x01",
            "reason to harm him, right?\x02\x03",
            "#5200464VWe can overcome this situation. Together.\x01",
            "And we'll free everybody, including your\x01",
            "grandfather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200465V#0102F#11PLloyd... Thank you.\x02\x03",
            "#5200466V#0104FAnd you're right. It's not like my grandfather\x01",
            "hasn't had his fair share of trouble over the\x01",
            "years.\x02\x03",
            "#5200467VEven in perils like this, I'm sure he'll manage\x01",
            "to pull through one way or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200468V#0002F#5PAgreed. Someone like the mayor won't be\x01",
            "taken down by a situation like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200469V#0102F#11PHeehee...\x02\x03",
            "#5200470V#0106FOh, geez. How are you always able to tell\x01",
            "how I'm feeling? You make it look so easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200548V#0005F#5PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200472V#0113F#11PIf you think about it, it's a bit unfair.\x02\x03",
            "#5200473VI've already laid bare the majority of my\x01",
            "problems to you. But...\x02\x03",
            "#5200474V#0111F...you keep yours under lock and key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200475V#0011F#5PU-Uh... Elie?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0xC,
        (
            "#5200476V#0103F#11PHey, Lloyd.\x02\x03",
            "#5200477V#0100FHave you managed to catch up to your\x01",
            "brother at all?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5200478V#0005F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200479V#0104F#11PWell, I can only assume...that you've always\x01",
            "been chasing after your brother. Desperately,\x01",
            "carelessly chasing after him.\x02\x03",
            "#5200480VOver these past five months, you've often\x01",
            "spoken of overcoming Crossbell's barriers.\x02\x03",
            "#5200481V#0100FLloyd. Is that how you perceive your own brother,\x01",
            "as well? Is catching him a barrier you've created\x01",
            "for yourself?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5200482V#0004F#5P...Yeah. Something like that.\x02\x03",
            "#5200534V#0008F...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(57610, 1500, 240, 2800)
    MoveCamera(105, 24, 0, 2800)
    OP_6E(500, 2800)
    SetCameraDistance(13000, 2800)
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_2285():
        OP_96(0x101, 0xE10A, 0x0, 0xF0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2285)
    Sleep(1000)

    def lambda_22A2():
        OP_93(0xC, 0x122, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_22A2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    OP_6F(0x79)
    Fade(200)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200484V#0004F#5PIt's no secret that my brother was always my\x01",
            "hero growing up. Heck, he still is.\x02\x03",
            "#5200485VGuy was...amazing. He'd never surrender, and\x01",
            "always achieve anything he set his mind to.\x01",
            "He wouldn't let anything bring him down.\x02\x03",
            "#5200486V#0008FBut, three years ago...he vanished. And I was\x01",
            "left wandering without a destination. No goal\x01",
            "to strive towards. Nothing.\x02\x03",
            "#5200487VSo, I ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5200488V#0105F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200489V#0006F#5PI... I didn't believe that I had the strength\x01",
            "to become as strong a man as he was.\x02\x03",
            "#5200490VI lacked the confidence to protect the ones\x01",
            "I loved like he did.\x02\x03",
            "#5200491V#0008FSo, that's why...I ran. Far away from Crossbell.\x01",
            "From home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200492V#0103F#11PYet here you stand, in Crossbell once again.\x02\x03",
            "#5200493V#0100FWhy come back, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200494V#0004F#5PHaha. It's not really that surprising. The long and\x01",
            "short of it is that I love this city.\x02\x03",
            "#5200495VMy brother, Cecile, the time I spent with my friends,\x01",
            "and everything that goes along with that...\x02\x03",
            "#5200496VEven while living in the Republic, there was no way\x01",
            "I could leave that part of me behind. I could never\x01",
            "forget those precious people. Those memories.\x02\x03",
            "#5200497V#0000FThat's probably why I forced myself to take the\x01",
            "detective exam during my time at the academy.\x02\x03",
            "#5200498V#0008FAfter all, it was the first step I needed to take in\x01",
            "order to overcome my brother.\x02\x03",
            "#5200499V#0003F'What right do I have to return to Crossbell if I\x01",
            "can never replace its slain hero?' That was my\x01",
            "thought process at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200500V#0105F#11PB-But, in the end, you did manage to become a\x01",
            "detective.\x02\x03",
            "#5200501V#0102FSurely that's a sign that you've caught up to\x01",
            "your brother to some degree, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200502V#0006F#5PNo, actually. To be honest, I've always felt like\x01",
            "I didn't pass the exam on my own merit.\x02\x03",
            "#5200503V#0002FThough he was definitely unconventional, Guy was a\x01",
            "first-rate detective. At least, in my eyes he was.\x02\x03",
            "#5200504V#0004FSo, I often ask myself, 'What would Guy do?'\x01",
            "He'd never give up. He'd always find a way\x01",
            "to push through.\x02\x03",
            "#5200505VThe only reason I've made it this far is because\x01",
            "I draw on his strength--the source of my motivation.\x02\x03",
            "#5200506V#0008FBut... I've always felt like it's been a handicap.\x01",
            "If I'm so often relying on him, then what have\x01",
            "I earned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5200507V#0101F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200508V#0000F#5PAnd I think that I've finally come to realize that.\x02\x03",
            "#5200509VMindlessly chasing after my brother, my hero,\x01",
            "will never make me stronger. Not really.\x02\x03",
            "#5200510V#0012FA little too late for those kinds of revelations,\x01",
            "given our current situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5200511V#0103F#11P...Lloyd.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    SetChrFlags(0xC, 0x40)
    OP_95(0xC, 57880, 0, -270, 800, 0x0)
    Fade(500)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xC, 57970, 0, -180, 300)
    SetChrSubChip(0x101, 0x0)
    MoveCamera(75, 27, 0, 0)
    SetCameraDistance(14500, 0)
    OP_68(57640, 1500, 140, 0)
    OP_0D()
    Sound(804, 0, 70, 0)
    Sound(910, 0, 80, 0)
    OP_A1(0x101, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5200512V#0011F#5PE-Elie?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(13500, 60000)
    OP_A1(0x101, 0x3E8, 0x3, 0x18, 0x19, 0x1A)

    ChrTalk(
        0xC,
        (
            "#5200513V#0100F#11PThere's something I have to say.\x02\x03",
            "#5200514VI may have never met Guy...\x02\x03",
            "#5200515V#0104F...but I know one thing for certain.\x02\x03",
            "#5200516VYou've been the glue that holds us together.\x01",
            "The one that continues to motivate us, no\x01",
            "matter the odds! You always have been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200517V#0005F#5PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200518V#0102F#11PYou've always been guiding me--no, us, through\x01",
            "thick and thin.\x02\x03",
            "#5200519VYou know us. We were all lost in this great, gray\x01",
            "city. Yet, you managed to be our guiding light.\x02\x03",
            "#5200520V#0104FYou're gentle, earnest, probably a little too dense\x01",
            "at times, but...\x02\x03",
            "#5200521V...through everything, you have always stayed by\x01",
            "our sides, continuing to search for the truth when\x01",
            "no one else will.\x02\x03",
            "#5200522V#0102FHad you not been our foundation, I doubt we would\x01",
            "have made it this far.\x02\x03",
            "#5200523VIt wasn't Guy who did that, or anyone else. It was\x01",
            "you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200524V#0005F#5P...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#5200525V#0104F#11PI thank the Goddess above every day for allowing\x01",
            "me to meet you.\x02\x03",
            "#5200526VA part of me wishes we had met at Sunday School,\x01",
            "back when we were kids.\x02\x03",
            "#5200527V#0102FEven I like to indulge myself in silly fantasies\x01",
            "like that, every now and then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x384, 0x2, 0x4, 0x5)

    ChrTalk(
        0x101,
        "#5200528V#0004F#5PElie, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200529V#0104F#11PBelieve in yourself, Lloyd Bannings.\x02\x03",
            "#5200530VThe part of you that loves your brother and the\x01",
            "part that's always struggling to catch him...\x01",
            "Both make you who you are. So embrace it, okay?\x02\x03",
            "#5200531VBecause, that's the Lloyd Bannings that we--no...\x01",
            "That's the Lloyd that I admire.\x02\x03",
            "#5200532V#0102FThat's why I think you're fine just the way you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200533V#0004F#5PElie...\x02\x03",
            "#5200483V#0002F...\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x514, 0x4, 0x6, 0x7, 0x8, 0x9)
    Sleep(500)

    ChrTalk(
        0xC,
        "#5200535V#0112F#11POh...?\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A1(0x101, 0x4B0, 0x6, 0xA, 0xB, 0xC, 0x15, 0x16, 0x17)
    Sleep(500)
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    VolumeBGM(0x3C, 0x5DC)
    SetChrSubChip(0x101, 0x1E)
    Sleep(8)
    SetChrSubChip(0x101, 0x1F)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200536V\x07\x05",
            "A short announcement to everyone remaining\x01",
            "in the building.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200537V\x07\x05",
            "In the event of an emergency situation, a portion\x01",
            "of the floor's lighting will be turned off.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200538V\x07\x05",
            "Also, for security reasons, all exits besides\x01",
            "the front entrance will now be sealed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200539V\x07\x05",
            "We would please ask for your understanding and\x01",
            "to be extremely cautious about using open flames\x01",
            "within the building at this time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0xC, 0x8)
    TurnDirection(0x101, 0xC, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#5200540V#0012F#5PHaha. Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200541V#0109F#11PHeehee...\x02\x03",
            "#5200542V#0112FI-I should probably get back to Bell.\x02\x03",
            "#5200543V#0113FThere may be something that I can assist\x01",
            "Uncle and the others with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200544V#0004F#5PY-Yeah, of course. I should stock up on\x01",
            "supplies and double-check our equipment\x01",
            "while I still can.\x02\x03",
            "#5200545V#0002FAnyway, I'll catch up with you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200546V#0102F#11PR-Right. Of course.\x02\x03",
            "#5200547V#0113FUm, Lloyd? Once we've resolved this whole mess,\x01",
            "would you like to continue with our unfinished\x01",
            "business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200471V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3976():

        label("loc_3976")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_3976")

    QueueWorkItem2(0x101, 2, lambda_3976)
    OP_96(0xC, 0xE394, 0x0, 0xFFFFFD3A, 0x3E8, 0x0)

    ChrTalk(
        0xC,
        (
            "#5200549V#0112F#11PN-Never mind!\x02\x03",
            "#5200550V#0109FSee you later!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x12C)
    OP_95(0xC, 58570, 0, 1430, 2000, 0x0)
    OP_95(0xC, 57880, 0, 4330, 2000, 0x0)
    ClearChrFlags(0xC, 0x40)

    def lambda_3A15():
        OP_95(0xFE, 53120, 0, 17620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3A15)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Fade(500)
    MoveCamera(105, 24, 0, 0)
    SetCameraDistance(14000, 0)
    OP_93(0x101, 0x14A, 0x0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200551V#0002F#5P(Elie's cheek was so soft...)\x02\x03",
            "#5200552V#0002F(Was she wearing perfume?)\x02\x03",
            "#5200553V#0006F(I was so close. Just a little more, and--)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5200554V#0011F#5PGah! What the hell am I thinking?!\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x2, 0x1C, 0x1D)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5200555V#0004F#5P(Still. I'm fine just the way I am...?)\x02\x03",
            "#5200556V(Had I heard that a few months ago, I would have\x01",
            "felt just as confused and lost as ever. But now...)\x02\x03",
            "#5200557V#0000F(...I think I can agree, as strange as it sounds.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x4B0, 0x2, 0x1C, 0x1B)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x12C)

    ChrTalk(
        0x101,
        "#5200558V#0002F#11PThank you, Elie. For everything.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2E")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Elie learned \x07\x02",
            "[Star Blast 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Their \x07\x02",
            "[Star Blast]\x07\x05",
            " combo craft was strengthened.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attack power, range, and area of effect have all been\x01",
            "improved, and they can act sooner after use.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_3E2E")

    OP_CA(0x1, 0xFF, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x1)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 59090, 30, 121360, 0)
    OP_68(57610, 1500, 240, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 57610, 0, 240, 315)
    SetScenarioFlags(0xE7, 2)
    OP_DE(0x2D, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_191B end

    def Function_13_3EB6(): pass

    label("Function_13_3EB6")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    LoadChrToIndex("apl/ch50543.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xD,
        "#5200601V#0208F#5P#30W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200560V#0005F#5PWhat's up, Tio?\x02",
    )

    CloseMessageWindow()
    Sound(1269, 255, 90, 0)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1267, 255, 90, 0)
    OP_93(0xD, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        "#5200561VOh. Lloyd.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200562V#0005FIs something wrong--oh. That's a dumb question.\x02\x03",
            "#5200563V#0000FYou came to assess the situation, right?\x02",
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
        0xD,
        (
            "#5200564V#0203F#11PYes. My anxiety is rising, so I wanted to\x01",
            "analyze it myself.\x02\x03",
            "#5200565V#0205FYou came to that conclusion rather quickly,\x01",
            "though, did you not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200566V#0000F#5PWell, sure. Because you're always sticking\x01",
            "your neck out for us, Tio.\x02\x03",
            "#5200567V#0001FSo? How's the situation looking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200568V#0206F#11PIt appears that various firefights have broken\x01",
            "out throughout the city.\x02\x03",
            "#5200569V#0208FI strongly suspect that the CPD and CGF are\x01",
            "engaged in open combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200570V#0008F#5PI figured as much.\x02\x03",
            "#5200571V#0003FI really hope the citizenry are able to stay\x01",
            "out of the crossfire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200572V#0208F#11P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5200573V#0005F#5PYou okay, Tio? I bet you're exhausted.\x02\x03",
            "#5200574VWell, I guess we did just run around\x01",
            "#0001Fthe entire city. To tell the truth, I would\x01",
            "rather see you resting with KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200575V#0211F#11P*stare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200576V#0011F#5PW-Wait a second! Honest to Aidios, I'm not trying\x01",
            "to treat you like a child! I'm just concerned!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200577V#0202F#11PHeehee... I know.\x02\x03",
            "#5200578VYou do not need to worry, Lloyd. I have\x01",
            "considerably more endurance now than\x01",
            "when we began working together.\x02\x03",
            "#5200579V#0204FThough, I don't think I'd be able to fall\x01",
            "asleep in the middle of something this\x01",
            "intense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200580V#0002F#5PI can't blame you.\x02\x03",
            "#5200581V#0006FI don't think I'd be able to dream up a situation\x01",
            "this wild. It really is unbelievable.\x02\x03",
            "#5200582V#0001FCome to think of it, you aren't formally a part of\x01",
            "the CPD, yet we still dragged you into this mess.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xD,
        "#5200583V#0211F#11P*STARE*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200584V#0012F#5PS-Sorry! I'm not saying that you aren't personally\x01",
            "invested in this or anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200585V#0206F#11PIt's okay.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    ChrTalk(
        0xD,
        (
            "#5200586V#0206F#11PY-You know, now that things are spiraling\x01",
            "out of control, I worry about what awaits\x01",
            "us at the end.\x02\x03",
            "#5200587VI don't even know how the Epstein Foundation\x01",
            "will feel about my temporary transfer here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200588V#0005F#5PReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200589V#0208F#11PThey may consider relocating orbal staff testing\x01",
            "outside of Crossbell.\x02\x03",
            "#5200590VIt will depend on the foundation's plans, but\x01",
            "it is entirely possible that I'm withdrawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200591V#0001F#5PTh-That's...\x02\x03",
            "#5200592V#0003F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200593V#0208F#11PUm...\x02\x03",
            "#5200594V#0200FIf that were to happen...would you be saddened\x01",
            "by my departure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200595V#0006F#5PSad...?\x02\x03",
            "#5200596VI don't even want to imagine it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200597V#0205F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200598V#0012F#5PA Special Support Section without Tio Plato?\x01",
            "I don't think that's even possible.\x02\x03",
            "#5200599V#0000FThe SSS would still be in the Middle Ages\x01",
            "if you weren't there to handle the terminal.\x02\x03",
            "#5200600VI doubt anyone else on the continent could\x01",
            "operate it as well as you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200559V#0205F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200602V#0008F#5PStill, though... I can't just ignore the possibility\x01",
            "that they may decide to take you back.\x02\x03",
            "#5200603V#0006FBefore now, it was something I didn't even want\x01",
            "to acknowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200604V#0206F#11PIt is, as you said, simply a possibility\x01",
            "at the moment.\x02\x03",
            "#5200605V#0202FThe foundation has made a large investment\x01",
            "in Crossbell. The cutting edge technology\x01",
            "it has built here is a testament to that.\x02\x03",
            "#5200606VThe situation may seem dire, but I do not expect\x01",
            "one incident to cause that investment to end.\x02\x03",
            "#5200607V#0204FAnd as long as that is the case, Crossbell is,\x01",
            "and will remain, the ideal testing grounds for\x01",
            "my staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200608V#0002F#5PI hope so.\x02\x03",
            "#5200609V#0000FRegardless, we need to do everything in our power\x01",
            "to end this stalemate and resolve this incident.\x01",
            "We can't give them a reason to change their minds.\x02\x03",
            "#5200610V#0009FAfter all, the Special Support Section needs you.\x01",
            "We won't let you go so easily!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xD,
        "#5200611V#0205F#11PAh...\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200612V#0011F#5PU-Uh... What is it this time? Whatever it is I said,\x01",
            "I swear I didn't mean to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200613V#0203F#5PObviously. Still, you are quite absurd,\x01",
            "Lloyd Bannings.\x02\x03",
            "#5200614V#0211FElie was right. You are far more dangerous\x01",
            "than you give yourself credit for.\x02\x03",
            "#5200615VOf all the ways you could have reacted,\x01",
            "you still managed to surprise me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200616V#0005F#5PWhat was wrong with my reaction?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200617V#0208F#5PWhat I am trying to say is that you are\x01",
            "an insensitive, good-for-nothing little\x01",
            "brother character.\x02\x03",
            "#5200618V#0201FYou have somehow managed to surpass your\x01",
            "brother in all of those qualities, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200619V#0006F#5PI-I'm not quite sure that I follow...\x02\x03",
            "#5200620V#0001FAm I really just as bad as Guy was?\x02\x03",
            "#5200621VI wouldn't exactly call him insensitive, but he was\x01",
            "definitely as thick as a brick.\x02\x03",
            "#5200622V#0008FHe was completely oblivious to how Cecile felt for\x01",
            "the longest time...\x02\x03",
            "#5200623V#0006FThere were SO many times I wanted to kick him\x01",
            "to make him finally realize what he was missing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)
    OP_68(58920, 1400, -10, 1200)
    OP_96(0xD, 0xE6F0, 0x0, 0xFFFFFE52, 0x320, 0x0)
    Sound(1197, 255, 85, 0)
    Sleep(500)
    Fade(150)
    Sound(819, 0, 100, 0)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sound(1029, 255, 90, 1)

    def lambda_544F():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_544F)
    Sleep(390)
    Fade(250)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5200626V#0012F#5PHey! What was that for, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200627V#0203F#11PDon't pay it any mind.\x02\x03",
            "#5200628V#0211FBut know that you got what you deserved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200629V#0011F#5PI did?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200630V\x07\x05",
            "A short announcement to everyone remaining\x01",
            "in the building.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200631V\x07\x05",
            "In the event of an emergency situation, a portion\x01",
            "of the floor's lighting will be turned off.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200632V\x07\x05",
            "Also, for security reasons, all exits besides\x01",
            "the front entrance will now be sealed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200633V\x07\x05",
            "We would please ask for your understanding and\x01",
            "to be extremely cautious about using open flames\x01",
            "within the building at this time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)

    ChrTalk(
        0x101,
        "#5200634V#0001F#5PI guess we're officially on lockdown.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200635V#0204F#11PI think I'll go assist the researchers\x01",
            "in the terminal room.\x02\x03",
            "#5200636VWe'll likely have more options if I can\x01",
            "establish communications with Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200637V#0002F#5PThat sounds like a good idea. I'll be counting\x01",
            "on you, then.\x02\x03",
            "#5200638VLeave checking our supplies and equipment to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200639V#0202F#11PThat would be greatly appreciated.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0x101,
        (
            "#5200640V#0011F#5PIs something wrong, Tio?\x01",
            "(Don't tell me she's mad at me again...)\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(14500, 60000)

    ChrTalk(
        0xD,
        (
            "#5200641V#0208F#11PThe promise you proposed taking over. The\x01",
            "one that Guy made to me.\x02\x03",
            "#5200642V#0201FDo you remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200643V#0005F#5PY-Yeah, of course I do.\x02\x03",
            "#5200644V#0000FYou said that if I wanted to honor it, I should\x01",
            "make my own promise on new terms.\x02\x03",
            "#5200645V#0006FSorry, Tio. I've been thinking about it ever since\x01",
            "that day, but I haven't been able to come up with\x01",
            "anything yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200646V#0203F#11PIn that case...\x01",
            "I would like to make my own wish.\x02\x03",
            "#5200647V#0201FIs that acceptable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200648V#0005F#5PO-Of course. I don't mind, Tio.\x02\x03",
            "#5200649V#0000FLay it on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200650V#0202F#11P...\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x190)
    Sleep(300)
    OP_68(58720, 1400, -290, 1500)
    OP_96(0xD, 0xE6D2, 0x0, 0xFFFFFBD2, 0x320, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0xD,
        (
            "#5200651V#0204F#5PMishelam Wonderland.\x02\x03",
            "#5200652VI would like you to take me there once this\x01",
            "crisis is averted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200653V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5200654V#0011F#5PSeriously?! That's all you want?!\x02\x03",
            "#5200655V#0001FDon't you think that's...a little small?\x01",
            "Don't you think it'd be better to promise\x01",
            "something a little more significant?\x02\x03",
            "#5200656VYou could even say, 'When I'm in trouble,\x01",
            "always come to my rescue.' Wouldn't that\x01",
            "be better?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200657V#0204F#5PNot at all. This is more than enough.\x02\x03",
            "#5200658V#0208FBesides, if we fail to resolve this crisis, then\x01",
            "it is a promise you won't be able to keep.\x02\x03",
            "#5200659V#0202FWith that in mind, isn't what I'm asking for\x01",
            "very significant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200660V#0004F#5PWell, I guess you got me there.\x02\x03",
            "#5200661V#0002FAll right, then. It's a promise.\x02\x03",
            "#5200662VI'd be more than happy to take you to Mishelam\x01",
            "Wonderland once this is all over.\x02\x03",
            "#5200663V#0005FOh, but is it fine if we invite the others?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x320)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xD,
        "#5200664V#0211F#11P*S T A R E*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200665V#0012F#5PI-I'll take that as a no. I suppose it is a promise\x01",
            "that I'm making to you and you alone.\x02\x03",
            "#5200666V#0006FThat's too bad, though. I wanted to bring KeA with\x01",
            "us, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5200667V#0204F#11PWell... If that's the case, I will\x01",
            "amend the promise.\x02\x03",
            "#5200668V#0202FOur first trip can be with everybody.\x01",
            "But after, it has to be just us.\x02\x03",
            "#5200669VDo you have any complaints?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200670V#0000F#5PN-No. None at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5200671V#0209F#11PI'll be looking forward to it.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_626C():

        label("loc_626C")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_626C")

    QueueWorkItem2(0x101, 2, lambda_626C)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(21500, 8000)
    Sleep(300)
    OP_95(0xD, 58140, 0, -380, 2000, 0x0)
    OP_95(0xD, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xD, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xD, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xD, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xD, 55730, 0, 13960, 2000, 0x0)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_6353():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6353)
    Sleep(1000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xD, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(58830, 1500, 600, 0)
    MoveCamera(127, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_93(0x101, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5200672V#0006F#11PIs she really fine with such a simple promise?\x02\x03",
            "#5200673V#0002FWell, as long as it makes her happy, I guess\x01",
            "it's all right.\x02\x03",
            "#5200674V#0004FFor the sake of our promise...\x01",
            "I swear that I'll get to the bottom of this case!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6628")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio learned \x07\x02",
            "[Omega Strike 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Their \x07\x02",
            "[Omega Strike]\x07\x05",
            " combo craft was strengthened.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attack power, range, and area of effect have all been\x01",
            "improved, and they can act sooner after use.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_6628")

    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    SetScenarioFlags(0xE7, 3)
    OP_DE(0x2E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_13_3EB6 end

    def Function_14_6683(): pass

    label("Function_14_6683")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xE, 0xFF)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    SetChrPos(0x101, 59090, 0, 360, 180)
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xE,
        "#5200694V#0308F#5P#30W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200676V#0005F#5PRandy? What are you up to?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1364, 255, 100, 0)
    OP_93(0xE, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 32, 3)
    Sleep(500)

    AnonymousTalk(
        0xE,
        (
            "#5200677VHey there, partner.\x02\x03",
            "#5200678VMan, this whole debacle is damn\x01",
            "near unbelievable, eh?\x02",
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
        0x101,
        "#5200679V#0005F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200680V#0305F#11PWhat's gotten into you?\x01",
            "I say somethin' funny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200681V#0012F#5PN-No, not particularly...\x02\x03",
            "#5200682V#0008FI need your honest opinion, Randy.\x01",
            "What do you make of the situation?\x02\x03",
            "#5200683V#0001FI'm not confident we'll be able to hold out\x01",
            "against the CGF's onslaught much longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200684V#0303F#11PTo be frank, I don't like our odds one bit.\x02\x03",
            "#5200685V#0301FThey may not be an army, but the CGF is legit.\x02\x03",
            "#5200686VSure, they're not allowed to have tanks\x01",
            "or patrol ships, but the guardsmen are\x01",
            "equipped with the best weaponry out there.\x02\x03",
            "#5200687V#0306FThis is one decked out building, but it\x01",
            "ain't no fortress. Some office building\x01",
            "isn't gonna stand a chance against 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200688V#0008F#5PI was afraid you might say that...\x02\x03",
            "#5200689V#0003FAll the more reason why reestablishing\x01",
            "communication with HQ and the guild\x01",
            "should be our top priority.\x02\x03",
            "#5200690V#0013FUntil then, we have to do everything in\x01",
            "our power to defend the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200691V#0303F#11PPretty much, yeah.\x02\x03",
            "#5200692V#0308FDamn... I sure wish I had THAT with me\x01",
            "right about now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5200693V#0005F#5P'That'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200675V#0303F#11P...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#5200695V#0304F#5PI mean the orbal rifle I used up\x01",
            "until about two years ago.\x02\x03",
            "#5200696V#0300FIt packs one hell of a punch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200697V#0008F#5PThat's right. You were part of\x01",
            "a jaeger corps...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    ChrTalk(
        0x101,
        (
            "#5200698V#0003F#5PThe Red Constellation, right?\x02\x03",
            "#5200699V#0000FI did a little bit of research, and they're\x01",
            "apparently famous among the authorities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200700V#0309F#5PHaha... 'Famous,' he says. I think you mean\x01",
            "infamous, my friend.\x02\x03",
            "#5200701V#0304FThey're nothin' short of the vilest corps in all of\x01",
            "western Zemuria. Those crimson gods of death treat\x01",
            "battles like they're some kind of playground.\x02\x03",
            "#5200702V#0300FI heard they were locked in battle with Heiyue over\x01",
            "in Calvard a lil' while back, too.\x02\x03",
            "#5200703VNo doubt it was a real bloodbath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200704V#0008F#5PYeah? I can't even imagine how awful it was.\x02\x03",
            "#5200705V...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5200706V#0302F#11PSorry. Didn't mean to start yammerin' about a\x01",
            "nasty topic while our situation's already dire.\x02\x03",
            "#5200707V#0303FAnyway, if the CGF starts getting serious,\x01",
            "you can bet all hell's gonna break loose.\x02\x03",
            "#5200708V#0301FAnd don't even get me started on their newest\x01",
            "armored car. If that thing starts roll--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200709V#0004F#5PHey, Randy...\x02\x03",
            "#5200710V#0002FDo you mind if I retract what I said\x01",
            "a little while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200711V#0305F#11PWhat'cha talkin' about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200712V#0000F#5PYou remember our little chat after the chase battle?\x02\x03",
            "#5200713VUntil I'm able to stand tall and proud like you and\x01",
            "my brother, I won't pry into your past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200714V#0305F#11POh, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200715V#0008F#5PI've mentioned this before, but my brother\x01",
            "truly was my hero.\x02\x03",
            "#5200716V#0003FIt's like Chief Sergei, Dudley, and Arios\x01",
            "have said before.\x02\x03",
            "#5200717V#0000FGuy's presence alone was enough to make\x01",
            "anyone feel like they'd be able to overcome\x01",
            "the worst of odds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200718V#0300F#11PYeah, it sure sounds like it.\x02\x03",
            "#5200719V#0306FGeez, dude. How much of a friggin' beast\x01",
            "was this brother of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200720V#0002F#5PHaha. I guess that's one way to put it. I wouldn't\x01",
            "say he was a powerhouse, though.\x02\x03",
            "#5200721V#0006FEver since his death, I've been telling myself\x01",
            "that I have to grow strong enough to fill the\x01",
            "gap he left behind.\x02\x03",
            "#5200722VAnd if I couldn't, what right did I have to\x01",
            "return to Crossbell?\x02\x03",
            "#5200723V#0008FI kept hammering it in my head to earn my\x01",
            "detective's license and become the treasure\x01",
            "Crossbell once lost...\x02\x03",
            "#5200724V#0002FAnd to be honest, I think that I've always known to\x01",
            "some extent that it was an unreasonable goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200725V#0303F#11PUh-huh...\x02\x03",
            "#5200726V#0300FY'know, despite all that, you still look totally\x01",
            "composed. What gives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200727V#0012F#5PHaha. Do I?\x02\x03",
            "#5200728V#0004FI suppose I've become oddly optimistic,\x01",
            "now that we've come this far.\x02\x03",
            "#5200729VI may not be able to fill my brother's shoes...\x02\x03",
            "#5200730V#0000F...but, I think that if I can reach my full\x01",
            "potential and become my own man, then maybe\x01",
            "that'd be satisfying enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200731V#0305F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200732V#0006F#5PI say that, but I honestly have no clue where\x01",
            "to even begin.\x02\x03",
            "#5200733VSince we've taken in KeA, I've realized\x01",
            "that my hesitating and worrying over every\x01",
            "little detail is going to drag us all down.\x02\x03",
            "#5200734V#0002FI'm grateful you're all by my side. I may not\x01",
            "be strong enough on my own, but together,\x01",
            "we'll pull through.\x02\x03",
            "#5200735VWith that said, I hope you don't mind me\x01",
            "leaning on your strength in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200736V#0309F#11PMan... What's up with you?\x02\x03",
            "#5200737V#0302FYou're already plenty mature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200738V#0004F#5PYou already knew, too, didn't you, Randy?\x02\x03",
            "#5200739V#0000FYou knew I'd trip and fall if I continued\x01",
            "trying to chase after my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200740V#0306F#11P...Guilty as charged.\x02\x03",
            "#5200741V#0304FActually, I figured your eventual misstep would\x01",
            "cause that passion of yours to burn even brighter.\x02\x03",
            "#5200742V#0302FBut it looks like ya managed to figure that out\x01",
            "on your own before it was too late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200743V#0004F#5PYeah, but I definitely couldn't have done it\x01",
            "without the rest of you.\x02\x03",
            "#5200744V#0002FAnd that's why right here, right now, I want you\x01",
            "tell me about your past--the good and bad.\x02\x03",
            "#5200745VI want to know the truth behind the guy\x01",
            "who's been watching over me this whole\x01",
            "time, as if he were my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200746V#0309F#11P#40WHaha...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    OP_93(0xE, 0xB4, 0x190)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0xE)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7001", 0)
    SetCameraDistance(14500, 60000)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#5200747V#0308F#5PSay, Lloyd.\x02\x03",
            "#5200748V#0304FCare to take a guess at how many enemies\x01",
            "I've killed on the battlefield?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200749V#0006F#5PI could never imagine you killing anyone.\x02\x03",
            "#5200750V#0001FIt's probably because we've lived lives\x01",
            "so vastly different from one another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200751V#0312F#5PBingo, my friend. And sadly, the answer is that\x01",
            "I've killed so many that I've lost track.\x02\x03",
            "#5200752V#0304FFor as long as I could remember, I lived in the hell\x01",
            "known as the field of battle.\x02\x03",
            "#5200753VI was handed my first knife at the ripe age of four.\x01",
            "At six, I fired my first gun.\x02\x03",
            "#5200754V#0303FI had my first combat experience when I was only\x01",
            "nine years old. I was a scout in my old man's unit,\x01",
            "and we slew each and every last one of our enemies.\x02\x03",
            "#5200755VThey gave me a small unit to command when I was\x01",
            "twelve, and at fourteen, that upgraded to a larger\x01",
            "unit.\x02\x03",
            "#5200756V#0311FFor five long, long years, I was a damn dog,\x01",
            "sniffing out death on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200763V#0005F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200758V#0308F#5PBut eventually, I turned tail and ran away.\x02\x03",
            "#5200759VDon't get me wrong, though. I didn't escape\x01",
            "the corps by the book like Garcia was able to.\x02\x03",
            "#5200760VOh, and I was a real piece of shit. I didn't\x01",
            "even feel remorse for killing the way I did.\x02\x03",
            "#5200761V#0303FOne day, I just...was lost. Lost from myself...\x01",
            "Lost from the battlefield.\x02\x03",
            "#5200762V#0311FLike I was some kinda wandering corpse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200757V#0001F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200764V#0304F#5PFrom there, I drifted from place to place,\x01",
            "eventually winding up in Crossbell...\x02\x03",
            "#5200765VI managed to worm my way into the CGF, but\x01",
            "I refused to touch a rifle. That son of a\x01",
            "bitch commander ended up dischargin' me.\x02\x03",
            "#5200766V#0308FAnd then, as if it were fate, the chief\x01",
            "took me in like a dirty stray. Lo and behold, here I am.\x02\x03",
            "#5200767V#0312FThis is who I am, Lloyd. That's the tale of\x01",
            "the man known as Randolph Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200768V#0003F#5PRandy...\x02\x03",
            "#5200769V#0002FThank you. Thank you for telling me your story.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x190)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5200770V#0306F#11PSheesh, Lloyd. You a masochist?\x02\x03",
            "#5200771V#0308FWhy the hell'd you ever wanna know\x01",
            "about trash like me?\x02\x03",
            "#5200772V#0301FYou just couldn't leave well enough\x01",
            "alone, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200773V#0004F#5PYeah, I may be partially to blame.\x02\x03",
            "#5200774VEven so, I was determined to hear\x01",
            "your story, no matter what.\x02\x03",
            "#5200775V#0000FAnd besides, how fair would it be for\x01",
            "you to know my life's story while I'm\x01",
            "in the dark about yours?\x02\x03",
            "#5200776V#0002FKnowing each other inside and out is\x01",
            "what makes us partners, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5200777V#0305F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200778V#0001F#5PWell, you called me your partner,\x01",
            "didn't you, Randy?\x02\x03",
            "#5200779VRight as I walked up to you earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200780V#0305F#11PThink you're readin' into it a little too much...\x01",
            "That was just a greetin', my man.\x02\x03",
            "#5200781V#0301FWait, hold up... Have I really never called you\x01",
            "that before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200782V#0002F#5PYeah, I'm pretty sure.\x02\x03",
            "#5200783V#0012FT-To be honest, I was a little happy to hear\x01",
            "you say that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Sound(1376, 255, 100, 0)
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    ChrTalk(
        0xE,
        "#5200784V#0309F#11PHaha... #4SHahahahahahaha!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200785V#0011F#5PYou don't have to laugh at me!\x02\x03",
            "#5200786V#0006FNow I'm embarrassed that\x01",
            "I told you anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200787V#0302F#11PSo that's why you pulled me aside.\x02\x03",
            "#5200788V#0304FNot only that, but you drove me into a\x01",
            "corner by pourin' your heart out first!\x02\x03",
            "#5200789V#0309FWell, well, well, Lloyd. Looks like I had you\x01",
            "all wrong. A masochist? No. You're a bona\x01",
            "fide sadist, my friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200790V#0011F#5PI have absolutely no idea what you're talking about.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200791V\x07\x05",
            "A short announcement to everyone remaining\x01",
            "in the building.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200792V\x07\x05",
            "In the event of an emergency situation, a portion\x01",
            "of the floor's lighting will be turned off.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200793V\x07\x05",
            "Also, for security reasons, all exits besides\x01",
            "the front entrance will now be sealed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5200794V\x07\x05",
            "We would please ask for your understanding and\x01",
            "to be extremely cautious about using open flames\x01",
            "within the building at this time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x7D0)

    ChrTalk(
        0xE,
        (
            "#5200795V#0304F#11PI guess we're officially on lockdown.\x02\x03",
            "#5200796V#0300FThink I'll head on down to the first floor.\x01",
            "Y'know, just in case it goes south, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200797V#0000F#5PGood idea. I'm going to stock up on supplies\x01",
            "and look over our equipment again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200798V#0302F#11PThanks, man. We're countin' on ya.\x02",
    )

    CloseMessageWindow()

    def lambda_8F90():

        label("loc_8F90")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8F90")

    QueueWorkItem2(0x101, 2, lambda_8F90)
    OP_68(57170, 1500, 860, 2500)
    MoveCamera(119, 22, 0, 2500)
    OP_95(0xE, 58140, 0, -380, 1200, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0xE,
        (
            "#5200799V#0303F#11PYou and I are gonna get worked to the bone if\x01",
            "the CGF breaches this place.\x02\x03",
            "#5200800V#0300FDon't want Mademois-Elie and Tio Tot pushin'\x01",
            "themselves too hard, y'know what I'm sayin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200801V#0004F#5PYeah, I agree.\x02\x03",
            "#5200802V#0000FYou and I will have to figure out a way to\x01",
            "stop their advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200803V#0302F#11PThat's the spirit.\x02\x03",
            "#5200804V#0309FI've got your back...partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200805V#0005F#5POh...\x02\x03",
            "#5200806V#0002FRight back at you!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(550, 8000)
    SetCameraDistance(21500, 8000)
    OP_95(0xE, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xE, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xE, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xE, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xE, 55730, 0, 13960, 2000, 0x0)
    StopBGM(0x2AF8)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_9275():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9275)
    Sleep(1000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xE, 0x1)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F7")
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Randy learned \x07\x02",
            "[Burning Rage 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Their \x07\x02",
            "[Burning Rage]\x07\x05",
            " combo craft was strengthened.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Attack power, range, and area of effect have all been\x01",
            "improved, and they can act sooner after use.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_93F7")

    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    PlayBGM("ed7513", 0)
    SetScenarioFlags(0xE7, 4)
    OP_DE(0x2F, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_14_6683 end

    def Function_15_9454(): pass

    label("Function_15_9454")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(171000, 1400, 123500, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0xA, 171500, 200, 123500, 270)
    SetChrPos(0xB, 171500, 200, 124400, 270)
    MoveCamera(40, 23, 0, 6000)
    SetCameraDistance(19000, 6000)
    FadeToBright(2000, 0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(55000, 1200, 125000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 54500, 30, 124600, 0)
    SetChrPos(0x102, 55500, 30, 124600, 0)
    SetChrPos(0x103, 54300, 30, 123500, 0)
    SetChrPos(0x104, 55700, 30, 123500, 0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 56600, 30, 126100, 315)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(55000, 1200, 126500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#5200359V#5P#2803F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200360V#2901F#11PFather...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200361V#12P#0006FWe don't have evidence decisive enough\x01",
            "to confirm anything right now.\x02\x03",
            "#5200362V#0008FWe'll have to prioritize evidence\x01",
            "collection at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200363V#5P#2800FYou're right... From your perspective,\x01",
            "that's the long and short of it.\x02\x03",
            "#5200364V#2806FHowever, I feel overwhelmingly\x01",
            "disappointed in myself.\x02\x03",
            "#5200365VOf course, the remaining cult members are\x01",
            "partially to blame. However...\x02\x03",
            "#5200366V#2801FI'm dumbfounded at the fools who've associated\x01",
            "with them and allowed this to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200367V#12P#0003FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200368V#5P#2803FI'm more than aware of the sheer complexity\x01",
            "of Crossbell's state of affairs.\x02\x03",
            "#5200369VI understand that the very existence of Revache\x01",
            "and the rampant corruption of our politicians are,\x01",
            "to some extent, unavoidable...\x02\x03",
            "#5200370V#2801FHowever, it seems I was a complete and utter fool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200371V#0108F#12PUncle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200372V#2903F#11PRight you are.\x02\x03",
            "#5200373VIBC is a mammoth of a business and holds\x01",
            "considerable influence over Crossbellan politics.\x02\x03",
            "#5200374V#2901FHowever, Father has intentionally remained neutral\x01",
            "to this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200375V#5P#2801FMy naive laziness is the cause\x01",
            "of our current predicament.\x02\x03",
            "#5200376V#2803FI apologize. I doubt there's much I could do\x01",
            "to make up for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200377V#12P#0011FN-No, I wouldn't go that far.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200378V#12P#0306FHey, don'tcha think you're beatin' yourself\x01",
            "up a lil' too hard over this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200379V#12P#0200FIn reality, you hold no responsibility,\x01",
            "nor was this your duty to prevent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200380V#5P#2800FNo, the financial realm is expected to\x01",
            "have a certain degree of influence over\x01",
            "the political landscape.\x02\x03",
            "#5200381V#2803FMore importantly, I used to be proud\x01",
            "to call myself Crossbellan. I loved my\x01",
            "home...\x02\x03",
            "#5200382V#2801FAs I became busier, I fear that love\x01",
            "faded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200383V#12P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200384V#0106F#12PI think every citizen has that experience at some\x01",
            "point in their life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200385V#5P#2803FMaybe so...\x02\x03",
            "#5200386V#2800FAt any rate, lamenting will get us nowhere.\x02\x03",
            "#5200387VI, Dieter Crois, with the entirety of the\x01",
            "IBC backing me, will give you my full\x01",
            "support to help put an end to this crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200388V#12P#0002FThank you, Mr. Crois. Your assistance\x01",
            "is invaluable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200389V#0102F#12PI feel much more reassured already.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5200390V#5P#2906FRegardless, this situation has us in quite\x01",
            "the predicament.\x02\x03",
            "#5200391V#2901FAll communications with CPD headquarters and\x01",
            "Tangram Gate have been cut off, correct?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F9A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F9A)
    Sleep(50)

    def lambda_9FAA():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FAA)
    Sleep(50)

    def lambda_9FBA():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9FBA)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5200392V#6P#0006FYeah, we've tried to contact them\x01",
            "countless times already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200393V#6P#0206FLogically speaking, there must be a reason\x01",
            "behind the communications interference.\x02\x03",
            "#5200394V#0201FCould we attempt to contact someone directly\x01",
            "through the orbal network?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200395V#5P#2903FOur staff uncovered that someone sabotaged the orbal\x01",
            "cable connected to the Geofront.\x02\x03",
            "#5200396V#2901FI think we may be able to restore the communications\x01",
            "network if we secure a bypass route.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#5200397V#5P#2801FIf that's truly the case, please make it the\x01",
            "top priority of the technology department.\x02\x03",
            "#5200398V#2803FNaturally, we need to get in contact with the police\x01",
            "force, Tangram Gate, and the Bracer Guild...\x02\x03",
            "#5200399V#2800FIf we are able to reconnect to the the terminals\x01",
            "in the city, that should give us a better idea of\x01",
            "the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)

    ChrTalk(
        0x9,
        "#5200400V#2902F#11PYes, Father.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5200401V#5P#2801FThen... I presume your other worry is protecting\x01",
            "KeA, correct?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3A5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A3A5)
    Sleep(50)

    def lambda_A3B5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3B5)
    Sleep(50)

    def lambda_A3C5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3C5)
    Sleep(50)

    def lambda_A3D5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3D5)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#5200402V#12P#0008FYes...\x02\x03",
            "#5200403V#0013FThere's a strong possibility that the manipulated\x01",
            "CGF is pursuing us because we have KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200404V#12P#0303FYou could tell they weren't aimin' to kill\x01",
            "when they opened fire on us.\x02\x03",
            "#5200405V#0301FMeanwhile, the rear unit attacked the\x01",
            "Chief and Dudley without mercy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200406V#12P#0203F'Capture KeA completely unharmed...'\x02\x03",
            "#5200407V#0201FI imagine that was the order ingrained\x01",
            "into their brainwashing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200408V#5P#2904FWell, given how she's cute as a button,\x01",
            "I can relate with wanting to kidnap her.\x02\x03",
            "#5200409V#2901FI believe the man responsible is called Joachim?\x01",
            "He seems like a creep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200410V#12P#0006FWell...\x01",
            "In all honesty, we're not exactly sure what\x01",
            "his motive is, yet.\x02\x03",
            "#5200411V#0008FFor example, why he desires KeA so badly...\x02\x03",
            "#5200412V#0013FAnd, where that photo at the end of the\x01",
            "white file was taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200413V#0106F#12PWe still don't know the details of how KeA\x01",
            "came to be at the auction to begin with.\x02\x03",
            "#5200414V#0108FWe'd have a clue or two to work with if her memories\x01",
            "came back, but we've had no such luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200415V#5P#2901FI see... How vexing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200416V#5P#2803FWell, regardless. He definitely appears to be\x01",
            "the culprit behind all of this mayhem.\x02\x03",
            "#5200417VIt would be wise of you to operate on the belief\x01",
            "that this man is highly dangerous.\x02\x03",
            "#5200418V#2801FI'm confident he can't easily discern\x01",
            "that you're taking shelter inside here.\x02\x03",
            "#5200419VWorst-case scenarios DO happen, however.\x01",
            "It's better to prepare yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200420V#12P#0013FYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200421V#12P#0301FYeah, you're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200422V#5P#2804FLet the IBC staff handle getting into contact\x01",
            "with the appropriate organizations.\x02\x03",
            "#5200423VSince KeA and Shizuku are resting, you\x01",
            "should all take a break while you still can.\x02\x03",
            "#5200424V#2800FWould you like us to prepare some beds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200425V#12P#0002FNo, that's all right. I doubt we'll get much\x01",
            "resting done tonight.\x02\x03",
            "#5200426V#0000FOur equipment isn't looking too great,\x01",
            "so I'm a little more concerned about\x01",
            "stocking up on supplies right now.\x02\x03",
            "#5200427VIs there anywhere in the building that\x01",
            "can take care of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200428V#12P#0306FYeah, they totally caught us with our\x01",
            "pants down back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200429V#5P#2800FIn that case, we have a wide variety of services\x01",
            "available down at the first floor reception desk.\x02\x03",
            "#5200430VMany major manufacturers operate branches\x01",
            "in this building, so we have a wide selection\x01",
            "of weapons to choose from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200431V#5P#2902FThe Epstein Foundation is present, too,\x01",
            "so feel free to use their facilities.\x02\x03",
            "#5200432VWe're always prepared for emergencies,\x01",
            "so we can supply you with food if need be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200433V#0102F#12PAmazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200434V#12P#0202FThe IBC understandably has the ability to hold\x01",
            "every facility in one convenient location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200435V#12P#0309FDamn, the IBC's iconic building never fails\x01",
            "to impress me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200436V#12P#0004FThank you for everything, sir.\x02\x03",
            "#5200437V#0002FWe'll take this opportunity to\x01",
            "catch some rest, then.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Your party has temporarily disbanded.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Speaking with the first floor receptionists will\x01",
            "allow you to use the functions of every shop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Furthermore, you may change equipment and\x01",
            "quartz for any members outside of your party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetMapFlags(0x10000)
    OP_68(53000, 1500, 45000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 53000, 0, 45000, 180)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B19C")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1D5")

    label("loc_B19C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B1BB")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B1D5")

    label("loc_B1BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B1D5")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B1D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B1F4")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B22D")

    label("loc_B1F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B213")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B22D")

    label("loc_B213")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B22D")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B22D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B24C")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B285")

    label("loc_B24C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B26B")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B285")

    label("loc_B26B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B285")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_END)), "loc_B29A")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_END)), "loc_B2AF")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_B2C4")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_END)), "loc_B2D9")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_END)), "loc_B2EE")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_B303")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_END)), "loc_B318")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_END)), "loc_B32D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_B342")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B342")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B38A")
    ClearChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x7)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x10)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_B3C1")

    label("loc_B38A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3A8")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_B3C1")

    label("loc_B3A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3C1")
    ClearChrFlags(0xE, 0x80)

    label("loc_B3C1")

    SetScenarioFlags(0xE3, 7)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_15_9454 end

    def Function_16_B3CD(): pass

    label("Function_16_B3CD")

    EventBegin(0x0)
    Fade(1000)
    OP_68(171500, 900, 122600, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 171000, 0, 121600, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xA,
        "#5200438V#5P#1113F#80WZzz... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200439V#11P#0002F(Haha... She's out like a light.)\x02\x03",
            "#5200440V#0004F(I can't blame her, though. That was a tough fight.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)

    def lambda_B4CA():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B4CA)
    WaitChrThread(0xA, 2)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#5200441V#5P#1114F#80WMmm...\x02\x03",
            "#5200442V#70WLloyd...where are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(21000, 30000)

    ChrTalk(
        0xA,
        (
            "#5200443V#1P#1114F#60W#5PElie... Tio...\x01",
            "Randy...\x02\x03",
            "#5200444VDark... It's so dark...\x02\x03",
            "#5200445VWhere...where has everyone gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200446V#11P#0001F(KeA.)\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(820, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gently caressed KeA's head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200447V#11P#0004FIt's all right. We'll always protect you, KeA.\x02\x03",
            "#5200448V#0002FSo please, rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200449V#5P#1113F#70WMmm...\x02\x03",
            "#5200450V#5P#1104F#70WZzz...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200451V#11P#0008F(We may have been trying our best\x01",
            "this entire time, but...)\x02\x03",
            "#5200452V#0004F(I feel like I've finally come to understand...)\x02\x03",
            "#5200453V(Why I returned to Crossbell.\x01",
            "Why I became a detective.)\x02\x03",
            "#5200454V#0002F(You were the same, weren't you, Guy?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(169830, 1400, 121000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 169830, 0, 121000, 270)
    SetScenarioFlags(0xE4, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_B3CD end

    def Function_17_B883(): pass

    label("Function_17_B883")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    SoundLoad(806)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    ClearMapFlags(0x10000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01100.itp")
    OP_68(55000, 1000, 128000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 55000, 30, 118000, 0)
    SetChrPos(0x102, 56200, 30, 125800, 90)
    SetChrPos(0x103, 54500, 30, 117000, 0)
    SetChrPos(0x104, 55600, 30, 117000, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 57800, 30, 126400, 270)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    SetCameraDistance(18500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5200818V#0001FExcuse me.\x02",
    )

    CloseMessageWindow()
    OP_68(55000, 1000, 126500, 2000)

    def lambda_B9E5():
        OP_95(0xFE, 55000, 0, 124100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B9E5)
    Sleep(200)

    def lambda_BA02():

        label("loc_BA02")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BA02")

    QueueWorkItem2(0x102, 2, lambda_BA02)
    Sleep(100)

    def lambda_BA17():

        label("loc_BA17")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BA17")

    QueueWorkItem2(0x9, 2, lambda_BA17)
    Sleep(1200)

    ChrTalk(
        0x102,
        "#5200819V#5P#0101FLloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5200820V#5P#2800FOh, there you are.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)

    ChrTalk(
        0x101,
        "#5200821V#12P#0001FWhat's the situation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200822V#5P#2803FWell, two of the CGF's squadrons have\x01",
            "reached the front gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5200823V#12P#0013FAnd...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200824V#11P#2903FInterestingly enough, they've ceased\x01",
            "their assault.\x02\x03",
            "#5200825V#2901FEither way, that gate is made of a\x01",
            "special alloy, so breaking through\x01",
            "it would be quite the feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200826V#12P#0006FI see...\x02\x03",
            "#5200827V#0008FOdds are, they've figured out that we're\x01",
            "laying low in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200828V#5P#0106FTrue.\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)

    ChrTalk(
        0x103,
        "#5200829V#0201FSorry we are late.\x02",
    )

    CloseMessageWindow()

    def lambda_BCB5():
        OP_95(0xFE, 55600, 30, 122600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BCB5)

    def lambda_BCCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BCCF)
    Sleep(150)

    def lambda_BCE3():
        OP_95(0xFE, 54500, 30, 122500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BCE3)

    def lambda_BCFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BCFD)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#5200830V#5P#0005FThanks for coming, Tio, Randy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x104,
        (
            "#5200831V#12P#0301FDid I hear that right? The CGF's hunkered down\x01",
            "by the front gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200832V#5P#0001FYeah, they aren't doing anything, though...\x02",
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BE8F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE8F)

    def lambda_BE9C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE9C)

    def lambda_BEA9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BEA9)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5200833V#5P#2801FIt's me.\x02\x03",
            "#5200834V#2805FWhat?\x02\x03",
            "#5200835V#2803FHuh? Hmm...\x02\x03",
            "#5200836V...\x02\x03",
            "#5200837V#2801FWhat did you just say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200838V#12P#0001F(What's wrong?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200839V#0108F(I don't like the sound of this...)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5200840V#5P#2803FThey are engaging in some kind of peculiar activity.\x02\x03",
            "#5200841V#2801FThey're supposedly installing some cylinder-shaped\x01",
            "devices near the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5200842V#12P#0201FDo not tell me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200843V#12P#0307FDirectional orbal bombs?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C15B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C15B)
    Sleep(50)

    def lambda_C16B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C16B)
    Sleep(50)

    def lambda_C17B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C17B)

    ChrTalk(
        0x101,
        "#5200844V#5P#0011FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200845V#12P#0301FIt's a type of orbal bomb used in the\x01",
            "military for sabotage operations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200846V#12P#0206FIt pains me to state this, but I am unsure your\x01",
            "special alloy gate will be able to withstand the\x01",
            "explosion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200847V#5P#0101FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5200848V#5P#2801FDarn it. To resort to such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200849V#11P#2901FFor a bunch of puppets being manipulated,\x01",
            "they're fairly intelligent.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    ChrTalk(
        0x101,
        (
            "#5200850V#5P#0003FWell, I guess we have no other choice.\x02\x03",
            "#5200851V#0000FIt's time, Randy. Let's head out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200852V#12P#0304FYou read my mind...\x01",
            "We're outta options at this point.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C461():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C461)

    ChrTalk(
        0x8,
        "#5200853V#5P#2805FLloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200854V#11P#2910FAre you two trying to get yourselves killed?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#5200855V#6P#0000FNot in the slightest. We're going to disarm\x01",
            "that orbal bomb.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200856V#12P#0309FWell, we're probably gonna have a few scuffles\x01",
            "at this rate, but you can ignore that part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200857V#5P#0100FYou weren't planning on leaving us behind,\x01",
            "were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200858V#12P#0202FIt is our duty as fellow SSS members\x01",
            "to fight with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200859V#6P#0000FYeah, of course... We'll be counting on\x01",
            "your support!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200860V#11P#2901FElie, Tio...\x02",
    )

    CloseMessageWindow()

    def lambda_C6AE():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C6AE)
    Sleep(100)
    TurnDirection(0x103, 0x9, 500)
    Sleep(200)

    ChrTalk(
        0x102,
        "#5200861V#6P#0109FIt's just a part of the job, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200862V#12P#0204FNo need to worry.\x02",
    )

    CloseMessageWindow()

    def lambda_C72C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C72C)
    Sleep(150)

    def lambda_C73C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C73C)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#5200863V#12P#0004FRest assured, we have no intention of dying here.\x02\x03",
            "#5200864V#0000FBe it the CPD, or Deputy Commander Baelz's squad...\x01",
            "We'll hold the line until reinforcements arrive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200865V#12P#0300FWe've got the high ground in front of the gate, too.\x02\x03",
            "#5200866VWe can handle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5200867V#5P#2803FVery well, then.\x02\x03",
            "#5200868V#2801FMay Aidios' protection be your shield...\x01",
            "...and please, be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(52700, 1100, 45900, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 52200, 0, 46500, 180)
    SetChrPos(0x102, 53200, 0, 46500, 180)
    SetChrPos(0x103, 52200, 0, 46500, 180)
    SetChrPos(0x104, 53200, 0, 46500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 52700, 0, 46500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xA, 56500, 0, 38800, 270)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xB, 56500, 0, 38800, 270)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(52700, 1100, 39800, 4000)

    def lambda_CA70():
        OP_96(0xFE, 0xCB84, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CA70)

    def lambda_CA8A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CA8A)
    Sleep(400)

    def lambda_CA9E():
        OP_96(0xFE, 0xD034, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CA9E)

    def lambda_CAB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CAB8)
    Sleep(400)

    def lambda_CACC():
        OP_96(0xFE, 0xCB84, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CACC)

    def lambda_CAE6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CAE6)
    Sleep(400)

    def lambda_CAFA():
        OP_96(0xFE, 0xD034, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CAFA)

    def lambda_CB14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CB14)
    Sleep(700)

    def lambda_CB28():
        OP_96(0xFE, 0xCDDC, 0x0, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CB28)

    def lambda_CB42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CB42)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_CB9C():

        label("loc_CB9C")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_CB9C")

    QueueWorkItem2(0x101, 2, lambda_CB9C)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_CBCA():

        label("loc_CBCA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_CBCA")

    QueueWorkItem2(0x102, 2, lambda_CBCA)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_CBF8():

        label("loc_CBF8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_CBF8")

    QueueWorkItem2(0x103, 2, lambda_CBF8)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_CC26():

        label("loc_CC26")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_CC26")

    QueueWorkItem2(0x104, 2, lambda_CC26)

    def lambda_CC38():

        label("loc_CC38")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_CC38")

    QueueWorkItem2(0x9, 2, lambda_CC38)
    Sleep(1000)
    OP_79(0x1)
    OP_79(0x2)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)
    Fade(500)
    OP_68(53200, 1100, 39730, 0)
    MoveCamera(67, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)

    def lambda_CC8C():
        OP_95(0xFE, 54100, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CC8C)

    def lambda_CCA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CCA6)
    Sound(2040, 255, 100, 0)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)
    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xA,
        "#5200870V#40WWhere are you guys going?\x02",
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
        0x101,
        "#5200871V#6P#0005FOh, you're awake, KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200872V#5P#0309FHaha... Nothin' to worry about, kiddo.\x01",
            "Just a lil' job we gotta take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200873V#11P#1100FHmm...\x02\x03",
            "#5200874V#1109FCan I come with you, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200875V#5P#0108FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200876V#6P#0208FHow do we put this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200877V#6P#0003FSorry, KeA. But it's about time\x01",
            "for you to head to bed, right?\x02\x03",
            "#5200878V#0000FShizuku was already sound\x01",
            "asleep, so why don't you--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CF36():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CF36)

    def lambda_CF50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CF50)
    WaitChrThread(0xB, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CFB0():

        label("loc_CFB0")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_CFB0")

    QueueWorkItem2(0x102, 2, lambda_CFB0)

    def lambda_CFC2():

        label("loc_CFC2")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_CFC2")

    QueueWorkItem2(0x103, 2, lambda_CFC2)
    WaitChrThread(0xB, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    OP_93(0xB, 0x12C, 0x1F4)

    ChrTalk(
        0x102,
        "#5200879V#5P#0105FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200880V#5P#0306FThe racket musta woke her up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5200881V#11P#6005FS-Sorry...\x01",
            "I know I should be asleep, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200882V#6P#0002FNo...\x01",
            "It's our fault for being so loud.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200883V#12P#0003FMariabell, can we leave\x01",
            "these two in your care?\x02\x03",
            "#5200884V#0000FWe'd appreciate it if you\x01",
            "could get them back to bed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x9,
        "#5200885V#2904F#5POf course. I'll see to it.\x02",
    )

    CloseMessageWindow()

    def lambda_D196():

        label("loc_D196")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_D196")

    QueueWorkItem2(0x101, 2, lambda_D196)
    OP_68(53790, 1100, 39870, 1000)

    def lambda_D1B9():
        OP_95(0xFE, 54700, 0, 41500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D1B9)
    WaitChrThread(0x9, 1)

    def lambda_D1D7():
        OP_95(0xFE, 54700, 0, 40000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D1D7)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        (
            "#5200886V#5P#2902FHow about I make you both some cocoa, okay?\x02\x03",
            "#5200887VIt'll warm you right up, and then it's nighty-night.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D279():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D279)
    Sleep(50)
    TurnDirection(0xB, 0x9, 500)

    ChrTalk(
        0xA,
        "#5200888V#11P#1112F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5200889V#11P#6008F...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 5000)
    BeginChrThread(0xB, 3, 0, 18)
    BeginChrThread(0xA, 3, 0, 19)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_D2E3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D2E3)
    Sleep(50)

    def lambda_D2F3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D2F3)
    Sleep(50)

    def lambda_D303():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D303)
    Sleep(50)

    def lambda_D313():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D313)
    WaitChrThread(0x101, 2)

    def lambda_D324():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D324)
    Sleep(50)

    def lambda_D341():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D341)
    Sleep(50)

    def lambda_D35E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D35E)
    Sleep(50)

    def lambda_D37B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D37B)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x9, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7513", "ed7512")
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c133B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_B883 end

    def Function_18_D3E7(): pass

    label("Function_18_D3E7")


    def lambda_D3EC():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D3EC)
    Sleep(300)

    def lambda_D409():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D409)
    WaitChrThread(0xB, 1)
    Return()

    # Function_18_D3E7 end

    def Function_19_D41A(): pass

    label("Function_19_D41A")

    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(500)

    def lambda_D429():
        OP_96(0xFE, 0xDCB4, 0x0, 0x9790, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D429)
    Sleep(500)

    def lambda_D446():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D446)
    WaitChrThread(0xA, 1)
    Return()

    # Function_19_D41A end

    def Function_20_D457(): pass

    label("Function_20_D457")

    Sleep(900)

    def lambda_D45F():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D45F)
    WaitChrThread(0x9, 1)

    def lambda_D47D():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D47D)
    Sleep(300)

    def lambda_D49A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D49A)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_D457 end

    def Function_21_D4AB(): pass

    label("Function_21_D4AB")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an exquisite doll that exhibits lifelike features.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_21_D4AB end

    SaveToFile()

Try(main)
