from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r308e.bin",                # FileName
        "r308e",                    # MapName
        "r308e",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -74000, 0, -2000, 0, 0, 1, 101, 0, 2, 0, 3],
    )

    BuildStringList((
        "r308e",                  # 0
        "KeA",                    # 1
        "Chief Sergei",           # 2
        "Zeit",                   # 3
        "Detective Dudley",       # 4
        "Arios",                  # 5
        "Sergeant Major Seeker",  # 6
        "Deputy Commander Baelz", # 7
        "Renne",                  # 8
        "Grace",                  # 9
        "Reins",                  # 10
        "車１",                   # 11
        "車２",                   # 12
        "車３",                   # 13
        "車４",                   # 14
    ))

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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_2D8",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_317",          # 02, 2
        "Function_3_33B",          # 03, 3
        "Function_4_33C",          # 04, 4
        "Function_5_21E6",         # 05, 5
        "Function_6_2205",         # 06, 6
        "Function_7_222B",         # 07, 7
        "Function_8_2251",         # 08, 8
        "Function_9_2277",         # 09, 9
        "Function_10_22BF",        # 0A, 10
        "Function_11_2315",        # 0B, 11
        "Function_12_2334",        # 0C, 12
        "Function_13_2361",        # 0D, 13
        "Function_14_2387",        # 0E, 14
        "Function_15_23AD",        # 0F, 15
        "Function_16_23D3",        # 10, 16
    ))


    def Function_0_2D8(): pass

    label("Function_0_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F9")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sound(832, 0, 100, 0)
    Jump("Function_0_2D8")

    label("loc_2F9")

    Return()

    # Function_0_2D8 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_316")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_1_2FA")

    label("loc_316")

    Return()

    # Function_1_2FA end

    def Function_2_317(): pass

    label("Function_2_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_32B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_33A")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_33A")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 16)

    label("loc_33A")

    Return()

    # Function_2_317 end

    def Function_3_33B(): pass

    label("Function_3_33B")

    Return()

    # Function_3_33B end

    def Function_4_33C(): pass

    label("Function_4_33C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("apl/ch50520.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch00900.itc", 0x21)
    LoadChrToIndex("chr/ch02400.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch05700.itc", 0x24)
    LoadChrToIndex("chr/ch09500.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("apl/ch50378.itc", 0x27)
    LoadChrToIndex("chr/ch08201.itc", 0x28)
    LoadChrToIndex("apl/ch50380.itc", 0x29)
    LoadChrToIndex("chr/ch02751.itc", 0x2A)
    LoadChrToIndex("apl/ch50314.itc", 0x2B)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis105.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01102.itp")
    OP_68(48100, 22100, -2000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 56000, 20000, -2000, 270)
    SetChrPos(0x103, 57100, 20000, -2900, 270)
    SetChrPos(0x102, 57100, 20000, -1100, 270)
    SetChrPos(0x104, 58200, 20000, -2000, 270)
    SetChrPos(0x107, 32400, 20000, -1600, 270)
    SetChrPos(0x108, 32400, 20000, -3400, 270)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x108, 0x8)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 32400, 20000, -2500, 270)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    OP_90(0x8, 6300, 11700, -2000, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x8000)
    OP_90(0x9, 6600, 11800, -1400, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    OP_90(0xA, 5900, 11450, 400, 90)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    OP_90(0xB, 6200, 11650, -2200, 90)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    OP_90(0xC, 4100, 10600, -300, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    OP_90(0xD, 5400, 11250, -4200, 90)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    OP_90(0xE, 5400, 11250, -3400, 90)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    OP_90(0x10, 8100, 12540, -2000, 90)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    OP_90(0x11, 7600, 12320, -1100, 90)

    def lambda_621():
        OP_96(0xFE, 0xB798, 0x4E20, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_621)
    Sleep(50)

    def lambda_63E():
        OP_96(0xFE, 0xBBE4, 0x4E20, 0xFFFFFBB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63E)
    Sleep(50)

    def lambda_65B():
        OP_96(0xFE, 0xBBE4, 0x4E20, 0xFFFFF4AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65B)
    Sleep(50)

    def lambda_678():
        OP_96(0xFE, 0xC030, 0x4E20, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_678)
    Sound(829, 0, 100, 0)
    OP_68(48100, 21100, -2000, 4500)
    MoveCamera(30, 17, 0, 4500)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x41)

    ChrTalk(
        0x101,
        "#5301068V#11P#0002F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5301022V#0102F#11PThe sunrise...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301023V#0202F#11PIt's beautiful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5301024V#0304F#11PFor real. The warmth feels amazin', too.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 36150, 21000, -2410, 100)
    Sound(2042, 255, 90, 0)

    NpcTalk(
        0x8,
        "Girl's Voice",
        "#5301025V#2P#24ALlooooyd!\x02",
    )

    Sleep(1800)
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
    ClearChrFlags(0x8, 0x4)

    ChrTalk(
        0x101,
        "#5301026V#0005F#11PWait, that voice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301027V#0205F#11PIt can't be!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(11300, 15100, -2000, 0)
    MoveCamera(35, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 32000, 20000, -2000, 270)
    SetChrPos(0x102, 32400, 20000, -3100, 270)
    SetChrPos(0x103, 32200, 20000, -400, 270)
    SetChrPos(0x104, 33600, 20000, -600, 270)
    OP_90(0x8, 6300, 11700, -2000, 90)
    BeginChrThread(0x8, 3, 0, 9)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 8)
    Sleep(900)
    OP_68(19330, 17100, -2040, 1500)
    MoveCamera(58, 20, 0, 1500)
    SetCameraDistance(18000, 1500)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0xA, 3, 0, 10)
    Sleep(50)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    BeginChrThread(0x9, 3, 0, 12)
    Sleep(50)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(400)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    BeginChrThread(0xE, 3, 0, 14)
    Sleep(50)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 3, 0, 15)
    Sleep(400)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(500)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x108, 0x8)
    ClearChrFlags(0xF, 0x8)

    def lambda_9ED():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF9C0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9ED)
    Sleep(100)

    def lambda_A0A():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF2B8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A0A)
    Sleep(300)

    def lambda_A27():
        OP_96(0xFE, 0x5780, 0x3E80, 0xFFFFF63C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A27)
    WaitChrThread(0x8, 3)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 70, 0)
    OP_6F(0x79)
    SetCameraDistance(17000, 80000)

    ChrTalk(
        0x101,
        "#5301028V#11P#0011FKeA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5301029V#6P#1114FMmm!\x02",
    )

    CloseMessageWindow()
    Sound(910, 0, 100, 0)

    def lambda_A9B():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A9B)

    def lambda_AB4():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AB4)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    Sound(804, 0, 70, 0)
    Sleep(300)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#5301030VThank goodness!\x02\x03",
            "#5301031VLloyd, Elie, Tio, Randy... You're all okay!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    WaitChrThread(0xA, 3)

    ChrTalk(
        0xA,
        "#5301032V#1200FGrrrrr...woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5301033V#0102F#11PWhat are you doing here, KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5301034V#5P#0309FHaha. Looks like we got ourselves\x01",
            "a whole slew of visitors.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    ChrTalk(
        0xC,
        (
            "#5301035V#6P#1404FAll of the CGF troops within the city\x01",
            "fainted only moments ago.\x02\x03",
            "#5301036V#1402FSo naturally, we took her and left\x01",
            "as quickly as we could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5301037V#6P#0606FThe four of you need to teach her some manners.\x01",
            "She wouldn't stop throwing a tantrum until we\x01",
            "agreed to bring her with us.\x02\x03",
            "#5301038V#0601FHmph. I suppose it's no surprise to see why she\x01",
            "meshes with you all so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5301039V#6P#1004FHah. You say that, but how very much\x01",
            "like you to comply.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0xB,
        "#5301040V#12P#0605FS-Sergei!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5301041V#11P#0009FHaha...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_96(0x8, 0x4B64, 0x3E80, 0xFFFFF830, 0x3E8, 0x0)
    Sleep(300)
    TurnDirection(0x101, 0xE, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5301042V#5P#0002FOh! You're here, too, Deputy Commander\x01",
            "Baelz and Sergeant Major Seeker.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F08():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F08)
    Sleep(50)

    def lambda_F18():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F18)
    Sleep(300)

    ChrTalk(
        0xD,
        "#5301043V#12P#0502FGreat job in there, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5301044V#6P#2004FEveryone in the CGF has finally been\x01",
            "freed thanks to your efforts.\x02\x03",
            "#5301045V#2002FAnd thus, we decided to come visit you.\x01",
            "Has the danger subsided?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5301046V#5P#0004FYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5301047V#0204F#5PAll of the fiends within the fort\x01",
            "have vanished, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5301048V#5P#0300FGood thing, too. Made escortin' everyone\x01",
            "out a helluva lot easier.\x02\x03",
            "#5301049V#0306FMan, tyin' up those mafiosos and leaving\x01",
            "'em in those cells felt good, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5301050V#0108F#11PStill, I feel as if the situation will only\x01",
            "continue to become more complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5301051V#6P#2006FIndeed. We'll need to provide an explanation\x01",
            "to the citizenry and brace ourselves for\x01",
            "potential international backlash.\x02\x03",
            "#5301052V#2001FWe must also administer the proper care\x01",
            "to any CGF members that were affected\x01",
            "by the brainwashing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5301053V#12P#0501FThe mafia members will probably have\x01",
            "to be restrained for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5301054V#6P#0603FNot to mention, we still have to assemble\x01",
            "the trail of evidence linked to this case.\x02\x03",
            "#5301055V#0601FYou can kiss your free time for the next\x01",
            "month goodbye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5301056V#6P#1402FHaha. Please allow the Bracer Guild\x01",
            "to assist you in your endeavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5301057V#6P#0604FWe appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301058V#0202F#5PHeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5301059V#5P#0304FThis sounds friggin' lame. I don't wanna\x01",
            "get worked to death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5301060V#0109F#11PHowever, I think the situation has finally\x01",
            "taken a turn for the better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5301061V#5P#0002F...Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5301087V#6P#1109FUh-huh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5301063V#1200FWoof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5301064V#6P#1002FHaha...\x02\x03",
            "#5301065V#1003FLloyd, Elie, Tio, Randy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_15F9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_15F9)
    Sleep(50)

    def lambda_1609():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1609)
    Sleep(50)

    def lambda_1619():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1619)
    Sleep(50)

    def lambda_1629():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1629)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5301066V#6P#1003FI'll need that report of yours at\x01",
            "some point...but take your time.\x02\x03",
            "#5301067V#1002FFor now, have you settled all of\x01",
            "your business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5301021V#11P#0005FOh...\x02",
    )

    CloseMessageWindow()

    def lambda_16F1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16F1)
    Sleep(100)

    def lambda_1701():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1701)
    Sleep(1300)

    def lambda_1711():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1711)
    Sleep(100)

    def lambda_1721():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1721)
    Sleep(50)

    def lambda_1731():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1731)
    Sleep(1500)

    def lambda_1741():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1741)
    Sleep(50)

    def lambda_1751():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1751)
    Sleep(50)

    def lambda_1761():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1761)
    Sleep(50)

    def lambda_1771():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1771)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Everyone")
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    AnonymousTalk(
        0xFF,
        "#5301069V#5SYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x9,
        (
            "#5301073V#6P#1004FHaha... Good work, team.\x02\x03",
            "#5301074VI have to admit, you guys have\x01",
            "really matured.\x02\x03",
            "#5301075V#1002FGuy would have been proud of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5301076V#11P#0005FChief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5301077V#3P#1402F...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)

    NpcTalk(
        0x10,
        "Woman's Voice",
        (
            "#5301078VThe camera has arrived, everyone!\x01",
            "Step aside, folks! Outta my way!\x02",
        )
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
    SetCameraDistance(18000, 2000)
    OP_68(17710, 17100, -1790, 2000)
    MoveCamera(50, 20, 0, 2000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    def lambda_1996():
        OP_96(0xFE, 0x37DC, 0x3D2C, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1996)
    Sleep(100)

    def lambda_19B3():
        OP_96(0xFE, 0x35E8, 0x3C46, 0xFFFFFBB4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19B3)

    def lambda_19CD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_19CD)
    Sleep(50)

    def lambda_19DD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_19DD)
    Sleep(50)

    def lambda_19ED():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_19ED)
    Sleep(50)

    def lambda_19FD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19FD)
    Sleep(50)

    def lambda_1A0D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A0D)
    Sleep(50)

    def lambda_1A1D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1A1D)
    Sleep(50)

    def lambda_1A2D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1A2D)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    OP_6F(0x41)

    ChrTalk(
        0x101,
        "#5301079V#0011F#11PGrace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5301080V#0105F#11PEven you're here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5301081V#2109F#6P#NYou think I'd let a scoop THIS juicy escape\x01",
            "my clutches? Hah! Get real!\x02\x03",
            "#5301082V#2102FAnyway, I'm going to need you all together\x01",
            "nice and tightly! I think this whole situation\x01",
            "calls for a group photo!\x02\x03",
            "#5301083VC'mon, people! No need to be shy!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x9,
        "#5301084V#1006F#11PThere's no stopping this lady, is there?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "#5301085V#5P#1110FWe're going to be in a picture?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5301086V#0002F#11PYeah, so give her your biggest smile,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5301062V#5P#1109FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5301088V#11P#0202F#NShall we join them, Zeit?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0xA, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0xA,
        "#5301089V#5P#1200FGrrrr... Woof.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        "#5301090V#0802F#11P#NSo...you want us out of here, or what?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        (
            "#5301091V#0904F#11P#NI feel like we shouldn't steal your\x01",
            "thunder.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x107, 500)

    ChrTalk(
        0x104,
        (
            "#5301092V#6P#0301FOh, shut up! Get your butts in here!\x02\x03",
            "#5301093V#0309FYou, too, lil' missy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5301094V#3300F#11P#NWell, if you insist.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xB,
        "#5301095V#11P#0606FThis is an utter waste of time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5301096V#1404F#5PSurely it's fine to indulge in times\x01",
            "like this, no?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#5301097V#12P#0509FRight! Deputy Commander Baelz and\x01",
            "Chief Sergei can get in on the sides!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5301098V#11P#2002FOkay, fine... Hmm, I do wonder\x01",
            "how this photo will turn out.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(24300, 17100, -2000, 0)
    MoveCamera(90, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_90(0x8, 23400, 16000, -2000, 270)
    OP_90(0x101, 24300, 16140, -2100, 270)
    OP_90(0x102, 24000, 16000, -2700, 270)
    OP_90(0x103, 23800, 16000, -1300, 270)
    OP_90(0x104, 24450, 16219, -1150, 270)
    OP_90(0x9, 23750, 16000, -3550, 270)
    OP_90(0xA, 23400, 16000, -300, 225)
    OP_90(0x107, 25200, 16600, -2300, 270)
    OP_90(0x108, 25200, 16600, -3500, 270)
    OP_90(0xF, 25300, 16650, -2900, 270)
    OP_90(0xB, 24900, 16450, -450, 270)
    OP_90(0xC, 24900, 16450, 550, 270)
    OP_90(0xD, 24500, 16260, -4950, 270)
    OP_90(0xE, 24500, 16260, -4250, 270)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 19200, 16000, -2000, 90)
    SetChrPos(0x10, 18800, 16000, -3000, 90)
    FadeToBright(1000, 0)
    OP_68(22300, 17100, -2000, 4000)
    SetCameraDistance(18500, 4000)
    OP_0D()
    OP_6F(0x11)

    ChrTalk(
        0x10,
        (
            "#5301099V#2102F#6P#NHere we go, guys! Put on your best smile!\x02\x03",
            "#5301100V#2109FSay 'cheese!'\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(817, 0, 100, 0)
    FadeToDark(0, -1, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(3000)
    OP_C9(0x0, 0x3, 0xFFCCAA77, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x0, 0x3, 0xCCAA77, 0xBB8, 0x0)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    FadeToBright(0, -1)
    OP_C7(0x1, 0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x4F, 0x4, 0x10)
    OP_29(0x4F, 0x4, 0x20)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    OP_DE(0x80, 0x0)
    Call(0, 16)
    Return()

    # Function_4_33C end

    def Function_5_21E6(): pass

    label("Function_5_21E6")


    def lambda_21EB():
        OP_96(0xFE, 0x4E20, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21EB)
    WaitChrThread(0x101, 1)
    Return()

    # Function_5_21E6 end

    def Function_6_2205(): pass

    label("Function_6_2205")


    def lambda_220A():
        OP_96(0xFE, 0x4FB0, 0x3E80, 0xFFFFF3E4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_220A)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Return()

    # Function_6_2205 end

    def Function_7_222B(): pass

    label("Function_7_222B")


    def lambda_2230():
        OP_96(0xFE, 0x4EE8, 0x3E80, 0xFFFFFE70, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2230)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xE1, 0x1F4)
    Return()

    # Function_7_222B end

    def Function_8_2251(): pass

    label("Function_8_2251")


    def lambda_2256():
        OP_96(0xFE, 0x5460, 0x3E80, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2256)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xE1, 0x1F4)
    Return()

    # Function_8_2251 end

    def Function_9_2277(): pass

    label("Function_9_2277")

    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)

    def lambda_2284():
        OP_96(0xFE, 0x4C90, 0x3E80, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2284)
    WaitChrThread(0x8, 1)

    def lambda_22A2():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A2)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_9_2277 end

    def Function_10_22BF(): pass

    label("Function_10_22BF")

    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)

    def lambda_22E8():
        OP_96(0xFE, 0x4844, 0x3E80, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_22E8)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    OP_93(0xA, 0x87, 0x1F4)
    Return()

    # Function_10_22BF end

    def Function_11_2315(): pass

    label("Function_11_2315")


    def lambda_231A():
        OP_96(0xFE, 0x4330, 0x3E80, 0xFFFFF768, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_231A)
    WaitChrThread(0xB, 1)
    Return()

    # Function_11_2315 end

    def Function_12_2334(): pass

    label("Function_12_2334")

    BeginChrThread(0x9, 0, 0, 1)

    def lambda_233F():
        OP_96(0xFE, 0x44C0, 0x3E80, 0xFFFFFA88, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_233F)
    WaitChrThread(0x9, 1)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_12_2334 end

    def Function_13_2361(): pass

    label("Function_13_2361")


    def lambda_2366():
        OP_96(0xFE, 0x40D8, 0x3E80, 0xFFFFFED4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2366)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0x87, 0x1F4)
    Return()

    # Function_13_2361 end

    def Function_14_2387(): pass

    label("Function_14_2387")


    def lambda_238C():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFF2B8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_238C)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x2D, 0x1F4)
    Return()

    # Function_14_2387 end

    def Function_15_23AD(): pass

    label("Function_15_23AD")


    def lambda_23B2():
        OP_96(0xFE, 0x43F8, 0x3E80, 0xFFFFEF98, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_23B2)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x2D, 0x1F4)
    Return()

    # Function_15_23AD end

    def Function_16_23D3(): pass

    label("Function_16_23D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_23D3 end

    SaveToFile()

Try(main)
