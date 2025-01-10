from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1140.bin",                # FileName
        "m1140",                    # MapName
        "m1140",                    # Location
        0x006E,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, -28000, -30000, 0, 0, 1, 110, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1140",                  # 0
        "Iron Stack",             # 1
        "bm1040",                 # 2
        "bm1040",                 # 3
        "bm1040",                 # 4
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_B4", 6,   6,   15,  9,   0,   0,   0)
    Sepith("Sepith_C4", 4,   4,   0,   0,   9,   9,   9)

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
    MonsterBattlePostion("MonsterBattlePostion_134", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 12, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_154", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_B4", 60, 25, 10, 5,
        (
            ("ms65000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms65000.dat", "ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_21C", 0x0000, 21, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_C4", 60, 25, 10, 5,
        (
            ("ms62700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            ("ms62700.dat", "ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2E4", 0x0000, 40, 6, 0, 0, 1, 0, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72900.dat", "ms72900.dat", "ms72900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_F4", "ed7401", "ed7403", "ATBonus_A4"),
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
        "monster/ch65050.itc",               # 10
        "monster/ch65050.itc",               # 11
        "monster/ch62750.itc",               # 12
        "monster/ch62750.itc",               # 13
        "monster/ch72950.itc",               # 14
        "monster/ch72951.itc",               # 15
    ))

    DeclNpc(0,       -27500,  23000,   0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(20770,   2670,    -28000,  0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(7940,    18540,   -29190,  0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-1260,   21090,   -29200,  0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-12520,  16300,   -29190,  0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21210,  -550,    -28000,  0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4300,    4670,    -27200,  0x1010000,    "BattleInfo_154", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7580,   4170,    -27200,  0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(320,     -6970,   -27200,  0x1010000,    "BattleInfo_21C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(0,       -29000,  23000,   1200,    0,       -28000,  23000,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_500",          # 00, 0
        "Function_1_51F",          # 01, 1
        "Function_2_520",          # 02, 2
        "Function_3_538",          # 03, 3
    ))


    def Function_0_500(): pass

    label("Function_0_500")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_500")

    label("loc_51E")

    Return()

    # Function_0_500 end

    def Function_1_51F(): pass

    label("Function_1_51F")

    Return()

    # Function_1_51F end

    def Function_2_520(): pass

    label("Function_2_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_70(0x0, 0x0)
    Jump("loc_537")

    label("loc_533")

    OP_70(0x0, 0x1E)

    label("loc_537")

    Return()

    # Function_2_520 end

    def Function_3_538(): pass

    label("Function_3_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D3")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sense powerful monsters in the chest.\x01",
            "Monster level: 40\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_5D3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_792")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_62C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_62C)

    def lambda_646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_646)
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
    Battle("BattleInfo_2E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_6B3"),
        (2, "loc_6C2"),
        (1, "loc_6CF"),
        (SWITCH_DEFAULT, "loc_6D2"),
    )


    label("loc_6B3")

    SetScenarioFlags(0x72, 4)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_6D2")

    label("loc_6C2")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_6CF")

    OP_B7(0x0)
    Return()

    label("loc_6D2")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x9C, 1)"), scpexpr(EXPR_END)), "loc_72A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11B, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_78D")

    label("loc_72A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
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

    label("loc_78D")

    Jump("loc_7DF")

    label("loc_792")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You came back! You actually came back for me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7DF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_538 end

    SaveToFile()

Try(main)
