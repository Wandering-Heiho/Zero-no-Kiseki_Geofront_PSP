from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1410.bin",                # FileName
        "c1410",                    # MapName
        "c1410",                    # Location
        0x0075,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 117, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1410",                  # 0
        "Wazy",                   # 1
        "Abbas",                  # 2
        "Kienz",                  # 3
        "Vesse",                  # 4
        "Ryan",                   # 5
        "Azel",                   # 6
        "Wazy",                   # 7
        "Ashleigh",               # 8
        "Sarina",                 # 9
        "Geithner",               # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Glass",                  # 17
        "Glass",                  # 18
    ))

    AddCharChip((
        "chr/ch00400.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch30900.itc",                   # 02
        "chr/ch31800.itc",                   # 03
        "apl/ch50016.itc",                   # 04
        "chr/ch24500.itc",                   # 05
        "chr/ch21300.itc",                   # 06
        "chr/ch09202.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch21000.itc",                   # 09
        "chr/ch24502.itc",                   # 0A
        "chr/ch21302.itc",                   # 0B
        "chr/ch23702.itc",                   # 0C
        "chr/ch23602.itc",                   # 0D
        "apl/ch50375.itc",                   # 0E
        "apl/ch50091.itc",                   # 0F
    ))

    DeclNpc(0,       0,       11220,   135,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2980,    0,       14779,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2950,    29,      6579,    180,  261,  0x0, 0,   3,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(10229,   0,       4409,    90,   261,  0x0, 0,   2,   0,   0,   2,   0,   25,  255,  0)
    DeclNpc(14069,   0,       13409,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(12770,   0,       15310,   180,  261,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-2599,   50,      12600,   0,    261,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-479,    150,     12600,   0,    389,  0x0, 0,   7,   0,   255, 255, 0,   38,  255,  0)
    DeclNpc(0,       0,       5789,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-1269,   0,       12640,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-1240,   0,       4139,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(-170,    0,       4019,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-2900,   150,     3500,    0,    405,  0x0, 0,   10,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-4300,   150,     3500,    0,    405,  0x0, 0,   11,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(3730,    150,     12600,   0,    405,  0x0, 0,   12,  0,   255, 255, 0,   47,  255,  0)
    DeclNpc(1559,    150,     12600,   0,    405,  0x0, 0,   13,  0,   255, 255, 0,   50,  255,  0)
    DeclNpc(-2599,   519,     13449,   0,    374,  0x0, 0,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-479,    540,     13449,   0,    502,  0x0, 4,   15,  0,   255, 255, 255, 255, 255,  0)

    DeclActor(2590,    0,       13420,   1500,    2980,    1500,    14780,   0x007E, 0,  16, 0x0000)
    DeclActor(750,     0,       13420,   1500,    750,     1500,    14770,   0x007E, 0,  29, 0x0000)
    DeclActor(750,     0,       13420,   1500,    750,     1500,    14770,   0x007E, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_559",          # 02, 2
        "Function_3_632",          # 03, 3
        "Function_4_B58",          # 04, 4
        "Function_5_C17",          # 05, 5
        "Function_6_E62",          # 06, 6
        "Function_7_38BE",         # 07, 7
        "Function_8_3DB7",         # 08, 8
        "Function_9_46C3",         # 09, 9
        "Function_10_4E75",        # 0A, 10
        "Function_11_55C9",        # 0B, 11
        "Function_12_57E8",        # 0C, 12
        "Function_13_5B85",        # 0D, 13
        "Function_14_5E87",        # 0E, 14
        "Function_15_6009",        # 0F, 15
        "Function_16_702E",        # 10, 16
        "Function_17_7032",        # 11, 17
        "Function_18_714A",        # 12, 18
        "Function_19_7202",        # 13, 19
        "Function_20_7230",        # 14, 20
        "Function_21_8815",        # 15, 21
        "Function_22_88DA",        # 16, 22
        "Function_23_8989",        # 17, 23
        "Function_24_8A76",        # 18, 24
        "Function_25_92DD",        # 19, 25
        "Function_26_A7E2",        # 1A, 26
        "Function_27_A8B1",        # 1B, 27
        "Function_28_AA30",        # 1C, 28
        "Function_29_BC51",        # 1D, 29
        "Function_30_BC55",        # 1E, 30
        "Function_31_BD91",        # 1F, 31
        "Function_32_BE83",        # 20, 32
        "Function_33_BFC5",        # 21, 33
        "Function_34_C154",        # 22, 34
        "Function_35_D06A",        # 23, 35
        "Function_36_D06E",        # 24, 36
        "Function_37_D164",        # 25, 37
        "Function_38_D232",        # 26, 38
        "Function_39_D724",        # 27, 39
        "Function_40_D7D3",        # 28, 40
        "Function_41_DACB",        # 29, 41
        "Function_42_DBD3",        # 2A, 42
        "Function_43_DC7E",        # 2B, 43
        "Function_44_DD8C",        # 2C, 44
        "Function_45_DE27",        # 2D, 45
        "Function_46_DEBC",        # 2E, 46
        "Function_47_DFCA",        # 2F, 47
        "Function_48_E0DB",        # 30, 48
        "Function_49_E1B6",        # 31, 49
        "Function_50_E2B6",        # 32, 50
        "Function_51_E41F",        # 33, 51
        "Function_52_11B89",       # 34, 52
        "Function_53_11BFC",       # 35, 53
        "Function_54_11C6F",       # 36, 54
        "Function_55_11CE2",       # 37, 55
        "Function_56_12CEB",       # 38, 56
        "Function_57_130B1",       # 39, 57
        "Function_58_130E1",       # 3A, 58
        "Function_59_13111",       # 3B, 59
        "Function_60_13155",       # 3C, 60
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_558")
    OP_95(0xFE, 2970, 30, 4200, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(5500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    OP_95(0xFE, 6630, 30, 6580, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Sleep(8500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    Jump("Function_1_4E4")

    label("loc_558")

    Return()

    # Function_1_4E4 end

    def Function_2_559(): pass

    label("Function_2_559")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_631")
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 6340, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 5070, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    Jump("Function_2_559")

    label("loc_631")

    Return()

    # Function_2_559 end

    def Function_3_632(): pass

    label("Function_3_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_648")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_667")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_675")
    Jump("loc_B57")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6CD")
    SetChrPos(0xC, 1070, 0, 15400, 270)
    SetChrPos(0xD, -300, 0, 15400, 90)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4")
    SetChrFlags(0xD, 0x10)

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_6C8")

    Jump("loc_B57")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6E0")
    SetChrFlags(0xD, 0x80)
    Jump("loc_B57")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6FF")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0xF, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7AB")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0xC, 10230, 0, 4410, 90)
    SetChrPos(0x11, 2950, 30, 6580, 180)
    BeginChrThread(0xC, 0, 0, 2)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_B57")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_85E")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0xA, -1730, 0, 6920, 0)
    SetChrPos(0xC, 750, 0, 14770, 180)
    SetChrPos(0x11, 2950, 30, 6580, 180)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x12, -2600, 0, 10330, 0)
    SetChrPos(0x13, -1200, 0, 10360, 315)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x11, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859")
    SetChrFlags(0x11, 0x10)

    label("loc_859")

    Jump("loc_B57")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_91D")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xA, 0, 0, 7400, 180)
    SetChrPos(0xB, 1000, 0, 7720, 225)
    SetChrPos(0xC, 750, 0, 14770, 180)
    SetChrPos(0x12, 0, 0, 5790, 0)
    SetChrPos(0x13, 680, 0, 5200, 0)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x10)

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_918")
    SetChrFlags(0x11, 0x10)

    label("loc_918")

    Jump("loc_B57")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_955")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0xD, 750, 0, 14770, 180)
    Jump("loc_B57")

    label("loc_955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_986")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_B57")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A26")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 1160, 0, 10170, 315)
    SetChrPos(0xA, 2840, 30, 8000, 270)
    SetChrPos(0xB, 1350, 0, 8000, 90)
    SetChrPos(0xC, -750, 0, 7000, 0)
    SetChrPos(0xD, -750, 0, 8500, 180)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A0D")
    SetChrFlags(0x8, 0x10)

    label("loc_A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_A21")

    Jump("loc_B57")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A45")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AB3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0xF, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AAE")
    SetChrPos(0x9, -4000, 0, 16690, 0)
    SetChrPos(0xD, -350, 0, 14760, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE")
    SetChrFlags(0xD, 0x10)

    label("loc_AAE")

    Jump("loc_B57")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_AD2")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AF1")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B1E")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0xD, 0, 0, 7400, 180)
    SetChrChipByIndex(0xD, 0x2)
    Jump("loc_B57")

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B30")
    SetChrChipByIndex(0xD, 0x2)
    Jump("loc_B57")

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B52")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4D")
    SetChrFlags(0xA, 0x10)

    label("loc_B4D")

    Jump("loc_B57")

    label("loc_B52")

    SetChrFlags(0xD, 0x80)

    label("loc_B57")

    Return()

    # Function_3_632 end

    def Function_4_B58(): pass

    label("Function_4_B58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_B77")

    label("loc_B71")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_B77")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B8D")
    Jump("loc_C16")

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BA3")
    OP_65(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_C16")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BB9")
    OP_65(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_C16")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BCB")
    OP_66(0x2, 0x1)
    Jump("loc_C16")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_BDD")
    OP_65(0x0, 0x1)
    Jump("loc_C16")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BEF")
    OP_65(0x0, 0x1)
    Jump("loc_C16")

    label("loc_BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BFD")
    Jump("loc_C16")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C16")
    OP_65(0x0, 0x1)

    label("loc_C16")

    Return()

    # Function_4_B58 end

    def Function_5_C17(): pass

    label("Function_5_C17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CDE")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "#0404FWe've got a rare opportunity to check it out,\x01",
            "Abbas. Shall we depart after our toast?\x02\x03",
            "#0400FHeh. After all, this festival is meant to\x01",
            "praise Crossbell's virtues.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_E5E")

    label("loc_CDE")


    ChrTalk(
        0x8,
        (
            "#0404FIt would be a swell idea to go check out\x01",
            "the Anniversary Festival with everyone.\x02\x03",
            "#0400FWhat about you guys? Wanna come with?\x01",
            "I bet it'd be pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSorry, we can't. We're on duty right now.\x02\x03",
            "#0001FActually, I'm pretty sure you invited us\x01",
            "knowing that full well, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0409FAhahaha! Caught red-handed. You guys\x01",
            "are too by-the-book.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_E5E")

    TalkEnd(0xFE)
    Return()

    # Function_5_C17 end

    def Function_6_E62(): pass

    label("Function_6_E62")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EF6")
    Jump("loc_F40")

    label("loc_EF6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F16")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F40")

    label("loc_F16")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F36")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F40")

    label("loc_F36")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F40")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1031")

    ChrTalk(
        0xE,
        (
            "#0400F(I don't know much about Abbas, either.)\x02\x03",
            "(I'm pretty sure he's from the\x01",
            "Central East part of Zemuria.)\x02\x03",
            "(Heh. Well, the only thing I know for sure\x01",
            "is that he's quite eccentric.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B6")

    label("loc_1031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10B7")

    ChrTalk(
        0xE,
        (
            "#0400FIt's getting dark outside.\x02\x03",
            "I don't know what your plans are, but\x01",
            "isn't it about time you head out?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1233")

    label("loc_10B7")


    ChrTalk(
        0xE,
        "#0404F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat's wrong, Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0400FI just remembered that there's going to\x01",
            "be a full moon tonight.\x02\x03",
            "#0402FWe were blessed with clear skies today.\x01",
            "We should be able to bask in the\x01",
            "magnificent moonlight, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe moon has a reputation for\x01",
            "being an ominous symbol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FThis ain't really an appropriate\x01",
            "time to be jokin'.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1233")

    Jump("loc_38B6")

    label("loc_1238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_143B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12C8")

    ChrTalk(
        0xE,
        (
            "#0400FWell, I'm a little worried about our friends\x01",
            "over in the Saber Vipers.\x02\x03",
            "You guys should probably get to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1436")

    label("loc_12C8")


    ChrTalk(
        0xE,
        (
            "#0403FWald's quick to get irritated.\x02\x03",
            "#0400FOur lives would be much easier if we could\x01",
            "cure that short temper of his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou care for Wald a lot more than you\x01",
            "let on, don't you?\x02\x03",
            "#0005FHave you been worried about the Saber\x01",
            "Vipers all this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FHeh. I wonder...\x02\x03",
            "#0402FThere's a part inside of me that just can't\x01",
            "seem to leave Wald alone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1436")

    Jump("loc_38B6")

    label("loc_143B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 6)), scpexpr(EXPR_END)), "loc_14FA")

    ChrTalk(
        0xE,
        (
            "#0400FHeh. Bit of a surprise to see you partnered up\x01",
            "with the First Division's ace detective.\x02\x03",
            "I suppose this isn't the best time to ask,\x01",
            "but what's the occasion?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FD")

    label("loc_14FA")

    Call(0, 7)

    label("loc_14FD")

    Jump("loc_38B6")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1724")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_15D4")

    ChrTalk(
        0xE,
        (
            "#0400FI don't think anybody around these parts,\x01",
            "other than Dino, has used the drug yet.\x02\x03",
            "Still, though. Who could have given it to him?\x01",
            "I'd better be more careful with my guys, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171F")

    label("loc_15D4")


    ChrTalk(
        0xE,
        "#0402FYou came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FI know it's sudden, but do you mind\x01",
            "if we ask you a question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FI'd normally charge you for it, but this\x01",
            "one's on me.\x02\x03",
            "#0406FIt's not like this awful situation doesn't\x01",
            "concern us, either.\x02",
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
    Call(0, 8)

    label("loc_171F")

    Jump("loc_38B6")

    label("loc_1724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(
        0xE,
        (
            "#0404FHow inept do you have to be to not kill their\x01",
            "boss in a raid like that?\x02\x03",
            "#0402FIf I were Revache, I would have definitely\x01",
            "made plans to silence him. Permanently.\x02",
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
        (
            "#0106F(I sometimes forget how dangerous Wazy\x01",
            "can truly be...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A52")

    label("loc_188E")


    ChrTalk(
        0xE,
        (
            "#0400FI heard about Heiyue's office being raided.\x02\x03",
            "#0403FRevache is acting far too recklessly.\x01",
            "It won't end with simply taking\x01",
            "revenge at this rate, will it?\x02",
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
        "#0003FI fear you may be right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0400FHeh. Well, it makes sense, doesn't it?\x01",
            "If I were Heiyue, I'd definitely be giving them a\x01",
            "nice little 'thank you' for the present they gave.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A52")

    Jump("loc_38B6")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1BBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(
        0xE,
        (
            "#0403FWhat's with all the commotion in the city?\x02\x03",
            "#0402FHeh. You think everybody's excited for\x01",
            "tomorrow's full moon?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB7")

    label("loc_1AE8")


    ChrTalk(
        0xE,
        "#0403F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWhat's up, Wazy? Something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402FOh, it's nothing.\x02\x03",
            "I'm just a little worried about what the Vipers\x01",
            "plan to do. I heard a bit of a minor dispute\x01",
            "going on last night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1BB7")

    Jump("loc_38B6")

    label("loc_1BBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 4)), scpexpr(EXPR_END)), "loc_1DA5")
    SetChrSubChip(0xE, 0x0)
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x109, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C66")
    Jump("loc_1CB0")

    label("loc_1C66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C86")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB0")

    label("loc_1C86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CA6")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CB0")

    label("loc_1CA6")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CB0")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0x109,
        (
            "#0501FH-Hold on a second. I don't think a minor\x01",
            "should be drinking, let alone in the middle\x01",
            "of the day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#0402FMa'am? This is juice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(There's no way he isn't doing it intentionally.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA8")

    label("loc_1DA5")

    Call(0, 9)

    label("loc_1DA8")

    Jump("loc_38B6")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_1E27")

    ChrTalk(
        0xE,
        (
            "#0400FWell, feel free to stick around for a while.\x02\x03",
            "Could I interest you three in milkshakes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2A")

    label("loc_1E27")

    Call(0, 10)

    label("loc_1E2A")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_1E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(
        0xE,
        (
            "#0406FI may seem lax, but I'm actually far busier than\x01",
            "you could imagine during the Anniversary Festival.\x02\x03",
            "#0400FHeh. It's a pity, but I won't be able to\x01",
            "keep you company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFD")

    label("loc_1EFA")

    Call(0, 11)

    label("loc_1EFD")

    Jump("loc_38B6")

    label("loc_1F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2238")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_1FDA")

    ChrTalk(
        0xE,
        (
            "#0400FYou guys should relax a bit and take it\x01",
            "easy for the day, too.\x02\x03",
            "He doesn't look like it, but Abbas\x01",
            "makes a mean cocktail.\x02\x03",
            "Heh. Today's recipe is pretty good.\x01",
            "Want to give it a try?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2233")

    label("loc_1FDA")


    ChrTalk(
        0xE,
        (
            "#0404FThanks for the spectacular show yesterday.\x02\x03",
            "#0400FThat bracer duo sure gave us\x01",
            "a run for our mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FAren't you the slightest bit tired, Wazy?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#0405FHuh? Why would I be?\x01",
            "Oh, you mean because of that little race?\x02\x03",
            "#0402FHahaha! That's perfectly normal for me.\x02\x03",
            "That wasn't any more tiring than my\x01",
            "usual skirmishes with Wald.\x02",
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
            "#0003F(They may be delinquents, but there's\x01",
            "no denying their stamina.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(He's makin' me feel like an old geezer.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 0)

    label("loc_2233")

    Jump("loc_38B6")

    label("loc_2238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_226E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_225E")
    Call(0, 13)
    Jump("loc_2261")

    label("loc_225E")

    Call(0, 12)

    label("loc_2261")

    Jump("loc_2269")

    label("loc_2266")

    Call(0, 13)

    label("loc_2269")

    Jump("loc_38B6")

    label("loc_226E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_22A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_229C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_2294")
    Call(0, 14)
    Jump("loc_2297")

    label("loc_2294")

    Call(0, 12)

    label("loc_2297")

    Jump("loc_229F")

    label("loc_229C")

    Call(0, 14)

    label("loc_229F")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_22A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2718")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 5)), scpexpr(EXPR_END)), "loc_23BB")

    ChrTalk(
        0xE,
        (
            "#0400FHeiyue's been clawing their way\x01",
            "into Crossbell's underworld.\x02\x03",
            "#0400FI've heard they've been engaging in skirmishes\x01",
            "over smuggling routes as of late.\x02\x03",
            "#0406FSheesh, just another thing to worry about.\x01",
            "I hope their actions don't affect us, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2713")

    label("loc_23BB")


    ChrTalk(
        0xE,
        (
            "#0400FHeiyue's been clawing their way\x01",
            "into Crossbell's underworld.\x02\x03",
            "They're supposedly a large group that\x01",
            "operates in the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I've heard they're a crime syndicate\x01",
            "with a strong foothold in Calvard.\x02\x03",
            "#0001FDo you know anything about them, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#0405FHmm?\x01",
            "No, I can't say I do.\x02\x03",
            "#0400FBut, I've heard they've been engaging in skirmishes\x01",
            "over smuggling routes as of late.\x02\x03",
            "I heard they've been strengthening their forces,\x01",
            "even though they're already keeping Revache at bay.\x02\x03",
            "#0406FWe're remaining cautious, for now.\x01",
            "Their actions could affect us, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FHuh. Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FHey, how'd someone like yourself manage to\x01",
            "find that juicy piece of info?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FWell, I suppose it is a bit out of my\x01",
            "area of expertise.\x02\x03",
            "#0402FI may not look the part, but I actually have\x01",
            "connections everywhere.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 5)

    label("loc_2713")

    Jump("loc_38B6")

    label("loc_2718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 4)), scpexpr(EXPR_END)), "loc_28D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27E8")

    ChrTalk(
        0xE,
        (
            "#0400FHeh. The Special Support Section's starting\x01",
            "to become a bit of a household name, eh?\x02\x03",
            "#0404FWell, keep it up. I'm looking forward to seeing\x01",
            "what you can accomplish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_27E8")


    ChrTalk(
        0xE,
        (
            "#0400FHeh. You Special Support Section guys\x01",
            "are starting to become a bit of a household\x01",
            "name, eh?\x02\x03",
            "#0409FA household name to mock, that is.\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FYou can thank the Crossbell Times\x01",
            "for that one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FYeah...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_28D4")

    Jump("loc_2B0F")

    label("loc_28D9")


    ChrTalk(
        0xE,
        (
            "#0400FOh, you guys are here.\x02\x03",
            "Haven't seen you around in a while.\x01",
            "Conducting another investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNot today. We're just taking care of\x01",
            "some support requests.\x02\x03",
            "#0006FWe have been assisting headquarters\x01",
            "more often, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FDealing with the rush before the\x01",
            "Anniversary Festival, I take it.\x02\x03",
            "#0400FWell, keep up the good work.\x02\x03",
            "Even the Crossbell Times is showing off your\x01",
            "exploits in a better light these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FY-Yeah, I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(There's somethin' outta character about the\x01",
            "boss of some delinquents sayin' that.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 4)

    label("loc_2B0F")

    Jump("loc_38B6")

    label("loc_2B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B78")

    ChrTalk(
        0xE,
        (
            "#0400F*sigh* Maybe I'll just go ahead\x01",
            "and close up the bar for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C4D")

    label("loc_2B78")


    ChrTalk(
        0xE,
        "#0406FSheesh. Time to deal with some work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWork? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402FHeh. Wouldn't you like to know? It's. A. Secret.\x02\x03",
            "Cough up some mira, and I might be willing to\x01",
            "tell you some more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2C4D")

    Jump("loc_38B6")

    label("loc_2C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D66")

    ChrTalk(
        0xE,
        (
            "#0403FThe white wolf keeps vigil over this karmic land,\x01",
            "for here is where the bell tolls...\x01",
            "...Or something like that, I think?\x02\x03",
            "#0400FIt sounds like a story you'd hear in the\x01",
            "Septian Church Testaments.\x02\x03",
            "#0404FI don't really believe in it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2D66")


    ChrTalk(
        0xE,
        (
            "#0400FThe CGF's hunting wolf-like monsters\x01",
            "out in the mountains?\x02\x03",
            "#0404FHmm... I'm admittedly a little curious\x01",
            "about our wolven friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FWell, I wouldn't exactly call it a 'hunt.'\x01",
            "They're just patrolling the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FHey, where'd ya find somethin' like\x01",
            "that out, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FHeheh...\x01",
            "Looks like there's some truth to my words.\x02\x03",
            "#0400FI'm pretty sure I remember hearing a similar story\x01",
            "in the church's Testaments.\x02\x03",
            "#0403FThe white wolf keeps vigil over this karmic land,\x01",
            "for here is where the bell tolls...\x01",
            "...or something like that, I think?\x02\x03",
            "#0400FI don't really believe in it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FO-Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FThat's the same story the village chief told us...\x01",
            "I wasn't expecting to hear that from you,\x01",
            "of all people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3063")

    Jump("loc_38B6")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_33D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3135")

    ChrTalk(
        0xE,
        (
            "#0403FWe still owe you big time from when\x01",
            "you helped us out.\x02\x03",
            "#0402FHeh. Feel free to drop by again some time.\x01",
            "Who knows? If I'm in the mood, I may even\x01",
            "throw you another bone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D3")

    label("loc_3135")


    ChrTalk(
        0xE,
        (
            "#0405FYou came to see me, Lloyd?\x02\x03",
            "#0402FI'm so happy you came all the way\x01",
            "out here for little old me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0013FW-Wait, what?!\x02\x03",
            "#0013FWhy are you coming up with some twisted story?\x01",
            "I'm just here to offer you my thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x103,
        (
            "#0211FLloyd's overly flustered reaction raises\x01",
            "suspicion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0403FHeheh... I'll stop teasing you for a moment.\x02\x03",
            "#0400FWe still owe you big time from when\x01",
            "you helped us out.\x02\x03",
            "#0402FHeh. Feel free to drop by again some time.\x01",
            "Who knows? If I'm in the mood, I may even\x01",
            "throw you another bone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FY-Yeah, sure. I'll be sure to, when the time comes.\x01",
            "(I'm still not a fan of this guy...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_33D3")

    Jump("loc_38B6")

    label("loc_33D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_34B9")

    ChrTalk(
        0xE,
        (
            "#0404FI told the members to stop acting of\x01",
            "their own accord.\x02\x03",
            "#0400FWe'll postpone our actions for the day,\x01",
            "at the very least.\x02\x03",
            "#0402FHeh. You'd better hurry up that investigation\x01",
            "of yours, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3752")

    label("loc_34B9")


    ChrTalk(
        0xE,
        (
            "#0404FI told the members to stop acting of\x01",
            "their own accord.\x02\x03",
            "#0400FWe'll postpone our actions for the day,\x01",
            "at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FOh, really? Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402FSpare me the gratitude.\x01",
            "I wasn't doing it for your sake,\x01",
            "so don't get the wrong idea.\x02",
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
        0xE,
        (
            "#0402FWe're just conserving our stamina while we can,\x01",
            "so that we may bathe in the blood of those\x01",
            "filthy Vipers.\x02",
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
        (
            "#0306F(Dude might be pretty on the outside, but damn,\x01",
            "his personality's hideous.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3752")

    Jump("loc_38B6")

    label("loc_3757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_37E7")

    ChrTalk(
        0xE,
        (
            "#0400FHeh...\x01",
            "Feed me some interesting information, will you?\x02\x03",
            "I don't mind waiting a little while, as long\x01",
            "as it's worth it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B6")

    label("loc_37E7")


    ChrTalk(
        0xE,
        (
            "#0400FLloyd, right? You're a pretty interesting guy.\x02\x03",
            "#0402FHeh. Feel free to drop by and feed me some\x01",
            "interesting information every once in a while.\x02\x03",
            "I don't mind waiting, as long as it's worth it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_38B6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_E62 end

    def Function_7_38BE(): pass

    label("Function_7_38BE")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(-1760, 1100, 11760, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -890, 0, 11490, 315)
    SetChrPos(0x102, -780, 0, 10570, 315)
    SetChrPos(0x103, -2780, 0, 10550, 0)
    SetChrPos(0x104, -3990, 0, 10450, 45)
    SetChrPos(0x10A, -1990, 0, 10100, 0)
    SetChrPos(0xE, -2500, 50, 12400, 135)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0xE, 0x2)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#0402FWell, well, well. What do we have here?\x01",
            "This is a rare guest if I've ever seen one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0603FIt's been a while, Wazy Hemisphere.\x02\x03",
            "#0601FDo you intend on continuing to masquerade\x01",
            "as a delinquent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FHeh. As I've told you many times before,\x01",
            "none of it really matters to me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AAF():
        TurnDirection(0x101, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AAF)

    def lambda_3ABC():
        TurnDirection(0x102, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ABC)

    def lambda_3AC9():
        TurnDirection(0x103, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AC9)

    def lambda_3AD6():
        TurnDirection(0x104, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AD6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#0011FDo you know him, Detective Dudley?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#0601FYes. I met him when he moved downtown two\x01",
            "years ago and formed this group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FHeh. He's a part of the esteemed First Division,\x01",
            "yet he still bothers to visit this dump we call\x01",
            "the Downtown District.\x02\x03",
            "#0402FMust be the influence of a certain somebody,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FA certain somebody? Who are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#0603FYour idle chatter ceases now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x9, 350)

    ChrTalk(
        0x10A,
        (
            "#0601F#6PAbbas. Keep this man in line, and prevent\x01",
            "him from provoking Wald any further.\x02\x03",
            "Unless you'd rather the First Division come\x01",
            "here in full force.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 350)

    ChrTalk(
        0x9,
        "Understood.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        "#0404FYikes.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 0, 11490, 315)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xD0, 6)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_7_38BE end

    def Function_8_3DB7(): pass

    label("Function_8_3DB7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-2940, 1100, 11130, 0)
    MoveCamera(51, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, -2690, 0, 10450, 360)
    SetChrPos(0x102, -1410, 0, 10430, 315)
    SetChrPos(0x103, -4080, 0, 10220, 45)
    SetChrPos(0x104, -4600, 0, 11800, 90)
    SetChrPos(0xE, -2690, 50, 12150, 180)
    SetChrSubChip(0xE, 0x0)
    SetCameraDistance(19950, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xE,
        (
            "#0403F#5PYou know that new gopher for the Vipers?\x01",
            "I think his name was...Dino?\x02\x03",
            "#0401FHe's been looking a little different lately.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0x104,
        (
            "#0303F#6PYeah, I heard rumors. Didn't he try\x01",
            "to take on his superior in a fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402F#5PYeah, he actually challenged Wald to a\x01",
            "fight yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40A1")

    label("loc_3F92")


    ChrTalk(
        0x101,
        "#0008F#12PI thought so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0406F#5PHe was all up in Wald's face. He wasn't giving\x01",
            "the impression of a complete rookie at all.\x02\x03",
            "#0401FHe likes to constantly bark at our members\x01",
            "and try to fight them, but...\x02\x03",
            "#0402FHe actually challenged Wald to a fight yesterday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A1")

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
        "#0007F#12PW-Wait, seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402F#5PSeriously.\x02\x03",
            "#0404FI didn't get to watch it with my own eyes,\x01",
            "but he was supposedly keeping up with\x01",
            "Wald in terms of power and speed.\x02\x03",
            "Wald finally managed to take him down\x01",
            "when he started trying his hardest.\x02\x03",
            "#0400FAfter he lost, Dino stormed out of the place.\x01",
            "No one's seen him since that morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F#6PThings ain't lookin' too good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F#12PRight. This is becoming quite serious.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    ChrTalk(
        0xE,
        (
            "#0404F#5PSo...\x02\x03",
            "#0402FIs this all thanks to that fancy new drug?\x02",
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
        "#0011F#12PHow the?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105F#12PWhere did you hear...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0405F#5PAh, I thought that might have been the case.\x02\x03",
            "#0404FI heard some strange rumor about a magical drug\x01",
            "that grants your wishes or something. I thought\x01",
            "that thing might have been responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F#6PSo, you baited us with a leading question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F#6PHey, pal. Try not to run your mouth off about\x01",
            "it too much.\x02\x03",
            "Don't need more people knowin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0409F#5PHeh. I'll try and heed your words.\x02\x03",
            "#0400F#5PFor what it's worth, I don't think anybody other\x01",
            "than Dino's used that thing around these parts.\x02\x03",
            "#0404FOnly problem is, I have no clue who would\x01",
            "have even given him the drugs.\x01",
            "I'd better keep a stronger watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#12PThanks, Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#12PWe appreciate the help.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -2690, 0, 10250, 360)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetScenarioFlags(0xC8, 1)
    OP_29(0x4C, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_8_3DB7 end

    def Function_9_46C3(): pass

    label("Function_9_46C3")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-1760, 1100, 11760, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -890, 0, 11490, 315)
    SetChrPos(0x102, -780, 0, 10570, 315)
    SetChrPos(0x103, -2780, 0, 10550, 0)
    SetChrPos(0x104, -3990, 0, 10450, 45)
    SetChrPos(0x109, -1990, 0, 10100, 0)
    SetChrPos(0xE, -2500, 50, 12400, 135)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#0402FWell, if it isn't my SSS friends.\x01",
            "Are you working right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, just taking care of a few things.\x02\x03",
            "#0000FAny changes in the Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0403F...\x02\x03",
            "#0400FI suppose the Testaments are the same as usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#0400FBut enough about that.\x02\x03",
            "#0402FI see a new face among your ranks.\x01",
            "Is she from the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah. Circumstances led to us working together,\x01",
            "so she's with us for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FMy name's Noel Seeker.\x02\x03",
            "Are you an acquaintance of the SSS?\x01",
            "It's a pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0xE,
        (
            "#0402FWow...\x02\x03",
            "#0404FI could tell her to loosen up, but I bet it'd\x01",
            "be way more fun to mess with her.\x01",
            "Don't you guys think so, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#0505FExcuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FHonestly, Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0403FOh, come on. Manners are wasted on\x01",
            "a bad boy like myself.\x02\x03",
            "#0402FI'd rather hear a girl like her yell at\x01",
            "me until she's red in the face.\x02\x03",
            "#0405FDon't get me wrong, though.\x01",
            "I'm no masochist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0503FN-Now, you listen here...\x02\x03",
            "#0501FI gave you the most forthright greeting\x01",
            "I could, so why are you returning the\x01",
            "favor by making fun of me?\x02\x03",
            "Furthermore, what's with your wardrobe?\x01",
            "Dress more like someone your age!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#0409FYep, that's definitely more like it. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0505F*gawk*\x02",
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
            "#0003F(Bringing someone as straitlaced as the\x01",
            "sergeant major here might have been\x01",
            "a miscalculation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Haha, I wouldn't say that. They seem to\x01",
            "be gettin' along juuuust fine.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 0, 11490, 315)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xD0, 4)
    EventEnd(0x5)
    Return()

    # Function_9_46C3 end

    def Function_10_4E75(): pass

    label("Function_10_4E75")

    SetChrSubChip(0xE, 0x2)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-2840, 1100, 11440, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -2660, 0, 10470, 0)
    SetChrPos(0xEF, -1570, 0, 10560, 315)
    SetChrPos(0x153, -3700, 0, 10800, 45)
    SetChrPos(0xE, -2710, 0, 12150, 180)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    ChrTalk(
        0x153,
        "#1110FAh, it's Wazy.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0xE,
        (
            "#0402FHey there, little lady. Haven't seen you in a while.\x01",
            "Have you been doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FYep! I just ate a nice, big breakfast!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#0402FHeh. Good, it's important to make sure you do.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    ChrTalk(
        0xE,
        (
            "#0404FYou guys seem to be hanging on just fine.\x02\x03",
            "#0400FI heard you managed to strike up a\x01",
            "deal with Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah. This morning, actually.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_511F")

    ChrTalk(
        0x102,
        (
            "#0100FWe're just showing KeA around the city now.\x02\x03",
            "#0101F...Wazy. You'd better not teach\x01",
            "KeA anything strange, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5262")

    label("loc_511F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51C1")

    ChrTalk(
        0x103,
        (
            "#0200FWe are now acquainting KeA with the\x01",
            "sights around the city.\x02\x03",
            "#0203FWazy. I urge you to refrain from uttering\x01",
            "any oddities to KeA.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5262")

    label("loc_51C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5262")

    ChrTalk(
        0x104,
        (
            "#0300FWe're just showin' KeDo around\x01",
            "the city now, is all.\x02\x03",
            "#0301FHey, Wazy. I'd better not catch ya tellin'\x01",
            "KeDo anythin' strange. Got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5262")


    ChrTalk(
        0x101,
        (
            "#0003FYeah, definitely.\x02\x03",
            "#0001FTry to moderate your language around\x01",
            "her a little bit, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404FHeh. I wouldn't dream of corrupting her.\x02\x03",
            "#0400FI have to say, the two of you have perfectly\x01",
            "grown into the roles of guardians.\x02\x03",
            "You're essentially her mom and dad\x01",
            "for the time being, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_541B")

    ChrTalk(
        0x102,
        "#0105FY-You think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. Well, we've assumed the role of her\x01",
            "guardians until we find her family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AA")

    label("loc_541B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54DC")

    ChrTalk(
        0x103,
        (
            "#0211FClaiming me to be her mother is a\x01",
            "slight exaggeration, I would think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. Well, we've assumed the role of her\x01",
            "guardians until we find her family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AA")

    label("loc_54DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55AA")

    ChrTalk(
        0x104,
        (
            "#0309FI'm totally the dad, and Lloyd's\x01",
            "the mom, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, I don't think so.\x02\x03",
            "#0000FWell, either way. We've assumed the role\x01",
            "of her guardians until we can find her family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AA")

    SetScenarioFlags(0xB0, 1)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x1)
    EventEnd(0x5)
    Return()

    # Function_10_4E75 end

    def Function_11_55C9(): pass

    label("Function_11_55C9")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0x12,
        "Can we sit next to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Uh, we're a little bit lost at the moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "There's a lot of scary-looking people here,\x01",
            "so we're, like, totally helpless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "But, you know what? I feel like we were totally\x01",
            "lucky to meet someone like Wazy here. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0403F...\x02\x03",
            "#0400FOh, is that what you think?\x01",
            "Well, I'm sorry to tell you this, but...\x02\x03",
            "#0402F...I'm the scariest one out of all of them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0001F(Sheesh, Wazy. What a guy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F(Ain't he a pro...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_11_55C9 end

    def Function_12_57E8(): pass

    label("Function_12_57E8")


    ChrTalk(
        0xE,
        (
            "#0402FHeh. Good work, you guys.\x02\x03",
            "Looks like you gave not only us, but\x01",
            "the Vipers' underlings some valuable\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FNo problem. You can never be too careful\x01",
            "when you live down here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58B4():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_58B4)

    def lambda_58C1():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_58C1)

    def lambda_58CE():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_58CE)

    def lambda_58DB():
        TurnDirection(0x3, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_58DB)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    def lambda_594F():
        TurnDirection(0x0, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_594F)

    def lambda_595C():
        TurnDirection(0x1, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_595C)

    def lambda_5969():
        TurnDirection(0x2, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5969)

    def lambda_5976():
        TurnDirection(0x3, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5976)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)

    ChrTalk(
        0x102,
        (
            "#0101F(If you don't mind us asking, what kind of\x01",
            "person is Abbas? I can't get a read on him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(I get the feelin' that he's got some\x01",
            "serious skills.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0404F(Heh. I know where you're coming from.)\x02\x03",
            "#0400F(I'm pretty sure he's from around the\x01",
            "middle eastern part of Zemuria.)\x02\x03",
            "(Considering he idolizes an oddball\x01",
            "like myself, I think it's pretty safe to\x01",
            "say he's an eccentric guy.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "I can hear everything you are saying, Wazy.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5B73")
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_5B7A")

    label("loc_5B73")

    OP_93(0x9, 0x0, 0x0)

    label("loc_5B7A")

    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x8F, 7)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_12_57E8 end

    def Function_13_5B85(): pass

    label("Function_13_5B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5CC3")

    ChrTalk(
        0xE,
        (
            "#0404FOh, yeah. A busty Eastern-looking chick moved\x01",
            "into the Downtown District pretty recently.\x02\x03",
            "#0400FShe told me she'll be playing the co-lead\x01",
            "for Arc en Ciel's new production.\x02\x03",
            "#0402FYou think she'll be okay? I can't stop thinking\x01",
            "about her massive knockers getting in the\x01",
            "way of her acrobatics.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E86")

    label("loc_5CC3")


    ChrTalk(
        0xE,
        (
            "#0405FOh? Those glum faces of yours tell me\x01",
            "that you're in hot water again.\x02\x03",
            "#0400FHeh. What happened this time?\x01",
            "You guys in a pinch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FYeah, I guess we are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402FWell, I can't claim to know your circumstances,\x01",
            "but good luck.\x02\x03",
            "Either way, I'm pretty excited to check out\x01",
            "Arc en Ciel's new show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F(Doesn't look like he knows squat, huh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(He may have been trying to goad us into\x01",
            "leaking information to him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_5E86")

    Return()

    # Function_13_5B85 end

    def Function_14_5E87(): pass

    label("Function_14_5E87")

    SetChrSubChip(0xE, 0x2)

    ChrTalk(
        0xE,
        (
            "#0402FWhoa. Isn't it pretty risky to buy\x01",
            "up those kinds of goods?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Not particularly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I only dabble in goods that easily sell.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6008")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_END)), "loc_5FD3")
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
        "#0001F(Looks like they're in the middle of a conversation.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6005")

    label("loc_5FD3")


    ChrTalk(
        0x101,
        "#0006F(Wh-What are they even talking about?)\x02",
    )

    CloseMessageWindow()

    label("loc_6005")

    SetScenarioFlags(0x0, 0)

    label("loc_6008")

    Return()

    # Function_14_5E87 end

    def Function_15_6009(): pass

    label("Function_15_6009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6032")
    Call(0, 55)
    Return()

    label("loc_6032")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62D5")

    ChrTalk(
        0x9,
        (
            "I would like to have the Testaments trained in\x01",
            "the art of self-defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Will you do the honor of teaching suppression\x01",
            "techniques taught to police officers?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6231")
    TalkEnd(0x9)
    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(1290, 1000, 9450, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0x9, 3060, 0, 8960, 270)
    SetChrPos(0x101, 700, 0, 9600, 90)
    SetChrPos(0x102, 560, 0, 8000, 90)
    SetChrPos(0x103, -990, 0, 8000, 90)
    SetChrPos(0x104, -990, 0, 9600, 90)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, 14390, 0, 7400, 178)
    SetChrPos(0xC, 14000, 0, 7400, 268)
    SetChrPos(0xA, 9250, 0, 4150, 225)
    SetChrPos(0xB, 5000, 0, 2000, 90)
    OP_0D()
    Call(0, 56)
    Return()

    label("loc_6231")


    ChrTalk(
        0x101,
        (
            "#0001FCould you give us a bit? We still need\x01",
            "time to get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We are free all day. You would be wise to\x01",
            "fully prepare yourselves before accepting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_62D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6343")

    ChrTalk(
        0x9,
        "There is nothing abnormal here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should proceed with your investigation\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_6343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_63B3")

    ChrTalk(
        0x9,
        "Leave this area to Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should proceed with your investigation\x01",
            "elsewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640F")

    label("loc_63B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_END)), "loc_63D6")

    ChrTalk(
        0x9,
        "May I help you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_640F")

    label("loc_63D6")


    ChrTalk(
        0x9,
        "Are you looking for Wazy? He is not here right now.\x02",
    )

    CloseMessageWindow()

    label("loc_640F")

    Jump("loc_702A")

    label("loc_6414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_6447")

    ChrTalk(
        0x9,
        "Do you wish to speak with Wazy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_6447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_64A4")

    ChrTalk(
        0x9,
        (
            "One of the Vipers has been behaving\x01",
            "strangely for the last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_64A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_652F")

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Will you be placing an order?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(It's always so difficult to strike up a\x01",
            "conversation with this guy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_652F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_674D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_65D8")

    ChrTalk(
        0x9,
        (
            "If Wazy has assessed the situation, then there\x01",
            "are no problems. His judgment is absolute.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_6748")

    label("loc_65D8")


    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I urge you to refrain from involving Wazy\x01",
            "in any future disputes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FWazy was the one who took charge at\x01",
            "Mishelam, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That was Wazy's judgment?\x01",
            "Everything is fine, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006F(Kind of weird that he came to a conclusion on\x01",
            "something so complex that easily, don't you think?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6748")

    Jump("loc_702A")

    label("loc_674D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_68D2")

    ChrTalk(
        0x9,
        "Are you looking for Wazy? He left for work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I would recommend returning at a later time\x01",
            "if you wish to speak with him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68CD")

    ChrTalk(
        0x101,
        "#0005FHe has work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I am not obligated to answer your questions.\x02",
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
        "#0006F(Still difficult to strike up a conversation...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_68CD")

    Jump("loc_702A")

    label("loc_68D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_696A")

    ChrTalk(
        0x9,
        (
            "We are serving a special cocktail to\x01",
            "commemorate the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please place your order if you would\x01",
            "like to try it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_696A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_69EA")

    ChrTalk(
        0x9,
        "We are temporarily closed for the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Please return tomorrow if you would\x01",
            "like to come in for a drink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_69EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6A20")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_6A10")
    Call(0, 18)
    Jump("loc_6A13")

    label("loc_6A10")

    Call(0, 17)

    label("loc_6A13")

    Jump("loc_6A1B")

    label("loc_6A18")

    Call(0, 18)

    label("loc_6A1B")

    Jump("loc_702A")

    label("loc_6A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6A56")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_6A46")
    Call(0, 19)
    Jump("loc_6A49")

    label("loc_6A46")

    Call(0, 17)

    label("loc_6A49")

    Jump("loc_6A51")

    label("loc_6A4E")

    Call(0, 19)

    label("loc_6A51")

    Jump("loc_702A")

    label("loc_6A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6B19")

    ChrTalk(
        0x9,
        (
            "We plan to regularly patrol the Downtown District to\x01",
            "prevent the mafia from worming their way in again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Preventing such a situation from recurring\x01",
            "is preferable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE7")

    label("loc_6B19")


    ChrTalk(
        0x9,
        (
            "If the mafia's dispute rages on, then we may\x01",
            "feel some of the effects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It would be wise of us to plan accordingly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Our first course of action is to begin patrolling\x01",
            "the Downtown District.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6BE7")

    Jump("loc_702A")

    label("loc_6BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6CC3")

    ChrTalk(
        0x9,
        (
            "We have been faced with many more\x01",
            "challenges of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CBE")
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
        0x9,
        "No, never mind.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6CBE")

    Jump("loc_702A")

    label("loc_6CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6D63")

    ChrTalk(
        0x9,
        (
            "I have no intention of prying into our\x01",
            "members' personal lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We leave it up to our members' judgment\x01",
            "to decide if they want to stay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_6D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6DC0")

    ChrTalk(
        0x9,
        "We will look after Azel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It is futile to continue worrying.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E58")

    label("loc_6DC0")


    ChrTalk(
        0x9,
        (
            "Azel must continue to visit the hospital for\x01",
            "regular checkups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "His extended period of unconsciousness makes\x01",
            "it necessary for him to do so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6E58")

    Jump("loc_702A")

    label("loc_6E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6F1B")

    ChrTalk(
        0x9,
        "We are currently open for business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "We would be happy to take your order.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F16")

    ChrTalk(
        0x101,
        "#0003FS-Sure. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F(That huge dude runs this place, right?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_6F16")

    Jump("loc_702A")

    label("loc_6F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6F9C")

    ChrTalk(
        0x9,
        (
            "Please notify Wazy of any new information\x01",
            "you may have stumbled upon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "There is no need to speak with us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_702A")

    label("loc_6F9C")


    ChrTalk(
        0x9,
        (
            "We are waiting for the hospital to notify\x01",
            "us of his condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You should leave immediately if you\x01",
            "have finished saying your piece.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702A")

    TalkEnd(0x9)
    Return()

    # Function_15_6009 end

    def Function_16_702E(): pass

    label("Function_16_702E")

    Call(0, 15)
    Return()

    # Function_16_702E end

    def Function_17_7032(): pass

    label("Function_17_7032")


    ChrTalk(
        0x9,
        "Here, take this with you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1D5, 1)

    ChrTalk(
        0x101,
        "#0005FTh-Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203F(This must be our reward. His inability to\x01",
            "communicate makes it difficult to discern.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(Let's just accept it for now, then.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 1)
    Return()

    # Function_17_7032 end

    def Function_18_714A(): pass

    label("Function_18_714A")


    ChrTalk(
        0x9,
        (
            "Now, then.\x01",
            "The Anniversary Festival draws near.\x01",
            "We must begin our preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Huh? Are they planning on offering\x01",
            "special discounts for their drinks,\x01",
            "or something?)\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_714A end

    def Function_19_7202(): pass

    label("Function_19_7202")


    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do not disturb Wazy right now.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_19_7202 end

    def Function_20_7230(): pass

    label("Function_20_7230")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_73A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_72CC")

    ChrTalk(
        0xA,
        (
            "The Testaments fight honorably. We don't\x01",
            "intend on resorting to petty tricks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ahem! You would do well to remember that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_739D")

    label("loc_72CC")


    ChrTalk(
        0xA,
        (
            "The Vipers have been weakened. Now's the\x01",
            "perfect time to get rid of them, once and for all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "However, Wazy isn't the type of man that\x01",
            "would resort to that kind of tactic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That's Wazy for you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_739D")

    Jump("loc_8811")

    label("loc_73A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7447")

    ChrTalk(
        0xA,
        (
            "Wazy's been wearing a serious expression\x01",
            "on his face all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't imagine what has him looking that way.\x01",
            "I've never seen him so focused.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8811")

    label("loc_7447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_75C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_74C2")

    ChrTalk(
        0xA,
        (
            "Man, if only I had Wazy's permission...\x01",
            "I would give that rookie a beatdown he'd\x01",
            "never forget.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75C2")

    label("loc_74C2")


    ChrTalk(
        0xA,
        (
            "Ahem! Apparently, one of the Vipers'\x01",
            "underlings has been acting strangely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I bet it's that little rookie of theirs. He's been\x01",
            "trying to mess with us every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wazy told us not to lay a finger on him,\x01",
            "though.\x01",
            "Damn it! That pisses me off!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_75C2")

    Jump("loc_8811")

    label("loc_75C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_76F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_762A")

    ChrTalk(
        0xA,
        (
            "Can't say I'm surprised that the police\x01",
            "are finally making their move.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76F2")

    label("loc_762A")


    ChrTalk(
        0xA,
        (
            "The mafia's dispute has sent a bunch of people\x01",
            "to the hospital where my old man works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Sounds like that rumor wasn't a lie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmph. Pretty gutsy thing to do in the\x01",
            "middle of downtown.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_76F2")

    Jump("loc_8811")

    label("loc_76F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_782A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_774C")

    ChrTalk(
        0xA,
        (
            "Damn those Vipers... Does their audacity\x01",
            "know no bounds?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7825")

    label("loc_774C")


    ChrTalk(
        0xA,
        (
            "We got into a little spat with the Vipers\x01",
            "in the middle of the street yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Those guys never change. They don't have\x01",
            "a single shred of integrity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It just makes me want to beat them\x01",
            "even harder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7825")

    Jump("loc_8811")

    label("loc_782A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_794C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_78D1")

    ChrTalk(
        0xA,
        (
            "Wazy's word is absolute. We have no choice\x01",
            "but to follow his lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "S-Sorry, Wazy. I tried to get them to leave\x01",
            "before you got back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7947")

    label("loc_78D1")


    ChrTalk(
        0xA,
        "Ahem! Leave Wazy alone, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I bet if it were Abbas, he'd say something\x01",
            "like 'Wazy's word is absolute.'\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7947")

    Jump("loc_8811")

    label("loc_794C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_79C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_79BD")

    ChrTalk(
        0xA,
        "Wazy and Abbas aren't here right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "W-We've gotta hold the fort on our own...\x02",
    )

    CloseMessageWindow()
    Jump("loc_79C0")

    label("loc_79BD")

    Call(0, 21)

    label("loc_79C0")

    Jump("loc_8811")

    label("loc_79C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7A7F")

    ChrTalk(
        0xA,
        (
            "Our relationship with the Vipers has\x01",
            "been tense for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "...but hey, at least we're civil enough to set aside\x01",
            "our differences during the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B80")

    label("loc_7A7F")


    ChrTalk(
        0xA,
        (
            "Even those guys in the mafia have settled down\x01",
            "now that the festivities have begun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've set aside our differences with the\x01",
            "Vipers for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Sheesh. Now we've gotta wait a little longer\x01",
            "before we can completely annihilate them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7B80")

    Jump("loc_8811")

    label("loc_7B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7BBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_7BAB")
    Call(0, 23)
    Jump("loc_7BAE")

    label("loc_7BAB")

    Call(0, 22)

    label("loc_7BAE")

    Jump("loc_7BB6")

    label("loc_7BB3")

    Call(0, 23)

    label("loc_7BB6")

    Jump("loc_8811")

    label("loc_7BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7DF6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7CB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_7CB0")

    ChrTalk(
        0xA,
        (
            "The Vipers have been acting snakier than\x01",
            "usual. We'll have to strengthen our patrol\x01",
            "and make sure they aren't plotting anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We won't let them get away scot-free\x01",
            "if we find them pulling anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB3")

    label("loc_7CB0")

    Call(0, 22)

    label("loc_7CB3")

    Jump("loc_7DF1")

    label("loc_7CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7D35")

    ChrTalk(
        0xA,
        (
            "Even on slower days, Wazy has a giant load\x01",
            "of work to deal with. I hope he's taking good\x01",
            "care of himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DF1")

    label("loc_7D35")


    ChrTalk(
        0xA,
        (
            "Looks like Wazy stayed up the entire\x01",
            "night drinking again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Um. I obviously don't intend on voicing my\x01",
            "concerns to him, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I just want him to take care of himself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7DF1")

    Jump("loc_8811")

    label("loc_7DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E97")

    ChrTalk(
        0xA,
        (
            "There's been a number of disputes in\x01",
            "the Back Alley and Entertainment\x01",
            "District lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Isn't it all thanks to your negligence,\x01",
            "you pigs?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8811")

    label("loc_7E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7F5B")

    ChrTalk(
        0xA,
        "We'll settle things with the Vipers...eventually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've called a truce for the duration of the\x01",
            "Anniversary Festival. Too many cops\x01",
            "around ready to get in our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_800C")

    label("loc_7F5B")


    ChrTalk(
        0xA,
        (
            "We haven't had a decent fight with\x01",
            "the Vipers in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Too many cops roaming since the Anniversary\x01",
            "Festival is coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Thanks for ruining our fun. Geez.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_800C")

    Jump("loc_8811")

    label("loc_8011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_806F")

    ChrTalk(
        0xA,
        "By the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You don't think Azel is going to\x01",
            "quit, do you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8120")

    label("loc_806F")


    ChrTalk(
        0xA,
        (
            "The Vipers are hanging around\x01",
            "the plaza again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I get sick just looking at them. They've become\x01",
            "quite egotistical. Someone ought to put those\x01",
            "guys in their place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_8120")

    Jump("loc_8811")

    label("loc_8125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_830A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_81C1")

    ChrTalk(
        0xA,
        (
            "As a practitioner of martial arts, I'm\x01",
            "confident with hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm nowhere near as skilled as Wazy is, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8305")

    label("loc_81C1")


    ChrTalk(
        0xA,
        (
            "I'm so damn bored. We haven't been getting\x01",
            "into any fights with the Vipers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't let this lull put a damper on my skills.\x01",
            "I'd better practice shooting a slingshot for\x01",
            "a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've been practicing martial arts ever since\x01",
            "I was a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'm pretty confident in hand-to-hand combat, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_8305")

    Jump("loc_8811")

    label("loc_830A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_84B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_83BB")

    ChrTalk(
        0xA,
        (
            "Phew... Azel's finally out of the hospital.\x01",
            "What a load off my chest that was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now we can get back to figuring\x01",
            "out how to take down the Vipers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84B0")

    label("loc_83BB")


    ChrTalk(
        0xA,
        (
            "Phew... What a relief. Azel is finally\x01",
            "out of the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I may be thankful to you now, but don't\x01",
            "let it get to your head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Testaments are the moving parts to\x01",
            "Wazy's brain. That's why he's the one\x01",
            "who calls all the shots.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_84B0")

    Jump("loc_8811")

    label("loc_84B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_855E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 3)), scpexpr(EXPR_END)), "loc_8556")

    ChrTalk(
        0xA,
        "Azel being hospitalized has me worried.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "My old man works there, so maybe I'll use\x01",
            "him as an excuse to go visit Azel tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8559")

    label("loc_8556")

    Call(0, 24)

    label("loc_8559")

    Jump("loc_8811")

    label("loc_855E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8611")

    ChrTalk(
        0xA,
        (
            "Azel got beat up pretty badly. He was\x01",
            "covered in cuts and bruises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It looked like the work of those nail bats\x01",
            "the Vipers are so fond of.\x01",
            "Those scumbags...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8811")

    label("loc_8611")


    ChrTalk(
        0xA,
        (
            "It may not seem like it, but we don't\x01",
            "act on our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Azel was returning home for the first time\x01",
            "in a while on that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "When we found Azel, he was already\x01",
            "collapsed on the ground, covered in\x01",
            "cuts and bruises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This was definitely the work of a nail bat\x01",
            "those brutes are so fond of!\x01",
            "...Damn it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_880E")

    ChrTalk(
        0x101,
        (
            "#0003FI see. Thanks for taking the time to\x01",
            "give us information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I-I only talked to you 'cause Wazy\x01",
            "asked me to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't get so full of yourselves,\x01",
            "you incompetent cops!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 2)

    label("loc_880E")

    SetScenarioFlags(0x0, 2)

    label("loc_8811")

    TalkEnd(0xFE)
    Return()

    # Function_20_7230 end

    def Function_21_8815(): pass

    label("Function_21_8815")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "I-I'm bad at serving customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'll let Kienz deal with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You say that, but I'm not particularly\x01",
            "good at it, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I'll take it from here, though.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_21_8815 end

    def Function_22_88DA(): pass

    label("Function_22_88DA")


    ChrTalk(
        0xA,
        (
            "I actually partake in secret training sessions.\x01",
            "Today's scrimmage will serve as a useful\x01",
            "reference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm only going to say this once, all right?\x01",
            "Thanks, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 2)
    Return()

    # Function_22_88DA end

    def Function_23_8989(): pass

    label("Function_23_8989")


    ChrTalk(
        0xA,
        (
            "I can't believe the Vipers have started\x01",
            "patrolling the area, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "No wonder I've been seeing their ugly mugs\x01",
            "more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wazy doesn't intend to stifle their\x01",
            "efforts quite yet, but that entirely\x01",
            "depends on their attitude.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_8989 end

    def Function_24_8A76(): pass

    label("Function_24_8A76")


    ChrTalk(
        0xA,
        (
            "Now that it's come to this, I regret not\x01",
            "reading my old man's medical textbooks.\x02",
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
        0x103,
        "#0205FMedical textbooks?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x0, 500)

    ChrTalk(
        0xA,
        "Wh-What the...? Oh, it's just you guys again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You got a problem with that?\x01",
            "Everybody has a secret or two.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "We dragged Azel back here after he was\x01",
            "assaulted to administer some emergency\x01",
            "medical care, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He didn't regain consciousness. We ended up\x01",
            "calling an ambulance and had to wait until\x01",
            "dawn before we could shuttle him off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I may despise my old man, but I really\x01",
            "regret not having him teach me some\x01",
            "basic first aid techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSo that's what happened. You guys\x01",
            "must be worried sick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Yeah. Strangely enough, the ambulance\x01",
            "didn't depart for the hospital immediately\x01",
            "after picking up Azel.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_8F7C")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FOh, yeah. That's because they ended up\x01",
            "picking up that kid from the Saber Vipers\x01",
            "that got hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FI am relieved the ambulance did not\x01",
            "unnecessarily double their efforts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#4SWh-Why the hell are you guys relieved?!\x01",
            "That punk is a stinkin' Viper!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_921E")

    label("loc_8F7C")

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
        0x102,
        "#0105FWhat do you mean, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Apparently, some other person downtown\x01",
            "got injured and sent to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmph. It was some stinkin' Saber Viper.\x01",
            "One of his comrades told us he got hurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The ambulance ended up taking both injured\x01",
            "victims to the hospital at the same time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSo, members from both of your groups were\x01",
            "assaulted on the same night? Interesting...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301FTalk about some convenient timin', eh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#4SConvenient?! The timing was HORRIBLE!\x01",
            "Do you think we wanna share an ambulance\x01",
            "with some Viper?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_921E")


    ChrTalk(
        0xA,
        "#2SA-Ahem! Lost my cool there for a second.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Azel being hospitalized has me worried.\x01",
            "My old man works there, so maybe I'll use\x01",
            "him as an excuse to go visit Azel tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x4E, 3)
    Return()

    # Function_24_8A76 end

    def Function_25_92DD(): pass

    label("Function_25_92DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_944E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9381")

    ChrTalk(
        0xB,
        (
            "Wazy rejected our idea to launch a\x01",
            "surprise attack on the Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Th-Those red plagues managed to\x01",
            "narrowly escape their deaths.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9449")

    label("loc_9381")


    ChrTalk(
        0xB,
        (
            "W-We hold quite a bit of resentment towards\x01",
            "the V-Vipers, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-If Wazy doesn't want us to do anything,\x01",
            "then th-there's not much we can do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "W-We'll spare them this time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_9449")

    Jump("loc_A7DE")

    label("loc_944E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_94D0")

    ChrTalk(
        0xB,
        "W-Wazy's been going out more often th-these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-I think he's conducting s-some sort of investigation.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7DE")

    label("loc_94D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_963C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9564")

    ChrTalk(
        0xB,
        (
            "Th-The Vipers have been quarreling\x01",
            "among th-themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hah. There's no point in worrying about\x01",
            "those red plagues.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9637")

    label("loc_9564")


    ChrTalk(
        0xB,
        (
            "I ch-checked it out earlier, and it seemed\x01",
            "to hold true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "One of the Vipers' leaders was beaten to\x01",
            "a pulp and sent to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I don't get how. Leave it to those idiots\x01",
            "to let it happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_9637")

    Jump("loc_A7DE")

    label("loc_963C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_969B")

    ChrTalk(
        0xB,
        (
            "I'll rearrange those m-mobsters' faces if\x01",
            "they show up here again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_972E")

    label("loc_969B")


    ChrTalk(
        0xB,
        (
            "Those m-mobsters have been wandering\x01",
            "around here again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "D-Do us a favor and arrest th-them. You've\x01",
            "already helped us out once before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_972E")

    Jump("loc_A7DE")

    label("loc_9733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_97F1")

    ChrTalk(
        0xB,
        (
            "Th-That blue-haired ruffian has been\x01",
            "p-provoking us more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not only that, b-but his appearance has changed.\x01",
            "I remember him being way more wimpy before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_988E")

    label("loc_97F1")


    ChrTalk(
        0xB,
        (
            "S-Something about that blue-haired ruffian\x01",
            "feels off to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-If I remember correctly, he was that little twerp\x01",
            "who used to guard the entrance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_988E")

    Jump("loc_A7DE")

    label("loc_9893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_992F")

    ChrTalk(
        0xB,
        "Kienz left t-to meet his old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-His old man's a doctor at St. Ursula\x01",
            "Medical College.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I d-don't think they get along well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7DE")

    label("loc_992F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_99BD")

    ChrTalk(
        0xB,
        (
            "Fortunately, Ryan's going to help us\x01",
            "hold down the fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I'm worried about Wazy meeting strange\x01",
            "customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA4")

    label("loc_99BD")


    ChrTalk(
        0xB,
        (
            "I didn't know Ryan was skilled at\x01",
            "making cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A-Abbas makes a delicious cocktail, but\x01",
            "Ryan's no slouch, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That reminds me. Ryan doesn't stand out\x01",
            "much, but he's actually pretty skilled with\x01",
            "his hands.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_9AA4")

    Jump("loc_A7DE")

    label("loc_9AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9B33")
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0xB,
        (
            "F-Feel free to talk to me if you'd like to play\x01",
            "a round of billiards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I can teach you the rules.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_9B36")

    label("loc_9B33")

    Call(0, 21)

    label("loc_9B36")

    Jump("loc_A7DE")

    label("loc_9B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9BAE")

    ChrTalk(
        0xB,
        "W-We're all going out together today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wazy's a busy man, so we didn't have\x01",
            "time yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7DE")

    label("loc_9BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9BE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_9BD4")
    Call(0, 27)
    Jump("loc_9BD7")

    label("loc_9BD4")

    Call(0, 26)

    label("loc_9BD7")

    Jump("loc_9BDF")

    label("loc_9BDC")

    Call(0, 27)

    label("loc_9BDF")

    Jump("loc_A7DE")

    label("loc_9BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9D9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_9CF5")

    ChrTalk(
        0xB,
        (
            "I-If I learn some self-defense techniques,\x01",
            "I won't be afraid of the mafia anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We'll kick them out of the Downtown District\x01",
            "if we come across them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CED")

    ChrTalk(
        0x101,
        (
            "#0006FCan you do us a favor and not do\x01",
            "anything reckless?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CED")

    SetScenarioFlags(0x0, 3)
    Jump("loc_9CF8")

    label("loc_9CF5")

    Call(0, 26)

    label("loc_9CF8")

    Jump("loc_9D96")

    label("loc_9CFD")


    ChrTalk(
        0xB,
        (
            "Th-That customer always comes here once\x01",
            "a week, without fail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "She appears to be conversing with Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Y-Yeah. Wazy's an adult, all right.\x02",
    )

    CloseMessageWindow()

    label("loc_9D96")

    Jump("loc_A7DE")

    label("loc_9D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A0C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 3)), scpexpr(EXPR_END)), "loc_9E66")

    ChrTalk(
        0xB,
        (
            "There's a warehouse district filled with\x01",
            "abandoned buildings near downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The m-mobsters have been getting\x01",
            "into skirmishes around there lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Th-They're a pain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A0C1")

    label("loc_9E66")


    ChrTalk(
        0xB,
        (
            "There's a warehouse district filled with\x01",
            "abandoned buildings near downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The m-mobsters have been getting\x01",
            "into skirmishes around there lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Th-They're a pain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FSo, what you're saying is...\x02\x03",
            "#0001FYou're feeling the effects of Revache\x01",
            "and Heiyue's conflict down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FAnd it's gettin' in the way of your own fight\x01",
            "with the Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Their conflict is different from ours.\x01",
            "O-Ours is a fight that is necessary.\x02",
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
        "#0106FI'm not sure I can agree with you...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 3)

    label("loc_A0C1")

    Jump("loc_A7DE")

    label("loc_A0C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A2B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A153")

    ChrTalk(
        0xB,
        (
            "A-Any government official that comes\x01",
            "down here is a hypocrite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "There's no way we'd trust anybody like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2B4")

    label("loc_A153")


    ChrTalk(
        0xB,
        (
            "Government officials always decide to make their\x01",
            "rounds here when the Anniversary Festival nears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They review our business licenses and warn\x01",
            "us to be careful of tourists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Th-They're irresponsible, though. They always\x01",
            "ch-check off items they haven't actually reviewed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-Hmpf. As if I'd ever trust a bunch\x01",
            "of hypocrites like them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_A2B4")

    Jump("loc_A7DE")

    label("loc_A2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A34E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A2F7")

    ChrTalk(
        0xB,
        "I wonder what Azel's going to do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A349")

    label("loc_A2F7")


    ChrTalk(
        0xB,
        "I-I'm surprised she came here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Azel's sister is s-surprisingly bold.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_A349")

    Jump("loc_A7DE")

    label("loc_A34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A4EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A440")

    ChrTalk(
        0xFE,
        (
            "I was walking along East Street earlier when\x01",
            "a w-woman called out to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It turns out it was Azel's sister. She was\x01",
            "wondering how he was doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sh-She's worried about Azel, since\x01",
            "he was hospitalized.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A4E5")

    label("loc_A440")


    ChrTalk(
        0xFE,
        "I ran into Azel's sister on East Street.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C-Come to think of it... I feel like she was\x01",
            "staring intently at me as I left.\x01",
            "It's probably just my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4E5")

    Jump("loc_A7DE")

    label("loc_A4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A62D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A580")

    ChrTalk(
        0xB,
        "W-We still can't trust you, you dogs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You're welcome to come as you please,\x01",
            "b-but don't you dare try anything funny.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A628")

    label("loc_A580")


    ChrTalk(
        0xB,
        "Y-You're here again, you dogs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y-You definitely helped us out, but\x01",
            "Trinity is Wazy's holy ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wazy's word is absolute here.\x01",
            "D-Do you understand?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_A628")

    Jump("loc_A7DE")

    label("loc_A62D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A6EF")

    ChrTalk(
        0xB,
        (
            "D-Damn those Saber Vipers. They've\x01",
            "been holding a grudge against us ever\x01",
            "since they lost the last fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sh-Shameful cowards. There's no doubt\x01",
            "that they're the culprits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7DE")

    label("loc_A6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A75D")

    ChrTalk(
        0xB,
        (
            "Hah. I've got no desire to cooperate with\x01",
            "you d-dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "H-How about you make your exit?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7DE")

    label("loc_A75D")


    ChrTalk(
        0xB,
        (
            "Y-You'd better listen well. Trinity is\x01",
            "Wazy's holy ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You'll p-pay the price if you do anything\x01",
            "to hinder him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_A7DE")

    TalkEnd(0xFE)
    Return()

    # Function_25_92DD end

    def Function_26_A7E2(): pass

    label("Function_26_A7E2")


    ChrTalk(
        0xB,
        "I-I planned to train earlier in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-How about it? Have you ever seen\x01",
            "a thrust like mine? I bet you were\x01",
            "s-surprised, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYes. Hoorah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FI guess ya could say that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 4)
    Return()

    # Function_26_A7E2 end

    def Function_27_A8B1(): pass

    label("Function_27_A8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A95B")

    ChrTalk(
        0xB,
        (
            "I hate the mafia, but th-those guys are\x01",
            "a pain, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "W-We only just started tolerating their actions,\x01",
            "and now they're getting this carried away?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA2F")

    label("loc_A95B")


    ChrTalk(
        0xB,
        (
            "Th-The red plague has been patrolling\x01",
            "the Downtown District lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I r-ran into them three times during my daily\x01",
            "patrol yesterday. Wh-What a pain in my neck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Y-Yeah, they're definitely a pain.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_AA2F")

    Return()

    # Function_27_A8B1 end

    def Function_28_AA30(): pass

    label("Function_28_AA30")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AAC9")

    ChrTalk(
        0xC,
        "We shouldn't be fighting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, I'd do anything for the sake\x01",
            "of my companions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "We're all in this together, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_AAC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AB46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AB3E")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        "You'll get good at it if you practice, Azel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Just keep trying your hardest.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_AB41")

    label("loc_AB3E")

    Call(0, 30)

    label("loc_AB41")

    Jump("loc_BC4D")

    label("loc_AB46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_AC3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AB9B")

    ChrTalk(
        0xC,
        (
            "I may hate the Vipers, but those\x01",
            "rumors have me worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC38")

    label("loc_AB9B")


    ChrTalk(
        0xC,
        (
            "I heard a rumor that the Vipers have been\x01",
            "fighting amongst themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hate the Vipers, but I'd be lying if I said\x01",
            "I wasn't a little worried.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_AC38")

    Jump("loc_BC4D")

    label("loc_AC3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AD52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_ACCF")

    ChrTalk(
        0xC,
        (
            "Azel's worried about his family, so he\x01",
            "went back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He's managed to become a little more\x01",
            "honest with himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD4D")

    label("loc_ACCF")


    ChrTalk(
        0xC,
        (
            "Azel returned home after he heard about\x01",
            "the incident in the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "His house is pretty close to there.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_AD4D")

    Jump("loc_BC4D")

    label("loc_AD52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AE8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_ADC1")

    ChrTalk(
        0xC,
        "The Downtown District refuses to change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "That's precisely why I like it here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE8A")

    label("loc_ADC1")


    ChrTalk(
        0xC,
        (
            "Business in Crossbell appears to be\x01",
            "booming these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Day after day, all I hear about is how yet\x01",
            "another company is expanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The Downtown District is as desolate as ever,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_AE8A")

    Jump("loc_BC4D")

    label("loc_AE8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AF14")

    ChrTalk(
        0xC,
        (
            "Just another plain old relaxing day\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Days like this make me want to go out\x01",
            "on a nice, long walk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_AF14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_AFA1")

    ChrTalk(
        0xC,
        "I'm helping out with the store today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Welcome. Please speak with Abbas when\x01",
            "you're ready to place an order.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFFC")

    label("loc_AFA1")


    ChrTalk(
        0xC,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Everybody went out today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm doing my part by running the bar.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_AFFC")

    Jump("loc_BC4D")

    label("loc_B001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B0B2")

    ChrTalk(
        0xC,
        (
            "Have you ever seen Wazy when he's angry?\x01",
            "He can be pretty scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's usually because of all the women that\x01",
            "try to latch onto him like leeches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B11D")

    label("loc_B0B2")


    ChrTalk(
        0xC,
        "I feel kind of sorry for them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm sure he'll give them a swift, yet harsh\x01",
            "rejection later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_B11D")

    Jump("loc_BC4D")

    label("loc_B122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B1E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B175")

    ChrTalk(
        0xC,
        "Abbas isn't here right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'll take your order.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1E0")

    label("loc_B175")


    ChrTalk(
        0xC,
        "What would you like to have?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Abbas isn't here for the day,\x01",
            "so I'm taking orders in his place.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_B1E0")

    Jump("loc_BC4D")

    label("loc_B1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B28C")

    ChrTalk(
        0xC,
        (
            "It's a lot better to hang out here with friends\x01",
            "than it is to go back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I suppose I'm not the only person\x01",
            "in the world like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B361")

    label("loc_B28C")


    ChrTalk(
        0xC,
        (
            "A lot of people visit the Anniversary\x01",
            "Festival as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I don't have any parents, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "All I've got waiting at home for me are\x01",
            "an awful aunt and uncle.\x01",
            "I'd be fine never going home again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_B361")

    Jump("loc_BC4D")

    label("loc_B366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B429")

    ChrTalk(
        0xC,
        "Ah, it's the police.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks for your service. The world is filled with\x01",
            "all kinds of bad people, so be careful.\x01",
            "Never know what kind of person you might run into.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B42C")

    label("loc_B429")

    Call(0, 31)

    label("loc_B42C")

    Jump("loc_BC4D")

    label("loc_B431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_B467")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B45F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_B457")
    Call(0, 33)
    Jump("loc_B45A")

    label("loc_B457")

    Call(0, 32)

    label("loc_B45A")

    Jump("loc_B462")

    label("loc_B45F")

    Call(0, 33)

    label("loc_B462")

    Jump("loc_BC4D")

    label("loc_B467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B54E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B501")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_B4F9")

    ChrTalk(
        0xC,
        (
            "It gets kinda lonely when Azel's manning the counter...\x01",
            "I don't have anybody else to play billiards with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4FC")

    label("loc_B4F9")

    Call(0, 32)

    label("loc_B4FC")

    Jump("loc_B549")

    label("loc_B501")


    ChrTalk(
        0xC,
        "Hey, do you guys have time for a round?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Actually, never mind.\x02",
    )

    CloseMessageWindow()

    label("loc_B549")

    Jump("loc_BC4D")

    label("loc_B54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_B6A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B5FA")

    ChrTalk(
        0xC,
        (
            "We're planning to start patrolling\x01",
            "the Downtown District as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rest assured, we never plan on letting\x01",
            "something like that happen again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6A0")

    label("loc_B5FA")


    ChrTalk(
        0xC,
        (
            "I've spotted the mafia hanging out\x01",
            "in the Back Alley lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll never forget how they ambushed Azel.\x01",
            "Just looking at them makes me sick to my stomach.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_B6A0")

    Jump("loc_BC4D")

    label("loc_B6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B77E")

    ChrTalk(
        0xFE,
        "Azel's still out of commission for another week.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I offered to help him, but he told me he didn't want\x01",
            "me meddling in his affairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get the impression that Azel has\x01",
            "grown up a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_B77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B7FD")

    ChrTalk(
        0xC,
        "Azel really cares for his sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I imagine he feels a little guilty,\x01",
            "considering he's a troublemaker.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_B7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B945")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B8A0")

    ChrTalk(
        0xC,
        (
            "We all help out one another in our\x01",
            "times of need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That's one of the things about the Testaments\x01",
            "that I've really come to respect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B940")

    label("loc_B8A0")


    ChrTalk(
        0xC,
        (
            "Azel will need to return to the hospital for\x01",
            "regular checkups for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Don't worry, though. We all plan on\x01",
            "pitching in for the hospital bills.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_B940")

    Jump("loc_BC4D")

    label("loc_B945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BAF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_B9F3")

    ChrTalk(
        0xC,
        (
            "Azel could have died if one of his\x01",
            "vitals were hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We've been on high alert ever since the fiasco.\x01",
            "I'll be sure to pay those mobsters back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAF0")

    label("loc_B9F3")


    ChrTalk(
        0xC,
        "Azel was discharged with a clean bill of health.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um... I know it's late to say this,\x01",
            "but thank you. Truly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Azel could have died if one of his\x01",
            "vitals were hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I must offer you my gratitude for taking\x01",
            "revenge on them in our stead.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_BAF0")

    Jump("loc_BC4D")

    label("loc_BAF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_BB55")

    ChrTalk(
        0xC,
        "I wonder how Azel's doing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope he's regained consciousness\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_BB55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_BBBD")

    ChrTalk(
        0xC,
        "We're going to take revenge for our friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't even think about stopping us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC4D")

    label("loc_BBBD")


    ChrTalk(
        0xC,
        "Azel's the one that got ambushed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "We're going to take revenge for our comrade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Wazy forbade us from acting of our own accord.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_BC4D")

    TalkEnd(0xC)
    Return()

    # Function_28_AA30 end

    def Function_29_BC51(): pass

    label("Function_29_BC51")

    Call(0, 28)
    Return()

    # Function_29_BC51 end

    def Function_30_BC55(): pass

    label("Function_30_BC55")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Hey, Ryan. Anybody ever tell you that\x01",
            "you make one hell of a cocktail?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Come to think of it, you've got a solid command over\x01",
            "your hands. You play a mean game of billiards, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "You'll get good at it if you practice, Azel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Just keep trying your hardest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Y-Yeah, sure.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_30_BC55 end

    def Function_31_BD91(): pass

    label("Function_31_BD91")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        "How's your family, Azel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Don't spare me any details, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sure. I plan on spending the second half of\x01",
            "the festival with my sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I wanna use today to go out and screw\x01",
            "around with you guys.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_31_BD91 end

    def Function_32_BE83(): pass

    label("Function_32_BE83")


    ChrTalk(
        0xC,
        (
            "Thank you for earlier. I'll use our battle as a\x01",
            "reference to further develop my fighting style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope to apply what I've learned to any\x01",
            "future bouts with the Vipers.\x02",
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
        "#0006FPlease. I'd rather you didn't.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 5)
    Return()

    # Function_32_BE83 end

    def Function_33_BFC5(): pass

    label("Function_33_BFC5")


    ChrTalk(
        0xC,
        (
            "The leader of the Saber Vipers controlled\x01",
            "the Downtown District for as long as I\x01",
            "could remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "However, that all changed two years ago when Wazy\x01",
            "came out of nowhere and challenged him to a fight.\x01",
            "Wazy emerged victorious from their raging battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Following his victory, he established the Testaments\x01",
            "as a haven for those who oppose Wald's rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...Wazy is unbelievably strong.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_33_BFC5 end

    def Function_34_C154(): pass

    label("Function_34_C154")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C212")

    ChrTalk(
        0xD,
        (
            "I've gotten pretty used to working here, so I've\x01",
            "kinda lost interest in fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I gotta be honest with you. I was pretty relieved\x01",
            "when Wazy stepped in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C264")

    label("loc_C212")


    ChrTalk(
        0xD,
        "Is it true? Has Wald really grown weak?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I-I can't even imagine it...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_C264")

    Jump("loc_D066")

    label("loc_C269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C31A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C312")

    ChrTalk(
        0xD,
        (
            "I don't really get how he does it, but Ryan's\x01",
            "skilled at everything he does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm glad I've got a good friend like him\x01",
            "watching my back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C315")

    label("loc_C312")

    Call(0, 30)

    label("loc_C315")

    Jump("loc_D066")

    label("loc_C31A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C391")

    ChrTalk(
        0xD,
        (
            "Wazy earns a sizeable income with his\x01",
            "nighttime job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Can't say I'm surprised, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C40C")

    label("loc_C391")


    ChrTalk(
        0xD,
        (
            "Wazy usually works two or three nights\x01",
            "a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Apparently, he earns a sizeable income\x01",
            "from his nighttime job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_C40C")

    Jump("loc_D066")

    label("loc_C411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C4C9")

    ChrTalk(
        0xD,
        "I'm pretty experienced at working in stores.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Nothing beats the feeling of working hard to\x01",
            "earn a living. It's all thanks to you that I'm\x01",
            "able to feel this way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D066")

    label("loc_C4C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C57A")

    ChrTalk(
        0xD,
        (
            "I'm sure most of our customers are here\x01",
            "'cause they're interested in Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Is it really that surprising? The man stands out\x01",
            "like a Shining Pom.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C632")

    label("loc_C57A")


    ChrTalk(
        0xD,
        "We're seeing a sudden influx of customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Probably has to do with what happened yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We have a bunch more customers than usual\x01",
            "here right now for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_C632")

    Jump("loc_D066")

    label("loc_C637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C70B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C703")

    ChrTalk(
        0xD,
        (
            "I plan to spend the latter half of the Anniversary\x01",
            "Festival with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The Testaments don't have to work around then,\x01",
            "and I'm sure my sister will be happy to see me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C706")

    label("loc_C703")

    Call(0, 31)

    label("loc_C706")

    Jump("loc_D066")

    label("loc_C70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_C741")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_C731")
    Call(0, 37)
    Jump("loc_C734")

    label("loc_C731")

    Call(0, 36)

    label("loc_C734")

    Jump("loc_C73C")

    label("loc_C739")

    Call(0, 37)

    label("loc_C73C")

    Jump("loc_D066")

    label("loc_C741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C8ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C885")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_C86F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_C7E4")

    ChrTalk(
        0xD,
        "(This lady's kinda scary, don't you think?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "(I'm surprised she and Wazy seem to be\x01",
            "getting along just fine.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86A")

    label("loc_C7E4")


    ChrTalk(
        0xD,
        "E-Excuse me. Here's the cocktail you ordered.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Oh. Just leave it there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "U-Understood. I'll take my leave, then.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_C86A")

    Jump("loc_C880")

    label("loc_C86F")

    TurnDirection(0xD, 0x0, 0)
    Call(0, 36)
    OP_93(0xD, 0xB4, 0x0)

    label("loc_C880")

    Jump("loc_C8E8")

    label("loc_C885")


    ChrTalk(
        0xD,
        (
            "Ahem! I have some important matters to\x01",
            "tend to today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Think it's about time I get ready.\x02",
    )

    CloseMessageWindow()

    label("loc_C8E8")

    Jump("loc_D066")

    label("loc_C8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_CA86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9FB")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Let's see... I have to wipe the glasses,\x01",
            "and then check the stock...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Abbas is a strict guy. He dishes out a harsh\x01",
            "scolding whenever I mess up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never really noticed it before, but isn't he\x01",
            "kind of totally ripped?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_CA81")

    label("loc_C9FB")


    ChrTalk(
        0xFE,
        (
            "Abbas dishes out a harsh scolding whenever\x01",
            "I mess up at my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, aren't part-time jobs way harder\x01",
            "than they seem to be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA81")

    Jump("loc_D066")

    label("loc_CA86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CC7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBB8")

    ChrTalk(
        0xFE,
        "I started working a part-time job here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm thinking of saving up my money to repay\x01",
            "what my sister spent on my medical bills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't like worrying my sister, so I might\x01",
            "quit the Testaments and find a different\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But for now, I'll keep on keeping on here.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_CC79")

    label("loc_CBB8")


    ChrTalk(
        0xFE,
        (
            "I thought about it for a while, and I really\x01",
            "don't want to quit the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sister's okay with me working here,\x01",
            "so long as the mira goes to repaying\x01",
            "her for the medical bills.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC79")

    Jump("loc_D066")

    label("loc_CC7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_CCC8")

    ChrTalk(
        0xD,
        "My sister came to visit me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Wh-What should I do?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_D066")

    label("loc_CCC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_CE6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_CD7A")

    ChrTalk(
        0xD,
        (
            "After I apologize about my circumstances,\x01",
            "I'm sure she'll try and convince me to quit\x01",
            "the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "*sigh* I just can't find the right timing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE67")

    label("loc_CD7A")


    ChrTalk(
        0xD,
        (
            "I can't find the right timing to\x01",
            "apologize to my sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I thought I'd be able to offer a bit of reassurance,\x01",
            "since I've been worrying her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I guess I'll apologize to her after check-ups\x01",
            "say that I've fully recovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_CE67")

    Jump("loc_D066")

    label("loc_CE6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_CF07")

    ChrTalk(
        0xD,
        "I feel bad for worrying my sister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't feel like I've done anything wrong, but\x01",
            "it's still kind of hard to look her in the eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D066")

    label("loc_CF07")


    ChrTalk(
        0xD,
        (
            "My wound is almost done healing, so I no\x01",
            "longer need to go in for check-ups. But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I've been making my sister worried sick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "My sister's not exactly fond of the Testaments,\x01",
            "and now I've gone and gotten myself hospitalized.\x01",
            "Not only that, but I haven't been home in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "*sigh* It's going to be hard to look her in the eyes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_D066")

    TalkEnd(0xD)
    Return()

    # Function_34_C154 end

    def Function_35_D06A(): pass

    label("Function_35_D06A")

    Call(0, 34)
    Return()

    # Function_35_D06A end

    def Function_36_D06E(): pass

    label("Function_36_D06E")


    ChrTalk(
        0xD,
        "S-Sorry for causing you guys a bunch of trouble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Getting beaten to a pulp by the mafia was a\x01",
            "lesson I'll never forget. I'm going to start\x01",
            "brushing up on my self-defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOh, really? Good luck with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yep, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 6)
    Return()

    # Function_36_D06E end

    def Function_37_D164(): pass

    label("Function_37_D164")


    ChrTalk(
        0xD,
        (
            "My sister is supposedly taking some time\x01",
            "off during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I think I'll take some time off, too.\x01",
            "I want to hang out with her for a bit.\x01",
            "I'm tired of worrying her all the time.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_37_D164 end

    def Function_38_D232(): pass

    label("Function_38_D232")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D2C6")
    Jump("loc_D310")

    label("loc_D2C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D2E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D310")

    label("loc_D2E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D306")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D310")

    label("loc_D306")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D310")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_D5E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_D51F")
    SetChrSubChip(0xF, 0x1)

    ChrTalk(
        0xF,
        "Haha. Well, this deal ended ridiculously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I thought you'd be able to provide me\x01",
            "with a little bit more fun than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#0402FHahaha! You've got a wretched personality.\x01",
            "It's been one thing after another for the last week.\x01",
            "I'm surprised you kept it up for that long.\x02\x03",
            "#0404FI must admit, I was starting to get a little worried\x01",
            "there. I wasn't sure how much longer I'd be able to\x01",
            "hold out against you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What are they even talking about...?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_D5E4")

    label("loc_D51F")


    ChrTalk(
        0xF,
        "Hmm? Oh, well aren't you just a cutie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You look like you're about Jingo's age, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I own Neinvalli. It's just up the stairs.\x01",
            "Don't be afraid to drop by if you ever\x01",
            "feel like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 5)

    label("loc_D5E4")

    Jump("loc_D71C")

    label("loc_D5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D69F")

    ChrTalk(
        0xF,
        "Oh, crap. It's morning already, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Whoops! Stayed up drinking the night away...again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Is Jingo going to be fine opening the store\x01",
            "on her own?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_D71C")

    label("loc_D69F")


    ChrTalk(
        0xF,
        (
            "Haha. These guys might be lame as heck,\x01",
            "but they make a pretty good cocktail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "You guys want one? Drinks are on me.\x02",
    )

    CloseMessageWindow()

    label("loc_D71C")

    TalkEnd(0xFE)
    SetChrSubChip(0xF, 0x1)
    Return()

    # Function_38_D232 end

    def Function_39_D724(): pass

    label("Function_39_D724")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_D7CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7AA")

    ChrTalk(
        0xFE,
        "What are you planning, Azel?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did you ever stop to think about\x01",
            "how worried Eugot and I were?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_D7CF")

    label("loc_D7AA")


    ChrTalk(
        0xFE,
        "Are you listening to me, Azel?!\x02",
    )

    CloseMessageWindow()

    label("loc_D7CF")

    TalkEnd(0xFE)
    Return()

    # Function_39_D724 end

    def Function_40_D7D3(): pass

    label("Function_40_D7D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D8F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_D881")

    ChrTalk(
        0x11,
        (
            "I'm embarrassed to admit that I may have let\x01",
            "my prejudices cloud my judgment.\x02\x03",
            "They may be delinquents, but they're\x01",
            "not actually all that bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8F2")

    label("loc_D881")


    ChrTalk(
        0x11,
        (
            "Oh, boy! The festival was a ton of fun!\x02\x03",
            "They may be delinquents, but they're\x01",
            "not actually all that bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_D8F2")

    Jump("loc_DAC7")

    label("loc_D8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_D9D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_D97C")

    ChrTalk(
        0x11,
        (
            "Hahaha. Don't let your eyes deceive\x01",
            "you. I'm a pro at billiards.\x02\x03",
            "There we go! Boom, another one for me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D9D2")

    label("loc_D97C")

    TurnDirection(0x11, 0xB, 0)

    ChrTalk(
        0x11,
        (
            "Okay, it's my turn.\x02\x03",
            "Haha, look at me go! I'm a pro at billiards!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_D9D2")

    Jump("loc_DAC7")

    label("loc_D9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_DA36")

    ChrTalk(
        0x11,
        (
            "Damn, this is one swell bar. I think I'll take my\x01",
            "time enjoying this drink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAC7")

    label("loc_DA36")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x11,
        (
            "L-Let's see... One scotch, please.\x02\x03",
            "And, make it a double.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "A double scotch, then? I'll begin preparing it now.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_DAC7")

    TalkEnd(0xFE)
    Return()

    # Function_40_D7D3 end

    def Function_41_DACB(): pass

    label("Function_41_DACB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DB07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DAFF")

    ChrTalk(
        0x12,
        "N-No way, my Wazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_DB02")

    label("loc_DAFF")

    Call(0, 11)

    label("loc_DB02")

    Jump("loc_DBCF")

    label("loc_DB07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_DBCC")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x12,
        "So, Wazy isn't here today...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-Yeah, sorry about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wazy's not here right now,\x01",
            "but, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Please stop asking me the same question\x01",
            "over and over again.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_DBCF")

    label("loc_DBCC")

    Call(0, 42)

    label("loc_DBCF")

    TalkEnd(0xFE)
    Return()

    # Function_41_DACB end

    def Function_42_DBD3(): pass

    label("Function_42_DBD3")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x12,
        "Hey, isn't that him?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "That's the cool-looking pretty boy from yesterday!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Look at him, he's drinking a cocktail!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "He's soooo dreamy~ ㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_42_DBD3 end

    def Function_43_DC7E(): pass

    label("Function_43_DC7E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD12")
    Jump("loc_DD5C")

    label("loc_DD12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD5C")

    label("loc_DD32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD52")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD5C")

    label("loc_DD52")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD5C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_DC7E end

    def Function_44_DD8C(): pass

    label("Function_44_DD8C")

    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x14,
        "*sigh* Wazy's not here today, either...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Those cool eyes...\x01",
            "...that marvelous green hair...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Oh... Where could you be, my dear Wazy?\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_44_DD8C end

    def Function_45_DE27(): pass

    label("Function_45_DE27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DE6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DE67")

    ChrTalk(
        0x13,
        "Oh, how my heart aches for thee!\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE6A")

    label("loc_DE67")

    Call(0, 11)

    label("loc_DE6A")

    Jump("loc_DEB8")

    label("loc_DE6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_DEB5")

    ChrTalk(
        0x13,
        "We managed to come again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "But where's Wazy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DEB8")

    label("loc_DEB5")

    Call(0, 42)

    label("loc_DEB8")

    TalkEnd(0xFE)
    Return()

    # Function_45_DE27 end

    def Function_46_DEBC(): pass

    label("Function_46_DEBC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF50")
    Jump("loc_DF9A")

    label("loc_DF50")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF70")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF9A")

    label("loc_DF70")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF90")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF9A")

    label("loc_DF90")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF9A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_DEBC end

    def Function_47_DFCA(): pass

    label("Function_47_DFCA")

    TalkBegin(0xFE)
    SetChrSubChip(0x16, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E05B")
    SetChrSubChip(0x16, 0x1)

    ChrTalk(
        0x16,
        "Yep, I knew it. I was right all along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The Downtown District is filled with\x01",
            "nothing but poor people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E05E")

    label("loc_E05B")

    Call(0, 48)

    label("loc_E05E")

    Jump("loc_E0D7")

    label("loc_E063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E0D4")
    SetChrSubChip(0x16, 0x1)

    ChrTalk(
        0x16,
        "That's okay, though. I'm here for the thrill.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "I've had my fair share of fun already.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0D7")

    label("loc_E0D4")

    Call(0, 49)

    label("loc_E0D7")

    TalkEnd(0xFE)
    Return()

    # Function_47_DFCA end

    def Function_48_E0DB(): pass

    label("Function_48_E0DB")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x16,
        (
            "This bartender looks like he's pretty\x01",
            "rough around the edges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "You think he's a part of the mafia\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "You idiot. The mafia live in the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I'm pretty sure those guys are rich.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_48_E0DB end

    def Function_49_E1B6(): pass

    label("Function_49_E1B6")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x16,
        "Hey, this place looks pretty nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Aren't you glad we came here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I've told you this before, but you need to stop\x01",
            "wandering off on your own all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Just a fair warning. I've heard the delinquents\x01",
            "here are pretty scary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_49_E1B6 end

    def Function_50_E2B6(): pass

    label("Function_50_E2B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E377")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E36F")
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x17,
        (
            "While we're on the topic of the mafia,\x01",
            "aren't they called Revache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Aren't those guys pretty rich?\x01",
            "No way in hell they'd be in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E372")

    label("loc_E36F")

    Call(0, 48)

    label("loc_E372")

    Jump("loc_E41B")

    label("loc_E377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E418")
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x17,
        (
            "Didn't these guys get into a bit of a tussle\x01",
            "with the mafia before?\x01",
            "I've heard they're pretty ferocious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Well, not that I've seen.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E41B")

    label("loc_E418")

    Call(0, 49)

    label("loc_E41B")

    TalkEnd(0xFE)
    Return()

    # Function_50_E2B6 end

    def Function_51_E41F(): pass

    label("Function_51_E41F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30950.itc", 0x1E)
    LoadChrToIndex("chr/ch31850.itc", 0x1F)
    OP_68(12000, 1000, 12000, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -300, 0, -500, 0)
    SetChrPos(0x102, 500, 0, -500, 0)
    SetChrPos(0x103, -300, 0, -500, 0)
    SetChrPos(0x104, 500, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2600, 50, 12600, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    OP_68(4000, 1000, 7000, 8000)
    MoveCamera(25, 17, 0, 8000)
    SetCameraDistance(23500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1000, 1700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetCameraDistance(24500, 2000)

    def lambda_E61B():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E61B)

    def lambda_E635():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E635)
    Sleep(400)

    def lambda_E649():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E649)

    def lambda_E663():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E663)
    Sleep(400)

    def lambda_E677():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E677)

    def lambda_E691():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E691)
    Sleep(400)

    def lambda_E6A5():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E6A5)

    def lambda_E6BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E6BF)
    WaitChrThread(0x101, 1)

    def lambda_E6D4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E6D4)
    WaitChrThread(0x102, 1)

    def lambda_E6E5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E6E5)
    WaitChrThread(0x103, 1)

    def lambda_E6F6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E6F6)
    WaitChrThread(0x104, 1)

    def lambda_E707():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E707)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    ChrTalk(
        0x102,
        "#0400226V#0105F#6PA billiards table...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400227V#12P#0300FOh, nice. They've got a pool table here?\x01",
            "Must be one of them so-called billiards clubs.\x01",
            "Looks pretty interestin' to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400228V#6P#0200FTrinity is a legitimate operation in possession\x01",
            "of a business permit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400229V#6P#0001FWe'd better get a good look at the Testaments'\x01",
            "base of operations.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 7200, 0, 9500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    NpcTalk(
        0x9,
        "Man's Voice",
        "#0400230VWhat business do you have with us?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0xA, 7200, 0, 9500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, 7200, 0, 9500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_68(0, 1000, 3600, 3000)
    MoveCamera(45, 23, 0, 3000)
    SetCameraDistance(22500, 3000)
    BeginChrThread(0x9, 3, 0, 52)
    Sleep(700)
    BeginChrThread(0xA, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0xB, 3, 0, 54)
    Sleep(1200)

    def lambda_E9D9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E9D9)
    Sleep(300)

    def lambda_E9E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E9E9)

    def lambda_E9F6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E9F6)
    Sleep(300)

    def lambda_EA06():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_EA06)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400231VW-Wait, you're...?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Blue",
        "#0400232V#5PTh-Those police dogs?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400247V#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400234V#12P#0003FThank you for cooperating with us earlier.\x02\x03",
            "#0400235V#0000FThe sign said you were open, so I figured\x01",
            "we'd come by and have a friendly chat.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400236VH-Have you no shame?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        (
            "#0400237V#1PWhat do you want with us?! You'd better\x01",
            "have a good reason for being here!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Blue",
        (
            "#0400238V#5PW-We'll continue where we left off\x01",
            "and settle it once and for all!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400239V#5PSettle down.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    OP_0D()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400240V#1PAbbas...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Blue",
        "#0400241V#5PWh-Why are you stopping us?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        (
            "#0400242V#5PDo not forget that this is our holy ground.\x01",
            "Cease your petty arguments.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x190)

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400243V#11PWhat are your orders, Wazy?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Voice",
        "#0400244VHmm... Let's see.\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 1000, 12600, 2000)
    MoveCamera(35, 23, 0, 2000)
    SetCameraDistance(22000, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#0400245V#0404FEh. I don't see the harm in letting them stay.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400246VUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, 3600, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_EEE7():

        label("loc_EEE7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_EEE7")

    QueueWorkItem2(0x101, 2, lambda_EEE7)

    def lambda_EEF9():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EEF9)
    Sleep(50)

    def lambda_EF16():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EF16)
    Sleep(50)

    def lambda_EF33():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EF33)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    TurnDirection(0x9, 0x101, 500)

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400233V#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400248V#12P#0005FTh-Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400249V#4P#0305F(What's the matter with these people?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400250V#0106F#6P(Do they worship the ground\x01",
            "he walks on or something?)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_F038():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F038)
    Sleep(50)

    def lambda_F055():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F055)
    Sleep(50)

    def lambda_F072():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F072)
    Sleep(50)

    def lambda_F08F():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F08F)
    Sleep(1500)
    Fade(500)
    OP_68(-2500, 1100, 10700, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, -1600, 0, 6700, 0)
    SetChrPos(0x102, -600, 0, 6700, 0)
    SetChrPos(0x103, -1500, 0, 5500, 0)
    SetChrPos(0x104, -500, 0, 5500, 0)
    SetChrPos(0x9, 1000, 0, 2400, 0)
    SetChrPos(0xA, 1900, 0, 1700, 0)
    SetChrPos(0xB, 1900, 0, 500, 0)

    def lambda_F166():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F166)

    def lambda_F180():
        OP_96(0xFE, 0xFFFFF9C0, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F180)
    Sleep(50)

    def lambda_F19D():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F19D)

    def lambda_F1B7():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F1B7)

    def lambda_F1D1():
        OP_96(0xFE, 0x0, 0x0, 0x2C88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F1D1)
    Sleep(50)

    def lambda_F1EE():
        OP_96(0xFE, 0x384, 0x0, 0x29CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F1EE)

    def lambda_F208():
        OP_96(0xFE, 0x384, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F208)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x9, 1)

    def lambda_F236():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F236)
    WaitChrThread(0xA, 1)

    def lambda_F247():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F247)
    WaitChrThread(0xB, 1)

    def lambda_F258():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F258)
    SetChrFlags(0x8, 0x20)

    def lambda_F26A():
        OP_96(0xFE, 0xFFFFF63C, 0x32, 0x3070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F26A)

    def lambda_F284():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F284)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(1432, 255, 90, 0)

    AnonymousTalk(
        0x8,
        (
            "#0400251VWell? Why are you here?\x02\x03",
            "#0400252VDidn't I tell you already?\x01",
            "I don't have anything to say to\x01",
            "a bunch of dogs.\x02",
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
        (
            "#0400253V#12P#0003FJust because you don't have anything\x01",
            "to say to us, doesn't mean the opposite\x01",
            "holds true.\x02\x03",
            "#0400254V#0000FWe'd appreciate it if you could cooperate\x01",
            "with us in an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400255V#5P#0403FHeh. An investigation?\x02\x03",
            "#0400256V#0402FI'm going to cut you off and tell you that I don't\x01",
            "plan on settling our differences with the Vipers,\x01",
            "if that's your request.\x02\x03",
            "#0400257V#0404FThe residents may be bothered by our disputes,\x01",
            "but that's not our problem. They'll just have to\x01",
            "deal with it until it's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400258V#12P#0003FWe're not here to stop your dispute\x01",
            "with the Vipers.\x02\x03",
            "#0400259V#0001FWe want to know what prompted this\x01",
            "desire to wipe each other out.\x02\x03",
            "#0400260VWhat specific reason do you have?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#0400261V#5P#0400FOh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400262V#2PTh-That's...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400263V#5PSilence. Let Wazy handle this.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400264V#2PS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400265V#12P#0001FConsidering your reactions, there's more\x01",
            "to this story than meets the eye.\x02\x03",
            "#0400266VCare to share the details with us?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrPos(0x8, -2600, 0, 11500, 180)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1433, 255, 90, 0)
    Sleep(800)

    def lambda_F844():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2A94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F844)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#0400268V#0400FWhat could you hope to accomplish?\x02\x03",
            "#0400269VIf you were bracers, that'd be one thing.\x01",
            "But the police? Very unlikely.\x02\x03",
            "#0400270VDon't tell me you guys plan on helping\x01",
            "out a bunch of ruffians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400271V#12P#0006FI'll admit the police have been negligent when\x01",
            "it comes to the Downtown District.\x02\x03",
            "#0400272VAnd you're not wrong. Knowing the details\x01",
            "doesn't necessarily mean that we'd be able\x01",
            "to help you out.\x02\x03",
            "#0400273V#0000FHowever, our objectives don't fall in line with\x01",
            "the Bracer Guild. They place the safety of the\x01",
            "citizens above all else.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FA98)
    Sleep(50)

    def lambda_FAA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FAA8)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        "#0400274V#0301FWhat're you sayin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400275V#0101F#11PWait a minute, Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400276V#0404FCome on. You don't get it, do you?\x02\x03",
            "#0400277V#0402FDo you honestly think I'd graciously provide you\x01",
            "information with nothing in return? Has no one\x01",
            "taught you the concept of give and take?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400278V#12P#0004FThat's where you're wrong. You're the one\x01",
            "implying that I have nothing to give in return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400279V#0405FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400280V#12P#0001FIt's any detective's duty to shine a light\x01",
            "on the secrets shrouded deep within the\x01",
            "darkness.\x02\x03",
            "#0400281VAt least, that's what I learned growing up.\x02\x03",
            "#0400282V#0004FIf you happen to be holding any doubts\x01",
            "about this situation...\x02\x03",
            "#0400283V...then, we'll help you uncover the truth,\x01",
            "no matter what.\x02\x03",
            "#0400284V#0000FThis is what I can provide you in return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400285V#0105F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400286V#0302FImpressive speech, pal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400287V#12P#0202F...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1434, 255, 100, 0)

    ChrTalk(
        0x8,
        "#0400288V#0404FHaha...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(1431, 255, 100, 0)

    ChrTalk(
        0x8,
        "#0400289V#0409F#4SAhahahahahahahaha!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0400290V#0402FFantastic! Absolutely fantastic!\x02\x03",
            "#0400291VAn overly-dramatic speech of that\x01",
            "caliber is a rarity these days!\x02\x03",
            "#0400292V#0409FYou're Lloyd, right?! Man, I like you!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF6E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FF6E)

    def lambda_FF7B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FF7B)

    ChrTalk(
        0x101,
        (
            "#0400293V#12P#0006FI wasn't saying that just to impress you.\x02\x03",
            "#0400294V#0001FAnyway... Are you willing to share your story?\x02\x03",
            "#0400295VI'd like to learn your motivation behind wanting\x01",
            "to annihilate the Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10064():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2CEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10064)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, -2500, 50, 12400, 135)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x2)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0400296V#5P#0404F#5PHaha. All right, fine.\x02\x03",
            "#0400297VIt'd be rude of me to deny you any sincerity\x01",
            "after delivering such a gut-busting speech.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    ChrTalk(
        0x8,
        "#0400298V#5P#0402FAbbas. If you would, please.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400299V#11PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_68(-2140, 1100, 10430, 1000)

    def lambda_101BB():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_101BB)
    Sleep(150)

    def lambda_101CB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_101CB)
    Sleep(50)

    def lambda_101DB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_101DB)
    Sleep(50)

    def lambda_101EB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_101EB)
    Sleep(50)

    def lambda_101FB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_101FB)
    WaitChrThread(0x104, 2)
    Sleep(1000)

    NpcTalk(
        0x9,
        "Bald Man",
        "#0400300V#5PI have yet to introduce myself.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Bald Man",
        (
            "#0400301V#5PMy name is Abbas, and I am\x01",
            "a member of the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400302V#1B#6Z#30B#39Z#61B#85Z#6P#0005FO-Oh... Pleased to meet you.\x02\x03",
            "#0L#0400303V#0B#20Z#61B#100Z#0001F(He's huge. Just who is he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400304V#5PThe incident responsible for our dispute\x01",
            "occurred five nights ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400305V#5POne of our members was ambushed\x01",
            "by the Vipers in a nearby alleyway.\x02",
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
        "#0400306V#6P#0007FAmbushed?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400307V#6P#0101FWould you say that it wasn't\x01",
            "just a normal, everyday fight?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400308V#11PHow could it have been a normal fight?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        (
            "#0400309V#11PHe took a heavy blow to the back of his\x01",
            "head and was beaten by a group of guys\x01",
            "well after he lost consciousness!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Blue",
        "#0400310VThe whole thing was one-sided from start to finish...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Blue",
        (
            "#0400311VThey beat him so bad that he was sent\x01",
            "to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400312V#12P#0306FDamn. No mercy at all, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400313V#6P#0001FSo, how's the victim doing now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400314V#5PAccording to the latest report from the hospital,\x01",
            "he has yet to regain consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400315V#5PThe doctor has finished treating his wounds,\x01",
            "but he did suffer a heavy blow to his head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400316V#5PWe are currently waiting for any further\x01",
            "updates from the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400351V#6P#0003FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400318V#6P#0101FExcuse me. Did you attempt to contact\x01",
            "the police at any point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400319V#5PWhy would we do that? They are unlikely\x01",
            "to offer any assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400320V#5PRegardless, the culprit is already obvious.\x01",
            "Calling the police would only serve to\x01",
            "interfere with our plans to enact revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400321V#6P#0108FOh.\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0400322V#6P#0205FI would like to ask a question.\x02\x03",
            "#0400323V#0200FIf the victim has yet to regain consciousness...\x02\x03",
            "#0400324V...to what degree of certainty can you claim\x01",
            "the Saber Vipers are the culprits, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0400325V#6P#0005FHey, she's right...\x02\x03",
            "#0400326VDon't tell me you guys determined that\x01",
            "using your own biased deductions.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#0400327V#5P#0404FHeh. As if we're that stupid.\x02\x03",
            "#0400328V#0402FUnlike those meatheads, we're actually\x01",
            "fairly intelligent.\x02\x03",
            "#0400329V#0409FThough I suppose you may find that\x01",
            "hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0400330V#11PWazy...!\x02",
    )

    CloseMessageWindow()

    def lambda_10BBD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10BBD)
    Sleep(50)

    def lambda_10BCD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10BCD)
    Sleep(50)

    def lambda_10BDD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10BDD)
    Sleep(50)

    def lambda_10BED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10BED)

    ChrTalk(
        0x8,
        (
            "#0400331V#5P#0404FWe've got good reason to be damn sure\x01",
            "that they're the culprits.\x02\x03",
            "#0400332V#0400FI'm sure you've got it all figured out, too.\x01",
            "Care to tell us your answer, Mr. Detective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400333V#12P#0003FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The location of the assault]\x01",           # 0
            "[The wounds on the victim]\x01",              # 1
            "[The footprints left at the scene]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10D72"),
        (1, "loc_10FD7"),
        (2, "loc_11164"),
        (SWITCH_DEFAULT, "loc_11498"),
    )


    label("loc_10D72")


    ChrTalk(
        0x101,
        (
            "#0400334V#12P#0001FYou were able to discern the identity\x01",
            "of the assailants based on the location\x01",
            "of the attack, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400335V#5P#0406FWell. I did mention that the ambush\x01",
            "took place in the nearby alleyway.\x02\x03",
            "#0400336V#0400FWhile the Vipers may walk through\x01",
            "there often, that's not the decisive\x01",
            "evidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400337V#12P#0005FO-Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400352V#5POur deciding factor was the type of\x01",
            "wound inflicted on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400353V#5PWhile most of the injuries were bumps and\x01",
            "bruises, there were also a few lacerations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400354V#5PThe weapon used had to have\x01",
            "been both blunt and serrated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11498")

    label("loc_10FD7")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0400341V#12P#0008FHere's what I was thinking...\x02\x03",
            "#0400342V#0001FYou were able to discern their identities\x01",
            "by the type of wound inflicted, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400343V#5P#0409FRight you are, my friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400344V#5PWhile most of the injuries were bumps and\x01",
            "bruises, there were also a few lacerations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400345V#5PThe weapon used had to have\x01",
            "been both blunt and serrated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11498")

    label("loc_11164")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0400346V#12P#0008FBoth of your groups wear coordinated\x01",
            "outfits, including your footwear.\x02\x03",
            "#0400347V#0001FWere you able to discern their identity based\x01",
            "off the footprints left at the scene of the crime?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400348V#5P#0405FHeh. Pretty interesting take.\x02\x03",
            "#0400349V#0406FThe road down here is comprised mostly of\x01",
            "old stone, so footprints aren't clearly visible.\x02\x03",
            "#0400350V#0400FMoreover, the Vipers pass by there often enough\x01",
            "that the presence of their footprints fails to\x01",
            "implicate them in the crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400317V#12P#0005FO-Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400338V#5POur deciding factor was the type\x01",
            "of wound inflicted on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400339V#5PWhile most of the injuries were bumps and\x01",
            "bruises, there were also a few lacerations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0400340V#5PThe weapon used had to have\x01",
            "been both blunt and serrated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11498")

    label("loc_11498")


    ChrTalk(
        0x102,
        (
            "#0400355V#0105F#12PWounds from a blunt weapon accompanied\x01",
            "by lacerations from a sharp weapon...\x02\x03",
            "#0400356V#0101FOh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400357V#0301F#12PGot'cha. You figure it was done by a nail\x01",
            "bat like we saw one of them usin' earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400358V#6P#0204FThe wounds inflicted on him could certainly\x01",
            "serve as decisive pieces of evidence.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0400359V#12P#0003FOkay, I think I've written down everything\x01",
            "I need.\x02\x03",
            "#0400360V#0000FThanks. This information should prove\x01",
            "useful in our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400361V#5P#0405FSure, no problem. Are you fine with\x01",
            "just this, though?\x02\x03",
            "#0400362VAre you not going to beg me to not\x01",
            "exact my revenge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400363V#12P#0006FI'd obviously love for you to refrain from\x01",
            "carrying out your plans against the Vipers...\x02\x03",
            "#0400364V#0001FBut I still don't have enough information to\x01",
            "come to a conclusion yet.\x02\x03",
            "#0400365VWe need to pay the Saber Vipers a visit and\x01",
            "hear their side of the story first. If we learn\x01",
            "anything new, we'll let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400366V#5P#0404FMakes sense. Looks like you're dead set on\x01",
            "carrying out this little investigation of yours,\x01",
            "Mr. Detective.\x02\x03",
            "#0400367V#0402FI suppose I should wait in anticipation for\x01",
            "you to return with interesting information.\x02\x03",
            "#0400368V#0409FAnd don't forget: If your investigation fails,\x01",
            "this district will be engulfed in a bloodbath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400369V#12P#0003FI'll keep that in mind.\x02\x03",
            "#0400370V#0000FI'll be sure to bring you back information\x01",
            "that won't leave you disappointed.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -2600, 50, 12600, 0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    OP_4C(0x9, 0xFF)
    SetChrPos(0xA, 2950, 30, 6580, 180)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xB, 10230, 0, 4410, 90)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_68(0, 1100, 9500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 9500, 180)
    SetChrPos(0x1, 0, 0, 9500, 180)
    SetChrPos(0x2, 0, 0, 9500, 180)
    SetChrPos(0x3, 0, 0, 9500, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x42, 1)
    OP_29(0x3E, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_51_E41F end

    def Function_52_11B89(): pass

    label("Function_52_11B89")


    def lambda_11B8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11B8E)

    def lambda_11B9F():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11B9F)
    WaitChrThread(0xFE, 1)

    def lambda_11BBD():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11BBD)
    WaitChrThread(0xFE, 1)

    def lambda_11BDB():
        OP_95(0xFE, 0, 0, 4800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11BDB)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)
    Return()

    # Function_52_11B89 end

    def Function_53_11BFC(): pass

    label("Function_53_11BFC")


    def lambda_11C01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11C01)

    def lambda_11C12():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11C12)
    WaitChrThread(0xFE, 1)

    def lambda_11C30():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11C30)
    WaitChrThread(0xFE, 1)

    def lambda_11C4E():
        OP_95(0xFE, -600, 0, 6100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11C4E)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_53_11BFC end

    def Function_54_11C6F(): pass

    label("Function_54_11C6F")


    def lambda_11C74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11C74)

    def lambda_11C85():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11C85)
    WaitChrThread(0xFE, 1)

    def lambda_11CA3():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11CA3)
    WaitChrThread(0xFE, 1)

    def lambda_11CC1():
        OP_95(0xFE, 700, 0, 6700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11CC1)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_54_11C6F end

    def Function_55_11CE2(): pass

    label("Function_55_11CE2")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x0, 0x9, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2960, 1100, 12800, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25980, 0)
    SetChrPos(0x101, 2740, 0, 11700, 0)
    SetChrPos(0x102, 1500, 0, 10260, 0)
    SetChrPos(0x103, 1500, 0, 11700, 0)
    SetChrPos(0x104, 2740, 0, 10260, 0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#5PFinally. You've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F#11PYOU requested us, didn't you?\x02\x03",
            "#0001FIt sounds like you want us to train the Testaments.\x01",
            "That's a bit of a risky request, don't you think?\x02\x03",
            "What makes you so sure that we'd train\x01",
            "a bunch of delinquents anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FNot only that, but I was expecting to see\x01",
            "Wazy's name on the request. Was this\x01",
            "all your idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PHmm. I believe you've misunderstood\x01",
            "the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PGive me a moment. I will explain\x01",
            "the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_11F61():

        label("loc_11F61")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_11F61")

    QueueWorkItem2(0x0, 1, lambda_11F61)

    def lambda_11F73():

        label("loc_11F73")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_11F73")

    QueueWorkItem2(0x1, 1, lambda_11F73)

    def lambda_11F85():

        label("loc_11F85")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_11F85")

    QueueWorkItem2(0x2, 1, lambda_11F85)

    def lambda_11F97():

        label("loc_11F97")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_11F97")

    QueueWorkItem2(0x3, 1, lambda_11F97)

    def lambda_11FA9():
        OP_95(0xFE, 7550, 0, 14780, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_11FA9)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x9, 0x0)
    OP_68(1290, 1000, 9450, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0x9, 3060, 0, 8960, 270)
    SetChrPos(0x101, 700, 0, 9600, 90)
    SetChrPos(0x102, 560, 0, 8000, 90)
    SetChrPos(0x103, -990, 0, 8000, 90)
    SetChrPos(0x104, -990, 0, 9600, 90)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, 14390, 0, 7400, 178)
    SetChrPos(0xC, 14000, 0, 7400, 268)
    SetChrPos(0xA, 9250, 0, 4150, 225)
    SetChrPos(0xB, 5000, 0, 2000, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11PIt's not particularly complicated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI would like to request a lesson in the art\x01",
            "of self-defense for our members.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0305FYou wanna be taught self-defense?\x02\x03",
            "#0301FThe hell? You plannin' on using our\x01",
            "teachings in your brawls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PAgain. Please do not misunderstand the request.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PLet us suppose that the mafia assaults us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FWhen you say the mafia, are you referring to\x01",
            "Revache or Heiyue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FIs this all related to the increased tensions\x01",
            "between them? We've noticed them getting\x01",
            "into more fights lately.\x02\x03",
            "#0103FI've heard they've even engaged in\x01",
            "gunfights. Luckily, it doesn't seem\x01",
            "to be frequent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PPrecisely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe Downtown District also happens to be\x01",
            "in the line of fire at times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere's a warehouse district nearby filled\x01",
            "with abandoned buildings and empty\x01",
            "plots of land. It's perfect for fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'm not pleased with the situation we've\x01",
            "been placed in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FThus, fueling your desire to learn self-defense.\x02\x03",
            "#0200FI do seem to recall one of your members\x01",
            "suffering from obnubilation for a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0001FIt all makes sense, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'm glad you catch on quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWazy is typically tasked with giving our\x01",
            "members lessons in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHowever, his fighting style is too unique.\x01",
            "It requires a flexible body and a strong\x01",
            "affinity for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHence why we've come to you,\x01",
            "Lloyd Bannings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe skills you've displayed boast defensive\x01",
            "prowess, while being easy to learn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMay I humbly request you once again\x01",
            "show our members your skills in a real\x01",
            "test of combat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNaturally, I don't expect them to master it in a day.\x01",
            "However, having first-hand experience would be\x01",
            "good incentive to try picking it up.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    def lambda_1288D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1288D)
    Sleep(10)

    def lambda_1289D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1289D)

    def lambda_128AA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_128AA)

    def lambda_128B7():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_128B7)
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#12P#0100FI'm glad that the request doesn't have\x01",
            "any nefarious intentions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FAgreed. I take no issues in accepting their request.\x02\x03",
            "#0200FWhat are your thoughts, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FA lesson in self-defense?\x01",
            "Hmm...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_129AF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_129AF)
    Sleep(50)

    def lambda_129BF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129BF)

    def lambda_129CC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_129CC)

    def lambda_129D9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_129D9)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#0001FI wouldn't necessarily call it self-defense.\x01",
            "It's a suppression technique taught at\x01",
            "the police academy.\x02\x03",
            "That being said, is that fine with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI take no issue with it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt is only for training purposes, so I intended to\x01",
            "allow your comrades to aid you in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003FHmm...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B79")
    OP_29(0x12, 0x1, 0x1)
    Call(0, 56)
    Return()

    label("loc_12B79")


    ChrTalk(
        0x101,
        (
            "#6P#0001FCould you give us a bit? We still need\x01",
            "time to get ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe are free all day. You would be wise to\x01",
            "fully prepare yourselves before accepting.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xD, 12470, 0, 16210, 180)
    SetChrPos(0xC, 14030, 30, 11040, 270)
    SetChrPos(0xA, 2950, 30, 6580, 180)
    SetChrPos(0xB, 10230, 0, 4410, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_12CAD")
    SetChrPos(0xD, -4000, 0, 16690, 0)

    label("loc_12CAD")

    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0x0, 600, 0, 8000, 90)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    OP_4C(0x9, 0xFF)
    BeginChrThread(0x9, 0, 0, 0)
    OP_29(0x12, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_55_11CE2 end

    def Function_56_12CEB(): pass

    label("Function_56_12CEB")

    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xD, 0x2)

    ChrTalk(
        0x101,
        (
            "#6P#0003FNow that we've heard your circumstances,\x01",
            "we have no reason to refuse your request.\x02\x03",
            "#0000FNot only that, but this is a good opportunity\x01",
            "for me to brush up my skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FHeh. Figures you'd say that.\x02\x03",
            "#0300FMay have some trouble taking 'em all on\x01",
            "at once, Lloyd. Might wanna get some\x01",
            "help from us, pal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12E4E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12E4E)

    def lambda_12E5B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12E5B)

    def lambda_12E68():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12E68)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#11P#0000FFor sure. I'll be counting on you guys\x01",
            "to back me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIt's been settled, then.\x02",
    )

    CloseMessageWindow()

    def lambda_12EDF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12EDF)

    def lambda_12EEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12EEC)

    def lambda_12EF9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12EF9)
    Sleep(300)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(500)

    ChrTalk(
        0x9,
        "#5P#4SEverybody, assemble!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(2240, 1100, 7350, 4200)
    MoveCamera(79, 30, 0, 4200)
    OP_6E(260, 4200)
    SetCameraDistance(32250, 4200)
    BeginChrThread(0xA, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 58)
    Sleep(400)
    BeginChrThread(0xD, 0, 0, 57)
    Sleep(300)
    BeginChrThread(0xB, 0, 0, 60)

    def lambda_12F83():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12F83)
    Sleep(10)

    def lambda_12F93():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12F93)

    def lambda_12FA0():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12FA0)
    Sleep(8)

    def lambda_12FB0():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12FB0)
    WaitChrThread(0xD, 0)
    Sleep(700)

    ChrTalk(
        0x9,
        (
            "#5PThe Testaments will now engage in a\x01",
            "series of practice fights with the SSS!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 60, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#5SJa!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Testaments Training]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_12CEB end

    def Function_57_130B1(): pass

    label("Function_57_130B1")

    OP_95(0xD, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xD, 2880, 30, 6910, 2000, 0x0)
    OP_93(0xD, 0x13B, 0x190)
    Return()

    # Function_57_130B1 end

    def Function_58_130E1(): pass

    label("Function_58_130E1")

    OP_95(0xC, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xC, 2180, 0, 6080, 2000, 0x0)
    OP_93(0xC, 0x13B, 0x190)
    Return()

    # Function_58_130E1 end

    def Function_59_13111(): pass

    label("Function_59_13111")

    OP_95(0xA, 9250, 0, 7400, 2000, 0x0)
    OP_95(0xA, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xA, 1330, 0, 5310, 2000, 0x0)
    OP_93(0xA, 0x13B, 0x190)
    Return()

    # Function_59_13111 end

    def Function_60_13155(): pass

    label("Function_60_13155")

    OP_95(0xB, 2460, 20, 2000, 2000, 0x0)
    OP_95(0xB, 2460, 20, 4550, 2000, 0x0)
    OP_95(0xB, 490, 0, 4550, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x190)
    Return()

    # Function_60_13155 end

    SaveToFile()

Try(main)
