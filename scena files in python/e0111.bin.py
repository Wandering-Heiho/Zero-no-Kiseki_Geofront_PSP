from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0111.bin",                # FileName
        "e0111",                    # MapName
        "e0111",                    # Location
        0x0001,                     # MapIndex
        "ed7516",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0111",                  # 0
        "Zeit",                   # 1
        "Mr. Crois",              # 2
        "Mariabell",              # 3
        "Chief Sergei",           # 4
        "SE制御",                 # 5
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A0",          # 02, 2
        "Function_3_2A1",          # 03, 3
        "Function_4_1080",         # 04, 4
        "Function_5_10A5",         # 05, 5
        "Function_6_10CA",         # 06, 6
        "Function_7_10FB",         # 07, 7
        "Function_8_2321",         # 08, 8
        "Function_9_2379",         # 09, 9
        "Function_10_2565",        # 0A, 10
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)
    Jump("loc_29F")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_29F")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_29F")

    Return()

    # Function_1_27C end

    def Function_2_2A0(): pass

    label("Function_2_2A0")

    Return()

    # Function_2_2A0 end

    def Function_3_2A1(): pass

    label("Function_3_2A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02708.itc", 0x1E)
    LoadChrToIndex("apl/ch50511.itc", 0x1F)
    LoadChrToIndex("chr/ch05502.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("chr/ch00102.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("chr/ch00302.itc", 0x24)
    LoadChrToIndex("chr/ch08202.itc", 0x25)
    LoadChrToIndex("chr/ch08702.itc", 0x26)
    SoundLoad(460)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(305, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x153, 0x25)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x158, 0x26)
    SetChrSubChip(0x158, 0x0)
    SetChrFlags(0x158, 0x4)
    SetChrPos(0x101, -400, 100, 600, 90)
    SetChrPos(0x102, -400, 100, 2000, 90)
    SetChrPos(0x103, -100, 100, 2600, 135)
    SetChrPos(0x104, 1300, 100, 3000, 180)
    SetChrPos(0x153, -400, 100, 1300, 90)
    SetChrPos(0x158, 500, 100, 3000, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 900, 100, -600, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 100, -1900, 180)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 900, 100, -1900, 180)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(460, 2, 80, 0)
    OP_68(0, 1100, 0, 5000)
    SetCameraDistance(26500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#5200323V#2803F#5PNot only Revache, but the\x01",
            "Guardian Force as well...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200324V#12P#2906FSounds like we're in a bit\x01",
            "of a predicament.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200325V#11P#0006FYeah. Honestly, all of this feels\x01",
            "like some insane nightmare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200326V#11P#0105FBy the way, how did you\x01",
            "know we needed help?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200327V#2800F#5PAh, you see, I was just heading home from\x01",
            "a business meeting in the Republic.\x02\x03",
            "#5200328V#2803FWhile passing through Tangram Gate,\x01",
            "we were ambushed by the mafia.\x02\x03",
            "#5200329V#2801FLuckily, we shook them and made it to\x01",
            "the city, just in time to see that you\x01",
            "were all in a pinch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200330V#11P#0101FWe got lucky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200331V#11P#0304FMan, you seriously saved\x01",
            "our skin back there.\x02\x03",
            "#5200332V#0305FThis car bulletproof?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200333V#2809F#5PIndeed, it was custom-made.\x02\x03",
            "#5200334V#2800FThe glass is bulletproof, too,\x01",
            "so it can take a beating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200335V#0202F#11PThe latest model of bulletproof limousine,\x01",
            "manufactured by the Reinford Company,\x01",
            "if I am not mistaken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200336V#11P#0300FThis thing is a beast...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200337V#12P#2903FWell, it's not like it can\x01",
            "withstand explosions.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#5200338V#12P#2901FFather. Are we returning\x01",
            "to the IBC now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200339V#2804F#5PYes, that's the plan.\x02\x03",
            "#5200340V#2800FI'm sure our friends here are exhausted\x01",
            "from what's happened. Let's prepare\x01",
            "beds for them right when we get back.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5200341V#11P#0011FSir, you really don't have\x01",
            "to do any more than this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200342V#11P#0108FWe appreciate the offer,\x01",
            "but we really should...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200343V#12P#2904FElie. Please, don't\x01",
            "talk like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200344V#2800F#5PThe IBC's front gate is made with a\x01",
            "special alloy. It won't come down easily.\x02\x03",
            "#5200345V#2803FAnd as the CEO of the IBC,\x01",
            "I cannot allow myself to turn a\x01",
            "blind eye to this chaos...\x02\x03",
            "#5200346V#2801FIf possible, I'd love it if you could give\x01",
            "me a brief report on the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200347V#11P#0102FUncle Dieter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200348V#11P#0002FUnderstood, sir. I apologize\x01",
            "for all the trouble, in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5200349V#12P#2902FHehe, well, that's that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#5200350V#5P#1108F#60W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x158,
        "#5200351V#11P#6008F#60W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200352V#0000F#5PYou two look like you're about\x01",
            "to pass out from exhaustion...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#5200353V#11P#1101F#40WHuh...? No, I'm not\x01",
            "sleepy! Not one bit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x158,
        "#5200354V#11P#6000F#40WI-I'm fine, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200355V#11P#0106FI can hardly blame them.\x01",
            "It's almost 10PM, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200356V#11P#0300FCan't forget that we dragged the\x01",
            "poor kiddos all over the city, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5200357V#12P#2909FHehe, once we arrive at the IBC,\x01",
            "we'll find nice, warm beds for you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200358V#2800F#5PAll right, now that everything's\x01",
            "settled...it's time to floor it!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1100, 5000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    BeginChrThread(0xC, 1, 0, 6)
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x158, 0x4)
    SetChrChipByIndex(0x158, 0xFF)
    SetChrSubChip(0x158, 0x0)
    RemoveParty(0x52, 0x0)
    RemoveParty(0x57, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xC, 1)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2A1 end

    def Function_4_1080(): pass

    label("Function_4_1080")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_4_1080")

    label("loc_10A4")

    Return()

    # Function_4_1080 end

    def Function_5_10A5(): pass

    label("Function_5_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10C9")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_5_10A5")

    label("loc_10C9")

    Return()

    # Function_5_10A5 end

    def Function_6_10CA(): pass

    label("Function_6_10CA")

    Sleep(200)
    OP_25(0x1CC, 0x3C)
    Sleep(200)
    OP_25(0x1CC, 0x32)
    Sleep(200)
    OP_25(0x1CC, 0x28)
    Sleep(200)
    OP_25(0x1CC, 0x1E)
    Sleep(200)
    OP_25(0x1CC, 0x14)
    Sleep(200)
    OP_25(0x1CC, 0xA)
    Sleep(200)
    OP_24(0x1CC)
    Return()

    # Function_6_10CA end

    def Function_7_10FB(): pass

    label("Function_7_10FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50518.itc", 0x1E)
    LoadChrToIndex("apl/ch50519.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    SoundLoad(492)
    OP_68(100000, 900, 5000, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 99600, 100, -300, 90)
    SetChrPos(0x102, 99600, 100, -1200, 90)
    SetChrPos(0x104, 99600, 100, -2200, 90)
    SetChrPos(0x103, 100900, 100, -3000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, -100, 900, 270)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 101000, 100, 2250, 0)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0xFF, "wine", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x4)
    LoadEffect(0x0, "battle\\cr008101.eff")
    LoadEffect(0x1, "event\\ev608_01.eff ")
    LoadEffect(0x2, "event\\eva01_00.eff")
    LoadEffect(0x3, "event\\eva03_00.eff")
    BeginChrThread(0x101, 3, 0, 4)
    Sound(492, 2, 100, 0)
    OP_68(100000, 900, 0, 5000)
    SetCameraDistance(28500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_0D()
    OP_6F(0x11)

    ChrTalk(
        0x104,
        "#5300001V#0309FWoohoohoooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300002V#0002F#5PChief...you're incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5300003V#0109F#5PYou broke through their\x01",
            "line like it was nothing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300004V#6P#0202FColor me surprised.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5300005V#1004F#5PWell, it's been about half a year since\x01",
            "I was behind the wheel, but I still got it.\x02\x03",
            "#5300006V#1001FAll right, now we'll keep cruising like\x01",
            "this till we get to Old Armorica Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300007V#0000F#5PNo complaints here!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)
    Sound(2047, 255, 100, 0)

    ChrTalk(
        0x8,
        "#5300008V#11P#1201FGrrrrr...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300009V#0005F#5PZeit...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300010V#0301FSomethin' comin', boy?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5300011V#6P#0207FVehicles on our six...!\x02\x03",
            "#5300012VThe Guardian Force caught up to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5300013V#1005F#5PWhat...?!\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 2000)
    FadeToDark(2000, 0, -1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev03.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x102, 3, 0, 8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5300014V#0010F#5PCrap...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300015V#0106F#5PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5300016V#6P#0208FThis isn't ideal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300017V#0310FThey really brought out\x01",
            "the big guns, didn't they?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5300018V#1007F#5PAll we can do is shake 'em off!\x02\x03",
            "#5300019VHope you're wearing your seatbelts!\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x0)
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xB, 0x0, -200, 300, 300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_1853():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1853)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        "#5300020V#1010F#4SGah...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    OP_68(100000, 900, 1000, 1500)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5300021V#0011F#5PCh-Chief?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300022V#0101F#5PAre you all right...?!\x02",
    )

    CloseMessageWindow()

    def lambda_190F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_190F)
    SetChrSubChip(0xB, 0x2)
    Sleep(800)

    ChrTalk(
        0xB,
        (
            "#5300023V#1003F#5P#40WD-Don't worry about me.\x01",
            "It's just a scratch...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300024V#0013F#5PB-But, that injury...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300025V#0307FWe gotta stop the bleedin'!\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5300026V#6P#0201FAnother vehicle approaching\x01",
            "from the rear!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x102,
        "#5300027V#0108F#11PN-No way...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5300028V#0007F#5PPlease, just stop the car!\x02\x03",
            "#5300029VWe have to treat this, now!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#5300030V#1010F#5P#30WListen, I said I'm fine.\x01",
            "Now hold on tight...!\x02\x03",
            "#5300031VClearing the way for you youngsters\x01",
            "is my responsibility as your superior...\x02\x03",
            "#5300032V#1007FAnd I'm not letting you down...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300033V#0005F#5PCh-Chief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5300034V#0306FWho's this hothead and where's our chief...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5300035V#6P#0205FWait...\x02\x03",
            "#5300036V#0214FTheir reinforcement vehicle\x01",
            "isn't one of the newer models!\x02\x03",
            "#5300037VIt's Noel's...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5300038V#0002F#5P...!\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev04.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xC, 1, 0, 10)
    Sleep(2500)

    ChrTalk(
        0x101,
        "#5300039V#0000F#5PSergeant Major Seeker...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5300040V#0102F#5PShe came for us...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5300041V#0309FHaha, that's the Guardian Force's\x01",
            "up-and-coming star for ya...!\x02",
        )
    )

    CloseMessageWindow()
    Sound(962, 0, 100, 0)
    Sleep(1800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5300042V\x07\x05",
            "Everyone, do you read me?!\x02\x03",
            "#5300043VThis is Sergeant Major Noel Seeker!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    ChrTalk(
        0x101,
        "#5300044V#0002F#6PWe hear you loud and clear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5300045V#1004F#6P#30WSonya's pride and joy, eh?\x01",
            "You saved our asses, kid!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("Noel's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5300046V\x07\x05",
            "Haha, it's my duty, sir.\x02\x03",
            "#5300047VYou can leave the remaining\x01",
            "vehicle to me!\x02\x03",
            "#5300048VPlease, go on ahead!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xB,
        "#5300049V#1007F#6PGot it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5300050V#0007F#6PBe careful, Sergeant Major!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xC, 0x1)
    EndChrThread(0x101, 0x3)
    OP_82(0x96, 0x0, 0xBB8, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 4)
    Fade(100)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    PlayEffect(0x3, 0x0, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_68(100000, 900, -10000, 4000)
    MoveCamera(330, 13, 0, 4000)
    SetCameraDistance(32000, 4000)
    FadeToDark(4000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev05.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1EC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r307B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_10FB end

    def Function_8_2321(): pass

    label("Function_8_2321")

    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(196, 0, 100, 0)
    Sleep(1000)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)
    Sound(200, 0, 100, 0)
    Sleep(1200)
    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(834, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_8_2321 end

    def Function_9_2379(): pass

    label("Function_9_2379")

    Sound(960, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 98500, -500, 2200, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(99000, 900, 0, 100)
    OP_82(0x320, 0x0, 0x1388, 0x2BC)
    Sleep(100)
    ClearMapObjFlags(0x2, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x3, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x4, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1700, 1800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x5, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 1300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 2900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x7, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_9_2379 end

    def Function_10_2565(): pass

    label("Function_10_2565")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2590")
    Sound(961, 0, 100, 0)
    Sleep(1500)
    Sound(961, 0, 100, 0)
    Sleep(2500)
    Sound(961, 0, 100, 0)
    Sleep(2000)
    Jump("Function_10_2565")

    label("loc_2590")

    Return()

    # Function_10_2565 end

    SaveToFile()

Try(main)
