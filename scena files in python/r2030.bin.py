from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2030.bin",                # FileName
        "r2030",                    # MapName
        "r2030",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2030", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2030",                  # 0
        "Kopan",                  # 1
        "Peter",                  # 2
        "Armored Hydra",          # 3
        "車",                     # 4
        "Bus",                    # 5
        "br2000",                 # 6
        "br2000",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "br2000",                 # 10
        "br2000",                 # 11
        "br2000",                 # 12
        "To Crossbell City",      # 13
        "To Doll Studio",         # 14
        "To Mainz Mining Village",# 15
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_B4", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_C4", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_D4", 9,   0,   4,   0,   2,   0,   7)
    Sepith("Sepith_E4", 10,  0,   0,   4,   3,   5,   0)
    Sepith("Sepith_F4", 32,  32,  32,  32,  32,  32,  32)

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
    MonsterBattlePostion("MonsterBattlePostion_164", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_184", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_24C", 0x0010, 14, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms62500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_314", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_C4", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3DC", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69400.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4A4", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_56C", 0x0000, 14, 6, 90, 8, 1, 50, 0, "br2000", "Sepith_F4", 30, 40, 20, 10,
        (
            ("ms66402.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66402.dat", "ms66402.dat", "ms66402.dat", "ms66402.dat", 0, 0, 0, 0, "MonsterBattlePostion_144", "MonsterBattlePostion_124", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_634", 0x0000, 35, 6, 0, 0, 1, 0, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77800.dat", "ms77800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_164", "MonsterBattlePostion_124", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50166.itc",                   # 00
        "apl/ch50165.itc",                   # 01
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch77450.itc",               # 16
        "monster/ch77450.itc",               # 17
        "monster/ch69450.itc",               # 18
        "monster/ch69450.itc",               # 19
        "monster/ch66450.itc",               # 1A
        "monster/ch66450.itc",               # 1B
        "monster/ch77850.itc",               # 1C
        "monster/ch77851.itc",               # 1D
    ))

    DeclNpc(-61770,  0,       150589,  90,   405,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-59430,  0,       145979,  45,   405,  0x0, 0,   1,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-55750,  7500,    67959,   180,  484,  0x0, 0,   28,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-7080,   38670,   1500,    0x1010000,    "BattleInfo_184", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-51440,  65480,   6000,    0x1010000,    "BattleInfo_24C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-34210,  55840,   0,       0x1010000,    "BattleInfo_314", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-22190,  95940,   0,       0x1010000,    "BattleInfo_3DC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-35010,  114720,  0,       0x1010000,    "BattleInfo_3DC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(2700,    112600,  3810,    0x1010000,    "BattleInfo_4A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-73010,  151070,  0,       0x1010000,    "BattleInfo_184", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-29990,  100980,  0,       0x1010000,    "BattleInfo_56C", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 16,  -29.84000015258789,    82.05000305175781,     -1.0,                  2500.0,                [0.05000000074505806,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.4919999837875366,    -16.410001754760742,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 20,  -42.72999954223633,    124.55999755859375,    -0.5,                  256.0,                 [0.17677663266658783,  0.08838837593793869,   -0.0,                  0.0,                   -0.17677675187587738,  0.08838831633329391,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   29.57297706604004,     -7.232813358306885,    0.10000000149011612,   1.0])

    DeclActor(-55750,  6000,    67960,   1200,    -55750,  7000,    67960,   0x007C, 0,  4,  0x0000)
    DeclActor(-26000,  0,       116600,  1500,    -26000,  1500,    116600,  0x007C, 0,  15, 0x0000)
    DeclActor(-64190,  0,       161190,  1200,    -53600,  -2000,   160500,  0x007C, 0,  14, 0x0000)
    DeclActor(-32950,  0,       55220,   1200,    -32950,  0,       55220,   0x007C, 0,  5,  0x0000)
    DeclActor(-66470,  0,       184850,  1200,    -66470,  0,       184850,  0x007C, 0,  6,  0x0000)
    DeclActor(-61640,  0,       151360,  5000,    -61640,  0,       151360,  0x007C, 0,  18, 0x0000)
    DeclActor(-38630,  0,       101340,  1500,    -38630,  1700,    101340,  0x007C, 0,  19, 0x0000)

    PlaceName(-1.0, 0.0, -15.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(38.25, 0.0, 116.25, 0x0000, 0x0000, "To Doll Studio")
    PlaceName(-86.0, 0.0, 235.0, 0x0000, 0x0000, "To Mainz Mining Village")
    PlaceName(-26.0, 0.0, 116.5999984741211, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_B6C",          # 00, 0
        "Function_1_B8B",          # 01, 1
        "Function_2_BA8",          # 02, 2
        "Function_3_C20",          # 03, 3
        "Function_4_DF8",          # 04, 4
        "Function_5_10C4",         # 05, 5
        "Function_6_10D8",         # 06, 6
        "Function_7_10EC",         # 07, 7
        "Function_8_1103",         # 08, 8
        "Function_9_11C7",         # 09, 9
        "Function_10_12E8",        # 0A, 10
        "Function_11_142B",        # 0B, 11
        "Function_12_14C0",        # 0C, 12
        "Function_13_167C",        # 0D, 13
        "Function_14_17F1",        # 0E, 14
        "Function_15_18EB",        # 0F, 15
        "Function_16_1A70",        # 10, 16
        "Function_17_1F25",        # 11, 17
        "Function_18_2099",        # 12, 18
        "Function_19_3058",        # 13, 19
        "Function_20_30D6",        # 14, 20
    ))


    def Function_0_B6C(): pass

    label("Function_0_B6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_B6C")

    label("loc_B8A")

    Return()

    # Function_0_B6C end

    def Function_1_B8B(): pass

    label("Function_1_B8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA7")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_B8B")

    label("loc_BA7")

    Return()

    # Function_1_B8B end

    def Function_2_BA8(): pass

    label("Function_2_BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BB6")
    Jump("loc_BFE")

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BD8")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    Jump("loc_BFE")

    label("loc_BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    Jump("loc_BFE")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BFE")

    label("loc_BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C0D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 17)

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_C1C")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 11)

    label("loc_C1C")

    Call(0, 7)
    Return()

    # Function_2_BA8 end

    def Function_3_C20(): pass

    label("Function_3_C20")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C38")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C38")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C4A")
    Jump("loc_C87")

    label("loc_C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C64")
    Jump("loc_C87")

    label("loc_C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C76")
    Jump("loc_C87")

    label("loc_C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_C87")
    OP_66(0x5, 0x1)

    label("loc_C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9A")
    OP_70(0x0, 0x0)
    Jump("loc_C9E")

    label("loc_C9A")

    OP_70(0x0, 0x1E)

    label("loc_C9E")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 5)), scpexpr(EXPR_END)), "loc_D04")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -32950, 0, 55220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_D5D")

    label("loc_D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 6)), scpexpr(EXPR_END)), "loc_D5D")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -66470, 0, 184850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_D5D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D75")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_D75")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -53600, -3000, 160500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7A, 0xFFFF2C20, 0x0, 0x3087C, 0x2710, 0x13880, 0x64, 0x0)
    OP_E1(0xFFFFADBC, 0x0, 0x20E54)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF7")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_DF7")

    Return()

    # Function_3_C20 end

    def Function_4_DF8(): pass

    label("Function_4_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E93")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sense powerful monsters in the chest.\x01",
            "Monster level: 35\x01",
            "Open and challenge?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E93")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_E93")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1052")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F92")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_EEC():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EEC)

    def lambda_F06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F06)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_634", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F73"),
        (2, "loc_F82"),
        (1, "loc_F8F"),
        (SWITCH_DEFAULT, "loc_F92"),
    )


    label("loc_F73")

    SetScenarioFlags(0x72, 3)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_F92")

    label("loc_F82")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_F8F")

    OP_B7(0x0)
    Return()

    label("loc_F92")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA2, 1)"), scpexpr(EXPR_END)), "loc_FEA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_104D")

    label("loc_FEA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA2),
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

    label("loc_104D")

    Jump("loc_10B8")

    label("loc_1052")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is unbecoming for a law enforcer to be this greedy.\x01",
            "You lose 15 DP.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10B8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DF8 end

    def Function_5_10C4(): pass

    label("Function_5_10C4")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 5)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_10C4 end

    def Function_6_10D8(): pass

    label("Function_6_10D8")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 6)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_10D8 end

    def Function_7_10EC(): pass

    label("Function_7_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7C, 0)), scpexpr(EXPR_END)), "loc_10FD")
    ClearScenarioFlags(0x7C, 0)
    Jump("loc_1102")

    label("loc_10FD")

    SetChrFlags(0x14, 0x80)

    label("loc_1102")

    Return()

    # Function_7_10EC end

    def Function_8_1103(): pass

    label("Function_8_1103")

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
            "Mainz Mining Village\x01",             # 1
            "Leave\x01",                            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    Call(0, 9)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11BF")

    label("loc_119F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")
    Call(0, 10)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_11BF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1103 end

    def Function_9_11C7(): pass

    label("Function_9_11C7")

    Fade(1000)
    OP_68(-31260, 600, 114980, 0)
    MoveCamera(26, 35, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xC)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, -44260, 0, 125040, 45)
    OP_D3(0xC, 0x0, 0xAFC8, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_12A2():
        OP_95(0xFE, -31020, 0, 111190, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12A2)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_9_11C7 end

    def Function_10_12E8(): pass

    label("Function_10_12E8")

    Fade(1000)
    OP_68(-27890, 600, 110180, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24420, 0, 115080, 225)
    SetChrPos(0x2, -23880, 0, 114510, 225)
    SetChrPos(0x3, -23300, 0, 113860, 225)
    ClearChrFlags(0xC, 0x80)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    OP_78(0x1, 0xC)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xC, -29790, 0, 93520, 0)
    OP_D3(0xC, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)

    def lambda_13C3():
        OP_95(0xFE, -28360, 0, 100110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13C3)
    Sleep(500)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xC, 1)

    def lambda_13F0():
        OP_9E(0xFE, 0xFFFF67A8, 0x19064, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13F0)
    WaitChrThread(0xC, 1)
    OP_71(0x1, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_10_12E8 end

    def Function_11_142B(): pass

    label("Function_11_142B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -24980, 0, 115700, 225)
    SetChrPos(0x1, -24980, 0, 115700, 225)
    SetChrPos(0x2, -24980, 0, 115700, 225)
    SetChrPos(0x3, -24980, 0, 115700, 225)
    OP_68(-24980, 600, 115700, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_142B end

    def Function_12_14C0(): pass

    label("Function_12_14C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159A")

    ChrTalk(
        0xFE,
        (
            "You guys are never going to believe\x01",
            "what I just heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The branch manager apparently invited\x01",
            "a legendary master angler from Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You think he's really all that?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1611")

    label("loc_159A")


    ChrTalk(
        0xFE,
        (
            "Still, it's kinda annoying that Cerdan\x01",
            "treats him like he's some fishing god.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You think he'd sign my rod...?\x02",
    )

    CloseMessageWindow()

    label("loc_1611")

    Jump("loc_1678")

    label("loc_1616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1678")

    ChrTalk(
        0xFE,
        "Hey. Some nice weather, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I might just chill out\x01",
            "here all day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1678")

    TalkEnd(0xFE)
    Return()

    # Function_12_14C0 end

    def Function_13_167C(): pass

    label("Function_13_167C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1748")

    ChrTalk(
        0xFE,
        (
            "Heh. Cerdan and I are throwing a\x01",
            "special event for all the anglers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You see, Kopan normally fishes\x01",
            "alone like a bum, but I want him\x01",
            "to fish together with everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17ED")

    label("loc_1748")


    ChrTalk(
        0xFE,
        (
            "We're going to throw a special contest\x01",
            "for fishing enthusiasts during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's time for you to step out of your\x01",
            "comfort zone, Kopan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17ED")

    TalkEnd(0xFE)
    Return()

    # Function_13_167C end

    def Function_14_17F1(): pass

    label("Function_14_17F1")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FI almost feel bad reeling fish away\x01",
            "from such a perfect view... Almost.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-65120, 3500, 159810, 1500)
    MoveCamera(58, 36, 0, 1500)
    OP_6E(370, 1500)
    SetCameraDistance(25720, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E6")
    OP_E0(0x2)
    MiniGame(0x6, 0x6, 0xFFFF0088, 0x0, 0x27434, 0x67, 0xFFFF2EA0, 0xFFFFF448, 0x272F4)

    label("loc_18E6")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_14_17F1 end

    def Function_15_18EB(): pass

    label("Function_15_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18FC")
    Call(0, 8)
    Jump("loc_1A6F")

    label("loc_18FC")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19A5")

    ChrTalk(
        0x101,
        (
            "#0000FLet's not take the bus today.\x02\x03",
            "It's probably better if we hit the highway\x01",
            "on foot for this investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A69")

    label("loc_19A5")


    ChrTalk(
        0x104,
        (
            "#0300FLooks like Mainz-bound buses\x01",
            "come by, like, once an hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FSure would be nice if we could\x01",
            "use it right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108F(It's a little annoying how\x01",
            "relaxed these two are...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A69")

    SetScenarioFlags(0x0, 2)
    TalkEnd(0xFF)

    label("loc_1A6F")

    Return()

    # Function_15_18EB end

    def Function_16_1A70(): pass

    label("Function_16_1A70")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-68240, 3000, 154870, 0)
    MoveCamera(50, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(46000, 0)
    SetChrPos(0x101, -30810, 0, 99000, 0)
    SetChrPos(0x102, -29380, 0, 99060, 0)
    SetChrPos(0x103, -30840, 0, 97470, 0)
    SetChrPos(0x104, -29420, 0, 97610, 0)
    OP_68(-51220, 3000, 134370, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(8530, 600, 113580, 0)
    MoveCamera(85, 8, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(56000, 0)
    SetCameraDistance(53000, 6000)
    OP_6F(0x10)
    OP_0D()
    Fade(1000)

    def lambda_1B48():
        OP_95(0xFE, -30700, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B48)

    def lambda_1B62():
        OP_95(0xFE, -29300, 0, 104000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B62)

    def lambda_1B7C():
        OP_95(0xFE, -30700, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B7C)

    def lambda_1B96():
        OP_95(0xFE, -29300, 0, 102600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B96)
    OP_68(-30480, 4400, 103110, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(20770, 0)
    OP_68(-30480, 2400, 103110, 4000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-30480, 1400, 103110, 0)
    MoveCamera(30, 13, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(14500, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#1200253V#0001F#5PIs this the fork in the road you\x01",
            "were talking about, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200254V#0301F#12PCan't say I notice any traces of\x01",
            "a wolf 'round here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200255V#0103F#11PIt's possible it may have moved\x01",
            "elsewhere again.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-28670, 1400, 102930, 1000)
    OP_93(0x102, 0x5A, 0x190)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#1200256V#0105F#6PI know the path to the left will take us to\x01",
            "Mainz, but I'm not so sure about the right...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DBF)
    Sleep(50)

    def lambda_1DCF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DCF)
    Sleep(50)

    def lambda_1DDF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DDF)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x103,
        (
            "#1200257V#0205F#6PBased on the database's information,\x01",
            "details on that path are unknown.\x02\x03",
            "#1200258V#0201FIt might prove beneficial to investigate\x01",
            "it for the CPD's records.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200259V#0001F#6PYeah, might as well. Let's check it\x01",
            "out before committing to Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -30700, 0, 104000, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x64, 4)
    OP_29(0x40, 0x1, 0x3)
    OP_E0(0x2)
    Call(0, 7)
    EventEnd(0x5)
    Return()

    # Function_16_1A70 end

    def Function_17_1F25(): pass

    label("Function_17_1F25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-66420, 2100, 151650, 0)
    MoveCamera(19, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(28380, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x2, 0x400)
    SetChrFlags(0xB, 0x8000)
    OP_78(0x2, 0xB)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    OP_D3(0xB, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0x0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0xFA, 0x0)
    SetMapObjFrame(0xFF, "model11_shade", 0x0, 0x1)
    Sound(487, 0, 100, 0)
    OP_68(-61690, 2100, 149860, 7000)
    FadeToBright(1000, 0)
    SetChrPos(0xB, -68170, 250, 169170, 180)

    def lambda_2024():
        OP_95(0xFE, -67630, 0, 159580, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2024)
    Sleep(1550)
    Sound(458, 0, 100, 0)

    def lambda_2047():
        OP_9E(0xFE, 0xFFFF54B6, 0x27524, 0xFFFF7748, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2047)
    Sleep(2050)

    def lambda_2065():
        OP_95(0xFE, -53340, 250, 135000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2065)
    WaitChrThread(0xB, 1)
    OP_0D()
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1F25 end

    def Function_18_2099(): pass

    label("Function_18_2099")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-62080, 2900, 146930, 0)
    MoveCamera(28, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15120, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -63780, 0, 154290, 90)
    SetChrPos(0x102, -62070, 0, 153010, 90)
    SetChrPos(0x103, -63380, 0, 151590, 90)
    SetChrPos(0x104, -61980, 0, 150430, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#6P#0205FThe sight never becomes any less\x01",
            "impressive. I was not aware Crossbell\x01",
            "had such an amazing waterfall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FYes, this is one of Crossbell's landmarks.\x01",
            "You would be hard-pressed to find a\x01",
            "waterfall this grand in another country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FI bet. It gives off such a soothing vibe.\x02\x03",
            "#0004FNext time someone talks about cleansing\x01",
            "their heart and mind, I know exactly where\x01",
            "to send them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FShould we meditate under the waterfall?\x01",
            "We can do the oms and everything.\x02\x03",
            "#0309FThey say meditatin' under a waterfall\x01",
            "while only wearing a loincloth can help\x01",
            "you reach true enlightenment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0006FPoetic, but I think I'll pass.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0211FI would rather vomit than picture you\x01",
            "in a loincloth, thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0309FHahaha. C'mon, Tio Tot, don't be shy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FPutting that idea aside... This spot would\x01",
            "make a nice photo for Grace's article.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA1")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#0000FDo you mind taking a few photos for us,\x01",
            "Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0108FN-Not at all. Don't expect a masterpiece\x01",
            "from me, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
            "Ya just gotta peek through that lens,\x01",
            "give it a lil' click, then bam, we good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#12P#0103F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "There are no second chances when\x01",
            "it comes to a picture-perfect moment.\x02",
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
            "#6P#0000FC-Calm down, everyone. We should\x01",
            "let Elie focus on taking the photo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FRight... I'll try to live up to your\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x103, 0x5A, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#12P#0103FPhew... There we go. I took a\x01",
            "couple of extras, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHey, it looks like you pulled through.\x02\x03",
            "Well? How'd they turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI won't have an answer for you until\x01",
            "I've seen the developed photos.\x02\x03",
            "At the very least, I think they'll\x01",
            "get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIt would be a safe assumption to think\x01",
            "Elie has regained her photography skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2CA1")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x103, 0x5A, 0x1F4)
    OP_93(0x104, 0x5A, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#0103FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2E39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2E50")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2E67")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2E7E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2E95")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2EAC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2EC3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2EDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2EF1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2EF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FBE")

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FBE")


    ChrTalk(
        0x101,
        (
            "#6P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -61640, 0, 151360, 90)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x6)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x5, 0x1)
    EventEnd(0x5)
    Return()

    # Function_18_2099 end

    def Function_19_3058(): pass

    label("Function_19_3058")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South: Crossbell City - 159 selge\x01",
            "North: Mainz Mining Village - 152 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_3058 end

    def Function_20_30D6(): pass

    label("Function_20_30D6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0005FIt looks like there's another path to\x01",
            "the right. We should investigate it\x01",
            "before proceeding.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -37920, 0, 119750, 135)
    OP_68(-37920, 600, 119750, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x4)
    Return()

    # Function_20_30D6 end

    SaveToFile()

Try(main)
