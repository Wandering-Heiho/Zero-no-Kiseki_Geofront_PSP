from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2510.bin",                # FileName
        "t2510",                    # MapName
        "t2510",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2510",                  # 0
        "Guardsman Oliver",       # 1
        "Guardsman Jack",         # 2
        "Guardsman Alexei",       # 3
        "Temas",                  # 4
        "Rog",                    # 5
        "Tourist",                # 6
        "Merchant",               # 7
        "Boy",                    # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Merchant",               # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Tourist",                # 17
        "Tourist",                # 18
        "Tourist",                # 19
        "Tourist",                # 20
        "Tourist",                # 21
        "Merchant",               # 22
        "Tourist",                # 23
        "Tourist",                # 24
        "Tourist",                # 25
        "Tourist",                # 26
        "Harold",                 # 27
        "Chiruru",                # 28
        "Bracer Scott",           # 29
        "Bracer Wenzel",          # 30
        "Bracer Lynn",            # 31
        "Bracer Aeolia",          # 32
        "車１",                   # 33
        "Sergeant Major Seeker",  # 34
        "Black-Haired Woman",     # 35
        "Old Lady",               # 36
        "Old Man",                # 37
        "Merchant",               # 38
        "Woman",                  # 39
        "Older Brother",          # 40
        "Younger Sister",         # 41
        "Father",                 # 42
        "Boy",                    # 43
        "Bus",                    # 44
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31302.itc",                   # 01
        "chr/ch25000.itc",                   # 02
        "chr/ch31300.itc",                   # 03
        "chr/ch23400.itc",                   # 04
        "chr/ch21202.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21402.itc",                   # 07
        "chr/ch21900.itc",                   # 08
        "chr/ch21200.itc",                   # 09
        "chr/ch21100.itc",                   # 0A
        "chr/ch20500.itc",                   # 0B
        "chr/ch20802.itc",                   # 0C
        "chr/ch21002.itc",                   # 0D
        "chr/ch21102.itc",                   # 0E
        "chr/ch21800.itc",                   # 0F
        "chr/ch21602.itc",                   # 10
        "chr/ch09300.itc",                   # 11
        "chr/ch21600.itc",                   # 12
        "chr/ch27202.itc",                   # 13
        "chr/ch27302.itc",                   # 14
        "chr/ch32002.itc",                   # 15
        "chr/ch32102.itc",                   # 16
        "chr/ch00800.itc",                   # 17
        "chr/ch07300.itc",                   # 18
        "chr/ch24100.itc",                   # 19
        "chr/ch20800.itc",                   # 1A
        "chr/ch33000.itc",                   # 1B
        "chr/ch24500.itc",                   # 1C
        "chr/ch21300.itc",                   # 1D
        "chr/ch21400.itc",                   # 1E
        "chr/ch07302.itc",                   # 1F
        "chr/ch24102.itc",                   # 20
        "chr/ch21302.itc",                   # 21
        "chr/ch21402.itc",                   # 22
    ))

    DeclNpc(7780,    0,       6809,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4280,   0,       5130,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(95629,   150,     2380,    270,  341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(106529,  0,       1980,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(163020,  0,       -2410,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(102949,  150,     3920,    270,  469,  0x0, 0,   5,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   6,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(98620,   150,     -2180,   90,   469,  0x0, 0,   7,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   8,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-660,    0,       6809,    180,  385,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(100970,  150,     -3950,   270,  469,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-4150,   0,       3960,    0,    401,  0x0, 0,   10,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(6650,    0,       -2170,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(7519,    0,       5110,    0,    401,  0x0, 0,   18,  0,   0,   0,   0,   5,   255,  0)
    DeclNpc(98620,   150,     -3950,   90,   469,  0x0, 0,   5,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(8100,    0,       -3130,   0,    401,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(1539,    0,       2160,    180,  401,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(-8500,   0,       3460,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   469,  0x0, 0,   13,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(102949,  150,     2150,    270,  469,  0x0, 0,   14,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(6960,    0,       2359,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(98620,   150,     -2180,   90,   469,  0x0, 0,   16,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(7489,    0,       2099,    180,  385,  0x0, 0,   15,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(6349,    0,       2099,    180,  385,  0x0, 0,   8,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(98620,   150,     -3950,   90,   469,  0x0, 0,   5,   0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-16989,  0,       -6710,   135,  389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(156389,  0,       -3119,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  469,  0x0, 0,   19,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(100569,  150,     3920,    90,   469,  0x0, 0,   20,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(100599,  109,     4019,    90,   469,  0x0, 0,   21,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  469,  0x0, 0,   22,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(7000,    0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-59,     0,       -5000,   0,    389,  0x0, 0,   23,  0,   0,   0,   0,   37,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   24,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  405,  0x0, 0,   25,  0,   255, 255, 0,   39,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   26,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   27,  0,   255, 255, 0,   41,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  389,  0x0, 0,   28,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   9,   0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   29,  0,   255, 255, 0,   44,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   6,   0,   255, 255, 0,   45,  255,  0)
    DeclNpc(-2309,   0,       6309,    180,  469,  0x0, 0,   30,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 71,  95.81999969482422,     -8.289999961853027,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -47.90999984741211,    4.144999980926514,     -0.0,                  1.0])
    DeclEvent(0x0000, 0, 72,  89.77999877929688,     -0.11999999731779099,  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   -44.88999938964844,    0.05999999865889549,   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 73,  -8.050000190734863,    10.380000114440918,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   4.025000095367432,     -5.190000057220459,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 74,  -0.05000000074505806,  10.520000457763672,    0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   0.02500000037252903,   -5.260000228881836,    -0.0,                  1.0])

    DeclActor(7580,    0,       5630,    1000,    7780,    1500,    6810,    0x007E, 0,  4,  0x0000)
    DeclActor(105420,  0,       1980,    1000,    106530,  1500,    1980,    0x007E, 0,  8,  0x0000)
    DeclActor(161990,  0,       -2450,   1000,    163020,  1500,    -2410,   0x007E, 0,  11, 0x0000)
    DeclActor(-1750,   0,       -12300,  1000,    -1750,   1000,    -12300,  0x007C, 0,  75, 0x0000)

    ScpFunction((
        "Function_0_930",          # 00, 0
        "Function_1_9E8",          # 01, 1
        "Function_2_A13",          # 02, 2
        "Function_3_C39",          # 03, 3
        "Function_4_E46",          # 04, 4
        "Function_5_E4A",          # 05, 5
        "Function_6_1CAD",         # 06, 6
        "Function_7_21B4",         # 07, 7
        "Function_8_2CFA",         # 08, 8
        "Function_9_2CFE",         # 09, 9
        "Function_10_39AC",        # 0A, 10
        "Function_11_3B72",        # 0B, 11
        "Function_12_3B76",        # 0C, 12
        "Function_13_43E8",        # 0D, 13
        "Function_14_4558",        # 0E, 14
        "Function_15_46B6",        # 0F, 15
        "Function_16_4760",        # 10, 16
        "Function_17_4914",        # 11, 17
        "Function_18_4967",        # 12, 18
        "Function_19_4A98",        # 13, 19
        "Function_20_4C8C",        # 14, 20
        "Function_21_4CBD",        # 15, 21
        "Function_22_4CF1",        # 16, 22
        "Function_23_4E4B",        # 17, 23
        "Function_24_4EEA",        # 18, 24
        "Function_25_50BA",        # 19, 25
        "Function_26_50EF",        # 1A, 26
        "Function_27_51C2",        # 1B, 27
        "Function_28_546F",        # 1C, 28
        "Function_29_5542",        # 1D, 29
        "Function_30_5633",        # 1E, 30
        "Function_31_5795",        # 1F, 31
        "Function_32_5914",        # 20, 32
        "Function_33_59FA",        # 21, 33
        "Function_34_5E49",        # 22, 34
        "Function_35_5FE0",        # 23, 35
        "Function_36_6426",        # 24, 36
        "Function_37_6777",        # 25, 37
        "Function_38_680C",        # 26, 38
        "Function_39_6DD0",        # 27, 39
        "Function_40_7324",        # 28, 40
        "Function_41_77CE",        # 29, 41
        "Function_42_7BE4",        # 2A, 42
        "Function_43_8137",        # 2B, 43
        "Function_44_8644",        # 2C, 44
        "Function_45_880B",        # 2D, 45
        "Function_46_8C99",        # 2E, 46
        "Function_47_8F4B",        # 2F, 47
        "Function_48_9DA6",        # 30, 48
        "Function_49_9DC5",        # 31, 49
        "Function_50_9DE4",        # 32, 50
        "Function_51_9E03",        # 33, 51
        "Function_52_9E22",        # 34, 52
        "Function_53_9ED7",        # 35, 53
        "Function_54_9FA1",        # 36, 54
        "Function_55_A03F",        # 37, 55
        "Function_56_A0AF",        # 38, 56
        "Function_57_A1B8",        # 39, 57
        "Function_58_A1B9",        # 3A, 58
        "Function_59_AB3A",        # 3B, 59
        "Function_60_AB59",        # 3C, 60
        "Function_61_AB78",        # 3D, 61
        "Function_62_AB97",        # 3E, 62
        "Function_63_ABB6",        # 3F, 63
        "Function_64_ABE6",        # 40, 64
        "Function_65_AC52",        # 41, 65
        "Function_66_ACA3",        # 42, 66
        "Function_67_AD12",        # 43, 67
        "Function_68_AD63",        # 44, 68
        "Function_69_ADE3",        # 45, 69
        "Function_70_AE3E",        # 46, 70
        "Function_71_AE68",        # 47, 71
        "Function_72_AF54",        # 48, 72
        "Function_73_B040",        # 49, 73
        "Function_74_B0AD",        # 4A, 74
        "Function_75_B11A",        # 4B, 75
    ))


    def Function_0_930(): pass

    label("Function_0_930")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_970"),
        (1, "loc_97C"),
        (2, "loc_988"),
        (3, "loc_994"),
        (4, "loc_9A0"),
        (5, "loc_9AC"),
        (6, "loc_9B8"),
        (SWITCH_DEFAULT, "loc_9C4"),
    )


    label("loc_970")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_97C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_988")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_994")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9D0")

    label("loc_9E7")

    Return()

    # Function_0_930 end

    def Function_1_9E8(): pass

    label("Function_1_9E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A12")
    OP_94(0xFE, 0xFFFFF178, 0x1360, 0x8C0, 0x1EDC, 0x3E8)
    Sleep(450)
    Jump("Function_1_9E8")

    label("loc_A12")

    Return()

    # Function_1_9E8 end

    def Function_2_A13(): pass

    label("Function_2_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A30")
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    Jump("loc_BDE")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A4D")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_BDE")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A74")
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_BDE")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x9, 7150, 0, -1840, 0)
    Jump("loc_BDE")

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_ABA")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_BDE")

    label("loc_ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AD2")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 47)

    label("loc_AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AFE")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x9, -4280, 0, 5130, 180)
    Jump("loc_B66")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_B30")
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, 1720, 0, 7110, 270)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_B66")

    label("loc_B30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B4A")
    SetChrFlags(0xA, 0x80)
    Call(0, 56)
    Jump("loc_B66")

    label("loc_B4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_B66")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x29, 0x80)

    label("loc_B66")

    Jump("loc_BDE")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B98")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    BeginChrThread(0x11, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_BDE")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BD0")
    SetChrPos(0x9, 7150, 0, -1840, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    Jump("loc_BDE")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BDE")
    ClearChrFlags(0xD, 0x80)

    label("loc_BDE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C38")
    Event(0, 58)

    label("loc_C38")

    Return()

    # Function_2_A13 end

    def Function_3_C39(): pass

    label("Function_3_C39")

    OP_70(0x6, 0x8C)
    OP_78(0x4, 0x28)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_CA2")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CC9")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D0B")
    ClearMapObjFlags(0x4, 0x4)
    SetChrPos(0x28, -8690, 0, 220, 0)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Jump("loc_DB7")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D38")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_DB7")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_DB7")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D74")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_D74")

    Jump("loc_DB7")

    label("loc_D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D87")
    Jump("loc_DB7")

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_DAE")
    ClearMapObjFlags(0x4, 0x4)
    OP_D3(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    Jump("loc_DB7")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_DB7")

    label("loc_DB7")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DD8")
    Jump("loc_DE7")

    label("loc_DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DE7")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_DE7")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E0C")
    Jump("loc_E45")

    label("loc_E0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_E2E")
    SetMapObjFlags(0x4, 0x4)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    Jump("loc_E45")

    label("loc_E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_E45")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E45")

    Return()

    # Function_3_C39 end

    def Function_4_E46(): pass

    label("Function_4_E46")

    Call(0, 5)
    Return()

    # Function_4_E46 end

    def Function_5_E4A(): pass

    label("Function_5_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E60")
    TalkBegin(0x15)
    Jump("loc_E8F")

    label("loc_E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E76")
    TalkBegin(0x10)
    Jump("loc_E8F")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8C")
    TalkBegin(0xE)
    Jump("loc_E8F")

    label("loc_E8C")

    TalkBegin(0x8)

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_108E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC0")

    ChrTalk(
        0x8,
        (
            "These inspections are going to go perfectly\x01",
            "today. At least, that's what I'm planning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The top brass is rotten to the core.\x01",
            "We can't even keep some people\x01",
            "behind bars, no matter how hard we try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, despite all that...I don't think our work\x01",
            "here is meaningless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1089")

    label("loc_FC0")


    ChrTalk(
        0x8,
        (
            "There are some criminals that always elude\x01",
            "justice, thanks to our lousy commander and\x01",
            "his love for bribes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, if we continue to press on, I'm sure that\x01",
            "our efforts here will be worthwhile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1089")

    Jump("loc_1C67")

    label("loc_108E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1191")

    ChrTalk(
        0x8,
        (
            "We actually find loads of contraband during\x01",
            "our inspections here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...but too often, all it takes is a bribe to the\x01",
            "commander for them to be on their way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A system that turns a blind eye to evil when\x01",
            "shown some mira isn't moral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C67")

    label("loc_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1410")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DD")

    ChrTalk(
        0x8,
        "Sergeant Major Seeker, are they the ones...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FThat's right. This is the\x01",
            "Special Support Section.\x02\x03",
            "They'll be assisting the CGF with the\x01",
            "investigation of the temple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Understood. I want to apologize, though.\x01",
            "If we weren't so useless, then you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FPlease, don't worry about it. Jobs like this\x01",
            "have become commonplace for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FHaha, ain't that the truth.\x02\x03",
            "#0300FYou can leave this to us, man. You just\x01",
            "keep guardin' the gate, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah, I will. From all of us at Tangram\x01",
            "Gate, please keep the sergeant major safe.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_140B")

    label("loc_13DD")


    ChrTalk(
        0x8,
        "Please, take care of the sergeant major.\x02",
    )

    CloseMessageWindow()

    label("loc_140B")

    Jump("loc_1C67")

    label("loc_1410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14BA")

    ChrTalk(
        0x8,
        (
            "These orbal car inspections are going to\x01",
            "be pretty annoying, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And I was counting on Jack to give me\x01",
            "a hand with this, but now he's tied up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C67")

    label("loc_14BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1634")
    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157F")

    ChrTalk(
        0x8,
        "Okay, looks good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The regularly scheduled bus to Calvard\x01",
            "will arrive in roughly 40 minutes. Please\x01",
            "wait a little longer, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "Thanks for the info.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1627")

    label("loc_157F")


    ChrTalk(
        0x8,
        (
            "If you want to kill some time, how about\x01",
            "you grab a meal over in the mess hall?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "You know, I might just do that. My stomach\x01",
            "has been growling for a while now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1627")

    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    Jump("loc_1C67")

    label("loc_1634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1887")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(
        0x8,
        (
            "Jack left around noon to Crossbell City\x01",
            "in order to check on the freight's cargo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He was lucky to avoid all of that mess\x01",
            "with the counterfeit dealer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_16EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_17F4")

    ChrTalk(
        0x8,
        (
            "You know, it's near impossible to tell apart\x01",
            "counterfeit dealers from ordinary travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From my own experiences, I've found that the real\x01",
            "bad guys are best at pretending to be good ones.\x01",
            "You always have to keep your wits about you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1882")

    label("loc_17F4")


    ChrTalk(
        0x8,
        (
            "The bus coming from Calvard should be arriving\x01",
            "just a bit past noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm... Things are probably going to pick up\x01",
            "when it gets here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1882")

    Jump("loc_1C67")

    label("loc_1887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A03")
    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1965")

    ChrTalk(
        0x8,
        (
            "If you don't mind signing here...and here\x01",
            "on the entry application...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "There...there. Am I good to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, I believe so. Have a wonderful\x01",
            "time at the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F6")

    label("loc_1965")


    ChrTalk(
        0x8,
        (
            "If you head west along the highway,\x01",
            "you'll eventually hit Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Have a great time at the festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Haha. Oh, I plan to.\x02",
    )

    CloseMessageWindow()

    label("loc_19F6")

    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    Jump("loc_1C67")

    label("loc_1A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B32")
    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0x8,
        (
            "I'm going to give your cargo one last\x01",
            "inspection, just to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I know this might be a nuisance, but I assure\x01",
            "you, this is all according to our regulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Inconvenient as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "My son is waiting for me, so do try\x01",
            "to keep it brief.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_1B89")

    label("loc_1B32")


    ChrTalk(
        0xE,
        (
            "What a mess. My son is waiting for\x01",
            "me in the mess hall, so let's hurry,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B89")

    Jump("loc_1C67")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(
        0x8,
        (
            "This is where we conduct basic inspections\x01",
            "for cars going to or coming from Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You know, considering how cheap this\x01",
            "gate is, they could probably drive their\x01",
            "way through if they really wanted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C7D")
    TalkEnd(0x15)
    Jump("loc_1CAC")

    label("loc_1C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C93")
    TalkEnd(0x10)
    Jump("loc_1CAC")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA9")
    TalkEnd(0xE)
    Jump("loc_1CAC")

    label("loc_1CA9")

    TalkEnd(0x8)

    label("loc_1CAC")

    Return()

    # Function_5_E4A end

    def Function_6_1CAD(): pass

    label("Function_6_1CAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D2A")

    ChrTalk(
        0xFE,
        "There's nothing unusual to report, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm simply following my commanding\x01",
            "officer's orders, sir!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_1D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DA1")

    ChrTalk(
        0xFE,
        "The cargo looks good to go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All that's left is to get the papers signed\x01",
            "at the reception desk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1E04")

    ChrTalk(
        0xFE,
        "Everything is going smoothly today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good afternoon, Sergeant Major Seeker!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_1E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E7B")

    ChrTalk(
        0xFE,
        (
            "No problems to report! Well, if we\x01",
            "ignore my exhaustion, that is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Today's been quite the rush!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(
        0xFE,
        "Everything is operating well, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This traffic is never going to end!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2093")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2007")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA6")
    TurnDirection(0x9, 0x13, 0)

    ChrTalk(
        0xFE,
        (
            "The bus for Crossbell City will stop\x01",
            "at the right-hand boarding station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There shouldn't be any issues with the\x01",
            "highway today, so take care, ma'am!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2002")

    label("loc_1FA6")


    ChrTalk(
        0xFE,
        (
            "Phew. I usually don't mind giving directions\x01",
            "to first-time tourists, but THIS many...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2002")

    Jump("loc_208E")

    label("loc_2007")


    ChrTalk(
        0xFE,
        (
            "Later today, I have to transfer over\x01",
            "to Crossbell Station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of my guardsman buddies, Romeo,\x01",
            "is typically stationed there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208E")

    Jump("loc_21B0")

    label("loc_2093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20FC")

    ChrTalk(
        0xFE,
        (
            "Nothing to report!\x01",
            "Well, so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's too many people! I'm going\x01",
            "to pass out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_20FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2146")

    ChrTalk(
        0xFE,
        "Cargo is green!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't worry, I triple-checked it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B0")

    label("loc_2146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21B0")

    ChrTalk(
        0xFE,
        "Daily traffic has been proceeding smoothly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There's no need to worry when I'm on duty!\x02",
    )

    CloseMessageWindow()

    label("loc_21B0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1CAD end

    def Function_7_21B4(): pass

    label("Function_7_21B4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2248")
    Jump("loc_2292")

    label("loc_2248")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2268")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2292")

    label("loc_2268")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2288")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2292")

    label("loc_2288")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2292")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_235C")

    ChrTalk(
        0xFE,
        (
            "Since buses constantly come and go,\x01",
            "we need to maintain the parking lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But man, am I getting hungry. I think\x01",
            "I'll take my lunch break now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_235C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2471")

    ChrTalk(
        0xFE,
        (
            "Burrell seems to have finally recovered\x01",
            "from that scouting mission of his. Even\x01",
            "managed to get back to guard duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, having to cover for him was a\x01",
            "real hassle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. I guess I'll grab a bite to eat\x01",
            "before heading back to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_24C3")

    label("loc_2471")


    ChrTalk(
        0xFE,
        (
            "Might as well grab some food before\x01",
            "going back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mmm, delicious!\x02",
    )

    CloseMessageWindow()

    label("loc_24C3")

    Jump("loc_2CF2")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24D6")
    Jump("loc_2CF2")

    label("loc_24D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2569")

    ChrTalk(
        0xFE,
        (
            "*sigh* I hate always having to eat\x01",
            "in a rush like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eating really fast isn't good for\x01",
            "your digestive system, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260D")

    ChrTalk(
        0xFE,
        (
            "From the looks of it, we're going to\x01",
            "be busy tomorrow, too. I better get\x01",
            "my stamina up while I still can!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "*furiously eats*\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2672")

    label("loc_260D")

    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        "*furiously eats*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Agh! Too fast...! *gulp* \x01",
            "Aaaah, that's better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*furiously eats*\x02",
    )

    CloseMessageWindow()

    label("loc_2672")

    Jump("loc_2CF2")

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278E")

    ChrTalk(
        0xFE,
        (
            "Seeing all those tourists reminded\x01",
            "me of a dream I once had...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just really want to try visiting the\x01",
            "Liberl Kingdom one of these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear that because of their super\x01",
            "clean air and water, their food is\x01",
            "out of this world.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_281C")

    label("loc_278E")


    ChrTalk(
        0xFE,
        (
            "Personally, I bet Armorica Village's\x01",
            "produce is just as delicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I really want to visit Liberl at\x01",
            "least once in my life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281C")

    Jump("loc_28B2")

    label("loc_2821")


    ChrTalk(
        0xFE,
        (
            "It's not even noon yet, and my stomach\x01",
            "is already yelling at me for grub.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if anyone would do me a\x01",
            "solid and bring me a snack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B2")

    Jump("loc_2CF2")

    label("loc_28B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A9C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299E")

    ChrTalk(
        0xFE,
        (
            "Our mess hall actually serves anyone\x01",
            "who pays, not just the guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can be a little awkward. Customers sometimes\x01",
            "have a hard time eating if all the guardsmen are\x01",
            "chowing down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2A01")

    label("loc_299E")


    ChrTalk(
        0xFE,
        (
            "Dang, there's loads of people today...\x01",
            "Guess I gotta clean my plate and head\x01",
            "back to my post.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A01")

    Jump("loc_2A97")

    label("loc_2A06")


    ChrTalk(
        0xFE,
        (
            "It's not even noon yet, and my stomach\x01",
            "is already yelling at me for grub.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if anyone would do me a\x01",
            "solid and bring me a snack.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A97")

    Jump("loc_2CF2")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B7C")

    ChrTalk(
        0xFE,
        (
            "You know, our mess hall's food is\x01",
            "nothing to scoff about, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...CGF rations are downright\x01",
            "disgusting. Hardly even edible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a self-proclaimed lover of food,\x01",
            "that's a pretty serious problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF2")

    label("loc_2B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C54")

    ChrTalk(
        0xFE,
        (
            "*munch* *munch*\x01",
            "Aaah, it's too good! Too delicious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Our mess hall's food isn't half bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I think the city's Long Lao Tavern &\x01",
            "Inn might beat it out, if only by a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CF2")

    label("loc_2C54")


    ChrTalk(
        0xFE,
        (
            "Whenever I'm off duty, I usually stop\x01",
            "by Long Lao in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tangram Gate's mess hall is good\x01",
            "enough, but that inn's food has a\x01",
            "charm of its own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_21B4 end

    def Function_8_2CFA(): pass

    label("Function_8_2CFA")

    Call(0, 9)
    Return()

    # Function_8_2CFA end

    def Function_9_2CFE(): pass

    label("Function_9_2CFE")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D5C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2D5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7C")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39A3")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D90")
    Jump("loc_39A3")

    label("loc_2D90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2E80")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC5")
    Call(0, 10)
    Jump("loc_2E7B")

    label("loc_2DC5")


    ChrTalk(
        0xB,
        (
            "Most guardsmen come here to eat right\x01",
            "around noon, so it's starting to get busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All right... I need to prep the rest of the\x01",
            "ingredients before too many customers\x01",
            "show up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7B")

    Jump("loc_39A3")

    label("loc_2E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F53")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9C")
    Call(0, 10)
    Jump("loc_2F4E")

    label("loc_2E9C")


    ChrTalk(
        0xB,
        (
            "Lately, people have been traveling all the\x01",
            "way to Tangram Gate just for our food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Having a customer come back for another\x01",
            "meal is the best compliment a chef could get.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4E")

    Jump("loc_39A3")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_317D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6F")
    Call(0, 10)
    Jump("loc_3178")

    label("loc_2F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DB")

    ChrTalk(
        0xB,
        (
            "Oh, Sergeant Major Seeker. Heading out\x01",
            "on another mission?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FThat's right!\x02\x03",
            "#0509FMr. Temas, will you do me a favor?\x01",
            "While I'm here, could you treat me\x01",
            "to a little energy booster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hahaha! Sorry, Sergeant Major. I'd love to,\x01",
            "but I have a business to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you want some food, you've got to\x01",
            "pay for it like everyone else.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3178")

    label("loc_30DB")


    ChrTalk(
        0xB,
        (
            "I'd love to give you a freebie, ma'am,\x01",
            "but I have a business to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you want that energy booster of yours,\x01",
            "you have to pay like everyone else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3178")

    Jump("loc_39A3")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3219")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3199")
    Call(0, 10)
    Jump("loc_3214")

    label("loc_3199")


    ChrTalk(
        0xB,
        "There are lots of customers today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Serving them all by myself definitely isn't\x01",
            "the easiest thing in the world...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3214")

    Jump("loc_39A3")

    label("loc_3219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3445")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3235")
    Call(0, 10)
    Jump("loc_3440")

    label("loc_3235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E9")

    ChrTalk(
        0xB,
        (
            "Deputy Commander Baelz always waits until\x01",
            "the other guardsmen have finished eating\x01",
            "before taking her lunch break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Instead of cultivating her relationships with them,\x01",
            "the deputy commander prefers to draw a distinct\x01",
            "line between herself and her subordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's not easy for a boss to grasp what their dynamic\x01",
            "with their subordinates should be, so the fact that\x01",
            "she has is a testament to her intellect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3440")

    label("loc_33E9")


    ChrTalk(
        0xB,
        (
            "I'm never going to understand how\x01",
            "Deputy Commander Baelz ISN'T the\x01",
            "CGF commander.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3440")

    Jump("loc_39A3")

    label("loc_3445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3461")
    Call(0, 10)
    Jump("loc_36AE")

    label("loc_3461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_356A")

    ChrTalk(
        0xB,
        (
            "This might come as a surprise to you, but the\x01",
            "guardsmen and regular customers eat from\x01",
            "vastly different menus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For example, the guardsmen menu has loads\x01",
            "of meals that serve as energy boosters. How\x01",
            "else would they make it through the day?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AE")

    label("loc_356A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(
        0xB,
        "Phew. Lunchtime is crazy as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And what's more, these Calvardians are\x01",
            "extremely picky. I swear, they'll complain if\x01",
            "the slightest thing doesn't suit their tastes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36AE")

    label("loc_362E")


    ChrTalk(
        0xB,
        "I better finish the rest of the food prep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Once the Calvardian bus shows up, it's\x01",
            "going to get insanely busy in here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36AE")

    Jump("loc_39A3")

    label("loc_36B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_378B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CF")
    Call(0, 10)
    Jump("loc_3786")

    label("loc_36CF")


    ChrTalk(
        0xB,
        (
            "Setting aside the railway, a lot of Calvardians\x01",
            "make their way to Tangram Gate on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I guess it is basically a straight shot...\x01",
            "but I'm sure you knew that already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3786")

    Jump("loc_39A3")

    label("loc_378B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_385F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A7")
    Call(0, 10)
    Jump("loc_385A")

    label("loc_37A7")


    ChrTalk(
        0xB,
        (
            "It's already been a year since I was first\x01",
            "stationed at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "All in all, I can't complain. Being able to\x01",
            "serve my food to all these foreigners is\x01",
            "a real treat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385A")

    Jump("loc_39A3")

    label("loc_385F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_39A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3905")

    ChrTalk(
        0xB,
        (
            "This fine establishment has everything a\x01",
            "traveler would need if forced to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You four looking for something to eat, too?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39A3")

    label("loc_3905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3918")
    Call(0, 10)
    Jump("loc_39A3")

    label("loc_3918")


    ChrTalk(
        0xB,
        (
            "This fine establishment has everything a\x01",
            "traveler would need if forced to stay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You four looking for something to eat, too?\x02",
    )

    CloseMessageWindow()

    label("loc_39A3")

    Jump("loc_2D0B")

    label("loc_39A8")

    TalkEnd(0xB)
    Return()

    # Function_9_2CFE end

    def Function_10_39AC(): pass

    label("Function_10_39AC")


    ChrTalk(
        0xB,
        (
            "The other day, these people calling themselves\x01",
            "members of a 'Fisherman's Guild' came and\x01",
            "handed me a recipe for a fish hotpot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Fish is pretty nutritious. I'm sure the\x01",
            "guardsmen would love some of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, yeah. Might as well teach you guys\x01",
            "how to make it, too. Sit down and enjoy it\x01",
            "together sometime, all right?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A3),
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
            scpstr(SCPSTR_CODE_ITEM, 0x1A3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x7)
    Return()

    # Function_10_39AC end

    def Function_11_3B72(): pass

    label("Function_11_3B72")

    Call(0, 12)
    Return()

    # Function_11_3B72 end

    def Function_12_3B76(): pass

    label("Function_12_3B76")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF4")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43DF")

    label("loc_3BF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C08")
    Jump("loc_43DF")

    label("loc_3C08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3CB7")

    ChrTalk(
        0xC,
        (
            "You must be a weird bunch to be\x01",
            "looking for a bed this early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No skin off my back, I guess.\x01",
            "Go ahead and rest if you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_3CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD6")

    ChrTalk(
        0xC,
        (
            "Deputy Commander Baelz makes sure\x01",
            "to not put too much on a guardsman's\x01",
            "plate throughout the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If we were drained when stuff really hits\x01",
            "the fan, we'd be done for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You guys should stay in tip-top shape, too.\x01",
            "You have to be ready for anything!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E54")

    label("loc_3DD6")


    ChrTalk(
        0xC,
        (
            "Make sure you use any break you can get,\x01",
            "just in case something pops up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Heck, rest here if you want. I don't mind.\x02",
    )

    CloseMessageWindow()

    label("loc_3E54")

    Jump("loc_43DF")

    label("loc_3E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3F58")

    ChrTalk(
        0xC,
        (
            "From what I've heard, as soon as those\x01",
            "ghosts or whatever showed up in the ruins,\x01",
            "the gate's scouting team retreated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That really grinds my gears. Who gives\x01",
            "a hoot that they were ghosts? I say they\x01",
            "should've gone and thrashed 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_3F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FC1")

    ChrTalk(
        0xC,
        "Everyone seems busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I s'pose I'll go help Temas later, since\x01",
            "I've got the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_3FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_406C")

    ChrTalk(
        0xC,
        "I'm a massive Ilya Platiere fan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Trust me, it physically hurts me that I'm\x01",
            "stuck slaving away here, missing all of\x01",
            "the Arc en Ciel performances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_406C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_41F6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4178")

    ChrTalk(
        0xC,
        (
            "Are you looking to stay with us? You're\x01",
            "in luck. We have plenty of free beds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Since it's the Anniversary Festival, most people are\x01",
            "staying in the city or the towns. Besides, I doubt\x01",
            "many would want to spend it in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F1")

    label("loc_4178")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_41BE")

    ChrTalk(
        0xC,
        "Sure are a lot of people coming through today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_41F1")

    label("loc_41BE")


    ChrTalk(
        0xC,
        "What? You looking to take a nap or something?\x02",
    )

    CloseMessageWindow()

    label("loc_41F1")

    Jump("loc_43DF")

    label("loc_41F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4276")

    ChrTalk(
        0xC,
        (
            "Yesterday was the big, grand opening of\x01",
            "Arc en Ciel's new performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I really, REALLY wanted to go...\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_4276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_434E")

    ChrTalk(
        0xC,
        (
            "The only people that ever stay here are\x01",
            "Calvardians and traveling merchants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You see, every once in a while, people will\x01",
            "miss the bus and have nowhere to go. That's\x01",
            "why this place was set up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43DF")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_43DF")

    ChrTalk(
        0xC,
        "Looking for a place to rest?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Do whatever you'd like. Can't guarantee that your\x01",
            "stay is going to be a comfortable one, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43DF")

    Jump("loc_3B83")

    label("loc_43E4")

    TalkEnd(0xC)
    Return()

    # Function_12_3B76 end

    def Function_13_43E8(): pass

    label("Function_13_43E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_447C")
    Jump("loc_44C6")

    label("loc_447C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_449C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44C6")

    label("loc_449C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44C6")

    label("loc_44BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "*munch* *munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. My plan is to wind down today and\x01",
            "head back home on the bus tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_43E8 end

    def Function_14_4558(): pass

    label("Function_14_4558")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45EC")
    Jump("loc_4636")

    label("loc_45EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_460C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_460C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_462C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4636")

    label("loc_462C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4636")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Have they not finished the inspections yet?\x01",
            "...I've already cleaned my plate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_4558 end

    def Function_15_46B6(): pass

    label("Function_15_46B6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Hmm, so this is Tangram Gate? It doesn't\x01",
            "seem very fortified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With defenses like this, it's only a matter of\x01",
            "time before it falls into Republican hands.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_46B6 end

    def Function_16_4760(): pass

    label("Function_16_4760")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47F4")
    Jump("loc_483E")

    label("loc_47F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4814")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_483E")

    label("loc_4814")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4834")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_483E")

    label("loc_4834")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_483E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "The bus service seems like the best\x01",
            "way to get to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The bus stop's out in the parking lot, right?\x01",
            "Now that my belly's full, I'll go have a look.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_4760 end

    def Function_17_4914(): pass

    label("Function_17_4914")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Where in the world does the bus heading\x01",
            "for Crossbell City stop at...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_4914 end

    def Function_18_4967(): pass

    label("Function_18_4967")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Phew. Seems like it's too late to be worrying\x01",
            "about getting here on a less crowded day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I have to work with the hand I\x01",
            "was dealt. I must head to the city to\x01",
            "stock up at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I'm being honest, I'm much more excited to take\x01",
            "in the sights of the festival than do my business!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_4967 end

    def Function_19_4A98(): pass

    label("Function_19_4A98")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B2C")
    Jump("loc_4B76")

    label("loc_4B2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B4C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B76")

    label("loc_4B4C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B6C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B76")

    label("loc_4B6C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B76")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "There's still another whole day of the Anniversary\x01",
            "Festival, but I decided to head back today. I'm not\x01",
            "trying to fight against that crowd of people leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that many others had the same\x01",
            "idea as me, unfortunately.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_4A98 end

    def Function_20_4C8C(): pass

    label("Function_20_4C8C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I'm in a hurry here! C'mon, move it!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_4C8C end

    def Function_21_4CBD(): pass

    label("Function_21_4CBD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Inspections are always such a bother...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_4CBD end

    def Function_22_4CF1(): pass

    label("Function_22_4CF1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D85")
    Jump("loc_4DCF")

    label("loc_4D85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4DA5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DCF")

    label("loc_4DA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DCF")

    label("loc_4DC5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4DCF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Where's the bus? I've been waiting nearly\x01",
            "an hour now for the next one...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_4CF1 end

    def Function_23_4E4B(): pass

    label("Function_23_4E4B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Having to wake up so early has left me\x01",
            "quite drowsy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't afford to fall asleep at the wheel,\x01",
            "so I'm resting here for a bit to perk me up.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_4E4B end

    def Function_24_4EEA(): pass

    label("Function_24_4EEA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F7E")
    Jump("loc_4FC8")

    label("loc_4F7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FC8")

    label("loc_4F9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FC8")

    label("loc_4FBE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Huh. I wasn't expecting it to taste this good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought I was going to be served some\x01",
            "cheap, two-bit meal, but my, oh, my...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can happily say they exceeded all of my\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_4EEA end

    def Function_25_50BA(): pass

    label("Function_25_50BA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "It's quite delicious, isn't it, darling?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_50BA end

    def Function_26_50EF(): pass

    label("Function_26_50EF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I came to Crossbell seeking to sell goods\x01",
            "from the Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering there aren't any places that\x01",
            "specialize in selling Eastern accessories...\x01",
            "these are going to sell like hot cakes!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_50EF end

    def Function_27_51C2(): pass

    label("Function_27_51C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5256")
    Jump("loc_52A0")

    label("loc_5256")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5276")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52A0")

    label("loc_5276")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5296")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52A0")

    label("loc_5296")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52A0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C6")

    ChrTalk(
        0xFE,
        "*munch*...*munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I probably should have thought up some\x01",
            "plans before actually coming to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I could always go to Armorica Village. One\x01",
            "of my friends who visited during the festival\x01",
            "said it was definitely a must-see.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5467")

    label("loc_53C6")


    ChrTalk(
        0xFE,
        (
            "He wouldn't stop going on about the sights,\x01",
            "so maybe that's not a bad idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then again, going on a tour of Mainz's\x01",
            "mines would be cool, too. Hmmm...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5467")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_51C2 end

    def Function_28_546F(): pass

    label("Function_28_546F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I finally got a long vacation, so I took my\x01",
            "wife to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing the contrast between the modern Crossbell\x01",
            "City and the relatively natural Mainz and Armorica\x01",
            "up close was really something.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_546F end

    def Function_29_5542(): pass

    label("Function_29_5542")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Crossbell City looks so grand on the outside,\x01",
            "but walking into some of the alleyways makes\x01",
            "you feel as if you wandered into the underworld...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's safe to say that I experienced a fear I haven't\x01",
            "felt before during my visit.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_5542 end

    def Function_30_5633(): pass

    label("Function_30_5633")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56C7")
    Jump("loc_5711")

    label("loc_56C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5711")

    label("loc_56E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5707")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5711")

    label("loc_5707")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5711")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "I'm going to treat myself to some brunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's see, waffles or pancakes...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_5633 end

    def Function_31_5795(): pass

    label("Function_31_5795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5812")

    ChrTalk(
        0x22,
        (
            "#3600FHello, everyone. Work has brought me to\x01",
            "the mess hall today, selling ingredients.\x02\x03",
            "Wish me luck!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5910")

    label("loc_5812")


    ChrTalk(
        0x22,
        (
            "#3600FThe mess hall was running a bit low on\x01",
            "ingredients, so I decided to stop by to\x01",
            "wholesale some to them.\x02\x03",
            "#3604FNow, then, I don't want to keep Temas\x01",
            "waiting.\x02\x03",
            "I should hurry and bring the rest of the\x01",
            "crates in before I get too carried away.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_5910")

    TalkEnd(0xFE)
    Return()

    # Function_31_5795 end

    def Function_32_5914(): pass

    label("Function_32_5914")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A2")

    ChrTalk(
        0xFE,
        "These beds aren't too shabby.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've slept in many, many inns, so believe\x01",
            "me, I know a comfy bed when I see one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_59F6")

    label("loc_59A2")


    ChrTalk(
        0xFE,
        (
            "Despite not having the most...elegant of\x01",
            "appearances, the beds are quite soft.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F6")

    TalkEnd(0xFE)
    Return()

    # Function_32_5914 end

    def Function_33_59FA(): pass

    label("Function_33_59FA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A8E")
    Jump("loc_5AD8")

    label("loc_5A8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AAE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AD8")

    label("loc_5AAE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ACE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AD8")

    label("loc_5ACE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AD8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5E41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D98")

    ChrTalk(
        0x24,
        (
            "We had the pleasure of taking the request\x01",
            "of a tourist headed back to Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "We finally managed to retrieve the wallet\x01",
            "he dropped on Tangram Hill, not far away\x01",
            "from the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUh, was that it?\x02\x03",
            "That sounds like a pretty straightforward\x01",
            "job to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        "That's what one would think, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Unfortunately, you're forgetting that\x01",
            "Tangram Hill is Republic territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "Even something as insignificant as picking up\x01",
            "a lost wallet requires time and cooperation\x01",
            "with Republican officials.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FCalvard sounds like quite the strict place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "You're telling me. Basically, not all easy\x01",
            "jobs can be done quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5E41")

    label("loc_5D98")


    ChrTalk(
        0xFE,
        (
            "This one took us more time than I would\x01",
            "have liked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, we still have other requests to take\x01",
            "care of, so we're going to make our way\x01",
            "back to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E41")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_59FA end

    def Function_34_5E49(): pass

    label("Function_34_5E49")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EDD")
    Jump("loc_5F27")

    label("loc_5EDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5EFD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F27")

    label("loc_5EFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F1D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F27")

    label("loc_5F1D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F27")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F67")
    Call(0, 33)
    Jump("loc_5FD8")

    label("loc_5F67")


    ChrTalk(
        0xFE,
        (
            "Both the Empire and Republic are extremely\x01",
            "territorial... You'd better remember that as\x01",
            "members of the CPD.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_5E49 end

    def Function_35_5FE0(): pass

    label("Function_35_5FE0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6074")
    Jump("loc_60BE")

    label("loc_6074")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6094")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60BE")

    label("loc_6094")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60B4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60BE")

    label("loc_60B4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60BE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_641E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E5")

    ChrTalk(
        0xFE,
        (
            "We're heading to a Republican guild branch\x01",
            "for some official bracer business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I've got an itch to show off my skills in\x01",
            "my home country, and I'm ready to scratch it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On top of that, I'm interested to see how my\x01",
            "cute little junior is going to handle the trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0009FWow, Lynn. You're merciless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally. You've gotta whip them\x01",
            "into shape early, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was training in the martial\x01",
            "arts, my teachers never let me slack,\x01",
            "not even for a second!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_641E")

    label("loc_62E5")


    ChrTalk(
        0xFE,
        (
            "The guild branch we're heading\x01",
            "to is in a bit of a tricky location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we went by train, we'd have to take\x01",
            "a connecting ride, but we can go straight\x01",
            "there if we take an orbal bus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remember, a train may be able to move\x01",
            "way faster than a bus, but sometimes a\x01",
            "bus can be a lot faster in the long run.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_641E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_5FE0 end

    def Function_36_6426(): pass

    label("Function_36_6426")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64BA")
    Jump("loc_6504")

    label("loc_64BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6504")

    label("loc_64DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6504")

    label("loc_64FA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6504")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_676F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66D7")

    ChrTalk(
        0xFE,
        (
            "Lynn is a master practitioner of the\x01",
            "Taito martial arts style, which originates\x01",
            "from old Calvard tradition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to hand-to-hand combat,\x01",
            "she's probably the best the Crossbell\x01",
            "guild branch has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FDamn, really? I've heard that's the same\x01",
            "martial art that some high-ranked bracer\x01",
            "from Calvard uses.\x02\x03",
            "#0304FThat'd explain why Lynn here carries\x01",
            "herself the way she does.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_676F")

    label("loc_66D7")


    ChrTalk(
        0xFE,
        (
            "We have a job that's taking us to the\x01",
            "Republic, so Lynn's raring to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If she gets any more fired up, she'll\x01",
            "end up scaring our client away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_6426 end

    def Function_37_6777(): pass

    label("Function_37_6777")

    TalkBegin(0xFE)

    ChrTalk(
        0x29,
        (
            "#0500FThe bus is in the parking lot, everyone.\x02\x03",
            "#0501FI wish I could do more, but I've done all I\x01",
            "can. I'll be praying for your success!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_6777 end

    def Function_38_680C(): pass

    label("Function_38_680C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_68A0")
    Jump("loc_68EA")

    label("loc_68A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68EA")

    label("loc_68C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68EA")

    label("loc_68E0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68EA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_6A3A")

    ChrTalk(
        0x2A,
        (
            "#3404FI came to Crossbell to search for a\x01",
            "certain bit of septium, so to speak.\x02\x03",
            "#3400FAnd if I'm successful in obtaining it,\x01",
            "I'll have the power to bring a vortex\x01",
            "of enthusiasm to the Republic's people.\x02\x03",
            "#3402FHowever, doing so may require me\x01",
            "to use whatever means necessary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC8")

    label("loc_6A3A")


    ChrTalk(
        0x104,
        "#0305F(Dude! Check her out!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3405FOh?\x02\x03",
            "#3400FYou weren't riding on the bus, were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWh-What?\x02\x03",
            "#0012FOh! Well, since we got here so late,\x01",
            "we decided we'd spend the night.\x02\x03",
            "#0006F(Yeah, let's not push our luck.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3404FHehe. Is that so?\x02\x03",
            "#3400FWell, I suppose that would be the\x01",
            "rational thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FEnlighten me, madam. What exactly\x01",
            "are ya doin' here in Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3404FI suppose you could say that I'm\x01",
            "searching for a jewel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhat sort of jewel are you talking about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        (
            "#3400FA beautiful one. One that can enchant\x01",
            "people and sleeps in this very state.\x02\x03",
            "#3404FIf I'm successful in obtaining it, I'll\x01",
            "have the power to bring a vortex of\x01",
            "enthusiasm to the Republic's people.\x02\x03",
            "#3402FHowever, doing so may require me\x01",
            "to use whatever means necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Why is she being so cryptic...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#3404FHehe. I wouldn't think too hard about it.\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x5)

    label("loc_6DC8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_680C end

    def Function_39_6DD0(): pass

    label("Function_39_6DD0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E64")
    Jump("loc_6EAE")

    label("loc_6E64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EAE")

    label("loc_6E84")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EA4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6EAE")

    label("loc_6EA4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EAE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_7015")

    ChrTalk(
        0xFE,
        (
            "I think it's been around three years\x01",
            "since I last visited Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohoho, I can't wait to see my grandson. The\x01",
            "mere thought of him puts a smile on this old face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes I can't help but remember the\x01",
            "time we went to Mishelam Wonderland\x01",
            "together when he was still just a little tyke...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731C")

    label("loc_7015")


    ChrTalk(
        0xFE,
        "Oh, dear, oh, my... What a handsome young man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You remind me of my grandchild, sonny.\x01",
            "Such a smart-looking demeanor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FUm, thank you...? Ma'am, are you from\x01",
            "Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, no, no. I'm from Calvard, dear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, my son's family lives in Crossbell\x01",
            "City, so I'm using that as an excuse to have\x01",
            "a bit of fun at the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did I mention it's been almost three years\x01",
            "since I last came here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FYou sure seem happy, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ohoho. How could I not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it's been so long since I've been\x01",
            "able to play with my precious grandson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It feels like it was only yesterday I was\x01",
            "playing with him in Mishelam Wonderland...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see how much he's grown over\x01",
            "the years. My dear grandson, all grown up...\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x6)

    label("loc_731C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_6DD0 end

    def Function_40_7324(): pass

    label("Function_40_7324")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_738A")

    ChrTalk(
        0xFE,
        "I came to Crossbell to fish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's all. Now could you leave\x01",
            "me alone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77CA")

    label("loc_738A")


    ChrTalk(
        0xFE,
        "Whaddaya want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(This guy looks like an oddball...)\x02\x03",
            "#0000FUmmm... Excuse me, sir. Could you give\x01",
            "us your reason for coming to Crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wh-Why do you need to know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FJ-Just curious, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWhy the hostility, old man? Got some secret\x01",
            "you're hidin'? Don't wanna let anyone know\x01",
            "about that guilty conscience of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wh-What are you talking about...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FWhoa, Randy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FDon't worry. I've got the same tastes as you.\x02\x03",
            "#0300FCrossbell is swarmin' with all sorts of cuties.\x01",
            "Not to mention, it's full of fun lil' places that\x01",
            "you can take 'em to.\x02\x03",
            "#0309FMan, I like your style! Want me to tell\x01",
            "ya about some of my favorite spots?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "S-S-Such shamelessness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Fishing! I came here to fish, okay?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know it's the Anniversary Festival and\x01",
            "all, but I just came here to fish for some\x01",
            "of your freshwater species! ALONE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Something wrong with that, PUNK?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FHaha. Nah, I'm cool with that. Sorry\x01",
            "for teasing ya, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(I can't tell if he was playing bad cop or what...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph! Good day, then!\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x7)

    label("loc_77CA")

    TalkEnd(0xFE)
    Return()

    # Function_40_7324 end

    def Function_41_77CE(): pass

    label("Function_41_77CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_78EA")

    ChrTalk(
        0xFE,
        (
            "I deal in rare knickknacks and other\x01",
            "Calvardian doodads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pride myself in having contacts from every\x01",
            "country in Zemuria, and business is coming\x01",
            "along quite smoothly, much to my surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you'd like, I'd be more than happy\x01",
            "to show you my wares.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE0")

    label("loc_78EA")


    ChrTalk(
        0xFE,
        (
            "Wahahaha! Oh, I can't wait until the bus\x01",
            "arrives and takes me to financial success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear that Crossbell is the ideal place to\x01",
            "do business. Mira awaits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FExcuse me, sir. You're some kind of\x01",
            "merchant, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Exactly right. I deal in rare Calvardian\x01",
            "novelties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing an opportunity, I decided to come\x01",
            "expand my wares with Crossbellan goods\x01",
            "to sell back in Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FYou run your business by yourself...?\x01",
            "Is that not difficult?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite how things sound, I have quite\x01",
            "the wide array of personal connections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pride myself in having contacts from every\x01",
            "country in Zemuria, and business is coming\x01",
            "along quite smoothly, much to my surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you'd like, I'd be more than happy\x01",
            "to show you my wares.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x8)

    label("loc_7BE0")

    TalkEnd(0xFE)
    Return()

    # Function_41_77CE end

    def Function_42_7BE4(): pass

    label("Function_42_7BE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_7D09")

    ChrTalk(
        0xFE,
        (
            "I've been vacationing in Calvard, but\x01",
            "I made sure to come back in order to\x01",
            "make the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, why are you wasting your time\x01",
            "with me...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're boarding the bus, too, I think\x01",
            "you should pay attention to the lady\x01",
            "with the black hair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8133")

    label("loc_7D09")


    ChrTalk(
        0xFE,
        (
            "Hey, you four...don't you think that\x01",
            "lady's up to something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh? Lady? Which one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The black-haired one sitting over on\x01",
            "the other side, wearing the pantsuit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw her with the rest of the passengers,\x01",
            "but she sticks out like a sore thumb. I'm\x01",
            "telling you, she's suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's like, she's TOO calm. I just get the\x01",
            "feeling she's not your average lady.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_7F64")

    ChrTalk(
        0x102,
        (
            "#0103FWell, it's certainly true that she's not\x01",
            "dressed like the typical tourist...and\x01",
            "doesn't talk like one, either.\x02\x03",
            "#0100FThat aside, did you come to Crossbell\x01",
            "to sightsee? Or personal reasons?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FFC")

    label("loc_7F64")


    ChrTalk(
        0x102,
        (
            "#0103FWe can't substantiate that unless we talk\x01",
            "to her ourselves...\x02\x03",
            "#0100FThat aside, did you come to Crossbell\x01",
            "to sightsee? Or personal reasons?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FFC")


    ChrTalk(
        0xFE,
        "I guess I'd say that I'm returning home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been vacationing in Calvard, but\x01",
            "I made sure to come back for the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, why are you wasting your time\x01",
            "with me...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're boarding the bus, too, I think\x01",
            "you should pay attention to the lady\x01",
            "with the black hair.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x9)

    label("loc_8133")

    TalkEnd(0xFE)
    Return()

    # Function_42_7BE4 end

    def Function_43_8137(): pass

    label("Function_43_8137")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81CB")
    Jump("loc_8215")

    label("loc_81CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_81EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8215")

    label("loc_81EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_820B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8215")

    label("loc_820B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8215")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_82DE")

    ChrTalk(
        0xFE,
        "We're siblings, but we don't really look alike.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luckily, we both love to travel, so we stick\x01",
            "together during trips, just the two of us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_863C")

    label("loc_82DE")


    ChrTalk(
        0x2F,
        (
            "Morning. Are you heading to\x01",
            "Crossbell City, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYou could say that.\x02\x03",
            "#0005FSo, are you two...traveling together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Pfft! That's a roundabout way of asking\x01",
            "if we're dating. And no, we aren't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0205FOh? That is a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "Haha. Here we go again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Contrary to what you think, we're siblings,\x01",
            "not a couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Since we barely look alike, people are\x01",
            "always getting the wrong impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "But we both love to travel. We stick\x01",
            "together during trips, just the two of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWow. Sounds like you two really get along well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Well, I'd feel bad if she went places by\x01",
            "herself, since she doesn't have a boyfriend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        (
            "Ha ha. Aren't you hilarious? Isn't it you who\x01",
            "Mother's always nagging to find that special\x01",
            "someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "Okay, you got me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "How about we put that behind us and make\x01",
            "this trip the best one yet?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xA)

    label("loc_863C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_8137 end

    def Function_44_8644(): pass

    label("Function_44_8644")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86D8")
    Jump("loc_8722")

    label("loc_86D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86F8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8722")

    label("loc_86F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8718")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8722")

    label("loc_8718")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8722")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_8800")

    ChrTalk(
        0xFE,
        (
            "How many times have we been mistaken\x01",
            "for a couple on this trip now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, well. Let's ignore it and have a great\x01",
            "time at the Anniversary Festival together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8803")

    label("loc_8800")

    Call(0, 43)

    label("loc_8803")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_8644 end

    def Function_45_880B(): pass

    label("Function_45_880B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_889F")
    Jump("loc_88E9")

    label("loc_889F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88BF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88E9")

    label("loc_88BF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88DF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88E9")

    label("loc_88DF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_88E9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_8A0C")

    ChrTalk(
        0xFE,
        (
            "I'm actually having a nice father-son\x01",
            "bonding trip today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm constantly having to go on business\x01",
            "trips, I have to take advantage of times like\x01",
            "these to show off my fatherly love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's all there is to it. Wahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C91")

    label("loc_8A0C")


    ChrTalk(
        0xFE,
        (
            "You know, traveling by bus has a unique\x01",
            "charm to it. It's almost beautiful, in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "My boy seems to be having a blast, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FOh, are you having a family vacation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, I suppose that's a good way to put it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My son has always supported me, through thick\x01",
            "and thin, so I wanted to be able to show my love\x01",
            "and appreciation for him. Hence this trip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FYou sound like quite the caring father, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come, now, I'm going to blush!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm constantly having to go on business trips,\x01",
            "so I have to take advantage of times like\x01",
            "these to show off my fatherly love.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's all there is to it. Wahaha!\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xB)

    label("loc_8C91")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_880B end

    def Function_46_8C99(): pass

    label("Function_46_8C99")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D2D")
    Jump("loc_8D77")

    label("loc_8D2D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D4D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D77")

    label("loc_8D4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D6D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D77")

    label("loc_8D6D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D77")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_8E35")

    ChrTalk(
        0xFE,
        (
            "My father has visited loads of countries on his\x01",
            "business trips, and between you and me, I can't\x01",
            "wait to see what he can teach me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F43")

    label("loc_8E35")


    ChrTalk(
        0xFE,
        (
            "People keep mentioning how pretty a place\x01",
            "Crossbell is. To be honest, I'm really excited\x01",
            "to see whether that's true or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My father has visited loads of countries on his\x01",
            "business trips, and between you and me, I can't\x01",
            "wait to see what he can teach me.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xC)

    label("loc_8F43")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_8C99 end

    def Function_47_8F4B(): pass

    label("Function_47_8F4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(22280, 1000, 1150, 0)
    MoveCamera(359, 27, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20000, 0)
    OP_4B(0x29, 0xFF)
    ClearMapObjFlags(0x1, 0x10)
    SetChrPos(0x101, -7150, 0, 9500, 90)
    SetChrPos(0x102, -7150, 0, 8000, 90)
    SetChrPos(0x103, -8650, 0, 9500, 90)
    SetChrPos(0x104, -8650, 0, 8000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2A, -40, 600, 0, 180)
    SetChrPos(0x2B, -40, 600, 0, 180)
    SetChrPos(0x2C, -40, 600, 0, 180)
    SetChrPos(0x2D, -40, 600, 0, 180)
    SetChrPos(0x2E, -40, 600, 0, 180)
    SetChrPos(0x2F, -40, 600, 0, 180)
    SetChrPos(0x30, -40, 600, 0, 180)
    SetChrPos(0x31, -40, 600, 0, 180)
    SetChrPos(0x32, -40, 600, 0, 180)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x2E, 0x40)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x33)
    OP_D3(0x33, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x33, 33000, 0, 0, 0)
    OP_70(0x9, 0x0)
    OP_74(0x9, 0x1E)
    Sound(466, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(16030, 1000, 3510, 3000)
    MoveCamera(21, 27, 0, 3000)
    OP_6E(470, 3000)
    SetCameraDistance(28000, 3000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_91D5():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_91D5)
    WaitChrThread(0x33, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    Sleep(500)
    OP_71(0x7, 0x0, 0x8C, 0x0, 0x0)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    OP_79(0x7)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    Sound(473, 0, 100, 0)
    OP_79(0x9)
    OP_68(450, 1000, -1190, 6000)
    MoveCamera(115, 37, 0, 8000)
    SetCameraDistance(20000, 6000)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_926C():
        OP_98(0xFE, 0xFFFFADF8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_926C)
    WaitChrThread(0x33, 1)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_6F(0x79)
    Fade(1000)
    OP_68(210, 1000, -2670, 0)
    MoveCamera(82, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(18190, 0)
    OP_0D()
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)

    def lambda_92E4():
        OP_95(0x2D, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_92E4)

    def lambda_92FE():
        OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_92FE)
    WaitChrThread(0x2D, 1)
    WaitChrThread(0x2D, 2)

    ChrTalk(
        0x29,
        (
            "#0503FWelcome to Crossbell State, sir.\x01",
            "I'm sure you must be tired from\x01",
            "your long journey here.\x02\x03",
            "#0500FFortunately, it won't be long until\x01",
            "the bus to Crossbell City arrives.\x02\x03",
            "If you'd like, feel free to rest up in\x01",
            "the mess hall while you wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#5PI think I'll take you up on that.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x29, 3, 0, 52)

    def lambda_943F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_943F)
    Sleep(750)
    Fade(1000)
    OP_68(-420, 1000, 4100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    BeginChrThread(0x2D, 3, 0, 54)
    BeginChrThread(0x31, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x32, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2C, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2B, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2E, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2F, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x30, 3, 0, 53)
    Sleep(750)
    BeginChrThread(0x2A, 3, 0, 55)
    Sleep(750)
    Sleep(5000)
    FadeToDark(500, 0, -1)
    OP_0D()
    WaitChrThread(0x29, 3)
    WaitChrThread(0x2A, 3)
    OP_68(580, 1000, 8990, 0)
    MoveCamera(38, 21, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(15260, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x33, 0x80)
    SetMapObjFlags(0x9, 0x4)
    SetChrPos(0x29, 1630, 0, 8660, 270)
    SetChrPos(0x2A, 440, 0, 8900, 270)

    def lambda_95A5():
        OP_95(0xFE, 0, 0, 13900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_95A5)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_95C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_95C9)
    WaitChrThread(0x2A, 1)
    WaitChrThread(0x2A, 2)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x1)
    OP_63(0x29, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x29)

    ChrTalk(
        0x104,
        "#0301FThat all of 'em?\x02",
    )

    CloseMessageWindow()
    OP_68(-370, 1000, 9430, 2000)
    MoveCamera(29, 21, 0, 2000)
    OP_6E(470, 2000)
    SetCameraDistance(18150, 2000)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 2, 0, 50)
    BeginChrThread(0x104, 2, 0, 51)
    Sleep(1000)

    def lambda_9674():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9674)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x29,
        (
            "#11P#0501FYes, it should be.\x02\x03",
            "Here's the passenger list. You should\x01",
            "probably give it a quick glance.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_970C():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_970C)
    WaitChrThread(0x29, 1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noel pulled out the passenger list and handed it to Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI appreciate it, Sergeant Major Seeker. This is\x01",
            "going to be a huge help.\x02\x03",
            "#0003FNine passengers total. And we're\x01",
            "positive that all of them came from\x01",
            "the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FAre you sure you are allowed to show\x01",
            "this list to people outside the CGF?\x02\x03",
            "In a way, this is tantamount to the\x01",
            "disclosure of personal information...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#11P#0500FDeputy Commander Baelz already authorized\x01",
            "me to give you any information that may assist\x01",
            "you in your investigation.\x02\x03",
            "#0503F'Considering their names and addresses aren't\x01",
            "shown on the list, we don't have to worry about\x01",
            "disclosing the details we have,' or so she said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0104FThere's the quick judgment we've come to\x01",
            "expect from the deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0306FWhew. She's scary smart, man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FAll right, then. Thanks for letting\x01",
            "us see this, Sergeant Major.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd handed the list back to Noel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9AE1():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9AE1)
    WaitChrThread(0x29, 1)

    ChrTalk(
        0x29,
        (
            "#11P#0503FIt's no problem.\x02\x03",
            "#0501FDid anything stand out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FHmm. We're definitely going to need to take a\x01",
            "closer look, if we want to be absolutely certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FWell, we should strike while the iron's hot.\x02\x03",
            "There's not much time until the bus arrives.\x02\x03",
            "We should interview the passengers and try\x01",
            "to flush out the counterfeit dealer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001FAgreed. Let's move out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FOnwards!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        "#11P#0501FI believe in you, everyone!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(95990, 750, -6440, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27500, 0)
    SetMapObjFlags(0x1, 0x10)
    OP_70(0x7, 0x0)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetChrPos(0x0, 95990, 0, -6440, 0)
    SetChrPos(0x1, 95990, 0, -6440, 0)
    SetChrPos(0x2, 95990, 0, -6440, 0)
    SetChrPos(0x3, 95990, 0, -6440, 0)
    ClearChrFlags(0x2B, 0x40)
    ClearChrFlags(0x2D, 0x40)
    ClearChrFlags(0x2E, 0x40)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_70(0x7, 0x0)
    Call(0, 56)
    OP_29(0x1B, 0x1, 0x4)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x6)
    Return()

    # Function_47_8F4B end

    def Function_48_9DA6(): pass

    label("Function_48_9DA6")


    def lambda_9DAB():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DAB)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_9DA6 end

    def Function_49_9DC5(): pass

    label("Function_49_9DC5")


    def lambda_9DCA():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9DCA)
    WaitChrThread(0x102, 1)
    Return()

    # Function_49_9DC5 end

    def Function_50_9DE4(): pass

    label("Function_50_9DE4")


    def lambda_9DE9():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9DE9)
    WaitChrThread(0x103, 1)
    Return()

    # Function_50_9DE4 end

    def Function_51_9E03(): pass

    label("Function_51_9E03")


    def lambda_9E08():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E08)
    WaitChrThread(0x104, 1)
    Return()

    # Function_51_9E03 end

    def Function_52_9E22(): pass

    label("Function_52_9E22")


    def lambda_9E27():
        OP_95(0xFE, -5000, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E27)
    WaitChrThread(0xFE, 1)

    def lambda_9E45():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E45)
    WaitChrThread(0xFE, 1)

    def lambda_9E63():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E63)
    WaitChrThread(0xFE, 1)

    def lambda_9E81():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E81)
    WaitChrThread(0xFE, 1)

    def lambda_9E9F():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E9F)
    WaitChrThread(0xFE, 1)

    def lambda_9EBD():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EBD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_9E22 end

    def Function_53_9ED7(): pass

    label("Function_53_9ED7")


    def lambda_9EDC():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EDC)

    def lambda_9EF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EF6)
    WaitChrThread(0xFE, 1)

    def lambda_9F0B():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F0B)
    WaitChrThread(0xFE, 1)

    def lambda_9F29():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F29)
    WaitChrThread(0xFE, 1)

    def lambda_9F47():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F47)
    WaitChrThread(0xFE, 1)

    def lambda_9F65():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F65)
    WaitChrThread(0xFE, 1)

    def lambda_9F83():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F83)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_9ED7 end

    def Function_54_9FA1(): pass

    label("Function_54_9FA1")

    Sleep(900)

    def lambda_9FA9():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FA9)
    WaitChrThread(0xFE, 1)

    def lambda_9FC7():
        OP_95(0xFE, -5000, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FC7)
    WaitChrThread(0xFE, 1)

    def lambda_9FE5():
        OP_95(0xFE, -5000, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FE5)
    WaitChrThread(0xFE, 1)

    def lambda_A003():
        OP_95(0xFE, 440, 0, 3300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A003)
    WaitChrThread(0xFE, 1)

    def lambda_A021():
        OP_95(0xFE, 440, 0, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A021)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_54_9FA1 end

    def Function_55_A03F(): pass

    label("Function_55_A03F")


    def lambda_A044():
        OP_95(0xFE, -60, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A044)

    def lambda_A05E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A05E)
    WaitChrThread(0xFE, 1)

    def lambda_A073():
        OP_95(0xFE, -5000, 0, -3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A073)
    WaitChrThread(0xFE, 1)

    def lambda_A091():
        OP_95(0xFE, -5000, 0, 1150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A091)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_55_A03F end

    def Function_56_A0AF(): pass

    label("Function_56_A0AF")

    ClearChrFlags(0x2A, 0x80)
    SetChrChipByIndex(0x2A, 0x1F)
    SetChrSubChip(0x2A, 0x0)
    SetChrPos(0x2A, 100990, 0, -4180, 270)
    ClearChrFlags(0x2B, 0x80)
    SetChrChipByIndex(0x2B, 0x20)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 92890, 0, 2210, 90)
    ClearChrFlags(0x2F, 0x80)
    SetChrChipByIndex(0x2F, 0x5)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, 100360, 0, 3970, 90)
    ClearChrFlags(0x30, 0x80)
    SetChrChipByIndex(0x30, 0x21)
    SetChrSubChip(0x30, 0x0)
    SetChrPos(0x30, 102900, 0, 3710, 270)
    ClearChrFlags(0x31, 0x80)
    SetChrChipByIndex(0x31, 0xD)
    SetChrSubChip(0x31, 0x0)
    SetChrPos(0x31, 162320, 150, 3010, 270)
    ClearChrFlags(0x32, 0x80)
    SetChrChipByIndex(0x32, 0x22)
    SetChrSubChip(0x32, 0x0)
    SetChrPos(0x32, 159720, 150, 3010, 90)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x2D, 104170, 0, -5830, 0)
    BeginChrThread(0x2D, 0, 0, 0)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2E, 96390, 0, 6290, 180)
    BeginChrThread(0x2E, 0, 0, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 152940, 0, 3430, 180)
    BeginChrThread(0x2C, 0, 0, 0)
    Return()

    # Function_56_A0AF end

    def Function_57_A1B8(): pass

    label("Function_57_A1B8")

    Return()

    # Function_57_A1B8 end

    def Function_58_A1B9(): pass

    label("Function_58_A1B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x2D, 0xFF)
    OP_4B(0x2E, 0xFF)
    OP_4B(0x2C, 0xFF)
    OP_4B(0x29, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(97480, 750, -770, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(28920, 0)
    OP_0D()
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, 95990, 0, -8109, 0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x40)
    ClearChrFlags(0x2E, 0x40)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Sound(105, 0, 100, 0)

    def lambda_A273():
        OP_95(0xFE, 95610, 0, -6230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_A273)

    def lambda_A28D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_A28D)
    WaitChrThread(0x29, 1)
    WaitChrThread(0x29, 2)

    ChrTalk(
        0x29,
        (
            "#0500FAttention, passengers. The bus bound\x01",
            "for Crossbell City has just arrived.\x02\x03",
            "For those boarding, please head towards\x01",
            "Tangram Gate's parking lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "#12PThe bus is here! Let's get going!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#6PYeah, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6PHoho, the time when I finally get to\x01",
            "see my grandson is almost here.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x2A, 0x18)
    SetChrSubChip(0x2A, 0x0)
    SetChrPos(0x2A, 100730, 0, -5320, 180)
    SetChrChipByIndex(0x2B, 0x19)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 92920, 0, 1410, 180)
    SetChrChipByIndex(0x2F, 0x9)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x2F, 99180, 0, 4019, 180)
    SetChrChipByIndex(0x30, 0x1D)
    SetChrSubChip(0x30, 0x0)
    SetChrPos(0x30, 104160, 0, 3700, 180)
    SetChrPos(0x2C, 98010, 0, 8280, 0)
    SetChrPos(0x31, 98010, 0, 8280, 0)
    SetChrPos(0x32, 98010, 0, 8280, 0)
    Sound(820, 0, 100, 0)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x31, 0x40)
    SetChrFlags(0x32, 0x40)
    SetChrChipByIndex(0x31, 0x6)
    SetChrChipByIndex(0x32, 0x1E)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    BeginChrThread(0x29, 3, 0, 63)
    BeginChrThread(0x2A, 3, 0, 64)
    BeginChrThread(0x2D, 3, 0, 65)
    BeginChrThread(0x2B, 3, 0, 66)
    BeginChrThread(0x2E, 3, 0, 67)
    BeginChrThread(0x2F, 3, 0, 68)
    BeginChrThread(0x30, 3, 0, 69)
    Sleep(2500)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x3)
    BeginChrThread(0x31, 3, 0, 70)
    Sleep(700)
    BeginChrThread(0x32, 3, 0, 70)
    Sleep(1500)
    BeginChrThread(0x2C, 3, 0, 70)
    Sleep(1500)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(95930, 1150, -2040, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24270, 0)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetCameraDistance(23270, 3000)
    SetChrPos(0x101, 96600, 0, -1500, 180)
    SetChrPos(0x102, 95100, 0, -1500, 180)
    SetChrPos(0x103, 96600, 0, 0, 180)
    SetChrPos(0x104, 95100, 0, 0, 180)
    SetChrPos(0x29, 95850, 0, -3800, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x29,
        "#12P#0501FHow'd it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FMy assessment is that we do not have\x01",
            "enough information to fully determine\x01",
            "who the dealer is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0301FAll those guys struck me as regular\x01",
            "people comin' to enjoy the festival.\x02\x03",
            "#0306FIs there really a criminal hidin' in that\x01",
            "group? I find it hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0003F...\x02",
    )

    CloseMessageWindow()

    def lambda_A75B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A75B)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#5P#0105FLloyd, you're being quiet. Did you\x01",
            "come to some conclusion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FSort of. There was one person who\x01",
            "said something that sounded odd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#5P#0305FSeriously?! What the hell was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FIt's still just a hunch, Randy.\x02\x03",
            "#0001FBut right now, we need to board that\x01",
            "bus and put our heads together if we\x01",
            "want to get to the bottom of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FWe should be on our way.\x02\x03",
            "Once that bus reaches the city, the passengers\x01",
            "are going to split up, and we will not be able to\x01",
            "track them down.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A9D8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A9D8)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#5P#0101FTo the bus stop, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x29,
        (
            "#12P#0501FIt's right outside the gate, in the parking lot.\x02\x03",
            "#0503FI wish I could do more, but I've done all I\x01",
            "can. I'll be praying for your success!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FThanks, Sergeant Major. We'll get it done.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x29, 0xFF)
    SetChrPos(0x0, -280, 0, 8060, 180)
    SetChrPos(0x29, 1720, 0, 7110, 270)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x4, 0x4)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_29(0x1B, 0x1, 0xD)
    EventEnd(0x5)
    Return()

    # Function_58_A1B9 end

    def Function_59_AB3A(): pass

    label("Function_59_AB3A")


    def lambda_AB3F():
        OP_95(0xFE, -1500, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB3F)
    WaitChrThread(0x101, 1)
    Return()

    # Function_59_AB3A end

    def Function_60_AB59(): pass

    label("Function_60_AB59")


    def lambda_AB5E():
        OP_95(0xFE, -1500, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB5E)
    WaitChrThread(0x102, 1)
    Return()

    # Function_60_AB59 end

    def Function_61_AB78(): pass

    label("Function_61_AB78")


    def lambda_AB7D():
        OP_95(0xFE, -3000, 0, 9500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB7D)
    WaitChrThread(0x103, 1)
    Return()

    # Function_61_AB78 end

    def Function_62_AB97(): pass

    label("Function_62_AB97")


    def lambda_AB9C():
        OP_95(0xFE, -3000, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AB9C)
    WaitChrThread(0x104, 1)
    Return()

    # Function_62_AB97 end

    def Function_63_ABB6(): pass

    label("Function_63_ABB6")


    def lambda_ABBB():
        OP_95(0xFE, 93970, 0, -5720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_ABBB)
    WaitChrThread(0x29, 1)

    def lambda_ABD9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_ABD9)
    WaitChrThread(0x29, 1)
    Return()

    # Function_63_ABB6 end

    def Function_64_ABE6(): pass

    label("Function_64_ABE6")


    def lambda_ABEB():
        OP_95(0xFE, 100730, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ABEB)
    WaitChrThread(0xFE, 1)

    def lambda_AC09():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC09)
    WaitChrThread(0xFE, 1)

    def lambda_AC27():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC27)

    def lambda_AC41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AC41)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_ABE6 end

    def Function_65_AC52(): pass

    label("Function_65_AC52")

    Sleep(2000)

    def lambda_AC5A():
        OP_95(0xFE, 95850, 0, -6040, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC5A)
    WaitChrThread(0xFE, 1)

    def lambda_AC78():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AC78)

    def lambda_AC92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AC92)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_AC52 end

    def Function_66_ACA3(): pass

    label("Function_66_ACA3")


    def lambda_ACA8():
        OP_95(0xFE, 92920, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACA8)
    WaitChrThread(0xFE, 1)

    def lambda_ACC6():
        OP_95(0xFE, 95850, 0, -3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACC6)
    WaitChrThread(0xFE, 1)

    def lambda_ACE4():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ACE4)
    Sleep(2000)

    def lambda_AD01():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AD01)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_66_ACA3 end

    def Function_67_AD12(): pass

    label("Function_67_AD12")


    def lambda_AD17():
        OP_95(0xFE, 97290, 0, 4720, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD17)
    WaitChrThread(0xFE, 1)

    def lambda_AD35():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD35)
    Sleep(6000)

    def lambda_AD52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AD52)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_AD12 end

    def Function_68_AD63(): pass

    label("Function_68_AD63")


    def lambda_AD68():
        OP_95(0xFE, 99180, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD68)
    WaitChrThread(0xFE, 1)

    def lambda_AD86():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD86)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_AD9A():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD9A)
    WaitChrThread(0xFE, 1)

    def lambda_ADAB():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADAB)
    WaitChrThread(0xFE, 1)

    def lambda_ADC9():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADC9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_AD63 end

    def Function_69_ADE3(): pass

    label("Function_69_ADE3")


    def lambda_ADE8():
        OP_95(0xFE, 104160, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADE8)
    WaitChrThread(0xFE, 1)

    def lambda_AE06():
        OP_95(0xFE, 95850, 0, -330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE06)
    WaitChrThread(0xFE, 1)

    def lambda_AE24():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE24)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_ADE3 end

    def Function_70_AE3E(): pass

    label("Function_70_AE3E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)

    def lambda_AE4E():
        OP_95(0xFE, 95850, 0, -9890, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE4E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_AE3E end

    def Function_71_AE68(): pass

    label("Function_71_AE68")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AEB6")

    ChrTalk(
        0x101,
        "#0001FLet's interview the passengers while we still can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF40")

    label("loc_AEB6")


    ChrTalk(
        0x101,
        (
            "#0001FWe don't have much time until the bus bound for\x01",
            "Crossbell City arrives.\x02\x03",
            "Let's interview the passengers while we still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_AF40")

    SetChrPos(0x0, 95790, 0, -5540, 0)
    EventEnd(0x5)
    Return()

    # Function_71_AE68 end

    def Function_72_AF54(): pass

    label("Function_72_AF54")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AFA2")

    ChrTalk(
        0x101,
        "#0001FLet's interview the passengers while we still can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B02C")

    label("loc_AFA2")


    ChrTalk(
        0x101,
        (
            "#0001FWe don't have much time until the bus bound\x01",
            "for Crossbell City arrives.\x02\x03",
            "Let's interview the passengers while we still can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_B02C")

    SetChrPos(0x0, 92410, 0, -50, 90)
    EventEnd(0x5)
    Return()

    # Function_72_AF54 end

    def Function_73_B040(): pass

    label("Function_73_B040")

    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#0003FThe bus heading to the city is about to\x01",
            "leave. Let's hurry to the bus stop.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -8140, 0, 8140, 180)
    EventEnd(0x5)
    Return()

    # Function_73_B040 end

    def Function_74_B0AD(): pass

    label("Function_74_B0AD")

    EventBegin(0x0)

    ChrTalk(
        0x101,
        (
            "#0003FThe bus heading to the city is about to\x01",
            "leave. Let's hurry to the bus stop.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 8140, 189)
    EventEnd(0x5)
    Return()

    # Function_74_B0AD end

    def Function_75_B11A(): pass

    label("Function_75_B11A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "Past this point is the Crossbell Guardian Force freight line.\x01",
            "Unauthorized entry is strictly prohibited.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_75_B11A end

    SaveToFile()

Try(main)
