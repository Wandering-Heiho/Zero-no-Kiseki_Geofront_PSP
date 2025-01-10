from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0594.bin",                # FileName
        "c0594",                    # MapName
        "c0594",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0594",                  # 0
        "Event Monster",          # 1
        "Event Monster",          # 2
        "Event Monster",          # 3
        "Killer Hammerhead",      # 4
        "bc0540",                 # 5
        "bc0540",                 # 6
        "bc0540",                 # 7
        "bc0540",                 # 8
        "bc0540",                 # 9
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 0,   15,  0,   20,  20,  0,   0)
    Sepith("Sepith_B4", 12,  7,   0,   18,  0,   0,   18)
    Sepith("Sepith_C4", 16,  0,   0,   0,   12,  12,  12)

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

    # monster count: 3

    BattleInfo(
        "BattleInfo_134", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_A4", 40, 30, 20, 10,
        (
            ("ms76700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76700.dat", "ms76700.dat", "ms76700.dat", "ms76700.dat", 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1FC", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0540", "Sepith_B4", 40, 30, 20, 10,
        (
            ("ms76900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2C4", 0x0000, 33, 6, 60, 4, 1, 30, 0, "bc0540", "Sepith_C4", 40, 30, 20, 10,
        (
            ("ms76500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76500.dat", "ms76500.dat", "ms76500.dat", "ms76500.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_38C", 0x0000, 33, 6, 45, 0, 1, 0, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76800.dat", "ms76800.dat", "ms76800.dat", "ms76800.dat", 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3D0", 0x0002, 33, 6, 45, 0, 1, 0, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76900.dat", "ms76900.dat", "ms76900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch76950.itc",               # 10
        "monster/ch76951.itc",               # 11
        "monster/ch76750.itc",               # 12
        "monster/ch76750.itc",               # 13
        "monster/ch76550.itc",               # 14
        "monster/ch76551.itc",               # 15
        "monster/ch76850.itc",               # 16
        "monster/ch76850.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   16,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-2000,   3500,    12000,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-14380,  10040,   500,     0x1010000,    "BattleInfo_134", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-31150,  10850,   30,      0x1010000,    "BattleInfo_1FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-28130,  -2100,   20,      0x1010000,    "BattleInfo_2C4", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-34000,  6000,    16000,   1200,    -34000,  7000,    16000,   0x007C, 0,  4,  0x0000)
    DeclActor(-18000,  1500,    500,     1200,    -18000,  2500,    500,     0x007C, 0,  5,  0x0000)
    DeclActor(-2000,   3000,    12000,   1200,    -2000,   4000,    12000,   0x007C, 0,  6,  0x0000)
    DeclActor(-14000,  500,     13000,   1200,    -14000,  1500,    13000,   0x007C, 0,  7,  0x0000)
    DeclActor(-5000,   500,     -8000,   1200,    -5000,   1500,    -8000,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_678",          # 00, 0
        "Function_1_695",          # 01, 1
        "Function_2_6B2",          # 02, 2
        "Function_3_6C4",          # 03, 3
        "Function_4_A56",          # 04, 4
        "Function_5_BB5",          # 05, 5
        "Function_6_CF0",          # 06, 6
        "Function_7_F04",          # 07, 7
        "Function_8_FE3",          # 08, 8
        "Function_9_10C2",         # 09, 9
        "Function_10_12DC",        # 0A, 10
        "Function_11_1816",        # 0B, 11
        "Function_12_1864",        # 0C, 12
        "Function_13_18B2",        # 0D, 13
    ))


    def Function_0_678(): pass

    label("Function_0_678")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_694")
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_678")

    label("loc_694")

    Return()

    # Function_0_678 end

    def Function_1_695(): pass

    label("Function_1_695")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B1")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_695")

    label("loc_6B1")

    Return()

    # Function_1_695 end

    def Function_2_6B2(): pass

    label("Function_2_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C3")
    Event(0, 10)

    label("loc_6C3")

    Return()

    # Function_2_6B2 end

    def Function_3_6C4(): pass

    label("Function_3_6C4")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -16000, 0, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -12000, 0, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -16000, 3000, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -12000, 3000, 16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -16000, 3000, -16000, 3000, 1000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -12000, 3000, -16000, 3000, 1000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 2)), scpexpr(EXPR_END)), "loc_7C0")
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_70(0x3, 0x2D)
    OP_70(0x4, 0x2D)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_800")

    label("loc_7C0")

    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)

    label("loc_800")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A23")
    OP_70(0x0, 0x0)
    Jump("loc_A27")

    label("loc_A23")

    OP_70(0x0, 0x1E)

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3A")
    OP_70(0x1, 0x0)
    Jump("loc_A3E")

    label("loc_A3A")

    OP_70(0x1, 0x1E)

    label("loc_A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A51")
    OP_70(0x2, 0x0)
    Jump("loc_A55")

    label("loc_A51")

    OP_70(0x2, 0x1E)

    label("loc_A55")

    Return()

    # Function_3_6C4 end

    def Function_4_A56(): pass

    label("Function_4_A56")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x78, 1)"), scpexpr(EXPR_END)), "loc_AD6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_B3B")

    label("loc_AD6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x78),
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

    label("loc_B3B")

    Jump("loc_BA9")

    label("loc_B40")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Annie's not okay. She wants you to\x01",
            "Arrest the Smooth Criminal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_BA9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A56 end

    def Function_5_BB5(): pass

    label("Function_5_BB5")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x200\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x113, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_CDE")

    label("loc_C7A")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In Crossbell...first you get the sepith,\x01",
            "then you get the mira,\x01",
            "then you get the women.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_CDE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BB5 end

    def Function_6_CF0(): pass

    label("Function_6_CF0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAF")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D49():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D49)

    def lambda_D63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_D63)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_38C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_DD0"),
        (2, "loc_DDF"),
        (1, "loc_DEC"),
        (SWITCH_DEFAULT, "loc_DEF"),
    )


    label("loc_DD0")

    SetScenarioFlags(0x76, 1)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_DEF")

    label("loc_DDF")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DEC")

    OP_B7(0x0)
    Return()

    label("loc_DEF")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x90, 1)"), scpexpr(EXPR_END)), "loc_E47")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_EAA")

    label("loc_E47")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x90),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EAA")

    Jump("loc_EF8")

    label("loc_EAF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Getting Over It with Lloyd Bannings & Co.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EF8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CF0 end

    def Function_7_F04(): pass

    label("Function_7_F04")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control panel.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")
    Fade(500)
    SetChrPos(0x0, -14290, 500, 11950, 0)
    SetChrPos(0x1, -13300, 500, 10400, 0)
    SetChrPos(0x2, -14700, 500, 10400, 0)
    SetChrPos(0x3, -14170, 500, 9040, 0)
    OP_68(-14130, 1000, 11990, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 9)

    label("loc_FDB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_F04 end

    def Function_8_FE3(): pass

    label("Function_8_FE3")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a lift control panel.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BA")
    Fade(500)
    SetChrPos(0x0, -6280, 500, -8440, 89)
    SetChrPos(0x1, -8000, 500, -7280, 89)
    SetChrPos(0x2, -8000, 500, -8730, 89)
    SetChrPos(0x3, -9640, 500, -8320, 89)
    OP_68(-6670, 1000, -8280, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Call(0, 9)

    label("loc_10BA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_FE3 end

    def Function_9_10C2(): pass

    label("Function_9_10C2")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD5, 2)), scpexpr(EXPR_END)), "loc_11D7")
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14240, 750, 16100, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x3, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-12930, 1000, -14980, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x4, 0x2D, 0x0, 0x0, 0x0)
    OP_79(0x4)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    ClearScenarioFlags(0xD5, 2)
    Jump("loc_12DB")

    label("loc_11D7")

    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-14240, 750, 16100, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x3, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x3)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    OP_68(-12930, 1000, -14980, 0)
    MoveCamera(45, 49, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sound(147, 0, 100, 0)
    OP_71(0x4, 0x0, 0x2D, 0x0, 0x0)
    OP_79(0x4)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetScenarioFlags(0xD5, 2)

    label("loc_12DB")

    Return()

    # Function_9_10C2 end

    def Function_10_12DC(): pass

    label("Function_10_12DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    OP_68(-12000, 1000, 2500, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(40500, 0)
    SetChrPos(0x101, -3700, 30, 700, 270)
    SetChrPos(0x102, -2000, 0, 0, 270)
    SetChrPos(0x103, -1800, 0, -1100, 270)
    SetChrPos(0x104, -2200, 0, 1100, 270)
    SetChrPos(0x10A, -3500, 20, -700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 0, 15500, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -2000, 0, 15500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -2000, 0, 15500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-17000, 500, 2500, 8000)
    MoveCamera(30, 7, 0, 8000)
    SetCameraDistance(34500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-6000, 1000, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_68(-3000, 1000, 0, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        (
            "#4300264V#0101F#11PThis place seems to be...a warehouse\x01",
            "to smuggle goods?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300265V#11P#0603FThere's no mistaking it.\x02\x03",
            "#4300266V#0610FDamn it, if only we had a search warrant.\x01",
            "We'd search every nook and cranny of this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300267V#11P#0008FI wish so, too.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x104,
        "#4300268V#12P#0301FHold on a sec, we ain't alone here!\x02",
    )

    CloseMessageWindow()

    def lambda_15FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_15FF)
    Sleep(50)

    def lambda_160F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_160F)
    Sleep(50)

    def lambda_161F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_161F)
    Sleep(50)
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x103,
        "#4300269V#0205F#12PThose are?\x02",
    )

    CloseMessageWindow()
    OP_68(-2400, 700, 3000, 2500)
    MoveCamera(35, 20, 0, 2500)
    SetCameraDistance(20500, 2500)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x8, 3, 0, 11)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0x9, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_16C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_16C0)

    def lambda_16D1():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16D1)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4300270V#6P#0005FM-Monsters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300271V#0607F#12PTch... Take them out!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19000, 300)

    def lambda_17A0():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17A0)

    def lambda_17BA():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17BA)

    def lambda_17D4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17D4)
    Sleep(300)
    Battle("BattleInfo_3D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    Call(0, 13)
    Return()

    # Function_10_12DC end

    def Function_11_1816(): pass

    label("Function_11_1816")


    def lambda_181B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_181B)

    def lambda_182C():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x2134, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_182C)
    WaitChrThread(0xFE, 1)

    def lambda_184A():
        OP_96(0xFE, 0xFFFFF2B8, 0x0, 0x1194, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1816 end

    def Function_12_1864(): pass

    label("Function_12_1864")


    def lambda_1869():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1869)

    def lambda_187A():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x2134, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_187A)
    WaitChrThread(0xFE, 1)

    def lambda_1898():
        OP_96(0xFE, 0xFFFFED40, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1898)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_1864 end

    def Function_13_18B2(): pass

    label("Function_13_18B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    OP_68(-1650, 700, 2590, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20850, 0)
    SetChrPos(0x101, -3700, 30, 700, 0)
    SetChrPos(0x102, -2000, 0, 0, 0)
    SetChrPos(0x103, -1800, 0, -1100, 0)
    SetChrPos(0x104, -2200, 0, 1100, 0)
    SetChrPos(0x10A, -3500, 20, -700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_E0(0x1)
    OP_68(-1650, 700, 1590, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4300272V#6P#0005FWh-What are monsters doing in\x01",
            "a place like this?!\x02\x03",
            "#4300273V#0001FAre those things even native to Crossbell?\x01",
            "I've never seen them before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300274V#0108F#11PThey remind me of Flying Felines, but\x01",
            "those are only native to Liberl.\x02\x03",
            "#4300275V#0101FI don't recall them ever being\x01",
            "that strong, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300276V#12P#0603FWe can only assume that smuggling monsters\x01",
            "is one of their business practices.\x02\x03",
            "#4300277V#0601FSeems like they were hiding them in\x01",
            "here, along with those mutts.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C13():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C13)
    Sleep(50)

    def lambda_1C23():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C23)
    Sleep(50)

    def lambda_1C33():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C33)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    ChrTalk(
        0x101,
        (
            "#4300278V#5P#0011FSmuggling monsters...?\x01",
            "Is there that high of a demand for them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300279V#12P#0606FThey're likely targeting eccentric millionaires\x01",
            "who enjoy that kind of thing.\x02\x03",
            "#4300280V#0601FIt goes without saying that smuggling monsters\x01",
            "is illegal in most countries, for good reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300281V#5P#0306FBoy, what a shocker.\x02\x03",
            "#4300282V#0301FHeads-up, Lloyd. I can feel the presence of\x01",
            "some more critters roamin' around the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300283V#0211F#11PWhatever the case may be, I advise\x01",
            "we proceed with caution for now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    OP_68(-2500, 500, 0, 0)
    MoveCamera(45, 36, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -2500, 0, 0, 270)
    SetChrPos(0x1, -2500, 0, 0, 270)
    SetChrPos(0x2, -2500, 0, 0, 270)
    SetChrPos(0x3, -2500, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 7)
    OP_29(0x4C, 0x1, 0x11)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_18B2 end

    SaveToFile()

Try(main)
