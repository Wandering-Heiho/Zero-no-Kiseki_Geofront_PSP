from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0010.bin",                # FileName
        "e0010",                    # MapName
        "e0010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0010",                  # 0
        "Driver",                 # 1
        "Passenger",              # 2
        "Passenger",              # 3
        "Passenger",              # 4
        "Black-Haired Woman",     # 5
        "Old Lady",               # 6
        "Old Man",                # 7
        "Merchant",               # 8
        "Woman",                  # 9
        "Older Brother",          # 10
        "Younger Sister",         # 11
        "Father",                 # 12
        "Boy",                    # 13
        "SE制御",                 # 14
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_268",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_C35",          # 03, 3
        "Function_4_C5A",          # 04, 4
        "Function_5_1292",         # 05, 5
        "Function_6_164B",         # 06, 6
        "Function_7_1684",         # 07, 7
        "Function_8_16BD",         # 08, 8
        "Function_9_16F9",         # 09, 9
        "Function_10_1735",        # 0A, 10
        "Function_11_177D",        # 0B, 11
        "Function_12_17E8",        # 0C, 12
        "Function_13_1849",        # 0D, 13
        "Function_14_188D",        # 0E, 14
        "Function_15_1975",        # 0F, 15
        "Function_16_3A0B",        # 10, 16
        "Function_17_3A4F",        # 11, 17
        "Function_18_3A93",        # 12, 18
    ))


    def Function_0_268(): pass

    label("Function_0_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_27C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_2B3")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 4)
    Jump("loc_2B3")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_2A4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 5)
    Jump("loc_2B3")

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_2B3")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 15)

    label("loc_2B3")

    Return()

    # Function_0_268 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Return()

    # Function_1_2B4 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch20402.itc", 0x23)
    LoadChrToIndex("chr/ch20302.itc", 0x24)
    LoadChrToIndex("chr/ch22302.itc", 0x25)
    SoundLoad(468)
    OP_68(46910, 1100, -180, 0)
    MoveCamera(328, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16350, 0)
    OP_68(52300, 1100, -180, 10000)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x101, 52250, 0, 800, 0)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0x9, 46150, 150, -1840, 270)
    SetChrPos(0xA, 48050, 150, 1880, 270)
    SetChrPos(0xB, 48050, 150, 880, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#1101647V#0000F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1101648V#0100F#6PWhat a beautiful sunset...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101649V#0203F#4PIt is... However, I would not\x01",
            "advise looking right at it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#1101650V#0304F#11PPhew... Orbal vehicles make\x01",
            "life a breeze, don't they?\x02\x03",
            "#1101651V#0300FMan. Imagine if we got our\x01",
            "hands on our own car.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1101652V#0006F#6PYeah, I wouldn't count on that.\x02\x03",
            "#1101653V#0000FI think the other investigative\x01",
            "divisions use them, though.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    ChrTalk(
        0x103,
        (
            "#1101654V#0200F#4PIf I recall correctly, I believe that\x01",
            "each First Division detective has a\x01",
            "private car prepared for them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101655V#0005F#5PS-Seriously?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101656V#0106F#6PYou would think there's a\x01",
            "limit to special treatment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1101657V#0306F#5PGeez, it's times like this when it\x01",
            "really sucks to be the misfits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101658V#0006F#5PWell, it's no use begging\x01",
            "for stuff we can't get.\x02\x03",
            "#1101659V#0000FBesides, traveling on the highway is\x01",
            "pretty good training, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1101660V#0203F#4PI am hesitant to agree, but I think\x01",
            "I have to.\x02\x03",
            "#1101661V#0211FBut we won't be investigating\x01",
            "any further today, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1101662V#0003F#5PYeah, all that's left is Mainz.\x02\x03",
            "#1101663V#0000FLike I said, let's head back for\x01",
            "now and write up our reports.\x01",
            "Tomorrow, we'll pick up where we left off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#1101664V#0206F#4P*sigh* Roger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1101665V#0109F#6PI think today was more exhausting\x01",
            "than we were expecting.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    OP_63(0x104, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#1101666V#0309F#11PYou got that right... But, man,\x01",
            "Cecile really saved our skins, eh?\x02\x03",
            "#1101667V#0307FAll right! Next time, I'll use a mixer\x01",
            "as an excuse to score big time!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#1101668V#0006F#6PYour persistence is admirable, Randy...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x15, 0, 0, 16)
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
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2B5 end

    def Function_3_C35(): pass

    label("Function_3_C35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C59")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_C35")

    label("loc_C59")

    Return()

    # Function_3_C35 end

    def Function_4_C5A(): pass

    label("Function_4_C5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch21102.itc", 0x22)
    LoadChrToIndex("chr/ch21602.itc", 0x23)
    LoadChrToIndex("apl/ch50382.itc", 0x24)
    SoundLoad(468)
    OP_68(147980, 1000, 1450, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16170, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_CE4")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_D0B")

    label("loc_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CFA")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_D0B")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D0B")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_D0B")

    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x2)
    SetChrFlags(0x153, 0x10)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0x24)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x101, 148050, 150, 1800, 180)
    SetChrPos(0x153, 147350, 350, 1800, 0)
    SetChrPos(0xEF, 146600, 150, 1800, 180)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 145000, 150, 790, 90)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 145000, 150, -100, 90)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_68(146980, 1000, 1450, 3000)
    OP_0D()
    OP_6F(0x1)
    Sound(2033, 255, 100, 0)
    Sleep(1800)
    SetChrSubChip(0x153, 0x1)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#3600675V#1109F#5PWhoa, look there, Lloyd!\x01",
            "It's sooo pretty!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)
    Sleep(200)

    ChrTalk(
        0x101,
        "#3600676V#0011F#11PShh, that's too loud, KeA!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x2)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_EC4")

    ChrTalk(
        0x102,
        "#3600677V#0106F#11PS-Sorry about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F3D")

    label("loc_EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F03")

    ChrTalk(
        0x103,
        "#3600678V#0206F#11POur apologies, everyone.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F3D")

    label("loc_F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F3D")

    ChrTalk(
        0x104,
        "#3600679V#0306F#11PSorry 'bout that, folks.\x02",
    )

    CloseMessageWindow()

    label("loc_F3D")


    ChrTalk(
        0x9,
        (
            "#3600680V#5PHaha, don't worry about it.\x01",
            "A lively kid is a healthy kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3600681V#1PHoho, are you going\x01",
            "to visit someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3600682V#0000F#11PNo, we just need to consult some\x01",
            "of the hospital's doctors.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x153, 0x0)

    ChrTalk(
        0x153,
        (
            "#3600683V#1107F#5PWow! I can see a cute\x01",
            "little island over there!\x02\x03",
            "#3600684V#1109FHehe, it's funny-looking!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)

    ChrTalk(
        0x101,
        "#3600685V#0012F#12PWhat are we going to do with you...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1169")

    ChrTalk(
        0x102,
        (
            "#3600686V#0102F#6PShe's popular wherever she\x01",
            "goes, isn't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1211")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_11B7")

    ChrTalk(
        0x103,
        (
            "#3600687V#0202F#6POnce again, KeA charms\x01",
            "anyone she meets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1211")

    label("loc_11B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1211")

    ChrTalk(
        0x104,
        (
            "#3600688V#0309F#6PHaha, our little lady is always\x01",
            "a hit with the crowd, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1211")

    SetCameraDistance(15670, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    ClearChrFlags(0x153, 0x2)
    ClearChrFlags(0x153, 0x10)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    BeginChrThread(0x15, 0, 0, 16)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_C5A end

    def Function_5_1292(): pass

    label("Function_5_1292")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2600, -500, -450, 270)
    SetChrPos(0x102, 2600, -500, 450, 270)
    SetChrPos(0x103, 3700, -500, 450, 270)
    SetChrPos(0x104, 3700, -500, -450, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(900, 900, 0, 0)
    MoveCamera(270, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bg00_y", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(400, 900, 0, 2500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 900, 0, 0)
    OP_68(0, 900, -2500, 4000)
    MoveCamera(320, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    Sleep(1500)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_68(0, 500, 500, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 600, 0, -4800, 0)
    SetChrPos(0x102, 800, 0, 2300, 0)
    SetChrPos(0x103, 0, 0, 3700, 0)
    SetChrPos(0x104, -800, 0, 2600, 0)
    OP_68(0, 500, 4500, 6000)

    def lambda_14C6():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14C6)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5100334V#0008F#6PThey left their gifts and flowers behind...\x02\x03",
            "#5100335V#0013FThese must have been for the people\x01",
            "they were visiting at the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100336V#0106F#6PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100337V#0208F#6PA Mishy plush... Could this be a\x01",
            "'get well soon' present for a sick\x01",
            "child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5100338V#0306F#6PYeah, probably.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(17200, 2500)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1292 end

    def Function_6_164B(): pass

    label("Function_6_164B")


    def lambda_1650():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1650)

    def lambda_1665():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1665)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_6_164B end

    def Function_7_1684(): pass

    label("Function_7_1684")


    def lambda_1689():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1689)

    def lambda_169E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_169E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_7_1684 end

    def Function_8_16BD(): pass

    label("Function_8_16BD")


    def lambda_16C2():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16C2)
    Sleep(500)

    def lambda_16DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16DA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_8_16BD end

    def Function_9_16F9(): pass

    label("Function_9_16F9")


    def lambda_16FE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FE)
    Sleep(500)

    def lambda_1716():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1716)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_9_16F9 end

    def Function_10_1735(): pass

    label("Function_10_1735")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1741():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1741)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_1761():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1761)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1735 end

    def Function_11_177D(): pass

    label("Function_11_177D")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_178C():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_178C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_17AC():
        OP_9B(0x0, 0xFE, 0x0, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17AC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_17CC():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17CC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_177D end

    def Function_12_17E8(): pass

    label("Function_12_17E8")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_17F4():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_1814():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1814)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1834():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1834)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_17E8 end

    def Function_13_1849(): pass

    label("Function_13_1849")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1858():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1858)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_1878():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1878)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_1849 end

    def Function_14_188D(): pass

    label("Function_14_188D")

    EventBegin(0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The elderly man]\x01",            # 0
            "[The elderly woman]\x01",          # 1
            "[The dark-haired woman]\x01",      # 2
            "[The young woman]\x01",            # 3
            "[The merchant]\x01",               # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1922"),
        (1, "loc_1930"),
        (2, "loc_193E"),
        (3, "loc_194C"),
        (4, "loc_195A"),
        (SWITCH_DEFAULT, "loc_1968"),
    )


    label("loc_1922")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_1968")

    label("loc_1930")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_1968")

    label("loc_193E")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_1968")

    label("loc_194C")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_1968")

    label("loc_195A")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_1968")

    label("loc_1968")

    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_188D end

    def Function_15_1975(): pass

    label("Function_15_1975")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch07302.itc", 0x23)
    LoadChrToIndex("chr/ch24102.itc", 0x24)
    LoadChrToIndex("chr/ch20802.itc", 0x25)
    LoadChrToIndex("chr/ch33000.itc", 0x26)
    LoadChrToIndex("chr/ch24500.itc", 0x27)
    LoadChrToIndex("chr/ch21202.itc", 0x28)
    LoadChrToIndex("chr/ch21302.itc", 0x29)
    LoadChrToIndex("chr/ch21002.itc", 0x2A)
    LoadChrToIndex("chr/ch21402.itc", 0x2B)
    SoundLoad(474)
    OP_68(47090, 1100, -430, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_68(51930, 1100, 120, 8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x2)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x2B)
    SetChrSubChip(0x14, 0x2)
    SetChrPos(0x101, 52250, 150, 1700, 180)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0xC, 48000, 150, -2000, 270)
    SetChrPos(0xD, 44000, 150, -2000, 270)
    SetChrPos(0xE, 46000, 150, -2000, 270)
    SetChrPos(0xF, 50270, -250, -2029, 225)
    SetChrPos(0x10, 49540, -250, 1520, 270)
    SetChrPos(0x11, 48000, 150, 600, 270)
    SetChrPos(0x12, 48000, 150, 1600, 270)
    SetChrPos(0x13, 46000, 150, 600, 270)
    SetChrPos(0x14, 46000, 150, 1600, 270)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    PlayBGM("ed7516", 0)
    Sound(474, 2, 0, 0)
    BeginChrThread(0x15, 0, 0, 17)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x15, 0x0)

    ChrTalk(
        0x101,
        (
            "#5P#0001F(First off, we should sort through\x01",
            "all the information we have on the\x01",
            "counterfeit ring.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203F(The group of counterfeit dealers split up\x01",
            "and entered Crossbell via the train station,\x01",
            "airport, and Tangram Gate...)\x02\x03",
            "#0200F(At least, according to the report\x01",
            "given by Donovan.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000F(Yes, that's right.)\x02\x03",
            "#0003F(If the report is accurate, our\x01",
            "culprit should be one of the\x01",
            "passengers on this bus.)\x02\x03",
            "(With that information, we can\x01",
            "deduce one, infallible truth...)\x02\x03",
            "#0001F(The counterfeit dealer who\x01",
            "boarded this bus is...)\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Working independently]\x01",       # 0
            "[Working with a partner]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E93"),
        (1, "loc_2527"),
        (SWITCH_DEFAULT, "loc_2D6C"),
    )


    label("loc_1E93")

    OP_60(0x0)
    OP_2C(0x1B, 0x1)

    ChrTalk(
        0x101,
        (
            "#5P#0001F(...working independently.)\x02\x03",
            "#0003F(From that, we can conclude that\x01",
            "this is likely the ring's leader.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0305F(Whoa, seriously...? Would\x01",
            "their leader be workin' solo,\x01",
            "with no backup?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105F(It's possible...but what's\x01",
            "your reasoning behind that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0004F(It's relatively simple to explain.)\x02\x03",
            "(For them to sell their merchandise,\x01",
            "they have to transport their counterfeit\x01",
            "goods into Crossbell, right?)\x02\x03",
            "#0000F(Naturally, it seems odd for them to be\x01",
            "using the bus route to Tangram Gate.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203F(Yes, now that you mention it...)\x02\x03",
            "#0200F(If I were a counterfeit dealer, I would\x01",
            "make my friends enter Crossbell via\x01",
            "train or airship.)\x02\x03",
            "(Unlike the border gates, the station and airport\x01",
            "do not require as strict security screenings for\x01",
            "people from the Republic or the Empire.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303F(On top of that, smugglin' goods is a tricky\x01",
            "business. Handin' off the dirty work to\x01",
            "underlings is the name of the game.)\x02\x03",
            "(Oh, and by process of elimination...\x01",
            "Our culprit already ordered his goons to\x01",
            "smuggle through the station and airport...)\x02\x03",
            "#0301F(With that outta the way, he's free to\x01",
            "nonchalantly enter Crossbell. Is that\x01",
            "kinda what you're gettin' at, Lloyd?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000F(Couldn't have summed it up better.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103F(It's circumstantial evidence, but\x01",
            "it still holds some weight.)\x02\x03",
            "#0101F(When we apply that logic to this case,\x01",
            "people traveling in pairs can be ruled out.\x01",
            "So, the siblings and father and son are clear.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001F(Exactly, but there's something else...)\x02\x03",
            "#0003F(When I was questioning the passengers,\x01",
            "one of them said something fishy.)\x02\x03",
            "(That person is most likely the leader\x01",
            "of the counterfeit ring.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6C")

    label("loc_2527")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#5P#0003F(...working with a partner.)\x02\x03",
            "#0001F(They're probably acting as couriers\x01",
            "in the counterfeit ring.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0305F(Two of 'em?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001F(For them to sell their merchandise,\x01",
            "they have to transport their counterfeit\x01",
            "goods into Crossbell, right?)\x02\x03",
            "#0003F(It wouldn't be efficient to carry\x01",
            "the goods in individually.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0305F(So that means it's either the\x01",
            "siblings or the father-son duo?)\x02\x03",
            "#0306F(Uh, well, those guys\x01",
            "weren't my first guess.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200F(Are you certain about this, Lloyd?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005F(What do you mean?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203F(If I were a counterfeit dealer, I would\x01",
            "make my friends enter Crossbell via\x01",
            "train or airship.)\x02\x03",
            "#0200F(Unlike the border gates, the station and airport\x01",
            "do not require as strict security screenings for\x01",
            "people from the Republic or the Empire.)\x02\x03",
            "(Therefore, Tangram Gate is not the\x01",
            "ideal connection for a transportation\x01",
            "route.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103F(She has a good point...)\x02\x03",
            "#0101F(If that's the case, the dealer\x01",
            "who boarded this bus is likely\x01",
            "working alone. I'm sure of it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005F(By themselves...?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101F(Yes, that person should\x01",
            "be the leader of the\x01",
            "counterfeit ring.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0305F(You might be on to somethin'...)\x02\x03",
            "#0303F(Besides, smugglin' goods is a tricky\x01",
            "business. Handin' off the dirty work to\x01",
            "underlings is the name of the game.)\x02\x03",
            "(Oh, and by process of elimination...\x01",
            "Our culprit already ordered his goons to\x01",
            "smuggle through the station and airport...)\x02\x03",
            "#0301F(With that outta the way, he's free to\x01",
            "nonchalantly enter Crossbell. Is that\x01",
            "kinda what you're gettin' at?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005F(That all lines up...)\x02\x03",
            "#0006F(Thanks, guys. Looks like\x01",
            "I'm having an off day.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100F(It's fine, Lloyd. Besides, if we leave\x01",
            "every investigation to you, we'll never\x01",
            "improve ourselves.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200F(We are stealing the show.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0309F(Haha, right on.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001F(Well, going by your conclusion,\x01",
            "there's only one person who\x01",
            "stands out among the suspects.)\x02\x03",
            "#0003F(When I was questioning the passengers,\x01",
            "one of them said something fishy.)\x02\x03",
            "#0001F(That person is most likely the leader\x01",
            "of the counterfeit ring.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D6C")

    label("loc_2D6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        "#11P#0301F(Somethin' fishy, eh...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0203F(There are five remaining suspects.)\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(45920, 1100, -1670, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()
    SetMessageWindowPos(350, 0, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#0200F\x09",
            "(The eccentric old man who claims\x01",
            "he came to Crossbell to fish.)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(43880, 1100, -1880, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    AnonymousTalk(
        0x103,
        (
            "#0200F(The kind old lady who claims she came\x01",
            "to Crossbell to see her grandchild for the\x01",
            "first time in three years.)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(48010, 1100, -1960, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(17640, 0)
    OP_0D()

    AnonymousTalk(
        0x103,
        (
            "#0200F(The dark-haired woman shrouded\x01",
            "in mystery.)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(49460, 1100, 1460, 0)
    MoveCamera(335, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    AnonymousTalk(
        0x103,
        (
            "#0200F(The young girl who seemed to\x01",
            "distrust the dark-haired woman.)\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(50240, 1100, -1870, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(19450, 0)
    OP_0D()

    AnonymousTalk(
        0x103,
        (
            "#0200F(And the merchant, who says he\x01",
            "travels back and forth between\x01",
            "Crossbell and the Republic...)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(51930, 1100, 120, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#12P#0105F(Is one of them really the culprit?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F(Yeah, I think I've got them pinned down.)\x02\x03",
            "#0001F(Among the suspects, the leader of\x01",
            "the counterfeit dealers must be...)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3192")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3956")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The elderly man]\x01",            # 0
            "[The elderly woman]\x01",          # 1
            "[The dark-haired woman]\x01",      # 2
            "[The young woman]\x01",            # 3
            "[The merchant]\x01",               # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3234"),
        (1, "loc_3266"),
        (2, "loc_329A"),
        (3, "loc_32D2"),
        (4, "loc_3304"),
        (SWITCH_DEFAULT, "loc_3333"),
    )


    label("loc_3234")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#5P#0001F(...the elderly man.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_3333")

    label("loc_3266")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#5P#0001F(...the elderly woman.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_3333")

    label("loc_329A")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#5P#0001F(...the dark-haired woman.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_3333")

    label("loc_32D2")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#5P#0001F(...the young woman.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_3333")

    label("loc_3304")

    OP_60(0x0)

    ChrTalk(
        0x101,
        "#5P#0001F(...the merchant.)\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_3333")

    label("loc_3333")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        "#11P#0301F(You positive?)\x02",
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Definitely]\x01",          # 0
            "[Let me rethink]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_339C"),
        (1, "loc_36E1"),
        (SWITCH_DEFAULT, "loc_3951"),
    )


    label("loc_339C")

    OP_60(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_33B1")
    OP_2C(0x1B, 0x2)

    label("loc_33B1")


    ChrTalk(
        0x101,
        (
            "#5P#0001F(Yeah. Given the evidence, it wouldn't\x01",
            "make sense for the counterfeit dealer\x01",
            "to be anyone else.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0105F(I guess that's true...)\x02",
    )

    CloseMessageWindow()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Announcer")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bus will be arriving at Crossbell's\x01",
            "east exit momentarily.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When disembarking, please remember\x01",
            "to take all personal belongings with you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#12P#0200F(We will arrive shortly.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101F(It's now or never.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001F(Once we arrive, we'll hurry and\x01",
            "apprehend the suspect.)\x02\x03",
            "(Everyone, get ready.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0304F(Don't have to tell me twice.)\x02\x03",
            "#0300F(Remember, Lloyd, it's up to you\x01",
            "to get the suspect to drop their\x01",
            "cover. You up to the challenge?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0001F(Of course. Leave it to me!)\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_68(47810, 1100, -1860, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18710, 0)
    OP_0D()
    SetCameraDistance(17710, 2000)
    OP_6F(0x10)

    ChrTalk(
        0xC,
        "#11P#3403F...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3951")

    label("loc_36E1")

    OP_60(0x0)

    ChrTalk(
        0x101,
        (
            "#5P#0003F(Well, the more I think about it,\x01",
            "the less confident I get.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#0306F(Dude?! Are you kiddin' me?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0106F(*sigh* Please, pull yourself together.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0011F(S-Sorry... Let me think\x01",
            "this through again.)\x02\x03",
            "#0003F(While I was questioning them,\x01",
            "there was definitely someone\x01",
            "who said something fishy.)\x02\x03",
            "(They said something impossible like it\x01",
            "was the most natural thing in the world...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300F(We're almost back to Crossbell City.\x01",
            "Better make up your mind, quick.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0001F(Among the suspects, the leader of\x01",
            "the counterfeit dealers must be...)\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x2, 0xE)
    OP_29(0x1B, 0x2, 0xF)
    OP_29(0x1B, 0x2, 0x10)
    OP_29(0x1B, 0x2, 0x11)
    OP_29(0x1B, 0x2, 0x12)
    Jump("loc_3951")

    label("loc_3951")

    Jump("loc_3192")

    label("loc_3956")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x15, 0, 0, 18)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
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
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_24(0x1DA)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1975 end

    def Function_16_3A0B(): pass

    label("Function_16_3A0B")

    OP_25(0x1D4, 0x5A)
    Sleep(80)
    OP_25(0x1D4, 0x50)
    Sleep(80)
    OP_25(0x1D4, 0x46)
    Sleep(80)
    OP_25(0x1D4, 0x3C)
    Sleep(80)
    OP_25(0x1D4, 0x32)
    Sleep(80)
    OP_25(0x1D4, 0x28)
    Sleep(80)
    OP_25(0x1D4, 0x1E)
    Sleep(80)
    OP_25(0x1D4, 0x14)
    Sleep(80)
    OP_25(0x1D4, 0xA)
    Sleep(80)
    OP_25(0x1D4, 0x0)
    Return()

    # Function_16_3A0B end

    def Function_17_3A4F(): pass

    label("Function_17_3A4F")

    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x64)
    Return()

    # Function_17_3A4F end

    def Function_18_3A93(): pass

    label("Function_18_3A93")

    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x0)
    Return()

    # Function_18_3A93 end

    SaveToFile()

Try(main)
