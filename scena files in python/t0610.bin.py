from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0610.bin",                # FileName
        "t0610",                    # MapName
        "t0610",                    # Location
        0x006A,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 106, 0, 0, 0, 1],
    )

    BuildStringList((
        "t0610",                  # 0
        "bt0600",                 # 1
        "bt0600",                 # 2
        "bt0600",                 # 3
        "bt0600",                 # 4
        "bt0600",                 # 5
        "bt0600",                 # 6
        "bt0600",                 # 7
        "bt0600",                 # 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 10,  7,   0,   7,   9,   6,   9)
    Sepith("Sepith_B4", 0,   17,  5,   0,   12,  10,  12)
    Sepith("Sepith_C4", 13,  0,   7,   14,  0,   4,   9)
    Sepith("Sepith_D4", 7,   7,   0,   0,   9,   15,  9)

    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_10C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_110", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_114", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_11C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_124", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 8, 14, 180)

    # monster count: 16

    BattleInfo(
        "BattleInfo_144", 0x0000, 23, 6, 45, 6, 1, 40, 0, "bt0600", "Sepith_A4", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1B4", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_B4", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_224", 0x0000, 23, 6, 45, 6, 1, 50, 0, "bt0600", "Sepith_C4", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61701.dat", "ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_294", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_D4", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65801.dat", "ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0400, 23, 6, 45, 6, 1, 40, 0, "bt0600", "Sepith_A4", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_374", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_B4", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3E4", 0x0400, 23, 6, 45, 6, 1, 50, 0, "bt0600", "Sepith_C4", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61701.dat", "ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0600", "Sepith_D4", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65801.dat", "ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

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
        "monster/ch64850.itc",               # 10
        "monster/ch64851.itc",               # 11
        "monster/ch60850.itc",               # 12
        "monster/ch60850.itc",               # 13
        "monster/ch65850.itc",               # 14
        "monster/ch65851.itc",               # 15
        "monster/ch61750.itc",               # 16
        "monster/ch61750.itc",               # 17
    ))

    DeclMonster(12730,   15260,   50,      0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(45860,   30110,   7550,    0x1010000,    "BattleInfo_1B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(83400,   26570,   10500,   0x1010000,    "BattleInfo_224", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-94420,  25490,   50,      0x1010000,    "BattleInfo_294", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-73900,  25580,   -2950,   0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(60600,   23080,   1550,    0x1010000,    "BattleInfo_1B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(37780,   6050,    1550,    0x1010000,    "BattleInfo_294", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(26470,   1850,    1550,    0x1010000,    "BattleInfo_224", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(12730,   15260,   50,      0x1810000,    "BattleInfo_304", 1490, 16,  0xFFFF, 0,  1)
    DeclMonster(45860,   30110,   7550,    0x1810000,    "BattleInfo_374", 1491, 18,  0xFFFF, 2,  3)
    DeclMonster(83400,   26570,   10500,   0x1810000,    "BattleInfo_3E4", 1492, 22,  0xFFFF, 6,  7)
    DeclMonster(-94420,  25490,   50,      0x1810000,    "BattleInfo_454", 1493, 20,  0xFFFF, 4,  5)
    DeclMonster(-73900,  25580,   -2950,   0x1810000,    "BattleInfo_304", 1494, 16,  0xFFFF, 0,  1)
    DeclMonster(60600,   23080,   1550,    0x1810000,    "BattleInfo_374", 1495, 18,  0xFFFF, 2,  3)
    DeclMonster(37780,   6050,    1550,    0x1810000,    "BattleInfo_454", 1496, 20,  0xFFFF, 4,  5)
    DeclMonster(26470,   1850,    1550,    0x1810000,    "BattleInfo_3E4", 1497, 22,  0xFFFF, 6,  7)

    DeclActor(85540,   10500,   27550,   1200,    85540,   11500,   27550,   0x007C, 0,  3,  0x0000)
    DeclActor(25000,   1500,    -4000,   1200,    25000,   2500,    -4000,   0x007C, 0,  4,  0x0000)
    DeclActor(-88000,  50,      15000,   1200,    -88000,  1050,    15000,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_814",          # 00, 0
        "Function_1_8F3",          # 01, 1
        "Function_2_DD4",          # 02, 2
        "Function_3_E9D",          # 03, 3
        "Function_4_FB4",          # 04, 4
        "Function_5_10FB",         # 05, 5
        "Function_6_1241",         # 06, 6
        "Function_7_17A8",         # 07, 7
        "Function_8_1C28",         # 08, 8
    ))


    def Function_0_814(): pass

    label("Function_0_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_822")
    Jump("loc_8F2")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F2")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_867")
    ClearChrFlags(0x10, 0x80)

    label("loc_867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_876")
    ClearChrFlags(0x11, 0x80)

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_885")
    ClearChrFlags(0x12, 0x80)

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_894")
    ClearChrFlags(0x13, 0x80)

    label("loc_894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    ClearChrFlags(0x14, 0x80)

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B2")
    ClearChrFlags(0x15, 0x80)

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C1")
    ClearChrFlags(0x16, 0x80)

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D0")
    ClearChrFlags(0x17, 0x80)

    label("loc_8D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F2")
    Event(0, 6)

    label("loc_8F2")

    Return()

    # Function_0_814 end

    def Function_1_8F3(): pass

    label("Function_1_8F3")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D26")
    OP_70(0x0, 0x0)
    Jump("loc_D2A")

    label("loc_D26")

    OP_70(0x0, 0x1E)

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3D")
    OP_70(0x1, 0x0)
    Jump("loc_D41")

    label("loc_D3D")

    OP_70(0x1, 0x1E)

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D54")
    OP_70(0x2, 0x0)
    Jump("loc_D58")

    label("loc_D54")

    OP_70(0x2, 0x1E)

    label("loc_D58")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D77")
    OP_1B(0x0, 0x0, 0x8)

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD0")
    Event(0, 7)

    label("loc_DD0")

    Call(0, 2)
    Return()

    # Function_1_8F3 end

    def Function_2_DD4(): pass

    label("Function_2_DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFA")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0x14, 0x80)
    Jump("loc_E2F")

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E0D")
    ClearChrFlags(0xC, 0x8)
    Jump("loc_E2F")

    label("loc_E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E25")
    ClearChrFlags(0x14, 0x80)

    label("loc_E25")

    Jump("loc_E2F")

    label("loc_E2A")

    ClearChrFlags(0xC, 0x8)

    label("loc_E2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E67")
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x10, 0x80)
    Jump("loc_E9C")

    label("loc_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E7A")
    ClearChrFlags(0x8, 0x8)
    Jump("loc_E9C")

    label("loc_E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    ClearChrFlags(0x10, 0x80)

    label("loc_E92")

    Jump("loc_E9C")

    label("loc_E97")

    ClearChrFlags(0x8, 0x8)

    label("loc_E9C")

    Return()

    # Function_2_DD4 end

    def Function_3_E9D(): pass

    label("Function_3_E9D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7E")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 100)
    AddSepith(0x1, 100)
    AddSepith(0x2, 100)
    AddSepith(0x3, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x100\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x100\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x100\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x114, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_FA2")

    label("loc_F7E")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mine your own business.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_FA2")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_E9D end

    def Function_4_FB4(): pass

    label("Function_4_FB4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_109E")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6F, 1)"), scpexpr(EXPR_END)), "loc_1034")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1099")

    label("loc_1034")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1099")

    Jump("loc_10EF")

    label("loc_109E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm not empty. I'm making a statement.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_FB4 end

    def Function_5_10FB(): pass

    label("Function_5_10FB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C0")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 100)
    AddSepith(0x5, 100)
    AddSepith(0x6, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x100\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x100\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x114, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_122F")

    label("loc_11C0")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Did you hear about the woman who had a craving for goldia\x01",
            "sepith?\x01",
            "She just wanted some space, man.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_122F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10FB end

    def Function_6_1241(): pass

    label("Function_6_1241")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    OP_68(92500, 2400, 60350, 0)
    MoveCamera(38, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(45700, 0)
    SetChrPos(0x101, 1810, 50, 2520, 45)
    SetChrPos(0x102, 2200, 50, 840, 45)
    SetChrPos(0x103, -170, 50, 1890, 45)
    SetChrPos(0x104, 500, 0, 290, 45)
    Sleep(500)
    SetCameraDistance(43630, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(70700, 1000, 38130, 0)
    MoveCamera(29, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(39380, 0)
    OP_68(31200, 1000, 7200, 7000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(18510, 1000, 20080, 0)
    MoveCamera(76, 33, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(28950, 0)
    OP_68(2520, 1000, 2740, 7000)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(1370, 1000, 1460, 0)
    MoveCamera(86, 32, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21360, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0001FSo this is the abandoned mine.\x02\x03",
            "#0005FIt doesn't really strike me as being a\x01",
            "particularly old place...\x02\x03",
            "I mean, look. The orbal lamps still\x01",
            "seem to be in okay condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FIt's probably just to keep monsters from\x01",
            "appearing near the entrance.\x02\x03",
            "I get the feeling that this place is used\x01",
            "for storing materials and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FMaybe. Still, this place doesn't sit\x01",
            "well with me. Gives me bad vibes.\x02\x03",
            "#0304FActually, this would be the perfect\x01",
            "place to test your mettle, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0006FHappy-go-lucky as always...\x02\x03",
            "#0001FWe're here on work. Not some random\x01",
            "dare, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FHaha, don't have to tell me twice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI can detect the presence of multiple\x01",
            "monsters deeper in.\x02\x03",
            "#0200FThe structure of the mine will likely get\x01",
            "more complex the farther we go. We\x01",
            "should proceed with caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001FAbsolutely. Let's try not to get\x01",
            "lost while we're at it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -580, 0, -580, 45)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Sleep(500)
    OP_29(0x1C, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_6_1241 end

    def Function_7_17A8(): pass

    label("Function_7_17A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(13580, 550, 13530, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22340, 0)
    SetChrPos(0x101, 12000, 50, 15200, 180)
    SetChrPos(0x102, 13300, 50, 15200, 180)
    SetChrPos(0x103, 12000, 50, 16500, 180)
    SetChrPos(0x104, 13300, 50, 16500, 180)
    SetCameraDistance(21340, 3000)

    def lambda_1836():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1836)

    def lambda_1850():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1850)

    def lambda_186A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_186A)

    def lambda_1884():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1884)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_18B8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18B8)

    def lambda_18C5():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18C5)

    def lambda_18D2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18D2)

    def lambda_18DF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18DF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#6P#0000FThat's the last of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0203FYes, it should be.\x02\x03",
            "#0200FI can not detect any more monsters\x01",
            "within the abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FPhew, finally!\x02\x03",
            "Runnin' around this ugly place\x01",
            "has tuckered me out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe've definitely worked hard.\x02\x03",
            "Now, Lloyd. Shall we head on back\x01",
            "to Mayor Bickson's house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FYeah, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FUgh, I don't think I'm gonna make it...\x02\x03",
            "#0309FLloooooyd. Do a pal a solid and carry\x01",
            "me back to the entrance, pleeeease? ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#0003FNot gonna happen.\x02\x03",
            "#0000FStop messing around.\x01",
            "It's time to head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306FTch, killjoy.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x1, 0x4)
    SetChrName("")
    SetMessageWindowPos(-1, 40, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Return to Mayor Bickson's house?\x07\x00",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Return]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0F")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C27")

    label("loc_1C0F")

    OP_1B(0x0, 0x0, 0x8)
    SetChrPos(0x0, 12000, 50, 15200, 180)
    EventEnd(0x5)

    label("loc_1C27")

    Return()

    # Function_7_17A8 end

    def Function_8_1C28(): pass

    label("Function_8_1C28")

    EventBegin(0x1)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Return]\x01",      # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C79")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C8C")

    label("loc_1C79")

    SetChrPos(0x0, 1170, 50, 1170, 45)
    EventEnd(0x5)

    label("loc_1C8C")

    Return()

    # Function_8_1C28 end

    SaveToFile()

Try(main)
