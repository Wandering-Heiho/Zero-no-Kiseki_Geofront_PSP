from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t163b.bin",                # FileName
        "t163b",                    # MapName
        "t163b",                    # Location
        0x0056,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 86, 0, 0, 0, 1],
    )

    BuildStringList((
        "t163b",                  # 0
        "Doctor Gailey",          # 1
        "Chief Ursuline",         # 2
        "Doctor Lago",            # 3
        "bt162b",                 # 4
        "bt162b",                 # 5
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A4", 3,   14,  4,   4,   12,  12,  12)
    Sepith("Sepith_B4", 13,  13,  24,  10,  0,   0,   0)

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

    # monster count: 5

    BattleInfo(
        "BattleInfo_124", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_A4", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1EC", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_B4", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch67550.itc",               # 10
        "monster/ch67551.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(110030,  -1160,   0,       0x1010000,    "BattleInfo_124", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-6640,   34720,   0,       0x1010000,    "BattleInfo_1EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-63640,  51560,   0,       0x1010000,    "BattleInfo_124", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-72820,  59500,   0,       0x1010000,    "BattleInfo_1EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-54530,  42350,   0,       0x1010000,    "BattleInfo_124", 0,   18,  0xFFFF, 2,  3)

    DeclActor(110480,  0,       5410,    1200,    110480,  1000,    5410,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_47C",          # 00, 0
        "Function_1_497",          # 01, 1
        "Function_2_74B",          # 02, 2
        "Function_3_7E7",          # 03, 3
        "Function_4_92D",          # 04, 4
        "Function_5_C0A",          # 05, 5
        "Function_6_1955",         # 06, 6
        "Function_7_1999",         # 07, 7
        "Function_8_19DD",         # 08, 8
        "Function_9_1A21",         # 09, 9
        "Function_10_1A7F",        # 0A, 10
        "Function_11_1AE0",        # 0B, 11
    ))


    def Function_0_47C(): pass

    label("Function_0_47C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_496")
    Event(0, 5)

    label("loc_496")

    Return()

    # Function_0_47C end

    def Function_1_497(): pass

    label("Function_1_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_4EC")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4EC")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_509")
    OP_1B(0x3, 0x0, 0x4)

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_520")
    OP_1B(0x3, 0x0, 0xB)

    label("loc_520")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743")
    OP_70(0x5, 0x0)
    Jump("loc_747")

    label("loc_743")

    OP_70(0x5, 0x1E)

    label("loc_747")

    Call(0, 2)
    Return()

    # Function_1_497 end

    def Function_2_74B(): pass

    label("Function_2_74B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_769")
    SetChrFlags(0xB, 0x8)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_774")

    label("loc_769")

    ClearChrFlags(0xB, 0x8)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_774")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A7")
    SetChrFlags(0xC, 0x8)
    Jump("loc_7AC")

    label("loc_7A7")

    ClearChrFlags(0xC, 0x8)

    label("loc_7AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    Jump("loc_7E6")

    label("loc_7D7")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)

    label("loc_7E6")

    Return()

    # Function_2_74B end

    def Function_3_7E7(): pass

    label("Function_3_7E7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D1")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_867")
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
    SetScenarioFlags(0x10F, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_8CC")

    label("loc_867")

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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8CC")

    Jump("loc_921")

    label("loc_8D1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I have a sinking feeling in my chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_921")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7E7 end

    def Function_4_92D(): pass

    label("Function_4_92D")

    EventBegin(0x0)
    Fade(1000)
    OP_E0(0x1)
    OP_68(44510, 900, 18470, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22760, 0)
    OP_68(46010, 900, 18470, 2500)
    SetChrPos(0x101, 42280, 0, 18600, 270)
    SetChrPos(0x102, 42280, 0, 17300, 270)
    SetChrPos(0x103, 43580, 0, 17300, 270)
    SetChrPos(0x104, 43580, 0, 18600, 270)
    SetChrPos(0x106, 44880, 0, 17950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_6F(0x1)
    OP_0D()
    SetMessageWindowPos(230, 40, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#5100736V#1SIf that's the case...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 30, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#5100737V#1SHey...they're coming...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_AD9():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD9)

    def lambda_AE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AE6)
    Sleep(100)

    def lambda_AF6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF6)

    def lambda_B03():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B03)
    Sleep(100)

    def lambda_B13():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B13)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0x103,
        "#5100738V#0201F#6PIt is coming from that room...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100739V#0301F#6PIt might be our missin' doctors,\x01",
            "but then again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100740V#0013F#6PWe have to check it out.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 43500, 0, 17800, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_1B(0x3, 0x0, 0xB)
    SetScenarioFlags(0xE3, 1)
    OP_E0(0x1)
    EventEnd(0x5)
    Return()

    # Function_4_92D end

    def Function_5_C0A(): pass

    label("Function_5_C0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch32700.itc", 0x1E)
    LoadChrToIndex("chr/ch32900.itc", 0x1F)
    LoadChrToIndex("chr/ch29200.itc", 0x20)
    LoadEffect(0x0, "event\\ev604_00.eff")
    OP_68(49400, 1200, 53960, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 49400, 0, 49000, 0)
    SetChrPos(0x102, 50600, 0, 49000, 0)
    SetChrPos(0x103, 49400, 0, 47800, 0)
    SetChrPos(0x104, 50600, 0, 47800, 0)
    SetChrPos(0x106, 50000, 0, 46600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 47600, 0, 57000, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 50000, 0, 57000, 180)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 48800, 0, 57000, 180)
    FadeToBright(1000, 0)
    OP_68(49400, 1200, 54960, 2500)

    def lambda_D8B():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8B)
    Sleep(50)

    def lambda_DA3():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA3)
    Sleep(50)

    def lambda_DBB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DBB)
    Sleep(50)

    def lambda_DD3():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DD3)
    Sleep(50)

    def lambda_DEB():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DEB)
    Sleep(200)

    def lambda_E03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E03)
    Sleep(50)

    def lambda_E17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E17)
    Sleep(500)

    def lambda_E2B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E2B)
    Sleep(50)

    def lambda_E3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E3F)
    Sleep(500)

    def lambda_E53():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_E53)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()

    NpcTalk(
        0x9,
        "Woman's Voice",
        "#5100741V#5P#2SH-Here they come!\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 55460, 1000)
    OP_6F(0x1)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#5100742V#5PEat this!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Old Man's Voice",
        "#5100743V#5PGo to hell, you monsters!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5100744V#0005F#11PHuh?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 9)
    BeginChrThread(0xA, 3, 0, 10)
    OP_68(49400, 1200, 54460, 2000)
    Sleep(1500)
    Sound(949, 0, 100, 0)

    def lambda_FFC():
        OP_9D(0xFE, 0xBEF0, 0x0, 0xCF12, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FFC)

    def lambda_1019():
        OP_9D(0xFE, 0xC878, 0x0, 0xCF58, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1019)

    def lambda_1036():
        OP_9D(0xFE, 0xBE32, 0x32, 0xC8DC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1036)

    def lambda_1053():
        OP_9D(0xFE, 0xC88C, 0x32, 0xC832, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1053)

    def lambda_1070():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1070)

    def lambda_108A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_108A)

    def lambda_1097():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1097)

    def lambda_10A4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10A4)

    def lambda_10B1():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10B1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        "#5100745V#0305F#11PWhoa, chill!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100746V#0101F#11PThat was close.\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 54960, 1500)

    def lambda_1146():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1146)

    def lambda_1153():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1153)
    Sleep(100)

    def lambda_1163():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1163)

    def lambda_1170():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1170)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0x8, 500)

    NpcTalk(
        0xA,
        "Old Man's Voice",
        "#5100747V#11PIdiot! Why'd you throw that?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Old Man's Voice",
        (
            "#5100748V#11PHonestly, this is why surgeons are\x01",
            "all incompetent fools!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0xA, 500)

    NpcTalk(
        0x8,
        "Man's Voice",
        (
            "#5100749V#1PWeren't you the one telling me\x01",
            "to throw it?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man's Voice",
        (
            "#5100750V#1PThis is why physicians are useless!\x01",
            "They're all talk, no action!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    NpcTalk(
        0x9,
        "Woman's Voice",
        "#5100751V#11PExcuse me, doctors...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Woman's Voice",
        (
            "#5100752V#11PThey don't look like any kind\x01",
            "of monster I've seen before.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_13D3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13D3)

    def lambda_13E0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13E0)
    Sleep(100)

    def lambda_13F0():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13F0)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Sleep(1000)
    OP_68(48480, 1200, 54180, 3500)

    def lambda_141D():

        label("loc_141D")

        TurnDirection(0x101, 0xA, 500)
        Yield()
        Jump("loc_141D")

    QueueWorkItem2(0x101, 1, lambda_141D)

    def lambda_142F():

        label("loc_142F")

        TurnDirection(0x102, 0xA, 500)
        Yield()
        Jump("loc_142F")

    QueueWorkItem2(0x102, 1, lambda_142F)

    def lambda_1441():

        label("loc_1441")

        TurnDirection(0x103, 0xA, 500)
        Yield()
        Jump("loc_1441")

    QueueWorkItem2(0x103, 1, lambda_1441)

    def lambda_1453():

        label("loc_1453")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_1453")

    QueueWorkItem2(0x104, 1, lambda_1453)

    def lambda_1465():

        label("loc_1465")

        TurnDirection(0x106, 0xA, 500)
        Yield()
        Jump("loc_1465")

    QueueWorkItem2(0x106, 1, lambda_1465)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 6)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x106, 0x1)
    OP_6F(0x1)

    ChrTalk(
        0xA,
        "#5100753V#5PYou guys...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5100754V#5PYou're from the CPD, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100755V#0012F#11PYes, we're the Special Support Section.\x01",
            "You all look fine, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100756V#0300F#11PLast thing I was expectin' when we\x01",
            "barged in here was a chemical attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100757V#0211F#11PIs this some sort of acid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100758V#5PS-Sorry about that. It was one of our\x01",
            "experimental oxidizing agents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5100759V#5PIt has a strong kick, but it's not toxic.\x01",
            "No need to worry on that front.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#5100760V#5PUnbelievable, you two. Try to not\x01",
            "be so hasty in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_172B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_172B)
    Sleep(50)

    def lambda_173B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_173B)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#5100761V#6PWait a minute...weren't you the one\x01",
            "who said, 'They're coming!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5100762V#12PAnd weren't you the one who found the\x01",
            "oxidizing agent in the first place...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5100763V#5PO-Oh. Is that right?\x02",
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
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#5100764V#0001F#11PA-Anyway, there are still monsters\x01",
            "wandering around in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100765V#0100F#11PIf you all are ready, we're going to\x01",
            "escort you outside.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C0A end

    def Function_6_1955(): pass

    label("Function_6_1955")


    def lambda_195A():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_195A)
    WaitChrThread(0xFE, 1)

    def lambda_1978():
        OP_95(0xFE, 45910, 0, 54880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1978)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_6_1955 end

    def Function_7_1999(): pass

    label("Function_7_1999")


    def lambda_199E():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_199E)
    WaitChrThread(0xFE, 1)

    def lambda_19BC():
        OP_95(0xFE, 44750, 0, 55520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19BC)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_7_1999 end

    def Function_8_19DD(): pass

    label("Function_8_19DD")


    def lambda_19E2():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19E2)
    WaitChrThread(0xFE, 1)

    def lambda_1A00():
        OP_95(0xFE, 45790, 0, 56050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A00)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_19DD end

    def Function_9_1A21(): pass

    label("Function_9_1A21")


    def lambda_1A26():
        OP_9D(0xFE, 0xB9F0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A26)
    Sleep(150)
    Sound(814, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 330, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_9_1A21 end

    def Function_10_1A7F(): pass

    label("Function_10_1A7F")

    Sleep(100)

    def lambda_1A87():
        OP_9D(0xFE, 0xBEA0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A87)
    Sleep(150)
    Sound(541, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 345, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_1A7F end

    def Function_11_1AE0(): pass

    label("Function_11_1AE0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FI'm curious about those voices\x01",
            "we heard earlier. For now, let's\x01",
            "see if we can't locate them.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 41500, 0, 18000, 90)
    EventEnd(0x4)
    Return()

    # Function_11_1AE0 end

    SaveToFile()

Try(main)
