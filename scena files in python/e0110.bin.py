from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0110.bin",                # FileName
        "e0110",                    # MapName
        "e0110",                    # Location
        0x0001,                     # MapIndex
        "ed7102",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0110",                  # 0
        "Lechter",                # 1
        "Mr. Crois",              # 2
    ))

    DeclNpc(-449,    150,     1500,    90,   500,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(750,     150,     3150,    180,  500,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07402.itc", 0x1E)
    LoadChrToIndex("chr/ch05602.itc", 0x1F)
    OP_68(0, 1000, 2650, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28500, 0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "bg00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x32, 0x1F4)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_END)), "loc_3AA")

    ChrTalk(
        0x9,
        (
            "#2801FAllow me to be frank. How would\x01",
            "you like to come work for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3510FHmm, let's see... It kinda hinges on the hourly wage,\x01",
            "to be honest.\x02\x03",
            "#3509FOh, and if you threw in overtime and hazard pay,\x01",
            "you'd be driving a hard bargain!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2809FHahaha...! I think that can be arranged!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500F#3P(Huh? That's the IBC CEO, but...who's that tourist\x01",
            "in the weird getup?)\x02\x03",
            "(They make a strange duo...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F#3P(I wouldn't think about it too hard.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6B7")

    label("loc_3AA")


    ChrTalk(
        0x8,
        (
            "#3509FWell, I might have gotten a lil' impatient,\x01",
            "but I sure was useful, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2809FHahaha, you truly are unique!\x02\x03",
            "#2803FI'd be horrified to let your talent slip\x01",
            "away from me.\x02\x03",
            "#2801FAllow me to be frank. How would\x01",
            "you like to come work for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    ChrTalk(
        0x8,
        (
            "#3505FHmm...? Ohhh, you want me\x01",
            "to work under the IBC CEO...?\x02\x03",
            "#3502FWhat's my hourly wage?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0x9)

    ChrTalk(
        0x9,
        "#2809FHahaha...! You're a genuine comedian, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3509FAhahahahaha! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F#3P(Wh-What the hell is this guy's deal...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0111F#3P(I can't believe he already worked himself\x01",
            "into Uncle Dieter's good graces...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012F#3P(I-I'm kinda at a loss for words.\x01",
            "How am I supposed to react to this?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F#3P(This man... Just who is he?)\x02",
    )

    CloseMessageWindow()

    label("loc_6B7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x1F4)
    SetScenarioFlags(0xD3, 7)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
