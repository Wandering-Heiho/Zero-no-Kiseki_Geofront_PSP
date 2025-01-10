from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t160b.bin",                # FileName
        "t160b",                    # MapName
        "t160b",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 0, 0, 1],
    )

    BuildStringList((
        "t160b",                  # 0
        "Medical Intern Lytton",  # 1
        "犬１",                   # 2
        "犬２",                   # 3
        "犬３",                   # 4
        "Cecile",                 # 5
        "Michael",                # 6
        "Event Monster",          # 7
        "Event Monster",          # 8
        "Event Monster",          # 9
        "Event Monster",          # 10
        "Doctor Gailey",          # 11
        "Chief Ursuline",         # 12
        "Doctor Lago",            # 13
        "bt160b",                 # 14
        "Ursula Road",            # 15
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 9, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
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

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 7,   5.5,                   10.5,                  6.0,                   625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.7071075439453125,    -1.1313707828521729,   -1.2000000476837158,   1.0])

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_37C",          # 00, 0
        "Function_1_3C8",          # 01, 1
        "Function_2_457",          # 02, 2
        "Function_3_987",          # 03, 3
        "Function_4_9A6",          # 04, 4
        "Function_5_9C5",          # 05, 5
        "Function_6_A13",          # 06, 6
        "Function_7_A51",          # 07, 7
        "Function_8_15D0",         # 08, 8
        "Function_9_1646",         # 09, 9
        "Function_10_165E",        # 0A, 10
        "Function_11_1688",        # 0B, 11
        "Function_12_1727",        # 0C, 12
        "Function_13_17E5",        # 0D, 13
        "Function_14_1E57",        # 0E, 14
        "Function_15_29CF",        # 0F, 15
        "Function_16_29F5",        # 10, 16
        "Function_17_322F",        # 11, 17
        "Function_18_32FB",        # 12, 18
    ))


    def Function_0_37C(): pass

    label("Function_0_37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_390")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_3C7")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_3A4")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 13)
    Jump("loc_3C7")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_3B8")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 14)
    Jump("loc_3C7")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_3C7")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 16)

    label("loc_3C7")

    Return()

    # Function_0_37C end

    def Function_1_3C8(): pass

    label("Function_1_3C8")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_422")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_456")

    label("loc_422")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_456")

    Return()

    # Function_1_3C8 end

    def Function_2_457(): pass

    label("Function_2_457")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xA0, 0xA0, 0xF0, 0x0, 0x0)
    LoadChrToIndex("chr/ch29400.itc", 0x1E)
    LoadChrToIndex("monster/ch75650.itc", 0x1F)
    LoadChrToIndex("monster/ch75652.itc", 0x20)
    LoadChrToIndex("monster/ch75651.itc", 0x21)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_68(18820, 8000, -18070, 0)
    MoveCamera(36, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, -1500, 7000, 23500, 180)
    SetChrPos(0x1, -1500, 7000, 23500, 180)
    SetChrPos(0x2, -1500, 7000, 23500, 180)
    SetChrPos(0x3, -1500, 7000, 23500, 180)
    SetChrPos(0x4, -1500, 7000, 23500, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18380, 7000, -15790, 180)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 19450, 7000, -13130, 180)
    OP_A7(0x9, 0x37, 0x37, 0x37, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 16920, 7000, -13390, 180)
    OP_A7(0xA, 0x37, 0x37, 0x37, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 19540, 7000, -10010, 180)
    OP_A7(0xB, 0x37, 0x37, 0x37, 0x0, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#1101236V\x07\x0C",
            "You see, this particular research paper\x01",
            "was for Doctor Lago, who's notoriously\x01",
            "hard to please.\x02\x03",
            "#1101237VI'd already written well into the night, putting\x01",
            "every fiber of my being into that paper, so I\x01",
            "was getting a little woozy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    SetCameraDistance(28000, 3000)

    def lambda_72A():
        OP_95(0xFE, 18670, 7000, -18200, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72A)
    Sleep(1000)
    SetChrName("Medical Intern Lytton")

    AnonymousTalk(
        0x8,
        (
            "#1101238V\x07\x0C",
            "It sort of felt like I was on a high, honestly.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)
    OP_6F(0x10)
    OP_0D()

    AnonymousTalk(
        0x8,
        (
            "#1101239V\x07\x0C",
            "Anyway, I found myself exposed to\x01",
            "the chilly night wind...and that's when\x01",
            "I heard it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)
    Sleep(800)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)
    OP_68(18220, 8000, -16770, 1500)
    SetCameraDistance(26500, 1500)

    def lambda_84C():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_84C)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 3, 0, 5)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_899():
        OP_96(0xFE, 0x495C, 0x1B58, 0xFFFFB672, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_899)
    WaitChrThread(0x8, 1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 6)
    Sleep(100)
    Sound(814, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 6)
    FadeToDark(0, -1, 0)
    FadeToDark(1000, 16777215, -1)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xC)
    SetCameraDistance(15000, 1000)
    OP_68(18820, 8000, -18070, 1000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetScenarioFlags(0x5C, 2)
    NewScene("t1540", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_2_457 end

    def Function_3_987(): pass

    label("Function_3_987")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9A5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_987")

    label("loc_9A5")

    Return()

    # Function_3_987 end

    def Function_4_9A6(): pass

    label("Function_4_9A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_4_9A6")

    label("loc_9C4")

    Return()

    # Function_4_9A6 end

    def Function_5_9C5(): pass

    label("Function_5_9C5")

    BeginChrThread(0xFE, 0, 0, 4)

    def lambda_9D0():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D0)

    def lambda_9E5():
        OP_A7(0xFE, 0x37, 0x37, 0x37, 0xFF, 0x2BC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 3)
    Return()

    # Function_5_9C5 end

    def Function_6_A13(): pass

    label("Function_6_A13")

    SetChrChipByIndex(0xFE, 0x20)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0x495C, 0x1B58, 0xFFFFB672, 0xBB8, 0x1388)
    Return()

    # Function_6_A13 end

    def Function_7_A51(): pass

    label("Function_7_A51")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch34000.itc", 0x1F)
    LoadChrToIndex("monster/ch75750.itc", 0x20)
    LoadChrToIndex("monster/ch75750.itc", 0x21)
    LoadChrToIndex("monster/ch75750.itc", 0x22)
    LoadChrToIndex("chr/ch00050.itc", 0x23)
    LoadChrToIndex("chr/ch00051.itc", 0x24)
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    LoadChrToIndex("chr/ch00151.itc", 0x26)
    LoadChrToIndex("chr/ch00250.itc", 0x27)
    LoadChrToIndex("chr/ch00251.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch00351.itc", 0x2A)
    LoadChrToIndex("chr/ch00550.itc", 0x2B)
    LoadChrToIndex("chr/ch00551.itc", 0x2C)
    LoadChrToIndex("chr/ch00052.itc", 0x2D)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    OP_68(7160, 8000, 9090, 0)
    MoveCamera(15, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26750, 0)
    SetChrPos(0x101, 6200, 7000, 10440, 135)
    SetChrPos(0x102, 5570, 7000, 12240, 135)
    SetChrPos(0x103, 4770, 7000, 10160, 135)
    SetChrPos(0x104, 3860, 7000, 12290, 135)
    SetChrPos(0x106, 4720, 7000, 13350, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18630, 7000, -14670, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19630, 7000, -15010, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x20)
    SetChrPos(0xE, 21060, 7000, -10800, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    TurnDirection(0xE, 0xC, 0)
    OP_9B(0x1, 0xE, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x20)
    SetChrPos(0xF, 16600, 7500, -12300, 135)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    TurnDirection(0xF, 0xC, 0)
    OP_9B(0x1, 0xF, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, 15620, 7000, -14850, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    TurnDirection(0x10, 0xC, 0)
    OP_9B(0x1, 0x10, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x20)
    SetChrPos(0x11, 16760, 7000, -18190, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    TurnDirection(0x11, 0xC, 0)
    OP_9B(0x1, 0x11, 0x0, 0xFFFFFE0C, 0xEA60, 0x0)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0xF, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0x10, 0, 0, 9)
    Sleep(10)
    BeginChrThread(0x11, 0, 0, 9)
    FadeToBright(1000, 0)
    SetCameraDistance(25250, 1500)

    def lambda_D35():
        OP_95(0xFE, 7150, 7000, 9240, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D35)

    def lambda_D4F():
        OP_95(0xFE, 6870, 7000, 10580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D4F)
    Sleep(50)

    def lambda_D6C():
        OP_95(0xFE, 5710, 7000, 8900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D6C)

    def lambda_D86():
        OP_95(0xFE, 5030, 7000, 10760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D86)
    Sleep(50)

    def lambda_DA3():
        OP_95(0xFE, 5980, 7000, 11680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DA3)
    WaitChrThread(0x101, 1)
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
    Sound(1089, 255, 100, 0)

    ChrTalk(
        0x101,
        "#5100658V#0013F#5PThere!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100659V#0307F#5PThat's bad news, man!\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_68(17880, 7900, -13870, 3000)
    MoveCamera(60, 19, 0, 3000)
    SetCameraDistance(26250, 3000)
    OP_6F(0x79)
    Sound(835, 0, 100, 0)

    def lambda_ED2():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_ED2)
    Sleep(200)

    def lambda_EEA():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_EEA)
    Sleep(100)

    def lambda_F02():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_F02)
    Sleep(160)

    def lambda_F1A():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F1A)
    Sleep(500)

    def lambda_F32():
        OP_96(0xFE, 0x4B14, 0x1B58, 0xFFFFC626, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F32)
    Sleep(300)

    def lambda_F4F():
        OP_96(0xFE, 0x4E3E, 0x1B58, 0xFFFFC504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F4F)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)

    def lambda_F81():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F81)
    Sleep(500)

    ChrTalk(
        0xD,
        "#5100660V#11PM-Miss Neues, wh-what do we do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5100661V#1304F#5PShush now, everything's going to be just fine.\x02\x03",
            "#5100662V#1301FC'mon, hold on to me and don't let go, okay?\x02\x03",
            "#5100663VWe'll make it out of here, I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100664V#11P*sniff* O-Okay!\x02",
    )

    CloseMessageWindow()
    OP_68(18420, 7900, -13900, 2000)
    SetCameraDistance(23250, 10000)

    def lambda_10C1():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_10C1)
    Sleep(160)

    def lambda_10D9():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_10D9)
    Sleep(100)

    def lambda_10F1():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_10F1)
    Sleep(200)

    def lambda_1109():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1109)
    SetCameraDistance(23250, 10000)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#5100665V#1301F#11P(They've cut off our escape routes.)\x02\x03",
            "#5100666V(Hopefully, if this goes as planned,\x01",
            "he'll be able to get out.)\x02\x03",
            "#5100667V#1303F(Dad, Mom, Ilya...)\x02\x03",
            "#5100668V#1308F(Lloyd, Guy... I'm so sorry!)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 16800, 7000, -7900, 135)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#5100669V#0007F#4S#2PCECILE!\x02",
    )

    CloseMessageWindow()
    OP_64(0xC)
    OP_64(0xD)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_12A3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12A3)

    def lambda_12B0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12B0)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Fade(500)
    SetChrPos(0xF, 16920, 7000, -11530, 135)
    SetChrPos(0x11, 17850, 7000, -18160, 0)
    OP_68(19250, 8000, -14850, 0)
    MoveCamera(325, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(21000, 1000)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0x11, 3, 0, 10)
    Sleep(400)
    BeginChrThread(0xE, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 10)
    BeginChrThread(0xF, 3, 0, 10)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0xC, 3)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x27)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x2B)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x101, 13900, 7000, -5430, 135)
    SetChrPos(0x102, 14960, 7000, -4030, 135)
    SetChrPos(0x103, 11490, 7000, -6790, 135)
    SetChrPos(0x104, 9360, 7000, -6960, 135)
    SetChrPos(0x106, 11980, 7000, -4590, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(16900, 7900, -11490, 1000)
    MoveCamera(325, 15, 0, 1000)
    BeginChrThread(0x101, 3, 0, 8)

    def lambda_1409():
        OP_95(0xFE, 17280, 7000, -8620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1409)

    def lambda_1423():
        OP_95(0xFE, 13910, 7000, -10360, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1423)

    def lambda_143D():
        OP_95(0xFE, 12240, 7000, -12520, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_143D)

    def lambda_1457():
        OP_95(0xFE, 13940, 7000, -8820, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1457)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#5100671V#1305F#6PLloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100672V#12PAren't they the police...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100673V#0007F#11PSave the talking for later! We have to\x01",
            "take these out, right here, right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100674V\x07\x03",
            "#0707F#5PTake care not to interfere...!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    Call(0, 13)
    Return()

    # Function_7_A51 end

    def Function_8_15D0(): pass

    label("Function_8_15D0")


    def lambda_15D5():
        OP_9D(0xFE, 0x3F48, 0x1B58, 0xFFFFD6DE, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_15D5)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    ClearChrFlags(0xFE, 0x1)
    Sound(1015, 255, 100, 0)
    Sleep(450)
    Sound(854, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x2, 0x3)
    BeginChrThread(0xF, 3, 0, 11)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x6)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xF, 3)
    Return()

    # Function_8_15D0 end

    def Function_9_1646(): pass

    label("Function_9_1646")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_165D")
    OP_A0(0xFE, 1250, 0x0, 0xFB)
    Jump("Function_9_1646")

    label("loc_165D")

    Return()

    # Function_9_1646 end

    def Function_10_165E(): pass

    label("Function_10_165E")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_166F():
        OP_A6(0xFE, 0x0, 0x50, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_166F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_165E end

    def Function_11_1688(): pass

    label("Function_11_1688")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 17000, 8300, -12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x12C)
    Sound(816, 0, 100, 0)
    Sound(246, 0, 100, 0)

    def lambda_16E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_16E1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_16FA():
        OP_A6(0xFE, 0x0, 0x50, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 0)
    Sound(514, 0, 100, 0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_11_1688 end

    def Function_12_1727(): pass

    label("Function_12_1727")

    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 18190, 7000, -16430, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 19120, 7000, -12070, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    Sleep(100)
    Sound(530, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 16560, 7000, -13120, 0, 0, 0, 1350, 1350, 1350, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_12_1727 end

    def Function_13_17E5(): pass

    label("Function_13_17E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch34000.itc", 0x1F)
    OP_68(17410, 8000, -12880, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 16810, 7000, -12960, 90)
    SetChrPos(0x102, 16100, 7000, -11900, 90)
    SetChrPos(0x103, 15080, 7000, -14420, 90)
    SetChrPos(0x104, 14290, 7000, -13590, 90)
    SetChrPos(0x106, 13800, 7000, -12240, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
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
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 19310, 7000, -13460, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19340, 7000, -14290, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(23500, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#5100675V#1302F#11PLloyd...no, all of you.\x02\x03",
            "#5100676V#1304FYou saved us. I don't know how\x01",
            "I'll ever be able to repay you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100677V#0302F#6PHey, now! None of that 'I owe you' stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100678V#0102F#6PWhat matters is that you're safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100679V#0204F#6PI am just relieved we made it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5100680V\x07\x03",
            "#0700F#6P...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100681V\x07\x00",
            "#0008F#6PTh-Thank Aidios you're okay.\x02\x03",
            "#5100682V#0006FIf something happened to you, I don't\x01",
            "know how I'd ever apologize to Guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5100683V#1305F#11PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    def lambda_1B38():
        OP_A6(0xFE, 0x0, 0x14, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B38)

    ChrTalk(
        0xD,
        "#5100684V#11P#40W*cough* *cough* *cough*\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5100685V#0005F#6PH-Hey, are you all right?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    ChrTalk(
        0xC,
        (
            "#5100686V#1303F#5PIt's just a coughing fit.\x02\x03",
            "#5100687V#1300FMichael, let's get you back to your room\x01",
            "and find you some medicine.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xC, 400)
    Sleep(300)

    ChrTalk(
        0xD,
        "#5100688V#11P#40WO-Okay... *cough* *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#5100689V#11P#40WI'm so sorry, Miss Neues...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5100690V#11P#40WIf I wasn't so selfish and said that thing,\x01",
            "this never would have happened. *cough*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5100691V#1302F#5PShhh, don't mind that. Everything's okay.\x02",
    )

    CloseMessageWindow()
    OP_68(18160, 8000, -12960, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x28A, 0x4B0, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5100692V#0000F#6PCecile, let me carry him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100693V#0300F#6PYeah, let's get back inside already.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_17E5 end

    def Function_14_1E57(): pass

    label("Function_14_1E57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32700.itc", 0x1E)
    LoadChrToIndex("chr/ch32900.itc", 0x1F)
    LoadChrToIndex("chr/ch29200.itc", 0x20)
    OP_68(14000, 8000, -3000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 14150, 7000, -3400, 270)
    SetChrPos(0x102, 14950, 7000, -1870, 270)
    SetChrPos(0x103, 14960, 7000, -3810, 270)
    SetChrPos(0x104, 15580, 7000, -4440, 270)
    SetChrPos(0x106, 16020, 7000, -2150, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 11700, 7000, -2950, 90)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 10800, 7000, -3500, 90)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 11700, 7000, -4050, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5100766V#0013FSo you haven't seen Doctor Guenter at all?\x01",
            "Anywhere?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#5100767V#6PHmm. By the time the mafia stormed the\x01",
            "research ward, I hadn't yet seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5100768V#5PA part of me wants to say that he probably\x01",
            "went night fishing, but I have no way of\x01",
            "knowing for certain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5100769V#0006F#11PIf only...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5100770V#0203F#11PI apologize, sir, but I highly doubt that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100771V#0106F#11PSo do I.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5100772V#0305F#11PHey, riddle me this. Where the hell did\x01",
            "those monsters in the research ward\x01",
            "come from?\x02\x03",
            "#5100773V#0301FDid the mafia bring them with their\x01",
            "war hounds or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5100774V#6PI have no earthly idea, actually. It was as\x01",
            "if they appeared out of nowhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5100775V#5PI didn't see them enter the building, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100776V#6POh... I might have something. When I saw\x01",
            "them in the hall, they had a man walking\x01",
            "among them. Quite fishy, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100777V#6PEspecially because he wasn't wearing\x01",
            "a black suit like the rest of the mafia.\x02",
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
        0x102,
        "#5100778V#0105F#11PDoes that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100779V#0201F#11PBy any chance, was he a balding fat\x01",
            "man, or did he resemble a bear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100780V#6PNo, nothing of the sort. He was rather\x01",
            "plain-looking, to tell the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100781V#6PThe last thing I saw was him taking\x01",
            "the elevator to the fourth floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5100782V#0001F#11PThat's where all the research labs\x01",
            "are, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100783V#0101F#11PWho would want to go there at a\x01",
            "time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5100784V#6PNo matter his identity, if you intend to\x01",
            "investigate, you'd best be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5100785V#5PIndeed. For the time being, we'll take\x01",
            "shelter in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5100786V#6PIf you find yourselves in a spot of trouble,\x01",
            "don't hesitate to come find us.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14000, 8000, -1000, 4000)

    def lambda_26D2():

        label("loc_26D2")

        TurnDirection(0x101, 0x14, 500)
        Yield()
        Jump("loc_26D2")

    QueueWorkItem2(0x101, 1, lambda_26D2)

    def lambda_26E4():

        label("loc_26E4")

        TurnDirection(0x102, 0x14, 500)
        Yield()
        Jump("loc_26E4")

    QueueWorkItem2(0x102, 1, lambda_26E4)

    def lambda_26F6():

        label("loc_26F6")

        TurnDirection(0x103, 0x14, 500)
        Yield()
        Jump("loc_26F6")

    QueueWorkItem2(0x103, 1, lambda_26F6)

    def lambda_2708():

        label("loc_2708")

        TurnDirection(0x104, 0x14, 500)
        Yield()
        Jump("loc_2708")

    QueueWorkItem2(0x104, 1, lambda_2708)

    def lambda_271A():

        label("loc_271A")

        TurnDirection(0x106, 0x14, 500)
        Yield()
        Jump("loc_271A")

    QueueWorkItem2(0x106, 1, lambda_271A)
    BeginChrThread(0x12, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x14, 3, 0, 15)
    OP_6F(0x1)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x106, 0x1)
    Fade(1000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_68(15800, 8000, -2380, 0)
    MoveCamera(65, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x106, 0x101, 500)

    ChrTalk(
        0x106,
        (
            "#5100787V\x07\x03",
            "#0700F#5PAn intruder able to command monsters, hmm?\x02\x03",
            "#5100788VDo you have any idea who it might be?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2838():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2838)
    Sleep(50)

    def lambda_2848():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2848)
    Sleep(50)

    def lambda_2858():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2858)
    Sleep(50)

    def lambda_2868():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2868)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        (
            "#5100789V#0006F#6PNo clue.\x02\x03",
            "#5100790V#0008FAll we know is that it doesn't seem to be\x01",
            "Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#5100791V#0303F#11PStill gotta catch 'em anyway, right?\x02\x03",
            "#5100792V#0301FC'mon, let's head up to the fourth floor.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#5100793V#0013F#6PLet's go!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, 14000, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE3, 2)
    OP_29(0x4D, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_1E57 end

    def Function_15_29CF(): pass

    label("Function_15_29CF")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_29DB():
        OP_97(0xFE, 0x0, 0x0, 0x36B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29DB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_29CF end

    def Function_16_29F5(): pass

    label("Function_16_29F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00501.itc", 0x1E)
    OP_68(550, 8500, 2390, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19370, 0)
    SetChrPos(0x101, 4880, 7000, 2680, 270)
    SetChrPos(0x102, 6660, 7000, 4040, 270)
    SetChrPos(0x103, 5810, 7000, 1720, 270)
    SetChrPos(0x104, 7430, 7000, 3180, 270)
    SetChrPos(0x106, 8189, 7000, 1130, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_68(4550, 8500, 2390, 4500)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#5101035V#0302F#11PLooks like we can leave the rest\x01",
            "to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5101036V#0106F#11PYes, but I don't think we can afford\x01",
            "to let our guard down just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5101037V#0208F#11PElie is correct.\x02\x03",
            "#5101038V#0201FWe cannot forget about the message\x01",
            "Ernest left us with, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101039V#0013F#11PYeah. First, let's rendezvous with the\x01",
            "deputy commander, then we'll hurry\x01",
            "back to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5101040V\x07\x03",
            "#0702F#11PThis is as far as our cooperation\x01",
            "extends, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(5890, 8500, 1050, 1500)
    SetCameraDistance(17440, 1500)

    def lambda_2CF9():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF9)

    def lambda_2D06():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D06)
    Sleep(100)

    def lambda_2D16():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D16)

    def lambda_2D23():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D23)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#5101041V\x07\x00",
            "#0001F#6PYou're leaving, Yin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#5101042V\x07\x03",
            "#0702F#11PHeh, it's not as if I hold any obligation\x01",
            "to accompany you any longer.\x02\x03",
            "#5101043VI have more than enough information\x01",
            "to report to Cao, and I also have\x01",
            "something I must protect.\x02\x03",
            "#5101044VJust the same as you do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5101045V#0005F#8PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5101046V#0105F#5PWhat needs your protection...?\x02",
    )

    CloseMessageWindow()
    OP_93(0x106, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x106,
        (
            "#5101047V\x07\x03",
            "#0700F#5PThat mystery will not be solved tonight.\x02\x03",
            "#5101048VHowever, the night is still young. You should\x01",
            "exercise caution, if you mean to press on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5101049V\x07\x00",
            "#0002F#6PDon't worry, we will. And, Yin...thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5101050V#0300F#5PYou're a hell of a lifesaver, man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5101051V#0202F#6PYou have our gratitude.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1614, 255, 100, 0)

    ChrTalk(
        0x106,
        (
            "#5101052V\x07\x03",
            "#0702F#5P#20AYes. Farewell.\x07\x00\x02",
        )
    )

    Sleep(2000)

    def lambda_3045():
        OP_95(0xFE, 9020, 7000, -5060, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3045)
    WaitChrThread(0x106, 1)
    Fade(500)
    OP_68(6470, 10000, -19480, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(13000, 3000)
    BeginChrThread(0x106, 3, 0, 17)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After their goodbye with Yin, the four police officers found\x01",
            "Sergeant Major Seeker and Deputy Commander Baelz, and\x01",
            "then gave them a brief rundown of the situation.\x02\x03",
            "It was agreed that the Special Support Section would be\x01",
            "given a ride back to Crossbell City in a CGF vehicle.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    OP_BA(0x5)
    RemoveParty(0x5, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_29F5 end

    def Function_17_322F(): pass

    label("Function_17_322F")

    SetChrPos(0xFE, 8350, 8000, -4940, 0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)

    def lambda_325D():
        OP_95(0xFE, 8350, 8000, -13940, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_325D)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    Sound(814, 0, 100, 0)

    def lambda_3297():
        OP_9D(0xFE, 0x209E, 0x1F40, 0xFFFFB9EC, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3297)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_32C2():
        OP_9D(0xFE, 0x209E, 0x0, 0xFFFF7478, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C2)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_17_322F end

    def Function_18_32FB(): pass

    label("Function_18_32FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3312")
    OP_A0(0xFE, 3000, 0x0, 0xFB)
    Jump("Function_18_32FB")

    label("loc_3312")

    Return()

    # Function_18_32FB end

    SaveToFile()

Try(main)
