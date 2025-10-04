from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3099.bin",                # FileName
        "m3099",                    # MapName
        "m3099",                    # Location
        0x00A3,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -100000, 0, -7000, 0, 0, 1, 163, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3099",                  # 0
        "High Priest Joachim",    # 1
        "Aguel Golem",            # 2
        "Aguel Golem",            # 3
        "Demon Joachim",          # 4
        "Renne",                  # 5
        "Dummy Joachim",          # 6
        "Pater-Mater",            # 7
        "杖",                     # 8
        "SE制御",                 # 9
        "bm3050",                 # 10
        "bm3060",                 # 11
        "bm3070",                 # 12
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_B4", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_C4", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 13, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 13, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_10C", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_110", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_124", 0x0042, 44, 6, 0, 0, 0, 0, 0, "bm3050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", "ms72600.dat", "ms72600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_C4", "MonsterBattlePostion_C4", "ed7404", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_168", 0x00DA, 45, 6, 0, 0, 0, 0, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", "ms69600.dat", "ms61600.dat", 0, 0, 0, 0, "ms70100.dat", "MonsterBattlePostion_E4", "MonsterBattlePostion_E4", "ed7406", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1AC", 0x00CA, 45, 6, 0, 0, 0, 0, 0, "bm3070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_104", "ed7406", "ed7403", "ATBonus_B4"),
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    484,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 3,   -45.5,                 -8.0,                  -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.166666984558105,    0.800000011920929,     0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_480",          # 01, 1
        "Function_2_4B8",          # 02, 2
        "Function_3_4ED",          # 03, 3
        "Function_4_506",          # 04, 4
        "Function_5_51C",          # 05, 5
        "Function_6_52F",          # 06, 6
        "Function_7_53F",          # 07, 7
        "Function_8_52F8",         # 08, 8
        "Function_9_5313",         # 09, 9
        "Function_10_992B",        # 0A, 10
        "Function_11_9AB4",        # 0B, 11
        "Function_12_9AE3",        # 0C, 12
        "Function_13_9B22",        # 0D, 13
        "Function_14_9B87",        # 0E, 14
        "Function_15_9BCA",        # 0F, 15
        "Function_16_9BE4",        # 10, 16
        "Function_17_B71C",        # 11, 17
        "Function_18_B75A",        # 12, 18
        "Function_19_B7AC",        # 13, 19
        "Function_20_B7EF",        # 14, 20
        "Function_21_B832",        # 15, 21
        "Function_22_B875",        # 16, 22
        "Function_23_B8B8",        # 17, 23
        "Function_24_B8FB",        # 18, 24
        "Function_25_B95C",        # 19, 25
        "Function_26_B9B8",        # 1A, 26
        "Function_27_BA14",        # 1B, 27
        "Function_28_BA70",        # 1C, 28
        "Function_29_BACC",        # 1D, 29
        "Function_30_BB28",        # 1E, 30
        "Function_31_BB4D",        # 1F, 31
        "Function_32_BB72",        # 20, 32
        "Function_33_E7E8",        # 21, 33
        "Function_34_E80D",        # 22, 34
        "Function_35_E858",        # 23, 35
        "Function_36_E880",        # 24, 36
        "Function_37_E929",        # 25, 37
        "Function_38_E963",        # 26, 38
        "Function_39_E997",        # 27, 39
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_464")

    label("loc_47F")

    Return()

    # Function_0_464 end

    def Function_1_480(): pass

    label("Function_1_480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_494")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_4B7")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_4A8")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_4B7")

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_4B7")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 6)

    label("loc_4B7")

    Return()

    # Function_1_480 end

    def Function_2_4B8(): pass

    label("Function_2_4B8")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0xFF, "broken0", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_4EC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4EC")

    Return()

    # Function_2_4B8 end

    def Function_3_4ED(): pass

    label("Function_3_4ED")

    Call(0, 7)
    Call(0, 9)
    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4ED end

    def Function_4_506(): pass

    label("Function_4_506")

    Call(0, 9)
    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_506 end

    def Function_5_51C(): pass

    label("Function_5_51C")

    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_51C end

    def Function_6_52F(): pass

    label("Function_6_52F")

    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_52F end

    def Function_7_53F(): pass

    label("Function_7_53F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("chr/ch09600.itc", 0x2A)
    LoadChrToIndex("chr/ch02000.itc", 0x2B)
    LoadChrToIndex("monster/ch72650.itc", 0x2C)
    LoadChrToIndex("monster/ch72650.itc", 0x2D)
    LoadChrToIndex("chr/ch02050.itc", 0x2E)
    LoadChrToIndex("chr/ch02054.itc", 0x2F)
    LoadChrToIndex("chr/ch02056.itc", 0x30)
    LoadChrToIndex("apl/ch50014.itc", 0x31)
    LoadChrToIndex("apl/ch50525.itc", 0x32)
    LoadChrToIndex("apl/ch50526.itc", 0x33)
    SoundLoad(861)
    OP_68(-41300, 3500, -8000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -41300, 0, -8000, 90)
    SetChrPos(0x102, -42400, 0, -7700, 90)
    SetChrPos(0x103, -42800, 0, -9100, 90)
    SetChrPos(0x104, -43900, 0, -8600, 90)
    SetChrPos(0x107, -43500, 0, -7000, 90)
    SetChrPos(0x108, -44700, 0, -7700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 28500, -66000, 2000, 180)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -3800, -1000, -10800, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -3800, -1000, -5200, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06700.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis104.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06800.itp")
    LoadEffect(0x0, "event\\ev618_00.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "event\\ev618_01.eff")
    LoadEffect(0x3, "event\\ev618_02.eff")
    LoadEffect(0x4, "event\\ev618_01.eff")

    def lambda_86D():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86D)
    Sleep(50)

    def lambda_88A():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88A)
    Sleep(50)

    def lambda_8A7():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8A7)
    Sleep(50)

    def lambda_8C4():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8C4)
    Sleep(50)

    def lambda_8E1():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8E1)
    Sleep(50)

    def lambda_8FE():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8FE)
    FadeToBright(1000, 0)
    OP_68(-15000, 500, -8000, 7000)
    MoveCamera(60, 34, 0, 7000)
    OP_6E(700, 7000)
    SetCameraDistance(55000, 7000)
    OP_6F(0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(-21300, 900, -8000, 0)
    MoveCamera(34, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    Sleep(1)
    SetCameraDistance(20500, 2000)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5300519V#6P#0013FWhat is this place...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x2D, 0x1F4)

    ChrTalk(
        0x102,
        "#5300520V#0108F#6PAn underground lake?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#5300521V#6P#0301FFeels like this ruin just gets bigger\x01",
            "and bigger...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5300522V#6P#0207FEveryone, over there...!\x02",
    )

    CloseMessageWindow()

    def lambda_AB4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB4)

    def lambda_AC1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_68(28000, 14000, -8000, 4000)
    MoveCamera(34, 30, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(26500, 4000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(27500, 14000, -8000, 0)
    MoveCamera(115, -10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    MoveCamera(65, -10, 0, 7000)
    SetCameraDistance(23000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xAAFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    ChrTalk(
        0x104,
        "#5300523V#0307F#2PThat's the thing in KeDo's photo!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300524V#0101F#2PSo we finally found where it was taken...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5300525V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "All I remember is a big, dark room...\x02\x03",
            "#5300526VA light shined down from above, but\x01",
            "it always made me a little scared.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5300527V#0003F#2PShe was trying to describe this place,\x01",
            "wasn't she?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19200, 7000, -10000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(300)
    Sound(1956, 255, 100, 0)
    Sleep(800)

    NpcTalk(
        0x8,
        "Man's Voice",
        "#5300528V#2PHaha... Indeed she was.\x02",
    )

    CloseMessageWindow()
    OP_68(19200, 8000, -10000, 2000)
    MoveCamera(90, 10, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    SetChrPos(0xD, 17800, 4000, -8000, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5300529V#0013F#11PJoachim Guenter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300530V#0801F#5PWh-When did you show up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300531V#0901F#5PThis guy is anything but ordinary.\x01",
            "That much is clear.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    OP_68(17800, 7500, -8000, 1500)
    MoveCamera(56, 10, 0, 1500)

    def lambda_E7A():
        OP_95(0xFE, 17800, 7000, -8000, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E7A)
    WaitChrThread(0x8, 1)
    OP_6F(0x41)
    OP_6B(0xD)

    def lambda_E9D():
        OP_95(0xFE, -2700, -5000, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E9D)

    def lambda_EB7():
        OP_95(0xFE, -2700, 0, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EB7)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 29, 4)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#5300532V\x07\x00",
            "#20A#20WWelcome...to the holy ground\x01",
            "of our origin.\x02\x03",
            "#5300533V#25ALadies and gentlemen from the\x01",
            "Special Support Section, as\x01",
            "well as the esteemed guests\x01",
            "from the Bracer Guild.\x02\x03",
            "#5300534V#20AI'm glad you could join me.\x02",
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
    SetChrPos(0x101, -19300, 0, -8000, 90)
    SetChrPos(0x102, -20400, 0, -7700, 90)
    SetChrPos(0x103, -20800, 0, -9100, 90)
    SetChrPos(0x104, -21900, 0, -8600, 90)
    SetChrPos(0x107, -20500, 0, -6000, 90)
    SetChrPos(0x108, -21700, 0, -6700, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Fade(1000)
    OP_6B(0xFF)
    OP_68(-6150, 1000, -7560, 0)
    MoveCamera(57, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    EndChrThread(0x8, 0x1)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, -8000, 270)

    def lambda_1144():
        OP_95(0xFE, -3000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1144)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_1168():
        OP_95(0xFE, -9500, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1168)
    Sleep(5)

    def lambda_1185():
        OP_96(0xFE, 0xFFFFD7C4, 0x0, 0xFFFFE570, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1185)
    Sleep(5)

    def lambda_11A2():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11A2)

    def lambda_11BC():
        OP_95(0xFE, -8500, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11BC)
    Sleep(5)

    def lambda_11D9():
        OP_96(0xFE, 0xFFFFD24C, 0x0, 0xFFFFDE04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11D9)

    def lambda_11F3():
        OP_95(0xFE, -10200, 0, -4700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_11F3)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x104, 1)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x107, 1)

    def lambda_122E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_122E)
    WaitChrThread(0x108, 1)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 70, 0)

    def lambda_124B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_124B)
    WaitChrThread(0x8, 1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5300535V#6P#0208F#N...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300536V#0101F#6PYou monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300537V#6P#0301FA laid-back one, at that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300538V#0013F#6P...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(-5700, 1000, -7320, 1000)

    def lambda_1317():
        OP_95(0xFE, -9200, 0, -8000, 800, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1317)
    WaitChrThread(0x101, 1)
    Sound(31, 0, 100, 0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#5300539V#0003F#6PJoachim Guenter. I'm going to\x01",
            "cut to the chase.\x02\x03",
            "#5300540V#0001FRelease everyone who's been\x01",
            "brainwashed by Gnosis. Now.\x02\x03",
            "#5300541VI don't know the science behind it,\x01",
            "but I know you're the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5300542V#6705F#11POf course. I wouldn't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300543V#0011F#6P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300544V#6704F#11PI told you at the IBC, didn't I?\x02\x03",
            "#5300545V#6714FHand over Lady KeA, and everything\x01",
            "will come to an end.\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#5300546V#0007F#6PDon't be stupid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300547V#0110F#6PStop with your crazy talk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300548V#0307F#6PLookin' for a fight, bastard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300549V#6P#0211F#NYou're the sickest criminal that has\x01",
            "ever had the misfortune of existing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300550V#0808F(This guy has the same messed-up personality as\x01",
            "the professor... I didn't think that was possible.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300551V#0906F(Even Weissmann wasn't this insane...)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300552V#6703F#11POh, what a shame. You're making this\x01",
            "conversation harder than it needs to be.\x02\x03",
            "#5300553VLady KeA has always been our humble\x01",
            "organization's Divine Child. Our love.\x02\x03",
            "#5300554V#6701FIs it so unreasonable that we would\x01",
            "want the object of our worship back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300555V#0010F#6PDo you think we aren't aware of\x01",
            "what happened six years ago?!\x02\x03",
            "#5300556VYou will never lay your hands\x01",
            "on that girl ever again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300557V#0107F#6PBetter yet, tell us everything you\x01",
            "know about KeA's identity!\x02\x03",
            "#5300558VYou know where she came from,\x01",
            "don't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300559V#6702F#11PHaha... How interesting.\x02\x03",
            "#5300560V#6704FYou're still clinging to the foolish\x01",
            "idea that Lady KeA was born in\x01",
            "this era...\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5300561V#0005F#6P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300562V#6P#0201F#NTh-This era...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300563V#6704F#11PVery well, then.\x02\x03",
            "#5300564V#6700FDivulging this information to people who\x01",
            "haven't achieved Wisdom would normally\x01",
            "be prohibited...\x02\x03",
            "#5300565V...but allow me to provide enlightenment\x01",
            "for you poor, lost souls.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(22000, 12000, -8000, 3000)
    MoveCamera(90, -10, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(23000, 3000)
    OP_93(0x8, 0x5A, 0x190)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5300566V#6704F#11PJust a month ago, Lady KeA was sleeping...\x02\x03",
            "#5300567V...in that cradle you see resting at the top\x01",
            "of the altar.\x02\x03",
            "#5300568V#6714FShe had been slumbering there for over\x01",
            "500 years!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#5300569V#0007F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300570V#0107FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300571V#0207FThat's not possible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300572V#0310FYou bastard... Cut the bullshit!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2900, 1000, -8000, 0)
    MoveCamera(33, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    Sleep(1)
    MoveCamera(65, 17, 0, 50000)
    SetCameraDistance(19500, 50000)
    OP_0D()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5300573V#6702F#11PSurely you can't be THAT surprised.\x02\x03",
            "#5300574V#6704FWhile modern technology cannot hope to\x01",
            "achieve such wonders, it's easily done with\x01",
            "the technology of the ancient civilization.\x02\x03",
            "#5300575VFive hundred years ago, there lived a group\x01",
            "of alchemists who gathered in this land with\x01",
            "the intent of studying artifacts.\x02\x03",
            "#5300576V#6700FRecords say that this very altar was built\x01",
            "using their powerful tools.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    AnonymousTalk(
        0x108,
        (
            "#5300577V#0901FThe same alchemists that constructed\x01",
            "Stargazer's Tower, I bet.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x107,
        (
            "#5300578V#0806FI-It's kinda crazy to think these connections\x01",
            "stretch back to such a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300579V#6704F#11PAs I said, Lady KeA had been in slumber\x01",
            "since those times...\x02\x03",
            "#5300580VBut of course, no one in our orders knows\x01",
            "of her origins.\x02\x03",
            "#5300581V#6700FThat is the truth.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        "#5300582V#0008FI can't believe this...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#5300583V#0306FWhat the hell, man...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#5300584V#0108FKeA's past... I thought, together, we'd be\x01",
            "able to help her find it...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#5300611V#0208F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300586V#6704F#11PHaha. Come, now, what's with all the\x01",
            "long faces?\x02\x03",
            "#5300587VLady KeA doesn't need a past...\x02\x03",
            "#5300588V#6713FBecause, after all, soon she will take\x01",
            "her rightful place as the True God!\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    AnonymousTalk(
        0x101,
        "#5300589V#0007F...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x107,
        "#5300590V#0801FG-God?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300591V#6714F#11PHahaha, you heard me!\x02\x03",
            "#5300592VDuring your journeys, you must have\x01",
            "realized the truth by now!\x02\x03",
            "#5300593VAidios, the Goddess of the Sky?!\x01",
            "There is no such thing!\x02\x03",
            "#5300594VWhy can't you understand that her\x01",
            "very existence is a fabrication\x01",
            "created by the Septian Church?!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        "#5300595V#0310FHave you lost your mind?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#5300596V#0101FI-I can't believe that there are people\x01",
            "who genuinely doubt the Goddess...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#5300597V#6702F#11PThis is the truth that D∴G faithfully\x01",
            "preaches.\x02\x03",
            "#5300598V#6704FHowever, we're often misunderstood...\x01",
            "You see, we don't worship the devils\x01",
            "at all. Quite the contrary, actually.\x02\x03",
            "#5300599VWe simply use them because they're\x01",
            "convenient in our fight in denying\x01",
            "the very concept of this 'goddess.'\x02\x03",
            "#5300600V#6700FFighting fire with fire, so to speak.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-10000, 1000, -9700, 0)
    MoveCamera(295, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x104, -11700, 0, -8300, 90)
    SetChrPos(0x103, -10000, 0, -9700, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    SetCameraDistance(14500, 500)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#5300601V#5P#0207F#4SY-You can't be serious!\x02",
    )

    CloseMessageWindow()
    OP_6F(0x10)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_27F3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27F3)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_2808():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2808)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_281D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_281D)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)

    def lambda_2832():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2832)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)

    def lambda_2847():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2847)
    Sound(808, 0, 80, 0)
    Sound(531, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#5300602V#5P#0208F#30WIf that's really the truth, what compelled\x01",
            "you to do all those horrible things to us...?!\x02\x03",
            "#5300603V#0210F#40WAll of them... Everywhere I looked, it was\x01",
            "nothing but screams and cries for help!\x02\x03",
            "#5300604VAnd I'm supposed to accept that the lodge\x01",
            "I was in was one of the luckier ones...?!\x02\x03",
            "#5300605VIf you aren't worshiping devils... Why...?!\x01",
            "Why did you do all those things?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300606V#11P#0008FTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300607V#11P#0308FTio Tot...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5700, 1000, -7320, 0)
    MoveCamera(57, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x104, -11700, 0, -8700, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5300608V#6702F#11PHaha... Tio Plato. I remember you well.\x02\x03",
            "#5300609V#6704FAn Altair Lodge test subject, whose\x01",
            "superb sensory receptivity was almost\x01",
            "miraculous...\x02\x03",
            "#5300610VLucky me, being able to meet such a\x01",
            "wonderful test subject like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300585V#6P#0208F#N...\x02",
    )

    CloseMessageWindow()

    def lambda_2BD6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BD6)
    Sleep(50)

    def lambda_2BE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BE6)
    Sleep(50)

    def lambda_2BF6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BF6)
    Sleep(50)

    def lambda_2C06():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2C06)
    Sleep(50)

    def lambda_2C16():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2C16)

    ChrTalk(
        0x101,
        (
            "#5300612V#0006F#6PI suppose now is as good a time to\x01",
            "ask as ever, since you're on the topic.\x02\x03",
            "#5300613V#0013FAnswer honestly. What was the goal\x01",
            "of those inhuman rituals that took\x01",
            "place all across the continent?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300614V#6705F#11PGoodness, you still haven't figured it out?\x02\x03",
            "#5300615V#6704FEvery ceremony served the greater purpose\x01",
            "of enhancing Gnosis toward its prime form.\x02\x03",
            "#5300616VThe willpower and hidden potential that\x01",
            "blossoms when one is brought to their\x01",
            "breaking point...\x02\x03",
            "#5300617V#6700FThat kind of data was a necessity if we\x01",
            "wanted to perfect Gnosis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300618V#0010F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300619V#6714F#11PThe reason we used children for our\x01",
            "tests was simply because it ensured\x01",
            "more accurate data.\x02\x03",
            "#5300620VYou see, test subjects that have yet to\x01",
            "reach puberty are, in various aspects--\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x103,
        "#5300621V#6P#0210F#N...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#5300622V#0007F#6PThat's enough!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300623V#0110F#6PHave you no shame?!\x01",
            "This cruelty is just...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300624V#3P#0311F#6PNever thought I'd meet someone\x01",
            "more screwed up than we were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x108, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x107)
    OP_64(0x108)
    Fade(500)
    OP_68(-8090, 900, -6540, 0)
    MoveCamera(270, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x107, -8000, 0, -4100, 135)
    SetChrPos(0x108, -9900, 0, -4500, 135)
    MoveCamera(280, 17, 0, 50000)
    SetCameraDistance(18000, 50000)

    def lambda_30D0():
        OP_96(0xFE, 0xFFFFDD3C, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_30D0)
    WaitChrThread(0x108, 1)
    Sleep(300)

    ChrTalk(
        0x108,
        (
            "#5300625V#0903F#11PJoachim Guenter.\x02\x03",
            "#5300626V#0901FBased on everything we've heard, you must\x01",
            "have been the person responsible for organizing\x01",
            "these experiments all over Zemuria, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x13B, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5300627V#6P#6702F#NHaha. Precisely.\x02\x03",
            "#5300628V#6704FHowever, my rank within the order\x01",
            "isn't something to brag about.\x02\x03",
            "#5300629VAfter all, we're all equals under\x01",
            "our True God...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300630V#0806F#11PTo be honest, I don't give a crap about\x01",
            "whatever your cult believes in.\x02\x03",
            "#5300631V#0808FBut, you must've known about that place.\x02\x03",
            "#5300632V#0801FOne of the cult's most infamous lodges:\x01",
            "Paradise.\x02",
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
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_33E5():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33E5)
    Sleep(50)

    def lambda_33F5():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33F5)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_340D():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_340D)
    Sleep(50)

    def lambda_341D():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_341D)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300633V#0005F#5PWe read that name earlier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300634V#5P#0101FIt was mentioned in the black file.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300635V#6P#6705F#NOh? You know of its existence, then?\x02\x03",
            "#5300636V#6704FThat particular lodge was formed by the high-\x01",
            "ranking officials of the order.\x02\x03",
            "#5300637VWhenever an influential figure visited Paradise\x01",
            "and exposed their ugliest weaknesses, they\x01",
            "became easy to bend to the order's will.\x02\x03",
            "#5300638V#6700FTruth be told, that lodge deviated from my\x01",
            "research principles, which I did not appreciate.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5300639V#0808F#11PSo it's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300640V#0908F#11PJust like we thought...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300641V#0003F#5PThat answers another one of my questions...\x02\x03",
            "#5300642V#0013FYou lured Speaker Hartmann to Paradise in order\x01",
            "to coerce him into helping the cult, didn't you?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_379B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_379B)

    def lambda_37A8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37A8)

    def lambda_37B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37B5)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#5300643V#11P#0107F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300644V#5P#0307FThere's our connection!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5300645V#6P#6702F#NI only began to truly understand what happened\x01",
            "there after I pored over the results of every\x01",
            "established lodge.\x02\x03",
            "#5300646V#6704FAfter that aggravating operation six years ago,\x01",
            "we nearly lost all of our precious lodges...\x02\x03",
            "#5300647VFortunately, we stumbled across the perfect\x01",
            "backer for our cause: Speaker Hartmann.\x02\x03",
            "#5300648V#6712FConveniently enough, he came with the nice\x01",
            "bonus of Revache & Co.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5300649V#0006F#5PEverything's falling into place now...\x02\x03",
            "#5300650V#0013FAnd you manipulated the Crossbell Guardian\x01",
            "Force through the same connection, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A6B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A6B)

    def lambda_3A78():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A78)

    def lambda_3A85():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A85)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#5300651V#11P#0108FHe must have...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300652V#5P#0301FHow'd you even get them to take\x01",
            "your crappy drug in the first place?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300653V#6P#6702F#NOh, that was simple. The CGF commander\x01",
            "is Speaker Hartmann's protege, so he\x01",
            "effectively dances in the palm of my hand.\x02\x03",
            "#5300654VAll I had to do was pass Gnosis off as a\x01",
            "new supplement developed at St. Ursula.\x02\x03",
            "#5300655V#6709FHow fast he believed me did come as a bit\x01",
            "of a shock, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#5300656V#0008F#5PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300657V#5P#0310FWhat a dumbass! How idiotic can one\x01",
            "guy get?!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5300658V#6P#6704F#NIf I can segue back to Paradise, there was\x01",
            "something about its demise that bugs me.\x02\x03",
            "#5300659VInstead of being ambushed by that operation,\x01",
            "it was decimated entirely by the society that\x01",
            "caused the Liberl incident last year...\x02\x03",
            "#5300660V#6700FOh, dear, just what were they thinking?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5300661V#0808F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300662V#0903F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300663V#6P#6703F#NWell, the destruction of Paradise only\x01",
            "left me with one genuine regret...\x02\x03",
            "#5300664VThat being the loss of a young subject\x01",
            "who demonstrated a remarkable level of\x01",
            "adaptability...\x02\x03",
            "#5300665V#6713FOh, she was simply a marvel!\x02\x03",
            "#5300666VThrough harnessing Gnosis, she could\x01",
            "absorb other failed subjects' personalities\x01",
            "and manifest them in her own mind!\x02\x03",
            "#5300667V#6709FIf only we could have recovered all of that\x01",
            "oh-so valuable data, but alas...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300668V#0803F#11PThat's enough.\x02\x03",
            "#5300669V#0801FWe have what we came for.\x01",
            "You can shut your disgusting\x01",
            "mouth now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300670V#0908F#11P...Sorry, Lloyd. I think we might\x01",
            "have cut your interrogation short.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300671V#0004F#5PIt's fine. Thanks to your help, I was able to\x01",
            "draw a lot of conclusions about the case.\x02\x03",
            "#5300672V#0000FI'm prepared to arrest him now--without\x01",
            "hesitation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Fade(500)
    OP_68(-7500, 1000, -8000, 0)
    MoveCamera(270, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -9700, 0, -8000, 90)

    def lambda_41F4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_41F4)
    SetCameraDistance(16000, 700)

    def lambda_420A():
        OP_95(0xFE, -9000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_420A)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(18, 0, 80, 0)
    OP_6F(0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)

    ChrTalk(
        0x101,
        (
            "#5300673V#0003F#5PHigh Priest Joachim Guenter of the D∴G cult...\x02\x03",
            "#5300674V#0007FAccording to Crossbell State law, you're hereby\x01",
            "under arrest on the charges of assault, incitement\x01",
            "of a riot, unlawful occupation of property,\x01",
            "misuse of drugs, and child abuse!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300675V#2P#0107F#11PTelling you is just a formality, but rest\x01",
            "assured the search and arrest warrant\x01",
            "have already been approved!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300676V#5P#0307FThe jig is up, buddy. Don't resist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300677V#6P#6704FHaha... How intriguing.\x02\x03",
            "#5300678V#6700FI have an idea. Why don't we make\x01",
            "a wager?\x02\x03",
            "#5300679VWhich of us will be the ones to\x01",
            "accomplish their goal...?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0xD, 0x32)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -3000, 0, -8000, 270)
    Sound(804, 0, 100, 0)

    def lambda_44E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_44E0)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3000, 2500, -8000, 0)
    SetChrFlags(0xF, 0x8000)

    def lambda_451E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_451E)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    Sound(1960, 255, 100, 0)
    Fade(500)
    OP_68(-3000, 1500, -8000, 0)
    MoveCamera(225, 40, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(968, 0, 100, 0)

    def lambda_460C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_460C)

    def lambda_461D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_461D)
    MoveCamera(90, 33, 0, 9000)
    SetCameraDistance(15000, 9000)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x3, 0xFF, 0xF, 0x40, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(969, 0, 100, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_468E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_468E)
    Sound(202, 0, 100, 0)
    OP_6F(0x79)

    def lambda_46A7():
        OP_96(0xFE, 0xFFFFF448, 0x5DC, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_46A7)
    WaitChrThread(0xF, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrPos(0x107, -8500, 0, -4100, 135)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x108, -10100, 0, -5100, 135)
    Sound(808, 0, 100, 0)
    OP_68(-3000, 300, -8000, 1500)
    MoveCamera(90, 14, 0, 1500)
    SetCameraDistance(22000, 1500)
    Sleep(1000)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)

    def lambda_47E5():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47E5)
    Sleep(10)

    def lambda_4802():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4802)
    Sleep(10)

    def lambda_481F():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_481F)

    def lambda_4839():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4839)
    Sleep(10)

    def lambda_4856():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4856)

    def lambda_4870():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4870)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x108, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        "#5300681V#0101F#6PH-His hair...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300682V#0201F#12PAnd some sort of orbal staff...?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 30, 3)

    AnonymousTalk(
        0x8,
        (
            "#5300683V\x07\x02",
            "This is my true hair color,\x01",
            "if you were curious...\x02\x03",
            "#5300684VAs a result of repeated Gnosis\x01",
            "consumption, my body has grown\x01",
            "somewhat...unordinary.\x02\x03",
            "#5300685VAs a result, I haven't been\x01",
            "able to get a wink of sleep\x01",
            "for the past several years.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    ChrTalk(
        0x104,
        (
            "#5300686V\x07\x00",
            "#0310F#12P#NSuits you, you sick son of a bitch.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5300687V#6P#0008FSo, that explains how you were able to\x01",
            "accomplish all of this while working\x01",
            "full-time at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300688V\x07\x02",
            "#6804F#5PHaha. Maybe you're a better detective\x01",
            "than I gave you credit for.\x02\x03",
            "#5300689V#6800FThis staff here is one of the orbal\x01",
            "masterpieces created by the ancient\x01",
            "alchemists of Crossbell.\x02\x03",
            "#5300690VIt's power even surpasses that of an\x01",
            "average artifact.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    PlayEffect(0x1, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    Sound(861, 2, 100, 0)
    BeginChrThread(0x8, 2, 0, 8)
    Sleep(500)
    Sound(1921, 255, 100, 0)
    Sleep(500)
    Fade(250)
    OP_68(-3490, 900, -7360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    MoveCamera(45, 30, 0, 3000)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -3800, 0, -10800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -3800, 0, -5200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    OP_24(0x35D)

    def lambda_4DCB():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFD5D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4DCB)

    def lambda_4DE5():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFEBB0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DE5)

    def lambda_4DFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4DFF)

    def lambda_4E10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4E10)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    EndChrThread(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5300692V\x07\x02",
            "#6813F#11PAnd it allows me to command these to my\x01",
            "every whim!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5300693V\x07\x00",
            "#0010FTch!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x107,
        "#5300694V#0807FNo way!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x108,
        (
            "#5300695V#0901FArchaisms from the Middle Ages,\x01",
            "created with the power of alchemy!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x1194)
    Fade(300)
    OP_68(-3000, 300, -8000, 0)
    MoveCamera(90, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x1)
    Sleep(600)
    Sound(1959, 255, 100, 0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(20500, 300)
    SetChrSubChip(0x8, 0x2)
    Sleep(80)
    SetChrSubChip(0x8, 0x3)
    Sound(808, 0, 100, 0)
    Sound(540, 0, 70, 0)
    Sleep(500)
    OP_6F(0x10)
    CancelBlur(0)

    ChrTalk(
        0x8,
        (
            "#5300697V\x07\x02",
            "#6804F#5PNow, I believe it's time for our finale to\x01",
            "get underway.\x02\x03",
            "#5300698VIf things go as planned, today will be the\x01",
            "greatest day the world has ever seen...\x02\x03",
            "#5300699V#6814FThe day when our desire to see Lady KeA\x01",
            "become God and take her throne is finally\x01",
            "realized!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7404", 0)

    ChrTalk(
        0x101,
        (
            "#5300700V\x07\x00",
            "#6P#0007FKeep dreaming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300701V#0207F#12PI will never lose to the likes of you!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 415)
    BlurSwitch(0x19F, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_5216():
        OP_95(0xFE, -2000, 0, -8000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5216)
    Sleep(5)

    def lambda_5233():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE4A8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5233)
    Sleep(5)

    def lambda_5250():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5250)

    def lambda_526A():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_526A)
    Sleep(5)

    def lambda_5287():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5287)

    def lambda_52A1():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_52A1)
    Sleep(400)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x35D)
    Battle("BattleInfo_124", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x108, 0x1)
    Return()

    # Function_7_53F end

    def Function_8_52F8(): pass

    label("Function_8_52F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5312")
    OP_A1(0x8, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_8_52F8")

    label("loc_5312")

    Return()

    # Function_8_52F8 end

    def Function_9_5313(): pass

    label("Function_9_5313")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("chr/ch02053.itc", 0x2A)
    LoadChrToIndex("chr/ch02050.itc", 0x2B)
    LoadChrToIndex("chr/ch02054.itc", 0x2C)
    LoadChrToIndex("chr/ch02000.itc", 0x2D)
    LoadChrToIndex("chr/ch00053.itc", 0x2E)
    LoadChrToIndex("chr/ch00153.itc", 0x2F)
    LoadChrToIndex("chr/ch00253.itc", 0x30)
    LoadChrToIndex("chr/ch00353.itc", 0x31)
    LoadChrToIndex("chr/ch00653.itc", 0x32)
    LoadChrToIndex("chr/ch00753.itc", 0x33)
    LoadChrToIndex("chr/ch00056.itc", 0x34)
    LoadChrToIndex("chr/ch00156.itc", 0x35)
    LoadChrToIndex("chr/ch00256.itc", 0x36)
    LoadChrToIndex("chr/ch00356.itc", 0x37)
    LoadChrToIndex("chr/ch00059.itc", 0x3A)
    LoadChrToIndex("chr/ch00054.itc", 0x3B)
    LoadChrToIndex("monster/ch72050.itc", 0x3C)
    LoadChrToIndex("apl/ch50526.itc", 0x3D)
    LoadChrToIndex("apl/ch50527.itc", 0x3E)
    LoadChrToIndex("apl/ch50528.itc", 0x3F)
    SoundLoad(861)
    SoundLoad(971)
    SoundLoad(930)
    OP_68(-6100, 1000, -8000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x101, -9500, 0, -8000, 90)
    SetChrPos(0x102, -10300, 0, -6600, 90)
    SetChrPos(0x103, -10800, 0, -10400, 90)
    SetChrPos(0x104, -11500, 0, -8900, 90)
    SetChrPos(0x107, -8500, 0, -4400, 135)
    SetChrPos(0x108, -10200, 0, -4700, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, -3000, 0, -8000, 270)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x3D)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3500, 500, -6700, 0)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0xB)
    OP_49()
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x2, 0xF)
    OP_70(0x2, 0xA)
    OP_CA(0x1, 0xFF, 0x0)
    OP_49()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis112.itp")
    LoadEffect(0x0, "event\\ev611_01.eff")
    LoadEffect(0x1, "event\\ev611_02.eff")
    LoadEffect(0x2, "event\\ev602_01.eff")
    LoadEffect(0x3, "event\\ev602_02.eff")
    LoadEffect(0x4, "event\\ev612_00.eff")
    LoadEffect(0x5, "event\\ev611_00.eff")
    LoadEffect(0x6, "event\\ev607_00.eff")
    LoadEffect(0x7, "battle\\mgaria0.eff")
    SetCameraDistance(18500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5300702V#0007F#6PYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300703V#3P#0300FHaha! Looks like we won the bet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300704V#0107F#6PThrow aside your weapon and get on the ground!\x02",
    )

    CloseMessageWindow()

    def lambda_5711():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5711)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x8,
        (
            "#5300705V\x07\x02",
            "#6804F#11P#40WHaha... I'll have to decline.\x02\x03",
            "#5300706V#6802FThere's something you should know.\x02\x03",
            "#5300707VGnosis doesn't just enhance the user's\x01",
            "physical strength and capabilities...\x02\x03",
            "#5300708VIt also heightens their sensory receptivity,\x01",
            "unlocking humanity's true, hidden potential.\x02\x03",
            "#5300709V#6814FWhen used correctly...anything can be achieved!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5898():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5898)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(80)
    SetChrSubChip(0x8, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(80)
    Fade(250)
    OP_68(-3200, 1000, -8000, 0)
    MoveCamera(91, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(20000, 2000)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 2, 0, 8)
    OP_0D()
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(506, 0, 90, 0)
    Sound(565, 0, 90, 0)
    Sleep(2000)
    PlayEffect(0x5, 0x1, 0x8, 0x0, -2500, 3200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(970, 0, 100, 0)
    Sleep(1200)
    Sound(972, 0, 100, 0)
    Sleep(700)
    PlayEffect(0x0, 0x2, 0x101, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x102, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x103, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x104, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0x107, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0x108, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(969, 0, 100, 0)
    Sound(971, 2, 100, 0)
    Sound(1030, 255, 100, 0)
    Sound(1128, 255, 100, 1)
    Sound(1223, 255, 100, 2)
    Sound(1317, 255, 100, 3)
    Sound(1670, 255, 100, 4)
    Sound(1739, 255, 100, 5)
    OP_82(0xC8, 0xC8, 0x3E8, 0x3E8)
    Fade(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2E)
    BeginChrThread(0x101, 3, 0, 11)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x102, 0x2F)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x30)
    BeginChrThread(0x103, 3, 0, 11)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x104, 0x31)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x107, 0x32)
    BeginChrThread(0x107, 3, 0, 11)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x108, 0x33)
    BeginChrThread(0x108, 3, 0, 11)
    OP_0D()
    StopEffect(0x1, 0x2)
    Sleep(1500)

    def lambda_5C3F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C3F)

    ChrTalk(
        0x101,
        (
            "#5300834V\x07\x00",
            "#0010FWhat?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C75():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5C75)

    ChrTalk(
        0x104,
        "#5300711V#11P#0307FThe hell is this?!\x02",
    )

    CloseMessageWindow()

    def lambda_5CB9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5CB9)

    ChrTalk(
        0x103,
        (
            "#5300712V#11P#0208FO-Our movement has been sealed?!\x01",
            "But how?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D15():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5D15)

    ChrTalk(
        0x107,
        "#5300713V#0813F#5PThis is just like...Weissman's Evil Eye!\x02",
    )

    CloseMessageWindow()

    def lambda_5D6E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_5D6E)

    ChrTalk(
        0x108,
        "#5300714V#0907F#5PThat should be impossible!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(18000, 60000)
    StopEffect(0x0, 0x2)
    OP_24(0x35D)
    Fade(250)
    EndChrThread(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#5300715V\x07\x02",
            "#6802F#5PThe two of you have had quite the adventure\x01",
            "over the last two years, haven't you?\x02\x03",
            "#5300716V#6804FThe Liber Ark and...Phantasma, was it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5EB8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5EB8)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x107, 0x2)
    OP_0D()

    ChrTalk(
        0x107,
        (
            "#5300717V#0807F#6P#NHow does he know that?! It's like he's\x01",
            "looking into our memories!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F39():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_5F39)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x108, 0x2)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#5300718V#0907F#6P#NNo way... Is he using them to recreate\x01",
            "Evil Eye?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300719V\x07\x02",
            "#6805F#5PWeissmann... Heh. From the looks of it,\x01",
            "him and I would have gotten along quite\x01",
            "well.\x02\x03",
            "#5300720V#6800FHow interesting. I wasn't expecting this\x01",
            "amount of intel on Ouroboros...\x02\x03",
            "#5300721V#6809FHaha. I think that's enough on them to\x01",
            "keep me entertained for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300722V#0901F#6P#N...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5300723V#0801F#6P#NUgh, I can't believe this...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300724V\x07\x02",
            "#6804F#5PIt would seem I'm the victor of our\x01",
            "bet, after all.\x02\x03",
            "#5300725V#6800FI know. How about a serving of Gnosis\x01",
            "for each and every one of you?\x02\x03",
            "#5300726VSoon, you'll be slaving away for a\x01",
            "greater cause.\x02\x03",
            "#5300727VAnd Lady KeA will have no choice but\x01",
            "to return to my arms.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_62DC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62DC)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x37)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#5300728V\x07\x00",
            "#0310F#12P#NYou bastard...!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6332():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6332)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#5300729V#0110F#6P#NS-So that's why you wanted to lure\x01",
            "us here! Just to use us!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300730V\x07\x02",
            "#6804F#5PWell, what other use would imbeciles\x01",
            "like you have for me?\x02\x03",
            "#5300731V#6814FEverything I've done has been for\x01",
            "Lady KeA's safe return...\x02\x03",
            "#5300732VWhat better reason is there?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_647A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_647A)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x103, 0x36)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#5300733V\x07\x00",
            "#6P#0201F#12P#NY-You monster...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    def lambda_64EC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64EC)
    Fade(250)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300734V#0006F#6P#NIf you already have this much power...\x02\x03",
            "#5300735V#0008F...why are you so obsessed with KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5300736V\x07\x02",
            "#6805F#5POh?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6100, 1000, -8000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(33, 15, 0, 85000)
    SetCameraDistance(20000, 85000)
    OP_0D()

    def lambda_6605():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6605)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5300737V\x07\x00",
            "#0003F#6P#NEven if she was born 500 years ago,\x01",
            "just as you say...\x02\x03",
            "#5300738V...that doesn't change the fact that\x01",
            "she's an ordinary little girl, does it?\x02\x03",
            "#5300739V#0001FWhat does someone with so much\x01",
            "power want with a girl like KeA?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300740V#0108F#6P#N...That's right.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300741V#0908F#6P#NGood question...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300742V\x07\x02",
            "#6813F#11PDid I not answer that question already?\x01",
            "Lady KeA is destined to become God.\x02\x03",
            "#5300743VComparing my power to that of Lady\x01",
            "KeA's is quite ignorant.\x02\x03",
            "#5300744V#6809FNo, rather... Should I perhaps say the\x01",
            "comparison in and of itself doesn't\x01",
            "make much sense...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300745V#0310F#6P#NStop talkin' in riddles, jackass.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300746V#0806F#6P#NGeez, it's like Weissmann had a\x01",
            "twin that we didn't know about...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5300747V#0003F#6P#NFine. Then answer me this instead.\x02\x03",
            "#5300748V#0001FWhat led to KeA being moved to the\x01",
            "Schwarze Auction?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5300749V\x07\x02",
            "#6801F#11P...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300750V\x07\x00",
            "#0108F#6P#NThat's definitely a loose string...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#5300751V#6P#0201F#6P#NThe mafia didn't seem to be aware\x01",
            "of her existence, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5300752V#0006F#6P#NActually, I'll keep the questions rolling.\x02\x03",
            "#5300753V#0013FWere you the one who killed my brother,\x01",
            "Guy Bannings?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5300754V\x07\x02",
            "#6805F#11POh, that's it! It all makes sense now!\x02\x03",
            "#5300755V#6800FTwo brothers, ten years apart in age...\x02\x03",
            "#5300756VAfter the older brother fell in the line of\x01",
            "duty, the younger left Crossbell, only to\x01",
            "return years later...\x02\x03",
            "#5300757V#6809FHaha! What an amazing development!\x02\x03",
            "#5300758VI had no idea that you were the little\x01",
            "brother of that nuisance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300759V\x07\x00",
            "#0001F#6P#N...Can I take that as a 'yes,' then?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300760V\x07\x02",
            "#6804F#11PI'll admit, he came close to uncovering\x01",
            "my true identity during his investigation.\x02\x03",
            "#5300761V#6800FGuy Bannings was such a distraction,\x01",
            "I had no choice but to ask Revache to\x01",
            "silence him...permanently.\x02\x03",
            "#5300762VBut some other faction killed our poor\x01",
            "detective before Revache could.\x02\x03",
            "#5300763V#6804FThree years ago, Marconi tried to spin\x01",
            "the story like they did it, bragging about\x01",
            "how much I owed him...\x02\x03",
            "#5300764V...but Garcia denied everything, which made\x01",
            "me hesitant to believe Revache killed him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300765V\x07\x00",
            "#0004F#6P#NThat's exactly what I thought, too.\x02\x03",
            "#5300766V#0000FBecause I know my brother would have\x01",
            "never lost to the likes of you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x8,
        (
            "#5300767V\x07\x02",
            "#6801F#11P...!\x02\x03",
            "#5300768V#6800FOh? What a bold claim to make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300769V\x07\x00",
            "#0003F#6P#NI think I know your answer to how\x01",
            "KeA came to be at the auction.\x02\x03",
            "#5300770VIt's because something, somewhere,\x01",
            "didn't go according to your plan.\x02\x03",
            "#5300771V#0001FThere's no way you'd lose sight of\x01",
            "your 'God' willingly...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300772V#0101F#6P#NI have to agree...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#5300773V#6P#0203F#6P#NIt would be illogical.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300774V\x07\x02",
            "#6811F#11PTch...\x02\x03",
            "#5300775VIt's true that, on that day, Lady KeA\x01",
            "finally awoke from her long slumber...\x02\x03",
            "#5300776V#6803FHowever, by the time I became aware\x01",
            "of it, she was nowhere to be seen.\x02\x03",
            "#5300777VInitially, I thought she might have lost\x01",
            "her way and wandered to the surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300778V\x07\x00",
            "#0005F#6P#NAnd accidentally got herself locked in that trunk,\x01",
            "instead of the doll that was meant for the auction?\x02\x03",
            "#5300779V#0006FThat's ridiculous. You and I both know that never\x01",
            "would have happened.\x02\x03",
            "#5300780VThere's also the intel sent to Heiyue to consider.\x02\x03",
            "#5300781V#0001FIn other words, while you may be the mastermind\x01",
            "pulling the strings behind this case, you somehow\x01",
            "managed to misplace a few.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300782V\x07\x02",
            "#6811F#11PArgh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300783V\x07\x00",
            "#0309F#6P#NHaha, nice kick to the balls!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5300784V#0802F#6P#NAmazing work, Lloyd!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300785V#0902F#6P#NSome things are just better suited for a detective.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300786V\x07\x02",
            "#6807F#11PWh-What's your point?!\x02\x03",
            "#5300787VAs soon as Lady KeA returns to me,\x01",
            "none of these questions will matter...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-3200, 1000, -8000, 0)
    MoveCamera(91, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(16500, 30000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5300788V\x07\x00",
            "#0002F#6P#NThen what about Gnosis? Come on, your jokes\x01",
            "have to end somewhere.\x02\x03",
            "#5300789V#0003FRight now, all you're doing is peering\x01",
            "into people, stealing their memories,\x01",
            "and mimicking what you see.\x02\x03",
            "#5300790VIt's the same thing with your despicable\x01",
            "experiments...\x02\x03",
            "#5300791V#0008FThe results have been nothing more than\x01",
            "accidents generated through trial and error,\x01",
            "all while torturing innocent children...\x02\x03",
            "#5300792V#0013FTell me, where's the 'wisdom' in that?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300793V\x07\x02",
            "#6811F#5PC-Curse you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300794V\x07\x00",
            "#0101F#6P#NClaiming it as wisdom is a disgrace to\x01",
            "the word itself.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#5300795V#6P#0211F#12P#N'Vile' might be a better description\x01",
            "of the acts you've committed.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300796V#0806F#6P#NPunch me in the face, Joshua, 'cause I think\x01",
            "Weissmann might have had better morals\x01",
            "than this piece of work.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300797V#0903F#6P#NYeah... I feel the same.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    LoadEffect(0x5, "event\\ev621_00.eff")
    LoadEffect(0x6, "event\\ev619_00.eff")
    LoadEffect(0x7, "event\\ev610_00.eff")
    Fade(500)
    OP_68(-9600, 700, -8000, 0)
    MoveCamera(310, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrSubChip(0x107, 0x3)
    SetChrPos(0x108, -10000, 0, -4700, 135)
    SetChrSubChip(0x108, 0x3)
    SetChrPos(0x102, -10300, 0, -6300, 90)
    SetChrPos(0x8, -3500, 0, -8000, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MoveCamera(310, 19, 5, 6500)
    SetCameraDistance(16000, 6500)
    OP_0D()
    PlayEffect(0x7, 0x1, 0x101, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)

    def lambda_7A20():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A20)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5300798V#5P#0008FAnd even now...\x02\x03",
            "#5300799VYou're trying to force your worthless\x01",
            "delusions onto KeA.\x02\x03",
            "#5300800V#0003FA girl as bright as sunshine itself,\x01",
            "the light of our lives...\x02\x03",
            "#5300801V#0010FShe's grown more precious to us\x01",
            "than you'd ever know.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    PlayEffect(0x4, 0xFF, 0x101, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(506, 0, 90, 0)
    Sound(565, 0, 90, 0)
    Sleep(2000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x3A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x3A)
    SetChrSubChip(0x101, 0x1)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x8, 3, 0, 10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7533", 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5300802V#5P#0007F#4SAnd there's no way in hell we'll let\x01",
            "your insanity reach her again!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x8, 3)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5300803V\x07\x02",
            "#11P#6810FI-Impossible!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CF6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7CF6)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#5300804V\x07\x00",
            "#0205F#5P...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D43():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7D43)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#5300805V#5P#0302FWe can move?!\x02",
    )

    CloseMessageWindow()

    def lambda_7D98():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7D98)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#5300806V#5P#0102FThe seal is gone!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7DF4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_7DF4)
    Sleep(100)

    def lambda_7E10():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7E10)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(540, 0, 80, 0)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x108,
        (
            "#5300807V#5P#0904FIn the end, his Evil Eye was nothing more\x01",
            "than a pale imitation of the real thing...\x02\x03",
            "#5300808V#0900FAs soon as he loses focus, he falters.\x01",
            "His mastery of it was far from perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300809V#11P#0809FAnd Lloyd's burning spirit was enough\x01",
            "to smash it to pieces!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-6640, 1000, -7610, 1000)
    MoveCamera(305, 15, 0, 1000)
    SetCameraDistance(17000, 1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x3B)
    SetChrSubChip(0x101, 0x4)
    Sound(808, 0, 90, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5300810V#5P#0013FWe've seen through every masquerade\x01",
            "you've set for us, Joachim Guenter.\x02\x03",
            "#5300811VNo matter what you may have up your\x01",
            "sleeve, nothing is going to stop us.\x02\x03",
            "#5300812V#0007FSurrender now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_808D():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_808D)
    WaitChrThread(0x8, 2)
    Sleep(600)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Sleep(300)

    def lambda_80C8():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE5D4, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_80C8)

    def lambda_80E5():
        OP_96(0xFE, 0xFFFFF510, 0x0, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_80E5)
    Sound(974, 0, 100, 0)
    WaitChrThread(0xF, 1)

    def lambda_8109():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE7C8, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_8109)
    WaitChrThread(0x8, 1)
    Sleep(300)

    def lambda_812D():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_812D)
    WaitChrThread(0x8, 2)
    Sleep(600)

    ChrTalk(
        0x8,
        (
            "#5300813V\x07\x02",
            "#11P#6803F#40WHaha...\x02\x03",
            "#5300814V#2S#50WI suppose...you leave me no choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300815V\x07\x00",
            "#5P#0001F...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300816V#5P#0307FHey, speak up, asshole!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5300817V\x07\x02",
            "#11P#6814F#4SHahaha! I didn't think I'd be forced to\x01",
            "use my trump card, but here we are!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2500, 300, -8000, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -3000, 0, -8000, 270)
    SetChrPos(0x101, -9600, 0, -8000, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -10300, 0, -6600, 90)
    SetChrPos(0x103, -10800, 0, -10400, 90)
    SetChrPos(0x104, -11500, 0, -8900, 90)
    SetChrPos(0x107, -9500, 0, -4100, 135)
    SetChrPos(0x108, -11100, 0, -5100, 135)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    SetCameraDistance(21000, 1000)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x3E)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(975, 0, 100, 0)
    OP_6F(0x10)
    CancelBlur(0)
    Sleep(500)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5300818V\x07\x00",
            "#0007F#6P#N...?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300819V#0107F#6P#NThat can't be...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x320)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#5300820V\x07\x02",
            "#6813FAllow me to enlighten you once more.\x02\x03",
            "#5300821VWhat you see here is perfected Gnosis.\x01",
            "My life's work, you could say.\x02\x03",
            "#5300822VIf we call the drugs you found 'blue Gnosis'...\x02\x03",
            "#5300823V...then the only appropriate name for this is\x01",
            "'red Gnosis,' right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x103,
        (
            "#5300824V\x07\x00",
            "#0201F#12P#NDoes he mean to...?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#5300825V#0307F#12P#NIt's the ones that turned the mafia\x01",
            "and Ernest into monsters!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1959, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5300826V\x07\x02",
            "#5P#6809F#4SHahaha! Right you are!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x3F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(975, 0, 100, 0)
    OP_0D()
    Sleep(500)
    StopBGM(0x1F40)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5300827V\x07\x00",
            "#0010F#6P#NDon't...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300828V#0907F#6P#NThat's too big a dosage!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x10, 2, 0, 15)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)

    def lambda_87BB():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_87BB)
    Sleep(300)
    OP_68(-2050, 300, -8000, 1500)

    def lambda_87E8():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_87E8)
    WaitChrThread(0x8, 1)

    def lambda_8806():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8806)
    Sleep(300)

    def lambda_8822():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8822)
    WaitChrThread(0x8, 1)

    def lambda_8840():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8840)

    ChrTalk(
        0x103,
        "#5300829V#0207F#12P#NHe'll overdose!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300830V#0807F#6P#NC-C'mon, we have to make him spit\x01",
            "them out!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E5()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(1000, 300, -8000, 5000)
    MoveCamera(90, 13, 0, 5000)
    SetCameraDistance(19000, 5000)

    ChrTalk(
        0x8,
        (
            "#5300831V\x07\x02",
            "#11P#6805F#45AI-I see it! It's right there!\x02\x03",
            "#5300832V#6814F#65AThe almighty D... The origin of lost power!\x02",
        )
    )

    OP_6F(0x79)
    Fade(500)
    OP_68(-2000, 900, -8000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_EE(0x0, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x3C)
    SetChrSubChip(0x8, 0x0)
    CancelBlur(0)
    OP_68(-2000, 1500, -8000, 8000)
    MoveCamera(50, 13, 10, 8000)
    SetCameraDistance(10500, 8000)
    Sleep(1000)
    Sleep(120)
    SetChrSubChip(0x8, 0x1)
    Sleep(120)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x101, 3, 0, 13)
    Sound(868, 0, 100, 0)
    Sound(930, 2, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(1961, 255, 100, 0)
    PlayEffect(0x2, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x8,
        (
            "#5300833V\x07\x02",
            "#11P#5S#35AHAHAHAHAHAHAHAHAHA!\x02",
        )
    )

    BlurSwitch(0x1194, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1500)

    def lambda_8AA6():
        OP_A6(0xFE, 0x0, 0x32, 0x1770, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8AA6)
    Sleep(1000)
    Sound(976, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(150)
    SetChrSubChip(0x8, 0x4)
    Sleep(150)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(150)
    SetChrSubChip(0x8, 0x7)
    Sleep(150)
    SetChrSubChip(0x8, 0x8)
    Sleep(150)
    SetChrSubChip(0x8, 0x9)
    Sleep(150)
    SetChrSubChip(0x8, 0xA)
    Sleep(150)
    SetChrSubChip(0x8, 0xB)
    Sleep(150)
    SetChrSubChip(0x8, 0xC)
    Sleep(150)
    SetChrSubChip(0x8, 0xD)
    Sleep(150)
    SetChrSubChip(0x8, 0xE)
    Sleep(150)
    PlayEffect(0x6, 0x1, 0x8, 0x40, 0, 100, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x8, 0xF)
    Sleep(150)
    SetChrSubChip(0x8, 0x10)
    Sleep(150)
    SetChrSubChip(0x8, 0x11)
    Sleep(150)
    SetChrSubChip(0x8, 0x12)
    Sleep(150)
    SetChrSubChip(0x8, 0x13)
    Sleep(150)
    SetChrSubChip(0x8, 0x14)
    Sleep(150)
    SetChrSubChip(0x8, 0x15)
    Sleep(150)
    SetChrSubChip(0x8, 0x16)
    Sleep(150)
    SetChrSubChip(0x8, 0x17)
    Sleep(150)
    FadeToDark(1500, 16777215, -1)
    Sound(937, 0, 100, 0)
    SetChrSubChip(0x8, 0x18)
    Sleep(150)
    SetChrSubChip(0x8, 0x19)
    Sleep(150)
    SetChrSubChip(0x8, 0x1A)
    Sleep(150)
    SetChrSubChip(0x8, 0x1B)
    Sleep(150)
    SetChrSubChip(0x8, 0x1C)
    Sleep(150)
    SetChrSubChip(0x8, 0x1D)
    Sleep(150)
    SetChrSubChip(0x8, 0x1E)
    PlayEffect(0x3, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1F)
    OP_0D()
    EndChrThread(0x8, 0x3)
    EndChrThread(0x101, 0x3)
    Sleep(1000)
    BeginChrThread(0x10, 1, 0, 14)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x108, 0x8)
    SetChrPos(0xB, -2000, 0, -8000, 0)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0xA)
    OP_71(0x2, 0x41A, 0x42E, 0x0, 0x20)
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    CancelBlur(0)
    OP_68(-3000, 3100, -8000, 0)
    MoveCamera(270, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(6000, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3000, 2100, -8000, 5000)
    FadeToBright(2000, 16777215)
    OP_6F(0x1)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3700, 1300, -8000, 0)
    MoveCamera(180, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(5500, 0)
    OP_68(-3700, 2300, -8000, 5000)
    OP_6F(0x1)
    Sleep(500)
    EndChrThread(0x10, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7406", 0)
    Fade(1000)
    Sound(976, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3700, 2500, -8000, 0)
    MoveCamera(55, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7000, 0)
    MoveCamera(65, -13, 0, 5000)
    SetCameraDistance(10000, 5000)
    OP_74(0x2, 0xF)
    ClearMapObjFlags(0x2, 0x20)
    OP_71(0x2, 0x334, 0x384, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0xA, 0x31, 0x0, 0x20)
    OP_6F(0x50)
    Sleep(500)
    EndChrThread(0x10, 0x1)
    Fade(1000)
    Sound(977, 0, 90, 0)
    Sound(978, 0, 100, 0)
    OP_24(0x35D)
    OP_68(-3000, 3000, -8000, 0)
    MoveCamera(90, -10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(5500, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 2000)
    OP_6F(0x10)
    Sleep(1500)
    CancelBlur(0)
    OP_E6()

    ChrTalk(
        0x101,
        "#5300710V#0011F#6P#NWhat?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300835V#0105F#6P#NDid he...?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#5300836V#0305F#12P#NYou can't be serious...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#5300837V#0207F#12P#NTh-This intense pressure...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5300838V#0813F#N#6PJ-Joshua, do you think...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#5300839V#0903F#N#6PDefinitely.\x02\x03",
            "#5300840V#0901FThis might be worse than Weissmann\x01",
            "fused with the Sept-Terrion...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6000, 1500, -8000, 0)
    MoveCamera(295, 31, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x108, 0x8)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sleep(1)
    MoveCamera(245, 31, 0, 30000)
    SetCameraDistance(18000, 30000)
    OP_0D()
    Sleep(1000)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5300841V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WAAAAH... HOW REFRESHING...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300842V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WI FEEL IT... I HAVE REACHED THE TRUTH\x01",
            "OF EVERYTHING...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300843V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WI CAN SEE THE STATE OF THE WORLD...\x01",
            "AND THE HIDDEN DESIGNS BEHIND IT...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_C7(0x1, 0x800)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300844V\x07\x00",
            "#0010F#N#5PDamn it... Get a hold of yourself!\x02\x03",
            "#5300845V#0007FYou're spewing nothing but lies!\x01",
            "Truth isn't something you can\x01",
            "seize just like that!\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5300846V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WHAHA. ONLY HUMANITY IS BOUND\x01",
            "TO SUCH TRIVIAL IDEALS.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300847V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WI CAN SEE EVERYTHING.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300848V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTHE TRUTH BEHIND LADY KEA'S DISAPPEARANCE,\x01",
            "THE TRUTH BEHIND YOUR BROTHER'S MURDER...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300849V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W...AND THE INEVITABLE FATE OF CROSSBELL.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300850V\x07\x00",
            "#0010F#5P#NTch...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#5300851V#0307FStop makin' shit up!\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5300852V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WTHERE REMAINS NO REASON TO ALLOW YOU\x01",
            "INSECTS TO LIVE ANY LONGER...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#5300853V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60WNOW, LAMENT OVER YOUR FRAGILE EXISTENCE\x01",
            "...AND DIE BEFORE ME!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(300)
    Fade(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-4010, 2300, -7660, 0)
    MoveCamera(90, -2, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(14000, 2000)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1750)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    CancelBlur(0)
    SetCameraDistance(13000, 20000)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#5300854V\x07\x00",
            "#0206F#12P#NHis demonization is nothing like Ernest's.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#5300855V#0303F#12P#NYup, that moron was just a little baby\x01",
            "compared to this monster...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#5300856V#0101F#6P#NThere's nothing we can do but\x01",
            "stand our ground and fight.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5300857V#0003F#6P#NYeah. Get ready.\x02\x03",
            "#5300858V#0013FElie, Tio, Randy...\x02\x03",
            "#5302001VEstelle, Joshua...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x101,
        (
            "#5300859V#0007F#6P#NThis is it: our last stand.\x01",
            "Don't give up, no matter what!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Everyone")
    Sound(1153, 255, 100, 0)
    Sound(1249, 255, 100, 1)
    Sound(1343, 255, 100, 2)
    Sound(1689, 255, 100, 3)
    Sound(1759, 255, 100, 4)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    AnonymousTalk(
        0xFF,
        (
            "#5300860V\x07\x00",
            "#5SRight!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(13000, 1000)
    Sleep(300)
    Sound(979, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xC)
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x35D)
    OP_24(0x3CB)
    OP_24(0x3A2)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_168", 0x30200010, 0x0, 0x4, 0xA, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1388)
    WaitBGM()
    Return()

    # Function_9_5313 end

    def Function_10_992B(): pass

    label("Function_10_992B")

    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    OP_24(0x3CB)
    OP_24(0x35D)
    Sound(973, 0, 100, 0)
    Sound(969, 0, 100, 0)
    Sound(204, 0, 80, 0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x1, 0xFF, 0x101, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x102, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x104, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x107, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x108, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_992B end

    def Function_11_9AB4(): pass

    label("Function_11_9AB4")


    def lambda_9AB9():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9AB9)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Return()

    # Function_11_9AB4 end

    def Function_12_9AE3(): pass

    label("Function_12_9AE3")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_68(-9280, 900, -7620, 300)
    MoveCamera(310, 19, 0, 300)
    SetCameraDistance(17500, 300)
    OP_6F(0x79)
    CancelBlur(1000)
    Return()

    # Function_12_9AE3 end

    def Function_13_9B22(): pass

    label("Function_13_9B22")

    OP_82(0x64, 0x64, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0x96, 0x96, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xFA, 0xFA, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sleep(1500)
    Return()

    # Function_13_9B22 end

    def Function_14_9B87(): pass

    label("Function_14_9B87")

    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x28)
    Sleep(200)
    OP_25(0x3A2, 0x1E)
    Sleep(200)
    OP_25(0x3A2, 0x14)
    Sleep(200)
    OP_25(0x3A2, 0xA)
    Sleep(200)
    OP_24(0x3A2)
    Return()

    # Function_14_9B87 end

    def Function_15_9BCA(): pass

    label("Function_15_9BCA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9BE3")
    Sound(915, 0, 100, 0)
    Sleep(2000)
    Jump("Function_15_9BCA")

    label("loc_9BE3")

    Return()

    # Function_15_9BCA end

    def Function_16_9BE4(): pass

    label("Function_16_9BE4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("apl/ch50547.itc", 0x2A)
    LoadChrToIndex("chr/ch00653.itc", 0x2B)
    LoadChrToIndex("chr/ch00753.itc", 0x2C)
    LoadChrToIndex("chr/ch00056.itc", 0x2D)
    LoadChrToIndex("chr/ch00156.itc", 0x2E)
    LoadChrToIndex("chr/ch00256.itc", 0x2F)
    LoadChrToIndex("chr/ch00356.itc", 0x30)
    LoadChrToIndex("apl/ch50338.itc", 0x31)
    LoadChrToIndex("apl/ch50548.itc", 0x32)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(930)
    OP_68(-2000, 2700, -8000, 0)
    MoveCamera(45, -5, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11500, 0)
    OP_EE(0x0, 0xA)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x101, -11300, 0, -8000, 90)
    SetChrPos(0x102, -12200, 0, -6600, 90)
    SetChrPos(0x103, -12700, 0, -10400, 90)
    SetChrPos(0x104, -13400, 0, -8900, 90)
    SetChrPos(0x107, -11400, 0, -4100, 135)
    SetChrPos(0x108, -13000, 0, -5100, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    OP_32(0x6, 0x5, 0xC8)
    OP_32(0x7, 0x5, 0xC8)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, -2000, 0, -8000, 0)
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0xF)
    OP_70(0x0, 0x65)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    OP_78(0x1, 0xE)
    OP_49()
    OP_74(0x1, 0xF)
    OP_CA(0x1, 0xFF, 0x0)
    LoadEffect(0x0, "event\\ev620_00.eff")
    LoadEffect(0x1, "event\\ev614_01.eff")
    LoadEffect(0x2, "event\\eva03_01.eff")
    LoadEffect(0x3, "event\\ev613_00.eff")
    LoadEffect(0x4, "event\\ev613_01.eff")
    LoadEffect(0x5, "event\\ev613_02.eff")
    LoadEffect(0x6, "event\\ev613_03.eff")
    LoadEffect(0x7, "event\\eva04_00.eff")
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    BeginChrThread(0xB, 3, 0, 30)
    MoveCamera(70, 25, 0, 6000)
    SetCameraDistance(14500, 6000)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x1770)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x1770)
    Sound(930, 2, 100, 0)
    PlayBGM("ed7406", 0)
    FadeToBright(1000, 0)
    Sound(978, 0, 100, 0)
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(1962, 255, 100, 0)

    AnonymousTalk(
        0xB,
        (
            "#5300865V\x07\x02",
            "#4S#20A#60WOOOOOOOHHHHH!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(2000)
    OP_6F(0x50)
    Fade(500)
    OP_68(-7300, 1700, -8000, 0)
    MoveCamera(60, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    CancelBlur(0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5300866V#0010F#6P#NWhat's wrong with him?!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#5300867V#0201F#6P#NHe seems to have gone completely berserk...\x02\x03",
            "#5300868V#0206FAt this point, I'm not sure how much longer\x01",
            "his body can withstand the pressure...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300869V#0101F#6P#NNo way...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300870V#0901F#6P#N...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-300, 2500, -8000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    BeginChrThread(0xB, 3, 0, 31)
    SetCameraDistance(16500, 1500)
    OP_0D()
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0xBF, 0xE6, 0x0, 0x0)
    Sound(976, 0, 90, 0)
    Sound(978, 0, 100, 0)
    Sound(948, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(1963, 255, 100, 0)

    AnonymousTalk(
        0xB,
        (
            "#5300871V\x07\x02",
            "#4S#60W#15AGYAAHHHHHHHH!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x10)
    OP_79(0x0)
    OP_68(-10800, 700, -8000, 1000)
    MoveCamera(47, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xE7, 0xF0, 0x0, 0x0)
    Sound(977, 0, 90, 0)
    OP_79(0x0)
    PlayEffect(0x0, 0x6, 0xB, 0x0, -3300, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0xB, 0x0, -3600, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xF1, 0x118, 0x0, 0x20)
    OP_6F(0x79)
    OP_68(-10800, 1700, -8000, 1000)
    MoveCamera(47, 17, 0, 1000)
    SetCameraDistance(14500, 1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(981, 0, 100, 0)
    Sound(1029, 255, 100, 0)
    Sound(1129, 255, 100, 1)
    Sound(1224, 255, 100, 2)
    Sound(1319, 255, 100, 3)
    Sound(1671, 255, 100, 4)
    Sound(1741, 255, 100, 5)
    PlayEffect(0x1, 0x0, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(100)
    PlayEffect(0x1, 0x1, 0x102, 0x0, 0, 0, 0, 30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0x103, 0x0, 0, 0, 0, 70, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0x104, 0x0, 0, 0, 0, 130, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(100)
    PlayEffect(0x1, 0x4, 0x107, 0x0, 0, 0, 0, 200, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x107, 3, 0, 28)
    Sleep(100)
    PlayEffect(0x1, 0x5, 0x108, 0x0, 0, 0, 0, 170, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x108, 3, 0, 29)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x107, 3)
    WaitChrThread(0x108, 3)
    SetCameraDistance(11000, 20000)
    Sleep(500)

    ChrTalk(
        0x107,
        "#5300872V#6P#0813FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300873V#6P#0307FShit...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300874V#0907F#6PN-No!\x02",
    )

    CloseMessageWindow()
    Sound(978, 0, 100, 0)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("")
    Sound(1962, 255, 100, 0)

    AnonymousTalk(
        0xB,
        (
            "#5300875V\x07\x02",
            "#4S#70W#60AOOOOOOOHHHH!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#5300876V#0108F#6PUgh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300877V#6P#0310FDamn it! If this holds up...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300878V#6P#0807FWe've made it this far! There's no way\x01",
            "we can let this end now!\x02\x03",
            "#5300879V#0806FNot until she's...\x02\x03",
            "#5300880V#0808FNot until we can finally hold that girl\x01",
            "in our arms and grant her the happiness\x01",
            "she deserves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300881V#6P#0007FWe're the same!\x02\x03",
            "#5300882V#0003FYou can't stop us...! We're making it back\x01",
            "to our little girl, no matter what!\x02\x03",
            "#5300883V#0010FGuy...! Please!\x02\x03",
            "#5300884VLend me your strength...!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, -8000, 9000, 8000, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    NpcTalk(
        0xC,
        "Girl's Voice",
        "#5300885V#4PHeehee...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Girl's Voice",
        (
            "#5300886V#4PI may not be your brother, but\x01",
            "I could still give you a hand.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(500)
    EndChrThread(0xB, 0x3)
    Sleep(500)
    Fade(500)
    OP_68(-8000, 27500, 8000, 0)
    MoveCamera(310, -10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x1, 0x4)
    OP_D1(0xC, 0x1, "Null_ren(52)")
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xE, -8000, 35000, 8000, 0)
    OP_D3(0xE, 0x0, 0x249F0, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0xF1, 0x104, 0x0, 0x20)
    PlayEffect(0x2, 0x6, 0xE, 0x40, 0, 0, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x7, 0xE, 0x40, 0, 0, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 0, 100, 0)

    def lambda_AAA7():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x1F40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AAA7)
    OP_0D()
    OP_68(-8000, 12500, 8000, 4000)
    MoveCamera(310, 70, 0, 4000)
    SetCameraDistance(13000, 4000)
    OP_6F(0x79)
    Fade(250)
    OP_68(-8000, 400, 8000, 0)
    MoveCamera(290, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11500, 0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    OP_70(0x1, 0xDD)
    OP_77(0x1, 0x3E8)
    WaitChrThread(0xE, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(-8000, 2400, 8000, 2000)
    MoveCamera(290, 13, 0, 2000)
    SetCameraDistance(17500, 2000)
    PlayEffect(0x7, 0xFF, 0xE, 0x40, 0, 0, 0, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_24(0x3A2)
    Sound(944, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    OP_71(0x1, 0xDD, 0xF0, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    OP_6F(0x79)
    Fade(1000)
    CancelBlur(0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5300887V#0011F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300888V#0105FW-We saw that back at the hospital!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300889V#0901FPater-Mater!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300890V#0802FRenne!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-9300, 2700, 4800, 0)
    MoveCamera(5, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    OP_EE(0x0, 0x5)
    PlayEffect(0x0, 0x6, 0xB, 0x0, -3300, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0xB, 0x0, -3600, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    NpcTalk(
        0xC,
        "Angel of Slaughter, Renne",
        (
            "#5300891V#3308F#5PPitiful, but he probably deserves this.\x02\x03",
            "#5300892V#3303FI'll put him out of his misery.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D1(0xC, 0xFF, "")
    OP_93(0xC, 0x96, 0x0)
    SetChrFlags(0xC, 0x4)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x31)
    SetChrSubChip(0xC, 0x2)
    SetChrChip(0x0, 0xC, 0x32, 0x12C)
    Sound(854, 0, 100, 0)

    def lambda_ADE3():
        OP_9D(0xFE, 0xFFFFCE64, 0x352, 0x1388, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_ADE3)
    WaitChrThread(0xC, 1)
    PlayEffect(0x7, 0xFF, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(50)
    Sound(31, 0, 100, 0)
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    Fade(500)
    OP_68(-9300, 2100, 3300, 0)
    MoveCamera(100, -3, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(12500, 0)
    OP_0D()
    MoveCamera(108, -3, 0, 1000)
    SetCameraDistance(10500, 1000)
    OP_77(0x1, 0x12C)
    OP_71(0x1, 0x79, 0x8C, 0x0, 0x0)
    Sound(945, 0, 100, 0)
    Sleep(600)
    Sound(947, 0, 100, 0)
    OP_79(0x1)
    Sound(945, 0, 100, 0)
    OP_6F(0x79)

    NpcTalk(
        0xC,
        "Angel of Slaughter, Renne",
        "#5300893V#6P#3301FPater-Mater! Blast him to smithereens!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    NpcTalk(
        0xC,
        "Angel of Slaughter, Renne",
        "#5300894V#6P#3307F#4SDouble Buster Cannon!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(943, 0, 100, 0)
    Sleep(800)
    Fade(250)
    OP_68(-6900, 3100, 4000, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(9500, 0)
    OP_EE(0x0, 0xA)
    OP_D3(0xE, 0x0, 0x27100, 0x0, 0x0)
    OP_93(0xE, 0xA0, 0x0)
    SetChrPos(0xB, -1000, 0, -8000, 0)
    SetCameraDistance(8500, 4750)
    OP_82(0x32, 0x32, 0xBB8, 0x128E)
    OP_0D()
    PlayEffect(0x5, 0xFF, 0xE, 0x0, 2700, 4500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xE, 0x0, -100, 4500, -4300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(982, 0, 100, 0)
    Sleep(3000)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 2700, 4500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, -100, 4500, -4300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(1500)
    OP_68(-3200, 1600, -2000, 500)
    MoveCamera(24, 15, 0, 500)
    SetCameraDistance(17500, 500)
    Sleep(150)
    PlayEffect(0x4, 0xFF, 0xE, 0x140, -1700, 4500, 4000, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xE, 0x140, 900, 4500, 4300, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x6, 0xFF, 0xB, 0x0, -3500, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xB, 0x0, -1000, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(983, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    BeginChrThread(0xB, 1, 0, 17)
    Sleep(500)
    OP_71(0x1, 0x8D, 0xA0, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 31)
    Sound(930, 2, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    OP_79(0x1)
    Fade(500)
    OP_68(-11700, 2000, -8000, 0)
    MoveCamera(38, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_0D()
    LoadEffect(0x2, "event\\ev614_02.eff")
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    PlayEffect(0x2, 0xFF, 0x101, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x102, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x103, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x104, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x107, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x108, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(816, 0, 100, 0)
    Sleep(250)
    OP_68(-11700, 1000, -8000, 300)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x103, 3, 0, 20)
    BeginChrThread(0x104, 3, 0, 21)
    BeginChrThread(0x107, 3, 0, 22)
    BeginChrThread(0x108, 3, 0, 23)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x107, 3)
    WaitChrThread(0x108, 3)
    Sleep(500)

    ChrTalk(
        0x103,
        "#5300895V#6P#0202FWe're free!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300896V#6P#0307FHell yeah! Let's finish this!\x02",
    )

    CloseMessageWindow()
    OP_71(0x1, 0xA1, 0xB4, 0x0, 0x0)
    Sound(945, 0, 100, 0)
    Sleep(600)
    Sound(947, 0, 100, 0)
    Sound(945, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    OP_93(0xC, 0xB4, 0x1F4)

    NpcTalk(
        0xC,
        "Angel of Slaughter, Renne",
        (
            "#5300897V#3307F#13PThis is your last chance!\x02\x03",
            "#5300898VHe can't keep it up much longer,\x01",
            "so hurry and finish this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300899V#5P#0010F...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 90, 0)
    Sound(804, 0, 100, 0)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)
    Sound(1019, 255, 100, 0)

    ChrTalk(
        0x101,
        "#5300900V#5P#0007F#4S#14A#40WHaaaaaaaahhhh!\x02",
    )

    Sleep(500)
    OP_68(-5700, 1100, -8000, 915)
    MoveCamera(53, 15, -9, 915)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_B615():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B615)
    Sleep(5)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_B63A():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B63A)
    Sleep(5)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x102, 0x0)

    def lambda_B65F():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B65F)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)

    def lambda_B681():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B681)
    Sleep(5)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_B6A6():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B6A6)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)

    def lambda_B6C8():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B6C8)
    Sleep(900)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x108, 0x1)
    OP_24(0x3A2)
    Battle("BattleInfo_1AC", 0x30200010, 0x0, 0x4, 0xB, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1388)
    WaitBGM()
    Return()

    # Function_16_9BE4 end

    def Function_17_B71C(): pass

    label("Function_17_B71C")

    OP_71(0x0, 0x33, 0x37, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    OP_74(0x0, 0xA)
    Sound(948, 0, 100, 0)
    Sound(978, 0, 100, 0)
    OP_71(0x0, 0x123, 0x136, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x137, 0x15E, 0x0, 0x20)
    Return()

    # Function_17_B71C end

    def Function_18_B75A(): pass

    label("Function_18_B75A")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B764():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B764)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(50)
    Sound(31, 0, 100, 0)
    Return()

    # Function_18_B75A end

    def Function_19_B7AC(): pass

    label("Function_19_B7AC")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B7B6():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7B6)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_B7AC end

    def Function_20_B7EF(): pass

    label("Function_20_B7EF")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B7F9():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7F9)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_B7EF end

    def Function_21_B832(): pass

    label("Function_21_B832")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B83C():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B83C)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_B832 end

    def Function_22_B875(): pass

    label("Function_22_B875")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B87F():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B87F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_B875 end

    def Function_23_B8B8(): pass

    label("Function_23_B8B8")

    ClearChrFlags(0xFE, 0x4)

    def lambda_B8C2():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8C2)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_B8B8 end

    def Function_24_B8FB(): pass

    label("Function_24_B8FB")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_B917():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B917)

    def lambda_B930():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B930)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_24_B8FB end

    def Function_25_B95C(): pass

    label("Function_25_B95C")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_B978():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B978)

    def lambda_B991():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B991)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x3)
    Return()

    # Function_25_B95C end

    def Function_26_B9B8(): pass

    label("Function_26_B9B8")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_B9D4():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B9D4)

    def lambda_B9ED():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9ED)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x2)
    Return()

    # Function_26_B9B8 end

    def Function_27_BA14(): pass

    label("Function_27_BA14")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_BA30():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA30)

    def lambda_BA49():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA49)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x1)
    Return()

    # Function_27_BA14 end

    def Function_28_BA70(): pass

    label("Function_28_BA70")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_BA8C():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA8C)

    def lambda_BAA5():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAA5)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x107, 0x32)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_28_BA70 end

    def Function_29_BACC(): pass

    label("Function_29_BACC")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_BAE8():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAE8)

    def lambda_BB01():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB01)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x108, 0x32)
    SetChrSubChip(0x108, 0x4)
    Return()

    # Function_29_BACC end

    def Function_30_BB28(): pass

    label("Function_30_BB28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB4C")
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_30_BB28")

    label("loc_BB4C")

    Return()

    # Function_30_BB28 end

    def Function_31_BB4D(): pass

    label("Function_31_BB4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB71")
    OP_82(0x0, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_31_BB4D")

    label("loc_BB71")

    Return()

    # Function_31_BB4D end

    def Function_32_BB72(): pass

    label("Function_32_BB72")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("apl/ch50547.itc", 0x2A)
    LoadChrToIndex("chr/ch09500.itc", 0x2B)
    LoadChrToIndex("apl/ch50338.itc", 0x2C)
    LoadChrToIndex("apl/ch50529.itc", 0x2D)
    LoadChrToIndex("apl/ch50531.itc", 0x2E)
    LoadChrToIndex("apl/ch50536.itc", 0x2F)
    SoundLoad(930)
    SoundLoad(986)
    OP_68(-3000, 2300, -8000, 0)
    MoveCamera(120, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -10000, 0, -8000, 90)
    SetChrPos(0x102, -11300, 0, -6600, 90)
    SetChrPos(0x103, -12100, 0, -10400, 90)
    SetChrPos(0x104, -12800, 0, -8900, 90)
    SetChrPos(0x107, -9700, 0, -4000, 135)
    SetChrPos(0x108, -11900, 0, -5000, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -12700, 850, 5000, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, -2000, 0, -8000, 0)
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0xA)
    OP_70(0x0, 0x137)
    OP_71(0x0, 0x137, 0x15E, 0x0, 0x20)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x0)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x0)
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    OP_78(0x1, 0xE)
    OP_49()
    OP_74(0x1, 0xF)
    SetChrPos(0xE, -8000, -1000, 8000, 0)
    OP_D3(0xE, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "event\\ev616_00.eff")
    LoadEffect(0x1, "event\\ev615_00.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    MoveCamera(60, 19, 0, 15000)
    SetCameraDistance(17000, 15000)
    BeginChrThread(0xB, 3, 0, 33)
    BeginChrThread(0xB, 2, 0, 34)
    PlayBGM("ed7534", 0)
    Sleep(1500)
    BeginChrThread(0x10, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(
        0xB,
        (
            "#5300901V\x07\x0C",
            "#60WHah...haha... You continue to surprise me.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            "#5300902V\x07\x0C",
            "#60WI hate to admit it, but...you made me regain\x01",
            "control... For that...you...have my thanks...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(210, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5300903V\x07\x00",
            "#0001F#5PJoachim... Why?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 200, -1, -1)

    AnonymousTalk(
        0x107,
        "#5300904V#0808F#11P...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(
        0xB,
        (
            "#5300905V\x07\x0C",
            "#60WHaha. Please...spare me your pitying looks.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            "#5300906V\x07\x0C",
            "#60WOur goal may still remain unfulfilled...\x01",
            "yet our ambitions were reached...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xB,
        (
            "#5300907V\x07\x0C",
            "#60WShe can do it... Someday, Lady KeA will...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x10, 0x1)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xB, 0x2)
    BeginChrThread(0xB, 3, 0, 35)
    BeginChrThread(0x10, 1, 0, 37)
    PlayEffect(0x0, 0xFF, 0xB, 0x40, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(250)
    OP_68(-2500, 2100, -8000, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13500, 0)
    OP_0D()
    Sleep(2000)
    SetCameraDistance(22500, 1500)
    Fade(1000)
    SetMapObjFlags(0x0, 0x4)
    OP_6F(0x10)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x61, 0x8D, 0x9E, 0x14, 0x64, 0x5DC)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#5300908V\x07\x00",
            "#0011F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300909V#0303FTch... Full of nonsense, right up\x01",
            "until the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300910V#0108FBut...I still feel sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301006V#0206FYes...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x10, 0x1)
    Fade(500)
    OP_68(-9280, 900, -7900, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(19000, 2500)

    def lambda_C2A1():
        OP_95(0xFE, -9000, 0, -8000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C2A1)
    Sleep(700)

    def lambda_C2BE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C2BE)
    Sleep(50)

    def lambda_C2CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C2CE)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    Sleep(250)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_6F(0x10)
    SetCameraDistance(18000, 10000)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300912V#0008F#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300913V#0908FDon't let it eat at you.\x02\x03",
            "#5300914V#0903FThe moment he swallowed all of those\x01",
            "pills, his fate was sealed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    ChrTalk(
        0x107,
        (
            "#5300915V#5P#0806FYeah, that's true...\x02\x03",
            "#5300916V#0808FStill, I would have liked to have\x01",
            "saved him, if it was possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5301018V#0008FYeah.\x02\x03",
            "#5300918V#0006FHe wasn't able to snap out of his delusions,\x01",
            "even with death staring him in the face...\x02\x03",
            "#5300919VI had hoped that he would answer for his\x01",
            "crimes and admit his guilt.\x02\x03",
            "#5300920V#0008FI wanted that so badly for the victims, and\x01",
            "even for himself...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        "#5300921V#6P#0108FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300922V#6P#0208F#NIt's okay, Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    OP_68(-9030, 900, -7890, 1000)

    def lambda_C5DC():
        OP_95(0xFE, -9300, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5DC)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x9)
    SetChrSubChip(0x101, 0x1)
    Sleep(140)
    OP_82(0x32, 0x0, 0xBB8, 0x64)
    SetChrSubChip(0x104, 0xA)
    SetChrSubChip(0x101, 0x2)
    Sleep(140)
    SetChrSubChip(0x104, 0xB)
    SetChrSubChip(0x101, 0x3)
    Sound(819, 0, 100, 0)
    Sleep(140)
    SetChrSubChip(0x104, 0xD)
    SetChrSubChip(0x101, 0x4)
    Sleep(140)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x101, 0x5)

    ChrTalk(
        0x104,
        (
            "#5300923V#12P#0307FHey! What the hell are you gettin'\x01",
            "all moody about?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x6)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300924V#0005F#5PRandy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300925V#12P#0303FWe ain't the Goddess, pal! Things aren't\x01",
            "always gonna go our way!\x02\x03",
            "#5300926V#0301FLook, we only got this far 'cause we\x01",
            "worked our asses off!\x02\x03",
            "#5300927VI'm not sayin' this is the ideal outcome...\x01",
            "but it's still pretty damn good, ain't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300928V#0005FRandy, I...\x02",
    )

    CloseMessageWindow()

    def lambda_C822():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C822)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5300929V#6P#0206FDuring the operation against the lodges,\x01",
            "a lot of cult members committed suicide.\x02\x03",
            "#5300930VGuy, Arios, and Chief Sergei stepped over\x01",
            "countless dead bodies to save me.\x02\x03",
            "#5300931V#0202FUnfortunately, there are times when\x01",
            "sacrifices are inevitable.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#5300932V#0005F...Tio.\x02",
    )

    CloseMessageWindow()

    def lambda_C981():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C981)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        (
            "#5300933V#6P#0103FHe was responsible for his own destruction...\x01",
            "but the consequences of his actions still have\x01",
            "to be taken care of.\x02\x03",
            "#5300934VCrossbell State is still in a panic, and we still\x01",
            "don't know the status of the Gnosis victims...\x02\x03",
            "#5300935V#0100FWe don't have time to grieve yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300936V#11P#0008FElie...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#5300937V#11P#0004F...Thank you.\x02\x03",
            "#5300938V#0002FEverything you said was right.\x01",
            "Now isn't the time to feel down.\x02\x03",
            "#5300939V#0000FPlus, we have promises to keep!\x01",
            "To the chief and to KeA!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300940V#6P#0102FOf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300941V#6P#0204FWe promised her that we'd return\x01",
            "to her side, safe and sound...\x02\x03",
            "#5300942V#0202FAnd we promised the chief that\x01",
            "we'd settle this case, so we can\x01",
            "have our strength recognized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300943V#0309F#12PHaha, would ya look at that...\x01",
            "Managed to keep 'em both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300944V#5P#0802FHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300945V#0904FThey're a family.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0xC,
        "#5300946V#3300F#13PIt would appear this is the final curtain, then.\x02",
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_CDBC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_CDBC)

    def lambda_CDC9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_CDC9)
    Sleep(150)

    def lambda_CDD9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CDD9)

    def lambda_CDE6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CDE6)
    Sleep(50)

    def lambda_CDF6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CDF6)

    def lambda_CE03():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CE03)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x107,
        "#5300947V#12P#0805FAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-12700, 1700, 5000, 0)
    MoveCamera(35, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0x107, -10000, 0, -6800, 0)
    SetChrPos(0x108, -9000, 0, -7300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#5300948V#3300F#5PFor your information, I never intended\x01",
            "to help at the last moment.\x02\x03",
            "#5300949V#3304FHeehee... Loewe's heroism must have\x01",
            "rubbed off on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300950V#0901FRenne!\x02",
    )

    CloseMessageWindow()
    OP_68(-10400, 1700, 1100, 1500)
    SetCameraDistance(16500, 1500)

    def lambda_CF9E():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_CF9E)
    Sleep(200)

    def lambda_CFBB():
        OP_96(0xFE, 0xFFFFDCD8, 0x0, 0xFFFFF704, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_CFBB)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x2)
    SetChrChip(0x0, 0xC, 0x32, 0x12C)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(854, 0, 100, 0)

    def lambda_CFF6():
        OP_9D(0xFE, 0xFFFFD5D0, 0x7D0, 0x16A8, 0x6D6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CFF6)
    WaitChrThread(0xC, 1)
    Sound(30, 0, 100, 0)
    Sleep(30)
    Sound(31, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_93(0xC, 0x0, 0x0)
    OP_D1(0xC, 0x1, "Null_ren(52)")
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0xC, 0x2B)
    SetChrSubChip(0xC, 0x0)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#5300951V#3304F...I've settled all my past regrets and\x01",
            "grievances with Crossbell.\x02\x03",
            "#5300952V#3300FI enjoyed it, but I think my presence\x01",
            "will cause more harm than good.\x01",
            "So, it's about time I take my leave...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300953V#0800F#11PRenne.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_D1AF():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D1AF)
    Sleep(800)
    OP_93(0xC, 0x5A, 0xFA)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#5300954V#3306F#12P...Yes, Estelle?\x02\x03",
            "#5300955V#3308FI'm just...not ready to be caught yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300956V#0803F#11PNope. Sorry, Renne.\x02\x03",
            "#5300957V#0802FYou're not getting away this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300958V#3305F#12P...!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7520", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x208), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-10400, 2100, 1800, 25000)
    MoveCamera(29, 1, 0, 25000)
    SetCameraDistance(17500, 25000)

    ChrTalk(
        0x107,
        (
            "#5300959V#0808F#11PIt's been over half a year since I last\x01",
            "saw your adorable face...\x02\x03",
            "#5300960VAfter stopping by Liberl, we've been\x01",
            "here for the past three months.\x02\x03",
            "#5300961V#0800FAnd every day, I've known you were\x01",
            "watching over us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300962V#0904F#11PWe know you were staying at the\x01",
            "Rosenberg Studio, occasionally going\x01",
            "to Crossbell City to play around.\x02\x03",
            "#5300963V#0900FThe hard part was catching you on\x01",
            "the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5300964V#3307F#12PW-Well, of course it was...\x02\x03",
            "#5300965V#3308FNo one could ever possibly\x01",
            "catch Kitty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300966V#0800FExcept us, right?\x02\x03",
            "#5300967V#0803FRenne, we know everything there\x01",
            "is to know about you.\x02\x03",
            "#5300968VYour past, your sorrow, your pain...\x01",
            "But also your happiness and\x01",
            "everything you love doing.\x02\x03",
            "#5300969V#0802FYou can't run away from us.\x01",
            "Not anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300970V#3308F#12P...\x02",
    )

    CloseMessageWindow()

    def lambda_D62C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D62C)
    Sleep(800)
    OP_93(0xC, 0xB4, 0x12C)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#5300971V#3312F#12P#40WI-I thought... I thought you'd give up...\x02\x03",
            "#5300972VAfter learning about Paradise...\x02\x03",
            "#5300973V#3313FOnce you learned about Paradise, Estelle,\x01",
            "I was convinced you would...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300974V#0806F#11PIf I was the same person I was two years ago,\x01",
            "I might have.\x02\x03",
            "#5300975V#0802FBut after meeting wonderful people like you and\x01",
            "Loewe, I've become stronger than I once was.\x02\x03",
            "#5300976VNo matter what things happened in the past,\x01",
            "good or bad...they're irreplaceable moments\x01",
            "that make you who you are.\x02\x03",
            "#5300977V#0809FAnd, with every bit of my heart, I can't help\x01",
            "but love you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300978V#3312F#12P...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#5300979V#0903F#11PIt might be better for you to return\x01",
            "to your family here in Crossbell...\x02\x03",
            "#5300980V#0901F...but, no matter how unreasonable\x01",
            "this may sound, we want you to be\x01",
            "a part of our family, Renne.\x02\x03",
            "#5300981V#0902FAfter coming to Crossbell, we came\x01",
            "to that conclusion all over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5300982V#3313F#12P*sob*...\x02\x03",
            "#5300983VI-I don't understand...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(943, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 36)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0xC, 0xF0, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#5300984V#3311F#6PPater-Mater?!\x02\x03",
            "#5300985VWhy are you moving?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300986V#0805F#12P#NTh-There's no way...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#5300987V#0902F#12P#NSo that's it... He's been worried\x01",
            "about Renne this whole time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0xE, 3)
    Fade(500)
    OP_68(-9600, 800, -1900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_93(0xC, 0x10E, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x107, -10000, 0, -2600, 0)
    SetChrPos(0x108, -9200, 0, -3000, 0)
    SetCameraDistance(17000, 2000)
    OP_0D()
    Sound(943, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x10, 1, 0, 38)
    OP_71(0x1, 0x1CD, 0x1F4, 0x0, 0x0)
    Sleep(500)

    def lambda_DC0B():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF1F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_DC0B)
    Sleep(100)

    def lambda_DC28():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF060, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_DC28)
    OP_79(0x1)
    OP_71(0x1, 0x1F5, 0x208, 0x0, 0x0)
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        "#5300988V#11P#3310F#10A#40W#NS-Stop, please...!\x02",
    )

    CloseMessageWindow()
    OP_79(0x1)
    Fade(500)
    OP_D1(0xC, 0xFF, "")
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, -9600, 0, -1700, 0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x2E)
    SetChrSubChip(0xC, 0x0)
    OP_71(0x1, 0x209, 0x212, 0x0, 0x0)
    OP_79(0x1)
    OP_0D()
    OP_71(0x1, 0x213, 0x226, 0x0, 0x0)
    OP_79(0x1)
    OP_6F(0x10)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    EndChrThread(0x10, 0x1)
    OP_68(-9530, 800, -1690, 1000)

    def lambda_DD27():
        OP_96(0xFE, 0xFFFFDA1C, 0x0, 0xFFFFF704, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_DD27)
    Sleep(1300)
    Fade(500)
    SetChrPos(0xC, -9600, 0, -1800, 0)
    SetChrSubChip(0xC, 0xA)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    Sound(910, 0, 100, 0)
    SetChrSubChip(0xC, 0xB)
    Sleep(130)
    SetChrSubChip(0xC, 0xC)
    Sleep(130)
    SetChrSubChip(0xC, 0xD)
    Sound(804, 0, 70, 0)
    Sleep(130)
    SetChrSubChip(0xC, 0xE)
    Sleep(130)
    SetChrSubChip(0xC, 0xF)
    Sleep(300)
    MoveCamera(57, 17, 0, 30000)
    SetCameraDistance(16000, 30000)

    ChrTalk(
        0x107,
        "#5300989V#11P#0804FCaught you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300990V#11P#3312F...\x02",
    )

    CloseMessageWindow()

    def lambda_DE11():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF2B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_DE11)
    WaitChrThread(0x108, 1)

    ChrTalk(
        0x108,
        (
            "#5300991V#12P#0904FThank you, Pater-Mater.\x02\x03",
            "#5300992V#0900FThe adjustments made by the meister\x01",
            "gave you the ability to move on your\x01",
            "own, right?\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0xC,
        "#5300993V#11P#3313F*sob*...\x02",
    )

    CloseMessageWindow()

    def lambda_DEEE():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_DEEE)

    ChrTalk(
        0x107,
        (
            "#5300994V#11P#0812FNever again. I'm never letting you\x01",
            "get away from us again.\x02\x03",
            "#5300995VFrom here on out, where we go,\x01",
            "how we live, what we do... Let's\x01",
            "figure those things out together...\x02\x03",
            "#5300996V#0811FBut first, how about heading back\x01",
            "to Liberl?\x02\x03",
            "#5300997VI know Tita has been dying to play\x01",
            "with you...and for you to come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5300998V#11P#3312F*sob*...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 60, 0)
    Sleep(110)
    SetChrSubChip(0xC, 0x3)
    Sleep(110)
    SetChrSubChip(0xC, 0x4)
    Sleep(110)
    SetChrSubChip(0xC, 0x5)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0xC,
        "#5300999V#5P#3310F#4SWaaaahhhh...!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x10)
    Sound(820, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0xC, 0x11)
    Sleep(130)
    SetChrSubChip(0xC, 0x12)

    ChrTalk(
        0x107,
        "#5301000V#11P#0810F...Renne.\x02",
    )

    CloseMessageWindow()
    Sleep(130)
    SetChrSubChip(0xC, 0x11)
    Sleep(130)
    SetChrSubChip(0xC, 0x10)

    ChrTalk(
        0xC,
        "#5301001V#5P#3313F*sob* *whimper*...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x7)
    Sleep(100)
    SetChrSubChip(0xC, 0x8)
    Sleep(100)
    SetChrSubChip(0xC, 0x9)
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0xC,
        "#5301002V#5P#3310F#4SWaaaaaaahhhhh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5301003V#0910F#11P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x101, -9300, 0, -7900, 0)
    SetChrPos(0x102, -11000, 0, -8500, 0)
    SetChrPos(0x103, -10200, 0, -9300, 0)
    SetChrPos(0x104, -8500, 0, -8800, 0)
    OP_68(-9170, 1000, -3990, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_E21F():
        OP_96(0xFE, 0xFFFFDBAC, 0x0, 0xFFFFECDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E21F)
    Sleep(200)

    def lambda_E23C():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFEA84, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E23C)
    Sleep(200)

    def lambda_E259():
        OP_96(0xFE, 0xFFFFD828, 0x0, 0xFFFFE764, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E259)
    Sleep(200)

    def lambda_E276():
        OP_96(0xFE, 0xFFFFDECC, 0x0, 0xFFFFE958, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E276)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5301004V#0002F#11PHaha...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#5301005V#12P#0106F*sniff* This is beautiful...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)

    ChrTalk(
        0x103,
        "#5300911V#12P#0208FIt is...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#5301007V#0302FHaha... Didn't think I'd be\x01",
            "sheddin' a tear today.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x108,
        (
            "#5301008V#0910F#5PEveryone...\x02\x03",
            "#5301009V#0911FThank you so much for everything.\x01",
            "I really don't know what to say...\x02\x03",
            "#5301010V#0904FI don't know how we could ever\x01",
            "come close to repaying you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5301011V#0004F#11PDon't mention it. We were only helping out\x01",
            "a good cause.\x02\x03",
            "#5301012VI sincerely believe that you two made this\x01",
            "possible by never giving up and, more\x01",
            "importantly, never giving up on her.\x02\x03",
            "#5301013V#0002FJoshua. Allow me to be the first one to\x01",
            "congratulate you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5301014V#0911F#5PThank you, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5301015V#12P#0102FAll of this is making the wait\x01",
            "to see KeA that much harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301016V#12P#0204FAgreed... Zeit and the chief, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5301017V#0309FHaha, then let's get a move on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300917V#0002F#11PYeah...\x02",
    )

    CloseMessageWindow()
    OP_68(-8860, 1000, -4920, 1500)
    MoveCamera(51, 17, 0, 1500)

    def lambda_E670():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E670)
    Sleep(250)

    def lambda_E680():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E680)

    def lambda_E68D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E68D)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    OP_6F(0x1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x4)
    Sleep(130)
    SetChrSubChip(0x101, 0x3)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5301019V#5P#0004FSpecial Support Section, prepare to withdraw.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x3)
    Sleep(130)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5301020V#5P#0000FOur mission may be complete, but we still need\x01",
            "to arrest the Revache members and escort the\x01",
            "civilians to the surface. Let's move out...!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_24(0x3A2)
    OP_24(0x3DA)
    Return()

    # Function_32_BB72 end

    def Function_33_E7E8(): pass

    label("Function_33_E7E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E80C")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_33_E7E8")

    label("loc_E80C")

    Return()

    # Function_33_E7E8 end

    def Function_34_E80D(): pass

    label("Function_34_E80D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E857")
    PlayEffect(0x1, 0xFF, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    Jump("Function_34_E80D")

    label("loc_E857")

    Return()

    # Function_34_E80D end

    def Function_35_E858(): pass

    label("Function_35_E858")

    OP_77(0x0, 0x3E8)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x5A, 0x64, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x0)
    Return()

    # Function_35_E858 end

    def Function_36_E880(): pass

    label("Function_36_E880")

    OP_77(0x1, 0x12C)

    def lambda_E889():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x708, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E889)
    OP_71(0x1, 0x1A5, 0x1CC, 0x0, 0x0)
    Sleep(500)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    Sleep(1200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    OP_79(0x1)
    OP_71(0x1, 0x1A5, 0x1CC, 0x0, 0x0)
    Sleep(500)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    Sleep(1200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    OP_79(0x1)
    WaitChrThread(0xE, 1)
    Return()

    # Function_36_E880 end

    def Function_37_E929(): pass

    label("Function_37_E929")

    Sound(202, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sound(946, 0, 100, 0)
    OP_24(0x3A2)
    OP_24(0x3DA)
    Sleep(1000)
    Sound(969, 0, 100, 0)
    Sleep(1400)
    Sound(984, 0, 100, 0)
    Sleep(300)
    Sound(973, 0, 100, 0)
    Sound(985, 0, 100, 0)
    Return()

    # Function_37_E929 end

    def Function_38_E963(): pass

    label("Function_38_E963")

    Sound(987, 0, 100, 0)
    Sleep(1900)
    Sound(945, 0, 80, 0)
    Sleep(600)
    Sound(987, 0, 100, 0)
    Sleep(1600)
    Sound(945, 0, 80, 0)
    Sleep(400)
    Sound(987, 0, 100, 0)
    Sleep(1700)
    Sound(945, 0, 80, 0)
    Return()

    # Function_38_E963 end

    def Function_39_E997(): pass

    label("Function_39_E997")

    Sound(930, 2, 0, 0)
    Sound(986, 2, 0, 0)
    Sleep(100)
    OP_25(0x3A2, 0xA)
    OP_25(0x3DA, 0xA)
    Sleep(100)
    OP_25(0x3A2, 0x14)
    OP_25(0x3DA, 0x14)
    Sleep(100)
    OP_25(0x3A2, 0x1E)
    OP_25(0x3DA, 0x1E)
    Sleep(100)
    OP_25(0x3A2, 0x28)
    OP_25(0x3DA, 0x28)
    Sleep(100)
    OP_25(0x3A2, 0x32)
    OP_25(0x3DA, 0x32)
    Sleep(100)
    OP_25(0x3A2, 0x3C)
    OP_25(0x3DA, 0x3C)
    Sleep(100)
    OP_25(0x3A2, 0x46)
    OP_25(0x3DA, 0x46)
    Sleep(100)
    OP_25(0x3A2, 0x50)
    OP_25(0x3DA, 0x50)
    Sleep(100)
    OP_25(0x3A2, 0x5A)
    OP_25(0x3DA, 0x5A)
    Sleep(100)
    OP_25(0x3A2, 0x64)
    OP_25(0x3DA, 0x64)
    Return()

    # Function_39_E997 end

    SaveToFile()

Try(main)
