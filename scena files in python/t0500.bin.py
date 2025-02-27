from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0500.bin",                # FileName
        "t0500",                    # MapName
        "t0500",                    # Location
        0x003C,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x06,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0500",                  # 0
        "Amy",                    # 1
        "Carlos",                 # 2
        "Alec",                   # 3
        "Miner Logy",             # 4
        "Mine Chief Hoffmann",    # 5
        "Miner Gantz",            # 6
        "Miner Marlow",           # 7
        "Miner Max",              # 8
        "Tourist",                # 9
        "Tourist Lunarie",        # 10
        "Tourist Coby",           # 11
        "車",                     # 12
        "Miner Marlow",           # 13
        "Mafioso",                # 14
        "Mafioso",                # 15
        "Deputy Commander Baelz", # 16
        "Sergeant Major Seeker",  # 17
        "Bus",                    # 18
        "CGF Guardsman",          # 19
        "CGF Guardsman",          # 20
        "CGF Guardsman",          # 21
        "CGF Guardsman",          # 22
        "SE制御",                 # 23
        "Mainz Mountain Path",    # 24
        "Mainz Mine",             # 25
    ))

    AddCharChip((
        "chr/ch23700.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch26300.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch32200.itc",                   # 06
        "chr/ch30700.itc",                   # 07
        "chr/ch22100.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
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

    DeclNpc(6739,    0,       42729,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(10399,   0,       55259,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(28329,   -3000,   62000,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(15710,   -9000,   39830,   225,  385,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-24540,  11439,   55959,   90,   385,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-21579,  11439,   57630,   180,  385,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(850,     6000,    77519,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4519,    -2000,   25190,   0,    385,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-610,    0,       67440,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(870,     6000,    77220,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  19.399999618530273,    63.29999923706055,     -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.4666666984558105,   -12.65999984741211,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 37,  5.199999809265137,     58.400001525878906,    -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.3466666638851166,   -19.46666717529297,    0.20000000298023224,   1.0])

    DeclActor(-4600,   -2000,   28700,   1500,    -4600,   -500,    28700,   0x007C, 0,  25, 0x0000)
    DeclActor(12000,   400,     70000,   1500,    12000,   1400,    70000,   0x007C, 0,  26, 0x0000)
    DeclActor(-13210,  -2000,   25680,   1200,    -13210,  0,       25680,   0x007C, 0,  60, 0x0000)
    DeclActor(-25900,  11440,   56000,   1500,    -25900,  12940,   56000,   0x007C, 0,  27, 0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "Mainz Mine")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")
    PlaceName(-14.5, 0.0, 24.75, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_737",          # 02, 2
        "Function_3_762",          # 03, 3
        "Function_4_A14",          # 04, 4
        "Function_5_CC6",          # 05, 5
        "Function_6_D8C",          # 06, 6
        "Function_7_F0F",          # 07, 7
        "Function_8_FA4",          # 08, 8
        "Function_9_157D",         # 09, 9
        "Function_10_166C",        # 0A, 10
        "Function_11_167A",        # 0B, 11
        "Function_12_2653",        # 0C, 12
        "Function_13_2784",        # 0D, 13
        "Function_14_3709",        # 0E, 14
        "Function_15_45AB",        # 0F, 15
        "Function_16_4D66",        # 10, 16
        "Function_17_4E75",        # 11, 17
        "Function_18_50A1",        # 12, 18
        "Function_19_5291",        # 13, 19
        "Function_20_55E4",        # 14, 20
        "Function_21_5E0A",        # 15, 21
        "Function_22_5EA8",        # 16, 22
        "Function_23_5F77",        # 17, 23
        "Function_24_60CD",        # 18, 24
        "Function_25_61EA",        # 19, 25
        "Function_26_64F9",        # 1A, 26
        "Function_27_654A",        # 1B, 27
        "Function_28_6638",        # 1C, 28
        "Function_29_6664",        # 1D, 29
        "Function_30_66C9",        # 1E, 30
        "Function_31_6E71",        # 1F, 31
        "Function_32_6E97",        # 20, 32
        "Function_33_6EBD",        # 21, 33
        "Function_34_6EE3",        # 22, 34
        "Function_35_6F09",        # 23, 35
        "Function_36_7894",        # 24, 36
        "Function_37_789B",        # 25, 37
        "Function_38_78A2",        # 26, 38
        "Function_39_865F",        # 27, 39
        "Function_40_86A3",        # 28, 40
        "Function_41_86E7",        # 29, 41
        "Function_42_8722",        # 2A, 42
        "Function_43_9072",        # 2B, 43
        "Function_44_90D5",        # 2C, 44
        "Function_45_9138",        # 2D, 45
        "Function_46_919B",        # 2E, 46
        "Function_47_91ED",        # 2F, 47
        "Function_48_A67D",        # 30, 48
        "Function_49_A6CF",        # 31, 49
        "Function_50_A73F",        # 32, 50
        "Function_51_A753",        # 33, 51
        "Function_52_A767",        # 34, 52
        "Function_53_ABD2",        # 35, 53
        "Function_54_ABDC",        # 36, 54
        "Function_55_AF3D",        # 37, 55
        "Function_56_AF8F",        # 38, 56
        "Function_57_AFE1",        # 39, 57
        "Function_58_B033",        # 3A, 58
        "Function_59_B085",        # 3B, 59
        "Function_60_B0E8",        # 3C, 60
        "Function_61_B189",        # 3D, 61
        "Function_62_B2C4",        # 3E, 62
    ))


    def Function_0_654(): pass

    label("Function_0_654")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_694"),
        (1, "loc_6A0"),
        (2, "loc_6AC"),
        (3, "loc_6B8"),
        (4, "loc_6C4"),
        (5, "loc_6D0"),
        (6, "loc_6DC"),
        (SWITCH_DEFAULT, "loc_6E8"),
    )


    label("loc_694")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_70B")

    Return()

    # Function_0_654 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_736")
    OP_94(0xFE, 0x1C98, 0x8EDA, 0x1F40, 0xB72A, 0x3E8)
    Sleep(300)
    Jump("Function_1_70C")

    label("loc_736")

    Return()

    # Function_1_70C end

    def Function_2_737(): pass

    label("Function_2_737")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_761")
    OP_94(0xFE, 0x648C, 0xEA38, 0x727E, 0xF488, 0x3E8)
    Sleep(300)
    Jump("Function_2_737")

    label("loc_761")

    Return()

    # Function_2_737 end

    def Function_3_762(): pass

    label("Function_3_762")

    BeginChrThread(0xA, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_792")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7BC")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_817")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 910, 0, 50450, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -22550, 11440, 56120, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -20140, 11440, 57900, 45)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_971")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_82B")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_971")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_855")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_86E")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_887")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x8, 4520, -2000, 26540, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_971")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8C4")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_971")

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8DD")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_8DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F6")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_913")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_971")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_95D")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -21670, 11440, 55170, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -21580, 11440, 56390, 0)
    Jump("loc_971")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_971")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_99D")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99D")
    Event(0, 54)

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_9B1")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 42)
    Jump("loc_9D4")

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_9C5")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 47)
    Jump("loc_9D4")

    label("loc_9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_9D4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 52)

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_9FB")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 7)

    label("loc_9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_A13")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_A13")

    Return()

    # Function_3_762 end

    def Function_4_A14(): pass

    label("Function_4_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2B")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A80")
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x13)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)

    label("loc_A80")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9C")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_A9C")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB0")
    ClearMapObjFlags(0x6, 0x10)

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABE")
    OP_66(0x3, 0x1)

    label("loc_ABE")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Call(0, 28)
    SetMapObjFlags(0x9, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B54")
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_B54")
    OP_66(0x2, 0x1)

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B65")
    Call(0, 29)

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BDF")
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_66(0x2, 0x1)

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_END)), "loc_BF2")
    OP_16(0x3, 0x5, 0x1, 0x0)
    Jump("loc_C18")

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C13")
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0E")
    OP_16(0x3, 0x5, 0x1, 0x0)

    label("loc_C0E")

    Jump("loc_C18")

    label("loc_C13")

    OP_16(0x3, 0x5, 0x1, 0x0)

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C44")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    Jump("loc_C6B")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6B")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)

    label("loc_C6B")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA9")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_CA9")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Return()

    # Function_4_A14 end

    def Function_5_CC6(): pass

    label("Function_5_CC6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City - North Exit\x01",      # 0
            "Bus Stop (Doll Studio)\x01",           # 1
            "Leave\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D64")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D84")

    label("loc_D64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D84")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_D84")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_CC6 end

    def Function_6_D8C(): pass

    label("Function_6_D8C")

    Fade(1000)
    OP_68(1060, -550, -2890, 0)
    MoveCamera(308, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -5300, -2000, 27570, 180)
    SetChrPos(0x2, -6100, -2000, 27430, 180)
    SetChrPos(0x3, -6860, -2000, 27250, 180)
    ClearChrFlags(0x19, 0x80)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_78(0xA, 0x19)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x19, 0, -2000, -8290, 0)
    OP_D3(0x19, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)

    def lambda_E67():
        OP_95(0xFE, 450, -2000, 6620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E67)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)
    Fade(1000)
    OP_68(-3860, -550, 26120, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x19, -6320, -2000, 18640, 0)

    def lambda_ED5():
        OP_95(0xFE, -6320, -2000, 21130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_ED5)
    WaitChrThread(0x19, 1)
    OP_71(0xA, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0xA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_D8C end

    def Function_7_F0F(): pass

    label("Function_7_F0F")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -4540, -2000, 27710, 180)
    SetChrPos(0x2, -4540, -2000, 27710, 180)
    SetChrPos(0x3, -4540, -2000, 27710, 180)
    OP_68(-4540, -550, 27710, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_F0F end

    def Function_8_FA4(): pass

    label("Function_8_FA4")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1575")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1512")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104A")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1065")

    label("loc_104A")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_1065")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1093")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_10A9")

    label("loc_1093")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_10A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D7")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_10ED")

    label("loc_10D7")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_10ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1133")

    label("loc_111C")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_1133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1162")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1179")

    label("loc_1162")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_1179")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_11B5")

    label("loc_11A3")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_11B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E1")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_11F5")

    label("loc_11E1")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_11F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122D")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_124D")

    label("loc_122D")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_124D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127B")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1291")

    label("loc_127B")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_1291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_12DD")

    label("loc_12C3")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_12DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1317")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1339")

    label("loc_1317")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_1339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1368")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_137F")

    label("loc_1368")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_137F")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1503")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1456"),
        (1, "loc_1464"),
        (2, "loc_1472"),
        (3, "loc_1480"),
        (4, "loc_148E"),
        (5, "loc_149C"),
        (6, "loc_14AA"),
        (7, "loc_14B8"),
        (8, "loc_14C6"),
        (9, "loc_14D4"),
        (10, "loc_14E2"),
        (11, "loc_14F0"),
        (SWITCH_DEFAULT, "loc_14FE"),
    )


    label("loc_1456")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_1464")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_1472")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_1480")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_148E")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_149C")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14AA")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14B8")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14C6")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14D4")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14E2")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14F0")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14FE")

    label("loc_14FE")

    Jump("loc_150D")

    label("loc_1503")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_150D")

    Jump("loc_1570")

    label("loc_1512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155D")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1570")

    label("loc_155D")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1570")

    Jump("loc_FBE")

    label("loc_1575")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_FA4 end

    def Function_9_157D(): pass

    label("Function_9_157D")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -11920, -2000, 26400, 45)
    SetChrPos(0x1, -11920, -2000, 26400, 45)
    SetChrPos(0x2, -11920, -2000, 26400, 45)
    SetChrPos(0x3, -11920, -2000, 26400, 45)
    SetChrPos(0x4, -11920, -2000, 26400, 45)
    SetChrPos(0x5, -11920, -2000, 26400, 45)
    Sleep(1)
    OP_68(-11920, -550, 26400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1651")
    Sound(1502, 255, 100, 0)
    Jump("loc_1657")

    label("loc_1651")

    Sound(1503, 255, 100, 0)

    label("loc_1657")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_157D end

    def Function_10_166C(): pass

    label("Function_10_166C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_166C end

    def Function_11_167A(): pass

    label("Function_11_167A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16E8")

    ChrTalk(
        0xFE,
        (
            "Gantz and the mayor ended up not\x01",
            "returning yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Umm, did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_16E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1757")

    ChrTalk(
        0xFE,
        (
            "Wait, Gantz decided to pack up his bags\x01",
            "and live in the big city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Fine. Good riddance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1819")

    ChrTalk(
        0xFE,
        (
            "Carlos looks pretty torn up over\x01",
            "Gantz having gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think he should beat himself\x01",
            "up over it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He honestly takes everything\x01",
            "far too seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_18CB")

    ChrTalk(
        0xFE,
        "Oh, looks like it's getting dark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I bet my brother, Logy, is going to be cranky\x01",
            "when he gets home from work. I know they've\x01",
            "been working him hard lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_18CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198C")
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Well, I DO find you to be both\x01",
            "attractive and chivalrous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* A pity. If only you were a man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0505FHuh? Come again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, don't mind me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A0C")

    label("loc_198C")


    ChrTalk(
        0xFE,
        (
            "I thought my knight in shining armor had\x01",
            "finally appeared, only for her to be a woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, no point crying over it.\x02",
    )

    CloseMessageWindow()

    label("loc_1A0C")

    Jump("loc_264F")

    label("loc_1A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AF2")

    ChrTalk(
        0xFE,
        (
            "Another Anniversary Festival, another\x01",
            "failed attempt at bagging me a good man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's okay! I'll turn it around next year!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? Why do I feel a sense of deja vu?\x01",
            "Did I say the same thing last year?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C23")

    ChrTalk(
        0xFE,
        "*siiiiigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A super handsome tourist stopped by\x01",
            "town for a little while yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He soaked in the sights, then immediately\x01",
            "went right back to Crossbell City!\x01",
            "Can you believe that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Argh! This is so frustrating! Why's it feel\x01",
            "like life's always mocking me?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CBC")

    label("loc_1C23")


    ChrTalk(
        0xFE,
        (
            "Why'd he have to come and just\x01",
            "see the sights before leaving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oooh! I knew I should have brought him\x01",
            "to Der Ziegel and gotten him drunk first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBC")

    Jump("loc_264F")

    label("loc_1CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDC")
    Call(0, 12)
    Jump("loc_1D62")

    label("loc_1CDC")


    ChrTalk(
        0xFE,
        (
            "Now, now... No need to be a\x01",
            "stranger around little old me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Follow me, and I'll show you the\x01",
            "best view in all of Mainz... ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    Jump("loc_264F")

    label("loc_1D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1E48")

    ChrTalk(
        0xFE,
        (
            "I hear the opening day of Arc en Ciel's new show had\x01",
            "lines stretching all the way to the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave it to Arc en Ciel's star, Ilya Platiere,\x01",
            "to be able to attract that many people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_264F")

    label("loc_1E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_206F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA2")

    ChrTalk(
        0xFE,
        (
            "I recently took the bus over to Crossbell City\x01",
            "in hopes of finding myself a good man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And as we exited the mountain tunnel, I\x01",
            "noticed the cutest little girl on the side of\x01",
            "the road. I almost mistook her for a doll!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got the impression that she wasn't from here...\x01",
            "I wonder what she was doing all alone?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_206A")

    label("loc_1FA2")


    ChrTalk(
        0xFE,
        (
            "I seem to recall her being near the path that\x01",
            "leads to the...Rosen-what Studio? Can't quite\x01",
            "remember the full name of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I wonder what a girl like her was\x01",
            "doing out there all alone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206A")

    Jump("loc_264F")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2247")

    ChrTalk(
        0xFE,
        (
            "*sigh* Did all of the best men in Mainz\x01",
            "decide to skip town when I was born?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "See, my brother is lazy to his very core and extremely\x01",
            "unsociable. I know he's a miner, but no matter what he\x01",
            "does, he just smells like mud all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carlos may be an option, but he's far\x01",
            "too gentle for my tastes. I prefer a\x01",
            "man who's more...wild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess the only thing I can do is go to Crossbell\x01",
            "City and fish--er, I mean, LOOK for a man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_22C4")

    label("loc_2247")


    ChrTalk(
        0xFE,
        (
            "There's only one thing left to do. I've got to\x01",
            "find myself a nice man from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "When does the bus come again?\x02",
    )

    CloseMessageWindow()

    label("loc_22C4")

    Jump("loc_264F")

    label("loc_22C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_22D7")
    Jump("loc_264F")

    label("loc_22D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_241F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B4")

    ChrTalk(
        0xFE,
        "Brrrrr... It's really started to get cold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, oops. Mayor Bickson wanted me home\x01",
            "before it got dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd rather not get attacked by monsters\x01",
            "on the street, so I'll do just that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_241A")

    label("loc_23B4")


    ChrTalk(
        0xFE,
        (
            "Nights on the mountain are brutally cold.\x01",
            "Maybe a nice stew for dinner would warm\x01",
            "everyone up...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241A")

    Jump("loc_264F")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_264F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2444")
    SetScenarioFlags(0x66, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_2444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(
        0xFE,
        (
            "(Oh, my... TWO handsome men?\x01",
            "At the same time?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FIs something wrong, ma'am?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nope. Nothing at all, mister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Welcome to Mainz. Please take your time\x01",
            "to savor everything our town has to offer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6F, 6)
    Jump("loc_264F")

    label("loc_2560")


    ChrTalk(
        0xFE,
        (
            "(Mmm. The guy with the jacket is super\x01",
            "cute, but the tall redhead looks like a total\x01",
            "bad boy... ㈱)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Is there something wrong with her, or...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F(Eh. Havin' a lady stare at you ain't\x01",
            "the end of the world, Lloyd.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264F")

    TalkEnd(0xFE)
    Return()

    # Function_11_167A end

    def Function_12_2653(): pass

    label("Function_12_2653")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0x8, 0x10, 0)
    TurnDirection(0x10, 0x8, 0)

    ChrTalk(
        0x10,
        (
            "Is this Armorica Village?\x01",
            "Nope, doesn't look like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Oh, barnacles. Did I take the wrong bus?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hello, mister. You made it to Mainz, a wonderful\x01",
            "town with quite a few...desirable views.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you'd like, I would looove to show\x01",
            "you around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "U-U-Uhh...\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_12_2653 end

    def Function_13_2784(): pass

    label("Function_13_2784")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_294A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CD")

    ChrTalk(
        0xFE,
        (
            "I was going to drive over to the city\x01",
            "to pick up the mayor and Gantz last\x01",
            "night, but I got shot down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Bickson told me that they might be\x01",
            "staying in Crossbell City for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's fine, I guess, but his voice bothered me.\x01",
            "I've never heard the mayor sound so downcast\x01",
            "before...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2945")

    label("loc_28CD")


    ChrTalk(
        0xFE,
        (
            "The mayor said they have to stay in\x01",
            "Crossbell City for a little while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why'd he sound so depressed, though?\x02",
    )

    CloseMessageWindow()

    label("loc_2945")

    Jump("loc_3705")

    label("loc_294A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_29FE")

    ChrTalk(
        0xFE,
        (
            "Mayor Bickson finally decided to go\x01",
            "to the city himself to pick up Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Just the fact that we know where\x01",
            "he is takes a huge load off my shoulders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_29FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_2BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B39")

    ChrTalk(
        0xFE,
        (
            "Y'see, I was the one who took Gantz\x01",
            "to Crossbell City in the first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I had to deliver some septium, so he insisted\x01",
            "that I take him along for the ride...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but Gantz didn't come back at the\x01",
            "time we agreed on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I'm begging you.\x01",
            "You have to help find Gantz!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2BE0")

    label("loc_2B39")


    ChrTalk(
        0xFE,
        (
            "A part of me feels responsible for\x01",
            "Gantz's disappearance since I\x01",
            "was the one who took him to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I'm begging you.\x01",
            "You have to help find Gantz!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE0")

    Jump("loc_3705")

    label("loc_2BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9C")

    ChrTalk(
        0xFE,
        (
            "Oh, you're that Special Support\x01",
            "Section that the mayor asked for\x01",
            "help from, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for coming. The mayor's house\x01",
            "is the furthest one back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CCD")

    label("loc_2C9C")


    ChrTalk(
        0xFE,
        "The mayor's house is the furthest one back.\x02",
    )

    CloseMessageWindow()

    label("loc_2CCD")

    Jump("loc_3705")

    label("loc_2CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2DC6")

    ChrTalk(
        0xFE,
        (
            "You know how the road branches off in\x01",
            "the tunnel on your way to Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A few people swear they've been hearing some\x01",
            "freaky bell ringing down that path recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That area's pretty desolate, so it's\x01",
            "a little creepy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_2DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(
        0xFE,
        (
            "Well, come tonight, I'll have to go pick\x01",
            "up all the miners from the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You think Gantz managed to\x01",
            "break even this year?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, doubt it. We ARE talking about\x01",
            "Gantz, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_2E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2F89")

    ChrTalk(
        0xFE,
        (
            "I had the chance to check out the\x01",
            "Anniversary Festival, and man, was\x01",
            "Crossbell City crowded this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard people say it's because of\x01",
            "Arc en Ciel's new show, and after seeing\x01",
            "the state the city is in, I believe it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_2F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_307C")

    ChrTalk(
        0xFE,
        (
            "I'll be transporting some septium deposits over to the city\x01",
            "today, so I thought I might as well check out the festival, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, this is going to be great. Maybe I should\x01",
            "grab a bite to eat at Long Lao while I'm there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_307C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_313E")

    ChrTalk(
        0xFE,
        (
            "Most of the younger miners have gone to the\x01",
            "city because of the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those guys are always working so hard\x01",
            "in the mines, so I'm glad they can let loose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_313E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_328F")

    ChrTalk(
        0xFE,
        (
            "All of the septium we mine here is used in\x01",
            "a variety of different industries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The smaller sepith fragments are used in manufacturing\x01",
            "quartz, and larger crystals are primarily used in\x01",
            "making jewelry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whenever I start thinking about how the\x01",
            "septium we mine will be used, it...it really\x01",
            "makes me proud. *sniff*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_328F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(
        0xFE,
        (
            "I've been transporting septium with my truck for\x01",
            "a while now, so sometimes I can't help but think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When will we end up running out of\x01",
            "septium? It's not like the mine has\x01",
            "an infinite amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, man. Thinking about this always\x01",
            "puts me in a bad mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3705")

    label("loc_33A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_33B5")
    Jump("loc_3705")

    label("loc_33B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_364F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355A")

    ChrTalk(
        0xFE,
        (
            "The sunset looks absolutely amazing from\x01",
            "the mountain. One look is beautiful enough\x01",
            "cleanse your weary heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. I also remember seeing some\x01",
            "huge thing flying in the sky earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never seen birds or monsters around here\x01",
            "even come close to that size, so what the heck\x01",
            "could it be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(This definitely sounds sketchy, but it's\x01",
            "not related to our current case.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 0)
    Jump("loc_364A")

    label("loc_355A")


    ChrTalk(
        0xFE,
        (
            "I remember seeing something huge\x01",
            "flying in the sky earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've never seen anything around\x01",
            "here even come close to that size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, I only saw it when it was raining last night,\x01",
            "so maybe my eyes were playing tricks on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364A")

    Jump("loc_3705")

    label("loc_364F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3674")
    SetScenarioFlags(0x66, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_3674")


    ChrTalk(
        0xFE,
        (
            "What's with the van parked at the\x01",
            "front of town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm no expert on vehicles, but that van is\x01",
            "obviously really nice... Just whose is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3705")

    TalkEnd(0xFE)
    Return()

    # Function_13_2784 end

    def Function_14_3709(): pass

    label("Function_14_3709")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3824")

    ChrTalk(
        0xFE,
        (
            "The mining crew's been trying to work\x01",
            "extra hard to make up for Gantz's\x01",
            "absence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those guys always try their best to look\x01",
            "after each other. Even that slacker Logy\x01",
            "has been going at it pretty hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've always found them really admirable.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_38A9")

    label("loc_3824")


    ChrTalk(
        0xFE,
        (
            "I want to become a miner and\x01",
            "be able to help everyone out, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My mom seems to think\x01",
            "it's too dangerous for me, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A9")

    Jump("loc_45A7")

    label("loc_38AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F0")

    ChrTalk(
        0xFE,
        (
            "You found Gantz, right?\x01",
            "Oh, thank the Goddess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, how was he doing?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_396D")

    ChrTalk(
        0x101,
        (
            "#0008F...\x02\x03",
            "(I can't just tell him that Gantz\x01",
            "might be hooked on drugs...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39E8")

    label("loc_396D")


    ChrTalk(
        0x101,
        (
            "#0000FI don't think you have anything to worry about.\x01",
            "(His circumstances are anything but\x01",
            "normal, that's for sure...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E8")

    SetScenarioFlags(0x0, 5)
    Jump("loc_3A61")

    label("loc_39F0")


    ChrTalk(
        0xFE,
        (
            "When Gantz finally comes back, he's\x01",
            "going to have to tell me about all of his\x01",
            "adventures in Crossbell City!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A61")

    Jump("loc_45A7")

    label("loc_3A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3AF2")

    ChrTalk(
        0xFE,
        "I wonder where Gantz ran off to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's usually only gone for about\x01",
            "three days, but no one's been able to find him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3B6B")

    ChrTalk(
        0xFE,
        (
            "I asked Marlow, and even he doesn't\x01",
            "know where Gantz went off to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened to him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3BEB")

    ChrTalk(
        0xFE,
        (
            "You know, I haven't seen Gantz\x01",
            "around Mainz lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was looking forward to asking\x01",
            "him about the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3D97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0F")

    ChrTalk(
        0xFE,
        (
            "Logy was constantly complaining about\x01",
            "how boring work was yesterday that it\x01",
            "made me start to wonder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do any of the miners\x01",
            "actually enjoy their job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They look like they have a lot of fun\x01",
            "just drinking and talking about the\x01",
            "casino after work, too...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D92")

    label("loc_3D0F")


    ChrTalk(
        0xFE,
        (
            "Do any of the miners\x01",
            "actually enjoy their job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not sure how to feel about\x01",
            "that, since I want to be a miner myself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D92")

    Jump("loc_45A7")

    label("loc_3D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E59")

    ChrTalk(
        0xFE,
        (
            "I want to be a miner someday,\x01",
            "so I tried asking Logy if he could\x01",
            "teach me some tricks of the trade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He didn't look too enthused, though.\x01",
            "I guess he doesn't like his job?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F1E")

    ChrTalk(
        0xFE,
        (
            "Did you know my dad is Mainz's official\x01",
            "mine chief? That's because he's super\x01",
            "strong and cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I'm going to be a miner, just\x01",
            "like him! Hehe. Jealous, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3FDA")

    ChrTalk(
        0xFE,
        (
            "My dad ended up going to one of the mining\x01",
            "crew's drinking parties yesterday. That's pretty unusual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I'm so jealous... Why couldn't\x01",
            "he have taken me with him?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_3FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E2")

    ChrTalk(
        0xFE,
        (
            "I kind of fell down pretty hard\x01",
            "while I was running around town yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I got back home all scraped up from\x01",
            "head to toe, and my mom was furious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha... I guess I should pay more attention\x01",
            "to my surroundings next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4182")

    label("loc_40E2")


    ChrTalk(
        0xFE,
        (
            "I got my foot caught on the grating\x01",
            "yesterday and fell down really hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That hurt so freaking bad... I need to be\x01",
            "more careful from now on, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4182")

    Jump("loc_45A7")

    label("loc_4187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4327")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4272")

    ChrTalk(
        0xFE,
        (
            "Have you ever gone to those creepy ruins\x01",
            "down the mountain path's branching road?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't help but get fired up when I see\x01",
            "something like that. I swear, I'm going\x01",
            "to explore them one of these days.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4322")

    label("loc_4272")


    ChrTalk(
        0xFE,
        (
            "Have you ever gone to those creepy ruins\x01",
            "down the mountain path's branching road?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what it looks like inside...\x01",
            "I'll have to go explore it one of these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4322")

    Jump("loc_45A7")

    label("loc_4327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4335")
    Jump("loc_45A7")

    label("loc_4335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_43EF")

    ChrTalk(
        0xFE,
        (
            "My dad is the mine chief, AKA, the\x01",
            "most important person in the mine!\x01",
            "Cool, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The mine shift must be done for the\x01",
            "day. I guess I'll go and pick up my\x01",
            "dad now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A7")

    label("loc_43EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_45A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4414")
    SetScenarioFlags(0x66, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_4414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_452F")

    ChrTalk(
        0xFE,
        (
            "You know about that locked tunnel\x01",
            "outside of town, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, it's a long-abandoned mine\x01",
            "shaft. Doesn't that sound awesome?\x01",
            "I really want to explore it someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then again, going anywhere near there\x01",
            "would only put me on the mayor's bad side.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_45A7")

    label("loc_452F")


    ChrTalk(
        0xFE,
        (
            "In an old, abandoned mine like that, you just\x01",
            "KNOW there has to be some sort of secret\x01",
            "treasure sleeping in there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A7")

    TalkEnd(0xFE)
    Return()

    # Function_14_3709 end

    def Function_15_45AB(): pass

    label("Function_15_45AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_45BC")
    Jump("loc_4D62")

    label("loc_45BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_45CA")
    Jump("loc_4D62")

    label("loc_45CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_4631")

    ChrTalk(
        0xFE,
        "*sigh* Work's finally over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pooped. I think I'll just go\x01",
            "home and relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D62")

    label("loc_4631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_463F")
    Jump("loc_4D62")

    label("loc_463F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_464D")
    Jump("loc_4D62")

    label("loc_464D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_46FD")

    ChrTalk(
        0xFE,
        (
            "The mine chief's son looked down\x01",
            "in the dumps today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess that was probably my fault.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* Look at me, complaining to\x01",
            "a kid. I'm a failure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D62")

    label("loc_46FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_47C5")

    ChrTalk(
        0xFE,
        (
            "The chief's son was asking me\x01",
            "about my job today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I know he's just interested\x01",
            "in what we do, but all I did\x01",
            "was end up complaining to him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, I screwed up big time...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D62")

    label("loc_47C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_488F")

    ChrTalk(
        0xFE,
        (
            "Life is so dull... Even a drinking party\x01",
            "can't get me motivated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not that I ever have any motivation.\x01",
            "Oh, well. It's the Anniversary Festival,\x01",
            "so it's the perfect time to relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D62")

    label("loc_488F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_489D")
    Jump("loc_4D62")

    label("loc_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4984")

    ChrTalk(
        0xFE,
        "A miner's salary is nothing special.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's fine if you're living here, but if you\x01",
            "went to the city's Entertainment District,\x01",
            "you'd be broke in no time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Geez, is any of this really worth it?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A0E")

    label("loc_4984")


    ChrTalk(
        0xFE,
        (
            "I work and work and work, and life\x01",
            "doesn't seem to get any easier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I slack off on my shift a lot,\x01",
            "so that might be why.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A0E")

    Jump("loc_4D62")

    label("loc_4A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAD")

    ChrTalk(
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okay, yeah. I'm slacking, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It'll just be for a little bit, so don't\x01",
            "tell the other miners, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4B04")

    label("loc_4AAD")


    ChrTalk(
        0xFE,
        (
            "I'm worn out right now, so\x01",
            "I just need a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Don't tell the others, okay?\x02",
    )

    CloseMessageWindow()

    label("loc_4B04")

    Jump("loc_4D62")

    label("loc_4B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4B17")
    Jump("loc_4D62")

    label("loc_4B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B32")
    Call(0, 16)
    Jump("loc_4BFF")

    label("loc_4B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD2")

    ChrTalk(
        0xFE,
        (
            "*yawn*... I'll probably just head home\x01",
            "and lay in my bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(I'm not really that tired, given that I\x01",
            "didn't do much at work today...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4BFF")

    label("loc_4BD2")


    ChrTalk(
        0xFE,
        "*yawn*... I think I'm going to go home.\x02",
    )

    CloseMessageWindow()

    label("loc_4BFF")

    Jump("loc_4D62")

    label("loc_4C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C29")
    SetScenarioFlags(0x66, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_4C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D04")

    ChrTalk(
        0xFE,
        (
            "One of the miners was attacked by\x01",
            "monsters not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His wounds weren't too serious,\x01",
            "but he was told to take a few days\x01",
            "off, just to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Goddess, I wish that was me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4D62")

    label("loc_4D04")


    ChrTalk(
        0xFE,
        (
            "Being able to sit in bed all day\x01",
            "because of some little cuts would\x01",
            "be a dream come true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D62")

    TalkEnd(0xFE)
    Return()

    # Function_15_45AB end

    def Function_16_4D66(): pass

    label("Function_16_4D66")


    ChrTalk(
        0xFE,
        (
            "(Well, it's not like I do much anyway.\x01",
            "I've mainly been reading a book while\x01",
            "on the job, recently.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Hey, guys. Mind taking this book off my\x01",
            "hands before the mine chief finds out?)\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C8, 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_16_4D66 end

    def Function_17_4E75(): pass

    label("Function_17_4E75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E86")
    Jump("loc_509D")

    label("loc_4E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E94")
    Jump("loc_509D")

    label("loc_4E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_4F56")

    ChrTalk(
        0xFE,
        "Is today's shift over already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since Gantz disappeared, the whole\x01",
            "crew has been really inefficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For better or worse, that guy knew how\x01",
            "to get us pumped up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_509D")

    label("loc_4F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4F64")
    Jump("loc_509D")

    label("loc_4F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4F72")
    Jump("loc_509D")

    label("loc_4F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4F80")
    Jump("loc_509D")

    label("loc_4F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F8E")
    Jump("loc_509D")

    label("loc_4F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F9C")
    Jump("loc_509D")

    label("loc_4F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FAA")
    Jump("loc_509D")

    label("loc_4FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4FB8")
    Jump("loc_509D")

    label("loc_4FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4FC6")
    Jump("loc_509D")

    label("loc_4FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4FD4")
    Jump("loc_509D")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_5094")
    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "Listen, guys! I don't care if you get a few\x01",
            "drinks, but try to get home quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until Max recovers, I won't stand for\x01",
            "any one of you getting hurt, you hear me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_509D")

    label("loc_5094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_509D")

    label("loc_509D")

    TalkEnd(0xFE)
    Return()

    # Function_17_4E75 end

    def Function_18_50A1(): pass

    label("Function_18_50A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_50B2")
    Jump("loc_528D")

    label("loc_50B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_50C0")
    Jump("loc_528D")

    label("loc_50C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_50CE")
    Jump("loc_528D")

    label("loc_50CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_50DC")
    Jump("loc_528D")

    label("loc_50DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50EA")
    Jump("loc_528D")

    label("loc_50EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_50F8")
    Jump("loc_528D")

    label("loc_50F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5106")
    Jump("loc_528D")

    label("loc_5106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5114")
    Jump("loc_528D")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_51B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512F")
    Call(0, 19)
    Jump("loc_51B4")

    label("loc_512F")


    ChrTalk(
        0xFE,
        (
            "Ugh... This hangover is going to be\x01",
            "the end of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I almost envy Logy. He got completely\x01",
            "smashed so he's still passed out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51B4")

    Jump("loc_528D")

    label("loc_51B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_51C7")
    Jump("loc_528D")

    label("loc_51C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_51D5")
    Jump("loc_528D")

    label("loc_51D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_51E3")
    Jump("loc_528D")

    label("loc_51E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_5284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51FE")
    Call(0, 19)
    Jump("loc_527F")

    label("loc_51FE")


    ChrTalk(
        0xFE,
        (
            "Look, I work all day in a dark, depressing\x01",
            "cave. You can't blame me for wanting to\x01",
            "reward myself with a drink now and then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_527F")

    Jump("loc_528D")

    label("loc_5284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_528D")

    label("loc_528D")

    TalkEnd(0xFE)
    Return()

    # Function_18_50A1 end

    def Function_19_5291(): pass

    label("Function_19_5291")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52B5")
    Jump("loc_55D5")

    label("loc_52B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52C3")
    Jump("loc_55D5")

    label("loc_52C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_52D1")
    Jump("loc_55D5")

    label("loc_52D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_52DF")
    Jump("loc_55D5")

    label("loc_52DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_52ED")
    Jump("loc_55D5")

    label("loc_52ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_52FB")
    Jump("loc_55D5")

    label("loc_52FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5309")
    Jump("loc_55D5")

    label("loc_5309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5317")
    Jump("loc_55D5")

    label("loc_5317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_546F")

    ChrTalk(
        0xD,
        "Ugh... My poor head.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You drank WAY too much, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You know, I can't believe the mayor\x01",
            "would treat all of us to drinks for the\x01",
            "festival. He's a really nice guy, ain't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, but thanks to that, Logy is still\x01",
            "passed out in Der Ziegel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, yesterday was still a good time,\x01",
            "so I guess I'll let it slide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55D5")

    label("loc_546F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_547D")
    Jump("loc_55D5")

    label("loc_547D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_548B")
    Jump("loc_55D5")

    label("loc_548B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_5499")
    Jump("loc_55D5")

    label("loc_5499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_55CC")

    ChrTalk(
        0xE,
        "Phew, I never thought that shift would end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hey. After this, let's grab a few drinks\x01",
            "at Der Ziegel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Did you not hear the mayor? He said\x01",
            "we need to hurry and get home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Don't be such a worry-wart. The night\x01",
            "is still young, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I guess a few drinks won't hurt...\x02",
    )

    CloseMessageWindow()
    Jump("loc_55D5")

    label("loc_55CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55D5")

    label("loc_55D5")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_5291 end

    def Function_20_55E4(): pass

    label("Function_20_55E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_57C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5721")

    ChrTalk(
        0xFE,
        (
            "We're low on manpower right now,\x01",
            "so we've had to start working earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even while Gantz is gone, we still\x01",
            "have our jobs to do, so we're trying\x01",
            "our best to make up for his part, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. When Gantz drags his sorry butt back\x01",
            "here, he's going to have to make it up to us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_57BC")

    label("loc_5721")


    ChrTalk(
        0xFE,
        (
            "Even while Gantz is gone we\x01",
            "still have our jobs to do, so we're trying\x01",
            "our best to make up for his part, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, time to hit the mines again.\x02",
    )

    CloseMessageWindow()

    label("loc_57BC")

    Jump("loc_5E06")

    label("loc_57C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_593F")

    ChrTalk(
        0xFE,
        "Seems like Gantz was finally found yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That guy would never stop complaining\x01",
            "about how his mining work was too tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He ended up becoming a gambling addict to\x01",
            "blow off some steam, but I never would've\x01",
            "guessed he'd go completely missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry for all the trouble he's caused the\x01",
            "SSS. Please, allow me to apologize for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5A57")

    label("loc_593F")


    ChrTalk(
        0xFE,
        (
            "Mining is a strenuous job and the pay\x01",
            "isn't anything to write home about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's probably a bunch of people who\x01",
            "are dissatisfied, but no one really speaks\x01",
            "up about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I think this whole mess with\x01",
            "Gantz boiled down to his pent-up stress\x01",
            "overflowing...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A57")

    Jump("loc_5E06")

    label("loc_5A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_5AF6")

    ChrTalk(
        0xFE,
        (
            "Gantz and I have been friends ever since\x01",
            "we were kids, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So whenever he's not around, everything\x01",
            "just feels kind of wrong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E06")

    label("loc_5AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_5B04")
    Jump("loc_5E06")

    label("loc_5B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5B31")

    ChrTalk(
        0xFE,
        "Where the heck did he go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E06")

    label("loc_5B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5C84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0xFE,
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though the Anniversary Festival\x01",
            "is going on, it doesn't look like we'll be\x01",
            "doing anything interesting while it's going on.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5C7F")

    label("loc_5BE0")


    ChrTalk(
        0xFE,
        (
            "Hmm? I'm not playing hooky.\x01",
            "Don't lump me together with that slacker, Logy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I went and asked the mine chief for\x01",
            "permission before going for a smoke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7F")

    Jump("loc_5E06")

    label("loc_5C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5C92")
    Jump("loc_5E06")

    label("loc_5C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5CA0")
    Jump("loc_5E06")

    label("loc_5CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CBB")
    Call(0, 19)
    Jump("loc_5D71")

    label("loc_5CBB")


    ChrTalk(
        0xFE,
        (
            "Last night was a hoot. I felt like a celebrity\x01",
            "with the mayor treating us to drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like I've got my morale back, thanks\x01",
            "to that... Well, time to get back to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D71")

    Jump("loc_5E06")

    label("loc_5D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D84")
    Jump("loc_5E06")

    label("loc_5D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5D92")
    Jump("loc_5E06")

    label("loc_5D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_5DA0")
    Jump("loc_5E06")

    label("loc_5DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_5DFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DBB")
    Call(0, 19)
    Jump("loc_5DF8")

    label("loc_5DBB")


    ChrTalk(
        0xFE,
        (
            "Socializing isn't too bad when it's done\x01",
            "in moderation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DF8")

    Jump("loc_5E06")

    label("loc_5DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5E06")

    label("loc_5E06")

    TalkEnd(0xFE)
    Return()

    # Function_20_55E4 end

    def Function_21_5E0A(): pass

    label("Function_21_5E0A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "It's been almost two weeks since we've\x01",
            "had any sort of party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One of our coworkers is missing, so it'd\x01",
            "be kinda tasteless to go celebrating.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_5E0A end

    def Function_22_5EA8(): pass

    label("Function_22_5EA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EBD")
    Call(0, 12)
    Jump("loc_5F73")

    label("loc_5EBD")


    ChrTalk(
        0xFE,
        (
            "Man, I wanted to go visit Armorica Village,\x01",
            "but I ended up here, instead...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I can take a look around while I'm here.\x01",
            "All these high-up views should be pretty nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F73")

    TalkEnd(0xFE)
    Return()

    # Function_22_5EA8 end

    def Function_23_5F77(): pass

    label("Function_23_5F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6044")

    ChrTalk(
        0xFE,
        (
            "I haven't been around many\x01",
            "mining towns before, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must say, the scenery is really nice,\x01",
            "and there's a lot of unusual things you can\x01",
            "spot. Overall, I'm glad I visited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_60C9")

    label("loc_6044")


    ChrTalk(
        0xFE,
        (
            "Still, what could this equipment be\x01",
            "used for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess ordinary people like me would\x01",
            "have trouble understanding this stuff.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60C9")

    TalkEnd(0xFE)
    Return()

    # Function_23_5F77 end

    def Function_24_60CD(): pass

    label("Function_24_60CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_616E")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "WOO HOOOO!!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("Booming Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S(...woo...hoooo...)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0xFE,
        "Haha, there's that echo I was looking for.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_61E6")

    label("loc_616E")


    ChrTalk(
        0xFE,
        (
            "Remember, if you ever go mountain climbing,\x01",
            "you've got to do this at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...As embarrassing as it is.\x02",
    )

    CloseMessageWindow()

    label("loc_61E6")

    TalkEnd(0xFE)
    Return()

    # Function_24_60CD end

    def Function_25_61EA(): pass

    label("Function_25_61EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6418")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628A")

    ChrTalk(
        0x101,
        (
            "#0000FWe don't need to ride the bus today,\x01",
            "thanks to Sergeant Major Seeker and her car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6410")

    label("loc_628A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62D4")

    ChrTalk(
        0x102,
        "#0100FWe don't need to ride the bus today, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6410")

    label("loc_62D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6343")

    ChrTalk(
        0x103,
        (
            "#0200FGiven we can use the sergeant major's car,\x01",
            "we do not need to ride the bus today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6410")

    label("loc_6343")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63A1")

    ChrTalk(
        0x104,
        (
            "#0300FWhy ride the bus when we can\x01",
            "cruise around in Noel's sick ride?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6410")

    label("loc_63A1")


    ChrTalk(
        0x109,
        (
            "#0500FUmm... You know you don't need to ride\x01",
            "the bus, right? I can take you back to the\x01",
            "city with my car.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6410")

    TalkEnd(0xFF)
    Jump("loc_64F8")

    label("loc_6418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6450")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_64F8")

    label("loc_6450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6461")
    Call(0, 5)
    Jump("loc_64F8")

    label("loc_6461")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0000FLet's avoid using the bus today.\x02\x03",
            "It'd be better if we hike alongside the path\x01",
            "for this investigation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_64F8")

    Return()

    # Function_25_61EA end

    def Function_26_64F9(): pass

    label("Function_26_64F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_650B")
    Call(0, 35)
    Jump("loc_6549")

    label("loc_650B")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Voices can be heard from behind the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_6549")

    Return()

    # Function_26_64F9 end

    def Function_27_654A(): pass

    label("Function_27_654A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65EB")
    Sound(810, 0, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0005FThis must be the entrance to\x01",
            "Mainz Mine.\x02\x03",
            "#0003FIt's locked. I can't blame them for\x01",
            "being cautious after the wolf attacks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6634")

    label("loc_65EB")

    Sound(810, 0, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0001FIt's locked. Let's save this place\x01",
            "for some other time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6634")

    TalkEnd(0xFF)
    Return()

    # Function_27_654A end

    def Function_28_6638(): pass

    label("Function_28_6638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6663")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6663")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_6663")

    Return()

    # Function_28_6638 end

    def Function_29_6664(): pass

    label("Function_29_6664")

    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    SetMapObjFlags(0x8, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x8, 0x13)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetChrPos(0x13, -5500, -2000, 20700, 180)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x0)
    Return()

    # Function_29_6664 end

    def Function_30_66C9(): pass

    label("Function_30_66C9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, 1130, -2000, 15860, 0)
    SetChrPos(0x102, -160, -2000, 13680, 0)
    SetChrPos(0x103, 940, -2000, 13950, 0)
    SetChrPos(0x104, -70, -2000, 15410, 0)
    Call(0, 29)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    FadeToBright(1000, 0)
    OP_68(34130, -500, 46430, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(49940, 0)
    OP_68(1670, -500, 43690, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(1190, 5500, 41450, 0)
    MoveCamera(309, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(45590, 0)
    OP_68(1190, -500, 41450, 10000)
    SetCameraDistance(72340, 10000)
    Sleep(5000)
    PlaceName2(340, 200, "c_plac17", 0x0, 0)

    def lambda_67E7():
        OP_95(0xFE, 1200, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67E7)

    def lambda_6801():
        OP_95(0xFE, -100, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6801)

    def lambda_681B():
        OP_95(0xFE, 1200, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_681B)

    def lambda_6835():
        OP_95(0xFE, -100, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6835)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)
    OP_0D()
    Fade(1000)
    OP_68(440, 350, 19370, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    OP_68(440, -850, 19370, 3000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1200470V#0000F#6PA town filled with rich septium deposits...\x01",
            "So, this is Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200471V#0205F#6PIt is in a rather inaccessible\x01",
            "place, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200472V#0300F#6PYeah, I gotta agree.\x02\x03",
            "#1200473V#0300FIt reminds me of Armorica Village. Gap between\x01",
            "here and the city is nothin' to laugh about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200474V#0103F#6PYes...\x02\x03",
            "#1200475V#0100FThe mining operation looks to be\x01",
            "more-or-less fully developed.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x102, 0x10E, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#1200476V#0105F#12PHold on... What's the deal with\x01",
            "that black vehicle over there?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6ACF():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6ACF)

    def lambda_6ADC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6ADC)
    Sleep(50)

    def lambda_6AEC():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6AEC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_68(-3300, -800, 21380, 2500)
    MoveCamera(310, 19, 0, 2500)
    SetCameraDistance(17800, 2500)
    BeginChrThread(0x102, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(80)
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(120)
    BeginChrThread(0x103, 3, 0, 33)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200477V#0005F#12PIs it used for transporting septium deposits\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200478V#0301F#2PDon't you think it's a lil' too heavy duty\x01",
            "for something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200479V#0203F#12PIt appears to be a special transport vehicle\x01",
            "designed by the Empire's Reinford Company.\x02\x03",
            "#1200480V#0200FTheir latest model, on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200481V#0105F#6PIf it's that cutting-edge, it must have\x01",
            "cost a fortune.\x02\x03",
            "#1200482V#0100FPerhaps it's the town mayor's private car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200483V#0003F#12PIt's a possibility.\x02\x03",
            "#1200484V#0000FEither way, we should try visiting\x01",
            "him before anything else.\x02\x03",
            "#1200485VHopefully, he can shed some light on\x01",
            "circumstances regarding the monster\x01",
            "attack here in Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -280, -2000, 19780, 0)
    ClearChrFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x65, 1)
    OP_29(0x40, 0x1, 0x7)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_66C9 end

    def Function_31_6E71(): pass

    label("Function_31_6E71")


    def lambda_6E76():
        OP_95(0xFE, -1850, -2000, 22150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E76)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_6E71 end

    def Function_32_6E97(): pass

    label("Function_32_6E97")


    def lambda_6E9C():
        OP_95(0xFE, -3100, -2000, 20750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E9C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_6E97 end

    def Function_33_6EBD(): pass

    label("Function_33_6EBD")


    def lambda_6EC2():
        OP_95(0xFE, -1850, -2000, 20650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EC2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_33_6EBD end

    def Function_34_6EE3(): pass

    label("Function_34_6EE3")


    def lambda_6EE8():
        OP_95(0xFE, -3100, -2000, 22250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EE8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_34_6EE3 end

    def Function_35_6F09(): pass

    label("Function_35_6F09")

    EventBegin(0x0)
    Fade(1000)
    OP_68(12530, 1450, 68850, 0)
    MoveCamera(325, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18140, 0)
    SetChrPos(0x101, 12000, 250, 69500, 0)
    SetChrPos(0x102, 11700, 0, 67400, 0)
    SetChrPos(0x103, 13480, 0, 66130, 0)
    SetChrPos(0x104, 11700, 0, 66100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1200486V#0005F#5PHold on...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Voices can be heard from behind the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#1200487V#0105F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200488V#0003F#5PNot really, but it sounds like the mayor\x01",
            "is in the middle of something.\x02\x03",
            "#1200489V#0000FMaybe he has visitors?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 22250, -1420, 63410, 270)

    NpcTalk(
        0x14,
        "Young Man's Voice",
        "#1200490VOh, you folks have business with the mayor?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(14640, 1650, 65760, 2000)
    MoveCamera(325, 14, 0, 2000)

    def lambda_7161():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7161)

    def lambda_716E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_716E)

    def lambda_717B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_717B)
    Sleep(50)

    def lambda_718B():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_718B)

    def lambda_7198():
        OP_95(0xFE, 17000, 0, 63700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7198)
    WaitChrThread(0x14, 1)
    TurnDirection(0x14, 0x101, 500)
    OP_6F(0x41)

    ChrTalk(
        0x101,
        "#1200491V#0000F#5PYeah, we were looking for him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200492V#0100F#5PSo we came to the right place after\x01",
            "all. That's good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#1200493VYup, this is the place. But, y'see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200494VProbably not a good time to barge in right now.\x01",
            "Sounds like he's havin' a serious discussion\x01",
            "with someone or another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200495V#0005F#5PA discussion about what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200496VYou know how the CGF pulled their\x01",
            "forces from the area this mornin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200497VThey didn't find any clues on the beasts that attacked\x01",
            "Mainz, so we were freakin' out about what to do. As that\x01",
            "was happenin', some help showed up from the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200498V#0001F#5PHelp? Only one group comes to mind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200499V#0301F#5PThe bracers, probably.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200500VI dunno much, but I think they were coming up\x01",
            "with countermeasures against the monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#1200501VNow, I also dunno why you're here, either, but\x01",
            "I'd wait a bit before you see the mayor.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xE1, 0x1F4)
    OP_68(13760, 1650, 65630, 3000)

    def lambda_75EE():
        OP_95(0xFE, 8330, 0, 61360, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_75EE)

    def lambda_7608():

        label("loc_7608")

        TurnDirection(0x101, 0x14, 500)
        Yield()
        Jump("loc_7608")

    QueueWorkItem2(0x101, 1, lambda_7608)

    def lambda_761A():

        label("loc_761A")

        TurnDirection(0x102, 0x14, 500)
        Yield()
        Jump("loc_761A")

    QueueWorkItem2(0x102, 1, lambda_761A)

    def lambda_762C():

        label("loc_762C")

        TurnDirection(0x103, 0x14, 500)
        Yield()
        Jump("loc_762C")

    QueueWorkItem2(0x103, 1, lambda_762C)

    def lambda_763E():

        label("loc_763E")

        TurnDirection(0x104, 0x14, 500)
        Yield()
        Jump("loc_763E")

    QueueWorkItem2(0x104, 1, lambda_763E)
    WaitChrThread(0x14, 1)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#1200502V#0200F#6PWhat should we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200503V#0006F#11PHmm... If he's busy, it'd be unprofessional to\x01",
            "storm in on him now.\x02\x03",
            "#1200504V#0001FLet's gather all the information we can around\x01",
            "town and reconvene here later.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77B3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77B3)
    Sleep(100)

    def lambda_77C3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77C3)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#1200505V#0106F#6P*sigh* I think that's about all we can do\x01",
            "in this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200506V#0303F#6PNothin' likes to be clear cut in this\x01",
            "line of work, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 12000, 0, 67500, 180)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x65, 2)
    OP_29(0x40, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_35_6F09 end

    def Function_36_7894(): pass

    label("Function_36_7894")

    SetScenarioFlags(0x0, 0)
    Call(0, 38)
    Return()

    # Function_36_7894 end

    def Function_37_789B(): pass

    label("Function_37_789B")

    SetScenarioFlags(0x0, 1)
    Call(0, 38)
    Return()

    # Function_37_789B end

    def Function_38_78A2(): pass

    label("Function_38_78A2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_794E")
    OP_68(21240, 1450, 62400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_90(0x101, 21200, -600, 62700, 270)
    OP_90(0x102, 21200, -600, 63800, 270)
    OP_90(0x104, 22200, -1300, 63800, 270)
    OP_90(0x103, 22200, -1300, 62700, 270)
    Jump("loc_79C0")

    label("loc_794E")

    OP_68(6800, 1450, 57800, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7200, 0, 58500, 0)
    SetChrPos(0x102, 5800, 0, 58500, 0)
    SetChrPos(0x103, 7200, 0, 57100, 0)
    SetChrPos(0x104, 5800, 0, 57100, 0)

    label("loc_79C0")

    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 12000, 380, 71000, 180)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 12000, 380, 71000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, -4000, -2000, 20700, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    OP_68(12000, 1450, 68500, 2300)
    OP_6F(0x1)
    Sleep(300)

    NpcTalk(
        0x15,
        "Man's Voice",
        (
            "#1200507V#2S#1PGive our offer some thought, okay?\x01",
            "We'll be in touch reeeeal soon!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man's Voice",
        (
            "#1200508V#2S#11PActually, we'll come ask you about it\x01",
            "tomorrow, so we'll expect an answer then!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(11750, 1450, 66200, 4000)

    def lambda_7BBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7BBD)

    def lambda_7BCE():
        OP_95(0xFE, 12000, 0, 65000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7BCE)
    Sleep(1000)

    def lambda_7BEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7BEB)

    def lambda_7BFC():
        OP_95(0xFE, 12000, 0, 66800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7BFC)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    OP_93(0x15, 0x0, 0x1F4)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    ReplaceBGM("ed7121", "ed7302")

    ChrTalk(
        0x15,
        (
            "#1200509V#6PHeh... All it'll take is one more\x01",
            "little push from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#1200510V#11PAlmost there! I can see\x01",
            "the bonus already.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 39)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 40)
    Sleep(2000)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7E59")
    OP_68(20240, 1450, 62400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(21240, 1450, 62400, 3000)
    OP_90(0x101, 21200, -600, 62700, 270)
    OP_90(0x102, 21200, -600, 63800, 270)
    OP_90(0x104, 22200, -1300, 63800, 270)
    OP_90(0x103, 22200, -1300, 62700, 270)
    OP_6F(0x1)
    Sleep(1500)
    OP_68(17240, 1450, 62400, 4000)

    def lambda_7D92():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D92)
    Sleep(200)

    def lambda_7DAF():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DAF)
    Sleep(250)

    def lambda_7DCC():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DCC)
    Sleep(200)

    def lambda_7DE9():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7DE9)
    WaitChrThread(0x101, 1)

    def lambda_7E07():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E07)
    WaitChrThread(0x102, 1)

    def lambda_7E18():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E18)
    WaitChrThread(0x103, 1)

    def lambda_7E29():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E29)
    WaitChrThread(0x104, 1)

    def lambda_7E3A():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E3A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Jump("loc_7F81")

    label("loc_7E59")

    OP_68(6070, 1450, 54600, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -1800, 250, 53800, 90)
    SetChrPos(0x102, -3200, 250, 53800, 90)
    SetChrPos(0x103, -1800, 250, 54840, 90)
    SetChrPos(0x104, -3200, 250, 54840, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(7000)
    OP_68(2070, 1450, 54600, 3000)
    OP_6F(0x1)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_68(3070, 1450, 53600, 4000)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 41)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 41)
    Sleep(3000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    label("loc_7F81")

    OP_0D()

    ChrTalk(
        0x101,
        "#1200511V#0001F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200512V#0101F#11PRevache goons? They're the last people\x01",
            "I expected to show up in Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200513V#0301F#11PWhoa, wait a second now... Why the hell\x01",
            "were they talkin' to the mayor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200514V#0206F#11PWe assumed the bracers were going to help,\x01",
            "but the reality was much worse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200515V#0006F#11PYeah, I'd rather they had been bracers...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1200516V#0005F#11PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    Fade(500)
    OP_68(-700, -550, 21400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x15, -2100, -2000, 20200, 270)
    SetChrPos(0x16, -2100, -2000, 25200, 180)

    def lambda_81A0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_81A0)
    OP_71(0x8, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    Sleep(300)
    SetChrFlags(0x15, 0x4)

    def lambda_81D7():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_81D7)

    def lambda_81F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_81F1)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(300)
    SetChrFlags(0x16, 0x4)

    def lambda_821D():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_821D)

    def lambda_8237():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8237)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    OP_0D()
    OP_71(0x8, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x8)
    OP_71(0x8, 0x3C, 0x5A, 0x0, 0x0)
    Sound(465, 0, 100, 0)
    OP_79(0x8)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_8287():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8287)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_68(610, -550, 25820, 5000)
    SetChrPos(0x101, 1070, 0, 37010, 180)
    SetChrPos(0x102, -310, 0, 37020, 180)
    SetChrPos(0x103, 1050, 0, 38460, 180)
    SetChrPos(0x104, -300, 0, 38460, 180)

    def lambda_8333():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8333)
    Sleep(200)

    def lambda_8350():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8350)
    Sleep(250)

    def lambda_836D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_836D)
    Sleep(200)

    def lambda_838A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_838A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#1200517V#0001F#11PSo that wasn't the mayor's van, but theirs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200518V#0106F#5PRevache has got their hands on Imperial-made\x01",
            "vehicles, have they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200519V#0201F#11PThe question still stands...\x02\x03",
            "#1200520VWhat business could the mafia have with\x01",
            "a mining town like Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200521V#0306F#11PTrue. I bet they'd rather avoid workin'\x01",
            "outside of town. Not really their M.O.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#1200522V#0003F#11PAll we can do is ask the mayor about it.\x02\x03",
            "#1200523V#0001FHopefully, he can give us leads on the wolves\x01",
            "and why the mafia decided to pay him a visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetChrPos(0x0, 310, -2000, 26720, 180)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x4, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x65, 3)
    OP_29(0x40, 0x1, 0x9)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_78A2 end

    def Function_39_865F(): pass

    label("Function_39_865F")

    OP_93(0x15, 0xE1, 0x1F4)

    def lambda_866B():
        OP_95(0xFE, 7000, 0, 60000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_866B)
    WaitChrThread(0x15, 1)

    def lambda_8689():
        OP_95(0xFE, 7000, 0, 40000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8689)
    WaitChrThread(0x15, 1)
    Return()

    # Function_39_865F end

    def Function_40_86A3(): pass

    label("Function_40_86A3")

    OP_93(0x16, 0xE1, 0x1F4)

    def lambda_86AF():
        OP_95(0xFE, 7000, 0, 61800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_86AF)
    WaitChrThread(0x16, 1)

    def lambda_86CD():
        OP_95(0xFE, 7000, 0, 41800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_86CD)
    WaitChrThread(0x16, 1)
    Return()

    # Function_40_86A3 end

    def Function_41_86E7(): pass

    label("Function_41_86E7")


    def lambda_86EC():
        OP_97(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86EC)

    def lambda_8706():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8706)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_86E7 end

    def Function_42_8722(): pass

    label("Function_42_8722")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12030, 1250, 67730, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14310, 0)
    SetChrPos(0x101, 11820, 400, 71040, 270)
    SetChrPos(0x102, 11820, 400, 71040, 270)
    SetChrPos(0x103, 11820, 400, 71040, 270)
    SetChrPos(0x104, 11820, 400, 71040, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    OP_68(12030, 1250, 65730, 4000)
    BeginChrThread(0x101, 3, 0, 43)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 44)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 45)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#1200590V#0101F#5PLloyd, was it wise to promise\x01",
            "something like that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200591V#0306F#11PWe confirmed that there are two types\x01",
            "of wolves present in the case...\x02\x03",
            "#1200592V#0301FYou really think we'll be able to take down\x01",
            "the culprits by tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200593V#0004F#6PWell, we don't necessarily need to\x01",
            "exterminate them, for starters.\x02\x03",
            "#1200594V#0000FFrom the very beginning, our job was to\x01",
            "clear the fog surrounding the mysteries\x01",
            "in the CGF's report, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0x102,
        "#1200595V#0105F#5PWell, when you put it that way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200596V#0206F#11PWithout meaning to, we swapped that objective\x01",
            "to dealing with the monsters themselves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200597V#0003F#6PI have a proposal, everyone...\x02\x03",
            "#1200598V#0000FLike that white wolf implied, I think we\x01",
            "already hold all the clues to the case.\x02\x03",
            "#1200599VWhy don't we try to have one last meeting\x01",
            "and brainstorm about the entire case?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200600V#0106F#5PI think that's a good idea. If we try to piece\x01",
            "everything together, maybe we'll discover something\x01",
            "new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200601V#0300F#11PAll righty! If that's the plan, we should\x01",
            "probably catch the bus back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200602V#0004F#6PThat's not necessary. We can always\x01",
            "just stay in Mainz overnight.\x02\x03",
            "#1200603V#0000FThe inn's guest room is big enough for\x01",
            "us to hold our meeting.\x02",
        )
    )

    CloseMessageWindow()
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
        "#1200604V#0101F#5PIn other words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200605V#0205F#11PLloyd, if our first case is anything to judge by...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200606V#0302F#11PYou musta realized somethin' about the case, eh?\x01",
            "Like you did with that mess in the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200607V#0004F#6PYeah, I have. Though, I'm not 100 percent sold\x01",
            "on my theory yet.\x02\x03",
            "#1200608V#0000FIf you're willing, I'd appreciate your help in\x01",
            "sifting through all this evidence at the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200609V#0100F#5PWe're happy to help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200610V#0204F#11PWe should hurry and book a room at the inn,\x01",
            "if we are ready.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15310, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x65, 4)
    OP_29(0x40, 0x1, 0xA)
    OP_1B(0x0, 0x0, 0x3E)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_42_8722 end

    def Function_43_9072(): pass

    label("Function_43_9072")


    def lambda_9077():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9077)

    def lambda_9091():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9091)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_90AA():
        OP_95(0xFE, 11990, 0, 64780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90AA)
    WaitChrThread(0x101, 1)

    def lambda_90C8():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90C8)
    WaitChrThread(0x101, 1)
    Return()

    # Function_43_9072 end

    def Function_44_90D5(): pass

    label("Function_44_90D5")


    def lambda_90DA():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90DA)

    def lambda_90F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_90F4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_910D():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_910D)
    WaitChrThread(0xFE, 1)

    def lambda_912B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_912B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_90D5 end

    def Function_45_9138(): pass

    label("Function_45_9138")


    def lambda_913D():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_913D)

    def lambda_9157():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9157)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_9170():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9170)
    WaitChrThread(0xFE, 1)

    def lambda_918E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_918E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_9138 end

    def Function_46_919B(): pass

    label("Function_46_919B")


    def lambda_91A0():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A0)

    def lambda_91BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_91BA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_91D3():
        OP_95(0xFE, 11900, 0, 66840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91D3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_919B end

    def Function_47_91ED(): pass

    label("Function_47_91ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch31000.itc", 0x20)
    LoadChrToIndex("chr/ch31100.itc", 0x21)
    LoadChrToIndex("apl/ch50157.itc", 0x23)
    LoadChrToIndex("apl/ch50158.itc", 0x25)
    SetChrPos(0x101, 550, -2000, 18000, 0)
    SetChrPos(0x102, -350, -2000, 17300, 0)
    SetChrPos(0x103, 1450, -2000, 16700, 0)
    SetChrPos(0x104, 550, -2000, 16000, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x17, 50, -2000, 20000, 180)
    SetChrPos(0x18, 1160, -2000, 20000, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 12000, 380, 71000, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 12000, 380, 71000, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1A, -4940, -2000, 23820, 180)
    SetChrPos(0x1B, -3780, -2000, 23800, 180)
    SetChrPos(0x1C, -4940, -2000, 14000, 0)
    SetChrPos(0x1D, -3780, -2000, 14000, 0)
    SetChrPos(0x15, -4940, -2000, 15300, 0)
    SetChrPos(0x16, -3780, -2000, 15300, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, -7240, -2000, 22350, 180)
    OP_D3(0x13, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x10E, 0x10E, 0x0, 0x0)
    OP_79(0x9)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    Sound(829, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7126", 0)
    FadeToBright(1000, 0)
    OP_68(6920, 2550, 28230, 0)
    MoveCamera(318, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(36300, 0)
    OP_68(1420, 2550, 18280, 8000)
    BeginChrThread(0x15, 0, 0, 48)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x1C, 0, 0, 50)
    BeginChrThread(0x1D, 0, 0, 51)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(510, -800, 18460, 0)
    MoveCamera(317, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#1200956V#0509F#11PYou've blown me away, everyone!\x02\x03",
            "#1200957V#0502FI never would have guessed that you'd\x01",
            "single-handedly solve the entire case!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200958V#2004F#5PHonestly, I'm quite impressed.\x02\x03",
            "#1200959V#2001FNext time, though, give us a call before\x01",
            "you start a fight right outside a town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200960V#0006F#6PEr, sorry about that.\x02\x03",
            "#1200961V#0008FI'm hesitant to admit it, but the possibility that\x01",
            "the mafia were getting their intel from the CGF\x01",
            "commander crossed my mind last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200962V#2006F#5P*sigh* It pains me to hear you say that,\x01",
            "but I suppose I can't fault you for it.\x02\x03",
            "#1200963V#2001FGut feelings aside, what would you have\x01",
            "done if those white wolves didn't save you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200964V#0011F#6PWell, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200965V#0306F#6PWe probably would have been served as dinner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200966V#2001F#5PIn that sort of situation, it would have been\x01",
            "prudent to discuss the matter directly with me,\x01",
            "or with Sergei at least. There are always more\x01",
            "options on the table.\x02\x03",
            "#1200967VCrossbell faces a myriad of trials and tribulations\x01",
            "currently. That's an undeniable fact.\x02\x03",
            "#1200968VBut trying to solve them all on your own\x01",
            "is nothing more than mere selfishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200969V#0006F#6PYou may be right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200970V#0106F#6PI can't argue against that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200971V#2004F#5PWell, I think that's enough scolding\x01",
            "for one day.\x02\x03",
            "#1200972V#2002FI'm glad that you all are safe.\x02\x03",
            "#1200973VAs the Deputy Commander of the Crossbell\x01",
            "Guardian Force, I thank you for your assistance\x01",
            "in this case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200974V#0000F#6PYou're welcome, Deputy Commander.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200975V#0309F#6PHaha, would ya look at this... I never thought I'd\x01",
            "see the day when you thanked me for somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1200976V#0504F#11PBy the way, Deputy Commander.\x02\x03",
            "#1200977V#0500FWhat do we plan to do with the white wolves\x01",
            "that saved the SSS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200978V#2003F#5PHmm, I suppose our initial suspicions were\x01",
            "completely unsubstantiated.\x02\x03",
            "#1200979V#2000FIt should be fine to leave them be, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200980V#0204F#6PI would not let it worry you, Deputy Commander.\x02\x03",
            "#1200981V#0202FThey do not seem the type to cause any\x01",
            "unnecessary trouble for those around them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200982V#2002F#5POh? Is that your conclusion?\x02\x03",
            "#1200983V#2006FIn that regard, we humans were the foolish\x01",
            "ones in this string of incidents.\x02\x03",
            "#1200984VTo think that the mafia caused uproars all across\x01",
            "the state in order to test their war hounds...\x02\x03",
            "#1200985V#2001FAnd just because someone's backing them,\x01",
            "they underestimated us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200986V#0108F#6PIt's far-fetched on paper, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200987V#0000F#6PBut, considering the extent of the damage...\x02\x03",
            "#1200988V...surely there's no way they can\x01",
            "talk their way out of this, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x17)
    OP_64(0x18)

    ChrTalk(
        0x101,
        "#1200989V#0011F#6PYou're kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200990V#0101F#6PThey still have the chance to pay bail?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#1200991V#2003F#5PYes, there's a high probability they do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#1200992V#0506F#11PUp until now, we've managed to expose\x01",
            "the mafia's smuggling operation near the\x01",
            "border, but that comes at a cost.\x02\x03",
            "#1200993VEach time we catch them, they pressure\x01",
            "us and get bailed out of jail.\x02\x03",
            "#1200994V#0508FWhat's more, the smuggled goods are\x01",
            "usually brought back to them under\x01",
            "blatantly false pretenses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200995V#0007F#6PThat can't be!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1200996V#0206F#6PAn annoying, endless cycle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200997V#0301F#6PCome to think of it, Bellguard Gate was\x01",
            "facin' a similar problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200998V#0108F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1200999V#2003F#5PStill, you have to remember that not\x01",
            "everyone gives in to corruption.\x02\x03",
            "#1201000V#2001FIf every good man and woman were to\x01",
            "lose hope now, Crossbell would be in peril.\x02\x03",
            "#1201001VWith that in mind, don't forget that there are\x01",
            "people fighting against corruption as hard\x01",
            "as they possibly can.\x02\x03",
            "#1201002V#2000FPeople like yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#1201003V#0002F#6P...\x02\x03",
            "#1201004V#0004FYes, ma'am. We'll make sure\x01",
            "to never forget that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#1201005V#2002F#5PGood. I'm looking forward\x01",
            "to seeing what you can do.\x02\x03",
            "#1201006V#2004FFollow me. I can drive you back to\x01",
            "Crossbell City, if you want.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 500)
    Sleep(300)

    ChrTalk(
        0x17,
        "#1201007V#2000F#5PSeeker, prepare to head out.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)
    Sound(1479, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x18,
        "#1201008V#0502F#2PYes, ma'am!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x23)
    OP_D5(0x25)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_91ED end

    def Function_48_A67D(): pass

    label("Function_48_A67D")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_A69D():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A69D)
    Sleep(650)

    def lambda_A6BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A6BA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_48_A67D end

    def Function_49_A6CF(): pass

    label("Function_49_A6CF")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_A6EF():
        OP_97(0xFE, 0xFFFFFB78, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A6EF)
    WaitChrThread(0xFE, 1)

    def lambda_A70D():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A70D)
    Sleep(650)

    def lambda_A72A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A72A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_A6CF end

    def Function_50_A73F(): pass

    label("Function_50_A73F")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_A73F end

    def Function_51_A753(): pass

    label("Function_51_A753")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_A753 end

    def Function_52_A767(): pass

    label("Function_52_A767")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3840, 4950, 31680, 0)
    MoveCamera(329, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(54120, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    OP_68(3840, -250, 31680, 8000)
    SetChrPos(0x101, -940, -2000, 21970, 270)
    SetChrPos(0x102, 150, -2000, 22750, 270)
    SetChrPos(0x103, 890, -2000, 21090, 270)
    SetChrPos(0x104, 1790, -2000, 21770, 270)
    SetChrPos(0x109, -2690, -2000, 22000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -1260, -2000, -800, 0)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x1E, 1, 0, 53)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -1150, -2000, 6310)
    OP_9F(0x1, -5650, -2000, 15640)
    OP_9F(0x1, -5760, -2000, 21610)
    OP_9F(0x2, 0x13, 4000, 0x6)
    OP_0D()
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_65(0x2, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_68(-3410, -1050, 22410, 0)
    MoveCamera(309, 13, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19530, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_68(-1410, -1050, 22410, 3000)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    Sound(1503, 255, 100, 0)
    Sleep(300)

    ChrTalk(
        0x109,
        "#4100508V#0502F#5PAll right, we made it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100509V#0002F#12PI'm always impressed by how much\x01",
            "faster we travel with your car.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4100510V#0000F#5PLet's hurry and ask the town mayor for\x01",
            "details on the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100511V#0304F#12PSounds good, man.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#4100512V#0100F#11PIf I remember correctly, it was the\x01",
            "house in the back of town.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, -2000, 18000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0xC1, 1)
    OP_29(0x4A, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_52_A767 end

    def Function_53_ABD2(): pass

    label("Function_53_ABD2")

    Sleep(1000)
    Sound(485, 0, 90, 0)
    Return()

    # Function_53_ABD2 end

    def Function_54_ABDC(): pass

    label("Function_54_ABDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(10950, 850, 69530, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15780, 0)
    SetChrPos(0x101, 11820, 400, 71040, 270)
    SetChrPos(0x102, 11820, 400, 71040, 270)
    SetChrPos(0x103, 11820, 400, 71040, 270)
    SetChrPos(0x104, 11820, 400, 71040, 270)
    SetChrPos(0x109, 11820, 400, 71040, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    OP_68(10950, 850, 67290, 4000)
    BeginChrThread(0x101, 3, 0, 55)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 56)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 57)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 58)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 59)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4100553V#0005F#11PIt's already evening...\x02\x03",
            "#4100554V#0000FIt's probably about time we\x01",
            "head back to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100555V#0103F#11PWe still need to gather more information\x01",
            "before the day is done, so, yes, we should\x01",
            "return before it gets dark.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#4100556V#0100F#6PCould you give us a ride, Noel?\x02",
    )

    CloseMessageWindow()

    def lambda_AE8D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE8D)
    Sleep(50)

    def lambda_AE9D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AE9D)
    Sleep(50)

    def lambda_AEAD():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AEAD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x109,
        (
            "#4100557V#0509F#11PYes, of course!\x02\x03",
            "#4100558V#0502FHop in, and we'll move out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 13210, 0, 65069, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0xC1, 3)
    EventEnd(0x5)
    Return()

    # Function_54_ABDC end

    def Function_55_AF3D(): pass

    label("Function_55_AF3D")


    def lambda_AF42():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF42)

    def lambda_AF5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF5C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_AF75():
        OP_95(0xFE, 12200, 0, 64769, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF75)
    WaitChrThread(0x101, 1)
    Return()

    # Function_55_AF3D end

    def Function_56_AF8F(): pass

    label("Function_56_AF8F")


    def lambda_AF94():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF94)

    def lambda_AFAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFAE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_AFC7():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFC7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_AF8F end

    def Function_57_AFE1(): pass

    label("Function_57_AFE1")


    def lambda_AFE6():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFE6)

    def lambda_B000():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B000)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_B019():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B019)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_AFE1 end

    def Function_58_B033(): pass

    label("Function_58_B033")


    def lambda_B038():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B038)

    def lambda_B052():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B052)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_B06B():
        OP_95(0xFE, 12550, 0, 67610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B06B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_B033 end

    def Function_59_B085(): pass

    label("Function_59_B085")


    def lambda_B08A():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B08A)

    def lambda_B0A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B0A4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_B0BD():
        OP_95(0xFE, 11220, 0, 67760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0BD)
    WaitChrThread(0xFE, 1)

    def lambda_B0DB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0DB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_B085 end

    def Function_60_B0E8(): pass

    label("Function_60_B0E8")

    EventBegin(0x1)
    Sound(1499, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ride in Guardian Force car?\x02",
        )
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B179")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City\x01",      # 0
            "Leave\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B174")
    Call(0, 61)
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_B174")

    Jump("loc_B186")

    label("loc_B179")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_B186")

    EventEnd(0x5)
    Return()

    # Function_60_B0E8 end

    def Function_61_B189(): pass

    label("Function_61_B189")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(470, 0, 70, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(-290, -2150, 10870, 0)
    MoveCamera(341, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20940, 0)
    OP_68(-290, 750, 10870, 4000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, 180, -2000, 16790, 180)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sound(486, 0, 100, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_B29E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B29E)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    OP_6F(0x1)
    Return()

    # Function_61_B189 end

    def Function_62_B2C4(): pass

    label("Function_62_B2C4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B382")

    ChrTalk(
        0x101,
        (
            "#0003FIt's already getting dark. It wouldn't be\x01",
            "a smart move to walk on the highway now.\x02\x03",
            "#0001FBesides, we still need to sort through all\x01",
            "our evidence back at the inn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3FE")

    ChrTalk(
        0x101,
        (
            "#0000FThis way leads to the highway.\x02\x03",
            "#0003FIt'd be a waste to leave without even\x01",
            "speaking to the mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B484")

    ChrTalk(
        0x101,
        (
            "#0000FThis way leads to the highway.\x02\x03",
            "#0004FSince Sergeant Major Seeker is with us,\x01",
            "we can have her drive us back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B484")

    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_62_B2C4 end

    SaveToFile()

Try(main)
