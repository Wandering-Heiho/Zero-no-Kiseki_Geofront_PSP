from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1160.bin",                # FileName
        "c1160",                    # MapName
        "c1160",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1160",                  # 0
        "Vice Commissioner Pierre",# 1
        "Deputy Commander Baelz", # 2
        "Noel",                   # 3
    ))

    AddCharChip((
        "chr/ch06402.itc",                   # 00
        "chr/ch06400.itc",                   # 01
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

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_1B8",          # 01, 1
        "Function_2_1D0",          # 02, 2
        "Function_3_BE2",          # 03, 3
        "Function_4_C1B",          # 04, 4
        "Function_5_162A",         # 05, 5
        "Function_6_4D43",         # 06, 6
        "Function_7_4D87",         # 07, 7
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_194")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_1B7")

    label("loc_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1A8")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_1B7")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1B7")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 2)

    label("loc_1B7")

    Return()

    # Function_0_180 end

    def Function_1_1B8(): pass

    label("Function_1_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF")

    Return()

    # Function_1_1B8 end

    def Function_2_1D0(): pass

    label("Function_2_1D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(40710, 1200, -390, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x101, 41600, 0, -2500, 0)
    SetChrPos(0x103, 40600, 0, -2750, 0)
    SetChrPos(0x102, 41600, 0, -4000, 0)
    SetChrPos(0x104, 40600, 0, -4250, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#5PWhat is your report?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHave you actually managed to find it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FYes, sir. We've retrieved the ring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FVice Commissioner Pierre, take a deep breath.\x01",
            "Please stay strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWhat exactly are you preparing me for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#5PIt's just a simple little ring! Do you actually\x01",
            "believe me to be afraid of my wife?!\x01",
            "Well? Do you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0006FNo, sir, of course not...\x01",
            "Um... Anyway, here is our report.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0003F...And that's how it went.\x02\x03",
            "#0001FWe were fortunate enough to persuade\x01",
            "the hostess to return the ring...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWh-Wh-Wha...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 41320, 30, 1710, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_68(40720, 1200, -2260, 3000)
    OP_95(0x8, 43880, 30, 1710, 2000, 0x0)
    OP_95(0x8, 43880, 30, -870, 2000, 0x0)
    OP_95(0x8, 41100, 30, -870, 2000, 0x0)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 3)

    ChrTalk(
        0x8,
        (
            "#5PSurely you must be joking, right?!\x01",
            "There must be some kind of mistake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI did something like that?\x01",
            "ME, OF ALL PEOPLE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FThis lil' carnelian beauty fits your description\x01",
            "of it to a tee. Wild night, eh, Vice Commish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FZeit's keen nose was able to also confirm\x01",
            "the ring as yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0000FWell, uh. Here's the ring we found.\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    EndChrThread(0x8, 0x1)
    OP_95(0x8, 41600, 30, -870, 3000, 0x0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_93(0x8, 0xB4, 0x2EE)
    Sleep(750)
    OP_95(0x8, 41600, 30, -1250, 1000, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Handed over \x07\x02",
            "#16ICarnelia Wedding Ring\x07\x00",
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_98(0x101, 0x0, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#5POh, shi-- *cough, cough*!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#5PGood work.\x01",
            "You all are dismissed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever...our little 'encounter' is\x01",
            "strictly confidential, you hear?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNot even Sergei can know.\x01",
            "NOT A PEEP OUT OF YOU!\x01",
            "Do I make myself clear?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0205FOkay...but I believe you have forgotten\x01",
            "to thank Zeit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 750)

    ChrTalk(
        0x8,
        "#5P*GLARE*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0211FUnderstood.\x01",
            "(Not to worry, Zeit. We will reward you\x01",
            "handsomely with beef treats later.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A1():

        label("loc_9A1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9A1")

    QueueWorkItem2(0x0, 1, lambda_9A1)

    def lambda_9B3():

        label("loc_9B3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9B3")

    QueueWorkItem2(0x1, 1, lambda_9B3)

    def lambda_9C5():

        label("loc_9C5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9C5")

    QueueWorkItem2(0x2, 1, lambda_9C5)

    def lambda_9D7():

        label("loc_9D7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_9D7")

    QueueWorkItem2(0x3, 1, lambda_9D7)
    OP_95(0x8, 43880, 30, -1250, 2000, 0x0)
    OP_95(0x8, 43880, 30, 0, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    ChrTalk(
        0x8,
        (
            "#5PPhew... Saved by the skin of my teeth.\x01",
            "Everything will be okay, Pierre.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(
        0x104,
        "#12P#0300F(Dude just instantly chilled out. Wild.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100F(I'd say this is case closed.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000F(Haha. We shouldn't disturb him\x01",
            "anymore. Let's get back to work.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200F(An agreeable plan.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Lost Wedding Ring]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x33D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x15, 0x1, 0x9)
    OP_29(0x15, 0x4, 0x10)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1D0 end

    def Function_3_BE2(): pass

    label("Function_3_BE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1A")
    OP_95(0x8, 42500, 30, -870, 3000, 0x0)
    OP_95(0x8, 40500, 30, -870, 3000, 0x0)
    Jump("Function_3_BE2")

    label("loc_C1A")

    Return()

    # Function_3_BE2 end

    def Function_4_C1B(): pass

    label("Function_4_C1B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(41000, 1900, -500, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 41100, 0, -2500, 0)
    SetChrPos(0x102, 40100, 0, -2500, 0)
    SetChrPos(0x103, 39100, 0, -2500, 0)
    SetChrPos(0x104, 42100, 0, -2500, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 41100, 200, 1700, 180)
    Sound(818, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Fussy Voice")

    AnonymousTalk(
        0xFF,
        (
            "#0100805V#4SWhat was going through those\x01",
            "thick skulls of yours?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    OP_68(41000, 900, -500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x8,
        (
            "#0100806V#5PHow dare you steer the course away\x01",
            "from the objective of your mission?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100807V#5PNot to mention, all of the credit was\x01",
            "claimed by that damn Arios MacLaine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100808V#5PAnd the worst part about this situation?\x01",
            "This little 'mishap' of yours was exposed\x01",
            "by the Crossbell Times!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0100809V#12P#0011FW-Well, the thing is--\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    ChrTalk(
        0x8,
        (
            "#0100810V#5P#4SKeep each and every one of your mouths\x01",
            "shut. I don't want to hear your excuses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100811V#5P#3SI knew I should have been more vocal\x01",
            "against the formation of this new division!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100812V#5PIf only that damned Sergei hadn't tacked\x01",
            "on so many conditions! This would have\x01",
            "never happened otherwise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100813V#12P#0105FCare to elaborate, sir?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        "#0100814V#5P#4SSilence! This doesn't concern you in any form!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x8,
        "#0100815V#1P#2SD-Damn it all... I've got the perfect idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100816V#1P#2SIt's simple. If I eliminate his subordinates,\x01",
            "that pest will fail to have any clout.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    ChrTalk(
        0x8,
        "#0100817V#5PListen up, maggots. This is for your sake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100818V#5PDecline your assignment to the\x01",
            "'Special Support Section' within\x01",
            "the next couple of days.\x02",
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
        "#0100819V#12P#0005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0100820V#2P#0301FJust a sec, pal. What exactly are you\x01",
            "insinuatin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0100821V#6P#0211FHow cryptic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100822V#5PI don't believe I stuttered, did I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100823V#5PThe SSS is sure to fail within half a year.\x01",
            "I doubt it'll advance your careers at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100824V#5PIt's quite the opposite, actually.\x01",
            "Keep running into trouble, and your\x01",
            "resumes will begin to suffer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0100825V#5PAn utter waste. Do you not agree?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x8,
        (
            "#0100826V#5PAren't you aiming to become a detective, Lloyd?\x01",
            "I'll personally see to it that you are placed\x01",
            "within one of our investigative divisions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100827V#5PNot to worry. I intend on assigning you\x01",
            "roles more synergistic with your skill sets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0100828V#5PI promise you won't regret your decision.\x01",
            "Try sleeping on it. You are dismissed.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C1B end

    def Function_5_162A(): pass

    label("Function_5_162A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("apl/ch50109.itc", 0x20)
    OP_68(-2000, 1100, 15900, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -2300, 0, 16500, 180)
    SetChrPos(0x102, -1700, 0, 16500, 180)
    SetChrPos(0x103, -2300, 0, 16500, 180)
    SetChrPos(0x104, -1700, 0, 16500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02000.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Police Headquarters, 3F...\x07\x00\x02",
        )
    )

    Sleep(2500)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-2000, 1100, 12900, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(1000)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)

    def lambda_17F1():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17F1)

    def lambda_180B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_180B)
    Sleep(350)

    def lambda_181F():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x300C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_181F)

    def lambda_1839():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1839)
    Sleep(350)

    def lambda_184D():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_184D)

    def lambda_1867():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1867)
    Sleep(350)

    def lambda_187B():
        OP_96(0xFE, 0xFFFFFA88, 0x0, 0x34BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_187B)

    def lambda_1895():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1895)
    WaitChrThread(0x101, 1)

    def lambda_18AA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_18AA)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x3)
    WaitChrThread(0x102, 1)

    def lambda_18D0():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_18D0)
    WaitChrThread(0x103, 1)

    def lambda_18E1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18E1)
    WaitChrThread(0x104, 1)

    def lambda_18F2():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_18F2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#1100070V#0306FI can't believe we have to go to Vice\x01",
            "Commish Jackass' office.\x02\x03",
            "#1100071V#0301FWhat kinda bitchin' awaits us this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100072V#6P#0003FRemember that we were told this\x01",
            "was about a client waiting for us.\x02\x03",
            "#1100073V#0000FI think it's safe to say he didn't call\x01",
            "us here to complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100074V#0203FI have a sinking feeling he will find\x01",
            "a reason to scold us regardless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100075V#0106FI know what you mean. We can't let it\x01",
            "get to us, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AE0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AE0)
    Sleep(100)

    def lambda_1AF0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AF0)
    Sleep(50)

    def lambda_1B00():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B00)
    Sleep(50)

    def lambda_1B10():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B10)
    WaitChrThread(0x101, 2)
    OP_68(-2000, 1100, 9900, 3000)

    def lambda_1B32():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B32)
    Sleep(100)
    WaitChrThread(0x102, 2)

    def lambda_1B53():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B53)
    Sleep(50)
    WaitChrThread(0x103, 2)

    def lambda_1B74():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B74)
    Sleep(100)
    WaitChrThread(0x104, 2)

    def lambda_1B95():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B95)
    Sleep(2500)
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(700, 1100, 2300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 700, 30, 2300, 90)
    SetChrPos(0x102, 700, 30, 900, 90)
    SetChrPos(0x103, -500, 30, 2300, 90)
    SetChrPos(0x104, -500, 30, 900, 90)
    OP_68(3700, 1100, 2300, 2000)

    def lambda_1C4A():
        OP_96(0xFE, 0xE74, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C4A)
    Sleep(50)

    def lambda_1C67():
        OP_96(0xFE, 0xE74, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C67)
    Sleep(50)

    def lambda_1C84():
        OP_96(0xFE, 0x9C4, 0x1E, 0x8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C84)
    Sleep(50)

    def lambda_1CA1():
        OP_96(0xFE, 0x9C4, 0x1E, 0x384, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CA1)
    WaitChrThread(0x101, 1)

    def lambda_1CBF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CBF)
    WaitChrThread(0x102, 1)

    def lambda_1CD0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CD0)
    WaitChrThread(0x103, 1)

    def lambda_1CE1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CE1)
    WaitChrThread(0x104, 1)

    def lambda_1CF2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CF2)
    WaitChrThread(0x104, 2)

    def lambda_1D03():
        OP_95(0xFE, 3700, 0, 3200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D03)
    WaitChrThread(0x101, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#1100076V#2P#0001FDetective Bannings reporting in.\x01",
            "The Special Support Section has\x01",
            "arrived.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 3500, 0, 5200, 0)

    NpcTalk(
        0x8,
        "Fussy Voice",
        "#1100077V#2S#5PHmph... Come in!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100078V#2P#0003FExcuse us.\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_79(0x0)
    Sleep(300)

    def lambda_1E2F():
        OP_95(0xFE, 3700, 0, 4500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E2F)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_68(41270, 1000, -4180, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, 42100, 30, 1900, 180)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 42100, 30, -900, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 43000, 0, -1400, 180)
    SetChrPos(0x101, 41000, 0, -7000, 0)
    SetChrPos(0x102, 41000, 0, -7000, 0)
    SetChrPos(0x103, 41000, 0, -7000, 0)
    SetChrPos(0x104, 41000, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(41840, 1000, -2380, 2500)
    SetCameraDistance(22000, 2500)

    def lambda_1F83():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F83)

    def lambda_1F9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F9D)
    Sleep(350)

    def lambda_1FB1():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FB1)

    def lambda_1FCB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1FCB)
    Sleep(350)

    def lambda_1FDF():
        OP_96(0xFE, 0x9EFC, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FDF)

    def lambda_1FF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1FF9)
    Sleep(350)

    def lambda_200D():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_200D)

    def lambda_2027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2027)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#1100079V#6P#0005F(Oh, I recognize that uniform...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100080V#6P#0105F(The Crossbell Guardian Force, right?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_20EE():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFEAE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20EE)
    Sound(1365, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#1100081V#11P#0307F#4SAw, hell!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(
        0x9,
        "Bespectacled Woman",
        (
            "#1100082V#2004F#5POh, my. Is that how you greet an old\x01",
            "acquaintance, Randy Orlando?\x02\x03",
            "#1100083V#2002FCare to elaborate on any hidden meanings\x01",
            "behind that outburst of yours?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100084V#12P#0309FO-Oh, you've got it all wrong...\x01",
            "I was just so excited to see you\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_226C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_226C)
    Sleep(50)

    def lambda_227C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_227C)
    Sleep(50)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x101,
        "#1100085V#5P#0005FDo you two know each other?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100086V#6P#0211FYour reaction is that of a man\x01",
            "with a guilty conscience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100087V#5PAhem... Ahem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100088V#5PShow some respect, you four!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100089V#5PThis here is Lieutenant Colonel Sonya Baelz,\x01",
            "deputy commander of the CGF!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_23F4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23F4)
    Sleep(50)

    def lambda_2404():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2404)
    Sleep(50)
    OP_93(0x103, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#1100090V#6P#0005FDeputy commander of the Guardian Force?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100091V#12P#0101FP-Please forgive our misbehavior.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1100092V#6P#0208F(Lieutenant colonel is one of the higher\x01",
            "ranks in the military chain of command.)\x02\x03",
            "#1100093V(She is that distinguished?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100094V#0306F#12P(Oh, you have no freakin' idea... She IS the\x01",
            "CGF's second-in-command, after all.)\x02\x03",
            "#1100095V#0300F(Takin' in her charisma and expertise, hell,\x01",
            "she might as well be in charge.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100096V#2004F#5PAt ease, Detectives.\x02\x03",
            "#1100097V#2000FYou're the 'Special Support Section,' correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100098V#6P#0000FY-Yes, ma'am.\x02\x03",
            "#1100099VHave you come here to submit\x01",
            "a support request, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100100V#5PHmph, don't get your hopes up, rookies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100101V#5PYou greenhorns better realize how big an\x01",
            "honor it is to meet the deputy commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0x15E, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#1100102V#12P#2003FVice Commissioner Pierre. Allow me to handle\x01",
            "it from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100103V#5PB-But!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100104V#5P...Understood. I'll leave it in your capable hands,\x01",
            "ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100105V#12P#2000FThank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x9,
        (
            "#1100106VAllow me to formally introduce myself. My name\x01",
            "is Sonya Baelz, deputy commander of the Crossbell\x01",
            "Guardian Force.\x02\x03",
            "#1100107VI came here to ask the Special Support Section to\x01",
            "lend us your expertise on a particular matter.\x02\x03",
            "#1100108VLet me begin with a brief overview of the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_68(41300, 900, -2100, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x9, 42200, 0, -2100, 270)
    SetChrPos(0xA, 42500, 0, -3000, 270)
    SetChrPos(0x101, 39700, 0, -2600, 90)
    SetChrPos(0x102, 39700, 0, -1600, 90)
    SetChrPos(0x104, 38400, 0, -2500, 90)
    SetChrPos(0x103, 38400, 0, -1500, 90)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        "#1100109V#0001FAn investigation of monster attacks?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x9,
        (
            "#1100110V#2003F#11PCorrect, Detective.\x02\x03",
            "#1100111V#2000FSeveral locations throughout Crossbell\x01",
            "have reported similar cases of monster\x01",
            "attacks over the past month.\x02\x03",
            "#1100112VWe wish to cooperate with you to\x01",
            "investigate this matter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        (
            "#1100113V#6P#0011FW-Wait, did I just hear you correctly?\x02\x03",
            "#1100114VThese incidents were all reported outside\x01",
            "of Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#1100115V#2000F#11PYes, do you take issue with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100116V#6P#0003FN-No... Not at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100117V#0101F#6PExcuse me, ma'am. An investigation\x01",
            "was already conducted by the CGF,\x01",
            "correct?\x02\x03",
            "#1100118VIs there anything left for us to\x01",
            "investigate at this point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100119V#2006F#11PYes. Plenty, in fact.\x02\x03",
            "#1100120V#2001FToo many questions remain unanswered to\x01",
            "write these off as ordinary monster attacks.\x02\x03",
            "#1100121VAs much as I hate to admit it, our investigators\x01",
            "have hit a dead end.\x02\x03",
            "#1100122VTherefore, I'm hoping that a different point of\x01",
            "view is what the investigation needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100123V#6P#0005F'A different point of view'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100124V#2003F#11PA trained detective's, to be exact.\x01",
            "One that will differ greatly from\x01",
            "a guardsman's.\x02\x03",
            "#1100125V#2000FYou might be wondering, 'Why come\x01",
            "to us, of all people?'\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#1100126V#2002F#2PA valid question. I could have just as easily\x01",
            "sought the help of the renowned First Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#1100127V#5PW-Well, haha... I would love to introduce\x01",
            "you to them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100128V#5P...but, as you know, they are preoccupied\x01",
            "with their duties.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#1100129V#2004F#11PAs you can see, a number of unforeseen\x01",
            "circumstances have led us to seeking the\x01",
            "aid of the SSS.\x02\x03",
            "#1100130V#2000FAre there any objections?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100131V#6P#0002FNo, ma'am...\x02\x03",
            "#1100132V#0004FWe'll gladly accept your request and aid you in\x01",
            "your ongoing investigation.\x02\x03",
            "#1100133V#0001FYou've given us a brief rundown of the situation,\x01",
            "but it'll be hard to begin without concrete facts.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "#1100134V#5P#2000FSeeker, hand it to them.\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1491, 255, 100, 0)

    NpcTalk(
        0xA,
        "Female Guardsman",
        "#1100135V#11P#0500FYes, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(40840, 900, -2120, 1000)

    def lambda_339B():

        label("loc_339B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_339B")

    QueueWorkItem2(0x102, 2, lambda_339B)

    def lambda_33AD():

        label("loc_33AD")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_33AD")

    QueueWorkItem2(0x103, 2, lambda_33AD)

    def lambda_33BF():
        OP_95(0xFE, 40500, 0, -2800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_33BF)
    WaitChrThread(0xA, 1)

    def lambda_33DD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_33DD)
    EndChrThread(0x102, 0x2)

    def lambda_33EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33EE)
    EndChrThread(0x103, 0x2)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(1492, 255, 100, 0)
    SetChrName("Female Guardsman")

    AnonymousTalk(
        0xFF,
        "#1100136VHere you are.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(60, 180, -1, -1)

    AnonymousTalk(
        0x101,
        "#1100137V#0000FOh, thank you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#1100138V#6P#0005F(Huh, could she be?)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Female Guardsman",
        "#1100139V#11P#0505FHmm? Is everything okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100140V#6P#0003FI-I'm fine. My apologies.\x02\x03",
            "#1100141V#0008F(Hmm... I can't help but feel like\x01",
            "I've seen her somewhere before.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D4, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(41300, 900, -2100, 1000)

    def lambda_3646():
        OP_96(0xFE, 0xA604, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3646)
    WaitChrThread(0xA, 1)
    Sleep(500)
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1100142V#6P#0001FIs this a...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100143V#0101F#5PIt appears to be a case report from the CGF.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100144V#2003F#11PCorrect. We've written all of our findings\x01",
            "thus far in that report.\x02\x03",
            "#1100145V#2000FPlease begin your investigation as soon\x01",
            "as you've finished reviewing the case file.\x02\x03",
            "#1100146VDoing so will eliminate unwanted bias from\x01",
            "your work.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37D6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_37D6)
    Sleep(100)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x102,
        "#1100147V#0100F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100148V#6P#0000FIn that case, we'll begin as soon as possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100149V#2004F#11PWe leave it in your capable hands.\x02\x03",
            "#1100150V#2002FWell, I suppose we'll have to excuse ourselves\x01",
            "for now.\x02\x03",
            "#1100151VWe'll establish a direct line of communication\x01",
            "with the SSS, so please contact us if you make\x01",
            "a breakthrough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100152V#6P#0000FWill do.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        "#1100153V#2000F#12PThank you for your time, Vice Commissioner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100154V#5PNo, no. Not at all. Feel free to\x01",
            "drop by my office any time.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    def lambda_3A17():

        label("loc_3A17")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_3A17")

    QueueWorkItem2(0x101, 2, lambda_3A17)

    def lambda_3A29():

        label("loc_3A29")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_3A29")

    QueueWorkItem2(0x102, 2, lambda_3A29)

    def lambda_3A3B():

        label("loc_3A3B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_3A3B")

    QueueWorkItem2(0x103, 2, lambda_3A3B)

    def lambda_3A4D():

        label("loc_3A4D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_3A4D")

    QueueWorkItem2(0x104, 2, lambda_3A4D)

    def lambda_3A5F():
        OP_95(0xFE, 40500, 0, -3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A5F)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#1100155V#2002F#11PHaha...\x02\x03",
            "#1100156VLooks like you're a bit more comfortable\x01",
            "with your current work, Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100157V#0302F#6PHaha, well...\x02\x03",
            "#1100158V#0304FI'd say the work here is more thrillin' than\x01",
            "staring at the border and doin' drills all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1100159V#2004F#11PGood to know... I'm glad it was worth the\x01",
            "effort to introduce you two.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#1100160V#6P#2000FLet's head out, Seeker.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)
    Sound(1478, 255, 100, 0)

    NpcTalk(
        0xA,
        "Female Guardsman",
        "#1100161V#0500F#5PRoger!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(1498, 255, 100, 0)
    Sleep(1000)
    OP_68(41300, 1000, -3600, 2000)
    BeginChrThread(0x9, 3, 0, 6)
    BeginChrThread(0xA, 3, 0, 7)
    WaitChrThread(0x9, 3)
    EndChrThread(0x104, 0x2)

    def lambda_3CC2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3CC2)
    WaitChrThread(0xA, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    Sound(104, 0, 100, 0)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(39100, 1000, -2100, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    OP_93(0x8, 0xE1, 0x0)
    SetChrPos(0x102, 39700, 0, -1500, 180)
    SetChrPos(0x103, 38400, 0, -1400, 180)
    OP_0D()

    ChrTalk(
        0x104,
        "#1100163V#6P#0300FPhew... Man, oh, man.\x02",
    )

    CloseMessageWindow()

    def lambda_3D88():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D88)
    Sleep(100)
    TurnDirection(0x102, 0x104, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100164V#11P#0000FWas she your superior back in the\x01",
            "Guardian Force, Randy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#1100165V#6P#0300FYou got that right... Sonya wasn't my\x01",
            "direct boss, though.\x02\x03",
            "#1100166VShe just gave me a bunch of pointers\x01",
            "for our training and drill sessions.\x02\x03",
            "#1100167V#0306FDon't let her gorgeous looks fool you.\x01",
            "That lady will make you piss your pants\x01",
            "if you cross her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100168V#0200F#5PKnowing you, Randy, your slovenly disposition\x01",
            "likely set her off on multiple occasions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100169V#5P#0104FI imagine so.\x02\x03",
            "#1100170V#0100FHe does have a knack for getting in trouble\x01",
            "with women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100171V#11P#0005FThat reminds me...\x02\x03",
            "#1100172V#0001FDo you know the girl that was accompanying\x01",
            "the deputy commander, Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100173V#6P#0300FDidn't ring a bell... Woulda remembered a cutie\x01",
            "like her.\x02\x03",
            "#1100174VI'd bet a pretty mira that she's in the Tangram\x01",
            "Gate division of the CGF. Those guys work\x01",
            "directly under Sonya.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#1100175V#6P#0305FWait a tick. She catch your eye or somethin'?\x02\x03",
            "#1100176V#0309FWell, I'll be damned. Was it love at first sight?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_41D7)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#1100177V#5P#0111FWell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100178V#0211F#5P*stare*\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#1100179V#11P#0011FWh-What?! No, I didn't mean it like that!\x02\x03",
            "#1100180VI just had a strange feeling that I had\x01",
            "met her somewhere before.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#1100181V#4SAHEM!\x02",
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
    OP_68(40800, 800, 0, 1200)
    SetCameraDistance(22800, 1200)

    def lambda_437E():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_437E)
    Sleep(50)

    def lambda_438E():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_438E)
    Sleep(50)

    def lambda_439E():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_439E)
    Sleep(50)

    def lambda_43AE():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_43AE)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#1100182V#0005F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100183V#5PHow long do you rookies plan to take up\x01",
            "space in my precious office to spew your\x01",
            "pointless drivel all over the floor?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100184V#5PDon't tell me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100185V#5PIs this a plot by that good-for-nothing Sergei\x01",
            "to have you come here and humiliate me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100186V#12P#0011FN-No, sir. Definitely not!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100187V#0103F#6PSorry, sir. Please excuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100188V#5PHmph... Go on! Get out of here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100189V#5PTo think that every single one of\x01",
            "you ignored my kind advice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100190V#5PYou should know full well what's\x01",
            "about to come, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100191V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1100192V#6P#0301FThe hell you implyin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100193V#5PHmph. Enjoy that little investigation of yours\x01",
            "out in the wilderness. I'm sure it'll be a fun little\x01",
            "camping trip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100194V#5PWhy don't we transfer your entire team\x01",
            "to the Guardian Force while we're at it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#1100195V#5PWe can boot that damn Sergei out along with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100196V#6P#0211F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100197V#0103F#6PIf you'll please excuse us.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(3700, 1000, 3500, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 3700, 0, 4000, 180)
    SetChrPos(0x102, 3700, 0, 4000, 180)
    SetChrPos(0x103, 3700, 0, 4000, 180)
    SetChrPos(0x104, 3700, 0, 4000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    OP_68(3700, 1100, 1400, 2500)

    def lambda_48DF():
        OP_96(0xFE, 0xE74, 0x0, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48DF)

    def lambda_48F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48F9)
    Sleep(500)

    def lambda_490D():
        OP_96(0xFE, 0x125C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_490D)

    def lambda_4927():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4927)
    Sleep(500)

    def lambda_493B():
        OP_96(0xFE, 0xA8C, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_493B)

    def lambda_4955():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4955)
    Sleep(500)

    def lambda_4969():
        OP_96(0xFE, 0xE74, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4969)

    def lambda_4983():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4983)
    Sleep(500)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x101, 1)

    def lambda_49B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_49B0)
    WaitChrThread(0x102, 1)

    def lambda_49C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_49C1)
    WaitChrThread(0x103, 1)

    def lambda_49D2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_49D2)
    WaitChrThread(0x104, 1)

    def lambda_49E3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_49E3)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#1100198V#0306F#5PGeez... That jackass sure knows\x01",
            "how to get on my nerves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1100199V#0203F#6PI wish I had earplugs on hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100200V#11P#0106FThen again, I suppose we were being\x01",
            "disrespectful in front of him.\x02\x03",
            "#1100201V#0101FHowever, that doesn't warrant his\x01",
            "condescendingly vulgar tone with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100202V#12P#0003FTry not to think about it too much.\x01",
            "Arguing will get us nowhere.\x02\x03",
            "#1100203V#0001FLet's head back and go through the\x01",
            "report in more detail.\x02\x03",
            "#1100204VWe can get started once we've decided\x01",
            "on the direction of our investigation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C28)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#1100205V#5P#0100FI get the impression these attacks\x01",
            "weren't from an ordinary monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100206V#6P#0200FThe culprit behind these attacks\x01",
            "certainly seems enigmatic.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_162A end

    def Function_6_4D43(): pass

    label("Function_6_4D43")

    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_4D4F():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4D4F)
    Sleep(1000)

    def lambda_4D6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4D6C)
    Sound(103, 0, 100, 0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_6_4D43 end

    def Function_7_4D87(): pass

    label("Function_7_4D87")

    Sleep(600)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_4D97():
        OP_95(0xFE, 40500, 0, -5000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4D97)
    WaitChrThread(0xA, 1)

    def lambda_4DB5():
        OP_95(0xFE, 40500, 0, -7500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4DB5)
    Sleep(500)

    def lambda_4DD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DD2)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    Return()

    # Function_7_4D87 end

    SaveToFile()

Try(main)
