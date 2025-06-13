from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1020.bin",                # FileName
        "r1020",                    # MapName
        "r1020",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1020",                  # 0
        "Billy",                  # 1
        "列車",                   # 2
        "br1000",                 # 3
        "br1000",                 # 4
        "br1000",                 # 5
        "br1000",                 # 6
        "br1000",                 # 7
        "br1000",                 # 8
        "br1000",                 # 9
        "To Crossbell City",      # 10
        "To Bellguard Gate",      # 11
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   8,   0,   12,  4,   8,   0)
    Sepith("Sepith_B4", 0,   13,  0,   13,  0,   0,   4)
    Sepith("Sepith_C4", 4,   2,   11,  0,   0,   8,   5)
    Sepith("Sepith_D4", 4,   4,   10,  2,   0,   5,   5)
    Sepith("Sepith_E4", 4,   4,   4,   10,  3,   3,   3)
    Sepith("Sepith_F4", 12,  7,   4,   3,   6,   14,  7)

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
    MonsterBattlePostion("MonsterBattlePostion_164", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_184", 0x0000, 17, 6, 60, 8, 1, 40, 0, "br1000", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms70300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70300.dat", "ms70300.dat", "ms71900.dat", "ms70300.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_24C", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms70500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70500.dat", "ms70500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70500.dat", "ms70500.dat", "ms70400.dat", "ms70500.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_314", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms63200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63200.dat", "ms63200.dat", "ms63200.dat", "ms63200.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3DC", 0x0000, 17, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4A4", 0x0000, 17, 6, 60, 8, 1, 50, 0, "br1000", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", "ms70400.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_56C", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br1000", "Sepith_F4", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_608", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72401.dat", "ms72401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_164", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    AddCharChip((
        "chr/ch23600.itc",                   # 00
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
        "monster/ch70350.itc",               # 10
        "monster/ch70351.itc",               # 11
        "monster/ch70550.itc",               # 12
        "monster/ch70550.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch70450.itc",               # 16
        "monster/ch70451.itc",               # 17
        "monster/ch63250.itc",               # 18
        "monster/ch63251.itc",               # 19
        "monster/ch72450.itc",               # 1A
        "monster/ch72450.itc",               # 1B
        "monster/ch60750.itc",               # 1C
        "monster/ch60750.itc",               # 1D
    ))

    DeclNpc(-84500,  0,       18899,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16250,  -32920,  0,       0x1010000,    "BattleInfo_184", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-31700,  -5730,   0,       0x1010000,    "BattleInfo_24C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-47140,  -40730,  -1000,   0x1010000,    "BattleInfo_314", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-72720,  -30360,  -1000,   0x1010000,    "BattleInfo_3DC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-67110,  -42180,  -1000,   0x1010000,    "BattleInfo_184", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-66360,  4440,    -10,     0x1010000,    "BattleInfo_314", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-105190, -11350,  -10,     0x1010000,    "BattleInfo_4A4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-115390, -20350,  -10,     0x1010000,    "BattleInfo_4A4", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-125510, -7100,   -10,     0x1010000,    "BattleInfo_24C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-14910,  -19080,  0,       0x1010000,    "BattleInfo_56C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-66880,  -6860,   0,       0x1010000,    "BattleInfo_56C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-100640, 4780,    0,       0x1010000,    "BattleInfo_56C", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-76100,  -38740,  500,     0x185002D,    "BattleInfo_608", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 12,  -76.5,                 9.0,                   -1.0,                  2500.0,                [0.14142131805419922,  0.035355351865291595,  -0.0,                  0.0,                   -0.14142140746116638,  0.035355329513549805,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.091523170471191,    2.386486530303955,     0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 9,   -76.0999984741211,     -38.7400016784668,     -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   9.512499809265137,     4.84250020980835,      0.5,                   1.0])

    DeclActor(-31810,  -50,     -1990,   1200,    -31810,  950,     -1990,   0x007C, 0,  4,  0x0000)
    DeclActor(-107180, -50,     -24250,  1200,    -107180, 950,     -24250,  0x007C, 0,  5,  0x0000)
    DeclActor(-4460,   0,       -4850,   1200,    -4460,   0,       -4850,   0x007C, 0,  6,  0x0000)
    DeclActor(-66530,  -1000,   -40600,  1200,    -66530,  -1000,   -40600,  0x007C, 0,  7,  0x0000)
    DeclActor(-122090, -10,     -9540,   1200,    -122090, -10,     -9540,   0x007C, 0,  8,  0x0000)
    DeclActor(-82960,  0,       28280,   5000,    -82960,  0,       28280,   0x007C, 0,  13, 0x0000)

    PlaceName(25.0, 0.0, 10.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(-160.0, 0.0, -16.0, 0x0000, 0x0000, "To Bellguard Gate")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_B28",          # 00, 0
        "Function_1_BE0",          # 01, 1
        "Function_2_BFF",          # 02, 2
        "Function_3_C16",          # 03, 3
        "Function_4_1593",         # 04, 4
        "Function_5_16DC",         # 05, 5
        "Function_6_180D",         # 06, 6
        "Function_7_1821",         # 07, 7
        "Function_8_1835",         # 08, 8
        "Function_9_1849",         # 09, 9
        "Function_10_1AA1",        # 0A, 10
        "Function_11_1ABF",        # 0B, 11
        "Function_12_1B42",        # 0C, 12
        "Function_13_24DE",        # 0D, 13
        "Function_14_3805",        # 0E, 14
    ))


    def Function_0_B28(): pass

    label("Function_0_B28")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_B68"),
        (1, "loc_B74"),
        (2, "loc_B80"),
        (3, "loc_B8C"),
        (4, "loc_B98"),
        (5, "loc_BA4"),
        (6, "loc_BB0"),
        (SWITCH_DEFAULT, "loc_BBC"),
    )


    label("loc_B68")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B74")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B80")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B8C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_B98")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BA4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BB0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BBC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BC8")

    label("loc_BDF")

    Return()

    # Function_0_B28 end

    def Function_1_BE0(): pass

    label("Function_1_BE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BFE")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_BE0")

    label("loc_BFE")

    Return()

    # Function_1_BE0 end

    def Function_2_BFF(): pass

    label("Function_2_BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C12")
    ClearChrFlags(0x8, 0x80)

    label("loc_C12")

    Call(0, 10)
    Return()

    # Function_2_BFF end

    def Function_3_C16(): pass

    label("Function_3_C16")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4F")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_C4F")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x3, 0x4)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_13B5")
    Jump("loc_13F2")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13CF")
    Jump("loc_13F2")

    label("loc_13CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_13E1")
    Jump("loc_13F2")

    label("loc_13E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_13F2")
    OP_66(0x5, 0x1)

    label("loc_13F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1414")
    SetChrFlags(0x16, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_1428")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1428")
    ClearChrFlags(0x16, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1428")

    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x16, 0x100)
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1456")
    OP_70(0x0, 0x0)
    Jump("loc_145A")

    label("loc_1456")

    OP_70(0x0, 0x1E)

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146D")
    OP_70(0x1, 0x0)
    Jump("loc_1471")

    label("loc_146D")

    OP_70(0x1, 0x1E)

    label("loc_1471")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_14DB")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -4460, 0, -4850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_1592")

    label("loc_14DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_1539")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -66530, -1000, -40600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_1592")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_1592")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -122090, -10, -9540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1592")

    Return()

    # Function_3_C16 end

    def Function_4_1593(): pass

    label("Function_4_1593")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167D")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1613")
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
    SetScenarioFlags(0x118, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1678")

    label("loc_1613")

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

    label("loc_1678")

    Jump("loc_16D0")

    label("loc_167D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Someone should EP Charge you with theft.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_16D0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1593 end

    def Function_5_16DC(): pass

    label("Function_5_16DC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x118, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C6")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_175C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x118, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_17C1")

    label("loc_175C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
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

    label("loc_17C1")

    Jump("loc_1801")

    label("loc_17C6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mya~uun.\x01",
            "Nya~on.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1801")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DC end

    def Function_6_180D(): pass

    label("Function_6_180D")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_180D end

    def Function_7_1821(): pass

    label("Function_7_1821")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1821 end

    def Function_8_1835(): pass

    label("Function_8_1835")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1835 end

    def Function_9_1849(): pass

    label("Function_9_1849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 2)), scpexpr(EXPR_END)), "loc_1853")
    Return()

    label("loc_1853")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1936"),
        (SWITCH_DEFAULT, "loc_194D"),
    )


    label("loc_1936")

    Sleep(500)
    OP_90(0x0, -70820, -1000, -33900, 225)
    EventEnd(0x5)
    Return()

    label("loc_194D")

    Battle("BattleInfo_608", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-70820, 0, -33900, 0)
    OP_90(0x0, -70820, -1000, -33900, 225)
    OP_90(0x1, -70820, -1000, -33900, 225)
    OP_90(0x2, -70820, -1000, -33900, 225)
    OP_90(0x3, -70820, -1000, -33900, 225)
    OP_90(0x4, -70820, -1000, -33900, 225)
    OP_90(0x5, -70820, -1000, -33900, 225)
    OP_90(0x6, -70820, -1000, -33900, 225)
    OP_90(0x7, -70820, -1000, -33900, 225)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1A0F"),
        (1, "loc_1A12"),
        (SWITCH_DEFAULT, "loc_1A15"),
    )


    label("loc_1A0F")

    EventEnd(0x5)
    Return()

    label("loc_1A12")

    OP_B7(0x0)
    Return()

    label("loc_1A15")

    EventBegin(0x1)
    SetChrFlags(0x16, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster on West Crossbell Highway!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x79, 2)
    OP_29(0x2F, 0x4, 0x10)
    OP_29(0x2F, 0x4, 0x2)
    OP_29(0x2F, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_9_1849 end

    def Function_10_1AA1(): pass

    label("Function_10_1AA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1ABE")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_1ABE")

    Return()

    # Function_10_1AA1 end

    def Function_11_1ABF(): pass

    label("Function_11_1ABF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Argh! This would have never happened\x01",
            "had I double-checked the cargo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wh-Whatever! Ignore me and\x01",
            "go find that kid!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1ABF end

    def Function_12_1B42(): pass

    label("Function_12_1B42")

    EventBegin(0x0)
    OP_E0(0x3)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    Fade(1000)
    OP_68(-75330, 1300, 6410, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-75840, 1300, 7500, 1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C07")
    SetChrPos(0x101, -75760, 0, 7730, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1D3A")

    label("loc_1C07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6F")
    SetChrPos(0x101, -74340, 0, 7660, 315)
    SetChrPos(0x102, -75760, 0, 7730, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1D3A")

    label("loc_1C6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD7")
    SetChrPos(0x101, -75880, 0, 5340, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75760, 0, 7730, 315)
    SetChrPos(0x104, -73920, 0, 5600, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)
    Jump("loc_1D3A")

    label("loc_1CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3A")
    SetChrPos(0x101, -73920, 0, 5600, 315)
    SetChrPos(0x102, -74340, 0, 7660, 315)
    SetChrPos(0x103, -75880, 0, 5340, 315)
    SetChrPos(0x104, -75760, 0, 7730, 315)
    SetChrPos(0x160, -74970, 0, 4520, 315)

    label("loc_1D3A")

    OP_0D()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D87")

    ChrTalk(
        0x101,
        "#3400598V#0005F#11POh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1D87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC3")

    ChrTalk(
        0x102,
        "#3400599V#0101F#11PLook over there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E05")

    ChrTalk(
        0x103,
        "#3400600V#0201F#11PSecond target located.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1E05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E4A")

    ChrTalk(
        0x104,
        "#3400601V#0301F#11PSo that's where he was hidin'!\x02",
    )

    CloseMessageWindow()

    label("loc_1E4A")

    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-84580, 900, 18690, 0)
    MoveCamera(37, 19, 0, 0)
    MoveCamera(18, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19950, 0)
    SetCameraDistance(18950, 2000)
    SetChrPos(0x101, -78290, 0, 11660, 315)
    SetChrPos(0x102, -76720, 0, 12340, 315)
    SetChrPos(0x103, -77250, 0, 10600, 315)
    SetChrPos(0x104, -75680, 0, 11560, 315)
    SetChrPos(0x160, -79910, 0, 11150, 315)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        "#3400602V#11PMan, where are you guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400603V#11PThat kid's gonna be in some real trouble\x01",
            "if you don't hurry up!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -73080, 0, 15330, 315)

    ChrTalk(
        0x101,
        "#3400604V#0007F#1PHey!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrPos(0x101, -78290, 0, 11660, 315)
    OP_93(0x8, 0x87, 0x1F4)
    OP_68(-83980, 900, 18240, 2500)

    def lambda_1FE0():
        OP_95(0xFE, -83600, 0, 17100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FE0)

    def lambda_1FFA():
        OP_95(0xFE, -82500, 0, 18200, 2900, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FFA)

    def lambda_2014():
        OP_95(0xFE, -82500, 0, 16000, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2014)

    def lambda_202E():
        OP_95(0xFE, -81400, 0, 17100, 2700, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_202E)
    Sleep(500)

    def lambda_204B():
        OP_95(0xFE, -84900, 0, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_204B)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        "#3400605V#5PY-You came!\x02",
    )

    WaitChrThread(0x160, 1)
    OP_93(0x160, 0x0, 0x1F4)
    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400606V#5POh, what a relief! You guys\x01",
            "sure move quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400607V#0001F#12PNot true. We kept you waiting a bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400608V#3303F#6PHey, mister.\x02\x03",
            "#3400609V#3301FHave you heard any ear-shattering screams\x01",
            "since the boy disappeared?\x02\x03",
            "#3400610VOr maybe the sound of a moderately heavy bag\x01",
            "of flesh falling off the cliffside and violently\x01",
            "hitting the ground?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_2218():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2218)

    def lambda_2225():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2225)
    Sleep(100)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2247():
        TurnDirection(0xFE, 0x160, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2247)

    def lambda_2254():
        TurnDirection(0xFE, 0x160, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2254)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        "#3400611V#5PWh-What are you saying, little lady?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3400612V#5POf course I haven't heard anything even\x01",
            "remotely CLOSE to what you're asking!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400613V#3304F#6PThe good news is, our sneaky child is likely\x01",
            "still alive and well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x160,
        "#3400614V#3300F#6PShall we be off then, mister?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400615V#0005F#11PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3400616V#0302F#11P(Haha. Impressive lil' lady.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3400617V#0108F#11P(Her assessment was completely accurate...\x01",
            "It's almost impossible to believe she's just\x01",
            "a child.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3400618V#0206F#11P(Her being Kitty makes perfect sense now.)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -83600, 0, 17100, 315)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xA3, 1)
    OP_29(0x46, 0x1, 0xD)
    OP_E0(0x2)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_12_1B42 end

    def Function_13_24DE(): pass

    label("Function_13_24DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2635")
    TalkBegin(0xFF)
    OP_93(0x0, 0x15E, 0x0)

    ChrTalk(
        0x101,
        (
            "#0001F(We might be able to take\x01",
            "one of Grace's photos here...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3301FExcuse me, Detective? Should I remind you\x01",
            "that now is not the time to be daydreaming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FO-Oh, yeah. Sorry about that.\x02\x03",
            "#0001F(It'd be highly inappropriate of us to start\x01",
            "taking photos while we should be looking\x01",
            "for Colin.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_3804")

    label("loc_2635")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-84950, -100, 31330, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23410, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -84440, 0, 26710, 350)
    SetChrPos(0x102, -82980, 0, 27830, 350)
    SetChrPos(0x103, -86040, 0, 27310, 35)
    SetChrPos(0x104, -81800, 0, 26750, 35)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x3, 0x9)
    OP_49()
    SetChrPos(0x9, -120000, -15000, 56000, 0)
    OP_D3(0x9, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0000FThe Transcontinental Railroad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FYep. Thing connects Erebonia to Calvard,\x01",
            "all while runnin' smack dab through the\x01",
            "middle of Crossbell.\x02\x03",
            "#0303FDamn impressive, when you think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103FFreight trains are also used to transport\x01",
            "goods in and out of the state.\x02\x03",
            "#0100FIt wouldn't be a stretch to say that the\x01",
            "railroad symbolizes modern-day Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FIt's too bad we can't take a picture of the\x01",
            "train to give to Grace. It would have made\x01",
            "for something really spectacular.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2957():
        OP_93(0xFE, 0x131, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2957)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    def lambda_2980():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2980)

    def lambda_298D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_298D)

    def lambda_299A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_299A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#12P#0005FHmm? What's up, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FIt would seem a train is approaching, after all.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#0011FW-Wait, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FThat's friggin' sweet, man! Think it's\x01",
            "time for that picture-perfect moment,\x01",
            "Mademois-Elie!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AEE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AEE)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#12P#0011FG-Get the camera, Elie!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3343")

    ChrTalk(
        0x102,
        (
            "#12P#0105FO-Okay, but I'm not entirely--\x01",
            "I wish my hands would stop shaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x15E, 0x1F4)
    OP_93(0x101, 0x15E, 0x1F4)
    OP_93(0x103, 0x15E, 0x1F4)
    OP_93(0x104, 0x15E, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(2000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#6P#0200FThere it goes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWhew. Think that mighta been the first\x01",
            "time I've seen a movin' train up close\x01",
            "and personal like that.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D5A():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D5A)

    def lambda_2D67():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D67)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x101,
        "#12P#0000FHow'd it go, Elie?\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0100FDecent...maybe? I may have taken\x01",
            "the picture before the train was\x01",
            "fully within frame, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FI'm sure ya did a swell job, Mademois-Elie.\x02\x03",
            "Takin' pictures basically boils down to\x01",
            "hittin' the shutter at the right time, eh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0106F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "Much like now, some pictures can only\x01",
            "ever be taken once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThe difference in quality between\x01",
            "amateur and professional photography\x01",
            "is immediately apparent.\x02\x03",
            "#0203FI would imagine a simpleton would have\x01",
            "difficulty grasping any level of intricacy\x01",
            "or nuance, however.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#12P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FA-Anyway... I'm sure it all turned out fine.\x01",
            "You managed to pull the camera out pretty\x01",
            "quickly, so we owe you one.\x02\x03",
            "And besides, even if it IS a little off, it's been\x01",
            "a while since you had to take a difficult shot.\x01",
            "I'm sure you're starting to get a feel for it again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0100FWell, it's getting there, I suppose.\x01",
            "I won't know how they turned out until\x01",
            "they're fully developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FSounds good, but we should keep our\x01",
            "eyes peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "Anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B5")

    label("loc_3343")


    ChrTalk(
        0x102,
        "#12P#0105FO-Okay!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x15E, 0x1F4)
    OP_93(0x101, 0x15E, 0x1F4)
    OP_93(0x103, 0x15E, 0x1F4)
    OP_93(0x104, 0x15E, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(2000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x103,
        "#6P#0200FThere it goes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWhew. Think that mighta been the first\x01",
            "time I've seen a movin' train up close\x01",
            "and personal like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FHow'd it go Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWell, it was a moving object, and I was\x01",
            "a bit rushed. But, um...I think it'll get\x01",
            "the job done.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3595")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_35AC")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_35C3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_35DA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_35F1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_35F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_3608")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_361F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_361F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3636")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_364D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_364D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3730")

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, really? Well, you managed to pull the\x01",
            "camera out pretty quickly, so we owe you one.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B5")

    label("loc_3730")


    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, really? Well, you managed to pull the\x01",
            "camera out pretty quickly, so we owe you one.\x02\x03",
            "Anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -84030, 0, 26840, 350)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x7)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x1000)
    ClearMapFlags(0x8000000)
    OP_37()
    Call(0, 10)
    OP_65(0x5, 0x1)
    Sleep(500)
    EventEnd(0x5)

    label("loc_3804")

    Return()

    # Function_13_24DE end

    def Function_14_3805(): pass

    label("Function_14_3805")


    def lambda_380A():
        OP_95(0xFE, 80000, -15000, 56000, 25000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_380A)
    Sound(451, 0, 100, 0)
    Fade(500)
    OP_68(-77630, 200, 37840, 0)
    MoveCamera(341, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19310, 0)
    OP_0D()
    OP_68(-80740, 200, 33810, 4000)
    MoveCamera(58, 26, 0, 4000)
    OP_6E(510, 2000)
    SetCameraDistance(19310, 2000)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(-84950, -100, 31330, 0)
    MoveCamera(27, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23410, 0)
    OP_0D()
    Return()

    # Function_14_3805 end

    SaveToFile()

Try(main)
