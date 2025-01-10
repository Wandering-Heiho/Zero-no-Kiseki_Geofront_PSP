from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t152b.bin",                # FileName
        "t152b",                    # MapName
        "t152b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t152b",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Nurse Meifa",            # 3
        "Nurse Cirone",           # 4
        "Cecile",                 # 5
        "bt152b",                 # 6
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 2, 13, 180)
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
        "BattleInfo_E4", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch29800.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(204550,  0,       53200,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(204550,  0,       52250,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  100.0,                 9.0,                   -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -12.5,                 -3.0,                  0.20000001788139343,   1.0])

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_2EC",          # 00, 0
        "Function_1_3A4",          # 01, 1
        "Function_2_3CE",          # 02, 2
        "Function_3_412",          # 03, 3
        "Function_4_443",          # 04, 4
        "Function_5_605",          # 05, 5
        "Function_6_79F",          # 06, 6
        "Function_7_34F5",         # 07, 7
        "Function_8_353B",         # 08, 8
        "Function_9_3558",         # 09, 9
        "Function_10_3573",        # 0A, 10
        "Function_11_3592",        # 0B, 11
        "Function_12_3861",        # 0C, 12
        "Function_13_38DC",        # 0D, 13
        "Function_14_3E25",        # 0E, 14
    ))


    def Function_0_2EC(): pass

    label("Function_0_2EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_32C"),
        (1, "loc_338"),
        (2, "loc_344"),
        (3, "loc_350"),
        (4, "loc_35C"),
        (5, "loc_368"),
        (6, "loc_374"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_32C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_338")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_344")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_350")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_35C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_368")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_374")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_380")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_38C")

    label("loc_3A3")

    Return()

    # Function_0_2EC end

    def Function_1_3A4(): pass

    label("Function_1_3A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BE")
    Event(0, 13)

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3CD")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_3CD")

    Return()

    # Function_1_3A4 end

    def Function_2_3CE(): pass

    label("Function_2_3CE")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_411")
    Call(0, 12)

    label("loc_411")

    Return()

    # Function_2_3CE end

    def Function_3_412(): pass

    label("Function_3_412")

    TalkBegin(0xFE)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The mafioso is unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_412 end

    def Function_4_443(): pass

    label("Function_4_443")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(
        0xFE,
        (
            "We decided to chat in our dorm after\x01",
            "finishing our chores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, all of a sudden, a bunch of men and dogs\x01",
            "busted down the door. I don't think I've ever\x01",
            "been that frightened in my entire life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But now that you all are here, we can finally\x01",
            "relax, if just a little. Everyone, you have my\x01",
            "sincerest thanks!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_601")

    label("loc_596")

    TurnDirection(0xFE, 0xB, 0)

    ChrTalk(
        0xFE,
        (
            "Those men in black and their dogs are\x01",
            "still on the prowl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Cirone, stay by my side.\x02",
    )

    CloseMessageWindow()

    label("loc_601")

    TalkEnd(0xFE)
    Return()

    # Function_4_443 end

    def Function_5_605(): pass

    label("Function_5_605")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2")

    ChrTalk(
        0xFE,
        (
            "Cecile and the other nurses are still working\x01",
            "the night shift inside the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "P-Please, you have to save them. In the\x01",
            "meantime, I'll keep hiding out here with\x01",
            "Meifa, where it's safe...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_79B")

    label("loc_6E2")


    ChrTalk(
        0xFE,
        (
            "Phew... I feel so exhausted, now\x01",
            "that I know we're going to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wh-Why are my legs shaking so badly?\x01",
            "I should probably sit down, but I can't\x01",
            "find the strength to move...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79B")

    TalkEnd(0xFE)
    Return()

    # Function_5_605 end

    def Function_6_79F(): pass

    label("Function_6_79F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("apl/ch50411.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05500.itp")
    OP_68(151770, 800, 52760, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetChrPos(0x101, 148870, 0, 55580, 45)
    SetChrPos(0x102, 149220, 0, 54230, 0)
    SetChrPos(0x104, 151350, 0, 55460, 315)
    SetChrPos(0x103, 150150, 100, 57600, 270)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1F)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 150080, 0, 55940, 0)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    FadeToBright(1000, 0)
    OP_68(150040, 800, 56760, 4000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#4201001V#1309F#11PIt was just her anemia acting\x01",
            "up, thank goodness.\x02\x03",
            "#4201002V#1300FAfter a bit of rest, she should wake up\x01",
            "and be good as new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201003V#0006F#6PThat's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201004V#0102F#12PWhat a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201005V#0306F#11PYou said it. For a second there,\x01",
            "I was gettin' pretty worried.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    ChrTalk(
        0xC,
        (
            "#4201006V#1306F#11PStill, you have to forgive me for\x01",
            "making her use my bed, everyone...\x02\x03",
            "#4201007V#1301FUnfortunately, every room we have\x01",
            "in the hospital is occupied right now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB6():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB6)
    Sleep(50)

    def lambda_AC6():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC6)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4201008V#0002F#6PThat's all right.\x02\x03",
            "#4201009VI'm sure your room will be more than\x01",
            "enough to help Tio recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201010V#0104F#12PCecile, thank you so very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    ChrTalk(
        0xC,
        (
            "#4201011V#1309F#5PDon't mention it, Elie.\x02\x03",
            "#4201012V#1300FI have to work the night shift tonight,\x01",
            "so it's perfectly fine if she wants to\x01",
            "rest here until tomorrow morning.\x02\x03",
            "#4201013VWell, I'll be going, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201014V#0002F#6PAll right. Thanks for this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201015V#0302F#11P'Preciate the help!\x02",
    )

    CloseMessageWindow()
    OP_68(150040, 800, 55260, 3000)

    def lambda_CCE():

        label("loc_CCE")

        TurnDirection(0x101, 0xC, 500)
        Yield()
        Jump("loc_CCE")

    QueueWorkItem2(0x101, 1, lambda_CCE)

    def lambda_CE0():

        label("loc_CE0")

        TurnDirection(0x102, 0xC, 500)
        Yield()
        Jump("loc_CE0")

    QueueWorkItem2(0x102, 1, lambda_CE0)

    def lambda_CF2():

        label("loc_CF2")

        TurnDirection(0x104, 0xC, 500)
        Yield()
        Jump("loc_CF2")

    QueueWorkItem2(0x104, 1, lambda_CF2)
    BeginChrThread(0xC, 3, 0, 7)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_6F(0x79)
    Sleep(1000)

    def lambda_D29():
        OP_92(0xFE, 0x24A40, 0xD890, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D29)
    WaitChrThread(0x102, 1)
    OP_68(150000, 800, 57600, 3500)
    MoveCamera(33, 21, 0, 3500)

    def lambda_D5C():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D5C)

    def lambda_D69():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D69)

    def lambda_D76():
        OP_95(0xFE, 150080, 0, 55440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D76)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0x103, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#4201016V#0008F#6PTio... If only we noticed sooner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201017V#0106F#12PNow that I think about it, she first started\x01",
            "to look a little sick during our conversation\x01",
            "with Doctor Guenter, right?\x02\x03",
            "#4201018V#0108FI'm almost positive it was...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201019V#0306F#11PWas it when he started tellin' us about that\x01",
            "drug those devil-worshipers made...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    ChrTalk(
        0x103,
        (
            "#4201020V#5P#40W#2SI'm fine, you know. If you have any\x01",
            "questions, you can ask me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    BeginChrThread(0x103, 0, 0, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#4201021V#0002F#6PTio, you're awake?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201022V#0102F#12PI'm so glad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201023V#0304F#12PYou had us worried, y'know?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    Fade(250)
    Sound(1276, 255, 90, 0)
    Sound(804, 0, 100, 0)
    OP_A1(0x103, 0x3E8, 0x6, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23)
    OP_0D()
    Sleep(300)
    OP_A1(0x103, 0x3E8, 0x5, 0x24, 0x25, 0x1A, 0x1B, 0x1C)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)

    AnonymousTalk(
        0x103,
        (
            "#4201025V#40WPlease...there was no need to be.\x02\x03",
            "#4201026VAs someone involved in the ongoing\x01",
            "drug investigation, I'm sure you have\x01",
            "to ask.\x02\x03",
            "#4201027VAbout everything I know, I mean.\x02",
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
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4201028V#0006F#6PListen, Tio.\x02\x03",
            "#4201029V#0000FDo you really think we would push you\x01",
            "to share something you're clearly\x01",
            "uncomfortable talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201030V#5505F#5P#40WHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4201031V#0100F#12PWhile the investigation is definitely important,\x01",
            "these are two separate matters.\x02\x03",
            "#4201032V#0104FYou're more to us than just a colleague.\x02\x03",
            "#4201033V#0102FAbove all, you're an irreplaceable friend, Tio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201034V#5508F#5P#40WOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201035V#0300F#12PI'm sure you got your reasons for\x01",
            "hidin' whatever you know.\x02\x03",
            "#4201036V#0306FI mean, my past got put out in the\x01",
            "open a lil' bit, but...\x02\x03",
            "#4201037V#0303FTio Tot, if you REALLY don't wanna\x01",
            "tell us about it, then that's fine.\x02\x03",
            "#4201038V#0302FWe'll still be backin' you up with\x01",
            "everything we've got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201039V#5506F#5P#40WElie...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201040V#0000F#6PThat's how we all feel.\x02\x03",
            "#4201041V#0003FBut, if you ever want to tell us about the\x01",
            "things you've kept hidden...\x02\x03",
            "#4201042V...and if doing so makes the burden easier\x01",
            "to bear...\x02\x03",
            "#4201043V#0002FI hope that we can help shoulder it\x01",
            "for you, if even just for a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4201044V#5508F#5P#40WLloyd...\x02\x03",
            "#4201045V#5510F#40W...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#4201046V#5504F#5P#30WHow can you say things like that\x01",
            "with a straight face?\x02\x03",
            "#4201047VNot just you, Lloyd, but Elie and\x01",
            "Randy, too...\x02\x03",
            "#4201048V#5511FYou must be rubbing off on the\x01",
            "rest of the team, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201049V#0309F#12PHaha, s'pose he might.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201050V#0104F#12PHmm, that might be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201051V#0006F#6PYeah, yeah, laugh it up.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x103,
        "#4201052V#5509F#5P#40WHeehee...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    Sound(820, 0, 100, 0)
    SetChrPos(0x103, 150000, 200, 56750, 270)
    OP_A1(0x103, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_0D()
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#4201053V#5506F#5PI already told Lloyd a fragment of this story,\x01",
            "but let me explain.\x02\x03",
            "#4201054VI was snatched away from my parents when\x01",
            "I was five years old...\x02\x03",
            "#4201055V#5508F...held captive by a cult of religious fanatics.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetCameraDistance(21000, 100000)

    ChrTalk(
        0x101,
        "#4201056V#0013F#6P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201057V#0101F#12PThey couldn't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201058V#0310F#12PDamn it...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x2, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4201059V#5508F#5PWhat the objective of the cult was is still\x01",
            "unknown, but one thing is clear.\x02\x03",
            "#4201060VThey were attempting to obtain something by\x01",
            "rejecting the Goddess and worshiping devils.\x02\x03",
            "#4201061V#5506FI think that they saw me and the other captive\x01",
            "children as offerings. Nothing more, nothing less.\x01",
            "Simply a means to obtain whatever they wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201062V#0001F#6POfferings...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4201063V#5502F#5PYes. I call them offerings, because 'sacrifices'\x01",
            "wouldn't exactly be right...\x02\x03",
            "#4201064V#5506F...but I suppose you could call some of the\x01",
            "other kids' experiences something akin to\x01",
            "that.\x02\x03",
            "#4201065VThe cult had several lodges and each was\x01",
            "experimenting with different ceremonies.\x02\x03",
            "#4201066V#5508FAnd as for the ceremony they conducted\x01",
            "at the lodge I was taken to...\x02\x03",
            "#4201067V...it was primarily human experimentation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201068V#0107F#12PHuman experimentation?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201069V#0301F#12PThat where your knack for sensin' stuff\x01",
            "came from?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4201070V#5503F#5P#30WPrecisely.\x02\x03",
            "#4201071VSensors were attached to our entire bodies,\x01",
            "and we were pumped full of drugs...\x02\x03",
            "#4201072VThey attempted to enhance our five senses,\x01",
            "using any method imaginable.\x02\x03",
            "#4201073V#5508FThey even tried enhancing our sensitivity\x01",
            "to supernatural phenomena by applying\x01",
            "psychological stress and hypnosis.\x02\x03",
            "#4201074VFor three long years...that was my life, day\x01",
            "in, day out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201075V#0013F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201076V#0108F#12PTh-That can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201106V#0303F#12P...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x2, 0x2A, 0x2B)

    ChrTalk(
        0x103,
        (
            "#4201078V#5502F#5P#30WDespite all that...I might have been the\x01",
            "luckiest person at my lodge.\x02\x03",
            "#4201079VNone of the children could withstand\x01",
            "the ceremonies, except for me.\x02\x03",
            "#4201080V#5508FOne by one, they began to disappear...\x02\x03",
            "#4201081VAnd it was only when I was the last\x01",
            "child left that I gained this power...\x02\x03",
            "#4201082V#5506FMy sensory receptivity became strong enough\x01",
            "to hear the final cries of the others on the\x01",
            "opposite side of that massive rock wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201083V#0010F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201084V#0106F#12PTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201085V#0308F#12PThose monsters...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201134V#5508F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x7, 0x2B, 0x2A, 0x4, 0x3, 0x2, 0x1, 0x0)

    ChrTalk(
        0x103,
        (
            "#4201087V#5502F#5PThen, something happened.\x02\x03",
            "#4201088VLloyd's brother, Guy, was able\x01",
            "to break into the lodge.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4201089V#0011F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4201090V#5503F#5PThe team accompanying Guy was\x01",
            "able to neutralize the cult followers\x01",
            "and dismantle the lodge's operation.\x02\x03",
            "#4201091VThe resistance was strong, but the\x01",
            "moment the lodge fell, most of the\x01",
            "cultists committed suicide.\x02\x03",
            "#4201092V#5508FWhile stepping over so many of their\x01",
            "corpses, Guy finally reached what was\x01",
            "known as the ceremonial chamber...\x02\x03",
            "#4201093V...and that was when he found the only\x01",
            "child left alive in that nightmare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201094V#0008F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4201095V#5506F#5PBy the time Guy took me into his custody,\x01",
            "I was debilitated beyond recognition.\x02\x03",
            "#4201096VBecause of that, I was hospitalized for\x01",
            "several months in order to recover.\x02\x03",
            "#4201097V#5508FWhat happened after that, I've already\x01",
            "told Lloyd about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201098V#0003F#6P...I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4201099V#0106F#12PTio...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4201100V#5504F#5PIt's almost ironic.\x02\x03",
            "#4201101VDespite being so grateful to Guy\x01",
            "for saving me from that place...\x02\x03",
            "#4201102V#5502F...when I heard that he passed\x01",
            "away three years ago, I wasn't\x01",
            "even that sad.\x02\x03",
            "#4201103V#5508FIt's as if, in exchange for this power,\x01",
            "I had my emotions stripped away.\x02\x03",
            "#4201104VAt least, that's what I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4201105V#0008F#6PTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4201077V#0308F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4201107V#5504F#5PI wanted to ask him something.\x02\x03",
            "#4201108VI wanted to ask Guy, a strong,\x01",
            "impossibly optimistic person...\x02\x03",
            "#4201109V...how exactly should a broken\x01",
            "person like me live?\x02\x03",
            "#4201110V#5508FBut, in the end, I wasn't able to\x01",
            "ask him, and I was recruited by\x01",
            "the Epstein Foundation.\x02\x03",
            "#4201111VAfter that, I joined the Special\x01",
            "Support Section and began to\x01",
            "live with all of you...\x02\x03",
            "#4201112V#5506F#40WI...I still don't know the answer.\x02\x03",
            "#4201113V#40WHow do I go about living?\x02\x03",
            "#4201114V#40WJust...why? Why am I alive?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x102,
        "#4201115V#0101F#12PTio!\x02",
    )

    CloseMessageWindow()
    OP_68(150220, 800, 57570, 1200)
    BeginChrThread(0x102, 3, 0, 10)
    WaitChrThread(0x102, 3)
    StopBGM(0xFA0)
    Sleep(500)
    OP_A1(0x103, 0x3E8, 0x3, 0x5, 0x6, 0x7)
    Sleep(300)
    Fade(1000)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrSubChip(0x103, 0x8)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1269, 255, 65, 0)

    ChrTalk(
        0x103,
        "#4201116V#5P#30WAh...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x8, 0x9, 0xA, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    NpcTalk(
        0x103,
        "Elie",
        (
            "#4201117V#0103F#11PYou don't have to worry about that!\x01",
            "It's okay to not know the answers!\x02\x03",
            "#4201118V#0107FWe're all the same...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201119V#5505F#5P#30WWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201120V#0003F#6PWhy do we live? How should we live?\x02\x03",
            "#4201121VThere aren't many people who know\x01",
            "the answers to those questions, Tio.\x02\x03",
            "#4201122V#0000FMe, Elie, Randy... We're all lost, the\x01",
            "same as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201123V#0304F#12PI had definitely lost my way,\x01",
            "that's for sure.\x02\x03",
            "#4201124V#0302FStill, Tio Tot. You're bein' way too\x01",
            "serious 'bout all this.\x02\x03",
            "#4201125VWhat's the point in rushin' to\x01",
            "answer questions like those?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0xA, 0xB, 0xC)

    ChrTalk(
        0x103,
        "#4201126V#5506F#5P#30WB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4201127V#0004F#6PIf you still can't help but wonder what the\x01",
            "answers are...keep searching for them.\x02\x03",
            "#4201128VJust remember, there's no need to rush,\x01",
            "and you don't have to do it alone.\x02\x03",
            "#4201129V#0000FLet's find these answers together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201130V#5508F#5P#40W...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Elie",
        (
            "#4201131V#0104F#11PI'll always be here for you, too.\x02\x03",
            "#4201132VSo will Randy, the chief, KeA, even Zeit...\x01",
            "We're all here for you.\x02\x03",
            "#4201133VWe'll help you find the answers to these\x01",
            "questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4201086V#5510F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_A1(0x103, 0x3E8, 0x4, 0xF, 0x10, 0x11, 0x12)

    ChrTalk(
        0x103,
        (
            "#4201135V#5508F#5P#40WYes, I think Lloyd has definitely\x01",
            "rubbed off on you, Elie and Randy.\x02\x03",
            "#4201136V#5513FHearing you all say this stuff...\x01",
            "It's too embarrassing...\x02\x03",
            "#4201137VWhy would you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4201138V#0309F#12PIt's fate, ain't it?\x02\x03",
            "#4201139VWhen we joined the SSS, we all\x01",
            "fell prey to this guy's cheesiness.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "Elie",
        (
            "#4201140V#0109F#11PRandy's right.\x02\x03",
            "#4201141V#0102FWe're a team. We share what we\x01",
            "feel, be it embarrassing or not.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#4201142V#0012F#6PI don't get why I'm the one being blamed\x01",
            "for that, but...\x02\x03",
            "#4201143V#0000FI definitely agree with Elie's last point.\x02\x03",
            "#4201144V#0004FWe share everything. Embarrassment,\x01",
            "our past pains...\x02\x03",
            "#4201145V...and, of course, our happiness and\x01",
            "daily jokes, too.\x02\x03",
            "#4201146V#0002FThat's what it means to be a team, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x12, 0x13, 0x14)
    Sound(1277, 255, 100, 0)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#4201147V#5512F#5P#40WPlease stop...\x02\x03",
            "#4201148VIt's TOO embarrassing...and it's burning\x01",
            "up in here. I'm not sure how much more\x01",
            "of this I can take...\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x17, 0x18, 0x19, 0x18)
    Sleep(150)

    ChrTalk(
        0x103,
        (
            "#4201149V#5513F#5P#40WBut...for some reason, I don't think this\x01",
            "is such a bad feeling.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 0, 0, 9)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(22000, 3000)
    OP_6F(0x10)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After their heartfelt talk, the SSS took the bus\x01",
            "back to Crossbell City.\x02\x03",
            "When they returned to the SSS building and put\x01",
            "an exhausted Tio in bed...\x02\x03",
            "Lloyd, Elie, and Randy decided to have one\x01",
            "more talk with Chief Sergei.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    EndChrThread(0x103, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_79F end

    def Function_7_34F5(): pass

    label("Function_7_34F5")


    def lambda_34FA():
        OP_95(0xFE, 150120, 0, 49160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34FA)
    Sleep(2700)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_3520():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3520)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(104, 0, 100, 0)
    Return()

    # Function_7_34F5 end

    def Function_8_353B(): pass

    label("Function_8_353B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3557")
    OP_A1(0xFE, 0x3E8, 0x3, 0x1F, 0x1E, 0x1D)
    Sleep(4000)
    Jump("Function_8_353B")

    label("loc_3557")

    Return()

    # Function_8_353B end

    def Function_9_3558(): pass

    label("Function_9_3558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3572")
    OP_A1(0xFE, 0x3E8, 0x4, 0x15, 0x16, 0x17, 0x16)
    Jump("Function_9_3558")

    label("loc_3572")

    Return()

    # Function_9_3558 end

    def Function_10_3573(): pass

    label("Function_10_3573")


    def lambda_3578():
        OP_96(0xFE, 0x24BBC, 0x0, 0xDB92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3578)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_3573 end

    def Function_11_3592(): pass

    label("Function_11_3592")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(99060, 1000, 12500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 97690, 0, 11720, 270)
    SetChrPos(0x102, 98330, 0, 10890, 270)
    SetChrPos(0x103, 99270, 0, 12710, 270)
    SetChrPos(0x104, 100540, 0, 12610, 270)
    SetChrPos(0x106, 99810, 0, 10770, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 85000, 0, 12690, 90)
    SetChrPos(0x9, 85000, 0, 11100, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(92640, 1000, 12400, 0)
    OP_68(97340, 1000, 12400, 1750)
    SetCameraDistance(17500, 1750)

    def lambda_3774():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3774)

    def lambda_3789():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3789)
    Sleep(750)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 12)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x0, 98700, 0, 11800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_3592 end

    def Function_12_3861(): pass

    label("Function_12_3861")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 93740, 0, 13280, 270)
    SetChrPos(0x9, 94870, 0, 10340, 90)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_12_3861 end

    def Function_13_38DC(): pass

    label("Function_13_38DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(200880, 900, 52400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 199450, 0, 49200, 0)
    SetChrPos(0x102, 200570, 0, 49200, 0)
    SetChrPos(0x103, 199450, 0, 47900, 0)
    SetChrPos(0x104, 200570, 0, 47900, 0)
    SetChrPos(0x106, 200000, 0, 46600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(201940, 900, 53610, 3000)

    def lambda_39D3():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39D3)

    def lambda_39E8():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39E8)

    def lambda_39FD():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_39FD)

    def lambda_3A12():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A12)

    def lambda_3A27():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3A27)
    Sleep(200)

    def lambda_3A3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A3F)

    def lambda_3A50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3A50)
    Sleep(500)

    def lambda_3A64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3A64)

    def lambda_3A75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A75)
    Sleep(500)

    def lambda_3A89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3A89)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_3AA2():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AA2)

    def lambda_3AAF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AAF)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_3AC4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AC4)

    def lambda_3AD1():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AD1)
    WaitChrThread(0x106, 1)

    def lambda_3AE2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3AE2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3B5F():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B5F)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3B81():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3B81)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    ChrTalk(
        0xA,
        "#5100508V#5PEeeek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100509V#11PN-No, stay away...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5100510V#0100F#6PYou can relax. We're with the CPD.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#5100511V#11PA-A girl...? What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100512V#5PYou said CPD? Are you here to save us?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5100513V#0103F#6PThat's right. As of now, we've been checking\x01",
            "on everyone while incapacitating any intruders\x01",
            "we stumble across.\x02\x03",
            "#5100514V#0101FI'm sorry, but we're going to have to ask you to\x01",
            "wait here for just a little while longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5100515V#5PThat's okay. We understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5100516V#11PJ-Just be safe, everyone!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 200200, 0, 52410, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE1, 2)
    OP_29(0x4D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_38DC end

    def Function_14_3E25(): pass

    label("Function_14_3E25")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A framed photograph of Cecile, Lloyd, and a muscular man with\x01",
            "a determined look on his face sits on the shelf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F6B")

    AnonymousTalk(
        0x101,
        (
            "#0008F(So she still has this photo, too...)\x02\x03",
            "(I always keep it on me, but Cecile\x01",
            "went and framed it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FE3")

    label("loc_3F6B")


    AnonymousTalk(
        0x101,
        (
            "#0005F(A photo of me, Cecile, and Guy?)\x02\x03",
            "#0003F(If that's here, that must mean that\x01",
            "this is Cecile's room, right?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE3")

    SetScenarioFlags(0x69, 5)

    label("loc_3FE6")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_3E25 end

    SaveToFile()

Try(main)
