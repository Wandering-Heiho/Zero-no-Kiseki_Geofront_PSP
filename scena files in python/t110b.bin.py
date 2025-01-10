from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t110b.bin",                # FileName
        "t110b",                    # MapName
        "t110b",                    # Location
        0x0046,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 2, 0, 3],
    )

    BuildStringList((
        "t110b",                  # 0
        "Man in Suit",            # 1
        "Man in Suit",            # 2
        "Mafioso",                # 3
        "Mafioso",                # 4
        "Mafioso",                # 5
        "Mafioso",                # 6
        "Mafioso",                # 7
        "Invitee",                # 8
        "Invitee",                # 9
        "Chakram",                # 10
        "Chakram",                # 11
        "Chakram",                # 12
        "Chakram",                # 13
        "To Hotel Delphinia",     # 14
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "apl/ch50363.itc",                   # 04
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   2,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 31,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ScpFunction((
        "Function_0_36C",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_446",          # 03, 3
        "Function_4_47A",          # 04, 4
        "Function_5_56D",          # 05, 5
        "Function_6_111B",         # 06, 6
        "Function_7_24DD",         # 07, 7
        "Function_8_250D",         # 08, 8
        "Function_9_253D",         # 09, 9
        "Function_10_256D",        # 0A, 10
        "Function_11_259D",        # 0B, 11
        "Function_12_25F2",        # 0C, 12
        "Function_13_2629",        # 0D, 13
        "Function_14_3DFE",        # 0E, 14
        "Function_15_3E5A",        # 0F, 15
        "Function_16_3EBB",        # 10, 16
        "Function_17_3F1C",        # 11, 17
        "Function_18_3F91",        # 12, 18
        "Function_19_3FFA",        # 13, 19
        "Function_20_406F",        # 14, 20
        "Function_21_40E4",        # 15, 21
        "Function_22_414D",        # 16, 22
        "Function_23_416C",        # 17, 23
        "Function_24_4194",        # 18, 24
        "Function_25_41BC",        # 19, 25
        "Function_26_4202",        # 1A, 26
        "Function_27_429C",        # 1B, 27
        "Function_28_42E2",        # 1C, 28
        "Function_29_4392",        # 1D, 29
        "Function_30_43D8",        # 1E, 30
        "Function_31_4481",        # 1F, 31
    ))


    def Function_0_36C(): pass

    label("Function_0_36C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_36C end

    def Function_1_424(): pass

    label("Function_1_424")

    Return()

    # Function_1_424 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_436")
    Event(0, 5)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_445")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_445")

    Return()

    # Function_2_425 end

    def Function_3_446(): pass

    label("Function_3_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_END)), "loc_452")
    Call(0, 4)

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_45B")

    label("loc_45B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_473")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_473")

    Sound(126, 1, 80, 0)
    Return()

    # Function_3_446 end

    def Function_4_47A(): pass

    label("Function_4_47A")

    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 2500, 0, -10500, 315)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 1340, 0, -12150, 135)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xD, -1950, 0, -13510, 315)
    SetChrChipByIndex(0xE, 0x4)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x1)
    SetChrPos(0xE, 1910, 0, -15040, 180)
    Return()

    # Function_4_47A end

    def Function_5_56D(): pass

    label("Function_5_56D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08100.itc", 0x1E)
    OP_68(0, 1800, -27300, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_5FF")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 600, 0, -31250, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_651")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1250, 0, -33500, 315)
    SetChrPos(0x103, 600, 0, -31250, 315)
    SetChrPos(0x104, 1990, 0, -32500, 315)
    Jump("loc_69E")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_69E")
    SetChrPos(0x101, -600, 0, -30250, 0)
    SetChrPos(0x102, 1990, 0, -32500, 315)
    SetChrPos(0x103, 1250, 0, -33500, 315)
    SetChrPos(0x104, 600, 0, -31250, 315)

    label("loc_69E")

    FadeToBright(1000, 0)
    OP_68(0, 900, -27300, 3000)
    OP_6F(0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_721")
    TurnDirection(0x102, 0x101, 300)

    ChrTalk(
        0x102,
        (
            "#3500710V#5304F#2PI'm ready if you are.\x02\x03",
            "#3500711V#5300FShall we get going?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FD")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_79A")
    TurnDirection(0x103, 0x101, 300)

    ChrTalk(
        0x103,
        (
            "#3500712V#5403F#2PI believe I am as ready as I will ever be.\x02\x03",
            "#3500713V#5401FShould we go now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FD")

    label("loc_79A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_7FD")
    TurnDirection(0x104, 0x101, 300)

    ChrTalk(
        0x104,
        (
            "#3500714V#5604F#2PI'm ready to go, man.\x02\x03",
            "#3500715V#5600FTime to hit the road?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FD")

    TurnDirection(0x101, 0xEF, 400)

    ChrTalk(
        0x101,
        "#3500716V#5003F#5PWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Enter the Schwarze Auction.\x01",      # 0
            "Hold off for now.\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_88B"),
        (1, "loc_F0C"),
        (SWITCH_DEFAULT, "loc_111A"),
    )


    label("loc_88B")

    StopBGM(0xBB8)
    Sleep(150)
    Fade(1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(882, 0, 100, 0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd put on his pair of glasses.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#3500717V#5100F#5PI'm ready. First things first:\x01",
            "Let's try to get in the auction.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_AD9")

    ChrTalk(
        0x102,
        "#3500718V#5304F#2PWe can do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500719V#0201F#12PLloyd, Elie. You are going into a precarious\x01",
            "situation... Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#3500720V#0301F#12PWe'll be hangin' out around this area\x01",
            "like we planned.\x02\x03",
            "#3500727VIf anything comes up, give us a call\x01",
            "on your Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500734V#5102F#5POf course. You guys make sure\x01",
            "to be cautious, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500723V#5302F#5PI think it's time, Lloyd.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_C72")

    ChrTalk(
        0x103,
        "#3500738V#5404F#2PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500725V#0101F#12PLloyd, Tio. There's still a lot of unknown\x01",
            "factors... Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#3500726V#0301F#12PWe'll be hangin' out around this area\x01",
            "like we planned.\x02\x03",
            "#3500721VIf anything comes up, give us a call\x01",
            "on your Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500728V#5102F#5POf course. You guys make sure\x01",
            "to be cautious, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500729V#5402F#5PWe will be off, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_E20")

    ChrTalk(
        0x104,
        "#3500730V#5604F#2PLet's roll, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500731V#0201F#12PLloyd, Randy. You are going into a precarious\x01",
            "situation... Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#3500732V#0101F#12PWe'll wait in the nearby area,\x01",
            "just like we planned.\x02\x03",
            "#3500733VIf anything comes up, please\x01",
            "contact us on your Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500722V#5102F#5POf course. You guys make sure\x01",
            "to be cautious, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500735V#5602F#5PLet's get this party started.\x02",
    )

    CloseMessageWindow()

    label("loc_E20")

    WaitBGM()
    PlayBGM("ed7125", 0)

    def lambda_E2A():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E2A)

    def lambda_E37():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E37)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_68(0, 2600, -27300, 6000)

    def lambda_E5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5D)

    def lambda_E72():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E72)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_D5(0x1E)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipPat(0x0, 0x1, 0x51)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_EE1")
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_F04")

    label("loc_EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_EF5")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    Jump("loc_F04")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_F04")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)

    label("loc_F04")

    Call(0, 6)
    Jump("loc_111A")

    label("loc_F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_FBA")

    ChrTalk(
        0x102,
        (
            "#3500736V#5303FWe don't have much time, Lloyd.\x02\x03",
            "#3500737V#5301FWe should attempt to disguise ourselves\x01",
            "by mixing with the other guests entering\x01",
            "the venue.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FF")

    label("loc_FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1063")

    ChrTalk(
        0x103,
        (
            "#3500724V#5403FI am prepared and ready when you are.\x02\x03",
            "#3500739V#5401FBut, would it not be a smart idea to try\x01",
            "to blend in with other guests entering?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FF")

    label("loc_1063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_10FF")

    ChrTalk(
        0x104,
        (
            "#3500740V#5605FWhat? You still need time to prep?\x02\x03",
            "#3500741V#5601FAs long as we go in while other guests\x01",
            "are around, it'll be smooth sailin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t101B", 101, 0, 0)
    IdleLoop()
    Jump("loc_111A")

    label("loc_111A")

    Return()

    # Function_5_56D end

    def Function_6_111B(): pass

    label("Function_6_111B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50354.itc", 0x1E)
    LoadChrToIndex("apl/ch50355.itc", 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0xF, -340, 200, 1500, 0)
    SetChrPos(0x10, 770, 200, 750, 0)
    SetChrPos(0x101, 600, 0, -19500, 0)
    SetChrPos(0xEF, -600, 0, -21000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    OP_70(0x0, 0xA)
    ClearMapObjFlags(0x0, 0x10)
    FadeToBright(1000, 0)
    OP_68(0, 500, 1470, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44890, 0)
    OP_68(0, 500, 22520, 15000)

    def lambda_122C():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_122C)

    def lambda_1246():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1246)

    def lambda_1260():
        OP_95(0xFE, -600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1260)

    def lambda_127A():
        OP_95(0xFE, 600, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_127A)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    BeginChrThread(0xF, 3, 0, 11)
    Sleep(1000)
    BeginChrThread(0x10, 3, 0, 11)
    Sleep(2000)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 10)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    Sleep(1000)
    OP_0D()
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    SetChrPos(0x8, 600, 0, 23800, 180)
    SetChrPos(0x9, -600, 0, 23800, 180)
    SetChrPos(0x101, 600, 0, 13500, 0)
    SetChrPos(0xEF, -600, 0, 12500, 0)
    OP_68(0, 1000, 22320, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21700, 0)
    SetCameraDistance(19200, 3000)

    def lambda_1373():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1373)

    def lambda_1388():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1388)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_13C5():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13C5)
    Sleep(100)

    def lambda_13DD():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13DD)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x10)

    ChrTalk(
        0x8,
        "#3500742V#5PWelcome to the Schwarze Auction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500743V#5PMay I see your invitation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500744V#5100F#11POf course. Here you are.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd handed over the invitation to\x01",
            "whom he assumes is a mafioso.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#3500745V#5PEverything checks out on my end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500746V#5PFor security reasons, could you please\x01",
            "give us your names for verification?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500747V#5105F#11PName...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#3500748V#5104F#11PI'm Guy Bannings. I presume it's not\x01",
            "mandatory to use my real name, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3500749V#5PNo, that won't be required of you.\x02",
    )

    CloseMessageWindow()

    def lambda_1642():

        label("loc_1642")

        TurnDirection(0xFE, 0xEF, 500)
        Yield()
        Jump("loc_1642")

    QueueWorkItem2(0x8, 1, lambda_1642)
    Sleep(300)

    ChrTalk(
        0x8,
        "#3500750V#5PAnd your guest...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1A8C")

    ChrTalk(
        0x102,
        (
            "#3500751V#5304F#12PAren't you boys working hard?\x02\x03",
            "#3500752V#5300FUnfortunately, I can't exactly reveal\x01",
            "my name in this setting...\x02\x03",
            "#3500753VThat won't be a problem, will it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500754V#5PW-Well, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500755V#5PStill, do you mind informing us of your\x01",
            "relationship with this gentleman?\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x102, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#3500756V#5309F#12POh? We don't look like lovers to you?\x02\x03",
            "#3500757V#5302FHeehee... To be more specific, we're in\x01",
            "the middle of a passionate relationship\x01",
            "that I have yet to tell my parents about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500758V#5106F#11PForgive me, dear. I've caused you all this\x01",
            "trouble because of my social status...\x02\x03",
            "#3500759V#5101FHowever, I will work tirelessly in order to stand\x01",
            "before your parents and ask them for their\x01",
            "beloved daughter's hand in marriage...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500760V#5309F#12POh, you will? Better not let me down, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500761V#5PAhem. My apologies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3500794V#5PWell, honored guests...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500795V#5PWe hope and pray that you enjoy tonight's\x01",
            "auction to the fullest extent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_245A")

    label("loc_1A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1FB6")
    TurnDirection(0x103, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3500764V#5406F#6PUm, Brother?\x02\x03",
            "#3500765V#5408FDo I really have to tell this strange\x01",
            "man my name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500766V#5104F#11PNo, that shouldn't be necessary.\x02\x03",
            "#3500767V#5101FThis young lady is my little sister.\x01",
            "Is that going to be a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500768V#5PNo, of course not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500769V#5PForgive my rudeness, but you\x01",
            "two hardly resemble each other.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x190)

    ChrTalk(
        0x103,
        (
            "#3500770V#5404F#12PThere's a simple explanation for that.\x02\x03",
            "#3500771V#5402FI joined their family after my mother\x01",
            "married into it, so my brother and\x01",
            "I are actually step siblings.\x02\x03",
            "#3500772V#5409FThat means we could get married,\x01",
            "if we wanted to.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3500773V#5106F#11PWhat am I going to do with you?\x01",
            "You're not old enough to be\x01",
            "worrying about marriage.\x02\x03",
            "#3500774V#5102FThere are a lot of complex things\x01",
            "going on in our family, as you can\x01",
            "see.\x02\x03",
            "#3500775VOn a different note, my sister here\x01",
            "has some of the sharpest eyes\x01",
            "I know.\x02\x03",
            "#3500776VI brought her along in order to help\x01",
            "me size up some of the items that\x01",
            "will be bid on tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500777V#5402F#12PTeehee. I won't let you down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500778V#5PHaha. You don't see siblings who\x01",
            "get along this well every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3500779V#5PWell, honored guests...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500780V#5PWe hope and pray that you enjoy tonight's\x01",
            "auction to the fullest extent.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    Jump("loc_245A")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(
        0x104,
        (
            "#3500781V#5600F#12PYo! I've been this guy's bud ever since\x01",
            "we were tykes.\x02\x03",
            "#3500782V#5609FI'll let ya in on a lil' secret. This guy is\x01",
            "waaay too uptight.\x02\x03",
            "#3500783V'Cause of that, I convinced him to go\x01",
            "to this shindig with me. I'm hopin' that\x01",
            "he can let loose and live a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3500784V#5111F#11PI-I would appreciate it if you didn't talk\x01",
            "about me like that in front of them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3500785V#5PHaha, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3500786V#5PAs far as experiences go, you'll definitely\x01",
            "want to have this one under your belt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500787V#5106F#11PAlso, stop treating me like some kid.\x02\x03",
            "#3500788V#5101FI didn't agree to come because you\x01",
            "kept pestering me about it.\x02\x03",
            "#3500789VI just thought learning a thing or two\x01",
            "about high society would do me good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500790V#5604F#12PYeah, yeah. No need to get all worked\x01",
            "up about it.\x02\x03",
            "#3500791V#5602FHey, I hear there's some real nice stuff\x01",
            "up for bid in there...\x02\x03",
            "#3500792VMy hype ain't going to go to waste, is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        "#3500793V#5PYou don't need to worry on that front.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#3500762V#5PWell, honored guests...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3500763V#5PWe hope and pray that you enjoy tonight's\x01",
            "auction to the fullest extent.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)

    label("loc_245A")

    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_68(0, 1000, 23820, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_24AC")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x102, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    Jump("loc_24C3")

    label("loc_24AC")

    BeginChrThread(0x101, 3, 0, 11)
    Sleep(750)
    BeginChrThread(0xEF, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)

    label("loc_24C3")

    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_111B end

    def Function_7_24DD(): pass

    label("Function_7_24DD")


    def lambda_24E2():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24E2)

    def lambda_24FC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24FC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_24DD end

    def Function_8_250D(): pass

    label("Function_8_250D")


    def lambda_2512():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2512)

    def lambda_252C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_252C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_250D end

    def Function_9_253D(): pass

    label("Function_9_253D")


    def lambda_2542():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2542)

    def lambda_255C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_255C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_253D end

    def Function_10_256D(): pass

    label("Function_10_256D")


    def lambda_2572():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2572)

    def lambda_258C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_258C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_256D end

    def Function_11_259D(): pass

    label("Function_11_259D")


    def lambda_25A2():
        OP_95(0xFE, 0, 0, 24380, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25A2)
    WaitChrThread(0xFE, 1)

    def lambda_25C0():
        OP_95(0xFE, 0, 800, 29450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25C0)
    Sleep(2000)

    def lambda_25DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25DD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_259D end

    def Function_12_25F2(): pass

    label("Function_12_25F2")


    def lambda_25F7():
        OP_97(0xFE, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25F7)
    Sleep(3500)

    def lambda_2614():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2614)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_25F2 end

    def Function_13_2629(): pass

    label("Function_13_2629")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31100.itc", 0x22)
    LoadChrToIndex("chr/ch31150.itc", 0x23)
    LoadChrToIndex("chr/ch31151.itc", 0x24)
    LoadChrToIndex("chr/ch31153.itc", 0x25)
    LoadChrToIndex("chr/ch31900.itc", 0x26)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch31953.itc", 0x29)
    LoadChrToIndex("apl/ch50372.itc", 0x2A)
    LoadEffect(0x0, "event\\ev310_00.eff")
    LoadEffect(0x1, "battle\\ms00001.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xA, 2500, 0, -16500, 0)
    SetChrPos(0xB, -2500, 0, -16500, 0)
    SetChrPos(0xC, 0, 0, -17500, 0)
    SetChrPos(0xD, 1000, 0, -15500, 0)
    SetChrPos(0xE, -1000, 0, -15500, 0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x11, 0, 0, 50000, 0)
    SetChrPos(0x12, 0, 0, 50000, 0)
    BeginChrThread(0x11, 0, 0, 22)
    BeginChrThread(0x12, 0, 0, 22)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0x14, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 800, 29650, 180)
    SetChrPos(0xEF, 0, 800, 29650, 180)
    SetChrPos(0x105, 0, 800, 29650, 180)
    SetChrPos(0x133, 0, 800, 29650, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_286E")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_28C9")

    label("loc_286E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_289E")
    SetChrPos(0x102, 600, 200, -14600, 0)
    SetChrPos(0x104, -600, 200, -14600, 0)
    Jump("loc_28C9")

    label("loc_289E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_28C9")
    SetChrPos(0x103, 600, 200, -14600, 0)
    SetChrPos(0x102, -600, 200, -14600, 0)

    label("loc_28C9")

    OP_68(0, 1100, 32500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26840, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(25840, 2500)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(0, 1100, 21000, 3500)
    MoveCamera(0, 30, 0, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(300)
    BeginChrThread(0xEF, 3, 0, 15)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 16)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1100, -2600, 0)
    MoveCamera(325, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25840, 0)
    SetCameraDistance(20320, 4000)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x105, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2A4D")

    def lambda_2A18():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A18)
    Sleep(300)

    def lambda_2A30():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A30)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_2ACE")

    label("loc_2A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2A90")

    def lambda_2A5B():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A5B)
    Sleep(300)

    def lambda_2A73():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A73)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_2ACE")

    label("loc_2A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2ACE")

    def lambda_2A9E():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A9E)
    Sleep(300)

    def lambda_2AB6():
        OP_9B(0x0, 0xFE, 0x0, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2AB6)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)

    label("loc_2ACE")

    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B03")

    ChrTalk(
        0x103,
        "#3501731V#0201F#6PLloyd...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B2A")

    label("loc_2B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2B2A")

    ChrTalk(
        0x104,
        "#3501732V#0307F#6PLloyd!\x02",
    )

    CloseMessageWindow()

    label("loc_2B2A")


    ChrTalk(
        0x101,
        "#3501733V#0002F#11PThank goodness you guys were close by!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2C04")

    ChrTalk(
        0x104,
        "#3501734V#0306F#6PPhew, you had me scared there for a second...\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#3501735V#0305F#6PWait, who's the kid?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB2")

    label("loc_2C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CB2")

    ChrTalk(
        0x102,
        (
            "#3501736V#0106F#6PWe were so worried that you wouldn't\x01",
            "be able to get out...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#3501737V#0105F#6PHold on... Who's this girl?!\x02",
    )

    CloseMessageWindow()

    label("loc_2CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2D2D")

    ChrTalk(
        0x102,
        (
            "#3501738V#0106F#11PWe told you earlier, didn't we? We found\x01",
            "this little girl and took her into custody.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E08")

    label("loc_2D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2D9A")

    ChrTalk(
        0x103,
        (
            "#3501739V#0206F#11PWe contacted you earlier and told you\x01",
            "about taking her into custody...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E08")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2E08")

    ChrTalk(
        0x104,
        (
            "#3501740V#0309F#11PYou forget? We told ya that we found\x01",
            "this kiddo and took her under our wing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E08")


    NpcTalk(
        0x101,
        "KeA",
        "#3501741V#5805F#5PHey, Lloyd! Are these people your friends?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501742V#0004F#11PYeah, we can count on them.\x02\x03",
            "#3501743V#0000FGuys, we don't have much time left.\x01",
            "We need to get out of here while we--\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    NpcTalk(
        0xD,
        "Man's Voice",
        "#3501744V#2PHeh. That ain't happening, kid!\x02",
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1200, -7000, 2500)
    MoveCamera(310, 20, 0, 2500)
    OP_6E(560, 2500)
    SetCameraDistance(21000, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3028")

    def lambda_300E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_300E)

    def lambda_301B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_301B)
    Jump("loc_3073")

    label("loc_3028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3050")

    def lambda_3036():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3036)

    def lambda_3043():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3043)
    Jump("loc_3073")

    label("loc_3050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3073")

    def lambda_305E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_305E)

    def lambda_306B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_306B)

    label("loc_3073")


    def lambda_3078():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3078)
    Sleep(50)

    def lambda_3090():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3090)
    Sleep(50)

    def lambda_30A8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_30A8)
    Sleep(50)

    def lambda_30C0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_30C0)
    Sleep(50)

    def lambda_30D8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30D8)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501745V#0010F#11PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#3501746V#0406F#2PIt looks like they saw through our\x01",
            "tricks with ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501747V#6PI wasn't sure about the boss' orders\x01",
            "at first, but I guess keepin' an eye\x01",
            "on this area was the right call after all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3501748V#5PSo you guys are those police twerps\x01",
            "I've heard about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3501749V#5PSorry, but you've played your little game\x01",
            "for long enough, don'tcha think?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(150)
    Fade(500)
    SetCameraDistance(20500, 500)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x2)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_360B")
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501750V#0007F#11PLook out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501751V#0307F#11POrbal machine guns...? How the hell\x01",
            "did they get their hands on those?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3501752V#0201F#11PAnd they appear to be the latest model\x01",
            "from Erebonia's Reinford Company...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3501753V#6PHeh heh... Resist all you like. It won't help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#3501754V#5PHaha! With this kinda firin' speed,\x01",
            "you'll be mincemeat in seconds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501755V#0110F#11PUgh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#3501756V#5801F#5PHey, Lloyd...\x02\x03",
            "#3501757VIs this what it means to be in a 'pinch'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501758V#0013F#11PPretty much...\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#3501759V#0404F#11PI wouldn't say we're out of luck just yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501760V#0005F#11PHuh...?\x02",
    )

    CloseMessageWindow()

    label("loc_360B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37E9")
    Fade(500)
    OP_68(-11030, 3200, -1010, 0)
    MoveCamera(310, 8, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(23000, 0)
    Sleep(300)
    OP_68(-140, 1200, -10540, 1500)
    MoveCamera(300, 28, 0, 1500)
    SetCameraDistance(17930, 1500)
    BeginChrThread(0x11, 3, 0, 26)
    Sleep(1350)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    ChrTalk(
        0xE,
        "#3501761V#4S#5PGah...?!\x05\x02",
    )

    BeginChrThread(0xE, 3, 0, 17)
    Sleep(100)

    ChrTalk(
        0xD,
        "#3501762V#4S#6PUgh...?!\x05\x02",
    )

    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x11, 3)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#3501763V#5PWhat the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3501764V#5PThe hell...?!\x02",
    )

    CloseMessageWindow()

    label("loc_37E9")

    Fade(500)
    OP_68(2450, 800, -11290, 0)
    MoveCamera(224, 35, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30050, 0)
    OP_68(0, 800, -9180, 3000)
    MoveCamera(305, 25, 0, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0x11, 3, 0, 28)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(1650)
    OP_82(0x1F4, 0x0, 0xBB8, 0x96)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    ChrTalk(
        0xB,
        "#3501765V#4S#5PGyaaaah...!\x05\x02",
    )

    BeginChrThread(0xB, 3, 0, 19)
    Sleep(1600)
    OP_82(0x1F4, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(500)

    ChrTalk(
        0xC,
        "#3501766V#4S#6PNo...!\x05\x02",
    )

    BeginChrThread(0xC, 3, 0, 21)
    Sleep(150)

    ChrTalk(
        0xA,
        "#3501767V#4S#6PUgh...!\x05\x02",
    )

    BeginChrThread(0xA, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(0, 1100, -3200, 2500)
    MoveCamera(325, 13, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(21000, 2500)
    OP_6F(0x79)

    NpcTalk(
        0x101,
        "KeA",
        (
            "#3501768V#5805F#5PWoooow...\x02\x03",
            "#3501769V#5810FThat looked like it hurt a bunch.\x01",
            "Are they going to be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501770V#0011F#11PWh-What just happened...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3ADF")
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#3501771V#0301F#6PThat thing came flyin' in from\x01",
            "over by the mansion...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B2D")

    label("loc_3ADF")


    ChrTalk(
        0x104,
        (
            "#3501771V#0301F#11PThat thing came flyin' in from\x01",
            "over by the mansion...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2D")


    ChrTalk(
        0x105,
        (
            "#3501772V#0404F#11PHaha, some sympathetic soul must\x01",
            "have decided to help us out.\x02\x03",
            "#3501773V#0402FHow about we save our thanks for\x01",
            "later and continue our escape?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501774V#0007F#11PRight! Let's move!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C60")
    OP_93(0x102, 0x0, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#3501775V#0101F#6PThere should be a ferry arriving\x01",
            "right about now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CBA")

    label("loc_3C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3CBA")
    OP_93(0x103, 0x0, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#3501776V#0201F#6PThere should be a ferry arriving\x01",
            "around this time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D08")
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x104,
        "#3501777V#0307F#6PLet's just hurry to the dock!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4C")

    label("loc_3D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3D4C")
    OP_93(0x103, 0x0, 0x1F4)

    ChrTalk(
        0x103,
        "#3501778V#0201F#6PWe should hurry to the dock!\x02",
    )

    CloseMessageWindow()

    label("loc_3D4C")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(20000, 2000)
    OP_6F(0x10)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x5A, 3)
    Call(0, 4)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_49()
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    OP_70(0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    SetScenarioFlags(0xA7, 3)
    OP_29(0x47, 0x1, 0x12)
    EventEnd(0x5)
    Return()

    # Function_13_2629 end

    def Function_14_3DFE(): pass

    label("Function_14_3DFE")


    def lambda_3E03():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E03)

    def lambda_3E18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E18)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_3E45():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E45)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_3DFE end

    def Function_15_3E5A(): pass

    label("Function_15_3E5A")


    def lambda_3E5F():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E5F)

    def lambda_3E74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3E74)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0x258, 0x0, 0x0, 0x0, 0x0)

    def lambda_3EA1():
        OP_95(0xFE, -600, 200, -1700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EA1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_3E5A end

    def Function_16_3EBB(): pass

    label("Function_16_3EBB")


    def lambda_3EC0():
        OP_9B(0x0, 0xFE, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EC0)

    def lambda_3ED5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3ED5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_98(0xFE, 0xFFFFFDA8, 0x0, 0x0, 0x0, 0x0)

    def lambda_3F02():
        OP_95(0xFE, 600, 200, -2200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F02)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_3EBB end

    def Function_17_3F1C(): pass

    label("Function_17_3F1C")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_3F66():
        OP_9D(0xFE, 0xFFFFFC18, 0x0, 0xFFFFCB44, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F66)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_17_3F1C end

    def Function_18_3F91(): pass

    label("Function_18_3F91")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1000, 900, -10500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_3FD5():
        OP_9D(0xFE, 0x3E8, 0x0, 0xFFFFC950, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FD5)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_18_3F91 end

    def Function_19_3FFA(): pass

    label("Function_19_3FFA")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_4044():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFD8F0, 0xFFFFCD38, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4044)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(927, 0, 100, 0)
    Return()

    # Function_19_3FFA end

    def Function_20_406F(): pass

    label("Function_20_406F")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2500, 900, -11500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_40B9():
        OP_9D(0xFE, 0x9C4, 0x0, 0xFFFFCF2C, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40B9)
    WaitChrThread(0xFE, 1)
    Sound(514, 0, 100, 0)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_20_406F end

    def Function_21_40E4(): pass

    label("Function_21_40E4")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 900, -12500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_4128():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFCB44, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4128)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_21_40E4 end

    def Function_22_414D(): pass

    label("Function_22_414D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_416B")
    OP_A1(0xFE, 0xFA0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_22_414D")

    label("loc_416B")

    Return()

    # Function_22_414D end

    def Function_23_416C(): pass

    label("Function_23_416C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4193")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_23_416C")

    label("loc_4193")

    Return()

    # Function_23_416C end

    def Function_24_4194(): pass

    label("Function_24_4194")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41BB")
    OP_52(0xFE, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("Function_24_4194")

    label("loc_41BB")

    Return()

    # Function_24_4194 end

    def Function_25_41BC(): pass

    label("Function_25_41BC")

    SetChrPos(0xFE, 0, 0, 14500, 0)
    OP_9E(0xFE, 0x0, 0x7D0, 0xFFFEA070, 0xEA60, 0x0)

    def lambda_41E7():
        OP_9E(0xFE, 0x0, 0x7D0, 0xFFFD40E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41E7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_41BC end

    def Function_26_4202(): pass

    label("Function_26_4202")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 25)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1388), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_425D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_428B")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_425D")

    label("loc_428B")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_26_4202 end

    def Function_27_429C(): pass

    label("Function_27_429C")

    SetChrPos(0xFE, -2500, 0, 16000, 0)
    OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x13880, 0xEA60, 0x0)

    def lambda_42C7():
        OP_9E(0xFE, 0xFFFFF63C, 0x8CA, 0x347D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42C7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_429C end

    def Function_28_42E2(): pass

    label("Function_28_42E2")

    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrFlags(0xFE, 0x800)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x13, 3, 0, 27)
    BeginChrThread(0xFE, 2, 0, 23)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4E20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4342")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_437C")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_4342")

    label("loc_437C")

    WaitChrThread(0x13, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x800)
    Return()

    # Function_28_42E2 end

    def Function_29_4392(): pass

    label("Function_29_4392")

    SetChrPos(0xFE, 0, 0, 15000, 0)
    OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0xEA60, 0x0)

    def lambda_43BD():
        OP_9E(0xFE, 0x0, 0x3E8, 0xFFFDF0A8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43BD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_4392 end

    def Function_30_43D8(): pass

    label("Function_30_43D8")

    Sleep(2000)
    PlayEffect(0x0, 0xFF, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(926, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x12C)
    BeginChrThread(0x14, 3, 0, 29)
    BeginChrThread(0xFE, 2, 0, 24)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4436")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4470")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_NEG), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    Jump("loc_4436")

    label("loc_4470")

    WaitChrThread(0x14, 3)
    EndChrThread(0xFE, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_43D8 end

    def Function_31_4481(): pass

    label("Function_31_4481")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FThere's no time to backtrack...\x01",
            "We have to hurry and take her\x01",
            "to the dock!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    Return()

    # Function_31_4481 end

    SaveToFile()

Try(main)
