from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c020c.bin",                # FileName
        "c020c",                    # MapName
        "c020c",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 2, 0, 3],
    )

    BuildStringList((
        "c020c",                  # 0
        "Ponce",                  # 1
        "Burik",                  # 2
        "Bennet",                 # 3
        "Elsa",                   # 4
        "Momo",                   # 5
        "Old Man Levick",         # 6
        "Olga",                   # 7
        "Katerina",               # 8
        "Chiruru",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Old Man Rays",           # 15
        "Colin",                  # 16
        "Harold",                 # 17
        "Sophia",                 # 18
        "Sully",                  # 19
        "SE制御",                 # 20
        "Central Square",         # 21
        "West Street",            # 22
        "Administrative District",# 23
        "Residential District",   # 24
        "Entertainment District", # 25
        "East Street",            # 26
        "Downtown District",      # 27
        "Harbor District",        # 28
        "IBC",                    # 29
        "Station Street",         # 30
        "Back Alley",             # 31
        "Ursula Road",            # 32
        "East Crossbell Highway", # 33
        "West Crossbell Highway", # 34
        "Mainz Mountain Path",    # 35
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20402.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch21600.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch21800.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch21602.itc",                   # 0C
        "chr/ch21100.itc",                   # 0D
        "chr/ch21602.itc",                   # 0E
        "chr/ch24400.itc",                   # 0F
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

    DeclNpc(-25120,  0,       4139,    180,  261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4869,    0,       629,     225,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4820,    3000,    17420,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6309,    3000,    17329,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6579,   0,       7170,    90,   261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5219,   0,       7170,    270,  261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-15020,  -2599,   -8350,   180,  405,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-13739,  -2599,   -8350,   180,  405,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3349,    0,       -9760,   270,  261,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(2089,    0,       -9760,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1629,    3000,    13079,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8039,    -150,    6960,    180,  469,  0x0, 0,   12,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(6980,    -300,    7619,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5500,    -200,    8000,    270,  469,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  4,  0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  5,  0x0000)
    DeclActor(4050,    0,       -190,    1000,    4870,    1500,    630,     0x007E, 0,  8,  0x0000)
    DeclActor(-31040,  -1000,   9420,    1500,    -29950,  1000,    8850,    0x007C, 0,  30, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central Square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "West Street")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential District")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Station Street")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_7C8",          # 01, 1
        "Function_2_7F3",          # 02, 2
        "Function_3_A97",          # 03, 3
        "Function_4_C3E",          # 04, 4
        "Function_5_DE4",          # 05, 5
        "Function_6_F62",          # 06, 6
        "Function_7_135A",         # 07, 7
        "Function_8_1838",         # 08, 8
        "Function_9_183C",         # 09, 9
        "Function_10_1E59",        # 0A, 10
        "Function_11_1FE4",        # 0B, 11
        "Function_12_204B",        # 0C, 12
        "Function_13_2350",        # 0D, 13
        "Function_14_2545",        # 0E, 14
        "Function_15_288F",        # 0F, 15
        "Function_16_28FC",        # 10, 16
        "Function_17_2995",        # 11, 17
        "Function_18_2C20",        # 12, 18
        "Function_19_2E3C",        # 13, 19
        "Function_20_31FA",        # 14, 20
        "Function_21_338D",        # 15, 21
        "Function_22_34B7",        # 16, 22
        "Function_23_36F5",        # 17, 23
        "Function_24_37BD",        # 18, 24
        "Function_25_4A7A",        # 19, 25
        "Function_26_4AE2",        # 1A, 26
        "Function_27_4B4A",        # 1B, 27
        "Function_28_4E8D",        # 1C, 28
        "Function_29_4FBF",        # 1D, 29
        "Function_30_55D5",        # 1E, 30
        "Function_31_5679",        # 1F, 31
        "Function_32_6121",        # 20, 32
        "Function_33_615E",        # 21, 33
        "Function_34_617A",        # 22, 34
        "Function_35_6196",        # 23, 35
        "Function_36_61B2",        # 24, 36
        "Function_37_61CE",        # 25, 37
        "Function_38_6415",        # 26, 38
        "Function_39_64C4",        # 27, 39
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_750"),
        (1, "loc_75C"),
        (2, "loc_768"),
        (3, "loc_774"),
        (4, "loc_780"),
        (5, "loc_78C"),
        (6, "loc_798"),
        (SWITCH_DEFAULT, "loc_7A4"),
    )


    label("loc_750")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_75C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_768")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_774")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_780")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_78C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_798")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7C7")

    Return()

    # Function_0_710 end

    def Function_1_7C8(): pass

    label("Function_1_7C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F2")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_1_7C8")

    label("loc_7F2")

    Return()

    # Function_1_7C8 end

    def Function_2_7F3(): pass

    label("Function_2_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BE")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_8B0")

    label("loc_891")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_8B0")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95F")

    label("loc_8BE")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_937")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_956")

    label("loc_937")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_956")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_956")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_98C")
    SetChrPos(0x13, 21980, 0, -10790, 135)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_A4E")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D3")
    SetChrPos(0x13, -2410, 0, -1730, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9CE")
    LoadEffect(0x0, "event\\eva02_00.eff")

    label("loc_9CE")

    Jump("loc_A4E")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A3B")
    ClearChrFlags(0xB, 0x80)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrPos(0x13, -6580, 0, 5810, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A36")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_A36")

    Jump("loc_A4E")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A4E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5F")
    Event(0, 24)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A73")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_A96")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_A87")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 28)
    Jump("loc_A96")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_A96")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 31)

    label("loc_A96")

    Return()

    # Function_2_7F3 end

    def Function_3_A97(): pass

    label("Function_3_A97")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x8, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACD")
    OP_1B(0x1, 0x0, 0x25)
    OP_1B(0x8, 0x0, 0x26)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE0")
    OP_1B(0x1, 0x0, 0x25)

    label("loc_AE0")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFD")
    OP_66(0x3, 0x1)

    label("loc_AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    OP_65(0x1, 0x1)
    OP_66(0x3, 0x1)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")
    OP_70(0x7, 0x0)
    Jump("loc_B35")

    label("loc_B31")

    OP_70(0x7, 0x1E)

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    OP_70(0x8, 0x0)
    Jump("loc_B4C")

    label("loc_B48")

    OP_70(0x8, 0x1E)

    label("loc_B4C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -25000, -4000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 24000, -4000, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 4000, -1000, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_A97 end

    def Function_4_C3E(): pass

    label("Function_4_C3E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D72")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x80.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_DD2")

    label("loc_D72")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I tried to go join the festivities, too, but...\x01",
            "I kind of got lost in the B Sector.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_DD2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C3E end

    def Function_5_DE4(): pass

    label("Function_5_DE4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECE")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_E64")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_EC9")

    label("loc_E64")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EC9")

    Jump("loc_F3D")

    label("loc_ECE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please close my lid. Can't you see how much\x01",
            "confetti I'm collecting?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F3D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F61")
    Call(0, 29)

    label("loc_F61")

    Return()

    # Function_5_DE4 end

    def Function_6_F62(): pass

    label("Function_6_F62")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1014")

    ChrTalk(
        0xFE,
        (
            "Once nighttime hits, the festival's\x01",
            "closing fireworks show is going to start!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no way I'm missing that!\x01",
            "I gotta hurry and secure a nice spot...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1356")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(
        0xFE,
        "Happy anniversary!\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ponce set up the orbal camera.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    ChrTalk(
        0xFE,
        (
            "How're you guys doing?\x01",
            "You all having fun?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_11A7")

    label("loc_111E")


    ChrTalk(
        0xFE,
        (
            "Like usual, it's nothing less than the very\x01",
            "best, pristine photos from me today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Long live Crossbell State!\x01",
            "Happy anniversary!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A7")

    Jump("loc_1356")

    label("loc_11AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah, the smiles from all the\x01",
            "tourists and locals are fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm itching to develop this photo-quartz already...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1356")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12CC")

    ChrTalk(
        0xFE,
        "Oh, man, they've got airships flying around, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, let's take one more photo\x01",
            "to commemorate this special occasion.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1356")

    label("loc_12CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1356")

    ChrTalk(
        0xFE,
        (
            "Just what I've come to expect from Crossbell's\x01",
            "delightful Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "There's no shortage of photos to take!\x02",
    )

    CloseMessageWindow()

    label("loc_1356")

    TalkEnd(0xFE)
    Return()

    # Function_6_F62 end

    def Function_7_135A(): pass

    label("Function_7_135A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13EE")
    Jump("loc_1438")

    label("loc_13EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_140E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1438")

    label("loc_140E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1438")

    label("loc_142E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1438")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1506")

    ChrTalk(
        0xFE,
        (
            "The closing ceremony is going to be held\x01",
            "in the afternoon at City Hall today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll go check it out. Mayor\x01",
            "MacDowell will be in attendance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_1506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_15C0")

    ChrTalk(
        0xFE,
        (
            "It truly feels like a festival when I'm\x01",
            "able to converse with foreigners\x01",
            "in such a casual manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd love it if you all came to visit\x01",
            "Crossbell again next year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_15C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1615")
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0xFE,
        "Haha, don't mind me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Come, now, let's enjoy the present!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_1615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16F3")

    ChrTalk(
        0xFE,
        (
            "Between the buses and the airships packed\x01",
            "with tourists, they've made this festival\x01",
            "as flashy as can be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll take a nice stroll around town.\x01",
            "There's no way I'll be able to read in peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1830")

    label("loc_16F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1830")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BE")

    ChrTalk(
        0xFE,
        (
            "I went to hear the mayor's opening\x01",
            "speech yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell is already pushing\x01",
            "past 70, isn't he...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He doesn't even seem fazed by\x01",
            "his recent accident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1830")

    label("loc_17BE")


    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell is as every bit extraordinary\x01",
            "as I thought he'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder when he plans on retiring.\x02",
    )

    CloseMessageWindow()

    label("loc_1830")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_135A end

    def Function_8_1838(): pass

    label("Function_8_1838")

    Call(0, 9)
    Return()

    # Function_8_1838 end

    def Function_9_183C(): pass

    label("Function_9_183C")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1849")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E55")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_189A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BA")
    OP_AF(0xCF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E50")

    label("loc_18BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CE")
    Jump("loc_1E50")

    label("loc_18CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E50")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1979")

    ChrTalk(
        0xA,
        (
            "Haha...\x01",
            "Go ahead and enjoy yourself, Oscar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "In the meantime, I'll be experimenting\x01",
            "with ideas for my next bread creation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_1979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_19EE")

    ChrTalk(
        0xA,
        "This crowd has been fantastic for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone will flock like gulls to my\x01",
            "baked delicacies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B74")

    ChrTalk(
        0x101,
        "#0001F(Hmm, she might know something about Colin...)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Huh...?\x01",
            "I think I've seen this kid around before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Definitely hasn't been recently, though.\x01",
            "He'd stand out if he were by himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FI see... Thank you for your cooperation.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 23)
    Jump("loc_1BFF")

    label("loc_1B74")


    ChrTalk(
        0xA,
        (
            "All I know is, he didn't come by to\x01",
            "sample any of our bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If he came, I'd have remembered\x01",
            "recommending my tasty bread to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFF")

    Jump("loc_1E50")

    label("loc_1C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C7A")

    ChrTalk(
        0xA,
        "This crowd is a gift from the Goddess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone will flock like gulls to my\x01",
            "baked delicacies!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(
        0xA,
        "Welcooome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Come and buy my treats\x01",
            "to your heart's content!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D98")

    ChrTalk(
        0xA,
        (
            "Haha... I've been tasked with creating this\x01",
            "month's masterpiece of a bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It'll be a huge success thanks to the\x01",
            "massive festival crowd! Oscar doesn't\x01",
            "stand a chance against me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E50")

    label("loc_1D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E02")

    ChrTalk(
        0xA,
        "Oh, please. Try a sample.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Please buy a loaf if you enjoyed it, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E50")

    label("loc_1E02")


    ChrTalk(
        0xA,
        "I baked all of the bread today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "C-Come and buy some, if you'd like.\x02",
    )

    CloseMessageWindow()

    label("loc_1E50")

    Jump("loc_1849")

    label("loc_1E55")

    TalkEnd(0xA)
    Return()

    # Function_9_183C end

    def Function_10_1E59(): pass

    label("Function_10_1E59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ECB")

    ChrTalk(
        0xFE,
        "Welcome to Tallys' General Store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thank you for your continued patronage!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F50")

    label("loc_1ECB")


    ChrTalk(
        0xFE,
        (
            "Momo's already retreated from all\x01",
            "the bustle outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, maybe this huge crowd is\x01",
            "off-putting for a shy girl like her...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F50")

    Jump("loc_1FE0")

    label("loc_1F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FE0")

    ChrTalk(
        0xFE,
        "Welcooome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That husband of mine...\x01",
            "Leaving all the work to me, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No matter. I've got to keep working hard.\x02",
    )

    CloseMessageWindow()

    label("loc_1FE0")

    TalkEnd(0xFE)
    Return()

    # Function_10_1E59 end

    def Function_11_1FE4(): pass

    label("Function_11_1FE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2035")

    ChrTalk(
        0xFE,
        (
            "The festival... T-Too many customers...\x01",
            "I hate this...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2047")

    label("loc_2035")


    ChrTalk(
        0xFE,
        "W-Welcome...\x02",
    )

    CloseMessageWindow()

    label("loc_2047")

    TalkEnd(0xFE)
    Return()

    # Function_11_1FE4 end

    def Function_12_204B(): pass

    label("Function_12_204B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20F8")

    ChrTalk(
        0xFE,
        (
            "Hmm, maybe I should try checking out\x01",
            "Central Square's attractions today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet they've got some furnishings that\x01",
            "would match my home's aesthetic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_217F")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "I received an invitation to\x01",
            "a dinner party tonight, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You didn't just forget about it, did you?\x02",
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2207")

    ChrTalk(
        0xFE,
        "Geez, where has the time gone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's annual, but whenever the festival\x01",
            "ends, it leaves a small void in my heart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_2207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2294")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "The parade should be easier to see\x01",
            "from a high vantage point, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You aren't the most sensible person, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_2294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22A5")
    Call(0, 13)
    Jump("loc_234C")

    label("loc_22A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_234C")

    ChrTalk(
        0xFE,
        (
            "This festival has filled Crossbell with joy.\x01",
            "All of Crossbell should savor the experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's try to put aside social standing during this time.\x02",
    )

    CloseMessageWindow()

    label("loc_234C")

    TalkEnd(0xFE)
    Return()

    # Function_12_204B end

    def Function_13_2350(): pass

    label("Function_13_2350")

    OP_4B(0xD, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xD, 0x13, 0)
    TurnDirection(0x13, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247A")

    ChrTalk(
        0x13,
        "Hey, aren't you a member of the diet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Oops, since you retired, I suppose\x01",
            "you're a former member now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm almost positive you were an executive\x01",
            "of one of the subcommittees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hoho, been in good health lately?\x01",
            "That's most important, I say.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_253C")

    label("loc_247A")


    ChrTalk(
        0xD,
        (
            "Hoho, I don't involve myself with\x01",
            "politics anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "More importantly, won't you come visit\x01",
            "my home? Let us share a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Gladly. If you don't mind me\x01",
            "imposing on you, of course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253C")

    OP_4C(0xD, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_13_2350 end

    def Function_14_2545(): pass

    label("Function_14_2545")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25E3")
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hey, weren't you going to go see\x01",
            "Arc en Ciel today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better hustle! Make a detour, and you\x01",
            "might miss the whole performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_25E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_267E")
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "Oh, who cares about that?\x01",
            "Just have a few bites, then leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And don't forget you need to\x01",
            "go buy groceries on the way back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2721")

    ChrTalk(
        0xFE,
        (
            "The parade always does a great job\x01",
            "of making me feel revitalized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Watching everybody's cheery faces manages\x01",
            "to wipe away all of my stress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_2721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_27C5")
    OP_93(0xFE, 0x10E, 0x0)

    ChrTalk(
        0xFE,
        (
            "Oh, looks like the parade will pass through\x01",
            "here during its route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is, without a doubt, the best\x01",
            "spot to experience the parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_27C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_283E")

    ChrTalk(
        0xFE,
        "My husband used to be a member of the diet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's accumulated lots of connections over the years.\x02",
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_283E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_288B")

    ChrTalk(
        0xFE,
        (
            "I hope we'll be able to enjoy the festival\x01",
            "together this year.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_288B")

    TalkEnd(0xFE)
    Return()

    # Function_14_2545 end

    def Function_15_288F(): pass

    label("Function_15_288F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Look, look! An airship!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoa... Look at how they decorated it\x01",
            "for the Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_288F end

    def Function_16_28FC(): pass

    label("Function_16_28FC")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        "Ugh, I wanted to sleep in today...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xFE, 500)

    ChrTalk(
        0xF,
        "Whaaat?! We can't waste this day!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "C'mon, Chiruru, let's explore the city!\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x0)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_28FC end

    def Function_17_2995(): pass

    label("Function_17_2995")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A2A")

    ChrTalk(
        0xFE,
        (
            "*huff* *huff*\x01",
            "It's already the last day of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This city is just TOO big!\x01",
            "I haven't even toured half of it yet!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2AB7")

    ChrTalk(
        0xFE,
        (
            "*munch* *munch*\x01",
            "Go check out that baker over there.\x01",
            "She's offering free samples.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm considering trying some more...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BA3")

    ChrTalk(
        0xFE,
        (
            "Did you guys hear already? Some people from\x01",
            "the village are running a food stall in front of the\x01",
            "fountain at the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I give it my recommendation! Five stars!\x01",
            "That omelet rice was to die for!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C1C")

    ChrTalk(
        0xFE,
        (
            "A three-hour bumpy train ride\x01",
            "from the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but here we are! We finally made it\x01",
            "to Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1C")

    TalkEnd(0xFE)
    Return()

    # Function_17_2995 end

    def Function_18_2C20(): pass

    label("Function_18_2C20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CD8")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "C'mon, let's check out the Entertainment District!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You wouldn't believe the trouble I went\x01",
            "through to sneak away from home...\x01",
            "Now's the time for fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E38")

    label("loc_2CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D27")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        "Hey, you cheater!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't dodge the conversation!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E38")

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(
        0xFE,
        (
            "The sweets shop in Central Square\x01",
            "had the most delightful candy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They almost melt in your mouth!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E38")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E38")

    ChrTalk(
        0xFE,
        (
            "My mom really didn't want me going\x01",
            "to the festival...so I snuck out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In any case, I'm here to party it up\x01",
            "and have a hell of a time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E38")

    TalkEnd(0xFE)
    Return()

    # Function_18_2C20 end

    def Function_19_2E3C(): pass

    label("Function_19_2E3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F06")

    ChrTalk(
        0xFE,
        (
            "If I recall correctly, that building used to\x01",
            "be the Crossbell News Service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't they move to the Harbor District,\x01",
            "though? What's it being used for\x01",
            "these days?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2F8C")

    label("loc_2F06")


    ChrTalk(
        0xFE,
        (
            "You never know what you'll discover\x01",
            "when you take a stroll around the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's that building being used\x01",
            "for these days?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F8C")

    Jump("loc_31F6")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FE6")

    ChrTalk(
        0xFE,
        (
            "Wow, they really pulled out all the stops\x01",
            "for this year's parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F6")

    label("loc_2FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3094")

    ChrTalk(
        0xFE,
        (
            "Here's to hoping that I chose a good spot\x01",
            "to view the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the Anniversary Festival's pride and joy,\x01",
            "so I definitely can't afford to miss it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F6")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30A5")
    Call(0, 13)
    Jump("loc_31F6")

    label("loc_30A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3167")

    ChrTalk(
        0xFE,
        (
            "Casually strolling around the festival\x01",
            "is just as fun I thought it'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it's not every day you get to see\x01",
            "the boisterous crowds of the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_31F6")

    label("loc_3167")


    ChrTalk(
        0xFE,
        (
            "You can't turn a single street corner\x01",
            "without finding a food stall!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This city is on an entirely different\x01",
            "level during the festival.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F6")

    TalkEnd(0xFE)
    Return()

    # Function_19_2E3C end

    def Function_20_31FA(): pass

    label("Function_20_31FA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_328E")
    Jump("loc_32D8")

    label("loc_328E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32AE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32D8")

    label("loc_32AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32CE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32D8")

    label("loc_32CE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32D8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "The locals seem to love the influx of\x01",
            "tourists visiting the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I'd be at home living in a\x01",
            "city like this.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_31FA end

    def Function_21_338D(): pass

    label("Function_21_338D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3422")

    ChrTalk(
        0xFE,
        "Wow, that parade lived up to its hype!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Boy, am I glad I came. Easily one of the\x01",
            "best decisions I've ever made in my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34B3")

    label("loc_3422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_34B3")

    ChrTalk(
        0xFE,
        (
            "You can't talk about the Anniversary Festival\x01",
            "without talking about the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came from a land far, far away\x01",
            "to watch it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B3")

    TalkEnd(0xFE)
    Return()

    # Function_21_338D end

    def Function_22_34B7(): pass

    label("Function_22_34B7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_354B")
    Jump("loc_3595")

    label("loc_354B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_356B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3595")

    label("loc_356B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_358B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3595")

    label("loc_358B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3595")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3606")

    ChrTalk(
        0x16,
        (
            "I think I'll lounge around on\x01",
            "West Street today.\x01",
            "Hahaha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36ED")

    label("loc_3606")


    ChrTalk(
        0x16,
        (
            "I normally do all of my relaxing in the\x01",
            "Residential District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Thing is, there was an exhausted-looking\x01",
            "man sitting on my favorite bench.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Hoho! Poor chap looked so glum that\x01",
            "I surrendered and left the seat to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_36ED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_34B7 end

    def Function_23_36F5(): pass

    label("Function_23_36F5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37BC")
    OP_29(0x46, 0x1, 0xB)

    ChrTalk(
        0x101,
        (
            "#0000F(Okay, I should have covered all of\x01",
            "West Street with this...)\x02\x03",
            "(I wonder if the other guys are having any\x01",
            "luck with their investigations.)\x02",
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

    label("loc_37BC")

    Return()

    # Function_23_36F5 end

    def Function_24_37BD(): pass

    label("Function_24_37BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(13500, 1000, -8500, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 12700, 0, -8500, 90)
    SetChrPos(0x160, 14300, 0, -8500, 270)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400435V#0001FYes, Lloyd speaking.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_391B():
        OP_9A(0xFE, 0x101, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_391B)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400436V\x07\x05",
            "It's Elie.\x01",
            "I heard something unsettling that\x01",
            "I thought I should report to you...\x02\x03",
            "#3400437VTio's with me now, by the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400438V\x07\x05",
            "Hello, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400439V\x07\x00",
            "#0000FOh, you guys met up?\x02\x03",
            "#3400440VOkay, Elie, what'd you want to report?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400441V\x07\x05",
            "It's about Colin. Apparently, he was sighted\x01",
            "standing at the pier, gazing at all the boats.\x02\x03",
            "#3400442VWitnesses don't know where\x01",
            "he went after that, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400443V\x07\x05",
            "I asked Zeit to search for his\x01",
            "scent in the surrounding area.\x02\x03",
            "#3400444VBut... Upon climbing the stairs\x01",
            "exiting the pier, Colin's scent\x01",
            "suddenly vanished.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400445V\x07\x00",
            "#0005FHis scent disappeared?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400446V\x07\x05",
            "Yes, at the southeastern end of the Harbor District...\x02\x03",
            "#3400447VWhat could this mean?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400448V\x07\x00",
            "#0008FCould it be...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x160, 1)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[He entered an automobile]\x01",      # 0
            "[He fell into the river]\x01",        # 1
            "[Someone carried him away]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D64"),
        (1, "loc_3F2A"),
        (2, "loc_42C3"),
        (SWITCH_DEFAULT, "loc_45C3"),
    )


    label("loc_3D64")

    OP_2C(0x46, 0x2)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400449V#0003FAn airtight space where a person's\x01",
            "scent wouldn't easily escape.\x02\x03",
            "#3400450V#0001FIt's entirely possible that he\x01",
            "entered an automobile.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400471V\x07\x05",
            "Oh, that makes sense.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400472V\x07\x05",
            "I see... Your logic is sound.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400453V\x07\x00",
            "#3304FI agree, Lloyd.\x02\x03",
            "#3400474V#3301FWith that in mind, the question now becomes,\x01",
            "which vehicle did he enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_45C3")

    label("loc_3F2A")

    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400455V#0011FHe couldn't have...\x01",
            "Did he fall into the river?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400456V#3306FSilly detective. You may want to recount\x01",
            "the details you were given.\x02\x03",
            "#3400457V#3301FDidn't that pup of yours state that he\x01",
            "climbed the stairs from the pier?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400458V#0006FOh, that's true.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400459V#3303FBesides, even if he were carried away,\x01",
            "a lingering trail of his scent would remain.\x02\x03",
            "#3400469V#3300FHowever, what if he were to suddenly enter\x01",
            "an airtight space? The scent would be cut off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400470V#0005FHe must have entered an automobile!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400462V\x07\x05",
            "Oh, that's right...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400463V\x07\x05",
            "I see... Your logic is sound.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400473V\x07\x00",
            "#3304FHeehee, you see now?\x02\x03",
            "#3400465V#3301FWith that in mind, the question now becomes,\x01",
            "which vehicle did he enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_45C3")

    label("loc_42C3")

    OP_2C(0x46, 0x1)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400466V#0013FWe should consider the possibility that\x01",
            "Colin was carried away by someone else.\x02\x03",
            "#3400467V#0008FWait, no... That can't be right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400468V#3303FCorrect. Even if he were carried away, a\x01",
            "lingering trail of his scent would remain.\x02\x03",
            "#3400460V#3300FHowever, what if he were to suddenly enter\x01",
            "an airtight space? The scent would be cut off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400461V#0005FHe must have entered an automobile!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400451V\x07\x05",
            "Oh, that's right...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400452V\x07\x05",
            "I see... Your logic is sound.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400464V\x07\x00",
            "#3304FHeehee, you see now?\x02\x03",
            "#3400454V#3301FWith that in mind, the question now becomes,\x01",
            "which vehicle did he enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_45C3")

    label("loc_45C3")

    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400475V\x07\x05",
            "By the way, Lloyd...\x01",
            "Are you with someone?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400476V\x07\x05",
            "I believe I heard the voice of a\x01",
            "young girl with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400477V\x07\x00",
            "#0006FAh, it's a long and complicated story.\x02\x03",
            "#3400478V#0001FAnyway. Why don't we meet up and\x01",
            "sift through the details?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4728():
        OP_96(0xFE, 0x37DC, 0x0, 0xFFFFDECC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_4728)
    WaitChrThread(0x160, 1)
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x160,
        (
            "#3400479V#3304FHey, Detective.\x02\x03",
            "#3400480V#3300FI'm going to borrow your terminal for a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400481V#0005FYou're going to do what?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x160, 3, 0, 25)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x101,
        "#3400482V#5P#0011FH-Hold on a second!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400483V#0013FElie, Tio! Do me a favor. Contact Randy\x01",
            "and head back to the base ASAP!\x02\x03",
            "#3400484VI'll explain everything once you're there!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Elie's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400485V\x07\x05",
            "O-Okay... Understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Tio's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400486V\x07\x05",
            "I am confused at the situation you're in,\x01",
            "but roger, I suppose.\x07\x00\x02",
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
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    SetCameraDistance(18500, 3000)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x160, 0xFF)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 3)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_37BD end

    def Function_25_4A7A(): pass

    label("Function_25_4A7A")

    OP_92(0x160, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_4A8C():
        OP_95(0xFE, 18000, 0, -11200, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_4A8C)
    WaitChrThread(0x160, 1)

    def lambda_4AAA():
        OP_95(0xFE, 18000, -2000, -19600, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_4AAA)
    WaitChrThread(0x160, 1)

    def lambda_4AC8():
        OP_95(0xFE, 27000, -4000, -19600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_4AC8)
    WaitChrThread(0x160, 1)
    Return()

    # Function_25_4A7A end

    def Function_26_4AE2(): pass

    label("Function_26_4AE2")

    OP_92(0x101, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_4AF4():
        OP_95(0xFE, 18000, 0, -11200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AF4)
    WaitChrThread(0x101, 1)

    def lambda_4B12():
        OP_95(0xFE, 18000, -2000, -19600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B12)
    WaitChrThread(0x101, 1)

    def lambda_4B30():
        OP_95(0xFE, 27000, -4000, -19600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B30)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_4AE2 end

    def Function_27_4B4A(): pass

    label("Function_27_4B4A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07200.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    OP_68(32800, -3000, -19000, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 35000, -4000, -19500, 270)
    SetChrPos(0x102, 35000, -4000, -18500, 270)
    SetChrPos(0x103, 36300, -4000, -19500, 270)
    SetChrPos(0x104, 36300, -4000, -18500, 270)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 31300, -4000, -19000, 90)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 30300, -4000, -18300, 90)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 30300, -4000, -19700, 90)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    MoveCamera(43, 23, 0, 11000)
    SetCameraDistance(21500, 11000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_93(0x17, 0x10E, 0x1F4)

    def lambda_4D6D():

        label("loc_4D6D")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_4D6D")

    QueueWorkItem2(0x18, 2, lambda_4D6D)

    def lambda_4D7F():

        label("loc_4D7F")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_4D7F")

    QueueWorkItem2(0x19, 2, lambda_4D7F)

    def lambda_4D91():
        OP_96(0xFE, 0x75F8, 0xFFFFF060, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4D91)
    WaitChrThread(0x17, 1)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    OP_63(0x17, 0x0, 1600, 0x8, 0x9, 0xFA, 0x0)

    def lambda_4DC9():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4DC9)

    def lambda_4DE3():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4DE3)

    def lambda_4DFD():
        OP_98(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4DFD)
    WaitChrThread(0x18, 1)

    def lambda_4E1B():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4E1B)

    def lambda_4E35():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4E35)

    def lambda_4E4F():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4E4F)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x17)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x17, 0x1)
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_4B4A end

    def Function_28_4E8D(): pass

    label("Function_28_4E8D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(160, 5000, 20460, 0)
    MoveCamera(23, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1000, 3000, 22200, 180)
    SetChrPos(0x102, 400, 3000, 22700, 180)
    SetChrPos(0x103, 400, 3000, 24260, 180)
    SetChrPos(0x104, -1000, 3000, 23860, 180)
    Sleep(50)

    def lambda_4F14():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F14)
    Sleep(100)

    def lambda_4F2C():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F2C)
    Sleep(100)

    def lambda_4F44():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F44)
    Sleep(100)

    def lambda_4F5C():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F5C)
    OP_68(-2940, 5000, 12880, 4800)
    MoveCamera(41, 28, 0, 4800)
    OP_6E(600, 4800)
    SetCameraDistance(16500, 4800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4E8D end

    def Function_29_4FBF(): pass

    label("Function_29_4FBF")

    EventBegin(0x0)
    Fade(800)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -31110, -1000, 11250, 270)
    SetChrPos(0x102, -28840, -1000, 11440, 270)
    SetChrPos(0x103, -29910, -1000, 11720, 270)
    SetChrPos(0x104, -27680, -1000, 11600, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_93(0x101, 0xB4, 0x190)
    Sleep(600)

    ChrTalk(
        0x101,
        "#5P#0005FWhat the...?\x02",
    )

    CloseMessageWindow()

    def lambda_5085():

        label("loc_5085")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_5085")

    QueueWorkItem2(0x104, 1, lambda_5085)

    def lambda_5097():

        label("loc_5097")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_5097")

    QueueWorkItem2(0x102, 1, lambda_5097)

    def lambda_50A9():

        label("loc_50A9")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_50A9")

    QueueWorkItem2(0x103, 1, lambda_50A9)
    OP_95(0x101, -31250, -1000, 9570, 700, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fresh scuff marks are on the handrail.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x104,
        "#12P#0305FWhat's goin' on, Lloyd?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FCome check this out. There are\x01",
            "scratch marks on this surface.\x02\x03",
            "#0003FI don't think they were caused by a random\x01",
            "passerby. The scratches are facing\x01",
            "inwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0200FIf you think about it logically, the\x01",
            "back door is an ideal entry point\x01",
            "to sneak into the building.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    TurnDirection(0x101, 0x103, 500)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_52B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_52B1)
    Sleep(10)

    def lambda_52C1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_52C1)

    def lambda_52CE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_52CE)
    Sleep(12)

    def lambda_52DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_52DE)
    Sleep(200)
    OP_68(-19620, 700, 13840, 4000)
    MoveCamera(16, 20, 0, 4000)
    Sleep(5200)
    Fade(500)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#0305FGood thinkin', Tio Tot. You could sneak past\x01",
            "the main entrance usin' this alleyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FIf they were able to avoid the main entrance,\x01",
            "that would explain the lack of witnesses.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_550F")

    ChrTalk(
        0x101,
        (
            "#5P#0000FOkay, I think we should halt our investigation.\x02\x03",
            "Let's head back to Ilya's apartment and\x01",
            "sort through the details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FAye aye! Time to start stitchin' our\x01",
            "master plan together!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x9)
    Jump("loc_55B3")

    label("loc_550F")


    ChrTalk(
        0x101,
        (
            "#5P#0003F...\x02\x03",
            "#0001FIt'd be careless of us to draw a conclusion\x01",
            "this early. Let's look for more clues first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FRoger, I'm keepin' my eyes peeled!\x02",
    )

    CloseMessageWindow()

    label("loc_55B3")

    SetChrPos(0x0, -30970, -1000, 11070, 270)
    OP_66(0x3, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_4FBF end

    def Function_30_55D5(): pass

    label("Function_30_55D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55EF")
    Call(0, 29)
    Return()

    label("loc_55EF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Scuff marks are found on the handrail.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears that the marks were left there recently...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_30_55D5 end

    def Function_31_5679(): pass

    label("Function_31_5679")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(53, 41, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, -29500, -1000, 11640, 56)
    SetChrPos(0x102, -8400, 0, 6880, 0)
    SetChrPos(0x103, -8400, 0, 6880, 0)
    SetChrPos(0x104, -10300, 0, 13950, 0)
    SetChrPos(0x1A, -19560, -1000, 14750, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    MoveCamera(37, 31, 0, 3900)

    def lambda_5759():
        OP_95(0xFE, -19560, -1000, 12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5759)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1200)
    OP_95(0x104, -10300, 0, 7880, 4000, 0x0)
    Sleep(900)

    NpcTalk(
        0x104,
        "Voice",
        "#5C#1PDid you find him?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "Voice",
        (
            "#5C#1PNo luck.\x01",
            "No one saw him on the street.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Voice",
        "#5C#3PHow strange...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        (
            "#5PHah, you think you can catch\x01",
            "me that easily?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(40, 36, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(27430, 0)
    OP_0D()
    Sleep(200)
    OP_93(0x1A, 0x10E, 0x190)
    Sleep(300)

    NpcTalk(
        0x1A,
        "Boy",
        (
            "#5PThis city is filled with a bunch\x01",
            "of useless idiots...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        (
            "#5PHmph, just you wait...\x01",
            "I'll have my revenge!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-22720, 660, 11450, 1200)
    MoveCamera(56, 36, 0, 1200)
    OP_95(0x1A, -19900, -1000, 11430, 6000, 0x1)
    OP_95(0x1A, -22720, -1000, 11450, 6000, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)

    NpcTalk(
        0x1A,
        "Boy",
        "#11PHuh?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Voice",
        "#2PYour revenge is going to have to be put on hold.\x02",
    )

    CloseMessageWindow()
    OP_68(-24890, 660, 11580, 2000)
    SetCameraDistance(31610, 2000)
    OP_95(0x101, -26250, -1000, 12160, 1800, 0x0)

    ChrTalk(
        0x101,
        (
            "#6P#0001FWe knew how you'd move. Looks\x01",
            "like we won this little game\x01",
            "of cat and mouse.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        "#11PDamn it!\x02",
    )

    CloseMessageWindow()

    def lambda_5A70():
        OP_95(0xFE, -21200, -1000, 11420, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5A70)
    Sleep(50)

    ChrTalk(
        0x101,
        "#5P#0007FWhy won't you give up already?!\x02",
    )

    OP_68(-20560, 660, 11200, 2000)
    MoveCamera(306, 36, 0, 2000)
    OP_95(0x101, -21850, -1000, 11450, 6000, 0x0)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        (
            "#12PWhoa!!! Watch where you're touching,\x01",
            "you dumbass!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(100)
    BeginChrThread(0x101, 2, 0, 32)

    NpcTalk(
        0x1A,
        "Boy",
        "#12PL-Let go... Let go of me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FNo can do.\x01",
            "You broke the law.\x02\x03",
            "#0006FCan't you just...behave yourself?!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x1B, 1, 0, 36)

    NpcTalk(
        0x1A,
        "Boy",
        "#12PDamn... DAMN IT!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0010FOuch!\x01",
            "Hey, watch where you're swinging those things!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x104, -11580, 0, 6930, 261)
    SetChrPos(0x102, -10570, 0, 6180, 261)
    SetChrPos(0x103, -10050, 0, 7210, 261)

    ChrTalk(
        0x104,
        (
            "#0300FJust how much energy does this\x01",
            "kid have?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    EndChrThread(0x1A, 0x2)

    def lambda_5CC2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5CC2)

    def lambda_5CCF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CCF)
    OP_68(-18900, 860, 8630, 2000)
    MoveCamera(309, 24, 0, 2000)
    BeginChrThread(0x104, 1, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 1, 0, 33)
    Sleep(200)
    BeginChrThread(0x103, 1, 0, 34)
    Sleep(1200)

    NpcTalk(
        0x1A,
        "Boy",
        "#11PW-Wait, you're the guys from before.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        "#11PTh-This was all a setup?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F#12P*sigh*\x01",
            "Keeping up the charade was tiresome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FYour swift movements managed to\x01",
            "catch us off guard, but our plan\x01",
            "still worked out in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FYeah, but...\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1B58)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x1A, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(800)
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

    ChrTalk(
        0x104,
        (
            "#6P#0303FYour description ain't addin' up.\x02\x03",
            "#0300FWitnesses were tellin' us the culprit\x01",
            "was a dude in a plain getup. Really,\x01",
            "you look like you're from the slums.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FBesides, he doesn't match the appearance\x01",
            "of a teenager from Crossbell.\x02\x03",
            "Where did he actually come from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FHis crimes match the description\x01",
            "of a burglar more than an\x01",
            "obsessed fan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FI hope you have a good reason\x01",
            "for your actions.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#0006FAnd for crying out loud, can't\x01",
            "you behave for just a second?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Boy",
        (
            "#11PStop it! Let go!\x01",
            "Let go of me, you jackass!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(35190, 1800)
    OP_0D()
    EndChrThread(0x1B, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5679 end

    def Function_32_6121(): pass

    label("Function_32_6121")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_615D")
    OP_A6(0xFE, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(800)
    OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
    Sleep(1200)
    Jump("Function_32_6121")

    label("loc_615D")

    Return()

    # Function_32_6121 end

    def Function_33_615E(): pass

    label("Function_33_615E")

    OP_95(0x102, -17370, 0, 6510, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_33_615E end

    def Function_34_617A(): pass

    label("Function_34_617A")

    OP_95(0x103, -16239, 0, 7090, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_34_617A end

    def Function_35_6196(): pass

    label("Function_35_6196")

    OP_95(0x104, -17830, 0, 7480, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_35_6196 end

    def Function_36_61B2(): pass

    label("Function_36_61B2")

    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_36_61B2 end

    def Function_37_61CE(): pass

    label("Function_37_61CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_637A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62C7")

    ChrTalk(
        0x101,
        (
            "#0003FMr. Hayworth should have the Residential District\x01",
            "covered...\x02\x03",
            "If he manages to spot him, he'll contact me\x01",
            "immediately.\x02\x03",
            "#0001FI'll stick to the plan for now, and continue to\x01",
            "search for clues in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6364")

    label("loc_62C7")


    ChrTalk(
        0x101,
        (
            "#0003FMr. Hayworth should have the Residential District\x01",
            "covered...\x02\x03",
            "#0001FI'll stick to the plan for now, and continue to\x01",
            "search for clues in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6364")

    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_637A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6414")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThis isn't the time to be taking a detour...\x02\x03",
            "I need to head over to West Crossbell Highway\x01",
            "immediately!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_6414")

    Return()

    # Function_37_61CE end

    def Function_38_6415(): pass

    label("Function_38_6415")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FI'm not going to find any information\x01",
            "outside of the city.\x02\x03",
            "I should spend a bit more time gathering\x01",
            "information around this neighborhood.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_6415 end

    def Function_39_64C4(): pass

    label("Function_39_64C4")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FI have no reason to return to the SSS\x01",
            "right now, so let's focus on finding Colin!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_64C4 end

    SaveToFile()

Try(main)
