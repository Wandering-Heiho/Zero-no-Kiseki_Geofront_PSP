from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c014c.bin",                # FileName
        "c014c",                    # MapName
        "c014c",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c014c",                  # 0
        "Chaco",                  # 1
        "Wendy",                  # 2
        "Fernand",                # 3
        "Mizette",                # 4
        "Basilio",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24400.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(11119,   4000,    8699,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3309,   0,       790,     90,   261,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    3140,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_200",          # 00, 0
        "Function_1_2B8",          # 01, 1
        "Function_2_409",          # 02, 2
        "Function_3_4FB",          # 03, 3
        "Function_4_4FC",          # 04, 4
        "Function_5_6A8",          # 05, 5
        "Function_6_E83",          # 06, 6
        "Function_7_13B5",         # 07, 7
        "Function_8_13B9",         # 08, 8
        "Function_9_2695",         # 09, 9
        "Function_10_3020",        # 0A, 10
        "Function_11_34DD",        # 0B, 11
        "Function_12_39DB",        # 0C, 12
        "Function_13_3E96",        # 0D, 13
        "Function_14_3F69",        # 0E, 14
        "Function_15_4431",        # 0F, 15
    ))


    def Function_0_200(): pass

    label("Function_0_200")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_240"),
        (1, "loc_24C"),
        (2, "loc_258"),
        (3, "loc_264"),
        (4, "loc_270"),
        (5, "loc_27C"),
        (6, "loc_288"),
        (SWITCH_DEFAULT, "loc_294"),
    )


    label("loc_240")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_24C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_258")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_264")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_270")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_27C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_288")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_294")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2B7")

    Return()

    # Function_0_200 end

    def Function_1_2B8(): pass

    label("Function_1_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408")
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
    Jump("Function_1_2B8")

    label("loc_408")

    Return()

    # Function_1_2B8 end

    def Function_2_409(): pass

    label("Function_2_409")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_450")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    SetChrPos(0xD, 10670, 4000, 15920, 0)
    SetChrPos(0xE, 1050, 0, 3500, 90)
    Jump("loc_4FA")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_46F")
    SetChrPos(0xE, 1680, 0, 12640, 0)
    Jump("loc_4FA")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49F")
    SetChrPos(0xD, 11460, 4000, -1040, 90)
    SetChrPos(0xE, 40, 0, 4670, 315)
    Jump("loc_4FA")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrPos(0xD, 9090, 4000, 3890, 180)
    SetChrPos(0xE, 3670, 0, -2980, 0)
    Jump("loc_4FA")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4FA")
    SetChrPos(0xD, 11040, 4000, 7060, 225)
    SetChrPos(0xE, 310, 0, -2980, 0)

    label("loc_4FA")

    Return()

    # Function_2_409 end

    def Function_3_4FB(): pass

    label("Function_3_4FB")

    Return()

    # Function_3_4FB end

    def Function_4_4FC(): pass

    label("Function_4_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69E")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC")

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

    label("loc_5EC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_696")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_651")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_651")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_691")

    label("loc_672")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_691")

    Jump("loc_5F6")

    label("loc_696")

    TalkEnd(0x8)
    Jump("loc_6A7")

    label("loc_69E")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_6A7")

    Return()

    # Function_4_4FC end

    def Function_5_6A8(): pass

    label("Function_5_6A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E82")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6F2")
    MenuCmd(1, 0, "Blue Sheriff (Purchased)")
    MenuCmd(3, 0, 0x0)
    Jump("loc_70E")

    label("loc_6F2")

    MenuCmd(1, 0, "Blue Sheriff (1000 mira)")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_73B")
    MenuCmd(1, 0, "Peace Green (Purchased)")
    MenuCmd(3, 0, 0x1)
    Jump("loc_756")

    label("loc_73B")

    MenuCmd(1, 0, "Peace Green (1000 mira)")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_781")
    MenuCmd(1, 0, "Black Cat (Purchased)")
    MenuCmd(3, 0, 0x2)
    Jump("loc_79A")

    label("loc_781")

    MenuCmd(1, 0, "Black Cat (1000 mira)")

    label("loc_79A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_7C9")
    MenuCmd(1, 0, "Danger Orange (Purchased)")
    MenuCmd(3, 0, 0x3)
    Jump("loc_7E6")

    label("loc_7C9")

    MenuCmd(1, 0, "Danger Orange (1000 mira)")

    label("loc_7E6")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_841")
    Sleep(1)
    Return()

    label("loc_841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_881")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_93C")

    label("loc_881")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C1")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_93C")

    label("loc_8C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_901")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_93C")

    label("loc_901")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93C")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_93C")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EE")

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
    Jump("loc_B8A")

    label("loc_9EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A79")

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
    Jump("loc_B8A")

    label("loc_A79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B03")

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
    Jump("loc_B8A")

    label("loc_B03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A")

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

    label("loc_B8A")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E65")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C85")

    ChrTalk(
        0x8,
        (
            "Oh, no, you seem to be short on mira.\x01",
            "Come back when you've got a bit more on hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E56")

    label("loc_C85")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D31")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Lloyd's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_DE9")

    label("loc_D31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D70")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Elie's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_DE9")

    label("loc_D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAE")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Tio's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_DE9")

    label("loc_DAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE9")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Replaced Randy's orbment cover.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_DE9")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E24")
    OP_DE(0x16, 0x0)

    label("loc_E24")


    ChrTalk(
        0x8,
        "I look forward to your next visit!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_E56")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E6F")

    label("loc_E65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E6F")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_6B2")

    label("loc_E82")

    Return()

    # Function_5_6A8 end

    def Function_6_E83(): pass

    label("Function_6_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA7")

    ChrTalk(
        0x8,
        (
            "I'm glad the festival could end\x01",
            "this year without anything\x01",
            "major happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Tranquility is always best!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Hmm, quite a few incidents\x01",
            "did pop up, though...)\x02\x03",
            "#0000F(Well, I guess that's the difference\x01",
            "between the police and the average citizen.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1002")

    label("loc_FA7")


    ChrTalk(
        0x8,
        (
            "I'm relieved that the Anniversary Festival\x01",
            "is going to be able to end on a high note.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1002")

    Jump("loc_13B4")

    label("loc_1007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10BE")

    ChrTalk(
        0x8,
        (
            "The parade was phenomenal!\x01",
            "I took so many photos of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Using one of the display cameras...\x01",
            "I'll have to go stealthily develop the film later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113D")

    label("loc_10BE")


    ChrTalk(
        0x8,
        (
            "I took some photos of the parade!\x01",
            "...With that camera on display over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Keep it a secret from my manager, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_113D")

    Jump("loc_13B4")

    label("loc_1142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11E2")

    ChrTalk(
        0x8,
        (
            "There are demo products inside the\x01",
            "store for performance comparisons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That way, you can buy products\x01",
            "after you've tested them yourself!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_12A1")

    ChrTalk(
        0x8,
        "Tomorrow's the highly anticipated parade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why not get an orbal camera and\x01",
            "take some souvenir photos?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to earlier years,\x01",
            "their prices have really dropped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1336")

    ChrTalk(
        0x8,
        (
            "All my friends decided to get together\x01",
            "and go to Mishelam today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* If I didn't have work,\x01",
            "I would've been able to go...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B4")

    label("loc_1336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(
        0x8,
        "Wow, there are so many people outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The festival is so lively, but it's\x01",
            "about the same as ever in here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B4")

    Return()

    # Function_6_E83 end

    def Function_7_13B5(): pass

    label("Function_7_13B5")

    Call(0, 8)
    Return()

    # Function_7_13B5 end

    def Function_8_13B9(): pass

    label("Function_8_13B9")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2691")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Upgrade/Synthesis\x01",      # 1
            "Ask Questions\x01",          # 2
            "Leave\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1432")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_176F")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EC")

    ChrTalk(
        0x9,
        (
            "I haven't actually handled\x01",
            "high-level quartz before, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll take care of the slot strengthening,\x01",
            "so if you need help, give me a shout.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_15EC")


    ChrTalk(
        0x9,
        (
            "I've actually just started to handle\x01",
            "slot strengthening and high-level quartz,\x01",
            "so if you need help, gimme a shout.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1664")

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

    label("loc_176F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_177F")
    OP_AF(0xF)
    Jump("loc_17C1")

    label("loc_177F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_178F")
    OP_AF(0xE)
    Jump("loc_17C1")

    label("loc_178F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_179F")
    OP_AF(0xD)
    Jump("loc_17C1")

    label("loc_179F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17AF")
    OP_AF(0xC)
    Jump("loc_17C1")

    label("loc_17AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_17BF")
    OP_AF(0xB)
    Jump("loc_17C1")

    label("loc_17BF")

    OP_AF(0xA)

    label("loc_17C1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_268C")

    label("loc_17D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Jump("loc_268C")

    label("loc_17F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1805")
    Jump("loc_268C")

    label("loc_1805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_19B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(
        0x9,
        (
            "Hey, Lloyd! Out investigating again?\x01",
            "Being detectives sounds like tough work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey, since you're finally back home,\x01",
            "let's go hang out with Oscar sometime!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, that'd be nice.\x01",
            "If I can find the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I should be\x01",
            "the one saying that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19B3")

    label("loc_1944")


    ChrTalk(
        0x9,
        (
            "Everyone is so busy now...\x01",
            "Well, if we can free up our schedules,\x01",
            "let's go somewhere with Oscar sometime!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B3")

    Jump("loc_268C")

    label("loc_19B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_1B10")

    ChrTalk(
        0x9,
        "Are you all still looking for that lost kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just let me know if I can do anything.\x01",
            "If you need an orbal vehicle,\x01",
            "I'll come flying out of the store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FHaha, knowing you, Wendy,\x01",
            "you'd actually do it!\x02\x03",
            "#0000FThe investigation is still underway.\x01",
            "I'm just searching for leads now.\x01",
            "I appreciate the thought, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268C")

    label("loc_1B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DED")

    ChrTalk(
        0x101,
        (
            "#0001FWendy, do you have a minute?\x02\x03",
            "Could you tell me if you've\x01",
            "seen this kid before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Eh? What now?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if\x01",
            "she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "Ummmm, he's around five years old, you say?\x01",
            "He's a bit younger than Pansy, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry, Lloyd. I wasn't able to catch\x01",
            "the parade, so I haven't seen this kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSo, you don't think he entered Genten at any point?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, I can say with full confidence\x01",
            "that he hasn't entered the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I like to keep track of how many times\x01",
            "the orbal door over there opens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI-I see...\x01",
            "(Why doesn't that surprise me at all?)\x02\x03",
            "#0000FThanks for the help, Wendy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    Jump("loc_2011")

    label("loc_1DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAF")

    ChrTalk(
        0x9,
        (
            "Apparently, it was crazy outside,\x01",
            "so I'm worried about that kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey, why don't you use that dog of yours to\x01",
            "help search? His name was Zeit, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha, one step ahead of you.\x01",
            "Zeit is working with Tio currently.\x02\x03",
            "#0008FThe massive crowd of people here for the\x01",
            "festival definitely isn't saving us time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It sounds like the only course of action\x01",
            "is to gather even more info!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Keep working hard, Lloyd!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2011")

    label("loc_1FAF")


    ChrTalk(
        0x9,
        (
            "In the end, it really just hinges\x01",
            "on you finding a good lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Keep working hard, Lloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_2011")

    Jump("loc_268C")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_210B")

    ChrTalk(
        0x9,
        (
            "I wonder what kind of specs the\x01",
            "orbal vehicles in the parade had...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whenever I start to daydream about stuff,\x01",
            "suddenly it's time for me to close up shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hahaha, maybe it's that 'occupational disease'\x01",
            "I've heard of!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268C")

    label("loc_210B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(
        0x9,
        (
            "With the rise of new orbment models,\x01",
            "older types of quartz have become\x01",
            "cheap enough to outsell newer types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It takes a while for the new models to be as widespread,\x01",
            "and the old quartz are simpler to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, once we do start making the transition to\x01",
            "newer quartz, at least we can break down the\x01",
            "old ones into sepith and recycle them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268C")

    label("loc_2279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_23B2")

    ChrTalk(
        0x9,
        (
            "I had planned to go to an Arc en Ciel\x01",
            "performance if I had the chance, but\x01",
            "this year is really keeping me busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Business boomed pretty quickly after\x01",
            "we turned into an orbal store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm definitely glad it happened,\x01",
            "but sometimes I miss being able to\x01",
            "kick back and tinker with orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268C")

    label("loc_23B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E2")

    ChrTalk(
        0x9,
        "A customer tried hitting on me earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This guy was just completely oblivious to all the\x01",
            "other customers around and the fact that I'm on\x01",
            "the job. I almost socked him in the face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FWe're adults now. You can't just go\x01",
            "hitting customers in the face, Wendy...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25AF")

    label("loc_24E2")


    ChrTalk(
        0x9,
        (
            "Wow. I didn't actually hit him, Lloyd!\x01",
            "Since the store was packed with people,\x01",
            "I threw him out as quick as I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Geez, I just want people to realize\x01",
            "when I'm busy and stop chitter-chattering.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AF")

    Jump("loc_268C")

    label("loc_25B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_268C")

    ChrTalk(
        0x9,
        (
            "Wow, what a massive crowd. I've been seeing\x01",
            "more people visiting the store without actually\x01",
            "buying anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It kind of makes me want to go and check out\x01",
            "the festival for myself when the sun sets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268C")

    Jump("loc_13C6")

    label("loc_2691")

    TalkEnd(0x9)
    Return()

    # Function_8_13B9 end

    def Function_9_2695(): pass

    label("Function_9_2695")


    ChrTalk(
        0x9,
        (
            "Okay, then, what did you\x01",
            "want to ask me about?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3015")
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
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2770"),
        (1, "loc_29DB"),
        (2, "loc_2B4F"),
        (3, "loc_2CAE"),
        (SWITCH_DEFAULT, "loc_3001"),
    )


    label("loc_2770")


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
    Jump("loc_3010")

    label("loc_29DB")


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
    Jump("loc_3010")

    label("loc_2B4F")


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
    Jump("loc_3010")

    label("loc_2CAE")


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
    Jump("loc_3010")

    label("loc_3001")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3010")

    label("loc_3010")

    Jump("loc_26D3")

    label("loc_3015")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_2695 end

    def Function_10_3020(): pass

    label("Function_10_3020")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(
        0xFE,
        (
            "A tourist from Erebonia purchased\x01",
            "one of our orbal vehicles earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like I can thank the parade\x01",
            "for that sale, since he was talking\x01",
            "about how he wanted to follow it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_30E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31B5")

    ChrTalk(
        0xFE,
        (
            "When I think about it,\x01",
            "I have the feeling I'm relying too much\x01",
            "on Wendy's knowledge of orbal tech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should consider\x01",
            "starting to seriously study\x01",
            "orbal technology, like her...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_31B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_328C")

    ChrTalk(
        0xFE,
        (
            "Tourists have been coming to Wendy\x01",
            "lately to have their broken photo-quartz\x01",
            "repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought about advising them to just\x01",
            "buy replacements, but this way, we\x01",
            "get a lot more repeat business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_328C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_32EA")

    ChrTalk(
        0xFE,
        (
            "Dang it, if only I could figure out\x01",
            "how to pull in more of the tourists...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_32EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33DE")

    ChrTalk(
        0xFE,
        (
            "Damn, Wendy... I didn't think she'd\x01",
            "try to assault a customer, of all things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rumors say that at her\x01",
            "previous workshop, she was\x01",
            "even more wild than she is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, what kind of education\x01",
            "did her teacher give her?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D9")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_34D9")

    ChrTalk(
        0xFE,
        (
            "It seems like the orbal camera's popularity\x01",
            "is beginning to rise little by little, but\x01",
            "international sales still have a ways to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could the food stalls outside be stealing\x01",
            "customers from us? I need to try and\x01",
            "attract more people!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D9")

    TalkEnd(0xFE)
    Return()

    # Function_10_3020 end

    def Function_11_34DD(): pass

    label("Function_11_34DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35EA")

    ChrTalk(
        0xFE,
        "We've finally reached the end of the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For some reason, I didn't do much sightseeing\x01",
            "this year. I've been too caught up looking in here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, maybe gazing at all these\x01",
            "new orbal gadgets is enjoyable\x01",
            "for an old lady like myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D7")

    label("loc_35EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3674")

    ChrTalk(
        0xFE,
        (
            "My photos of today's parade\x01",
            "are to die for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the new camera model for\x01",
            "you; being simple to use is the best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D7")

    label("loc_3674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3723")

    ChrTalk(
        0xFE,
        (
            "I need to remember to take a look at\x01",
            "the second floor displays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard brand new, ostentatious goods are\x01",
            "on display... Maybe I should take a look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D7")

    label("loc_3723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_37F7")

    ChrTalk(
        0xFE,
        "*click* *click*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm already here, I bet photos\x01",
            "of the busy store would be spectacular!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll photograph the fancy new products, too,\x01",
            "so I'll be killing two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D7")

    label("loc_37F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_38DD")

    ChrTalk(
        0xFE,
        (
            "You see, I don't particularly care\x01",
            "for large crowds of people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In that regard, this store is quite comfortable\x01",
            "to me, not to mention the air conditioning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I find myself losing track of time in here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39D7")

    label("loc_38DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_39D7")

    ChrTalk(
        0xFE,
        (
            "Since orbal cameras have gotten so cheap,\x01",
            "I spoiled myself and purchased one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Taking all the photos I want has always\x01",
            "been a dream of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this in hand, I'll document all the great\x01",
            "memories of this Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D7")

    TalkEnd(0xFE)
    Return()

    # Function_11_34DD end

    def Function_12_39DB(): pass

    label("Function_12_39DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A88")

    ChrTalk(
        0xFE,
        (
            "Chaco...\x01",
            "She's really been going at it non-stop\x01",
            "during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's decided! Next year, I'll take\x01",
            "her to Mishelam or something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3B3D")

    ChrTalk(
        0xFE,
        (
            "When the parade came close to the store,\x01",
            "Chaco dropped everything and rushed outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had thought we made eye contact,\x01",
            "but I guess she didn't notice me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C25")

    ChrTalk(
        0xFE,
        (
            "Looks like the time for the parade's gotten\x01",
            "pretty close while I was daydreaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard it's extremely difficult to take\x01",
            "nice photos without practice beforehand...\x01",
            "Maybe I should wait to buy a camera...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3CFA")

    ChrTalk(
        0xFE,
        (
            "Hmm, I've been observing for a while now,\x01",
            "but doesn't Chaco's superior look like\x01",
            "quite the dependable girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that's the case, I should be able to\x01",
            "leave Chaco in her care with no worries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD6")

    ChrTalk(
        0xFE,
        "Th-That shocked me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Th-The girl at the counter next to\x01",
            "Chaco tried to hit an unyielding\x01",
            "customer with a spanner!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-Is Chaco going to be all right under\x01",
            "such a brutal superior?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E18")

    label("loc_3DD6")


    ChrTalk(
        0xFE,
        (
            "Is Chaco going to be all right under\x01",
            "such a brutal superior?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E18")

    Jump("loc_3E92")

    label("loc_3E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E92")

    ChrTalk(
        0xFE,
        (
            "Hmm... I wonder which\x01",
            "camera I should go with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be ideal if it could last\x01",
            "me for a long time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E92")

    TalkEnd(0xFE)
    Return()

    # Function_12_39DB end

    def Function_13_3E96(): pass

    label("Function_13_3E96")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F68")

    ChrTalk(
        0x160,
        (
            "#3300F(Should we conclude our investigation\x01",
            "of Central Square here?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Yes, I think we've covered enough ground.)\x02\x03",
            "(Next, let's try investigating\x01",
            "Station Street.)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_3F68")

    Return()

    # Function_13_3E96 end

    def Function_14_3F69(): pass

    label("Function_14_3F69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3FCF")

    ChrTalk(
        0xFE,
        (
            "Ever since I can remember, orbal devices\x01",
            "and I are like cats and dogs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_408F")

    label("loc_3FCF")


    ChrTalk(
        0xFE,
        (
            "I managed to break the orbal wristwatch\x01",
            "I bought today as soon as I put it on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm currently having it fixed\x01",
            "at the repair counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha, maybe I really\x01",
            "am orbal-impaired.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_408F")

    Jump("loc_442D")

    label("loc_4094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4170")

    ChrTalk(
        0xFE,
        (
            "The clerk girl was telling me, 'I hope\x01",
            "you'll love it,' along with a bunch\x01",
            "of other stuff I didn't understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's so bright and really fits my type,\x01",
            "but maybe it wasn't meant to be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4242")

    label("loc_4170")


    ChrTalk(
        0xFE,
        (
            "Earlier, that clerk girl gave me a whole\x01",
            "explanation about orbal goods...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While I didn't understand much of\x01",
            "what she said, she told me, 'I hope\x01",
            "you'll love it.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She really is cute, isn't she?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4242")

    Jump("loc_442D")

    label("loc_4247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_42ED")

    ChrTalk(
        0xFE,
        (
            "Um, let's see here...\x01",
            "It says 'bright orbal light.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, wow! There's different colors, too?!\x01",
            "I should get one as a souvenir before I go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442D")

    label("loc_42ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_435E")

    ChrTalk(
        0xFE,
        (
            "Th-This seems like the latest\x01",
            "model of tactical orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "W-Will it break if I touch it?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_442D")

    label("loc_435E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43B7")

    ChrTalk(
        0xFE,
        "Hmm? What's with all the noise downstairs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_442D")

    label("loc_43B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_442D")

    ChrTalk(
        0xFE,
        (
            "I-Incredible!\x01",
            "I-Is this real?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To an orbal-illiterate like myself,\x01",
            "this stuff is all gobbledygook!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442D")

    TalkEnd(0xFE)
    Return()

    # Function_14_3F69 end

    def Function_15_4431(): pass

    label("Function_15_4431")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_451A")

    ChrTalk(
        0xFE,
        (
            "I wanted a memento of my trip to Crossbell,\x01",
            "so I bought this gorgeous pendant with a\x01",
            "little orbal light attached!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a lot of really unique trinkets here,\x01",
            "but they're all a bit too extravagant for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_451A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_45DB")

    ChrTalk(
        0xFE,
        (
            "While absorbed with checking out all of the\x01",
            "neat luxuries here, I missed the parade!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should've paid more attention...\x01",
            "I'll just go look at the orbal vehicles instead!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_45DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46AC")

    ChrTalk(
        0xFE,
        (
            "'Exceptional Thermal Insulation!\x01",
            "Latest High-Output Quartz Built In!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is this one the best?\x01",
            "The specification documents are too convoluted.\x01",
            "I'm having trouble understanding anything...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_46AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_471D")

    ChrTalk(
        0xFE,
        "An orbal refrigerator...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm...I really want to buy this,\x01",
            "but how would I carry it home?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_471D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4796")

    ChrTalk(
        0xFE,
        "Self-oscillating function?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's Crossbell for you.\x01",
            "Nothing but the latest model for all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481D")

    label("loc_4796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_481D")

    ChrTalk(
        0xFE,
        "Oh, this is that store I heard about!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, since everyone's busy with the\x01",
            "festival, I'll take a quick glance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481D")

    TalkEnd(0xFE)
    Return()

    # Function_15_4431 end

    SaveToFile()

Try(main)
