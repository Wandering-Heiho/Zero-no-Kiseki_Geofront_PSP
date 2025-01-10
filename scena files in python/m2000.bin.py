from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2000.bin",                # FileName
        "M2000",                    # MapName
        "M2000",                    # Location
        0x0077,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 119, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2000",                  # 0
        "Event Monster",          # 1
        "Event Monster",          # 2
        "Event Monster",          # 3
        "bm2000",                 # 4
        "bm2000",                 # 5
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_B4", 0,   0,   22,  0,   14,  14,  0)

    MonsterBattlePostion("MonsterBattlePostion_C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_EC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_F0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_F4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_F8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_FC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_124", 0x0000, 30, 6, 45, 6, 1, 30, 0, "bm2000", "Sepith_B4", 40, 30, 20, 10,
        (
            ("ms73400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1EC", 0x0002, 30, 6, 45, 0, 1, 0, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7401", "ed7403", "ATBonus_A4"),
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
        "monster/ch73450.itc",               # 10
        "monster/ch73450.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(112650,  -360,    0,       0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(111370,  -16710,  0,       0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(110950,  10260,   0,       0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)

    DeclActor(113500,  9630,    8130,    1200,    113500,  10630,   8130,    0x007C, 0,  4,  0x0000)
    DeclActor(113500,  9650,    -8160,   1200,    113500,  10650,   -8160,   0x007C, 0,  5,  0x0000)
    DeclActor(34000,   0,       4000,    1200,    34000,   1500,    4000,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 1

    ScpFunction((
        "Function_0_3F4",          # 00, 0
        "Function_1_447",          # 01, 1
        "Function_2_9CF",          # 02, 2
        "Function_3_A2E",          # 03, 3
        "Function_4_B2E",          # 04, 4
        "Function_5_D1A",          # 05, 5
        "Function_6_F03",          # 06, 6
        "Function_7_1804",         # 07, 7
        "Function_8_181C",         # 08, 8
        "Function_9_1841",         # 09, 9
        "Function_10_189A",        # 0A, 10
        "Function_11_2036",        # 0B, 11
        "Function_12_2B9E",        # 0C, 12
        "Function_13_2BCB",        # 0D, 13
        "Function_14_2C0C",        # 0E, 14
        "Function_15_2C61",        # 0F, 15
        "Function_16_2CD1",        # 10, 16
    ))


    def Function_0_3F4(): pass

    label("Function_0_3F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_418")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_437")

    label("loc_418")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_437")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_446")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_446")

    Return()

    # Function_0_3F4 end

    def Function_1_447(): pass

    label("Function_1_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_459")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_468")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4CE")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)
    Jump("loc_4DC")

    label("loc_4CE")

    SetMapObjFrame(0xFF, "glow02", 0x0, 0x1)

    label("loc_4DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_503")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_503")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 120500, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 115000, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 132500, 9000, 5000, 2000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 132500, 9000, -5000, 2000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 0)), scpexpr(EXPR_END)), "loc_5B6")
    SetMapObjFrame(0x6, "root", 0x2, "on")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    SetMapObjFrame(0x9, "root", 0x2, "on")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jump("loc_5EA")

    label("loc_5B6")

    SetMapObjFrame(0x6, "root", 0x2, "off")
    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_5EA")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 120500, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 115000, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 136950, 9000, 2160, 3000, 2000, 150000)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 136950, 9000, -2160, 3000, 2000, 30000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_END)), "loc_69D")
    SetMapObjFrame(0x7, "root", 0x2, "on")
    SetMapObjFrame(0x5, "root", 0x2, "on")
    SetMapObjFrame(0xA, "root", 0x2, "on")
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jump("loc_6D1")

    label("loc_69D")

    SetMapObjFrame(0x7, "root", 0x2, "off")
    SetMapObjFrame(0x5, "root", 0x2, "off")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)

    label("loc_6D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_706")
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_706")

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
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1D, 0x0, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x1, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x2, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CB")
    Sound(129, 1, 100, 0)

    label("loc_9CB")

    Call(0, 2)
    Return()

    # Function_1_447 end

    def Function_2_9CF(): pass

    label("Function_2_9CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1E")
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    Jump("loc_A2D")

    label("loc_A1E")

    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)

    label("loc_A2D")

    Return()

    # Function_2_9CF end

    def Function_3_A2E(): pass

    label("Function_3_A2E")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B11")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xB, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0xB, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_B11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_B2D")

    Return()

    # Function_3_A2E end

    def Function_4_B2E(): pass

    label("Function_4_B2E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 0)), scpexpr(EXPR_END)), "loc_B7F")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already been activated.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_D19")

    label("loc_B7F")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch here.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    Fade(500)
    SetChrPos(0x0, 113260, 9000, 9260, 180)
    SetChrPos(0x1, 110400, 9000, 9300, 90)
    SetChrPos(0x2, 108400, 9000, 9300, 90)
    SetChrPos(0x3, 106400, 9000, 9300, 90)
    OP_68(113920, 11500, 9260, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetMapObjFrame(0x6, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x9, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetScenarioFlags(0xD4, 0)

    label("loc_D12")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_D19")

    Return()

    # Function_4_B2E end

    def Function_5_D1A(): pass

    label("Function_5_D1A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 1)), scpexpr(EXPR_END)), "loc_D6B")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The switch has already been activated.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_F02")

    label("loc_D6B")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a switch here.\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFB")
    Fade(500)
    SetChrPos(0x0, 113660, 9000, -9380, 0)
    SetChrPos(0x1, 110400, 9000, -10100, 90)
    SetChrPos(0x2, 108400, 9000, -10100, 90)
    SetChrPos(0x3, 106400, 9000, -10100, 90)
    OP_68(114150, 11500, -10180, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sound(141, 0, 100, 0)
    SetMapObjFrame(0x7, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0xA, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x5, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetScenarioFlags(0xD4, 1)

    label("loc_EFB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_F02")

    Return()

    # Function_5_D1A end

    def Function_6_F03(): pass

    label("Function_6_F03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    LoadChrToIndex("monster/ch73450.itc", 0x23)
    LoadChrToIndex("monster/ch73450.itc", 0x24)
    LoadEffect(0x0, "event\\ev602_00.eff")
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x8, 112860, 2500, -230, 270)
    SetChrPos(0x9, 114450, 2500, 920, 270)
    SetChrPos(0xA, 114450, 2500, -1260, 270)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 7)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xA, 0, 0, 7)
    SetChrPos(0x101, 103040, 0, 300, 135)
    SetChrPos(0x102, 100740, 0, -250, 135)
    SetChrPos(0x103, 102170, 0, 1300, 135)
    SetChrPos(0x104, 102270, 0, -760, 135)
    SetChrPos(0x109, 99960, 0, 360, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(115890, 11300, 1670, 0)
    MoveCamera(65, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30100, 0)
    OP_68(115890, 1100, 1670, 12000)
    Sleep(8000)

    def lambda_109B():
        OP_95(0xFE, 107910, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_109B)

    def lambda_10B5():
        OP_95(0xFE, 105330, 0, -660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10B5)

    def lambda_10CF():
        OP_95(0xFE, 106880, 0, 820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10CF)

    def lambda_10E9():
        OP_95(0xFE, 106050, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10E9)

    def lambda_1103():
        OP_95(0xFE, 104410, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1103)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        "#4100322V#0005F#5PWhat is this place...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100323V#0101F#5PI-It seems to be a chapel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100324V#0506F#5PAccording to records, this place was\x01",
            "some kind of temple way back in the\x01",
            "Middle Ages.\x02\x03",
            "#4100325V#0501FThe Moon Temple.\x02\x03",
            "#4100326VApparently, it was built around the same\x01",
            "period as Stargazer's Tower and that old\x01",
            "fortress on the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100327V#0108F#5PSo, basically, this ruin is roughly\x01",
            "500 years old.\x02\x03",
            "#4100328V#0103FConstructed during a time\x01",
            "of chaos and war...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(100)
    Sound(935, 0, 100, 0)
    Sleep(500)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#4100329V#0505F#5PD-Do you hear that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100330V#0013F#5PA bell...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100331V#0201F#5P...!\x02\x03",
            "#4100332V#0207FLook out!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x101, 3, 0, 8)
    Sound(934, 0, 100, 0)
    OP_68(109000, 1600, 0, 0)
    OP_68(112450, 1600, 0, 4000)
    MoveCamera(90, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(27500, 0)
    OP_6F(0x79)
    Fade(1000)
    SetCameraDistance(21500, 2000)
    Sleep(300)
    Sound(868, 0, 100, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    PlayEffect(0x1D, 0xFF, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(250)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    PlayEffect(0x1D, 0xFF, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(250)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    PlayEffect(0x1D, 0xFF, 0xA, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xA, 3, 0, 9)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_68(107910, 1600, -1240, 2000)
    MoveCamera(53, 20, 0, 2000)
    SetCameraDistance(15500, 2000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
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
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4100333V#0011F#6P#N...?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sound(1182, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4100335V#0107F#6P#NGh-Gh-Ghosts?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#4100336V#0507F#6P#NThe reports were true!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#4100337V#0307F#6P#NCan't chicken out now, Mademois-Elie!\x01",
            "Here they come!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(12000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)

    def lambda_17A9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17A9)

    def lambda_17BE():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17BE)

    def lambda_17D3():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17D3)
    Sleep(500)
    Battle("BattleInfo_1EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 10)
    Return()

    # Function_6_F03 end

    def Function_7_1804(): pass

    label("Function_7_1804")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_181B")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("Function_7_1804")

    label("loc_181B")

    Return()

    # Function_7_1804 end

    def Function_8_181C(): pass

    label("Function_8_181C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1840")
    OP_82(0x46, 0x46, 0xBB8, 0x3E8)
    Sleep(1000)
    Jump("Function_8_181C")

    label("loc_1840")

    Return()

    # Function_8_181C end

    def Function_9_1841(): pass

    label("Function_9_1841")

    ClearChrFlags(0xFE, 0x1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChip(0x0, 0xFE, 0x96, 0x12C)

    def lambda_185E():
        OP_98(0xFE, 0x0, 0xFFFFF63C, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_185E)

    def lambda_1878():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1878)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x1)
    Return()

    # Function_9_1841 end

    def Function_10_189A(): pass

    label("Function_10_189A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    OP_68(109140, 1000, -40, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17850, 0)
    OP_68(107180, 1000, -140, 2500)
    SetChrPos(0x101, 107910, 0, -100, 90)
    SetChrPos(0x102, 105240, 0, -330, 90)
    SetChrPos(0x103, 107120, 0, 1380, 90)
    SetChrPos(0x104, 106840, 0, -1310, 90)
    SetChrPos(0x109, 103830, 0, 100, 90)
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
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4100338V#0006F#6PPhew, the academy never trained\x01",
            "me for ghost extermination...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#4100339V#0001F#11PElie, are you okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100340V#0106F#6PY-Yes. I think so.\x02\x03",
            "#4100341V#0107FJ-J-Just what were those things?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#4100342V#0306F#11PDefinitely looked like ghosts to me,\x01",
            "that's for sure...\x02\x03",
            "#4100343V#0308FAnd that light they gave off when\x01",
            "they vanished was damn weird.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        (
            "#4100344V#0203F#5PThe three higher elements are\x01",
            "exerting a powerful force in this area.\x02\x03",
            "#4100345V#0201FFor whatever reason, this place is also\x01",
            "brimming with spiritual energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100346V#0003F#11PSpiritual energy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100347V#0508F#6PNow that you mention it...\x02\x03",
            "#4100348VWe all heard the temple bell\x01",
            "ring just now, right?\x02\x03",
            "#4100349V#0501FIs it possible that it was rung\x01",
            "by the gho--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D18():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D18)
    TurnDirection(0x102, 0x109, 500)
    WaitChrThread(0x103, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        (
            "#4100350V#0107F#11PNoel, please stop!\x02\x03",
            "#4100351V#0109FI-It was probably just the wind!\x01",
            "Yes, that MUST have been it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100352V#0306F#11PStill stuck in the denial stage, Mademois-Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100353V#0006F#11PI understand how you feel, Elie. I do.\x02\x03",
            "#4100354V#0001FBut considering how that last fight went,\x01",
            "I say we continue our investigation.\x02\x03",
            "#4100355VSergeant Major, are you ready to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100356V#0501F#6PYes, of course!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4100357V#0106F#11P*sigh* I guess I have no choice now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100358V#0203F#5PAt least our attacks are\x01",
            "effective against them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100359V#0301F#11PGeez, it's like we're explorin' some\x01",
            "haunted mansion or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18100, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 106000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 4)
    OP_29(0x49, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_189A end

    def Function_11_2036(): pass

    label("Function_11_2036")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("apl/ch50109.itc", 0x1E)
    OP_68(103440, 11600, -2110, 0)
    MoveCamera(66, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15200, 0)
    SetChrPos(0x101, 127760, 9000, 150, 270)
    SetChrPos(0x102, 128639, 9000, 1980, 270)
    SetChrPos(0x103, 128380, 9000, -920, 270)
    SetChrPos(0x104, 128160, 9000, -2340, 270)
    SetChrPos(0x109, 129520, 9000, -3410, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(103440, 3400, -2110, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(123610, 11200, -1950, 0)
    MoveCamera(54, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16280, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#4100419V#0505F#11PWould you look at that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100420V#0102F#11PWow, the sunlight's shining through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100421V#0304F#11PMy monster radar ain't pickin'\x01",
            "up any signals, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100422V#0000F#11PYeah. Let's check out the lower floor, too.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(106000, 2500, 0, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 106000, 0, 0, 270)
    SetChrPos(0x102, 105000, 0, 0, 270)
    SetChrPos(0x103, 104000, 0, 0, 270)
    SetChrPos(0x104, 103000, 0, 0, 270)
    SetChrPos(0x109, 102000, 0, 0, 270)
    FadeToBright(1000, 0)
    OP_68(106910, 3200, 9230, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22100, 0)
    OP_68(106910, 200, 9230, 6000)
    BeginChrThread(0x101, 3, 0, 13)
    BeginChrThread(0x102, 3, 0, 15)
    BeginChrThread(0x103, 3, 0, 14)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x109, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#4100423V#0204F#6PI no longer detect the presence of time,\x01",
            "space, or mirage in the area.\x02\x03",
            "#4100424V#0202FIt appears as if the distorted space\x01",
            "is returning back to normal.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23E8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23E8)
    Sleep(50)

    def lambda_23F8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23F8)
    Sleep(50)

    def lambda_2408():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2408)
    Sleep(50)

    def lambda_2418():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2418)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        (
            "#4100425V#0004F#11PYeah...\x02\x03",
            "#4100426V#0001FBut what exactly was\x01",
            "the deal with this temple?\x02\x03",
            "#4100427VThere must have been a reason behind\x01",
            "the strange resonance of that bell, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100428V#0206F#6PUnfortunately, that is beyond my knowledge.\x02\x03",
            "#4100429V#0200FHowever, I'd say that there's an extremely\x01",
            "high possibility of that bell being an artifact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100430V#0005F#11PAn artifact?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100431V#0103F#5PArtifacts are the remnants of the ancient Zemurian\x01",
            "civilization that existed 1,200 years ago.\x02\x03",
            "#4100432V#0101FThey seem to hold powers beyond orbal technology\x01",
            "and are under the strict control of the church...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#4100433V#0303F#5PYeah, you hear stories about those suckers from\x01",
            "time to time.\x02\x03",
            "#4100434V#0301FThey're usually about some pompous rich guy\x01",
            "who secretly had a crazy powerful one. Always\x01",
            "ends with the church confiscatin' them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100435V#0008F#11PWow, this is news to me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100436V#0506F#11PFirst I've heard of it, as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100437V#0206F#6PIt is not surprising that the average\x01",
            "person is unaware of their existence.\x02\x03",
            "#4100438V#0200FAfter all, it's impossible to analyze\x01",
            "artifacts using current technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100439V#0006F#11PR-Really?\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#4100440V#0503F#11PEither way, I think we've collected\x01",
            "enough information here.\x02\x03",
            "#4100441V#0501FLet's turn in a report and leave further\x01",
            "investigations to the specialists.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29B5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29B5)
    Sleep(50)

    def lambda_29C5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29C5)
    Sleep(50)

    def lambda_29D5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29D5)
    Sleep(50)

    def lambda_29E5():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29E5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#4100442V#0000F#5PI'm with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100443V#0202F#5PWell, we did all we could.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4100444V#0300F#5PSo, time to call it a day?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100445V#0504F#11PSure.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(105730, 200, 5520, 0)
    MoveCamera(111, 18, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17860, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#4100446V#0502F#11PEveryone, thank you so much for your\x01",
            "help with the investigation!\x02\x03",
            "#4100447VWe can safely say: mission accomplished!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("r2070", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2036 end

    def Function_12_2B9E(): pass

    label("Function_12_2B9E")

    SetChrPos(0xFE, 104660, 0, 12870, 0)
    OP_95(0xFE, 102510, 0, 4220, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_12_2B9E end

    def Function_13_2BCB(): pass

    label("Function_13_2BCB")

    SetChrPos(0xFE, 106840, 0, 14160, 0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 102840, 0, 6380, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_13_2BCB end

    def Function_14_2C0C(): pass

    label("Function_14_2C0C")

    SetChrPos(0xFE, 109730, 1580, 14140, 0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 102160, 0, 7740, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_2C0C end

    def Function_15_2C61(): pass

    label("Function_15_2C61")

    SetChrPos(0xFE, 111930, 3230, 14120, 0)
    OP_95(0xFE, 109730, 1580, 14140, 2000, 0x0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 104460, 0, 8570, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Return()

    # Function_15_2C61 end

    def Function_16_2CD1(): pass

    label("Function_16_2CD1")

    SetChrPos(0xFE, 114370, 5060, 14180, 0)
    OP_95(0xFE, 111930, 3230, 14120, 2000, 0x0)
    OP_95(0xFE, 109730, 1580, 14140, 2000, 0x0)
    OP_95(0xFE, 106840, 0, 14160, 2000, 0x0)
    OP_95(0xFE, 104660, 0, 12870, 2000, 0x0)
    OP_95(0xFE, 103920, 0, 10210, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_16_2CD1 end

    SaveToFile()

Try(main)
