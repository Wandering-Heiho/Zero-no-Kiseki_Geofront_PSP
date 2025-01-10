from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0250.bin",                # FileName
        "c0250",                    # MapName
        "c0250",                    # Location
        0x000E,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 14, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0250",                  # 0
        "Miles",                  # 1
        "Leyte",                  # 2
        "Koken",                  # 3
        "Koken",                  # 4
        "Pansy",                  # 5
        "Ryu",                    # 6
        "Anri",                   # 7
        "Fay",                    # 8
        "Fay",                    # 9
        "Chiruru",                # 10
        "Katerina",               # 11
        "Kitty",                  # 12
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch10300.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch22300.itc",                   # 04
        "chr/ch20600.itc",                   # 05
        "chr/ch22200.itc",                   # 06
        "chr/ch32700.itc",                   # 07
        "apl/ch50148.itc",                   # 08
        "chr/ch20500.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch39000.itc",                   # 0B
    ))

    DeclNpc(57950,   0,       103470,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-51779,  150,     112519,  90,   469,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  261,  0x0, 0,   4,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-58000,  0,       107489,  0,    389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-57930,  0,       110510,  180,  389,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  389,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-51250,  500,     57180,   315,  469,  0x0, 0,   8,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-57729,  0,       106739,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(57950,   0,       103470,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-58200,  699,     108930,  225,  468,  0x0, 0,   11,  0,   0,   4,   255, 255, 255,  0)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_37B",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_3D1",          # 04, 4
        "Function_5_431",          # 05, 5
        "Function_6_45C",          # 06, 6
        "Function_7_9A6",          # 07, 7
        "Function_8_A04",          # 08, 8
        "Function_9_1988",         # 09, 9
        "Function_10_43F2",        # 0A, 10
        "Function_11_4CCC",        # 0B, 11
        "Function_12_4F3C",        # 0C, 12
        "Function_13_5A91",        # 0D, 13
        "Function_14_5D8E",        # 0E, 14
        "Function_15_64D9",        # 0F, 15
        "Function_16_7C08",        # 10, 16
        "Function_17_7E62",        # 11, 17
        "Function_18_801C",        # 12, 18
        "Function_19_8668",        # 13, 19
        "Function_20_8B78",        # 14, 20
        "Function_21_8F49",        # 15, 21
        "Function_22_926B",        # 16, 22
        "Function_23_95A1",        # 17, 23
        "Function_24_96C4",        # 18, 24
        "Function_25_9764",        # 19, 25
        "Function_26_9EFB",        # 1A, 26
        "Function_27_A31B",        # 1B, 27
        "Function_28_ADED",        # 1C, 28
        "Function_29_B988",        # 1D, 29
        "Function_30_C087",        # 1E, 30
        "Function_31_C0B7",        # 1F, 31
        "Function_32_C0D3",        # 20, 32
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A")
    OP_94(0xFE, 0xCF80, 0x19938, 0xD890, 0x190AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_350")

    label("loc_37A")

    Return()

    # Function_1_350 end

    def Function_2_37B(): pass

    label("Function_2_37B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_94(0xFE, 0xFFFF2676, 0x19C08, 0xFFFF2F22, 0x1A3CE, 0x3E8)
    Sleep(300)
    Jump("Function_2_37B")

    label("loc_3A5")

    Return()

    # Function_2_37B end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_3_3A6")

    label("loc_3D0")

    Return()

    # Function_3_3A6 end

    def Function_4_3D1(): pass

    label("Function_4_3D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_430")
    OP_94(0xFE, 0xFFFF1ED8, 0x1ABA8, 0xFFFF1A78, 0x1A7E8, 0x12C)
    Sleep(1200)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    Sleep(500)
    Jump("loc_42B")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    Sleep(800)

    label("loc_42B")

    Jump("Function_4_3D1")

    label("loc_430")

    Return()

    # Function_4_3D1 end

    def Function_5_431(): pass

    label("Function_5_431")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_94(0xFE, 0xFFFF2CD4, 0x1B5B2, 0xFFFF270C, 0x1A90A, 0x3E8)
    Sleep(300)
    Jump("Function_5_431")

    label("loc_45B")

    Return()

    # Function_5_431 end

    def Function_6_45C(): pass

    label("Function_6_45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -54590, 0, 106800, 180)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51630, 0, 101720, 90)
    Jump("loc_9A5")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrPos(0xA, -55660, 0, 105850, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54300, 0, 105850, 270)
    Jump("loc_9A5")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_510")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53E")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5AB")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57950, 0, 103470, 90)
    SetChrPos(0xC, -54920, 0, 51450, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53650, 0, 51450, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54530, 0, 106440, 180)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_9A5")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_600")
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -57280, 0, 114110, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -58290, 0, 114110, 90)
    Jump("loc_9A5")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x8, 54190, 0, 103940, 270)
    BeginChrThread(0x8, 0, 0, 1)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -53150, 0, 112450, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -54140, 0, 112450, 0)
    Jump("loc_9A5")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D2")
    SetChrPos(0x8, 54410, 0, 103050, 90)
    SetChrPos(0x9, 55730, 0, 103050, 270)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51530, 0, 102490, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -51530, 0, 101260, 0)
    Jump("loc_9A5")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_756")
    SetChrPos(0x8, 57080, 0, 106510, 315)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -53130, 0, 105180, 0)
    SetChrPos(0xA, -53120, 0, 106320, 180)
    SetChrPos(0xC, -52650, 0, 54740, 45)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_9A5")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_784")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xC, -51660, 0, 46480, 90)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_9A5")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7FC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_825")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85C")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_857")

    Jump("loc_9A5")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_930")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -10020, 0, 3600, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E2")
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    BeginChrThread(0xD, 0, 0, 5)
    Jump("loc_92B")

    label("loc_8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926")
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    Jump("loc_92B")

    label("loc_926")

    ClearChrFlags(0x13, 0x80)

    label("loc_92B")

    Jump("loc_9A5")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_978")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_973")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_973")

    Jump("loc_9A5")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_99C")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9A5")

    label("loc_9A5")

    Return()

    # Function_6_45C end

    def Function_7_9A6(): pass

    label("Function_7_9A6")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CA")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_9D0")

    label("loc_9CA")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A03")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_A03")

    Return()

    # Function_7_9A6 end

    def Function_8_A04(): pass

    label("Function_8_A04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AF5")

    ChrTalk(
        0xFE,
        "Today's the last day of the Anniversary Festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The festival sprung into existence to celebrate\x01",
            "Crossbell State's founding and to pray for\x01",
            "its continued peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I just want to spend the whole day meditating.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1984")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_C1F")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Were you able to find the missing child, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure his parents are terribly worried.\x01",
            "Please, you have to find him as soon as\x01",
            "possible.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(
        0x101,
        (
            "#0000FYou can count on us. We've already managed\x01",
            "to pinpoint his whereabouts.\x02\x03",
            "Thanks for your help, Uncle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C17")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1984")

    label("loc_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")

    ChrTalk(
        0x101,
        (
            "#0003F(I'm sure Uncle Miles saw the parade.\x01",
            "We should try asking him for details.)\x02\x03",
            "#0000FHey, Uncle. Do you have a second?\x01",
            "There's something I need to ask...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked if he\x01",
            "knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Is this the child you were talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks exactly like him. I'm pretty sure\x01",
            "I've met this kid before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSeriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep, he bumped into me while I was walking\x01",
            "around East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I believe he ran up north from there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3308FHe ran north from East Street...? That\x01",
            "means he headed to the Harbor District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, sounds likely.\x02\x03",
            "#0000FThanks a lot, Uncle. You've been\x01",
            "incredibly helpful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Jump("loc_1009")

    label("loc_F02")


    ChrTalk(
        0xFE,
        (
            "I'm pretty sure I've met him before.\x01",
            "An energetic one, he was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He bumped into me at the intersection\x01",
            "on East Street, and I believe he ran up\x01",
            "north afterwards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but feel worried for him... Lloyd,\x01",
            "you've got to help the poor fella out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    Jump("loc_1984")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_108D")

    ChrTalk(
        0xFE,
        "Goodness gracious, what a crowd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha, imagine if someone at my\x01",
            "age got lost. What would we even do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1984")

    label("loc_108D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(
        0xFE,
        "We're heading out to see the parade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, figure I can't invite you and\x01",
            "your friends. Right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please be careful out there.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1159")

    ChrTalk(
        0x101,
        "#0000FOf course. Thank you, Uncle.\x02",
    )

    CloseMessageWindow()

    label("loc_1159")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1984")

    label("loc_1161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_135D")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AA")

    ChrTalk(
        0xFE,
        "Well, if it isn't Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're on duty today, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, a detective's work is never finished.\x02\x03",
            "Hey, Uncle. Have you started your\x01",
            "vacation yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yep. I'm planning on going out for\x01",
            "a bit of a stroll later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love for Cecile to join us, but she's\x01",
            "too busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1358")

    label("loc_12AA")


    ChrTalk(
        0xFE,
        (
            "I think even a detective like yourself would\x01",
            "have trouble navigating this crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure you take rests when you need\x01",
            "to. Wouldn't want you to wear yourself out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1358")

    Jump("loc_1984")

    label("loc_135D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1984")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")

    ChrTalk(
        0x101,
        "#0000FLong time no see, Uncle Miles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, you're...! Well, if it isn't little\x01",
            "Lloyd from next door!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What a pleasant surprise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd heard that you were back in town,\x01",
            "but I didn't think that you'd grown\x01",
            "so much. I hardly recognize you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FI may have grown physically, but\x01",
            "I'd hardly call myself a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wouldn't say that. You did pass the\x01",
            "qualification exam to become a\x01",
            "detective, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure if Guy were still here, he'd be\x01",
            "proud of his little brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FYou...really think so?\x02\x03",
            "I'd be glad if that were truly the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He absolutely would. Don't worry about it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AF")

    ChrTalk(
        0xFE,
        (
            "By the way, did you want to stick around?\x01",
            "The wife's in the kitchen if you wanted\x01",
            "to say hello.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sure she'll be ecstatic to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah. I'll do just that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1752")

    label("loc_16AF")


    ChrTalk(
        0xFE,
        (
            "My job keeps me out of the house, but\x01",
            "my wife is usually home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please rely on her if you ever need some\x01",
            "help, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks, I'm in your debt.\x02",
    )

    CloseMessageWindow()

    label("loc_1752")

    SetScenarioFlags(0x4D, 7)
    Jump("loc_1984")

    label("loc_175A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193F")

    ChrTalk(
        0xFE,
        (
            "To think you'd come back so\x01",
            "grown up... I guess that means\x01",
            "I've also aged a fair bit, haha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You've said hi to Cecile already, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI have. Well, by phone, anyway.\x02\x03",
            "I'll meet up with her when I have some\x01",
            "time off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, I see. Well, that's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, you're family to us.\x01",
            "I'm relieved to have you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My job keeps me out of the house, but\x01",
            "my wife is usually home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please rely on her if you ever need some\x01",
            "help, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1984")

    label("loc_193F")


    ChrTalk(
        0xFE,
        (
            "You're family. You can rely on us\x01",
            "whenever you need help, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1984")

    TalkEnd(0xFE)
    Return()

    # Function_8_A04 end

    def Function_9_1988(): pass

    label("Function_9_1988")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A1")
    Call(0, 25)
    TalkEnd(0xFE)
    Return()

    label("loc_19A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBF")

    ChrTalk(
        0x101,
        (
            "#0000FHi, Auntie. It's been a while.\x02\x03",
            "#0006FSorry I haven't been able to stay in touch.\x01",
            "I've been really busy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, well, if it isn't Lloyd and his friends!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard that you've been working your\x01",
            "butts off lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't you get featured in the Crossbell Times?\x01",
            "Hehehe, I'm so proud of you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, now. Come here and tell me\x01",
            "all about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, ma'am. I'll recount my heroic exploits\x01",
            "to you and spare no details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FWe had a hard time dealing\x01",
            "with a lot of it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202FPlease contact the SSS if you ever find\x01",
            "yourself needing our assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0006FHold on a minute, everyone... Don't you\x01",
            "have the slightest bit of shame?\x02\x03",
            "Haven't you all been acting WAY too\x01",
            "friendly with my aunt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FOh, don't be so stingy. She's Cecile's\x01",
            "mother, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYeah, man. She treats us like family\x01",
            "and feeds us. Why are you killin'\x01",
            "the vibe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Listen to your friends, Lloyd. There's no\x01",
            "need to be a stranger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That goes to the rest of you, too.\x01",
            "Come by any time you'd like. We'd\x01",
            "be more than happy to have you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYou bet'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThank you, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FRoger.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006F(Yeah, you're all being a little bit too friendly\x01",
            "for my tastes...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 6)
    TalkEnd(0xFE)
    Return()

    label("loc_1EBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1ECD")
    Jump("loc_43EE")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F37")

    ChrTalk(
        0xFE,
        "I hope to pray at the cathedral today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to hurry up and get ready to leave.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43EE")

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_220A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215E")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Oh, Tio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FYes, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got a weary look on your face,\x01",
            "so I thought you might be exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is it my imagination? Are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0208FI think it is simple fatigue from investigating\x01",
            "the Moon Temple yesterday.\x02\x03",
            "#0203FI may have strained myself a bit too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FTio Tot's always savin' us with her\x01",
            "perceptive abilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, she's helped us more times than I can count.\x01",
            "Try not to push yourself too hard, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FYes, I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2205")

    label("loc_215E")


    ChrTalk(
        0xFE,
        (
            "I don't know what happened, but it sounds\x01",
            "like she had a rough day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure you get lots of rest, okay? You're\x01",
            "banned from straining yourself any further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2205")

    Jump("loc_43EE")

    label("loc_220A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EA")

    ChrTalk(
        0x104,
        "#0300F'Sup, Mrs. Neues. It's been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0102FIt's lovely to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSorry to barge in with a crowd every\x01",
            "time, Aunt Leyte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I don't mind at all! Things are\x01",
            "more lively this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems like you guys are hard\x01",
            "at work again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "What's this? I don't believe I've seen that\x01",
            "girl before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is she a new member of the SSS? You\x01",
            "look like a lovely young lady.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_240C")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_240C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_244D")
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    label("loc_244D")


    ChrTalk(
        0x109,
        (
            "#0505FL-Lovely?\x02\x03",
            "I-I serve the Guardian Force, and, um,\x01",
            "I'm cooperating with the S-Special\x01",
            "Support S-Section for now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYa gotta chill out a bit, Noel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0505FS-Sorry, I'm not doing it on purpose...\x02\x03",
            "#0503FI'm just a bit shocked because it's the f-first\x01",
            "time anybody's ever called me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I am detecting an unexpected weakness\x01",
            "of Noel's.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You really are a lovely girl.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 0)
    Jump("loc_26BB")

    label("loc_25EA")


    ChrTalk(
        0xFE,
        (
            "You said you work for the Guardian Force?\x01",
            "No need to be so tense. You can relax around us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0501FYes, ma'am! Noel Seeker now relaxing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Sergeant Major Seeker hasn't loosened\x01",
            "up at all...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BB")

    Jump("loc_43EE")

    label("loc_26C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_27A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26DB")
    Call(0, 10)
    Jump("loc_279C")

    label("loc_26DB")


    ChrTalk(
        0xFE,
        (
            "KeA sure loves to read books,\x01",
            "doesn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'm going to borrow some children's\x01",
            "books for her to read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my husband will be more than\x01",
            "happy to oblige if I ask him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    Jump("loc_43EE")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_28BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286E")

    ChrTalk(
        0xFE,
        "It's good to see you all again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worn down from soaking in the entire\x01",
            "festival, so I'm taking it easy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, of course, plan to watch the fireworks\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28B9")

    label("loc_286E")


    ChrTalk(
        0xFE,
        (
            "Having a lazy day with your uncle\x01",
            "every once in a while isn't so bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B9")

    Jump("loc_43EE")

    label("loc_28BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_29E9")

    ChrTalk(
        0xFE,
        (
            "He got separated from his parents during\x01",
            "the parade due to the heavy congestion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time for the police to do their duty, Lloyd.\x01",
            "You have to find him as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E1")

    ChrTalk(
        0x101,
        (
            "#0000FYeah, you're right. Everyone, get ready to\x01",
            "depart. We've gotta find him fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E1")

    SetScenarioFlags(0x0, 1)
    Jump("loc_43EE")

    label("loc_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2AD9")

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd. You said you were looking\x01",
            "for a missing child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking back on it, your uncle did meet\x01",
            "a little boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was standing out there all alone,\x01",
            "so he was worried that he'd been\x01",
            "separated from his parents.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43EE")

    label("loc_2AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C06")

    ChrTalk(
        0xFE,
        (
            "Phew... That crowd during the parade sure\x01",
            "was something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was everything okay for you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, about that... We actually ended\x01",
            "up missing the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What, you did?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's a crying shame. This year's\x01",
            "parade was unlike any other.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C8A")

    label("loc_2C06")


    ChrTalk(
        0xFE,
        (
            "Fortunately for you, I took great pictures\x01",
            "of the whole thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll make some copies to give to you\x01",
            "and the others later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8A")

    Jump("loc_43EE")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D00")

    ChrTalk(
        0xFE,
        "It's about time for the parade to begin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if we could get Cecile\x01",
            "to join us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43EE")

    label("loc_2D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(
        0xFE,
        "Your uncle isn't here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FHuh? You're not going with him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, he said he was interested in going\x01",
            "to that symposium that's being\x01",
            "held at the reception hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your uncle has always had a soft\x01",
            "spot for events like these.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E92")

    label("loc_2E11")


    ChrTalk(
        0xFE,
        (
            "I'll be watching the house alone while\x01",
            "he's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, maybe I should prepare a feast. I've\x01",
            "got the time, after all...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E92")

    Jump("loc_43EE")

    label("loc_2E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3121")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B8")

    ChrTalk(
        0x101,
        (
            "#0000FHi, Auntie.\x02\x03",
            "#0009FThank you for dinner yesterday.\x01",
            "It was indescribably delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it was no big deal. Come by\x01",
            "again any time you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FLloyd's gone and imposed himself upon\x01",
            "the Neues household again, has he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FWhat's the big idea, bud? Where's our\x01",
            "invitation?\x02\x03",
            "#0306FI wanted to see Cecile, too, man.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006FThat's rich, coming from you. Weren't\x01",
            "you out partying with her coworkers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0111FHave some shame, Randy...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_311C")

    label("loc_30B8")


    ChrTalk(
        0xFE,
        (
            "I'm planning to check out the\x01",
            "festival with your uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Keep up the good work, everybody.\x02",
    )

    CloseMessageWindow()

    label("loc_311C")

    Jump("loc_43EE")

    label("loc_3121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_33D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3356")

    ChrTalk(
        0xFE,
        "Oh, welcome back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you going somewhere again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, there are still a few things that\x01",
            "need investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. I'm pleased that you seem to be\x01",
            "enjoying your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should tell me more about it when\x01",
            "you've got time. I'm looking forward\x01",
            "to hearing some interesting stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FOf course. It'd be our pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(We obviously have to keep the whole Arc\x01",
            "en Ciel situation under wraps for now.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F(Yeah, the sooner we wrap this up,\x01",
            "the sooner it becomes a funny story\x01",
            "to tell.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33CB")

    label("loc_3356")


    ChrTalk(
        0xFE,
        (
            "You should tell me more about it when\x01",
            "you've got time. I'm looking forward\x01",
            "to hearing some interesting stories.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33CB")

    Jump("loc_43EE")

    label("loc_33D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D4")

    ChrTalk(
        0xFE,
        "Hey, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FYes? What is it, Auntie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You seem like you've matured a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about you seems more\x01",
            "sharp. It reminds me a little of Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha, really? Probably cause I've\x01",
            "caught up to him in age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F(Nah, dude. It's 'cause you officially grew\x01",
            "into a man last night.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204F(I believe this is what they call 'climbing the\x01",
            "stairs of adulthood.')\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    ChrTalk(
        0x101,
        "#0011FI-I told you guys that you've got it all wrong!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F#2S*sigh*...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_364E")

    label("loc_35D4")


    ChrTalk(
        0xFE,
        "You seem like you've matured a bit, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about you seems more\x01",
            "sharp. It reminds me a little of Guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364E")

    Jump("loc_43EE")

    label("loc_3653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_372B")

    ChrTalk(
        0xFE,
        (
            "Things are about to get a lot more lively with\x01",
            "the Anniversary Festival next month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope Cecile can take some time off\x01",
            "to come visit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She'd better ask well in advance,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43EE")

    label("loc_372B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_37AB")

    ChrTalk(
        0xFE,
        (
            "You Special Support Section folks shouldn't\x01",
            "act reserved, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'd love for you to visit more often.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43EE")

    label("loc_37AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_39D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C7")
    Call(0, 11)
    Jump("loc_39CF")

    label("loc_37C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D9")
    Call(0, 26)
    Jump("loc_39CF")

    label("loc_37D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393A")

    ChrTalk(
        0xFE,
        (
            "She's an adult. I don't intend to tell\x01",
            "her how she should live her life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I think it's time for her to start thinking\x01",
            "a little more carefully about her future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should go to the cathedral and pray\x01",
            "for Cecile to find herself a nice man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I'm just going to...walk away and\x01",
            "pretend I didn't hear anything.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39CF")

    label("loc_393A")


    ChrTalk(
        0xFE,
        (
            "I'll be going to the cathedral later today to\x01",
            "pray all afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to pray for Cecile to find herself\x01",
            "a nice man while I'm there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CF")

    Jump("loc_43EE")

    label("loc_39D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3C37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F0")
    Call(0, 11)
    Jump("loc_3C32")

    label("loc_39F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB8")

    ChrTalk(
        0xFE,
        (
            "Cecile's so busy with work that she can't\x01",
            "even visit us on weekends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish she would, though. It's not like she\x01",
            "has a husband to keep her busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FDon't be too hard on her, Auntie.\x01",
            "Cecile's already got enough on her\x01",
            "plate to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, yes. I'm well aware. That doesn't\x01",
            "change the fact that I'd like to see her\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She should at least come home and enjoy\x01",
            "the occasional meal with us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C32")

    label("loc_3BB8")


    ChrTalk(
        0xFE,
        (
            "Work, work, work. That's all Cecile ever\x01",
            "thinks about. It'd be nice for her to come\x01",
            "and visit us during the weekend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C32")

    Jump("loc_43EE")

    label("loc_3C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3EA4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C53")
    Call(0, 11)
    Jump("loc_3E9F")

    label("loc_3C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E3E")

    ChrTalk(
        0xFE,
        "Lloyd and his friends have come to visit again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't seen you in quite some time.\x01",
            "How's everything? Is work going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, it's all right, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FIt's nothin' more than a bunch of chores.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't sweat it! Everybody\x01",
            "starts off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure everything will turn out okay\x01",
            "as long as you give it your all. I'm\x01",
            "sure Guy is watching over you, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FYeah, you're right. Thanks for the\x01",
            "encouragement, Auntie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E9F")

    label("loc_3E3E")


    ChrTalk(
        0xFE,
        "Anyway, your uncle's gone to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to tidy up the place before I\x01",
            "leave to pray.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E9F")

    Jump("loc_43EE")

    label("loc_3EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_41F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4135")
    OP_93(0xFE, 0x13B, 0x0)

    ChrTalk(
        0xFE,
        "Oh, thank you Aidios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm beyond grateful that you kept those\x01",
            "children safe from harm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F(She's quite pious, isn't she?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Yeah, she's always been like this.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD2")

    ChrTalk(
        0x101,
        (
            "#0000F(Auntie's always been praying, even when\x01",
            "my brother was...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_3FD2")


    ChrTalk(
        0x101,
        (
            "#0000F(Auntie's always been praying, even when\x01",
            "Guy was killed in the line of duty.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_402B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oh, my. I didn't notice all of you\x01",
            "standing there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your uncle's gone off to the library to work,\x01",
            "if you're looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He loves being a librarian. You can tell by\x01",
            "the spring in his step as he goes off to work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41F3")

    label("loc_4135")


    ChrTalk(
        0xFE,
        (
            "Your uncle's gone off to work, if you're\x01",
            "looking for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His love for books runs so deep that he\x01",
            "became a librarian. He always leaves for\x01",
            "work with a giant smile across his face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F3")

    Jump("loc_43EE")

    label("loc_41F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_43EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435B")

    ChrTalk(
        0xFE,
        "It's been three years since the incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cecile used to tell me about how lonely\x01",
            "and upset she was every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should gather everyone and\x01",
            "throw a nice little party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011F(It'd be pointless to try and stop her now...)\x02\x03",
            "#0006F(She's too powerful when she gets like\x01",
            "this... Some things just never change.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_43EE")

    label("loc_435B")


    ChrTalk(
        0xFE,
        (
            "It's been three years since you've been\x01",
            "home, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the perfect occasion for everybody\x01",
            "to get together and throw a celebration!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43EE")

    TalkEnd(0xFE)
    Return()

    # Function_9_1988 end

    def Function_10_43F2(): pass

    label("Function_10_43F2")

    OP_93(0x9, 0x5A, 0x0)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(56890, 1000, 103430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, 55780, 0, 103550, 90)
    SetChrPos(0xEF, 55940, 0, 104600, 135)
    SetChrPos(0x153, 55940, 0, 102750, 90)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_44C2")

    ChrTalk(
        0x9,
        "Oh, it's Lloyd and Elie...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4519")

    label("loc_44C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_44EF")

    ChrTalk(
        0x9,
        "Oh, it's Lloyd and Tio...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4519")

    label("loc_44EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4519")

    ChrTalk(
        0x9,
        "Oh, it's Lloyd and Randy...\x02",
    )

    CloseMessageWindow()

    label("loc_4519")


    ChrTalk(
        0x9,
        (
            "And... Oh, my. Who's this little\x01",
            "bundle of sunshine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThis is KeA. She's actually going\x01",
            "to be staying with us at the SSS\x01",
            "building for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FHiya, miss! You've got SO many\x01",
            "books here! I'm jealous!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do you like to read, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "My husband and I do, too. He even\x01",
            "works over at the library.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E4")

    ChrTalk(
        0x153,
        (
            "#1111FLie-berry?\x02\x03",
            "#1110FOh, I know! That's where you can\x01",
            "go borrow a bunch of books!\x02\x03",
            "#1109FLloyd, Lloyd! Can we go there next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FWell, maybe. I'm just not sure if we\x01",
            "should make any unnecessary stops...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_47D9")

    ChrTalk(
        0x102,
        (
            "#0100FBut think about how happy it would make\x01",
            "KeA. Surely it wouldn't hurt for us\x01",
            "to stop by there for a bit, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48C0")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_484F")

    ChrTalk(
        0x103,
        (
            "#0200FImagine how excited KeA would\x01",
            "be if we went. Is there an issue\x01",
            "with going for a few minutes?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48C0")

    label("loc_484F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_48C0")

    ChrTalk(
        0x104,
        (
            "#0300FThink about how happy you'd make\x01",
            "KeDo, Lloyd. What's the issue with\x01",
            "showin' her the library?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48C0")


    ChrTalk(
        0x101,
        "#0000FI guess we could...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B69")

    label("loc_48E4")


    ChrTalk(
        0x153,
        (
            "#1110FLie-berry? I think I've been to one\x01",
            "of those before!\x02\x03",
            "#1109FLloooyd! I wanna go to the library\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FI know you do, but I'm not sure if\x01",
            "we should make any detours now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4A06")

    ChrTalk(
        0x102,
        (
            "#0100FOh, come on, Lloyd. KeA was so\x01",
            "ecstatic when we went last time,\x01",
            "remember?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B1C")

    label("loc_4A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4AA2")

    ChrTalk(
        0x103,
        (
            "#0200FLloyd. It was obvious that KeA\x01",
            "loved visiting the library. Would\x01",
            "it really hurt to go once more?\x02\x03",
            "Is it that big an inconvenience?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B1C")

    label("loc_4AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4B1C")

    ChrTalk(
        0x104,
        (
            "#0300FLighten up, Lloyd. You remember how\x01",
            "KeDo lit up when we first stepped in the\x01",
            "place? Why not go again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B1C")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0000FWhen did we all become her parents...?\x02",
    )

    CloseMessageWindow()

    label("loc_4B69")


    ChrTalk(
        0x9,
        (
            "Oh, Lloyd. Most people would\x01",
            "love to be in your position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "KeA, please make sure to come\x01",
            "visit again. Auntie Leyte will read\x01",
            "all sorts of books with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1109FI'd love that!\x02\x03",
            "See ya, Auntie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Until next time, sweetie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Makes sense that Aunt Leyte would be\x01",
            "used to handling kids. She'd always\x01",
            "look after me, after all.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 7)
    EventEnd(0x5)
    Return()

    # Function_10_43F2 end

    def Function_11_4CCC(): pass

    label("Function_11_4CCC")


    ChrTalk(
        0xFE,
        "Lloyd and his friends have come to visit again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't seen you in quite some time.\x01",
            "How's everything? Is work going well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha, it's all right, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FIt's nothin' more than a bunch of chores.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, don't sweat it! Everybody\x01",
            "starts off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While you're here, why don't I give\x01",
            "you a few cooking tips?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Given how many calories you must burn\x01",
            "in a day, it's crucial that your diet has the\x01",
            "proper vitamins and minerals you need.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
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
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F3B")
    SetScenarioFlags(0x0, 1)

    label("loc_4F3B")

    Return()

    # Function_11_4CCC end

    def Function_12_4F3C(): pass

    label("Function_12_4F3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5014")

    ChrTalk(
        0xFE,
        (
            "Chiruru says she wants to hike through\x01",
            "the Mainz Mountains and into Leman State.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's impossible. And besides, that's Erebonia\x01",
            "on the other side of the mountains, not Leman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_504C")

    label("loc_5014")


    ChrTalk(
        0xFE,
        (
            "I've got the most difficult children in\x01",
            "the world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504C")

    Jump("loc_5A8D")

    label("loc_5051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5062")
    Call(0, 13)
    Jump("loc_5A8D")

    label("loc_5062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514C")

    ChrTalk(
        0xFE,
        (
            "Why can't Ryu be like Momo from Tallys'\x01",
            "place? She's a good kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's a smart cookie, and she always helps\x01",
            "out with their work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish that my little Ryu would learn a\x01",
            "thing or two from her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_517E")

    label("loc_514C")


    ChrTalk(
        0xFE,
        (
            "*sigh* If only Ryu would follow her\x01",
            "example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517E")

    Jump("loc_5A8D")

    label("loc_5183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5212")

    ChrTalk(
        0xFE,
        (
            "Sounds like Chiruru's going some place\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ryu's already a handful, but I can't seem\x01",
            "to figure out Chiruru, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8D")

    label("loc_5212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_52E1")

    ChrTalk(
        0xFE,
        (
            "There's nothing quite like festivals!\x01",
            "I think I'll go to Central Square today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Chiruru is still acting like a social recluse...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm treatin' her and everything today, and\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8D")

    label("loc_52E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_53DE")

    ChrTalk(
        0xFE,
        (
            "The kids from West Street and the Residential\x01",
            "District have Sunday School today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'd be nice if I could get Ryu to treat\x01",
            "his studies a little more seriously...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 0)), scpexpr(EXPR_END)), "loc_53D9")

    ChrTalk(
        0x101,
        (
            "#0003F(...Sorry. He's busy fooling around\x01",
            "with Zeit.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53D9")

    Jump("loc_5A8D")

    label("loc_53DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CE")

    ChrTalk(
        0xFE,
        (
            "I want Ryu to be the future successor\x01",
            "of my business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if that's going to happen, though.\x01",
            "He's foolin' around again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not particularly bright, either.\x01",
            "He always skips Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5583")

    label("loc_54CE")


    ChrTalk(
        0xFE,
        (
            "I want to teach Ryu the basics of\x01",
            "running a business, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...that kid's been testing my patience, and\x01",
            "he's pushing his luck. He doesn't listen to\x01",
            "a single thing I say!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5583")

    Jump("loc_5A8D")

    label("loc_5588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5612")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hmm, Ryu better not be thinking about\x01",
            "keeping it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want him to listen to my words for once\x01",
            "in his life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A8D")

    label("loc_5612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_575A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571F")

    ChrTalk(
        0xFE,
        (
            "I'm heading to the Times Department Store\x01",
            "to wholesale some goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've found a new item to invest in, so I\x01",
            "want to try creating a market for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta do something to stand out amongst\x01",
            "the other traders in this business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5755")

    label("loc_571F")


    ChrTalk(
        0xFE,
        (
            "It takes time to create a market for a new\x01",
            "item.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5755")

    Jump("loc_5A8D")

    label("loc_575A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5920")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586B")

    ChrTalk(
        0xFE,
        (
            "I've been doing business in Crossbell for\x01",
            "about three years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most traders wholesale items like sundries\x01",
            "to larger shops, like a department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm from Calvard, so I've got a pretty good\x01",
            "grasp on the goods being sold there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_591B")

    label("loc_586B")


    ChrTalk(
        0xFE,
        (
            "I'm finally earning a stable income after\x01",
            "starting my business here three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Scoring that contract with the Times\x01",
            "Department Store grew my\x01",
            "business big time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_591B")

    Jump("loc_5A8D")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A36")

    ChrTalk(
        0xFE,
        (
            "You wouldn't believe what I saw this morning\x01",
            "when I opened my copy of the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was a picture of Ryu staring right\x01",
            "at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Th-That damn fool of a son!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd better believe I went and scolded\x01",
            "him as hard as I could.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A8D")

    label("loc_5A36")


    ChrTalk(
        0xFE,
        (
            "Geez, that kid. After a scolding like that,\x01",
            "I hope he learns his lesson for once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A8D")

    TalkEnd(0xFE)
    Return()

    # Function_12_4F3C end

    def Function_13_5A91(): pass

    label("Function_13_5A91")

    OP_4B(0xA, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0xA, 0x11, 0)
    TurnDirection(0x11, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C03")

    ChrTalk(
        0xA,
        (
            "Hey, Chiruru. Did you just get back?\x01",
            "How was your trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I almost drowned on three different occasions.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I went to some marshlands this time...\x01",
            "Pretty dangerous stuff. Those swamps\x01",
            "seemed like they were bottomless.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Wh-What?! Isn't that way too dangerous?\x01",
            "Just where the heck did you go?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5D85")

    label("loc_5C03")


    ChrTalk(
        0xA,
        (
            "I knew I should have listened to my gut.\x01",
            "I can't leave you to your own devices, Chiruru.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm coming along with you next time.\x01",
            "I think it'll be a good idea for me to join\x01",
            "you every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Fine by me. Are you sure you can handle\x01",
            "it, though? I walk fairly long distances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just because I'm old, it doesn't mean I'm frail!\x01",
            "I can handle something that simple!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D85")

    OP_4C(0xA, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_13_5A91 end

    def Function_14_5D8E(): pass

    label("Function_14_5D8E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E22")
    Jump("loc_5E6C")

    label("loc_5E22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E42")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E6C")

    label("loc_5E42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E62")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5E6C")

    label("loc_5E62")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E6C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E9F")
    Jump("loc_64D1")

    label("loc_5E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5EAD")
    Jump("loc_64D1")

    label("loc_5EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5EBB")
    Jump("loc_64D1")

    label("loc_5EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6041")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FAA")

    ChrTalk(
        0xFE,
        (
            "Hahaha! This is what it means to have\x01",
            "a booming business!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've scored contracts with three new stores\x01",
            "this month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And you know what the best part is?\x01",
            "I didn't chase after them. They approached me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_603C")

    label("loc_5FAA")


    ChrTalk(
        0xFE,
        (
            "I've scored contracts with three new stores\x01",
            "this month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha! All this work to build up my reputation\x01",
            "is finally starting to pay off!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_603C")

    Jump("loc_64D1")

    label("loc_6041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_613A")
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hmm, I'm purchasing a lot more goods than I\x01",
            "was anticipating. I should look into delivering\x01",
            "them via freight train or airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, it's too late now. I'd have to look into\x01",
            "shipping it via truck when it arrives at\x01",
            "Altair.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D1")

    label("loc_613A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_62E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6249")

    ChrTalk(
        0xFE,
        (
            "Sorting purchasing slips, arranging transportation,\x01",
            "balancing accounts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sheesh, I've got a ton of work to do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to grit my teeth and bear it, though!\x01",
            "How else am I going to get time off during\x01",
            "the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_62E4")

    label("loc_6249")


    ChrTalk(
        0xFE,
        (
            "I'm a Crossbellan, too. I wanna relax and\x01",
            "enjoy the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to take care of all of my business\x01",
            "while I've still got time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E4")

    Jump("loc_64D1")

    label("loc_62E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_64D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6413")

    ChrTalk(
        0xFE,
        (
            "Most shops hold large sales during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've got my work cut out for me as a wholesaler.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    ChrTalk(
        0xFE,
        (
            "An extra 84 tubes of toothpaste and 250 more\x01",
            "copies of the standard magazines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(*click* *click*) Hmm, I think I'll be able\x01",
            "to make it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_64D1")

    label("loc_6413")


    ChrTalk(
        0xFE,
        (
            "Curious about this little gadget, are we?\x01",
            "This is called an 'abacus.' It's an analog\x01",
            "calculator from the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just about any trader from the East will\x01",
            "have one of these bad boys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64D1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5D8E end

    def Function_15_64D9(): pass

    label("Function_15_64D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6503")
    Call(0, 27)
    Return()

    label("loc_6503")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6871")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F7")

    ChrTalk(
        0x101,
        (
            "#0000FCould we speak to you for a moment?\x02\x03",
            "Have you recently started taking care of\x01",
            "a cat? Or, do you know anyone else\x01",
            "who may be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh! You're talking about that kitten\x01",
            "Ryu found the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They told me a bit about the kitten,\x01",
            "but I don't know who has it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not impossible to think that Dad or\x01",
            "Wendy would keep the cat, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those two are freak engineers.\x01",
            "I don't know if they're interested in\x01",
            "anything that can breathe.\x02",
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
        (
            "#0006F(Wendy's sister is pretty sharp for\x01",
            "her age...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI doubt she knows any more information\x01",
            "than she has already stated.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x3)
    Jump("loc_686C")

    label("loc_67F7")


    ChrTalk(
        0xFE,
        (
            "Ryu and Anri came earlier to ask about\x01",
            "the kitten, but I don't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't think anyone here owns a pet.\x02",
    )

    CloseMessageWindow()

    label("loc_686C")

    Jump("loc_7C04")

    label("loc_6871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6995")

    ChrTalk(
        0xC,
        (
            "I bet Dad borrowed that book to try\x01",
            "and get me to become a railway\x01",
            "engineer when I grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He did the same thing with Wendy.\x01",
            "Got her a bunch of toys to play with,\x01",
            "and now she's an engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He probably thinks he's sooo smart.\x01",
            "I'm not going to fall for his plan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C04")

    label("loc_6995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BA8")

    ChrTalk(
        0x101,
        (
            "#0000FHey there, Pansy. You watchin' the house\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, yeah. You're Wendy's friend, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thanks for always looking after her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102FWe should be the ones thanking her.\x01",
            "She always does excellent work for us.\x02\x03",
            "#0100FAre you handling the cleaning today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah. There's no point in relying on\x01",
            "my dad or Wendy, they don't know how\x01",
            "to clean at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can you guys tell them to try a\x01",
            "little bit harder? Thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FHa, haha...\x01",
            "(Kids grow up so fast these days, huh?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)
    Jump("loc_7C04")

    label("loc_6BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C99")

    ChrTalk(
        0xFE,
        (
            "I heard that Mariabell deals with all\x01",
            "of the technology at the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And, she's not a half-bad orbal engineer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is she super pretty, but she's\x01",
            "also super smart! I love her sooo much!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CE1")

    label("loc_6C99")


    ChrTalk(
        0xFE,
        "Mariabell is super cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's the ideal woman. I admire her!\x02",
    )

    CloseMessageWindow()

    label("loc_6CE1")

    Jump("loc_7C04")

    label("loc_6CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6DDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA2")

    ChrTalk(
        0xFE,
        "Wendy slept in late this morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried whispering into her ear about orbal\x01",
            "circuits, but I couldn't get her to wake up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* She's hopeless.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6DD5")

    label("loc_6DA2")


    ChrTalk(
        0xFE,
        (
            "She's one of the laziest people\x01",
            "in the world!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD5")

    Jump("loc_7C04")

    label("loc_6DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBA")

    ChrTalk(
        0xFE,
        (
            "Mariabell was featured in some\x01",
            "business magazine today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care what kind of magazine it is.\x01",
            "I need it. Now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to cut out her pictures\x01",
            "and make a scrapbook out of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6EFF")

    label("loc_6EBA")


    ChrTalk(
        0xFE,
        (
            "Mariabell is amazing! When I grow up,\x01",
            "I wanna be just like her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EFF")

    Jump("loc_7C04")

    label("loc_6F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_70C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7038")

    ChrTalk(
        0xFE,
        (
            "Hey, Lloyd. You're friends with Wendy,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, I used to live in this same apartment\x01",
            "complex back when we were kids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So you hung out with her a lot, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She went out with some crazy bedhead\x01",
            "this morning. I can't believe how\x01",
            "much of a klutz she is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_70BD")

    label("loc_7038")


    ChrTalk(
        0xFE,
        (
            "Yep. There's no way I'm going to\x01",
            "become an engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She doesn't put on makeup when she goes\x01",
            "out, either. What a disgrace!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70BD")

    Jump("loc_7C04")

    label("loc_70C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_714A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70DD")
    Call(0, 17)
    Jump("loc_7145")

    label("loc_70DD")


    ChrTalk(
        0xFE,
        "Dad's leaving on another business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't need a souvenir, so can he\x01",
            "stay home instead?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7145")

    Jump("loc_7C04")

    label("loc_714A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_71A0")
    OP_93(0xFE, 0x2D, 0x0)

    ChrTalk(
        0xFE,
        "Hey, Dad?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You promised you'd take me to the festival!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C04")

    label("loc_71A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7249")

    ChrTalk(
        0xFE,
        (
            "Mariabell was on the front of a fashion\x01",
            "magazine today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "She's sooo cool!\x01",
            "I bet that one was a special edition!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7322")

    label("loc_7249")


    ChrTalk(
        0xFE,
        (
            "She's the most important lady in all of Crossbell.\x01",
            "Not only is she super smart and a business\x01",
            "manager, but she's also very pretty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mariabell being on the front cover\x01",
            "definitely makes it a special edition!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7322")

    Jump("loc_7C04")

    label("loc_7327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_74C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7438")

    ChrTalk(
        0xFE,
        (
            "I was gossiping about Arc en Ciel\x01",
            "when I went out to shop earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I like Ilya a lot, but Mariabell is still\x01",
            "my favorite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mariabell works for the IBC and is the\x01",
            "most important lady in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's the coolest person ever!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_74BB")

    label("loc_7438")


    ChrTalk(
        0xFE,
        "Mariabell is the IBC CEO's only child.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only is she super smart and a business\x01",
            "manager, but she's also very pretty...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74BB")

    Jump("loc_7C04")

    label("loc_74C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7545")

    ChrTalk(
        0xFE,
        "I have to go to Sunday School.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* What's the point in going if\x01",
            "I'm going to become a model?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_757D")

    label("loc_7545")


    ChrTalk(
        0xFE,
        (
            "I have to go to Sunday School.\x01",
            "*sigh* What a pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_757D")

    Jump("loc_7C04")

    label("loc_7582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_76FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768B")

    ChrTalk(
        0xFE,
        (
            "There are five different fashion magazines\x01",
            "you can read in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We make three of them in Crossbell,\x01",
            "while the other two are from the\x01",
            "Empire and the Republic, respectively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I read through all of them as much\x01",
            "as I can!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_76F7")

    label("loc_768B")


    ChrTalk(
        0xFE,
        "I'm going to become a model when I grow up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It only makes sense for me to read them\x01",
            "all the time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76F7")

    Jump("loc_7C04")

    label("loc_76FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_796E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78D4")

    ChrTalk(
        0xFE,
        "My father is a railway engineer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He went out on a business trip and won't\x01",
            "be back home for two months.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FIt sounds like Wendy's father is a busy man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, get this--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My dad got her a bunch of engineering toys\x01",
            "to play with when she was growing up. Look\x01",
            "at her now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I need to be careful and not fall for his trap.\x02",
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
    SetScenarioFlags(0x0, 3)
    Jump("loc_7966")

    label("loc_78D4")


    ChrTalk(
        0xFE,
        "My father is a railway engineer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He wants me to be one, too, but I won't fall for his\x01",
            "tricks. No engineer training toys for me, thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7966")

    SetScenarioFlags(0x71, 5)
    Jump("loc_7C04")

    label("loc_796E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7989")
    Call(0, 16)
    Jump("loc_7B88")

    label("loc_7989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B09")

    ChrTalk(
        0xFE,
        (
            "I'm going to become a model when\x01",
            "I grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not going to fall for the same trap as\x01",
            "Wendy and become an engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have the nicest body\x01",
            "you've ever seen!\x02",
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
            "#0300FYou've definitely got some spunk in ya,\x01",
            "missy. I'll support your cause.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7B88")

    label("loc_7B09")


    ChrTalk(
        0xFE,
        (
            "I'm going to become a model when\x01",
            "I grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not going to fall for the same trap as\x01",
            "Wendy and become an engineer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B88")

    Jump("loc_7C04")

    label("loc_7B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BAB")
    Call(0, 16)
    SetScenarioFlags(0x0, 3)
    Jump("loc_7C04")

    label("loc_7BAB")


    ChrTalk(
        0xFE,
        (
            "Dad and Wendy don't know how to\x01",
            "clean at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to do it aaall by myself!\x02",
    )

    CloseMessageWindow()

    label("loc_7C04")

    TalkEnd(0xFE)
    Return()

    # Function_15_64D9 end

    def Function_16_7C08(): pass

    label("Function_16_7C08")


    ChrTalk(
        0xC,
        "Cleaning, laundry, washing the dishes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Dad and Wendy don't know how to\x01",
            "clean at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ugh! It's because they're so lazy!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E61")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FOh, hey. Aren't you the little girl I used\x01",
            "to see at Wendy's place back in the day?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "Hmm? Are you friends with my sister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, no. It's nothing. Sorry for bothering you.\x02\x03",
            "#0004F(Figures she doesn't remember me.\x01",
            "It's been three years, after all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309FNice, Lloyd! Didn't know ya liked 'em\x01",
            "that young. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FNo. I. Do. Not. Are you TRYING to\x01",
            "destroy my reputation?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)

    label("loc_7E61")

    Return()

    # Function_16_7C08 end

    def Function_17_7E62(): pass

    label("Function_17_7E62")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xC, 0xF, 0)
    TurnDirection(0xF, 0xC, 0)

    ChrTalk(
        0xF,
        (
            "How about I give you a souvenir before\x01",
            "I go on this business trip, Pansy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Look, I built this model orbal car!\x01",
            "It even moves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Wait, wait. Check this out! If you do this,\x01",
            "you can control it remotely via orbal waves.\x01",
            "Pretty cool, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What is this junk? I don't want it.\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "Gah! I make a revolutionary toy and this\x01",
            "is the response I get? You're killing me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_17_7E62 end

    def Function_18_801C(): pass

    label("Function_18_801C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8035")
    Call(0, 28)
    Return()

    label("loc_8035")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_804F")
    Call(0, 32)
    Return()

    label("loc_804F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8129")

    ChrTalk(
        0xFE,
        "Oh, it's you guys again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you guys on patrol during the festival?\x01",
            "Haha, sucks to be you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, yeah. Are you on your way out again?\x01",
            "Don't cause too much of a ruckus, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8664")

    label("loc_8129")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8234")

    ChrTalk(
        0xFE,
        (
            "Man, I only got to do it for a week.\x01",
            "Lame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*grumble* I wanted to keep taking\x01",
            "care of it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, whatever. Thanks, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'm starting to see you all\x01",
            "in a new light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FIs that honesty I'm hearing?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_82B4")

    label("loc_8234")


    ChrTalk(
        0xFE,
        (
            "Aww, I wish Dad said yes.\x01",
            "I really wanted to keep the cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a shame, but she's been returned\x01",
            "to her owner safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B4")

    Jump("loc_8664")

    label("loc_82B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8389")

    ChrTalk(
        0xFE,
        "I really wanted to keep her, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anri's parents won't let him keep\x01",
            "a pet, and neither will my dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I'm begging you guys to\x01",
            "help us out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8664")

    label("loc_8389")

    TurnDirection(0xE, 0x0, 0)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "Did you guys manage to finish doing\x01",
            "what you were doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Can you find this kitten's owner, then?\x02",
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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8455"),
        (1, "loc_850A"),
        (SWITCH_DEFAULT, "loc_8659"),
    )


    label("loc_8455")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_850A")


    ChrTalk(
        0x101,
        (
            "#0006FI hate to do this to you guys, but we're\x01",
            "in the middle of something right now.\x01",
            "We can come back when we've got some free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Not much we can do about it, then.\x01",
            "We'll take care of her in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Darn, I don't wanna spend my whole\x01",
            "day watching some cat that doesn't\x01",
            "even like me. Make it snappy, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8659")

    label("loc_8659")

    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)

    label("loc_8664")

    TalkEnd(0xFE)
    Return()

    # Function_18_801C end

    def Function_19_8668(): pass

    label("Function_19_8668")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8681")
    Call(0, 28)
    Return()

    label("loc_8681")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_869B")
    Call(0, 32)
    Return()

    label("loc_869B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8789")

    ChrTalk(
        0xFE,
        "Thanks so much, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We promised Ryu's dad that we'd do a\x01",
            "good job cleaning after it, but it's been\x01",
            "really tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We only kept her for a little while, but\x01",
            "I still had a ton of fun!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8801")

    label("loc_8789")


    ChrTalk(
        0xFE,
        (
            "We only kept her for a little while, but\x01",
            "I still had a ton of fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I...also want to have my own cat some day.\x02",
    )

    CloseMessageWindow()

    label("loc_8801")

    Jump("loc_8B74")

    label("loc_8806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88C6")

    ChrTalk(
        0xFE,
        (
            "Ryu's dad is really strict, so we need to be\x01",
            "thorough when we clean up after her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks, you guys. I'll leave the little one\x01",
            "to you, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B74")

    label("loc_88C6")

    TurnDirection(0xD, 0x0, 0)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "Hey guys, could you help us find this\x01",
            "kitten's owner?\x02",
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
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8962"),
        (1, "loc_8A17"),
        (SWITCH_DEFAULT, "loc_8B69"),
    )


    label("loc_8962")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_8A17")


    ChrTalk(
        0x101,
        (
            "#0006FI hate to do this to you guys, but we're\x01",
            "in the middle of something right now.\x01",
            "We can come back when we've got some free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Meh. Not much I can do about it, then.\x01",
            "I'll take care of her in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Darn, I don't wanna spend my whole\x01",
            "day watching some cat that doesn't\x01",
            "even like me. Make it snappy, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8B69")

    label("loc_8B69")

    OP_93(0xD, 0x0, 0x0)
    OP_4C(0xD, 0xFF)

    label("loc_8B74")

    TalkEnd(0xFE)
    Return()

    # Function_19_8668 end

    def Function_20_8B78(): pass

    label("Function_20_8B78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DEE")

    ChrTalk(
        0xFE,
        (
            "Hey, Lloyd. It's been a while.\x01",
            "How's the job treatin' you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FLong time no see, Fay.\x01",
            "You're right, it has been a while.\x02\x03",
            "You only just came back home\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, yeah... Speaking of, I'm about to head\x01",
            "out on another two-month-long business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FSetting up more railway systems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, there's still a ton of countries that are\x01",
            "technologically underdeveloped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not just setting up railway systems.\x01",
            "I also have to educate on how to manage\x01",
            "and safely use them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got a lot of duties I need to take care of\x01",
            "as an engineering adviser.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 2)
    Jump("loc_8E35")

    label("loc_8DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E00")
    Call(0, 17)
    Jump("loc_8E35")

    label("loc_8E00")


    ChrTalk(
        0xFE,
        (
            "Hmm, maybe it was too early to try\x01",
            "for Pansy...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E35")

    Jump("loc_8F45")

    label("loc_8E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8F45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EFC")

    ChrTalk(
        0x101,
        "#0005FOh, it's Wendy's dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FHe looks pretty exhausted...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Zzz... Zzz...\x01",
            "I just got home from my trip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let me sleep in for a while, Pansy...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8F45")

    label("loc_8EFC")


    ChrTalk(
        0xFE,
        (
            "Zzz... How I missed my soft...and comfy\x01",
            "bed back home... So good...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F45")

    TalkEnd(0xFE)
    Return()

    # Function_20_8B78 end

    def Function_21_8F49(): pass

    label("Function_21_8F49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8FF3")

    ChrTalk(
        0xFE,
        "I have another journey I must prepare for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I plan to hike the Mainz Mountains\x01",
            "on foot this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've wanted to go there for a long time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9267")

    label("loc_8FF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9004")
    Call(0, 13)
    Jump("loc_9267")

    label("loc_9004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_905D")

    ChrTalk(
        0xFE,
        "It's time to head out on my next journey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Where shall I go next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9267")

    label("loc_905D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9078")
    Call(0, 22)
    Jump("loc_9101")

    label("loc_9078")


    ChrTalk(
        0xFE,
        (
            "I'm planning on walking around the outskirts\x01",
            "of town with Katerina today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to find her a nice spot\x01",
            "with a great view.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9101")

    Jump("loc_9267")

    label("loc_9106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_916B")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Yep, the parade's good stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Time to head out like it's no big deal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9267")

    label("loc_916B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_917C")
    Call(0, 22)
    Jump("loc_9267")

    label("loc_917C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_918A")
    Jump("loc_9267")

    label("loc_918A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9198")
    Jump("loc_9267")

    label("loc_9198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9267")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_923D")

    ChrTalk(
        0xFE,
        (
            "I came back home for the first time in a\x01",
            "while... The city is too noisy for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ugh, how annoying.\x01",
            "This is why I hate people...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9267")

    label("loc_923D")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "Screw it, I'm going to sleep.\x02",
    )

    CloseMessageWindow()

    label("loc_9267")

    TalkEnd(0xFE)
    Return()

    # Function_21_8F49 end

    def Function_22_926B(): pass

    label("Function_22_926B")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9353")
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x12, 0x5A, 0x0)

    ChrTalk(
        0x12,
        "Whoa. You're a fantastic cook, Chiruru.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Not a lot of inns where I go, so I often\x01",
            "end up camping out for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hurry up and finish eating so we can go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Y-Yeah, okay.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Jump("loc_9598")

    label("loc_9353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9598")
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94CA")

    ChrTalk(
        0x11,
        (
            "Hey, let's go outside and play with\x01",
            "Ryu and Anri!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Sure. What game are we going to play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Check this out. I gathered a bunch of\x01",
            "souvenirs during my travels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "This small bottle has sand from a\x01",
            "desert out in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "Your strange taste in hobbies never\x01",
            "ceases to amaze me, Chiruru.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9598")

    label("loc_94CA")


    ChrTalk(
        0x11,
        (
            "Look at this old plate that came from\x01",
            "a railway car. Someone at Bellguard\x01",
            "Gate gave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "And, these are orbal lamp parts used\x01",
            "in a Liberlian airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Each one is stranger than the last.\x02",
    )

    CloseMessageWindow()

    label("loc_9598")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_926B end

    def Function_23_95A1(): pass

    label("Function_23_95A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_964D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95BF")
    Call(0, 22)
    Jump("loc_9648")

    label("loc_95BF")


    ChrTalk(
        0xFE,
        (
            "I knew it. She's been traveling alone\x01",
            "this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to admit, I'm surprised at how\x01",
            "on-point her seasoning game is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9648")

    Jump("loc_96C0")

    label("loc_964D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_96B4")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "Check out how many cars showed up this year.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't it amazing, Chiruru?\x02",
    )

    CloseMessageWindow()
    Jump("loc_96C0")

    label("loc_96B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_96C0")
    Call(0, 22)

    label("loc_96C0")

    TalkEnd(0xFE)
    Return()

    # Function_23_95A1 end

    def Function_24_96C4(): pass

    label("Function_24_96C4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9763")
    OP_29(0x46, 0x1, 0xB)

    ChrTalk(
        0x101,
        (
            "#0003F(That should cover West Street...)\x02\x03",
            "#0001F(I wonder if the others are having\x01",
            "better luck than me?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        "#3308F(...)\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_9763")

    Return()

    # Function_24_96C4 end

    def Function_25_9764(): pass

    label("Function_25_9764")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_97EB")
    OP_68(56910, 1000, 104970, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 56750, 0, 104300, 0)
    SetChrPos(0x102, 57300, 0, 103300, 0)
    SetChrPos(0x103, 56100, 0, 103300, 0)
    SetChrPos(0x104, 56750, 0, 102300, 0)
    Jump("loc_985D")

    label("loc_97EB")

    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112500, 0)

    label("loc_985D")

    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#1POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1PIs that really you, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FIt is. I'm home, Aunt Leyte.\x02\x03",
            "I'm sorry it took so long for me to visit.\x01",
            "It should've been the first thing I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1POh, Lloyd! You've finally come home!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PI heard that the CPD basically\x01",
            "hired you on the spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PSo, how is it? Have you already started\x01",
            "working, or are you in training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FIt's fine so far. It might be a bit too easygoing\x01",
            "for my tastes, though.\x02\x03",
            "#0000FOur chief kinda just lets us do our own thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PReally? That sounds like an enjoyable\x01",
            "place to work to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PHonestly, I'm just happy to see you looking\x01",
            "healthy and cheery again. I'll have to thank\x01",
            "Aidios next time I'm at the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PLloyd, if you ever need anything\x01",
            "while you're living in the dorms,\x01",
            "you'd better let me know right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1PYou can count on me to charge in and\x01",
            "protect my little angel!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0012FC'mon, Auntie. I'm not a little kid anymore.\x01",
            "And besides, I've been living in dorms since\x01",
            "I was enrolled at the police academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1POh, don't be such a stranger, Lloyd!\x01",
            "You just came home. Don't be afraid\x01",
            "to rely on your Auntie to help you out!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#0006FS-Sorry, Auntie... I'll be sure to drop by\x01",
            "again soon. I'll bring some desserts, and\x01",
            "we can catch up over them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300F(Lloyd's aunt just totally smoked him!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(Despite her seemingly gentle nature, she\x01",
            "appears to be quite the formidable force.)\x02\x03",
            "(On that note, are they even related\x01",
            "by blood?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(Maybe not, but they're as close as any\x01",
            "family as I've ever seen. I'm a bit jealous.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9EE4")
    SetChrPos(0x0, 56750, 0, 105300, 0)
    Jump("loc_9EF5")

    label("loc_9EE4")

    SetChrPos(0x0, 51830, 0, 114500, 0)

    label("loc_9EF5")

    SetScenarioFlags(0x4E, 0)
    EventEnd(0x5)
    Return()

    # Function_25_9764 end

    def Function_26_9EFB(): pass

    label("Function_26_9EFB")

    EventBegin(0x0)
    Fade(500)
    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112350, 0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0005FOh, Auntie. I finally met up with\x01",
            "Cecile yesterday.\x02\x03",
            "#0000FShe hasn't changed one bit.\x01",
            "I think I actually got a little bit self-conscious\x01",
            "meeting up with her after all this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, really? I'm glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, how'd it go? Did she find herself\x01",
            "a nice man to settle down with?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWh-What? How am I supposed to know?\x01",
            "(And besides, I wouldn't really feel\x01",
            "comfortable with it...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh* That child of mine needs to start\x01",
            "thinking about her future more carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Perhaps I'll look into finding her\x01",
            "a prospective husband.\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x104, 0x0, 0x0, 0xFA, 0x3E8, 0x0)

    ChrTalk(
        0x104,
        (
            "#0309F(Did she say a prospective husband?\x01",
            "Hell yes! It's time to announce my\x01",
            "candidacy, baby!)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        "#0111F(Don't get any funny ideas, Randy.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FHaha...hahaha...\x01",
            "(There's NO freaking way that's happening.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FExcuse me, Lloyd. Is it my imagination,\x01",
            "or has your voice gotten hoarse?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 51830, 0, 114500, 0)
    SetScenarioFlags(0x70, 5)
    EventEnd(0x5)
    Return()

    # Function_26_9EFB end

    def Function_27_A31B(): pass

    label("Function_27_A31B")

    EventBegin(0x0)
    Fade(500)
    OP_68(-58260, 1000, 57850, 0)
    MoveCamera(46, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, -57760, 0, 57480, 0)
    SetChrPos(0x102, -58760, 0, 57230, 0)
    SetChrPos(0x103, -57760, 0, 55980, 0)
    SetChrPos(0x104, -58760, 0, 55730, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_END)), "loc_A51D")

    ChrTalk(
        0x101,
        (
            "#11P#0000F(It doesn't seem like Fay is in right\x01",
            "now... Maybe I'll try asking Pansy.)\x02\x03",
            "Hey there, Pansy. Is your dad busy\x01",
            "working today?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#5PHuh? Aren't you one of Wendy's\x01",
            "friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PDid you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FYeah, actually. I wanted to ask your\x01",
            "dad a quick question if he's around,\x01",
            "but it doesn't look like he is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6CA")

    label("loc_A51D")


    ChrTalk(
        0x101,
        (
            "#11P#0000F(It doesn't seem like Fay is in right now...\x01",
            "Guess I'll just ask this girl, then.)\x02\x03",
            "#0005FExcuse me. Aren't you Fay's youngest\x01",
            "daughter?\x02\x03",
            "I'm surprised. You and Wendy don't look\x01",
            "alike at all...\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        "#5PHuh? Oh, you're her friend, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0002FOh, haha. You still remember me?\x02\x03",
            "Actually, I wanted to ask your dad\x01",
            "a quick question if he's around.\x01",
            "Is he at work or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6CA")


    ChrTalk(
        0xC,
        "#5POh, Dad? He's off on a business trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHe won't be back for another two months.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 5)), scpexpr(EXPR_END)), "loc_A75E")

    ChrTalk(
        0x101,
        "#11P#0003FOh, that's right. Darn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A792")

    label("loc_A75E")


    ChrTalk(
        0x101,
        "#11P#0003FSounds like we're out of luck, then.\x02",
    )

    CloseMessageWindow()

    label("loc_A792")


    ChrTalk(
        0x104,
        (
            "#12P#0306FYeah. I'm not about to start goin' through\x01",
            "his stuff without permission.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#5PAre you looking for something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FYes. We're here to retrieve a book\x01",
            "your father borrowed from the library.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FDo you recall any mentions of it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PIs it the one I'm reading right now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FMind if I take a look at it?\x01",
            "I can check to see if it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PSure.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pansy retrieved a book and held it out for Lloyd to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#11P#0000FIt's got a stamp from the library.\x01",
            "That's probably the one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PReally, Dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI can't believe you'd leave on a forever-\x01",
            "long trip without returning your book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PSorry about that, mister. Do you\x01",
            "mind taking the book in for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FAre you sure? Didn't you say you\x01",
            "were in the middle of reading it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FI believe you can apply for an extension\x01",
            "at the library's front desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PNo, it's okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI was kinda just looking through it.\x01",
            "It's actually pretty boring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PI mean, did you even read the title?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FUh, let's see... 'Train Fanatic Recs.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FThe name alone is enough to tell you\x01",
            "that it's only for weirdo train nuts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI bet Dad borrowed it to try and get me\x01",
            "interested in becoming a railway engineer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PI'm not going to fall for his tricks that easily.\x01",
            "No, siree! So, yeah. Feel free to return it for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FS-Sure thing. Thanks for helping us out.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D5, 1)
    OP_29(0x5, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADCB")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_ADCB")

    SetChrPos(0x0, -58260, 0, 57480, 0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    EventEnd(0x5)
    Return()

    # Function_27_A31B end

    def Function_28_ADED(): pass

    label("Function_28_ADED")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, -55690, 0, 108350, 270)
    SetChrPos(0x102, -54350, 0, 108180, 270)
    SetChrPos(0x103, -55690, 0, 109530, 270)
    SetChrPos(0x104, -54390, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 0)
    SetChrPos(0xE, -57930, 0, 110500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        "#12PHey, it's the Special Support Section!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PIt's been a while since we last saw you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FAbout a week, I think.\x02\x03",
            "#0005FSo, what's up? Actually, what's\x01",
            "the deal with the kitten?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FIt looks fairly young. Maybe about\x01",
            "six months old, if I were to guess.\x02\x03",
            "#0100FAre you her owners?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PNo, uh, we found her roaming around\x01",
            "West Street all alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PWe think she might be lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PShe was pretty weak, but we made\x01",
            "sure to give her a ton of food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAnd, look! She's as good as new!\x01",
            "Aren't we amazing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0xE,
        "#6PYeah, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 500)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#6PWait a minute. Why don't we just ask\x01",
            "them to help us out, Ryu?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        "#12PHuh? You're talkin' about that idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PYou know we can't do it ourselves...\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        "#0305F#11PWhat's this idea you're talkin' about?\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)

    ChrTalk(
        0xE,
        (
            "#6PActually, there's a request we'd like\x01",
            "to make...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PMind hearing us out?\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Special Support Section listened to Ryu\x01",
            "and Anri's story about finding the kitten.\x02",
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
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#0205F#11PTo summarize, you would like for us\x01",
            "to find her true owner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PPlease do. She was wearing a collar\x01",
            "when we first found her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PWe took it off because it looked like\x01",
            "she was uncomfortable with it on.\x01",
            "But it should mean she has an owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PYeah, she doesn't really seem to like us\x01",
            "all that much, either. Probably 'cause\x01",
            "she has no idea who we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FI'd imagine her real owners are worried\x01",
            "sick by now.\x02\x03",
            "#0001FWe should try finding them, for the\x01",
            "kitten's sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FDo you have any clues as to who\x01",
            "the owner might be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PYeeeah, about that... Anri here\x01",
            "was thinkin' that it might be a kid.\x02",
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
        "#6PThe collar looked handmade.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PDoesn't that seem like something\x01",
            "a kid like us would do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F#11PYeah, I can see that. I guess we should\x01",
            "narrow the search to households with\x01",
            "kids, then.\x02\x03",
            "Wow, that sure narrowed down our leads.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#0300F#11PEither way, it's your call, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0003FWell...\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x4, 0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept\x01",      # 0
            "Refuse\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B7E8"),
        (1, "loc_B7F2"),
        (SWITCH_DEFAULT, "loc_B955"),
    )


    label("loc_B7E8")

    OP_29(0x8, 0x1, 0x2)
    Call(0, 29)
    Return()

    label("loc_B7F2")


    ChrTalk(
        0x101,
        (
            "#11P#0006FI hate to do this to you guys, but we're in\x01",
            "the middle of something right now. We can\x01",
            "come back when we've got some free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PMeh. Not much I can do about it, then.\x01",
            "I'll take care of her in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PDarn, I don't wanna spend my whole\x01",
            "day watching some cat that doesn't\x01",
            "even like me. Make it snappy, 'kay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x8, 0x1, 0x0)
    Jump("loc_B955")

    label("loc_B955")

    Fade(500)
    SetChrPos(0x0, -55530, 0, 109140, 270)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0x13, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_ADED end

    def Function_29_B988(): pass

    label("Function_29_B988")

    SetChrFlags(0xD, 0x40)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x101,
        (
            "#11P#0000FWe're probably going to end up being late\x01",
            "going to St. Ursula, but let's try and look\x01",
            "for the kitten's owner for a bit.\x02\x03",
            "First of all, we should probably take the\x01",
            "kitten with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#0200FIs that wise? She is quite feeble at the\x01",
            "moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FShe would hardly be able to keep up\x01",
            "with us, no?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB44():

        label("loc_BB44")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BB44")

    QueueWorkItem2(0xE, 1, lambda_BB44)

    def lambda_BB56():

        label("loc_BB56")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BB56")

    QueueWorkItem2(0x103, 1, lambda_BB56)

    def lambda_BB68():

        label("loc_BB68")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BB68")

    QueueWorkItem2(0x104, 1, lambda_BB68)

    def lambda_BB7A():

        label("loc_BB7A")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_BB7A")

    QueueWorkItem2(0x102, 1, lambda_BB7A)
    BeginChrThread(0x101, 1, 0, 30)
    OP_68(-55760, 500, 110100, 3000)

    ChrTalk(
        0x101,
        (
            "#11P#0004FI have just the solution for that.\x02\x03",
            "#0000FMind letting me hold her, Ryu?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6PO-Oh, sure...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    BeginChrThread(0xD, 1, 0, 31)
    Sleep(300)

    def lambda_BC1E():
        OP_95(0xFE, -58000, 0, 107500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC1E)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        "#11P#0009FOkay. C'mere, girl...\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x13, 0x101, 300)
    Sleep(800)
    OP_95(0x13, -58010, 700, 108520, 300, 0x0)
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(1000)
    Sound(804, 0, 100, 0)
    Fade(500)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the frail kitten in his arms and\x01",
            "gently placed her inside his jacket.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x101,
        "#11P#0000FThere we go. All tucked in.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FThis should work. Or, we should be able\x01",
            "to walk around safely, at the very least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309F#11POh, what's this? Who knew you had a\x01",
            "way with animals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F#11PI am surprised you are not a veterinarian.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FWell done, Lloyd.\x02\x03",
            "So let me get this straight. You think\x01",
            "it'd be best to assume that the owner\x01",
            "is a child, right, Anri?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 500)
    TurnDirection(0xD, 0x102, 500)

    ChrTalk(
        0xE,
        "#6PYes, probably...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PAnd since we found her over near the\x01",
            "Residential District, her home might be\x01",
            "somewhere over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FEither way, our best bet is focusing on\x01",
            "residential communities.\x02\x03",
            "#0000FReady, everyone?\x02",
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
            "[Search for the Kitten's Owner]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x0, 0x1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -55530, 0, 109140, 180)
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xD, 0x40)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_B988 end

    def Function_30_C087(): pass

    label("Function_30_C087")

    OP_95(0x101, -56270, 0, 107500, 1000, 0x0)
    OP_95(0x101, -57120, 0, 107500, 1000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_30_C087 end

    def Function_31_C0B7(): pass

    label("Function_31_C0B7")

    OP_95(0xD, -57290, 0, 106710, 1000, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Return()

    # Function_31_C0B7 end

    def Function_32_C0D3(): pass

    label("Function_32_C0D3")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(-54300, 700, 110230, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -54200, 0, 108980, 0)
    SetChrPos(0x102, -55340, 0, 107320, 0)
    SetChrPos(0x103, -55340, 0, 108980, 0)
    SetChrPos(0x104, -54200, 0, 107320, 0)
    SetChrPos(0xD, -53900, 0, 110740, 180)
    SetChrPos(0xE, -55030, 0, 110700, 180)
    OP_0D()

    ChrTalk(
        0xD,
        "#5PHey, guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PHow'd it go? You manage to find\x01",
            "the kitten's owner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOf course.\x02\x03",
            "We hit a few snags along the way,\x01",
            "but she's safe and sound at her\x01",
            "owner's house now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5PG-Got'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PWhew, thank goodness. I was going\x01",
            "to be so worried if we were the only\x01",
            "ones taking care of her.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PRyu, you okay? Do you miss her\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0xE, 500)

    ChrTalk(
        0xD,
        "#11PG-Get real!\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#11PC'mon, Anri! Let's finish cleaning\x01",
            "so we can go out and play!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PYeah, all right.\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PEveryone, thanks for your help!\x01",
            "Have a wonderful day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FWhat a good kid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FIf you need any more help, make\x01",
            "sure to call us, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -54960, 0, 107860, 0)
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x70, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_C0D3 end

    SaveToFile()

Try(main)
