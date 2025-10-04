from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3034.bin",                # FileName
        "m3034",                    # MapName
        "m3034",                    # Location
        0x007E,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -71000, 0, 0, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3034",                  # 0
        "Garcia",                 # 1
        "SE制御",                 # 2
        "bm3040",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 8, 14, 180)
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
        "BattleInfo_E4", 0x0042, 43, 6, 180, 0, 0, 0, 0, "bm3040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7405", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50524.itc",                   # 00
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

    DeclNpc(0,       0,       0,       0,    277,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   -53.0,                 0.0,                   -5.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   17.666667938232422,    -0.0,                  1.0,                   1.0])

    DeclActor(15200,   5030,    6000,    2500,    15200,   6030,    6000,    0x007C, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_27C",          # 00, 0
        "Function_1_2A6",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_346",          # 03, 3
        "Function_4_4A8",          # 04, 4
        "Function_5_DAA",          # 05, 5
        "Function_6_22B4",         # 06, 6
        "Function_7_22F7",         # 07, 7
    ))


    def Function_0_27C(): pass

    label("Function_0_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_28B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrPos(0x8, -5000, -4000, 3000, 270)

    label("loc_2A5")

    Return()

    # Function_0_27C end

    def Function_1_2A6(): pass

    label("Function_1_2A6")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2BE")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_2DA")
    OP_70(0x2, 0x96)
    OP_70(0x1, 0x1E)
    Jump("loc_2E2")

    label("loc_2DA")

    OP_70(0x2, 0x78)
    OP_70(0x1, 0x0)

    label("loc_2E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30A")
    OP_24(0x82)
    Jump("loc_310")

    label("loc_30A")

    Sound(130, 1, 100, 0)

    label("loc_310")

    Return()

    # Function_1_2A6 end

    def Function_2_311(): pass

    label("Function_2_311")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Garcia is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_2_311 end

    def Function_3_346(): pass

    label("Function_3_346")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_393")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever has already been pulled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4A7")

    label("loc_393")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Pull it?\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    Fade(500)
    SetChrPos(0x0, 14090, 4000, 6000, 90)
    SetChrPos(0x1, 12000, 4000, 6800, 90)
    SetChrPos(0x2, 12000, 4000, 5200, 90)
    SetChrPos(0x3, 11320, 4000, 6000, 90)
    OP_68(15910, 5800, 2130, 0)
    MoveCamera(90, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x2, 0x78, 0x96, 0x0, 0x0)
    OP_79(0x2)
    Sleep(500)
    Sound(155, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    SetScenarioFlags(0xF5, 6)

    label("loc_4A0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4A7")

    Return()

    # Function_3_346 end

    def Function_4_4A8(): pass

    label("Function_4_4A8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    StopBGM(0x2710)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch02250.itc", 0x24)
    LoadChrToIndex("chr/ch02254.itc", 0x25)
    LoadChrToIndex("chr/ch02252.itc", 0x26)
    LoadEffect(0x0, "event\\ev602_00.eff")
    SoundLoad(861)
    OP_68(-40000, -3000, 0, 0)
    MoveCamera(35, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5000, -2000, 0, 7000)
    MoveCamera(65, 10, 0, 7000)
    SetCameraDistance(35000, 7000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-12500, -3100, 0, 0)
    MoveCamera(90, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    SetMapObjFrame(0xFF, "moya1", 0x0, 0x1)
    SetChrPos(0x101, -25000, -4000, 0, 90)
    SetChrPos(0x102, -26000, -4000, -1500, 90)
    SetChrPos(0x103, -27500, -4000, -600, 90)
    SetChrPos(0x104, -26500, -4000, 900, 90)
    SetChrPos(0x107, -25500, -4000, 2700, 90)
    SetChrPos(0x108, -27300, -4000, 2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_68(-7500, -3100, 0, 3500)
    SetCameraDistance(22000, 3500)

    def lambda_6A8():
        OP_96(0xFE, 0xFFFFD508, 0xFFFFF060, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A8)
    Sleep(50)

    def lambda_6C5():
        OP_96(0xFE, 0xFFFFD120, 0xFFFFF060, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C5)
    Sleep(50)

    def lambda_6E2():
        OP_96(0xFE, 0xFFFFCB44, 0xFFFFF060, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E2)
    Sleep(50)

    def lambda_6FF():
        OP_96(0xFE, 0xFFFFCF2C, 0xFFFFF060, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6FF)
    Sleep(50)

    def lambda_71C():
        OP_96(0xFE, 0xFFFFD314, 0xFFFFF060, 0xA8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_71C)
    Sleep(50)

    def lambda_739():
        OP_96(0xFE, 0xFFFFCC0C, 0xFFFFF060, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_739)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_767():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_767)
    WaitChrThread(0x108, 1)

    def lambda_778():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_778)
    WaitChrThread(0x108, 2)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5300442V#6P#0007FGarcia Rossi...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300443V#6P#0301FHmph. Been hidin' down here, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300458V\x07\x02",
            "#40W...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300445V\x07\x00",
            "#12P#0101FI was afraid of this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5300446V#12P#0208F#NHe appears to be brainwashed,\x01",
            "same as the rest of the mafia.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300447V#6P#0801FWhoa. This guy might be as big as Zin.\x02\x03",
            "#5300448VHe'll give us a run for our money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300449V#6P#0903F#NFormer commanding officer of Zephyr\x01",
            "and current manager at Revache & Co...\x02\x03",
            "#5300450V#0901FI think his credentials speak for themselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300451V\x07\x02",
            "#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_68(-5000, -3100, 0, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x7D0)
    MoveCamera(65, 17, 0, 2000)
    SetCameraDistance(21500, 2000)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 100, 0)
    Sound(861, 2, 100, 0)
    OP_6F(0x79)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5300452V\x07\x00",
            "#0013F#6P#NIt doesn't look like the demonization\x01",
            "is going to hit him, though.\x02\x03",
            "#5300453VEveryone, stay alert.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4D")

    ChrTalk(
        0x104,
        (
            "#5300454V#0311F#6P#NYo, Killing Bear...\x02\x03",
            "#5300455V#0303FYou might not be able to understand me,\x01",
            "but I'll grant you your damn wish...\x01",
            "No holding back anymore.\x02\x03",
            "#5300456V#0312FPrepare to witness the power of the\x01",
            "Red Reaper... Son of the War God!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_C4D")


    ChrTalk(
        0x104,
        (
            "#5300457V#0307F#6P#NYeah... Don't let up!\x01",
            "Not even for a second!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    OP_5A()

    ChrTalk(
        0x8,
        (
            "#5300444V\x07\x02",
            "#40W#11P...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1838, 255, 100, 0)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(100)

    def lambda_CE4():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE4)
    WaitChrThread(0x8, 1)
    Sleep(500)
    Sound(1839, 255, 100, 1)
    Sound(250, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-9000, -3100, 0, 400)
    SetCameraDistance(17000, 400)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrFlags(0x8, 0x20)

    def lambda_D49():
        OP_96(0xFE, 0xFFFFD6FC, 0xFFFFF060, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D49)
    SetChrSubChip(0x8, 0x4)
    Sleep(80)
    SetChrSubChip(0x8, 0x5)
    Sleep(320)
    OP_24(0x35D)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x20)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    EndChrThread(0x8, 0xFF)
    StopEffect(0x0, 0x0)
    Call(0, 5)
    Return()

    # Function_4_4A8 end

    def Function_5_DAA(): pass

    label("Function_5_DAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00351.itc", 0x22)
    LoadChrToIndex("chr/ch00650.itc", 0x23)
    LoadChrToIndex("chr/ch00750.itc", 0x24)
    LoadChrToIndex("chr/ch02253.itc", 0x25)
    LoadChrToIndex("chr/ch02254.itc", 0x26)
    LoadChrToIndex("chr/ch00056.itc", 0x27)
    LoadChrToIndex("chr/ch00351.itc", 0x28)
    SoundLoad(861)
    SoundLoad(930)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x23)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    OP_68(-5000, -3100, 0, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -11000, -4000, 0, 90)
    SetChrPos(0x102, -12000, -4000, -1500, 90)
    SetChrPos(0x103, -13500, -4000, -600, 90)
    SetChrPos(0x104, -12500, -4000, 900, 90)
    SetChrPos(0x107, -11500, -4000, 2700, 135)
    SetChrPos(0x108, -13300, -4000, 2000, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F26():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F26)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_00.eff")
    LoadEffect(0x2, "event\\ev602_03.eff")
    SetMapObjFrame(0xFF, "moya1", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1859, 255, 100, 0)

    ChrTalk(
        0x8,
        (
            "#5300460V\x07\x02",
            "#11P#60W#17AGuh... Ughhhh...\x02",
        )
    )

    Sleep(3000)
    Sleep(500)
    Sound(1860, 255, 100, 1)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(100)
    Fade(500)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(930, 2, 100, 0)
    OP_25(0x82, 0x32)
    OP_82(0x64, 0x0, 0xBB8, 0x5DC)
    MoveCamera(65, 17, 0, 1500)
    SetCameraDistance(22500, 1500)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    EndChrThread(0x8, 0x1)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)

    ChrTalk(
        0x8,
        (
            "#5300461V\x07\x02",
            "#5S#25A#11PGaaaaAAAAHHHHH!!\x02",
        )
    )

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#5300462V\x07\x00",
            "#0107F#6P#NN-No way!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x108,
        "#5300463V#0907F#6P#NDemonization! Look out!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x107,
        (
            "#5300464V#0813F#6P#NI don't think we'll be able to handle him\x01",
            "if that happens! He'll be unstoppable!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#5300465V#0310F#6P#NTch...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(-8370, -3000, 900, 0)
    MoveCamera(318, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x107, 0x73, 0x0)
    OP_93(0x108, 0x73, 0x0)
    SetCameraDistance(15500, 1500)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x0)

    def lambda_1262():
        OP_96(0xFE, 0xFFFFD634, 0xFFFFF060, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1262)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x10)

    ChrTalk(
        0x104,
        (
            "#5300466V#5P#0301FHey, old man!\x02\x03",
            "#5300467VYou're a veteran of the corps, aren't you?!\x01",
            "How can you be so weak, then?!\x02\x03",
            "#5300468V#0303FYou might be with the mafia now, but you\x01",
            "escaped from that hell, didn't you?!\x02\x03",
            "#5300469V#0307FC'mon! Show off that strength of yours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300470V#5P#0005FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300471V#5P#0208FRandy, are you trying too...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-8100, -3000, 0, 0)
    MoveCamera(63, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    OP_93(0x107, 0x87, 0x0)
    OP_93(0x108, 0x87, 0x0)
    OP_0D()
    Sleep(500)
    Sound(1860, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    def lambda_1454():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1454)

    ChrTalk(
        0x8,
        (
            "#5300472V\x07\x02",
            "#11P#4S#40WGAAAAAHHHH...!\x02\x03",
            "#5300473V#50WOOOOOooooh!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 2, 0, 7)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x1, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x8,
        (
            "#5300474V\x07\x02",
            "#11P#60WAaaahhhh...aaaahhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 6)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x1, 0x2)
    Fade(500)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    Sound(819, 0, 100, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#5300475V\x07\x00",
            "#11P#3111F#60WHaaaah...ugh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
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
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    EndChrThread(0x8, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        "#5300476V#3P#0202F#NThe miasma vanished...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#5300477V#6P#0102FDid he pull himself together?\x02",
    )

    CloseMessageWindow()

    def lambda_165C():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_165C)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#5300478V#11P#3111F#50WGyah... *cough*...\x02\x03",
            "#5300479V#3110F#50WHaaaah...haaaah...haaaah...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300480V#6P#0304FHeh. Glad to see you didn't lose\x01",
            "yourself to it, Killing Bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300481V#11P#3103F#40WHmph. Look at you, talking like\x01",
            "you're some kind of big shot...\x02\x03",
            "#5300482V#3100FWhatever. I think...I might\x01",
            "owe you my thanks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300483V#6P#0013FJoachim used Gnosis on you, didn't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300484V#11P#3103F#40WYeah... Direct injection, too.\x02\x03",
            "#5300485V#3101FThat bastard... I knew he was slimy\x01",
            "from the moment I laid eyes on him.\x02\x03",
            "#5300486V#3107FDamn it! He thinks he can do this to\x01",
            "my men and get away with it...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300487V#6P#0003FYou can rest easy. We'll apprehend him.\x02\x03",
            "#5300488V#0001FI'm sorry to say, but I doubt you and your\x01",
            "subordinates will be able to avoid arrest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5300489V#11P#3104F#40WHmph. Can't say we don't deserve it after\x01",
            "this pathetic-ass display.\x02\x03",
            "#5300490VThat bastard should still be in there.\x02\x03",
            "#5300491V#3102FHey, Son of the War God and...Lloyd, right?\x02\x03",
            "#5300492VYou guys may get on my nerves, but that\x01",
            "bastard makes me want to punch a wall...\x02\x03",
            "#5300493V#3107FListen well. You will not...lose to him!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1AFC():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AFC)
    WaitChrThread(0x8, 1)
    Fade(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(514, 0, 100, 0)
    OP_0D()
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_68(-8100, -3000, 0, 2000)
    MoveCamera(47, 17, 0, 2000)
    SetCameraDistance(17500, 2000)

    def lambda_1B63():
        OP_96(0xFE, 0xFFFFE69C, 0xFFFFF060, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B63)
    Sleep(600)

    def lambda_1B80():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B80)
    Sleep(100)

    def lambda_1B9D():
        OP_98(0xFE, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1B9D)

    def lambda_1BB7():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BB7)
    Sleep(50)

    def lambda_1BD4():
        OP_98(0xFE, 0x898, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BD4)

    def lambda_1BEE():
        OP_98(0xFE, 0x76C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1BEE)
    WaitChrThread(0x101, 1)

    def lambda_1C0C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1C0C)

    def lambda_1C19():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C19)

    def lambda_1C26():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C26)
    Fade(250)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x104,
        "#5300494V#5P#0306FDown for the count.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300495V#5P#0008FYeah. He's out cold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5300496V#6P#0900FHe probably used every last bit of his\x01",
            "energy to resist demonization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#5300497V#5P#0803FHmm, he might be one of the baddies,\x01",
            "but he had an iron will.\x02\x03",
            "#5300498V#0800FI think I can relate with him a bit more\x01",
            "than that nasty old mafia boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300499V#6P#0100FAgreed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300500V#6P#0204FWell said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300501V#5P#0304FHmph. I'll say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300502V#5P#0000FHe's better than some...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x101, 0x10E, 0x1F4)
    Fade(500)
    OP_68(-8100, -3100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5300503V#0003F#5PThe true mastermind behind this case\x01",
            "is only steps away now.\x02\x03",
            "#5300504V#0008FConsidering how powerful Ernest and\x01",
            "Garcia were, I'm afraid that this might\x01",
            "be our toughest arrest yet.\x02\x03",
            "#5300505V#0001F...Everyone ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300506V#12P#0101FOf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300507V#12P#0201FYes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300508V#6P#0307FAlways!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#5300509V#3P#0807FLet's wrap this case up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5300510V#6P#0901FReady and able!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5300511V#0004FThat's what I like to hear.\x02\x03",
            "#5300512V#0013FWe will now commence the\x01",
            "arrest of D∴G cult high priest\x01",
            "Joachim Guenter...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#5300513V#0007F#5PGive it everything you've got!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Everyone")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(1153, 255, 100, 0)
    Sound(1249, 255, 100, 1)
    Sound(1343, 255, 100, 2)
    Sound(1689, 255, 100, 3)
    Sound(1759, 255, 100, 4)

    AnonymousTalk(
        0xFF,
        "#5300514V#5SYeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 3000, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_37()
    OP_68(-10000, -1000, 0, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x0, -10000, -4000, 0, 90)
    SetChrPos(0x1, -10000, -4000, 0, 90)
    SetChrPos(0x2, -10000, -4000, 0, 90)
    SetChrPos(0x3, -10000, -4000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE6, 4)
    OP_29(0x4F, 0x1, 0xA)
    SetMapObjFrame(0xFF, "moya1", 0x1, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x2)
    OP_25(0x82, 0x64)
    OP_24(0x35D)
    OP_24(0x3A2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_DAA end

    def Function_6_22B4(): pass

    label("Function_6_22B4")

    OP_25(0x35D, 0x5A)
    Sleep(200)
    OP_25(0x35D, 0x50)
    Sleep(200)
    OP_25(0x35D, 0x46)
    Sleep(200)
    OP_25(0x35D, 0x3C)
    Sleep(200)
    OP_25(0x35D, 0x32)
    Sleep(200)
    OP_25(0x35D, 0x28)
    Sleep(200)
    OP_25(0x35D, 0x1E)
    Sleep(200)
    OP_25(0x35D, 0x14)
    Sleep(200)
    OP_25(0x35D, 0xA)
    Sleep(200)
    OP_24(0x35D)
    Return()

    # Function_6_22B4 end

    def Function_7_22F7(): pass

    label("Function_7_22F7")

    OP_25(0x3A2, 0x5A)
    Sleep(400)
    OP_25(0x3A2, 0x50)
    Sleep(400)
    OP_25(0x3A2, 0x46)
    Sleep(400)
    OP_25(0x3A2, 0x3C)
    Sleep(400)
    OP_25(0x3A2, 0x32)
    Sleep(400)
    OP_25(0x3A2, 0x28)
    Sleep(400)
    OP_25(0x3A2, 0x1E)
    Sleep(400)
    OP_25(0x3A2, 0x14)
    Sleep(400)
    OP_25(0x3A2, 0xA)
    Sleep(400)
    OP_24(0x3A2)
    Return()

    # Function_7_22F7 end

    SaveToFile()

Try(main)
