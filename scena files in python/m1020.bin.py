from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1020.bin",                # FileName
        "m1020",                    # MapName
        "m1020",                    # Location
        0x006C,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, -35000, 0, 0, 1, 108, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1020",                  # 0
        "Golem Soldier",          # 1
        "Golem Soldier",          # 2
        "Living Axe",             # 3
        "SE制御",                 # 4
        "bm1020",                 # 5
        "bm1020",                 # 6
        "bm1000",                 # 7
        "bm1020",                 # 8
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A4", 0,   0,   14,  5,   3,   7,   6)
    Sepith("Sepith_B4", 0,   15,  0,   6,   4,   5,   5)

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
    MonsterBattlePostion("MonsterBattlePostion_124", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_144", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_A4", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_20C", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_B4", 40, 30, 20, 10,
        (
            ("ms62800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms62800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_2D4", 0x0000, 21, 6, 45, 0, 1, 0, 0, "bm1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", "ms64600.dat", "ms62800.dat", 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_E4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_318", 0x0002, 21, 6, 45, 0, 1, 0, 0, "bm1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_124", "MonsterBattlePostion_E4", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch62850.itc",               # 12
        "monster/ch62850.itc",               # 13
        "monster/ch64650.itc",               # 14
        "monster/ch64650.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-5650,   1500,    30610,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-31440,  3550,    0,       0x1010000,    "BattleInfo_144", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-620,    25220,   0,       0x1010000,    "BattleInfo_20C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(-5650,   0,       30610,   1200,    -5650,   1000,    30610,   0x007C, 0,  3,  0x0000)
    DeclActor(-18970,  0,       -2900,   1200,    -18970,  1000,    -2900,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_52C",          # 00, 0
        "Function_1_54B",          # 01, 1
        "Function_2_571",          # 02, 2
        "Function_3_700",          # 03, 3
        "Function_4_92B",          # 04, 4
        "Function_5_AB6",          # 05, 5
        "Function_6_1C99",         # 06, 6
        "Function_7_1CB8",         # 07, 7
        "Function_8_1CD5",         # 08, 8
        "Function_9_1D27",         # 09, 9
        "Function_10_1D77",        # 0A, 10
        "Function_11_1D95",        # 0B, 11
        "Function_12_1DAF",        # 0C, 12
        "Function_13_1DC9",        # 0D, 13
    ))


    def Function_0_52C(): pass

    label("Function_0_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_52C")

    label("loc_54A")

    Return()

    # Function_0_52C end

    def Function_1_54B(): pass

    label("Function_1_54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_561")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_570")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_570")

    Return()

    # Function_1_54B end

    def Function_2_571(): pass

    label("Function_2_571")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    OP_70(0x0, 0x0)
    Jump("loc_6E8")

    label("loc_6E4")

    OP_70(0x0, 0x1E)

    label("loc_6E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FB")
    OP_70(0x1, 0x0)
    Jump("loc_6FF")

    label("loc_6FB")

    OP_70(0x1, 0x1E)

    label("loc_6FF")

    Return()

    # Function_2_571 end

    def Function_3_700(): pass

    label("Function_3_700")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BF")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_759():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_759)

    def lambda_773():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_773)
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
    Battle("BattleInfo_2D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_7E0"),
        (2, "loc_7EF"),
        (1, "loc_7FC"),
        (SWITCH_DEFAULT, "loc_7FF"),
    )


    label("loc_7E0")

    SetScenarioFlags(0x75, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_7FF")

    label("loc_7EF")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_7FC")

    OP_B7(0x0)
    Return()

    label("loc_7FF")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x648, 1)"), scpexpr(EXPR_END)), "loc_857")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_8BA")

    label("loc_857")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x648),
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

    label("loc_8BA")

    Jump("loc_91F")

    label("loc_8BF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "What do you say when your divine wolf sneezes?\x01",
            "...Goodhoundzeit!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_91F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_700 end

    def Function_4_92B(): pass

    label("Function_4_92B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A15")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_9AB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11A, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_A10")

    label("loc_9AB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
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

    label("loc_A10")

    Jump("loc_AAA")

    label("loc_A15")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Please take a seat and wait your turn.\x01",
            "I'm a very busy chest.\x01",
            "I am the Chest Executive Officer, after all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_AAA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_92B end

    def Function_5_AB6(): pass

    label("Function_5_AB6")

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
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("chr/ch00851.itc", 0x27)
    LoadChrToIndex("monster/ch63350.itc", 0x28)
    LoadChrToIndex("monster/ch63351.itc", 0x29)
    OP_68(50, -500, 570, 0)
    MoveCamera(74, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(74590, 0)
    SetChrPos(0x101, -620, 0, -38390, 0)
    SetChrPos(0x102, 650, 0, -38440, 0)
    SetChrPos(0x103, 50, 0, -40770, 0)
    SetChrPos(0x104, 1330, 0, -39600, 0)
    SetChrPos(0x109, -750, 0, -39780, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, -2600, 0, -31400, 135)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 4000, 0, -30000, 225)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    MoveCamera(55, 18, 0, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(170, 1600, -29170, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20640, 0)
    OP_68(170, 300, -29170, 3000)

    def lambda_C55():
        OP_95(0xFE, -590, 0, -33170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C55)

    def lambda_C6F():
        OP_95(0xFE, 850, 0, -33090, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6F)

    def lambda_C89():
        OP_95(0xFE, 10, 0, -35420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C89)

    def lambda_CA3():
        OP_95(0xFE, 1680, 0, -34170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CA3)

    def lambda_CBD():
        OP_95(0xFE, -580, 0, -34360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CBD)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        "#2201115V#0005F#6PThis place is something else...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201116V#0102F#12PIt's tremendous. If I recall, this tower\x01",
            "was built during the Middle Ages.\x02\x03",
            "#2201117VAnd, is it my imagination, or are\x01",
            "there fireflies floating about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201118V#0500F#6PNo, I see them, too.\x02\x03",
            "#2201119V#0506FIt's been nearly ten years since\x01",
            "this tower was cordoned off.\x02\x03",
            "#2201120VTruth be told, I always thought it'd be\x01",
            "smart to conduct another investigation\x01",
            "of this place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201121V#0306F#12PDoubt that would go over well with\x01",
            "your chickenshit commander.\x02\x03",
            "#2201122VI can picture him sayin' 'Sergeant Major Seeker,\x01",
            "that would be a waste of our precious budget!'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x104, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#2201123V#0506F#6P*sigh* Impeccable impression.\x02\x03",
            "#2201124V#0501FHe was your superior when you were in\x01",
            "the CGF, right, Randy?\x02\x03",
            "#2201125VI sure am lucky to work under Deputy\x01",
            "Commander Baelz. I doubt I could\x01",
            "handle him instead.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x109, 500)

    ChrTalk(
        0x104,
        (
            "#2201126V#0309F#11PHaha. That bastard's one of the\x01",
            "reasons I became a cop, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201127V#0505F#6POh, I hadn't realized.\x02",
    )

    CloseMessageWindow()

    def lambda_10F8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F8)
    Sleep(50)

    def lambda_1108():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1108)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2201128V#0105F#5PWait a minute, Randy.\x02\x03",
            "#2201129VDidn't you say you lost your job with the\x01",
            "Guardian Force because of your excessive\x01",
            "flirtatiousness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201130V#0000F#5PYeah, you definitely mentioned that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201131V#0305F#11PWeeeell, I guess there was that, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201132V#0503F#6PHmm, that's odd.\x02\x03",
            "#2201133V#0500FMy friends stationed at Bellguard Gate\x01",
            "never once brought up Randy acting\x01",
            "like a playboy or anything like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201134V#0309F#11PYeah, well, you'd be surprised how\x01",
            "complex relationships can be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201135V#0205F#12P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#2201136V#0005F#5PSomething up, Tio?\x02",
    )

    CloseMessageWindow()

    def lambda_1392():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1392)

    def lambda_139F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_139F)
    Sleep(50)

    def lambda_13AF():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13AF)

    def lambda_13BC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13BC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x103,
        (
            "#2201137V#0208F#12PI think so...\x02\x03",
            "#2201138V#0201FThis tower appears to be different from\x01",
            "every other place we have investigated\x01",
            "thus far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201139V#0005F#5PHow so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201140V#0301F#11PYeah, you're a lil' vague there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201141V#0203F#12PEarth, water, fire, wind...\x02\x03",
            "#2201142V#0201FAlong with those four basic elements,\x01",
            "I am detecting the presence of the\x01",
            "higher elements here, as well...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2201143V#0101F#5PSo, in other words...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201144V#0501F#5PThe elements of orbal arts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201145V#0203F#12PPrecisely.\x02\x03",
            "#2201146V#0201FA lot of monsters have weaknesses to earth, water,\x01",
            "fire, and wind arts, correct?\x02\x03",
            "#2201147VUnder normal circumstances, the higher elements--\x01",
            "time, space, and mirage--are very powerful, but no\x01",
            "monsters are weak to them.\x02\x03",
            "#2201148VThis place appears to follow very different rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201149V#0006F#5PWell, I'm not an orbal expert, so I can't claim\x01",
            "to understand everything you just said.\x02\x03",
            "#2201150V#0001FBut, to sum it up, arts aren't going\x01",
            "to act like they usually do, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201151V#0206F#12PYes, that is the general idea.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 1, 0, 11)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_190B():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_190B)

    def lambda_1918():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1918)
    Sleep(50)

    def lambda_1928():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1928)

    def lambda_1935():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1935)

    def lambda_1942():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1942)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        "#2201152V#0005F#11PWait, do you hear that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201153V#0301FMonsters?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xB, 0x1)
    Fade(1000)
    SetChrPos(0x109, -750, 0, -34740, 315)
    SetChrPos(0x103, 510, 0, -35150, 315)
    OP_68(-11600, 1500, -20800, 0)
    MoveCamera(9, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    OP_68(-2660, 1500, -33360, 10000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -13700, 0, -19290, 135)
    SetChrPos(0x9, -15890, 0, -17160, 135)
    OP_82(0x0, 0x32, 0xBB8, 0x2328)
    BeginChrThread(0x8, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 9)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_68(-2020, 1900, -33810, 0)
    OP_68(-1730, 1900, -34090, 0)
    MoveCamera(344, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201154V#0011F#12PLook out!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x109,
        "#2201155V#0507F#12PWh-What are these?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201156V#0307F#12PYou're kiddin' me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201157V#0107FSave the complaints for later!\x01",
            "Here they come!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    BeginChrThread(0x8, 3, 0, 10)
    BeginChrThread(0x9, 3, 0, 10)
    SetCameraDistance(12560, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle("BattleInfo_318", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    Call(0, 13)
    Return()

    # Function_5_AB6 end

    def Function_6_1C99(): pass

    label("Function_6_1C99")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CB7")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_6_1C99")

    label("loc_1CB7")

    Return()

    # Function_6_1C99 end

    def Function_7_1CB8(): pass

    label("Function_7_1CB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CD4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_7_1CB8")

    label("loc_1CD4")

    Return()

    # Function_7_1CB8 end

    def Function_8_1CD5(): pass

    label("Function_8_1CD5")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    BeginChrThread(0xB, 1, 0, 12)
    OP_95(0xFE, -6670, 0, -26030, 2000, 0x0)
    OP_95(0xFE, -5830, 0, -31660, 2000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 6)
    TurnDirection(0xFE, 0x109, 500)
    Return()

    # Function_8_1CD5 end

    def Function_9_1D27(): pass

    label("Function_9_1D27")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_95(0xFE, -6730, 0, -26130, 2000, 0x0)
    OP_95(0xFE, -4360, 0, -29180, 2000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    EndChrThread(0xB, 0x1)
    BeginChrThread(0xFE, 0, 0, 6)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_9_1D27 end

    def Function_10_1D77(): pass

    label("Function_10_1D77")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
    Return()

    # Function_10_1D77 end

    def Function_11_1D95(): pass

    label("Function_11_1D95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DAE")
    Sound(867, 0, 80, 0)
    Sleep(1000)
    Jump("Function_11_1D95")

    label("loc_1DAE")

    Return()

    # Function_11_1D95 end

    def Function_12_1DAF(): pass

    label("Function_12_1DAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DC8")
    Sound(867, 0, 100, 0)
    Sleep(1000)
    Jump("Function_12_1DAF")

    label("loc_1DC8")

    Return()

    # Function_12_1DAF end

    def Function_13_1DC9(): pass

    label("Function_13_1DC9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("monster/ch63350.itc", 0x28)
    LoadChrToIndex("monster/ch63352.itc", 0x2A)
    OP_68(-3650, 1900, -31720, 0)
    MoveCamera(344, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    SetChrPos(0x101, -590, 0, -33170, 315)
    SetChrPos(0x102, 850, 0, -33090, 315)
    SetChrPos(0x103, 510, 0, -35150, 315)
    SetChrPos(0x104, 1680, 0, -34170, 315)
    SetChrPos(0x109, -750, 0, -34740, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, -4520, 0, -28310, 135)
    SetChrPos(0x9, -7180, 0, -29770, 135)
    LoadEffect(0x0, "event\\ev602_00.eff")
    FadeToBright(1000, 0)
    OP_0D()
    OP_82(0x0, 0x32, 0xBB8, 0xBB8)
    SetChrFlags(0x8, 0x20)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x20)
    EndChrThread(0x9, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)

    def lambda_1F5D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F5D)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_1FAD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1FAD)
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1500, 2000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_200C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_200C)

    def lambda_201D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_201D)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    OP_68(-2020, 1900, -33810, 3000)
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
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#2201158V#0007F#11PWhat the hell were those things?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201159V#0506F#5PThey definitely weren't your run-of-\x01",
            "the-mill monsters, that's for sure.\x02\x03",
            "#2201160V#0501FAnd I don't think it's possible for a person\x01",
            "to move around in that bulky armor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201161V#0108F#11PW-W-Were they gh-ghosts...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201162V#0203F#11PIt is hard to tell. All I can confidently say is\x01",
            "that they were not controlled by orbments.\x02\x03",
            "#2201163V#0201FIt is possible they were golems created by\x01",
            "alchemists from the Middle Ages...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201164V#0306F#11PSounds like a stretch to me. How could somethin'\x01",
            "from way back then still move like that?\x02\x03",
            "#2201165V#0301FYou think these might be traps\x01",
            "laid out by our friend, Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201166V#0003F#11PI can't say for sure...\x02\x03",
            "#2201167V#0001FAt the very least, we've confirmed\x01",
            "what Tio said before the fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201168V#0106F#11PRight. Something about that\x01",
            "battle felt...strange.\x02\x03",
            "#2201169V#0108FTime, space, and mirage...\x01",
            "They're the reason, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201170V#0200F#11PYes. There must be some sort\x01",
            "of spiritual disturbance here.\x02\x03",
            "#2201171V#0206FI cannot provide much more information\x01",
            "than that without proper equipment.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#2201172V#0503F#5PI knew it was a bad idea to\x01",
            "leave this place unchecked.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#2201173V#0501F#6PEveryone, we should head further in.\x02\x03",
            "#2201174VI plan to conduct a thorough investigation\x01",
            "of this tower, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2629():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2629)
    Sleep(50)

    def lambda_2639():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2639)
    Sleep(50)

    def lambda_2649():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2649)
    Sleep(50)

    def lambda_2659():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2659)
    Sleep(200)

    ChrTalk(
        0x101,
        "#2201175V#0001F#5PYou can count on us, Sergeant Major.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16810, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In some special locations, the three\x01",
            "higher elements--time, space, and\x01",
            "mirage--will be present.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Here, some arts may be more effective, and new\x01",
            "AT bonuses with a variety of effects may appear.\x01",
            "Keep an eye out and plan accordingly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x20)
    OP_D5(0x22)
    OP_D5(0x24)
    OP_D5(0x26)
    OP_D5(0x28)
    OP_D5(0x2A)
    OP_37()
    OP_68(0, 1500, -35500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 0, 0, -35500, 0)
    SetChrPos(0x1, 0, 0, -35500, 0)
    SetChrPos(0x2, 0, 0, -35500, 0)
    SetChrPos(0x3, 0, 0, -35500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x84, 3)
    OP_29(0x43, 0x1, 0x9)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_13_1DC9 end

    SaveToFile()

Try(main)
