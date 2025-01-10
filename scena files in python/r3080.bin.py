from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3080.bin",                # FileName
        "r3080",                    # MapName
        "r3080",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 5, 0, 6],
    )

    BuildStringList((
        "r3080",                  # 0
        "Living Totem",           # 1
        "bm0110",                 # 2
        "Monster",                # 3
        "Monster",                # 4
        "Monster",                # 5
        "Monster",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Arios",                  # 9
        "Bracer Scott",           # 10
        "br3000",                 # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "To Old Armorica Road",   # 17
        "Sun Fort",               # 18
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 8,   16,  0,   10,  5,   3,   0)
    Sepith("Sepith_B4", 7,   7,   7,   7,   7,   7,   7)
    Sepith("Sepith_C4", 15,  0,   0,   15,  5,   5,   2)

    MonsterBattlePostion("MonsterBattlePostion_D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_100", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_104", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_10C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_114", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_174", 0x0000, 25, 6, 60, 10, 1, 20, 0, "br3000", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 25, 6, 60, 10, 1, 30, 0, "br3000", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_304", 0x0000, 25, 6, 60, 10, 1, 40, 0, "br3000", "Sepith_C4", 75, 25, 0, 0,
        (
            ("ms71600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms71600.dat", "ms71600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_374", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61501.dat", "ms61501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_F4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_3B8", 0x0000, 25, 6, 60, 0, 1, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", "ms63500.dat", "ms63400.dat", 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0022, 26, 6, 0, 0, 1, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76200.dat", "ms76200.dat", "ms76200.dat", "ms76200.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_F4", "ed7402", "ed7403", "ATBonus_94"),
            (),
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch71650.itc",               # 12
        "monster/ch71650.itc",               # 13
        "monster/ch76250.itc",               # 14
        "monster/ch76251.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
        "monster/ch63550.itc",               # 18
        "monster/ch63550.itc",               # 19
        "monster/ch61550.itc",               # 1A
        "monster/ch61550.itc",               # 1B
    ))

    DeclNpc(54990,   10500,   98699,   0,    484,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    501,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-41710,  -32650,  10,      0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-42160,  36440,   10,      0x1010000,    "BattleInfo_23C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-1780,   57680,   6250,    0x1010000,    "BattleInfo_304", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(40790,   54660,   12500,   0x1010000,    "BattleInfo_23C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(38370,   94280,   10000,   0x1010000,    "BattleInfo_174", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(50320,   90510,   10000,   0x185010E,    "BattleInfo_374", 0,   26,  0xFFFF, 8,  9)

    DeclEvent(0x0040, 0, 9,   50.31999969482422,     90.51000213623047,     10.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -6.289999961853027,    -11.313750267028809,   -2.5,                  1.0])

    DeclActor(-40000,  100,     -42000,  1200,    -40000,  1100,    -42000,  0x007C, 0,  7,  0x0000)
    DeclActor(54990,   10100,   98700,   1200,    54990,   11100,   98700,   0x007C, 0,  8,  0x0000)
    DeclActor(-24540,  500,     -2060,   1200,    -24540,  2000,    -2060,   0x007C, 0,  16, 0x0000)

    PlaceName(-94.0, 0.0, -5.0, 0x0000, 0x0000, "To Old Armorica Road")
    PlaceName(68.0, 0.0, -1.0, 0x0000, 0x0000, "Sun Fort")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 9

    ScpFunction((
        "Function_0_838",          # 00, 0
        "Function_1_857",          # 01, 1
        "Function_2_876",          # 02, 2
        "Function_3_893",          # 03, 3
        "Function_4_8B0",          # 04, 4
        "Function_5_925",          # 05, 5
        "Function_6_93F",          # 06, 6
        "Function_7_E3D",          # 07, 7
        "Function_8_FCF",          # 08, 8
        "Function_9_1207",         # 09, 9
        "Function_10_187C",        # 0A, 10
        "Function_11_23C8",        # 0B, 11
        "Function_12_3C9B",        # 0C, 12
        "Function_13_3CF7",        # 0D, 13
        "Function_14_3D88",        # 0E, 14
        "Function_15_3DF5",        # 0F, 15
        "Function_16_3E44",        # 10, 16
    ))


    def Function_0_838(): pass

    label("Function_0_838")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_856")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_838")

    label("loc_856")

    Return()

    # Function_0_838 end

    def Function_1_857(): pass

    label("Function_1_857")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_875")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_857")

    label("loc_875")

    Return()

    # Function_1_857 end

    def Function_2_876(): pass

    label("Function_2_876")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_892")
    OP_A1(0xFE, 0x4E2, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_876")

    label("loc_892")

    Return()

    # Function_2_876 end

    def Function_3_893(): pass

    label("Function_3_893")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AF")
    OP_A1(0xFE, 0x2EE, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_893")

    label("loc_8AF")

    Return()

    # Function_3_893 end

    def Function_4_8B0(): pass

    label("Function_4_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 1)), scpexpr(EXPR_END)), "loc_924")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_924")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(131, 1, 100, 0)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
    StopEffect(0x0, 0x2)
    OP_24(0x83)
    ClearScenarioFlags(0xBA, 1)
    Jump("loc_924")

    label("loc_924")

    Return()

    # Function_4_8B0 end

    def Function_5_925(): pass

    label("Function_5_925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93E")
    Event(0, 10)

    label("loc_93E")

    Return()

    # Function_5_925 end

    def Function_6_93F(): pass

    label("Function_6_93F")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DC3")
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_DD7")

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD7")
    ClearChrFlags(0x17, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DD7")

    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x17, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFA")
    OP_70(0x0, 0x0)
    Jump("loc_DFE")

    label("loc_DFA")

    OP_70(0x0, 0x1E)

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E11")
    OP_70(0x3, 0x0)
    Jump("loc_E15")

    label("loc_E11")

    OP_70(0x3, 0x1E)

    label("loc_E15")

    LoadEffect(0x0, "map/mpr3000.eff")
    BeginChrThread(0x9, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3C")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_E3C")

    Return()

    # Function_6_93F end

    def Function_7_E3D(): pass

    label("Function_7_E3D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_EBD")
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
    SetScenarioFlags(0x107, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_F22")

    label("loc_EBD")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F22")

    Jump("loc_FC3")

    label("loc_F27")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You check the chest to see it full of fan mail\x01",
            "addressed to the SSS. It's sweet, but you\x01",
            "wonder how it got there.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_FC3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_E3D end

    def Function_8_FCF(): pass

    label("Function_8_FCF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118E")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CE")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1028():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1028)

    def lambda_1042():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1042)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_3B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_10AF"),
        (2, "loc_10BE"),
        (1, "loc_10CB"),
        (SWITCH_DEFAULT, "loc_10CE"),
    )


    label("loc_10AF")

    SetScenarioFlags(0x75, 5)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_10CE")

    label("loc_10BE")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_10CB")

    OP_B7(0x0)
    Return()

    label("loc_10CE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA0, 1)"), scpexpr(EXPR_END)), "loc_1126")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1189")

    label("loc_1126")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1189")

    Jump("loc_11FB")

    label("loc_118E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You may have met my brethren. Between\x01",
            "you and me...they're a little unhinged.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_11FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_FCF end

    def Function_9_1207(): pass

    label("Function_9_1207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 4)), scpexpr(EXPR_END)), "loc_1211")
    Return()

    label("loc_1211")

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
        (1, "loc_12F4"),
        (SWITCH_DEFAULT, "loc_130B"),
    )


    label("loc_12F4")

    Sleep(500)
    OP_90(0x0, 45210, 10000, 90260, 270)
    EventEnd(0x5)
    Return()

    label("loc_130B")

    Battle("BattleInfo_374", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(45210, 11000, 90260, 0)
    OP_90(0x0, 45210, 10000, 90260, 270)
    OP_90(0x1, 45210, 10000, 90260, 270)
    OP_90(0x2, 45210, 10000, 90260, 270)
    OP_90(0x3, 45210, 10000, 90260, 270)
    OP_90(0x4, 45210, 10000, 90260, 270)
    OP_90(0x5, 45210, 10000, 90260, 270)
    OP_90(0x6, 45210, 10000, 90260, 270)
    OP_90(0x7, 45210, 10000, 90260, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_13CD"),
        (1, "loc_13D0"),
        (SWITCH_DEFAULT, "loc_13D3"),
    )


    label("loc_13CD")

    EventEnd(0x5)
    Return()

    label("loc_13D0")

    OP_B7(0x0)
    Return()

    label("loc_13D3")

    FadeToDark(0, 0, -1)
    OP_68(49920, 11500, 89700, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18070, 0)
    EventBegin(0x0)
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster in the Ancient Battlefield!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xC, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1537")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52220, 10000, 91130, 252)
    SetChrPos(0x103, 51600, 10000, 88890, 324)
    SetChrPos(0x104, 49140, 10000, 88890, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1521")
    SetChrPos(0x10A, 48420, 10000, 91130, 108)
    Jump("loc_1532")

    label("loc_1521")

    SetChrPos(0x109, 48420, 10000, 91130, 108)

    label("loc_1532")

    Jump("loc_157B")

    label("loc_1537")

    SetChrPos(0x101, 50320, 10000, 92510, 180)
    SetChrPos(0x102, 52320, 10000, 90510, 270)
    SetChrPos(0x103, 50320, 10000, 88510, 0)
    SetChrPos(0x104, 48320, 10000, 90510, 90)

    label("loc_157B")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CC")

    ChrTalk(
        0x101,
        "#5P#0005FA craft book? It looks pretty beat up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1616")

    label("loc_15CC")


    ChrTalk(
        0x101,
        (
            "#5P#0000FThis craft book looks just as old\x01",
            "as the last one we found.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1616")


    ChrTalk(
        0x102,
        (
            "#11P#0103FIt looks like it covers how to\x01",
            "use a combination craft.\x02\x03",
            "#0100FThe techniques described in here remind\x01",
            "me of Randy and Tio's combat styles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#0305FOh, yeah, it totally does.\x02\x03",
            "#0300FMight be kinda hard to get the hang of,\x01",
            "but wanna give it a whirl, Tio Tot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0202FYes, we should test it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17AE")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_17AE")

    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x14F)
    AddCraft(0x3, 0x14F)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy and Tio learned \x07\x02",
            "[Haken Storm]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x79, 4)
    SetScenarioFlags(0xD8, 7)
    OP_29(0x33, 0x4, 0x10)
    OP_29(0x33, 0x4, 0x2)
    OP_29(0x33, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE(0x22, 0x0)
    EventEnd(0x5)
    Return()

    # Function_9_1207 end

    def Function_10_187C(): pass

    label("Function_10_187C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch76252.itc", 0x26)
    LoadChrToIndex("chr/ch33100.itc", 0x27)
    SetChrChipByIndex(0xA, 0x14)
    SetChrChipByIndex(0xB, 0x14)
    SetChrChipByIndex(0xC, 0x14)
    SetChrChipByIndex(0xD, 0x14)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 1, 0, 2)
    BeginChrThread(0xB, 1, 0, 2)
    BeginChrThread(0xC, 1, 0, 2)
    BeginChrThread(0xD, 1, 0, 2)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    OP_68(-77000, 1500, -2000, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -77000, 0, -2000, 90)
    SetChrPos(0x102, -77500, 0, -1000, 90)
    SetChrPos(0x103, -78500, 0, -3000, 90)
    SetChrPos(0x104, -79250, 0, -2000, 90)
    SetChrPos(0xE, -31500, 500, -2000, 270)
    SetChrPos(0xA, -36000, 550, 500, 135)
    SetChrPos(0xB, -36000, 550, -4500, 45)
    SetChrPos(0xC, -34000, 550, 2500, 135)
    SetChrPos(0xD, -34000, 550, -6500, 45)

    def lambda_1A43():
        OP_98(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A43)
    Sleep(50)

    def lambda_1A60():
        OP_98(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A60)
    Sleep(50)

    def lambda_1A7D():
        OP_98(0x103, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A7D)
    Sleep(50)

    def lambda_1A9A():
        OP_98(0x104, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A9A)
    OP_68(-70000, 1500, -2000, 4500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    NpcTalk(
        0xE,
        "Man's Voice",
        "#2P#4SS-Someone, please help me!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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
        "#5P#0107FThere he is, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0007FYeah!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(-32450, 1500, -2000, 4000)
    MoveCamera(90, 25, 0, 4000)
    SetCameraDistance(20230, 4000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    OP_6F(0x79)
    OP_98(0xE, 0x1F4, 0x0, 0x0, 0x1F4, 0x0)

    ChrTalk(
        0xE,
        "Wh-Why's this happening to me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Heeeeelp! Can't anybody\x01",
            "help me?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C8E():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1C8E)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    def lambda_1CBB():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1CBB)
    SetChrChipByIndex(0xB, 0x15)
    BeginChrThread(0xB, 1, 0, 3)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1CE8():
        OP_9B(0x0, 0xC, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1CE8)
    SetChrChipByIndex(0xC, 0x15)
    BeginChrThread(0xC, 1, 0, 3)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_1D15():
        OP_9B(0x0, 0xD, 0x0, 0x1F4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1D15)
    SetChrChipByIndex(0xD, 0x15)
    BeginChrThread(0xD, 1, 0, 3)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xA, 2)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xB, 2)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xC, 2)
    SetChrChipByIndex(0xC, 0x14)
    BeginChrThread(0xC, 1, 0, 2)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xD, 2)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xD, 1, 0, 2)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(19750, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "E-Eeek...!\x01",
            "Goddess, please have mercy!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -45000, 0, -1500, 90)
    SetChrPos(0x102, -45500, 0, -500, 90)
    SetChrPos(0x103, -46500, 0, -3500, 90)
    SetChrPos(0x104, -47250, 0, -2500, 90)

    ChrTalk(
        0x101,
        "#5P#0007FHold it!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_1ECB():
        OP_98(0x101, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ECB)
    Sleep(50)

    def lambda_1EE8():
        OP_98(0x102, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1EE8)
    Sleep(50)

    def lambda_1F05():
        OP_98(0x103, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1F05)
    Sleep(50)

    def lambda_1F22():
        OP_98(0x104, 0x1770, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F22)

    def lambda_1F3C():
        OP_93(0xA, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F3C)
    Sleep(50)

    def lambda_1F4C():
        OP_93(0xB, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F4C)
    Sleep(50)

    def lambda_1F5C():
        OP_93(0xC, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F5C)
    Sleep(50)

    def lambda_1F6C():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1F6C)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_68(-38540, 1500, -1750, 2500)
    MoveCamera(90, 13, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#6P#0302FHaha. Talk about impeccable timing, eh?\x01",
            "Saved the dude from going splat by mere\x01",
            "seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206FPlease explain how this timing is, in\x01",
            "any form, 'impeccable.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0007FWe're with the Crossbell Police Department!\x02\x03",
            "We'll distract the monsters for you, so make\x01",
            "a run for it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PO-Okay!\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_97(0xE, 0x0, 0x0, 0x3A98, 0x1388, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(17000, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(16000, 1000)
    OP_A6(0xB, 0x5, 0x5, 0x3E8, 0x3E8)
    Fade(500)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#0010FWh-Whoa!\x02\x03",
            "What's with these monsters?!\x01",
            "They look seriously tough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0107FThey seem to be different from the\x01",
            "usual monsters inhabiting the area!\x02\x03",
            "Are they from ancient times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FWell, either way, we'd better\x01",
            "not go easy on them.\x02\x03",
            "#0307FThink it's about time we show\x01",
            "our friends a lesson in pain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0207FHere they come!\x02",
    )

    CloseMessageWindow()

    def lambda_231B():
        OP_9B(0x0, 0xA, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_231B)
    SetChrChipByIndex(0xA, 0x15)
    BeginChrThread(0xA, 1, 0, 3)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)

    def lambda_2348():
        OP_9B(0x0, 0xB, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2348)
    SetChrChipByIndex(0xB, 0x15)
    BeginChrThread(0xB, 1, 0, 3)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EndChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x1)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_3FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)
    Return()

    # Function_10_187C end

    def Function_11_23C8(): pass

    label("Function_11_23C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00053.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00153.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00253.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("monster/ch76252.itc", 0x26)
    LoadChrToIndex("monster/ch76253.itc", 0x27)
    LoadChrToIndex("apl/ch50540.itc", 0x28)
    LoadChrToIndex("chr/ch27200.itc", 0x29)
    LoadChrToIndex("chr/ch33100.itc", 0x2A)
    LoadChrToIndex("chr/ch34300.itc", 0x2B)
    LoadChrToIndex("apl/ch50376.itc", 0x2C)
    LoadEffect(0x1, "battle\\btgun00.eff")
    LoadEffect(0x2, "event\\ev001_00.eff")
    LoadEffect(0x3, "event\\ev000_00.eff")
    LoadEffect(0x4, "event\\eva04_00.eff")
    OP_68(-38540, 1200, -2000, 0)
    MoveCamera(90, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(16500, 2000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    SetChrPos(0x101, -39000, 0, -1500, 90)
    SetChrPos(0x102, -39500, 0, -500, 90)
    SetChrPos(0x103, -40500, 0, -3500, 90)
    SetChrPos(0x104, -41250, 0, -2500, 90)
    SetChrPos(0xA, -36000, 550, 500, 225)
    SetChrPos(0xB, -36000, 550, -4500, 315)
    SetChrPos(0xC, -34000, 550, 2500, 225)
    SetChrPos(0xD, -34000, 550, -6500, 315)
    SetChrPos(0x10, -70000, 0, -2000, 90)
    SetChrPos(0x11, -71500, 0, -2000, 90)
    SetChrPos(0xE, -72500, 0, -2500, 90)
    SetChrPos(0xF, -72750, 0, -1500, 90)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x6)
    SetChrFlags(0x10, 0x8000)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2699")
    SetChrChipByIndex(0x101, 0x1F)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x23)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0xA, 0x14)
    SetChrChipByIndex(0xB, 0x14)
    SetChrChipByIndex(0xC, 0x14)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    BeginChrThread(0xB, 1, 0, 2)
    BeginChrThread(0xC, 1, 0, 2)
    BeginChrThread(0xD, 1, 0, 2)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Jump("loc_2705")

    label("loc_2699")

    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xA, 0x27)
    SetChrChipByIndex(0xB, 0x27)
    SetChrChipByIndex(0xC, 0x27)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xA, 0x1)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x1)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    label("loc_2705")

    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDB")
    OP_2C(0x1F, 0x3)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#6P#0010FD-Did we defeat them...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0108FPhew... That was tougher than\x01",
            "I had anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FWell, that was a friggin' pain.\x01",
            "The hell are these things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0208F...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(848, 0, 100, 0)

    def lambda_286E():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_286E)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7511", 0)

    ChrTalk(
        0x101,
        "#6P#0005FY-You can't be serious!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 1)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_293B():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_293B)
    Sleep(100)

    def lambda_2957():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2957)
    Sleep(100)

    def lambda_2973():
        OP_A6(0xA, 0xA, 0xA, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2973)
    WaitChrThread(0xB, 1)
    SetChrChipByIndex(0xB, 0x14)
    BeginChrThread(0xB, 1, 0, 2)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x14)
    BeginChrThread(0xC, 1, 0, 2)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x14)
    BeginChrThread(0xD, 1, 0, 2)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(17000, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x23)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x3)
    SetChrSubChip(0x103, 0x3)
    SetChrSubChip(0x104, 0x2)
    Sound(514, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CancelBlur(0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#6P#0106FOh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0210F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0310FCan't you guys stay down\x01",
            "for ONE second?!\x02\x03",
            "I'm WAY too beat to think\x01",
            "about fightin' again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0010F(This is bad. Really bad!)\x02\x03",
            "(We need to find a way out of\x01",
            "this situation!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD5")

    label("loc_2BDB")

    PlayBGM("ed7511", 0)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#6P#0010FUgh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0108FThese monsters are far stronger\x01",
            "than they appeared to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0310FOh, for cryin' out loud! How much\x01",
            "stamina do these things have?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0208F...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(1000)
    OP_82(0x96, 0x64, 0xBB8, 0x320)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(17000, 1000)
    OP_A6(0xA, 0x5, 0x5, 0x3E8, 0x3E8)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0xA, 0x14)
    BeginChrThread(0xA, 1, 0, 2)
    CancelBlur(0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#0010F(This is bad. Really bad!)\x02\x03",
            "(We need to find a way out of\x01",
            "this situation!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD5")

    Sound(530, 0, 100, 0)
    Sleep(500)
    BeginChrThread(0xA, 2, 0, 13)
    StopBGM(0xBB8)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0xA, 2)

    ChrTalk(
        0x101,
        "#6P#0005FHuh?!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Fade(500)
    OP_68(-68000, 1500, -2000, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    OP_68(-71000, 1500, -2000, 500)
    BeginChrThread(0x11, 1, 0, 12)
    SetChrChip(0x0, 0x10, 0x3C, 0x1F4)
    SetChrFlags(0x10, 0x20)

    def lambda_2EF4():
        OP_98(0x10, 0x4E20, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2EF4)
    OP_0D()
    WaitChrThread(0x10, 1)
    EndChrThread(0x11, 0x1)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    Fade(500)
    SetChrPos(0x10, -48500, 3500, -2000, 90)
    OP_68(-34500, 1900, -2000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15670, 0)
    BeginChrThread(0xB, 2, 0, 13)
    Sleep(100)
    BeginChrThread(0xC, 2, 0, 13)
    Sleep(100)
    BeginChrThread(0xD, 2, 0, 13)
    OP_98(0x10, 0x2EE0, 0xFFFFF448, 0x0, 0x4E20, 0x0)
    SetChrSubChip(0x10, 0x1)
    Sound(250, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10,
        "#10A#5P#1407FStrike!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    SetCameraDistance(20250, 6000)
    SetChrChip(0x0, 0x10, 0x3C, 0x1F4)
    SetChrSubChip(0x10, 0x7)
    PlayEffect(0x4, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_92(0x10, 0xFFFF7842, 0xF3C, 0x3E8)

    def lambda_307F():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_307F)

    def lambda_3090():
        OP_96(0x10, 0xFFFF7874, 0x1F4, 0xF46, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3090)
    Sleep(200)

    def lambda_30AD():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30AD)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    WaitChrThread(0x10, 2)
    BeginChrThread(0xA, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF85EE, 0xFA, 0x3E8)

    def lambda_30E5():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30E5)

    def lambda_30F6():
        OP_96(0x10, 0xFFFF85EE, 0x1F4, 0xFA, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_30F6)
    Sleep(200)

    def lambda_3113():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3113)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xC, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF7C8E, 0xFFFFE188, 0x3E8)

    def lambda_314B():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_314B)

    def lambda_315C():
        OP_96(0x10, 0xFFFF7C8E, 0x1F4, 0xFFFFE188, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_315C)
    Sleep(200)

    def lambda_3179():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3179)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xD, 2, 0, 15)
    WaitChrThread(0x10, 1)
    OP_92(0x10, 0xFFFF716C, 0xFFFFF830, 0x3E8)

    def lambda_31B1():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_31B1)

    def lambda_31C2():
        OP_96(0x10, 0xFFFF716C, 0x1F4, 0xFFFFF830, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_31C2)
    Sleep(200)

    def lambda_31DF():
        OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_31DF)
    WaitChrThread(0x10, 2)
    Sound(815, 0, 100, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0xB, 2, 0, 15)
    SetChrSubChip(0x10, 0x5)
    WaitChrThread(0x10, 1)
    Sleep(500)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    SetCameraDistance(21250, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x14)
    Fade(500)
    Sound(816, 0, 100, 0)
    Sound(834, 0, 100, 0)
    Sound(502, 0, 100, 0)
    BeginChrThread(0xA, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xD, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xC, 2, 0, 14)
    Sleep(50)
    BeginChrThread(0xB, 2, 0, 14)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)
    CancelBlur(0)
    OP_68(-38470, 1500, -2170, 2000)
    MoveCamera(46, 16, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17940, 2000)
    Sleep(500)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#0005FA-Arios?!\x02",
    )

    CloseMessageWindow()
    Sound(531, 0, 100, 0)
    OP_93(0x10, 0x10E, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x10,
        "#11P#1404FI made it just in the nick of time.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#0305FNo, hold on just a damn second!\x01",
            "What are you even doin' here?!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            "Hmph. An awfully cold reception,\x01",
            "considering I just saved your lives.\x02\x03",
            "Scott took it upon himself to handle\x01",
            "the request on his own.\x02\x03",
            "I'm aware of how dangerous the area\x01",
            "can be, so I thought I would offer my\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#6P#0102FThank you for saving us, Arios.\x01",
            "We appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0204FWe were incredibly lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#0306FYou can fool the ladies, but that damn\x01",
            "near-perfect timing ain't foolin' me!\x02\x03",
            "#0301FYou had the whole thing planned from\x01",
            "the start, didn'tcha?! Oh, no, pal. You\x01",
            "ain't strikin' your way into this heart!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11P#1404FHaha... I'll leave it to your imagination.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Hey, are you guys all right?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x11, -50500, 0, -2000, 90)
    SetChrPos(0xE, -51500, 0, -2500, 90)
    SetChrPos(0xF, -51750, 0, -1500, 90)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    OP_68(-42000, 1500, -2000, 3000)
    MoveCamera(44, 11, 0, 3000)
    SetCameraDistance(19740, 3000)

    def lambda_36F0():
        OP_98(0x11, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_36F0)
    Sleep(50)

    def lambda_370D():
        OP_98(0xE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_370D)
    Sleep(50)

    def lambda_372A():
        OP_98(0xF, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_372A)

    def lambda_3744():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3744)

    def lambda_3751():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3751)

    def lambda_375E():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_375E)

    def lambda_376B():
        TurnDirection(0x104, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_376B)
    WaitChrThread(0x11, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#0000FOh, Scott... It looks like she finally\x01",
            "woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PYep. Not too long ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#6PThank you so much, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PI don't know how I'll ever be able\x01",
            "to repay you bracers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PSeriously! We even got to see\x01",
            "an awesome show!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PYou took down those insane monsters\x01",
            "with one fell swoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PU-Umm, Scott? I think I felt my heart\x01",
            "flutter when you saved me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#6PAnd your skill with that rifle\x01",
            "was just... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0xF, 500)

    ChrTalk(
        0xE,
        "#12PW-Wait, honey...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x110, 0x1F4)

    ChrTalk(
        0x11,
        "#11PI'm just glad the two of you are safe.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0012FH-Haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306F*sigh* History is doomed to\x01",
            "repeat itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0102FDon't fret too hard, Randy. At\x01",
            "least we all worked together to\x01",
            "save the tourists, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0204FI would consider this mission accomplished.\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x11, 0x10, 500)
    OP_64(0x10)
    OP_64(0x11)

    ChrTalk(
        0x11,
        "#5PHmm? Something up, Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#11P#1403FNot particularly.\x02\x03",
            "#1400FI think we should focus on escorting\x01",
            "these two back to Armorica Village.\x02\x03",
            "#1404FWatch our six, Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C21():
        TurnDirection(0x101, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C21)
    Sleep(50)

    def lambda_3C31():
        TurnDirection(0x102, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C31)
    Sleep(50)

    def lambda_3C41():
        TurnDirection(0x103, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C41)
    Sleep(50)

    def lambda_3C51():
        TurnDirection(0x104, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C51)
    Sleep(300)

    ChrTalk(
        0x101,
        "#6P#0000FUnderstood!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x1F, 0x1, 0x3)
    NewScene("t0020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_23C8 end

    def Function_12_3C9B(): pass

    label("Function_12_3C9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF6")
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x1, 0xFF, 0xFE, 0x80, 0, 1100, 1400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(250)
    Jump("Function_12_3C9B")

    label("loc_3CF6")

    Return()

    # Function_12_3C9B end

    def Function_13_3CF7(): pass

    label("Function_13_3CF7")

    PlayEffect(0xA, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3D4A():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D4A)
    OP_A6(0xFE, 0xA, 0xA, 0x3E8, 0x9C4)
    SetChrChipByIndex(0xFE, 0x14)
    BeginChrThread(0xFE, 1, 0, 2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_3CF7 end

    def Function_14_3D88(): pass

    label("Function_14_3D88")

    PlayEffect(0x2, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A6(0xFE, 0xA, 0xA, 0x2EE, 0x9C4)
    OP_A7(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
    Return()

    # Function_14_3D88 end

    def Function_15_3DF5(): pass

    label("Function_15_3DF5")

    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_3DF5 end

    def Function_16_3E44(): pass

    label("Function_16_3E44")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is shut tight.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_3E44 end

    SaveToFile()

Try(main)
