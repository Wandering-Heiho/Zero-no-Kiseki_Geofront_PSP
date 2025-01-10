from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0310.bin",                # FileName
        "e0310",                    # MapName
        "e0310",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0310",                  # 0
        "Harold",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_C0",           # 00, 0
        "Function_1_D0",           # 01, 1
        "Function_2_D1",           # 02, 2
        "Function_3_AD7",          # 03, 3
    ))


    def Function_0_C0(): pass

    label("Function_0_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_CF")

    Return()

    # Function_0_C0 end

    def Function_1_D0(): pass

    label("Function_1_D0")

    Return()

    # Function_1_D0 end

    def Function_2_D1(): pass

    label("Function_2_D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50101.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_68(210, 1100, -880, 0)
    MoveCamera(320, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11750, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 850, 100, -2000, 180)
    SetChrPos(0x102, 950, 100, 550, 180)
    SetChrPos(0x103, 50, 100, 550, 180)
    SetChrPos(0x104, -850, 100, 550, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -650, 100, -1850, 180)
    Sound(460, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    SetCameraDistance(10750, 2000)
    OP_6F(0x10)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#1100691V#0000F#12PThank you for the ride back,\x01",
            "Mr. Hayworth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100692V#3609F#5PHaha, my pleasure. I was heading\x01",
            "back to the city, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100693V#0302F#11PMan, must be awesome to own your own\x01",
            "orbal car.\x02\x03",
            "#1100694VHow much did this baby set you back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100695V#0203F#11PI believe a vehicle of this model and\x01",
            "manufacturer would cost approximately\x01",
            "800,000 mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1100696V#0005F#12P800,000 mira... I can't even imagine\x01",
            "having that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100697V#3604F#5PWell, it's an invaluable tool for a trader\x01",
            "like myself.\x02\x03",
            "#1100698V#3600FI could take the bus, but transit time\x01",
            "would end up bottlenecking business...\x02\x03",
            "#1100699VSo, I decided to bite the bullet and buy\x01",
            "a car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1100700V#0104F#11PI'm sure you had other reasons to buy it,\x01",
            "aside from business.\x02\x03",
            "#1100701V#0102FFor example, I bet it lets you get home to\x01",
            "your wife and son earlier, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#1100702V#3609F#5PHaha, you caught me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1100703V#0302F#11PAh, there's the real reason. Got gifts\x01",
            "for them and everything, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1100704V#0202F#11PIs this what people call the ideal\x01",
            "husband and father?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100705V#3604F#5PNo, no. That's giving me far too much\x01",
            "credit.\x02\x03",
            "#1100706V#3600FI often have to go on business trips,\x01",
            "forced to leave my wife and son at\x01",
            "home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100707V#0000F#12PHow old is your son?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100708V#3609F#5PHe turns five years old this year.\x02\x03",
            "#1100709VHe's not quite at that Sunday School\x01",
            "age yet, but he's filled with curiosity.\x02\x03",
            "#1100710V#3600FIn fact, his constant questions and desire\x01",
            "to learn about his surroundings can be a\x01",
            "bit overwhelming for his mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#1100711V#0002F#12PWow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1100712V#0102F#11PYou all sound like a happy family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100713V#3609F#5PHaha, yes, we are.\x02\x03",
            "#1100714V#3608F#30WBesides, I... We have to be happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#1100715V#0005F#12PPardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1100716V#3605F#5POh, pay no mind to that.\x01",
            "Simply thinking aloud.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#1100717V#3600F#5PLook, we should be close to the\x01",
            "end of the old road now.\x02\x03",
            "#1100718VI'll be taking a right turn up here,\x01",
            "just as a heads-up.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_25(0x1CC, 0x5A)
    Sleep(80)
    OP_25(0x1CC, 0x50)
    Sleep(80)
    OP_25(0x1CC, 0x46)
    Sleep(80)
    OP_25(0x1CC, 0x3C)
    Sleep(80)
    OP_25(0x1CC, 0x32)
    Sleep(80)
    OP_25(0x1CC, 0x28)
    Sleep(80)
    OP_25(0x1CC, 0x1E)
    Sleep(80)
    OP_25(0x1CC, 0x14)
    Sleep(80)
    OP_25(0x1CC, 0xA)
    Sleep(80)
    OP_25(0x1CC, 0x0)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_D1 end

    def Function_3_AD7(): pass

    label("Function_3_AD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFB")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_AD7")

    label("loc_AFB")

    Return()

    # Function_3_AD7 end

    SaveToFile()

Try(main)
