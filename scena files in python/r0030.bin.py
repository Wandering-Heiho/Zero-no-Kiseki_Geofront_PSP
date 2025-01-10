from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0030.bin",                # FileName
        "r0030",                    # MapName
        "r0030",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 0, 0, 1],
    )

    BuildStringList((
        "r0030",                  # 0
        "車",                     # 1
        "Zeit",                   # 2
        "Bus",                    # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "br0000",                 # 7
        "br0000",                 # 8
        "br0000",                 # 9
        "To Crossbell City",      # 10
        "To Tangram Gate",        # 11
        "To Armorica Village",    # 12
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_B4", 3,   0,   2,   6,   0,   0,   2)
    Sepith("Sepith_C4", 1,   6,   0,   3,   2,   1,   1)
    Sepith("Sepith_D4", 1,   2,   7,   0,   1,   2,   0)
    Sepith("Sepith_E4", 24,  24,  24,  24,  24,  24,  24)
    Sepith("Sepith_F4", 12,  20,  10,  28,  11,  2,   5)

    MonsterBattlePostion("MonsterBattlePostion_104", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_130", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_134", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_138", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_144", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 2, 13, 180)

    # monster count: 16

    BattleInfo(
        "BattleInfo_164", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_A4", 30, 45, 25, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66500.dat", "ms63000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66500.dat", "ms63000.dat", "ms66500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_200", 0x0000, 8, 6, 45, 6, 1, 75, 0, "br0000", "Sepith_B4", 30, 45, 25, 0,
        (
            ("ms61000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61000.dat", "ms61000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms61000.dat", "ms66500.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_29C", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_C4", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_338", 0x0000, 8, 6, 45, 6, 1, 50, 0, "br0000", "Sepith_D4", 30, 45, 25, 0,
        (
            ("ms64000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64000.dat", "ms64000.dat", "ms64000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3D4", 0x0000, 8, 6, 90, 8, 1, 50, 0, "br0000", "Sepith_E4", 30, 45, 25, 0,
        (
            ("ms66400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66400.dat", "ms66400.dat", "ms66400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_470", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch61050.itc",               # 12
        "monster/ch61050.itc",               # 13
        "monster/ch69950.itc",               # 14
        "monster/ch69950.itc",               # 15
        "monster/ch64050.itc",               # 16
        "monster/ch64051.itc",               # 17
        "monster/ch66450.itc",               # 18
        "monster/ch66450.itc",               # 19
        "monster/ch63750.itc",               # 1A
        "monster/ch63751.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(12880,   15780,   920,     0x1010000,    "BattleInfo_164", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(37140,   15560,   2450,    0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(54520,   6080,    3000,    0x1010000,    "BattleInfo_29C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(47250,   -9890,   2000,    0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(40910,   -27690,  2000,    0x1010000,    "BattleInfo_164", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(24140,   -10270,  2000,    0x1010000,    "BattleInfo_29C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(87050,   -38310,  4000,    0x1010000,    "BattleInfo_164", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(119910,  -34280,  4000,    0x1010000,    "BattleInfo_164", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(124190,  5590,    4000,    0x1010000,    "BattleInfo_200", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(116730,  27220,   4000,    0x1010000,    "BattleInfo_29C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(103280,  23510,   4000,    0x1010000,    "BattleInfo_164", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(94990,   -310,    4000,    0x1010000,    "BattleInfo_338", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(105490,  7860,    4000,    0x1010000,    "BattleInfo_3D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(34320,   -15610,  2000,    0x1010000,    "BattleInfo_470", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(98270,   -31570,  4000,    0x1010000,    "BattleInfo_470", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(103030,  8630,    4000,    0x1010000,    "BattleInfo_470", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 13,  83.0,                  -30.0,                 3.0,                   3906.25,               [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.03999999910593033,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -16.599998474121094,   1.1999999284744263,    -0.5999999642372131,   1.0])

    DeclActor(49000,   2000,    -10070,  1200,    49000,   3000,    -10070,  0x007C, 0,  2,  0x0000)
    DeclActor(49000,   2000,    -25660,  1200,    49000,   3000,    -25660,  0x007C, 0,  3,  0x0000)
    DeclActor(105110,  4000,    -27530,  1200,    105110,  5000,    -27530,  0x007C, 0,  12, 0x0000)
    DeclActor(25130,   2000,    -11040,  1200,    25130,   2000,    -11040,  0x007C, 0,  4,  0x0000)
    DeclActor(98320,   4000,    -59160,  1200,    98320,   4000,    -59160,  0x007C, 0,  5,  0x0000)
    DeclActor(94410,   4000,    -22120,  1500,    94410,   5700,    -22120,  0x007C, 0,  20, 0x0000)

    PlaceName(-17.0, 0.0, -10.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(152.0, 0.0, -82.0, 0x0000, 0x0000, "To Tangram Gate")
    PlaceName(79.0, 0.0, 66.0, 0x0000, 0x0000, "To Armorica Village")
    PlaceName(105.5999984741211, 0.0, -27.200000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 11

    ScpFunction((
        "Function_0_A3C",          # 00, 0
        "Function_1_A5E",          # 01, 1
        "Function_2_FDE",          # 02, 2
        "Function_3_1139",         # 03, 3
        "Function_4_12A5",         # 04, 4
        "Function_5_12B9",         # 05, 5
        "Function_6_12CD",         # 06, 6
        "Function_7_1301",         # 07, 7
        "Function_8_13F2",         # 08, 8
        "Function_9_150D",         # 09, 9
        "Function_10_164B",        # 0A, 10
        "Function_11_1767",        # 0B, 11
        "Function_12_17FC",        # 0C, 12
        "Function_13_189F",        # 0D, 13
        "Function_14_2215",        # 0E, 14
        "Function_15_2585",        # 0F, 15
        "Function_16_25BD",        # 10, 16
        "Function_17_25DC",        # 11, 17
        "Function_18_26A2",        # 12, 18
        "Function_19_26C4",        # 13, 19
        "Function_20_28F6",        # 14, 20
    ))


    def Function_0_A3C(): pass

    label("Function_0_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A4B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_A5A")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 11)

    label("loc_A5A")

    Call(0, 6)
    Return()

    # Function_0_A3C end

    def Function_1_A5E(): pass

    label("Function_1_A5E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A76")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A76")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEB")
    OP_70(0x0, 0x0)
    Jump("loc_EEF")

    label("loc_EEB")

    OP_70(0x0, 0x1E)

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_70(0x1, 0x0)
    Jump("loc_F06")

    label("loc_F02")

    OP_70(0x1, 0x1E)

    label("loc_F06")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 3)), scpexpr(EXPR_END)), "loc_F6C")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 25130, 2000, -11040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_FC5")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_FC5")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 98320, 4000, -59160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_FC5")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDD")
    OP_1B(0x1, 0x0, 0x13)

    label("loc_FDD")

    Return()

    # Function_1_A5E end

    def Function_2_FDE(): pass

    label("Function_2_FDE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C8")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_105E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_10C3")

    label("loc_105E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
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

    label("loc_10C3")

    Jump("loc_112D")

    label("loc_10C8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's empty, but the woodwork is amazing!\x01",
            "Is it...chestnut?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_112D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_FDE end

    def Function_3_1139(): pass

    label("Function_3_1139")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1223")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x44, 1)"), scpexpr(EXPR_END)), "loc_11B9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_121E")

    label("loc_11B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x44),
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

    label("loc_121E")

    Jump("loc_1299")

    label("loc_1223")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Can you feel how hard this chest is?\x01",
            "I could bench press your entire party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1299")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1139 end

    def Function_4_12A5(): pass

    label("Function_4_12A5")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 3)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_12A5 end

    def Function_5_12B9(): pass

    label("Function_5_12B9")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_12B9 end

    def Function_6_12CD(): pass

    label("Function_6_12CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12EA")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)

    label("loc_12EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7C, 0)), scpexpr(EXPR_END)), "loc_12FB")
    ClearScenarioFlags(0x7C, 0)
    Jump("loc_1300")

    label("loc_12FB")

    SetChrFlags(0x17, 0x80)

    label("loc_1300")

    Return()

    # Function_6_12CD end

    def Function_7_1301(): pass

    label("Function_7_1301")

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
            "Crossbell City - East Exit\x01",      # 0
            "Armorica Village\x01",                # 1
            "Tangram Gate\x01",                    # 2
            "Leave\x01",                           # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A5")
    Call(0, 8)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_13EA")

    label("loc_13A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CA")
    Call(0, 9)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_13EA")

    label("loc_13CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EA")
    Call(0, 10)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()

    label("loc_13EA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_1301 end

    def Function_8_13F2(): pass

    label("Function_8_13F2")

    Fade(1000)
    OP_68(101630, 4600, -27310, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xA)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 103230, 4000, -9370, 180)
    OP_D3(0xA, 0x0, 0x2EFF4, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_14C7():
        OP_95(0xFE, 99960, 4000, -24090, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14C7)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_71(0x3, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x3)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_8_13F2 end

    def Function_9_150D(): pass

    label("Function_9_150D")

    Fade(1000)
    OP_68(100290, 4600, -28120, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(29500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xA)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 80680, 4000, -26630, 90)
    OP_D3(0xA, 0x0, 0x16184, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_0D()
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_15E3():
        OP_95(0xFE, 92660, 4000, -29500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15E3)
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xA, 1)

    def lambda_1610():
        OP_9E(0xFE, 0x16EFE, 0xFFFFA560, 0xFFFEA840, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1610)
    WaitChrThread(0xA, 1)
    OP_71(0x3, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x3)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_9_150D end

    def Function_10_164B(): pass

    label("Function_10_164B")

    Fade(1000)
    OP_68(103530, 4600, -32380, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 106370, 4000, -27960, 225)
    SetChrPos(0x1, 107160, 4000, -28700, 225)
    SetChrPos(0x2, 107820, 4000, -29500, 225)
    SetChrPos(0x3, 108390, 4000, -30200, 225)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xA)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 90520, 4000, -25730, 135)
    OP_D3(0xA, 0x0, 0x16184, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    OP_74(0x3, 0x1E)
    OP_0D()
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1721():
        OP_95(0xFE, 100900, 4000, -36100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1721)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_71(0x3, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x3)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_10_164B end

    def Function_11_1767(): pass

    label("Function_11_1767")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 106740, 4000, -28000, 225)
    SetChrPos(0x1, 106740, 4000, -28000, 225)
    SetChrPos(0x2, 106740, 4000, -28000, 225)
    SetChrPos(0x3, 106740, 4000, -28000, 225)
    OP_68(106740, 4600, -28000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_1767 end

    def Function_12_17FC(): pass

    label("Function_12_17FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_180D")
    Call(0, 7)
    Jump("loc_189E")

    label("loc_180D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189B")

    ChrTalk(
        0x102,
        "#0103F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FThe regret on your faces is\x01",
            "as clear as day, you two.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_189B")

    TalkEnd(0xFF)

    label("loc_189E")

    Return()

    # Function_12_17FC end

    def Function_13_189F(): pass

    label("Function_13_189F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(96350, 4800, -29340, 0)
    MoveCamera(49, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26140, 0)
    SetChrPos(0x101, 90700, 4000, -27460, 90)
    SetChrPos(0x102, 84840, 4000, -26650, 90)
    SetChrPos(0x103, 81630, 4000, -28310, 90)
    SetChrPos(0x104, 87580, 4000, -28750, 90)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x17, 0x8)
    SetCameraDistance(23150, 4000)

    def lambda_197D():
        OP_95(0xFE, 96910, 4000, -30030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_197D)

    def lambda_1997():
        OP_95(0xFE, 95080, 4000, -28380, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1997)

    def lambda_19B1():
        OP_95(0xFE, 93470, 4000, -29390, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19B1)

    def lambda_19CB():
        OP_95(0xFE, 94610, 4000, -30580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19CB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x101, 0x87, 0x12C)
    Sleep(500)
    OP_93(0x101, 0x0, 0x12C)
    Sleep(500)
    OP_93(0x101, 0x10E, 0x12C)

    ChrTalk(
        0x101,
        (
            "#1100301V#0000F#11PLooks like we've hit a fork in the road.\x02\x03",
            "#1100302VI'm pretty sure we have to go north\x01",
            "in order to reach Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100303V#0300F#6PBingo. Takin' the road on the left's\x01",
            "gonna lead us in the right direction.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xE1, 0x12C)
    Sound(1175, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#1100305V#0106F#5P#40WThis...is a bit tougher than I was\x01",
            "anticipating.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)
    Sleep(150)
    Sound(1271, 255, 100, 0)
    Sleep(800)

    ChrTalk(
        0x103,
        (
            "#1100307V#0206F#6P#40WAgreed... My initial estimation has\x01",
            "led to a disastrous miscalculation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100308V#0002F#11PThese monsters roaming around the\x01",
            "highway aren't helping, either. You two\x01",
            "look like you're about to pass out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1100309V#0300F#12POh, boy. How 'bout we take a breather,\x01",
            "ladies?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x190)
    Sleep(200)

    ChrTalk(
        0x102,
        "#1100310V#0102F#5P#30WNo, I think I'll be okay.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x102,
        "#1100311V#0100F#5P#30WWhat about you, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100312V#0206F#6P#30WAs much as I would love to admit defeat\x01",
            "right about now...\x02\x03",
            "#1100313V#0201F...I was the one who suggested we walk,\x01",
            "so I must persevere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100314V#0000F#11PIf you insist.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1100315V#0302F#12PJust remember that if you can't take much\x01",
            "more of this, you can always ask good ol'\x01",
            "Randy here for a piggy-back ride.\x02\x03",
            "#1100316VOr would ya rather ride on my shoulders?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x190)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#1100317V#0203F#3PI strongly and unequivocally refuse.\x01",
            "Do not treat me like a child.\x02\x03",
            "#1100318V#0211FFurthermore, I doubt you would be\x01",
            "satisfied with someone of my stature\x01",
            "riding your back, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100319V#0309F#12PHey, true enough! I'd rather have a\x01",
            "chick with a voluptu--\x02\x03",
            "#1100320V#0307FHold up a second! You're makin' it\x01",
            "sound like I had ulterior motives!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x190)

    ChrTalk(
        0x102,
        "#1100321V#0102F#5PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100322V#0002F#11PHaha, she got you. Anyway, let's\x01",
            "keep moving.\x02\x03",
            "#1100323V#0004FI'd be surprised if we didn't run into\x01",
            "more monsters, so let's take it slow\x01",
            "and steady.\x02\x03",
            "#1100324V#0000FDon't be afraid to let us know if you\x01",
            "need to take a break, Tio. All right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x190)

    ChrTalk(
        0x103,
        "#1100325V#0202F#6P...Roger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(23650, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 94220, 4000, -30730, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x60, 2)
    ClearMapFlags(0x8000000)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x17, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_189F end

    def Function_14_2215(): pass

    label("Function_14_2215")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch02600.itc", 0x1E)
    LoadChrToIndex("chr/ch02651.itc", 0x1F)
    LoadChrToIndex("chr/ch02602.itc", 0x20)
    SoundLoad(832)
    OP_68(99850, 4600, -23130, 0)
    MoveCamera(32, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34410, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 80870, 7000, -11450, 160)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetMapObjFlags(0x2, 0x1000)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x8)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, 103300, 4000, -9400, 170)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    BeginChrThread(0x8, 3, 0, 15)
    FadeToBright(1000, 0)
    OP_68(98630, 3500, -27380, 3000)
    MoveCamera(32, 16, 0, 3000)
    SetCameraDistance(25000, 3000)
    OP_0D()
    Sound(458, 0, 100, 0)
    OP_6F(0x51)
    OP_68(85340, 5100, -27740, 5000)
    SetCameraDistance(16000, 5000)
    StopBGM(0x2328)
    OP_6F(0x11)
    WaitChrThread(0x8, 3)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 17)
    WaitChrThread(0x9, 3)
    SetChrChipByIndex(0x9, 0x20)
    BeginChrThread(0x9, 0, 0, 16)
    Sleep(800)
    Sound(2053, 255, 80, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)
    SetChrName("White Wolf")

    AnonymousTalk(
        0xFF,
        "#1100720V...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(300)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(87180, 5100, -29420, 1500)
    SetCameraDistance(20000, 1500)
    BeginChrThread(0x9, 3, 0, 18)

    def lambda_24C8():
        OP_96(0xFE, 0x15626, 0xFA0, 0xFFFF7A22, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24C8)

    def lambda_24E2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_24E2)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_250A():
        OP_9D(0xFE, 0x15B3A, 0xFA0, 0xFFFF68FC, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_250A)
    WaitChrThread(0x9, 1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    ReplaceBGM("ed7100", "ed7102")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2215 end

    def Function_15_2585(): pass

    label("Function_15_2585")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 96580, 4000, -29640)
    OP_9F(0x1, 80500, 4000, -27240)
    OP_9F(0x1, 64590, 4000, -26570)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_15_2585 end

    def Function_16_25BD(): pass

    label("Function_16_25BD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25DB")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_16_25BD")

    label("loc_25DB")

    Return()

    # Function_16_25BD end

    def Function_17_25DC(): pass

    label("Function_17_25DC")


    def lambda_25E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_25E1)
    ClearChrFlags(0x9, 0x1)

    def lambda_25F7():
        OP_9D(0xFE, 0x146D6, 0x1388, 0xFFFFB712, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25F7)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x9, 0x1)
    Sound(46, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x1)

    def lambda_2641():
        OP_9D(0xFE, 0x14E7E, 0xFA0, 0xFFFF95F2, 0x2EE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2641)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x9, 0x1)
    Sound(832, 0, 100, 0)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)

    def lambda_2682():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2682)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x9, 1)
    Return()

    # Function_17_25DC end

    def Function_18_26A2(): pass

    label("Function_18_26A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26C3")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(832, 0, 100, 0)
    Jump("Function_18_26A2")

    label("loc_26C3")

    Return()

    # Function_18_26A2 end

    def Function_19_26C4(): pass

    label("Function_19_26C4")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2849")

    ChrTalk(
        0x101,
        (
            "#0005FI'm pretty sure this way leads\x01",
            "to Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYep. The Calvardian border is over this way.\x01",
            "The CGF's deputy commander operates outta\x01",
            "Tangram Gate, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208FJoy...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0006FDon't worry, you two. I know now's\x01",
            "not the time for detours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FLet's get a move on.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28DF")

    label("loc_2849")


    ChrTalk(
        0x101,
        (
            "#0000FI'm pretty sure this way leads\x01",
            "to Tangram Gate.\x02\x03",
            "We're still pretty far away from\x01",
            "Armorica Village, so let's avoid\x01",
            "making any extra stops.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DF")

    Sleep(50)
    SetChrPos(0x0, 126580, 4000, -57650, 315)
    EventEnd(0x4)
    Return()

    # Function_19_26C4 end

    def Function_20_28F6(): pass

    label("Function_20_28F6")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "West: Crossbell City  - 108 selge\x01",
            "North: Armorica Village - 166 selge\x01",
            "Southeast: Tangram Gate - 98 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_28F6 end

    SaveToFile()

Try(main)
