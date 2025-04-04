from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0580",                  # 0
        "Imelda",                 # 1
        "Renne",                  # 2
        "Tourist",                # 3
        "Dolls",                  # 4
    ))

    AddCharChip((
        "chr/ch24400.itc",                   # 00
        "chr/ch09002.itc",                   # 01
        "chr/ch09500.itc",                   # 02
        "apl/ch50093.itc",                   # 03
    ))

    DeclNpc(-750,    100,     4800,    180,  261,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-4170,   0,       239,     270,  405,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(560,     0,       -1159,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-600,    850,     3500,    0,    502,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-750,    0,       3500,    1500,    -750,    1500,    4800,    0x007E, 0,  3,  0x0000)
    DeclActor(-5470,   0,       120,     1200,    -5470,   2000,    120,     0x007C, 0,  24, 0x0000)

    ScpFunction((
        "Function_0_1C0",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_48C",          # 03, 3
        "Function_4_490",          # 04, 4
        "Function_5_5258",         # 05, 5
        "Function_6_556D",         # 06, 6
        "Function_7_5851",         # 07, 7
        "Function_8_5A87",         # 08, 8
        "Function_9_5D8A",         # 09, 9
        "Function_10_62CB",        # 0A, 10
        "Function_11_6805",        # 0B, 11
        "Function_12_69B1",        # 0C, 12
        "Function_13_6A4C",        # 0D, 13
        "Function_14_739E",        # 0E, 14
        "Function_15_743C",        # 0F, 15
        "Function_16_7965",        # 10, 16
        "Function_17_7AAD",        # 11, 17
        "Function_18_7C63",        # 12, 18
        "Function_19_81AB",        # 13, 19
        "Function_20_8BA9",        # 14, 20
        "Function_21_9388",        # 15, 21
        "Function_22_9899",        # 16, 22
        "Function_23_A3F9",        # 17, 23
        "Function_24_B1B9",        # 18, 24
    ))


    def Function_0_1C0(): pass

    label("Function_0_1C0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C0 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_287")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_295")
    Jump("loc_2E0")

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B6")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B1")
    SetChrFlags(0xA, 0x10)

    label("loc_2B1")

    Jump("loc_2E0")

    label("loc_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C4")
    Jump("loc_2E0")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E0")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_2E0")
    ClearChrFlags(0x9, 0x10)

    label("loc_2E0")

    Return()

    # Function_1_278 end

    def Function_2_2E1(): pass

    label("Function_2_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_37F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_3C0")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_3C0")

    label("loc_3B7")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_3C0")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EF")
    Jump("loc_48B")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 5)), scpexpr(EXPR_END)), "loc_406")
    Jump("loc_431")

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_417")
    Jump("loc_431")

    label("loc_417")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x14), scpexpr(EXPR_PUSH_LONG, 0x120), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    Event(0, 21)

    label("loc_431")

    Jump("loc_48B")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_444")
    Jump("loc_48B")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_48B")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_46D")
    Jump("loc_48B")

    label("loc_46D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_48B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    Event(0, 20)

    label("loc_48B")

    Return()

    # Function_2_2E1 end

    def Function_3_48C(): pass

    label("Function_3_48C")

    Call(0, 4)
    Return()

    # Function_3_48C end

    def Function_4_490(): pass

    label("Function_4_490")

    SetScenarioFlags(0x53, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    Call(0, 5)
    Return()

    label("loc_4B8")

    Jump("loc_548")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_4E8")

    label("loc_4D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4E8")
    Call(0, 23)
    Return()

    label("loc_4E8")

    Jump("loc_548")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FB")
    Jump("loc_548")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_526")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_521")
    Call(0, 6)
    Return()

    label("loc_521")

    Jump("loc_548")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_548")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_548")
    Call(0, 15)
    Return()

    label("loc_548")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DC")
    Jump("loc_626")

    label("loc_5DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5FC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_626")

    label("loc_5FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_626")

    label("loc_61C")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_626")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6C2")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C6, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CC, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CD, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CE, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    Call(0, 10)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    label("loc_6C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5250")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_71D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_73C")
    OP_AF(0x44)
    Jump("loc_73E")

    label("loc_73C")

    OP_AF(0x43)

    label("loc_73E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_524B")

    label("loc_74D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_761")
    Jump("loc_524B")

    label("loc_761")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B8E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C6, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CC, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CD, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CE, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E9")
    Call(0, 10)
    Jump("loc_B89")

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 7)), scpexpr(EXPR_END)), "loc_88D")

    ChrTalk(
        0x8,
        "I'll have you kids work your fannies off for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Trust me, you'll have to if you want to get this\x01",
            "incomprehensible situation under control.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B89")

    label("loc_88D")


    ChrTalk(
        0x8,
        (
            "Rumor has it that Marconi and his men\x01",
            "up and vanished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What in the world could have happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FSo you know about it, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWell, when you're this close to their base,\x01",
            "you're bound to hear what's what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Naturally. Then again, too many aspects\x01",
            "of the disappearance are still foggy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even my sources in the diet and CPD\x01",
            "leadership didn't provide me with any\x01",
            "straight answers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108FThat doesn't bode well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FThere is confusion on all fronts, it seems.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, well. I'll have you kids work your fannies\x01",
            "off for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Trust me, you'll have to if you want to get this\x01",
            "incomprehensible situation under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYes, ma'am. You can count on us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe'll get to the bottom of what's happening.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 7)

    label("loc_B89")

    Jump("loc_524B")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CCD")

    ChrTalk(
        0x8,
        "Looks like things have finally gone topsy-turvy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See, I'm constantly paying taxes to our lovely\x01",
            "government. So, listen and listen well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You best come up with a solution to this mess\x01",
            "soon, or we're going to have a big problem on\x01",
            "our hands. Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0603FQuite.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA9")

    label("loc_CCD")


    ChrTalk(
        0x8,
        (
            "My, if it isn't the SSS. I see you\x01",
            "have an interesting face with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FImelda, the Special Support Section is\x01",
            "under my command for the time being.\x02\x03",
            "#0600FI would appreciate it if you didn't go\x01",
            "saying things you're in no place to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! You say that, but you're\x01",
            "just as whipped as the rest of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Don't go acting so full of yourself, boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0601FExcuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(As blunt as always.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(How embarrassing for him.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EA9")

    Jump("loc_524B")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1053")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F46")

    ChrTalk(
        0x8,
        (
            "By the way, I heard that Revache's cars\x01",
            "raced out of the Back Alley around dawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, they must be up to some mischief.\x02",
    )

    CloseMessageWindow()
    Jump("loc_104E")

    label("loc_F46")


    ChrTalk(
        0x8,
        "It's quiet today. Too quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And to top it off, Heiyue hasn't tried\x01",
            "to even the score yet. What in Aidios'\x01",
            "name is going on in this city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F(That's what we're going to figure out.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Man, I hope things don't go straight\x01",
            "to hell...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_104E")

    Jump("loc_524B")

    label("loc_1053")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1921")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x14), scpexpr(EXPR_PUSH_LONG, 0x120), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_118A")

    ChrTalk(
        0x8,
        (
            "Well, that little mystery can wait. I have\x01",
            "business to deal with today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That old man should be calling me any\x01",
            "minute now about that lovely piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh. I'll have to prepare quite the\x01",
            "arrangement to sway him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1185")

    ChrTalk(
        0x101,
        "#0003F(Wh-What is she talking about?)\x02",
    )

    CloseMessageWindow()

    label("loc_1185")

    Jump("loc_191C")

    label("loc_118A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1418")

    ChrTalk(
        0x8,
        (
            "#2PSpeaking of dolls, that reminds me of another\x01",
            "curious rumor I heard some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PIt spoke of these peculiar, mechanical dolls\x01",
            "that could move of their own accord and even\x01",
            "went on rampages during the Liberl incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PHyeh hyeh hyeh. Perhaps Joerg played some\x01",
            "role in those proceedings after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1413")
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
        0x103,
        (
            "#0211F(Is the shutdown of orbal technology throughout an\x01",
            "entire country really something to make light of?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(No, it's not--especially given what we\x01",
            "know about the society's role in it.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1413")

    Jump("loc_191C")

    label("loc_1418")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_158E")

    ChrTalk(
        0x8,
        (
            "Oh, right. I have news about your deadline.\x01",
            "Due to my buyer's special circumstances, it\x01",
            "was bumped up to today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "So, try to make it snappy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Do it for dear old Imelda!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1589")

    ChrTalk(
        0x101,
        "#0006F(Up go the expectations yet again...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Indeed. But since we have previous\x01",
            "obligations, there's no harm in giving\x01",
            "up if it seems impossible.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1589")

    Jump("loc_191C")

    label("loc_158E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1450, 2860, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "If only he would shut his mouth and stop\x01",
            "complaining. Honestly, the gall of that man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though, I suppose the bracers wouldn't have\x01",
            "made it on time, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, no matter. There's always clients out\x01",
            "there waiting for a juicy piece of bait.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FGood morning, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FDid you need us to help with anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, actually. You see, I think a rather eccentric\x01",
            "acquaintance of mine has finally gone senile...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! Oh, I understand! Aidios must\x01",
            "have sent me you four to assist me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, oh, yes! You will work wonderfully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FAre...you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FI've got a bad feeling about this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FA feeling...? No, it is a certainty.\x02",
    )

    CloseMessageWindow()
    Call(0, 22)
    ClearScenarioFlags(0xF1, 5)
    EventEnd(0x5)

    label("loc_191C")

    Jump("loc_524B")

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E6C")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A60")

    ChrTalk(
        0x8,
        (
            "*click* *clack* Why haven't the police\x01",
            "updated anything in the database yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Are they dilly-dallying, or are they truly\x01",
            "that incompetent? For crying out loud,\x01",
            "won't you start investigating already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(She's running her mouth off like we aren't\x01",
            "standing in front of her...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1A60")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Imelda is operating some sort of terminal\x01",
            "under the counter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "*click* *clack*...*click* *click* *clack*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, goodness! Heiyue's office? Raided?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. This is quite the serious offense.\x01",
            "I haven't been this excited in a good long while.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_1BAE")

    ChrTalk(
        0x103,
        "#0200FThat was information from Jona, I presume?\x02",
    )

    CloseMessageWindow()

    label("loc_1BAE")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh, who can say? After living in Crossbell for\x01",
            "as long as I have, you start to notice incidents\x01",
            "like this happen from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, how thrilling. Now, how exactly will Cao\x01",
            "respond to such an embarrassing slight...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FIsn't that a tad bit reckless to say, ma'am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FYeah, Revache & Co. is right down the\x01",
            "street. Aren't you at least a little worried?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hmm, I suppose so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I AM worried about real estate prices\x01",
            "dropping because of this commotion.\x02",
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
            "#0006F(Oh, right. I forgot about how crazy she\x01",
            "is about the real estate industry...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E67")

    Jump("loc_524B")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_20AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F12")

    ChrTalk(
        0x8,
        "We're open until quite late today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're looking for something in particular,\x01",
            "I'm sure I could nudge you in the right direction.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A6")

    label("loc_1F12")


    ChrTalk(
        0x8,
        "My, oh, my. Someone's tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh. In the spending mood, dears?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Look here. Hold this urn for a short while,\x01",
            "and you'll experience happiness, energy,\x01",
            "and the most wonderful of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNo thanks, ma'am. Also, I'd appreciate it\x01",
            "if you wouldn't try to sell us sketchy stuff\x01",
            "like your, uh, magic urn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYou really are a pro at takin' advantage\x01",
            "of people, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20A6")

    Jump("loc_524B")

    label("loc_20AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_23AA")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2174")

    ChrTalk(
        0x8,
        (
            "The specifications of the latest model airships\x01",
            "and CGF armored cars...? How lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bless my dear informant. He procures me\x01",
            "quite the curious bits of information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A5")

    label("loc_2174")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Imelda is operating some sort of terminal\x01",
            "under the counter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "*click* *clack*...*click* *click* *clack*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh? The specifications of the latest model\x01",
            "airships and CGF armored cars...? Lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Bless my dear informant. He procures me\x01",
            "quite the curious bits of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0505F(Just who is this lady? Those details are\x01",
            "supposed to be confidential, as of now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(She's one of our more...well-informed\x01",
            "acquaintances, you could say.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Jona certainly has no restraint when\x01",
            "it comes to pawning off information...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_23A5")

    Jump("loc_524B")

    label("loc_23AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_24FC")

    ChrTalk(
        0x8,
        (
            "How intriguing. Many rumors are flying\x01",
            "around about the girl, but she's quite\x01",
            "the funny one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Make sure to stop by and\x01",
            "see me again. I can keep you company and\x01",
            "show you all sorts of doodads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FThat'd be awesome! See ya, Granny!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Wow, KeA even managed to tame Imelda.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A64")

    label("loc_24FC")


    ChrTalk(
        0x8,
        "Well, well, well! Look who it is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! So you survived the auction,\x01",
            "I see! You're tenacious, I'll give you that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FThanks. It definitely wasn't easy.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_260E")

    ChrTalk(
        0x102,
        (
            "#0100FYou were at the auction, too, right?\x01",
            "How did it end up going?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_260E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2662")

    ChrTalk(
        0x103,
        (
            "#0200FYou attended the auction, too, correct?\x01",
            "How was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26AE")

    label("loc_2662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26AE")

    ChrTalk(
        0x104,
        (
            "#0300FYou scoped out the auction, yeah?\x01",
            "How'd that go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AE")


    ChrTalk(
        0x8,
        (
            "Oh, the auction ended in an uproar, thanks\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "So? Is that lovely little girl there the one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Now, let's see... Hmm, hmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111FHmmm?\x02\x03",
            "#1110FGranny, your glasses make you look\x01",
            "like a witch. Your face, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0011FI'm SO sorry about her. I swear she\x01",
            "didn't mean anything by that.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0)
    OP_64(0x1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x8,
        "#4SHyeh hyeh hyeh hyeh hyeh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know, she has a point! What a\x01",
            "delightfully amusing girl!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I like you, little one. Come and visit\x01",
            "me sometime, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I can show you around the shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FSure thing! I definitely will!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29A5")

    ChrTalk(
        0x102,
        "#0106F(She's fearless, isn't she?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_29A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A08")

    ChrTalk(
        0x103,
        (
            "#0200F(My preliminary findings show that\x01",
            "KeA is not afraid of anything.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_2A08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A61")

    ChrTalk(
        0x104,
        (
            "#0300F(Haha, amazing. Doesn't seem like\x01",
            "KeDo's afraid of anything.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    SetScenarioFlags(0xB1, 5)

    label("loc_2A64")

    Jump("loc_524B")

    label("loc_2A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B18")

    ChrTalk(
        0x8,
        "Afternoon, dearies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... If you're looking to\x01",
            "buy, I recommend you do it quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You see, I plan to close up shop by\x01",
            "evening today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_524B")

    label("loc_2B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2D74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BF5")

    ChrTalk(
        0x8,
        (
            "That reminds me. That stuffed animal\x01",
            "you were asking for finally arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll wrap it up in something nice, so\x01",
            "stop by on your way home later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3300FTeehee. I'll make sure to do so.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D6F")

    label("loc_2BF5")


    ChrTalk(
        0x8,
        "Hello there, Renne. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh? Accompanying this boy, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3304FYes. I saw he was having issues, so I\x01",
            "decided it would be amusing to assist.\x02\x03",
            "#3300FBesides, supporting incompetent men\x01",
            "is the duty of any respectable lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh! True, how very true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't go causing her too much trouble\x01",
            "now, boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FI don't plan to.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2D6F")

    Jump("loc_524B")

    label("loc_2D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_END)), "loc_2E45")

    ChrTalk(
        0x8,
        (
            "Now, I can't tell you about the Back Alley\x01",
            "itself, but I can assure you that no boy\x01",
            "wandered in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, does this look like a store a\x01",
            "child would willingly step into?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE3")

    label("loc_2E45")


    ChrTalk(
        0x101,
        (
            "#0001F(It's possible that Imelda might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed her Colin's picture and asked if she\x01",
            "knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "This boy? I'm afraid I've never seen him before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Also, does this look\x01",
            "like a store a child would willingly\x01",
            "step into?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI guess you have a point there. Still,\x01",
            "thanks for your help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_2FE3")

    Jump("loc_524B")

    label("loc_2FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_310C")

    ChrTalk(
        0x8,
        (
            "Oh, dear. And here I thought the\x01",
            "store wasn't going to have much\x01",
            "traffic today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I have business to attend to\x01",
            "throughout the city. Believe me, it\x01",
            "is quite the inconvenience.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3107")

    ChrTalk(
        0x102,
        (
            "#0100FSomething tells me that Imelda isn't in\x01",
            "the working mood today...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3107")

    Jump("loc_524B")

    label("loc_310C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_343D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3187")

    ChrTalk(
        0x8,
        (
            "I have meetings upon meetings to attend to.\x01",
            "So, if you want to make a purchase, do it quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3438")

    label("loc_3187")


    ChrTalk(
        0x8,
        (
            "I was summoned by the Business Owners' Association\x01",
            "earlier today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I could hardly refuse, considering I've done\x01",
            "business with them for years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. I plan on seeing the last Arc\x01",
            "en Ciel performance tonight. I hope it will be\x01",
            "as marvelous as people say it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHow'd you manage to get the tickets?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh! Why so surprised, boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why, isn't it obvious? I'm one of Arc en Ciel's\x01",
            "top investors. Tickets mean nothing to me.\x02",
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
        0x102,
        "#0105FAre you really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3435")

    ChrTalk(
        0x104,
        (
            "#0306FI mean, this IS Imelda we're talkin' about.\x01",
            "Story checks out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3435")

    SetScenarioFlags(0x0, 0)

    label("loc_3438")

    Jump("loc_524B")

    label("loc_343D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_351C")

    ChrTalk(
        0x8,
        (
            "You may be the authorities, but remember\x01",
            "that I will not hesitate to report you if you\x01",
            "damage anything in my apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F(Just go along with her, guys. This ain't\x01",
            "a battle we can win.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_370B")

    label("loc_351C")


    ChrTalk(
        0x8,
        (
            "Who would have thought that the four who\x01",
            "stopped the mayor's assassination still had\x01",
            "time to play downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See to it that you don't damage my\x01",
            "apartment, lest you face my wrath.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3679")

    ChrTalk(
        0x101,
        (
            "#0011FY-You don't have anything to worry about,\x01",
            "ma'am... I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYeah! I bet we won't even go back inside it.\x01",
            "(...Probably.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3708")

    label("loc_3679")


    ChrTalk(
        0x101,
        (
            "#0011FA-Apartment? (And here I thought that\x01",
            "she just lived in her store.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNo worries. We won't lay a finger on it!\x01",
            "(...Maybe.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3708")

    SetScenarioFlags(0x0, 0)

    label("loc_370B")

    Jump("loc_524B")

    label("loc_3710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38B1")

    ChrTalk(
        0x8,
        (
            "Believe it or not, I was invited to a party\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... I'll have to go through\x01",
            "my wardrobe to get all dressed up for it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38A9")

    ChrTalk(
        0x101,
        (
            "#0000F(I get the feeling Imelda has more connections\x01",
            "than she lets on.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Well, she's practically a Crossbellan celebrity.\x01",
            "It's hardly a surprise.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Celebrity, eh? All I see is a heartless real estate\x01",
            "tycoon.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A9")

    SetScenarioFlags(0x0, 0)
    Jump("loc_524B")

    label("loc_38B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3A62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38CE")
    Call(0, 7)
    Jump("loc_3A5D")

    label("loc_38CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_38DF")
    Call(0, 7)
    Jump("loc_3A5D")

    label("loc_38DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3A5A")

    ChrTalk(
        0x8,
        "The fox? He stopped by late last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He kept spouting some nonsense about\x01",
            "forgiveness for pilfering his wife's secret\x01",
            "savings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was alone, mind you, and complaining\x01",
            "up a storm. In the end, he stumbled out of\x01",
            "the shop, saying he needed another drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Apologies, but I have no\x01",
            "way of knowing what happened afterwards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A5D")

    label("loc_3A5A")

    Call(0, 7)

    label("loc_3A5D")

    Jump("loc_524B")

    label("loc_3A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C13")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A7F")
    Call(0, 8)
    Jump("loc_3C0E")

    label("loc_3A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_3A90")
    Call(0, 8)
    Jump("loc_3C0E")

    label("loc_3A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3C0B")

    ChrTalk(
        0x8,
        "The fox? He stopped by late last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He kept spouting some nonsense about\x01",
            "forgiveness for pilfering his wife's secret\x01",
            "savings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was alone, mind you, and complaining\x01",
            "up a storm. In the end, he stumbled out of\x01",
            "the shop, saying he needed another drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Apologies, but I have no\x01",
            "way of knowing what happened afterwards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C0E")

    label("loc_3C0B")

    Call(0, 8)

    label("loc_3C0E")

    Jump("loc_524B")

    label("loc_3C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D07")

    ChrTalk(
        0x8,
        (
            "Sheesh, I just remembered I still need\x01",
            "to negotiate with that crazy old kook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't imagine what sort of tomfoolery he\x01",
            "expects me to put up with this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What in the world is she talking about?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EBE")

    label("loc_3D07")


    ChrTalk(
        0x8,
        "You're friends of Renne, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. Oh, I do love coincidences.\x01",
            "They never fail to liven up my day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYou know Renne? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, she lives in an old acquaintance's\x01",
            "studio and comes to visit me every so\x01",
            "often. A lovely girl, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't believe she's his actual grandchild,\x01",
            "but he certainly loves her as if she was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, that child is a genius. I'm lucky\x01",
            "that she's a regular of mine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3EBE")

    Jump("loc_524B")

    label("loc_3EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F7C")

    ChrTalk(
        0x8,
        (
            "I still have to look into who retains the rights to that\x01",
            "particular plot sometime today. Boy, managing real\x01",
            "estate can be just as hard as running this shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_405E")

    label("loc_3F7C")


    ChrTalk(
        0x8,
        (
            "Ah, well. I suppose I can check in with some folks\x01",
            "at the IBC about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. You see, kids, I own a great deal\x01",
            "of real estate within Crossbell City. So much, in\x01",
            "fact, that it's become quite the hassle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_405E")

    Jump("loc_524B")

    label("loc_4063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_44EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4169")

    ChrTalk(
        0x8,
        (
            "You genuinely are hopeless when it comes\x01",
            "to everything orbal, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* So young, yet so incompetent.\x01",
            "I worry for you, boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(With you being so old, it's a miracle that\x01",
            "you're able to understand it so easily.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E6")

    label("loc_4169")


    ChrTalk(
        0x8,
        (
            "I have to make a visit to the IBC this\x01",
            "evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was able to purchase some delightful\x01",
            "antiques for a bargain price, but now I\x01",
            "have to actually transfer the mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What a pain. When the orbal network is finally\x01",
            "up and running, I won't have to visit the bank\x01",
            "every time I buy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHow does that work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FBasically, people will be able to access their IBC\x01",
            "accounts and make payments online via orbal\x01",
            "terminals.\x02\x03",
            "#0200FThe virtualization and expanded accessibility of\x01",
            "bank functions are the two greatest merits of the\x01",
            "IBC's involvement in the Orbal Network Project.\x02\x03",
            "Suffice to say, I think its realization is still\x01",
            "some ways off.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#0006FSorry. That went over my head.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FSame here. I don't get your\x01",
            "technobabble, Tio Tot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FWell, I think I understood the\x01",
            "gist of it? Sort of?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_44E6")

    Jump("loc_524B")

    label("loc_44EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4750")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4511")
    Call(0, 9)
    Jump("loc_461C")

    label("loc_4511")


    ChrTalk(
        0x8,
        (
            "I'll let you hang on to my apartment\x01",
            "key for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. If you have time, be a\x01",
            "dear and give it a good scrubbing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Sounds like we'll be spending a lot\x01",
            "of time with this lady from now on...\x01",
            "Well, we better get used to it.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_461C")

    Jump("loc_474B")

    label("loc_4621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4733")

    ChrTalk(
        0x8,
        (
            "There are monsters loose in my Downtown\x01",
            "District apartment complex, Maison Imelda.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You'll know it when you see it, I'm sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, go exterminate every one of those\x01",
            "pests for me, okay? Don't let me down,\x01",
            "Special Support Section. Hyeh hyeh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_474B")

    label("loc_4733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_4748")
    Call(0, 16)
    Jump("loc_474B")

    label("loc_4748")

    Call(0, 9)

    label("loc_474B")

    Jump("loc_524B")

    label("loc_4750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_END)), "loc_482B")

    ChrTalk(
        0x8,
        (
            "A goldia-made ring, engraved with the crest\x01",
            "of the white falcon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! I'd wager it's a little out of\x01",
            "your price range, dearies. I hear the pay at the\x01",
            "CPD is dreadfully low.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B78")

    label("loc_482B")


    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Quite the impressive\x01",
            "piece came into my possession today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "See? A goldia ring, engraved with the crest\x01",
            "of the white falcon. And if my hunch is right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...it's an heirloom of the royal Liberlian family, and\x01",
            "a gem of extraordinary beauty that was pawned off\x01",
            "by a debaucherous duke a few years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(A royal heirloom? Is it legal for her\x01",
            "to possess something like that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105F(I'm not sure, but if she isn't cautious, it\x01",
            "might grow into an international issue...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(I doubt we could even file a report on it\x01",
            "without proving it's the genuine article.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. You know, if you want to\x01",
            "investigate it that badly, you can always\x01",
            "buy it, dearies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep in mind, it will cost you an arm and a\x01",
            "leg. The craftsmanship is superb and the\x01",
            "goldia used is of the highest quality.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 3)

    label("loc_4B78")

    Jump("loc_524B")

    label("loc_4B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_4C06")

    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh. You four are quite entertaining.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll make sure to keep a close eye on you\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F57")

    label("loc_4C06")


    ChrTalk(
        0x8,
        (
            "Accomplished quite the feat the other day,\x01",
            "didn't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I didn't expect you to go along with the\x01",
            "Testaments leader's plan to lure them\x01",
            "out. Hyeh hyeh. Color me impressed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FHuh? How do you know about that?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_4D94")

    ChrTalk(
        0x102,
        (
            "#0105FI don't think it was covered in the latest\x01",
            "issue of the Crossbell Times...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DDD")

    label("loc_4D94")


    ChrTalk(
        0x102,
        (
            "#0105FDid Grace decide to turn the case into\x01",
            "an article, after all?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DDD")


    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. Oh, I didn't read about it.\x01",
            "You DO know about informants, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the right amount of mira, you can get\x01",
            "just about any information you'd like.\x02",
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
        0x103,
        "#0200FInformants?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FLeave it to Crossbell to have a bunch of\x01",
            "sketchy jobs like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 2)

    label("loc_4F57")

    Jump("loc_524B")

    label("loc_4F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5123")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 1)), scpexpr(EXPR_END)), "loc_4FA9")

    ChrTalk(
        0x8,
        "See anything you like...Special Support Section?\x02",
    )

    CloseMessageWindow()
    Jump("loc_511E")

    label("loc_4FA9")


    ChrTalk(
        0x8,
        "See anything you like...Special Support Section?\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FWait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FHow do you know our name, Granny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. Curious, are we? All\x01",
            "sorts of information finds its way\x01",
            "to the Back Alley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Congratulations on the new job.\x01",
            "I pray you find it to your liking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 1)

    label("loc_511E")

    Jump("loc_524B")

    label("loc_5123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_519E")

    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh! Welcome, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Feel free to inspect any and all of my\x01",
            "prized antiques, dearies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_524B")

    label("loc_519E")


    ChrTalk(
        0x8,
        "Hyeh hyeh hyeh! Welcome, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Feel free to inspect any and all of my\x01",
            "prized antiques, dearies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Something about this place gives me\x01",
            "the creeps.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_524B")

    Jump("loc_6CC")

    label("loc_5250")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_490 end

    def Function_5_5258(): pass

    label("Function_5_5258")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52EC")
    Jump("loc_5336")

    label("loc_52EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_530C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5336")

    label("loc_530C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_532C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5336")

    label("loc_532C")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5336")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(
        0x8,
        "Came back, did you? How bold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI'm really sorry, Imelda. Something\x01",
            "came up and we didn't have the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FIf there's anything we can do to make up\x01",
            "for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Never mind that. You were preoccupied.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... Besides, I don't need\x01",
            "that silly broker anymore. I found myself\x01",
            "a new, more reliable buyer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The mira is much better, too. I suppose your\x01",
            "ineptitude ended up being my blessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWell, that's good...I guess?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FI feel less guilty, at the very least.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 3)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_5258 end

    def Function_6_556D(): pass

    label("Function_6_556D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5601")
    Jump("loc_564B")

    label("loc_5601")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5621")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_564B")

    label("loc_5621")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5641")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_564B")

    label("loc_5641")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_564B")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(
        0x8,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "So you had to abandon your job at\x01",
            "Maison Imelda, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No matter. Some bracers took care\x01",
            "of it with ease afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! Quite reliable, aren't\x01",
            "they? Unlike a certain squad I know.\x02",
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
        "#0000FMa'am, we're really, really sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Careful, guys. This doesn't look like a grudge\x01",
            "that'll be goin' away any time soon...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 4)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_6_556D end

    def Function_7_5851(): pass

    label("Function_7_5851")

    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_58CB")

    ChrTalk(
        0x8,
        (
            "A showdown between Yin and the Special Support\x01",
            "Section, eh? Hyeh hyeh hyeh! Oh, I can hardly wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A86")

    label("loc_58CB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Imelda is operating some sort of terminal\x01",
            "under the counter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "*click* *clack*...*click* *click* *clack*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What's this? It seems my dear informant decided\x01",
            "to send me some new bites of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm? A showdown between the Special Support\x01",
            "Section and Yin...? How peculiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Jona! That's not the kind of information you\x01",
            "can just throw around!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F(I will have to thoroughly discipline him later.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_5A86")

    Return()

    # Function_7_5851 end

    def Function_8_5A87(): pass

    label("Function_8_5A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5B0F")

    ChrTalk(
        0x8,
        (
            "Police seem to be coming and going out\x01",
            "of Arc en Ciel. That, my dears, requires\x01",
            "my utmost attention. Hyeh hyeh hyeh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D89")

    label("loc_5B0F")


    ChrTalk(
        0x8,
        "According to the information I was sent...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The CPD seem to be coming and going\x01",
            "out of Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "My, how dreadful it would be for them if there\x01",
            "was a scandal right before their new show\x01",
            "debuted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With luck, this won't spoil the excitement that\x01",
            "has been building up around the piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(It looks like details about the situation\x01",
            "are finally starting to leak...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_5D3E")

    ChrTalk(
        0x104,
        (
            "#0306F(Must be her informant, right? I wonder\x01",
            "how much they really know.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D86")

    label("loc_5D3E")


    ChrTalk(
        0x104,
        (
            "#0300F(Well, it sounds like they still\x01",
            "don't have the full story.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D86")

    SetScenarioFlags(0x0, 0)

    label("loc_5D89")

    Return()

    # Function_8_5A87 end

    def Function_9_5D8A(): pass

    label("Function_9_5D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E9B")

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh... I've lived in this city for\x01",
            "nigh seventy years now, and it's never\x01",
            "bored me even once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lately, I've been buying first-hand intel\x01",
            "from a new informant of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That, along with everything else, makes\x01",
            "every day so very amusing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62CA")

    label("loc_5E9B")


    ChrTalk(
        0x8,
        (
            "Did you hear? The Guardian Force members\x01",
            "who were watching over Mainz have already\x01",
            "withdrawn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pathetic. They didn't even take care of\x01",
            "those monsters yet, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FThat should have been classified\x01",
            "information.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_60B3")

    ChrTalk(
        0x101,
        (
            "#0003F(She must have heard what's happened\x01",
            "from one of her informants.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_606F")

    ChrTalk(
        0x104,
        (
            "#0306F(So this old lady is a real estate tycoon AND\x01",
            "has eyes and ears everywhere? Damn, she's\x01",
            "craftier than I gave her credit for.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60AE")

    label("loc_606F")


    ChrTalk(
        0x104,
        "#0303F(I can't tell if she's just plain curious or what.)\x02",
    )

    CloseMessageWindow()

    label("loc_60AE")

    Jump("loc_62C7")

    label("loc_60B3")


    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. Oh, I didn't read about it.\x01",
            "You DO know about informants, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the right amount of mira, you can get\x01",
            "just about any information you'd like.\x02",
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
        "#0003FInformants?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6278")

    ChrTalk(
        0x104,
        (
            "#0306F(So this old lady is a real estate tycoon AND\x01",
            "has eyes and ears everywhere? Damn, she's\x01",
            "craftier than I gave her credit for.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C4")

    label("loc_6278")


    ChrTalk(
        0x104,
        (
            "#0300FLeave it to Crossbell to have a bunch of\x01",
            "sketchy jobs like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C4")

    SetScenarioFlags(0x6C, 2)

    label("loc_62C7")

    SetScenarioFlags(0x0, 0)

    label("loc_62CA")

    Return()

    # Function_9_5D8A end

    def Function_10_62CB(): pass

    label("Function_10_62CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_640B")

    ChrTalk(
        0x8,
        (
            "Do my eyes deceive me, or do you have\x01",
            "the entire set of Back Alley Doctor Glenn?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... I've been meaning to collect\x01",
            "all of them, but I wasn't able to find\x01",
            "every volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I have a proposition for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you give me the entire series, I'll give\x01",
            "you one of my most precious antiques.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 6)
    Jump("loc_6491")

    label("loc_640B")


    ChrTalk(
        0x8,
        (
            "You DO have the entire set of Back Alley\x01",
            "Doctor Glenn novels, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Won't you trade them for one of my\x01",
            "priceless antiques?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6491")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6775")

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh! Wonderful! Everything\x01",
            "here seems to be accounted for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now to uphold my end of the bargain.\x01",
            "This may prove useful to you four.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2C6, 1)
    SubItemNumber(0x2C7, 1)
    SubItemNumber(0x2C8, 1)
    SubItemNumber(0x2C9, 1)
    SubItemNumber(0x2CA, 1)
    SubItemNumber(0x2CB, 1)
    SubItemNumber(0x2CC, 1)
    SubItemNumber(0x2CD, 1)
    SubItemNumber(0x2CE, 1)
    SubItemNumber(0x2CF, 1)
    SubItemNumber(0x2D0, 1)
    SubItemNumber(0x2D1, 1)
    SubItemNumber(0x2D2, 1)
    SubItemNumber(0x2D3, 1)
    AddItemNumber(0x396, 1)
    SetScenarioFlags(0x9D, 6)

    ChrTalk(
        0x101,
        (
            "#0005FTh-Thank you, ma'am.\x02\x03",
            "But, what exactly is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hyeh hyeh hyeh. You see, this is a treasure\x01",
            "I obtained through...certain means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I believe it to be a relic of the ancient\x01",
            "Zemurian civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's incredibly dense and doesn't seem to be\x01",
            "manufacturable with any modern methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But perhaps it may be of some use to you\x01",
            "in the coming days. You never know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6804")

    label("loc_6775")


    ChrTalk(
        0x8,
        "Ah, what a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I suppose it's back to the used bookstores\x01",
            "with me. All I want is to own the entire set\x01",
            "and binge-read them all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6804")

    Return()

    # Function_10_62CB end

    def Function_11_6805(): pass

    label("Function_11_6805")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_68C1")
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Ten, one hundred, one thousand...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Something tells me that there's a few more\x01",
            "zeros in there, but...maybe that's just my\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69AD")

    label("loc_68C1")


    ChrTalk(
        0xA,
        (
            "Who knew that a store like this was hiding all\x01",
            "the way back here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "On my way back to my hotel after the parade,\x01",
            "I made an unexpected discovery... This place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Should I pick up a souvenir before\x01",
            "heading back?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_69AD")

    TalkEnd(0xFE)
    Return()

    # Function_11_6805 end

    def Function_12_69B1(): pass

    label("Function_12_69B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_6A45")

    ChrTalk(
        0x9,
        (
            "#3300FThat wolf became your friend, didn't he?\x02\x03",
            "#3309FIf you could, please introduce me to him\x01",
            "next time you have the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A48")

    label("loc_6A45")

    Call(0, 13)

    label("loc_6A48")

    TalkEnd(0xFE)
    Return()

    # Function_12_69B1 end

    def Function_13_6A4C(): pass

    label("Function_13_6A4C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3250, 1450, 180, 0)
    MoveCamera(320, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20690, 0)
    SetChrPos(0x101, -2800, 0, 310, 270)
    SetChrPos(0x102, -2500, 0, 1400, 225)
    SetChrPos(0x103, -2550, 0, -960, 315)
    SetChrPos(0x104, -3500, 0, 1870, 180)
    SetChrSubChip(0x9, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    ChrTalk(
        0x9,
        "#3305F#5POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205F#6PWe have met her before, yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F#12PYeah, we have. Back at the doll studio.\x02\x03",
            "#0000FIt's been a while. Your name was...\x01",
            "Renne, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "Teehee. Correct. I believe it's\x01",
            "been about a month since we last\x01",
            "saw each other.\x02\x03",
            "And, you know, it's very impolite\x01",
            "to have to double-check what a\x01",
            "lady's name is.\x02\x03",
            "As a gentleman, shouldn't you have\x01",
            "had no trouble remembering it?\x01",
            "Tsk, tsk.\x02",
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
        "#0012F#12PHaha, you're right. Sorry, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0304F#11PStern lil' girl, ain't she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F#11PYou look like you're alone. Did\x01",
            "you take the bus to come look\x01",
            "around the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3304F#5PYes. Something like that.\x02\x03",
            "#3300FYou see, I enjoy visiting the antique shop by\x01",
            "myself every so often.\x02\x03",
            "They occasionally put Grandpa's dolls on\x01",
            "display, and, oh, they have the absolute\x01",
            "cutest stuffed animals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F#12PThey do? Huh.\x02\x03",
            "#0006FStill, isn't wandering around this part of town\x01",
            "alone kind of irresponsible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3304F#5PI assure you, nothing here possibly poses a\x01",
            "threat to me.\x02\x03",
            "The barkers and hostesses are all very nice\x01",
            "people...\x02\x03",
            "#3302F...and those men in the back wearing all the\x01",
            "black glasses never fail to make me laugh.\x02",
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
        "#0003F#12PTh-That's... Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F#11PYou make me worried, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3304F#5PTeehee. Oh, that reminds me.\x02\x03",
            "#3302FDid you have fun playing\x01",
            "hide-and-seek with the wolves?\x02\x03",
            "It looked as though you had quite a\x01",
            "few uninvited guests show up at the\x01",
            "last second, too.\x02",
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
        0x102,
        "#0105F#11PCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F#12PDid you get all that from reading the\x01",
            "Crossbell Times article about the case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3304F#5PSure. Let's go with that.\x02\x03",
            "#3300FThat wolf became your friend, didn't he?\x02\x03",
            "#3309FIf you could, please introduce me to him\x01",
            "next time you have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002F#12PUh, sure. We'd love to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0302F#11P(Mysterious as always, this one.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F#6P(Indeed she is.)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -2800, 0, 310, 270)
    OP_93(0x9, 0x10E, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x93, 0)
    EventEnd(0x5)
    Return()

    # Function_13_6A4C end

    def Function_14_739E(): pass

    label("Function_14_739E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743B")
    OP_29(0x46, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#0003F(All right, that's a wrap on the Back Alley\x01",
            "investigation.)\x02\x03",
            "#0001F(Let's try asking around Central Square next!)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)

    label("loc_743B")

    Return()

    # Function_14_739E end

    def Function_15_743C(): pass

    label("Function_15_743C")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch09000.itc", 0x1E)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11PSo you came, after all...Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FGood morning, ma'am. You must be Imelda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PIndeed I am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. I see quite a few youngsters\x01",
            "have come to help, eh? Let me get a good\x01",
            "look at you...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -750, 0, 4600, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Imelda began to analyze each member from head to toe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#5P#0005F(W-Wow. Is it just me, or is her face massive?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0105F(Lloyd, shush. But, I will say, she certainly has\x01",
            "quite the presence...)\x02\x03",
            "#0103F(...and it's obvious why. She's practically a\x01",
            "Crossbellan celebrity.)\x02\x03",
            "#0100FExcuse us, Imelda. Your support request mentioned\x01",
            "that monsters are running loose in your apartment\x01",
            "complex, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0305FAnd ain't it in the city? That's dangerous, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHyeh hyeh hyeh! Well, of course it is.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -750, 100, 4800, 180)
    Sound(820, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#6P#0200F(She does not seem very concerned,\x01",
            "does she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306F(Heh. This lady's got nerves of steel.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PSo, kids, will you take care of them?\x02",
    )

    CloseMessageWindow()
    OP_29(0xA, 0x1, 0x0)
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D9")
    Call(0, 18)

    label("loc_78D9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(-750, 1450, 2000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetChrPos(0x1, -750, 0, 2000, 0)
    SetChrPos(0x2, -750, 0, 2000, 0)
    SetChrPos(0x3, -750, 0, 2000, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_15_743C end

    def Function_16_7965(): pass

    label("Function_16_7965")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1450, 2860, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11PI have some monsters running rampant\x01",
            "in an apartment complex I own, and I'd\x01",
            "like you four to eliminate them for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHyeh hyeh hyeh. Can you do it?\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A99")
    Call(0, 18)

    label("loc_7A99")

    SetChrPos(0x0, -750, 0, 2000, 0)
    EventEnd(0x5)
    Return()

    # Function_16_7965 end

    def Function_17_7AAD(): pass

    label("Function_17_7AAD")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C62")

    ChrTalk(
        0x101,
        (
            "#5P#0006FActually, we're sort of preoccupied right\x01",
            "now. I'm sorry, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POh? Is that so? Be quick about your\x01",
            "business, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou wouldn't want me to turn to the\x01",
            "Bracer Guild instead, now would you?\x02",
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
        "#5P#0003FTh-That won't be necessary, ma'am.\x02",
    )

    CloseMessageWindow()

    label("loc_7C62")

    Return()

    # Function_17_7AAD end

    def Function_18_7C63(): pass

    label("Function_18_7C63")


    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. Wonderful! Shall we talk\x01",
            "business, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FSure. Could you give us the details?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, as I'm sure you know, I own quite\x01",
            "a bit of land and property in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe apartment complex in question is called\x01",
            "Maison Imelda, named after yours truly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's in the Downtown District. Near that rowdy\x01",
            "Ignis or whatever those fools call it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0105FYou own property downtown...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0303FI'm sure it's a mess. Leavin' a place\x01",
            "like that unchecked, I'd say monsters\x01",
            "are the least of your worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, well, they're there, and I want\x01",
            "them gone. Especially considering\x01",
            "how wild they've gotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you don't tidy up the place, I doubt\x01",
            "the property will last another week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAll I ask is that you go in, find where they\x01",
            "are, and evict-scerate them. Simple as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FYes, ma'am. It just sounds like another\x01",
            "straightforward extermination for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThe situation could escalate if we leave\x01",
            "them be. I will begin prepping my sensors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI suppose I should give you this, too.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x33C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33C, 1)

    ChrTalk(
        0x101,
        "#5P#0000FThank you, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FDowntown District, then?\x02",
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
            "[Abandoned Apartment Monster Cleanup]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0xA, 0x1, 0x1)
    Return()

    # Function_18_7C63 end

    def Function_19_81AB(): pass

    label("Function_19_81AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11POh? Finished the job, have you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh! The Special Support Section\x01",
            "has proven more interesting than I thought!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou were clumsy, but you did what had to be\x01",
            "done. And for that, job well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0006FThanks, I guess?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0301FHold the phone. For that many monsters\x01",
            "to have nested there, you must've been\x01",
            "neglecting that place for years!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FIndeed. You may want to develop some\x01",
            "management skills in order to maintain\x01",
            "security from now on, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FBut on the bright side, you're free to start\x01",
            "renting out rooms.\x02\x03",
            "If people began to move in, I doubt you'd\x01",
            "have to call pest control again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI suppose you're right. I was just thinking\x01",
            "about how much longer I should wait to\x01",
            "open Maison Imelda's doors.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5P#0105FHow much longer...? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYou see, dear, downtown rent is dirt cheap. So,\x01",
            "I was merely biding my time, waiting for the land\x01",
            "value to go up a bit more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. When it comes to real estate\x01",
            "matters, you should trust in my judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI'm Imelda, one of the greatest real estate minds\x01",
            "in all of Crossbell, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThat run-down apartment complex is the cheapest\x01",
            "piece of property I own, but I have many other\x01",
            "places I profit from thanks to rising land values.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FYou sound like a genuine real estate tycoon,\x01",
            "ma'am.\x02\x03",
            "#0006F(Wait... Is this place just her side business?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103F(Madam Imelda is a famous name in\x01",
            "Crossbellan high society...)\x02\x03",
            "#0100F(I've heard she's incredibly wealthy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0300F(Damn, really? I could tell she wasn't\x01",
            "your ordinary granny.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf property is left unchecked, monsters will\x01",
            "occasionally make it their home. That calls\x01",
            "for eviction, in my opinion.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11POh, and I'll leave the Maison Imelda key\x01",
            "with you for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. If you ever have any free time,\x01",
            "do an old lady a favor and give it a clean?\x02",
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
        0x103,
        "#6P#0200F(Persuasive as always.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006F(Can we get back to work? Talking to her\x01",
            "has given me a headache.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0106F(Yes, I would love to...)\x02",
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
            "[Abandoned Apartment Monster Cleanup]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0xA, 0x1, 0x7)
    OP_29(0xA, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_19_81AB end

    def Function_20_8BA9(): pass

    label("Function_20_8BA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-750, 1450, -2000, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, -1250, 0)
    SetChrPos(0x103, -1250, 0, -1250, 0)
    SetChrPos(0x11C, -750, 0, -3000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x11C,
        "#6P#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FHe appears to have tracked the vice\x01",
            "commissioner scent inside of the shop.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8CD7")

    ChrTalk(
        0x101,
        "#11P#0003FImelda might be able to help us out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D22")

    label("loc_8CD7")


    ChrTalk(
        0x101,
        (
            "#11P#0003FShould we ask the owner about it? She\x01",
            "might know something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D22")

    OP_68(-730, 1450, 2860, 3000)

    def lambda_8D38():
        OP_97(0x101, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D38)
    Sleep(50)

    def lambda_8D55():
        OP_97(0x103, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D55)
    Sleep(50)

    def lambda_8D72():
        OP_97(0x11C, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_8D72)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0000FExcuse us, ma'am. We'd like to ask you\x01",
            "a few questions about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh? The Special Support Section, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh! Finally fired from the CPD,\x01",
            "were we?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8E75")

    ChrTalk(
        0x101,
        "#6P#0006FWh-What? No!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8EF5")

    label("loc_8E75")


    ChrTalk(
        0x101,
        (
            "#6P#0006FWh-Why the heck would you say that?\x01",
            "(I don't like this. She's already ringing\x01",
            "every warning bell I can think of.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF5")


    ChrTalk(
        0x101,
        (
            "#6P#0001FAnyway, I'd like to ask you a bit of an\x01",
            "awkward question. Did an intoxicated\x01",
            "man stumble in here last night?\x02\x03",
            "#0003FHe actually lost something in the area\x01",
            "while, uh, under the influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAre you talking about the fox?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNow that I think about it, he did reek of cheap\x01",
            "wine as he crashed through my door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe was babbling some nonsense and asking\x01",
            "to be forgiven for stealing his wife's savings...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe was alone, but complained enough for\x01",
            "three men. Eventually, he left, claiming he\x01",
            "was going to drink again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#0006FG-Geez... He was further gone than we\x01",
            "thought, wasn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FWe apologize on his behalf, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. It's fine. Tell him that\x01",
            "next time he stops by, I expect him to\x01",
            "buy one of my finest jewels!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003F(If we can't find the wedding ring, he\x01",
            "might just have to...)\x02\x03",
            "#0000FWell, we appreciate your help. Have\x01",
            "a nice rest of your day, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#0203FThat eliminates this location, then.\x02\x03",
            "#0200FWe should continue the search.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#12P#0000FDefinitely.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x15, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_20_8BA9 end

    def Function_21_9388(): pass

    label("Function_21_9388")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-430, 1450, 4410, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(19970, 0)
    SetChrPos(0x101, -250, 0, -1750, 0)
    SetChrPos(0x102, -1250, 0, -2000, 0)
    SetChrPos(0x103, -250, 0, -3250, 0)
    SetChrPos(0x104, -1250, 0, -3500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Imelda is using a communication device\x01",
            "installed beneath the counter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#11PWhat?! Don't joke with me, you old fool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PI've had a buyer lined up for ages!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's ready, isn't it? Send it here immediately!\x01",
            "Do I make myself clear?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#11PDamn it! He hung up on me!\x02",
    )

    CloseMessageWindow()
    OP_68(-10, 1350, 1330, 3000)
    MoveCamera(317, 17, 0, 3000)
    SetCameraDistance(21890, 3000)

    def lambda_9596():
        OP_97(0x101, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9596)
    Sleep(50)

    def lambda_95B3():
        OP_97(0x102, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_95B3)
    Sleep(50)

    def lambda_95D0():
        OP_97(0x103, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_95D0)
    Sleep(50)

    def lambda_95ED():
        OP_97(0x104, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_95ED)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#6P#0100FGood morning, Imelda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FIs something wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11PAh, it's just you four.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWell, I'll just say that this crazy old man\x01",
            "I know has started to go senile...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh! That's it! The Goddess\x01",
            "must have had mercy on me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PYes, yes! This is too perfect a chance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0011FWhat are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306FNot sure, but I have a bad feeling about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0211FFeeling? More like a certainty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAre you free now, by chance?\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#11PYou are? Splendid!\x02",
    )

    CloseMessageWindow()
    Call(0, 22)
    EventEnd(0x5)
    Return()

    # Function_21_9388 end

    def Function_22_9899(): pass

    label("Function_22_9899")


    ChrTalk(
        0x101,
        (
            "#6P#0012FN-No, wait. We actually have somewhere\x01",
            "to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph. Oh, I'm sure you do. I bet it's not\x01",
            "for anything urgent, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAfter all, you had time to stop by here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001F*sigh* Okay, you got me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FDo you have a job for us, Imelda?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PSmart girl! Not that I would expect anything\x01",
            "less from old MacDowell's granddaughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHyeh hyeh hyeh. I do, in fact, have something\x01",
            "for you to do. Will compensation be necessary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FN-No, you don't have to pay us.\x02\x03",
            "#0000FOkay, go ahead and tell us what's wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PVery well, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAll I need you to do is go pick up a doll\x01",
            "and deliver it to me.\x02",
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
        "#6P#0005FA doll...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105FBy that, do you mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI do. One from Rosenberg Studio, which\x01",
            "you'll find on the outskirts of the northern\x01",
            "mountain path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNaturally, it's no fake like that one at the\x01",
            "Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's a genuine Rosenberg doll, and it's in\x01",
            "mint condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FWhoa, back it up! Don't those things go\x01",
            "for tens of thousands of mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FA single Rosenberg doll is worth the average\x01",
            "annual income of one Crossbellan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PYes, well, I'm contracted as the studio's\x01",
            "sales agent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe only problem is that the meister is an\x01",
            "old fool who hates human interaction!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI went to great lengths to find a buyer\x01",
            "for his latest doll, and he has the nerve\x01",
            "to start complaining now?!\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#6P#0012FSorry, Imelda. I don't think that's\x01",
            "a problem we can do anything about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FWe should be able to bring you this doll\x01",
            "you keep mentioning, but I'm curious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWhy is the meister suddenly against\x01",
            "selling it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAh, well, the buyer is slightly problematic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PTruth be told, he's an infamous broker\x01",
            "that always resells rare works of art at\x01",
            "exorbitantly high prices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI can only assume that the old coot is\x01",
            "put off by that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0108FAs the artist, I can hardly blame him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0301FI dunno, guys. Aren't we busy enough\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PExcuse me? Youngsters these days\x01",
            "are so extremely lazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PCome, now. I'm paying for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI have no doubt you can change that man's\x01",
            "callous heart and safely retrieve the doll!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FR-Right...\x02\x03",
            "#0008F(Rosenberg Studio... That name\x01",
            "just causes me to worry about Renne.)\x02\x03",
            "(KeA, too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#6P#0003FWe can't promise that we'll get the job\x01",
            "done, since we have other things to\x01",
            "take care of, but...\x02\x03",
            "#0000F...if you're okay with that, we accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, how wonderful!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDon't let me down, dearies!\x02",
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
            "[Getting a New Doll]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x30, 0x4, 0x2)
    Return()

    # Function_22_9899 end

    def Function_23_A3F9(): pass

    label("Function_23_A3F9")

    EventBegin(0x1)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Is that trunk what I think it is?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThat's right. Joerg agreed to leave it\x01",
            "with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWould you like to confirm its contents?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    EventBegin(0x0)
    OP_68(200, 1350, 2420, 0)
    MoveCamera(317, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22800, 0)
    SetCameraDistance(20800, 3000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#2PHyeh hyeh hyeh! Sweet Aidios, it really is\x01",
            "that nut's new doll!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PI cannot fathom how you convinced him,\x01",
            "but bravo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0309FI'm not sure if we convinced him, or if he was\x01",
            "just impressed by our raw stubbornness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FEither way, it is a marvelous doll, isn't it?\x02\x03",
            "#0102FI've seen some before at a friend's place, but\x01",
            "each one truly is a masterpiece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0202FThe craftsmanship takes one's breath away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0004FI am inclined to agree. They're remarkable.\x02\x03",
            "#0005FI was expecting it to be about the\x01",
            "same size as KeA, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_A807")

    ChrTalk(
        0x8,
        "#2PThat sweet little girl you brought before, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PThere are Rosenberg dolls that are about\x01",
            "her height, yes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A879")

    label("loc_A807")


    ChrTalk(
        0x8,
        "#2PThe Schwarze Auction mystery child, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PThere are Rosenberg dolls that are about\x01",
            "her height, yes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A879")


    ChrTalk(
        0x8,
        (
            "#2PJoerg seldom makes them, though, so you\x01",
            "never see them on the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PThat's also why they're said to fetch\x01",
            "such outrageous prices at the auction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FPerhaps older dolls were more her size.\x02\x03",
            "#0100FFor example, I remember Bell's being\x01",
            "a similar height.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FOh, really?\x02\x03",
            "#0001FI have a question, Imelda.\x02\x03",
            "Are you aware of the 'other dolls'\x01",
            "Rosenberg Studio has made?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2POther dolls? Whatever do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FHow about giant dolls that can move on\x01",
            "their own. Ring any bells?\x02\x03",
            "#0301FSpecifically one that looks like an angel,\x01",
            "and another with a big face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2POh? Are you perhaps talking about the\x01",
            "automata?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2PIf anything, I'd say he specializes in them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PTheir movements seem to be even more\x01",
            "elaborate, now that Joerg is developing\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0105FY-You know about them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PAnd you didn't? Even Arc en Ciel uses them\x01",
            "on stage from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PI believe the soldier with the spear in their\x01",
            "latest production was an automaton.\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#6P#0011FWh-What?! But, it was using the spear and\x01",
            "everything...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FI never would have guessed.\x01",
            "Not in a million years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PWell, surprise. The troupe sent an entire\x01",
            "order for complex stage props, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PThe lighting apparatus, the water control,\x01",
            "the wire-flying system... It was a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PThe public doesn't seem to have caught on\x01",
            "to these tricks, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0305FWell, my mind's blown.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0201FI will admit that I thought the stage\x01",
            "was incorporating impressive tech.\x02\x03",
            "#0208FBut does that mean that those angels\x01",
            "and monsters function similarly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PWho's to say? I just know that old coot's\x01",
            "obstinate, is full of mysteries, and hates\x01",
            "people, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P...if he puts out a new product every so\x01",
            "often and lets me dip in on the profit, I\x01",
            "don't have any complaints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2PAgain, thank you. If I need any helping\x01",
            "hands, I'll give you a call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0005FYou're welcome, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FWell, then... If you'll excuse us.\x02",
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
            "[Getting a New Doll]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SubItemNumber(0x359, 1)
    OP_68(-750, 1450, 2000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetChrPos(0x1, -750, 0, 2000, 0)
    SetChrPos(0x2, -750, 0, 2000, 0)
    SetChrPos(0x3, -750, 0, 2000, 0)
    OP_29(0x30, 0x1, 0x6)
    OP_29(0x30, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_A3F9 end

    def Function_24_B1B9(): pass

    label("Function_24_B1B9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B34E")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exquisite dolls are lined up, side by side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B34E")

    ChrTalk(
        0x101,
        "#0005FWhoa. Antique dolls?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThey look meticulously made. I would go\x01",
            "so far as to call them masterpieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FYeah, they're pretty amazing. Maybe not\x01",
            "for that high a price, but still pretty cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FWe are in an antique shop, after all.\x02\x03",
            "#0103F(They don't look like THOSE dolls, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 4)

    label("loc_B34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B67C")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exquisite dolls are lined up, side by side.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B67C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B42D")

    ChrTalk(
        0x101,
        (
            "#0000FWow, these dolls look really nice.\x02\x03",
            "#0005FCould they be from that doll studio\x01",
            "that's right off of the mountain path?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B49C")

    label("loc_B42D")


    ChrTalk(
        0x101,
        (
            "#0000FAntique dolls...\x02\x03",
            "#0005FCould these be from that doll studio\x01",
            "that's right off of the mountain path?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B49C")


    ChrTalk(
        0x102,
        (
            "#0103FNo, I don't think these are Rosenberg dolls.\x02\x03",
            "#0100FThose are much nicer, and more expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNicer than these? Damn.\x02\x03",
            "#0301FY'know, Mademois-Elie, you seem to know\x01",
            "an awful lot about dolls.\x02\x03",
            "You wouldn't happen to own one, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FAh, no. Not me, but someone I know.\x02\x03",
            "#0100FBecause of her, I've seen a couple of them\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI suppose that makes sense.\x02\x03",
            "I would like to see one someday. I hear\x01",
            "Rosenberg dolls are indescribable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 5)

    label("loc_B67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_B70F")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exquisite dolls are lined up, side by side.\x02\x03",
            "They seem to be worth a fortune, but not as much\x01",
            "as a Rosenberg doll would cost.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_B70F")

    TalkEnd(0xFF)
    Return()

    # Function_24_B1B9 end

    SaveToFile()

Try(main)
