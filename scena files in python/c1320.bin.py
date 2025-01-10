from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1320.bin",                # FileName
        "c1320",                    # MapName
        "c1320",                    # Location
        0x001F,                     # MapIndex
        "ed7522",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 31, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1320",                  # 0
        "Mariabell",              # 1
        "Researcher Clay",        # 2
        "Researcher David",       # 3
        "Chief Roberts",          # 4
        "Tio",                    # 5
        "Chief Guillaume",        # 6
        "SE制御",                 # 7
    ))

    AddCharChip((
        "chr/ch32800.itc",                   # 00
        "chr/ch29400.itc",                   # 01
        "chr/ch05500.itc",                   # 02
        "chr/ch32802.itc",                   # 03
        "chr/ch29402.itc",                   # 04
        "chr/ch29302.itc",                   # 05
        "chr/ch00202.itc",                   # 06
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4699,    -379,    22700,   45,   341,  0x0, 0,   3,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  341,  0x0, 0,   4,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       18239,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  469,  0x0, 0,   6,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 30,  70.63999938964844,     24.0,                  9.5,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -35.31999969482422,    -8.0,                  -1.9000002145767212,   1.0])

    ScpFunction((
        "Function_0_250",          # 00, 0
        "Function_1_308",          # 01, 1
        "Function_2_554",          # 02, 2
        "Function_3_55B",          # 03, 3
        "Function_4_60A",          # 04, 4
        "Function_5_2313",         # 05, 5
        "Function_6_406F",         # 06, 6
        "Function_7_46EE",         # 07, 7
        "Function_8_4DFE",         # 08, 8
        "Function_9_5635",         # 09, 9
        "Function_10_5A20",        # 0A, 10
        "Function_11_5C9B",        # 0B, 11
        "Function_12_6190",        # 0C, 12
        "Function_13_8BE0",        # 0D, 13
        "Function_14_8C0D",        # 0E, 14
        "Function_15_8C5B",        # 0F, 15
        "Function_16_8CAC",        # 10, 16
        "Function_17_8CFD",        # 11, 17
        "Function_18_8D4E",        # 12, 18
        "Function_19_8D99",        # 13, 19
        "Function_20_8E08",        # 14, 20
        "Function_21_8E64",        # 15, 21
        "Function_22_8EC7",        # 16, 22
        "Function_23_8F23",        # 17, 23
        "Function_24_8F8C",        # 18, 24
        "Function_25_8FAF",        # 19, 25
        "Function_26_9704",        # 1A, 26
        "Function_27_9A76",        # 1B, 27
        "Function_28_AACC",        # 1C, 28
        "Function_29_AAE4",        # 1D, 29
        "Function_30_AB00",        # 1E, 30
    ))


    def Function_0_250(): pass

    label("Function_0_250")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_290"),
        (1, "loc_29C"),
        (2, "loc_2A8"),
        (3, "loc_2B4"),
        (4, "loc_2C0"),
        (5, "loc_2CC"),
        (6, "loc_2D8"),
        (SWITCH_DEFAULT, "loc_2E4"),
    )


    label("loc_290")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_29C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2A8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2B4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2C0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2CC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_307")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F0")

    label("loc_307")

    Return()

    # Function_0_250 end

    def Function_1_308(): pass

    label("Function_1_308")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_329")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_348")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_357")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37B")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 700, -600, 13500, 0)

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_3DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_END)), "loc_3A1")
    ClearChrFlags(0xC, 0x80)

    label("loc_3A1")

    Jump("loc_3AB")

    label("loc_3A6")

    ClearChrFlags(0xC, 0x80)

    label("loc_3AB")

    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_544")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EC")
    Jump("loc_544")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FF")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_544")

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_40D")
    Jump("loc_544")

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_41B")
    Jump("loc_544")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_496")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -1070, 0, -640, 135)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1070, 0, -2590, 45)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 640, 0, -1590, 270)
    SetChrFlags(0x8, 0x10)
    Jump("loc_544")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4D2")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_544")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E0")
    Jump("loc_544")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FF")
    SetChrPos(0xA, 0, 0, 18240, 0)
    Jump("loc_544")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_536")
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4070, -480, 20560, 45)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x40)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_544")

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_END)), "loc_544")
    ClearChrFlags(0x8, 0x80)

    label("loc_544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_553")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 27)

    label("loc_553")

    Return()

    # Function_1_308 end

    def Function_2_554(): pass

    label("Function_2_554")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_554 end

    def Function_3_55B(): pass

    label("Function_3_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_577")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_589")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_589")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589")

    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_5EB")
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_5F1")

    label("loc_5EB")

    OP_10(0x2, 0x1)
    OP_10(0x3, 0x0)

    label("loc_5F1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_609")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_609")

    Return()

    # Function_3_55B end

    def Function_4_60A(): pass

    label("Function_4_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_8DF")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A7")
    Jump("loc_6F1")

    label("loc_6A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F1")

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F1")

    label("loc_6E7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7A9")

    ChrTalk(
        0xFE,
        "Leave restoring the orbal network to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We may not look the part, but we're actually\x01",
            "orbal network system administrators!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D3")

    label("loc_7A9")


    ChrTalk(
        0xFE,
        (
            "The computing system developed for the second\x01",
            "stage of the project should prove useful here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, it's well suited for analyzing\x01",
            "major systems like the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know who's responsible for obstructing the\x01",
            "network, but watch and learn! We'll outwit this saboteur!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_8D3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_8DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_BAF")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97C")
    Jump("loc_9C6")

    label("loc_97C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C6")

    label("loc_99C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9C6")

    label("loc_9BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A9E")

    ChrTalk(
        0xFE,
        (
            "We'll clean up this mess in record time to give\x01",
            "the mistress a pleasant surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet she'll lather us with her sweet, sweet\x01",
            "praise if we pull this off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA3")

    label("loc_A9E")


    ChrTalk(
        0xFE,
        (
            "We're creating a specialized system from the\x01",
            "ground up to use in large-scale networks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once we finally wrap this up, we should be\x01",
            "ready for the second stage of the project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet our mistress will reward us handsomely\x01",
            "if everything goes well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BA3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAA")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4C")
    Jump("loc_C96")

    label("loc_C4C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C6C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C96")

    label("loc_C6C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C96")

    label("loc_C8C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C96")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "We're grateful for the help Chief Roberts\x01",
            "has been providing us with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As one of its original developers, Chief Roberts\x01",
            "is a specialist when it comes to the orbal network.\x01",
            "Oh, man, is it reassuring to have him around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1004")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E47")
    Jump("loc_E91")

    label("loc_E47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E91")

    label("loc_E67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E91")

    label("loc_E87")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E91")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F10")

    ChrTalk(
        0xFE,
        (
            "We have to do everything we can to surpass\x01",
            "the mistress' expectations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_F10")


    ChrTalk(
        0xFE,
        (
            "The orbal network's operations appear to\x01",
            "remain stable thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't be much longer until we can proceed\x01",
            "to the second stage of the project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right! You just wait and see...\x01",
            "We'll make this plan a success!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FF8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_12C6")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A1")
    Jump("loc_10EB")

    label("loc_10A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10C1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10EB")

    label("loc_10C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10EB")

    label("loc_10E1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10EB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11D2")

    ChrTalk(
        0xFE,
        (
            "The hacker may have wreaked havoc on the mainframe,\x01",
            "but the network itself remains unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like the orbal network is finally back to\x01",
            "operating at a stable level.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_11D2")


    ChrTalk(
        0xFE,
        (
            "Thanks to the hacker the other day, the load average\x01",
            "on the network spiked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've got the orbal network operating under\x01",
            "stable conditions again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, Miss Crois had plenty of reasons\x01",
            "to give us a harsh scolding.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12BA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_12C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_13E9")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_13DE")

    ChrTalk(
        0xFE,
        (
            "Our systems detected a hacker running amok\x01",
            "in the network yesterday evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wh-When we traced the connection,\x01",
            "we discovered some...interesting data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hey, I'm not slacking off! I've been sitting\x01",
            "here trying to collect the hacker's data.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E1")

    label("loc_13DE")

    Call(0, 10)

    label("loc_13E1")

    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_13E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1659")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1486")
    Jump("loc_14D0")

    label("loc_1486")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14D0")

    label("loc_14A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14D0")

    label("loc_14C6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14D0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_164A")

    ChrTalk(
        0xFE,
        (
            "I managed to find it among a bunch of\x01",
            "other random files.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figure this was the hacker's work, but...\x01",
            "What the heck was the point behind\x01",
            "all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll just print out a copy of it for now,\x01",
            "for evidence's sake.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_164D")

    label("loc_164A")

    Call(0, 9)

    label("loc_164D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_19CD")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16F6")
    Jump("loc_1740")

    label("loc_16F6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1716")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1740")

    label("loc_1716")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1736")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1740")

    label("loc_1736")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1740")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_183D")

    ChrTalk(
        0xFE,
        (
            "Honestly, I've never been more proud to work\x01",
            "on something than the Orbal Network Project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been working my butt off to make sure\x01",
            "I repay Miss Crois for scouting me out in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C1")

    label("loc_183D")


    ChrTalk(
        0xFE,
        "You see, I was originally an academic researcher.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One day, Miss Crois appeared out of nowhere and\x01",
            "offered me a position at the IBC's tech department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The IBC's orbal network aims to connect terminals\x01",
            "throughout Zemuria in order to transfer customer\x01",
            "data in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once I heard about it, I knew I couldn't sit still\x01",
            "and allow for this opportunity to slip away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19C1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D16")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A6A")
    Jump("loc_1AB4")

    label("loc_1A6A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A8A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AB4")

    label("loc_1A8A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AAA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AB4")

    label("loc_1AAA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AB4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BE0")

    ChrTalk(
        0xFE,
        (
            "More and more businesses have been opting into\x01",
            "using the orbal network as of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just as we finally got more terminals, the festival\x01",
            "brought a ton of data, which overloaded our servers...\x01",
            "We'll have to come up with some countermeasures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0A")

    label("loc_1BE0")


    ChrTalk(
        0xFE,
        (
            "Okay, I give up... There is just way too much stress\x01",
            "on the server from all this Anniversary Festival data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still, this situation is far beyond what we anticipated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the way things are proceeding, the entire\x01",
            "network will become unstable. We have to do\x01",
            "something about this...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D0A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_1D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_202C")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DB3")
    Jump("loc_1DFD")

    label("loc_1DB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFD")

    label("loc_1DD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DF3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DFD")

    label("loc_1DF3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DFD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F0E")

    ChrTalk(
        0xFE,
        (
            "Chief Roberts from the Epstein Foundation is one of the\x01",
            "leading figures in the development of the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He knows it like the back of his hand, so it's no surprise\x01",
            "we borrow his wisdom from time to time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2020")

    label("loc_1F0E")


    ChrTalk(
        0xFE,
        "*sigh* What a pain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That darn hacker cleverly devised a system to\x01",
            "exploit the system's code in order to worm\x01",
            "their way into our network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is too much for us to handle on our own...\x01",
            "I think we should probably ask Chief Roberts\x01",
            "for his assistance again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2020")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2312")

    label("loc_202C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20C0")
    Jump("loc_210A")

    label("loc_20C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_210A")

    label("loc_20E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2100")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_210A")

    label("loc_2100")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_210A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21D6")

    ChrTalk(
        0xFE,
        (
            "I don't want the mistress to find\x01",
            "out about our failure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it! We've gotta track down the source\x01",
            "of this ASAP!\x01",
            "(*click* *clack* *click*!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_230B")

    label("loc_21D6")


    ChrTalk(
        0xFE,
        (
            "How was an official IBC terminal breached\x01",
            "from an outside source?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I'm so ashamed of myself... If a disaster like\x01",
            "this happens while the system is up and running,\x01",
            "I would never be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to hurry up and figure out the method so\x01",
            "that I can start working on a countermeasure!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_230B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_2312")

    Return()

    # Function_4_60A end

    def Function_5_2313(): pass

    label("Function_5_2313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_23C7")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hah. This machine's power was made especially\x01",
            "for trying times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just leave this to us! We'll have a bypass route\x01",
            "up and running in a jiffy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_23C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2760")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2464")
    Jump("loc_24AE")

    label("loc_2464")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2484")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24AE")

    label("loc_2484")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24AE")

    label("loc_24A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25A3")

    ChrTalk(
        0xFE,
        "Clay and I are constructing a brand new system.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We didn't really have much choice, considering the\x01",
            "current system is riddled with bugs...\x01",
            "Reexamining the code is downright depressing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2754")

    label("loc_25A3")


    ChrTalk(
        0xFE,
        (
            "I only noticed it recently, but there's a system\x01",
            "node that's been acting a little strangely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My initial impression was that we're being hacked.\x01",
            "But, it's weird... All they're doing is looking into\x01",
            "the network without actually causing any damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, where the heck's this terminal hiding?\x01",
            "...Mainz Mountain Path...Rosenberg Studio?\x01",
            "What the heck?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, there's another bug hiding somewhere\x01",
            "in the system...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2754")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_2760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_293D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27FD")
    Jump("loc_2847")

    label("loc_27FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_281D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2847")

    label("loc_281D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_283D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2847")

    label("loc_283D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2847")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Miss Crois is in a particularly bad mood today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's her problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we're hiding down here in this basement,\x01",
            "it feels like we're secluding ourselves from any\x01",
            "current events.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C6A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29DA")
    Jump("loc_2A24")

    label("loc_29DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A24")

    label("loc_29FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A1A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A24")

    label("loc_2A1A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A24")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B73")

    ChrTalk(
        0xFE,
        (
            "The plan for the second stage is to expand our\x01",
            "userbase, thus increasing the number of terminals\x01",
            "linked to the grid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why we're in the process of developing a new\x01",
            "system that can handle the heavier load... There's\x01",
            "nothing else we can do, now that we've come this far!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5E")

    label("loc_2B73")


    ChrTalk(
        0xFE,
        (
            "We told the mistress our test plans for the second stage,\x01",
            "and she seemed to really like them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All those long nights and hard labor\x01",
            "were worth it in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right! I'm going to do everything I can to\x01",
            "gather data!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C5E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_2C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2EE2")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D07")
    Jump("loc_2D51")

    label("loc_2D07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D27")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D51")

    label("loc_2D27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D51")

    label("loc_2D47")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D51")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DE6")

    ChrTalk(
        0xFE,
        (
            "We take your personal privacy seriously...\x01",
            "We need stronger countermeasures against hackers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED6")

    label("loc_2DE6")


    ChrTalk(
        0xFE,
        (
            "We've all decided that we're going to delete\x01",
            "any inappropriate files floating around on the\x01",
            "orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess we need to be more careful\x01",
            "with personal information...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Miss Crois really got on our cases\x01",
            "thanks to that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2ED6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_2EE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30BB")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30B0")

    ChrTalk(
        0xFE,
        (
            "We happened to find a very interesting--I mean,\x01",
            "inappropriate image on the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I definitely should have reported it to\x01",
            "our mistress as soon as I found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it was a shot of her very attractive\x01",
            "swimsuit figure from when she was a student.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AB")

    ChrTalk(
        0x101,
        "#0005F(You're kidding... Was that one of Jona's pranks?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I do seem to recall him mentioning scattering bait...\x01",
            "This may be said bait.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AB")

    Jump("loc_30B3")

    label("loc_30B0")

    Call(0, 10)

    label("loc_30B3")

    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_30BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3262")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 3)), scpexpr(EXPR_END)), "loc_3257")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_318F")

    ChrTalk(
        0xFE,
        (
            "Hey, Clay! This isn't fair! Be a pal\x01",
            "and print me a copy, too, will you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_3252")

    label("loc_318F")


    ChrTalk(
        0xFE,
        (
            "And, I'm begging you. PLEASE don't mention\x01",
            "a word of this to Miss Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She'd have our heads on a platter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FThat does not sound like my problem.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    OP_9E(0xA, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)

    label("loc_3252")

    Jump("loc_325A")

    label("loc_3257")

    Call(0, 9)

    label("loc_325A")

    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_3262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_35F0")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32FF")
    Jump("loc_3349")

    label("loc_32FF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_331F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3349")

    label("loc_331F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_333F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3349")

    label("loc_333F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3349")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3472")

    ChrTalk(
        0xFE,
        (
            "Apparently, there's been some hacker trying\x01",
            "to force their way into our systems all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right. I'll trace their location and figure out who they are!\x01",
            "After all, the first step in a war against hackers is to\x01",
            "collect their data!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E4")

    label("loc_3472")


    ChrTalk(
        0xFE,
        (
            "Since the orbal network's still in its developmental\x01",
            "phase, we run into a ton of different bugs and issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A hacker? I can really only think of\x01",
            "one possible location...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have a research facility over in Leman State\x01",
            "that's directly connected to the network, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...no one over there would ever try to hack\x01",
            "into the network, so that's a bust.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_35E4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_35F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_392A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_368D")
    Jump("loc_36D7")

    label("loc_368D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36AD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36D7")

    label("loc_36AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36D7")

    label("loc_36CD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36D7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37D7")

    ChrTalk(
        0xFE,
        (
            "Still, us admins need to brace for impact and\x01",
            "make sure the network doesn't go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't even imagine how mad she'd be... Just thinking\x01",
            "about it makes me want to curl up into a ball and die.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391E")

    label("loc_37D7")


    ChrTalk(
        0xFE,
        (
            "Keeping the orbal network running securely,\x01",
            "without any kinks in the system, is a feat in\x01",
            "itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a matter of fact, one of our processors\x01",
            "broke down yesterday. We pulled an all-nighter\x01",
            "trying to fix the blasted thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everyone's out enjoying the Anniversary Festival,\x01",
            "so it feels a little empty in here...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_391E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_392A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3B0D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_39C7")

    ChrTalk(
        0xA,
        (
            "If we don't come up with a way to combat the\x01",
            "hacker quickly, Miss Crois is going to punish\x01",
            "us again... W-We need to hurry up!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B05")

    label("loc_39C7")


    ChrTalk(
        0xA,
        "Huh. A breach from a place like that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Shouldn't it be impossible to pull something like\x01",
            "this off if you don't have the source code?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, that's exactly what I was thinking.\x01",
            "How are we supposed to track them down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our hacker friend seems to be awfully\x01",
            "familiar with how our system works...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)

    label("loc_3B05")

    TalkEnd(0xFE)
    Jump("loc_406E")

    label("loc_3B0D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BA1")
    Jump("loc_3BEB")

    label("loc_3BA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BC1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BEB")

    label("loc_3BC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BE1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BEB")

    label("loc_3BE1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BEB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3E33")

    ChrTalk(
        0xFE,
        (
            "I mean, if we can't figure some way to\x01",
            "counter this, Miss Crois is going to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, never mind.\x01",
            "Pretend you didn't hear anything, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4D")

    ChrTalk(
        0x101,
        "#0005F(I-I really feel for these guys.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2E")

    label("loc_3D4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DAB")

    ChrTalk(
        0x102,
        (
            "#0106F(Geez, Bell. You've been tormenting your\x01",
            "workers, haven't you?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E2E")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE6")

    ChrTalk(
        0x103,
        "#0200F(Are they going to survive?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2E")

    label("loc_3DE6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E2E")

    ChrTalk(
        0x104,
        "#0300F(Haha. That chick's like an unpinned grenade.)\x02",
    )

    CloseMessageWindow()

    label("loc_3E2E")

    Jump("loc_4067")

    label("loc_3E33")


    ChrTalk(
        0xFE,
        "Either way, that came off as a shock to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the first time I've ever witnessed a\x01",
            "tracing method like that in action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FYou can thank the Aeon system packaged\x01",
            "within the orbal staff's code for that. I would\x01",
            "otherwise be waving around a plain metal rod.\x02\x03",
            "#0200FMore importantly, are you able to handle the\x01",
            "situation from here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, you've been incredibly helpful.\x01",
            "We can take care of the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll clean up the remainder of this mess. Things\x01",
            "may have gone south, but we're still orbal network\x01",
            "researchers down to our cores!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4067")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_406E")

    Return()

    # Function_5_2313 end

    def Function_6_406F(): pass

    label("Function_6_406F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40A6")
    Call(0, 26)
    Return()

    label("loc_40A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_4342")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4143")
    Jump("loc_418D")

    label("loc_4143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4163")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_418D")

    label("loc_4163")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4183")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_418D")

    label("loc_4183")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_418D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4221")

    ChrTalk(
        0xFE,
        "Leave the orbal network to me and my crew!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll have it up and running in a few hours!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4336")

    label("loc_4221")


    ChrTalk(
        0xFE,
        "Leave the orbal network to me and my crew!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My analysis shows that a device was\x01",
            "attached to the network cable that sends\x01",
            "out waves of interference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're all incredibly skilled. Give us a few hours,\x01",
            "and the orbal network will be chugging along\x01",
            "like new again!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_4336")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_46ED")

    label("loc_4342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_43D7")

    ChrTalk(
        0xFE,
        (
            "Hmhmhmm... ♪\x01",
            "(*furiously typing*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Are his fingers even hitting the keyboard?\x01",
            "How is this speed humanly possible?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EA")

    label("loc_43D7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_446B")
    Jump("loc_44B5")

    label("loc_446B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_448B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44B5")

    label("loc_448B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44AB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44B5")

    label("loc_44AB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44B5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "I was asked by the folks at the IBC to lend a\x01",
            "bit of my genius to the project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're smack dab in the middle of coding a system\x01",
            "for the Orbal Network Project's second stage test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(They brought the chief out from the Epstein Foundation?\x01",
            "Their work today must be terribly difficult.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(Chief Roberts can actually be quite proficient when\x01",
            "he keeps his mouth shut and himself busy.)\x02\x03",
            "#0200F(As of now, he is classified as one of the continent's\x01",
            "leading minds in the field of orbal technology.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 2)

    label("loc_46EA")

    TalkEnd(0xFE)

    label("loc_46ED")

    Return()

    # Function_6_406F end

    def Function_7_46EE(): pass

    label("Function_7_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4B0E")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4873")

    ChrTalk(
        0x8,
        (
            "#2904FWell, they're fairly quick when it comes to\x01",
            "solving technical problems, aren't they?\x02\x03",
            "#2900FThe trick is to berate them at fixed intervals\x01",
            "in order to double their working efficiency.\x01",
            "It's been working wonders for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FTh-That's kind of messed up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(Bell sometimes gives off the impression of a\x01",
            "ruthless queen when she speaks...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B06")

    label("loc_4873")


    ChrTalk(
        0x8,
        "#2903FHmm. This is fairly difficult, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FIs something wrong, Bell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI've gotta say, this room never ceases\x01",
            "to amaze me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2900FIn fact, we're beginning the testing phase for\x01",
            "the second stage of the Orbal Network Project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe second stage testing phase...\x01",
            "I believe introducing the general populace to\x01",
            "the orbal terminals is the intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2903FYes, well. We have a long way to go before\x01",
            "we can sell terminals to the public.\x02\x03",
            "We're more concerned with the construction of a\x01",
            "more efficient, large-scale network...\x02\x03",
            "#2900FAlthough there's many hurdles to overcome,\x01",
            "it's still an endeavor worth tackling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4B06")

    TalkEnd(0x8)
    Jump("loc_4DFD")

    label("loc_4B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4CB1")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4CA6")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x102,
        (
            "#0103FBell... About you tormenting\x01",
            "your subordinates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2905FOh, my. I wouldn't go so far as to say\x01",
            "I'm tormenting my dear worker bees.\x02\x03",
            "#2904F...Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 300)
    TurnDirection(0xA, 0x0, 300)

    NpcTalk(
        0x9,
        "Clay & David",
        "Of course, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_9E(0xA, 0x0, 0x0, 0x20F58, 0x0, 0x0)
    OP_9E(0x9, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_4CA9")

    label("loc_4CA6")

    Call(0, 10)

    label("loc_4CA9")

    TalkEnd(0x8)
    Jump("loc_4DFD")

    label("loc_4CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CC7")
    Call(0, 25)
    Jump("loc_4DFD")

    label("loc_4CC7")

    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "#2900FLooks like our little hacker is hiding somewhere\x01",
            "inside the Geofront's B Sector.\x02\x03",
            "#2903FThe Geofront is managed by City Hall, so\x01",
            "your first order of business is to receive\x01",
            "their permission.\x02\x03",
            "#2900FShould you manage to solve the case,\x01",
            "I would love to hear the details on how\x01",
            "you pulled it off.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_4DFD")

    Return()

    # Function_7_46EE end

    def Function_8_4DFE(): pass

    label("Function_8_4DFE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E92")
    Jump("loc_4EDC")

    label("loc_4E92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EB2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EDC")

    label("loc_4EB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4ED2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EDC")

    label("loc_4ED2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4EDC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_END)), "loc_52DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51AA")

    ChrTalk(
        0xC,
        "#0205FOh, Lloyd. You're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FHey, Tio. Looks like the staff were quick\x01",
            "to ask for your help.\x02\x03",
            "I know you said you'd try to contact Jona,\x01",
            "but do you think he's all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0204FLikely.\x02\x03",
            "#0202FJona has placed back doors in various terminals\x01",
            "across the city to simplify the hacking process.\x02\x03",
            "As long as we have access to the terminals, we should be\x01",
            "able to reach him, and he can inform us of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FS-Seriously?\x01",
            "Well, what about contacting outside sources?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0204FI am still working on that issue...\x02\x03",
            "#0202FSince the situation has become dire, I'll have\x01",
            "Jona repay every last bit of debt he owes me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52D9")

    label("loc_51AA")


    ChrTalk(
        0xC,
        (
            "#0204FAs for providing me with assistance, I alone should suffice.\x01",
            "There is no need for concern.\x02\x03",
            "#0202FPlease consider resting after you have completed\x01",
            "resupplying, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D9")

    ChrTalk(
        0x101,
        (
            "#0004FDon't worry, I will.\x02\x03",
            "#0002FThat applies to you, too. Don't go too crazy\x01",
            "and overwork yourself, Tio.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_52D9")

    Jump("loc_562D")

    label("loc_52DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5586")

    ChrTalk(
        0x101,
        (
            "#0002FI'm guessing you've decided to help them\x01",
            "restore the orbal network, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#0203FYes, but I am working on a few more things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FOh? Like what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0202FI am currently trying to contact Jona.\x02\x03",
            "He has placed back doors in various terminals\x01",
            "across the city to simplify the hacking process.\x02\x03",
            "#0204FAs long as we have access to the terminals, we should be\x01",
            "able to reach him. Then he can inform us of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FS-Seriously?\x01",
            "Well, what about contacting outside sources?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0204FI am still working on that issue...\x02\x03",
            "#0202FSince the situation has become dire, I'll have\x01",
            "Jona repay every last bit of debt he owes me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_562D")

    label("loc_5586")


    ChrTalk(
        0xC,
        (
            "#0204FAs long as we have access to the control\x01",
            "terminals, we should be able to contact Jona.\x02\x03",
            "#0202FI will see to it that he cooperates with us,\x01",
            "so do not worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_4DFE end

    def Function_9_5635(): pass

    label("Function_9_5635")

    OP_4B(0xA, 0xFF)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x9, 0x0, 1000)
    TurnDirection(0xA, 0x0, 1000)
    Sleep(1000)
    OP_64(0x9)
    OP_64(0xA)

    ChrTalk(
        0x9,
        (
            "Wh-What? Oh, it's just you guys.\x01",
            "Don't scare me like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FSuspicious... Has something gone wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "O-Oh, nothing much. Just a bit of a situation.\x01",
            "Some peculiar data started transferring\x01",
            "through the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah, I was totally blown away by that sexy photo\x01",
            "of Miss Crois in a swimsuit from her student days\x01",
            "popping up on the network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Talk about hitting the jackpot.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "W-Wait! We're not just screwing around, okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I-I swear, we only found it by chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Who is capable of getting their hands on this\x01",
            "kind of...sensitive data?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(You're kidding... Was that one of Jona's pranks?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I do seem to recall him mentioning scattering bait...\x01",
            "This may be said bait.)\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    OP_9E(0x9, 0x0, 0x0, 0xAFC8, 0x0, 0x0)
    SetScenarioFlags(0xB2, 3)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_5635 end

    def Function_10_5A20(): pass

    label("Function_10_5A20")

    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "I can't believe you hand-delivered us\x01",
            "some delicious snacks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I-I'm moved to tears by your kindness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2904FI'm not so shallow that I wouldn't reward\x01",
            "my beloved workers during the Anniversary\x01",
            "Festival.\x02\x03",
            "#2900FSo... How is the Orbal Network Project\x01",
            "proceeding? Do you have any updates?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "N-Not particularly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeeeeeep! Everything is A-OK here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2902FYou pigs are hiding something, aren't you?\x01",
            "I'll give you three seconds to spit it out,\x01",
            "before I force it out of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "W-We're terribly sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "We'll tell you! Just don't yell at us, please!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_10_5A20 end

    def Function_11_5C9B(): pass

    label("Function_11_5C9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(69400, 11000, 24000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 72500, 10000, 23700, 270)
    SetChrPos(0x102, 72500, 10000, 24300, 270)
    SetChrPos(0x103, 72500, 10000, 23700, 270)
    SetChrPos(0x104, 72500, 10000, 24300, 270)
    SetChrPos(0x138, 72500, 10000, 24000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(160, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    OP_68(67400, 11000, 24000, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_5DB0():
        OP_96(0xFE, 0x1016C, 0x2710, 0x5DC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_5DB0)

    def lambda_5DCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_5DCA)
    Sleep(800)

    def lambda_5DDE():
        OP_96(0xFE, 0x108D8, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DDE)

    def lambda_5DF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DF8)
    Sleep(400)

    def lambda_5E0C():
        OP_96(0xFE, 0x108D8, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E0C)

    def lambda_5E26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5E26)
    Sleep(400)

    def lambda_5E3A():
        OP_96(0xFE, 0x10D24, 0x2710, 0x5B68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E3A)

    def lambda_5E54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E54)
    Sleep(400)

    def lambda_5E68():
        OP_96(0xFE, 0x10D24, 0x2710, 0x6018, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E68)

    def lambda_5E82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E82)
    WaitChrThread(0x138, 1)
    WaitChrThread(0x101, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_93(0x138, 0x5A, 0x1F4)

    ChrTalk(
        0x138,
        (
            "#2200645V#6P#2904FWelcome to B5F. This floor houses the IBC's\x01",
            "main terminal.\x02\x03",
            "#2200646V#2900FThe terminal room is right down the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200647V#0001F#11PYou pulled out all the stops securing this place,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200648V#6P#2903FOf course. We're considering storing all our\x01",
            "clientele's data here eventually.\x02\x03",
            "#2200649V#2901FSince we lack any safeguards against hackers,\x01",
            "we have to play it by ear in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200650V#11P#0101FThat's worriesome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200651V#11P#0206FWe could have a national scandal on our hands\x01",
            "if client data were to leak, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200652V#6P#2904FThat's correct. And for that reason, we're\x01",
            "still in the development stages.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 68000, 10000, 24000, 270)
    SetScenarioFlags(0x82, 6)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_5C9B end

    def Function_12_6190(): pass

    label("Function_12_6190")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadEffect(0x0, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(10000, 1100, 0, 0)
    MoveCamera(55, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 10500, 0, -500, 270)
    SetChrPos(0x102, 10500, 0, 500, 270)
    SetChrPos(0x103, 10500, 0, -500, 270)
    SetChrPos(0x104, 10500, 0, 500, 270)
    SetChrPos(0x138, 10500, 0, 0, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    StopBGM(0x5DC)
    FadeToBright(1000, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    BeginChrThread(0x138, 3, 0, 14)
    BeginChrThread(0x101, 3, 0, 15)
    BeginChrThread(0x102, 3, 0, 16)
    BeginChrThread(0x103, 3, 0, 17)
    BeginChrThread(0x104, 3, 0, 19)
    OP_68(0, 1100, 0, 5000)
    OP_6F(0x1)
    OP_68(0, 1100, 16500, 8000)
    MoveCamera(30, 13, 0, 8000)
    SetCameraDistance(25500, 8000)
    WaitChrThread(0x138, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 500, 12500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#2200653V#12P#0005FW-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200654V#0306FMan, I'm freakin' blown away. Is this what\x01",
            "the future looks like?\x02\x03",
            "#2200655V#0301FThe IBC's goin' balls to the wall with this\x01",
            "state-of-the-art tech, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200656V#12P#0204FThis is the latest, cutting-edge information processing\x01",
            "system developed by the Epstein Foundation.\x02\x03",
            "#2200657V#0202FI believe Liberl's high-speed cruiser also utilizes\x01",
            "a similar system.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    ChrTalk(
        0x138,
        (
            "#2200658V#2904FAh, you must be referring to the famous Arseille.\x02\x03",
            "#2200659V#2902FThe systems they use are essentially the same,\x01",
            "but there's one major difference.\x02\x03",
            "#2200660VWe've increased the processing power several fold\x01",
            "to handle the vast network of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200661V#0105FIncredible...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        "#2200662V#6PMiss Crois?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200663V#4PG-Good morning, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(300)
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(2000)
    OP_68(0, 500, 13000, 1000)

    def lambda_66F2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_66F2)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)

    ChrTalk(
        0x138,
        (
            "#2200664V#11P#2900FHeehee. Thank you. I hope the same for you.\x02\x03",
            "#2200665VI trust the project is proceeding smoothly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200666V#11POf course. All thanks to your continued support.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200667V#5POur recent simulations are proving to be\x01",
            "extremely successful...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0xA,
        "#2200668V#5PErm, sorry. Who exactly are these guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200669V#11P#2900FThey're with the Crossbell Police Department.\x02\x03",
            "#2200670VOh, by the way. There's a possibility that our\x01",
            "main terminal has been hacked into by an\x01",
            "external source.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6947():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6947)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#2200671V#11P#4SWHAAAAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200672V#5PH-Hacked?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200673V#12P#0003FWell...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2200674V#5P#0001FTio, mind explaining the situation to them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200705V#12P#0200FYes, allow me.\x02",
    )

    CloseMessageWindow()
    OP_68(0, 500, 13280, 1000)

    def lambda_6A45():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A45)
    Sleep(150)

    def lambda_6A62():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A62)
    Sleep(100)

    def lambda_6A72():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6A72)
    WaitChrThread(0x103, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio adeptly explained the situation using\x01",
            "complex terminology to the researchers.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x9,
        "#2200676V#11PSomebody hacked into the network?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200677V#11PI can't deny that the possibility exists, but\x01",
            "I'm in total disbelief that it actually happened.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        "#2200678V#1PNo! This should be impossible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200679V#1PI refuse to accept that somebody out there could\x01",
            "hack into our system this easily!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200680V#11P#2904FIf you're this adamant, then we'll have to assume\x01",
            "that one of you two sent the orbmail.\x02\x03",
            "#2200681V#2902FHeehee... So. Which of you two is Yin?\x01",
            "Cough it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6D24():
        TurnDirection(0xFE, 0x138, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6D24)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x9,
        "#2200682V#11PH-Hold on a second! That's crazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200683V#5PWe must have been hacked because\x01",
            "the two of us are completely worthless!\x02",
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
        "#2200684V#12P#0012F(He's, uh...being pretty hard on himself.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200685V#0300F(Mariabell reminds me of a queen, kinda like Ilya.\x01",
            "Granted, a more dominant one. But still...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200686V#11P#2903FThe Special Support Section's terminal\x01",
            "received the orbmail around 3AM...\x02\x03",
            "#2200687V#2901FBe a doll and look through the logs\x01",
            "around that time period, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200688V#11PY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200689V#5PWe'll look through them right away!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, 21500, 3500)
    MoveCamera(45, 27, 0, 3500)
    SetCameraDistance(23000, 3500)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(200)
    BeginChrThread(0xA, 3, 0, 23)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    Sleep(200)
    Sound(849, 0, 100, 0)
    Sleep(1300)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#2200690V#6PH-Here it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2200691V#6PThe orbmail's encryption algorithm was cracked\x01",
            "right under our noses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200692V#0101FIt's as we thought...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200693V#0303FPretty solid evidence our hacker's comin' from\x01",
            "outside the IBC, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200694V#11PHold on, I'll trace his point of access!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200695V#11POkay, the point of access is...\x01",
            "No good. I lost it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200696V#0001FSo, we still have no idea where the hacker\x01",
            "managed to enter the system from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200697V#11PYeah. This guy knows what he's doing. He managed\x01",
            "to erase any trace of tampering with the system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200698V#11PThe most I can confirm with complete confidence\x01",
            "is that he used a terminal somewhere in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#2200699V#2901FOh... He's good. Really good.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 500, 12500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    ChrTalk(
        0x103,
        "#2200700V#12P#0200FMay I use the terminal for a moment?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x2)
    Sleep(300)

    ChrTalk(
        0x9,
        "#2200701V#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200702V#4PB-But...\x02",
    )

    CloseMessageWindow()

    def lambda_7431():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_7431)
    WaitChrThread(0x138, 1)

    ChrTalk(
        0x138,
        (
            "#2200703V#11P#2904FGo ahead, sweetheart.\x02\x03",
            "#2200704V#2900FYou're Tio, right? You can tinker with our\x01",
            "system as much as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200675V#6P#0204FThank you. I will begin, then.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(0, 800, 18600, 3000)
    MoveCamera(40, 27, 0, 3000)
    SetCameraDistance(18000, 3000)
    SetChrSubChip(0x9, 0x0)

    def lambda_752D():

        label("loc_752D")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_752D")

    QueueWorkItem2(0x138, 2, lambda_752D)

    def lambda_753F():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_753F)
    WaitChrThread(0x103, 1)

    def lambda_755D():
        OP_95(0xFE, 0, -300, 17300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_755D)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 0, -200, 18600, 0)
    Sound(820, 0, 100, 0)
    OP_0D()
    EndChrThread(0x138, 0x2)
    OP_6F(0x79)
    Sleep(500)
    Sound(1278, 255, 100, 0)
    Sleep(1500)
    Sound(1280, 255, 100, 0)
    Sleep(2000)
    PlayEffect(0x0, 0x0, 0x103, 0x140, 0, 1250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(840, 2, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)

    ChrTalk(
        0x101,
        "#2200706V#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200707V#0101FTio?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#2200708V#2905FIs she...?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 1, 0, 24)
    Fade(500)
    OP_68(0, 800, 20500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "event")
    BeginChrThread(0x103, 3, 0, 13)
    SetCameraDistance(22500, 20000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2200709V#0201F#30WAttempting real-time control by\x01",
            "multidimensional analysis.\x02\x03",
            "#2200710VAnalyzing all terminal logs.\x01",
            "Examining all suspicious logins\x01",
            "leaving traces of concealment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200711V#5PSh-She's amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200712V#11PWhat is this insane processing speed?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200713V#0203FPlease support me, you two.\x02\x03",
            "#2200714V#0202FAccessing all Crossbell terminals\x01",
            "with administrator privileges.\x02\x03",
            "#2200715VI am transferring any suspicious logins to you,\x01",
            "so please examine them for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200716V#5PR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200717V#11PWe can handle it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 500, 14500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 500, 12500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_6F(0x1)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#2200718V#6P#0008FElie, are you following any of this?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#2200719V#0106F#11PN-No, not in the slightest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200720V#0309FI'm glad I'm not the only one that\x01",
            "doesn't know what's goin' on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200721V#5P#2904FNow I see. Tio is an orbal staff user.\x02\x03",
            "#2200722V#2902FWhile that impressive piece of technology allows\x01",
            "for the instantaneous use of magic...\x02\x03",
            "#2200723V...it also functions as a conduit for\x01",
            "augmented control of terminals.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B3E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B3E)
    Sleep(100)
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#2200724V#12P#0005FY-You understand what's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200725V#0100F#11PWell, Bell studied orbal engineering at the\x01",
            "Epstein Foundation, so it's no surprise she\x01",
            "is a bit familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200726V#2904F#5PYou could say I know a thing or\x01",
            "two about orbal technology.\x02",
        )
    )

    CloseMessageWindow()
    StopEffect(0x0, 0x2)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "event_stop")
    SetMapObjFrame(0xFF, "monita4_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "monita3_add", 0x1, 0x1)
    Sound(863, 0, 100, 0)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0xE, 0x1)
    OP_24(0x348)
    Sleep(800)
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x138, 0x0, 0x1F4)

    ChrTalk(
        0x138,
        "#2200727V#5P#2900FIt looks like they're just about finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200728V#0305FOh, sweet.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 800, 20500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        "#2200729V#0200F#6PHow was everything on your end?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200730V#11PAll of my stuff looks clean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200731V#11PHow about you, Clay?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#2200732V#5PBingo! I got it!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(200)
    SetMapObjFrame(0xFF, "monita5_add", 0x1, 0x1)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#2200733V#5PControl Terminal 8 in the Geofront's\x01",
            "B Sector...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2200734V#5PWe detected an unauthorized login from there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200735V#0001FThe Geofront...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200736V#0301FSo, our lil' rat snuck underground in that\x01",
            "area right near Station Street, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200737V#0203FYou are mistaken. That location leads to\x01",
            "the Geofront's A Sector.\x02\x03",
            "#2200738V#0201FThe terminal accessed by the hacker\x01",
            "was in Geofront B Sector...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#2200739V#11PUh... Looks like it's somewhere underneath\x01",
            "the northwestern part of the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(500)
    OP_68(0, 500, 14500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 0, -300, 17300, 0)
    BeginChrThread(0x103, 3, 0, 18)
    OP_68(0, 500, 12500, 2500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0xA, 3, 0, 22)

    ChrTalk(
        0x102,
        (
            "#2200740V#0103F#11PThe northwestern part of Crossbell City...\x01",
            "That should be the Residential District and\x01",
            "the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#2200741V#0101F#11PWhat's the plan, Lloyd?\x02",
    )

    CloseMessageWindow()

    def lambda_81E9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_81E9)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)

    ChrTalk(
        0x101,
        (
            "#2200742V#6P#0003FI say we head there immediately.\x02\x03",
            "#2200743V#0001FCity Hall should be responsible for all Geofront access,\x01",
            "if I remember correctly.\x02\x03",
            "#2200744VLet's start by asking the receptionist if we can borrow\x01",
            "the key for that sector.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200745V#0300FSounds like a swell plan to me.\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x138,
        (
            "#2200746V#2904FInching towards the truth\x01",
            "of this case, are we?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_837F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_837F)
    Sleep(50)

    def lambda_838F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_838F)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2200747V#12P#0000FYeah, I'd say so. We couldn't have done it\x01",
            "without your cooperation, Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200748V#0102F#11PThank you, Bell. You two, as well.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)

    def lambda_8451():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8451)
    Sleep(50)
    OP_93(0xA, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        "#2200749V#5PD-Don't mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#2200750V#5PForget us. This lady is the real champion.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_84E4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E4)
    Sleep(150)

    def lambda_84F4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_84F4)
    Sleep(50)

    def lambda_8504():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_8504)

    def lambda_8511():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8511)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2200751V#12P#0004FYou don't say?\x02\x03",
            "#2200752V#0002FGreat work, Tio. I can't pretend I have any idea\x01",
            "what you did, but you unquestionably helped us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200753V#0109F#11PHeehee. Good job, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200754V#0302FC'mon, guys. What were you expecting?\x01",
            "Tio Tot's nothin' short of perfection.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#2200755V#6P#0205FHmm? I don't believe I did anything extraordinary.\x02\x03",
            "#2200756V#0203FBesides, I'm a member of the Special Support\x01",
            "Section, too. It is the least I could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200757V#11P#2909FHeehee. That was no small feat, missy.\x02\x03",
            "#2200758V#2902FI have a proposition for you, Tio.\x02\x03",
            "#2200759VHow would you and Elie like to\x01",
            "come work for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200760V#6P#0205FHmm?\x02",
    )

    CloseMessageWindow()

    def lambda_87E2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_87E2)
    Sleep(50)

    def lambda_87F2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87F2)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        "#2200761V#0101F#11PC-Come on, Bell. Cut it out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200762V#0302FHaha. You scoutin' our members out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200763V#12P#0012FI'd much rather our team stick together...\x02",
    )

    CloseMessageWindow()

    def lambda_88B9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_88B9)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x138,
        (
            "#2200764V#2904FOh, settle down. I was just kidding.\x02\x03",
            "#2200765V#2900FFill me in on the details once you've\x01",
            "managed to solve the case.\x02\x03",
            "#2200766VAnd, another thing. I'll just leave that\x01",
            "key card in your hands for the time being.\x02\x03",
            "#2200767VIt will give you access to the top floor, as\x01",
            "well as this one. Make use of it as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200768V#0104F#11PThank you, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200769V#12P#0000FThanks again. Now, if you'll excuse us.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    RemoveParty(0x37, 0x0)
    OP_D5(0x1E)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 700, -600, 13500, 0)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x8000)
    OP_68(0, 1100, 10300, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, -600, 10300, 180)
    SetChrPos(0x1, 0, -600, 10300, 180)
    SetChrPos(0x2, 0, -600, 10300, 180)
    SetChrPos(0x3, 0, -600, 10300, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x82, 7)
    OP_29(0x43, 0x1, 0x4)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x20A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7102")
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_6190 end

    def Function_13_8BE0(): pass

    label("Function_13_8BE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8C0C")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_13_8BE0")

    label("loc_8C0C")

    Return()

    # Function_13_8BE0 end

    def Function_14_8C0D(): pass

    label("Function_14_8C0D")


    def lambda_8C12():
        OP_95(0xFE, 0, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_8C12)

    def lambda_8C2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_8C2C)
    WaitChrThread(0x138, 1)

    def lambda_8C41():
        OP_95(0xFE, 0, -600, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_8C41)
    WaitChrThread(0x138, 1)
    Return()

    # Function_14_8C0D end

    def Function_15_8C5B(): pass

    label("Function_15_8C5B")

    Sleep(800)

    def lambda_8C63():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C63)

    def lambda_8C7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8C7D)
    WaitChrThread(0x101, 1)

    def lambda_8C92():
        OP_95(0xFE, -500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C92)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_8C5B end

    def Function_16_8CAC(): pass

    label("Function_16_8CAC")

    Sleep(1300)

    def lambda_8CB4():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CB4)

    def lambda_8CCE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8CCE)
    WaitChrThread(0x102, 1)

    def lambda_8CE3():
        OP_95(0xFE, 500, -600, 11100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CE3)
    WaitChrThread(0x102, 1)
    Return()

    # Function_16_8CAC end

    def Function_17_8CFD(): pass

    label("Function_17_8CFD")

    Sleep(1700)

    def lambda_8D05():
        OP_95(0xFE, -500, 0, -500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D05)

    def lambda_8D1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8D1F)
    WaitChrThread(0x103, 1)

    def lambda_8D34():
        OP_95(0xFE, -1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D34)
    WaitChrThread(0x103, 1)
    Return()

    # Function_17_8CFD end

    def Function_18_8D4E(): pass

    label("Function_18_8D4E")

    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_8D5A():
        OP_95(0xFE, 0, -600, 14700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D5A)
    WaitChrThread(0x103, 1)

    def lambda_8D78():
        OP_95(0xFE, -1400, -600, 12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D78)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_18_8D4E end

    def Function_19_8D99(): pass

    label("Function_19_8D99")

    Sleep(2200)

    def lambda_8DA1():
        OP_95(0xFE, 500, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DA1)

    def lambda_8DBB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8DBB)
    Sleep(1000)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x104, 1)

    def lambda_8DEE():
        OP_95(0xFE, 1100, -600, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8DEE)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_8D99 end

    def Function_20_8E08(): pass

    label("Function_20_8E08")

    Fade(150)
    SetChrPos(0x9, 3500, -380, 21500, 45)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    def lambda_8E2C():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E2C)
    WaitChrThread(0x9, 1)

    def lambda_8E4A():
        OP_95(0xFE, 1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E4A)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_8E08 end

    def Function_21_8E64(): pass

    label("Function_21_8E64")

    OP_93(0x9, 0x2D, 0x1F4)

    def lambda_8E70():
        OP_95(0xFE, 3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E70)
    WaitChrThread(0x9, 1)

    def lambda_8E8E():
        OP_95(0xFE, 3500, -480, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E8E)
    WaitChrThread(0x9, 1)
    Fade(250)
    SetChrPos(0x9, 4700, -380, 22700, 45)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Return()

    # Function_21_8E64 end

    def Function_22_8EC7(): pass

    label("Function_22_8EC7")

    Fade(150)
    SetChrPos(0xA, -3500, -380, 21700, 315)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    def lambda_8EEB():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8EEB)
    WaitChrThread(0xA, 1)

    def lambda_8F09():
        OP_95(0xFE, -1000, -600, 14300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F09)
    WaitChrThread(0xA, 1)
    Return()

    # Function_22_8EC7 end

    def Function_23_8F23(): pass

    label("Function_23_8F23")

    OP_93(0xA, 0x13B, 0x1F4)

    def lambda_8F2F():
        OP_95(0xFE, -3500, -600, 16800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F2F)
    WaitChrThread(0xA, 1)

    def lambda_8F4D():
        OP_95(0xFE, -3500, -600, 22200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8F4D)
    WaitChrThread(0xA, 1)
    Fade(250)
    SetChrPos(0xA, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_23_8F23 end

    def Function_24_8F8C(): pass

    label("Function_24_8F8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FAE")
    Sound(849, 0, 100, 0)
    Sleep(950)
    Sound(850, 0, 100, 0)
    Sleep(1750)
    Jump("Function_24_8F8C")

    label("loc_8FAE")

    Return()

    # Function_24_8F8C end

    def Function_25_8FAF(): pass

    label("Function_25_8FAF")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(1000)
    OP_68(700, 400, 12300, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x8, 700, -600, 13500, 180)
    SetChrPos(0x101, 700, -600, 11700, 0)
    SetChrPos(0x102, 1300, -600, 10600, 0)
    SetChrPos(0x103, -900, -600, 11300, 45)
    SetChrPos(0x104, -200, -600, 10400, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#2200770V#2904F#5PNow, this may just be my intuition speaking...\x02\x03",
            "#2200771V#2902F...but I believe it's likely that the sender of the orbmail\x01",
            "and this Yin character are two different people.\x02\x03",
            "#2200772VOur sender clearly is knowledgeable about orbal\x01",
            "engineering. They may even be connected to\x01",
            "the Epstein Foundation. Who knows?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2200773V#0011FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200774V#0105FY-You managed to figure that out from intuition?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2200775V#6P#0203FI agree with your assessment. I have already\x01",
            "considered the same scenario.\x02\x03",
            "#2200776VThe orbal network is currently restricted to people\x01",
            "who understand advanced network technology...\x02\x03",
            "#2200777V#0208FAnd, despite it being used for hacking, I feel as\x01",
            "if I've seen this method deployed before.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_937A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_937A)
    Sleep(100)

    def lambda_938A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_938A)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x101,
        "#2200778V#0001F#5PYou have?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200779V#2904F#5POh, and in case you find our dear little hacker...\x02\x03",
            "#2200780V#2902FI want you to let him get off free, so please\x01",
            "don't do anything to him.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9464():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9464)
    Sleep(100)

    def lambda_9474():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9474)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#2200781V#0005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2200782V#0105FB-But, why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2200783V#2909F#5PThere is currently no legislation strictly\x01",
            "prohibiting any acts of hacking.\x02\x03",
            "#2200784VAs a matter of fact, I've deemed that he was\x01",
            "a useful tool in advancing our network's\x01",
            "security protocol.\x02\x03",
            "#2200785V#2902FWe've been meaning to create a defense system\x01",
            "against hacking now that we're orbalizing banking.\x02",
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
        0x102,
        "#2200786V#0106F*sigh* Oh, Bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2200787V#12P#0302FDamn. Chick's got stones, I'll give 'er that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 700, -600, 11500, 0)
    SetChrPos(0x8, 700, -600, 13500, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x83, 0)
    EventEnd(0x5)
    Return()

    # Function_25_8FAF end

    def Function_26_9704(): pass

    label("Function_26_9704")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9798")
    Jump("loc_97E2")

    label("loc_9798")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97B8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97E2")

    label("loc_97B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97D8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97E2")

    label("loc_97D8")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97E2")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "Oh, that reminds me...\x01",
            "How did the orbal staff upgrade go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I remember you were planning to gather\x01",
            "the materials, but did you ever get\x01",
            "around to doing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, yeah. Sorry about that.\x02\x03",
            "We managed to gather everything we needed,\x01",
            "but we were too busy to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, really?\x01",
            "What a shame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I would imagine that reinforcing Tio's\x01",
            "combat capabilities would be beneficial\x01",
            "in times like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm always ready for the upgrade, so please\x01",
            "speak with Guillaume if you'd still like to\x01",
            "upgrade her staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Bit of a lucky break that he has access\x01",
            "to all the tools he needs here.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x31, 0x1, 0x2)
    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_26_9704 end

    def Function_27_9A76(): pass

    label("Function_27_9A76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x28)
    LoadChrToIndex("chr/ch26400.itc", 0x29)
    LoadChrToIndex("chr/ch00200.itc", 0x2A)
    OP_68(-200, 1100, 12300, 0)
    MoveCamera(23, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13040, 0)
    SetChrPos(0x101, -70, -600, 12460, 45)
    SetChrPos(0xC, -1120, -600, 12910, 90)
    SetChrPos(0xB, -80, -600, 14300, 225)
    SetChrPos(0xD, 1130, -600, 13670, 225)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "I'm done verifyin' the required materials.\x01",
            "We're ready to roll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "All right, everything's ready.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0xB,
        (
            "Haha. I'm looking forward to this!\x01",
            "I can already picture Tio, gallantly\x01",
            "brandishing her new orbal staff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0200FChief.\x02\x03",
            "If the orbal staff is rendered useless thanks to\x01",
            "a bug, you will be punished. Do you understand?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "N-No way... A-Anything but that, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "What have I done to deserve this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#2PUh, Chief. Nothing's happened yet.\x01",
            "Take a deep breath and relax.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "Come back to us, Roberts.\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xB,
        "H-Huh?!\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x190)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "O-Oh, sorry.\x01",
            "Let's go ahead and begin the process, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Do you mind waiting a little bit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#2PYeah, no problem. We'll just sit here\x01",
            "and watch you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others spent the next thirty\x01",
            "minutes observing the process.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They were unable to understand the details, but\x01",
            "the orbal staff upgrade proceeded smoothly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "And then...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -4700, 0, -620, 90)
    SetChrPos(0xC, 1960, 0, -560, 270)
    SetChrPos(0xB, 1140, 0, 1320, 180)
    SetChrPos(0xD, 3470, 0, 1260, 225)
    OP_68(1050, 1700, -1130, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00257.itc", 0x1F)
    LoadChrToIndex("chr/ch0025A.itc", 0x20)
    LoadEffect(0x0, "battle\\cr002403.eff")
    LoadEffect(0x1, "battle\\cr002401.eff")
    SetChrChipByIndex(0xC, 0x1E)
    BeginChrThread(0xC, 0, 0, 28)
    SetCameraDistance(25500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0xC, 0x1F)
    OP_A0(0xC, 1500, 0x0, 0x2)
    Sleep(300)
    OP_A0(0xC, 1500, 0x2, 0x3)
    Sound(279, 0, 100, 0)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(363, 0, 100, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(274, 0, 100, 0)
    Sleep(100)
    Fade(300)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(2500)
    PlayEffect(0x1, 0xFF, 0xC, 0xC0, 200, 550, 850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 90, 0)
    Sound(323, 0, 90, 0)
    Sleep(4500)
    Fade(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 28)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0xC,
        "#0200FWell, then...\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)
    Fade(300)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    OP_0D()
    TurnDirection(0xC, 0xB, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#0200FI feel some discomfort due to the code having\x01",
            "been completely overwritten. It is not terrible,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bet it's due to the balance control. If anyone can\x01",
            "get used to it, it'd be you, Tio. I believe in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please copy any programs utilized by the\x01",
            "Aeon system when you change to a\x01",
            "different orbal staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Also, please don't forget to install any\x01",
            "of the attachments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#0200FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Still, I can work a heckuva lot faster usin'\x01",
            "the main machine. A man could get used\x01",
            "to this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "At this rate, I may even consider relocatin'\x01",
            "my shop down here!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Hahaha. I made a backup of the orbal staff's\x01",
            "core system, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hopefully, that'll let me be able to provide\x01",
            "even more thorough tune-ups for you, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0200FI would prefer not to habitually rely on your\x01",
            "help, Chief. However...\x02\x03",
            "...thanks to you, the program has become\x01",
            "approximately seven percent lighter.\x01",
            "I am anxious to try it in a real combat situation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A553():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A553)

    def lambda_A560():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A560)
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "Ah-ha! You love all of the new\x01",
            "improvements, don't you? ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(70)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(70)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(300)
    Fade(800)
    OP_68(-3750, 1700, -1220, 0)
    MoveCamera(41, 28, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21140, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0000FI-I'm getting the impression that they've\x01",
            "made her staff much more impressive.\x02\x03",
            "So, um, Tio. Did everything go well?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xC, 0x101, 400)

    def lambda_A6FE():
        OP_95(0xFE, -2500, 0, -380, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A6FE)
    Sleep(800)

    def lambda_A71B():
        OP_95(0xFE, -1120, 0, 810, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A71B)
    Sleep(100)
    BeginChrThread(0xD, 1, 0, 29)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xC,
        (
            "#0200F#2PYes, the upgrade is complete. I should be\x01",
            "able to perform all of the new functions\x01",
            "efficiently and without error.\x02\x03",
            "'Absolute Zero' allows me to launch\x01",
            "anti-energy bullets at zero degrees.\x02\x03",
            "Though I cannot fire them excessively,\x01",
            "I imagine they will prove quite useful\x01",
            "in more intense fights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FReally? Well, that's reassuring.\x02\x03",
            "(Though if I'm being totally honest...\x01",
            "I'd rather not involve her in an intense\x01",
            "situation that needs her to use it.)\x02\x03",
            "It's times like this where we have to give it\x01",
            "our all, Tio. I'll be counting on you and that\x01",
            "nifty new staff of yours, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0200F#2PHeehee. Understood, Lloyd.\x02\x03",
            "After all, I've found something that\x01",
            "I wish to protect...\x02\x03",
            "Let's continue to push our limits, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FRight!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    AddCraft(0x2, 0xAE)
    SubItemNumber(0x397, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -750, 0, 630, 180)
    SetChrPos(0xB, 0, 0, 18240, 0)
    SetChrPos(0xC, -4700, -380, 22700, 315)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAB1")
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)

    label("loc_AAB1")

    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_27_9A76 end

    def Function_28_AACC(): pass

    label("Function_28_AACC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAE3")
    OP_A0(0xC, 1200, 0x0, 0x4)
    Jump("Function_28_AACC")

    label("loc_AAE3")

    Return()

    # Function_28_AACC end

    def Function_29_AAE4(): pass

    label("Function_29_AAE4")

    OP_95(0xFE, -750, 0, -990, 1200, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Return()

    # Function_29_AAE4 end

    def Function_30_AB00(): pass

    label("Function_30_AB00")

    EventBegin(0x1)

    ChrTalk(
        0x138,
        (
            "#2905FDidn't you come here to see the\x01",
            "terminal room?\x02\x03",
            "#2900FRemember, the main terminal is just up ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, right. You said it was just down\x01",
            "these stairs.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 67810, 10000, 23760, 270)
    EventEnd(0x4)
    Return()

    # Function_30_AB00 end

    SaveToFile()

Try(main)
