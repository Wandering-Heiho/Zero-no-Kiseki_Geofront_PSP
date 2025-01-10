from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3010.bin",                # FileName
        "e3010",                    # MapName
        "e3010",                    # Location
        0x0000,                     # MapIndex
        "ed7515",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3010",                  # 0
        "Chief Sergei",           # 1
        "Zeit",                   # 2
        "Boat",                   # 3
        "SE制御",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_138",          # 01, 1
        "Function_2_14E",          # 02, 2
        "Function_3_FDF",          # 03, 3
        "Function_4_1009",         # 04, 4
        "Function_5_103A",         # 05, 5
        "Function_6_1054",         # 06, 6
        "Function_7_10A0",         # 07, 7
        "Function_8_10DF",         # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_137")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_137")

    Return()

    # Function_0_128 end

    def Function_1_138(): pass

    label("Function_1_138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_14D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_14D")

    Return()

    # Function_1_138 end

    def Function_2_14E(): pass

    label("Function_2_14E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("apl/ch50542.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis157.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 3, 0, 3)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 0, 300, -1500, 180)
    SetChrPos(0x133, 0, 900, 3300, 0)
    SetChrPos(0x9, -750, 900, 3300, 0)
    SetChrPos(0x101, 0, 900, 300, 0)
    SetChrPos(0x102, -900, 900, 1000, 90)
    SetChrPos(0x103, 900, 900, 1000, 270)
    SetChrPos(0x104, -900, 900, 2100, 90)
    SetChrPos(0x105, 900, 900, 2100, 270)
    BeginChrThread(0xB, 0, 0, 7)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 1, 0, 4)
    OP_68(690, 9850, 800, 0)
    MoveCamera(250, 6, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46340, 0)
    OP_68(690, 3850, 800, 5000)
    OP_6F(0x1)
    Sleep(1000)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x1)
    OP_0D()
    Fade(1000)
    BeginChrThread(0xB, 1, 0, 5)
    OP_68(160, 1750, 1530, 0)
    MoveCamera(219, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15070, 0)
    OP_0D()
    Sleep(500)
    EndChrThread(0xB, 0x1)

    ChrTalk(
        0x8,
        (
            "#3501979V#1003F#5POkay, I got it.\x02\x03",
            "#3501980V#1001FWell, for now, I'm ignoring\x01",
            "the fact that you completely\x01",
            "disregarded my warning...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        "#3501981V#0008F#11PS-Sorry, Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3501982V#1000F#5PThis girl is our primary issue.\x02\x03",
            "#3501983V#1003FDepending on how everything goes down,\x01",
            "things could take a turn for the worse.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_470():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_470)

    def lambda_47D():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47D)
    Sleep(100)

    def lambda_48D():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_48D)

    def lambda_49A():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_49A)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x104,
        (
            "#3501984V#0303F#11PTell me about it...\x02\x03",
            "#3501985V#0301FThat auction was about to sell a kid.\x01",
            "Not a doll, not a statue...a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#3501986V#0406F#5PI couldn't imagine anything\x01",
            "pleasant happening there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501987V#0208F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501988V#0106F#5PI find it hard to believe\x01",
            "that the mafia would try\x01",
            "something this stupid.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x133, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x133, 0xB4, 0x1F4)

    ChrTalk(
        0x133,
        (
            "#3501989V#5805F#12PHuh?\x02\x03",
            "#3501990V#5810FIs someone going to try to\x01",
            "do something bad to me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501991V#0004F#5PDon't worry about it, KeA.\x01",
            "We won't let that happen.\x02\x03",
            "#3501992V#0001FBut more importantly...\x02\x03",
            "#3501993VKeA, have you remembered\x01",
            "anything else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        (
            "#3501994V#5811F#12PHmmmmm...\x02\x03",
            "#3501995V#5809FHeeheehee. Nope. Not a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501996V#0006F#5P*sigh* I was afraid so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501997V#0108F#5PStill at square one...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3501998V#0308F#11P...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501999V#0001F#5PHey, Randy...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#3502000V#0304F#11PC'mon, let's save my story for some\x01",
            "other day, okay?\x02\x03",
            "#3502001V#0300FI'll tell ya, as long as you don't kick\x01",
            "me to the curb.\x02",
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
    Sleep(1000)

    def lambda_91B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91B)
    Sleep(50)

    def lambda_92B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92B)
    Sleep(50)

    def lambda_93B():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_93B)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#3502002V#0013F#5PDon't be ridiculous.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3502003V#0201F#6PLearn how to read the room, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3502004V#0101F#5PYes, now's not the time for joking\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3502005V#0302F#11PSorry 'bout that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3502006V#5801F#12PHmm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x133,
        (
            "#3502007V#5810F#6PHey, doggie. Why do Lloyd and the\x01",
            "others look upset?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3502008V#1203F#11PGrrrr...\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x190)

    ChrTalk(
        0x105,
        (
            "#3502009V#0409F#5PHaha, oh, the beauty of youth is\x01",
            "so marvelous.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x133, 0xB4, 0x1F4)

    ChrTalk(
        0x133,
        "#3502010V#5805F#12PYouth?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_B93():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B93)
    Sleep(50)

    def lambda_BA3():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BA3)
    Sleep(50)

    def lambda_BB3():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BB3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#3502011V#0309F#11PHaha, nothin' seems to ever shock\x01",
            "you, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3502012V#0012F#5PYeah, I still find it crazy to think that\x01",
            "we were chased down by the mafia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3502013V#0102F#5PThe world's turned upside down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3502014V#0202F#5PApologies, but this clearly is not a dream.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3502015V#1004F#5PHeh...\x02\x03",
            "#3502016V#1002FAt any rate, we'll go over everything\x01",
            "once we get back to the office.\x02\x03",
            "#3502017VStarting tomorrow, stay on high alert\x01",
            "for the time being.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DAA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DAA)
    Sleep(50)

    def lambda_DBA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DBA)
    Sleep(50)

    def lambda_DCA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DCA)
    Sleep(50)

    def lambda_DDA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DDA)
    Sleep(50)

    def lambda_DEA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DEA)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#3502018V#0001F#12PYes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3502019V#5809F#12POkie dokie!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(0, 6850, -23170, 0)
    MoveCamera(180, 1, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(35770, 0)
    OP_68(0, 6850, 20170, 6000)
    BeginChrThread(0xB, 1, 0, 6)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xB, 0)
    WaitChrThread(0xB, 1)
    SetScenarioFlags(0x5A, 2)
    ClearScenarioFlags(0x5A, 3)
    OP_BA(0x4)
    RemoveParty(0x4, 0x0)
    RemoveParty(0x32, 0x0)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x10)
    OP_29(0x45, 0x4, 0x20)
    SubItemNumber(0x329, 1)
    SubItemNumber(0x32A, 1)
    SubItemNumber(0x330, 1)
    SubItemNumber(0x2DB, 1)
    SubItemNumber(0x348, 1)
    SubItemNumber(0x347, 1)
    SubItemNumber(0x33B, 1)
    SubItemNumber(0x34C, 1)
    SubItemNumber(0x34F, 1)
    SubItemNumber(0x34D, 1)
    SubItemNumber(0x34E, 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x27, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1E3)
    OP_24(0x7E)
    SetScenarioFlags(0x5D, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_14E end

    def Function_3_FDF(): pass

    label("Function_3_FDF")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1008")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_FEA")

    label("loc_1008")

    Return()

    # Function_3_FDF end

    def Function_4_1009(): pass

    label("Function_4_1009")

    Sound(483, 2, 0, 0)
    Sleep(200)
    OP_25(0x1E3, 0xA)
    Sleep(200)
    OP_25(0x1E3, 0x14)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Return()

    # Function_4_1009 end

    def Function_5_103A(): pass

    label("Function_5_103A")

    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x64)
    Return()

    # Function_5_103A end

    def Function_6_1054(): pass

    label("Function_6_1054")

    Sleep(2500)
    OP_25(0x1E3, 0x5A)
    Sleep(400)
    OP_25(0x1E3, 0x50)
    Sleep(400)
    OP_25(0x1E3, 0x46)
    Sleep(400)
    OP_25(0x1E3, 0x3C)
    Sleep(400)
    OP_25(0x1E3, 0x32)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    BeginChrThread(0xB, 0, 0, 8)
    OP_25(0x1E3, 0x14)
    Sleep(400)
    OP_25(0x1E3, 0xA)
    Sleep(400)
    OP_24(0x1E3)
    Return()

    # Function_6_1054 end

    def Function_7_10A0(): pass

    label("Function_7_10A0")

    Sound(126, 2, 0, 0)
    Sleep(100)
    OP_25(0x7E, 0xA)
    Sleep(100)
    OP_25(0x7E, 0x14)
    Sleep(100)
    OP_25(0x7E, 0x1E)
    Sleep(100)
    OP_25(0x7E, 0x28)
    Sleep(100)
    OP_25(0x7E, 0x32)
    Sleep(100)
    OP_25(0x7E, 0x3C)
    Sleep(100)
    OP_25(0x7E, 0x46)
    Sleep(100)
    OP_25(0x7E, 0x50)
    Return()

    # Function_7_10A0 end

    def Function_8_10DF(): pass

    label("Function_8_10DF")

    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Sleep(200)
    OP_25(0x7E, 0x14)
    Sleep(200)
    OP_25(0x7E, 0xA)
    Sleep(200)
    OP_24(0x7E)
    Return()

    # Function_8_10DF end

    SaveToFile()

Try(main)
