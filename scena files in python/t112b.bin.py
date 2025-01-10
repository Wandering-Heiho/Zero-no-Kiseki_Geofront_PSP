from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t112b.bin",                # FileName
        "t112b",                    # MapName
        "t112b",                    # Location
        0x0048,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 72, 0, 9, 0, 10],
    )

    BuildStringList((
        "t112b",                  # 0
        "Butler Leonard",         # 1
        "Roxanne",                # 2
        "Brenda",                 # 3
        "Elizabeth",              # 4
        "Lechter",                # 5
        "Guide Berkeley",         # 6
        "Mariabell",              # 7
        "Kilika",                 # 8
        "Imelda",                 # 9
        "Nikita",                 # 10
        "Man in Suit",            # 11
        "Man in Suit",            # 12
        "Invitee",                # 13
        "Invitee",                # 14
        "Invitee",                # 15
        "Invitee",                # 16
        "Invitee",                # 17
        "Invitee",                # 18
        "Invitee",                # 19
        "Invitee",                # 20
        "Invitee",                # 21
        "Invitee",                # 22
        "Invitee",                # 23
        "Invitee",                # 24
        "Invitee",                # 25
        "Invitee",                # 26
        "Invitee",                # 27
        "Invitee",                # 28
        "Invitee",                # 29
        "Don Marconi",            # 30
        "Speaker Hartmann",       # 31
        "Mariabell",              # 32
    ))

    AddCharChip((
        "chr/ch27500.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch39100.itc",                   # 03
        "chr/ch07400.itc",                   # 04
        "chr/ch27902.itc",                   # 05
        "chr/ch25800.itc",                   # 06
        "chr/ch33202.itc",                   # 07
        "chr/ch33002.itc",                   # 08
        "chr/ch05502.itc",                   # 09
        "chr/ch36200.itc",                   # 0A
        "chr/ch36100.itc",                   # 0B
        "chr/ch07302.itc",                   # 0C
        "chr/ch09002.itc",                   # 0D
        "chr/ch27702.itc",                   # 0E
        "chr/ch21602.itc",                   # 0F
        "chr/ch26902.itc",                   # 10
        "chr/ch21802.itc",                   # 11
        "chr/ch26802.itc",                   # 12
        "chr/ch21902.itc",                   # 13
        "chr/ch33002.itc",                   # 14
        "chr/ch21700.itc",                   # 15
        "chr/ch22002.itc",                   # 16
        "chr/ch32402.itc",                   # 17
        "chr/ch33302.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-2670,   0,       22700,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-1340,   0,       7380,    90,   385,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-39,     1000,    28479,   180,  385,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(9770,    4000,    5820,    180,  385,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9090,    4000,    20329,   225,  385,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6099,   0,       3190,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(2400,    150,     6599,    0,    469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-2400,   150,     11600,   0,    385,  0x0, 0,   12,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(4000,    150,     19100,   0,    469,  0x0, 0,   13,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-2400,   150,     9100,    0,    469,  0x0, 0,   18,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(-3660,   0,       1009,    0,    385,  0x0, 0,   10,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3819,    0,       1009,    0,    385,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4000,   150,     19100,   0,    469,  0x0, 0,   7,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(-2400,   150,     19100,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(5550,    150,     11600,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   26,  255,  0)
    DeclNpc(2400,    150,     11600,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   27,  255,  0)
    DeclNpc(2400,    150,     16600,   0,    469,  0x0, 0,   14,  0,   255, 255, 0,   28,  255,  0)
    DeclNpc(5550,    150,     16600,   0,    469,  0x0, 0,   15,  0,   255, 255, 0,   29,  255,  0)
    DeclNpc(-5599,   150,     16600,   0,    469,  0x0, 0,   24,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-4000,   150,     16600,   0,    469,  0x0, 0,   23,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-5599,   150,     6599,    0,    469,  0x0, 0,   8,   0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-5599,   150,     11600,   0,    469,  0x0, 0,   17,  0,   255, 255, 0,   33,  255,  0)
    DeclNpc(4000,    150,     9100,    0,    469,  0x0, 0,   17,  0,   255, 255, 0,   34,  255,  0)
    DeclNpc(5550,    150,     9100,    0,    469,  0x0, 0,   19,  0,   255, 255, 0,   35,  255,  0)
    DeclNpc(-4000,   150,     14100,   0,    469,  0x0, 0,   20,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(-2400,   150,     14100,   0,    469,  0x0, 0,   21,  0,   255, 255, 0,   37,  255,  0)
    DeclNpc(-4000,   150,     9100,    0,    469,  0x0, 0,   22,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(2400,    150,     14100,   0,    469,  0x0, 0,   8,   0,   255, 255, 0,   39,  255,  0)
    DeclNpc(4000,    150,     14100,   0,    469,  0x0, 0,   16,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2400,    -150,    6599,    0,    469,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_588",          # 00, 0
        "Function_1_640",          # 01, 1
        "Function_2_641",          # 02, 2
        "Function_3_832",          # 03, 3
        "Function_4_85D",          # 04, 4
        "Function_5_888",          # 05, 5
        "Function_6_8E9",          # 06, 6
        "Function_7_9CB",          # 07, 7
        "Function_8_A5D",          # 08, 8
        "Function_9_AEF",          # 09, 9
        "Function_10_BF9",         # 0A, 10
        "Function_11_C16",         # 0B, 11
        "Function_12_EAF",         # 0C, 12
        "Function_13_1181",        # 0D, 13
        "Function_14_12FD",        # 0E, 14
        "Function_15_1462",        # 0F, 15
        "Function_16_14D4",        # 10, 16
        "Function_17_1B29",        # 11, 17
        "Function_18_1BA8",        # 12, 18
        "Function_19_1DA5",        # 13, 19
        "Function_20_21EB",        # 14, 20
        "Function_21_2499",        # 15, 21
        "Function_22_252D",        # 16, 22
        "Function_23_26F5",        # 17, 23
        "Function_24_2826",        # 18, 24
        "Function_25_29E2",        # 19, 25
        "Function_26_2CB2",        # 1A, 26
        "Function_27_2E90",        # 1B, 27
        "Function_28_3069",        # 1C, 28
        "Function_29_3219",        # 1D, 29
        "Function_30_3361",        # 1E, 30
        "Function_31_34E7",        # 1F, 31
        "Function_32_371B",        # 20, 32
        "Function_33_38FE",        # 21, 33
        "Function_34_3AAA",        # 22, 34
        "Function_35_3D8F",        # 23, 35
        "Function_36_4016",        # 24, 36
        "Function_37_41A4",        # 25, 37
        "Function_38_4330",        # 26, 38
        "Function_39_44C2",        # 27, 39
        "Function_40_46BE",        # 28, 40
        "Function_41_4878",        # 29, 41
        "Function_42_4CBC",        # 2A, 42
        "Function_43_616E",        # 2B, 43
        "Function_44_61AB",        # 2C, 44
        "Function_45_6B2A",        # 2D, 45
        "Function_46_6B73",        # 2E, 46
        "Function_47_6BBC",        # 2F, 47
        "Function_48_6C05",        # 30, 48
        "Function_49_6C4E",        # 31, 49
        "Function_50_6C97",        # 32, 50
        "Function_51_6CE0",        # 33, 51
        "Function_52_6D29",        # 34, 52
        "Function_53_6D72",        # 35, 53
        "Function_54_6DBB",        # 36, 54
        "Function_55_6E04",        # 37, 55
        "Function_56_6E4D",        # 38, 56
        "Function_57_6E96",        # 39, 57
        "Function_58_6EDF",        # 3A, 58
        "Function_59_6F28",        # 3B, 59
        "Function_60_6F71",        # 3C, 60
        "Function_61_6FBA",        # 3D, 61
        "Function_62_7003",        # 3E, 62
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C8"),
        (1, "loc_5D4"),
        (2, "loc_5E0"),
        (3, "loc_5EC"),
        (4, "loc_5F8"),
        (5, "loc_604"),
        (6, "loc_610"),
        (SWITCH_DEFAULT, "loc_61C"),
    )


    label("loc_5C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_604")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_628")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_63F")

    Return()

    # Function_0_588 end

    def Function_1_640(): pass

    label("Function_1_640")

    Return()

    # Function_1_640 end

    def Function_2_641(): pass

    label("Function_2_641")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_831")
    OP_95(0xFE, -1340, 0, 9870, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 12360, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 15020, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 17340, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 19800, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 19800, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 17340, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 15020, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 12360, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 9870, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 1200, 0, 7380, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1340, 0, 7380, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_2_641")

    label("loc_831")

    Return()

    # Function_2_641 end

    def Function_3_832(): pass

    label("Function_3_832")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85C")
    OP_94(0xFE, 0xFFFFF3F8, 0x6A5E, 0xAB4, 0x73FA, 0x3E8)
    Sleep(300)
    Jump("Function_3_832")

    label("loc_85C")

    Return()

    # Function_3_832 end

    def Function_4_85D(): pass

    label("Function_4_85D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_887")
    OP_94(0xFE, 0x20E4, 0xD84, 0x2AC6, 0x1F72, 0x3E8)
    Sleep(300)
    Jump("Function_4_85D")

    label("loc_887")

    Return()

    # Function_4_85D end

    def Function_5_888(): pass

    label("Function_5_888")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E8")
    OP_95(0xFE, 5570, 0, 3190, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -6100, 0, 3190, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    Jump("Function_5_888")

    label("loc_8E8")

    Return()

    # Function_5_888 end

    def Function_6_8E9(): pass

    label("Function_6_8E9")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4990, 0, 24290, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 3140, 0, 31200, 45)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8680, 4000, 20780, 225)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 8140, 4000, 20220, 315)
    ClearChrFlags(0xD, 0x80)
    BeginChrThread(0xD, 0, 0, 5)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    Return()

    # Function_6_8E9 end

    def Function_7_9CB(): pass

    label("Function_7_9CB")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    Return()

    # Function_7_9CB end

    def Function_8_A5D(): pass

    label("Function_8_A5D")

    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x8000)
    Return()

    # Function_8_A5D end

    def Function_9_AEF(): pass

    label("Function_9_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B05")
    Event(0, 41)
    Jump("loc_B16")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    Event(0, 42)

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B25")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 44)

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B33")
    Jump("loc_BF5")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B6C")
    Call(0, 6)
    SetChrPos(0x9, -3480, 1000, 29970, 135)
    SetChrPos(0xA, -2430, 1000, 30860, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_BF5")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_BA2")
    SetChrPos(0x9, -3480, 1000, 29970, 135)
    SetChrPos(0xA, -2430, 1000, 30860, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_BF5")

    label("loc_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    BeginChrThread(0xA, 0, 0, 3)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_END)), "loc_BEF")
    SetChrPos(0xB, 8250, 4000, 19670, 45)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_BF5")

    label("loc_BEF")

    BeginChrThread(0xB, 0, 0, 4)

    label("loc_BF5")

    Call(0, 7)
    Return()

    # Function_9_AEF end

    def Function_10_BF9(): pass

    label("Function_10_BF9")

    SoundDistance(0x7C, 0xFFFFFFF6, 0x3E8, 0x9F7E, 0x2710, 0x186A0, 0x64, 0x0)
    Return()

    # Function_10_BF9 end

    def Function_11_C16(): pass

    label("Function_11_C16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_C27")
    Jump("loc_EAB")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD3")
    OP_93(0xFE, 0x87, 0x0)

    ChrTalk(
        0xFE,
        (
            "Let's see. Auction list...? Check.\x01",
            "Gavel? Check.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        (
            "Oh, are you looking for the second floor\x01",
            "seats? Please, right this way.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4A")

    label("loc_CD3")


    ChrTalk(
        0xFE,
        (
            "Second floor seating will not affect your\x01",
            "auction participation in the slightest. If\x01",
            "you would follow me, please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_EAB")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_D5D")
    Jump("loc_EAB")

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E26")

    ChrTalk(
        0xFE,
        (
            "There's still a little time until the\x01",
            "auction begins, dear guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The main hall is still being prepared, so we would\x01",
            "appreciate it if you could wait a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EAB")

    label("loc_E26")


    ChrTalk(
        0xFE,
        (
            "There's still a little time until the\x01",
            "Schwarze Auction begins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't you pass the time with\x01",
            "a few drinks in the salon?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAB")

    TalkEnd(0xFE)
    Return()

    # Function_11_C16 end

    def Function_12_EAF(): pass

    label("Function_12_EAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_EC0")
    Jump("loc_117D")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_106A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA5")

    ChrTalk(
        0xFE,
        (
            "Oh, dear, Elizabeth seems to have\x01",
            "become quite fond of one of the\x01",
            "other guests, Mr. Arundel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was quite shocked, given her usual\x01",
            "unsociable attitude. I suppose stranger\x01",
            "things have happened.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1065")

    label("loc_FA5")


    ChrTalk(
        0xFE,
        (
            "Now that I think about it, Mr. Arundel\x01",
            "was calling Elizabeth 'Noire', for\x01",
            "whatever reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, what would I do if she\x01",
            "began to not respond to 'Elizabeth'?\x01",
            "That would be a disaster.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1065")

    Jump("loc_117D")

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1078")
    Jump("loc_117D")

    label("loc_1078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_117D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(
        0xFE,
        (
            "The master's pet cat, Elizabeth, seems to\x01",
            "have wandered off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, dear... I'm worried that she'll cause\x01",
            "trouble for the rest of the guests.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_117D")

    label("loc_1132")


    ChrTalk(
        0xFE,
        "Have you seen a black cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, Elizabeth...where are you hiding?\x02",
    )

    CloseMessageWindow()

    label("loc_117D")

    TalkEnd(0xFE)
    Return()

    # Function_12_EAF end

    def Function_13_1181(): pass

    label("Function_13_1181")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1192")
    Jump("loc_12F9")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_11FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AD")
    Call(0, 14)
    Jump("loc_11FA")

    label("loc_11AD")


    ChrTalk(
        0xFE,
        (
            "The stage is ready. All that's left\x01",
            "is to bring in all of the exhibits.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FA")

    Jump("loc_12F9")

    label("loc_11FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_120D")
    Jump("loc_12F9")

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_12F9")

    ChrTalk(
        0xFE,
        (
            "I'm very sorry. Due to the auction\x01",
            "preparations, we would ask you to\x01",
            "refrain from getting on-stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is where the exhibits are going to\x01",
            "be presented, so we have to take many\x01",
            "precautions to guarantee their safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F9")

    TalkEnd(0xFE)
    Return()

    # Function_13_1181 end

    def Function_14_12FD(): pass

    label("Function_14_12FD")


    ChrTalk(
        0xFE,
        (
            "There. We can finally mark the\x01",
            "stage check off our list.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We found a book in the back... Its\x01",
            "owner probably dropped it last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It doesn't look like that particular guest\x01",
            "is with us this year, though... If you'd like,\x01",
            "I'd be more than happy to let you have it.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CF, 1)
    SetScenarioFlags(0x9D, 1)
    Return()

    # Function_14_12FD end

    def Function_15_1462(): pass

    label("Function_15_1462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1473")
    Jump("loc_14D0")

    label("loc_1473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1491")

    ChrTalk(
        0xFE,
        "Fumyaaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_149F")
    Jump("loc_14D0")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_14D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 6)), scpexpr(EXPR_END)), "loc_14C2")

    ChrTalk(
        0xFE,
        "Nya~~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_14C2")


    ChrTalk(
        0xFE,
        "Nya~~go.\x02",
    )

    CloseMessageWindow()

    label("loc_14D0")

    TalkEnd(0xFE)
    Return()

    # Function_15_1462 end

    def Function_16_14D4(): pass

    label("Function_16_14D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_14E5")
    Jump("loc_1B25")

    label("loc_14E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_190D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x101,
        (
            "#5105FLechter? What are you doing\x01",
            "up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3509FOh, Noire's just got a lil' attached to me\x01",
            "and won't leave me alone.\x02\x03",
            "#3502FHandsome men have it rough, am I right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 400)

    ChrTalk(
        0xB,
        "Myaon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        "#5709FHaha! I could see myself getting along with him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3504FHey, you guys know the auction's about\x01",
            "to begin, right...?\x02\x03",
            "#3501FGonna play hooky?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5103FNo, not exactly.\x02\x03",
            "#5100FOur business here is finished, so I think\x01",
            "we'll leave our seats empty for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3507FOh, you're leaving?! The less competition,\x01",
            "the better, I always say.\x02\x03",
            "#3504FNow, I'm not sure what 'business' you had\x01",
            "to attend to, but I hope it went well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101FTh-Thanks... (Has he caught on to our act?)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_1908")

    label("loc_17BC")


    ChrTalk(
        0xC,
        (
            "#3510FOn top of being the old man's rep, I also\x01",
            "have to win something in the auction to\x01",
            "bring back.\x02\x03",
            "#3509FThere's only one thing to do. I'll hang out\x01",
            "here until some crazy expensive cat food\x01",
            "goes up for bid. For Noire's sake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5112F(Something tells me he's going to be hanging\x01",
            "out for a long time, if that's the case...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1908")

    Jump("loc_1B25")

    label("loc_190D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_191B")
    Jump("loc_1B25")

    label("loc_191B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1B25")
    OP_4B(0xB, 0xFF)
    TurnDirection(0xFE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC9")

    ChrTalk(
        0xC,
        (
            "#3500FNoire, it took a lot of time to catch\x01",
            "your dinner, y'hear?\x02\x03",
            "#3504FYou better scarf this down and gimme\x01",
            "some thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Nyaao~~n?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*eats furiously*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3509FGuys, lookie here! She's munching\x01",
            "on that thing like there's no tomorrow!\x02\x03",
            "#3500FHmm, hopefully, she won't get sick\x01",
            "from eating that... I've never seen that\x01",
            "species before, but oh, well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5106F(That poor cat...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B21")

    label("loc_1AC9")


    ChrTalk(
        0xB,
        "*eats furiously*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#3500FC'mon, Noire! There's still a\x01",
            "lot of room left in you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B21")

    OP_4C(0xB, 0xFF)

    label("loc_1B25")

    TalkEnd(0xFE)
    Return()

    # Function_16_14D4 end

    def Function_17_1B29(): pass

    label("Function_17_1B29")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The auction will be starting soon.\x01",
            "I recommend you go ahead and\x01",
            "find your seats.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1B29 end

    def Function_18_1BA8(): pass

    label("Function_18_1BA8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C3C")
    Jump("loc_1C86")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C5C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C86")

    label("loc_1C5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C7C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C86")

    label("loc_1C7C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C86")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4E")

    ChrTalk(
        0xE,
        (
            "#2904FI'll stay here and observe what\x01",
            "items they put up for bid.\x02\x03",
            "#2902FI don't know if anything is going to\x01",
            "happen, but try to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D9D")

    label("loc_1D4E")


    ChrTalk(
        0xE,
        (
            "#2902FI don't know if anything is going to\x01",
            "happen, but try to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_1BA8 end

    def Function_19_1DA5(): pass

    label("Function_19_1DA5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1E39")
    Jump("loc_1E83")

    label("loc_1E39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E59")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E83")

    label("loc_1E59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E79")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E83")

    label("loc_1E79")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E83")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212F")

    ChrTalk(
        0xF,
        (
            "#3400FYou all look excited...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5105FHuh?! Why would you say that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3404FJust now, when the auction was about\x01",
            "to start, you got up from your seats. In\x01",
            "quite the rush, I might add.\x02\x03",
            "#3402FIsn't it only natural to assume that\x01",
            "something has happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#5705FYour outfit isn't the only thing\x01",
            "that's sharp, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#3404FThat's quite the compliment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5103FI can't say much...but something\x01",
            "strange is going on in this mansion.\x01",
            "I'm just not sure what, yet.\x02\x03",
            "#5101FI wouldn't let your guard down, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#3400FVery well. I can't exactly leave the\x01",
            "main hall, but I'll stay alert.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21E3")

    label("loc_212F")


    ChrTalk(
        0xF,
        (
            "#3404FIt's clear that you all have a different\x01",
            "objective than attending the auction...\x01",
            "I'm sure it's serious.\x02\x03",
            "#3400FI can't exactly leave the main hall,\x01",
            "but I'll stay alert.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_1DA5 end

    def Function_20_21EB(): pass

    label("Function_20_21EB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_227F")
    Jump("loc_22C9")

    label("loc_227F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_229F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22C9")

    label("loc_229F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22BF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22C9")

    label("loc_22BF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22C9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E9")

    ChrTalk(
        0xFE,
        (
            "If a Rosenberg Studio doll is really going\x01",
            "to be up for bid, I imagine it'll be one of\x01",
            "the final items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, the real question is, what price is it\x01",
            "going to go for? Hyeh hyeh hyeh, I can't\x01",
            "wait to see how that plays out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2491")

    label("loc_23E9")


    ChrTalk(
        0xFE,
        (
            "If a Rosenberg Studio doll is really going\x01",
            "to be up for bid, I imagine it'll be one of\x01",
            "the final items.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hyeh hyeh hyeh. I think I'll just nod off\x01",
            "until then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2491")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_21EB end

    def Function_21_2499(): pass

    label("Function_21_2499")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x1)

    ChrTalk(
        0x11,
        (
            "You're going to be a man and win\x01",
            "me a big, shiny jewel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "Hmph, of course. Doing something\x01",
            "like that is child's play.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_21_2499 end

    def Function_22_252D(): pass

    label("Function_22_252D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AB")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0xFE,
        (
            "Just what do they think they're doing?\x01",
            "It's already past the start time and\x01",
            "items still haven't been brought in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This isn't going to reflect well on the\x01",
            "don. And we'll end up getting\x01",
            "the short end of the stick, by proxy...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(
        0xFE,
        "Oh, excuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything is proceeding as scheduled.\x01",
            "There's no need to worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_26F1")

    label("loc_26AB")


    ChrTalk(
        0xFE,
        (
            "Everything is proceeding as scheduled.\x01",
            "There's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F1")

    TalkEnd(0xFE)
    Return()

    # Function_22_252D end

    def Function_23_26F5(): pass

    label("Function_23_26F5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "A little while ago, our boss told us he\x01",
            "felt like someone uninvited is planning\x01",
            "to cause some trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There hasn't been any reports of\x01",
            "anybody trying to sneak into the auction\x01",
            "among the guests, as of yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With our security, you can rest easy and\x01",
            "enjoy this year's Schwarze Auction.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_26F5 end

    def Function_24_2826(): pass

    label("Function_24_2826")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28BA")
    Jump("loc_2904")

    label("loc_28BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2904")

    label("loc_28DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2904")

    label("loc_28FA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2904")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "It looks like the auction is finally\x01",
            "about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll leave the bidding to my husband.\x01",
            "After all, I'm not sure if I'm used to\x01",
            "this kind of environment just yet...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_2826 end

    def Function_25_29E2(): pass

    label("Function_25_29E2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A76")
    Jump("loc_2AC0")

    label("loc_2A76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A96")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AC0")

    label("loc_2A96")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AB6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AC0")

    label("loc_2AB6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AC0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x14, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B79")
    Jump("loc_2BC3")

    label("loc_2B79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B99")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC3")

    label("loc_2B99")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC3")

    label("loc_2BB9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hahaha. No need to be nervous, dear.\x01",
            "Try to think of this as if it were any\x01",
            "other shopping trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You could even think of this as buying\x01",
            "things for a slightly more expensive\x01",
            "hobby.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_25_29E2 end

    def Function_26_2CB2(): pass

    label("Function_26_2CB2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D46")
    Jump("loc_2D90")

    label("loc_2D46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D90")

    label("loc_2D66")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D86")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D90")

    label("loc_2D86")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D90")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Judging by Don Marconi's attitude\x01",
            "in the salon, I expect more than just the\x01",
            "standard fare in this year's auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to be conservative with my mira until\x01",
            "the items I really want come out for bid.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_2CB2 end

    def Function_27_2E90(): pass

    label("Function_27_2E90")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F24")
    Jump("loc_2F6E")

    label("loc_2F24")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F44")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F6E")

    label("loc_2F44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F6E")

    label("loc_2F64")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F6E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Showing how deep your wallet goes\x01",
            "early on is key to succeeding in the\x01",
            "Schwarze Auction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You have to bid with confidence, or else\x01",
            "other bidders will find the motivation they\x01",
            "need to keep going.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_2E90 end

    def Function_28_3069(): pass

    label("Function_28_3069")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30FD")
    Jump("loc_3147")

    label("loc_30FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_311D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3147")

    label("loc_311D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_313D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3147")

    label("loc_313D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3147")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Today, I accomplished what I came\x01",
            "here to do--get in contact with\x01",
            "Speaker Hartmann.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All I have to do now is make some\x01",
            "large bids to make myself look good.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_3069 end

    def Function_29_3219(): pass

    label("Function_29_3219")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32AD")
    Jump("loc_32F7")

    label("loc_32AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32F7")

    label("loc_32CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32F7")

    label("loc_32ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hahaha...! Now, what am I going\x01",
            "to take home this year?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_3219 end

    def Function_30_3361(): pass

    label("Function_30_3361")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33F5")
    Jump("loc_343F")

    label("loc_33F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3415")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_343F")

    label("loc_3415")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3435")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_343F")

    label("loc_3435")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_343F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "I won a pure septium ring last year...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I pray that I win something of\x01",
            "even greater value this time around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_3361 end

    def Function_31_34E7(): pass

    label("Function_31_34E7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_357B")
    Jump("loc_35C5")

    label("loc_357B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_359B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C5")

    label("loc_359B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C5")

    label("loc_35BB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Last year, I fought to the last breath in\x01",
            "order to win a painting by the famous\x01",
            "artist, Luddy Reynard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That mortified look my competitor gave\x01",
            "me when I made that decisive bid...\x01",
            "Nothing will ever beat that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope that this year's auction can\x01",
            "deliver a thrill as great as that one.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_34E7 end

    def Function_32_371B(): pass

    label("Function_32_371B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_37AF")
    Jump("loc_37F9")

    label("loc_37AF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37CF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F9")

    label("loc_37CF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37EF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F9")

    label("loc_37EF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37F9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "If you're looking for the best of the best,\x01",
            "look no further than the Schwarze Auction.\x01",
            "It never fails to entertain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I find it hard to stomach the fact that\x01",
            "all our mira is going straight to Marconi.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_371B end

    def Function_33_38FE(): pass

    label("Function_33_38FE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3992")
    Jump("loc_39DC")

    label("loc_3992")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DC")

    label("loc_39B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39DC")

    label("loc_39D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "All the VIPs have arrived, so all that's left\x01",
            "is to look forward to tonight's auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't look so tense! Hahaha, it's not\x01",
            "good to overthink things.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_38FE end

    def Function_34_3AAA(): pass

    label("Function_34_3AAA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B3E")
    Jump("loc_3B88")

    label("loc_3B3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B5E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B88")

    label("loc_3B5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B88")

    label("loc_3B7E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B88")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBA")

    ChrTalk(
        0xFE,
        (
            "On second glance, isn't that blonde\x01",
            "woman...the IBC CEO's daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I remember correctly, she has a\x01",
            "burning passion for the dolls made\x01",
            "by the Rosenberg Studio...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, dear. She very well could sweep\x01",
            "my legs from under me and beat me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3D87")

    label("loc_3CBA")


    ChrTalk(
        0xFE,
        (
            "If that lady truly is the daughter of the\x01",
            "IBC's CEO...I'm in for a wild ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "N-No! Now's not the time to lose heart!\x01",
            "I come from nobility... There's no way\x01",
            "she'll beat me when it comes to mira.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D87")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_3AAA end

    def Function_35_3D8F(): pass

    label("Function_35_3D8F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E23")
    Jump("loc_3E6D")

    label("loc_3E23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E43")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E6D")

    label("loc_3E43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E6D")

    label("loc_3E63")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E6D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    OP_52(0x1E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x1E, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F26")
    Jump("loc_3F70")

    label("loc_3F26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F46")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F70")

    label("loc_3F46")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F66")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F70")

    label("loc_3F66")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F70")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hey, now's not the time to lose your\x01",
            "cool. If you can't relax, you'll start losing\x01",
            "bids you would normally win.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_3D8F end

    def Function_36_4016(): pass

    label("Function_36_4016")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40AA")
    Jump("loc_40F4")

    label("loc_40AA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_40CA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40F4")

    label("loc_40CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40EA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40F4")

    label("loc_40EA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40F4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "They say this event is run by the mafia...\x01",
            "So what kind of auction is this, really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess I'll have to see for myself.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_4016 end

    def Function_37_41A4(): pass

    label("Function_37_41A4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4238")
    Jump("loc_4282")

    label("loc_4238")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4258")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4282")

    label("loc_4258")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4278")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4282")

    label("loc_4278")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4282")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "No matter who I talk to, I can't find\x01",
            "anyone that runs an honest business...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a little intimidating, to be honest.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_41A4 end

    def Function_38_4330(): pass

    label("Function_38_4330")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43C4")
    Jump("loc_440E")

    label("loc_43C4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43E4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_440E")

    label("loc_43E4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4404")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_440E")

    label("loc_4404")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_440E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "(Having this lady accompany me into the\x01",
            "auction will boost my sway with people.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "(In exchange for that, a jewel is nothing.)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_4330 end

    def Function_39_44C2(): pass

    label("Function_39_44C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4556")
    Jump("loc_45A0")

    label("loc_4556")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4576")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45A0")

    label("loc_4576")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4596")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_45A0")

    label("loc_4596")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45A0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x23,
        "Bwahahaha! It's finally time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Dear, do you know who's going to win\x01",
            "the majority of tonight's items?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x24,
        (
            "Well, the one with the most mira, of course...\x01",
            "In other words, you, Father!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "Bwahahaha, exactly! I'm glad\x01",
            "you understand.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_44C2 end

    def Function_40_46BE(): pass

    label("Function_40_46BE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4752")
    Jump("loc_479C")

    label("loc_4752")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4772")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_479C")

    label("loc_4772")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4792")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_479C")

    label("loc_4792")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_479C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Father's enthusiasm is almost infectious\x01",
            "at this point. I'm sure his pride is ready\x01",
            "for the auction, as well as his wallet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's what I try to look for in my men.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_46BE end

    def Function_41_4878(): pass

    label("Function_41_4878")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 7)
    SetChrPos(0x101, -600, 0, -1150, 0)
    SetChrPos(0xEF, 600, 0, -1150, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4910, 2700, 9100, 0)
    MoveCamera(343, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28640, 0)
    FadeToBright(1000, 0)
    OP_68(-560, 2700, 10410, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(0, 3800, 4200, 0)
    MoveCamera(0, 8, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16110, 0)
    OP_68(0, 2300, 4200, 4000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_4969():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4969)
    Sleep(200)

    def lambda_4981():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4981)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3500831V#5105F#5PApparently, this is where the actual\x01",
            "auction is being held, but...\x02\x03",
            "#3500832V#5106FThis place is so over-the-top...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4AC2")

    ChrTalk(
        0x102,
        (
            "#3500833V#5306F#11PIs that some sort of artificial\x01",
            "waterfall...?\x02\x03",
            "#3500834V#5301FI haven't seen anything this\x01",
            "lavish in my entire life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE2")

    label("loc_4AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4B56")

    ChrTalk(
        0x103,
        (
            "#3500835V#5406F#11PIs that an artificial waterfall?\x02\x03",
            "#3500836V#5411FIt is as if we transported to an\x01",
            "entirely different place...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE2")

    label("loc_4B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4BE2")

    ChrTalk(
        0x104,
        (
            "#3500837V#5606F#11PAre you serious...? He went\x01",
            "and made his own waterfalls?\x02\x03",
            "#3500838V#5601FAre we really in someone's house?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE2")

    TurnDirection(0x101, 0xEF, 500)

    ChrTalk(
        0x101,
        (
            "#3500839V#5103F#5PWell, let's just head somewhere else\x01",
            "for now.\x02\x03",
            "#3500840V#5101FI still want to see for myself the kinds of\x01",
            "people invited to an underground event\x01",
            "such as this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, -2900, 180)
    SetScenarioFlags(0xA5, 1)
    EventEnd(0x5)
    Call(0, 7)
    Return()

    # Function_41_4878 end

    def Function_42_4CBC(): pass

    label("Function_42_4CBC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08102.itc", 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4CE2")
    LoadChrToIndex("chr/ch07702.itc", 0x1F)
    Jump("loc_4D05")

    label("loc_4CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4CF6")
    LoadChrToIndex("chr/ch07802.itc", 0x1F)
    Jump("loc_4D05")

    label("loc_4CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4D05")
    LoadChrToIndex("chr/ch07902.itc", 0x1F)

    label("loc_4D05")

    LoadChrToIndex("chr/ch05502.itc", 0x20)
    AddParty(0x50, 0xFF, 0xFF)
    SetChrPos(0x101, 600, 0, -2250, 0)
    SetChrPos(0xEF, -600, 0, -2250, 0)
    SetChrPos(0x138, 0, 0, -1450, 0)
    SetChrPos(0x151, 0, 0, -3000, 0)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 6)
    OP_4B(0xD, 0xFF)
    SetChrPos(0xD, 0, 0, 16500, 180)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrPos(0x9, 2870, 1000, 31060, 45)
    Call(0, 7)
    OP_68(0, 1600, 30250, 0)
    MoveCamera(0, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, 9250, 12000)
    Sleep(7500)

    def lambda_4DEF():
        OP_95(0xFE, 600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DEF)

    def lambda_4E09():
        OP_95(0xFE, -600, 0, 3250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4E09)

    def lambda_4E23():
        OP_95(0xFE, 0, 0, 4450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_4E23)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x138, 1)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-890, 1800, 4510, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 2500)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501319V#5108F#2PSo many wealthy people in one place...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4F39")

    ChrTalk(
        0x102,
        (
            "#3501320V#5301F#12PIndeed. I don't even want to think about\x01",
            "how much mira these people are worth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4FC4")

    ChrTalk(
        0x103,
        (
            "#3501321V#5401F#12PJudging by their outfits and demeanor, I\x01",
            "bet we are surrounded by an inconceivable\x01",
            "amount of mira...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5035")

    label("loc_4FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5035")

    ChrTalk(
        0x104,
        (
            "#3501322V#5601F#12POh, yeah. I'd lose my mind tryin' to guess\x01",
            "how much mira these folks are worth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5035")

    OP_68(-890, 1800, 5010, 2000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_5056():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5056)
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5084():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5084)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        (
            "#3501323V#5PMs. Crois, my deepest apologies for\x01",
            "making you wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x12C)
    Sleep(300)
    OP_93(0xD, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xD, 0xB4, 0x12C)

    ChrTalk(
        0xD,
        "#3501324V#5PAre these seats to your liking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#3501325V#2902F#2PYes, they will do. Thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x138, 0xB4, 0x1F4)

    ChrTalk(
        0x138,
        "#3501326V#2900F#5PShall we sit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501327V#5102F#2PS-Sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5202")

    ChrTalk(
        0x102,
        (
            "#3501328V#5306F#12PI'm still a bit nervous about\x01",
            "this whole thing...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52DD")

    label("loc_5202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_527A")

    ChrTalk(
        0x103,
        (
            "#3501329V#5406F#12PI think the gravity of this entire situation\x01",
            "is finally starting to dawn on me...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52DD")

    label("loc_527A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_52DD")

    ChrTalk(
        0x104,
        (
            "#3501330V#5606F#12PY'know, now that we're here,\x01",
            "I'm startin' to get the butterflies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52DD")

    OP_93(0x138, 0x0, 0x1F4)
    Sleep(100)

    def lambda_52EC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_52EC)
    Sleep(300)
    BeginChrThread(0x138, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 43)
    Sleep(700)
    BeginChrThread(0xEF, 3, 0, 43)
    WaitChrThread(0xD, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x138, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0xEF, 0x3)
    EndChrThread(0x138, 0x3)
    FadeToBright(1000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x10)
    SetChrPos(0x101, 4000, 150, 6600, 0)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrSubChip(0xEF, 0x0)
    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0xEF, 0x10)
    SetChrPos(0xEF, 5550, 150, 6600, 0)
    SetChrChipByIndex(0x138, 0x20)
    SetChrSubChip(0x138, 0x0)
    SetChrFlags(0x138, 0x4)
    SetChrFlags(0x138, 0x40)
    SetChrPos(0x138, 2400, 150, 6600, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x151, 0x80)
    ClearChrBattleFlags(0x151, 0x8000)
    OP_A7(0x151, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(2110, 2200, 6880, 0)
    MoveCamera(38, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17670, 0)
    OP_68(2110, 1300, 6880, 3500)
    Sleep(2000)

    def lambda_5417():
        OP_95(0xFE, 0, 0, 3350, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5417)
    WaitChrThread(0x151, 1)
    OP_63(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x151, 0x101, 500)
    Sound(1438, 255, 90, 0)

    ChrTalk(
        0x151,
        "#3501331V#5P#5702FOh, so this is where you were hiding.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x138, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)
    Sleep(100)
    SetChrSubChip(0x138, 0x1)
    OP_68(3600, 1300, 8380, 3000)

    def lambda_54F0():
        OP_95(0xFE, 1610, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_54F0)
    WaitChrThread(0x151, 1)
    OP_93(0x151, 0x87, 0x1F4)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_553E")

    ChrTalk(
        0x102,
        "#3501332V#5305F#11PWazy?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5598")

    label("loc_553E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_556C")

    ChrTalk(
        0x103,
        "#3501333V#5405F#11PWazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5598")

    label("loc_556C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5598")

    ChrTalk(
        0x104,
        "#3501334V#5605F#11PHey, Wazy.\x02",
    )

    CloseMessageWindow()

    label("loc_5598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 2)), scpexpr(EXPR_END)), "loc_5673")

    ChrTalk(
        0x101,
        (
            "#3501335V#5100F#11PI saw that married couple earlier.\x02\x03",
            "#3501336VWere they able to make up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501337V#5704F#5PIt seems so.\x02\x03",
            "#3501338V#5702FAnd with that beautiful reunion,\x01",
            "I was relieved of duty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57A4")

    label("loc_5673")


    ChrTalk(
        0x101,
        (
            "#3501339V#5105F#11PI can't help but notice you're alone...\x02\x03",
            "#3501340V#5101FHow did that argument earlier turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501341V#5704F#5POh, you know how it goes. A spat was had\x01",
            "and they were able to settle their differences.\x02\x03",
            "#3501342V#5702FAnd with that beautiful reunion, I was relieved\x01",
            "of duty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A4")


    ChrTalk(
        0x101,
        "#3501343V#5102F#11PWell, I'm happy for them.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5839")

    ChrTalk(
        0x102,
        (
            "#3501344V#5302F#11PGood work, Wazy. I'm sure they\x01",
            "appreciate your intervention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58D5")

    label("loc_5839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5885")

    ChrTalk(
        0x103,
        "#3501345V#5402F#11PHost? More like a marriage counselor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_58D5")

    label("loc_5885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_58D5")

    ChrTalk(
        0x104,
        (
            "#3501346V#5602F#11PAtta way, Wazy. Savin' one marriage\x01",
            "at a time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58D5")


    ChrTalk(
        0x138,
        (
            "#3501347V#2902F#12PA friend of yours? He certainly seems\x01",
            "like quite the character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501348V#5105F#11PYeah... Mariabell, this guy is--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501349V#5703F#5PWazy. Wazy Hemisphere.\x02\x03",
            "#3501350V#5700FYou're the daughter of the IBC's CEO,\x01",
            "aren't you, Ms. Mariabell Crois?\x02\x03",
            "#3501351VIt's a pleasure to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#3501352V#2909F#12POh, my. I'll have to stay on my toes\x01",
            "around you, won't I?\x02\x03",
            "#3501353V#2900FIt's nice to meet you, Wazy. Would you\x01",
            "care for the seat in front of mine?\x01",
            "There's plenty of room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x151,
        (
            "#3501354V#5704F#5PThanks, but I'll have to pass.\x02\x03",
            "#3501355V#5700FTruth be told, I was hoping that I could\x01",
            "speak to those two for a second.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501356V#5105F#11PWazy...?\x02",
    )

    CloseMessageWindow()

    def lambda_5B9B():
        OP_95(0xFE, 4200, 0, 7750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5B9B)
    Sleep(300)
    SetChrSubChip(0x138, 0x0)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x151, 1)
    OP_93(0x151, 0xB4, 0x1F4)

    ChrTalk(
        0x151,
        (
            "#3501357V#5701F#5P(When I examined the courtyard from\x01",
            "one of the windows, I saw loads of guard\x01",
            "dogs passed out on the ground.)\x02\x03",
            "#3501358V(Any idea why that might be?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501359V#5113F#11P(Are you serious?)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5D6E")

    ChrTalk(
        0x102,
        (
            "#3501360V#5305F#11P(Watch dogs...? He must be talking\x01",
            "about Revache's war hounds.)\x02\x03",
            "#3501361V#5301F(But what are they doing asleep?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EA2")

    label("loc_5D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5DFD")

    ChrTalk(
        0x103,
        (
            "#3501362V#5405F#11P(He must be referring to Revache's war hounds.)\x02\x03",
            "#3501363V#5401F(Why would they be unconscious, though?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EA2")

    label("loc_5DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5EA2")

    ChrTalk(
        0x104,
        (
            "#3501364V#5605F#11P(Watch dogs, eh? Must be talkin' about\x01",
            "Revache's annoying war hounds.)\x02\x03",
            "#3501365V#5601F(Why the hell are they sleepin' on the job?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EA2")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3501366V#5103F#11PI'm sorry, Mariabell.\x02\x03",
            "#3501367V#5100FI think we're going to have to excuse\x01",
            "ourselves for a little while.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x138, 0x2)

    ChrTalk(
        0x138,
        (
            "#3501368V#2904F#6PHehe, things have started to heat\x01",
            "up on your end, haven't they?\x02\x03",
            "#3501369V#2902FWell, don't let me hold you up.\x02\x03",
            "#3501370VAt the very least, I can make some\x01",
            "bids in your stead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501371V#5102F#11PThat would be great.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6070")

    ChrTalk(
        0x102,
        "#3501372V#5302F#11PThanks, Bell.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60E1")

    label("loc_6070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_60B2")

    ChrTalk(
        0x103,
        "#3501373V#5402F#11PGood luck with the auction.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60E1")

    label("loc_60B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_60E1")

    ChrTalk(
        0x104,
        "#3501374V#5609F#11P'Preciate it!\x02",
    )

    CloseMessageWindow()

    label("loc_60E1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xD, -6100, 0, 3190, 90)
    OP_4C(0xD, 0xFF)
    SetChrPos(0x9, 3140, 0, 31200, 45)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x138, 0x4)
    ClearChrFlags(0x138, 0x10)
    ClearChrFlags(0x138, 0x40)
    SetChrChipByIndex(0x138, 0xFF)
    SetChrSubChip(0x138, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    RemoveParty(0x37, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_4CBC end

    def Function_43_616E(): pass

    label("Function_43_616E")


    def lambda_6173():
        OP_95(0xFE, 0, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6173)
    WaitChrThread(0xFE, 1)

    def lambda_6191():
        OP_95(0xFE, 5450, 0, 7450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6191)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_616E end

    def Function_44_61AB(): pass

    label("Function_44_61AB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06200.itc", 0x1E)
    LoadChrToIndex("chr/ch06500.itc", 0x1F)
    LoadChrToIndex("chr/ch33200.itc", 0x20)
    LoadChrToIndex("chr/ch33000.itc", 0x21)
    LoadChrToIndex("chr/ch27700.itc", 0x22)
    LoadChrToIndex("chr/ch21600.itc", 0x23)
    LoadChrToIndex("chr/ch33300.itc", 0x24)
    LoadChrToIndex("chr/ch21800.itc", 0x25)
    LoadChrToIndex("chr/ch21900.itc", 0x26)
    LoadChrToIndex("chr/ch20800.itc", 0x28)
    LoadChrToIndex("chr/ch20900.itc", 0x29)
    LoadChrToIndex("chr/ch22000.itc", 0x2A)
    SetChrPos(0x0, 0, 0, 0, 0)
    SetChrPos(0x1, 0, 0, 0, 0)
    SetChrPos(0x2, 0, 0, 0, 0)
    SetChrPos(0x3, 0, 0, 0, 0)
    SetChrPos(0x4, 0, 0, 0, 0)
    SetChrPos(0x5, 0, 0, 0, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    SetChrPos(0x25, 0, 1000, 26500, 180)
    SetChrPos(0x26, -1400, 1000, 29000, 180)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    Call(0, 6)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_93(0x12, 0x0, 0x0)
    OP_93(0x13, 0x0, 0x0)
    Call(0, 7)
    FadeToBright(1000, 0)
    OP_68(0, 2400, 21500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(33400, 0)
    OP_68(0, 100, 21500, 6000)
    OP_63(0x25, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x22, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x17, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x22, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1E, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x16, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x17, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1A, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1D, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x1)
    OP_64(0x25)
    OP_0D()
    Fade(1000)
    OP_68(-90, 2100, 22700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(22140, 0)
    SetCameraDistance(20140, 3000)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x25,
        (
            "#3501942V#3005F#5PEveryone, quiet down!\x02\x03",
            "#3501943V#3000FThere's been a minor incident, but the\x01",
            "auction will proceed as planned...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x15,
        (
            "#3501944V#5PMinor incident, my ass! Those were\x01",
            "gunshots we heard earlier, right?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        "#3501945V#5PWh-Who do you take us for?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1B,
        (
            "#3501946V#11PI'll bring the diet into this!\x01",
            "Don't think I won't!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x25, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x25,
        "#3501947V#3005F#5PPlease, everyone just calm down...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-700, 2100, 30550, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20740, 0)
    SetCameraDistance(19240, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x26,
        (
            "#3501948V#2703F#5PHmph, useless morons...\x02\x03",
            "#3501949V#2701FWho do they think they are? How\x01",
            "dare they make a fool of me?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x26, 0x10E, 0x190)

    def lambda_68E8():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_68E8)
    Sleep(500)
    OP_63(0x25, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x25, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x25, 0x26, 500)

    ChrTalk(
        0x25,
        (
            "#3501950V#3005F#12PSpeaker Hartmann?!\x02\x03",
            "#3501951V#3007FWh-Where are you going...?\x01",
            "Please wait a minute!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x26, 1)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    Fade(1000)
    SetChrSubChip(0xE, 0x1)
    OP_68(0, 2400, 21500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(33400, 0)
    OP_68(0, 100, 21500, 9000)
    BeginChrThread(0x8, 3, 0, 62)
    OP_6F(0x1)
    OP_0D()
    Fade(500)
    OP_68(1900, 100, 18300, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(23770, 0)
    OP_0D()
    Sleep(300)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x27, 0x8)

    NpcTalk(
        0x27,
        "Mariabell",
        (
            "#3501952V#2904F#11PI suppose that means the auction is canceled.\x01",
            "A pity.\x02\x03",
            "#3501953V#2902FI'd say this visit was still worth it, all in all.\x01",
            "Where else would I have been able to see\x01",
            "such a show?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t101B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_61AB end

    def Function_45_6B2A(): pass

    label("Function_45_6B2A")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6B3E():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B3E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6B5E():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B5E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_6B2A end

    def Function_46_6B73(): pass

    label("Function_46_6B73")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6B87():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B87)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6BA7():
        OP_9B(0x0, 0xFE, 0x0, 0x526C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BA7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_6B73 end

    def Function_47_6BBC(): pass

    label("Function_47_6BBC")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6BD0():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BD0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6BF0():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BF0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_47_6BBC end

    def Function_48_6C05(): pass

    label("Function_48_6C05")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6C19():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C19)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6C39():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C39)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_6C05 end

    def Function_49_6C4E(): pass

    label("Function_49_6C4E")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6C62():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C62)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6C82():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C82)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_6C4E end

    def Function_50_6C97(): pass

    label("Function_50_6C97")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6CAB():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CAB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6CCB():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CCB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_6C97 end

    def Function_51_6CE0(): pass

    label("Function_51_6CE0")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6CF4():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CF4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6D14():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D14)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_51_6CE0 end

    def Function_52_6D29(): pass

    label("Function_52_6D29")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6D3D():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D3D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6D5D():
        OP_9B(0x0, 0xFE, 0x0, 0x48A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D5D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_52_6D29 end

    def Function_53_6D72(): pass

    label("Function_53_6D72")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6D86():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D86)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6DA6():
        OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DA6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_53_6D72 end

    def Function_54_6DBB(): pass

    label("Function_54_6DBB")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6DCF():
        OP_9B(0x0, 0xFE, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DCF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6DEF():
        OP_9B(0x0, 0xFE, 0x0, 0x3520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DEF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_6DBB end

    def Function_55_6E04(): pass

    label("Function_55_6E04")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6E18():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E18)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6E38():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E38)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_6E04 end

    def Function_56_6E4D(): pass

    label("Function_56_6E4D")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6E61():
        OP_9B(0x0, 0xFE, 0x0, 0x15AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E61)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6E81():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E81)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_6E4D end

    def Function_57_6E96(): pass

    label("Function_57_6E96")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6EAA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EAA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6ECA():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6ECA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_6E96 end

    def Function_58_6EDF(): pass

    label("Function_58_6EDF")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6EF3():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EF3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6F13():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F13)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_6EDF end

    def Function_59_6F28(): pass

    label("Function_59_6F28")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_6F3C():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F3C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6F5C():
        OP_9B(0x0, 0xFE, 0x0, 0x2B5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F5C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_6F28 end

    def Function_60_6F71(): pass

    label("Function_60_6F71")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6F85():
        OP_9B(0x0, 0xFE, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F85)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6FA5():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FA5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_60_6F71 end

    def Function_61_6FBA(): pass

    label("Function_61_6FBA")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_6FCE():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FCE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_6FEE():
        OP_9B(0x0, 0xFE, 0x0, 0x3EE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FEE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_6FBA end

    def Function_62_7003(): pass

    label("Function_62_7003")

    BeginChrThread(0x15, 3, 0, 46)
    BeginChrThread(0x18, 3, 0, 49)
    BeginChrThread(0x1E, 3, 0, 55)
    Sleep(6000)
    BeginChrThread(0x19, 3, 0, 50)
    BeginChrThread(0x21, 3, 0, 58)
    BeginChrThread(0x1C, 3, 0, 53)
    Sleep(6000)
    BeginChrThread(0x14, 3, 0, 45)
    BeginChrThread(0x23, 3, 0, 60)
    BeginChrThread(0x17, 3, 0, 48)
    Sleep(6000)
    BeginChrThread(0x1B, 3, 0, 52)
    BeginChrThread(0x24, 3, 0, 61)
    BeginChrThread(0x1F, 3, 0, 56)
    Sleep(6000)
    BeginChrThread(0x1A, 3, 0, 51)
    BeginChrThread(0x20, 3, 0, 57)
    Return()

    # Function_62_7003 end

    SaveToFile()

Try(main)
