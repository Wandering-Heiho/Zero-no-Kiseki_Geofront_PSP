from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c133b.bin",                # FileName
        "c133b",                    # MapName
        "c133b",                    # Location
        0x001B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c133b",                  # 0
        "Elie",                   # 1
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_C8",           # 00, 0
        "Function_1_FB",           # 01, 1
        "Function_2_FC",           # 02, 2
        "Function_3_43B",          # 03, 3
        "Function_4_92C",          # 04, 4
        "Function_5_E66",          # 05, 5
    ))


    def Function_0_C8(): pass

    label("Function_0_C8")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3")
    Event(0, 3)
    Jump("loc_FA")

    label("loc_E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_F7")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_FA")

    label("loc_F7")

    Event(0, 2)

    label("loc_FA")

    Return()

    # Function_0_C8 end

    def Function_1_FB(): pass

    label("Function_1_FB")

    Return()

    # Function_1_FB end

    def Function_2_FC(): pass

    label("Function_2_FC")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x0, 2200, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166")
    SetChrPos(0x1, 500, 0, -500, 90)

    label("loc_166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_185")
    SetChrPos(0x2, 500, 0, 500, 90)

    label("loc_185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A4")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_1A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3")
    SetChrPos(0x4, -1900, 0, -600, 90)

    label("loc_1C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2")
    SetChrPos(0x5, -1900, 0, 600, 90)

    label("loc_1E2")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★[ 16F ]\x01",       # 0
            "　[ 1F ]\x01",        # 1
            "　[ B5 ]\x01",        # 2
            "　[Cancel]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D8")

    label("loc_243")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　[ 16F ]\x01",       # 0
            "★[ 1F ]\x01",        # 1
            "　[ B5 ]\x01",        # 2
            "　[Cancel]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D8")

    label("loc_290")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D8")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　[ 16F ]\x01",       # 0
            "　[ 1F ]\x01",        # 1
            "★[ B5 ]\x01",        # 2
            "　[Cancel]\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D8")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_37C")

    label("loc_2FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_338")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_37C")

    label("loc_338")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_371")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_37C")

    label("loc_371")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3A7"),
        (1, "loc_3B7"),
        (2, "loc_3C7"),
        (SWITCH_DEFAULT, "loc_3D7"),
    )


    label("loc_3A7")

    EventEnd(0x5)
    NewScene("c134B", 100, 0, 0)
    IdleLoop()
    Jump("loc_3D7")

    label("loc_3B7")

    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Jump("loc_3D7")

    label("loc_3C7")

    EventEnd(0x5)
    NewScene("c1320", 103, 0, 0)
    IdleLoop()
    Jump("loc_3D7")

    label("loc_3D7")

    Jump("loc_43A")

    label("loc_3DC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F8"),
        (1, "loc_40E"),
        (2, "loc_424"),
        (SWITCH_DEFAULT, "loc_43A"),
    )


    label("loc_3F8")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c134B", 100, 0, 0)
    IdleLoop()
    Jump("loc_43A")

    label("loc_40E")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Jump("loc_43A")

    label("loc_424")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1320", 103, 0, 0)
    IdleLoop()
    Jump("loc_43A")

    label("loc_43A")

    Return()

    # Function_2_FC end

    def Function_3_43B(): pass

    label("Function_3_43B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_4D7():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D7)

    def lambda_4F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F1)
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200807V\x07\x00",
            "#0000FLloyd Bannings of the\x01",
            "Special Support Section here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200808V\x07\x05",
            "Oh. It's me, Dieter Crois.\x02\x03",
            "#5200809VSorry about that. Did you mistake\x01",
            "it for a call from the police department?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200810V\x07\x00",
            "#0006FN-No, sir...\x02\x03",
            "#5200811V#0001FHave you had any luck\x01",
            "contacting anybody?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5200812V\x07\x05",
            "Not yet, I'm afraid.\x02\x03",
            "#5200813VI'll be frank. I'm concerned about a\x01",
            "report from the guards at the front gate.\x02\x03",
            "#5200814VI hate to ask this while you're resting, but\x01",
            "could you come to my office for a chat?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5200815V\x07\x00",
            "#0001FYeah, no problem.\x01",
            "I'll see you soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200816V#0008F(A report from the guards?\x01",
            "I've got a bad feeling about this.)\x02\x03",
            "#5200817V#0001F(I'd better make sure I've got\x01",
            "all my equipment in order before I go.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetScenarioFlags(0xE4, 4)
    OP_29(0x4E, 0x1, 0x1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Call(0, 2)
    Return()

    # Function_3_43B end

    def Function_4_92C(): pass

    label("Function_4_92C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(861)
    OP_68(600, -3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x102, 600, 0, -600, 90)
    SetChrPos(0x101, 600, 0, 600, 90)
    SetChrPos(0x103, -600, 0, -800, 90)
    SetChrPos(0x104, -600, 0, 800, 90)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, 0, 90)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(861, 2, 100, 0)
    OP_68(600, 1000, 0, 5000)
    SetCameraDistance(18500, 5000)
    FadeToBright(4000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5200890V#0004F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200891V#0102F#5PWe have to protect them. It's our duty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200892V#6P#0201FAgreed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200893V#6P#0303FI think now's a good time to remind you\x01",
            "that the CGF are elite combatants.\x02\x03",
            "#5200894VDrugs or not, these guys know what the\x01",
            "hell they're doin'.\x02\x03",
            "#5200895V#0301FIn other words, this battle's gonna be\x01",
            "unlike any other we've faced before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200896V#0004F#5PYeah, I'm well aware.\x02\x03",
            "#5200897V#0000FOur time together has led to this\x01",
            "very moment. It all comes down\x01",
            "to teamwork now.\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(17500, 800)

    def lambda_C2D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C2D)
    Sleep(50)

    def lambda_C3D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3D)
    Sleep(50)

    def lambda_C4D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C4D)
    Sleep(50)

    def lambda_C5D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C5D)
    WaitChrThread(0x101, 2)
    OP_6F(0x10)
    CancelBlur(0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5200898V#0003F#5POur first objective is to disarm the bombs.\x02\x03",
            "#5200899V#0013FNext, we'll prevent the soldiers from\x01",
            "breaching the gates.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5200900V#0007F#5PMay the Goddess watch over us!\x01",
            "Keep your wits about you, everyone!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(1153, 255, 100, 0)
    Sound(1249, 255, 100, 1)
    Sound(1343, 255, 100, 2)

    ChrTalk(
        0x8,
        "#0107F#1K#2PRoger!\x02",
    )


    ChrTalk(
        0x103,
        "#0201F#1K#6PUnderstood!\x02",
    )


    ChrTalk(
        0x104,
        "#5200901V#0307F#1K#1PIt's showtime!\x02",
    )

    OP_57(0x1)
    OP_5A()
    FadeToDark(2000, 0, -1)
    Sound(862, 0, 100, 0)
    OP_24(0x35D)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_6F(0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3F")
    OP_29(0x31, 0x4, 0x40)
    Jump("loc_E51")

    label("loc_E3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E51")
    OP_29(0x31, 0x4, 0x40)

    label("loc_E51")

    SetScenarioFlags(0xE7, 5)
    SetScenarioFlags(0x5F, 1)
    OP_24(0x35D)
    EventEnd(0x5)
    NewScene("c131B", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_4_92C end

    def Function_5_E66(): pass

    label("Function_5_E66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8A")
    OP_82(0x0, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_5_E66")

    label("loc_E8A")

    Return()

    # Function_5_E66 end

    SaveToFile()

Try(main)
