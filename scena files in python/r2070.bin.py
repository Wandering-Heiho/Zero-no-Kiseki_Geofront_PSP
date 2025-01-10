from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2070.bin",                # FileName
        "R2070",                    # MapName
        "R2070",                    # Location
        0x0074,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2070", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2070",                  # 0
        "SE制御",                 # 1
        "br2070",                 # 2
        "br2070",                 # 3
        "To Mainz Mountain Path", # 4
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 12,  0,   9,   1,   7,   3,   6)
    Sepith("Sepith_B4", 0,   7,   3,   12,  6,   7,   1)

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

    # monster count: 7

    BattleInfo(
        "BattleInfo_124", 0x0000, 23, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_A4", 30, 40, 20, 10,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1EC", 0x0000, 23, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms64300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64300.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64300.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64300.dat", "ms66300.dat", "ms66300.dat", "ms66300.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
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
        "monster/ch76150.itc",               # 10
        "monster/ch76150.itc",               # 11
        "monster/ch64350.itc",               # 12
        "monster/ch64350.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-27230,  5960,    0,       0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-68500,  36190,   10000,   0x1010000,    "BattleInfo_1EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-107980, 55130,   6000,    0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-111460, 28450,   2000,    0x1010000,    "BattleInfo_1EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-108740, 75420,   20000,   0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-137070, 87090,   20000,   0x1010000,    "BattleInfo_1EC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-134470, 133220,  20000,   0x1010000,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 10,  -96.0,                 175.0,                 18.75,                 1406.25,               [0.04714043438434601,  0.14142140746116638,   -0.0,                  0.0,                   -0.047140467911958694, 0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.775063514709473,    -11.172272682189941,   -3.75,                 1.0])
    DeclEvent(0x0000, 0, 8,   -136.0,                99.0,                  18.75,                 2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   13.600000381469727,    -9.90000057220459,     -3.75,                 1.0])

    DeclActor(-108720, 2000,    22560,   1200,    -108720, 3000,    22560,   0x007C, 0,  2,  0x0000)
    DeclActor(-116200, 2000,    29390,   1200,    -116200, 3000,    29390,   0x007C, 0,  3,  0x0000)
    DeclActor(-77840,  3750,    170050,  1200,    -77840,  4750,    170050,  0x007C, 0,  4,  0x0000)
    DeclActor(-99540,  7750,    191810,  1200,    -99540,  8750,    191810,  0x007C, 0,  5,  0x0000)
    DeclActor(-62380,  11750,   159630,  1200,    -62380,  12750,   159630,  0x007C, 0,  7,  0x0000)
    DeclActor(-94450,  20000,   67770,   1200,    -94450,  20000,   67770,   0x007C, 0,  6,  0x0000)
    DeclActor(-132900, 20000,   122090,  5000,    -132900, 20000,   122090,  0x007C, 0,  14, 0x0000)
    DeclActor(-108800, 2000,    28500,   1200,    -108800, 3000,    28500,   0x007C, 0,  15, 0x0000)

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "To Mainz Mountain Path")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_664",          # 00, 0
        "Function_1_685",          # 01, 1
        "Function_2_B29",          # 02, 2
        "Function_3_C8B",          # 03, 3
        "Function_4_E15",          # 04, 4
        "Function_5_F59",          # 05, 5
        "Function_6_10C8",         # 06, 6
        "Function_7_10DC",         # 07, 7
        "Function_8_1107",         # 08, 8
        "Function_9_1110",         # 09, 9
        "Function_10_1308",        # 0A, 10
        "Function_11_20CE",        # 0B, 11
        "Function_12_20DE",        # 0C, 12
        "Function_13_2881",        # 0D, 13
        "Function_14_28B5",        # 0E, 14
        "Function_15_3706",        # 0F, 15
    ))


    def Function_0_664(): pass

    label("Function_0_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675")
    Event(0, 9)

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_684")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)

    label("loc_684")

    Return()

    # Function_0_664 end

    def Function_1_685(): pass

    label("Function_1_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D7")

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D7")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F4")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_708")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_708")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_71A")
    Jump("loc_757")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_757")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_734")
    Jump("loc_757")

    label("loc_734")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_746")
    Jump("loc_757")

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_757")
    OP_66(0x6, 0x1)

    label("loc_757")

    OP_65(0x7, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77B")
    OP_66(0x7, 0x1)

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_78A")
    ClearMapObjFlags(0xD, 0x4)

    label("loc_78A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -62550, 11750, 159550, 5000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0")
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jump("loc_7C8")

    label("loc_7C0")

    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_7C8")

    SetBarrier(0x0, 0x1, 0x1, 0x0, -133980, 20000, 135680, 20000, 2000, 45000)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80E")
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_812")

    label("loc_80E")

    SetBarrier(0x2, 0x1, 0x1)

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_835")
    OP_11(0x28, 0x32, 0x1E, 0x1E, 0xC8, 0x0)
    Jump("loc_859")

    label("loc_835")

    SetMapObjFrame(0xFF, "panorama05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "panorama06", 0x0, 0x1)

    label("loc_859")

    SetMapObjFlags(0x0, 0x4)
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    OP_70(0x7, 0x0)
    Jump("loc_A86")

    label("loc_A82")

    OP_70(0x7, 0x1E)

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A99")
    OP_70(0x8, 0x0)
    Jump("loc_A9D")

    label("loc_A99")

    OP_70(0x8, 0x1E)

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB0")
    OP_70(0x9, 0x0)
    Jump("loc_AB4")

    label("loc_AB0")

    OP_70(0x9, 0x1E)

    label("loc_AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7")
    OP_70(0xA, 0x0)
    Jump("loc_ACB")

    label("loc_AC7")

    OP_70(0xA, 0x1E)

    label("loc_ACB")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 4)), scpexpr(EXPR_END)), "loc_B28")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -94450, 20000, 67770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_B28")

    Return()

    # Function_1_685 end

    def Function_2_B29(): pass

    label("Function_2_B29")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C13")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E3, 1)"), scpexpr(EXPR_END)), "loc_BA9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_C0E")

    label("loc_BA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C0E")

    Jump("loc_C7F")

    label("loc_C13")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Help! I'm careening off of a cliff!\x01",
            "I think my S-Brakes were cut!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C7F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_B29 end

    def Function_3_C8B(): pass

    label("Function_3_C8B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D75")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_D0B")
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
    SetScenarioFlags(0x105, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_D70")

    label("loc_D0B")

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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D70")

    Jump("loc_E09")

    label("loc_D75")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I had hoped that Phantom Thief B would be the one to\x01",
            "loot me. I guess I'm not beautiful enough. *whimper*\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E09")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_C8B end

    def Function_4_E15(): pass

    label("Function_4_E15")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFF")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x81, 1)"), scpexpr(EXPR_END)), "loc_E95")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_EFA")

    label("loc_E95")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EFA")

    Jump("loc_F4D")

    label("loc_EFF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Chests can't be arrested, you know.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F4D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_E15 end

    def Function_5_F59(): pass

    label("Function_5_F59")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1043")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_FD9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_103E")

    label("loc_FD9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_103E")

    Jump("loc_10BC")

    label("loc_1043")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "My parents warned me that bad chests go\x01",
            "to Gehenna where they can never speak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10BC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F59 end

    def Function_6_10C8(): pass

    label("Function_6_10C8")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_10C8 end

    def Function_7_10DC(): pass

    label("Function_7_10DC")

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

    # Function_7_10DC end

    def Function_8_1107(): pass

    label("Function_8_1107")

    SetScenarioFlags(0x87, 7)
    ModifyEventFlags(0, 1, 0x80)
    Return()

    # Function_8_1107 end

    def Function_9_1110(): pass

    label("Function_9_1110")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(2800, 600, -400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2200, 0, -1000, 270)
    SetChrPos(0x102, 2200, 0, 300, 270)
    SetChrPos(0x103, 3500, 0, -1000, 270)
    SetChrPos(0x104, 3500, 0, 300, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#1200370V#0005FI don't remember this path...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200371V#0301FHuh. This some kinda shortcut\x01",
            "to Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200372V#0101FI'm not sure... I don't see it\x01",
            "on the map.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200373V#0203FRegardless, the sound did not\x01",
            "come from this direction.\x02\x03",
            "#1200374V#0200FShould we turn back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1200375V#0003FYeah. We have to chase that echo.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x64, 7)
    EventEnd(0x5)
    NewScene("r2050", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1110 end

    def Function_10_1308(): pass

    label("Function_10_1308")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_11(0x28, 0x32, 0x1E, 0x37, 0x64, 0x0)
    OP_68(-62530, 30850, 175200, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    BeginChrThread(0x8, 1, 0, 11)
    OP_68(-83430, 30850, 189890, 12000)
    SetChrPos(0x101, -96040, 19750, 173960, 45)
    SetChrPos(0x102, -96170, 19750, 171980, 45)
    SetChrPos(0x103, -98380, 19750, 173760, 45)
    SetChrPos(0x104, -97620, 19750, 170810, 45)
    SetChrPos(0x109, -99220, 19750, 171180, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_13CA():
        OP_95(0xFE, -88160, 19750, 181910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CA)

    def lambda_13E4():
        OP_95(0xFE, -87720, 19750, 179610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13E4)

    def lambda_13FE():
        OP_95(0xFE, -89820, 19750, 181730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13FE)

    def lambda_1418():
        OP_95(0xFE, -89380, 19750, 178450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1418)

    def lambda_1432():
        OP_95(0xFE, -90830, 19750, 178970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1432)
    PlaceName2(340, 40, "c_plac29", 0x0, 6000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-88220, 22750, 181360, 0)
    MoveCamera(12, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21720, 0)
    OP_68(-88220, 20750, 181360, 3000)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_157E")

    ChrTalk(
        0x101,
        (
            "#4100288V#0006F#5PPhew... We finally made it.\x02\x03",
            "#4100289V#0005FHuh. Is it just me, or is the visibility\x01",
            "a lot worse than before...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100290V#0108F#6PIt's not just you. It wasn't foggy\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1682")

    label("loc_157E")


    ChrTalk(
        0x101,
        (
            "#4100291V#0005F#5PThis reminds me of a ruin\x01",
            "from the Middle Ages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100292V#0106F#6PWho knew something like this was tucked\x01",
            "away on the outskirts of the path?\x02\x03",
            "#4100293V#0108FTh-This fog is a little disconcerting...\x01",
            "Does anybody else feel a chill?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1682")


    ChrTalk(
        0x104,
        (
            "#4100294V#0301F#6PHeh. Guessin' this is where our friendly\x01",
            "ghosts come out to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100295V#0506F#6PI wouldn't quite call them ghosts. They're\x01",
            "more akin to mysterious monsters.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        "#4100296V#0501F#6PDo you sense something, Tio?\x02",
    )

    CloseMessageWindow()

    def lambda_1782():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1782)
    Sleep(50)

    def lambda_1792():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1792)
    Sleep(50)

    def lambda_17A2():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17A2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x103,
        "#4100297V#0205F#5P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#4100298V#0203F#5PI detect a strange fluctuation in\x01",
            "the atmosphere.\x02\x03",
            "#4100299V#0208FIs it simply oscillations in the air?\x01",
            "Or is it an incorporeal presence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100300V#0505F#6POscillations? Incorporeal...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_1965")

    ChrTalk(
        0x103,
        (
            "#4100301V#0206F#5PYes, but I did not sense it the first\x01",
            "time we came here.\x02\x03",
            "#4100302V#0201FI believe it is coming from the roof\x01",
            "where the bell is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D5")

    label("loc_1965")


    ChrTalk(
        0x103,
        (
            "#4100303V#0201F#5PThat is my hypothesis, at least.\x01",
            "I believe it is coming from the roof\x01",
            "where the bell is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D5")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1A25():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A25)
    Sleep(50)

    def lambda_1A35():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A35)
    Sleep(50)

    def lambda_1A45():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A45)
    Sleep(50)

    def lambda_1A55():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A55)
    Sleep(300)
    Fade(1000)
    Sound(866, 0, 100, 0)
    OP_68(-65349, 29450, 204690, 0)
    OP_68(-65349, 33950, 204690, 4000)
    MoveCamera(45, -8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(57870, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#4100304V#0105F#11PThat reminds me...\x02\x03",
            "#4100305V#0101FStargazer's Tower also had a bell\x01",
            "on its roof, much like these ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100306V#0013F#5PYeah, looks that way.\x02\x03",
            "#4100307VIt reminds me of the bell in Crossbell's\x01",
            "Central Square, actually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100308V#0301F#11PYou think there's some kinda connection\x01",
            "between all these bells?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4100309V#0501F#5P...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-88220, 20750, 181360, 0)
    MoveCamera(12, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21720, 0)
    OP_0D()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#4100310V#0503F#6PWell, our objective is to conduct a\x01",
            "search of the ruins' interior.\x02\x03",
            "#4100311V#0501FShould we set the bell as our target?\x02\x03",
            "#4100312VI'd like to investigate the fluctuations\x01",
            "Tio detected, if possible.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D50():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D50)
    Sleep(50)

    def lambda_1D60():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D60)
    Sleep(50)

    def lambda_1D70():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D70)
    Sleep(50)

    def lambda_1D80():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D80)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#4100313V#0004F#11PNo objections here.\x02\x03",
            "#4100314V#0000FNow that we've got a plan,\x01",
            "let's head inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4100315V#0106F#11P*sigh* If we have to...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100316V#0202F#5PCommence mission.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100317V#0304F#12PHaha. Can't say I've ever had to\x01",
            "bust some ghosts before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#4100318V#0112F#11PH-Hey! They're 'mysterious monsters,'\x01",
            "not ghosts!\x02\x03",
            "#4100319V#0109FIsn't that right, Sergeant Major?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1FA7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FA7)
    Sleep(50)

    def lambda_1FB7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FB7)
    Sleep(50)

    def lambda_1FC7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FC7)
    Sleep(50)

    def lambda_1FD7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FD7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x109,
        "#4100320V#0509F#6PY-Yeah, they're only monsters...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100321V#0012F#5P(You don't have to force yourself if\x01",
            "you're that scared, Elie...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -95800, 19750, 175000, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC0, 3)
    OP_29(0x49, 0x1, 0x1)
    OP_11(0x28, 0x32, 0x1E, 0x1E, 0xC8, 0x0)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1308 end

    def Function_11_20CE(): pass

    label("Function_11_20CE")

    Sound(866, 0, 100, 0)
    Sleep(3500)
    Sound(933, 0, 100, 0)
    Return()

    # Function_11_20CE end

    def Function_12_20DE(): pass

    label("Function_12_20DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-62740, 30450, 191600, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    SetChrPos(0x101, -77900, 19750, 191710, 225)
    SetChrPos(0x102, -76730, 19750, 191680, 225)
    SetChrPos(0x103, -76660, 19750, 195030, 225)
    SetChrPos(0x104, -75280, 19750, 194580, 225)
    SetChrPos(0x109, -78160, 19750, 193870, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-76410, 30450, 204910, 11000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-83880, 25000, 186180, 0)
    MoveCamera(15, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34120, 0)
    OP_68(-83880, 22850, 186180, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(750)
    OP_82(0x64, 0x64, 0x1388, 0x708)
    OP_74(0x1, 0x6)
    Sound(938, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 13)
    Sleep(4500)
    Fade(500)
    OP_68(-87810, 21250, 182120, 0)
    MoveCamera(12, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20120, 0)
    SetCameraDistance(17380, 3000)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x102,
        (
            "#4100448V#0106F#11P*sigh* It's finally over...\x02\x03",
            "#4100449V#0102FFor a second there, I thought\x01",
            "we were done for.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#4100450V#0509F#5PGood work in there, everyone!\x02\x03",
            "#4100451V#0506FI still can't get over that bell,\x01",
            "though...\x02\x03",
            "#4100452V#0501FThose monsters were absurd, too...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23F9():
        TurnDirection(0xFE, 0x109, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F9)
    TurnDirection(0x102, 0x109, 500)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#4100453V#0003F#6PStargazer's Tower was mysterious, but\x01",
            "this temple was really something else.\x02\x03",
            "#4100454V#0001FLet's not forget that creepy ritual chamber\x01",
            "behind the chapel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100455V#0106F#12PI honestly find it hard to believe such\x01",
            "an ominous place was once a church.\x02\x03",
            "#4100456V#0108FWhat happened 500 years ago...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4100457V#0208F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100458V#0304F#11PWell, I say we leave that question to\x01",
            "the historians and get outta here.\x02\x03",
            "#4100459V#0300FI expected that place to be like a haunted\x01",
            "house, but damn. That was nuts.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D7")

    ChrTalk(
        0x109,
        (
            "#4100463V#0509F#5PIt really was.\x02\x03",
            "#4100461V#0502FAnyway, should we head back to where\x01",
            "we parked the car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100462V#0002F#6PSounds good to me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27CB")

    label("loc_26D7")


    ChrTalk(
        0x109,
        (
            "#4100460V#0509F#5PIt really was.\x02\x03",
            "#4100464V#0505FOh, right... The car isn't parked\x01",
            "around here.\x02\x03",
            "#4100465V#0502FI'll contact the force and have it\x01",
            "delivered to the tunnel's midpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4100466V#0002F#6PGreat. That'd be really helpful.\x02",
    )

    CloseMessageWindow()

    label("loc_27CB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_68(-95800, 21250, 175000, 0)
    MoveCamera(10, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -95800, 19750, 175000, 225)
    SetChrPos(0x1, -95800, 19750, 175000, 225)
    SetChrPos(0x2, -95800, 19750, 175000, 225)
    SetChrPos(0x3, -95800, 19750, 175000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 7)
    OP_29(0x49, 0x1, 0x5)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_20DE end

    def Function_13_2881(): pass

    label("Function_13_2881")


    def lambda_2886():
        OP_97(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2886)

    def lambda_28A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28A0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_2881 end

    def Function_14_28B5(): pass

    label("Function_14_28B5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-131760, 25590, 131440, 0)
    MoveCamera(43, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26840, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0xF, 0x80)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -133660, 20000, 121680, 0)
    SetChrPos(0x102, -133200, 20000, 123580, 0)
    SetChrPos(0x103, -134930, 20000, 123500, 0)
    SetChrPos(0x104, -135130, 20000, 125140, 0)
    OP_68(-131760, 20990, 131440, 4000)
    MoveCamera(46, 6, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#6P#0205FWhat is with these ruins? They\x01",
            "look dilapidated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FI think it's the ruins of a temple built\x01",
            "during the Middle Ages.\x02\x03",
            "#0103FWhatever the details are, the CGF\x01",
            "doesn't want anyone entering,\x01",
            "judging by the barricade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#0300FThe same as Stargazer's Tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FNo reason to go trespassing...\x01",
            "Still, it's quite the view, isn't it?\x02\x03",
            "Hmm. I bet we could take a great photo\x01",
            "of this area for Grace's article.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_331A")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#12P#0000FDo you mind taking a few photos\x01",
            "for us, Elie?\x02",
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
            "#6P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
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
        "#6P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FC-Calm down, everyone. We should\x01",
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
    OP_93(0x102, 0x0, 0x1F4)
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x103, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
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
            "#12P#0000FHey, it looks like you pulled through.\x02\x03",
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
            "#6P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3698")

    label("loc_331A")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#12P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x0, 0x1F4)
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x103, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_34B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_34CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_34E1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_34F8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_34F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_350F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_350F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_3526")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3526")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_353D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_353D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3554")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3554")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_356B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_356B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3639")

    ChrTalk(
        0x101,
        (
            "#12P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3698")

    label("loc_3639")


    ChrTalk(
        0x101,
        (
            "#12P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3698")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-132900, 23500, 122090, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_69(0x1, 0x0)
    SetChrPos(0x0, -132900, 20000, 122090, 45)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x9)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x6, 0x1)
    EventEnd(0x5)
    Return()

    # Function_14_28B5 end

    def Function_15_3706(): pass

    label("Function_15_3706")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0xC, 0x80)
    OP_68(-107910, 2600, 29060, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18900, 0)
    SetChrPos(0x101, -110330, 2000, 28710, 90)
    SetChrPos(0x102, -110100, 2000, 30100, 135)
    SetChrPos(0x103, -109030, 2000, 26830, 0)
    SetChrPos(0x104, -107190, 2000, 26870, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37B6")
    SetChrPos(0x10A, -111890, 2000, 29150, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_37B6")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x34A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34A, 1)

    ChrTalk(
        0x101,
        (
            "#6P#0000FThese blue flowers are\x01",
            "requiums, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0206FThat took us ages to find.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FI know, right? Imagine how hard it\x01",
            "woulda blown if there weren't any\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FNow, now, you two. The flowers\x01",
            "were here, so it was worth it, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3954")

    ChrTalk(
        0x10A,
        "#6P#0603F(Still a complete waste of time...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_3992")

    label("loc_3954")


    ChrTalk(
        0x101,
        (
            "#0000FYeah. We got the job done,\x01",
            "and that's what counts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3992")

    OP_65(0x7, 0x1)
    OP_29(0x2E, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39BF")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_39BF")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39DF")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_39DF")

    SetChrPos(0x0, -110330, 2000, 28710, 90)
    EventEnd(0x5)
    Return()

    # Function_15_3706 end

    SaveToFile()

Try(main)
