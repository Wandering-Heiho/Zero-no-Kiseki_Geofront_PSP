from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0002.bin",                # FileName
        "m0002",                    # MapName
        "m0002",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 4, 0, 5],
    )

    BuildStringList((
        "m0002",                  # 0
        "Arios",                  # 1
        "お供１",                 # 2
        "お供２",                 # 3
        "お供１",                 # 4
        "お供２",                 # 5
        "お供２",                 # 6
        "Boss 1",                 # 7
        "SE制御",                 # 8
        "bm0002",                 # 9
        "bm0002",                 # 10
        "bm0002",                 # 11
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 12, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 2, 3, 90)
    MonsterBattlePostion("MonsterBattlePostion_B4", 14, 3, 270)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 9, 0)
    MonsterBattlePostion("MonsterBattlePostion_E8", 5, 11, 45)
    MonsterBattlePostion("MonsterBattlePostion_EC", 11, 11, 315)
    MonsterBattlePostion("MonsterBattlePostion_F0", 2, 13, 90)
    MonsterBattlePostion("MonsterBattlePostion_F4", 14, 13, 270)
    MonsterBattlePostion("MonsterBattlePostion_F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 3, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 13, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_124", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", "ms61700.dat", 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_168", 0x0002, 3, 6, 180, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1AC", 0x0002, 3, 6, 180, 0, 0, 0, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", "ms73100.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch67050.itc",               # 10
        "monster/ch67050.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       0,       0x18500B4,    "BattleInfo_124", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 6,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(-220,    500,     13170,   1200,    -220,    2000,    13170,   0x007C, 0,  24, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(250, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_45B",          # 01, 1
        "Function_2_477",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_4B3",          # 04, 4
        "Function_5_4D4",          # 05, 5
        "Function_6_64C",          # 06, 6
        "Function_7_B81",          # 07, 7
        "Function_8_1687",         # 08, 8
        "Function_9_16F4",         # 09, 9
        "Function_10_1739",        # 0A, 10
        "Function_11_177E",        # 0B, 11
        "Function_12_17C3",        # 0C, 12
        "Function_13_1808",        # 0D, 13
        "Function_14_184D",        # 0E, 14
        "Function_15_1892",        # 0F, 15
        "Function_16_18E5",        # 10, 16
        "Function_17_1938",        # 11, 17
        "Function_18_1AE9",        # 12, 18
        "Function_19_1B84",        # 13, 19
        "Function_20_4D9D",        # 14, 20
        "Function_21_4DF3",        # 15, 21
        "Function_22_4E49",        # 16, 22
        "Function_23_4E7B",        # 17, 23
        "Function_24_4EC6",        # 18, 24
        "Function_25_4F02",        # 19, 25
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_43C")

    label("loc_45A")

    Return()

    # Function_0_43C end

    def Function_1_45B(): pass

    label("Function_1_45B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_476")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_45B")

    label("loc_476")

    Return()

    # Function_1_45B end

    def Function_2_477(): pass

    label("Function_2_477")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_477")

    label("loc_495")

    Return()

    # Function_2_477 end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B2")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_496")

    label("loc_4B2")

    Return()

    # Function_3_496 end

    def Function_4_4B3(): pass

    label("Function_4_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C4")
    Event(0, 7)

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4D3")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_4D3")

    Return()

    # Function_4_4B3 end

    def Function_5_4D4(): pass

    label("Function_5_4D4")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E")
    SetMapObjFrame(0x0, "sign00", 0x0, 0x1)
    SetMapObjFrame(0x0, "light00", 0x0, 0x1)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    Jump("loc_52B")

    label("loc_50E")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)

    label("loc_52B")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546")
    OP_1B(0x1, 0x0, 0x19)

    label("loc_546")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_631")
    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_645")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_645")
    ClearChrFlags(0x10, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_645")

    Sound(128, 1, 100, 0)
    Return()

    # Function_5_4D4 end

    def Function_6_64C(): pass

    label("Function_6_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 0)), scpexpr(EXPR_END)), "loc_656")
    Return()

    label("loc_656")

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
        (1, "loc_739"),
        (SWITCH_DEFAULT, "loc_750"),
    )


    label("loc_739")

    Sleep(500)
    OP_90(0x0, 40, 0, -8060, 0)
    EventEnd(0x5)
    Return()

    label("loc_750")

    Battle("BattleInfo_124", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(40, 1000, -8060, 0)
    OP_90(0x0, 40, 0, -8060, 0)
    OP_90(0x1, 40, 0, -8060, 0)
    OP_90(0x2, 40, 0, -8060, 0)
    OP_90(0x3, 40, 0, -8060, 0)
    OP_90(0x4, 40, 0, -8060, 0)
    OP_90(0x5, 40, 0, -8060, 0)
    OP_90(0x6, 40, 0, -8060, 0)
    OP_90(0x7, 40, 0, -8060, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_812"),
        (1, "loc_815"),
        (SWITCH_DEFAULT, "loc_818"),
    )


    label("loc_812")

    EventEnd(0x5)
    Return()

    label("loc_815")

    OP_B7(0x0)
    Return()

    label("loc_818")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1200, -1500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 0, 0, -2500, 0)
    SetChrPos(0x102, 1000, 0, -3750, 0)
    SetChrPos(0x103, -1000, 0, -3750, 0)
    SetChrPos(0x104, 0, 0, -5000, 0)
    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster in Geofront A Sector!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(0, 1200, -3750, 1500)
    FadeToBright(300, 0)

    def lambda_912():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_912)
    Sleep(50)

    def lambda_922():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_922)
    Sleep(50)

    def lambda_932():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_932)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0000F#5PGood work, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304F#12PNot to be a downer, but that guy was way\x01",
            "weaker than the one Arios took down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0102F#11PThat may be so, but as long as we work\x01",
            "together, there's nothing we can't overcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0204F#6PAgreed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0202F#6PAlso, I just deactivated the lock on\x01",
            "the inner door.\x02\x03",
            "That should save us a lot of time,\x01",
            "so we should go that way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#0005F#5PG-Got'cha...\x01",
            "(When did she even do that?)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, -2500, 0)
    OP_29(0x3D, 0x1, 0x4)
    SetScenarioFlags(0x78, 0)
    OP_29(0x35, 0x4, 0x10)
    OP_29(0x35, 0x4, 0x2)
    OP_29(0x35, 0x1, 0x0)
    SetMapObjFrame(0x0, "sign00", 0x1, 0x1)
    SetMapObjFrame(0x0, "light00", 0x1, 0x1)
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)
    OP_1B(0x1, 0x0, 0x19)
    OP_65(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_6_64C end

    def Function_7_B81(): pass

    label("Function_7_B81")

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
    LoadChrToIndex("chr/ch00152.itc", 0x26)
    LoadChrToIndex("monster/ch73150.itc", 0x27)
    LoadChrToIndex("monster/ch73151.itc", 0x28)
    LoadChrToIndex("monster/ch73153.itc", 0x29)
    OP_68(0, -3000, -17500, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    AddParty(0x97, 0xFF, 0xFF)
    SetChrPos(0x101, -700, -4000, -18200, 0)
    SetChrPos(0x102, 700, -4000, -18200, 0)
    SetChrPos(0x103, -700, -4000, -18200, 0)
    SetChrPos(0x104, 700, -4000, -18200, 0)
    SetChrPos(0x197, 0, -4000, -18200, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x197, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x198, 0, 0, -1000, 180)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x9, 4800, 0, 1000, 270)
    SetChrPos(0xA, -4800, 0, 1000, 90)
    SetChrPos(0xB, 0, 0, -5500, 0)
    SetChrPos(0xC, 3400, 0, -3000, 315)
    SetChrPos(0xD, -3400, 0, -3000, 45)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    LoadEffect(0x0, "battle\\cr001000.eff")
    LoadEffect(0x1, "battle\\btgun00.eff")
    OP_68(0, -2000, -15500, 2000)
    SetCameraDistance(24000, 2000)
    FadeToBright(1000, 0)

    def lambda_DC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DC1)

    def lambda_DD2():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD2)
    Sleep(150)

    def lambda_DEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DEF)

    def lambda_E00():
        OP_97(0xFE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E00)
    Sleep(500)

    def lambda_E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E1D)

    def lambda_E2E():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E2E)
    Sleep(150)

    def lambda_E4B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E4B)

    def lambda_E5C():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E5C)
    Sleep(500)

    def lambda_E79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_E79)

    def lambda_E8A():
        OP_97(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_E8A)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    SetChrFlags(0x198, 0x4)
    SetChrPos(0x198, 0, 0, -1000, 180)

    NpcTalk(
        0x198,
        "Boy's Voice",
        "#0100602VS-Stay away from me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x198,
        "Boy's Voice",
        (
            "#0100603VSomebody! HEEEELP!\x01",
            "Please save me! Aidios!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x5DC)
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
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x198, 0x4)
    SetChrPos(0x198, 0, 0, -1000, 180)
    OP_68(0, 500, 0, 3000)
    MoveCamera(45, 22, 0, 3000)
    SetCameraDistance(22500, 3000)
    Sleep(500)
    PlayBGM("ed7511", 0)
    Sleep(500)
    BeginChrThread(0x198, 3, 0, 8)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x198, 3)
    Sleep(1000)
    OP_64(0x198)
    Fade(500)
    OP_68(0, -2000, -15500, 0)
    MoveCamera(55, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100604V#11P#0105F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100605VRyu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100606V#12P#0013F(Tch...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Attack the monsters from behind]\x01",      # 0
            "[Draw the monsters' attention]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetScenarioFlags(0x41, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1127"),
        (1, "loc_132A"),
        (SWITCH_DEFAULT, "loc_166F"),
    )


    label("loc_1127")

    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0100607V#12P#0007FEveryone, charge at them!\x02\x03",
            "#0100608VWe have the advantage of surprise!\x01",
            "But remember, our top priority is\x01",
            "that child's safety!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        "#0100609V#11P#0307FShowtime!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100610V#11P#0107FLet's go!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 700, -4500, 1700)
    MoveCamera(50, 22, 0, 1700)
    SetCameraDistance(25000, 1700)

    def lambda_1269():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1269)
    Sleep(50)

    def lambda_1286():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1286)
    Sleep(50)

    def lambda_12A3():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12A3)
    Sleep(50)

    def lambda_12C0():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12C0)
    Sleep(50)

    def lambda_12DD():
        OP_97(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_12DD)
    Sleep(1500)
    OP_6F(0x79)
    Battle("BattleInfo_168", 0x30200011, 0x2, 0x0, 0x13, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x197, 0x1)
    Jump("loc_166F")

    label("loc_132A")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#0100611V#6P#0007FElie, try to draw their attention!\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#0100612V#11P#0101FUnderstood!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(250)
    BeginChrThread(0x102, 3, 0, 17)
    WaitChrThread(0x102, 3)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 700, -6700, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    BeginChrThread(0x9, 3, 0, 15)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xC, 3, 0, 14)
    BeginChrThread(0xD, 3, 0, 14)

    def lambda_143D():
        OP_96(0xFE, 0x0, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_143D)

    def lambda_1457():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1457)
    Sleep(50)

    def lambda_1474():
        OP_97(0xFE, 0x0, 0x0, 0x189C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1474)
    Sleep(50)

    def lambda_1491():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1491)
    Sleep(50)

    def lambda_14AE():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_14AE)
    WaitChrThread(0x197, 1)
    WaitChrThread(0x198, 1)

    ChrTalk(
        0x103,
        (
            "#0100613V#12P#0201FWe managed to distract them,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100614V#12P#0007FAll right! Let's take them out!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x9, 0, 0, 1)

    def lambda_157F():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_157F)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_15AC():
        OP_98(0xFE, 0xBB8, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15AC)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xB, 0, 0, 1)

    def lambda_15D9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_15D9)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xC, 0, 0, 1)

    def lambda_1606():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1606)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xD, 0, 0, 1)

    def lambda_1633():
        OP_98(0xFE, 0x5DC, 0x0, 0xFFFFEC78, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1633)
    Sleep(500)
    Battle("BattleInfo_1AC", 0x30200011, 0x0, 0x0, 0x14, 0xFF)
    FadeToDark(0, 0, -1)
    CancelBlur(0)
    Jump("loc_166F")

    label("loc_166F")

    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    Call(0, 19)
    Return()

    # Function_7_B81 end

    def Function_8_1687(): pass

    label("Function_8_1687")

    BeginChrThread(0xB, 3, 0, 11)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_16A4():
        OP_96(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_16A4)
    WaitChrThread(0x198, 1)
    Sleep(1000)
    BeginChrThread(0x9, 3, 0, 9)
    BeginChrThread(0xC, 3, 0, 12)
    OP_93(0x198, 0x5A, 0x1F4)
    Sleep(1000)
    BeginChrThread(0xA, 3, 0, 10)
    BeginChrThread(0xD, 3, 0, 13)
    OP_93(0x198, 0x10E, 0x1F4)
    Sleep(1000)
    OP_93(0x198, 0xB4, 0x1F4)
    Return()

    # Function_8_1687 end

    def Function_9_16F4(): pass

    label("Function_9_16F4")

    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_170C():
        OP_96(0xFE, 0xCE4, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_170C)
    WaitChrThread(0x9, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_9_16F4 end

    def Function_10_1739(): pass

    label("Function_10_1739")

    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1751():
        OP_96(0xFE, 0xFFFFF31C, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1751)
    WaitChrThread(0xA, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_10_1739 end

    def Function_11_177E(): pass

    label("Function_11_177E")

    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1796():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1796)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_11_177E end

    def Function_12_17C3(): pass

    label("Function_12_17C3")

    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_17DB():
        OP_96(0xFE, 0x960, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_17DB)
    WaitChrThread(0xC, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    Return()

    # Function_12_17C3 end

    def Function_13_1808(): pass

    label("Function_13_1808")

    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1820():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1820)
    WaitChrThread(0xD, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    Return()

    # Function_13_1808 end

    def Function_14_184D(): pass

    label("Function_14_184D")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1865():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1865)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_184D end

    def Function_15_1892(): pass

    label("Function_15_1892")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_18B1():
        OP_98(0xFE, 0x514, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18B1)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_15_1892 end

    def Function_16_18E5(): pass

    label("Function_16_18E5")

    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1904():
        OP_98(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1904)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 0)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_16_18E5 end

    def Function_17_1938(): pass

    label("Function_17_1938")


    def lambda_193D():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_193D)
    Sleep(500)
    Fade(250)
    OP_68(700, 700, -6000, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x9, 3300, 0, 0, 270)
    SetChrPos(0xA, -3300, 0, 0, 90)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    Sound(1104, 255, 100, 0)
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xB, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    TurnDirection(0x102, 0x9, 500)
    Sound(1105, 255, 100, 0)
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xC, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    TurnDirection(0x102, 0xA, 500)
    Sound(1106, 255, 100, 0)
    OP_A0(0x102, 1500, 0x0, 0x2)
    Sleep(200)
    Sound(530, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xD, 3, 0, 18)
    OP_A1(0x102, 0x7D0, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_17_1938 end

    def Function_18_1AE9(): pass

    label("Function_18_1AE9")

    EndChrThread(0xFE, 0x0)

    def lambda_1AF2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1AF2)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_63(0xFE, 0x0, 1100, 0xC, 0xD, 0xFA, 0x2)
    OP_93(0xFE, 0xB4, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 0)
    Return()

    # Function_18_1AE9 end

    def Function_19_1B84(): pass

    label("Function_19_1B84")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch62350.itc", 0x26)
    LoadChrToIndex("monster/ch62352.itc", 0x27)
    LoadChrToIndex("chr/ch02400.itc", 0x28)
    LoadChrToIndex("apl/ch50007.itc", 0x29)
    LoadChrToIndex("apl/ch50540.itc", 0x2A)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 0, 0, -2300, 180)
    SetChrPos(0x102, -2300, 0, 0, 270)
    SetChrPos(0x103, 2300, 0, 0, 90)
    SetChrPos(0x104, 0, 0, 2300, 0)
    SetChrPos(0x198, 500, 0, 0, 90)
    SetChrPos(0x197, -500, 0, 0, 270)
    LoadEffect(0x0, "event\\ev001_00.eff")
    LoadEffect(0x1, "event\\ev000_00.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#0100615V#12P#0003FPhew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100616V#6P#0106FThat was more difficult than I thought\x01",
            "it would be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100617V#5P#0300FThey gave us a bit of a hard time, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100618V#11P#0206F*sigh* I am exhausted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100619V#5PWh-Whoa. That was a close one!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    def lambda_1F0A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F0A)
    Sleep(50)

    def lambda_1F1A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F1A)
    Sleep(50)

    def lambda_1F2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1F2A)
    Sleep(50)

    def lambda_1F3A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1F3A)
    Sleep(50)
    TurnDirection(0x197, 0x198, 500)

    ChrTalk(
        0x197,
        "#0100620V#6PRyu, are you okay?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    ChrTalk(
        0x198,
        (
            "#0100621V#11PY-Yeah. I could've handled\x01",
            "those monsters myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100622V#11PI'm glad you managed to stay\x01",
            "in one piece, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100623V#11PSeriously, you're so slow, man.\x01",
            "You'd have been monster chow\x01",
            "if I didn't come save you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        (
            "#0100624V#6PY-You're one to talk! Two minutes ago,\x01",
            "you were THIS close to getting gobbled up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        (
            "#0100625V#6PWasn't this all your idea to begin with?\x01",
            "'Yeah, let's go in, Anri!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100626V#11PWh-What the heck is your problem?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100627V#11PI remember YOU being the one talking so\x01",
            "much about this 'Geofront' or whatever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100628V#6PB-But I never actually wanted to go inside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100629V#12P#0003FAll right, break it up, you two.\x01",
            "No more fighting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_227E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_227E)
    Sleep(50)

    def lambda_228E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_228E)
    WaitChrThread(0x198, 2)

    ChrTalk(
        0x197,
        "#0100630V#1PS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100631V#5PHmm, I haven't seen you\x01",
            "guys around town before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100632V#5PYou're crazy strong! Are you\x01",
            "rookies or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100633V#12P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100634V#5P#0306FReal smooth, kid.\x02\x03",
            "#0100635V#0301FBut y'know, shouldn't you show us\x01",
            "some gratitude before anything else?\x01",
            "We did just save your hide.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23FA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_23FA)
    Sleep(500)

    ChrTalk(
        0x198,
        "#0100636V#12PHeh, fine. Thanks for the save!\x02",
    )

    CloseMessageWindow()

    def lambda_243C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_243C)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2464")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_248B")

    label("loc_2464")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1A), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2481")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_248B")

    label("loc_2481")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_248B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24A7"),
        (1, "loc_25B8"),
        (2, "loc_2695"),
        (SWITCH_DEFAULT, "loc_275F"),
    )


    label("loc_24A7")

    OP_2C(0x3C, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x198,
        "#0100637V#5PThey weren't even able to hit me once!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100638V#5PYou guys are preeetty good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100639V#7B#38Z#46B#48Z#12P#0005FWell, thanks...\x02\x03",
            "#0100640V#5B#14Z#37B#85Z#0012F#0EI can't really tell if this flattery is\x01",
            "genuine or not, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_25B8")

    OP_2C(0x3C, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x198,
        (
            "#0100641V#5PThere were some close calls, but\x01",
            "you guys managed to pull through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100642V#5PI'd give your performance a C-.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100643V#12P#0002FHaha... Yeah, we still have room\x01",
            "to improve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_2695")


    ChrTalk(
        0x198,
        (
            "#0100644V#5PStill, aren't you guys a little\x01",
            "too incompetent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100645V#5PI could've died back there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100646V#12P#0006FI'm sorry. We didn't mean to put\x01",
            "the two of you through that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_275F")


    ChrTalk(
        0x102,
        (
            "#0100647V#6P#0104FI'm glad they're both all right\x01",
            "in the end.\x02\x03",
            "#0100648V#0102FShouldn't we hurry out of here\x01",
            "while we have the chance?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100649V#11P#0204FYes, we should. I think this is as\x01",
            "far as we can go in A Sector.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0100650V#11P#0202FBesides, we have seemingly completed\x01",
            "Chief Sergei's mission, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100651V#12P#0000FTrue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100652V#5P#0306FWell, no way in hell was I expectin'\x01",
            "somethin' like this to go down.\x02\x03",
            "#0100653V#0302FAfter we get these rascals home,\x01",
            "we should report back to the\x01",
            "police department, yeah?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2998():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_2998)

    def lambda_29A5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_29A5)
    WaitChrThread(0x198, 2)
    OP_63(0x198, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x197, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x198)
    OP_64(0x197)

    ChrTalk(
        0x101,
        "#0100654V#12P#0000FUh, what's wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_2A0D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 2, lambda_2A0D)

    def lambda_2A1A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 2, lambda_2A1A)
    WaitChrThread(0x198, 2)

    ChrTalk(
        0x198,
        "#0100655V#5PWell, I'm just wonderin'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100656V#5P...are you guys really rookies?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100657V#12P#0005FY-Yeah, we are.\x02\x03",
            "#0100658V#0000FIs it that easy to tell? We aren't required to\x01",
            "wear uniforms... I'm impressed you noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100659V#5PHuh? Uniforms?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100660V#1PUmm, wait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100661V#1PAre you not from the guild?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0100662V#12P#0011FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100663V#6P#0105FBy guild, you mean the\x01",
            "Bracer Guild, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100664V#5PWhat?! Do you honestly think we'd be\x01",
            "talkin' about the Fisherman's Guild?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100665V#5PAre you kiddin' me?!\x01",
            "You AREN'T bracers?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100666V#12P#0012FN-No, we aren't.\x02\x03",
            "#0100667V#0000FWe're all new recruits at the\x01",
            "Crossbell Police Department.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x197,
        "#0100668V#1P#4SHuuuuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100669V#5P#4SYou're the freakin' police?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100670V#5PNo way! Why in the world would\x01",
            "cops be patrolling the Geofront?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100671V#12P#0003FW-Well, it's sort of an odd situation.\x02\x03",
            "#0100672VWhile we were on a mission in here,\x01",
            "we ran into Anri in a ventilation duct...\x02\x03",
            "#0100673V#0000FBut, what's so strange about the\x01",
            "police being involved here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100674V#5PYou've gotta be pullin' my leg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100675V#5PEveryone knows the police are famous\x01",
            "for being a bunch of cowards.\x02",
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

    ChrTalk(
        0x101,
        "#0100676V#12P#0011F#4SOh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100677V#5PDad's always sayin' that even though\x01",
            "they act all high-and-mighty, they\x01",
            "never actually help anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100678V#5PHe told me that in times of need,\x01",
            "I should always count on the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100679V#12P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100680V#6P#0108FOf course...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x197, 0x198, 500)
    Sleep(300)

    ChrTalk(
        0x197,
        "#0100681V#6PR-Ryu, don't be rude!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        (
            "#0100682V#6PDoes it matter if they're policemen or not?\x01",
            "They're the ones who saved us, after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x198, 0x197, 500)

    ChrTalk(
        0x198,
        "#0100683V#11PYeah, yeah. I know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100684V#11PI just thought that some new recruits\x01",
            "from the guild came to save us, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100685V#5P#0305FSounds like people have pretty, uh..\x01",
            "passionate feelings about the cops,\x01",
            "huh?\x02\x03",
            "#0100686V#0301F...Hold up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)

    ChrTalk(
        0x104,
        "#0100687V#5P#0307FWe got a problem here!\x02",
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
    Sleep(1000)
    SetChrPos(0xE, 0, 7000, -7000, 0)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_33D8():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33D8)
    Sleep(100)

    def lambda_33E8():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_33E8)

    def lambda_33F5():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33F5)

    ChrTalk(
        0x101,
        "#0100688V#5P#0005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100689V#5P#0201F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100690V#5P#0105FAbove us?!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1400, -7000, 1000)
    MoveCamera(43, 27, 0, 1000)
    SetCameraDistance(14000, 1000)
    Sleep(700)
    SetChrChip(0x0, 0xE, 0x1E, 0x64)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Sound(812, 0, 100, 0)

    def lambda_34AB():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0xA, 0x9C4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_34AB)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 2000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x0, 0x2BC, 0xBB8, 0x7D0)
    Sound(813, 0, 100, 0)
    Sleep(2500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    CancelBlur(0)
    OP_68(100000, 1500, -7000, 0)
    MoveCamera(130, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrPos(0x101, 100000, 0, -2600, 180)
    SetChrPos(0x102, 97400, 0, 0, 180)
    SetChrPos(0x103, 102600, 0, 0, 180)
    SetChrPos(0x104, 100000, 0, 2400, 180)
    SetChrPos(0x198, 100500, 0, 0, 180)
    SetChrPos(0x197, 99500, 0, 0, 180)
    SetChrPos(0xE, 100000, 0, -7000, 0)
    ClearChrFlags(0xE, 0x1)
    SetChrChip(0x1, 0xE, 0x0, 0x0)
    OP_68(100000, 700, -4000, 2000)
    MoveCamera(140, 15, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_0D()
    Sleep(500)

    def lambda_35FC():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35FC)
    Sleep(150)
    OP_63(0x197, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_362B():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_362B)
    Sleep(100)
    OP_63(0x198, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    def lambda_365A():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_365A)
    OP_6F(0x79)

    ChrTalk(
        0x197,
        "#0100691V#5POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100692VAhhh!\x02",
    )

    CloseMessageWindow()
    OP_64(0x198)
    OP_64(0x197)

    ChrTalk(
        0x101,
        "#0100693V#0010F#6PTch...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0100694V#0310F#6PThis the head honcho?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100695V#0107F#6PI-It's enormous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100696V#0208F#6PThe door behind us is locked.\x01",
            "We cannot get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100697V#0013F#6PDamn, at this rate...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x104,
        (
            "#0100698V#0307F#6PHey, what's the plan?!\x02\x03",
            "#0100699VEven if we go all out, we don't stand\x01",
            "a chance with our current gear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100700V#0007F#5PI know that!\x02\x03",
            "#0100701VListen, I'll draw its attention!\x01",
            "You guys take the kids and find\x01",
            "a way out!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_392C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_392C)
    Sleep(50)

    def lambda_393C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_393C)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        "#0100702V#12P#0101FY-You can't be...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100703V#0201FAre you insane?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0100704V#0007F#5PIt's our only option!\x02\x03",
            "#0100705VRandy, Elie! Take them and run!\x01",
            "Do what you have to do to get\x01",
            "them to safety!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100706V#0310F#6PTch... Are there really no other\x01",
            "alternatives?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100707V#5PN-No way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100708VH-Hey, wait...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 100000, 4000, -17700, 0)

    NpcTalk(
        0x8,
        "Voice",
        "#0100709V#3PI have to say I'm disappointed.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Voice",
        (
            "#0100710V#3PSelf-sacrifice is admirable, but don't\x01",
            "be too eager to meet your grave.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_3BF6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BF6)

    def lambda_3C03():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C03)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 100000, 6000, -17700, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_68(100000, 6900, -17700, 2500)
    MoveCamera(152, 18, 0, 2500)
    SetCameraDistance(16000, 2500)
    OP_6F(0x79)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Man")

    AnonymousTalk(
        0xFF,
        "#0100711V...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    OP_68(100320, 1700, -6240, 1100)
    MoveCamera(127, 15, 0, 1100)
    OP_6E(600, 1100)
    SetCameraDistance(15000, 1100)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3DA2():
        OP_9D(0xFE, 0x186A0, 0x0, 0xFFFFEE6C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3DA2)
    BeginChrThread(0x8, 3, 0, 22)
    Sleep(900)
    Sound(815, 0, 100, 0)
    Sound(259, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x0, 0, 1000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xE, 0x20)
    EndChrThread(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0x8, 1)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x8, 3)
    Sleep(300)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_6F(0x79)
    Sleep(1000)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0100712V#0005F#5P...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(300)
    MoveCamera(130, 17, 0, 1500)
    SetCameraDistance(19500, 1500)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetChrFlags(0xE, 0x20)
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)

    def lambda_3EDC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3EDC)
    PlayEffect(0x0, 0xFF, 0xE, 0x0, 0, 1000, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(816, 0, 100, 0)
    Sleep(500)

    def lambda_3F35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3F35)
    WaitChrThread(0xE, 2)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_6F(0x50)
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
    OP_63(0x197, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x198, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#0100713V#0005F#5P#4S...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(100000, 700, -6000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_68(100000, 700, -4000, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        "#0100714V#0305F#6PH-Holy crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100715V#0105F#6PThat was unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100716V#0205F#6PMy eyes could not keep up...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -3500, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 0, 0, -1300, 180)
    SetChrPos(0x102, -2100, 0, 0, 180)
    SetChrPos(0x103, 2100, 0, 0, 180)
    SetChrPos(0x104, 0, 0, 1500, 180)
    SetChrPos(0x198, 500, 0, 700, 180)
    SetChrPos(0x197, -500, 0, 700, 180)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, -5000, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x198,
        "#0100717V#5P#4SA-Amazing!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x198, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x197, 3, 0, 21)
    WaitChrThread(0x197, 3)
    OP_9C(0x198, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x198, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    ChrTalk(
        0x198,
        (
            "#0100718V#11PThat was freakin' sweet!\x01",
            "You're the best, Arios!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        (
            "#0100719V#11PWoooohooooo! This is the\x01",
            "greatest day of my life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100720V#6PTh-Thank you for saving us, Arios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100721V#6PBut, why are you here?\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    NpcTalk(
        0x8,
        "Man",
        (
            "#0100722V#11P#1403FWell, I read a report that mentioned two\x01",
            "kids were seen entering Central Square's\x01",
            "manhole. So, I decided to look into it.\x02\x03",
            "#0100723V#1401FWhat you did was incredibly foolish.\x02\x03",
            "#0100724VWhat would you have done if no one\x01",
            "showed up to rescue you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100725V#6P*sniff* I-I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100726V#11PUh, sorry 'bout that.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5F, 0x190)
    Sleep(300)

    NpcTalk(
        0x8,
        "Man",
        (
            "#0100727V#5P#1402FHah. You two are unharmed,\x01",
            "so we'll leave it at that.\x02\x03",
            "#0100728V#1404FIt's late. Let's get you home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x198,
        "#0100729V#11PSounds good to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x197,
        "#0100730V#6PR-Right!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    ClearChrFlags(0x8, 0x4)

    def lambda_45BE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_45BE)
    Sleep(150)

    def lambda_45DB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_45DB)
    Sleep(50)

    def lambda_45F8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_45F8)
    WaitChrThread(0x8, 1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_4632():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_4632)
    Sleep(50)

    def lambda_4642():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4642)
    Sleep(300)

    NpcTalk(
        0x8,
        "Man",
        (
            "#0100731V#12P#1400FWhat's the matter? You don't intend\x01",
            "to stay down here, do you?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#0100732V#0005F#5PN-No...\x02\x03",
            "#0100733V#0001FNo, we aren't. We'll head back\x01",
            "with you, if you don't mind.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Man",
        (
            "#0100734V#12P#1403FGood. No dawdling, then.\x02\x03",
            "#0100735V#1400FNever let your guard down until\x01",
            "you're certain everything is over.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    def lambda_47B3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_47B3)
    Sleep(50)

    def lambda_47C3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_47C3)

    def lambda_47D0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47D0)
    Sleep(150)

    def lambda_47ED():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_47ED)
    Sleep(50)

    def lambda_480A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFE890, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_480A)
    WaitChrThread(0x8, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(0, 1000, -500, 2000)
    OP_6F(0x1)
    Sleep(500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        "#0100736V#5P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100737V#5P#0305FWhat's with that smug old coot?!\x02\x03",
            "#0100738V#0306FThe guy had a strange aura,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0100739V#5P#0206FHis physical abilities were anything\x01",
            "but ordinary, as well.\x02\x03",
            "#0100740V#0200FJust who is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100741V#5P#0101FHe must be...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_49A8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_49A8)
    Sleep(50)

    def lambda_49B8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_49B8)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x104,
        "#0100742V#5P#0305FMademois-Elie, you know that guy?\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#0100743V#6P#0103FOnly by name.\x02\x03",
            "#0100744V#0105FAlso, why are you calling me that?\x01",
            "That's not my name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100745V#5P#0309FJust kinda felt like it. Fancy name\x01",
            "for a fancy lady.\x02\x03",
            "#0100746V#0301FSo, ya gonna spill the beans or what?\x01",
            "Who was that guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100747V#6P#0108FIf I'm not mistaken, that was--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100748V#5P#0003FArios MacLaine.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4BA7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4BA7)
    Sleep(50)

    def lambda_4BB7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4BB7)
    Sleep(50)

    def lambda_4BC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4BC7)
    WaitChrThread(0x102, 2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0100749V#5P#0006FI've read about him in the Crossbell Times more\x01",
            "times than I can count.\x02\x03",
            "#0100750VHe's an A-rank bracer who operates out of the\x01",
            "Bracer Guild's Crossbell branch...\x02\x03",
            "#0100751V#0008FHe's a man capable of responding to any request\x01",
            "and has earned the utmost trust of the citizens.\x01",
            "People call him the guardian of Crossbell.\x02\x03",
            "#0100752V#0001FThe Divine Blade of Wind, Arios MacLaine.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 0, 0, 23)
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0xF, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1B84 end

    def Function_20_4D9D(): pass

    label("Function_20_4D9D")

    OP_63(0x198, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_4DB4():
        OP_95(0xFE, 1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4DB4)
    WaitChrThread(0x198, 1)

    def lambda_4DD2():
        OP_95(0xFE, 1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x198, 1, lambda_4DD2)
    WaitChrThread(0x198, 1)
    TurnDirection(0x198, 0x8, 500)
    Return()

    # Function_20_4D9D end

    def Function_21_4DF3(): pass

    label("Function_21_4DF3")

    OP_63(0x197, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_4E0A():
        OP_95(0xFE, -1300, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_4E0A)
    WaitChrThread(0x197, 1)

    def lambda_4E28():
        OP_95(0xFE, -1000, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x197, 1, lambda_4E28)
    WaitChrThread(0x197, 1)
    TurnDirection(0x197, 0x8, 500)
    Return()

    # Function_21_4DF3 end

    def Function_22_4E49(): pass

    label("Function_22_4E49")

    Sleep(300)

    def lambda_4E51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4E51)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)

    def lambda_4E6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4E6A)
    WaitChrThread(0x8, 2)
    Return()

    # Function_22_4E49 end

    def Function_23_4E7B(): pass

    label("Function_23_4E7B")

    OP_25(0x80, 0x64)
    Sleep(200)
    OP_25(0x80, 0x5A)
    Sleep(200)
    OP_25(0x80, 0x50)
    Sleep(200)
    OP_25(0x80, 0x46)
    Sleep(200)
    OP_25(0x80, 0x3C)
    Sleep(200)
    OP_25(0x80, 0x32)
    Sleep(200)
    OP_25(0x80, 0x28)
    Sleep(200)
    OP_25(0x80, 0x1E)
    Sleep(200)
    OP_25(0x80, 0x14)
    Sleep(200)
    OP_25(0x80, 0xA)
    Sleep(200)
    OP_25(0x80, 0x0)
    Return()

    # Function_23_4E7B end

    def Function_24_4EC6(): pass

    label("Function_24_4EC6")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked and cannot be opened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_24_4EC6 end

    def Function_25_4F02(): pass

    label("Function_25_4F02")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE2")

    ChrTalk(
        0x103,
        (
            "#0200FLloyd, I unlocked the inner door.\x02\x03",
            "#0203FThere is a shortcut to the surface through\x01",
            "there. That should save us the most time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FGood work.\x02\x03",
            "#0000FLet's make our way out through there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_503D")

    label("loc_4FE2")


    ChrTalk(
        0x101,
        (
            "#0000FTio unlocked a shortcut to the surface.\x01",
            "Might as well use it, since we're here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_503D")

    Sleep(50)
    SetChrPos(0x0, 90, -3770, -16530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4F02 end

    SaveToFile()

Try(main)
