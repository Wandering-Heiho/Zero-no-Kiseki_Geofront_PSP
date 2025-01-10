from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3400.bin",                # FileName
        "e3400",                    # MapName
        "e3400",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 1250, 22670, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3400",                  # 0
        "Sun Princess",           # 1
        "Moon Princess",          # 2
        "Reflected Sun Glare",    # 3
        "Reflected Moon Glare",   # 4
        "Star Guardsman",         # 5
        "Wandering Prince",       # 6
        "Head Priestess",         # 7
        "Sybil",                  # 8
        "Homeless Boy",           # 9
        "Ra's Maid",              # 10
        "Ra's Maid",              # 11
        "Ra's Soldier",           # 12
        "Ra's Soldier",           # 13
        "Ra's Soldier",           # 14
        "Ra's Soldier",           # 15
        "Reflected Guardsman",    # 16
        "Objet d'art",            # 17
        "Objet d'art",            # 18
        "Manager Balsamo",        # 19
        "Detective Emma",         # 20
        "Detective Dudley",       # 21
        "First Division Detective",# 22
        "First Division Detective",# 23
        "Mayor MacDowell",        # 24
        "Secretary Ernest",       # 25
        "Cecile",                 # 26
        "SE制御",                 # 27
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_5FC",          # 00, 0
        "Function_1_779",          # 01, 1
        "Function_2_77A",          # 02, 2
        "Function_3_86F",          # 03, 3
        "Function_4_893",          # 04, 4
        "Function_5_938",          # 05, 5
        "Function_6_9C2",          # 06, 6
        "Function_7_9EF",          # 07, 7
        "Function_8_A1C",          # 08, 8
        "Function_9_A33",          # 09, 9
        "Function_10_A4A",         # 0A, 10
        "Function_11_A53",         # 0B, 11
        "Function_12_A5C",         # 0C, 12
        "Function_13_A65",         # 0D, 13
        "Function_14_A6E",         # 0E, 14
        "Function_15_A9B",         # 0F, 15
        "Function_16_AC8",         # 10, 16
        "Function_17_ADF",         # 11, 17
        "Function_18_AF6",         # 12, 18
        "Function_19_B15",         # 13, 19
        "Function_20_B34",         # 14, 20
        "Function_21_B53",         # 15, 21
        "Function_22_B72",         # 16, 22
        "Function_23_C34",         # 17, 23
        "Function_24_D16",         # 18, 24
        "Function_25_E7B",         # 19, 25
        "Function_26_148C",        # 1A, 26
        "Function_27_18E9",        # 1B, 27
        "Function_28_1934",        # 1C, 28
        "Function_29_19B6",        # 1D, 29
        "Function_30_1A38",        # 1E, 30
        "Function_31_1A89",        # 1F, 31
        "Function_32_1ADA",        # 20, 32
        "Function_33_1B2B",        # 21, 33
        "Function_34_1B96",        # 22, 34
        "Function_35_1BDF",        # 23, 35
        "Function_36_1C28",        # 24, 36
        "Function_37_1C7D",        # 25, 37
        "Function_38_2727",        # 26, 38
        "Function_39_275B",        # 27, 39
        "Function_40_2A04",        # 28, 40
        "Function_41_2BC1",        # 29, 41
        "Function_42_2ED7",        # 2A, 42
        "Function_43_2F22",        # 2B, 43
        "Function_44_2FF2",        # 2C, 44
        "Function_45_31BE",        # 2D, 45
        "Function_46_346F",        # 2E, 46
        "Function_47_34A8",        # 2F, 47
        "Function_48_34E1",        # 30, 48
        "Function_49_3CF1",        # 31, 49
        "Function_50_3D28",        # 32, 50
        "Function_51_3DB2",        # 33, 51
        "Function_52_3FAD",        # 34, 52
        "Function_53_4268",        # 35, 53
        "Function_54_439F",        # 36, 54
        "Function_55_461F",        # 37, 55
        "Function_56_4868",        # 38, 56
        "Function_57_4B19",        # 39, 57
        "Function_58_4BB2",        # 3A, 58
        "Function_59_4C4B",        # 3B, 59
        "Function_60_4C96",        # 3C, 60
        "Function_61_5426",        # 3D, 61
        "Function_62_5451",        # 3E, 62
        "Function_63_55AF",        # 3F, 63
        "Function_64_570D",        # 40, 64
        "Function_65_57DD",        # 41, 65
        "Function_66_58AD",        # 42, 66
        "Function_67_597D",        # 43, 67
        "Function_68_5A4D",        # 44, 68
        "Function_69_5A98",        # 45, 69
        "Function_70_5B1D",        # 46, 70
        "Function_71_5BE6",        # 47, 71
        "Function_72_5E46",        # 48, 72
        "Function_73_60BE",        # 49, 73
        "Function_74_6739",        # 4A, 74
        "Function_75_6AF8",        # 4B, 75
        "Function_76_6B21",        # 4C, 76
        "Function_77_7ACE",        # 4D, 77
        "Function_78_7B23",        # 4E, 78
        "Function_79_7B37",        # 4F, 79
        "Function_80_7B82",        # 50, 80
        "Function_81_7C72",        # 51, 81
        "Function_82_7CBD",        # 52, 82
        "Function_83_7EE2",        # 53, 83
        "Function_84_7EFC",        # 54, 84
        "Function_85_811D",        # 55, 85
        "Function_86_8137",        # 56, 86
        "Function_87_816E",        # 57, 87
        "Function_88_829B",        # 58, 88
        "Function_89_82EE",        # 59, 89
        "Function_90_8341",        # 5A, 90
        "Function_91_83E2",        # 5B, 91
        "Function_92_8401",        # 5C, 92
        "Function_93_8420",        # 5D, 93
        "Function_94_84FA",        # 5E, 94
        "Function_95_85D8",        # 5F, 95
        "Function_96_9555",        # 60, 96
        "Function_97_95FF",        # 61, 97
        "Function_98_97F6",        # 62, 98
        "Function_99_9DC1",        # 63, 99
        "Function_100_9F40",       # 64, 100
        "Function_101_A696",       # 65, 101
        "Function_102_A6F7",       # 66, 102
        "Function_103_AAED",       # 67, 103
        "Function_104_AB3A",       # 68, 104
        "Function_105_AB7D",       # 69, 105
        "Function_106_ABEF",       # 6A, 106
        "Function_107_ADD3",       # 6B, 107
        "Function_108_AE45",       # 6C, 108
        "Function_109_B0FD",       # 6D, 109
        "Function_110_B16F",       # 6E, 110
        "Function_111_B353",       # 6F, 111
        "Function_112_B6B3",       # 70, 112
        "Function_113_BA32",       # 71, 113
        "Function_114_BDD2",       # 72, 114
        "Function_115_BFCC",       # 73, 115
        "Function_116_C1D8",       # 74, 116
        "Function_117_C45E",       # 75, 117
        "Function_118_C57C",       # 76, 118
        "Function_119_C5B8",       # 77, 119
        "Function_120_C5D4",       # 78, 120
        "Function_121_C646",       # 79, 121
        "Function_122_D82E",       # 7A, 122
        "Function_123_D848",       # 7B, 123
        "Function_124_D8ED",       # 7C, 124
        "Function_125_D996",       # 7D, 125
        "Function_126_E21C",       # 7E, 126
    ))


    def Function_0_5FC(): pass

    label("Function_0_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_610")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 102)
    Jump("loc_778")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_624")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 37)
    Jump("loc_778")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_638")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 106)
    Jump("loc_778")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_64C")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 108)
    Jump("loc_778")

    label("loc_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_660")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 110)
    Jump("loc_778")

    label("loc_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_674")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 111)
    Jump("loc_778")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_688")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 112)
    Jump("loc_778")

    label("loc_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 0)), scpexpr(EXPR_END)), "loc_69C")
    ClearScenarioFlags(0x5D, 0)
    Event(0, 113)
    Jump("loc_778")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 1)), scpexpr(EXPR_END)), "loc_6B0")
    ClearScenarioFlags(0x5D, 1)
    Event(0, 114)
    Jump("loc_778")

    label("loc_6B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 2)), scpexpr(EXPR_END)), "loc_6C4")
    ClearScenarioFlags(0x5D, 2)
    Event(0, 115)
    Jump("loc_778")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 3)), scpexpr(EXPR_END)), "loc_6D8")
    ClearScenarioFlags(0x5D, 3)
    Event(0, 116)
    Jump("loc_778")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 4)), scpexpr(EXPR_END)), "loc_6EC")
    ClearScenarioFlags(0x5D, 4)
    Event(0, 48)
    Jump("loc_778")

    label("loc_6EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 5)), scpexpr(EXPR_END)), "loc_700")
    ClearScenarioFlags(0x5D, 5)
    Event(0, 60)
    Jump("loc_778")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 6)), scpexpr(EXPR_END)), "loc_714")
    ClearScenarioFlags(0x5D, 6)
    Event(0, 76)
    Jump("loc_778")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5D, 7)), scpexpr(EXPR_END)), "loc_728")
    ClearScenarioFlags(0x5D, 7)
    Event(0, 100)
    Jump("loc_778")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_73C")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 121)
    Jump("loc_778")

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 1)), scpexpr(EXPR_END)), "loc_750")
    ClearScenarioFlags(0x5E, 1)
    Event(0, 95)
    Jump("loc_778")

    label("loc_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 2)), scpexpr(EXPR_END)), "loc_764")
    ClearScenarioFlags(0x5E, 2)
    Event(0, 125)
    Jump("loc_778")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_775")
    Event(0, 3)
    Jump("loc_778")

    label("loc_775")

    Event(0, 2)

    label("loc_778")

    Return()

    # Function_0_5FC end

    def Function_1_779(): pass

    label("Function_1_779")

    Return()

    # Function_1_779 end

    def Function_2_77A(): pass

    label("Function_2_77A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x80)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Act 1\x01",             # 0
            "Act 2\x01",             # 1
            "Act 3\x01",             # 2
            "Act 4\x01",             # 3
            "Finale\x01",            # 4
            "Intermission\x01",      # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7FD"),
        (1, "loc_80E"),
        (2, "loc_81F"),
        (3, "loc_830"),
        (4, "loc_841"),
        (5, "loc_852"),
        (SWITCH_DEFAULT, "loc_863"),
    )


    label("loc_7FD")

    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_80E")

    SetScenarioFlags(0x5D, 4)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_81F")

    SetScenarioFlags(0x5D, 5)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_830")

    SetScenarioFlags(0x5D, 6)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_841")

    SetScenarioFlags(0x5E, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_852")

    SetScenarioFlags(0x5D, 7)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_863")

    label("loc_863")

    FadeToDark(300, 0, -1)
    OP_0D()
    Return()

    # Function_2_77A end

    def Function_3_86F(): pass

    label("Function_3_86F")

    Call(0, 37)
    Call(0, 48)
    Call(0, 60)
    Call(0, 76)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    Call(0, 100)
    Return()

    # Function_3_86F end

    def Function_4_893(): pass

    label("Function_4_893")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x4CE78, 0x0, 0x0)

    label("loc_8C5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_937")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_8C5")

    label("loc_937")

    Return()

    # Function_4_893 end

    def Function_5_938(): pass

    label("Function_5_938")

    ClearChrFlags(0xFE, 0x1)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xFE, 0x41EB0, 0x57E40, 0x0, 0x0)

    label("loc_96A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C1")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IDIV), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_96A")

    label("loc_9C1")

    Return()

    # Function_5_938 end

    def Function_6_9C2(): pass

    label("Function_6_9C2")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_6_9C2 end

    def Function_7_9EF(): pass

    label("Function_7_9EF")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_7_9EF end

    def Function_8_A1C(): pass

    label("Function_8_A1C")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_A1C end

    def Function_9_A33(): pass

    label("Function_9_A33")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_9_A33 end

    def Function_10_A4A(): pass

    label("Function_10_A4A")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_A4A end

    def Function_11_A53(): pass

    label("Function_11_A53")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_11_A53 end

    def Function_12_A5C(): pass

    label("Function_12_A5C")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_A5C end

    def Function_13_A65(): pass

    label("Function_13_A65")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_13_A65 end

    def Function_14_A6E(): pass

    label("Function_14_A6E")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_14_A6E end

    def Function_15_A9B(): pass

    label("Function_15_A9B")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_15_A9B end

    def Function_16_AC8(): pass

    label("Function_16_AC8")

    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_AC8 end

    def Function_17_ADF(): pass

    label("Function_17_ADF")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Sleep(33)
    SetChrSubChip(0xFE, 0x1)
    Sleep(33)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_17_ADF end

    def Function_18_AF6(): pass

    label("Function_18_AF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B14")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_18_AF6")

    label("loc_B14")

    Return()

    # Function_18_AF6 end

    def Function_19_B15(): pass

    label("Function_19_B15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B33")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_19_B15")

    label("loc_B33")

    Return()

    # Function_19_B15 end

    def Function_20_B34(): pass

    label("Function_20_B34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B52")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_20_B34")

    label("loc_B52")

    Return()

    # Function_20_B34 end

    def Function_21_B53(): pass

    label("Function_21_B53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B71")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(66)
    Jump("Function_21_B53")

    label("loc_B71")

    Return()

    # Function_21_B53 end

    def Function_22_B72(): pass

    label("Function_22_B72")

    FadeToBright(500, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 1300, 25500, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrPos(0x8, -3000, 1250, 26000, 90)
    OP_96(0x8, 0xFFFFF704, 0x4E2, 0x6590, 0x1770, 0x0)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    FadeToDark(1500, 0, -1)
    OP_9D(0x8, 0x8FC, 0x4E2, 0x6590, 0x5DC, 0x2BC)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    OP_96(0x8, 0x1388, 0x4E2, 0x6590, 0x1770, 0x0)
    Return()

    # Function_22_B72 end

    def Function_23_C34(): pass

    label("Function_23_C34")

    Fade(500)
    FadeToBright(0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 1300, 25500, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x11, 0x0)
    SetChrPos(0x8, 3000, 1250, 26000, 270)
    OP_96(0x8, 0x8FC, 0x4E2, 0x6590, 0x1770, 0x0)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    BeginChrThread(0x8, 3, 0, 18)
    FadeToDark(2000, 0, -1)
    OP_9D(0x8, 0xFFFFF704, 0x4E2, 0x6590, 0x5DC, 0x2BC)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    OP_96(0x8, 0xFFFFEC78, 0x4E2, 0x6590, 0x1770, 0x0)
    Return()

    # Function_23_C34 end

    def Function_24_D16(): pass

    label("Function_24_D16")

    BeginChrThread(0xA, 3, 0, 4)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1500, 0)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x11, 0x1E, 0x5DC)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xFA0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x1388, 0xDAC)
    OP_C9(0x0, 0x1, 0x3E8, 0x44C, 0xDAC)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    SetChrPos(0x8, 3000, 1250, 26000, 270)
    OP_9E(0x8, 0x0, 0x636A, 0x2BF20, 0x1770, 0x0)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0x15F90, 0x1388, 0x0)
    BeginChrThread(0x8, 3, 0, 19)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0xAFC8, 0xBB8, 0x0)
    OP_9E(0x8, 0xFFFFFA24, 0x636A, 0xAFC8, 0x5DC, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x87, 0x12C)
    Return()

    # Function_24_D16 end

    def Function_25_E7B(): pass

    label("Function_25_E7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_148B")
    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x101, 1, 0, 28)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 15000, 25500, 0, 180, 0, 830, 1500, 830, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_FB5():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FB5)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_FF7():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_FF7)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_1036():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1036)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_104C():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_104C)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_108B():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_108B)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_10C7():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_10C7)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_1130():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_1130)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0xBB8, 0x9C4)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    OP_9D(0x8, 0xA, 0x4E2, 0x636A, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_1269():
        OP_9E(0x8, 0x0, 0x5DC0, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1269)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_12AB():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_12AB)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_12EA():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_12EA)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_1300():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1300)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_133F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_133F)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_137B():
        OP_9E(0x8, 0x0, 0x636A, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_137B)
    Sleep(33)
    BeginChrThread(0x8, 1, 0, 27)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0x0, 0x4E2, 0x639C, 0x7D0, 0x7D0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x101, 0x1)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(10000)
    Jump("Function_25_E7B")

    label("loc_148B")

    Return()

    # Function_25_E7B end

    def Function_26_148C(): pass

    label("Function_26_148C")

    BeginChrThread(0x101, 1, 0, 29)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    SetChrPos(0x8, 0, 1250, 25450, 140)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9E(0x8, 0x0, 0x5FB4, 0x2BF20, 0xD48, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x2BF20, 0xD48, 0x0)
    OP_9E(0x8, 0x0, 0x5DC0, 0x2BF20, 0xD48, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(800)

    def lambda_15EB():
        OP_93(0x8, 0x12C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_15EB)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    BeginChrThread(0x8, 1, 0, 27)

    def lambda_160C():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_160C)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)

    def lambda_1657():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1657)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)

    def lambda_16B6():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_16B6)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(520)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x9C4, 0x960)
    EndChrThread(0x8, 0x3)

    def lambda_171B():
        OP_9E(0x8, 0x0, 0x636A, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_171B)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    Sleep(500)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x1)
    Sleep(900)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 1, 0, 27)
    BeginChrThread(0x8, 3, 0, 19)
    OP_9E(0x8, 0x0, 0x5DC0, 0x2BF20, 0x1194, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x2BF20, 0x1194, 0x0)
    OP_9E(0x8, 0x0, 0x5FB4, 0x2BF20, 0x1194, 0x0)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(2550)

    def lambda_17BE():
        OP_93(0xFE, 0x73, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_17BE)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1200, 25600, 0, 0, 0, 510, 1000, 510, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1300, 25600, 180, 0, 0, 570, 700, 570, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    EndChrThread(0x8, 0x1)
    Return()

    # Function_26_148C end

    def Function_27_18E9(): pass

    label("Function_27_18E9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1933")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_27_18E9")

    label("loc_1933")

    Return()

    # Function_27_18E9 end

    def Function_28_1934(): pass

    label("Function_28_1934")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B5")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1951)
    Jump("Function_28_1934")

    label("loc_19B5")

    Return()

    # Function_28_1934 end

    def Function_29_19B6(): pass

    label("Function_29_19B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A37")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4230, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4430, 3300, 19500, 0, 90, 0, 300, 600, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_29_19B6")

    label("loc_1A37")

    Return()

    # Function_29_19B6 end

    def Function_30_1A38(): pass

    label("Function_30_1A38")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A88")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A42")

    label("loc_1A88")

    Return()

    # Function_30_1A38 end

    def Function_31_1A89(): pass

    label("Function_31_1A89")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1A93")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AD9")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1A93")

    label("loc_1AD9")

    Return()

    # Function_31_1A89 end

    def Function_32_1ADA(): pass

    label("Function_32_1ADA")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_1AE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B2A")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x2), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_1AE4")

    label("loc_1B2A")

    Return()

    # Function_32_1ADA end

    def Function_33_1B2B(): pass

    label("Function_33_1B2B")

    OP_70(0x0, 0x1E)
    OP_71(0x0, 0x1, 0x3C, 0x0, 0x8)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    Sleep(1000)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    BeginChrThread(0xE, 0, 0, 34)
    BeginChrThread(0x11, 0, 0, 35)
    BeginChrThread(0x12, 0, 0, 36)
    OP_95(0xFE, 0, 1520, 29550, 1000, 0x0)

    def lambda_1B88():

        label("loc_1B88")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1B88")

    QueueWorkItem2(0xFE, 2, lambda_1B88)
    Return()

    # Function_33_1B2B end

    def Function_34_1B96(): pass

    label("Function_34_1B96")

    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, 800, 1910, 30140, 1000, 0x0)

    def lambda_1BD1():

        label("loc_1BD1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1BD1")

    QueueWorkItem2(0xFE, 2, lambda_1BD1)
    Return()

    # Function_34_1B96 end

    def Function_35_1BDF(): pass

    label("Function_35_1BDF")

    Sleep(3000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -970, 2200, 30570, 1000, 0x0)

    def lambda_1C1A():

        label("loc_1C1A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C1A")

    QueueWorkItem2(0xFE, 2, lambda_1C1A)
    Return()

    # Function_35_1BDF end

    def Function_36_1C28(): pass

    label("Function_36_1C28")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_95(0xFE, 0, 2430, 30920, 1000, 0x0)
    OP_95(0xFE, -180, 2190, 30560, 1000, 0x0)

    def lambda_1C63():

        label("loc_1C63")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1C63")

    QueueWorkItem2(0xFE, 2, lambda_1C63)
    OP_71(0x0, 0x3C, 0x0, 0x0, 0x8)
    Return()

    # Function_36_1C28 end

    def Function_37_1C7D(): pass

    label("Function_37_1C7D")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x101, 10, 1250, 30450, 140)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0xC, 0, 2590, 31870, 180)
    SetChrPos(0xE, 0, 2590, 31870, 180)
    SetChrPos(0x11, 0, 2590, 31870, 180)
    SetChrPos(0x12, 0, 2590, 31870, 180)
    OP_A7(0xC, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0xE, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x12, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrPos(0x8, 10, 1250, 25450, 140)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x100)
    SetChrFlags(0xA, 0x800)
    SetChrPos(0xA, 10, 1250, 25450, 230)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x80, 0x0)
    OP_D3(0xA, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xA, 3, 0, 5)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 15, 0, 0)
    OP_6E(1140, 0)
    SetCameraDistance(26500, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    LoadEffect(0x2, "event\\ev290_01.eff")
    LoadEffect(0x6, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x0, "event\\ev290_05.eff")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0x80, 0x80, 0x80, 0x0, 0x0)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    BeginChrThread(0x22, 0, 0, 103)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sound(871, 0, 100, 0)
    Sleep(3000)
    EndChrThread(0x22, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201423V\x07\x0D",
            "Everyone, we apologize for the delay.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201424V\x07\x0D",
            "The curtain will now rise for Arc en Ciel's\x01",
            "breathtaking new production...\x01",
            "'Golden Sun, Silver Moon.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201425V\x07\x0D",
            "Please, enjoy the show.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x22, 0, 0, 104)
    Sound(870, 0, 100, 0)
    OP_7D(0x0, 0x0, 0x0, 0x0, 0x7D0)
    Sleep(5000)
    OP_68(-20, 2900, 25450, 0)
    MoveCamera(1, 20, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(14500, 0)
    SetMapObjFlags(0x5, 0x4)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201426V\x07\x05",
            "The Land of Ra: an ancient kingdom that\x01",
            "prospered under the blessing and love of\x01",
            "the Divine Goddess.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201427V\x07\x05",
            "Ever since the birth of Ra, the decision of who\x01",
            "was to rule the country was held in the hands\x01",
            "of soaring dancers known as princesses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201428V\x07\x05",
            "These princesses, entrusted with the will of the\x01",
            "Goddess, brought to light the true, righteous ruler\x01",
            "of Ra by competing at the Star Sanctuary...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201429V\x07\x05",
            "However, ulterior motives lie in wait, leading\x01",
            "influential figures to support different princesses,\x01",
            "treating the holy ceremony as a trivial game.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201430V\x07\x05",
            "At that time, the Sun Princess, renowned as\x01",
            "the greatest dancer of their era, arrived at the\x01",
            "Star Sanctuary.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EndChrThread(0x22, 0x0)
    OP_E5()
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x11, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFE2B40, 0xFFFB6C20, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0xAF0, 0x0)
    Sleep(1000)
    PlayBGM("ed7500", 1)
    Sleep(4000)
    Sleep(450)
    BeginChrThread(0x101, 0, 0, 22)
    Sleep(550)
    Sleep(5000)
    BeginChrThread(0x101, 0, 0, 23)
    Sleep(150)
    Sleep(850)
    Sleep(4000)
    Sleep(1000)
    Sleep(200)
    Fade(100)
    BeginChrThread(0x101, 0, 0, 24)
    Sleep(800)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(4000)
    Sleep(300)
    Fade(150)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    FadeToBright(500, 0)
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x1F4)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x1F4)
    OP_11(0x0, 0x0, 0x0, 0x1E, 0x64, 0x1388)
    Sleep(150)
    BeginChrThread(0x101, 3, 0, 25)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(130, 3700, 25170, 10000)
    MoveCamera(1, 7, 0, 30000)
    OP_6E(760, 10000)
    SetCameraDistance(16000, 20000)
    BeginChrThread(0x22, 1, 0, 38)
    Sleep(350)
    Sleep(5000)
    Sleep(10000)
    Sleep(10000)
    Sleep(6000)
    BeginChrThread(0x101, 3, 0, 26)
    BeginChrThread(0xC, 0, 0, 33)
    OP_68(-50, 2900, 25220, 10000)
    MoveCamera(1, 18, 0, 10000)
    OP_6E(760, 10000)
    SetCameraDistance(16000, 10000)
    Sleep(4000)
    Sleep(10000)
    Sleep(3000)
    FadeToDark(3000, 0, -1)
    Sleep(100)

    def lambda_2603():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2603)
    Sleep(500)

    def lambda_2620():
        OP_96(0xFE, 0x528, 0x4E2, 0x6540, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2620)
    Sleep(400)

    def lambda_263D():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_263D)
    Sleep(500)

    def lambda_265A():
        OP_96(0xFE, 0xE6, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_265A)
    OP_0D()
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    OP_E6()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_2708")
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    EndChrThread(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_2708")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x211), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x32, 0x64)
    OP_24(0x369)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_1C7D end

    def Function_38_2727(): pass

    label("Function_38_2727")

    Sleep(700)
    Sound(873, 2, 100, 0)
    Sound(872, 0, 100, 0)
    Sleep(15500)
    Sound(874, 0, 100, 0)
    Sleep(5000)
    Sleep(10000)
    Sound(872, 0, 100, 0)
    Sleep(18000)
    OP_24(0x369)
    Sound(872, 0, 100, 0)
    Sleep(2000)
    Return()

    # Function_38_2727 end

    def Function_39_275B(): pass

    label("Function_39_275B")

    OP_68(10, 2900, 23030, 10000)
    MoveCamera(0, 19, 0, 10000)
    OP_6E(570, 10000)
    SetCameraDistance(19500, 10000)
    SetChrPos(0x9, 0, 9500, 23220, 270)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0xFF, 0x0)

    def lambda_27B6():
        OP_96(0x9, 0x0, 0x4E2, 0x5AB4, 0x44C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_27B6)
    Sleep(3000)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0xBB8)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0xBB8)
    OP_7D(0x8C, 0x8C, 0xFF, 0x0, 0xBB8)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 1, 0, 43)
    Sleep(1500)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -2110, 1250, 20950, 4500, 0x0)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_283E():
        OP_9E(0x9, 0x0, 0x5AB4, 0xFFFEA070, 0x898, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_283E)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x578, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x2BC)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_28C7():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_28C7)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFF9FC, 0x4E2, 0x5E38, 0xBB8, 0x4B0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2907():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2907)
    OP_9D(0x9, 0xFFFFF3C6, 0x4E2, 0x62F2, 0x3E8, 0x6A4)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)

    def lambda_2936():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2936)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA74, 0x4E2, 0x6496, 0x7D0, 0xA28)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x58C, 0x4E2, 0x6496, 0x7D0, 0xA28)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xF28, 0x4E2, 0x6496, 0x7D0, 0xA28)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xF28, 0x55F0, 0xFFFEA070, 0xBB8, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(1800)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_39_275B end

    def Function_40_2A04(): pass

    label("Function_40_2A04")

    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_96(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0x5DC, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_2A31():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A31)
    Sleep(1000)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, -2300, 1250, 23490, 4000, 0x0)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2A69():
        OP_9D(0x9, 0x974, 0x4E2, 0x5BC2, 0xDAC, 0x44C)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2A69)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_2A93():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A93)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x1310, 0x4E2, 0x5BCC, 0x5DC, 0x7D0)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x5A, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)

    def lambda_2AE3():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2AE3)
    Sleep(800)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, 1420, 1250, 23490, 4500, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_2B21():
        OP_9D(0x9, 0xFFFFF894, 0x4E2, 0x5BC2, 0x7D0, 0xB54)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B21)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 2, 0, 46)

    def lambda_2B48():
        OP_9D(0x9, 0xFFFFECF0, 0x4E2, 0x5BC2, 0xDAC, 0x2BC)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B48)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 0)

    def lambda_2B78():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2B78)
    Sleep(800)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 21)
    OP_9E(0x9, 0xFFFFF0D8, 0x4C2C, 0x15F90, 0x7D0, 0x0)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x1)

    def lambda_2BB1():
        OP_93(0x9, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2BB1)
    Sleep(1500)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_40_2A04 end

    def Function_41_2BC1(): pass

    label("Function_41_2BC1")

    OP_68(10, 3500, 23030, 10000)
    MoveCamera(0, 7, 0, 10000)
    OP_6E(580, 10000)
    SetCameraDistance(19500, 10000)

    def lambda_2BF4():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2BF4)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xA, 0x4E2, 0x48E4, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xBB8)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 18)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0x7D0, 0xBB8)

    def lambda_2C64():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2C64)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x587A, 0xDAC, 0x640)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x5DE8, 0x7D0, 0xC1C)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x6446, 0x7D0, 0xC1C)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x5DE8, 0x7D0, 0xC80)

    def lambda_2CF1():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2CF1)
    BeginChrThread(0x9, 2, 0, 11)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x587A, 0x7D0, 0xC80)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 7)
    OP_9D(0x9, 0x5DC, 0x4E2, 0x50BE, 0xDAC, 0x514)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFFA24, 0x4E2, 0x4E84, 0x7D0, 0xC80)

    def lambda_2D65():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2D65)
    BeginChrThread(0x9, 2, 0, 10)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xA, 0x4E2, 0x48E4, 0x7D0, 0xC80)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(733)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x1F)
    OP_95(0x9, 10, 1250, 23320, 1600, 0x0)
    OP_68(40, 7920, 29870, 2000)
    MoveCamera(0, -12, 0, 2000)
    OP_6E(800, 3000)
    SetCameraDistance(13500, 3000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 7)

    def lambda_2E08():
        OP_9D(0x9, 0x1E, 0x187E, 0x753A, 0x1D4C, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2E08)
    Sleep(1000)

    def lambda_2E28():
        OP_93(0x9, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2E28)
    OP_A7(0x9, 0x50, 0x50, 0x50, 0xFF, 0x12C)
    WaitChrThread(0x9, 0)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    Sleep(1700)
    BeginChrThread(0x9, 2, 0, 9)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_2E5F():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E5F)
    OP_68(100, 4000, 25480, 8000)
    MoveCamera(0, 7, 0, 8000)
    OP_6E(780, 8000)
    SetCameraDistance(19000, 8000)
    BeginChrThread(0x9, 0, 0, 42)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, -3580, 6000, 21170)
    OP_9F(0x1, 3580, 6000, 21170)
    OP_9F(0x1, 100, 3500, 25480)
    OP_9F(0x2, 0x9, 1700, 0x0)
    Return()

    # Function_41_2BC1 end

    def Function_42_2ED7(): pass

    label("Function_42_2ED7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F21")
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, -300, 0, 0, 180, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_42_2ED7")

    label("loc_2F21")

    Return()

    # Function_42_2ED7 end

    def Function_43_2F22(): pass

    label("Function_43_2F22")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FF1")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FCE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FCE")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_2FCE")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_43_2F22")

    label("loc_2FF1")

    Return()

    # Function_43_2F22 end

    def Function_44_2FF2(): pass

    label("Function_44_2FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31BD")
    Sleep(2166)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Jump("Function_44_2FF2")

    label("loc_31BD")

    Return()

    # Function_44_2FF2 end

    def Function_45_31BE(): pass

    label("Function_45_31BE")

    Sleep(530)

    label("loc_31C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_346E")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -5920, 1700, 21450, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -5920, 1000, 21450, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1700, 27650, 0, 0, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -6690, 1000, 27650, 0, 180, 0, 700, 900, 700, 0xFF, 0, 0, 0, 0)
    Sleep(722)
    Jump("loc_31C1")

    label("loc_346E")

    Return()

    # Function_45_31BE end

    def Function_46_346F(): pass

    label("Function_46_346F")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0x57E40, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_46_346F end

    def Function_47_34A8(): pass

    label("Function_47_34A8")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_D3(0xFE, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D3(0xFE, 0x0, 0x0, 0xFFFA81C0, 0x3E8)
    SetChrFlags(0xFE, 0x100)
    Return()

    # Function_47_34A8 end

    def Function_48_34E1(): pass

    label("Function_48_34E1")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50265.itc", 0x1E)
    LoadChrToIndex("apl/ch50266.itc", 0x1F)
    LoadChrToIndex("apl/ch50267.itc", 0x20)
    LoadChrToIndex("apl/ch50268.itc", 0x21)
    LoadChrToIndex("apl/ch50269.itc", 0x22)
    LoadChrToIndex("apl/ch50270.itc", 0x23)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch37100.itc", 0x39)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0xD, 0, 2200, 29540, 180)
    SetChrPos(0xF, 1100, 1800, 28360, 180)
    SetChrPos(0x13, -2170, 1800, 30000, 180)
    SetChrPos(0x14, 2170, 1800, 30000, 180)
    SetChrPos(0x15, -6200, 1250, 24300, 135)
    SetChrPos(0x16, 6200, 1250, 24300, 225)
    OP_A7(0xD, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0xF, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x13, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x14, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x15, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    OP_A7(0x16, 0xA0, 0xA0, 0xA0, 0xFF, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 10, 1250, 25450, 360)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x100)
    SetChrPos(0xB, 10, 1250, 25450, 230)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xB, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xB, 3, 0, 30)
    OP_68(10, 3200, 25450, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(1020, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    OP_7D(0x0, 0x0, 0x0, 0x0, 0x0)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(875)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201496V\x07\x0D",
            "Thus, the Sun Princess, supported by the\x01",
            "mighty Tribe of the Sun, had to be opposed...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201497V\x07\x0D",
            "In response, a new princess answered the\x01",
            "call and entered the celestial ceremony.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201498V\x07\x0D",
            "She was known as the Moon Princess...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201499V\x07\x0D",
            "Effectively splitting the governance of Ra in two,\x01",
            "she was raised by the Tribe of the Moon.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    OP_68(-80, 7300, 29380, 0)
    MoveCamera(0, -10, 0, 0)
    OP_6E(960, 0)
    SetCameraDistance(13000, 0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_7D(0x80, 0x80, 0xFF, 0x0, 0x1F4)
    OP_A7(0x9, 0x50, 0x50, 0x50, 0xFF, 0x0)
    LoadEffect(0x3, "event\\ev294_00.eff")
    LoadEffect(0x2, "event\\ev291_03.eff")
    LoadEffect(0x1, "event\\ev291_04.eff")
    LoadEffect(0x6, "event\\ev291_00.eff")
    LoadEffect(0x4, "event\\ev291_01.eff")
    LoadEffect(0x5, "event\\ev292_00.eff")
    LoadEffect(0x7, "event\\ev291_05.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_3A61")
    LoadEffect(0x0, "event\\evanull.eff")

    label("loc_3A61")

    SetChrPos(0x9, 50, 9540, 23220, 360)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    ClearChrFlags(0x9, 0x1)
    OP_C9(0x0, 0x0, 0xFFFE2B40, 0xFFFD40E0, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0x7D0, 0x0)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    Sleep(1000)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayBGM("ed7501", 1)
    BeginChrThread(0x101, 3, 0, 39)
    Sleep(26000)
    BeginChrThread(0x101, 2, 0, 45)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(1200)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x7D0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x7D0)
    Sleep(15000)
    EndChrThread(0x101, 0x2)
    Sleep(5700)
    BeginChrThread(0x101, 2, 0, 44)
    Sleep(2166)
    BeginChrThread(0x101, 3, 0, 41)
    BeginChrThread(0x22, 1, 0, 49)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x3E8)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x3E8)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x3E8)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3BAD():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_3BAD)

    def lambda_3BBE():
        OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3BBE)

    def lambda_3BCF():
        OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3BCF)

    def lambda_3BE0():
        OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3BE0)

    def lambda_3BF1():
        OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_3BF1)

    def lambda_3C02():
        OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3C02)
    WaitChrThread(0x101, 3)
    Sleep(2000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_3CD3")
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x4)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x13, 0xFF)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    EndChrThread(0x14, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x15, 0xFF)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x16, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_3CD3")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_48_34E1 end

    def Function_49_3CF1(): pass

    label("Function_49_3CF1")

    Sleep(15000)
    Sound(875, 0, 80, 0)
    Sound(877, 0, 100, 0)
    Sleep(3000)
    Sound(872, 0, 90, 0)
    Sound(873, 2, 100, 0)
    Sleep(4000)
    Sleep(4000)
    Sleep(5000)
    Sound(872, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(5000)
    Return()

    # Function_49_3CF1 end

    def Function_50_3D28(): pass

    label("Function_50_3D28")

    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x15, 0x0)
    OP_A8(0x9, 0x14, 0x14, 0x0, 0x0)
    BeginChrThread(0x9, 1, 0, 59)
    OP_C9(0x0, 0x0, 0xFFFC5680, 0xFFFB6C20, 0x0)
    OP_C9(0x0, 0x1, 0x5DC, 0xAF0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFDB610, 0xFFFB6C20, 0xFA0)
    SetChrChipByIndex(0x9, 0x28)
    OP_95(0x9, -3460, 1250, 25450, 800, 0x0)
    SetChrChipByIndex(0x9, 0x2D)
    OP_93(0x9, 0x87, 0x190)
    Sleep(1000)
    OP_93(0x9, 0xE1, 0x190)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x190)
    Return()

    # Function_50_3D28 end

    def Function_51_3DB2(): pass

    label("Function_51_3DB2")

    PlayEffect(0x5, 0x2, 0xFF, 0x0, 0, 1000, 25000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x23)

    def lambda_3DF2():

        label("loc_3DF2")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_3DF2")

    QueueWorkItem2(0x8, 3, lambda_3DF2)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, -690, 1250, 22710, 90)
    OP_A7(0x8, 0x0, 0x0, 0x0, 0xFF, 0x64)
    OP_68(-1890, 2900, 22370, 2000)
    MoveCamera(0, 16, 0, 2000)
    OP_6E(620, 2000)
    SetCameraDistance(17000, 2000)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -1370, 2000, 23670, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(900)

    def lambda_3E93():

        label("loc_3E93")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_3E93")

    QueueWorkItem2(0x9, 3, lambda_3E93)
    Sleep(1500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFFC5680, 0xFFFB6C20, 0xC8)
    OP_C9(0x0, 0x1, 0x7D0, 0xAF0, 0xC8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    OP_A8(0x8, 0x14, 0x14, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(1000)
    OP_96(0x9, 0xFFFFF5D8, 0x4E2, 0x5BCC, 0x5DC, 0x0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    OP_96(0x9, 0xFFFFF5D8, 0x4E2, 0x558C, 0x7D0, 0x0)
    Sleep(500)

    def lambda_3F83():
        OP_96(0x9, 0xFFFFF092, 0x4E2, 0x5C76, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3F83)
    OP_A8(0x8, 0x0, 0x0, 0x0, 0x3E8)
    OP_A8(0x9, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_51_3DB2 end

    def Function_52_3FAD(): pass

    label("Function_52_3FAD")

    BeginChrThread(0x8, 1, 0, 57)
    EndChrThread(0x9, 0x1)
    OP_68(-2440, 2900, 24920, 4000)
    MoveCamera(0, 19, 0, 4000)
    OP_6E(680, 4000)
    SetCameraDistance(17000, 4000)
    OP_11(0x0, 0x0, 0x0, 0x14, 0x32, 0xBB8)
    OP_C9(0x0, 0x0, 0xFFFA81C0, 0xFFFBBA40, 0xBB8)
    OP_C9(0x0, 0x1, 0x9C4, 0xBB8, 0xBB8)
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0xBB8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_95(0x8, -3550, 1250, 22010, 2400, 0x0)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_404D():
        OP_9E(0x8, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_404D)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    Sleep(1)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    WaitChrThread(0x8, 0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x384)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)

    def lambda_40D7():
        OP_93(0x8, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_40D7)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF614, 0x4E2, 0x622A, 0xBB8, 0x2BC)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_4107():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4107)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    Sleep(1100)

    def lambda_413E():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_413E)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_4191():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4191)
    OP_9D(0x8, 0xFFFFFD9E, 0x4E2, 0x65EA, 0x7D0, 0x578)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_9E(0x8, 0x3E8, 0x59D8, 0xFFFF15A0, 0x9C4, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(500)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    EndChrThread(0x8, 0x1)
    Sleep(800)

    def lambda_4221():

        label("loc_4221")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_4221")

    QueueWorkItem2(0x8, 3, lambda_4221)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF844, 0x4E2, 0x6004, 0x5DC, 0x7D0)
    Sleep(500)
    SetChrSubChip(0x8, 0x1)
    Sleep(60)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Return()

    # Function_52_3FAD end

    def Function_53_4268(): pass

    label("Function_53_4268")

    BeginChrThread(0x8, 1, 0, 57)

    def lambda_4273():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_4273)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF902, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF394, 0x4E2, 0x639C, 0x7D0, 0x578)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFEE30, 0x4E2, 0x639C, 0x7D0, 0x578)

    def lambda_42DD():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_42DD)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_9E(0x8, 0xFFFFEE44, 0x54B0, 0xBB80, 0x7D0, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x8, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(400)

    def lambda_433C():

        label("loc_433C")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_433C")

    QueueWorkItem2(0x8, 3, lambda_433C)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(1200)

    def lambda_4359():

        label("loc_4359")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_4359")

    QueueWorkItem2(0x8, 3, lambda_4359)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    Sleep(1100)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    BeginChrThread(0x8, 0, 0, 55)
    Sleep(700)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    BeginChrThread(0x9, 0, 0, 56)
    Return()

    # Function_53_4268 end

    def Function_54_439F(): pass

    label("Function_54_439F")

    BeginChrThread(0x9, 1, 0, 58)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_95(0x9, -3550, 1250, 22010, 2000, 0x0)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_43D6():
        OP_9E(0x9, 0xFFFFF858, 0x625C, 0xFFFF63C0, 0x4B0, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_43D6)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    Sleep(1)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x3E8)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    WaitChrThread(0x9, 0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x384)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)

    def lambda_4460():
        OP_93(0x9, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_4460)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFEE30, 0x4E2, 0x659A, 0xBB8, 0x2BC)
    BeginChrThread(0x9, 2, 0, 15)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_449A():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_449A)

    def lambda_44A7():
        OP_9D(0x8, 0xFFFFFFBA, 0x4E2, 0x61DA, 0x4B0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_44A7)

    def lambda_44C4():

        label("loc_44C4")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_44C4")

    QueueWorkItem2(0x9, 3, lambda_44C4)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x4B0, 0x1F4)

    def lambda_44ED():

        label("loc_44ED")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_44ED")

    QueueWorkItem2(0x8, 3, lambda_44ED)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    OP_95(0x9, -4560, 1250, 26010, 3000, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(1100)
    BeginChrThread(0x101, 2, 0, 53)

    def lambda_453C():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_453C)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFF394, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF902, 0x4E2, 0x65EA, 0x7D0, 0x578)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0xFFFFFD9E, 0x4E2, 0x65EA, 0x7D0, 0x578)

    def lambda_45A6():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_45A6)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    OP_9E(0x9, 0xFFFFFE0C, 0x59D8, 0xFFFF15A0, 0x7D0, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(700)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(400)
    EndChrThread(0x9, 0x3)

    def lambda_4609():

        label("loc_4609")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_4609")

    QueueWorkItem2(0x9, 3, lambda_4609)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_54_439F end

    def Function_55_461F(): pass

    label("Function_55_461F")

    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xFFFFFAD8, 0x59D8, 0x2BF20, 0x1194, 0x1)
    OP_9E(0xFE, 0xFFFFF8EE, 0x5BCC, 0x2BF20, 0x1194, 0x1)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0xFFFFF786, 0x4E2, 0x53F2, 0xBB8, 0x3E8)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9E(0xFE, 0xFFFFF8EE, 0x5BCC, 0x2BF20, 0x1770, 0x1)
    OP_96(0xFE, 0x582, 0x4E2, 0x67F2, 0x1770, 0x0)
    BeginChrThread(0xFE, 2, 0, 6)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x12C0, 0x7D0)

    def lambda_46C3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_46C3)
    BeginChrThread(0xFE, 2, 0, 7)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_4710():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4710)
    BeginChrThread(0xFE, 2, 0, 7)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 9)
    BeginChrThread(0xFE, 3, 0, 18)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    SetChrChipByIndex(0xFE, 0x1F)
    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xD7A, 0x6C16, 0xFFFD8F00, 0x1388, 0x1)
    OP_9D(0xFE, 0xFFFFF02E, 0x1F0E, 0x6F86, 0x1388, 0x7D0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0x9, 500)
    Sleep(500)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(1700)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 2, 0, 6)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFFC18, 0x20D0, 0x6978, 0x5DC, 0x320)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 18)

    def lambda_47EA():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0x1A3EC0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47EA)
    Sleep(1)

    def lambda_4808():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4808)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_55_461F end

    def Function_56_4868(): pass

    label("Function_56_4868")

    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xFFFFF84E, 0x59B0, 0x2BF20, 0xFA0, 0x1)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0xFFFFF9CA, 0x4E2, 0x636A, 0xBB8, 0x3E8)

    def lambda_48A9():
        OP_96(0xFE, 0xFFFFFAD8, 0x4E2, 0x6978, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_48A9)

    def lambda_48C3():

        label("loc_48C3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_48C3")

    QueueWorkItem2(0x10, 1, lambda_48C3)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x29)
    OP_95(0xFE, 1410, 1250, 26610, 5000, 0x0)
    OP_68(-1000, 7000, 26030, 3000)
    MoveCamera(0, 12, 0, 3000)
    OP_6E(620, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xFE, 2, 0, 14)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x12C0, 0x7D0)

    def lambda_493C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_493C)
    BeginChrThread(0xFE, 2, 0, 15)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0x15FE, 0x125C, 0x6B8A, 0x7D0, 0x578)

    def lambda_4989():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4989)
    BeginChrThread(0xFE, 2, 0, 15)
    OP_9D(0xFE, 0xD7A, 0x125C, 0x6C16, 0x7D0, 0x578)
    BeginChrThread(0xFE, 2, 0, 17)
    BeginChrThread(0xFE, 3, 0, 20)
    OP_9D(0xFE, 0x1158, 0x125C, 0x655E, 0x7D0, 0x578)
    SetChrChipByIndex(0xFE, 0x29)
    EndChrThread(0xFE, 0x3)
    OP_9E(0xFE, 0xD7A, 0x6C16, 0xFFFD8F00, 0x1388, 0x1)
    BeginChrThread(0xFE, 2, 0, 14)
    OP_9D(0xFE, 0xFFFFF02E, 0x1F0E, 0x6F86, 0x1388, 0x7D0)
    SetChrChipByIndex(0xFE, 0x28)
    OP_95(0xFE, -5770, 7950, 27760, 2000, 0x0)
    OP_95(0xFE, -6170, 7950, 26370, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 2, 0, 14)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFFC18, 0x20D0, 0x59D8, 0x5DC, 0x320)
    OP_68(-1000, 4000, 26030, 8000)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 20)

    def lambda_4A9B():
        OP_9E(0xFE, 0xFFFFFC18, 0x61A8, 0xFFE5C140, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A9B)
    Sleep(1)

    def lambda_4AB9():
        OP_96(0xFE, 0xFDB, 0x4E2, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AB9)
    Sleep(300)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_56_4868 end

    def Function_57_4B19(): pass

    label("Function_57_4B19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BB1")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B8E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B8E")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_4B8E")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_57_4B19")

    label("loc_4BB1")

    Return()

    # Function_57_4B19 end

    def Function_58_4BB2(): pass

    label("Function_58_4BB2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C4A")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C27")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C27")
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_4C27")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_58_4BB2")

    label("loc_4C4A")

    Return()

    # Function_58_4BB2 end

    def Function_59_4C4B(): pass

    label("Function_59_4C4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C95")
    PlayEffect(0x1, 0xFF, 0xFE, 0x40, 0, 100, 0, 0, 0, 0, 1100, 1800, 1100, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_59_4C4B")

    label("loc_4C95")

    Return()

    # Function_59_4C4B end

    def Function_60_4C96(): pass

    label("Function_60_4C96")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50280.itc", 0x1E)
    LoadChrToIndex("apl/ch50281.itc", 0x1F)
    LoadChrToIndex("apl/ch50282.itc", 0x20)
    LoadChrToIndex("apl/ch50283.itc", 0x21)
    LoadChrToIndex("apl/ch50284.itc", 0x22)
    LoadChrToIndex("chr/ch09900.itc", 0x23)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("chr/ch09800.itc", 0x2D)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x10, -9000, 1250, 25450, 270)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2580, 2900, 24350, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x9, -6960, 1250, 25450, 90)
    SetChrPos(0x8, 3890, 4700, 27480, 225)
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    SoundLoad(876)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201507V\x07\x05",
            "Was it simply a whim of the Goddess?\x01",
            "Or perhaps a bit of mischief?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201508V\x07\x05",
            "To her surprise, the Sun Princess learned that the\x01",
            "Moon Princess was not a stranger, but her younger\x01",
            "sister, separated from her at a tender age.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201509V\x07\x05",
            "Unaware of this revelation, the Moon Princess\x01",
            "faced her sister with a cold, hostile spirit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201510V\x07\x05",
            "The distraught Sun Princess, concealing her true\x01",
            "identity with a gown and mask of white, beckoned\x01",
            "the Moon Princess to the forest ruins...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201511V\x07\x05",
            "It was there that the two sisters, pure in\x01",
            "their youth, would secretly dance and\x01",
            "play under the thick forest canopy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    Sleep(1000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x1F4)
    FadeToBright(1000, 0)
    PlayBGM("ed7502", 1)
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadEffect(0x5, "event\\ev292_01.eff")
    LoadEffect(0x2, "event\\ev292_02.eff")
    LoadEffect(0x3, "event\\ev292_03.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_51D1")
    LoadEffect(0x0, "event\\evanull.eff")
    LoadEffect(0x4, "event\\evanull.eff")
    LoadEffect(0x6, "event\\evanull.eff")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_51D1")

    BeginChrThread(0x101, 0, 0, 50)
    Sleep(8810)
    BeginChrThread(0x101, 1, 0, 51)
    Sleep(8900)
    BeginChrThread(0x101, 0, 0, 52)
    Sleep(8900)
    Sleep(8900)
    BeginChrThread(0x101, 1, 0, 54)
    Sleep(8900)
    Sleep(8900)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x3E8)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x3E8)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1100, 1500, 0xFF, 0, 0, 0, 0)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x22, 1, 0, 61)
    OP_7D(0xFF, 0xB4, 0xB4, 0x0, 0x22C4)
    Sleep(8900)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4000)
    OP_7D(0x0, 0xFF, 0xFF, 0x0, 0x22C4)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 12000, 25000, 0, 180, 0, 1000, 1100, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(4900)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_5408")
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_5408")

    WaitChrThread(0x22, 1)
    OP_E6()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5D, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_60_4C96 end

    def Function_61_5426(): pass

    label("Function_61_5426")

    Sleep(2500)
    Sound(876, 0, 100, 0)
    Sound(873, 2, 100, 0)
    Sleep(6500)
    Sound(874, 0, 100, 0)
    Sleep(8000)
    Sound(872, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(3000)
    Return()

    # Function_61_5426 end

    def Function_62_5451(): pass

    label("Function_62_5451")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55AE")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_62_5451")

    label("loc_55AE")

    Return()

    # Function_62_5451 end

    def Function_63_55AF(): pass

    label("Function_63_55AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_570C")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_63_55AF")

    label("loc_570C")

    Return()

    # Function_63_55AF end

    def Function_64_570D(): pass

    label("Function_64_570D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57DC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57B9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B9")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_57B9")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_64_570D")

    label("loc_57DC")

    Return()

    # Function_64_570D end

    def Function_65_57DD(): pass

    label("Function_65_57DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_58AC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5889")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5889")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    label("loc_5889")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_65_57DD")

    label("loc_58AC")

    Return()

    # Function_65_57DD end

    def Function_66_58AD(): pass

    label("Function_66_58AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597C")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5959")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5959")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5959")

    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_66_58AD")

    label("loc_597C")

    Return()

    # Function_66_58AD end

    def Function_67_597D(): pass

    label("Function_67_597D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A4C")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A29")
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A29")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 100, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    label("loc_5A29")

    RunExpression(0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x6, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_67_597D")

    label("loc_5A4C")

    Return()

    # Function_67_597D end

    def Function_68_5A4D(): pass

    label("Function_68_5A4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A97")
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_68_5A4D")

    label("loc_5A97")

    Return()

    # Function_68_5A4D end

    def Function_69_5A98(): pass

    label("Function_69_5A98")


    def lambda_5A9D():

        label("loc_5A9D")

        TurnDirection(0xC, 0x8, 500)
        Yield()
        Jump("loc_5A9D")

    QueueWorkItem2(0xC, 1, lambda_5A9D)
    OP_95(0x8, -2000, 1250, 24200, 1000, 0x0)
    Sleep(1000)
    TurnDirection(0x8, 0xC, 500)
    Sleep(500)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(90)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sleep(1500)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0x8, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(13333)
    Sleep(3000)
    Return()

    # Function_69_5A98 end

    def Function_70_5B1D(): pass

    label("Function_70_5B1D")


    def lambda_5B22():

        label("loc_5B22")

        TurnDirection(0xC, 0x9, 500)
        Yield()
        Jump("loc_5B22")

    QueueWorkItem2(0xC, 1, lambda_5B22)
    OP_95(0x9, 2000, 1250, 24200, 1000, 0x0)
    Sleep(1000)
    TurnDirection(0x9, 0xC, 500)
    Sleep(500)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x1)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(90)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(1500)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xB, 0x0)
    Sleep(90)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    EndChrThread(0xC, 0x1)
    OP_93(0xC, 0xB4, 0x1F4)
    BeginChrThread(0xC, 0, 0, 75)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x2)
    OP_68(50, 3500, 23770, 5000)
    MoveCamera(0, 15, 0, 5000)
    OP_6E(720, 5000)
    SetCameraDistance(15000, 5000)
    Return()

    # Function_70_5B1D end

    def Function_71_5BE6(): pass

    label("Function_71_5BE6")

    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 15)

    def lambda_5BFB():
        OP_9D(0x9, 0xFA, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5BFB)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 1)
    OP_9D(0x9, 0x726, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x9, 0x3)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_9E(0x9, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)

    def lambda_5C73():
        OP_9E(0x9, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C73)
    Sleep(33)

    def lambda_5C91():

        label("loc_5C91")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_5C91")

    QueueWorkItem2(0x9, 3, lambda_5C91)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0x9, 2, 0, 17)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 0, 0, 67)
    OP_9E(0x9, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 14)

    def lambda_5D41():

        label("loc_5D41")

        TurnDirection(0x9, 0x8, 500)
        Yield()
        Jump("loc_5D41")

    QueueWorkItem2(0x9, 3, lambda_5D41)
    OP_9D(0x9, 0xFFFFEFF2, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, -1420, 1250, 24000, 6000, 0x0)
    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x384, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 47)

    def lambda_5DD6():
        OP_9D(0x9, 0xF28, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DD6)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    WaitChrThread(0x9, 1)

    def lambda_5E06():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_5E06)
    Sleep(700)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    SetChrSubChip(0x9, 0x0)
    Sleep(600)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, 500, 1250, 23750, 7000, 0x0)
    Return()

    # Function_71_5BE6 end

    def Function_72_5E46(): pass

    label("Function_72_5E46")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 7)

    def lambda_5E5B():
        OP_9D(0x8, 0xFFFFFF06, 0xCB2, 0x5C58, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5E5B)
    Sleep(200)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    WaitChrThread(0x8, 1)
    OP_9D(0x8, 0xFFFFF8DA, 0x4E2, 0x5C58, 0x1F4, 0x5DC)
    EndChrThread(0x8, 0x3)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_9E(0x8, 0x0, 0x5DC0, 0x20F58, 0x1770, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 18)

    def lambda_5ED9():
        OP_9E(0x8, 0x0, 0x5DC0, 0x1B7740, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5ED9)
    Sleep(33)

    def lambda_5EF7():

        label("loc_5EF7")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_5EF7")

    QueueWorkItem2(0x8, 3, lambda_5EF7)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0x7D0, 0x7D0)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xBB8, 0x3E8)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 0, 0, 66)
    OP_9E(0x8, 0x0, 0x5DC0, 0x50910, 0x1388, 0x1)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 6)

    def lambda_5FA7():

        label("loc_5FA7")

        TurnDirection(0x8, 0x9, 500)
        Yield()
        Jump("loc_5FA7")

    QueueWorkItem2(0x8, 3, lambda_5FA7)
    OP_9D(0x8, 0x100E, 0x4E2, 0x5DDE, 0xBB8, 0x3E8)
    EndChrThread(0x8, 0x3)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(900)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, 1420, 1250, 23000, 6000, 0x0)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFC7C, 0x4E2, 0x5BC2, 0x7D0, 0xDAC)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 46)

    def lambda_603C():
        OP_9D(0x8, 0xFFFFF0D8, 0x4E2, 0x5BC2, 0xDAC, 0x384)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_603C)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    WaitChrThread(0x8, 1)

    def lambda_606C():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_606C)
    Sleep(700)

    def lambda_607C():

        label("loc_607C")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_607C")

    QueueWorkItem2(0x8, 3, lambda_607C)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(600)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, -500, 1250, 23750, 7000, 0x0)
    Return()

    # Function_72_5E46 end

    def Function_73_60BE(): pass

    label("Function_73_60BE")

    OP_68(10, 7180, 26650, 3000)
    MoveCamera(0, 18, 0, 3000)
    OP_6E(720, 3000)
    SetCameraDistance(18500, 3000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x1720, 0x16A8, 0x605E, 0x157C, 0x7D0)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x10E, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(1000)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x14F0, 0x1DB0, 0x67F2, 0x9C4, 0x5DC)
    SetChrChipByIndex(0x9, 0x29)
    OP_95(0x9, 3810, 7600, 30020, 6000, 0x0)
    OP_95(0x9, 2080, 7600, 30770, 6000, 0x0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    TurnDirection(0x9, 0x8, 0)
    OP_68(0, 8920, 31090, 6000)
    MoveCamera(0, 0, 0, 6000)
    OP_6E(720, 6000)
    SetCameraDistance(18500, 6000)
    BeginChrThread(0x9, 0, 0, 68)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 16)
    Sleep(500)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 16)
    Sleep(200)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    Sleep(300)
    OP_9D(0x9, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x820, 0x1DB0, 0x7832, 0xBB8, 0xBB8)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFA, 0x2580, 0x7832, 0x834, 0xBB8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 9900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x9, 0x7D0, 0x1DB0, 0x7832, 0x64, 0x1388)

    def lambda_6379():

        label("loc_6379")

        TurnDirection(0x9, 0x8, 0)
        Yield()
        Jump("loc_6379")

    QueueWorkItem2(0x9, 3, lambda_6379)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(250)
    BeginChrThread(0x9, 2, 0, 17)
    OP_9D(0x9, 0xFA, 0x2198, 0x7832, 0x44C, 0xBB8)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x9, 0x7D0, 0x1C84, 0x7832, 0x64, 0xBB8)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x28)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_96(0x9, 0x10FE, 0x1C84, 0x76B6, 0x5DC, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    Sleep(30)
    SetChrSubChip(0x9, 0x0)
    Sleep(800)
    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0x7D0, 0x1DB0, 0x7832, 0x7D0, 0x1388)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9D(0x9, 0xFA, 0x2134, 0x7832, 0x5DC, 0x1388)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 8900, 30800, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_68(10, 2900, 23870, 5000)
    MoveCamera(0, 20, 0, 5000)
    OP_6E(720, 5000)
    SetCameraDistance(18500, 5000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    BeginChrThread(0x9, 0, 0, 68)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 3, 0, 21)
    OP_96(0x9, 0x190, 0x1B58, 0x61A8, 0xBB8, 0x0)

    def lambda_664D():
        OP_9E(0x9, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_664D)
    Sleep(33)
    OP_96(0x9, 0xFA, 0x4E2, 0x61A8, 0x4B0, 0x0)
    BeginChrThread(0x9, 0, 0, 67)
    BeginChrThread(0x9, 3, 0, 20)
    Sleep(800)
    OP_96(0x9, 0x6EA, 0x4E2, 0x5226, 0x3E8, 0x0)
    Sleep(1033)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(1500)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9C(0x9, 0x3E8, 0x0, 0x0, 0x44C, 0x578)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    BeginChrThread(0x9, 2, 0, 14)
    OP_9C(0x9, 0x0, 0xBB8, 0x0, 0x1004, 0x3E8)
    BeginChrThread(0x9, 0, 0, 68)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, -1510, 5250, 25740)
    OP_9F(0x1, 1510, 7250, 25740)
    OP_9F(0x1, 600, 8250, 20580)
    OP_9F(0x2, 0x9, 4000, 0x2)
    Return()

    # Function_73_60BE end

    def Function_74_6739(): pass

    label("Function_74_6739")

    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFE8E0, 0x16A8, 0x605E, 0x157C, 0x7D0)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x5A, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(1000)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFEB10, 0x1DB0, 0x67F2, 0x9C4, 0x5DC)
    SetChrChipByIndex(0x8, 0x1F)
    OP_95(0x8, -3810, 7600, 30020, 6000, 0x0)
    OP_95(0x8, -2080, 7600, 30770, 6000, 0x0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    BeginChrThread(0x8, 0, 0, 68)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0x820, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x9C4, 0xBB8)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 8)
    Sleep(500)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFF3F8, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(100)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0xC8, 0xBB8)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 20)
    OP_9D(0x8, 0x820, 0x1DB0, 0x7832, 0xBB8, 0xBB8)
    BeginChrThread(0x8, 2, 0, 8)
    EndChrThread(0x8, 0x3)
    Sleep(500)
    OP_9D(0x8, 0xFFFFF7E0, 0x1DB0, 0x7832, 0x1F4, 0x7D0)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFF06, 0x2580, 0x7832, 0x834, 0xBB8)
    OP_9D(0x8, 0xFFFFF830, 0x1DB0, 0x7832, 0x64, 0x1388)

    def lambda_68FA():

        label("loc_68FA")

        TurnDirection(0x8, 0x9, 0)
        Yield()
        Jump("loc_68FA")

    QueueWorkItem2(0x8, 3, lambda_68FA)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(250)
    BeginChrThread(0x8, 2, 0, 9)
    OP_9D(0x8, 0xFFFFFF06, 0x2198, 0x7832, 0x44C, 0xBB8)
    OP_9D(0x8, 0xFFFFF830, 0x1C84, 0x7832, 0x64, 0xBB8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_96(0x8, 0xFFFFEF02, 0x1C84, 0x76B6, 0x5DC, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x1)
    Sleep(30)
    SetChrSubChip(0x8, 0x0)
    Sleep(800)
    BeginChrThread(0x8, 2, 0, 10)
    BeginChrThread(0x8, 3, 0, 20)
    OP_9D(0x8, 0xFFFFF830, 0x1DB0, 0x7832, 0x7D0, 0x1388)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9D(0x8, 0xFFFFFF06, 0x2134, 0x7832, 0x5DC, 0x1388)
    BeginChrThread(0x8, 0, 0, 68)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 3, 0, 19)
    OP_96(0x8, 0xFFFFFE70, 0x1B58, 0x61A8, 0xBB8, 0x0)

    def lambda_6A0C():
        OP_9E(0x8, 0x0, 0x61A8, 0x20F580, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6A0C)
    Sleep(33)
    OP_96(0x8, 0xFFFFFF06, 0x4E2, 0x61A8, 0x4B0, 0x0)
    BeginChrThread(0x8, 0, 0, 66)
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(800)
    OP_96(0x8, 0xFFFFF916, 0x4E2, 0x5226, 0x3E8, 0x0)
    Sleep(1033)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(1500)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9C(0x8, 0xFFFFFC18, 0x0, 0x0, 0x44C, 0x578)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    Sleep(2000)
    BeginChrThread(0x8, 2, 0, 6)
    OP_9C(0x8, 0x0, 0xBB8, 0x0, 0x1004, 0x3E8)
    BeginChrThread(0x8, 0, 0, 68)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, 1510, 5250, 25740)
    OP_9F(0x1, -1510, 7250, 25740)
    OP_9F(0x1, -600, 8250, 20580)
    OP_9F(0x2, 0x8, 4000, 0x2)
    Return()

    # Function_74_6739 end

    def Function_75_6AF8(): pass

    label("Function_75_6AF8")

    OP_96(0xC, 0xA, 0x4E2, 0x7044, 0x3E8, 0x0)
    OP_96(0xC, 0x0, 0x8F2, 0x7486, 0x3E8, 0x0)
    Return()

    # Function_75_6AF8 end

    def Function_76_6B21(): pass

    label("Function_76_6B21")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetMapObjFrame(0x3, "ball", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Bback", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    LoadChrToIndex("chr/ch37100.itc", 0x39)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0xC, 10, 1250, 26300, 180)
    SetChrPos(0xE, -2920, 1800, 28680, 135)
    SetChrPos(0x10, -3610, 1800, 27530, 135)
    SetChrPos(0x11, -4670, 1800, 28800, 132)
    SetChrPos(0x12, -4830, 1800, 27400, 132)
    SetChrPos(0xD, 2920, 1800, 28680, 225)
    SetChrPos(0xF, 3610, 1800, 27530, 225)
    SetChrPos(0x13, 4670, 1800, 28800, 225)
    SetChrPos(0x14, 4830, 1800, 27400, 225)
    SetChrPos(0x15, -6200, 1250, 24300, 135)
    SetChrPos(0x16, 6200, 1250, 24300, 225)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2B)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x100)
    SetChrPos(0xB, 10, 1250, 25450, 230)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xB, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xB, 3, 0, 30)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x100)
    SetChrPos(0xA, 10, 1250, 25450, 230)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0xA, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0xA, 3, 0, 31)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x34)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x100)
    SetChrPos(0x17, 10, 1250, 25450, 230)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_D3(0x17, 0x2BF20, 0x0, 0x0, 0x0)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(10, 3830, 24760, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(15000, 0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x1F4)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetChrPos(0x101, 10, 1250, 28450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    LoadEffect(0x0, "event\\ev290_01.eff")
    LoadEffect(0x1, "event\\ev291_04.eff")
    LoadEffect(0x2, "event\\ev291_03.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev293_01.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_70A0")
    LoadEffect(0x7, "event\\evanull.eff")

    label("loc_70A0")

    SoundLoad(872)
    SoundLoad(873)
    SoundLoad(874)
    SoundLoad(876)
    Sound(877, 0, 100, 0)
    Sleep(4000)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201520V\x07\x0D",
            "The dreadful conspiracy existed only\x01",
            "to drive the young sisters apart...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201521V\x07\x0D",
            "Despite knowing the sad truth, the sisters\x01",
            "chose to compete against one another.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201522V\x07\x0D",
            "Because, after all, they were princesses...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201523V\x07\x0D",
            "Dancing was their all, their everything. Only one\x01",
            "of them could become the Shrine Princess,\x01",
            "carrying the will of the Goddess on their shoulders.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201524V\x07\x0D",
            "Their affection for one another strong, they\x01",
            "even fell in love with the same man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201525V\x07\x0D",
            "Their rivalry burned bright with passion and\x01",
            "understanding, like Ra had never seen before.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#2201526V\x07\x0D",
            "The two princesses, storing their passion in\x01",
            "their hearts, then traveled down to the Star\x01",
            "Sanctuary, ready for the fated ceremony...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_E5()
    Sleep(1000)
    PlayBGM("ed7503", 1)
    FadeToBright(1000, 0)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 62)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xDC, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    BeginChrThread(0x8, 0, 0, 64)
    BeginChrThread(0x101, 0, 0, 69)
    Sleep(10333)
    BeginChrThread(0x9, 0, 0, 65)
    BeginChrThread(0x101, 1, 0, 70)
    Sleep(3000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 400, 600, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, -4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 4160, -2000, 31100, 0, -90, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xFF, 0xDC, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0x3E8)
    Sleep(15000)
    BeginChrThread(0x101, 0, 0, 72)
    BeginChrThread(0x101, 1, 0, 71)
    Sleep(500)
    BeginChrThread(0x22, 1, 0, 77)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x1F4)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x1F4)
    OP_7D(0xE6, 0xDC, 0xFF, 0x0, 0x1F4)
    BeginChrThread(0x101, 3, 0, 63)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(15000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(200, 16777215)
    BeginChrThread(0x101, 0, 0, 74)
    BeginChrThread(0x101, 1, 0, 73)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 1900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 1900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(35000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitChrThread(0x22, 1)
    WaitBGM()
    OP_E6()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_7ABE")
    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xB, 0x4)
    EndChrThread(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x1000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x1000)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0xC, 0x4)
    EndChrThread(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x1000)
    SetChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x4)
    EndChrThread(0x17, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    EndChrThread(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    EndChrThread(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    EndChrThread(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    EndChrThread(0x13, 0xFF)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    EndChrThread(0x14, 0xFF)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x15, 0xFF)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x16, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_24(0x369)
    Return()

    label("loc_7ABE")

    OP_24(0x369)
    SetScenarioFlags(0x5D, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_76_6B21 end

    def Function_77_7ACE(): pass

    label("Function_77_7ACE")

    Sleep(500)
    Sound(874, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(873, 2, 100, 0)
    Sleep(14500)
    Sound(872, 0, 100, 0)
    Sleep(15000)
    Sound(872, 0, 100, 0)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(2000)
    Sound(872, 0, 100, 0)
    Sleep(2000)
    Sound(876, 0, 100, 0)
    Sleep(7000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    OP_24(0x369)
    Sleep(1000)
    Return()

    # Function_77_7ACE end

    def Function_78_7B23(): pass

    label("Function_78_7B23")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B36")
    Sleep(4138)
    Jump("Function_78_7B23")

    label("loc_7B36")

    Return()

    # Function_78_7B23 end

    def Function_79_7B37(): pass

    label("Function_79_7B37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B81")
    PlayEffect(0x7, 0xFF, 0xFE, 0x100, -500, -800, 0, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_79_7B37")

    label("loc_7B81")

    Return()

    # Function_79_7B37 end

    def Function_80_7B82(): pass

    label("Function_80_7B82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C71")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4410, 3700, 20000, 0, 90, 0, 300, 400, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -4100, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 4000, 4800, 31100, 0, 90, 0, 200, 300, 200, 0xFF, 0, 0, 0, 0)
    Sleep(833)
    Jump("Function_80_7B82")

    label("loc_7C71")

    Return()

    # Function_80_7B82 end

    def Function_81_7C72(): pass

    label("Function_81_7C72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7CBC")
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_81_7C72")

    label("loc_7CBC")

    Return()

    # Function_81_7C72 end

    def Function_82_7CBD(): pass

    label("Function_82_7CBD")

    SetChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    OP_9D(0x8, 0xA, 0x2E18, 0x61A8, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 19)

    def lambda_7D01():
        OP_9E(0x8, 0xFFFFFA24, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7D01)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7D43():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7D43)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_7D7C():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7D7C)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7D92():
        OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7D92)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x8, 0x0)

    def lambda_7DCB():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7DCB)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)

    def lambda_7E07():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7E07)
    Sleep(33)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x8, 2, 0, 6)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 18)
    OP_9C(0x8, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x8, 0x0)

    def lambda_7E6A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_7E6A)
    BeginChrThread(0x8, 2, 0, 7)
    OP_9D(0x8, 0xFFFFFE0C, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_7E94():
        OP_9E(0x8, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7E94)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 2, 0, 9)
    Sleep(1)
    OP_9D(0x8, 0xFFFFFE0C, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    EndChrThread(0x8, 0x3)
    OP_93(0x8, 0xB4, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_82_7CBD end

    def Function_83_7EE2(): pass

    label("Function_83_7EE2")

    Sleep(600)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x1)
    Return()

    # Function_83_7EE2 end

    def Function_84_7EFC(): pass

    label("Function_84_7EFC")

    SetChrFlags(0x9, 0x4)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    OP_9D(0x9, 0xA, 0x2E18, 0x61A8, 0xFA0, 0x3E8)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    BeginChrThread(0x9, 2, 0, 17)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 21)

    def lambda_7F40():
        OP_9E(0x9, 0x5DC, 0x61A8, 0x927C0, 0x1D4C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7F40)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x44C)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7F82():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7F82)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_7FBB():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7FBB)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_7FD1():
        OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x12C0, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_7FD1)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x406)
    EndChrThread(0x9, 0x0)

    def lambda_800A():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_800A)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)

    def lambda_8046():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFFA81C0, 0x2134, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8046)
    Sleep(33)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x320)
    BeginChrThread(0x9, 2, 0, 14)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 20)
    OP_9C(0x9, 0x0, 0x0, 0x0, 0xFA0, 0x3E8)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x9, 0x0)

    def lambda_80A9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_80A9)
    BeginChrThread(0x9, 2, 0, 15)
    OP_9D(0x9, 0x1F4, 0x319C, 0x61A8, 0x7D0, 0xBB8)

    def lambda_80D3():
        OP_9E(0x9, 0x0, 0x61A8, 0xFFF50380, 0x1194, 0x2)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_80D3)
    EndChrThread(0x9, 0x3)
    BeginChrThread(0x9, 2, 0, 17)
    Sleep(1)
    OP_9D(0x9, 0x1F4, 0x332C, 0x61A8, 0xBB8, 0x4B0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_84_7EFC end

    def Function_85_811D(): pass

    label("Function_85_811D")

    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(100)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x1)
    Return()

    # Function_85_811D end

    def Function_86_8137(): pass

    label("Function_86_8137")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_816D")
    OP_D3(0x18, 0x0, 0x36EE80, 0x0, 0xEA60)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    Jump("Function_86_8137")

    label("loc_816D")

    Return()

    # Function_86_8137 end

    def Function_87_816E(): pass

    label("Function_87_816E")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 4000, 0x0)
    Sleep(500)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2BC, 0xBB8)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x2BC, 0xBB8)
    Sleep(800)
    OP_93(0xFE, 0x5A, 0x2BC)
    Sleep(100)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(300)
    OP_93(0xFE, 0xC8, 0x2BC)
    OP_9E(0xFE, 0x0, 0x61A8, 0x99CF0, 0x1770, 0x1)
    OP_9E(0xFE, 0x0, 0x66BC, 0x29810, 0x1770, 0x1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)

    label("loc_8234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_829A")
    OP_A1(0xFE, 0x7D0, 0x4, 0x2, 0x3, 0x2, 0x4)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_826C")
    Sleep(1500)
    Jump("loc_8295")

    label("loc_826C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8283")
    Sleep(800)
    Jump("loc_8295")

    label("loc_8283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8295")
    Sleep(100)

    label("loc_8295")

    Jump("loc_8234")

    label("loc_829A")

    Return()

    # Function_87_816E end

    def Function_88_829B(): pass

    label("Function_88_829B")

    Sleep(4000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x8ED28, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x3E8, 0x1F4, 0x0)
    Return()

    # Function_88_829B end

    def Function_89_82EE(): pass

    label("Function_89_82EE")

    Sleep(4500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_95(0xFE, 2610, 1250, 24750, 5000, 0x0)
    OP_9E(0xFE, 0x0, 0x61A8, 0x83D60, 0x1388, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x10, 500)
    Sleep(1000)
    OP_99(0xFE, 0x10, 0x4B0, 0x1F4, 0x0)
    Return()

    # Function_89_82EE end

    def Function_90_8341(): pass

    label("Function_90_8341")

    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xBB8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x7D0, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x5DC, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x3E8, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x320, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFE0C, 0x0, 0x28A, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x1F4, 0x0)
    OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x12C, 0x0)
    Return()

    # Function_90_8341 end

    def Function_91_83E2(): pass

    label("Function_91_83E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8400")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_91_83E2")

    label("loc_8400")

    Return()

    # Function_91_83E2 end

    def Function_92_8401(): pass

    label("Function_92_8401")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_841F")
    OP_A1(0xFE, 0x7D0, 0x8, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3, 0x0, 0x1)
    Jump("Function_92_8401")

    label("loc_841F")

    Return()

    # Function_92_8401 end

    def Function_93_8420(): pass

    label("Function_93_8420")

    OP_9D(0x8, 0xFFFFFA06, 0x109A, 0x578A, 0x7D0, 0x7D0)
    SetChrChipByIndex(0x8, 0x1E)
    BeginChrThread(0x8, 2, 0, 91)
    Sleep(5200)
    SetChrChipByIndex(0x8, 0x1F)
    Sleep(2000)
    EndChrThread(0x8, 0x2)
    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    OP_9D(0x8, 0xFFFFFE0C, 0x157C, 0x61A8, 0xBB8, 0x4B0)

    def lambda_847A():

        label("loc_847A")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_847A")

    QueueWorkItem2(0x8, 2, lambda_847A)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_84DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84F9")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_84DB")

    label("loc_84F9")

    Return()

    # Function_93_8420 end

    def Function_94_84FA(): pass

    label("Function_94_84FA")

    OP_9D(0x9, 0x5FA, 0x109A, 0x578A, 0x7D0, 0x7D0)
    SetChrChipByIndex(0x9, 0x28)
    BeginChrThread(0x9, 2, 0, 92)
    Sleep(5200)
    SetChrChipByIndex(0x9, 0x29)
    Sleep(2000)
    EndChrThread(0x9, 0x2)
    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    OP_9D(0x9, 0x1F4, 0x157C, 0x61A8, 0xBB8, 0x4B0)

    def lambda_8554():

        label("loc_8554")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_8554")

    QueueWorkItem2(0x9, 2, lambda_8554)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_85B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85D7")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_85B9")

    label("loc_85D7")

    Return()

    # Function_94_84FA end

    def Function_95_85D8(): pass

    label("Function_95_85D8")

    OP_F8(0x14D)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50256.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("apl/ch50271.itc", 0x2E)
    LoadChrToIndex("chr/ch00102.itc", 0x2F)
    LoadChrToIndex("apl/ch50234.itc", 0x30)
    LoadChrToIndex("chr/ch25800.itc", 0x31)
    LoadChrToIndex("apl/ch50294.itc", 0x32)
    LoadChrToIndex("chr/ch36700.itc", 0x34)
    LoadChrToIndex("chr/ch36600.itc", 0x35)
    LoadChrToIndex("chr/ch36900.itc", 0x36)
    LoadChrToIndex("chr/ch37000.itc", 0x37)
    LoadChrToIndex("chr/ch36800.itc", 0x38)
    LoadChrToIndex("apl/ch50289.itc", 0x39)
    LoadChrToIndex("chr/ch37200.itc", 0x3A)
    LoadChrToIndex("apl/ch50290.itc", 0x3D)
    LoadChrToIndex("apl/ch50291.itc", 0x3C)
    LoadChrToIndex("apl/ch50292.itc", 0x3E)
    LoadChrToIndex("apl/ch50293.itc", 0x3F)
    SetChrPos(0x10, 7930, 1250, 24860, 270)
    SetChrPos(0x11, 7930, 1250, 24860, 270)
    SetChrPos(0x12, 7930, 1250, 24860, 270)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x35)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x36)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x37)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x38)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x3A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x3A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x39)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x39)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrPos(0x13, -5940, 5800, 24600, 180)
    SetChrPos(0x14, 5940, 5800, 24600, 180)
    SetChrPos(0x15, -5680, 7600, 26590, 180)
    SetChrPos(0x16, 5680, 7600, 26590, 180)
    SetChrPos(0xC, 7500, 1500, 25000, 225)
    SetChrPos(0xD, -7500, 1500, 25000, 225)
    SetChrPos(0xE, 7500, 1500, 25000, 135)
    SetChrPos(0xF, -7500, 1500, 25000, 135)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    LoadEffect(0x0, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_01.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev295_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev290_05.eff")
    LoadEffect(0x7, "event\\ev294_00.eff")
    SetChrPos(0x101, 10, 1250, 25450, 360)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Aback", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x1)
    LoadChrToIndex("chr/ch05800.itc", 0x3B)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -27000, 15200, 8500, 270)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x17, 0x1E, 0x0)
    SoundLoad(872)
    SoundLoad(874)
    SoundLoad(875)
    SoundLoad(876)
    SoundLoad(880)
    SoundLoad(881)
    OP_E5()
    PlayBGM("ed7506", 1)
    BeginChrThread(0x22, 1, 0, 96)
    BeginChrThread(0x101, 3, 0, 80)
    BeginChrThread(0x101, 2, 0, 78)
    FadeToBright(6000, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_68(10, 5680, 25450, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(15500, 0)
    OP_68(10, 13680, 25450, 12000)
    MoveCamera(0, -1, 0, 12000)
    OP_6E(640, 12000)
    SetCameraDistance(18000, 12000)
    BeginChrThread(0x18, 0, 0, 97)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 4000, 15000, 15, 0, 0, 1100, 1200, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(5000)
    BeginChrThread(0x8, 1, 0, 81)
    BeginChrThread(0x9, 1, 0, 81)
    BeginChrThread(0x101, 0, 0, 82)
    BeginChrThread(0x101, 1, 0, 84)
    WaitChrThread(0x101, 0)
    OP_11(0x0, 0x0, 0x0, 0x1E, 0x32, 0x1388)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    EndChrThread(0x18, 0xFF)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    PlayEffect(0x4, 0xFF, 0x14, 0x40, 0, 800, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x13, 0x40, 0, 800, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 0, 0, 83)
    BeginChrThread(0x101, 1, 0, 85)
    OP_68(10, 2900, 25450, 12000)
    MoveCamera(0, 30, 0, 12000)
    OP_6E(740, 12000)
    SetCameraDistance(18500, 12000)
    BeginChrThread(0x8, 0, 0, 90)
    BeginChrThread(0x9, 0, 0, 90)
    BeginChrThread(0x18, 1, 0, 90)

    def lambda_8F20():
        OP_95(0xF, 0, 1500, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8F20)
    Sleep(7000)

    def lambda_8F3D():
        OP_95(0xE, 0, 1500, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8F3D)
    Sleep(1000)

    def lambda_8F5A():
        OP_95(0xD, -3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_8F5A)
    Sleep(1000)

    def lambda_8F77():
        OP_95(0xC, 3500, 1500, 25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8F77)
    WaitChrThread(0xE, 0)
    OP_93(0xE, 0x0, 0x1F4)
    WaitChrThread(0x18, 1)
    OP_82(0x0, 0xC8, 0x7D0, 0xC8)
    BeginChrThread(0x8, 0, 0, 93)
    BeginChrThread(0x9, 0, 0, 94)
    Sleep(1200)
    OP_D3(0x18, 0x0, 0xAFC8, 0x0, 0x1388)
    OP_D3(0x18, 0x0, 0x16B48, 0x0, 0x7D0)

    def lambda_8FE6():
        OP_96(0xC, 0xDAC, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8FE6)

    def lambda_9000():
        OP_96(0xD, 0xFFFFF254, 0x1D4C, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_9000)

    def lambda_901A():
        OP_96(0xE, 0x0, 0x1D4C, 0x53FC, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_901A)

    def lambda_9034():
        OP_96(0xF, 0x0, 0x1D4C, 0x6F54, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_9034)

    def lambda_904E():

        label("loc_904E")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_904E")

    QueueWorkItem2(0xC, 2, lambda_904E)

    def lambda_906E():

        label("loc_906E")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_906E")

    QueueWorkItem2(0xD, 2, lambda_906E)

    def lambda_908E():

        label("loc_908E")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_908E")

    QueueWorkItem2(0xE, 2, lambda_908E)

    def lambda_90AE():

        label("loc_90AE")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0xDF2, 0x1)
        Yield()
        Jump("loc_90AE")

    QueueWorkItem2(0xF, 2, lambda_90AE)
    BeginChrThread(0xC, 1, 0, 79)
    BeginChrThread(0xD, 1, 0, 79)
    BeginChrThread(0xE, 1, 0, 79)
    BeginChrThread(0xF, 1, 0, 79)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x1000)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x1000)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x1000)
    SetChrChipByIndex(0xC, 0x3C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x3D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x3E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x3F)
    SetChrSubChip(0xF, 0x0)

    def lambda_912E():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_912E)
    BeginChrThread(0x18, 1, 0, 86)
    Sleep(2000)
    OP_68(0, 9500, 22670, 30000)
    SetCameraDistance(18000, 25000)
    BeginChrThread(0x10, 0, 0, 87)
    BeginChrThread(0x11, 0, 0, 88)
    BeginChrThread(0x12, 0, 0, 89)
    Sleep(13000)
    OP_68(0, 12000, 22670, 8000)
    MoveCamera(0, 10, 0, 13000)
    OP_6E(640, 14000)
    SetCameraDistance(13000, 14000)
    Sleep(12000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x101, 0x2)
    OP_68(-27390, 16850, 6230, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_11(0x0, 0x0, 0x0, 0x28, 0x96, 0x0)
    SetChrPos(0x101, -27230, 15100, 7870, 300)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xA, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -26230, 15050, 6870, 300)
    SetChrChipByIndex(0x102, 0x2F)
    SetChrSubChip(0x102, 0x2)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    SetChrPos(0x1F, -26700, 15200, 6600, 0)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x30)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1A, -24860, 15200, 3960, 290)
    SetChrChipByIndex(0x1A, 0x31)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_E6()

    ChrTalk(
        0x102,
        "#2201701V#0108F#12P#40WThat was amazing...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x1F, 0x1)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x1F, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)

    NpcTalk(
        0x1F,
        "Old Man's Voice",
        "#2201702V#6P#50WHaha, I'm thoroughly impressed as well.\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x102, 0x0)

    ChrTalk(
        0x102,
        (
            "#2201703V#0105F#11PG-Grandfather!\x02\x03",
            "#2201704V#0102FYou're already awake?! Thank Aidios!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#2201705V#2503F#6P#40WYes. I'm perfectly fine, Elie.\x02\x03",
            "#2201706V#2500FIt's unfortunate what just happened, but I\x01",
            "still intend to experience the performance\x01",
            "with my own two eyes.\x02\x03",
            "#2201707VThis is my way of paying respect to the\x01",
            "wonderful people of Arc en Ciel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201708V#0106F#11PGrandfather...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#2201709VYou honor us, sir.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(10000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(881, 0, 100, 0)
    Sleep(1000)
    OP_24(0x370)
    StopBGM(0x1F40)
    WaitBGM()
    EndChrThread(0x22, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5B, 0)), scpexpr(EXPR_END)), "loc_9545")
    ClearScenarioFlags(0x5B, 0)
    OP_24(0x370)
    OP_B7(0x0)
    Return()

    label("loc_9545")

    OP_24(0x370)
    SetScenarioFlags(0x5D, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_95_85D8 end

    def Function_96_9555(): pass

    label("Function_96_9555")

    Sleep(500)
    Sound(875, 0, 100, 0)
    Sleep(500)
    Sound(880, 2, 0, 0)
    Sleep(200)
    OP_25(0x370, 0xA)
    Sleep(200)
    OP_25(0x370, 0x14)
    Sleep(200)
    OP_25(0x370, 0x1E)
    Sleep(200)
    OP_25(0x370, 0x28)
    Sleep(200)
    OP_25(0x370, 0x32)
    Sleep(200)
    OP_25(0x370, 0x3C)
    Sleep(200)
    OP_25(0x370, 0x46)
    Sleep(200)
    OP_25(0x370, 0x50)
    Sleep(200)
    OP_25(0x370, 0x5A)
    Sleep(200)
    OP_25(0x370, 0x64)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(7000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(12000)
    Sound(876, 0, 100, 0)
    Sleep(8000)
    Sound(874, 0, 100, 0)
    Sleep(1000)
    Sound(875, 0, 100, 0)
    Sleep(19500)
    Sound(881, 0, 100, 0)
    Sleep(4000)
    Sound(876, 0, 100, 0)
    Return()

    # Function_96_9555 end

    def Function_97_95FF(): pass

    label("Function_97_95FF")

    SetChrPos(0x18, 0, 12000, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)

    label("loc_9623")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_97F5")

    def lambda_9633():
        OP_96(0xFE, 0xFFFFFA24, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9633)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF830, 0x3E8)

    def lambda_9660():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9660)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF63C, 0x1F4)

    def lambda_968D():
        OP_96(0xFE, 0xFFFFFA24, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_968D)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF5D8, 0xFA)

    def lambda_96BA():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_96BA)
    OP_D3(0x18, 0x0, 0x0, 0xFFFFF7CC, 0xFA)

    def lambda_96E7():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_96E7)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)

    def lambda_9714():
        OP_96(0xFE, 0x5DC, 0x2E18, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9714)
    OP_D3(0x18, 0x0, 0x0, 0x7D0, 0x3E8)

    def lambda_9741():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0xAA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9741)
    OP_D3(0x18, 0x0, 0x0, 0x9C4, 0x1F4)

    def lambda_976E():
        OP_96(0xFE, 0x5DC, 0x2E7C, 0x61A8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_976E)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_979B():
        OP_96(0xFE, 0x0, 0x2E18, 0x61A8, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_979B)
    OP_D3(0x18, 0x0, 0x0, 0x834, 0xFA)

    def lambda_97C8():
        OP_96(0xFE, 0x0, 0x2DB4, 0x61A8, 0x15E, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_97C8)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x2EE)
    Jump("loc_9623")

    label("loc_97F5")

    Return()

    # Function_97_95FF end

    def Function_98_97F6(): pass

    label("Function_98_97F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DC0")
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    BeginChrThread(0x8, 2, 0, 9)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x8, 1, 0, 68)
    OP_9D(0x8, 0xFFFFFE0C, 0x2EE0, 0x61A8, 0x7D0, 0x1388)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, -4000, 12000, 23000)
    OP_9F(0x1, -4000, 12000, 27000)
    OP_9F(0x1, -500, 12000, 25000)
    OP_9F(0x2, 0x8, 10000, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x8, 0xFFFFF830, 0x61A8, 0x57E40, 0x2EE0, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9F(0x0, 0x8)
    OP_9F(0x1, -3000, 14000, 25000)
    OP_9F(0x1, -3000, 10000, 25000)
    OP_9F(0x1, -500, 12000, 25000)
    OP_9F(0x2, 0x8, 10000, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x8, 0xFFFFF830, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0x8, 0x0, 0x61A8, 0x57E40, 0x1770, 0x0)
    OP_9E(0x8, 0xFFFFEC78, 0x61A8, 0xFFFA81C0, 0x1B58, 0x0)
    OP_9E(0x8, 0xFFFFEC78, 0x61A8, 0xFFFBE150, 0x2328, 0x0)
    OP_96(0x8, 0xFFFFFE0C, 0x2EE0, 0x61A8, 0x2328, 0x0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 180, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 11900, 25000, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9D(0x8, 0xFFFFEC0A, 0x34BC, 0x70E4, 0xBB8, 0xBB8)
    EndChrThread(0x8, 0x3)
    TurnDirection(0x8, 0x9, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1F)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x1000)
    OP_9E(0x8, 0x0, 0x61A8, 0xABE0, 0x1B58, 0x1)
    Jump("Function_98_97F6")

    label("loc_9DC0")

    Return()

    # Function_98_97F6 end

    def Function_99_9DC1(): pass

    label("Function_99_9DC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9F3F")
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    BeginChrThread(0x9, 2, 0, 17)
    BeginChrThread(0x9, 3, 0, 20)
    BeginChrThread(0x9, 1, 0, 68)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x1388)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, 4000, 12000, 23000)
    OP_9F(0x1, 4000, 12000, 27000)
    OP_9F(0x1, 500, 12000, 25000)
    OP_9F(0x2, 0x9, 10000, 0x0)
    OP_9E(0x9, 0x7D0, 0x61A8, 0x57E40, 0x2EE0, 0x0)
    OP_9F(0x0, 0x9)
    OP_9F(0x1, 3000, 10000, 25000)
    OP_9F(0x1, 3000, 14000, 25000)
    OP_9F(0x1, 500, 12000, 25000)
    OP_9F(0x2, 0x9, 10000, 0x0)
    OP_9E(0x9, 0x7D0, 0x61A8, 0x2BF20, 0x2328, 0x0)
    OP_9E(0x9, 0x0, 0x61A8, 0x57E40, 0x1770, 0x0)
    OP_9E(0x9, 0x1388, 0x61A8, 0xFFFA81C0, 0x1B58, 0x0)
    OP_9E(0x9, 0x1388, 0x61A8, 0xFFFBE150, 0x2328, 0x0)
    OP_96(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x2328, 0x0)
    OP_9D(0x9, 0x13F6, 0x34BC, 0x70E4, 0xBB8, 0xBB8)
    EndChrThread(0x9, 0x3)
    TurnDirection(0x9, 0x8, 0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x29)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x1000)
    OP_9E(0x9, 0x0, 0x61A8, 0xFFFF5420, 0x1B58, 0x1)
    Jump("Function_99_9DC1")

    label("loc_9F3F")

    Return()

    # Function_99_9DC1 end

    def Function_100_9F40(): pass

    label("Function_100_9F40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SoundLoad(873)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -5110, 13500, 28900, 90)
    SetChrPos(0x9, 5110, 13500, 28900, 270)
    LoadEffect(0x0, "event\\ev290_01.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x7, "event\\ev290_05.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    SetMapObjFrame(0x3, "ball", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Bback", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetChrPos(0x18, 0, 17500, 25000, 0)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x1A, 0x64, 0x0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 6500, 25000, 15, 0, 0, 1100, 1400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 6500, 15000, 15, 0, 0, 1100, 1400, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 20000, 25000, 90, 180, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(0, 8300, 22670, 0)
    MoveCamera(0, -5, 30, 0)
    OP_6E(540, 0)
    SetCameraDistance(22000, 0)
    OP_68(0, 14100, 22670, 14000)
    MoveCamera(0, -12, 20, 18000)
    OP_6E(540, 14000)
    SetCameraDistance(17000, 18000)
    BeginChrThread(0x101, 0, 0, 99)
    BeginChrThread(0x101, 1, 0, 98)
    PlayBGM("ed7504", 1)
    BeginChrThread(0x22, 1, 0, 101)
    FadeToBright(5000, 0)
    OP_0D()
    Sleep(4000)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_11(0x0, 0x0, 0x0, 0x32, 0x78, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x32)
    SetChrChipByIndex(0x1C, 0x32)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -50, 15200, -6400, 0)
    SetChrPos(0x101, 13000, 15200, -8300, 0)
    SetChrPos(0x102, 13000, 15200, -8700, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    BeginChrThread(0x18, 2, 0, 120)
    OP_68(-290, 11930, 27720, 0)
    MoveCamera(347, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(52500, 0)
    SetCameraDistance(57500, 3500)
    Fade(500)
    Sleep(1000)

    def lambda_A5B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5B2)

    def lambda_A5C3():
        OP_95(0xFE, -13000, 15200, -8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A5C3)
    Sleep(500)
    MoveCamera(8, 9, 4, 6000)

    def lambda_A5EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A5EB)

    def lambda_A5FC():
        OP_95(0xFE, -13000, 15200, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A5FC)
    Sleep(2000)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A634():

        label("loc_A634")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A634")

    QueueWorkItem2(0x1C, 0, lambda_A634)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#2201611V#0605F#11P#10AWhat?!\x02",
    )

    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x22, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x369)
    SetScenarioFlags(0x5E, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_100_9F40 end

    def Function_101_A696(): pass

    label("Function_101_A696")

    Sleep(500)
    Sound(873, 2, 100, 0)
    Sleep(2000)
    Sound(872, 0, 100, 0)
    Sleep(4500)
    Sound(874, 0, 100, 0)
    Sleep(8000)
    OP_25(0x369, 0x5A)
    Sleep(100)
    OP_25(0x369, 0x50)
    Sleep(100)
    OP_25(0x369, 0x46)
    Sleep(100)
    OP_25(0x369, 0x3C)
    Sleep(100)
    OP_25(0x369, 0x32)
    Sleep(100)
    OP_25(0x369, 0x28)
    Sleep(100)
    OP_25(0x369, 0x1E)
    Sleep(100)
    OP_25(0x369, 0x14)
    Sleep(100)
    OP_25(0x369, 0xA)
    Sleep(100)
    OP_24(0x369)
    Return()

    # Function_101_A696 end

    def Function_102_A6F7(): pass

    label("Function_102_A6F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SoundLoad(869)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_68(-5940, 2550, 10180, 0)
    MoveCamera(21, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22000, 0)
    OP_68(830, 4340, 340, 8000)
    MoveCamera(345, 19, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(22000, 8000)
    BeginChrThread(0x22, 0, 0, 103)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    EndChrThread(0x22, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(7600, 14840, -2520, 0)
    MoveCamera(4, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(9650, 16290, -2200, 8000)
    MoveCamera(18, 21, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(20500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    BeginChrThread(0x22, 0, 0, 104)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x22, 0)
    OP_24(0x365)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_102_A6F7 end

    def Function_103_AAED(): pass

    label("Function_103_AAED")

    Sound(869, 2, 0, 0)
    Sleep(100)
    OP_25(0x365, 0xA)
    Sleep(100)
    OP_25(0x365, 0x14)
    Sleep(100)
    OP_25(0x365, 0x1E)
    Sleep(100)
    OP_25(0x365, 0x28)
    Sleep(100)
    OP_25(0x365, 0x32)
    Sleep(100)
    OP_25(0x365, 0x3C)
    Sleep(100)
    OP_25(0x365, 0x46)
    Sleep(100)
    OP_25(0x365, 0x50)
    Sleep(100)
    OP_25(0x365, 0x5A)
    Sleep(100)
    OP_25(0x365, 0x64)
    Return()

    # Function_103_AAED end

    def Function_104_AB3A(): pass

    label("Function_104_AB3A")

    OP_25(0x365, 0x5A)
    Sleep(100)
    OP_25(0x365, 0x50)
    Sleep(100)
    OP_25(0x365, 0x46)
    Sleep(100)
    OP_25(0x365, 0x3C)
    Sleep(100)
    OP_25(0x365, 0x32)
    Sleep(100)
    OP_25(0x365, 0x28)
    Sleep(100)
    OP_25(0x365, 0x1E)
    Sleep(100)
    OP_25(0x365, 0x14)
    Sleep(100)
    OP_25(0x365, 0xA)
    Sleep(100)
    OP_24(0x365)
    Return()

    # Function_104_AB3A end

    def Function_105_AB7D(): pass

    label("Function_105_AB7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ABEE")
    OP_7D(0xFF, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xC8, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABC0")
    Sleep(500)
    Jump("loc_ABE9")

    label("loc_ABC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABD7")
    Sleep(300)
    Jump("loc_ABE9")

    label("loc_ABD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABE9")
    Sleep(100)

    label("loc_ABE9")

    Jump("Function_105_AB7D")

    label("loc_ABEE")

    Return()

    # Function_105_AB7D end

    def Function_106_ABEF(): pass

    label("Function_106_ABEF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 105)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_68(-14360, 3000, 14280, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22000, 0)
    OP_68(-5170, 3000, 8070, 5000)
    MoveCamera(49, 25, 0, 5000)
    OP_6E(650, 5000)
    SetCameraDistance(22000, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADC9")
    SetScenarioFlags(0x5C, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_ADD2")

    label("loc_ADC9")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_ADD2")

    Return()

    # Function_106_ABEF end

    def Function_107_ADD3(): pass

    label("Function_107_ADD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE44")
    OP_7D(0xC8, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0xA0, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE16")
    Sleep(500)
    Jump("loc_AE3F")

    label("loc_AE16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE2D")
    Sleep(300)
    Jump("loc_AE3F")

    label("loc_AE2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3F")
    Sleep(100)

    label("loc_AE3F")

    Jump("Function_107_ADD3")

    label("loc_AE44")

    Return()

    # Function_107_ADD3 end

    def Function_108_AE45(): pass

    label("Function_108_AE45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 107)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    LoadEffect(0x6, "event\\ev291_00.eff")
    LoadEffect(0x4, "event\\ev291_01.eff")
    LoadEffect(0x5, "event\\ev292_00.eff")
    LoadEffect(0x7, "event\\ev291_05.eff")
    SetMapObjFrame(0xFF, "yuka", 0x0, 0x1)
    BeginChrThread(0x101, 2, 0, 45)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, 1000, 15000, 15, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-260, 3900, 3530, 0)
    MoveCamera(353, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(-260, 3900, 2530, 8000)
    MoveCamera(377, 28, 0, 8000)
    OP_6E(700, 8000)
    SetCameraDistance(15000, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F3")
    SetScenarioFlags(0x5C, 5)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B0FC")

    label("loc_B0F3")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_B0FC")

    Return()

    # Function_108_AE45 end

    def Function_109_B0FD(): pass

    label("Function_109_B0FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B16E")
    OP_7D(0xC8, 0xFF, 0xC8, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x8C, 0xC8, 0x8C, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B140")
    Sleep(500)
    Jump("loc_B169")

    label("loc_B140")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B157")
    Sleep(300)
    Jump("loc_B169")

    label("loc_B157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B169")
    Sleep(100)

    label("loc_B169")

    Jump("Function_109_B0FD")

    label("loc_B16E")

    Return()

    # Function_109_B0FD end

    def Function_110_B16F(): pass

    label("Function_110_B16F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BeginChrThread(0x101, 2, 0, 109)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30200.itc", 0x20)
    LoadChrToIndex("chr/ch30300.itc", 0x21)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1B, -7310, 0, 18690, 156)
    SetChrPos(0x1D, -6330, 2700, 910, 21)
    SetChrPos(0x1E, 2650, 2700, 150, 336)
    SetChrPos(0x1C, 10390, 15200, -1250, 333)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_68(-1740, 1780, 22680, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(690, 0)
    SetCameraDistance(35500, 0)
    OP_68(-1740, 1780, 22680, 8000)
    MoveCamera(28, 20, 0, 8000)
    OP_6E(690, 8000)
    SetCameraDistance(35500, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B349")
    SetScenarioFlags(0x5C, 6)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B352")

    label("loc_B349")

    NewScene("c0410", 101, 0, 0)
    IdleLoop()

    label("loc_B352")

    Return()

    # Function_110_B16F end

    def Function_111_B353(): pass

    label("Function_111_B353")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 860, 15200, -9740, 357)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0xC8, 0xC8, 0x8C, 0x0, 0x0)
    OP_68(-3760, 16850, -7210, 0)
    MoveCamera(59, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(3700, 16850, -6690, 5000)
    MoveCamera(59, 18, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17500, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B689")
    SetScenarioFlags(0x5C, 7)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_B6B2")

    label("loc_B689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_B6A0")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_B6B2")

    label("loc_B6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_B6B2")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_B6B2")

    Return()

    # Function_111_B353 end

    def Function_112_B6B3(): pass

    label("Function_112_B6B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 60, 15200, -8580, 360)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0x8C, 0xC8, 0xFF, 0x0, 0x0)
    OP_68(3520, 17240, -8490, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(-3560, 17240, -8490, 5000)
    MoveCamera(0, 14, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(20500, 5000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x1C, 0x50, 0x1F4)
    Sleep(400)
    OP_93(0x1C, 0x118, 0x1F4)
    OP_93(0x1C, 0x50, 0x1F4)
    Sleep(2000)
    OP_93(0x1C, 0x118, 0x1F4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA08")
    SetScenarioFlags(0x5D, 0)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BA31")

    label("loc_BA08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_BA1F")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_BA31")

    label("loc_BA1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_BA31")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_BA31")

    Return()

    # Function_112_B6B3 end

    def Function_113_BA32(): pass

    label("Function_113_BA32")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-40, 15800, -7080, 0)
    MoveCamera(48, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("chr/ch27802.itc", 0x33)
    LoadChrToIndex("chr/ch27902.itc", 0x34)
    LoadChrToIndex("chr/ch33002.itc", 0x35)
    LoadChrToIndex("chr/ch33302.itc", 0x36)
    LoadChrToIndex("chr/ch27702.itc", 0x37)
    LoadChrToIndex("chr/ch27602.itc", 0x38)
    LoadChrToIndex("chr/ch33202.itc", 0x39)
    LoadChrToIndex("chr/ch33102.itc", 0x3A)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -6740, 15250, -5800, 6)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -7950, 15250, -3430, 18)
    SetChrChipByIndex(0xE, 0x35)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -5820, 15250, -5920, 8)
    SetChrChipByIndex(0xF, 0x36)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -3960, 15250, -3940, 8)
    SetChrChipByIndex(0x10, 0x37)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2930, 15250, -4190, 8)
    SetChrChipByIndex(0x11, 0x38)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2140, 15250, -4280, 8)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2140, 15250, -4280, 6)
    SetChrChipByIndex(0x13, 0x3A)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2930, 15250, -4190, 6)
    SetChrChipByIndex(0x14, 0x33)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 6870, 15250, -3670, 348)
    SetChrChipByIndex(0x15, 0x34)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 7840, 15250, -3470, 348)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 1080, 15200, -7180, 358)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_7D(0x8C, 0xC8, 0xC8, 0x0, 0x0)
    OP_68(930, 16850, -7260, 0)
    MoveCamera(28, 12, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(930, 16850, -7260, 5000)
    MoveCamera(37, 12, 0, 5000)
    OP_6E(380, 5000)
    SetCameraDistance(20500, 5000)
    OP_63(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDA8")
    SetScenarioFlags(0x5D, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BDD1")

    label("loc_BDA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_BDBF")
    NewScene("c0410", 106, 0, 0)
    IdleLoop()
    Jump("loc_BDD1")

    label("loc_BDBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 3)), scpexpr(EXPR_END)), "loc_BDD1")
    NewScene("c0410", 108, 0, 0)
    IdleLoop()

    label("loc_BDD1")

    Return()

    # Function_113_BA32 end

    def Function_114_BDD2(): pass

    label("Function_114_BDD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -24350, 15200, 2810, 1)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xC8, 0xC8, 0x8C, 0x0, 0x0)
    OP_68(-25840, 16850, 6000, 0)
    MoveCamera(100, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-26000, 16850, 8000, 6000)
    MoveCamera(75, 24, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(19500, 6000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFC2")
    SetScenarioFlags(0x5D, 2)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_BFCB")

    label("loc_BFC2")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_BFCB")

    Return()

    # Function_114_BDD2 end

    def Function_115_BFCC(): pass

    label("Function_115_BFCC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -24260, 15200, 4830, 45)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0x8C, 0xC8, 0xFF, 0x0, 0x0)
    OP_68(-26720, 16850, 8400, 0)
    MoveCamera(68, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-25060, 16850, 5820, 8000)
    MoveCamera(56, 24, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(19500, 8000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1CE")
    SetScenarioFlags(0x5D, 3)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_C1D7")

    label("loc_C1CE")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_C1D7")

    Return()

    # Function_115_BFCC end

    def Function_116_C1D8(): pass

    label("Function_116_C1D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-25620, 15800, 6780, 0)
    MoveCamera(28, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch30000.itc", 0x20)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -25480, 15200, 9430, 62)
    SetChrChipByIndex(0x20, 0x1F)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27330, 15200, 9810, 69)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -21760, 15200, 6080, 45)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_7D(0x8C, 0xC8, 0xC8, 0x0, 0x0)
    LoadEffect(0x3, "event\\ev292_03.eff")
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1100, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(-25230, 16850, 7010, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(-25230, 16850, 7010, 10000)
    MoveCamera(56, 10, 0, 10000)
    OP_6E(500, 10000)
    SetCameraDistance(16500, 10000)
    VolumeBGM(0x64, 0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C454")
    SetScenarioFlags(0x5D, 4)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_C45D")

    label("loc_C454")

    NewScene("c0410", 115, 0, 0)
    IdleLoop()

    label("loc_C45D")

    Return()

    # Function_116_C1D8 end

    def Function_117_C45E(): pass

    label("Function_117_C45E")

    SetChrChipByIndex(0xFE, 0x33)
    Sound(808, 0, 100, 0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1662, 0x2710, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    Sound(533, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    def lambda_C49F():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C49F)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1F40, 0x0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x5, 0xFF, 0xFE, 0x40, -1300, 2000, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(511, 0, 100, 0)
    Sound(830, 0, 100, 0)
    Sound(1876, 255, 100, 1)
    BeginChrThread(0x18, 0, 0, 118)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x1000)

    def lambda_C52A():
        OP_96(0xFE, 0xFFFF969C, 0x3B60, 0x23A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_C52A)
    SetChrChipByIndex(0x20, 0x2F)
    SetChrSubChip(0x20, 0x0)
    OP_96(0xFE, 0xFFFF95F2, 0x3B60, 0x1A4A, 0x1388, 0x0)
    Sound(532, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x32)

    def lambda_C56E():

        label("loc_C56E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_C56E")

    QueueWorkItem2(0xFE, 2, lambda_C56E)
    Return()

    # Function_117_C45E end

    def Function_118_C57C(): pass

    label("Function_118_C57C")

    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x18, 3, 0, 18)
    OP_9D(0x18, 0xFFFF8D64, 0x38A4, 0x292C, 0xBB8, 0xBB8)
    Sound(878, 0, 100, 0)
    SetChrFlags(0x18, 0x2)
    SetChrSubChip(0x18, 0x4)
    Return()

    # Function_118_C57C end

    def Function_119_C5B8(): pass

    label("Function_119_C5B8")

    OP_95(0xFE, -25200, 15200, 6000, 5000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_119_C5B8 end

    def Function_120_C5D4(): pass

    label("Function_120_C5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C645")
    OP_7D(0x50, 0xFF, 0xFF, 0x0, 0x64)
    Sleep(200)
    OP_7D(0x50, 0xC8, 0xC8, 0x0, 0xC8)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C617")
    Sleep(500)
    Jump("loc_C640")

    label("loc_C617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C62E")
    Sleep(300)
    Jump("loc_C640")

    label("loc_C62E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C640")
    Sleep(100)

    label("loc_C640")

    Jump("Function_120_C5D4")

    label("loc_C645")

    Return()

    # Function_120_C5D4 end

    def Function_121_C646(): pass

    label("Function_121_C646")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFC1800, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xBB8, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch05800.itc", 0x1F)
    LoadChrToIndex("chr/ch02300.itc", 0x20)
    LoadChrToIndex("apl/ch50241.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("chr/ch00951.itc", 0x23)
    LoadChrToIndex("apl/ch50223.itc", 0x28)
    LoadChrToIndex("apl/ch50234.itc", 0x29)
    LoadChrToIndex("apl/ch50225.itc", 0x2A)
    LoadChrToIndex("apl/ch50226.itc", 0x2B)
    LoadChrToIndex("apl/ch50240.itc", 0x2C)
    LoadChrToIndex("apl/ch50228.itc", 0x2D)
    LoadChrToIndex("apl/ch50229.itc", 0x2E)
    LoadChrToIndex("apl/ch50230.itc", 0x2F)
    LoadChrToIndex("chr/ch00050.itc", 0x32)
    LoadChrToIndex("chr/ch00051.itc", 0x33)
    LoadChrToIndex("chr/ch00052.itc", 0x34)
    LoadChrToIndex("chr/ch00150.itc", 0x37)
    LoadChrToIndex("chr/ch00156.itc", 0x38)
    BeginChrThread(0x18, 2, 0, 120)
    LoadEffect(0x7, "event\\ev290_05.eff")
    LoadEffect(0x6, "event\\ev292_04.eff")
    LoadEffect(0x5, "event\\eva01_01.eff")
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 20000, 25000, 90, 180, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, -27150, 15700, 8660, 225)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, -27900, 15200, 2620, 0)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -28000, 15200, 8400, 270)
    SetChrChipByIndex(0x20, 0x28)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -27000, 15200, 8500, 270)
    SetChrPos(0x101, -26770, 15200, 920, 0)
    SetChrPos(0x102, -25520, 15200, 650, 0)

    def lambda_C892():
        OP_96(0xFE, 0xFFFF976E, 0x3B60, 0xB68, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C892)

    def lambda_C8AC():
        OP_96(0xFE, 0xFFFF9C50, 0x3B60, 0xA5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C8AC)
    OP_68(-26750, 16850, 3330, 0)
    MoveCamera(30, 28, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(19500, 0)
    OP_68(-27740, 16440, 8450, 2000)
    MoveCamera(30, 28, 0, 2000)
    OP_6E(320, 2000)
    SetCameraDistance(23500, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sleep(400)
    SetChrSubChip(0x20, 0x2)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 80, 0)
    Sleep(500)
    OP_0D()

    ChrTalk(
        0x102,
        "#2201619V#0110F...?!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 0x3)
    Sleep(300)

    ChrTalk(
        0x20,
        "#2201620V#2611F#5POh?\x02",
    )

    CloseMessageWindow()
    Sound(1091, 255, 100, 0)
    Sleep(1000)
    Sound(1011, 255, 100, 0)
    SetCameraDistance(28500, 2000)
    BeginChrThread(0x101, 0, 0, 117)
    WaitChrThread(0x101, 0)
    Sleep(300)

    ChrTalk(
        0x20,
        "#2201622V#2614FDamn!\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    SetChrPos(0x20, -27250, 15200, 8650, 225)
    Sleep(200)
    Fade(500)
    SetChrPos(0x20, -27500, 15200, 8800, 270)
    SetChrChipByIndex(0x20, 0x20)
    Sound(804, 0, 100, 0)
    OP_93(0x20, 0xB4, 0x0)
    ClearChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x0, 0x0)
    Sleep(300)
    OP_68(-27030, 16850, 8000, 4000)
    MoveCamera(47, 22, 0, 4000)
    OP_6E(460, 4000)
    SetCameraDistance(20500, 4000)

    def lambda_CA47():
        OP_9D(0xFE, 0xFFFF9494, 0x3B60, 0x2968, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_CA47)

    def lambda_CA64():
        OP_9D(0xFE, 0xFFFF92A0, 0x3B60, 0x27D8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_CA64)
    Sound(814, 0, 100, 0)
    BeginChrThread(0x102, 0, 0, 119)
    WaitChrThread(0x20, 0)
    SetChrChipByIndex(0x20, 0x2D)
    SetChrSubChip(0x20, 0x0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x1F, 0x2C)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x2)

    ChrTalk(
        0x102,
        "#2201660V#0107FGrandfather!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201624V#0007FDamn it, he has a gun!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_95(0x1C, -28330, 15200, 5500, 5000, 0x0)
    OP_93(0x1C, 0x0, 0x320)
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1C,
        "#2201625V#0607FWh-What the hell is this?\x02",
    )

    CloseMessageWindow()
    MoveCamera(24, 31, 0, 30000)

    ChrTalk(
        0x20,
        (
            "#2201626V#2613FHeh. Who would've thought that you'd\x01",
            "show up in a place like this?\x02\x03",
            "#2201627V#2610FThis must be the Goddess' idea\x01",
            "of a blessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201628V#0108FErnest, why?!\x02\x03",
            "#2201629V#0107FWhy do all of this? You were always there\x01",
            "to support Grandfather... So why?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1899, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "#2201631V#2613FWe're cut from the same cloth, Elie.\x02\x03",
            "#2201632VYou have no idea how fed up I am with\x01",
            "Crossbell's sick situation.\x02\x03",
            "#2201633V#2611FAnd, in the end, man only pursues true\x01",
            "change when obeying the will of one\x01",
            "stronger than himself.\x02\x03",
            "#2201634V#2614FTHAT is why I had to act!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201635V#0003FSo that's the reason you impersonated Yin\x01",
            "and sent the threat letter to Ilya.\x02\x03",
            "#2201636V#0013FYou made us believe that Yin was behind\x01",
            "everything, all while plotting the mayor's\x01",
            "assassination from the shadows!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#2201637V#0603FDamn it! So that's what's really going on.\x02\x03",
            "#2201638V#0610FHave you enjoyed playing this game of\x01",
            "yours?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#2201639V#2613FHaha. You may hail from the First\x01",
            "Division, but in the end, you're\x01",
            "just a two-bit detective.\x02\x03",
            "#2201640VBe it Revache, Heiyue, or even\x01",
            "the real Yin, if he actually exists...\x02\x03",
            "#2201641V#2610FThey're nothing more than puppets\x01",
            "dancing in the palm of my hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#2201642V#0601FTch.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    EndChrThread(0x1C, 0x2)
    SetChrFlags(0x1C, 0x20)
    SetChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sound(1560, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1C,
        (
            "#2201644V#0603FPut the gun down, slowly.\x02\x03",
            "#2201645V#0601FYou can still get off with attempted\x01",
            "murder. Don't take it any further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#2201646V#2613F#5PDon't take it any further? Isn't that\x01",
            "my line?\x02\x03",
            "#2201647V#2610FThe life of this old, naive man, the\x01",
            "mayor of Crossbell State...\x02\x03",
            "#2201648V...I could end it with one swift pull\x01",
            "of this trigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201649V#0106FPlease, stop this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#2201650V#0610FPulling the hostage card, are we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#2201651V#2610F#5PSurely you don't want our dear Elie to\x01",
            "witness the moment her grandfather's\x01",
            "brain splatters on the floor, right?\x02\x03",
            "#2201652VSo, how about you ingrates line up on\x01",
            "the wall there and stay out of my way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201653V#0003FI'm having trouble figuring out your plan.\x02\x03",
            "#2201654V#0001FThe moment you step out of this theater,\x01",
            "there'll be nowhere to run.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x20,
        "#2201655V#2614F#5P#4SShut it! Just do as I say!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201656V#0013FBastard...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-27030, 16850, 6000, 4000)

    def lambda_D42B():

        label("loc_D42B")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_D42B")

    QueueWorkItem2(0x101, 2, lambda_D42B)

    def lambda_D43D():

        label("loc_D43D")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_D43D")

    QueueWorkItem2(0x102, 2, lambda_D43D)

    def lambda_D44F():

        label("loc_D44F")

        TurnDirection(0xFE, 0x20, 500)
        Yield()
        Jump("loc_D44F")

    QueueWorkItem2(0x1C, 2, lambda_D44F)
    ClearChrFlags(0x1C, 0x20)
    ClearChrFlags(0x1C, 0x2)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    Sound(531, 0, 100, 0)

    def lambda_D479():
        OP_96(0xFE, 0xFFFF9D90, 0x3B60, 0xE74, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D479)
    Sleep(500)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)

    def lambda_D4AA():
        OP_96(0xFE, 0xFFFF9B9C, 0x3B60, 0x14B4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D4AA)
    Sleep(500)

    def lambda_D4C7():
        OP_96(0xFE, 0xFFFFA04C, 0x3B60, 0x16A8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D4C7)
    WaitChrThread(0x1C, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7505", 0)

    ChrTalk(
        0x20,
        "#2201657V#2613F#5P#NGood. You have ears, after all.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x1F, 0x1000)

    def lambda_D530():

        label("loc_D530")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_D530")

    QueueWorkItem2(0x20, 1, lambda_D530)

    def lambda_D542():
        OP_97(0x20, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_D542)

    def lambda_D55C():
        OP_98(0x1F, 0x0, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_D55C)
    WaitChrThread(0x20, 0)
    EndChrThread(0x20, 0x1)
    TurnDirection(0x20, 0x101, 500)

    ChrTalk(
        0x20,
        "#2201658V#2614F#5PNow to hold up my end of the deal!\x02",
    )

    CloseMessageWindow()
    OP_68(-26670, 16850, 3880, 1000)
    MoveCamera(68, 27, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(19500, 1000)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x1F, 0x1)
    Sound(804, 0, 100, 0)
    OP_96(0x1F, 0xFFFF998A, 0x3B60, 0x16BC, 0x1F40, 0x0)

    def lambda_D60F():
        OP_96(0x1F, 0xFFFF9B9C, 0x3B60, 0x15E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_D60F)
    BeginChrThread(0x1F, 3, 0, 122)
    ClearChrFlags(0x20, 0x2)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x1000)
    SetChrChipByIndex(0x20, 0x2E)
    Sound(1904, 255, 100, 0)

    def lambda_D648():
        OP_95(0x20, -26690, 15200, 2410, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_D648)
    Sound(819, 0, 100, 0)
    OP_96(0x101, 0xFFFF9C00, 0x3B60, 0x1388, 0xFA0, 0x0)
    WaitChrThread(0x20, 0)

    def lambda_D680():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_D680)

    def lambda_D691():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_D691)
    WaitChrThread(0x20, 0)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x1C, 0xFF)
    OP_95(0x102, -25230, 15200, 5870, 3000, 0x0)
    Fade(500)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -25230, 15100, 5870, 300)
    SetChrFlags(0x1F, 0x2)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    Sound(820, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x38)
    SetChrSubChip(0x102, 0x0)

    ChrTalk(
        0x102,
        "#2201623V#0107F#11PGrandfather!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x20, 700)

    ChrTalk(
        0x101,
        "#2201661V#0007F#5PHold it!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    Sound(808, 0, 100, 0)
    OP_95(0x101, -26690, 15200, 2410, 6000, 0x0)

    def lambda_D775():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D775)

    def lambda_D786():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D786)

    ChrTalk(
        0x1C,
        "#2201662V#0607F#5PYou won't escape!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x23)
    Sound(531, 0, 100, 0)
    OP_95(0x1C, -26690, 15200, 2410, 6000, 0x0)

    def lambda_D7E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_D7E7)

    def lambda_D7F8():
        OP_95(0xFE, -26690, 15200, 1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_D7F8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1F9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 1)
    NewScene("c0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_121_C646 end

    def Function_122_D82E(): pass

    label("Function_122_D82E")

    WaitChrThread(0xFE, 0)
    SetChrSubChip(0x1F, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_122_D82E end

    def Function_123_D848(): pass

    label("Function_123_D848")

    OP_93(0x8, 0x87, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -500, 5500, 25000, 135)

    def lambda_D86D():

        label("loc_D86D")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_D86D")

    QueueWorkItem2(0x8, 2, lambda_D86D)
    Sleep(1)
    OP_96(0x8, 0xFFFFFE0C, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x8, 0x2)
    BeginChrThread(0x8, 2, 0, 7)
    ClearChrFlags(0x8, 0x1)
    OP_9D(0x8, 0xFFFFFE0C, 0x300C, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)

    label("loc_D8CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D8EC")
    OP_A1(0x8, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D8CE")

    label("loc_D8EC")

    Return()

    # Function_123_D848 end

    def Function_124_D8ED(): pass

    label("Function_124_D8ED")

    OP_93(0x9, 0xE1, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x2)
    SetChrPos(0x9, 500, 5500, 25000, 225)

    def lambda_D912():

        label("loc_D912")

        OP_9E(0xFE, 0x0, 0x61A8, 0x36EE80, 0x320, 0x3)
        Yield()
        Jump("loc_D912")

    QueueWorkItem2(0x9, 2, lambda_D912)
    Sleep(1)
    OP_96(0x9, 0x1F4, 0x2BC0, 0x61A8, 0x12C, 0x0)
    EndChrThread(0x9, 0x2)
    BeginChrThread(0x9, 2, 0, 15)
    ClearChrFlags(0x9, 0x1)
    OP_9D(0x9, 0x1F4, 0x2EE0, 0x61A8, 0x7D0, 0x7D0)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x6)

    label("loc_D977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D995")
    OP_A1(0x9, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_D977")

    label("loc_D995")

    Return()

    # Function_124_D8ED end

    def Function_125_D996(): pass

    label("Function_125_D996")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F8(0x14D)
    LoadChrToIndex("chr/ch00002.itc", 0x25)
    LoadChrToIndex("chr/ch07502.itc", 0x26)
    LoadChrToIndex("chr/ch21802.itc", 0x33)
    LoadChrToIndex("chr/ch21902.itc", 0x34)
    LoadChrToIndex("chr/ch22002.itc", 0x35)
    LoadChrToIndex("chr/ch22302.itc", 0x36)
    LoadChrToIndex("chr/ch22102.itc", 0x37)
    LoadChrToIndex("chr/ch33202.itc", 0x38)
    LoadChrToIndex("chr/ch27702.itc", 0x39)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 7850, 15250, -3320, 345)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 7000, 15250, -3560, 345)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0xC, 0x33)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 6400, 15250, -5600, 345)
    SetChrChipByIndex(0xD, 0x38)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 4800, 15250, -5840, 345)
    SetChrChipByIndex(0xE, 0x34)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 5600, 15250, -5720, 345)
    SetChrChipByIndex(0xF, 0x35)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 3600, 15250, -4000, 355)
    SetChrChipByIndex(0x10, 0x36)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 2700, 15250, -4090, 355)
    SetChrChipByIndex(0x11, 0x37)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1900, 15250, -4180, 355)
    SetChrChipByIndex(0x12, 0x39)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 8700, 15250, -3080, 345)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    LoadEffect(0x0, "event\\ev290_02.eff")
    LoadEffect(0x1, "event\\ev290_01.eff")
    LoadEffect(0x3, "event\\ev290_00.eff")
    LoadEffect(0x4, "event\\ev295_00.eff")
    LoadEffect(0x5, "event\\ev293_02.eff")
    LoadEffect(0x6, "event\\ev290_05.eff")
    LoadEffect(0x7, "event\\ev294_00.eff")
    SetMapObjFrame(0x3, "04moon_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water01", 0x0, 0x1)
    SetMapObjFrame(0x3, "02water02_add", 0x0, 0x1)
    SetMapObjFrame(0x3, "04Aback", 0x0, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 256, 256, 0xFFFFFFFF, 0x1, "cv_eff01.itp")
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xBB8, 0xFA0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x18)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    LoadChrToIndex("apl/ch50250.itc", 0x1E)
    LoadChrToIndex("apl/ch50251.itc", 0x1F)
    LoadChrToIndex("apl/ch50252.itc", 0x20)
    LoadChrToIndex("apl/ch50253.itc", 0x21)
    LoadChrToIndex("apl/ch50254.itc", 0x22)
    LoadChrToIndex("apl/ch50255.itc", 0x23)
    LoadChrToIndex("apl/ch50256.itc", 0x24)
    LoadChrToIndex("apl/ch50265.itc", 0x28)
    LoadChrToIndex("apl/ch50266.itc", 0x29)
    LoadChrToIndex("apl/ch50267.itc", 0x2A)
    LoadChrToIndex("apl/ch50268.itc", 0x2B)
    LoadChrToIndex("apl/ch50269.itc", 0x2C)
    LoadChrToIndex("apl/ch50270.itc", 0x2D)
    LoadChrToIndex("apl/ch50271.itc", 0x2E)
    LoadChrToIndex("apl/ch50289.itc", 0x2F)
    SoundLoad(880)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2F)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x2F)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x14, 0x2)
    SetChrFlags(0x15, 0x2)
    SetChrFlags(0x16, 0x2)
    SetChrPos(0x13, -5940, 5800, 24600, 180)
    SetChrPos(0x14, 5940, 5800, 24600, 180)
    SetChrPos(0x15, -5680, 7600, 26590, 180)
    SetChrPos(0x16, 5680, 7600, 26590, 180)
    PlayEffect(0x4, 0xFF, 0x14, 0x40, 0, 800, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x13, 0x40, 0, 800, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x15, 0x40, 0, 1000, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, -90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0x16, 0x40, 0, 1100, -350, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -6450, 1250, 24260, 90)
    SetChrPos(0x9, 6450, 1250, 24260, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x1)
    BeginChrThread(0x101, 3, 0, 80)
    BeginChrThread(0x101, 2, 0, 78)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x1000)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x1000)
    SetChrPos(0x18, 0, 12000, 25000, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 0, 1000, 25000, 90, 0, 0, 1500, 1600, 1500, 0xFF, 0, 0, 0, 0)
    OP_C9(0x0, 0x0, 0xFFF6D840, 0xFFFA2400, 0x0)
    OP_C9(0x0, 0x1, 0xDAC, 0xFA0, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_E5()
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x19)
    SetChrPos(0x19, 0, 18000, 24000, 0)
    OP_D3(0x19, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    SetChrPos(0x8, -500, 5100, 25000, 0)
    SetChrPos(0x9, 500, 5100, 25000, 0)
    OP_D3(0x18, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, 0, 4000, 25000, 0)
    BeginChrThread(0x8, 0, 0, 123)
    BeginChrThread(0x9, 0, 0, 124)

    def lambda_E0D7():
        OP_96(0x18, 0x0, 0x2710, 0x61A8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_E0D7)
    BeginChrThread(0x18, 1, 0, 86)
    OP_EE(0x0, 0x5)
    PlayBGM("ed7532", 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x22, 1, 0, 126)
    OP_68(7870, 17900, -3420, 0)
    MoveCamera(102, 7, 0, 0)
    OP_6E(1180, 0)
    SetCameraDistance(7000, 0)
    OP_68(7870, 17010, -3420, 5000)
    MoveCamera(102, 23, 0, 5000)
    OP_6E(1180, 5000)
    SetCameraDistance(7000, 5000)
    Sleep(3000)
    Fade(1500)
    OP_68(10, 8620, 25430, 0)
    MoveCamera(350, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40140, 0)
    OP_68(10, 10610, 25430, 15000)
    MoveCamera(350, 13, 0, 15000)
    OP_6E(380, 10000)
    SetCameraDistance(52000, 10000)
    Sleep(16000)

    def lambda_E1D1():
        OP_96(0x19, 0x0, 0x546, 0x5DC0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_E1D1)
    Sleep(5000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0x1770)
    WaitBGM()
    OP_EE(0x0, 0xA)
    OP_E6()
    OP_24(0x370)
    SetScenarioFlags(0x5C, 1)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_125_D996 end

    def Function_126_E21C(): pass

    label("Function_126_E21C")

    Sleep(1500)
    Sound(880, 2, 0, 0)
    Sleep(50)
    OP_25(0x370, 0xA)
    Sleep(50)
    OP_25(0x370, 0x14)
    Sleep(50)
    OP_25(0x370, 0x1E)
    Sleep(50)
    OP_25(0x370, 0x28)
    Sleep(50)
    OP_25(0x370, 0x32)
    Sleep(50)
    OP_25(0x370, 0x3C)
    Sleep(50)
    OP_25(0x370, 0x46)
    Sleep(50)
    OP_25(0x370, 0x50)
    Sleep(50)
    OP_25(0x370, 0x5A)
    Sleep(50)
    OP_25(0x370, 0x64)
    Sleep(17500)
    Sound(876, 0, 100, 0)
    Sleep(3000)
    Sound(875, 0, 100, 0)
    Sleep(2000)
    OP_25(0x370, 0x64)
    Sleep(50)
    OP_25(0x370, 0x5A)
    Sleep(50)
    OP_25(0x370, 0x50)
    Sleep(50)
    OP_25(0x370, 0x46)
    Sleep(50)
    OP_25(0x370, 0x3C)
    Sleep(50)
    OP_25(0x370, 0x32)
    Sleep(50)
    OP_25(0x370, 0x28)
    Sleep(50)
    OP_25(0x370, 0x1E)
    Sleep(50)
    OP_25(0x370, 0x14)
    Sleep(50)
    OP_25(0x370, 0xA)
    Sleep(50)
    OP_24(0x370)
    Return()

    # Function_126_E21C end

    SaveToFile()

Try(main)
