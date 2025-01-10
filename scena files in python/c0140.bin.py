from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "Chaco",                  # 1
        "Wendy",                  # 2
        "Fernand",                # 3
        "Mizette",                # 4
        "Basilio",                # 5
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_3D1",          # 02, 2
        "Function_3_570",          # 03, 3
        "Function_4_5A4",          # 04, 4
        "Function_5_750",          # 05, 5
        "Function_6_F2B",          # 06, 6
        "Function_7_1CD3",         # 07, 7
        "Function_8_1CD7",         # 08, 8
        "Function_9_2D77",         # 09, 9
        "Function_10_4CBA",        # 0A, 10
        "Function_11_5660",        # 0B, 11
        "Function_12_5981",        # 0C, 12
        "Function_13_6855",        # 0D, 13
        "Function_14_7430",        # 0E, 14
        "Function_15_8492",        # 0F, 15
        "Function_16_8845",        # 10, 16
        "Function_17_96E5",        # 11, 17
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_280")

    label("loc_3D0")

    Return()

    # Function_1_280 end

    def Function_2_3D1(): pass

    label("Function_2_3D1")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3EC")
    OP_93(0xA, 0x0, 0x0)
    Jump("loc_55D")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40B")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_419")
    Jump("loc_55D")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_427")
    Jump("loc_55D")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetChrFlags(0xC, 0x80)
    Jump("loc_55D")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_55D")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_467")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_486")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrPos(0xA, 11420, 4000, 7630, 270)
    Jump("loc_55D")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B3")
    Jump("loc_55D")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_55D")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4E0")
    SetChrPos(0xC, -4700, 0, -1320, 90)
    Jump("loc_55D")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xA, 820, 0, 850, 270)
    SetChrPos(0xB, -530, 0, 850, 90)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 11800, 4000, -1260, 90)
    Jump("loc_55D")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_546")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_554")
    Jump("loc_55D")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_55D")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F")
    Event(0, 15)

    label("loc_56F")

    Return()

    # Function_2_3D1 end

    def Function_3_570(): pass

    label("Function_3_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_5A3")

    Return()

    # Function_3_570 end

    def Function_4_5A4(): pass

    label("Function_4_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_746")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")

    ChrTalk(
        0x8,
        "Oh, you guys are Wendy's friends, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've started a brand new service\x01",
            "to replace your orbment covers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've got all the new, trendy designs\x01",
            "in stock. Please check them out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 4)

    label("loc_694")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                # 0
            "Replace Covers\x01",      # 1
            "Leave\x01",               # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_739")

    label("loc_71A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_739")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_739")

    Jump("loc_69E")

    label("loc_73E")

    TalkEnd(0x8)
    Jump("loc_74F")

    label("loc_746")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_74F")

    Return()

    # Function_4_5A4 end

    def Function_5_750(): pass

    label("Function_5_750")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2A")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_79A")
    MenuCmd(1, 0, "Blue Sheriff (Purchased)")
    MenuCmd(3, 0, 0x0)
    Jump("loc_7B6")

    label("loc_79A")

    MenuCmd(1, 0, "Blue Sheriff (1000 mira)")

    label("loc_7B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_7E3")
    MenuCmd(1, 0, "Peace Green (Purchased)")
    MenuCmd(3, 0, 0x1)
    Jump("loc_7FE")

    label("loc_7E3")

    MenuCmd(1, 0, "Peace Green (1000 mira)")

    label("loc_7FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_829")
    MenuCmd(1, 0, "Black Cat (Purchased)")
    MenuCmd(3, 0, 0x2)
    Jump("loc_842")

    label("loc_829")

    MenuCmd(1, 0, "Black Cat (1000 mira)")

    label("loc_842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_871")
    MenuCmd(1, 0, "Danger Orange (Purchased)")
    MenuCmd(3, 0, 0x3)
    Jump("loc_88E")

    label("loc_871")

    MenuCmd(1, 0, "Danger Orange (1000 mira)")

    label("loc_88E")

    MenuCmd(1, 0, "Cancel")

    AnonymousTalk(
        0x8,
        (
            scpstr(0x18),
            "Whose do you want to change?\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E9")
    Sleep(1)
    Return()

    label("loc_8E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_929")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_9E4")

    label("loc_929")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_9E4")

    label("loc_969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_9E4")

    label("loc_9A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E4")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_9E4")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A96")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Lloyd.\x01",
            "After purchase, the orbment cover visible\x01",
            "in the [ORBMENT] camp menu will be changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C32")

    label("loc_A96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Elie.\x01",
            "After purchase, the orbment cover visible\x01",
            "in the [ORBMENT] camp menu will be changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C32")

    label("loc_B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAB")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Tio.\x01",
            "After purchase, the orbment cover visible\x01",
            "in the [ORBMENT] camp menu will be changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C32")

    label("loc_BAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This cover is for Randy.\x01",
            "After purchase, the orbment cover visible\x01",
            "in the [ORBMENT] camp menu will be changed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C32")


    AnonymousTalk(
        0x8,
        "Is this what you want?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Replace]\x01",            # 0
            "[Don't Replace]\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D2D")

    ChrTalk(
        0x8,
        (
            "Oh, no. You seem to be short on mira.\x01",
            "Come back when you've got a bit more on hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFE")

    label("loc_D2D")


    ChrTalk(
        0x8,
        "Okay, just wait a moment!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "Here you are. Thanks for waiting.\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Lloyd's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_E91")

    label("loc_DD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E18")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Elie's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_E91")

    label("loc_E18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Tio's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_E91")

    label("loc_E56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E91")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Randy's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_E91")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECC")
    OP_DE(0x16, 0x0)

    label("loc_ECC")


    ChrTalk(
        0x8,
        "I look forward to your next visit!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_EFE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F17")

    label("loc_F0D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F17")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_75A")

    label("loc_F2A")

    Return()

    # Function_5_750 end

    def Function_6_F2B(): pass

    label("Function_6_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(
        0x8,
        (
            "Oh, Dad, are you still so\x01",
            "concerned about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even if it's not what I wanted at first,\x01",
            "this job is still great. He needs to\x01",
            "learn to let go sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1068")

    ChrTalk(
        0x8,
        (
            "Wendy always looks like she barely\x01",
            "slept at all in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "The manager's going to end up yelling at her again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_110E")

    ChrTalk(
        0x8,
        (
            "Dad's still trying to check on me, even\x01",
            "after everything I said yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm going to have to start ignoring him\x01",
            "completely until he stops.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_111C")
    Jump("loc_1CD2")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_11E6")

    ChrTalk(
        0x8,
        (
            "I told my dad I was tired of him coming\x01",
            "to spy on me at work, but then he\x01",
            "just left like he was about to cry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why do I have to feel so guilty\x01",
            "when I didn't do anything wrong...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_11E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1278")

    ChrTalk(
        0x8,
        (
            "Geez, my dad came to\x01",
            "watch me at work again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y'know, I'm happy he's worried and all,\x01",
            "but he's being really distracting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12F5")

    ChrTalk(
        0x8,
        (
            "Orbments from different manufacturers can\x01",
            "wildly vary in performance--even units in the\x01",
            "same price range.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(
        0x8,
        (
            "With orbments, I personally believe\x01",
            "that the most exciting moment is\x01",
            "choosing which one fits you best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please take your time and have\x01",
            "a look at what we have in stock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_13B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1486")

    ChrTalk(
        0x8,
        (
            "Look over there... Yeah, that's my\x01",
            "dad, thinking no one can see him...\x01",
            "Of course, he's completely obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Geez, no matter how much time passes,\x01",
            "he just can't let go of his little girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(
        0x8,
        (
            "Though all orbments use the same base tech,\x01",
            "manufacturers keep coming out with new models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Every customer has their own preferred brand.\x01",
            "It's fun to see these differences in action.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15EA")

    ChrTalk(
        0x8,
        (
            "Wendy used to train under someone,\x01",
            "but I don't know much about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard he's a very remarkable\x01",
            "orbal engineer, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_15EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C8")

    ChrTalk(
        0x8,
        (
            "The manager was being\x01",
            "so mean to Wendy\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And she was even helping him\x01",
            "out with something yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, I don't appreciate the\x01",
            "manager's ugly attitude one bit!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_177D")

    label("loc_16C8")


    ChrTalk(
        0x8,
        (
            "Even though Wendy went out of her\x01",
            "way to help him yesterday, he ended\x01",
            "up chewing her out this morning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Honestly, I don't appreciate the\x01",
            "manager's ugly attitude one bit!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177D")

    Jump("loc_1CD2")

    label("loc_1782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1857")

    ChrTalk(
        0x8,
        (
            "Our manager may be inconsiderate at times,\x01",
            "but he's really good at working with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our manager knows even less about\x01",
            "orbments than I do, but he's still\x01",
            "able to do a satisfying job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1930")

    ChrTalk(
        0x8,
        (
            "Good morning, everyone! ☆\x01",
            "A bracer just stopped by a little bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He had striking black hair,\x01",
            "beautiful amber-colored eyes... ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could this be love at first\x01",
            "sight for the young Chaco?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_19CA")

    ChrTalk(
        0x8,
        (
            "*sigh* Dad's back to spying\x01",
            "on me at work again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He always treats me like a little kid...\x01",
            "It's, like, super embarrassing, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_19CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(
        0x8,
        (
            "Welcoooome to Genten! ☆\x01",
            "This is the customer service desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For maintenance of your orbal goods,\x01",
            "please step right over to the other\x01",
            "counter!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD2")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE7")

    ChrTalk(
        0x8,
        "Oh, so you're a friend of Wendy's?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm Chaco, a salesperson here.\x01",
            "Pleased to meet you! ☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 0)
    Jump("loc_1CD2")

    label("loc_1AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4D")

    ChrTalk(
        0x8,
        (
            "This store has been thriving\x01",
            "ever since opening day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't really understand much about these\x01",
            "orbal doohickies myself... I learned\x01",
            "everything I know from Wendy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wendy's sooo smart. She knows\x01",
            "the answers to all of my questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(That sounds about right. Wendy's\x01",
            "been an orbal buff for as long as\x01",
            "I can remember.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CD2")

    label("loc_1C4D")


    ChrTalk(
        0x8,
        (
            "Wendy's sooo smart. She knows\x01",
            "the answer to all my questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm constantly learning new tidbits\x01",
            "about orbments from her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD2")

    Return()

    # Function_6_F2B end

    def Function_7_1CD3(): pass

    label("Function_7_1CD3")

    Call(0, 8)
    Return()

    # Function_7_1CD3 end

    def Function_8_1CD7(): pass

    label("Function_8_1CD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFC")
    Call(0, 17)
    Return()

    label("loc_1CFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1D")
    Call(0, 16)
    Return()

    label("loc_1D1D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298A")
    EventBegin(0x0)
    Fade(500)
    OP_68(7380, 1500, -2280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 6900, 0, -2250, 90)
    SetChrPos(0x102, 6900, 0, -1100, 90)
    SetChrPos(0x103, 5600, 0, -2250, 90)
    SetChrPos(0x104, 5600, 0, -1100, 90)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11PHowdy, everyone! Welcome to\x01",
            "Genten Orbal Factory--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PShoot, I mean, welcome\x01",
            "to Genten Orbal Store!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#11POh, no way... LLOYD! Is that really you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F#6PWendy?! Wait a second. What are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHmph, how rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCan't you tell by looking at me?\x01",
            "I'm a Genten engineer!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F71")
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    label("loc_1F71")


    ChrTalk(
        0x101,
        (
            "#0011F#6PS-Seriously?! I know you mentioned you\x01",
            "were looking for a job in your letters...\x02\x03",
            "#0002FI just wasn't really expecting to run into\x01",
            "you while working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302F#5POh, this lovely lady is an old friend of yours,\x01",
            "Lloyd? I'm a lil' jealous.\x02\x03",
            "#0309FWanna go on a date when your shift ends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F#6PNow isn't the time for this, Randy...\x01",
            "We're on duty, for crying out loud.\x02\x03",
            "#0100FIt's nice to meet you, Wendy. I've heard\x01",
            "great things about Genten, but the\x01",
            "rumors don't do it justice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh, are you guys Lloyd's colleagues?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PTruth be told, the store was decorated\x01",
            "based on the owner's personal taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI should've mentioned this sooner,\x01",
            "but this is customer service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom here, we can provide maintenance\x01",
            "for all of your orbment's needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#6PAll right. We'll be leaving our orbments in\x01",
            "your capable hands from now on, Wendy.\x02\x03",
            "#0005FOh, but our orbments are the Enigma models.\x01",
            "Is that going to be an issue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh, wow. So you guys got your hands\x01",
            "on the brand new models, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI've got you covered! I should have\x01",
            "the tools for them right here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI have a few regulars that use that model, too.\x01",
            "Man, bracers sure love their orbments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011F#6PTh-They have them, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F#6PI am not surprised the guild's connections\x01",
            "have allowed them to acquire cutting-edge\x01",
            "technology, as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0302F#5PHaha, damn. We better catch up or else\x01",
            "they're gonna leave us in the dust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F#6PThis isn't a laughing matter, Randy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#0012F#6PO-Oh. Just ignore them.\x02\x03",
            "#0000FAnyway, I'd recommend getting used to\x01",
            "us pestering you, Wendy. We'll be counting\x01",
            "on you for any orbment problems we have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PNo problem. Leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhenever you get that itch to modify\x01",
            "your orbment, just lemme know and\x01",
            "I'll get you all set up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso, if you have any general questions\x01",
            "about your orbments, just ask away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYou're speaking to an orbal pro, after all!\x02",
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 180, 60, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you select 'Upgrade/Synthesize' at the orbal store,\x01",
            "you can synthesize new quartz or open slots in your\x01",
            "tactical orbments.\x02\x03",
            "If you synthesize new quartz and place them in\x01",
            "your orbments, you'll be able to use new arts.\x01",
            "(Select [QUARTZ] from the menu.)\x02\x03",
            "If you open orbment slots, the number of quartz you can\x01",
            "set will increase, while also increasing your maximum EP.\x01",
            "(Select [SLOT] from the menu.)\x02\x03",
            "To use each function, septium fragments\x01",
            "called 'sepith' are required. You can\x01",
            "obtain sepith by defeating monsters.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x4C, 1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 6980, 0, -1400, 90)
    EventEnd(0x5)
    Return()

    label("loc_298A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C20")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Upgrade/Synthesize\x01",      # 1
            "Ask Questions\x01",           # 2
            "Ask About Request\x01",       # 3
            "Leave\x01",                   # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A30")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A50")
    Call(0, 11)

    label("loc_2A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2A60")
    OP_AF(0xF)
    Jump("loc_2AA2")

    label("loc_2A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A70")
    OP_AF(0xE)
    Jump("loc_2AA2")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A80")
    OP_AF(0xD)
    Jump("loc_2AA2")

    label("loc_2A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A90")
    OP_AF(0xC)
    Jump("loc_2AA2")

    label("loc_2A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2AA0")
    OP_AF(0xB)
    Jump("loc_2AA2")

    label("loc_2AA0")

    OP_AF(0xA)

    label("loc_2AA2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C1B")

    label("loc_2AB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2C1B")

    label("loc_2AD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEB")

    ChrTalk(
        0x9,
        (
            "In order to assess the Enigma's performance,\x01",
            "try casting the art that conceals yourself from\x01",
            "enemies, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I need ya to test it out in actual\x01",
            "combat in order to see if it works\x01",
            "or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once you give it a whirl,\x01",
            "lemme know the details!\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C1B")

    label("loc_2BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BFF")
    Jump("loc_2C1B")

    label("loc_2BFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C1B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_2C1B")

    Jump("loc_29B1")

    label("loc_2C20")

    Jump("loc_2D73")

    label("loc_2C25")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D73")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Upgrade/Synthesize\x01",      # 1
            "Ask Questions\x01",           # 2
            "Leave\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C9C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2C9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CBC")
    Call(0, 11)

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2CCC")
    OP_AF(0xF)
    Jump("loc_2D0E")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CDC")
    OP_AF(0xE)
    Jump("loc_2D0E")

    label("loc_2CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2CEC")
    OP_AF(0xD)
    Jump("loc_2D0E")

    label("loc_2CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2CFC")
    OP_AF(0xC)
    Jump("loc_2D0E")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2D0C")
    OP_AF(0xB)
    Jump("loc_2D0E")

    label("loc_2D0C")

    OP_AF(0xA)

    label("loc_2D0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D6E")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2D6E")

    label("loc_2D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D52")
    Jump("loc_2D6E")

    label("loc_2D52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_2D6E")

    Jump("loc_2C2F")

    label("loc_2D73")

    TalkEnd(0x9)
    Return()

    # Function_8_1CD7 end

    def Function_9_2D77(): pass

    label("Function_9_2D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2E66")

    ChrTalk(
        0x9,
        (
            "You really helped me out there. An Enigma\x01",
            "user's opinion will be invaluable for the report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, you better believe I'll be turning\x01",
            "to you when I need a hand, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou can always count\x01",
            "on us, Wendy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_2E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(
        0x9,
        (
            "Mr. Fernand seems to have finally\x01",
            "started to mellow out a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "More importantly, he's actually beginning\x01",
            "to study orbments to help out the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, should I take this opportunity\x01",
            "to try and tutor him again?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3001")

    label("loc_2F65")


    ChrTalk(
        0x9,
        (
            "Hopefully, this breakthrough will help us get\x01",
            "along better, since we're always butting heads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Should I help him with his\x01",
            "orbal studies next time?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3001")

    Jump("loc_4CB9")

    label("loc_3006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_307A")

    ChrTalk(
        0x9,
        "*yawn* ...I'm really not a morning gal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I envy Chaco's energy... It'd help right about now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_307A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A8")

    ChrTalk(
        0x9,
        (
            "I used to not think highly of orbal stores, but\x01",
            "they've grown on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The equipment is really well maintained, so it\x01",
            "makes servicing much easier. Customers also\x01",
            "visit more frequently compared to the old workshop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I guess presentation matters a lot, doesn't it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3254")

    label("loc_31A8")


    ChrTalk(
        0x9,
        (
            "There was one customer who stopped me in the\x01",
            "street a while ago to thank me for my repair work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Stuff like that is why I'm glad to\x01",
            "come into work in the morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3254")

    Jump("loc_4CB9")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_3267")
    Jump("loc_4CB9")

    label("loc_3267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_32EC")

    ChrTalk(
        0x9,
        "My dad had to go on another business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh* My life would be easier if\x01",
            "I made him take Pansy with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_32EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3907")

    ChrTalk(
        0x9,
        "Oh, heya Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Glad to see you're still kicking!\x01",
            "Woohoo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FWoohoo!\x01",
            "This place is amazing!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x153, 500)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33F8")

    ChrTalk(
        0x102,
        (
            "#0100FOnce again, KeA chimes\x01",
            "in with perfect timing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BE")

    label("loc_33F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3466")

    ChrTalk(
        0x103,
        (
            "#0200FIt is as if KeA always knows the perfect\x01",
            "time to cut into the conversation...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34BE")

    label("loc_3466")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34BE")

    ChrTalk(
        0x104,
        (
            "#0300FKeDo always knows the best time to\x01",
            "jump into a conversation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BE")

    OP_64(0x9)

    ChrTalk(
        0x9,
        "Oh, who's this? She's as cute as a button!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha. So we've heard.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "Hey, don't go thinking that I\x01",
            "only admire orbal tech, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, I'm shocked... Who knew that\x01",
            "you were so dependable, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHuh...? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The SSS is watching over a kid that got\x01",
            "lost during the Anniversary Festival, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aha! That must be the reason why\x01",
            "I haven't seen you in over a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(She's not technically wrong...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36F7")

    ChrTalk(
        0x102,
        (
            "#0100FHer name is KeA. We're actually looking\x01",
            "into who she is, at the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_36F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3767")

    ChrTalk(
        0x103,
        (
            "#0200FThis girl is named KeA... We are investigating\x01",
            "who she is and where she's from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37C9")

    label("loc_3767")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37C9")

    ChrTalk(
        0x104,
        (
            "#0300FThis bundle of joy here is KeA. We're tryin'\x01",
            "to track down her family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C9")


    ChrTalk(
        0x9,
        (
            "Haha, I was right on the mark. Hmm, don't\x01",
            "think I have any leads for you, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, if you need help, just gimme a shout!\x01",
            "I've got a little sister, so I've gotten pretty\x01",
            "used to taking care of kids, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI appreciate it, Wendy. If we ever need\x01",
            "a babysitter, I'll know who to call.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 6)
    Jump("loc_3A1D")

    label("loc_3907")

    TurnDirection(0x9, 0x153, 0)

    ChrTalk(
        0x9,
        (
            "KeA, eh? She looks\x01",
            "a little younger than\x01",
            "Pansy, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "KeA, if you start to get worn out,\x01",
            "be sure to let Lloyd know, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He isn't exactly the greatest when\x01",
            "it comes to noticing these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FOkay, I will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHahaha, thanks, Wendy...\x02",
    )

    CloseMessageWindow()

    label("loc_3A1D")

    Jump("loc_4CB9")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AE1")

    ChrTalk(
        0x9,
        (
            "By the way, Dad should be coming\x01",
            "home from his business trip next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He says he'll make it in time for the Anniversary\x01",
            "Festival. Phew, cutting it close, huh, Dad?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_3AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC4")

    ChrTalk(
        0x9,
        (
            "Your typical trains coming and going at the station\x01",
            "are mostly made by the Empire's Reinford Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, with that unicorn ornament stuck up\x01",
            "on the front, it feels very Erebonian indeed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C38")

    label("loc_3BC4")


    ChrTalk(
        0x9,
        (
            "When I think of everything that the Reinford\x01",
            "Company manufactures, the words\x01",
            "'rough' and 'stern' come to mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C38")

    Jump("loc_4CB9")

    label("loc_3C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3CCB")

    ChrTalk(
        0x9,
        "It's almost time for me to head home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe I'll stop by Morges and\x01",
            "buy a sweet roll as a little\x01",
            "present for Pansy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_3CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DEB")

    ChrTalk(
        0x9,
        (
            "How exactly did they get the orbal vehicle\x01",
            "on display into the shop, you ask?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, the correct answer is...\x01",
            "They built the shop around it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FS-Seriously?! Huh, that's really a\x01",
            "backwards way of doing things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Can't you tell I'm joking?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E48")

    label("loc_3DEB")


    ChrTalk(
        0x9,
        (
            "Haha, oh, Lloyd. That serious\x01",
            "demeanor of yours makes it\x01",
            "that much easier to tease you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E48")

    Jump("loc_4CB9")

    label("loc_3E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3FD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4B")

    ChrTalk(
        0x9,
        (
            "Lloyd, we got a new Epstein-made orbal\x01",
            "vacuum cleaner in stock today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FUh, Wendy...are you trying\x01",
            "to trick me into buying it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahaha, whaaat? No way!\x01",
            "I'm just getting you to admire\x01",
            "its insane suction power!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FCD")

    label("loc_3F4B")


    ChrTalk(
        0x9,
        (
            "We got a new Epstein-made orbal\x01",
            "vacuum cleaner in stock today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, I just adore the smell of a\x01",
            "fresh, new orbal gadget!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCD")

    Jump("loc_4CB9")

    label("loc_3FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_434B")

    ChrTalk(
        0x9,
        (
            "Wow, the Crossbell Guardian Force placed\x01",
            "an order for another armored car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Phew, their equipment is as\x01",
            "top-of-the-line as it can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Maybe I can ask to be one of their engineers...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4346")

    ChrTalk(
        0x104,
        (
            "#0300FWell, they're a government-funded group\x01",
            "that protects the state, y'know. They've\x01",
            "already got plenty of support.\x02\x03",
            "#0304FI would probably call it quits on tryin'\x01",
            "to work for 'em, if I were you.\x02\x03",
            "#0300FBuuuut I can think of another organization\x01",
            "that could make use of a pretty face like yours!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x9,
        "Oh, wow! Thanks a bunch, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I knew it. I really should aim to get\x01",
            "into an orbal design studio, right?\x02",
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
        0x104,
        "#0306F(That's not what I...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Brilliant encore after your performance\x01",
            "at St. Ursula. Another zero out of ten.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 4)

    label("loc_4346")

    Jump("loc_4CB9")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_43F9")

    ChrTalk(
        0x9,
        (
            "Our manager's at it again... He barely knows\x01",
            "anything about orbal tech, but he still\x01",
            "tries to show off for customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'll have to tutor him later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CB9")

    label("loc_43F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BD")

    ChrTalk(
        0x9,
        (
            "Howdy, Lloyd and company.\x01",
            "Work still treating you well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, well, we're chugging\x01",
            "along, somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FOur jobs are all over the place,\x01",
            "so it can be scabrous at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahahaha...Yes, well, as long\x01",
            "as you keep doing your best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before going out, lemme take\x01",
            "a look at all your orbments'\x01",
            "conditions, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You'll regret it if you dooon't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOkay, okay, I hear you.\x01",
            "Thanks, Wendy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 5)
    Jump("loc_4762")

    label("loc_45BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D4")

    ChrTalk(
        0x9,
        (
            "The Enigma seems to be really\x01",
            "popular already. Most of the\x01",
            "bracers are already using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even that Dudley guy from the police\x01",
            "came down to get one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FSounds like we better hurry up\x01",
            "and get the hang of this thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FThat's right...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4762")

    label("loc_46D4")


    ChrTalk(
        0x9,
        (
            "Police officers and bracers come here\x01",
            "pretty often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've noticed a big boom in the amount of\x01",
            "people starting to use newer orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4762")

    Jump("loc_4CB9")

    label("loc_4767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_48B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482A")

    ChrTalk(
        0x9,
        (
            "People keep telling me that our manager\x01",
            "used to be a famous designer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I mean, his artistic sense isn't lacking, but...\x01",
            "with THAT personality, I don't buy it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_48AF")

    label("loc_482A")


    ChrTalk(
        0x9,
        (
            "Our store's interior was all designed\x01",
            "by our manager, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You can probably tell just by\x01",
            "taking a few glances around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48AF")

    Jump("loc_4CB9")

    label("loc_48B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2E")

    ChrTalk(
        0x9,
        (
            "Y'know, this orbal store was actually just\x01",
            "an ordinary factory up until last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But when the previous manager was replaced,\x01",
            "the new manager's store policies aimed to\x01",
            "make Genten more appealing to customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Personally, I much prefer the unrefined\x01",
            "workshop aesthetic to this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, that image definitely\x01",
            "suits you better, Wendy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm sorry, what was that, Lloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006FS-Sorry, it was nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, yeah. I heard my old teacher opened\x01",
            "up his own store downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you guys find the time, it might\x01",
            "be worth popping in to say hello.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 0)
    Jump("loc_4CB9")

    label("loc_4B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C54")

    ChrTalk(
        0x9,
        (
            "Y'know, this orbal store was actually just\x01",
            "an ordinary factory up until last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My teacher is one of the most skilled\x01",
            "orbal engineers I've seen, but, well...\x01",
            "He was a bit of an outcast, so he quit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll admit, I prefer the unrefined\x01",
            "workshop more than this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4CB9")

    label("loc_4C54")


    ChrTalk(
        0x9,
        (
            "I heard my old teacher opened up\x01",
            "a store downtown, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You guys should check it out!\x02",
    )

    CloseMessageWindow()

    label("loc_4CB9")

    Return()

    # Function_9_2D77 end

    def Function_10_4CBA(): pass

    label("Function_10_4CBA")


    ChrTalk(
        0x9,
        (
            "All right. What did ya want\x01",
            "to ask me about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5652")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "About Tactical Orbments\x01",      # 0
            "About Quartz\x01",                 # 1
            "About Slots\x01",                  # 2
            "About Orbal Arts\x01",             # 3
            "Cancel\x01",                       # 4
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D8B")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_4D8B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4DAD"),
        (1, "loc_5018"),
        (2, "loc_518C"),
        (3, "loc_52EB"),
        (SWITCH_DEFAULT, "loc_563E"),
    )


    label("loc_4DAD")


    ChrTalk(
        0x9,
        (
            "Tactical orbments are small, portable orbal devices\x01",
            "specially tuned for their owner's combat style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not only do they strengthen the user, they also\x01",
            "support them through the use of orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The average person refers to them as orbments,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As for the ones you guys use, that's the Enigma,\x01",
            "the newest orbments around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Orbments are completely suited and optimized\x01",
            "for their operator, so the sepith lines may vary\x01",
            "depending on the user.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Slots can have different elemental locks, and the\x01",
            "layout of the sepith lines usually differ. It's a\x01",
            "good idea to compare the ones you possess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564D")

    label("loc_5018")


    ChrTalk(
        0x9,
        (
            "Quartz are crystal circuits used in orbments, made\x01",
            "from processed sepith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you bring me the required sepith, we can synthesize\x01",
            "the quartz you want here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are various benefits depending on the quartz,\x01",
            "and when the elemental values are over a fixed\x01",
            "threshold, you can start to use orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "When you've gathered some sepith, give it a try.\x02",
    )

    CloseMessageWindow()
    Jump("loc_564D")

    label("loc_518C")


    ChrTalk(
        0x9,
        (
            "It's common occurrence for quartz slots\x01",
            "to be sealed on a fresh orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to set a quartz, first you need\x01",
            "an open slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you open a slot, the number of quartz\x01",
            "you can use increases, as well as your\x01",
            "maximum EP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though you need sepith to open slots,\x01",
            "this service is invaluable. I'd come unseal\x01",
            "slots whenever you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564D")

    label("loc_52EB")


    ChrTalk(
        0x9,
        (
            "The magic activated using tactical orbments are\x01",
            "what we like to call orbal arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Most people just call them 'arts,' though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "With the orbment's internal mechanism, the quartz,\x01",
            "by forming a resonance chain with the user, can\x01",
            "produce magical phenomena...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Well, I'll spare you the intricacies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The variety of arts that can be summoned are\x01",
            "decided by the sum total of the elemental\x01",
            "values of the quartz on each sepith line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's a little difficult to explain... Right, here's\x01",
            "an example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By setting earth quartz on connecting lines,\x01",
            "if earth's elemental value total becomes two\x01",
            "or higher, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...the Quake art can now be activated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The more quartz you set, the more arts you'll\x01",
            "be able to use.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As for the other art combinations, they're\x01",
            "mentioned in the arts list. Feel free to check\x01",
            "it any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_564D")

    label("loc_563E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_564D")

    label("loc_564D")

    Jump("loc_4CF6")

    label("loc_5652")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_4CBA end

    def Function_11_5660(): pass

    label("Function_11_5660")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "That's right, don't you guys have\x01",
            "some high-level quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat's that, exactly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They're quartz that are too powerful\x01",
            "to set in a normal slot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to set them, the slot\x01",
            "itself needs to be strengthened.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57FD")

    ChrTalk(
        0x9,
        (
            "I'm actually still learning the ropes\x01",
            "on level-quartz synthesis myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Leave the slot strengthening to me.\x01",
            "If you need help, give me a shout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5875")

    label("loc_57FD")


    ChrTalk(
        0x9,
        (
            "I've actually just started to handle\x01",
            "slot strengthening and high-level quartz,\x01",
            "so if you need help, gimme a shout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5875")

    OP_5A()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can now upgrade your slots.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you select [SLOT] and choose a slot that is\x01",
            "already opened, you can upgrade its level.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In addition to gaining the ability to set high-level\x01",
            "quartz, your maximum EP is also raised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)
    Return()

    # Function_11_5660 end

    def Function_12_5981(): pass

    label("Function_12_5981")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A78")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Hmm... Okay, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't discount the possibility that the\x01",
            "lights are broken due to dirt in the socket...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "E-Excuse me, sir.\x01",
            "Might you be needing something?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    label("loc_5A78")


    ChrTalk(
        0xFE,
        "Would you like to hear about our orbments?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry. I'm still studying orbments...\x01",
            "Please, ask the employees\x01",
            "at the customer service desk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_5B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5BA0")

    ChrTalk(
        0xFE,
        (
            "Damn it, Wendy. She's about to fall\x01",
            "asleep while on the job again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, she's not going\x01",
            "to hear the end of this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_5BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5C39")

    ChrTalk(
        0xFE,
        (
            "Wendy's recently started to compliment\x01",
            "me on how I set up the displays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-It's not like I need her approval or\x01",
            "anything, though!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_5C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5C47")
    Jump("loc_6851")

    label("loc_5C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D2B")

    ChrTalk(
        0xFE,
        (
            "Wendy asked if she could work the customer\x01",
            "service desk outside regular support hours...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, it IS thanks\x01",
            "to her we've bagged so many regulars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, maybe I'll think about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_5D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E88")

    ChrTalk(
        0xFE,
        (
            "Oh, are you considering purchasing\x01",
            "this cutting-edge orbal car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105FOooh, Lloyd. Can I touch it?\x02\x03",
            "#1100F(*sneakily touches*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FW-Wait, no, stop! If you somehow\x01",
            "scratched it, we'd have to arrest\x01",
            "ourselves! We don't have the mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1106FAwww...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, try to keep a\x01",
            "closer eye on the girl.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5EE8")

    label("loc_5E88")


    ChrTalk(
        0xFE,
        (
            "*cough* Please, try to keep a\x01",
            "closer eye on the girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Crap, they caught us...)\x02",
    )

    CloseMessageWindow()

    label("loc_5EE8")

    Jump("loc_6851")

    label("loc_5EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5F96")

    ChrTalk(
        0xFE,
        (
            "I'd like for our orbal car sales\x01",
            "to start increasing soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the state government plans to keep\x01",
            "diffusing cars across all of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_5F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6094")

    ChrTalk(
        0xFE,
        (
            "I can't believe Wendy...\x01",
            "Claiming there was a flaw in\x01",
            "my fantastic displays...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's mortifying, but perhaps what\x01",
            "she said has some merit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only because she worked at the workshop\x01",
            "before it turned into this orbal store...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_6094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_629A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D0")

    ChrTalk(
        0xFE,
        (
            "Believe it or not, this incredible store\x01",
            "carries the brand new, jaw-dropping\x01",
            "orbal network...terminals? I think...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not really acquainted with them,\x01",
            "but they're pretty dang expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. If you'd like, please take a look\x01",
            "at our Epstein Foundation display\x01",
            "right here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6295")

    label("loc_61D0")


    ChrTalk(
        0xFE,
        (
            "Here in our second floor display, you'll\x01",
            "find all of those, uh, terminal doohickeys\x01",
            "developed by the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if everyone will have\x01",
            "one of these in the near future...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6295")

    Jump("loc_6851")

    label("loc_629A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_635F")

    ChrTalk(
        0xFE,
        (
            "For the Anniversary Festival, I plan\x01",
            "to hold a big orbal camera sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, orbal cameras have become\x01",
            "all the rage with the average person,\x01",
            "due to significant price cuts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_635F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_63FC")

    ChrTalk(
        0xFE,
        (
            "I intend to stock up on goods that'll sell like\x01",
            "wildfire during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehehe, next month can't come soon enough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_63FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_64A4")

    ChrTalk(
        0xFE,
        (
            "Damn it, Wendy. Yesterday, she\x01",
            "went and embarrassed me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because she has the brains doesn't\x01",
            "mean she should act stuck-up about it, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_64A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_64FA")
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "Umm, right... Suction power and,\x01",
            "uh, something else, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_64FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_65BD")

    ChrTalk(
        0xFE,
        (
            "Come on, everyone's got to have\x01",
            "some pep in their step today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our goal is to beat Times in sales.\x01",
            "This month I'm going to shatter that\x01",
            "irritable sales record! I swear it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6851")

    label("loc_65BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_66F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669D")

    ChrTalk(
        0xFE,
        (
            "Old-fashioned displays,\x01",
            "ugly-looking appliances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this era, even a mere workshop\x01",
            "must strive to be beautiful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Genten was designed with cleanliness\x01",
            "and beauty as a selling point.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_66EF")

    label("loc_669D")


    ChrTalk(
        0xFE,
        (
            "In this day and age, everything\x01",
            "must be a thing of beauty!\x01",
            "That is my credo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66EF")

    Jump("loc_6851")

    label("loc_66F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6851")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D0")

    ChrTalk(
        0xFE,
        (
            "Here at Genten, we offer various\x01",
            "orbal goods bound to find use in\x01",
            "everyone's day-to-day life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure there's a product here calling your\x01",
            "name. Please, shop to your heart's content.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6851")

    label("loc_67D0")


    ChrTalk(
        0xFE,
        (
            "Incidentally, this cutting-edge orbal car comes\x01",
            "in at a reasonable price of 15,000,000 mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How does that sound, sir?\x02",
    )

    CloseMessageWindow()

    label("loc_6851")

    TalkEnd(0xFE)
    Return()

    # Function_12_5981 end

    def Function_13_6855(): pass

    label("Function_13_6855")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6903")

    ChrTalk(
        0xFE,
        (
            "In the past, I never imagined I'd be\x01",
            "driving an orbal car on the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And in the future, I bet even more\x01",
            "unimaginable things will be invented.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6949")

    ChrTalk(
        0xFE,
        (
            "Hehe, I like to stop by here\x01",
            "early in the morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_69E2")

    ChrTalk(
        0xFE,
        (
            "Orbments are truly amazing. They've\x01",
            "made our lives much more convenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoever first invented them\x01",
            "must have been a great man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_69E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_69F0")
    Jump("loc_742C")

    label("loc_69F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE0")

    ChrTalk(
        0xFE,
        (
            "That service desk lady is so talented...\x01",
            "If you bring her a broken orbal light or\x01",
            "something, she fixes it right in front of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm impressed... Who knew Crossbell had\x01",
            "someone that amazing living here?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B38")

    label("loc_6AE0")


    ChrTalk(
        0xFE,
        (
            "I love orbal gadgets, but haven't the foggiest\x01",
            "idea about how they're constructed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B38")

    Jump("loc_742C")

    label("loc_6B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6C1F")

    ChrTalk(
        0xFE,
        (
            "Oh, my. Have you come to\x01",
            "buy an orbal stove, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm currently comparing all of the\x01",
            "ones available to each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a big purchase, after all. I have to\x01",
            "be sure I choose the right one, hehe...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6CE7")

    ChrTalk(
        0xFE,
        (
            "According to an employee, a new\x01",
            "Verne Company orbal camera is\x01",
            "going to be in stock next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... I can't pass this opportunity.\x01",
            "I've got to clear up next week's schedule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6DBB")

    ChrTalk(
        0xFE,
        (
            "I wonder why looking around\x01",
            "the orbal store is so much fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Vibrant orbal contraptions...\x01",
            "Sophisticated, sleek appliances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, even window shopping\x01",
            "is strangely exhilarating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6E9C")

    ChrTalk(
        0xFE,
        (
            "I bought a vacuum cleaner last month, and I\x01",
            "intend to purchase a refrigerator this month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But which model do I pick...?\x01",
            "I'm just so nervous since it's such a big\x01",
            "purchase, and I'd like a charming one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6F6E")

    ChrTalk(
        0xFE,
        (
            "Oh, my. Is this new? It's so fancy!\x01",
            "I do love looking at the newest gadgets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The making of complex stuff like this flies right over\x01",
            "my head, but I can't get enough of these new designs!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_6F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_704B")

    ChrTalk(
        0xFE,
        (
            "Personally, I'm not nearly as interested in\x01",
            "Arc en Ciel as everyone else seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I kind of want to see them at least once,\x01",
            "but before I invest in a ticket, I'd like to\x01",
            "buy a new refrigerator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_704B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_716F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7112")

    ChrTalk(
        0xFE,
        (
            "You'd be surprised at how many\x01",
            "tourists like to stop by Genten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, I can definitely relate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess since it stands out, you\x01",
            "just can't help but stop by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_716A")

    label("loc_7112")


    ChrTalk(
        0xFE,
        (
            "Foreigners are probably super curious\x01",
            "about what you can find in an 'orbal store.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_716A")

    Jump("loc_742C")

    label("loc_716F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_71FF")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "I was planning on buying a vacuum cleaner...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but what's the difference between\x01",
            "the red one and the white one?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_71FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7284")

    ChrTalk(
        0xFE,
        (
            "Huh, there's a brand new orbal\x01",
            "vacuum releasing this month?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I spoil myself a bit and\x01",
            "place an order?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_7284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7313")

    ChrTalk(
        0xFE,
        (
            "Hmm, there's too much fancy\x01",
            "stuff being made recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So this was made by...ZCF?\x01",
            "Huh, where's that manufacturer from?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_742C")

    label("loc_7313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_742C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7400")

    ChrTalk(
        0xFE,
        (
            "So, this is an orbal store.\x01",
            "I'm surprised by how colorful it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I only came to purchase an orbal light, but\x01",
            "now I want to look at all the other goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, my. What are those things over there?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_742C")

    label("loc_7400")


    ChrTalk(
        0xFE,
        "Are you out shopping? Heehee, me, too.\x02",
    )

    CloseMessageWindow()

    label("loc_742C")

    TalkEnd(0xFE)
    Return()

    # Function_13_6855 end

    def Function_14_7430(): pass

    label("Function_14_7430")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_75D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_758C")

    ChrTalk(
        0xFE,
        (
            "Chaco was trying to get a position at the department store\x01",
            "reception desk, but I stopped her outright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I started to feel like I was being mean,\x01",
            "so now I'm making sure she's able to\x01",
            "have a safe workday to make up for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, she's a bit unreliable in general,\x01",
            "so I have to make sure she does it right!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_75D1")

    label("loc_758C")


    ChrTalk(
        0xFE,
        (
            "Don't worry, Chaco... If anything\x01",
            "happens, Papa's right here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75D1")

    Jump("loc_848E")

    label("loc_75D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7675")

    ChrTalk(
        0xFE,
        (
            "Sometimes I worry that my\x01",
            "unwavering presence might\x01",
            "be a distraction to Chaco...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No... What am I saying? That\x01",
            "could never be the case!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_7675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_781E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7796")

    ChrTalk(
        0xFE,
        (
            "Chaco told me yesterday how I don't\x01",
            "need to watch over her and all that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...isn't it natural for a father to be worried about\x01",
            "how his only daughter is doing at work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, this just means I have to be\x01",
            "even sneakier so she doesn't catch me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7819")

    label("loc_7796")


    ChrTalk(
        0xFE,
        "I'm not here. I'm just a normal shopper...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*glance*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, Chaco seems to be working\x01",
            "hard. Papa's proud of you, baby!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7819")

    Jump("loc_848E")

    label("loc_781E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_782C")
    Jump("loc_848E")

    label("loc_782C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_783A")
    Jump("loc_848E")

    label("loc_783A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_78E4")

    ChrTalk(
        0xFE,
        (
            "My daughter seems to really be\x01",
            "getting the hang of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was concerned about her working in an\x01",
            "orbal store at first, but she's doing so well!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_78E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7974")

    ChrTalk(
        0xFE,
        (
            "Now...time to see how\x01",
            "Chaco will do today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how hard I try,\x01",
            "Chaco always seems to\x01",
            "notice me when I'm around...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_7974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7A50")

    ChrTalk(
        0xFE,
        (
            "Quite a few companies have already started to\x01",
            "adopt the orbal network into their business model.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given the massive scale of the\x01",
            "IBC, perhaps they've already started\x01",
            "using it on a practical level.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_7A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7B4D")

    ChrTalk(
        0xFE,
        (
            "Chaco, what are you thinking...?\x01",
            "A young woman working late\x01",
            "hours like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What would you do if some hoodlum\x01",
            "attacked you on the way home?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You just need to hurry home, and I'll have\x01",
            "a nice, warm dinner waiting for you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_7B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7BEA")

    ChrTalk(
        0xFE,
        (
            "Huh, an orbal camera...?\x01",
            "Maybe it's about time I finally get one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The way they've been able to shrink\x01",
            "recent models blows my mind...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_7BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D34")

    ChrTalk(
        0xFE,
        (
            "So, these new products were\x01",
            "manufactured by ZCF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ZCF is an acronym for Zeiss Central Factory.\x01",
            "It's an engineering factory located in Liberl\x01",
            "once run by clockmakers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're hailed as some of the brightest minds\x01",
            "in orbal engineering. I've heard they have the\x01",
            "best airship technology, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7DB8")

    label("loc_7D34")


    ChrTalk(
        0xFE,
        (
            "ZCF was the first factory to develop\x01",
            "an orbal airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nowadays, most international airships\x01",
            "you'll ride on are ZCF-made.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DB8")

    Jump("loc_848E")

    label("loc_7DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF8")

    ChrTalk(
        0xFE,
        (
            "Oh, here's that new type of penlight\x01",
            "created by the Verne Company!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, you see, I worked in a factory affiliated\x01",
            "with the Verne Company. My colleagues were\x01",
            "researching this, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like they finally made the finishing\x01",
            "touches on it. I'm kinda proud of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7F4F")

    label("loc_7EF8")


    ChrTalk(
        0xFE,
        (
            "Huh, so they finally finished it, did they?\x01",
            "I'm proud of them... Good work, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F4F")

    Jump("loc_848E")

    label("loc_7F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_807E")

    ChrTalk(
        0xFE,
        (
            "Erebonia's Reinford Company made their\x01",
            "name as a big weapons manufacturer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, they operate as a massive conglomerate,\x01",
            "with each of its divisions producing orbal goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Their products often reflect fortitude and energy,\x01",
            "much like the Erebonian people themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848E")

    label("loc_807E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_82D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81EA")

    ChrTalk(
        0xFE,
        (
            "As it stands, there are four major\x01",
            "orbment manufacturers in Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have the Empire's Reinford Company,\x01",
            "the Republic's Verne Company, Liberl's\x01",
            "ZCF, and the Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Among these, the Epstein Foundation is\x01",
            "the most research-oriented organization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Their products aren't really geared towards the public.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_82CB")

    label("loc_81EA")


    ChrTalk(
        0xFE,
        (
            "The Epstein Foundation focuses on\x01",
            "expanding their ever-growing research.\x01",
            "Their products aren't really geared towards the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Due to that, they crank out quite the odd\x01",
            "products. Well, they interest me, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82CB")

    Jump("loc_848E")

    label("loc_82D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_83AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8365")

    ChrTalk(
        0xFE,
        "Let's see... What's Chaco up to now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a concerned parent, I always end\x01",
            "up stopping by to see how she's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_83A9")

    label("loc_8365")


    ChrTalk(
        0xFE,
        (
            "J-Just to be clear, this\x01",
            "isn't stalking, not in the\x01",
            "slightest!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83A9")

    Jump("loc_848E")

    label("loc_83AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_848E")

    ChrTalk(
        0xFE,
        (
            "I was working as an orbment-maker\x01",
            "years ago, but I'm retired now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An assortment of goods from all over\x01",
            "Zemuria are sold right here in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's the ideal place to appreciate each and every one!\x02",
    )

    CloseMessageWindow()

    label("loc_848E")

    TalkEnd(0xFE)
    Return()

    # Function_14_7430 end

    def Function_15_8492(): pass

    label("Function_15_8492")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(11560, 1500, 5410, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26850, 0)
    SetChrPos(0x101, -2990, 0, 1860, 89)
    SetChrPos(0x102, -3340, 0, 3240, 45)
    SetChrPos(0x103, -4740, 0, 3260, 45)
    SetChrPos(0x104, -4310, 0, 1920, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetCameraDistance(24490, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(14920, 1500, 20510, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(43880, 0)
    OP_68(4170, 1500, 6370, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-2550, 1500, 2270, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22240, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#0305F#6PWow... So this is that orbal store people\x01",
            "have been clamorin' about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F#5PFrom the biggest orbal car to the smallest\x01",
            "orbment, they have it all...\x02\x03",
            "#0102FOn top of that, their new redesign gives off\x01",
            "that sleek and modern feeling, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F#5PHard to believe this was just a simple\x01",
            "factory three years ago...\x02\x03",
            "#0001FAnyway, we should look for the\x01",
            "technician to adjust our orbments.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#0203F#5PThere should be a customer service\x01",
            "counter over there.\x02\x03",
            "#0200FThey will be able to make various\x01",
            "adjustments if you ask them to.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#0000F#11PAll right. Let's check out the counter,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3570, 0, 2660, 89)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x4B, 2)
    EventEnd(0x5)
    Return()

    # Function_15_8492 end

    def Function_16_8845(): pass

    label("Function_16_8845")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        "#11PAh, Lloyd and the SSS. Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHey, Wendy. We're just stopping by to\x01",
            "handle a request.\x02\x03",
            "There should be someone here who wants\x01",
            "us to do a combat test for the Enigma, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh, that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYeah, I submitted that request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe foundation wanted us to test out something\x01",
            "on the Enigma, and who better to try it out\x01",
            "than the people who actually use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt'd be a huge weight off my shoulders\x01",
            "if you guys helped out with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FIf it's within our power, we'd be more\x01",
            "than happy to lend a hand.\x02\x03",
            "So, what exactly do these\x01",
            "Enigma tests entail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's not going to be too complicated,\x01",
            "so don't worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "First, I want to install a new benchmark\x01",
            "program onto your Enigma units!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#0005FUmm, you lost me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Epstein Foundation, the creators\x01",
            "of the Enigma orbments, are scouting\x01",
            "out ideas for the system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Enigma is still brand-spanking new\x01",
            "and isn't widespread yet, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe folks at the foundation are still fine-tuning\x01",
            "the specs, so they want reports on its efficiency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FTherefore, the foundation developed\x01",
            "this benchmark program...\x02\x03",
            "#0200FOn a basic level, the program collects data\x01",
            "on the orbment's durability and efficiency,\x01",
            "making troubleshooting issues easier.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#5P#0300FOh, that's right... Tio Tot, you're connected\x01",
            "to the foundation, right? Were ya not\x01",
            "aware of this kinda testing?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8ED6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8ED6)

    def lambda_8EE3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EE3)
    Sleep(100)
    TurnDirection(0x103, 0x104, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#12P#0200FRight. I was on the orbal staff development\x01",
            "team, not the Enigma's.\x02\x03",
            "I only had to conduct combat tests on my\x01",
            "staff on rare occasions.\x02",
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
        "#11P#0000FReally? That completely slipped my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSounds like the foundation is conducting\x01",
            "a lot of tests for their dev teams.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_906C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_906C)

    def lambda_9079():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9079)

    def lambda_9086():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9086)

    def lambda_9093():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9093)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#11PEither way, I've finished writing up most\x01",
            "of the evaluations, but I'm having some\x01",
            "issues with the combat benchmarks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, I could MAYBE try doing\x01",
            "them myself, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...for a proper evaluation, you'd\x01",
            "want to hear from actual Enigma\x01",
            "users, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FAh, and that's where your request comes in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FThat's Wendy for you...\x02\x03",
            "All right, we accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThanks, Lloyd! You're a lifesaver!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHaha, I don't know about that... It doesn't\x01",
            "sound like too terrible a request, after all.\x02\x03",
            "So, what exactly do you want us to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt should be a walk in the park.\x01",
            "I just want you to try casting the art\x01",
            "that conceals oneself from enemies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PApparently, it's an art that's only\x01",
            "possible to use with the Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000F'The art that conceals oneself from\x01",
            "enemies'? So all we have to do is\x01",
            "cast that correctly and that's that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FJudging by the effect, it must be\x01",
            "an exceptionally special art.\x02\x03",
            "We will have to take care to arrange\x01",
            "our quartz combination correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0309FRight, we'll leave all that\x01",
            "stuff to you, Tio Tot.\x02\x03",
            "#0300FSo once we get that squared away, we just\x01",
            "gotta test how the art works in combat, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FYes, that seems to be the case.\x02\x03",
            "While we're at it, this is a good opportunity\x01",
            "to start getting acquainted with our Enigmas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PGood luck, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POnce you've confirmed the art's effect,\x01",
            "come report all the details to me!\x01",
            "Thank ya!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Enigma Combat Test]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearScenarioFlags(0x5A, 7)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_8845 end

    def Function_17_96E5(): pass

    label("Function_17_96E5")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        "#11PHowdy, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo how'd your Enigma do\x01",
            "during those combat tests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWorked like a charm, Wendy. They're\x01",
            "definitely a huge asset in battles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FHollow Sphere, was it?\x02\x03",
            "#0200FOur opponents hardly seemed to notice\x01",
            "us under the aid of that art.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FI'm guessin' that art uses the\x01",
            "mirage element, eh?\x02\x03",
            "Given how much we rely on these Enigmas,\x01",
            "I bet increasin' our arsenal of arts like this\x01",
            "will pay off in the long run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FAgreed. On top of that, the Enigma's\x01",
            "communication function is quite handy.\x02\x03",
            "Not to mention synthesizing quartz and\x01",
            "unlocking slots is no different than past\x01",
            "orbment models, so that's convenient, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAh, okay, I see...\x01",
            "(*scribble*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYep, that should be enough\x01",
            "for my report.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x9,
        (
            "#11PLloyd and everyone, I really\x01",
            "appreciate all your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNow, what do I give to thank you?\x01",
            "Oh, this'll do. Please accept this.\x02",
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
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xAF, 1)

    ChrTalk(
        0x101,
        "#6P#0005FThis is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PApparently, this is an ancient quartz excavated\x01",
            "outta some giant ruins from the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI found this baby while fishing around\x01",
            "in the previous workshop's warehouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0305FExcavated quartz?\x01",
            "We can use stuff like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FTheoretically speaking, it would not be too\x01",
            "strange if they operate in the Enigmas.\x02\x03",
            "After all, orbments were originally created\x01",
            "through the analysis and modification of\x01",
            "ancient quartz.\x02\x03",
            "Some reports claim these quartz were being\x01",
            "used well before the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, none of that is confirmed...\x01",
            "but isn't it an awesome story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, its performance isn't totally guaranteed,\x01",
            "but there's still an orbal reaction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWith a little processing, I should be able\x01",
            "to get it compatible with your Enigmas!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHaha. This is basically treasure to you, isn't it?\x02\x03",
            "Thanks, Wendy. We'll use it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#0300FAppreciate it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FWendy, if you have any other requests,\x01",
            "don't hesitate to contact the SSS.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POf course! I'll be looking forward to it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Enigma Combat Test]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x1, 0x2)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_96E5 end

    SaveToFile()

Try(main)
