from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1099.bin",                # FileName
        "m1099",                    # MapName
        "m1099",                    # Location
        0x00A2,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, -10000, 0, 0, 1, 162, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1099",                  # 0
        "Yin",                    # 1
        "Yin",                    # 2
        "Talisman",               # 3
        "BM1010",                 # 4
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 0, 0, 180)
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
        "BattleInfo_E4", 0x0052, 22, 6, 0, 0, 0, 0, 0, "BM1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02800.dat", 0, 0, 0, 0, 0, "ms02801.dat", 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
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
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1F4",          # 00, 0
        "Function_1_21A",          # 01, 1
        "Function_2_21B",          # 02, 2
        "Function_3_1223",         # 03, 3
        "Function_4_1298",         # 04, 4
        "Function_5_3F04",         # 05, 5
        "Function_6_3F1C",         # 06, 6
        "Function_7_3FA5",         # 07, 7
        "Function_8_400A",         # 08, 8
        "Function_9_4015",         # 09, 9
        "Function_10_4020",        # 0A, 10
        "Function_11_402B",        # 0B, 11
        "Function_12_4036",        # 0C, 12
        "Function_13_4041",        # 0D, 13
    ))


    def Function_0_1F4(): pass

    label("Function_0_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_219")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_219")

    Return()

    # Function_0_1F4 end

    def Function_1_21A(): pass

    label("Function_1_21A")

    Return()

    # Function_1_21A end

    def Function_2_21B(): pass

    label("Function_2_21B")

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
    LoadChrToIndex("chr/ch00500.itc", 0x28)
    LoadChrToIndex("chr/ch00501.itc", 0x29)
    LoadChrToIndex("chr/ch00550.itc", 0x2A)
    LoadChrToIndex("chr/ch00551.itc", 0x2B)
    SetChrPos(0x101, -270, 0, -22390, 0)
    SetChrPos(0x102, -1130, 0, -23750, 0)
    SetChrPos(0x103, 530, 0, -23830, 0)
    SetChrPos(0x104, 540, 0, -25330, 0)
    SetChrPos(0x109, -1210, 0, -25020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 6120, 6160, 15750, 180)
    SetChrFlags(0x8, 0x8000)
    ClearMapFlags(0x10000000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    FadeToBright(1000, 0)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    OP_68(0, 1800, 0, 10000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_3E5():
        OP_95(0xFE, -270, 0, 1610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E5)

    def lambda_3FF():
        OP_95(0xFE, -1130, 0, 250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FF)

    def lambda_419():
        OP_95(0xFE, 530, 0, 170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_419)

    def lambda_433():
        OP_95(0xFE, 540, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_433)

    def lambda_44D():
        OP_95(0xFE, -1210, 0, -1020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44D)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_68(710, 1100, 11810, 0)
    MoveCamera(57, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41050, 0)
    OP_68(-200, 1100, 0, 9000)
    MoveCamera(45, 28, 0, 9000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20, 1100, 810, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18050, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#2201176V#0005F#5PWhat even is this room...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201177V#0105F#6PI've never seen bookshelves this big...\x01",
            "Is that some sort of armillary sphere?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sound(1629, 255, 100, 0)
    Sleep(800)

    NpcTalk(
        0x8,
        "Voice",
        (
            "#2201178V\x07\x03",
            "#4PIt's said that this tower was constructed\x01",
            "by the powerful alchemists of the past.\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(8400, 6400, 15410, 3000)
    MoveCamera(60, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(17440, 3000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#2201179V\x07\x00",
            "#0007F#1PYou...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201180V#0101F#1PThat black outfit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201181V#0307F#1PIt's about damn time you came\x01",
            "out of the shadows!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Black-Shrouded Man",
        (
            "#2201182V\x07\x03",
            "#5PI've been waiting for you...\x02\x03",
            "#2201183VAnd I see you brought along\x01",
            "a fifth wheel as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201184V\x07\x00",
            "#0501F#1PI'm just here as backup.\x01",
            "Don't mind me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Black-Shrouded Man",
        (
            "#2201185V\x07\x03",
            "#5PHeh, very well.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 3)
    OP_68(740, 1000, 2780, 2500)
    MoveCamera(14, 13, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(22410, 1450)
    OP_6F(0x10)
    SetCameraDistance(20410, 1050)
    SetChrPos(0x109, -420, 0, -960, 315)
    SetChrPos(0x104, 740, 0, -1400, 315)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x8, 0x104, 0)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    Sleep(500)
    Sound(1627, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#2201186V\x07\x03",
            "It's a pleasure to make your\x01",
            "acquaintance, Special Support\x01",
            "Section... I am known as Yin.\x02\x03",
            "#2201187VAllow me to thank you for agreeing\x01",
            "to my request. I imagine getting\x01",
            "here was no small feat.\x07\x00\x02",
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
            "#2201188V#0006F#6PYeah, it wasn't easy. You've had\x01",
            "us running in circles for a while now.\x02\x03",
            "#2201189V#0001FThe monsters didn't make it easy, either.\x01",
            "Do we have you to thank for that, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201190V\x07\x03",
            "#0702F#5PI assure you, those strange beings\x01",
            "were wandering in here long before\x01",
            "I found them.\x02\x03",
            "#2201191VIn order to maintain my edge, I searched\x01",
            "for a hunting ground worthy of my skills.\x01",
            "I eventually found this tower.\x02\x03",
            "#2201192VIt has proven even more interesting\x01",
            "than I expected it to.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201193V#0005F#6PSo it wasn't your doing, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201194V#0203F#12PI think it would be difficult for one person to\x01",
            "fill the entire tower with those monsters,\x01",
            "even for someone like Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201195V\x07\x03",
            "#0700F#5PNow, I know you must have a multitude\x01",
            "of questions for me...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrPos(0x8, 1290, 0, 6620, 180)
    OP_68(1340, 1000, 3930, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21410, 0)
    SetCameraDistance(20410, 1000)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#2201196V\x07\x03",
            "#0702F#5P...but before that, allow me to administer\x01",
            "the final test.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
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
        "#2201197V#0007F#6PTest...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201198V#0101F#11PWhat are you planning?!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7404", 0)

    ChrTalk(
        0x8,
        (
            "#2201199V\x07\x03",
            "#0700F#5PWeakness does not interest me...\x02\x03",
            "#2201200VDo you possess the strength to fulfill\x01",
            "my request?\x02\x03",
            "#2201201VCome at me with all of your might.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201202V#0013F#6PHere we go...\x02",
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
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        "#2201203V#0206F#2PHe does not appear to be bluffing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201204V#0304F#2PI'd like to say we got this in the\x01",
            "bag 'cause of our numbers, but...\x02\x03",
            "#2201205V#0307FKeep your eyes open, guys!\x01",
            "This guy's the real deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201206V#0501F#2PNo holding back now, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201207V#0107F#2PRight! Let's give it everything we've got!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201208V\x07\x03",
            "#0702F#5PHeh. I see you've stoked the\x01",
            "flames of your fighting spirit.\x02\x03",
            "#2201209V#0707FPrepare yourselves, SSS!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(15500, 400)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    def lambda_11F2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11F2)
    Sleep(400)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 4)
    Return()

    # Function_2_21B end

    def Function_3_1223(): pass

    label("Function_3_1223")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_123D():
        OP_9D(0xFE, 0x4D8, 0x0, 0x14A0, 0x6D6, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_123D)
    Sound(814, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x3)
    SetChrFlags(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(50)
    Sound(30, 0, 100, 0)
    Return()

    # Function_3_1223 end

    def Function_4_1298(): pass

    label("Function_4_1298")

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
    LoadChrToIndex("chr/ch00500.itc", 0x28)
    LoadChrToIndex("chr/ch00501.itc", 0x29)
    LoadChrToIndex("chr/ch00550.itc", 0x2A)
    LoadChrToIndex("chr/ch00551.itc", 0x2B)
    LoadChrToIndex("chr/ch00553.itc", 0x2C)
    LoadChrToIndex("apl/ch50221.itc", 0x2D)
    OP_68(-2770, 1100, -50, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21470, 0)
    SetChrPos(0x101, -2590, 0, -90, 270)
    SetChrPos(0x102, -1330, 0, -790, 270)
    SetChrPos(0x103, -150, 0, 490, 270)
    SetChrPos(0x104, -240, 0, -1700, 270)
    SetChrPos(0x109, 970, 0, -440, 270)
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
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -6220, 600, 450, 90)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x3)
    SetChrPos(0x9, -6220, 0, 450, 90)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -470, 0, 13300, 180)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadEffect(0x0, "event\\ev200_00.eff")
    LoadEffect(0x1, "event\\ev202_00.eff")
    FadeToBright(1000, 0)
    SetCameraDistance(19470, 2000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#2201210V#0007F#11PHow about that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201211V#0110F#11PD-Did we beat him...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201212V#0206F#11PI need some rest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201213V#0500F#11PAt least we're done here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201214V#0301F#11PNo, I wouldn't get your hopes up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201215V#0505F#11PWhat do you mean...?\x02",
    )

    CloseMessageWindow()
    Sound(1628, 255, 100, 0)
    Sleep(500)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("Yin's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#2201217V\x07\x03",
            "That man over there has\x01",
            "quite the keen senses.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_68(-4230, 1100, 300, 1500)
    Sleep(1200)
    PlayEffect(0x0, 0xFF, 0x9, 0x0, 0, 650, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 13)

    def lambda_1665():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1665)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x9, 0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(750)

    ChrTalk(
        0x101,
        "#2201218V#0005F#11PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201219V#0205F#11PSome sort of talisman?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 50, 0, 9990, 180)
    OP_68(160, 500, 7640, 2000)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_17AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17AA)

    def lambda_17BB():
        OP_95(0xFE, 50, 0, 7710, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17BB)
    Sleep(300)

    def lambda_17D8():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17D8)
    Sleep(50)

    def lambda_17E8():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17E8)

    def lambda_17F5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17F5)
    Sleep(50)

    def lambda_1805():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1805)

    def lambda_1812():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1812)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-400, 1400, 3860, 0)
    MoveCamera(145, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x9, 50, -500, 7710, 180)
    SetChrPos(0x101, -260, 0, 760, 0)
    SetChrPos(0x102, -800, 0, -280, 0)
    SetChrPos(0x103, -900, 0, -1750, 0)
    SetChrPos(0x104, 1130, 0, -130, 0)
    SetChrPos(0x109, 660, 0, -1760, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#2201220V#0105F#11PWh-When did he even...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201221V#0501F#11PHe went completely under my radar...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201222V#0303F#11PLettin' a double take care of things while\x01",
            "you kick back and observe the fight, eh?\x02\x03",
            "#2201223V#0301FMight be a handy power, but I can't\x01",
            "say it's very courteous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201224V\x07\x03",
            "#0700F#5PIf I somehow offended you, you\x01",
            "have my sincerest apologies.\x02\x03",
            "#2201225V#0702FHowever, the fact that you could keep\x01",
            "up with my movement during the battle...\x02\x03",
            "#2201226VYour eyes are sharp; I'll give you that much.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201227V#0306F#11PWell, my combat experience over\x01",
            "the years hasn't been for nothing.\x02\x03",
            "#2201228V#0301FUp for another round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201229V\x07\x03",
            "#0700F#5PHeh. I'll respectfully decline.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
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
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CCC")

    ChrTalk(
        0x101,
        (
            "#2201230V#0006F#11PI can't deny it. Your strength is first-class.\x01",
            "At our level, we can't hold a candle to you.\x02\x03",
            "#2201231V#0001FWith that in mind, what business do you\x01",
            "have with the SSS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201232V\x07\x03",
            "#0702F#1POh? But, Lloyd Bannings...\x02\x03",
            "#2201233VSurely you must have some idea, no?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201234V#0001F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201235V#0105F#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201236V#0205F#11PLloyd, what does he mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201237V\x07\x03",
            "#0700F#1PI've done my research.\x02\x03",
            "#2201238VYour investigative aptitude is\x01",
            "nothing to scoff at.\x02\x03",
            "#2201239VYou should understand what I'm after.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201240V#0003F#11PI do.\x02\x03",
            "#2201241V#0001FYour request is likely about one thing.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AE")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat does Yin's business with the\x01",
            "SSS have to do with?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Arc en Ciel]\x01",            # 0
            "[Revache & Co.]\x01",          # 1
            "[The threat letter]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FA0"),
        (1, "loc_205E"),
        (2, "loc_2107"),
        (SWITCH_DEFAULT, "loc_21A9"),
    )


    label("loc_1FA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB4")
    OP_2C(0x42, 0x1)

    label("loc_1FB4")


    ChrTalk(
        0x101,
        (
            "#2201242V#0006F#11P(While it's not irrelevant, it's definitely\x01",
            "not what Yin wants to talk about...)\x02\x03",
            "#2201252V#0001F(If they are related, then...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_21A9")

    label("loc_205E")


    ChrTalk(
        0x101,
        (
            "#2201244V#0006F#11P(No, that's pretty unrelated,\x01",
            "when looking at the big picture.)\x02\x03",
            "#2201245V#0001F(Let's try to think about this differently...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_21A9")

    label("loc_2107")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211B")
    OP_2C(0x42, 0x2)

    label("loc_211B")


    ChrTalk(
        0x101,
        (
            "#2201246V#0003F#11PThe mysterious threat letter that\x01",
            "was sent to Arc en Ciel for Ilya...\x02\x03",
            "#2201247V#0001FThat's your aim, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A9")

    label("loc_21A9")

    Jump("loc_1ED0")

    label("loc_21AE")


    ChrTalk(
        0x9,
        (
            "#2201248V\x07\x03",
            "#0702F#1PPrecisely.\x02\x03",
            "#2201249VBut, 'what' exactly would I want to\x01",
            "talk about, regarding that letter?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201250V#0005F#11PI know what you're referring to.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_226B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E9")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat aspect of the letter is Yin curious about?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The content]\x01",           # 0
            "[The author]\x01",            # 1
            "[The real purpose]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2330"),
        (1, "loc_23B6"),
        (2, "loc_2431"),
        (SWITCH_DEFAULT, "loc_24E4"),
    )


    label("loc_2330")


    ChrTalk(
        0x101,
        (
            "#2201251V#0006F#11P(No, that's a pretty big stretch.)\x02\x03",
            "#2201243V#0001F(If it's not the content, it must be...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_24E4")

    label("loc_23B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CA")
    OP_2C(0x42, 0x2)

    label("loc_23CA")


    ChrTalk(
        0x101,
        (
            "#2201253V#0003F#11PThe author of the threat letter...\x02\x03",
            "#2201254V#0001FIt wasn't you, was it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E4")

    label("loc_2431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2445")
    OP_2C(0x42, 0x1)

    label("loc_2445")


    ChrTalk(
        0x101,
        (
            "#2201255V#0008F#11P(That's not exactly wrong, but there's something\x01",
            "I need to point out before that...)\x02\x03",
            "#2201256V#0001F(That means...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_24E4")

    label("loc_24E4")

    Jump("loc_226B")

    label("loc_24E9")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#2201257V#0105F#11PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201258V#0305F#11PYou serious?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201259V#0201F#11PDo not tell me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201260V\x07\x03",
            "#0702F#1PIndeed.\x02\x03",
            "#2201261V#0700FThe Yin you see before you did not\x01",
            "send that letter to Ilya Platiere.\x02\x03",
            "#2201262VThe true culprit is a copycat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201263V#0006F#11PLooks like my hunch was right...\x02\x03",
            "#2201264V#0008FSomething felt...off when we were\x01",
            "conducting the investigation.\x02\x03",
            "#2201265VThe legendary assassin, Yin... A demon\x01",
            "hailing from the Eastern Quarter.\x02\x03",
            "#2201266VThe deeper we dove into the investigation,\x01",
            "the more the fog surrounding you lifted.\x02\x03",
            "#2201267V#0013FHowever, the threat letter struck me\x01",
            "more as a bluff than the real deal.\x02\x03",
            "#2201268VEven Ilya herself brushed it aside,\x01",
            "thinking it was no more than a prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201269V\x07\x03",
            "#0702F#1PThat's right.\x02\x03",
            "#2201270VIlya Platiere is a genius.\x02\x03",
            "#2201271VShe most likely realized that the true\x01",
            "target behind the threat letter wasn't her.\x02\x03",
            "#2201272V#0700FThat being the case, why was such a thing\x01",
            "sent to Arc en Ciel in the first place?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201273V#0506F#11PU-Umm, I'm not sure if I have a full\x01",
            "grasp on the situation...\x02\x03",
            "#2201274V#0501FCouldn't this just be a simple prank by\x01",
            "someone who doesn't like the troupe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201275V#0003F#11PNo. We can limit the suspects\x01",
            "to people who knew that Yin\x01",
            "had come to Crossbell.\x02\x03",
            "#2201276V#0001FHeiyue, Revache, the First Division...\x02\x03",
            "#2201277V...and any of their associates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#2201278V#0505F#11POh, is that so?\x02\x03",
            "#2201279V#0506FWhen you put it like that, the odds of this\x01",
            "being a prank DO seem incredibly low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201280V\x07\x03",
            "#0700F#1PCorrect again, Bannings. Still, it's impossible\x01",
            "for Arc en Ciel's new show to get canceled\x01",
            "over a lone threat letter.\x02\x03",
            "#2201281VWhat IS curious is that the letter made sure\x01",
            "to target Ilya directly by name.\x02\x03",
            "#2201282VAs a result, the First Division became involved\x01",
            "and began to take extreme safety precautions.\x02\x03",
            "#2201283VPrecautions that cover the possibility\x01",
            "of her being targeted during the show.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201284V#0208F#11PIn other words...\x02\x03",
            "#2201285V...the true culprit behind the threat\x01",
            "letter created this diversion in order\x01",
            "to accomplish something else?\x02\x03",
            "#2201286V#0201FOr perhaps to allow himself time to\x01",
            "prepare for said other goal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201287V\x07\x03",
            "#0700F#1PThat is a likely scenario.\x02\x03",
            "#2201288V#0702FI'd like to make a formal request.\x02\x03",
            "#2201289VUncover the culprit who stole\x01",
            "my name and thwart his plan.\x07\x00\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#2201290V#0011F#11PExcuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201291V#0301F#11PBein' sort of a selfish bastard there, aren't ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201292V\x07\x03",
            "#0702F#1PHeh. Think what you want of me,\x01",
            "but you'd be foolish to ignore this.\x02\x03",
            "#2201293VI, too, haven't the slightest idea of who\x01",
            "he is or what he intends to accomplish...\x02\x03",
            "#2201294V...however, surely you can see that someone\x01",
            "is in his crosshairs, no?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201295V#0303F#11PMaybe so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201296V#0106F#11PThat very well could be the case.\x02\x03",
            "#2201297V#0101FBut why go out of your way to\x01",
            "ask us for help?\x02\x03",
            "#2201298VWhy not do it yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201299V\x07\x03",
            "#0700F#1P...\x02\x03",
            "#2201300V#0702FBelieve it or not, I'm somewhat preoccupied\x01",
            "with my own responsibilities.\x02\x03",
            "#2201301VDealing with Revache alone keeps me\x01",
            "plenty busy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201302V#0013F#11POh?\x02\x03",
            "#2201303VSo you really are assisting Heiyue with\x01",
            "their fight against the mafia...\x02\x03",
            "#2201304V#0007FDo you enjoy this, knowing\x01",
            "we can't do anything about it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201305V\x07\x03",
            "#0702F#1PCalm down.\x02\x03",
            "#2201306VWe'd rather avoid the guild, so we're careful\x01",
            "not to involve any citizens in our bouts.\x02\x03",
            "#2201307VWell, Heiyue is, at least.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201308V#0013F#11PYin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201309V\x07\x03",
            "#0700F#1PIn any case, I will not allow someone to\x01",
            "use my name without consequence.\x02\x03",
            "#2201310VSSS, will you accept my request?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2201311V#0006F#11PFine.\x02\x03",
            "#2201312V#0001FWe'll stop the true culprit from carrying\x01",
            "out his plan, but don't think we're doing\x01",
            "it for your sake, Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201313V\x07\x03",
            "#0702F#1PThat suits me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201314V#0201F#11PBut where do we even begin?\x02\x03",
            "#2201315VWe have no leads, no idea who the\x01",
            "culprit is, and no motive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201316V\x07\x03",
            "#0700F#1PI might have a lead for you.\x02\x03",
            "#2201317VIf the culprit's plan truly does involve\x01",
            "Arc en Ciel...\x02\x03",
            "#2201318V...he must be planning to act on either the\x01",
            "opening day of their performance or the\x01",
            "day of the private performance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201319V#0005F#11PThose days would be ideal for our culprit, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201320V#0306F#11PI was thinkin' the same thing, man.\x02\x03",
            "#2201321V#0301FIf he wants to have a good time, he'd probably\x01",
            "go for the opening day, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201322V#0101F#11PThen again, he might want to make his move\x01",
            "while he's surrounded by a ton of influential\x01",
            "figures at the private performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201323V\x07\x03",
            "#0702F#1PPrecisely.\x02\x03",
            "#2201324V#0700FI ask you to stay vigilant on both of\x01",
            "those days...\x02\x03",
            "#2201325VYou will have to outwit the First Division in\x01",
            "order to be able to patrol the theater during\x01",
            "the two performances.\x02\x03",
            "#2201326VOnce you accomplish that, respond\x01",
            "accordingly to whatever may transpire.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201327V#2B#31Z#0006F#0E#11PEasier said than done.\x02\x03",
            "#2201328V#1B#12Z#40B#89Z#0000FBut still, you have a point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201329V#0104F#11PGaining access to the theater shouldn't\x01",
            "pose a problem, as long as we ask\x01",
            "Arc en Ciel for permission.\x02\x03",
            "#2201330V#0108FThe real challenge will be trying to\x01",
            "deceive the First Division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201331V#0206F#11PIndeed. It is highly probable they\x01",
            "would kick us out at first sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201332V#0300F#11PEh, we'll just have to be quick on our\x01",
            "feet when we cross that bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2201333V\x07\x03",
            "#0702F#1PWhat's important here is that you've complied.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#2201334V\x07\x03",
            "#0702F#11PWith that, I take my leave.\x02\x03",
            "#2201335VI'll be expecting good news.\x07\x00\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201336V#0005F#11PYin...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201337V#0501F#11PW-Wait a second!\x02",
    )

    CloseMessageWindow()

    label("loc_3CCC")

    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(17020, 1000)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    OP_95(0x8, -110, 0, 13100, 6000, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#2201338V#0007F#11PStop! Don't move!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201339V#0307F#11PDon't think you're gettin' away!\x02",
    )

    CloseMessageWindow()
    OP_68(-400, 1400, 4860, 1500)

    def lambda_3D74():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D74)
    Sleep(50)

    def lambda_3D8C():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D8C)
    Sleep(50)

    def lambda_3DA4():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DA4)
    Sleep(50)

    def lambda_3DBC():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DBC)
    Sleep(50)

    def lambda_3DD4():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DD4)
    Sleep(1500)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    SetChrPos(0x101, -680, 0, 3260, 270)
    SetChrPos(0x102, -2630, 0, 1420, 270)
    SetChrPos(0x103, 1040, 0, 0, 270)
    SetChrPos(0x104, -1850, 0, -1950, 270)
    SetChrPos(0x109, 970, 0, -3890, 270)
    OP_68(-2029, 3200, 9500, 0)
    MoveCamera(39, 3, 0, 0)
    SetCameraDistance(19380, 0)
    OP_68(11760, 12500, 14190, 8000)
    MoveCamera(340, 39, 0, 8000)
    SetCameraDistance(21130, 8000)
    BeginChrThread(0x8, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x109, 3, 0, 12)
    BeginChrThread(0x103, 3, 0, 10)
    BeginChrThread(0x104, 3, 0, 11)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1298 end

    def Function_5_3F04(): pass

    label("Function_5_3F04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F1B")
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    Jump("Function_5_3F04")

    label("loc_3F1B")

    Return()

    # Function_5_3F04 end

    def Function_6_3F1C(): pass

    label("Function_6_3F1C")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_95(0xFE, -1580, 4560, 23840, 7000, 0x1)
    OP_95(0xFE, 6950, 6760, 23080, 7000, 0x1)
    OP_95(0xFE, 12690, 8390, 20300, 7000, 0x1)
    OP_95(0xFE, 17630, 10020, 16290, 7000, 0x1)
    OP_95(0xFE, 21340, 11580, 11360, 7000, 0x1)
    EndChrThread(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_6_3F1C end

    def Function_7_3FA5(): pass

    label("Function_7_3FA5")

    OP_95(0xFE, -1580, 4560, 23840, 5000, 0x1)
    OP_95(0xFE, 6950, 6760, 23080, 5000, 0x1)
    OP_95(0xFE, 12690, 8390, 20300, 5000, 0x1)
    OP_95(0xFE, 17630, 10020, 16290, 5000, 0x1)
    OP_95(0xFE, 21340, 11580, 11360, 5000, 0x1)
    Return()

    # Function_7_3FA5 end

    def Function_8_400A(): pass

    label("Function_8_400A")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_400A end

    def Function_9_4015(): pass

    label("Function_9_4015")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_4015 end

    def Function_10_4020(): pass

    label("Function_10_4020")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_4020 end

    def Function_11_402B(): pass

    label("Function_11_402B")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_402B end

    def Function_12_4036(): pass

    label("Function_12_4036")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_4036 end

    def Function_13_4041(): pass

    label("Function_13_4041")


    def lambda_4046():
        OP_97(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4046)

    def lambda_4060():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4060)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_4041 end

    SaveToFile()

Try(main)
