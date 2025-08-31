from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0450.bin",                # FileName
        "c0450",                    # MapName
        "c0450",                    # Location
        0x0024,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 36, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0450",                  # 0
        "Receptionist Kyle",      # 1
        "Doris",                  # 2
        "Aeron",                  # 3
        "Manager Leticia",        # 4
        "Gantz",                  # 5
        "Mayor Bickson",          # 6
        "Chief Roberts",          # 7
        "Tront",                  # 8
    ))

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch27500.itc",                   # 02
        "chr/ch27900.itc",                   # 03
        "apl/ch50409.itc",                   # 04
        "chr/ch23200.itc",                   # 05
        "chr/ch29300.itc",                   # 06
        "chr/ch24400.itc",                   # 07
    ))

    DeclNpc(65440,   0,       59970,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4090,    9,       59900,   225,  261,  0x0, 0,   1,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(50740,   0,       9750,    90,   261,  0x0, 0,   2,   0,   0,   1,   0,   10,  255,  0)
    DeclNpc(-3990,   0,       7000,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(162000,  649,     5900,    90,   406,  0x0, 0,   4,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(162000,  0,       4500,    0,    389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(3549,    0,       4360,    45,   389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(114809,  0,       61029,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(-3500,   0,       7000,    1500,    -3990,   1500,    7000,    0x007E, 0,  6,  0x0000)
    DeclActor(64300,   0,       59970,   1500,    65440,   1500,    59970,   0x007E, 0,  8,  0x0000)
    DeclActor(68130,   10,      11650,   1200,    68130,   1500,    11650,   0x007C, 0,  14, 0x0000)
    DeclActor(162620,  0,       6480,    1200,    161500,  1500,    5570,    0x007E, 0,  15, 0x0000)

    ScpFunction((
        "Function_0_28C",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_3A5",          # 02, 2
        "Function_3_3D0",          # 03, 3
        "Function_4_3FB",          # 04, 4
        "Function_5_64E",          # 05, 5
        "Function_6_76C",          # 06, 6
        "Function_7_770",          # 07, 7
        "Function_8_1CF8",         # 08, 8
        "Function_9_1CFC",         # 09, 9
        "Function_10_2C62",        # 0A, 10
        "Function_11_38F6",        # 0B, 11
        "Function_12_4528",        # 0C, 12
        "Function_13_50C2",        # 0D, 13
        "Function_14_55AA",        # 0E, 14
        "Function_15_55DA",        # 0F, 15
        "Function_16_56E2",        # 10, 16
        "Function_17_5A90",        # 11, 17
        "Function_18_8681",        # 12, 18
        "Function_19_86C6",        # 13, 19
        "Function_20_86E2",        # 14, 20
        "Function_21_86FE",        # 15, 21
        "Function_22_871A",        # 16, 22
        "Function_23_8736",        # 17, 23
        "Function_24_8752",        # 18, 24
        "Function_25_9339",        # 19, 25
    ))


    def Function_0_28C(): pass

    label("Function_0_28C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2CC"),
        (1, "loc_2D8"),
        (2, "loc_2E4"),
        (3, "loc_2F0"),
        (4, "loc_2FC"),
        (5, "loc_308"),
        (6, "loc_314"),
        (SWITCH_DEFAULT, "loc_320"),
    )


    label("loc_2CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_2FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_308")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_314")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_32C")

    label("loc_343")

    Return()

    # Function_0_28C end

    def Function_1_344(): pass

    label("Function_1_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A4")
    OP_95(0xFE, 72280, 0, 9750, 1000, 0x0)
    OP_95(0xFE, 72280, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 5580, 1000, 0x0)
    OP_95(0xFE, 50740, 0, 9750, 1000, 0x0)
    Jump("Function_1_344")

    label("loc_3A4")

    Return()

    # Function_1_344 end

    def Function_2_3A5(): pass

    label("Function_2_3A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_94(0xFE, 0x604, 0xD714, 0x17C0, 0xFB9A, 0x3E8)
    Sleep(300)
    Jump("Function_2_3A5")

    label("loc_3CF")

    Return()

    # Function_2_3A5 end

    def Function_3_3D0(): pass

    label("Function_3_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FA")
    OP_94(0xFE, 0xFAD1, 0x141E, 0x11B66, 0x2652, 0x3E8)
    Sleep(300)
    Jump("Function_3_3D0")

    label("loc_3FA")

    Return()

    # Function_3_3D0 end

    def Function_4_3FB(): pass

    label("Function_4_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_40A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_428")
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_64D")

    label("loc_428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    Jump("loc_64D")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_48E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0xA, -2009, 0, 9290, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)

    label("loc_489")

    Jump("loc_64D")

    label("loc_48E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4B0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_64D")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4BE")
    Jump("loc_64D")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4E0")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_64D")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EE")
    Jump("loc_64D")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_553")
    SetChrPos(0xA, 4550, 0, 5360, 225)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_524")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_54E")

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_537")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_54E")

    label("loc_537")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_54E")

    label("loc_549")

    ClearChrFlags(0xE, 0x80)

    label("loc_54E")

    Jump("loc_64D")

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_561")
    Jump("loc_64D")

    label("loc_561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5AC")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xA, 4550, 0, 5360, 225)
    SetChrPos(0x9, 68150, 0, 7780, 225)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_64D")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5ED")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 4550, 0, 5360, 225)
    SetChrPos(0x9, 68150, 0, 7780, 225)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_64D")

    label("loc_5ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5FB")
    Jump("loc_64D")

    label("loc_5FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0x9, 114570, 0, 61510, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_64D")

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_62E")
    Jump("loc_64D")

    label("loc_62E")

    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64D")
    SetChrFlags(0xF, 0x10)
    OP_93(0xF, 0x0, 0x0)

    label("loc_64D")

    Return()

    # Function_4_3FB end

    def Function_5_64E(): pass

    label("Function_5_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_686")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D0")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_6D0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D0")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    SetMapObjFrame(0xFF, "futon", 0x0, 0x1)
    OP_66(0x3, 0x1)

    label("loc_6F3")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70F")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_70F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_71D")
    Jump("loc_76B")

    label("loc_71D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_737")
    Jump("loc_76B")

    label("loc_737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_745")
    Jump("loc_76B")

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_76B")
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x14)
    OP_1B(0xB, 0x0, 0x15)
    OP_1B(0xD, 0x0, 0x16)
    OP_1B(0xF, 0x0, 0x17)

    label("loc_76B")

    Return()

    # Function_5_64E end

    def Function_6_76C(): pass

    label("Function_6_76C")

    Call(0, 7)
    Return()

    # Function_6_76C end

    def Function_7_770(): pass

    label("Function_7_770")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(
        0xB,
        "Welcome to Hotel Millennium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We provide only the finest quality of\x01",
            "service at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We make for the perfect place to rest in Crossbell,\x01",
            "the entertainment capital of Zemuria!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_900")
    SetScenarioFlags(0x0, 0)

    label("loc_900")

    SetScenarioFlags(0x4B, 4)

    label("loc_903")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_95E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CEF")

    label("loc_97E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_992")
    Jump("loc_1CEF")

    label("loc_992")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A1B")

    ChrTalk(
        0xB,
        (
            "I heard that Gantz and several other\x01",
            "people have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Will everything be okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AB7")

    ChrTalk(
        0xB,
        (
            "It's difficult to know what to do as\x01",
            "a hotel manager in these situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I truly hope that Gantz and\x01",
            "the others are safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A")

    label("loc_AB7")


    ChrTalk(
        0xB,
        (
            "Gantz left the hotel on his own\x01",
            "early this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'd heard he was blackout drunk, so\x01",
            "I asked Aeron to check up on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I just hope he's okay.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B5A")

    Jump("loc_1CEF")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BE9")

    ChrTalk(
        0xB,
        (
            "Gantz may have had far too\x01",
            "much to drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I shall provide him with a tall glass\x01",
            "of water later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9E")

    label("loc_BE9")


    ChrTalk(
        0xB,
        (
            "I am truly curious to know what\x01",
            "happened to Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Would you like me to contact St. Ursula\x01",
            "and request for an ambulance to be\x01",
            "dispatched here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I'm a little worried about Gantz, but\x01",
            "I doubt it's anything too serious.)\x02\x03",
            "#0012FW-Well... I think he'll manage...probably.\x01",
            "He just had a few too many drinks.\x02\x03",
            "#0000FSomeone is taking care of him right now,\x01",
            "so I think he'll be just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, really? Good to know.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D9E")

    Jump("loc_E72")

    label("loc_DA3")


    ChrTalk(
        0xB,
        (
            "Gantz left the hotel looking like he was\x01",
            "in a good mood today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I could have sworn someone from\x01",
            "Mainz was coming to pick him up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wouldn't it have made more sense\x01",
            "for him to wait in his room?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E72")

    Jump("loc_1CEF")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_FBE")

    ChrTalk(
        0xB,
        (
            "Our newly-built online reservation system\x01",
            "has finally launched and can be accessed\x01",
            "via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's only a matter of time until use of the\x01",
            "orbal network becomes commonplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Transitioning to a new technology will\x01",
            "be challenging, but we want to stay\x01",
            "ahead of the curve if we can help it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(
        0xB,
        "Welcome to Hotel Millennium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This year marks the 60th anniversary of\x01",
            "the hotel's founding. Our wish is to\x01",
            "continue serving you the best we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_13BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B3")

    ChrTalk(
        0xB,
        "E-Excuse me, sir?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please refrain from bringing any\x01",
            "pets into the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FI'm sorry, but he's with the CPD.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FWe are conducting a minor investigation,\x01",
            "so please do not mind us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "O-Oh... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My apologies, then. You may freely\x01",
            "search the area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 5)
    TalkEnd(0xB)
    Return()

    label("loc_11B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_126B")

    ChrTalk(
        0xB,
        (
            "I believe the true meaning of service is\x01",
            "to lend a helping hand to those in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I would like for this establishment to follow\x01",
            "the spirit of Liberlian hotels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_126B")


    ChrTalk(
        0xB,
        (
            "There was a major incident where a dragon\x01",
            "attacked a town by the name of Bose about\x01",
            "a year and a half ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The town's hotel took charge of the relief\x01",
            "efforts and provided lodging to victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Such acts of kindness are the pinnacle of\x01",
            "what it means to provide service. I wish\x01",
            "for our hotel to follow their example.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13B6")

    Jump("loc_1CEF")

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1474")

    ChrTalk(
        0xB,
        (
            "Many of our patrons stay here with the\x01",
            "intention of visiting the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The variety of entertainment available in\x01",
            "Crossbell sets us apart from other countries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_152A")

    ChrTalk(
        0xB,
        (
            "As we've received a high volume of reservations,\x01",
            "we have very few vacant rooms available today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you wish to reserve a room, I recommend\x01",
            "you do so quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_15EE")

    ChrTalk(
        0xB,
        (
            "The orbal network currently runs between\x01",
            "Crossbell City, Mishelam, and St. Ursula\x01",
            "Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Access to the orbal network will help\x01",
            "us with our business capabilities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1693")

    ChrTalk(
        0xB,
        (
            "A person from the Epstein Foundation came\x01",
            "to set up our orbal network access today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We can provide even greater services\x01",
            "to our patrons now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_17B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_172B")

    ChrTalk(
        0xB,
        (
            "Our reservation service will be opening on\x01",
            "the orbal network in a few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please bear with us a little while longer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17B3")

    label("loc_172B")


    ChrTalk(
        0xB,
        (
            "We will soon provide a means for guests\x01",
            "to reserve rooms via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Please bear with us a little while longer.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17B3")

    Jump("loc_1CEF")

    label("loc_17B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_18EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_183E")

    ChrTalk(
        0xB,
        (
            "We're sure to get a massive edge over our\x01",
            "competitors once we get the reservation\x01",
            "service up and running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E5")

    label("loc_183E")


    ChrTalk(
        0xB,
        (
            "How fortunate of us to make the most profit\x01",
            "out of any business in the Entertainment\x01",
            "District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We have many rivals, though. Complacency\x01",
            "is not an option.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18E5")

    Jump("loc_1CEF")

    label("loc_18EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(
        0xB,
        (
            "Next month marks the start of Crossbell's\x01",
            "Anniversary Festival, along with the debut\x01",
            "of Arc en Ciel's newest production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am more than certain that our rooms\x01",
            "will be fully booked during that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADF")

    label("loc_19D1")


    ChrTalk(
        0xB,
        (
            "Crossbell will be hosting a few major\x01",
            "events next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Between the Anniversary Festival and\x01",
            "Arc en Ciel's newest production, there'll\x01",
            "be plenty of exciting things to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We are expecting to be fully booked, so we\x01",
            "recommend making a reservation ASAP.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1ADF")

    Jump("loc_1CEF")

    label("loc_1AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xB,
        (
            "Our hotel provides a complimentary\x01",
            "concierge service to our patrons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I would be most pleased if you made use of it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C2A")

    ChrTalk(
        0xB,
        (
            "We offer many services, from beauty\x01",
            "salons to various booking services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We make for the perfect place to rest in Crossbell,\x01",
            "the entertainment capital of Zemuria!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEF")

    label("loc_1C2A")


    ChrTalk(
        0xB,
        "Welcome to Hotel Millennium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We provide only the finest quality of\x01",
            "service at our hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We make for the perfect place to rest in Crossbell,\x01",
            "the entertainment capital of Zemuria!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CEF")

    Jump("loc_90D")

    label("loc_1CF4")

    TalkEnd(0xB)
    Return()

    # Function_7_770 end

    def Function_8_1CF8(): pass

    label("Function_8_1CF8")

    Call(0, 9)
    Return()

    # Function_8_1CF8 end

    def Function_9_1CFC(): pass

    label("Function_9_1CFC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3E")

    ChrTalk(
        0x8,
        "Good day. Welcome to Hotel Millenium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish to reserve a room, you may\x01",
            "do so at this front desk.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can replenish CP by staying in\x01",
            "hotels and inns.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regular inns recover 100 CP, while\x01",
            "luxury hotels recover 200 CP.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3B")
    SetScenarioFlags(0x0, 1)

    label("loc_1E3B")

    SetScenarioFlags(0x4B, 4)

    label("loc_1E3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E99")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB9")
    OP_AF(0x3C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C59")

    label("loc_1EB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ECD")
    Jump("loc_2C59")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C59")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1F5F")

    ChrTalk(
        0x8,
        "Hard at work at this hour? Well, keep it up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Do you require a room? We currently\x01",
            "have a vacancy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2018")

    ChrTalk(
        0x8,
        (
            "A businessman just finished checking out\x01",
            "a few moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Check-ins begin in the afternoon, but if you\x01",
            "require a room, I will prepare one for you\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_20DC")

    ChrTalk(
        0x8,
        (
            "Gantz is currently renting a deluxe suite\x01",
            "under a long-term contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He may be completely selfish, but it's okay.\x01",
            "A professional like myself knows how to\x01",
            "handle his type.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(
        0x8,
        (
            "Many of our patrons book a hotel with the\x01",
            "intention to play at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The occasional customer will return\x01",
            "with a beautiful hostess... I must say,\x01",
            "I am quite env--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ahem! Excuse me, for I said nothing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_21C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_22D1")

    ChrTalk(
        0x8,
        (
            "Our hotel was completely packed during\x01",
            "the Anniversary Festival, so it was quite\x01",
            "busy. I feel it was worth it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell's propensity to celebrate is on a\x01",
            "different level from anywhere else's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I have to say, I'm glad I work here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_23A4")

    ChrTalk(
        0x8,
        (
            "We're devoted to giving our patrons the\x01",
            "utmost care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our manager, Leticia, gained her experience\x01",
            "from managing the Times Department Store.\x01",
            "You can tell she truly cares for this industry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_23A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_244D")

    ChrTalk(
        0x8,
        (
            "Our hotel rooms come equipped with\x01",
            "telephones to call for room service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please don't hesitate to call the front desk\x01",
            "if you need any assistance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_244D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_24BF")

    ChrTalk(
        0x8,
        (
            "It's almost time for the group of\x01",
            "tourists to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I should prepare for their arrival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_24BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2567")

    ChrTalk(
        0x8,
        "Our hotel owns three orbal cars.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We use them to transport people to the train\x01",
            "station and airport. Please let us know if you'd\x01",
            "like to use one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_2567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2657")

    ChrTalk(
        0x8,
        (
            "The orbal network is still an unknown,\x01",
            "yet fascinating concept for Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our manager hopes to future-proof our hotel\x01",
            "by adopting it while it's still in its infancy,\x01",
            "for it will surely one day become mainstream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_2657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_272C")

    ChrTalk(
        0x8,
        (
            "It's all thanks to the manager's hard work\x01",
            "that we were able to implement our orbal\x01",
            "network-based reservation system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you all make use of the service\x01",
            "once it's operational.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_283C")

    label("loc_272C")


    ChrTalk(
        0x8,
        (
            "It's all thanks to the manager's hard work that\x01",
            "we were able to implement the reservation\x01",
            "service that utilizes the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our handy service can be used from\x01",
            "anywhere within the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you all make use of the service\x01",
            "once it's operational.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_283C")

    Jump("loc_2C59")

    label("loc_2841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_29AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28D5")

    ChrTalk(
        0x8,
        (
            "Crossbell has many laws in place that help\x01",
            "fuel the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I feel honored to do my part for the system.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A5")

    label("loc_28D5")


    ChrTalk(
        0x8,
        (
            "The government provides many incentives\x01",
            "to encourage the tourism industry to\x01",
            "flourish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tourism and trade are Crossbell's\x01",
            "key industries that help drive the\x01",
            "economy. I'm happy to be a part of it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29A5")

    Jump("loc_2C59")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2A58")

    ChrTalk(
        0x8,
        (
            "Good morning. Thank you for choosing\x01",
            "Hotel Millennium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A customer just finished checking out,\x01",
            "so we have a vacant room. Would you\x01",
            "like to reserve it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_2A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AC3")

    ChrTalk(
        0x8,
        (
            "I'm grateful to the manager for fostering a\x01",
            "satisfying environment to work in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B67")

    label("loc_2AC3")


    ChrTalk(
        0x8,
        (
            "I was working at a hotel in the Empire, but\x01",
            "the current manager recruited me here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. It feels satisfying to be able to\x01",
            "accommodate so many patrons.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B67")

    Jump("loc_2C59")

    label("loc_2B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2BE5")

    ChrTalk(
        0x8,
        "We currently have vacant rooms.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish to reserve a room, you may\x01",
            "do so at this front desk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C59")

    label("loc_2BE5")


    ChrTalk(
        0x8,
        "Good day. Welcome to Hotel Millenium.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you wish to reserve a room, you may\x01",
            "do so at this front desk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C59")

    Jump("loc_1E48")

    label("loc_2C5E")

    TalkEnd(0x8)
    Return()

    # Function_9_1CFC end

    def Function_10_2C62(): pass

    label("Function_10_2C62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2D36")

    ChrTalk(
        0xA,
        (
            "Bickson hasn't moved a muscle because\x01",
            "he's so worried about Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I feel as if he'll ruin his health if he continues\x01",
            "down this path. Perhaps I'll recommend that\x01",
            "he order room service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DD0")

    ChrTalk(
        0xA,
        "Huh... Gantz seemed a little strange.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I feel as if he were absentminded, maybe.\x01",
            "I don't believe he was suffering from a\x01",
            "hangover.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_2DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_2E63")

    ChrTalk(
        0xA,
        (
            "There. I've finally organized the reservations\x01",
            "on the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, did something\x01",
            "happen with Gantz?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F0B")

    label("loc_2E63")


    ChrTalk(
        0xA,
        (
            "Okay. I need to check up on our orbal\x01",
            "network reservations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to admit that I started having\x01",
            "fun once I figured out how to use\x01",
            "that complicated machine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0B")

    Jump("loc_38F2")

    label("loc_2F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2FF5")

    ChrTalk(
        0xFE,
        (
            "One of our patrons has been booking\x01",
            "a deluxe suite for multiple days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We give our most generous customers\x01",
            "the finest treatment in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please make sure you walk through the\x01",
            "hallways quietly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_30AA")

    ChrTalk(
        0xA,
        (
            "I haven't seen members of Revache\x01",
            "hanging around the Entertainment\x01",
            "District lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Did something happen during the Anniversary\x01",
            "Festival to drive them away?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_30AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3196")

    ChrTalk(
        0xA,
        (
            "Arc en Ciel was established the same\x01",
            "year I became the head receptionist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's been an interesting 20 years, that's for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha. I'm glad to see that Arc en Ciel's reached\x01",
            "the height of their popularity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_3196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_323E")

    ChrTalk(
        0xA,
        (
            "None of us know how to operate\x01",
            "these things, so we leave that\x01",
            "to the specialists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Though I think I can handle some\x01",
            "basic maintenance, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_32EA")

    ChrTalk(
        0xA,
        (
            "I think it's almost time for me\x01",
            "to check up on the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our waiters are going to be busy today. We've\x01",
            "got many large groups of tourists coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_32EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3304")

    ChrTalk(
        0xA,
        "Hmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_3304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_338C")

    ChrTalk(
        0xA,
        (
            "I don't get this 'online reservation system'\x01",
            "stuff. I'm getting too old to understand\x01",
            "these fancy trinkets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341C")

    label("loc_338C")


    ChrTalk(
        0xA,
        (
            "This is the online reservation the\x01",
            "manager implemented, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sure it's excellent, but I don't\x01",
            "really understand the details.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_341C")

    Jump("loc_38F2")

    label("loc_3421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_34E5")

    ChrTalk(
        0xA,
        (
            "The top floor of our hotel is reserved\x01",
            "for deluxe suites.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "While expensive to book, the first-class\x01",
            "service we offer is incomparable to what\x01",
            "you would get in a normal room.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_35C3")

    ChrTalk(
        0xA,
        (
            "Leticia hired all of our current staff members\x01",
            "when she became the manager a couple of\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We also have personal staff members\x01",
            "that will provide you with the finest\x01",
            "service we have to offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_35C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_37C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_368B")

    ChrTalk(
        0xA,
        (
            "Business has been booming ever since the\x01",
            "Non-Aggression Pact was signed a little\x01",
            "over a year ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We must always be wary of our neighboring\x01",
            "countries' current events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BE")

    label("loc_368B")


    ChrTalk(
        0xA,
        (
            "Most of our patrons are travelers from\x01",
            "foreign countries, so we pay attention\x01",
            "to current events around the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For instance... Calvard, Erebonia, and\x01",
            "Liberl signed a non-aggression pact\x01",
            "two years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "People became more willing to visit foreign\x01",
            "countries, thus increasing the tourists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_37BE")

    Jump("loc_38F2")

    label("loc_37C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3852")

    ChrTalk(
        0xA,
        (
            "It's almost time for our patrons to begin\x01",
            "checking into their rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We must be in tip-top shape when\x01",
            "we welcome them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F2")

    label("loc_3852")


    ChrTalk(
        0xA,
        (
            "This hotel has been in business for 60\x01",
            "years as of this year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We began offering tour planning services a\x01",
            "few years ago, which made us more popular.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F2")

    TalkEnd(0xFE)
    Return()

    # Function_10_2C62 end

    def Function_11_38F6(): pass

    label("Function_11_38F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_39BC")

    ChrTalk(
        0x9,
        "I haven't seen Gantz go to the casino today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's already evening. Maybe I should\x01",
            "have reported this to the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "O-Oh. You're all police officers?\x01",
            "My apologies...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_39BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A12")

    ChrTalk(
        0x9,
        (
            "*sigh* I feel disgusted for not\x01",
            "being considerate enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC5")

    label("loc_3A12")


    ChrTalk(
        0x9,
        "Gantz was oddly quiet yesterday...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Do you think he may have gotten\x01",
            "food poisoning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sorry, I shouldn't say something so\x01",
            "careless about a serious disappearance...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3AC5")

    Jump("loc_4524")

    label("loc_3ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3B6E")

    ChrTalk(
        0x9,
        (
            "I received an enormous tip from Gantz...\x01",
            "I felt bad about it, so I donated it to\x01",
            "City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe I should have kept a\x01",
            "little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C53")

    label("loc_3B6E")


    ChrTalk(
        0x9,
        "I received an enormous tip from Gantz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I felt uncomfortable holding that much money,\x01",
            "so I went and donated it to City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't know what they plan on using it\x01",
            "for, but it's better than keeping it myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3C53")

    Jump("loc_4524")

    label("loc_3C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3D4C")

    ChrTalk(
        0x9,
        (
            "The patron staying on the top floor can be\x01",
            "rather loud, so as you can imagine, we've\x01",
            "been receiving noise complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, each patron is valuable to us, so\x01",
            "it's important we be fair in helping settle\x01",
            "the grievance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_3D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3D98")

    ChrTalk(
        0x9,
        (
            "Good morning. Will you be staying here\x01",
            "with your family?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_3D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3F53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3E0E")
    TurnDirection(0x9, 0x11C, 0)

    ChrTalk(
        0x9,
        (
            "P-Please! Stay away from me!\x01",
            "I don't handle dogs well...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC1")

    label("loc_3E0E")

    TurnDirection(0x9, 0x11C, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Wh-Whoa! A dog?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "P-Please! Stay away from me!\x01",
            "I don't handle dogs well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FOh, haha. Sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        "#1203FGrrr...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3EC1")

    TalkEnd(0x9)
    Return()

    label("loc_3EC5")


    ChrTalk(
        0x9,
        (
            "Please deposit your key at the front desk\x01",
            "if you leave the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll make the beds and organize the\x01",
            "room while you're gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_3F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3FCA")

    ChrTalk(
        0x9,
        (
            "The beverages in your room are included\x01",
            "with the lodging fee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please drink them as you'd like.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_3FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_406B")

    ChrTalk(
        0x9,
        "I finished cleaning the rooms and hallways.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's a lot of things to organize in the\x01",
            "executive suites, so it gets to be\x01",
            "pretty tiring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_406B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_41B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_40D6")

    ChrTalk(
        0x9,
        (
            "I have to be diligent with my cleaning so\x01",
            "that Aeron doesn't yell at me later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41B0")

    label("loc_40D6")


    ChrTalk(
        0x9,
        "That should do it for the cleaning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have to be diligent with my cleaning so\x01",
            "that Aeron doesn't yell at me later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aeron isn't afraid to tell you off when he\x01",
            "gets angry. It's actually pretty scary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_41B0")

    Jump("loc_4524")

    label("loc_41B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_421A")

    ChrTalk(
        0x9,
        (
            "The hallways and rooms on the top floor are\x01",
            "larger, so it's harder to clean them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_421A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_431F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4290")

    ChrTalk(
        0x9,
        (
            "We've recently had more patrons come and\x01",
            "stay here in order to enjoy Arc en Ciel's shows.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431A")

    label("loc_4290")


    ChrTalk(
        0x9,
        (
            "Did you see that Arc en Ciel's newest\x01",
            "production was announced?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I must brace myself for the impending\x01",
            "flood of reservations.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_431A")

    Jump("loc_4524")

    label("loc_431F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_439C")

    ChrTalk(
        0x9,
        (
            "It's almost time for our sightseers\x01",
            "to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd best prepare myself to give them\x01",
            "a grand welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_439C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4430")

    ChrTalk(
        0x9,
        (
            "Good morning, and welcome to Hotel\x01",
            "Millennium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please ensure that you've retrieved all of\x01",
            "your belongings before you leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_4430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_44BC")

    ChrTalk(
        0x9,
        (
            "We've been getting many more patrons\x01",
            "compared to usual this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I imagine we'll run out of vacancies\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4524")

    label("loc_44BC")


    ChrTalk(
        0x9,
        "Good morning. Will you be staying here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Would you like me to carry your\x01",
            "luggage to your room?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4524")

    TalkEnd(0xFE)
    Return()

    # Function_11_38F6 end

    def Function_12_4528(): pass

    label("Function_12_4528")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A2")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0x101,
        "#0005FO-Oh, aren't you Tio's boss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWhat business does the Epstein Foundation\x01",
            "have with this hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, I'm here to supervise the installation\x01",
            "of the orbal network into the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any business or hotel may take part in\x01",
            "testing out the orbal network. All they\x01",
            "have to do is send in an application.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FMakes sense to me.\x02\x03",
            "#0301FIs this orbal network thingy that easy to\x01",
            "set up, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FWell, there are regular inspections regarding\x01",
            "the intended usage and the type of industry...\x02\x03",
            "#0200FHowever, the IBC pays for all of the equipment.\x01",
            "They get the privilege of becoming a test\x01",
            "environment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But anyway, they've graced me with the\x01",
            "opportunity to run various tests that I\x01",
            "otherwise wouldn't be able to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not many people can run the terminals\x01",
            "competently, so I've had a bit of trouble\x01",
            "training them, haha.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xA, 0)
    SetScenarioFlags(0x92, 6)
    Jump("loc_50BE")

    label("loc_48A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 6)), scpexpr(EXPR_END)), "loc_4933")

    ChrTalk(
        0xFE,
        "Okay, I've fixed the settings for this terminal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an expert in this field, I can operate\x01",
            "terminals with ease.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C56")

    label("loc_4933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_49F1")

    ChrTalk(
        0xFE,
        (
            "My precious little Tio isn't having any\x01",
            "mischievous thoughts about me, is she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep. I'm sure it's just my imagination, right?\x01",
            "Please take good care of her, everyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C56")

    label("loc_49F1")


    ChrTalk(
        0xFE,
        "Okay, I've fixed the settings for this terminal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As an expert in this field, I can operate\x01",
            "terminals with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FChief Roberts is one of the lead developers\x01",
            "of the Orbal Network Project, despite...how\x01",
            "he seems.\x02\x03",
            "#0200FCrossbell's access to the orbal network is largely\x01",
            "thanks to the chief's efforts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    ChrTalk(
        0xFE,
        (
            "Y-You're not wrong, but aren't you being a\x01",
            "bit too mean to me, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0211FHmm? I do not follow. I am behaving as\x01",
            "I usually would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yeah! You're right. Haha, it's probably\x01",
            "just my imagination.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 4)

    label("loc_4C56")

    Jump("loc_50BE")

    label("loc_4C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4D4F")

    ChrTalk(
        0xFE,
        (
            "Anyway, I'll be back tomorrow to check\x01",
            "on the settings again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, right. Please don't activate the terminal\x01",
            "yet. I need to initialize it still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(He behaves like a normal human\x01",
            "being when he works, and yet...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50BE")

    label("loc_4D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_50BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4E2B")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(
        0xFE,
        (
            "Let me know if your terminal breaks, my\x01",
            "dear Tio! I'll be there in a jiffy to fix it.\x02",
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
    Jump("loc_50BE")

    label("loc_4E2B")


    ChrTalk(
        0xFE,
        (
            "A terminal costs 1.5 million mira to buy\x01",
            "outright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Commonfolk won't be able to afford it\x01",
            "just quite yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0003FOh, wow. And here I was handling the terminal\x01",
            "at the SSS carelessly this entire time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou have little reason to worry. Physical\x01",
            "damage to the terminal is a minor concern.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    ChrTalk(
        0xFE,
        (
            "Do let me know if your terminal breaks\x01",
            "down, my dear Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be there to fix it in a jiffy! I'll fix it before\x01",
            "you can even say 'orbal terminal!'\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0200FI...do not believe that to be necessary. I am\x01",
            "qualified to repair it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_50BE")

    TalkEnd(0xFE)
    Return()

    # Function_12_4528 end

    def Function_13_50C2(): pass

    label("Function_13_50C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50FC")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 25)
    Return()

    label("loc_50FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5124")
    TurnDirection(0x0, 0xF, 0)
    Call(0, 24)
    Return()

    label("loc_5124")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_536F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528C")

    ChrTalk(
        0xFE,
        "I can finally return to my country.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you so much, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou should probably start by buying\x01",
            "a new suitcase, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Y-Yeah. You're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hahaha. Thank you!\x02",
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
        0x103,
        "#0200F(A lively one, he is.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_536A")

    label("loc_528C")


    ChrTalk(
        0xFE,
        (
            "Wallet, check! Souvenir, check!\x01",
            "Ticket, check!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. Too bad I don't have a\x01",
            "suitcase to put them in! Hahaha!\x02",
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

    label("loc_536A")

    Jump("loc_55A6")

    label("loc_536F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_5528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C4")

    ChrTalk(
        0xFE,
        (
            "It was always a dream for me to tour Crossbell.\x01",
            "Seeing the wonderful sights put me in a daze,\x01",
            "hence the situation I'm currently in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I'm tired of searching. Crossbell City\x01",
            "is way too large!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, and I intend to return to my home\x01",
            "country today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm begging you, officers! Please hurry!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5523")

    label("loc_54C4")


    ChrTalk(
        0xFE,
        "*sigh* I'm tired. Crossbell is way too large!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Anyway, I'm begging you! Please hurry!\x02",
    )

    CloseMessageWindow()

    label("loc_5523")

    Jump("loc_55A6")

    label("loc_5528")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5539")
    Jump("loc_55A6")

    label("loc_5539")


    ChrTalk(
        0xFE,
        "*sigh* I'm so done with walking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, what a pickle I'm in... Maybe\x01",
            "I'll just give up and go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55A6")

    TalkEnd(0xFE)
    Return()

    # Function_13_50C2 end

    def Function_14_55AA(): pass

    label("Function_14_55AA")

    EventBegin(0x2)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears to be locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_14_55AA end

    def Function_15_55DA(): pass

    label("Function_15_55DA")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_569E")

    ChrTalk(
        0xC,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FIt looks like he's totally unconscious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FThink it's a side effect of the drug?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FIt's too early for us to make a call...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_56DE")

    label("loc_569E")


    ChrTalk(
        0xC,
        "...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gantz is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_56DE")

    TalkEnd(0xC)
    Return()

    # Function_15_55DA end

    def Function_16_56E2(): pass

    label("Function_16_56E2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_575D")

    ChrTalk(
        0xFE,
        "Gantz has yet to return...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aidios, please! Allow our precious friend\x01",
            "to come home in one piece.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8C")

    label("loc_575D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57F1")

    ChrTalk(
        0xFE,
        "Oh, is that you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it, Gantz... Way to make all of\x01",
            "us worried sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where the heck did you run off to?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5874")

    label("loc_57F1")


    ChrTalk(
        0xFE,
        "Where the heck did you run off to, Gantz?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry to bother you while you're busy,\x01",
            "but please do not forget about him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5874")

    Jump("loc_5A8C")

    label("loc_5879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D8")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I apologize. I'm having difficulty\x01",
            "maintaining my composure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0008FIt's okay, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Gantz is not the type of person who would\x01",
            "get involved with drugs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if those pills are an illegal\x01",
            "substance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they truly are, then I'll track down whoever\x01",
            "is responsible for distributing them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A8C")

    label("loc_59D8")


    ChrTalk(
        0xFE,
        "Entrust Gantz's well-being to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll ask him for information on his\x01",
            "circumstances when he wakes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm just praying those pills are\x01",
            "nothing more than medication.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A8C")

    TalkEnd(0xD)
    Return()

    # Function_16_56E2 end

    def Function_17_5A90(): pass

    label("Function_17_5A90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(163000, 1000, 7200, 0)
    MoveCamera(307, 27, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 164300, 0, 3900, 270)
    SetChrPos(0x102, 164300, 0, 5000, 270)
    SetChrPos(0x103, 165200, 0, 3600, 270)
    SetChrPos(0x104, 165200, 0, 5300, 270)
    SetChrPos(0x13D, 164300, 0, 7600, 225)
    SetChrPos(0xC, 162000, 650, 5900, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xD, 162000, 0, 4500, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetMapObjFrame(0xFF, "futon", 0x0, 0x1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis087.itp")
    OP_68(163000, 1000, 5200, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0xD,
        (
            "#4200497V#5POh, sweet Goddess! How could such a\x01",
            "thing have happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200498V#5PHe may not have been the hardest worker,\x01",
            "but he was a kind man. There's not a soul\x01",
            "in Mainz who disliked him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200499V#0108F#12PMayor Bickson...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200500V#12P#0306FFor a nice guy, he sure was pretty violent\x01",
            "for a sec there.\x02\x03",
            "#4200501V#0301FHell, I wasn't expectin' that both of us\x01",
            "would need to hold him down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200502V#6P#0006FYeah, I couldn't believe how ridiculously\x01",
            "strong he was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200576V#12P#0201F#N...\x02",
    )

    CloseMessageWindow()
    OP_63(0x13D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13D)
    TurnDirection(0x13D, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x13D,
        (
            "#4200504V#2103F#11PListen, guys. This is just my impression,\x01",
            "but, uh...\x02\x03",
            "#4200505V#2101F...you think the guy could've been on some\x01",
            "kind of drugs?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5EFB():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5EFB)

    def lambda_5F08():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F08)
    Sleep(50)

    def lambda_5F18():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5F18)

    def lambda_5F25():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5F25)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xD,
        "#4200506V#5P#4SP-Pardon me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200545V#6P#0105FWhat is the basis for that assessment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200508V#6P#0305FYou kiddin'?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200509V#2100F#11PJudging by their silence, I think Lloyd\x01",
            "and Tio seem to agree with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200510V#0208F#6P#NI am not sure...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#4200511V#0006F#6PI don't want to say anything unsubstantiated,\x01",
            "but it's not out of the realm of possibility.\x02\x03",
            "#4200512V#0001FWe can't rule it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200513V#5PTh-That's preposterous... Gantz? On drugs?\x01",
            "I refuse to believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200514V#5PHe's just an ordinary miner, you hear\x01",
            "me?! There's no way he'd be able to\x01",
            "get a hold of such dangerous--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13D, 0xD, 500)

    ChrTalk(
        0x13D,
        (
            "#4200515V#2100F#11PSorry, sir, but hasn't it been almost half a month\x01",
            "since he arrived in Crossbell City?\x02\x03",
            "#4200516VKeep in mind that he earned quite a bit of mira\x01",
            "during his stay, too. Can you say for certain that\x01",
            "he couldn't have taken advantage of that wealth?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4200517V#5PI won't stand for this slander!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200518V#5PYou mentioned that you're a Crossbell\x01",
            "Times journalist, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200519V#5PKnow that if you write some libel piece\x01",
            "based on pure speculation, I will lead\x01",
            "Mainz and its people in protest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200520V#2106F#11POh, c'mon. Take it easy for a second. I don't\x01",
            "plan on writing an article on this, mister.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Fade(500)
    OP_68(163000, 1000, 4700, 0)
    MoveCamera(330, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0xC, 162000, 600, 5900, 90)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        (
            "#4200521V#12P#0003FWould you do us a favor, Mayor Bickson?\x02\x03",
            "#4200522V#0001FI'd like to go through Gantz's personal\x01",
            "belongings, if that's all right with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6572():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6572)
    Sleep(100)

    def lambda_6582():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6582)

    def lambda_658F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_658F)

    def lambda_659C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_659C)
    Sleep(50)
    TurnDirection(0x13D, 0x101, 500)

    ChrTalk(
        0xD,
        "#4200523V#5PYou, too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200524V#12P#0006FI don't intend to imply anything, sir, but there\x01",
            "are too many coincidences piling up here.\x02\x03",
            "#4200525V#0008FHis sudden violence, that inhuman strength,\x01",
            "the complete change in personality...\x02\x03",
            "#4200526V#0013FAll of these aspects are eerily similar to past\x01",
            "cases.\x02\x03",
            "#4200527VAnd in Gantz's case, we also saw an absurd\x01",
            "development in his gambling skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200528V#0303F#11PMight be 'cause he took some stimulants\x01",
            "to boost his perception or something.\x02\x03",
            "#4200529V#0301FThat'd explain that freakish intuition. People\x01",
            "kept tellin' us how it was like he could read\x01",
            "people's minds, y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200530V#12P#0206FIt is entirely possible.\x02\x03",
            "#4200531V#0200FI can only speculate that if I were to gamble,\x01",
            "I would likely be more adept than your\x01",
            "average person.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4200532V#0105F#5PTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200533V#0306F#11PSorry, Tio Tot. You know I didn't\x01",
            "mean it like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200534V#12P#0204FI am aware. Do not worry.\x02\x03",
            "#4200535V#0201FMayor Bickson, I understand you wish\x01",
            "to keep Mr. Gantz's reputation intact.\x02\x03",
            "#4200536VHowever, please envision the scenario\x01",
            "where he is, in fact, consuming drugs...\x02\x03",
            "#4200537VIf the situation were to remain unhandled,\x01",
            "it could pose a threat to himself and others.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6AB0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6AB0)
    Sleep(50)

    def lambda_6AC0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6AC0)

    ChrTalk(
        0xD,
        "#4200538V#5PTh-That may be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200539V#11P#2106FI could think of a bunch of possible\x01",
            "side effects that might crop up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200540V#12P#0006FSame here. And that's exactly what\x01",
            "we need to be scared of.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#4200541V#5PVery well. I fear I might have been\x01",
            "slightly inconsiderate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4200542V#5PGo ahead, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200543V#12P#0003FAll right.\x02",
    )

    CloseMessageWindow()

    def lambda_6C4C():

        label("loc_6C4C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C4C")

    QueueWorkItem2(0x13D, 2, lambda_6C4C)

    def lambda_6C5E():

        label("loc_6C5E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C5E")

    QueueWorkItem2(0x102, 2, lambda_6C5E)

    def lambda_6C70():

        label("loc_6C70")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C70")

    QueueWorkItem2(0x103, 2, lambda_6C70)

    def lambda_6C82():

        label("loc_6C82")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C82")

    QueueWorkItem2(0x104, 2, lambda_6C82)

    def lambda_6C94():

        label("loc_6C94")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C94")

    QueueWorkItem2(0xD, 2, lambda_6C94)
    OP_68(162700, 1000, 4930, 1200)

    def lambda_6CB7():
        OP_96(0xFE, 0x27B8C, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CB7)
    Sleep(300)

    def lambda_6CD4():
        OP_96(0xFE, 0x278D0, 0x0, 0xC80, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6CD4)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x14A, 0x1F4)
    WaitChrThread(0xD, 1)
    EndChrThread(0x13D, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xD, 0x2)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd carefully examined Gantz's pockets, making sure not\x01",
            "to wake him up in the process.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200544V#6P#0013F(This is what I was afraid of.)\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32B, 1)

    AnonymousTalk(
        0x102,
        "#4200507V#0105FP-Pills...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xD,
        "#4200546VGoddess, no!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x13D,
        "#4200547V#2101FSo our theory was spot on.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#4200548V#0301FPretty shade of blue...but what the\x01",
            "heck is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#4200549V#0201F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4200550V#0006F#5PWe can't rule out the possibility that\x01",
            "it's harmless medicine yet.\x02\x03",
            "#4200551VMaybe he has some kind of chronic\x01",
            "disease we don't know about.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    ChrTalk(
        0x101,
        (
            "#4200552V#11P#0001FDid he ever mention anything about\x01",
            "that, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200553V#6PFrom all my interactions with him,\x01",
            "no. Of course, I can't say for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200554V#11P#0003FInteresting.\x02\x03",
            "#4200555V#0001FWould you mind if we hung on to\x01",
            "these pills for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4200556V#6PPlease do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200557V#6PListen, though! I beg you...do not spread\x01",
            "this around, for Gantz's sake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200558V#11P#0004FOf course, sir. We'll make sure to take\x01",
            "his reputation into consideration.\x02\x03",
            "#4200559V#0001FAlso, could we leave him with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4200560V#6PYes. I'll take care of him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200561V#6PI'll try to speak with him once\x01",
            "he wakes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200562V#11P#0000FThanks. That'd be great.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(68000, 1000, 9700, 0)
    MoveCamera(310, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 73600, 0, 7400, 180)
    SetChrPos(0x102, 72400, 0, 7400, 180)
    SetChrPos(0x103, 73700, 0, 8600, 180)
    SetChrPos(0x104, 72300, 0, 8600, 180)
    SetChrPos(0x13D, 73000, 0, 5500, 0)
    OP_68(72710, 1000, 7410, 4000)
    SetCameraDistance(22500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)

    ChrTalk(
        0x13D,
        (
            "#4200563V#6P#2106FNow we have suspicions of an illegal drug\x01",
            "circulating throughout Crossbell, eh?\x02\x03",
            "#4200564VDefinitely didn't see that one coming.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#4200565V#11P#0305FReally?\x02\x03",
            "#4200566V#0301FI woulda thought the mafia was\x01",
            "big into the drug trade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200567V#6P#2104FThe contrary, actually. Illegal drugs hardly\x01",
            "ever show up in Crossbell.\x02\x03",
            "#4200568V#2100FDrugs are messy business, y'know? One\x01",
            "misstep and they'll spread to neighboring\x01",
            "countries like the plague.\x02\x03",
            "#4200569VI've heard the First Division monitors them\x01",
            "closely, thanks to pressure from Erebonia\x01",
            "and Calvard.\x02\x03",
            "#4200570V#2104FSo I guess Revache is smart enough\x01",
            "to read the room on that one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200571V#11P#0105FI suppose that makes sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200572V#11P#0003FYeah. They made sure to cover that\x01",
            "back at the police academy.\x02\x03",
            "#4200573V#0008FStill, something about these pills...\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x102,
        "#4200574V#0101FIt really is a lovely shade of blue, isn't it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#4200575V#0301FSure, but they're still suspicious as hell.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#4200503V#0208F#40W...\x02",
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
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#4200577V#6P#0005FSomething wrong, Tio?\x02",
    )

    CloseMessageWindow()

    def lambda_7847():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7847)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x103,
        (
            "#4200578V#0206F#11PNo, it is nothing. It must be my imagination.\x02\x03",
            "#4200579V#0201FMore importantly, what do you intend on\x01",
            "doing with the pills, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200580V#6P#0006FGood question.\x02\x03",
            "#4200581VI'm thinking this case is too much for\x01",
            "us to handle alone.\x02\x03",
            "#4200582V#0001FFor now, let's go talk with the chief.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_799B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_799B)
    Sleep(100)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4200583V#5P#0103FYes, he may know what to do.\x02\x03",
            "#4200584V#0101FWhile we're at it, we should give our\x01",
            "report on the Heiyue raid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200585V#5P#0306FWe got mafias fightin' each other AND\x01",
            "a chance of illegal drugs now, too?\x02\x03",
            "#4200586V#0301FGet ready, guys. I'm feelin' like things are\x01",
            "about to get pretty busy around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        "#4200587V#6P#2102FHeh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7B64():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B64)
    Sleep(50)

    def lambda_7B74():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B74)
    Sleep(50)

    def lambda_7B84():
        TurnDirection(0xFE, 0x13D, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7B84)
    Sleep(50)
    TurnDirection(0x104, 0x13D, 500)

    ChrTalk(
        0x13D,
        (
            "#4200588V#6P#2109FY'knooow, I've only known you guys\x01",
            "for four months...\x02\x03",
            "#4200589V...but I'm starting to think that you've\x01",
            "matured a lot since we first met!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200590V#11P#0005FGrace...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200591V#11P#0105FWhat's with the sudden praise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200592V#0211F#11PFlattery will get you nowhere, I hope\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200593V#6P#2104FNo, I'm serious! I've got some pretty\x01",
            "high expectations now.\x02\x03",
            "#4200594V#2100FAlmost as high as the ones I had for\x01",
            "your brother, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
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
        0x101,
        (
            "#4200595V#11P#0011FY-You know, I don't think I ever got a\x01",
            "straight answer last time you brought\x01",
            "up Guy.\x02\x03",
            "#4200596VSo...did you know my brother, Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200597V#6P#2104FOh, yeah. Back when I was still a newbie\x01",
            "at the CNS, he helped me out more times\x01",
            "than I can count.\x02\x03",
            "#4200598V#2106FAnd in the end, his case went cold...\x02\x03",
            "#4200599V#2102FAt the very least, I'm happy that the team\x01",
            "he wished for finally became a reality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200600V#11P#0005FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200601V#11P#0105FWhat do you mean, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13D,
        (
            "#4200602V#6P#2104FOopsie. Sergei might get angry at me\x01",
            "if I say too much.\x02\x03",
            "#4200603V#2100FAnyway, I've got an event to cover, so\x01",
            "I'm going to have to head out.\x02\x03",
            "#4200604V#2105FOh, and I won't write any articles about\x01",
            "the drug stuff, as tempting as it is.\x02\x03",
            "#4200605V#2109FBye byeee, everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13D, 0x5A, 0x1F4)
    OP_68(76000, 0, 6900, 2000)

    def lambda_812A():
        OP_98(0xFE, 0x1F40, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13D, 1, lambda_812A)

    def lambda_8144():

        label("loc_8144")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_8144")

    QueueWorkItem2(0x101, 2, lambda_8144)

    def lambda_8156():

        label("loc_8156")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_8156")

    QueueWorkItem2(0x102, 2, lambda_8156)

    def lambda_8168():

        label("loc_8168")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_8168")

    QueueWorkItem2(0x103, 2, lambda_8168)

    def lambda_817A():

        label("loc_817A")

        TurnDirection(0xFE, 0x13D, 500)
        Yield()
        Jump("loc_817A")

    QueueWorkItem2(0x104, 2, lambda_817A)
    Sleep(1500)

    def lambda_818F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13D, 2, lambda_818F)
    WaitChrThread(0x13D, 1)
    WaitChrThread(0x13D, 2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)
    Sleep(500)
    OP_68(73000, 1000, 8000, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#4200606V#5P#0008F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200607V#5P#0306FWhere does she get off teasing us\x01",
            "like that and just walking away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200608V#5P#0106F*sigh* Another addition to the pile\x01",
            "of things we have to think about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200609V#0206F#5PIndeed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4200610V#0200F#11PAre you concerned about what she\x01",
            "told us, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#4200611V#6P#0005FOh, well...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4200612V#6P#0006FEven if it's concerning Guy, I don't really\x01",
            "have time to think about it.\x02\x03",
            "#4200613V#0008FThe Heiyue raid, Revache's current\x01",
            "situation, and now these blue pills...\x02\x03",
            "#4200614V#0000FWe have a lot on our plate. For now, let's\x01",
            "put aside what Grace told us and ask the\x01",
            "chief how we should proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200615V#0202F#11PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200616V#5P#0100FHopefully, he has some ideas for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200617V#5P#0300FAll righty, then. Back to the SSS!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(73000, 1500, 9000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 74120, 0, 6470, 90)
    SetChrPos(0x1, 74120, 0, 6470, 90)
    SetChrPos(0x2, 74120, 0, 6470, 90)
    SetChrPos(0x3, 74120, 0, 6470, 90)
    RemoveParty(0x3C, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 162000, 650, 5900, 90)
    SetChrPos(0xD, 162000, 0, 4500, 0)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -2009, 0, 9290, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetScenarioFlags(0xC2, 7)
    OP_C7(0x1, 0x1000)
    OP_29(0x4A, 0x1, 0x9)
    OP_66(0x3, 0x1)
    BeginChrThread(0xD, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_17_5A90 end

    def Function_18_8681(): pass

    label("Function_18_8681")


    ChrTalk(
        0x11C,
        "#1200FWoof! Woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FLooks like this is the wrong way.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_18_8681 end

    def Function_19_86C6(): pass

    label("Function_19_86C6")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 56000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_19_86C6 end

    def Function_20_86E2(): pass

    label("Function_20_86E2")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 68000, 0, 11250, 180)
    EventEnd(0x4)
    Return()

    # Function_20_86E2 end

    def Function_21_86FE(): pass

    label("Function_21_86FE")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 66250, 180)
    EventEnd(0x4)
    Return()

    # Function_21_86FE end

    def Function_22_871A(): pass

    label("Function_22_871A")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 7250, 0, 60000, 270)
    EventEnd(0x4)
    Return()

    # Function_22_871A end

    def Function_23_8736(): pass

    label("Function_23_8736")

    EventBegin(0x1)
    Call(0, 18)
    Sleep(50)
    SetChrPos(0x0, 1000, 0, 53750, 0)
    EventEnd(0x4)
    Return()

    # Function_23_8736 end

    def Function_24_8752(): pass

    label("Function_24_8752")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115550, 1400, 59480, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 115750, 0, 59450, 0)
    SetChrPos(0x103, 115750, 0, 58030, 0)
    SetChrPos(0x102, 114340, 0, 59450, 0)
    SetChrPos(0x104, 114340, 0, 58030, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0xF,
        "Young Man",
        (
            "#11P*sigh* I don't think I can take\x01",
            "another step.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Young Man",
        (
            "#11PI might as well cut my losses and\x01",
            "head home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse me, sir. By any chance, did you\x01",
            "submit a request to the Special Support\x01",
            "Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xF, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xF,
        "#11POh, are you guys police officers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PWoohoohoo! I didn't think you were\x01",
            "actually going to come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0012FWell, uh, we're here to help...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FYour request mentioned that you lost\x01",
            "some of your belongings? Could you\x01",
            "explain how that happened exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYeah, of course. Sorry, this is just so\x01",
            "frustrating... I don't even have the\x01",
            "energy to cry anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xF,
        (
            "#11PYou see, I love shopping. So, I thought I'd\x01",
            "spend the day checking out some random\x01",
            "shops around the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI eventually noticed there was a gaping\x01",
            "hole in my bag, but it was already too\x01",
            "late. All my stuff had fallen out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI searched for what felt like forever, but\x01",
            "I still couldn't find any of my belongings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FThat really sucks, man.\x02\x03",
            "#0301FIt's almost been a full day, though.\x01",
            "Doubt your stuff's hangin' out where\x01",
            "you dropped it, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FPassersby may have noticed your belongings\x01",
            "and decided to hold on to them.\x02\x03",
            "Would you please state the locations you\x01",
            "visited during your shopping spree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PSure thing! As you'd expect, I stopped by\x01",
            "the department store first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI spent a good amount of time there.\x01",
            "With the new brand name stuff they\x01",
            "have on display, can you blame me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PSorry, that's beside the point. Afterwards,\x01",
            "I went to see East Street's marketplace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PAnd it wasn't until I stopped to rest near the park\x01",
            "in the Harbor District that I noticed the tear.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    ChrTalk(
        0xF,
        (
            "#11P*sigh* After an uneventful day of frantic\x01",
            "searching, I couldn't find diddly squat...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI think I ended up losing my wallet,\x01",
            "a souvenir I had bought, and...uh,\x01",
            "well, something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI'm pretty sure I lost three things in total.\x01",
            "But, about that last one...\x02",
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

    ChrTalk(
        0x101,
        (
            "#12P#0003FYou're going to tell us that you can't\x01",
            "remember what it was, aren't you?\x02\x03",
            "#0001FWell, it should still be enough for us to\x01",
            "go on. We'll start by searching around\x01",
            "the places you've visited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FTimes, East Street, and the Harbor District...\x02\x03",
            "#0100FThose are all commercial areas. It'll probably\x01",
            "save us a lot of time and effort if we simply\x01",
            "ask the workers there if they know anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#11PAwesome! Let me know if you find anything!\x02",
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
            "[Lost Item Search]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 115090, 0, 58830, 0)
    SetChrPos(0x1, 115090, 0, 58830, 0)
    SetChrPos(0x2, 115090, 0, 58830, 0)
    SetChrPos(0x3, 115090, 0, 58830, 0)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    OP_29(0x2, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_8752 end

    def Function_25_9339(): pass

    label("Function_25_9339")

    EventBegin(0x0)
    OP_4B(0xF, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115550, 1400, 59480, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 115750, 0, 59450, 0)
    SetChrPos(0x103, 115750, 0, 58030, 0)
    SetChrPos(0x102, 114340, 0, 59450, 0)
    SetChrPos(0x104, 114340, 0, 58030, 0)
    OP_93(0xF, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0000FYou really did lose three things, Tront.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FLuckily, we were able to track them down.\x02\x03",
            "Here you are. Take care of them from now\x01",
            "on, okay? And, please, stitch up that hole.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x102, 114480, 0, 60290, 1000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x337),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x338),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over ",
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    SubItemNumber(0x339, 1)
    OP_96(0x102, 0x1BEA4, 0x0, 0xE83A, 0x3E8, 0x0)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xF,
        "#11PYou guys are miracle workers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PThis is definitely my stuff! And here\x01",
            "I was about to give up on ever finding\x01",
            "them and head home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FExcuse me, but how would you have\x01",
            "gotten home without your wallet?\x01",
            "Or your ticket, for that matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xF,
        (
            "#11PUhhh... Y-You know what? You make\x01",
            "a pretty good point there. Hahaha...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PAnyway, thanks for your help. I didn't actually\x01",
            "expect the police to come give me a hand.\x01",
            "It was sort of a last-ditch effort on my part...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PI mean, you guys were great, but I haven't\x01",
            "heard the best things about the CPD.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PLike, I was REALLY surprised when you four\x01",
            "showed up to help.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        "#12P#0012FY-You don't say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI think I'm finally startin' to get why the\x01",
            "Special Support Section was made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FIsn't it wonderful, though? The feeling\x01",
            "of helping out someone in need?\x02\x03",
            "At any rate, that should be it for this\x01",
            "request.\x02",
        )
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
            "[Lost Item Search]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 115090, 0, 58830, 0)
    SetChrPos(0x1, 115090, 0, 58830, 0)
    SetChrPos(0x2, 115090, 0, 58830, 0)
    SetChrPos(0x3, 115090, 0, 58830, 0)
    OP_4C(0xF, 0xFF)
    OP_29(0x2, 0x2, 0x1F)
    OP_29(0x2, 0x1, 0x5)
    OP_29(0x2, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_9339 end

    SaveToFile()

Try(main)
