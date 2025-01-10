from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r000b.bin",                # FileName
        "r000b",                    # MapName
        "r000b",                    # Location
        0x005E,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 5700, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 2, 0, 3],
    )

    BuildStringList((
        "r000b",                  # 0
        "Zeit",                   # 1
        "Mafioso",                # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Mafioso",                # 5
        "Mafioso",                # 6
        "Mafioso",                # 7
        "Mafioso",                # 8
        "Mafioso",                # 9
        "Mafioso",                # 10
        "Mafioso",                # 11
        "Mafioso",                # 12
        "Mafioso",                # 13
        "Mafioso",                # 14
        "Mafioso",                # 15
        "Doven Kaiser",           # 16
        "Doven Kaiser",           # 17
        "CGF Guardsman",          # 18
        "CGF Guardsman",          # 19
        "CGF Guardsman",          # 20
        "CGF Guardsman",          # 21
        "CGF Guardsman",          # 22
        "CGF Guardsman",          # 23
        "車１",                   # 24
        "車２",                   # 25
        "車３",                   # 26
        "Mr. Crois",              # 27
        "Mariabell",              # 28
        "SE制御",                 # 29
        "br000b",                 # 30
        "To Crossbell City",      # 31
        "To Armorica Village & Tangram Gate",# 32
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 9, 11, 180)
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
        "BattleInfo_E4", 0x000A, 34, 6, 0, 0, 0, 0, 0, "br000b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31003.dat", "ms67101.dat", "ms67101.dat", "ms31103.dat", "ms31901.dat", "ms31901.dat", 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7405", "ed7000", "ATBonus_94"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "To Armorica Village & Tangram Gate")

    ScpFunction((
        "Function_0_5F8",          # 00, 0
        "Function_1_614",          # 01, 1
        "Function_2_630",          # 02, 2
        "Function_3_668",          # 03, 3
        "Function_4_669",          # 04, 4
        "Function_5_17B2",         # 05, 5
        "Function_6_17D8",         # 06, 6
        "Function_7_181C",         # 07, 7
        "Function_8_184B",         # 08, 8
        "Function_9_187A",         # 09, 9
        "Function_10_18A9",        # 0A, 10
        "Function_11_18FC",        # 0B, 11
        "Function_12_336D",        # 0C, 12
        "Function_13_348D",        # 0D, 13
        "Function_14_35EF",        # 0E, 14
        "Function_15_363D",        # 0F, 15
        "Function_16_369D",        # 10, 16
        "Function_17_36FD",        # 11, 17
        "Function_18_394C",        # 12, 18
        "Function_19_3AAA",        # 13, 19
        "Function_20_3C7D",        # 14, 20
        "Function_21_3D22",        # 15, 21
        "Function_22_3D93",        # 16, 22
        "Function_23_3E04",        # 17, 23
        "Function_24_3E6F",        # 18, 24
        "Function_25_3EA6",        # 19, 25
        "Function_26_3EDD",        # 1A, 26
        "Function_27_3F2E",        # 1B, 27
        "Function_28_3F79",        # 1C, 28
        "Function_29_3FCA",        # 1D, 29
        "Function_30_4027",        # 1E, 30
        "Function_31_404E",        # 1F, 31
        "Function_32_4075",        # 20, 32
        "Function_33_409C",        # 21, 33
        "Function_34_40C3",        # 22, 34
        "Function_35_40EA",        # 23, 35
        "Function_36_4111",        # 24, 36
        "Function_37_4138",        # 25, 37
        "Function_38_415F",        # 26, 38
        "Function_39_41B5",        # 27, 39
        "Function_40_420B",        # 28, 40
        "Function_41_4225",        # 29, 41
        "Function_42_423F",        # 2A, 42
        "Function_43_425C",        # 2B, 43
        "Function_44_4B1C",        # 2C, 44
        "Function_45_4BA3",        # 2D, 45
        "Function_46_4D71",        # 2E, 46
        "Function_47_4FF0",        # 2F, 47
        "Function_48_5071",        # 30, 48
        "Function_49_523F",        # 31, 49
        "Function_50_54BE",        # 32, 50
        "Function_51_552D",        # 33, 51
        "Function_52_5596",        # 34, 52
        "Function_53_5618",        # 35, 53
        "Function_54_566F",        # 36, 54
        "Function_55_56BA",        # 37, 55
        "Function_56_5742",        # 38, 56
        "Function_57_577F",        # 39, 57
        "Function_58_5903",        # 3A, 58
        "Function_59_5E3A",        # 3B, 59
        "Function_60_5F5A",        # 3C, 60
        "Function_61_607A",        # 3D, 61
        "Function_62_6098",        # 3E, 62
        "Function_63_60B0",        # 3F, 63
        "Function_64_60CA",        # 40, 64
    ))


    def Function_0_5F8(): pass

    label("Function_0_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_613")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_5F8")

    label("loc_613")

    Return()

    # Function_0_5F8 end

    def Function_1_614(): pass

    label("Function_1_614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62F")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_614")

    label("loc_62F")

    Return()

    # Function_1_614 end

    def Function_2_630(): pass

    label("Function_2_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_644")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_667")

    label("loc_644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_658")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_667")

    label("loc_658")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_667")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 43)

    label("loc_667")

    Return()

    # Function_2_630 end

    def Function_3_668(): pass

    label("Function_3_668")

    Return()

    # Function_3_668 end

    def Function_4_669(): pass

    label("Function_4_669")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9F, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    LoadChrToIndex("chr/ch00350.itc", 0x26)
    LoadChrToIndex("chr/ch00351.itc", 0x27)
    LoadChrToIndex("chr/ch31050.itc", 0x28)
    LoadChrToIndex("chr/ch31051.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("chr/ch31950.itc", 0x2C)
    LoadChrToIndex("chr/ch31951.itc", 0x2D)
    LoadChrToIndex("monster/ch67150.itc", 0x2E)
    LoadChrToIndex("monster/ch67151.itc", 0x2F)
    LoadChrToIndex("apl/ch50111.itc", 0x30)
    LoadChrToIndex("chr/ch02752.itc", 0x31)
    LoadChrToIndex("chr/ch02702.itc", 0x32)
    SoundLoad(891)
    OP_68(24300, 1000, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 15600, 0, 0, 90)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 14500, 0, 1000, 90)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 13100, 0, 0, 90)
    SetChrPos(0x104, 13900, 0, -1000, 90)
    SetChrPos(0x1A0, 45600, 0, -1000, 90)
    SetChrPos(0x158, 43900, 0, -2000, 90)
    SetChrFlags(0x1A0, 0x80)
    SetChrBattleFlags(0x1A0, 0x8000)
    SetChrFlags(0x158, 0x80)
    SetChrBattleFlags(0x158, 0x8000)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, 13300, 0, 2600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x18, 0x2E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 77000, 0, -1400, 270)
    SetChrPos(0xA, 77000, 0, 1400, 270)
    SetChrPos(0xB, 79000, 0, 0, 270)
    SetChrPos(0xD, 80500, 0, -900, 270)
    SetChrPos(0xE, 80500, 0, 900, 270)
    SetChrPos(0x17, 78400, 0, -3400, 270)
    SetChrPos(0x18, 78400, 0, 3400, 270)

    def lambda_8FC():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FC)
    Sleep(50)

    def lambda_919():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_919)
    Sleep(50)

    def lambda_936():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_936)
    Sleep(50)

    def lambda_953():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_953)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x24, 1, 0, 41)

    def lambda_99A():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_99A)
    SetCameraDistance(21000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(44500, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(19500, 1500)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x87, 0x1F4)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#5200263V#0006F#5P*pant* *pant*\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5200264V#0000F#11POkay, it looks like we managed\x01",
            "to shake them off.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AB5)
    Sleep(100)

    def lambda_AC5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AC5)
    Sleep(50)

    def lambda_AD5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AD5)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x102,
        (
            "#5200265V#0106F#11PIndeed. But only because Chief Sergei\x01",
            "and Dudley were able to buy us time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200266V#11P#0208FI hope they are okay, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200267V#11P#0303FAll we can do is leave 'em in\x01",
            "the hands of the Goddess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200268V#0006F#11PYeah...\x02\x03",
            "#5200269V#0001FBut anyway, are the both of\x01",
            "you doing okay?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C2D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C2D)
    Sleep(50)

    def lambda_C3D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3D)
    Sleep(50)

    def lambda_C4D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C4D)
    WaitChrThread(0x103, 2)

    NpcTalk(
        0x104,
        "Shizuku",
        "#5200270V#5P#6000FY-Yes...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#5200271V#5P#1110FYep! I'm A-OK!\x02\x03",
            "#5200272V#1109FHehehe. This reminds me of\x01",
            "when we first met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200273V#0012F#11PYeah, I can see the parallels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200274V#6P#0306FHeh. Kinda nuts it's only been a month\x01",
            "since the whole auction thing went down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200275V#6P#0202FIt is hard to believe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200276V#0104F#5PHeehee...\x02\x03",
            "#5200277V#0100FAnyway, we need to keep moving.\x01",
            "We have to make our way through\x01",
            "the highway.\x02\x03",
            "#5200278VShall I try contacting Tangram Gate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#5200279V#0000F#11PYeah. Please do.\x02\x03",
            "#5200280VIf you're having difficulty connecting\x01",
            "to them, then you can try directly\x01",
            "contacting Sergeant Major Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200281V#0100F#5PWill do.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x30)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    def lambda_F52():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F52)
    Sleep(50)

    def lambda_F62():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F62)
    Sound(807, 0, 100, 0)
    Sleep(800)
    Sound(891, 2, 100, 0)
    Sleep(3000)

    ChrTalk(
        0x102,
        "#5200282V#0108F#5P...No response.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200283V#12P#0300FCan't blame 'em. Probably got their\x01",
            "hands full with this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200284V#6P#0206FIt may prove difficult to establish\x01",
            "communications with them for\x01",
            "the time being.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_24(0x37B)
    Sound(807, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#5200285V#0100F#5PThere's not much we can do about it,\x01",
            "so I'll try contacting Serg--\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x2BC)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(45550, 1000, 160, 1000)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x24, 1, 0, 40)

    def lambda_1112():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1112)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2058, 255, 100, 0)

    ChrTalk(
        0x8,
        "#5200286V#6P#1201FGrrrr...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11E8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11E8)
    Sleep(50)

    def lambda_11F8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11F8)
    Sleep(50)

    def lambda_1208():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1208)
    Sleep(50)

    def lambda_1218():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1218)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x101,
        "#5200287V#0005F#6PWhat is it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200288V#6P#0301FOh, come ON!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x17, 3, 0, 10)
    BeginChrThread(0x18, 3, 0, 10)
    BeginChrThread(0x24, 1, 0, 40)
    BeginChrThread(0xB, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 9)
    OP_68(57000, 1000, 0, 2000)
    MoveCamera(35, 20, 0, 2000)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_6F(0x41)

    ChrTalk(
        0x101,
        "#5200289V#0007FRevache!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200290V#0201FIt appears to be a squadron from the\x01",
            "group responsible for the hospital raid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200291V#0310FI figure they've got about 300 troops\x01",
            "at the ready. Bet they've got even more\x01",
            "they're willin' to throw our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200292V#0103FI don't think we have much choice\x01",
            "but to break through them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(47500, 1000, 0, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x9, 54000, 0, -1400, 270)
    SetChrPos(0xA, 54000, 0, 1400, 270)
    SetChrPos(0xB, 56000, 0, 0, 270)
    SetChrPos(0xD, 57500, 0, -900, 270)
    SetChrPos(0xE, 57500, 0, 900, 270)
    SetChrPos(0x17, 55400, 0, -3400, 270)
    SetChrPos(0x18, 55400, 0, 3400, 270)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x26)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x1A0, 0x80)
    ClearChrBattleFlags(0x1A0, 0x8000)
    ClearChrFlags(0x158, 0x80)
    ClearChrBattleFlags(0x158, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5200293V#0013FHey, KeA, Shizuku. Get as far\x01",
            "behind us as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A0,
        "#5200294V#1101F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x158,
        "#5200295V#6001F#12P#NU-Understood!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x158, 3, 0, 5)
    Sleep(100)
    BeginChrThread(0x1A0, 3, 0, 6)
    WaitChrThread(0x158, 3)
    WaitChrThread(0x1A0, 3)

    ChrTalk(
        0x9,
        (
            "#5200296V\x07\x02",
            "#11P#30W...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200297V\x07\x02",
            "#5P#35W...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19500, 500)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)

    def lambda_1685():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1685)
    SetChrChipByIndex(0xA, 0x29)
    SetChrSubChip(0xA, 0x0)

    def lambda_16A7():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16A7)
    SetChrChipByIndex(0xB, 0x2B)
    SetChrSubChip(0xB, 0x0)

    def lambda_16C9():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_16C9)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)

    def lambda_16EB():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_16EB)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)

    def lambda_170D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_170D)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 1)

    def lambda_1735():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1735)
    SetChrChipByIndex(0x18, 0x2F)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 0, 0, 1)

    def lambda_175D():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_175D)
    Sleep(500)
    OP_24(0x37B)
    Battle("BattleInfo_E4", 0x30200011, 0x0, 0x0, 0x17, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x18, 0xFF)
    Call(0, 11)
    Return()

    # Function_4_669 end

    def Function_5_17B2(): pass

    label("Function_5_17B2")

    OP_93(0x158, 0x10E, 0x1F4)

    def lambda_17BE():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_17BE)
    WaitChrThread(0x158, 1)
    Return()

    # Function_5_17B2 end

    def Function_6_17D8(): pass

    label("Function_6_17D8")

    OP_93(0x1A0, 0xE1, 0x1F4)

    def lambda_17E4():
        OP_95(0xFE, 43900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_17E4)
    WaitChrThread(0x1A0, 1)

    def lambda_1802():
        OP_95(0xFE, 38900, 0, -2000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A0, 1, lambda_1802)
    WaitChrThread(0x1A0, 1)
    Return()

    # Function_6_17D8 end

    def Function_7_181C(): pass

    label("Function_7_181C")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1829():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1829)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_181C end

    def Function_8_184B(): pass

    label("Function_8_184B")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1858():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1858)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_184B end

    def Function_9_187A(): pass

    label("Function_9_187A")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1887():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1887)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_9_187A end

    def Function_10_18A9(): pass

    label("Function_10_18A9")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_18BC():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18BC)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x24, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_18A9 end

    def Function_11_18FC(): pass

    label("Function_11_18FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    RemoveParty(0x9F, 0x0)
    AddParty(0x52, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    LoadChrToIndex("chr/ch02750.itc", 0x14)
    LoadChrToIndex("chr/ch02751.itc", 0x15)
    LoadChrToIndex("chr/ch00050.itc", 0x16)
    LoadChrToIndex("chr/ch00051.itc", 0x17)
    LoadChrToIndex("chr/ch00150.itc", 0x18)
    LoadChrToIndex("chr/ch00151.itc", 0x19)
    LoadChrToIndex("chr/ch00250.itc", 0x1A)
    LoadChrToIndex("chr/ch00251.itc", 0x1B)
    LoadChrToIndex("chr/ch00350.itc", 0x1C)
    LoadChrToIndex("chr/ch00351.itc", 0x1D)
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31053.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x21)
    LoadChrToIndex("chr/ch31151.itc", 0x22)
    LoadChrToIndex("chr/ch31153.itc", 0x23)
    LoadChrToIndex("chr/ch31950.itc", 0x24)
    LoadChrToIndex("chr/ch31951.itc", 0x25)
    LoadChrToIndex("chr/ch31953.itc", 0x26)
    LoadChrToIndex("chr/ch31250.itc", 0x27)
    LoadChrToIndex("chr/ch31251.itc", 0x28)
    LoadChrToIndex("chr/ch31350.itc", 0x29)
    LoadChrToIndex("chr/ch31351.itc", 0x2A)
    LoadChrToIndex("chr/ch02752.itc", 0x2B)
    LoadChrToIndex("chr/ch31052.itc", 0x2C)
    LoadChrToIndex("chr/ch31952.itc", 0x2D)
    LoadChrToIndex("chr/ch31252.itc", 0x2E)
    LoadChrToIndex("apl/ch50363.itc", 0x2F)
    LoadChrToIndex("chr/ch02702.itc", 0x30)
    LoadChrToIndex("chr/ch05500.itc", 0x31)
    LoadChrToIndex("chr/ch00000.itc", 0x32)
    LoadChrToIndex("chr/ch00300.itc", 0x33)
    LoadChrToIndex("chr/ch00152.itc", 0x34)
    LoadChrToIndex("chr/ch00254.itc", 0x35)
    LoadChrToIndex("chr/ch31353.itc", 0x36)
    SoundLoad(460)
    SoundLoad(468)
    OP_68(44500, 900, 0, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x101, 0x16)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 43600, 0, 0, 90)
    SetChrChipByIndex(0x102, 0x18)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 42500, 0, 1000, 90)
    SetChrChipByIndex(0x103, 0x1A)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 41100, 0, 0, 90)
    SetChrChipByIndex(0x104, 0x1C)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 41900, 0, -1000, 90)
    SetChrPos(0x153, 39200, 0, 100, 90)
    SetChrPos(0x158, 39200, 0, -900, 90)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0x8, 43300, 0, 2600, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x23, 0x31)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x23, 37000, 150, -100, 315)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x2F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x2F)
    SetChrSubChip(0xB, 0x1)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrSubChip(0xD, 0x2)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x9, 46500, 0, -1900, 270)
    SetChrPos(0xA, 47200, 0, 1000, 315)
    SetChrPos(0xB, 48800, 0, -300, 180)
    SetChrPos(0xD, 50700, 0, -1700, 180)
    SetChrPos(0xE, 50500, 0, 1300, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x28)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x19, 1300, 0, 0, 90)
    SetChrPos(0x1A, 0, 0, 1200, 90)
    SetChrPos(0x1B, 0, 0, -1200, 90)
    SetChrPos(0x1C, 5300, 0, 0, 90)
    SetChrPos(0x1D, 4000, 0, 1200, 90)
    SetChrPos(0x1E, 4000, 0, -1200, 90)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x13, 111100, 500, -2400, 180)
    SetChrPos(0x14, 111100, 500, -2400, 180)
    SetChrPos(0x15, 111100, 500, -2400, 180)
    SetChrPos(0x16, 111100, 500, -2400, 180)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF, 113100, 500, 2400, 180)
    SetChrPos(0x10, 113100, 500, 2400, 180)
    SetChrPos(0x11, 113100, 500, 2400, 180)
    SetChrPos(0x12, 113100, 500, 2400, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x5, 0x1F)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x4)
    OP_49()
    SetChrPos(0x1F, 141500, 0, -2400, 0)
    OP_D3(0x1F, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB5, 0xF0, 0x0, 0x20)
    OP_78(0x6, 0x20)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFlags(0x6, 0x4)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x4)
    OP_49()
    SetChrPos(0x20, 143500, 0, 2400, 0)
    OP_D3(0x20, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    OP_78(0x7, 0x21)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x4)
    OP_49()
    SetChrPos(0x21, 153000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x7, "bul00", 0x0, 0x1)
    SetMapObjFrame(0x7, "bul01", 0x0, 0x1)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg040_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")
    LoadEffect(0x5, "event\\eva03_01.eff")
    LoadEffect(0x6, "event\\eva04_00.eff")
    SetCameraDistance(20500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x104,
        "#5200298V#6P#0302FHell yeah! That'll show 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200299V#0000F#5PWe have to keep moving,\x01",
            "everybo--\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(485, 0, 100, 0)
    Fade(500)
    OP_68(127500, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_EE(0x0, 0x1)
    OP_68(112500, 1000, 0, 4000)
    MoveCamera(55, 20, 0, 4000)
    SetCameraDistance(20000, 4000)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)

    def lambda_215E():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_215E)
    Sleep(50)

    def lambda_217B():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_217B)
    WaitChrThread(0x1F, 1)
    Sound(495, 0, 100, 0)
    SetMapObjFlags(0x5, 0x20)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x20, 1)
    OP_24(0x1E5)
    SetMapObjFlags(0x6, 0x20)
    OP_71(0x6, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x6, 0x1, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_79(0x6)
    OP_6F(0x79)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    BeginChrThread(0xF, 3, 0, 38)
    BeginChrThread(0x13, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x10, 3, 0, 38)
    BeginChrThread(0x14, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 38)
    BeginChrThread(0x15, 3, 0, 39)
    Sleep(400)
    BeginChrThread(0x12, 3, 0, 38)
    BeginChrThread(0x16, 3, 0, 39)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x13, 3)
    Fade(500)
    OP_68(44500, 900, 0, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_EE(0x0, 0xA)
    OP_0D()

    ChrTalk(
        0x101,
        "#5200300V#0007F#6PNo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200301V#6P#0310FDamn... Doesn't look like much of\x01",
            "an option anymore, Lloyd.\x02\x03",
            "#5200302V#0307FNo time for mopin'. Let's turn around\x01",
            "and head for the Downtown District.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    ChrTalk(
        0x103,
        "#5200303V#0201F#11PAh...\x02",
    )

    CloseMessageWindow()

    def lambda_23C7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23C7)
    Sleep(50)

    def lambda_23D7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23D7)
    Sleep(50)

    def lambda_23E7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_23E7)
    Sleep(50)

    def lambda_23F7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_23F7)

    def lambda_2404():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_2404)
    WaitChrThread(0x153, 2)
    OP_68(14500, 900, 0, 3000)
    MoveCamera(45, 20, 0, 3000)
    SetCameraDistance(18500, 3000)
    OP_6F(0x79)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)

    def lambda_2478():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2478)

    def lambda_2492():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2492)

    def lambda_24AC():
        OP_98(0xFE, 0x7530, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_24AC)

    def lambda_24C6():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_24C6)

    def lambda_24E0():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_24E0)

    def lambda_24FA():
        OP_98(0xFE, 0x88B8, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_24FA)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#5200304V#0010F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200305V#0108FWh-What are we going to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200306V#0310FWe're in one hell of a situation, eh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(31300, 900, 3200, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 32800, 0, 2400, 135)
    SetChrPos(0x102, 34500, 0, 4700, 90)
    SetChrPos(0x103, 29100, 0, 4700, 270)
    SetChrPos(0x104, 29800, 0, 2400, 225)
    SetChrPos(0x153, 32299, 0, 4800, 180)
    SetChrPos(0x158, 31300, 0, 4800, 180)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, 31800, 1000, 6000, 270)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x19, 20500, 0, 4600, 90)
    SetChrPos(0x1A, 19900, 0, 2000, 90)
    SetChrPos(0x1C, 23200, 0, -3600, 45)
    SetChrPos(0x1D, 29100, 0, -5400, 0)
    BeginChrThread(0x19, 3, 0, 34)
    BeginChrThread(0x1A, 3, 0, 35)
    BeginChrThread(0x1C, 3, 0, 36)
    BeginChrThread(0x1D, 3, 0, 37)
    SetChrPos(0xF, 43100, 0, 4600, 270)
    SetChrPos(0x10, 43700, 0, 2000, 270)
    SetChrPos(0x13, 40400, 0, -3600, 315)
    SetChrPos(0x14, 34500, 0, -5400, 0)
    BeginChrThread(0xF, 3, 0, 30)
    BeginChrThread(0x10, 3, 0, 31)
    BeginChrThread(0x13, 3, 0, 32)
    BeginChrThread(0x14, 3, 0, 33)
    MoveCamera(45, 19, 0, 2000)
    SetCameraDistance(20500, 2000)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1A, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1D, 3)
    OP_6F(0x79)

    ChrTalk(
        0x153,
        "#5200307V#5P#1101F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x158,
        "#5200308V#5P#6008FF-Father...help us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200309V#0008F#5P(Damn it! I have to do something\x01",
            "to protect these two!)\x02",
        )
    )

    CloseMessageWindow()
    Sound(490, 0, 80, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x158, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(460, 2, 100, 0)
    Sound(468, 2, 100, 0)

    def lambda_288B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_288B)
    Sleep(50)

    def lambda_289B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_289B)
    Sleep(50)

    def lambda_28AB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_28AB)
    Sleep(50)

    def lambda_28BB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_28BB)

    def lambda_28C8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x158, 2, lambda_28C8)
    WaitChrThread(0x153, 2)

    ChrTalk(
        0x101,
        "#5200310V#0005F#6PWait, what's that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200311V#0205F#6PAnother vehicle?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(491, 0, 100, 0)
    Fade(500)
    OP_68(143000, 900, 10, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x1F, 105500, 0, -2900, 0)
    SetChrPos(0x20, 113500, 0, 2900, 0)
    OP_68(133000, 900, 0, 2000)
    MoveCamera(45, 20, 0, 2000)
    SetCameraDistance(17000, 2000)
    BeginChrThread(0x101, 3, 0, 29)
    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2ABB():
        OP_96(0xFE, 0x20788, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2ABB)
    WaitChrThread(0x21, 1)
    OP_9F(0x0, 0x21)
    Sound(494, 0, 100, 0)
    OP_9F(0x1, 123900, 0, 0)
    OP_9F(0x1, 114300, 0, -1000)
    OP_9F(0x1, 105900, 0, 1000)
    OP_9F(0x2, 0x21, 11000, 0x6)
    OP_9F(0x0, 0x21)
    OP_9F(0x1, 91600, 0, 3500)
    OP_9F(0x1, 80300, 0, 0)
    OP_9F(0x2, 0x21, 11000, 0x6)
    Sound(493, 0, 100, 0)
    OP_24(0x1CC)
    OP_24(0x1D4)
    Fade(500)
    OP_68(47000, 900, -500, 0)
    MoveCamera(70, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 32500, 0, 2400, 135)
    SetChrPos(0x102, 33900, 0, 4700, 180)
    SetChrPos(0x103, 29700, 0, 4700, 135)
    SetChrPos(0x104, 30100, 0, 2400, 135)
    SetChrPos(0x153, 32299, 0, 4800, 135)
    SetChrPos(0x158, 31300, 0, 4800, 135)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 31800, 1000, 6000, 135)

    def lambda_2BFD():

        label("loc_2BFD")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2BFD")

    QueueWorkItem2(0xF, 2, lambda_2BFD)

    def lambda_2C0F():

        label("loc_2C0F")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2C0F")

    QueueWorkItem2(0x10, 2, lambda_2C0F)

    def lambda_2C21():

        label("loc_2C21")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2C21")

    QueueWorkItem2(0x13, 2, lambda_2C21)

    def lambda_2C33():

        label("loc_2C33")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_2C33")

    QueueWorkItem2(0x14, 2, lambda_2C33)
    BeginChrThread(0x10, 3, 0, 26)
    BeginChrThread(0x13, 3, 0, 28)
    BeginChrThread(0x14, 3, 0, 27)
    OP_68(38000, 900, -500, 3000)
    SetCameraDistance(18000, 3000)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    SetChrPos(0x21, 61000, 0, 500, 0)
    OP_D3(0x21, 0x0, 0x41EB0, 0x0, 0x0)
    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x2, 0x21, 0x40, 0, 0, 0, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2D43():
        OP_96(0xFE, 0xA028, 0x0, 0x1F4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2D43)
    WaitChrThread(0x21, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    Sound(495, 0, 100, 0)
    OP_82(0x12C, 0x0, 0xBB8, 0x258)

    def lambda_2D81():
        OP_9E(0xFE, 0xA028, 0xFFFFE69C, 0xFFFF8AD0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2D81)

    def lambda_2D9C():
        OP_D3(0xFE, 0x0, 0x35B60, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2D9C)
    BeginChrThread(0x21, 3, 0, 12)
    Sleep(300)
    SetMapObjFlags(0x7, 0x20)
    OP_71(0x7, 0x5B, 0x78, 0x0, 0x0)
    OP_24(0x1ED)
    WaitChrThread(0x21, 1)
    OP_79(0x7)
    OP_6F(0x79)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x10, 0x2)
    EndChrThread(0x14, 0x2)

    def lambda_2DE8():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2DE8)

    def lambda_2DF5():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2DF5)

    def lambda_2E02():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2E02)

    def lambda_2E0F():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_2E0F)
    OP_68(35000, 900, 2000, 1500)
    SetCameraDistance(19000, 1500)
    OP_6F(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x3)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E8A")

    ChrTalk(
        0x101,
        (
            "#5200312V#0005F#6PNo way! Isn't that Mr. Crois'\x01",
            "limousine?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECC")

    label("loc_2E8A")


    ChrTalk(
        0x102,
        (
            "#5200313V#0105F#5PY-You're right! I'd recognize it\x01",
            "anywhere!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ECC")

    OP_71(0x7, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x7)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)

    def lambda_2EF0():
        OP_96(0xFE, 0x8F5C, 0x96, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_2EF0)

    def lambda_2F0A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2F0A)
    WaitChrThread(0x23, 1)

    ChrTalk(
        0x23,
        "#5200314V#2901F#11PHurry up and get in the car!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200315V#0102F#5PYou're here, Bell!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200316V#6P#0011FWhat are you doing here, Mariabell?!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x22, 35900, 0, -1200, 315)
    SetChrFlags(0x22, 0x8)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)

    ChrTalk(
        0x22,
        (
            "#5200317V#2801FWe don't have time to talk!\x01",
            "Hurry on inside, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200318V#6P#0002FR-Right!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x153, 500)

    ChrTalk(
        0x101,
        "#5200319V#11P#0000FThis way, KeA!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    ChrTalk(
        0x153,
        "#5200320V#1102F#5POkay!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 24)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x0)
    TurnDirection(0x104, 0x158, 500)

    ChrTalk(
        0x104,
        "#5200321V#11P#0300FI got'cha, Shizuku!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x158, 0x104, 500)

    ChrTalk(
        0x158,
        "#5200322V#6000F#5PTh-Thank you.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x158, 3, 0, 25)
    OP_68(29000, 900, 500, 6000)
    MoveCamera(55, 17, 0, 6000)
    SetCameraDistance(21000, 6000)
    BeginChrThread(0x102, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x8, 3, 0, 17)

    def lambda_3149():
        OP_96(0xFE, 0x9088, 0x96, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_3149)

    def lambda_3163():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_3163)
    WaitChrThread(0x153, 3)
    BeginChrThread(0x101, 3, 0, 15)
    WaitChrThread(0x158, 3)
    BeginChrThread(0x104, 3, 0, 16)
    WaitChrThread(0x101, 3)
    Sound(470, 0, 100, 0)
    OP_71(0x7, 0x169, 0x186, 0x0, 0x0)
    WaitChrThread(0x104, 3)
    OP_93(0x21, 0xDC, 0x0)
    OP_71(0x7, 0x1E0, 0x1A5, 0x0, 0x20)

    def lambda_31B5():
        OP_9B(0x1, 0xFE, 0xB4, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_31B5)
    WaitChrThread(0x21, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sleep(300)

    def lambda_31E2():

        label("loc_31E2")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_31E2")

    QueueWorkItem2(0x1C, 2, lambda_31E2)
    Sound(490, 0, 100, 0)
    Sound(495, 0, 100, 0)
    OP_71(0x7, 0x1E1, 0x21C, 0x0, 0x20)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    def lambda_321D():
        OP_9E(0xFE, 0x7C38, 0x206C, 0xC350, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_321D)
    Sleep(800)
    BeginChrThread(0x1C, 3, 0, 14)
    WaitChrThread(0x21, 1)

    def lambda_3245():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3245)
    OP_6F(0x79)
    Fade(250)
    OP_68(15000, 900, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x19, 0x2)

    def lambda_3298():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3298)
    BeginChrThread(0x19, 3, 0, 13)
    BeginChrThread(0x24, 2, 0, 42)
    EndChrThread(0x1A, 0x2)

    def lambda_32B5():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_32B5)
    BeginChrThread(0x1A, 3, 0, 13)
    OP_68(5000, 900, 0, 4000)
    SetCameraDistance(21000, 4000)
    Sleep(1000)
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x0)

    def lambda_32ED():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_32ED)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x21, 0xFF)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x1A, 0xFF)
    EndChrThread(0x1C, 0xFF)
    EndChrThread(0x24, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetChrChipPat(0x0, 0x1, 0x0)
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1CC)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_18FC end

    def Function_12_336D(): pass

    label("Function_12_336D")

    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 43300, 0, 500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 42000, 0, 1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 40500, 0, 1500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 39000, 0, 2000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 37500, 0, 2300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_12_336D end

    def Function_13_348D(): pass

    label("Function_13_348D")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    label("loc_3498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35EE")

    def lambda_34A8():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_34A8)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("loc_3498")

    label("loc_35EE")

    Return()

    # Function_13_348D end

    def Function_14_35EF(): pass

    label("Function_14_35EF")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x1C, 0x2A)
    SetChrSubChip(0x1C, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_360D():
        OP_9D(0xFE, 0x61A8, 0x0, 0x320, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_360D)
    WaitChrThread(0x1C, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_35EF end

    def Function_15_363D(): pass

    label("Function_15_363D")

    OP_92(0x101, 0x8B10, 0x320, 0x1F4)

    def lambda_364F():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_364F)
    WaitChrThread(0x101, 1)
    SetChrFlags(0x101, 0x4)

    def lambda_3672():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3672)

    def lambda_368C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_368C)
    WaitChrThread(0x101, 1)
    Return()

    # Function_15_363D end

    def Function_16_369D(): pass

    label("Function_16_369D")

    OP_92(0x104, 0x8B10, 0x320, 0x1F4)

    def lambda_36AF():
        OP_95(0xFE, 35600, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36AF)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x104, 0x4)

    def lambda_36D2():
        OP_95(0xFE, 37000, 150, -100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36D2)

    def lambda_36EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_36EC)
    WaitChrThread(0x104, 1)
    Return()

    # Function_16_369D end

    def Function_17_36FD(): pass

    label("Function_17_36FD")

    Sleep(1000)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3723():
        OP_92(0xFE, 0x6BD0, 0x1A2C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3723)
    SetChrChip(0x0, 0x8, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_3744():
        OP_9D(0xFE, 0x6BD0, 0x3E8, 0x1A2C, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3744)
    Sleep(350)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_37AA():
        OP_92(0xFE, 0x55F0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_37AA)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x0)

    def lambda_37C5():

        label("loc_37C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37C5")

    QueueWorkItem2(0x19, 2, lambda_37C5)

    def lambda_37D7():

        label("loc_37D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_37D7")

    QueueWorkItem2(0x1A, 2, lambda_37D7)
    Sleep(3500)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_3801():
        OP_9D(0xFE, 0x55F0, 0x0, 0x708, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3801)
    Sleep(550)
    SetChrSubChip(0x8, 0x1)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    WaitChrThread(0x8, 1)
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3867():
        OP_92(0xFE, 0x4268, 0xFFFFF704, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3867)
    SetChrSubChip(0x8, 0x3)
    Sleep(50)
    SetChrSubChip(0x8, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_388B():
        OP_9D(0xFE, 0x4268, 0x76C, 0xFFFFF704, 0xA28, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_388B)
    Sleep(400)
    WaitChrThread(0x8, 1)
    Sound(925, 0, 100, 0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x8, 0x0, 0x0)

    def lambda_38D3():
        OP_98(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_38D3)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3921():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3921)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_36FD end

    def Function_18_394C(): pass

    label("Function_18_394C")

    OP_93(0x102, 0x6E, 0x1F4)
    SetChrChipByIndex(0x102, 0x34)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    BeginChrThread(0xF, 3, 0, 20)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    BeginChrThread(0x10, 3, 0, 20)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x18)
    SetChrSubChip(0x102, 0x0)
    Sleep(400)

    def lambda_3A5C():
        OP_95(0xFE, 37800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A5C)
    WaitChrThread(0x102, 1)
    SetChrFlags(0x102, 0x4)

    def lambda_3A7F():
        OP_95(0xFE, 39000, 150, 2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A7F)

    def lambda_3A99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A99)
    WaitChrThread(0x102, 1)
    Return()

    # Function_18_394C end

    def Function_19_3AAA(): pass

    label("Function_19_3AAA")

    OP_93(0x103, 0xB4, 0x1F4)
    SetChrChipByIndex(0x103, 0x35)
    SetChrSubChip(0x103, 0x0)
    PlayEffect(0x1, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(831, 0, 100, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0x103, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 80, 0)
    SetChrSubChip(0x103, 0x3)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 39600, 0, -4200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x13, 3, 0, 21)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 31400, 0, -4700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 0, 22)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 29100, 0, -2400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x1D, 3, 0, 23)
    SetChrSubChip(0x103, 0x4)
    Sleep(1200)
    SetChrChipByIndex(0x103, 0x1A)
    SetChrSubChip(0x103, 0x0)

    def lambda_3C2F():
        OP_95(0xFE, 32200, 0, 400, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C2F)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x103, 0x4)

    def lambda_3C52():
        OP_95(0xFE, 31200, 150, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C52)

    def lambda_3C6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C6C)
    WaitChrThread(0x103, 1)
    Return()

    # Function_19_3AAA end

    def Function_20_3C7D(): pass

    label("Function_20_3C7D")

    OP_93(0xFE, 0x10E, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_3CD3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CD3)

    def lambda_3CEC():
        OP_9C(0xFE, 0xFA0, 0x0, 0x190, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CEC)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_20_3C7D end

    def Function_21_3D22(): pass

    label("Function_21_3D22")

    Sleep(1100)
    OP_93(0xFE, 0x13B, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D44():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D44)

    def lambda_3D5D():
        OP_9D(0xFE, 0xA0F0, 0x0, 0xFFFFEA20, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D5D)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_21_3D22 end

    def Function_22_3D93(): pass

    label("Function_22_3D93")

    Sleep(1100)
    OP_93(0xFE, 0x0, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3DB5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DB5)

    def lambda_3DCE():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEB4C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DCE)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_3D93 end

    def Function_23_3E04(): pass

    label("Function_23_3E04")

    Sleep(1100)
    OP_93(0xFE, 0x2D, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E26():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E26)

    def lambda_3E3F():
        OP_9D(0xFE, 0x6C34, 0x0, 0xFFFFEE08, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E3F)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_3E04 end

    def Function_24_3E6F(): pass

    label("Function_24_3E6F")


    def lambda_3E74():
        OP_99(0xFE, 0x101, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3E74)
    WaitChrThread(0x153, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x153, 0x80)
    SetChrBattleFlags(0x153, 0x8000)
    OP_0D()
    Return()

    # Function_24_3E6F end

    def Function_25_3EA6(): pass

    label("Function_25_3EA6")


    def lambda_3EAB():
        OP_99(0xFE, 0x104, 0x320, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x158, 1, lambda_3EAB)
    WaitChrThread(0x158, 1)
    Fade(250)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x158, 0x80)
    SetChrBattleFlags(0x158, 0x8000)
    OP_0D()
    Return()

    # Function_25_3EA6 end

    def Function_26_3EDD(): pass

    label("Function_26_3EDD")

    Sleep(1300)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3EFE():
        OP_9D(0xFE, 0xA5A0, 0x0, 0xFA0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EFE)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_3EDD end

    def Function_27_3F2E(): pass

    label("Function_27_3F2E")

    Sleep(1800)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x1)

    def lambda_3F49():
        OP_9D(0xFE, 0x7AA8, 0x0, 0xFFFFEDA4, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3F49)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_3F2E end

    def Function_28_3F79(): pass

    label("Function_28_3F79")

    Sleep(1600)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_3F9A():
        OP_9D(0xFE, 0x9AB0, 0x0, 0xFFFFEF98, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3F9A)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_3F79 end

    def Function_29_3FCA(): pass

    label("Function_29_3FCA")

    OP_6F(0x79)
    Fade(250)
    OP_68(117700, 900, 0, 0)
    MoveCamera(65, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_68(102000, 900, -400, 4000)
    MoveCamera(35, 27, 0, 4000)
    SetCameraDistance(18000, 4000)
    OP_6F(0x79)
    Return()

    # Function_29_3FCA end

    def Function_30_4027(): pass

    label("Function_30_4027")


    def lambda_402C():
        OP_95(0xFE, 39100, 0, 4600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_402C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_30_4027 end

    def Function_31_404E(): pass

    label("Function_31_404E")


    def lambda_4053():
        OP_95(0xFE, 39700, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4053)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_31_404E end

    def Function_32_4075(): pass

    label("Function_32_4075")


    def lambda_407A():
        OP_95(0xFE, 37900, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_407A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    Return()

    # Function_32_4075 end

    def Function_33_409C(): pass

    label("Function_33_409C")


    def lambda_40A1():
        OP_95(0xFE, 34500, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40A1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_33_409C end

    def Function_34_40C3(): pass

    label("Function_34_40C3")


    def lambda_40C8():
        OP_95(0xFE, 24500, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40C8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x0)
    Return()

    # Function_34_40C3 end

    def Function_35_40EA(): pass

    label("Function_35_40EA")


    def lambda_40EF():
        OP_95(0xFE, 23900, 0, 2000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40EF)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x0)
    Return()

    # Function_35_40EA end

    def Function_36_4111(): pass

    label("Function_36_4111")


    def lambda_4116():
        OP_95(0xFE, 25700, 0, -1100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4116)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    Return()

    # Function_36_4111 end

    def Function_37_4138(): pass

    label("Function_37_4138")


    def lambda_413D():
        OP_95(0xFE, 29100, 0, -2400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_413D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x0)
    Return()

    # Function_37_4138 end

    def Function_38_415F(): pass

    label("Function_38_415F")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)

    def lambda_416C():
        OP_95(0xFE, 113100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_416C)

    def lambda_4186():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4186)
    WaitChrThread(0xFE, 1)

    def lambda_419B():
        OP_95(0xFE, 100100, 0, 400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_419B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_415F end

    def Function_39_41B5(): pass

    label("Function_39_41B5")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_41C2():
        OP_95(0xFE, 111100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41C2)

    def lambda_41DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41DC)
    WaitChrThread(0xFE, 1)

    def lambda_41F1():
        OP_95(0xFE, 100100, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41F1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_41B5 end

    def Function_40_420B(): pass

    label("Function_40_420B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4224")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_40_420B")

    label("loc_4224")

    Return()

    # Function_40_420B end

    def Function_41_4225(): pass

    label("Function_41_4225")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423E")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_41_4225")

    label("loc_423E")

    Return()

    # Function_41_4225 end

    def Function_42_423F(): pass

    label("Function_42_423F")

    Sleep(500)

    label("loc_4242")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_425B")
    Sound(957, 0, 100, 0)
    Sleep(1200)
    Jump("loc_4242")

    label("loc_425B")

    Return()

    # Function_42_423F end

    def Function_43_425C(): pass

    label("Function_43_425C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31053.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x21)
    LoadChrToIndex("chr/ch31151.itc", 0x22)
    LoadChrToIndex("chr/ch31153.itc", 0x23)
    LoadChrToIndex("chr/ch31950.itc", 0x24)
    LoadChrToIndex("chr/ch31951.itc", 0x25)
    LoadChrToIndex("chr/ch31953.itc", 0x26)
    LoadChrToIndex("chr/ch31152.itc", 0x27)
    LoadChrToIndex("chr/ch31952.itc", 0x28)
    LoadEffect(0x0, "battle\\btgun00.eff")
    LoadEffect(0x1, "event\\eva03_01.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    LoadEffect(0x3, "event\\ev606_00.eff")
    LoadEffect(0x4, "event\\eva01_00.eff")
    OP_68(71000, 500, 0, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27500, 0)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0xC, 53500, 0, 2900, 180)
    SetChrPos(0x16, 53500, 0, 1300, 0)
    SetChrPos(0xF, 66500, 0, -900, 90)
    SetChrPos(0x10, 66500, 0, -2100, 90)
    SetChrPos(0x11, 65400, 0, -900, 90)
    SetChrPos(0x12, 65400, 0, -2100, 90)
    SetChrPos(0x13, 68600, 0, -1500, 270)
    SetChrPos(0xD, 78000, 0, 900, 90)
    SetChrPos(0xE, 78000, 0, -900, 90)
    SetChrPos(0x14, 58000, 0, 3000, 180)
    SetChrPos(0x15, 58000, 0, 4500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_78(0x5, 0x1F)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1F, 0x4)
    OP_49()
    SetChrPos(0x1F, 56000, 0, 2400, 0)
    OP_D3(0x1F, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    OP_78(0x6, 0x20)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x20, 0x4)
    OP_49()
    SetChrPos(0x20, 71000, 0, -2400, 0)
    OP_D3(0x20, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x0)
    OP_78(0x7, 0x21)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "bul00", 0x0, 0x1)
    SetMapObjFrame(0x7, "bul01", 0x0, 0x1)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x21, 0x4)
    OP_49()
    SetChrPos(0x21, -10000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0xB5, 0xF0, 0x0, 0x20)
    OP_E5()
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe same day, 11:30PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7527", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(59000, 500, 0, 7000)
    SetCameraDistance(30500, 7000)
    FadeToBright(2000, 0)
    Sleep(4000)
    BeginChrThread(0x14, 3, 0, 56)
    BeginChrThread(0x15, 3, 0, 56)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x14, 20000, 0, 900, 270)
    SetChrPos(0x15, 20000, 0, -900, 270)
    Sound(490, 0, 100, 0)
    Sleep(3500)
    OP_68(9500, 500, 0, 0)
    MoveCamera(63, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayEffect(0x1, 0x0, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x21, 3, 0, 57)
    BeginChrThread(0x101, 3, 0, 58)
    OP_68(17500, 500, 0, 3500)
    SetCameraDistance(21000, 3500)
    Sound(493, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    CancelBlur(2000)
    BeginChrThread(0x14, 3, 0, 44)
    BeginChrThread(0x15, 3, 0, 47)
    BeginChrThread(0x24, 1, 0, 61)
    OP_6F(0x79)
    Fade(250)
    OP_68(48500, 500, 0, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)

    def lambda_485D():

        label("loc_485D")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_485D")

    QueueWorkItem2(0xC, 2, lambda_485D)

    def lambda_486F():

        label("loc_486F")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_486F")

    QueueWorkItem2(0x16, 2, lambda_486F)
    BeginChrThread(0xC, 0, 0, 55)
    BeginChrThread(0x16, 0, 0, 53)
    OP_68(63500, 500, 0, 2500)
    MoveCamera(47, 15, 0, 2500)
    SetCameraDistance(21000, 2500)
    Sound(491, 0, 100, 0)

    def lambda_48B8():

        label("loc_48B8")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_48B8")

    QueueWorkItem2(0x13, 2, lambda_48B8)
    BeginChrThread(0x13, 0, 0, 53)
    BeginChrThread(0x11, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 52)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 52)
    Sound(494, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    Fade(250)
    OP_68(65500, 0, 0, 0)
    MoveCamera(290, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x24, 0x1)
    BeginChrThread(0xD, 3, 0, 50)
    BeginChrThread(0xE, 3, 0, 51)
    BeginChrThread(0x24, 0, 0, 62)
    Sound(495, 0, 100, 0)
    Sound(491, 0, 100, 0)
    MoveCamera(305, 20, 0, 4000)
    SetCameraDistance(27000, 4000)
    OP_68(73500, 0, 2000, 1000)
    OP_6F(0x1)
    OP_68(88500, 0, 0, 3000)
    OP_6F(0x79)
    EndChrThread(0x21, 0x1)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Sound(490, 0, 100, 0)
    Fade(500)
    OP_68(90500, 500, 0, 0)
    MoveCamera(90, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x21, 70000, 0, 0, 0)
    OP_D3(0x21, 0x0, 0x15F90, 0x0, 0x0)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    PlayEffect(0x1, 0x0, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x21, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2500)

    def lambda_4AC5():
        OP_98(0xFE, 0x13880, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4AC5)
    MoveCamera(90, 17, 0, 5000)
    SetCameraDistance(24000, 5000)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    EndChrThread(0x24, 0x0)
    Sleep(1500)
    OP_E6()
    SetScenarioFlags(0x5C, 1)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_425C end

    def Function_44_4B1C(): pass

    label("Function_44_4B1C")

    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4B39():

        label("loc_4B39")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_4B39")

    QueueWorkItem2(0x14, 2, lambda_4B39)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_4B67():
        OP_9D(0xFE, 0x5014, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B67)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 45)
    Return()

    # Function_44_4B1C end

    def Function_45_4BA3(): pass

    label("Function_45_4BA3")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 18900, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19200, 0, -1900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19700, 0, -1500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20600, 0, -800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 21900, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 23800, 0, -2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 26100, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 29000, 0, -2200, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_45_4BA3 end

    def Function_46_4D71(): pass

    label("Function_46_4D71")

    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 77900, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 78200, 0, -2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, -500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, -1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, -500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 83700, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 86000, 0, -3100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 88300, 0, -2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 90800, 0, -1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 95000, 0, -2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_46_4D71 end

    def Function_47_4FF0(): pass

    label("Function_47_4FF0")

    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_500D():

        label("loc_500D")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_500D")

    QueueWorkItem2(0x15, 2, lambda_500D)
    Sleep(900)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_5035():
        OP_9D(0xFE, 0x5014, 0x32, 0xFFFFF0C4, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5035)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 53)
    BeginChrThread(0xFE, 1, 0, 48)
    Return()

    # Function_47_4FF0 end

    def Function_48_5071(): pass

    label("Function_48_5071")

    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 18900, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19200, 0, 1900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 19700, 0, 1500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 20600, 0, 800, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 21900, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 23800, 0, 2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 26100, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 29000, 0, 2200, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_48_5071 end

    def Function_49_523F(): pass

    label("Function_49_523F")

    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 77900, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 78200, 0, 2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, 500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 79400, 0, 1100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 81000, 0, 500, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 83700, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 86000, 0, 3100, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 88300, 0, 2400, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 90800, 0, 1600, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 95000, 0, 2900, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_49_523F end

    def Function_50_54BE(): pass

    label("Function_50_54BE")


    def lambda_54C3():

        label("loc_54C3")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_54C3")

    QueueWorkItem2(0xD, 2, lambda_54C3)
    Sleep(1000)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_54F1():
        OP_9D(0xFE, 0x13498, 0x32, 0xB54, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_54F1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 1, 0, 49)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_50_54BE end

    def Function_51_552D(): pass

    label("Function_51_552D")


    def lambda_5532():

        label("loc_5532")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_5532")

    QueueWorkItem2(0xE, 2, lambda_5532)
    Sleep(1100)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x1)

    def lambda_555A():
        OP_9D(0xFE, 0x132A4, 0x32, 0xFFFFF4AC, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_555A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 1, 0, 46)
    BeginChrThread(0xFE, 3, 0, 53)
    Return()

    # Function_51_552D end

    def Function_52_5596(): pass

    label("Function_52_5596")

    OP_93(0xFE, 0x10E, 0x0)
    BeginChrThread(0xFE, 0, 0, 55)
    Sleep(2250)
    EndChrThread(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0xFE, 0x10E, 0x2BC)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_55C9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_55C9)
    Sound(814, 0, 100, 0)

    def lambda_55E8():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFF63C, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55E8)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_52_5596 end

    def Function_53_5618(): pass

    label("Function_53_5618")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    BeginChrThread(0xFE, 0, 0, 54)

    label("loc_5637")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_566E")

    def lambda_5647():
        OP_A6(0xFE, 0x0, 0x1E, 0x3C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5647)
    SetChrSubChip(0xFE, 0x3)
    Sleep(30)
    SetChrSubChip(0xFE, 0x2)
    Sleep(30)
    Jump("loc_5637")

    label("loc_566E")

    Return()

    # Function_53_5618 end

    def Function_54_566F(): pass

    label("Function_54_566F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B9")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Jump("Function_54_566F")

    label("loc_56B9")

    Return()

    # Function_54_566F end

    def Function_55_56BA(): pass

    label("Function_55_56BA")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    label("loc_56CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5741")
    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 900, 900, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)

    def lambda_5713():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5713)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Jump("loc_56CC")

    label("loc_5741")

    Return()

    # Function_55_56BA end

    def Function_56_5742(): pass

    label("Function_56_5742")


    def lambda_5747():
        OP_95(0xFE, 58000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5747)
    WaitChrThread(0xFE, 1)

    def lambda_5765():
        OP_95(0xFE, 48000, 0, -600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5765)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_5742 end

    def Function_57_577F(): pass

    label("Function_57_577F")


    def lambda_5784():
        OP_95(0xFE, 56000, 0, -3000, 13000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5784)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 59)

    def lambda_57BA():
        OP_9E(0xFE, 0xE290, 0x1B58, 0xFFFF5038, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_57BA)

    def lambda_57D5():
        OP_D3(0xFE, 0x0, 0xAFC8, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_57D5)
    WaitChrThread(0x21, 2)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)

    def lambda_5803():
        OP_D3(0xFE, 0x0, 0xEA60, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_5803)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x3C, 0x0)

    def lambda_582C():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_582C)
    WaitChrThread(0x21, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 60)

    def lambda_585D():
        OP_9E(0xFE, 0x11B34, 0xFFFFF060, 0xC350, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_585D)

    def lambda_5878():
        OP_D3(0xFE, 0x0, 0x1E848, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_5878)
    Sleep(400)
    OP_82(0x12C, 0x0, 0xBB8, 0xFA)
    WaitChrThread(0x21, 1)
    CancelBlur(1000)
    OP_93(0x21, 0x7D, 0x0)

    def lambda_58B5():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_58B5)
    WaitChrThread(0x21, 1)

    def lambda_58CE():
        OP_9E(0xFE, 0x13C68, 0x30D4, 0xFFFF6F78, 0x2710, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_58CE)
    WaitChrThread(0x21, 1)

    def lambda_58ED():
        OP_96(0xFE, 0x27100, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_58ED)
    Return()

    # Function_57_577F end

    def Function_58_5903(): pass

    label("Function_58_5903")

    Sleep(2200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3000, 1500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3000, 1600, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1200, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1700, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1000, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 2000, 1500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 1000, 1000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1100, -900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 0, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1500, -700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1000, 1000, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 3500, 1100, -1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, 0, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -500, 1700, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1000, 1500, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -1500, 1400, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -2500, 1100, -1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1700, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x40, -3500, 1500, -1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_58_5903 end

    def Function_59_5E3A(): pass

    label("Function_59_5E3A")

    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 54200, 0, -3700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 55900, 0, -4700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 57600, 0, -5400, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 59500, 0, -4700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 62100, 0, -3800, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_59_5E3A end

    def Function_60_5F5A(): pass

    label("Function_60_5F5A")

    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 63200, 0, 2600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 64800, 0, 3600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 66600, 0, 4500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 68300, 0, 5300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 70400, 0, 5600, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_60_5F5A end

    def Function_61_607A(): pass

    label("Function_61_607A")

    Sleep(1600)
    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(3500)
    EndChrThread(0x24, 0x3)
    Sleep(500)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_61_607A end

    def Function_62_6098(): pass

    label("Function_62_6098")

    BeginChrThread(0x24, 2, 0, 63)
    BeginChrThread(0x24, 3, 0, 64)
    Sleep(4000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x2)
    Return()

    # Function_62_6098 end

    def Function_63_60B0(): pass

    label("Function_63_60B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60C9")
    Sound(355, 0, 90, 0)
    Sleep(600)
    Jump("Function_63_60B0")

    label("loc_60C9")

    Return()

    # Function_63_60B0 end

    def Function_64_60CA(): pass

    label("Function_64_60CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60E9")
    Sound(956, 0, 90, 0)
    Sound(957, 0, 90, 0)
    Sleep(1100)
    Jump("Function_64_60CA")

    label("loc_60E9")

    Return()

    # Function_64_60CA end

    SaveToFile()

Try(main)
