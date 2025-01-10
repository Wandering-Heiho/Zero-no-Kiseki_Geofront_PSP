from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t150b.bin",                # FileName
        "t150b",                    # MapName
        "t150b",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 0, 0, 1],
    )

    BuildStringList((
        "t150b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Dog",                    # 5
        "Dog",                    # 6
        "Dog",                    # 7
        "Deputy Commander Baelz", # 8
        "Sergeant Major Seeker",  # 9
        "Cecile",                 # 10
        "Head Nurse Martha",      # 11
        "Guardian Force Vehicle", # 12
        "Guardian Force Vehicle", # 13
        "Guardian Force Vehicle", # 14
        "CGF Guardsman",          # 15
        "CGF Guardsman",          # 16
        "CGF Guardsman",          # 17
        "CGF Guardsman",          # 18
        "Bus Passenger",          # 19
        "Bus Passenger",          # 20
        "SE制御",                 # 21
        "bt150b",                 # 22
        "bt155b",                 # 23
        "bt160b",                 # 24
        "Ursula Road",            # 25
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 16,  7,   7,   7,   7,   7,   7)

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
    MonsterBattlePostion("MonsterBattlePostion_124", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 8, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_130", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_134", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_138", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_144", 0x0000, 34, 6, 60, 6, 1, 40, 0, "bt150b", "Sepith_B4", 50, 50, 0, 0,
        (
            ("ms67101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67101.dat", "ms67101.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_1B4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt155b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", "ms67101.dat", "ms67101.dat", 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1F8", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31103.dat", "ms31003.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
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
        "monster/ch67150.itc",               # 10
        "monster/ch67151.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-24410,  -920,    0,       0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-32990,  -21890,  -850,    0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-15590,  -21490,  -850,    0x1010000,    "BattleInfo_144", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-38000,  3000,    20500,   1500,    -38000,  4000,    20500,   0x007C, 0,  16, 0x0000)
    DeclActor(2500,    1000,    0,       1500,    3000,    1500,    0,       0x007C, 0,  4,  0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_63C",          # 00, 0
        "Function_1_6D1",          # 01, 1
        "Function_2_A3F",          # 02, 2
        "Function_3_A70",          # 03, 3
        "Function_4_A86",          # 04, 4
        "Function_5_CC4",          # 05, 5
        "Function_6_D74",          # 06, 6
        "Function_7_1B95",         # 07, 7
        "Function_8_1BB1",         # 08, 8
        "Function_9_1BD0",         # 09, 9
        "Function_10_1BEA",        # 0A, 10
        "Function_11_1C04",        # 0B, 11
        "Function_12_3607",        # 0C, 12
        "Function_13_368E",        # 0D, 13
        "Function_14_3709",        # 0E, 14
        "Function_15_3A14",        # 0F, 15
        "Function_16_3A8F",        # 10, 16
        "Function_17_3E66",        # 11, 17
        "Function_18_4339",        # 12, 18
        "Function_19_4385",        # 13, 19
        "Function_20_439F",        # 14, 20
        "Function_21_43E3",        # 15, 21
        "Function_22_4419",        # 16, 22
        "Function_23_5228",        # 17, 23
        "Function_24_5261",        # 18, 24
        "Function_25_543B",        # 19, 25
        "Function_26_54D6",        # 1A, 26
        "Function_27_5529",        # 1B, 27
    ))


    def Function_0_63C(): pass

    label("Function_0_63C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_657")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_671")

    label("loc_657")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    Event(0, 14)

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_685")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_6D0")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_699")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_6D0")

    label("loc_699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_6AD")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 17)
    Jump("loc_6D0")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_6C1")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 22)
    Jump("loc_6D0")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_6D0")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 24)

    label("loc_6D0")

    Return()

    # Function_0_63C end

    def Function_1_6D1(): pass

    label("Function_1_6D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ED")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_702")

    label("loc_6ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_702")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_702")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_71F")

    label("loc_71B")

    OP_65(0x1, 0x1)

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730")
    Call(0, 13)

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    Call(0, 15)

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_783")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_7B7")

    label("loc_783")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_7B7")

    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A34")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_A34")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_1_6D1 end

    def Function_2_A3F(): pass

    label("Function_2_A3F")

    TalkBegin(0xFE)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafioso is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_2_A3F end

    def Function_3_A70(): pass

    label("Function_3_A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A82")
    Call(0, 16)
    Jump("loc_A85")

    label("loc_A82")

    Call(0, 2)

    label("loc_A85")

    Return()

    # Function_3_A70 end

    def Function_4_A86(): pass

    label("Function_4_A86")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(2260, 2000, -290, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 1470, 1000, -200, 90)
    SetChrPos(0x102, -30, 1000, 260, 90)
    SetChrPos(0x103, 500, 1000, -1570, 90)
    SetChrPos(0x104, -680, 1000, -1150, 90)
    SetChrPos(0x106, -1710, 1000, -440, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE2")

    ChrTalk(
        0x101,
        "#5100517V#0013F#5PWe don't have time for this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100518V#0301F#1PNothin' we can do, Lloyd. We\x01",
            "can come back to it later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE6, 5)

    label("loc_BE2")

    Jump("loc_CA1")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")

    ChrTalk(
        0x101,
        "#5100519V#0000F#5P(If we use that key we found...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C2C")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use Hospital Key\x01",      # 0
            "Cancel\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C7E"),
        (1, "loc_C9C"),
        (SWITCH_DEFAULT, "loc_CA1"),
    )


    label("loc_C7E")

    Sleep(300)
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xE1, 3)
    Jump("loc_CA1")

    label("loc_C9C")

    Jump("loc_CA1")

    label("loc_CA1")

    SetChrPos(0x0, 0, 1000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_A86 end

    def Function_5_CC4(): pass

    label("Function_5_CC4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    FadeToBright(1000, 0)
    OP_68(-37070, 1800, 4550, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(39780, 0)
    OP_68(-33430, 1800, 2000, 6000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-21950, 1800, 18380, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(41350, 0)
    SetCameraDistance(39280, 4000)
    OP_6F(0x10)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t152B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_CC4 end

    def Function_6_D74(): pass

    label("Function_6_D74")

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
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("monster/ch67150.itc", 0x2C)
    LoadChrToIndex("monster/ch67151.itc", 0x2D)
    SetChrPos(0x101, -55600, 0, 100, 90)
    SetChrPos(0x102, -56570, 0, 940, 90)
    SetChrPos(0x103, -56780, 0, -1100, 90)
    SetChrPos(0x104, -57910, 0, -360, 90)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x0)
    StopBGM(0x7D0)
    WaitBGM()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KSame day, 6:50PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7303", 0)
    FadeToBright(1000, 0)
    OP_68(-12000, 2500, 450, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(37890, 0)
    OP_68(-35000, 2200, 450, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)

    def lambda_FCD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FCD)

    def lambda_FE2():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FE2)

    def lambda_FF7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FF7)

    def lambda_100C():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_100C)
    OP_68(-49500, 900, 0, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(24000, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5100354V#0108F#6PThe sun's already gone down.\x02\x03",
            "#5100355V#0101FLook there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100356V#0306F#12PThe lamps are lit up, but the\x01",
            "actual building is pitch black.\x02\x03",
            "#5100357V#0301FThat can't be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100358V#0201F#12PAlso, it is too early for the gate\x01",
            "to be closed.\x02\x03",
            "#5100359V#0208FAnd where is the guard...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100360V#0013F#6PEverything about this is shady.\x01",
            "Anyway, we need to che--\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(836, 0, 100, 0)
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
    Sleep(1000)

    def lambda_1273():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1273)

    def lambda_1280():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1280)
    Sleep(100)

    def lambda_1290():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1290)

    def lambda_129D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_129D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-55500, 1300, 0, 0)
    MoveCamera(55, 20, 0, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(20500, 1000)
    SetChrPos(0xC, -61500, 0, 0, 90)
    SetChrPos(0xD, -62500, 0, 1700, 90)
    SetChrPos(0xE, -63500, 0, -1700, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0x1C, 1, 0, 9)
    BeginChrThread(0xC, 0, 0, 7)
    Sleep(50)
    BeginChrThread(0xD, 0, 0, 7)
    Sleep(50)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_1385():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1385)

    def lambda_139A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_139A)

    def lambda_13AF():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13AF)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x1C, 0x1)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xD, 0, 0, 8)
    BeginChrThread(0xE, 0, 0, 8)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100361V#0007F#11PLook out!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    OP_68(-55000, 1300, 0, 1000)

    def lambda_1492():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1492)
    Sleep(50)

    def lambda_14AA():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14AA)
    Sleep(50)

    def lambda_14C2():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14C2)
    Sleep(50)

    def lambda_14DA():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14DA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#5100362V#0107F#11PIt's Revache's war hounds!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100363V#0307F#11PDid they conceal their presence\x01",
            "or somethin'?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x5A, 0x2BC)

    ChrTalk(
        0x103,
        "#5100364V#0207F#5POn our six, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100365V#0011F#11PWhat?!\x02",
    )

    CloseMessageWindow()
    OP_68(-49000, 1000, 0, 2000)
    MoveCamera(50, 20, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_1629():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1629)
    Sleep(50)

    def lambda_1639():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1639)
    Sleep(50)

    def lambda_1649():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1649)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sound(113, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    SetChrPos(0x8, -40000, 0, -800, 270)
    SetChrPos(0x9, -40000, 0, 800, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_16B2():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16B2)

    def lambda_16C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_16C7)
    Sleep(100)

    def lambda_16DB():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_16DB)

    def lambda_16F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_16F0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_79(0x6)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#5100366V#0007F#6PRevache!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100367V#0101F#6PHave they been here the\x01",
            "whole time?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100368V#0301F#6PWhat the hell do you guys think you're doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100369V#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5100370V#5P...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
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
        0x101,
        "#5100371V#0013F#6PWhat's wrong with them...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100372V#0103F#6PIt's no use trying to reason with them.\x02",
    )

    CloseMessageWindow()
    OP_68(-54000, 900, 0, 2000)
    OP_68(-53500, 1000, 0, 2000)
    MoveCamera(55, 20, 0, 2000)
    SetCameraDistance(19500, 2000)

    def lambda_1935():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1935)
    Sleep(50)

    def lambda_1945():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1945)
    Sleep(650)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0x1C, 1, 0, 10)
    BeginChrThread(0xC, 0, 0, 7)
    BeginChrThread(0xD, 0, 0, 7)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_1985():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1985)

    def lambda_199A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_199A)

    def lambda_19AF():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_19AF)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0x1C, 0x1)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xD, 0, 0, 8)
    BeginChrThread(0xE, 0, 0, 8)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#5100373V#0207F#6PEveryone, be on guard. I have a bad\x01",
            "feeling about this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100374V#0307F#11PThey're gettin' ready to charge!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)

    def lambda_1AA1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AA1)

    def lambda_1AB6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AB6)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0x1C, 1, 0, 10)
    BeginChrThread(0xC, 0, 0, 7)
    BeginChrThread(0xD, 0, 0, 7)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_1AFB():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1AFB)

    def lambda_1B10():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B10)

    def lambda_1B25():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B25)
    SetCameraDistance(14500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x1C, 0x1)
    Battle("BattleInfo_1B4", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    Call(0, 11)
    Return()

    # Function_6_D74 end

    def Function_7_1B95(): pass

    label("Function_7_1B95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BB0")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_7_1B95")

    label("loc_1BB0")

    Return()

    # Function_7_1B95 end

    def Function_8_1BB1(): pass

    label("Function_8_1BB1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BCF")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_1BB1")

    label("loc_1BCF")

    Return()

    # Function_8_1BB1 end

    def Function_9_1BD0(): pass

    label("Function_9_1BD0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BE9")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_9_1BD0")

    label("loc_1BE9")

    Return()

    # Function_9_1BD0 end

    def Function_10_1BEA(): pass

    label("Function_10_1BEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C03")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_10_1BEA")

    label("loc_1C03")

    Return()

    # Function_10_1BEA end

    def Function_11_1C04(): pass

    label("Function_11_1C04")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0x5, 0x0, 0x23)
    OP_32(0x5, 0x5, 0x64)
    RemoveCraft(0x5, 0xFFFF)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x5, 0x81, 0x2)
    OP_38(0x5, 0x82, 0x2)
    OP_38(0x5, 0x83, 0x2)
    OP_38(0x5, 0x84, 0x2)
    OP_38(0x5, 0x85, 0x2)
    OP_38(0x5, 0x86, 0x2)
    OP_42(0x5, 0x43D, 0xFF)
    OP_42(0x5, 0x5EC, 0xFF)
    OP_42(0x5, 0x650, 0xFF)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0x113)
    SetChrChipPat(0x5, 0x6, 0x113)
    AddCraft(0x5, 0x13B)
    OP_42(0x5, 0x69, 0x0)
    OP_42(0x5, 0x99, 0x5)
    OP_42(0x5, 0x78, 0x4)
    OP_42(0x5, 0x90, 0x3)
    OP_42(0x5, 0x87, 0x2)
    OP_42(0x5, 0x80, 0x1)
    OP_42(0x5, 0x7E, 0x6)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("chr/ch31053.itc", 0x2C)
    LoadChrToIndex("chr/ch31153.itc", 0x2D)
    OP_68(-49000, 600, 0, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -52400, 0, 10, 90)
    SetChrPos(0x102, -53490, 0, 920, 90)
    SetChrPos(0x103, -53630, 0, -1030, 90)
    SetChrPos(0x104, -54650, 0, -140, 90)
    SetChrPos(0x106, -51650, 0, 6000, 180)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -47830, 0, 810, 270)
    SetChrPos(0x9, -48930, 0, -950, 270)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev603_00.eff")
    LoadEffect(0x2, "event\\ev202_00.eff")
    FadeToBright(1000, 0)
    OP_68(-51000, 600, 0, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        "#5100375V#0110F#6PHow are they so strong?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100376V#0006F#6PThe drug must be strengthening them...\x02\x03",
            "#5100377V#0013FThe war hounds, too, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100378V#0301F#6PSure, but what the hell was\x01",
            "up with them?\x02\x03",
            "#5100379VThey didn't say a single word\x01",
            "before goin' ballistic on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100380V#0206F#6P...I could hardly sense any\x01",
            "emotion coming from them.\x02\x03",
            "#5100381V#0208FThis reminds me of--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100382V\x07\x02",
            "#60W#11P...uggghhHHHH...\x02",
        )
    )

    CloseMessageWindow()
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
    Fade(500)
    OP_68(-48150, 600, 0, 0)
    MoveCamera(90, 25, 0, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(18500, 3000)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#5100383V\x07\x02",
            "#60W#5P...aaaahhhHHHH...\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(202, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xFA0, 0x1F4)

    def lambda_219A():
        OP_A6(0xFE, 0x28, 0x28, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_219A)

    def lambda_21B3():
        OP_A6(0xFE, 0x28, 0x28, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_21B3)
    Sleep(250)
    Fade(1000)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_68(-50000, 600, 0, 1500)
    MoveCamera(90, 17, 0, 1500)
    SetCameraDistance(20150, 1500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_2283():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2283)
    Sleep(50)

    def lambda_229B():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_229B)
    Sleep(50)

    def lambda_22B3():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22B3)
    Sleep(50)

    def lambda_22CB():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22CB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5100384V#0011F#6PThey're back up?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100385V#0307F#6PThey should've been knocked out cold!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100386V#0201F#12PThis is the power of Gnosis!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100387V#0101F#6PWh-What do we do...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1627, 255, 100, 0)
    Sleep(500)
    SetMessageWindowPos(0, 40, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5100389V\x07\x03",
            "Irksome pests.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-48350, 700, 0, 0)
    MoveCamera(45, 18, 0, 0)
    MoveCamera(55, 18, 0, 2000)
    SetCameraDistance(25500, 0)
    SetCameraDistance(15500, 2000)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x140, 0, 900, 0, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(200)

    def lambda_24B0():
        OP_A6(0xFE, 0x28, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_24B0)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x1)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    Sound(502, 0, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5100390V\x07\x02",
            "#5PGuh...\x05\x02",
        )
    )

    Sleep(300)
    PlayEffect(0x1, 0xFF, 0x9, 0x140, 0, 900, 0, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(200)

    def lambda_2545():
        OP_A6(0xFE, 0x28, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2545)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x1)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    Sound(502, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#5100391V\x07\x02",
            "#2PUgh...\x05\x02",
        )
    )

    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Call(0, 13)
    Sound(514, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-51000, 600, 0, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#5100392V#0105F#5PAre those needles?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100393V#0007F#5PYin! Did you kill them?!\x02",
    )

    CloseMessageWindow()
    OP_68(-52550, 1000, 1850, 3000)
    MoveCamera(30, 18, 0, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(1000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    BeginChrThread(0x106, 3, 0, 12)
    Sleep(700)

    def lambda_26B9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B9)
    Sleep(50)

    def lambda_26C9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26C9)
    Sleep(50)

    def lambda_26D9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26D9)
    Sleep(50)

    def lambda_26E9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26E9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 3)
    OP_6F(0x79)
    Sound(1629, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x106,
        (
            "#5100394V\x07\x03",
            "No. I simply used a form of acupuncture to\x01",
            "cut off the flow of their chi.\x02\x03",
            "#5100395VNo matter how much strength they possess,\x01",
            "they will be asleep for quite a while.\x02",
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
        0x101,
        (
            "#5100396V\x07\x00",
            "#0006F#12PThank goodness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100397V#0306F#6PYou sure have a knack for showin' up outta\x01",
            "the damn blue.\x02\x03",
            "#5100398V#0301FDid you come to investigate Revache, too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 300)
    Sleep(150)

    ChrTalk(
        0x106,
        (
            "#5100399V\x07\x03",
            "#0702F#5PI'm here at Cao's behest.\x02\x03",
            "#5100400V#0700FBut it seems that this simple request\x01",
            "will be more vexing than I thought.\x02\x03",
            "#5100401VI always believed this Gnosis was\x01",
            "nothing more than a rumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100402V\x07\x00",
            "#0205F#12PWhere did you hear that name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100403V#0101F#6PJust how much does Heiyue know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100404V\x07\x03",
            "#0702F#5PAbout as much as you all.\x02\x03",
            "#5100405VRevache's disappearance, the existence\x01",
            "of the D∴G cult and its remnants...\x02\x03",
            "#5100406VNeither Cao nor I know anything beyond\x01",
            "those two pieces of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100407V\x07\x00",
            "#0008F#12PAll right.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5100408V#0006F#12PListen, Yin. Regardless of your intentions,\x01",
            "St. Ursula is in a state of emergency.\x02\x03",
            "#5100409VAnd odds are that the mafia is currently\x01",
            "occupying the entire hospital.\x02\x03",
            "#5100410V#0008FIt's our job to verify whether the hospital\x01",
            "staff is safe and act from there.\x02\x03",
            "#5100411V#0001FNow that you know that...will you work\x01",
            "with us, Yin?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    def lambda_2D57():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D57)
    Sleep(50)

    def lambda_2D67():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D67)
    Sleep(50)

    def lambda_2D77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D77)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#5100412V#0105F#1PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100413V#0305F#6PDude, you realize who you're talkin' to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100414V\x07\x03",
            "#0702F#5PHeh. What are you babbling about, Bannings?\x02\x03",
            "#5100415VAre you actually requesting assistance\x01",
            "from someone you've tried to arrest?\x01",
            "Someone you've labeled a criminal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100416V\x07\x00",
            "#0006F#12PLike I said. State of emergency.\x02\x03",
            "#5100417V#0000FCorrect me if I'm wrong, but I think you\x01",
            "planned to uncover the truth behind all\x01",
            "this, with or without us.\x02\x03",
            "#5100418VIf that's the case, don't you think there's\x01",
            "merit in rescuing the people in there and\x01",
            "hearing what eyewitnesses have to say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100419V\x07\x03",
            "#0702F#5PHeh. So you wish to work as equals until\x01",
            "the end of this matter, is that it?\x02\x03",
            "#5100420V#0700FVery well.\x02\x03",
            "#5100421VHowever, if you start to become a burden,\x01",
            "I will act of my own accord.\x02\x03",
            "#5100422VIs that clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100423V\x07\x00",
            "#0004F#12PThat won't be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100424V#0106F#1PGeez. I don't know whether to call\x01",
            "you impulsive or what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100425V#0211F#6PLloyd CAN be a bit too audacious\x01",
            "in the heat of the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100426V#0303F#6PHey, now's not the time for talk.\x02\x03",
            "#5100427V#0300FAin't it about time we started our\x01",
            "infiltration?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#5100428V#0003F#11PRight. Our top priority is locating\x01",
            "the hospital staff and confirming\x01",
            "their safety.\x02\x03",
            "#5100429V#0001FAnd while we're at it, we can ask\x01",
            "them about the overall situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100430V#0101F#1PUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100431V#0201F#6PRoger that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100432V\x07\x03",
            "#0702F#5PHeh. Shall we go?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")

    def lambda_3372():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3372)

    def lambda_337F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_337F)
    Sleep(100)

    def lambda_338F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_338F)

    def lambda_339C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_339C)
    Sleep(100)

    def lambda_33AC():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_33AC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Fade(1000)
    SetChrPos(0x101, -52190, 0, 160, 90)
    SetChrPos(0x102, -54770, 0, -200, 90)
    SetChrPos(0x103, -53560, 0, -810, 90)
    SetChrPos(0x104, -53990, 0, 790, 90)
    SetChrPos(0x106, -51770, 0, 2400, 90)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-49330, 2000, 0, 0)
    MoveCamera(90, 7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(22500, 2000)
    OP_6F(0x10)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7510", 0)
    ReplaceBGM("ed7123", "ed7510")

    ChrTalk(
        0x101,
        (
            "#5100433V\x07\x00",
            "#0008F#6P#N(Cecile, please be safe...)\x02\x03",
            "#5100434V#0013F(Just hold on, everyone... We'll save you!)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-49330, 3900, 0, 5000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yin has joined the party.\x07\x05\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can add her to the active party in\x01",
            "the [TACTICS] menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_37()
    SetChrPos(0x0, -53000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0xE0, 3)
    OP_29(0x4D, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_1C04 end

    def Function_12_3607(): pass

    label("Function_12_3607")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_365C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_365C)

    def lambda_3671():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3671)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_12_3607 end

    def Function_13_368E(): pass

    label("Function_13_368E")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, -47830, 0, 810, 315)
    SetChrPos(0x9, -48930, 0, -950, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_13_368E end

    def Function_14_3709(): pass

    label("Function_14_3709")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(-32180, 4200, 22060, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -34350, 3000, 21720, 270)
    SetChrPos(0x102, -33520, 3000, 20960, 270)
    SetChrPos(0x103, -33020, 3000, 22710, 270)
    SetChrPos(0x104, -31720, 3000, 22660, 270)
    SetChrPos(0x106, -31870, 3000, 21200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xA, -39000, 3000, 22500, 90)
    SetChrPos(0xB, -39000, 3000, 20500, 90)
    FadeToBright(1000, 0)
    OP_68(-35060, 4200, 21920, 1800)
    Sleep(1500)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#5100497V#0013F#11PThey're here, too?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#5100498V\x07\x03",
            "#0700F#11PLet us finish them.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(18000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)

    def lambda_3964():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3964)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)

    def lambda_3981():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3981)
    Sleep(500)
    Battle("BattleInfo_1F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    Call(0, 15)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_37()
    SetChrPos(0x0, -34500, 3000, 22500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE0, 7)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_3709 end

    def Function_15_3A14(): pass

    label("Function_15_3A14")

    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xA, -38000, 3000, 22500, 90)
    SetChrPos(0xB, -38000, 3000, 20500, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_15_3A14 end

    def Function_16_3A8F(): pass

    label("Function_16_3A8F")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(-37230, 4400, 19950, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -36530, 3000, 20520, 270)
    SetChrPos(0x102, -35450, 3000, 19960, 270)
    SetChrPos(0x103, -34940, 3000, 21590, 270)
    SetChrPos(0x104, -33840, 3000, 21430, 270)
    SetChrPos(0x106, -33890, 3000, 20130, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafiosos are unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#5100499V#0001F#11PHmm?\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is something small lying near the\x01",
            "bodies of the unconscious mafiosos...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x334, 1)

    ChrTalk(
        0x101,
        "#5100500V#0005F#11PA key?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 1)), scpexpr(EXPR_END)), "loc_3CD9")

    ChrTalk(
        0x102,
        (
            "#5100501V#0103F#11PThis must be the hospital key\x01",
            "the head nurse told us about.\x02\x03",
            "#5100502V#0100FWith this, we should be able\x01",
            "to enter the hospital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0B")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_END)), "loc_3D8B")

    ChrTalk(
        0x103,
        (
            "#5100503V#0203F#11PIt must correspond to the lock\x01",
            "on the hospital's front door.\x02\x03",
            "#5100504V#0202FWith this, we should be able to\x01",
            "begin our investigation there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0B")

    label("loc_3D8B")


    ChrTalk(
        0x104,
        (
            "#5100505V#0303F#11PMight've been snatched from\x01",
            "one of the hospital workers.\x02\x03",
            "#5100506V#0300FThink we can use it somewhere?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0B")


    ChrTalk(
        0x101,
        "#5100507V#0000F#11PYeah, let's test it out.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -35500, 3000, 21100, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xE1, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_3A8F end

    def Function_17_3E66(): pass

    label("Function_17_3E66")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("chr/ch29600.itc", 0x21)
    LoadChrToIndex("apl/ch50157.itc", 0x22)
    LoadChrToIndex("apl/ch50157.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch21000.itc", 0x26)
    LoadChrToIndex("chr/ch20300.itc", 0x27)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -23560, 0, -5040, 90)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -23900, 0, -3970, 90)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -21800, 0, -4800, 270)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -21800, 0, -3600, 270)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x5)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x2)
    SetMapObjFlags(0x16, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x16, 0x13)
    SetMapObjFlags(0x16, 0x1000)
    SetMapObjFrame(0x16, "light", 0x0, 0x1)
    SetChrPos(0x13, -50360, 0, -2950, 0)
    OP_D3(0x13, 0x0, 0x1C138, 0x0, 0x0)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    SetMapObjFlags(0x17, 0x400)
    SetChrFlags(0x14, 0x8000)
    OP_78(0x17, 0x14)
    SetMapObjFlags(0x17, 0x1000)
    SetChrPos(0x14, -47990, 0, 10910, 0)
    OP_D3(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    SetMapObjFlags(0x18, 0x400)
    SetChrFlags(0x15, 0x8000)
    OP_78(0x18, 0x15)
    SetMapObjFlags(0x18, 0x1000)
    SetChrPos(0x15, -61810, 0, 1170, 0)
    OP_D3(0x15, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x18, 0x1E)
    OP_70(0x18, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x27)
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_420E")
    OP_68(-51000, 3600, 2300, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x16, -47870, 0, 4190, 270)
    SetChrPos(0x17, -51270, 0, 9800, 180)
    SetChrPos(0x18, -52570, 0, 9800, 180)
    SetChrPos(0x19, -54240, 0, -1180, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 18)
    BeginChrThread(0x18, 3, 0, 18)
    OP_68(-51000, 1900, 2300, 6000)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)

    label("loc_420E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_432C")
    OP_68(-35000, 3500, -6110, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x16, -20930, 0, 2850, 225)
    SetChrPos(0x17, -34310, 0, 500, 90)
    SetChrPos(0x18, -35750, 0, -660, 90)
    SetChrPos(0x19, -24040, 0, 10340, 180)
    SetChrPos(0x1A, -24810, 0, 11740, 180)
    SetChrPos(0x1B, -23540, 0, 12520, 180)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 19)
    BeginChrThread(0x18, 3, 0, 19)
    BeginChrThread(0x19, 3, 0, 20)
    BeginChrThread(0x1A, 3, 0, 21)
    BeginChrThread(0x1B, 3, 0, 21)
    OP_68(-25000, 3500, -6110, 12000)
    Sleep(1500)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    Sleep(7000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)

    label("loc_432C")

    SetScenarioFlags(0x5C, 3)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3E66 end

    def Function_18_4339(): pass

    label("Function_18_4339")


    def lambda_433E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_433E)
    WaitChrThread(0xFE, 1)

    def lambda_4357():
        OP_9B(0x0, 0xFE, 0xFFC4, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4357)
    WaitChrThread(0xFE, 1)

    def lambda_4370():
        OP_9B(0x0, 0xFE, 0xFFC4, 0x2328, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4370)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_4339 end

    def Function_19_4385(): pass

    label("Function_19_4385")


    def lambda_438A():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_438A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_4385 end

    def Function_20_439F(): pass

    label("Function_20_439F")


    def lambda_43A4():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43A4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_43CE():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43CE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_439F end

    def Function_21_43E3(): pass

    label("Function_21_43E3")


    def lambda_43E8():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43E8)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_4404():
        OP_9B(0x0, 0xFE, 0x5A, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4404)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_43E3 end

    def Function_22_4419(): pass

    label("Function_22_4419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("apl/ch50109.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(-50800, 2500, 0, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20600, 0)
    SetChrPos(0x101, -51540, 0, -50, 90)
    SetChrPos(0x102, -51540, 0, 1580, 135)
    SetChrPos(0x103, -53200, 0, -830, 90)
    SetChrPos(0x104, -53140, 0, 680, 90)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -48700, 0, -1200, 270)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -52280, 0, -2180, 45)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -49400, 0, 0, 270)
    SetChrFlags(0x11, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    SetMapObjFlags(0x17, 0x400)
    SetChrFlags(0x14, 0x8000)
    OP_78(0x17, 0x14)
    SetMapObjFrame(0x17, "light", 0x0, 0x1)
    SetMapObjFlags(0x17, 0x1000)
    SetChrPos(0x14, -47990, 0, 10910, 0)
    OP_D3(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    SetMapObjFlags(0x18, 0x400)
    SetChrFlags(0x15, 0x8000)
    OP_78(0x18, 0x15)
    SetMapObjFlags(0x18, 0x1000)
    SetChrPos(0x15, -59090, 0, 1500, 0)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x18, 0x1E)
    OP_70(0x18, 0x0)
    FadeToBright(1000, 0)
    OP_68(-50800, 1000, 0, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#5101053V#1300F#11PI understand. You have to return\x01",
            "to the city, so you should.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101054V#0006F#6PI'm sorry, Cecile.\x02\x03",
            "#5101055V#0008FI would definitely stay and help fix\x01",
            "things around the hospital, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5101056V#1302F#11PDon't be silly, Lloyd.\x02\x03",
            "#5101057V#1304FThe Guardian Force has things handled\x01",
            "here. Besides, there are pressing matters\x01",
            "that only you can solve.\x02\x03",
            "#5101058V#1301FKeA's in trouble, isn't she?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101059V#0003F#6PShe is.\x02\x03",
            "#5101060V#0008FTo be quite honest, we still don't know what\x01",
            "exactly Doctor Guenter wants to accomplish.\x02\x03",
            "#5101061VI'm having a hard time figuring out how we\x01",
            "should even proceed in all this chaos...\x02\x03",
            "#5101062V#0001FBut I know one thing...\x01",
            "We have to protect KeA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5101063V#0103F#6PI couldn't agree more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5101064V#0201F#6PAbsolutely. We WILL protect her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5101065V#0300F#6PYou said it. We ain't losin' our kiddo\x01",
            "to that bastard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5101066V#1304F#11PHeehee...\x02\x03",
            "#5101067V#1302FIt's clear how much you want to\x01",
            "protect what's precious to you.\x02\x03",
            "#5101068VAs long as you never lose sight\x01",
            "of that, I'm sure you'll find the\x01",
            "answers you're looking for.\x02\x03",
            "#5101069V#1309FIf it's the Special Support Section\x01",
            "on the case, it can be solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101070V#0002F#6PCecile...thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5101071V#0109F#6PIt's very encouraging to hear\x01",
            "you say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5101072V#2004F#11PShe essentially said everything I was\x01",
            "going to say.\x02\x03",
            "#5101073V#2001FNow that the prison has been attacked,\x01",
            "the CGF is in a state of disarray...\x02\x03",
            "#5101074VBut, if we coordinate with Bellguard Gate,\x01",
            "we should be able to calm things down.\x02\x03",
            "#5101075V#2002FIt's going to be a long night, everyone.\x01",
            "Let's buckle down and get through it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101076V#0000F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5101077V#0300F#6PNo holdin' back now, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5101078V#2004F#11PSergeant Major Seeker.\x02\x03",
            "#5101079V#2002FEscort the Special Support Section back\x01",
            "to Crossbell City, ASAP.\x02\x03",
            "#5101080VI give you permission to break speed limit,\x01",
            "but don't get into an accident.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Sound(1479, 255, 100, 0)

    ChrTalk(
        0x10,
        "#5101081V#0500F#6PYes, ma'am!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(750)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x15, -59090, 0, 0, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-48880, -1500, 2620, 0)
    MoveCamera(60, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24490, 0)
    Sound(488, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(-48880, 200, 2620, 3000)
    SetCameraDistance(22490, 3000)
    OP_71(0x18, 0x79, 0xB4, 0x0, 0x20)

    def lambda_4EF3():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4EF3)
    WaitChrThread(0x15, 1)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)
    TurnDirection(0xF, 0x11, 500)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#5101082V#2004F#11PWell, then, it's time to see what needs to\x01",
            "be done around here.\x02\x03",
            "#5101083V#2002FMs. Neues, could you show me the way\x01",
            "to the research ward?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xF, 500)

    ChrTalk(
        0x11,
        "#5101084V#1300F#5PYes, of course.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(1000)
    OP_68(-47790, 200, 1230, 3000)
    SetCameraDistance(20250, 3000)
    OP_93(0x11, 0x10E, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x11,
        (
            "#5101085V#1303F#11P#30W(Everyone, please be careful...)\x02\x03",
            "#5101086V#1301F#20W(...and Guy, watch over Lloyd.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    EndChrThread(0xF, 0x3)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xA)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_29(0x4D, 0x1, 0xF)
    OP_29(0x4D, 0x4, 0x10)
    OP_29(0x4E, 0x4, 0x2)
    OP_29(0x4E, 0x1, 0x0)
    SubItemNumber(0x334, 1)
    SubItemNumber(0x335, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_513C")
    OP_29(0x29, 0x4, 0x40)
    Jump("loc_514E")

    label("loc_513C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514E")
    OP_29(0x29, 0x4, 0x40)

    label("loc_514E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x32, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5160")
    OP_29(0x32, 0x4, 0x40)

    label("loc_5160")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_517E")
    OP_29(0x34, 0x4, 0x40)
    Jump("loc_5190")

    label("loc_517E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5190")
    OP_29(0x34, 0x4, 0x40)

    label("loc_5190")

    SubItemNumber(0x2DA, 1)
    SubItemNumber(0x2D9, 1)
    SubItemNumber(0x2D8, 1)
    SubItemNumber(0x34B, 1)
    SubItemNumber(0x349, 1)
    SubItemNumber(0x34A, 1)
    SubItemNumber(0x343, 1)
    SubItemNumber(0x342, 1)
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)
    SubItemNumber(0x359, 1)
    OP_E3(0xA)
    OP_E3(0x3)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    SetScenarioFlags(0x5F, 0)
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4419 end

    def Function_23_5228(): pass

    label("Function_23_5228")

    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_5234():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5234)
    Sleep(3000)

    def lambda_524C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_524C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_5228 end

    def Function_24_5261(): pass

    label("Function_24_5261")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("monster/ch75650.itc", 0x20)
    ClearMapObjFlags(0x15, 0x4)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    OP_A7(0xC, 0x37, 0x37, 0x37, 0xFF, 0x0)
    OP_A7(0xD, 0x37, 0x37, 0x37, 0xFF, 0x0)
    OP_A7(0xE, 0x37, 0x37, 0x37, 0xFF, 0x0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, -53470, 0, 16170, 90)
    SetChrPos(0xD, -54800, 0, 17760, 90)
    SetChrPos(0xE, -55280, 0, 14310, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, -50350, 0, 17450, 270)
    SetChrPos(0x9, -50350, 0, 15980, 270)
    OP_68(-51440, 1000, 16260, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23910, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(60000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    EventEnd(0x5)
    Return()

    # Function_24_5261 end

    def Function_25_543B(): pass

    label("Function_25_543B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThis is an emergency. We don't\x01",
            "have any time to head back.\x02\x03",
            "We have to make sure everyone\x01",
            "inside the hospital is safe!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_25_543B end

    def Function_26_54D6(): pass

    label("Function_26_54D6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St. Ursula Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_54D6 end

    def Function_27_5529(): pass

    label("Function_27_5529")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St. Ursula Medical College\x01",
            "        Le Lectier Inn\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_5529 end

    SaveToFile()

Try(main)
