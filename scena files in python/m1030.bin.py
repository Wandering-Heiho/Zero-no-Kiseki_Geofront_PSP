from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1030.bin",                # FileName
        "m1030",                    # MapName
        "m1030",                    # Location
        0x006D,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 30000, 0, 0, 0, 0, 1, 109, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1030",                  # 0
        "bm1000",                 # 1
        "bm1020",                 # 2
        "bm1020",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A4", 0,   0,   14,  5,   3,   7,   6)
    Sepith("Sepith_B4", 13,  0,   0,   6,   6,   5,   5)
    Sepith("Sepith_C4", 0,   15,  0,   6,   4,   5,   5)

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
        "BattleInfo_134", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_A4", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_1FC", 0x0000, 21, 6, 60, 4, 1, 25, 0, "bm1000", "Sepith_B4", 40, 30, 20, 10,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63300.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_2C4", 0x0000, 21, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_C4", 40, 30, 20, 10,
        (
            ("ms62800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms62800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
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

    DeclMonster(3010,    -18420,  0,       0x1010000,    "BattleInfo_134", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-5830,   160,     0,       0x1010000,    "BattleInfo_1FC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-24680,  -7250,   0,       0x1010000,    "BattleInfo_2C4", 0,   18,  0xFFFF, 2,  3)

    DeclActor(3600,    0,       5000,    1200,    3600,    1000,    5000,    0x007C, 0,  2,  0x0000)
    DeclActor(-25500,  0,       0,       1200,    -25500,  1000,    0,       0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_4E4",          # 00, 0
        "Function_1_4E5",          # 01, 1
        "Function_2_73A",          # 02, 2
        "Function_3_8D9",          # 03, 3
    ))


    def Function_0_4E4(): pass

    label("Function_0_4E4")

    Return()

    # Function_0_4E4 end

    def Function_1_4E5(): pass

    label("Function_1_4E5")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E")
    OP_70(0x0, 0x0)
    Jump("loc_722")

    label("loc_71E")

    OP_70(0x0, 0x1E)

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_735")
    OP_70(0x1, 0x0)
    Jump("loc_739")

    label("loc_735")

    OP_70(0x1, 0x1E)

    label("loc_739")

    Return()

    # Function_1_4E5 end

    def Function_2_73A(): pass

    label("Function_2_73A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_7BA")
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
    SetScenarioFlags(0x11A, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_81F")

    label("loc_7BA")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_81F")

    Jump("loc_8CD")

    label("loc_824")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I hear the Strega Corporation made a job offer\x01",
            "to Noel. Please look forward to the latest in\x01",
            "Zemurian footwear: Noel Sneakers.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_8CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_73A end

    def Function_3_8D9(): pass

    label("Function_3_8D9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C3")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_959")
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
    SetScenarioFlags(0x11A, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_9BE")

    label("loc_959")

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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_9BE")

    Jump("loc_A48")

    label("loc_9C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I haven't been opened in 500 years...\x01",
            "I can finally move on to the next life. Thank you...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_A48")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8D9 end

    SaveToFile()

Try(main)
