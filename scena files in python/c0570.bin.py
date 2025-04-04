from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0570.bin",                # FileName
        "c0570",                    # MapName
        "c0570",                    # Location
        0x0027,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 39, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0570",                  # 0
        "Eric",                   # 1
        "Sandra",                 # 2
        "Detective Dudley",       # 3
        "Detective Emma",         # 4
        "Guest",                  # 5
        "Guest",                  # 6
        "Guest",                  # 7
        "Bracer Scott",           # 8
        "Bracer Wenzel",          # 9
        "Grace",                  # 10
        "Chief Sergei",           # 11
        "Deputy Commander Baelz", # 12
        "Tableware",              # 13
        "Tableware",              # 14
        "いす",                   # 15
    ))

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch26802.itc",                   # 01
        "chr/ch32202.itc",                   # 02
        "chr/ch06002.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00900.itc",                   # 06
        "chr/ch30500.itc",                   # 07
        "chr/ch27200.itc",                   # 08
        "chr/ch27300.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch27802.itc",                   # 0B
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

    DeclNpc(0,       0,       6400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4699,   79,      4449,    0,    261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-1200,   0,       4190,    45,   389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-1340,   0,       2930,    45,   389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-2349,   100,     4449,    0,    389,  0x0, 0,   2,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(1240,    0,       1799,    0,    389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-8199,   100,     -479,    90,   405,  0x0, 0,   11,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1480,    0,       2569,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1019,    0,       1539,    315,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-8399,   100,     -500,    90,   405,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       5000,    1000,    0,       1500,    6400,    0x007E, 0,  4,  0x0000)
    DeclActor(-4600,   0,       -480,    2500,    -4600,   1000,    -480,    0x007C, 0,  23, 0x0000)
    DeclActor(-8640,   0,       -490,    2500,    -8640,   1000,    -490,    0x007C, 0,  24, 0x0000)
    DeclActor(-6950,   0,       4150,    2000,    -6950,   500,     4150,    0x007C, 0,  25, 0x0000)

    ScpFunction((
        "Function_0_3B8",          # 00, 0
        "Function_1_470",          # 01, 1
        "Function_2_545",          # 02, 2
        "Function_3_66E",          # 03, 3
        "Function_4_7F8",          # 04, 4
        "Function_5_7FC",          # 05, 5
        "Function_6_2E26",         # 06, 6
        "Function_7_2ED8",         # 07, 7
        "Function_8_3242",         # 08, 8
        "Function_9_34A3",         # 09, 9
        "Function_10_4610",        # 0A, 10
        "Function_11_47CA",        # 0B, 11
        "Function_12_4A28",        # 0C, 12
        "Function_13_4BB0",        # 0D, 13
        "Function_14_4DA1",        # 0E, 14
        "Function_15_4E3B",        # 0F, 15
        "Function_16_4EBC",        # 10, 16
        "Function_17_4F07",        # 11, 17
        "Function_18_5383",        # 12, 18
        "Function_19_53E8",        # 13, 19
        "Function_20_5637",        # 14, 20
        "Function_21_5CB1",        # 15, 21
        "Function_22_607E",        # 16, 22
        "Function_23_611C",        # 17, 23
        "Function_24_615C",        # 18, 24
        "Function_25_61D7",        # 19, 25
        "Function_26_6293",        # 1A, 26
        "Function_27_680E",        # 1B, 27
        "Function_28_7183",        # 1C, 28
        "Function_29_734A",        # 1D, 29
    ))


    def Function_0_3B8(): pass

    label("Function_0_3B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3F8"),
        (1, "loc_404"),
        (2, "loc_410"),
        (3, "loc_41C"),
        (4, "loc_428"),
        (5, "loc_434"),
        (6, "loc_440"),
        (SWITCH_DEFAULT, "loc_44C"),
    )


    label("loc_3F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_404")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_410")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_41C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_428")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_434")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_440")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_46F")

    Return()

    # Function_0_3B8 end

    def Function_1_470(): pass

    label("Function_1_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_544")
    OP_95(0xFE, 780, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -6210, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -6210, 0, 830, 1000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -6210, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -8480, 0, 1680, 1000, 0x0)
    OP_95(0xFE, -8480, 0, 6780, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0xFA)
    Sleep(2200)
    OP_95(0xFE, -8480, 0, 2480, 1000, 0x0)
    OP_95(0xFE, 290, 0, 2480, 1000, 0x0)
    OP_95(0xFE, 1170, 0, 3820, 1000, 0x0)
    Sleep(2800)
    Jump("Function_1_470")

    label("loc_544")

    Return()

    # Function_1_470 end

    def Function_2_545(): pass

    label("Function_2_545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_554")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x11, 0x80)

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_66D")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_592")
    Jump("loc_66D")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5AA")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_66D")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5C2")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_66D")

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_66D")

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5F9")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -4700, 80, 4450, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_66D")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_611")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_66D")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_61F")
    Jump("loc_66D")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_648")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -130, 0, 4420, 360)
    SetChrFlags(0x8, 0x10)
    Jump("loc_66D")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_66D")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_664")
    Jump("loc_66D")

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_66D")

    label("loc_66D")

    Return()

    # Function_2_545 end

    def Function_3_66E(): pass

    label("Function_3_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_70C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_74D")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_744")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_74D")

    label("loc_744")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_74D")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_767")
    Jump("loc_7A8")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_781")
    Jump("loc_7A8")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_78F")
    Jump("loc_7A8")

    label("loc_78F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_7A8")
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_7F7")

    Return()

    # Function_3_66E end

    def Function_4_7F8(): pass

    label("Function_4_7F8")

    Call(0, 5)
    Return()

    # Function_4_7F8 end

    def Function_5_7FC(): pass

    label("Function_5_7FC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_80D")
    Jump("loc_855")

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_83A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_835")
    Call(0, 26)
    Return()

    label("loc_835")

    Jump("loc_855")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")
    Call(0, 8)
    TalkEnd(0x8)
    Return()

    label("loc_855")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E22")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D0")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E1D")

    label("loc_8D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E4")
    Jump("loc_2E1D")

    label("loc_8E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A7")

    ChrTalk(
        0x8,
        (
            "How am I supposed to know where the\x01",
            "Revache guys disappeared off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've been bartending this whole time,\x01",
            "so I don't know diddly squat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A57")

    label("loc_9A7")


    ChrTalk(
        0x8,
        (
            "Some people from the First Division came\x01",
            "to question me about Revache a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sheesh, what a pain in my rear.\x01",
            "I'm just a bartender. What would I know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A57")

    Jump("loc_2E1D")

    label("loc_A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AFB")

    ChrTalk(
        0x8,
        (
            "The Revache building has been giving\x01",
            "me the creeps ever since last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "What are they doing inside there to\x01",
            "make it feel so ominous?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1D")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B90")

    ChrTalk(
        0x8,
        (
            "Guess they're waiting on Heiyue's next move...\x01",
            "Man, this is too much anxiety.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_END)), "loc_B8B")

    ChrTalk(
        0x8,
        "Drop by any time you'd like.\x02",
    )

    CloseMessageWindow()

    label("loc_B8B")

    Jump("loc_C39")

    label("loc_B90")


    ChrTalk(
        0x8,
        "A raid on their office? Seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "That came completely out of left field.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Given how things stand, I sure hope\x01",
            "it doesn't explode into an all-out war.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C39")

    Jump("loc_2E1D")

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(
        0x8,
        "Come in and have a relaxing time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D03")

    label("loc_C7C")


    ChrTalk(
        0x8,
        "Welcome to Garante.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Our stage will be open at 8PM.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Feel free to sit back, relax, and maybe\x01",
            "enjoy a drink until then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D03")

    Jump("loc_2E1D")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB3")

    ChrTalk(
        0x8,
        (
            "I don't have any particularly\x01",
            "important information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I simply hear the occasional rumor drift up\x01",
            "from Crossbell's underworld, that's all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F22")

    label("loc_DB3")


    ChrTalk(
        0x8,
        (
            "I've been hearing some talk about\x01",
            "this weird urban legend lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, well. It's not like urban legends\x01",
            "are out of the ordinary in this city.\x01",
            "Time to open up shop, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005F(Urban legend? That was a pretty\x01",
            "random thing to bring up...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F22")

    Jump("loc_2E1D")

    label("loc_F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_132E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 4)), scpexpr(EXPR_END)), "loc_11F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(
        0x8,
        (
            "Sounds like they really flubbed that\x01",
            "auction of theirs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard that Revache is in total\x01",
            "disarray because of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F0")

    label("loc_FC7")


    ChrTalk(
        0x8,
        (
            "Revache & Co. has been awfully\x01",
            "quiet this week...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sounds like they really flubbed that\x01",
            "auction of theirs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don Marconi and Speaker Hartmann have\x01",
            "been at each other's throats ever since.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1106")

    ChrTalk(
        0x102,
        (
            "#0108F(Wow, news about the criminal underworld\x01",
            "travels quickly throughout the Back Alley.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11ED")

    label("loc_1106")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1184")

    ChrTalk(
        0x103,
        (
            "#0200F(It does not take long for rumors about\x01",
            "the criminal underworld to spread in the\x01",
            "Back Alley.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11ED")

    label("loc_1184")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11ED")

    ChrTalk(
        0x104,
        (
            "#0306F(Dang, any word about the underground sure\x01",
            "moves quickly around these parts.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11ED")

    SetScenarioFlags(0x0, 0)

    label("loc_11F0")

    Jump("loc_1329")

    label("loc_11F5")


    ChrTalk(
        0x8,
        (
            "Welcome to Garante. Sorry, we're not\x01",
            "open right now. Mind coming back later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FOoooh, what kinda store is this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a jazz bar.\x01",
            "It's an adult establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Not the best place for kids like yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FS-Sorry about that. We just wanted\x01",
            "to stop by here for a second.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 4)

    label("loc_1329")

    Jump("loc_2E1D")

    label("loc_132E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_13BE")

    ChrTalk(
        0x8,
        (
            "Revache & Co. is being\x01",
            "pretty quiet today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I'm not complaining. Maybe I\x01",
            "can finally work in peace now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C4")

    label("loc_13BE")


    ChrTalk(
        0x8,
        (
            "Revache & Co. is being\x01",
            "pretty quiet today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I imagine half their crew is headed for\x01",
            "the estate right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Man, they've done this for, like...the\x01",
            "last seven or eight years straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(The Schwarze Auction must be well known\x01",
            "in the world of organized crime...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103F(It's definitely made a name for itself.\x01",
            "Even I've heard the rumors...)\x02\x03",
            "#0101F(Revache even goes as far as advertising it,\x01",
            "so I assume it serves as a sort of symbol of\x01",
            "status in Crossbell's criminal underworld.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15C4")

    Jump("loc_2E1D")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_165A")

    ChrTalk(
        0x8,
        (
            "The parade passed by Arc en Ciel\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our customers practically\x01",
            "vanished just to go see it.\x01",
            "Come on, now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1D")

    label("loc_165A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_187D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_16DC")

    ChrTalk(
        0x8,
        "You should know kids aren't allowed in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "And, no, I haven't seen the one you're looking for.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1878")

    label("loc_16DC")


    ChrTalk(
        0x101,
        (
            "#0001F(I doubt they'd let a child into a bar, but\x01",
            "he might know of Colin's whereabouts.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "A lost kid? Haven't seen any kids\x01",
            "around these parts, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This IS a bar, after all. We don't\x01",
            "let minors run around in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FMakes sense... Thanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 22)

    label("loc_1878")

    Jump("loc_2E1D")

    label("loc_187D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_190E")

    ChrTalk(
        0x8,
        (
            "The parade passed by Arc en Ciel\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That would explain where all of\x01",
            "our customers went. Just my luck...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1D")

    label("loc_190E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_199F")

    ChrTalk(
        0x8,
        "Today's going to be livelier than usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope people don't get swept up\x01",
            "in the moment and wander over to\x01",
            "Revache & Co.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1D")

    label("loc_199F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A04")

    ChrTalk(
        0x8,
        "Police must be struggling to stay on alert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You have my sympathies.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BCE")

    label("loc_1A04")


    ChrTalk(
        0x8,
        "Police must be struggling to stay on alert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I sometimes spot First Division investigators\x01",
            "patrolling around the city in their casual clothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The First Division's pro at blending in with\x01",
            "the crowd. I barely even noticed them.\x02",
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
        "#0100FYou know a surprising amount of information...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Eh, I'm used to picking up little tidbits of info.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BCE")

    Jump("loc_2E1D")

    label("loc_1BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C72")

    ChrTalk(
        0x8,
        (
            "We're always open through the night,\x01",
            "so I don't have much choice but to\x01",
            "sacrifice some of my free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Man, what a bummer...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CEA")

    label("loc_1C72")


    ChrTalk(
        0x8,
        "Welcome to Garante.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're open all day during\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Can't say I'm happy about it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CEA")

    Jump("loc_2E1D")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1DBF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D0C")
    Call(0, 6)
    Jump("loc_1DBA")

    label("loc_1D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1D1D")
    Call(0, 6)
    Jump("loc_1DBA")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(
        0x8,
        (
            "If you're looking for Sandra,\x01",
            "she's right over there, dozing\x01",
            "away at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why don't you try waking her\x01",
            "up and asking?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBA")

    label("loc_1DB7")

    Call(0, 6)

    label("loc_1DBA")

    Jump("loc_2E1D")

    label("loc_1DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1E8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DDC")
    Call(0, 21)
    Jump("loc_1E8A")

    label("loc_1DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1DED")
    Call(0, 21)
    Jump("loc_1E8A")

    label("loc_1DED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1E87")

    ChrTalk(
        0x8,
        (
            "If you're looking for Sandra,\x01",
            "she's right over there, dozing\x01",
            "away at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why don't you try waking her\x01",
            "up and asking?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8A")

    label("loc_1E87")

    Call(0, 21)

    label("loc_1E8A")

    Jump("loc_2E1D")

    label("loc_1E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F5F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EAC")
    Call(0, 7)
    Jump("loc_1F5A")

    label("loc_1EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1EBD")
    Call(0, 7)
    Jump("loc_1F5A")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1F57")

    ChrTalk(
        0x8,
        (
            "If you're looking for Sandra,\x01",
            "she's right over there, dozing\x01",
            "away at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Why don't you try waking her\x01",
            "up and asking?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5A")

    label("loc_1F57")

    Call(0, 7)

    label("loc_1F5A")

    Jump("loc_2E1D")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(
        0x8,
        "You all customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hold on a few minutes, please.\x01",
            "We're just about to open up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2051")

    label("loc_1FCF")


    ChrTalk(
        0x8,
        "We'll open our doors in just a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've got to call for our performers and\x01",
            "prepare all of our speciality cocktails.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2051")

    Jump("loc_2E1D")

    label("loc_2056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_234D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228F")

    ChrTalk(
        0x8,
        (
            "Been hearing some dangerous rumors\x01",
            "float around these parts lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Apparently, Heiyue's been blockading\x01",
            "Revache's smuggling routes.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2181")

    ChrTalk(
        0x101,
        "#0000FSeriously? Are you absolutely sure?\x02",
    )

    CloseMessageWindow()
    Jump("loc_21A3")

    label("loc_2181")


    ChrTalk(
        0x101,
        "#0000FWhere'd you hear that?\x02",
    )

    CloseMessageWindow()

    label("loc_21A3")


    ChrTalk(
        0x8,
        "Eh, don't worry about it. It's just a rumor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But it sounds like they've been strategically\x01",
            "breaking down their opponent outside of\x01",
            "the public eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to that, not even the bracers\x01",
            "can lay their hands on them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2348")

    label("loc_228F")


    ChrTalk(
        0x8,
        (
            "Heiyue is definitely crafty, considering how\x01",
            "they've managed to outmaneuver everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know the details, but several of Revache's\x01",
            "smuggling routes have been shut down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2348")

    Jump("loc_2E1D")

    label("loc_234D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2414")

    ChrTalk(
        0x8,
        (
            "Usually, Revache wouldn't cock their head\x01",
            "towards something like last month's incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Guys in that kind of business probably just\x01",
            "write it off as an inevitability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2552")

    label("loc_2414")


    ChrTalk(
        0x8,
        (
            "After last month's incident, it'd be\x01",
            "an understatement to say that all\x01",
            "of Revache was in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I even heard that they stooped to\x01",
            "chewing out some of their managers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, Revache's roots still spread\x01",
            "all throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not like they should be scared\x01",
            "by a little mistake like that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2552")

    Jump("loc_2E1D")

    label("loc_2557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_263B")

    ChrTalk(
        0x8,
        (
            "Hmm. Word is that a group of Easterners,\x01",
            "Heiyue, have started laundering mira\x01",
            "throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Revache IS one of Crossbell's\x01",
            "biggest trade companies. I doubt\x01",
            "they'll let this slide for long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2754")

    label("loc_263B")


    ChrTalk(
        0x8,
        (
            "Hmm. Word is that group of Easterners,\x01",
            "Heiyue, has started laundering mira\x01",
            "throughout the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heiyue's been trying their damned\x01",
            "hardest to push Revache's buttons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Given how things stand, it's only\x01",
            "a matter of time before an all-out\x01",
            "war breaks out between them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2754")

    Jump("loc_2E1D")

    label("loc_2759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_28AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2818")

    ChrTalk(
        0x8,
        (
            "Ignoring our customers' professions... I still wish\x01",
            "they'd refrain from causing trouble for Garante.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't want them doing anything\x01",
            "to ruin our reputation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A8")

    label("loc_2818")


    ChrTalk(
        0x8,
        (
            "Really? We got a barker\x01",
            "parked in front of our door?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Geez, what a pain...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're an honest business with\x01",
            "a license to operate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_28A8")

    Jump("loc_2E1D")

    label("loc_28AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_297F")

    ChrTalk(
        0x8,
        (
            "Garante's policy is to not interfere with\x01",
            "our customers' personal matters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I suppose that's why everyone's lips tend\x01",
            "to get looser when they step inside...\x01",
            "That's all I'll say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AEB")

    label("loc_297F")


    ChrTalk(
        0x8,
        (
            "A few of our customers got a little too\x01",
            "drunk recently and started talking about\x01",
            "a screwed-up job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "They mentioned something about downtown...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh* It'd be better if they didn't talk\x01",
            "where other people could hear them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWere they members of Revache?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Who knows?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But we get a lot of customers like that,\x01",
            "to tell you the truth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2AEB")

    Jump("loc_2E1D")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BCB")

    ChrTalk(
        0x8,
        (
            "Revache has been strengthening their forces\x01",
            "lately to get a leg up on everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "More specifically, their big rival group...\x01",
            "Well, so the rumor goes. I don't know\x01",
            "the finer details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFB")

    label("loc_2BCB")


    ChrTalk(
        0x8,
        (
            "In the past couple of days, Revache & Co. has\x01",
            "been deploying members all over Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Some customers have claimed they're buying\x01",
            "up all the weapons and vehicles they can find,\x01",
            "but I don't know what that entails...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "After all, that was just a rumor spread\x01",
            "by some talkative customers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CFB")

    Jump("loc_2E1D")

    label("loc_2D00")


    ChrTalk(
        0x8,
        "You in the mood for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FOrange juice, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sorry, kid. We don't have any juice.\x02",
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
        0x102,
        (
            "#0100FTio, it'd be best to go somewhere else.\x01",
            "After all, this is more of an adult location...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1D")

    Jump("loc_85F")

    label("loc_2E22")

    TalkEnd(0x8)
    Return()

    # Function_5_7FC end

    def Function_6_2E26(): pass

    label("Function_6_2E26")


    ChrTalk(
        0x8,
        (
            "Sandra sure loves to sit in here\x01",
            "and waste the day away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Our motto has been to never pry into our\x01",
            "customers' business, but maybe that's\x01",
            "done us more harm than good.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_6_2E26 end

    def Function_7_2ED8(): pass

    label("Function_7_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312E")

    ChrTalk(
        0x8,
        "Welcome to Garante.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Remember, we aren't an information\x01",
            "agency. We only deal in cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FUm... How about a Yin-flavored\x01",
            "cocktail, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    ChrTalk(
        0x8,
        (
            "Haha, clever. Heiyue's very own\x01",
            "Cao Lee is certainly cunning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He utilizes his intellect to corner his opponents,\x01",
            "leaving that enigmatic assassin of his to clean\x01",
            "up the mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even Revache's Garcia Rossi had\x01",
            "trouble dealing with Heiyue's\x01",
            "pincer attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And that's as far as\x01",
            "I'm willing to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(I-I can't believe that worked...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(So he knows about it, eh...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 0)
    Jump("loc_3241")

    label("loc_312E")


    ChrTalk(
        0x8,
        (
            "Haha, clever. Heiyue's very own\x01",
            "Cao Lee is certainly cunning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He utilizes his intellect to corner his opponents,\x01",
            "leaving that enigmatic assassin of his to clean\x01",
            "up the mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Geez, gives me the creeps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right, you want to order\x01",
            "something while you're here?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3241")

    Return()

    # Function_7_2ED8 end

    def Function_8_3242(): pass

    label("Function_8_3242")


    ChrTalk(
        0x8,
        "You need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sorry. We're not open yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOh, this looks like some\x01",
            "kind of jazz bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Right you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FPlace has a good selection of drinks.\x01",
            "It's pretty popular 'round here, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSo this is the jazz bar Garante?\x02\x03",
            "#0000F(Wait a second... I think I remember my\x01",
            "brother mentioning this place...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "Well, I'm not so cold as to give exhausted\x01",
            "customers nothing for stopping by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd be happy to whip up a cocktail or two\x01",
            "for you folks. Not for the kid, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0201FHmph...\x01",
            "(So I am the only one\x01",
            "left out, is that right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 0)
    Return()

    # Function_8_3242 end

    def Function_9_34A3(): pass

    label("Function_9_34A3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3537")
    Jump("loc_3581")

    label("loc_3537")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3557")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3581")

    label("loc_3557")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3577")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3581")

    label("loc_3577")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3581")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_35B4")
    Jump("loc_35DC")

    label("loc_35B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_35DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35DC")
    Call(0, 27)
    Return()

    label("loc_35DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3688")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35F8")
    Call(0, 12)
    Jump("loc_3683")

    label("loc_35F8")


    ChrTalk(
        0x9,
        "Another day of pouring wine for customers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh* What's the point of this\x01",
            "job anymore? Maybe it's time\x01",
            "for a career switch...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3683")

    Jump("loc_4608")

    label("loc_3688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_37E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3700")

    ChrTalk(
        0x9,
        (
            "Ugh. I think I may have had a little too much\x01",
            "to drink... My head is absolutely killing me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37DB")

    label("loc_3700")


    ChrTalk(
        0x9,
        "Ugh. My poor head...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I had to play along with a diet member\x01",
            "yesterday. Damn it, that was unpleasant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How many times did I have to tell him to\x01",
            "stop touching me for it to get through his\x01",
            "thick skull?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_37DB")

    Jump("loc_4608")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3847")
    OP_64(0x9)
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "Mmm... Zzz...\x01",
            "Stupid old man, stop trying to feel me up...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_4608")

    label("loc_3847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_396A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38ED")

    ChrTalk(
        0x9,
        (
            "I've got a gig with an Imperial Faction\x01",
            "diet member today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh* I don't want to see another old,\x01",
            "ugly mug for as long as I live...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3965")

    label("loc_38ED")


    ChrTalk(
        0x9,
        (
            "Eric told me to just suck it up and\x01",
            "get the job over with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Wahhh... He's been acting so cold to me lately.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3965")

    Jump("loc_4608")

    label("loc_396A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A1A")

    ChrTalk(
        0x9,
        (
            "We've been having a bunch of posh-looking\x01",
            "customers come in lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They may be generous, but they're ultra\x01",
            "stuck-up and hard to keep company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AEF")

    label("loc_3A1A")


    ChrTalk(
        0x9,
        (
            "A few of our recent customers have\x01",
            "been splurging like crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've never seen someone so generous in my life.\x01",
            "Hell, they were practically handing out mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Been lots of guys like that, lately...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3AEF")

    Jump("loc_4608")

    label("loc_3AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3BDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B57")

    ChrTalk(
        0x9,
        (
            "Maybe I'm just getting old...\x01",
            "I'm supposed to still be in my twenties.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD9")

    label("loc_3B57")


    ChrTalk(
        0x9,
        "The sun's too bright in the morning...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn it. I keep becoming more and more of\x01",
            "a night owl with each passing year.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3BD9")

    Jump("loc_4608")

    label("loc_3BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3BFB")
    Call(0, 10)
    Jump("loc_3C74")

    label("loc_3BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3C71")
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    ChrTalk(
        0x9,
        (
            "Mmmm...\x01",
            "Umm... Zzz... Mmmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lemme sleep a bit longer...Eric...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_3C74")

    label("loc_3C71")

    Call(0, 10)

    label("loc_3C74")

    Jump("loc_4608")

    label("loc_3C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C96")
    Call(0, 11)
    Jump("loc_3D0B")

    label("loc_3C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_3CA7")
    Call(0, 11)
    Jump("loc_3D0B")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3D08")
    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "Mmmm...\x01",
            "Umm... Zzz... Mmmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Lemme sleep a bit longer...Eric...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D0B")

    label("loc_3D08")

    Call(0, 11)

    label("loc_3D0B")

    Jump("loc_4608")

    label("loc_3D10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D60")

    ChrTalk(
        0x9,
        (
            "Why can't my customers all\x01",
            "be dashing young men...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDB")

    label("loc_3D60")


    ChrTalk(
        0x9,
        "Almost time for work again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ugh, do I really have to?! I can't handle\x01",
            "keeping ugly codgers company again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3DDB")

    Jump("loc_4608")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3E48")

    ChrTalk(
        0x9,
        "It's naptime for us hostesses!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, just leave me alone.\x01",
            "Lemme sleep...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EA8")

    label("loc_3E48")


    ChrTalk(
        0x9,
        (
            "I've already told you\x01",
            "everything I know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, just leave me alone.\x01",
            "Lemme sleep...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3EA8")

    Jump("loc_4608")

    label("loc_3EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_40B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F6F")

    ChrTalk(
        0x9,
        (
            "Eric is calm and collected, regardless\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He doesn't even break a sweat when\x01",
            "serving cocktails to Revache's goons...\x01",
            "I think I'm falling for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40AD")

    label("loc_3F6F")


    ChrTalk(
        0x9,
        (
            "Those goons from Revache came by\x01",
            "for some drinks again yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Something had them in a real foul mood.\x01",
            "It was pretty obvious, considering they\x01",
            "couldn't seem to stop bitching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I think they said something along the lines of,\x01",
            "'Screw those police brats...'\x01",
            "I guess they ran into some sort of trouble?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_40AD")

    Jump("loc_4608")

    label("loc_40B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_420A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_412E")

    ChrTalk(
        0x9,
        (
            "Sounds like the leaders of the Republican Faction\x01",
            "have been doing well for themselves recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4205")

    label("loc_412E")


    ChrTalk(
        0x9,
        (
            "Last night, I was assigned with entertaining\x01",
            "some Republican Faction bigwig.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's great and all that they're rich, but man,\x01",
            "I'm beat. Maybe I'll go recharge by soaking\x01",
            "in Eric's beautiful, calm face...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4205")

    Jump("loc_4608")

    label("loc_420A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4357")

    ChrTalk(
        0x9,
        (
            "I've been seeing this dreamy-looking young\x01",
            "guy pop up in the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He was kinda mysterious and cool looking.\x01",
            "Not to mention, he had this whole\x01",
            "androgynous look going for him. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's always with some wealthy lady,\x01",
            "so I haven't been able to make a move.\x01",
            "Y'know, I wonder if he's a host.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4608")

    label("loc_4357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43D3")

    ChrTalk(
        0x9,
        (
            "Work's been getting harder and harder\x01",
            "these days. Or maybe, I'm just getting\x01",
            "older and older...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_442D")

    label("loc_43D3")


    ChrTalk(
        0x9,
        "Wha? It's morning already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uuugh, lemme sleep in...\x01",
            "Just a few more minutes!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_442D")

    Jump("loc_4608")

    label("loc_4432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4580")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44AA")

    ChrTalk(
        0x9,
        (
            "Lemme tell you, Eric is a beauty.\x01",
            "Not to mention, super cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ah, I'm fully recharged!\x02",
    )

    CloseMessageWindow()
    Jump("loc_457B")

    label("loc_44AA")


    ChrTalk(
        0x9,
        (
            "Even those goons from Revache\x01",
            "drink here every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's how that brooding bartender\x01",
            "over there gets all of his info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, I feel positively recharged\x01",
            "by that dashing face of his!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_457B")

    Jump("loc_4608")

    label("loc_4580")

    SetChrSubChip(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "That dirty codger! Can't he\x01",
            "keep his hands to himself?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Geez, I'm exhausted... Being a\x01",
            "hostess isn't as easy as it looks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4608")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_34A3 end

    def Function_10_4610(): pass

    label("Function_10_4610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4667")

    ChrTalk(
        0x9,
        "Waaaahh. Eric's a meanie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Who ish drunk off dere ass, huuh?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_47C9")

    label("loc_4667")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x2)

    ChrTalk(
        0x9,
        (
            "Heeeeeey, Eriiiiic...\x01",
            "Gimme another drink...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#3PExcuse me, Sandra. What happened\x01",
            "to going home and getting some sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PIt's already the middle of the afternoon, woman!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_47BB")

    ChrTalk(
        0x101,
        "#0000F(She's still drinking...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I am concerned that this person may have\x01",
            "forgotten the concept of happiness.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BB")

    SetScenarioFlags(0x0, 1)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)

    label("loc_47C9")

    Return()

    # Function_10_4610 end

    def Function_11_47CA(): pass

    label("Function_11_47CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4830")

    ChrTalk(
        0x9,
        (
            "Psshh, the Anniversary Festival can go die\x01",
            "in a hole for all I care! *glug* *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A27")

    label("loc_4830")


    ChrTalk(
        0x9,
        (
            "The Anniversary Festival is almost here...\x01",
            "I bet everyone's looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn it, that pisses me off. Hostesses\x01",
            "have it rough during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Treating customers to drinks from morning till night,\x01",
            "giving cutesy responses, putting on fake smiles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Just the thought of it depresses me...\x01",
            "Geez, I can't take much more of this. *glug*\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A24")

    ChrTalk(
        0x101,
        "#0000F(She's still drinking...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I am concerned that this person may\x01",
            "have lost the concept of happiness.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A24")

    SetScenarioFlags(0x0, 1)

    label("loc_4A27")

    Return()

    # Function_11_47CA end

    def Function_12_4A28(): pass

    label("Function_12_4A28")


    ChrTalk(
        0xFE,
        (
            "Huh, evening already? Guess it's\x01",
            "almost time for my personal hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I guess I'll teach you\x01",
            "something good today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This cocktail was taught to me\x01",
            "by a customer some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that one day I'll drink a\x01",
            "cocktail as great as that one...\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D6),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x18)
    Return()

    # Function_12_4A28 end

    def Function_13_4BB0(): pass

    label("Function_13_4BB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D13")

    ChrTalk(
        0x101,
        "#0000FLong time no see, Detective Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#0601F...\x02\x03",
            "#0603FIt's you troublemakers again...\x01",
            "Don't get in the way of our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Whew, he's definitely givin' off that\x01",
            "'Don't talk to me. I'm pissed' kinda vibe.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(We might have caused even more problems\x01",
            "for him by interfering with the auction...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4D9D")

    label("loc_4D13")


    ChrTalk(
        0xFE,
        (
            "#0603FTrust me, you four have\x01",
            "meddled in this quite enough.\x02\x03",
            "#0601FDo us all a favor and try to keep\x01",
            "the grandstanding to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9D")

    TalkEnd(0xFE)
    Return()

    # Function_13_4BB0 end

    def Function_14_4DA1(): pass

    label("Function_14_4DA1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The First Division is in the middle\x01",
            "of an extremely important case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You kids in the SSS have no business\x01",
            "being anywhere near it. Got it?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_4DA1 end

    def Function_15_4E3B(): pass

    label("Function_15_4E3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4EB8")

    ChrTalk(
        0xFE,
        (
            "Sources say this bar is frequently\x01",
            "used by Revache's members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "All right, let's see what we can dig up!\x02",
    )

    CloseMessageWindow()

    label("loc_4EB8")

    TalkEnd(0xFE)
    Return()

    # Function_15_4E3B end

    def Function_16_4EBC(): pass

    label("Function_16_4EBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4F03")

    ChrTalk(
        0xFE,
        (
            "Hmmm... I don't mesh well\x01",
            "with these kinds of places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F03")

    TalkEnd(0xFE)
    Return()

    # Function_16_4EBC end

    def Function_17_4F07(): pass

    label("Function_17_4F07")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F9B")
    Jump("loc_4FE5")

    label("loc_4F9B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4FBB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FE5")

    label("loc_4FBB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FDB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FE5")

    label("loc_4FDB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FE5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_50F0")

    ChrTalk(
        0xC,
        (
            "*sigh* Is it time for me to mosey on over\x01",
            "to the casino today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. It doesn't matter.\x01",
            "Win or lose, it's all just a game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And besides, I've gotta end the Anniversary\x01",
            "Festival with a bang. So why not?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_537B")

    label("loc_50F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_517F")

    ChrTalk(
        0xC,
        (
            "Seventy years since Crossbell\x01",
            "State was founded, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sounds like this celebration\x01",
            "calls for some wine, and lots of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_537B")

    label("loc_517F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_530D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_520B")

    ChrTalk(
        0xC,
        (
            "Last month, I heard Mayor MacDowell\x01",
            "had a little date with danger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Haha. Good to see he's still kicking.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5308")

    label("loc_520B")


    ChrTalk(
        0xC,
        (
            "There's apparently some international\x01",
            "symposium being held in Crossbell\x01",
            "alongside all the festival attractions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It was originally Mayor MacDowell's\x01",
            "idea to host it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He might be getting up there in\x01",
            "years, but he's still full of energy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5308")

    Jump("loc_537B")

    label("loc_530D")


    ChrTalk(
        0xC,
        "Mmm, this wine is to die for...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The bartender's a little distant, but I\x01",
            "do enjoy this place's vibe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_537B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_4F07 end

    def Function_18_5383(): pass

    label("Function_18_5383")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Well, I guess I'll start off with a drink.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As they say, the night is young! Hahaha!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_5383 end

    def Function_19_53E8(): pass

    label("Function_19_53E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_547C")
    Jump("loc_54C6")

    label("loc_547C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_549C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_54C6")

    label("loc_549C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_54C6")

    label("loc_54BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5595")

    ChrTalk(
        0xFE,
        "*glug* *glug*...Aaaaaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, their president sure is taking his\x01",
            "sweet, sweet time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Even after I offered to pay for all this service.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_562F")

    label("loc_5595")


    ChrTalk(
        0xFE,
        (
            "The president of that one trading company\x01",
            "was supposed to come today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? What do you guys want?\x01",
            "I'm kinda in the middle of something, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_53E8 end

    def Function_20_5637(): pass

    label("Function_20_5637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_564D")
    Call(0, 29)
    Jump("loc_5CB0")

    label("loc_564D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5CA7")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56EA")
    Jump("loc_5734")

    label("loc_56EA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_570A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5734")

    label("loc_570A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_572A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5734")

    label("loc_572A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5734")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B17")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0x11,
        (
            "#2106F...\x02\x03",
            "It's finally the last day of\x01",
            "the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FGrace?\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_586F")
    Jump("loc_58B9")

    label("loc_586F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_588F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B9")

    label("loc_588F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58AF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B9")

    label("loc_58AF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x11,
        (
            "#2105FOh...it's my little ducklings.\x02\x03",
            "#2102FGeez, you startled me...\x01",
            "Cut me some slack here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FHaha, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FDid they give you time off for the last\x01",
            "day of the festival, too, Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2109FHah, as if. I was just taking a\x01",
            "teensy little break.\x02\x03",
            "#2100FAnd besides, I'm covering the big\x01",
            "closing ceremony this evening.\x02\x03",
            "#2104FTruth be told, I've been itchin' to research\x01",
            "an entirely different place tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0013FA different place...?\x01",
            "(Don't tell me...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(She must be aware of the\x01",
            "auction's existence as well.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 4)
    Jump("loc_5C9B")

    label("loc_5B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BFB")

    ChrTalk(
        0x11,
        (
            "#2100FOh, that reminds me. When you've taken\x01",
            "enough photos for the request, just scurry\x01",
            "on over to the CNS reception desk.\x02\x03",
            "#2109FYour deadline is fast approaching,\x01",
            "so don't let me down! ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_5C9B")

    label("loc_5BFB")


    ChrTalk(
        0x11,
        (
            "#2104FAt any rate, I was a little caught\x01",
            "off guard.\x02\x03",
            "#2100FThe voice is completely different,\x01",
            "but the tone itself sounds familiar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5C9B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_5CB0")

    label("loc_5CA7")

    TalkBegin(0xFE)
    Call(0, 21)
    TalkEnd(0xFE)

    label("loc_5CB0")

    Return()

    # Function_20_5637 end

    def Function_21_5CB1(): pass

    label("Function_21_5CB1")

    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5D56")

    ChrTalk(
        0x11,
        (
            "#2100FWow, isn't that store a little bit\x01",
            "TOO expensive?!\x02\x03",
            "You think they jacked up their prices?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, I'm not the best person to ask...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6079")

    label("loc_5D56")


    ChrTalk(
        0x11,
        (
            "#2105FOoooh, is that right?\x02\x03",
            "#2109FWell? Got anything else for me?!\x01",
            "Any details about that store all those\x01",
            "traders go to for 'entertainment'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, right. That's been the\x01",
            "talk of the town lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've heard it moved here from the\x01",
            "Empire's capital about half a year ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2105FWHAT?! You're talking about THE Neue Blanc?!\x02\x03",
            "It's only the finest club in all of Crossbell,\x01",
            "complete with the best hostesses money can buy!\x02\x03",
            "#2109FOh, how exciting! I'm definitely going to\x01",
            "hit it up when I'm less busy!\x02",
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
        "#0000F(Is Grace out collecting info again...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Prancin' around all cheery like that...\x01",
            "Is it all an act or is that seriously her?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(Probably a bit of both.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_6079")

    OP_4C(0x8, 0xFF)
    Return()

    # Function_21_5CB1 end

    def Function_22_607E(): pass

    label("Function_22_607E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611B")
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

    label("loc_611B")

    Return()

    # Function_22_607E end

    def Function_23_611C(): pass

    label("Function_23_611C")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff* *sniff*\x02\x03",
            "Grrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FNo good?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_23_611C end

    def Function_24_615C(): pass

    label("Function_24_615C")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff* *sniff*\x02\x03",
            "Grrrr...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThere does not appear to be a trace\x01",
            "around here, according to Zeit.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_24_615C end

    def Function_25_61D7(): pass

    label("Function_25_61D7")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff* *sniff*\x02\x03",
            "Woof!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FIt's a hit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FZeit claims that the vice commissioner\x01",
            "must have sat here to drink.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x7)
    TalkEnd(0xFF)
    Return()

    # Function_25_61D7 end

    def Function_26_6293(): pass

    label("Function_26_6293")

    EventBegin(0x0)
    Fade(500)
    OP_68(-120, 1430, 4230, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -1070, 0, 4440, 45)
    SetChrPos(0x103, -470, 0, 2890, 359)
    SetChrPos(0x11C, -1680, 0, 2890, 45)
    TurnDirection(0x8, 0x101, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11PWelcome to Garante.\x01",
            "Can I help you with something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FI have a potentially...awkward question. Did you\x01",
            "happen to see Vice Commissioner Pierre from the\x01",
            "CPD here last night?\x02\x03",
            "#0003FHe's a bit on the shorter side.\x01",
            "Has a face like a fox...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, you must be talking about Pierre.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHe stopped by for a little while last night.\x01",
            "It looked to me like he was dead drunk\x01",
            "already, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FThe vice commissioner seems to have\x01",
            "misplaced his wedding ring.\x02\x03",
            "#0200FDo you have any idea as\x01",
            "to where he lost it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PNot in the slightest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FI-I see...\x01",
            "(Talk about being blunt...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNow that I think about it... He was\x01",
            "really throwing a fit about his wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PEven talked about leaving her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11POn top of that, he kept trying to\x01",
            "hit on a hostess all night.\x02",
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
        "#6P#0006FI, uh, definitely didn't see this coming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0203FAn unexpected development.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe hostess I'm talking about is Sandra.\x01",
            "She's sitting at the counter over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWhy don't you try asking her\x01",
            "about it yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood idea...\x02\x03",
            "#0003F(Did he still have his wedding ring\x01",
            "on when he was here? We should\x01",
            "try to confirm that with Sandra.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -1070, 0, 4440, 45)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x15, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_26_6293 end

    def Function_27_680E(): pass

    label("Function_27_680E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5160, 1430, 3850, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)
    SetChrPos(0x101, -5730, 0, 4480, 90)
    SetChrPos(0x103, -5700, 0, 3490, 45)
    SetChrPos(0x11C, -6960, 0, 2880, 45)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FUm, excuse me.\x01",
            "We're with the Crossbell Police--\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#12PUuuughh... Zzz... Mmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PLemme shleep, Eric...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        "#5P#0200FShe appears to be asleep...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0006FGuess we have no other choice...\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd shook the woman's shoulder.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#0001FEXCUSE ME, MA'AM! We're with\x01",
            "the Crossbell police!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    ChrTalk(
        0x9,
        "#12PMmm... Geez, whadda ya want?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FSorry to ruin your sleep, but there's\x01",
            "something we need to ask you.\x02\x03",
            "#0001FWe heard you spent some time with\x01",
            "Vice Commissioner Pierre last night...\x02\x03",
            "Do you remember if he was wearing\x01",
            "his wedding ring at the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PVysh comnishiner? Ah, that fawx-fayshd\x01",
            "weirdo who kept tryna hit on me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P*hic* I told him that I only like young men,\x01",
            "and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PHe went and blurted out that I'm gorgeoush,\x01",
            "that ol' geezer did!!\x02",
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
        "#5P#0006FShe's too drunk. I doubt this will get us anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FAnalyzing the situation, it appears as if\x01",
            "she just kept drinking the night away...\x01",
            "She reeks of too much alcohol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PBeshides, that guy treated me\x01",
            "to a tonna drinksh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PNot to menshion, he grabbed my\x01",
            "hand and fell to his kneesh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PClaimin' that he'd leave hish wife and\x01",
            "we'd be togetha forever and shtuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F(I'm really not sure how much more\x01",
            "of this I can take... Can we leave yet?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200F(Yes, attempting to coerce any more\x01",
            "information may prove fruitless...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12PHold onna shecond, didn't he\x01",
            "gimme shomethin' before he left?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#0005FHe gave you something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12POh, thish is it.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received \x07\x02",
            "#16ICarnelia Wedding Ring\x07\x00",
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x9,
        (
            "#12P'A preshent for a beautiful maiden!'\x01",
            "and sho on, he told me. I kept inshistin'\x01",
            "that he washn't my type at all, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12PYou kids can keep it. *hic*\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#5P#0200FThis was not how I anticipated\x01",
            "we would find the missing ring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0011FVice Commissioner Pierre...you didn't even\x01",
            "drop it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#12PUmmm, is shomethin' wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11C,
        (
            "#5P#1203FGrrrr...\x01",
            "(Hmph, what a disappointing finale.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 2)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_680E end

    def Function_28_7183(): pass

    label("Function_28_7183")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02502.itc", 0x1E)
    LoadChrToIndex("chr/ch08602.itc", 0x1F)
    LoadChrToIndex("apl/ch50091.itc", 0x20)
    SetChrPos(0x0, -5780, 0, 1780, 142)
    SetChrPos(0x1, -5780, 0, 1780, 142)
    SetChrPos(0x2, -5780, 0, 1780, 142)
    SetChrPos(0x3, -5780, 0, 1780, 142)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x16)
    SetChrPos(0x16, -5800, 0, 4250, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -5800, 80, 4450, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, -6900, 80, 4450, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5800, 500, 5300, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -3800, 0, 6400, 180)
    FadeToBright(2000, 0)
    OP_68(-13480, 1830, 5770, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(410, 0)
    SetCameraDistance(25500, 0)
    OP_68(-6040, 1430, 4480, 10000)
    MoveCamera(297, 16, 0, 10000)
    OP_6E(310, 10000)
    SetCameraDistance(25500, 10000)
    Sleep(9000)
    SetChrSubChip(0x13, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_7183 end

    def Function_29_734A(): pass

    label("Function_29_734A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-8000, 1200, 500, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -8000, 0, 1400, 180)
    SetChrPos(0x102, -6800, 0, 1500, 225)
    SetChrPos(0x103, -8400, 0, 2800, 180)
    SetChrPos(0x104, -9500, 0, 2100, 135)
    SetChrPos(0x11, -8400, 100, -500, 90)
    SetChrSubChip(0x11, 0x1)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#4200317V#6P#2102FOh, look who's finally arrived.\x02\x03",
            "#4200318V#2109FSudden, I know, but do you all have any tidbits\x01",
            "about the Heiyue raid you're willing to share?\x02\x03",
            "#4200319VI'm sure Cao showered you with all sorts\x01",
            "of delightful details over at his office.\x02",
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
        "#4200320V#0006F#11PQuick to the punch, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200321V#11P#0211FActually, how were you even\x01",
            "aware we visited Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200322V#6P#2106FWell, if you must know, I found out this morning.\x01",
            "As I was about to interro--I mean...ask Cao some\x01",
            "questions, I saw ol' Duddles barge in.\x02\x03",
            "#4200323V#2105FRight as I was wondering, 'What's up with that?'\x01",
            "you all entered after him.\x02\x03",
            "#4200324V#2100FThen, once Dudley left with his partner and that\x01",
            "classic scowl on his face, you came out looking\x01",
            "mighty worried.\x02\x03",
            "#4200325V#2109FWith that kinda look covering your mug, I'd be\x01",
            "shocked if you DIDN'T hear anything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200326V#0001F#11PYou're deceptively sharp...\x01",
            "Were we that obvious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200327V#12P#0101FStill, Grace, I think you know better than\x01",
            "anyone that we can't casually disclose\x01",
            "information about an open investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200328V#6P#2109FOf course I know that, you silly goose!\x01",
            "That's why I proposed a bit of give-and-take.\x02\x03",
            "#4200329V#2102FAfter all, aren't you dying for some details\x01",
            "on Garcia Rossi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200330V#0005F#11PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200331V#5P#0306FAlways the pro at danglin' the\x01",
            "bait right under our noses, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200332V#6P#2100FTo put the cherry on top, I might have some\x01",
            "news about that so-called 'auction,' too...\x02\x03",
            "#4200333V#2104FWhispers say Revache screwed the pooch\x01",
            "and incurred the wrath of the speaker...\x02\x03",
            "#4200334V#2102FSurely you want to know how these two\x01",
            "matters might be related? No?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200335V#0006F#11P*sigh* All right, I'll bite.\x02\x03",
            "#4200336V#0013FHowever, everything about Cao\x01",
            "is strictly off the record, got it?\x02\x03",
            "#4200337VI can't stress that enough, Grace.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50091.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(806)
    OP_68(-7510, 800, -380, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(18450, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -7000, 100, -2050, 0)
    SetChrPos(0x102, -5800, 100, -2050, 0)
    SetChrPos(0x103, -4600, 100, -2050, 0)
    SetChrPos(0x104, -3100, 100, -500, 270)
    SetChrPos(0x11, -8400, 100, -500, 90)
    SetChrSubChip(0x11, 0x2)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x5)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -7200, 300, -500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    SetCameraDistance(19450, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x11,
        (
            "#4200338V#5P#2101FHmmm... I see.\x02\x03",
            "#4200339V#2106FSo, the situation is more\x01",
            "dire than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200340V#6P#0003FYeah... Unfortunately, it is.\x02\x03",
            "#4200341V#0001FAs things stand, both groups seem\x01",
            "to be trying not to involve the public,\x01",
            "if that's any consolation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200342V#5P#2101FWell, no matter which way you cut it, this raid\x01",
            "was too abrupt.\x02\x03",
            "#4200343VIgnoring that it happened in the dead of night,\x01",
            "a raid near OUR news agency?\x02\x03",
            "#4200344V#2106FNot to mention, it was right down the street\x01",
            "from the IBC... Sounds like this decision was\x01",
            "a little rushed, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200345V#6P#0106FYes, that's true...\x02\x03",
            "#4200346V#0101FIf things went south, this incident could have\x01",
            "shaken the continent, destroying Crossbell's\x01",
            "reputation as Zemuria's trade capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200347V#5P#2100FYou have a point there.\x02\x03",
            "#4200348V#2103FHmm, that also might make the info I got\x01",
            "my mitts on not necessarily false...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200349V#6P#0205FThis information you got your hands on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200350V#6P#0001FAre you willing to share it now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200351V#5P#2100FOkay, fine. It's my turn now, eh?\x02\x03",
            "#4200352V#2103FYou see... This whole fiasco\x01",
            "originated from inside the mafia.\x02\x03",
            "#4200353V#2101FLately, I've been hearing rumors that\x01",
            "Garcia Rossi's control over his goons\x01",
            "has been, well, lacking.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4200354V#6P#0005FIs that even possible?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200355V#12P#0306FYeah, I'm having a hard time buyin' it...\x02\x03",
            "#4200356V#0301FI can't imagine subordinates defying\x01",
            "that monstrous old geezer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200357V#5P#2106FWell, you can choose to believe it or not.\x02\x03",
            "#4200358V#2101FI'm just saying, maybe it's possible that the incident\x01",
            "in the Downtown District and the gunning for Mainz's\x01",
            "rights might not have been on Garcia's orders.\x02\x03",
            "#4200359VIt seemed like some of the mafiosos on\x01",
            "the lower rungs were looking to climb up.\x02\x03",
            "#4200360VIf clout inside Revache is what those rookies\x01",
            "were after, then that would explain them stepping\x01",
            "out of line and getting busted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200361V#12P#0301FHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200362V#6P#0105FP-Please, can we back up a second?\x02\x03",
            "#4200363V#0101FYou're saying that last night's raid was carried\x01",
            "out by junior members of the mafia?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200364V#5P#2106FGiven the scale of the attack, I personally\x01",
            "lean towards no, but...\x02\x03",
            "#4200365V#2100F...considering all that's happened, you can\x01",
            "hardly blame Garcia for his big outburst\x01",
            "earlier, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200366V#12P#0308FTrue... There wasn't a sign of\x01",
            "his lil' entourage anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200367V#6P#0003FDoes that mean, despite controlling Revache\x01",
            "from the inside, he's still having issues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200368V#6P#0200FBut, what is the don doing\x01",
            "during all of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200369V#5P#2106FAccording to what I've been able to gather,\x01",
            "Marconi is desperately trying to atone for\x01",
            "his giant blunder at the auction.\x02\x03",
            "#4200370V#2101FNaturally, he's buttering up Speaker Hartmann,\x01",
            "who was left less-than-pleased at Mishelam...\x02\x03",
            "#4200371VHe's even trying to lure more influential figures\x01",
            "of Crossbell into his fold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200372V#6P#0101FInfluential figures?\x01",
            "Who exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200373V#5P#2103FCutting right to the chase. Well, simply put,\x01",
            "it's Republican Faction diet members.\x02\x03",
            "#4200374V#2101FI've heard he's met with the CGF commander, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200375V#6P#0103FReally? Is he attempting to suppress\x01",
            "Heiyue's political influence in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200376V#6P#0008FAnd maybe meeting with the CGF commander\x01",
            "is related to Revache's weapon smuggling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200377V#12P#0306FYeah, wouldn't be surprised.\x02\x03",
            "#4200378V#0301FGotta remember, that moron of a commander\x01",
            "is also one of Speaker Hartmann's cronies.\x02\x03",
            "#4200379VSince the commander is in Marconi's pocket,\x01",
            "I reckon he's usin' him to win back the\x01",
            "speaker's favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200380V#5P#2104FBingo. That's what I was thinking, too.\x02\x03",
            "#4200381V#2102FI knew a nice chat with you guys would\x01",
            "help me get all my thoughts in order!\x02\x03",
            "#4200382V#2109FHaha, score! This turned out to be a\x01",
            "fruitful little info swap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200383V#6P#0002FI hate to admit it, but it's been helpful\x01",
            "for us as well.\x02\x03",
            "#4200384V#0006FIn fact, now that we've sifted through all of\x01",
            "the details, I still feel like there's something\x01",
            "we're missing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4200385V#6P#0105FSomething we're missing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#4200386V#5P#2105FCare to elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200387V#6P#0003FWe've been able to arrive at a convincing\x01",
            "motive behind each action thus far, but...\x02\x03",
            "#4200388V...they're all haphazard, like they aren't\x01",
            "acting as one, singular organization.\x02\x03",
            "#4200389V#0008FI felt like Revache had a particular 'style'\x01",
            "to their operations, characteristic of the\x01",
            "darkness that lies in the city.\x02\x03",
            "#4200390V#0001FBut in these cases, I just don't feel it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200391V#6P#0101FSo that's what you mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200392V#5P#2101FHmm... Now that you mention it,\x01",
            "I'm inclined to agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200393V#6P#0203FAn efficient system created to take advantage\x01",
            "of the mira reserve known as Crossbell...\x02\x03",
            "#4200394V#0201FFor an organization such as Revache to deviate\x01",
            "from that system is highly irregular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200395V#12P#0308FSo in other words, there's an element to this\x01",
            "case that threw Revache out of whack...\x02\x03",
            "#4200396V#0301FSomethin' like that?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#4200397V#5P#0000FRight... It's just a gut feeling, though.\x02\x03",
            "#4200398V#0003FCao's description made it sound like these\x01",
            "raiders who attacked Heiyue possessed\x01",
            "unnatural amounts of strength, too...\x02\x03",
            "#4200399V#0001FIt's possible that could be the reason\x01",
            "behind Garcia's strange attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200400V#5P#2102FWow, I should have expected this from\x01",
            "you, Lloyd. You're a sharp kid, aren't ya?\x02\x03",
            "#4200401V#2109FHey, if you get canned, how about joining me\x01",
            "at the Crossbell Times?\x02\x03",
            "#4200402VWe can aim for the Fulitzer Prize together!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4200403V#6P#0006FUh, I'll have to pass...\x02\x03",
            "#4200404V#0013FAnd for the record, I'd appreciate it if you\x01",
            "didn't make me worry more than I have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200405V#12P#0305FRemind me again. What's the Fulitzer Prize\x01",
            "thing she's so up in arms about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200406V#6P#0100FIt's a prestigious international award given to\x01",
            "the most outstanding journalist of the year.\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#4200407V#6P#0001FExcuse me for one second.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0xB)
    OP_24(0x326)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200408V#0001FYes, this is Lloyd Bannings of\x01",
            "the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Old Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4200409V\x07\x05",
            "I managed to get through!\x01",
            "It's me, Bickson over from Mainz!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200410V\x07\x00",
            "#0000FOh, the mayor? What's going on?\x02\x03",
            "#4200411VIs there some sort of problem\x01",
            "regarding Gantz?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4200412V\x07\x05",
            "W-Well...you see...\x01",
            "I'm at that Barca Casino at the\x01",
            "moment...\x02\x03",
            "#4200413VH-He started acting strangely,\x01",
            "so I decided to call you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200414V\x07\x00",
            "#0005F'Strangely'?\x02\x03",
            "#4200415V#0001FWhat exactly do you mean?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4200416V\x07\x05",
            "He's been engaged in a poker match\x01",
            "with another customer for quite some time...\x02\x03",
            "#4200417VThe atmosphere has gotten kind of\x01",
            "severe... It might actually get violent.\x02\x03",
            "#4200418VAnyway, could you come over\x01",
            "quickly and help sort this out?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4200419V\x07\x00",
            "#0011FU-Understood, sir.\x02\x03",
            "#4200420V#0001FBarca Casino, right? We're close by,\x01",
            "so we'll be there shortly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Mayor's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4200421V\x07\x05",
            "Okay, I'm counting on you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(825, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#4200422V#6P#0101FMainz's mayor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200423V#12P#0305FYou mentioned somethin' about the\x01",
            "casino, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#4200424V#5P#0013FYeah, apparently, Gantz might be getting\x01",
            "into some sort of violent situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200425V#6P#0105FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200426V#6P#0201FDid he somehow provoke his opponent\x01",
            "during a match?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200427V#12P#0306FWith Gantz's ego and crazy luck,\x01",
            "I could totally see it happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#4200428V#5P#2103FWell, we'd better hurry on over\x01",
            "and assess the situation.\x02\x03",
            "#4200429V#2110FAll right, off to Barca we gooo!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x11,
        "#4200430V#5P#2105FWhat? What's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4200431V#6P#0109FWell, Grace, it's just that...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4200432V#5P#0006FThere's no point in telling her not to come.\x01",
            "Let's just go to the casino.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    AddParty(0x3C, 0xFF, 0xFF)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(-8000, 1430, 1200, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -8000, 0, 1200, 0)
    SetChrPos(0x1, -8000, 0, 1200, 0)
    SetChrPos(0x2, -8000, 0, 1200, 0)
    SetChrPos(0x3, -8000, 0, 1200, 0)
    SetChrPos(0x4, -8000, 0, 1200, 0)
    SetScenarioFlags(0xC2, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x4A, 0x1, 0x8)
    OP_29(0x4B, 0x1, 0x4)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_29_734A end

    SaveToFile()

Try(main)
