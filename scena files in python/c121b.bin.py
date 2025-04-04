from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c121b.bin",                # FileName
        "c121b",                    # MapName
        "c121b",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 0, 0, 1],
    )

    BuildStringList((
        "c121b",                  # 0
        "Cao",                    # 1
        "Lau",                    # 2
        "Yin",                    # 3
        "Member",                 # 4
        "Member",                 # 5
        "SE制御",                 # 6
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_1EC",          # 01, 1
        "Function_2_1ED",          # 02, 2
        "Function_3_1391",         # 03, 3
        "Function_4_24CA",         # 04, 4
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1DC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_1EB")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1EB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 3)

    label("loc_1EB")

    Return()

    # Function_0_1C8 end

    def Function_1_1EC(): pass

    label("Function_1_1EC")

    Return()

    # Function_1_1EC end

    def Function_2_1ED(): pass

    label("Function_2_1ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06302.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch00500.itc", 0x20)
    OP_68(4450, 900, 130, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 0, 0, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7300, 0, 3300, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    LoadEffect(0x0, "event\\ev202_00.eff")
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x9,
        "#2101756V#5PThat concludes this week's report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2101757V#5PThe war hounds they've trained may\x01",
            "prove troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2101758V#5PIf Master Yin were available, he would\x01",
            "easily compensate for our lack of force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101759V#11P#3203FHmm... Very well.\x02\x03",
            "#2101760V#3200FProceed with preparations as planned.\x02\x03",
            "#2101761VNext on the agenda... Recall half of\x01",
            "our personnel currently dispatched\x01",
            "in Altair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2101762V#5PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2101763V#5PI shall take my leave, Master Cao. Have\x01",
            "a pleasant evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2101764V#11P#3209FYes, yes. To you, as well.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(2790, 900, 630, 2000)

    def lambda_59D():
        OP_95(0xFE, -4500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_59D)
    Sleep(3000)
    Sound(103, 0, 100, 0)

    def lambda_5C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5C0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(5030, 900, 220, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20760, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#2101765V#11P#3201F*sigh* How troublesome.\x02\x03",
            "#2101766VI'll have to worry about the consequences\x01",
            "later if I request the elders' assistance.\x02\x03",
            "#2101767V#3206FIf only Master Yin were more cooperative,\x01",
            "our plans would be proceeding splendidly.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1628, 255, 100, 0)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sleep(500)

    NpcTalk(
        0xA,
        "Voice",
        (
            "#2101768V\x07\x03",
            "#NWorry not. I plan to uphold my end of the\x01",
            "bargain.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(5680, 900, 1890, 3000)
    MoveCamera(47, 15, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0xFF, 0xA, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    ClearChrFlags(0xA, 0x8)
    SetChrChip(0x0, 0xA, 0x1E, 0x12C)

    def lambda_815():
        OP_95(0xFE, 5800, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_815)

    def lambda_82F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_82F)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_93(0xA, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2101769V\x07\x00",
            "#4P#3205FIt shouldn't surprise me that you were\x01",
            "eavesdropping.\x02\x03",
            "#2101770V#3204FDear me, I fear I may have made a few\x01",
            "slips of the tongue.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1627, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Man in Suit")

    AnonymousTalk(
        0xFF,
        (
            "#2101771V\x07\x03",
            "#30WPlease. As if you did not say those\x01",
            "things intentionally.\x02\x03",
            "#2101772VAlways the tough customer,\x01",
            "aren't you, Cao?\x02",
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
        0x8,
        (
            "#2101773V\x07\x00",
            "#4P#3204FGoodness, no! You, on the other hand...\x02\x03",
            "#2101774V#3200FNever mind that. Do you wish to discuss\x01",
            "business tonight?\x02\x03",
            "#2101775VOr are you perhaps in the mood to\x01",
            "cull some war hounds?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Black-Shrouded Man",
        (
            "#2101776V\x07\x03",
            "#5P#0700FYour subordinates are more than capable\x01",
            "enough to handle such a minor threat.\x02\x03",
            "#2101777VThe deal was to have me take care of\x01",
            "Revache's main force. Beginning with\x01",
            "that man, Garcia.\x02\x03",
            "#2101778VBut do correct me if I'm mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101779V\x07\x00",
            "#4P#3206FOh, dear. You truly are no fun.\x02\x03",
            "#2101780V#3201FIt's come to my attention that you've become\x01",
            "entangled with Arc en Ciel for some odd reason.\x02\x03",
            "#2101781VJust a reminder that the CPD isn't too shabby\x01",
            "at their jobs, so don't do anything to soil my\x01",
            "good name... Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Black-Shrouded Man",
        (
            "#2101782V\x07\x03",
            "#5P#0702FHeh. No need to worry.\x02\x03",
            "#2101783VMore importantly...what kind of impression has\x01",
            "the Special Support Section left on you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101784V\x07\x00",
            "#4P#3205FOh, so that's your game. You have ties to\x01",
            "them, do you?\x02\x03",
            "#2101785V#3204FLet's see...\x01",
            "They are an odd combination of children.\x02\x03",
            "#2101786V#3200FEspecially their leader, Lloyd.\x02\x03",
            "#2101787VHe's perfectly aware of his weakness, yet he\x01",
            "continues to push forward with determination.\x02\x03",
            "#2101788V#3209FHis intuition is enough to keep him on his toes,\x01",
            "too. I quite like his type, to be honest.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Black-Shrouded Man",
        (
            "#2101789V\x07\x03",
            "#5P#0700FI was not asking you about your tastes.\x02\x03",
            "#2101790VWhat about the other members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101791V\x07\x00",
            "#4P#3204FAgain, each one of them proves to be quite\x01",
            "interesting.\x02\x03",
            "#2101792V#3200FMayor MacDowell's granddaughter possesses\x01",
            "a keen sense of diplomacy and operates as the\x01",
            "team's administrator.\x02\x03",
            "#2101793VAs for the girl from the Epstein Foundation...\x01",
            "While her orbal staff itself is fascinating, she\x01",
            "is likely hiding a few tricks up her sleeve.\x02\x03",
            "#2101794V#3204FLastly, we have our ginger gentleman. This may\x01",
            "only be my intuition speaking, but I felt that he's\x01",
            "the same as us. Surely you understand?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Black-Shrouded Man",
        (
            "#2101795V\x07\x03",
            "#5P#0700FYes.\x02\x03",
            "#2101796V...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2101797V\x07\x00",
            "#4P#3200FI must ask... Why have you taken such\x01",
            "great interest in them?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Black-Shrouded Man",
        (
            "#2101798V\x07\x03",
            "#5P#0702FWhatever do you mean? I only wish\x01",
            "to put them to a little test.\x02\x03",
            "#2101799VA request from Yin... Was I right to\x01",
            "entrust them with such a task?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1ED end

    def Function_3_1391(): pass

    label("Function_3_1391")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    LoadChrToIndex("apl/ch50406.itc", 0x22)
    SoundLoad(940)
    SoundLoad(941)
    SoundLoad(942)
    OP_68(5800, 900, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7300, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6100, 0, -2100, 0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -4500, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -4500, 0, 0, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4100894VRevache managed to recover their\x01",
            "smuggling routes?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(7300, 900, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x9,
        "#4100895V#11PYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100896V#11PThree of the routes we decimated over the\x01",
            "last week have already been reorganized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100897V#11PWe've been trying to impede them, but their\x01",
            "resilience was most unexpected...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100898V#3203F#5PHmmm. How curious.\x02\x03",
            "#4100899VI was led to believe that they didn't have the\x01",
            "manpower to accomplish such a thing.\x02\x03",
            "#4100900V#3200FDid their boss finally involve himself in their\x01",
            "restoration efforts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4100901V#11PThat's the strangest part.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100902V#11PThe Killing Bear was nowhere to be found. This\x01",
            "appeared to solely be the work of subordinates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100903V#11PThe reports state that they only brought enough\x01",
            "for a small squad. Not only that, but there were\x01",
            "no war hounds present, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#4100904V#3205FHow interesting. Now I'm even more curious.\x02\x03",
            "#4100905V#3203FHad this been a battle of even numbers, Heiyue\x01",
            "should have come out victorious.\x02\x03",
            "#4100906V#3201FDid they employ those Reinford heavy machine\x01",
            "guns, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100907V#11PYes, actually. Their main forces appeared to\x01",
            "have been armed with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100908V#11PHowever, the report also mentions that their\x01",
            "battle prowess has skyrocketed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100909V#3203F#5PInteresting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#4100910V#3204F#5PI get the impression Don Marconi is trying his\x01",
            "damnedest to appease the speaker and quell\x01",
            "his rage.\x02\x03",
            "#4100911VI don't recall any new reports of jaegers being\x01",
            "employed or any training exercises being held,\x01",
            "either.\x02\x03",
            "#4100912V#3210FHmm. Very peculiar, indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100913V#11PAre you implying that they've acquired a trump\x01",
            "card right under our noses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#4100914V#3200FPrecisely.\x02\x03",
            "#4100915V#3204FWhen comparing our respective trump cards,\x01",
            "I get the feeling that theirs is extraordinary.\x02\x03",
            "#4100916V#3210FMuch like Master Yin, I believe that theirs is a\x01",
            "wild card--one that can turn the tides of battle\x01",
            "at a moment's notice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4100917V#11PDamn them. What in the world is it, then?\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(940, 2, 80, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(941, 2, 80, 0)

    def lambda_1D74():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D74)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    ChrTalk(
        0x9,
        "#4100918V#11PWh-What was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#4100919V#11P#3201FAh, yes. Speak of the devil, and he shall come.\x02",
    )

    CloseMessageWindow()
    Sound(942, 2, 80, 0)
    OP_68(6300, 800, 0, 1500)
    MoveCamera(50, 15, 0, 1500)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1E4A():
        OP_95(0xFE, 2100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1E4A)

    def lambda_1E64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E64)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_64(0xB)
    OP_6F(0x79)

    ChrTalk(
        0xB,
        "#4100920V#6PW-We've got a big problem on our hands!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4100921V#6PA group of men draped in black are unloading\x01",
            "rounds into the building! Revache, I think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4100922V#6PThere's about ten of them, and the Killing Bear\x01",
            "isn't one of them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100923V#11PThere are only ten measly grunts? Hurry it up\x01",
            "and finish them off, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4100924V#11PAnd don't worry about the police! This is self-\x01",
            "defense, so anything goes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#4100925V#6PW-Well, the thing is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#4100926V#6PThose guys aren't human, I'm telling you!\x01",
            "They're holding massive machine guns with\x01",
            "just one hand!\x02",
        )
    )

    CloseMessageWindow()
    Sound(834, 0, 100, 0)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2110():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2110)

    def lambda_2121():
        OP_95(0xFE, 2200, 0, -1100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2121)
    WaitChrThread(0xC, 1)
    OP_64(0xC)
    OP_93(0xC, 0x5A, 0x1F4)
    WaitChrThread(0xC, 2)

    ChrTalk(
        0xC,
        "#4100927V#6PThe first floor has been breached!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#4100928V#6PIt's only a matter of time before they reach\x01",
            "us, sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4100929V#11PD-Damn it... If only Master Yin was here!\x02",
    )

    CloseMessageWindow()
    OP_68(7300, 800, 0, 1500)
    SetCameraDistance(22500, 1500)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(882, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(500)
    OP_6F(0x11)

    ChrTalk(
        0x8,
        (
            "#4100930V#11P#3204FOh, dear.\x02\x03",
            "#4100931V#3200FI don't think I'll be able to outwit them in a\x01",
            "barbaric situation like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x0, 0x1F4)

    ChrTalk(
        0x9,
        "#4100932V#11PMaster Cao, you don't mean...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    SetCameraDistance(21500, 800)
    Fade(250)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sound(939, 0, 100, 0)
    OP_6F(0x10)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)

    ChrTalk(
        0x8,
        (
            "#4100933V#11P#3203FLet's go, Lau.\x02\x03",
            "#4100934V#3210FRelying on Yin for a petty squabble like\x01",
            "this would be a stain on Heiyue's name.\x02\x03",
            "#4100935VCome. Let us demonstrate our might as\x01",
            "the conquerors of the Eastern Quarter.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 4)
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    WaitChrThread(0xD, 1)
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    SetScenarioFlags(0x5D, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1391 end

    def Function_4_24CA(): pass

    label("Function_4_24CA")

    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x64)
    OP_25(0x3AD, 0x64)
    OP_25(0x3AE, 0x64)
    Sleep(1500)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)
    Sleep(300)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    OP_25(0x3AC, 0x32)
    OP_25(0x3AD, 0x32)
    OP_25(0x3AE, 0x32)
    Sleep(300)
    OP_25(0x3AC, 0x28)
    OP_25(0x3AD, 0x28)
    OP_25(0x3AE, 0x28)
    Sleep(300)
    OP_25(0x3AC, 0x1E)
    OP_25(0x3AD, 0x1E)
    OP_25(0x3AE, 0x1E)
    Sleep(300)
    OP_25(0x3AC, 0x14)
    OP_25(0x3AD, 0x14)
    OP_25(0x3AE, 0x14)
    Sleep(300)
    OP_25(0x3AC, 0xA)
    OP_25(0x3AD, 0xA)
    OP_25(0x3AE, 0xA)
    Sleep(300)
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    Return()

    # Function_4_24CA end

    SaveToFile()

Try(main)
