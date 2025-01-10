from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0112.bin",                # FileName
        "m0112",                    # MapName
        "m0112",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0112",                  # 0
        "Water Monster",          # 1
        "bm0114",                 # 2
        "bm0114",                 # 3
        "bm0114",                 # 4
        "bm0114",                 # 5
        "bm0113",                 # 6
        "bm0113",                 # 7
        "bm0113",                 # 8
        "bm0113",                 # 9
        "bm0114",                 # 10
        "bm0113",                 # 11
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 1,   1,   0,   1,   1,   0,   0)
    Sepith("Sepith_B4", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_C4", 1,   8,   6,   1,   1,   1,   2)
    Sepith("Sepith_D4", 2,   0,   0,   1,   1,   0,   1)

    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_108", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_110", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_114", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_148", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_14C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_150", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_154", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_15C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 5, 5, 45)

    # monster count: 13

    BattleInfo(
        "BattleInfo_164", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0114", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_22C", 0x0010, 48, 6, 60, 6, 1, 25, 0, "bm0113", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms71000.dat", 0, 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", "ms71000.dat", 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2F4", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms70600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_D4", 30, 45, 20, 5,
        (
            ("ms73200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73200.dat", "ms73200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73200.dat", "ms73200.dat", "ms73200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73200.dat", "ms73200.dat", "ms73200.dat", "ms73200.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_484", 0x0010, 48, 6, 60, 6, 1, 25, 0, "bm0114", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms71000.dat", 0, 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", 0, 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71000.dat", "ms71000.dat", "ms71000.dat", 0, 0, 0, "ms71000.dat", 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_54C", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0114", "Sepith_C4", 30, 45, 20, 5,
        (
            ("ms70600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
            ("ms70600.dat", "ms70600.dat", "ms70600.dat", "ms70600.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_104", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_614", 0x0000, 48, 6, 60, 6, 1, 40, 0, "bm0113", "Sepith_A4", 30, 45, 10, 5,
        (
            ("ms71200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71200.dat", "ms71200.dat", "ms71200.dat", "ms71200.dat", 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_144", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_6DC", 0x0812, 255, 6, 0, 0, 0, 0, 0, "bm0114", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_720", 0x0812, 255, 6, 0, 0, 0, 0, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_144", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 5

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
        "monster/ch70650.itc",               # 10
        "monster/ch70651.itc",               # 11
        "monster/ch71050.itc",               # 12
        "monster/ch71050.itc",               # 13
        "monster/ch73250.itc",               # 14
        "monster/ch73250.itc",               # 15
        "monster/ch71250.itc",               # 16
        "monster/ch71251.itc",               # 17
        "monster/ch73350.itc",               # 18
        "monster/ch73350.itc",               # 19
    ))

    DeclNpc(10699,   1000,    -100000, 270,  469,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-11090,  -100100, -200,    0x1010000,    "BattleInfo_164", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-88770,  -105390, -8000,   0x1010000,    "BattleInfo_22C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-102320, -96220,  -2000,   0x1010000,    "BattleInfo_2F4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-16550,  -299530, -6000,   0x1010000,    "BattleInfo_3BC", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-7990,   -306140, 2000,    0x1010000,    "BattleInfo_484", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(8090,    -311820, -6000,   0x1010000,    "BattleInfo_54C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(27520,   -311100, -3010,   0x1010000,    "BattleInfo_614", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(99810,   -299980, 0,       0x1010000,    "BattleInfo_614", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(10700,   -100000, 0,       0x115010E,    "BattleInfo_6DC", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(-197500, -200000, 0,       0x115005A,    "BattleInfo_720", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(-16000,  -292500, -6000,   0x11500B4,    "BattleInfo_6DC", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(10000,   -300000, -2000,   0x115010E,    "BattleInfo_6DC", 0,   24,  0xFFFF, 0,  0)
    DeclMonster(23500,   -300000, -2000,   0x115010E,    "BattleInfo_6DC", 0,   24,  0xFFFF, 0,  0)

    DeclEvent(0x0000, 0, 10,  10.699999809265137,    -100.0,                0.0,                   324.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.7833333015441895,   16.666667938232422,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 11,  -197.5,                -200.0,                0.0,                   14.2978515625,         [0.3636363744735718,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3636363744735718,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   71.81818389892578,     72.7272720336914,      -0.0,                  1.0])
    DeclEvent(0x0000, 0, 12,  -16.0,                 -292.5,                -6.0,                  144.0,                 [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.6666667461395264,    73.125,                1.2000000476837158,    1.0])
    DeclEvent(0x0000, 0, 13,  10.0,                  -300.0,                -2.0,                  64.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.5,                  75.0,                  0.4000000059604645,    1.0])
    DeclEvent(0x0000, 0, 14,  23.5,                  -300.0,                -2.0,                  64.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.875,                75.0,                  0.4000000059604645,    1.0])

    DeclActor(99830,   0,       -99820,  1200,    99830,   1000,    -99820,  0x007C, 0,  5,  0x0000)
    DeclActor(-199530, 0,       -200180, 1200,    -199530, 1000,    -200180, 0x007C, 0,  6,  0x0000)
    DeclActor(-16350,  -2000,   -303820, 1200,    -16350,  -1000,   -303820, 0x007C, 0,  7,  0x0000)
    DeclActor(24300,   -3000,   -311950, 1200,    24300,   -2000,   -311950, 0x007C, 0,  8,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  15, 0x0000)
    DeclActor(102000,  0,       -500000, 1200,    102500,  1000,    -500000, 0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_CEC",          # 00, 0
        "Function_1_D0B",          # 01, 1
        "Function_2_D28",          # 02, 2
        "Function_3_DF3",          # 03, 3
        "Function_4_1816",         # 04, 4
        "Function_5_1967",         # 05, 5
        "Function_6_1AA6",         # 06, 6
        "Function_7_1C15",         # 07, 7
        "Function_8_1D50",         # 08, 8
        "Function_9_1EAF",         # 09, 9
        "Function_10_2470",        # 0A, 10
        "Function_11_260E",        # 0B, 11
        "Function_12_288B",        # 0C, 12
        "Function_13_2A6E",        # 0D, 13
        "Function_14_2C68",        # 0E, 14
        "Function_15_2E61",        # 0F, 15
        "Function_16_2FE8",        # 10, 16
        "Function_17_312F",        # 11, 17
        "Function_18_32B8",        # 12, 18
    ))


    def Function_0_CEC(): pass

    label("Function_0_CEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D0A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_CEC")

    label("loc_D0A")

    Return()

    # Function_0_CEC end

    def Function_1_D0B(): pass

    label("Function_1_D0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D27")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_D0B")

    label("loc_D27")

    Return()

    # Function_1_D0B end

    def Function_2_D28(): pass

    label("Function_2_D28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D55")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_D6F")

    label("loc_D55")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_DAC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_D93")
    Jump("loc_DAC")

    label("loc_D93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x0)"), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAC")
    Event(0, 9)

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_END)), "loc_DBA")
    SetChrFlags(0x11, 0x80)

    label("loc_DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_END)), "loc_DC8")
    SetChrFlags(0x12, 0x80)

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_END)), "loc_DD6")
    SetChrFlags(0x13, 0x80)

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_END)), "loc_DE4")
    SetChrFlags(0x14, 0x80)

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_END)), "loc_DF2")
    SetChrFlags(0x15, 0x80)

    label("loc_DF2")

    Return()

    # Function_2_D28 end

    def Function_3_DF3(): pass

    label("Function_3_DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_END)), "loc_E4A")
    SetMapObjFrame(0xD, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_EA1")

    label("loc_E4A")

    SetMapObjFrame(0xD, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "on_kp")
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 4)), scpexpr(EXPR_END)), "loc_EF8")
    SetMapObjFrame(0xF, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "off_kp")
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_F58")

    label("loc_EF8")

    SetMapObjFrame(0xF, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "on_kp")
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    OP_1B(0x8, 0x0, 0xB)

    label("loc_F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_END)), "loc_FFD")
    SetMapObjFrame(0x11, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x11, 0x2)
    ClearMapObjFlags(0x12, 0x2)
    ClearMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_109F")

    label("loc_FFD")

    SetMapObjFrame(0x11, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x11, 0x2)
    SetMapObjFlags(0x12, 0x2)
    SetMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "on_kp")
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_END)), "loc_115E")
    SetMapObjFrame(0x14, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x14, 0x2)
    ClearMapObjFlags(0x15, 0x2)
    ClearMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 3, 0x80)
    Jump("loc_1219")

    label("loc_115E")

    SetMapObjFrame(0x14, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x14, 0x2)
    SetMapObjFlags(0x15, 0x2)
    SetMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "on_kp")
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_END)), "loc_12D7")
    SetMapObjFrame(0x19, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x19, 0x2)
    ClearMapObjFlags(0x1A, 0x2)
    ClearMapObjFlags(0x1B, 0x2)
    ClearMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "off_kp")
    ModifyEventFlags(0, 4, 0x80)
    Jump("loc_1391")

    label("loc_12D7")

    SetMapObjFrame(0x19, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x19, 0x2)
    SetMapObjFlags(0x1A, 0x2)
    SetMapObjFlags(0x1B, 0x2)
    SetMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "on_kp")
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1391")

    SetMapObjFrame(0xB, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C9")
    OP_70(0x1E, 0x0)
    Jump("loc_17CD")

    label("loc_17C9")

    OP_70(0x1E, 0x1E)

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E0")
    OP_70(0x1F, 0x0)
    Jump("loc_17E4")

    label("loc_17E0")

    OP_70(0x1F, 0x1E)

    label("loc_17E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F7")
    OP_70(0x20, 0x0)
    Jump("loc_17FB")

    label("loc_17F7")

    OP_70(0x20, 0x1E)

    label("loc_17FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180E")
    OP_70(0x21, 0x0)
    Jump("loc_1812")

    label("loc_180E")

    OP_70(0x21, 0x1E)

    label("loc_1812")

    Call(0, 4)
    Return()

    # Function_3_DF3 end

    def Function_4_1816(): pass

    label("Function_4_1816")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1845")
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x11, 0x8)
    Jump("loc_1859")

    label("loc_1845")

    ClearChrFlags(0x9, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1859")
    ClearChrFlags(0x11, 0x8)

    label("loc_1859")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1872")
    SetMapObjFlags(0x1E, 0x4)
    Jump("loc_1878")

    label("loc_1872")

    ClearMapObjFlags(0x1E, 0x4)

    label("loc_1878")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_189E")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    Jump("loc_18A8")

    label("loc_189E")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)

    label("loc_18A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F3")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    Jump("loc_1940")

    label("loc_18F3")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1922")
    ClearChrFlags(0x13, 0x8)

    label("loc_1922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1931")
    ClearChrFlags(0x14, 0x8)

    label("loc_1931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1940")
    ClearChrFlags(0x15, 0x8)

    label("loc_1940")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1961")
    SetChrFlags(0x10, 0x8)
    Jump("loc_1966")

    label("loc_1961")

    ClearChrFlags(0x10, 0x8)

    label("loc_1966")

    Return()

    # Function_4_1816 end

    def Function_5_1967(): pass

    label("Function_5_1967")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A51")
    Sound(14, 0, 100, 0)
    OP_71(0x1E, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_19E7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_1A4C")

    label("loc_19E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1E, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A4C")

    Jump("loc_1A9A")

    label("loc_1A51")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You just gave me indichestion.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1A9A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1967 end

    def Function_6_1AA6(): pass

    label("Function_6_1AA6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B90")
    Sound(14, 0, 100, 0)
    OP_71(0x1F, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x50, 1)"), scpexpr(EXPR_END)), "loc_1B26")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1B8B")

    label("loc_1B26")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1F, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B8B")

    Jump("loc_1C09")

    label("loc_1B90")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm glad you came to see me again, but\x01",
            "I really need some 'me' time right now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1C09")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1AA6 end

    def Function_7_1C15(): pass

    label("Function_7_1C15")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFF")
    Sound(14, 0, 100, 0)
    OP_71(0x20, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x51, 1)"), scpexpr(EXPR_END)), "loc_1C95")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x51),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_1CFA")

    label("loc_1C95")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x51),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x20, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CFA")

    Jump("loc_1D44")

    label("loc_1CFF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Aidios will remember that.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1D44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1C15 end

    def Function_8_1D50(): pass

    label("Function_8_1D50")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3A")
    Sound(14, 0, 100, 0)
    OP_71(0x21, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1DD0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1E35")

    label("loc_1DD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x21, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E35")

    Jump("loc_1EA3")

    label("loc_1E3A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Maybe the real Geofront was the\x01",
            "friends we made along the way.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1EA3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1D50 end

    def Function_9_1EAF(): pass

    label("Function_9_1EAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-640, 1500, -100980, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21990, 0)
    SetChrPos(0x101, -500, 200, -96250, 0)
    SetChrPos(0x102, 500, 200, -96000, 0)
    SetChrPos(0x103, -500, 200, -94750, 0)
    SetChrPos(0x104, 500, 200, -94500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x1, 0x0, 0x14, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x1)
    OP_68(0, 1700, -101250, 3000)

    def lambda_1FA2():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FA2)

    def lambda_1FBC():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FBC)
    Sleep(50)

    def lambda_1FD0():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FD0)

    def lambda_1FEA():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FEA)
    Sleep(50)

    def lambda_1FFE():
        OP_97(0x103, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FFE)

    def lambda_2018():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2018)
    Sleep(50)

    def lambda_202C():
        OP_97(0x104, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_202C)

    def lambda_2046():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2046)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    def lambda_205F():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_205F)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x102, 2)

    def lambda_2074():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2074)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)

    def lambda_2089():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2089)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x104, 2)

    def lambda_209E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_209E)
    OP_71(0x1, 0x14, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_79(0x1)
    OP_68(10670, 1500, -98680, 3000)
    SetCameraDistance(27840, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#2P#0105FWhat in the world is that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2P#0001FIs this what's causing all the\x01",
            "waterworks issues...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2P#0301FProbably. Can't say I've ever\x01",
            "seen this kinda thing, either...\x02\x03",
            "#0303FIs this another archaism? All the\x01",
            "ice must be this guy's fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2P#0203FYes, most likely.\x02\x03",
            "#0200FAccording to the database, there is not\x01",
            "any equipment here that could cause\x01",
            "such a drastic drop in temperature.\x02\x03",
            "On top of that, for the water shortages\x01",
            "to extend as far as they have, there must\x01",
            "be similar archaisms throughout this area.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-640, 1500, -100980, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21990, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0003FIf that's the case, we've got to\x01",
            "put an end to it, right now!\x02\x03",
            "#0001FEveryone, stay on guard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F#4PYes!\x02",
    )


    ChrTalk(
        0x103,
        "#0200F#3PRoger that.\x02",
    )


    ChrTalk(
        0x104,
        "#0307F#11PYou got it!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1250, 0, -100000, 90)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_29(0x34, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_9_1EAF end

    def Function_10_2470(): pass

    label("Function_10_2470")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x11, 0)
    TurnDirection(0x1, 0x11, 0)
    TurnDirection(0x2, 0x11, 0)
    TurnDirection(0x3, 0x11, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25F5")
    Battle("BattleInfo_6DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x11, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 7000, 0, -100500, 90)
    SetChrPos(0x1, 6750, 0, -99500, 90)
    SetChrPos(0x2, 5500, 0, -100500, 90)
    SetChrPos(0x3, 5250, 0, -99500, 90)
    OP_68(9810, 1500, -98880, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xD, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0xD, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 3)

    label("loc_25F5")

    SetChrPos(0x0, 7000, 0, -100000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_2470 end

    def Function_11_260E(): pass

    label("Function_11_260E")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMapFlags(0x8000000)
    OP_68(-196220, 1150, -199880, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -195220, 150, -199880, 270)
    SetChrPos(0x1, -195220, 150, -199880, 270)
    SetChrPos(0x2, -195220, 150, -199880, 270)
    SetChrPos(0x3, -195220, 150, -199880, 270)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x12, 0)
    TurnDirection(0x1, 0x12, 0)
    TurnDirection(0x2, 0x12, 0)
    TurnDirection(0x3, 0x12, 0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2844")
    Battle("BattleInfo_720", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x12, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x1, 0x1)
    OP_1B(0x8, 0xFF, 0xFFFF)
    SetChrPos(0x0, -197000, 0, -200500, 270)
    SetChrPos(0x1, -196750, 0, -199500, 270)
    SetChrPos(0x2, -195500, 0, -200500, 270)
    SetChrPos(0x3, -195250, 0, -199500, 270)
    OP_68(-199000, 1000, -200000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0xF, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFrame(0xFF, "simo01", 0x2, "off")
    SetMapObjFrame(0xFF, "simo01ice02_add", 0x2, "off")
    Sleep(2000)
    SetChrPos(0x0, -195250, 0, -200000, 270)
    SetScenarioFlags(0x56, 4)
    Jump("loc_2883")

    label("loc_2844")

    OP_68(-105610, 3500, -199960, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x0, -105610, 2000, -199960, 90)

    label("loc_2883")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_260E end

    def Function_12_288B(): pass

    label("Function_12_288B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x13, 0)
    TurnDirection(0x1, 0x13, 0)
    TurnDirection(0x2, 0x13, 0)
    TurnDirection(0x3, 0x13, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A55")
    Battle("BattleInfo_720", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x13, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetChrPos(0x0, -16500, -6000, -295500, 0)
    SetChrPos(0x1, -15500, -6000, -295750, 0)
    SetChrPos(0x2, -16500, -6000, -297000, 0)
    SetChrPos(0x3, -15500, -6000, -297250, 0)
    OP_68(-16650, -5000, -299430, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x11, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x12, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x13, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x11, 0x2)
    ClearMapObjFlags(0x12, 0x2)
    ClearMapObjFlags(0x13, 0x2)
    SetMapObjFrame(0xFF, "simo02", 0x2, "off")
    SetMapObjFrame(0xFF, "simo02ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo02ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 5)

    label("loc_2A55")

    SetChrPos(0x0, -16000, -6000, -295500, 0)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_288B end

    def Function_13_2A6E(): pass

    label("Function_13_2A6E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x14, 0)
    TurnDirection(0x1, 0x14, 0)
    TurnDirection(0x2, 0x14, 0)
    TurnDirection(0x3, 0x14, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4F")
    Battle("BattleInfo_6DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x14, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    SetChrPos(0x0, 6250, -2000, -300500, 90)
    SetChrPos(0x1, 6000, -2000, -299500, 90)
    SetChrPos(0x2, 4750, -2000, -300500, 90)
    SetChrPos(0x3, 4500, -2000, -299500, 90)
    OP_68(15720, -1000, -296640, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(60000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x14, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x15, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1C, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x14, 0x2)
    ClearMapObjFlags(0x15, 0x2)
    ClearMapObjFlags(0x1C, 0x2)
    SetMapObjFrame(0xFF, "simo03", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice03_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo03ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 6)

    label("loc_2C4F")

    SetChrPos(0x0, 6250, -2000, -300000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2A6E end

    def Function_14_2C68(): pass

    label("Function_14_2C68")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    TurnDirection(0x0, 0x15, 0)
    TurnDirection(0x1, 0x15, 0)
    TurnDirection(0x2, 0x15, 0)
    TurnDirection(0x3, 0x15, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E48")
    Battle("BattleInfo_720", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x1)
    OP_E0(0x2)
    SetChrFlags(0x15, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    SetChrPos(0x0, 19750, -2000, -300500, 90)
    SetChrPos(0x1, 19500, -2000, -299500, 90)
    SetChrPos(0x2, 18250, -2000, -300500, 90)
    SetChrPos(0x3, 18000, -2000, -299500, 90)
    OP_68(29410, -5000, -301840, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(58500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x19, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1A, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1B, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x1D, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x19, 0x2)
    ClearMapObjFlags(0x1A, 0x2)
    ClearMapObjFlags(0x1B, 0x2)
    ClearMapObjFlags(0x1D, 0x2)
    SetMapObjFrame(0xFF, "simo04", 0x2, "off")
    SetMapObjFrame(0xFF, "simo04ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo04ice03_01add", 0x2, "off")
    Sleep(2000)
    SetScenarioFlags(0x56, 7)

    label("loc_2E48")

    SetChrPos(0x0, 19750, -2000, -300000, 90)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2C68 end

    def Function_15_2E61(): pass

    label("Function_15_2E61")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE0")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F40")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_2F5F")

    label("loc_2F40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F5F")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_2F5F")

    OP_68(600, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 100000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0111", 0, 0, 0)
    IdleLoop()

    label("loc_2FE0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2E61 end

    def Function_16_2FE8(): pass

    label("Function_16_2FE8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 100600, 0)
    OP_90(0x1, -600, 30000, 100600, 0)
    OP_90(0x2, -600, 30000, 99400, 0)
    OP_90(0x3, 600, 30000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30BB")
    OP_90(0x4, -600, 30000, 98200, 0)
    OP_90(0x5, 600, 30000, 98200, 0)
    Jump("loc_30DA")

    label("loc_30BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30DA")
    OP_90(0x4, 0, 30000, 98200, 0)

    label("loc_30DA")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 100000, 3000)
    SetMapObjFrame(0xB, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xB)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_16_2FE8 end

    def Function_17_312F(): pass

    label("Function_17_312F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B0")
    Fade(500)
    SetChrPos(0x0, 100600, 0, -499400, 90)
    SetChrPos(0x1, 100600, 0, -500600, 90)
    SetChrPos(0x2, 99400, 0, -500600, 90)
    SetChrPos(0x3, 99400, 0, -499400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_320E")
    SetChrPos(0x4, 98200, 0, -500600, 90)
    SetChrPos(0x5, 98200, 0, -499400, 90)
    Jump("loc_322D")

    label("loc_320E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_322D")
    SetChrPos(0x4, 98200, 0, -500000, 90)

    label("loc_322D")

    OP_68(100000, 1000, -500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(100000, -4000, -500000, 2000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down")
    Sleep(1000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0113", 0, 0, 0)
    IdleLoop()

    label("loc_32B0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_17_312F end

    def Function_18_32B8(): pass

    label("Function_18_32B8")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x1, 0x0)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "down_kp")
    Sleep(1)
    OP_68(100000, -4000, -500000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 100600, -10000, -499400, 90)
    OP_90(0x1, 100600, -10000, -500600, 90)
    OP_90(0x2, 99400, -10000, -500600, 90)
    OP_90(0x3, 99400, -10000, -499400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_338D")
    OP_90(0x4, 98200, -10000, -500600, 90)
    OP_90(0x5, 98200, -10000, -499400, 90)
    Jump("loc_33AC")

    label("loc_338D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33AC")
    OP_90(0x4, 98200, -10000, -500000, 90)

    label("loc_33AC")

    Sound(145, 0, 100, 0)
    OP_68(100000, 1000, -500000, 3000)
    SetMapObjFrame(0xC, "m00ele00", 0x2, "up")
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0xC)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_32B8 end

    SaveToFile()

Try(main)
