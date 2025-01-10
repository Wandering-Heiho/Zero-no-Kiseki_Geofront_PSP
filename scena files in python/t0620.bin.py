from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0620.bin",                # FileName
        "t0620",                    # MapName
        "t0620",                    # Location
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
        "t0620",                  # 0
        "bt0610",                 # 1
        "bt0610",                 # 2
        "bt0610",                 # 3
        "bt0610",                 # 4
        "bt0610",                 # 5
        "bt0610",                 # 6
        "bt0610",                 # 7
        "bt0610",                 # 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 10,  7,   0,   7,   9,   6,   9)
    Sepith("Sepith_B4", 0,   17,  5,   0,   12,  10,  12)
    Sepith("Sepith_C4", 7,   7,   0,   0,   9,   15,  9)
    Sepith("Sepith_D4", 13,  0,   7,   14,  0,   4,   9)

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

    # monster count: 12

    BattleInfo(
        "BattleInfo_144", 0x0000, 23, 6, 45, 6, 1, 40, 0, "bt0610", "Sepith_A4", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1B4", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_B4", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_224", 0x0000, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_C4", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65801.dat", "ms61701.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_294", 0x0000, 23, 6, 45, 6, 1, 50, 0, "bt0610", "Sepith_D4", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61701.dat", "ms65801.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0400, 23, 6, 45, 6, 1, 40, 0, "bt0610", "Sepith_A4", 65, 35, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_374", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_B4", 65, 35, 0, 0,
        (
            ("ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60800.dat", "ms60800.dat", "ms60800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3E4", 0x0400, 23, 6, 45, 6, 1, 25, 0, "bt0610", "Sepith_C4", 65, 35, 0, 0,
        (
            ("ms65801.dat", "ms65801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65801.dat", "ms61701.dat", "ms65801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0400, 23, 6, 45, 6, 1, 50, 0, "bt0610", "Sepith_D4", 65, 35, 0, 0,
        (
            ("ms61701.dat", "ms61701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61701.dat", "ms65801.dat", "ms61701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
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

    DeclMonster(24880,   114060,  50,      0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(24730,   141020,  4550,    0x1010000,    "BattleInfo_1B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(18920,   159820,  6750,    0x1010000,    "BattleInfo_224", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(29570,   162040,  6750,    0x1010000,    "BattleInfo_294", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(61090,   190220,  7500,    0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(91740,   195770,  9000,    0x1010000,    "BattleInfo_1B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(24880,   114060,  50,      0x1810000,    "BattleInfo_304", 1498, 16,  0xFFFF, 0,  1)
    DeclMonster(24730,   141020,  4550,    0x1810000,    "BattleInfo_374", 1499, 18,  0xFFFF, 2,  3)
    DeclMonster(18920,   159820,  6750,    0x1810000,    "BattleInfo_3E4", 1500, 20,  0xFFFF, 4,  5)
    DeclMonster(29570,   162040,  6750,    0x1810000,    "BattleInfo_454", 1501, 22,  0xFFFF, 6,  7)
    DeclMonster(61090,   190220,  7500,    0x1810000,    "BattleInfo_304", 1502, 16,  0xFFFF, 0,  1)
    DeclMonster(91740,   195770,  9000,    0x1810000,    "BattleInfo_374", 1503, 18,  0xFFFF, 2,  3)

    DeclActor(-74400,  0,       126120,  1200,    -74400,  1000,    126120,  0x007C, 0,  3,  0x0000)
    DeclActor(-108460, 0,       147860,  1200,    -108460, 1000,    147860,  0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_764",          # 00, 0
        "Function_1_7F9",          # 01, 1
        "Function_2_B4A",          # 02, 2
        "Function_3_B73",          # 03, 3
        "Function_4_D33",          # 04, 4
        "Function_5_EC7",          # 05, 5
    ))


    def Function_0_764(): pass

    label("Function_0_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_772")
    Jump("loc_7F8")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    ClearChrFlags(0xE, 0x80)

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC")
    ClearChrFlags(0xF, 0x80)

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB")
    ClearChrFlags(0x10, 0x80)

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DA")
    ClearChrFlags(0x11, 0x80)

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    ClearChrFlags(0x12, 0x80)

    label("loc_7E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F8")
    ClearChrFlags(0x13, 0x80)

    label("loc_7F8")

    Return()

    # Function_0_764 end

    def Function_1_7F9(): pass

    label("Function_1_7F9")

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
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")
    OP_70(0x0, 0x0)
    Jump("loc_AD0")

    label("loc_ACC")

    OP_70(0x0, 0x1E)

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE3")
    OP_70(0x1, 0x0)
    Jump("loc_AE7")

    label("loc_AE3")

    OP_70(0x1, 0x1E)

    label("loc_AE7")

    Sound(124, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B46")
    Event(0, 5)

    label("loc_B46")

    Call(0, 2)
    Return()

    # Function_1_7F9 end

    def Function_2_B4A(): pass

    label("Function_2_B4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6C")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_B72")

    label("loc_B6C")

    ClearMapObjFlags(0x0, 0x4)

    label("loc_B72")

    Return()

    # Function_2_B4A end

    def Function_3_B73(): pass

    label("Function_3_B73")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5D")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_BF3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_C58")

    label("loc_BF3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C58")

    Jump("loc_D27")

    label("loc_C5D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'll let you in on a little secret. There was more than\x01",
            "one item in here, but someone beat you to it and\x01",
            "took the good stuff. The bad stuff? You're holding it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_D27")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B73 end

    def Function_4_D33(): pass

    label("Function_4_D33")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1D")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_DB3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_E18")

    label("loc_DB3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
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

    label("loc_E18")

    Jump("loc_EBB")

    label("loc_E1D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Your request for a rare, ultra powered quartz from\x01",
            "before the Septian Calendar is being processed.\x01",
            "Please stand by.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EBB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_D33 end

    def Function_5_EC7(): pass

    label("Function_5_EC7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(43180, 550, 128970, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(30730, 0)
    SetChrPos(0x101, 37520, 3000, 126230, 180)
    SetChrPos(0x102, 38800, 3000, 126340, 180)
    SetChrPos(0x103, 37750, 3000, 127850, 180)
    SetChrPos(0x104, 39090, 3000, 127870, 180)
    SetCameraDistance(29730, 3000)

    def lambda_F55():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F55)

    def lambda_F6F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6F)

    def lambda_F89():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F89)

    def lambda_FA3():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA3)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_FD7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD7)

    def lambda_FE4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE4)

    def lambda_FF1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FF1)

    def lambda_FFE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FFE)
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
            "#0000FStop messing around,\x01",
            "it's time to head back.\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132E")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_1341")

    label("loc_132E")

    SetChrPos(0x0, 38640, 3050, 124280, 180)
    EventEnd(0x5)

    label("loc_1341")

    Return()

    # Function_5_EC7 end

    SaveToFile()

Try(main)
