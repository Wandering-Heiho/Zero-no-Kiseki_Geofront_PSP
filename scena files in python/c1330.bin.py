from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1330.bin",                # FileName
        "c1330",                    # MapName
        "c1330",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1330",                  # 0
    ))

    ScpFunction((
        "Function_0_AC",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_F4",           # 02, 2
        "Function_3_5F4",          # 03, 3
        "Function_4_EC6",          # 04, 4
        "Function_5_1AE6",         # 05, 5
    ))


    def Function_0_AC(): pass

    label("Function_0_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2")
    Event(0, 3)
    Jump("loc_DB")

    label("loc_C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8")
    Event(0, 4)
    Jump("loc_DB")

    label("loc_D8")

    Event(0, 2)

    label("loc_DB")

    Return()

    # Function_0_AC end

    def Function_1_DC(): pass

    label("Function_1_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3")

    Return()

    # Function_1_DC end

    def Function_2_F4(): pass

    label("Function_2_F4")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 2200, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E")
    SetChrPos(0x1, 500, 0, -500, 90)

    label("loc_15E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D")
    SetChrPos(0x2, 500, 0, 500, 90)

    label("loc_17D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_19C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB")
    SetChrPos(0x4, -1900, 0, -600, 90)

    label("loc_1BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA")
    SetChrPos(0x5, -1900, 0, 600, 90)

    label("loc_1DA")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_END)), "loc_440")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_244")

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
    Jump("loc_2D9")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")

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
    Jump("loc_2D9")

    label("loc_291")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")

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

    label("loc_2D9")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_37D")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_339")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_37D")

    label("loc_339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_372")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_37D")

    label("loc_372")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3A8"),
        (1, "loc_3B8"),
        (2, "loc_3C8"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_3A8")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_3D8")

    label("loc_3B8")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_3D8")

    label("loc_3C8")

    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_3D8")

    label("loc_3D8")

    Jump("loc_43B")

    label("loc_3DD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F9"),
        (1, "loc_40F"),
        (2, "loc_425"),
        (SWITCH_DEFAULT, "loc_43B"),
    )


    label("loc_3F9")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_43B")

    label("loc_40F")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_43B")

    label("loc_425")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_43B")

    label("loc_43B")

    Jump("loc_5F3")

    label("loc_440")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_484")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★[ 16F ]\x01",       # 0
            "　[ 1F ]\x01",        # 1
            "　[Cancel]\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C3")

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C3")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　[ 16F ]\x01",       # 0
            "★[ 1F ]\x01",        # 1
            "　[Cancel]\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C3")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EA")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_567")

    label("loc_4EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_523")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_567")

    label("loc_523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55C")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_567")

    label("loc_55C")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_567")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B1")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_58C"),
        (1, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5AC"),
    )


    label("loc_58C")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_5AC")

    label("loc_59C")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_5AC")

    label("loc_5AC")

    Jump("loc_5F3")

    label("loc_5B1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C7"),
        (1, "loc_5DD"),
        (SWITCH_DEFAULT, "loc_5F3"),
    )


    label("loc_5C7")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_5F3")

    label("loc_5DD")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_5F3")

    label("loc_5F3")

    Return()

    # Function_2_F4 end

    def Function_3_5F4(): pass

    label("Function_3_5F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2400, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x102, -4500, 0, 0, 90)
    SetChrPos(0x101, -4500, 0, -500, 90)
    SetChrPos(0x103, -4500, 0, 500, 90)
    SetChrPos(0x104, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-400, 1000, 0, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_6C0():
        OP_96(0xFE, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C0)

    def lambda_6DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6DA)
    Sleep(500)

    def lambda_6EE():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6EE)

    def lambda_708():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_708)
    Sleep(300)

    def lambda_71C():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71C)

    def lambda_736():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_736)
    Sleep(600)

    def lambda_74A():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74A)

    def lambda_764():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_764)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    def lambda_787():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_787)
    Sleep(50)
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#2200333V#6P#0000FThe CEO's office is on the\x01",
            "top floor, right?\x02\x03",
            "#2200334VWhat's the purpose of this\x01",
            "card we were given, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)

    ChrTalk(
        0x102,
        (
            "#2200335V#11P#0100FThat's just an identification card.\x02\x03",
            "#2200336VBecause of all the different businesses that\x01",
            "operate out of this building, the IBC issues\x01",
            "cards to access the appropriate floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200337V#6P#0306FSo it's basically a beefed-up security\x01",
            "system, then.\x02\x03",
            "#2200338V#0301FI kinda feel like they're usin' all the\x01",
            "latest gadgets just 'cause they can.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2200339V#0203F#5PWell, the IBC once led the Crossbell City\x01",
            "portion of the Orbal Network Project.\x02\x03",
            "#2200340VThe scope of the project grew to its current\x01",
            "size once the Crossbellan government joined.\x02\x03",
            "#2200341V#0200FI have heard speculation that the IBC provides\x01",
            "approximately 60 percent of the funding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200342V#11P#0104FI've heard the same as well.\x02\x03",
            "#2200343V#0100FI believe the government provides 30 percent,\x01",
            "while the Epstein Foundation provides the final\x01",
            "10 percent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2200344V#6P#0005FIncredible... I didn't know they were\x01",
            "shouldering more than half the cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2200345V#6P#0300FSo you're tellin' me Crossbell's most generous\x01",
            "man's waiting for us up top, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200346V#11P#0100FYes... Now give me the card, please.\x01",
            "I'll take us to where we need to go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CB1():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CB1)
    Sleep(100)

    def lambda_CC1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CC1)
    WaitChrThread(0x102, 2)
    OP_68(600, 1000, 0, 1000)

    def lambda_CE3():
        OP_95(0xFE, 2300, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE3)
    Sleep(500)

    def lambda_D00():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D00)
    WaitChrThread(0x102, 1)
    OP_6F(0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie inserted the ID card into the slot.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(72, 0, 100, 0)
    Sleep(300)

    Menu(
        0,
        10,
        10,
        0,
        (
            "　[ 16F ]\x01",       # 0
            "★[ 1F ]\x01",        # 1
            "　[Cancel]\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetScenarioFlags(0x82, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DBC")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_E39")

    label("loc_DBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF5")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_E39")

    label("loc_DF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2E")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_E39")

    label("loc_E2E")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_E39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E83")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_E5E"),
        (1, "loc_E6E"),
        (SWITCH_DEFAULT, "loc_E7E"),
    )


    label("loc_E5E")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_E7E")

    label("loc_E6E")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_E7E")

    label("loc_E7E")

    Jump("loc_EC5")

    label("loc_E83")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E99"),
        (1, "loc_EAF"),
        (SWITCH_DEFAULT, "loc_EC5"),
    )


    label("loc_E99")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_EC5")

    label("loc_EAF")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_EC5")

    label("loc_EC5")

    Return()

    # Function_3_5F4 end

    def Function_4_EC6(): pass

    label("Function_4_EC6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(861)
    OP_68(-2400, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x102, -4500, 0, 300, 90)
    SetChrPos(0x101, -4500, 0, -300, 90)
    SetChrPos(0x103, -4500, 0, -500, 90)
    SetChrPos(0x104, -4500, 0, 500, 90)
    SetChrPos(0x138, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis121.itp")
    OP_68(600, 1000, 0, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_1009():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_1009)

    def lambda_1023():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_1023)
    Sleep(900)

    def lambda_1037():
        OP_96(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1037)

    def lambda_1051():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1051)
    Sleep(400)

    def lambda_1065():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFFD94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1065)

    def lambda_107F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_107F)
    Sleep(400)

    def lambda_1093():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1093)

    def lambda_10AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10AD)
    Sleep(400)

    def lambda_10C1():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0xFFFFFCE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10C1)

    def lambda_10DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10DB)
    WaitChrThread(0x138, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    Sound(72, 0, 100, 0)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_68(600, -3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(861, 2, 100, 0)
    OP_68(600, 1000, 0, 5000)
    FadeToBright(4000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_93(0x138, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x138,
        (
            "#2200618V#11P#2903FHmm... Yin, was it?\x02\x03",
            "#2200619V#2901FWhat exactly is his objective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2200620V#0106F#6PWe haven't been able to come to\x01",
            "a conclusion yet, unfortunately.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#2200621V#0305FGot any takes for us, Lloyd?\x02\x03",
            "#2200622V#0300FI'm sure you've probably figured out\x01",
            "a thing or two already.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12CB():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12CB)
    Sleep(100)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x101,
        "#2200623V#11P#0005FYeah, about that...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#2200624V#11P#0003FWhat if I told you...\x02\x03",
            "#2200625V#0001F...the threat letter and the orbmail were\x01",
            "written by two different people?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
        0x104,
        "#2200626V#0301FWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2200627V#6P#0205FI am not sure I follow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200628V#11P#0004FIt's actually pretty simple.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "CEASE PRODUCTION OF YOUR NEW SHOW,\x01",
            "OR THE BELOVED FERVENT DANCER WILL\x01",
            "HAVE A TRAGIC ACCIDENT.    -Yin\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#2200629V#0001FThe threat letter's phrasing is odd but\x01",
            "straightforward. Meanwhile, if you'll\x01",
            "recall the orbmail...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_DB()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "I, Yin, hereby submit my support request.\x01",
            "Overcome this trial and face me. Only then\x01",
            "will I grant you your mission.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#2200630V#0003FThe orbmail is written with an old-fashioned\x01",
            "diction.\x02\x03",
            "#2200631V#0000FDon't you think they read nothing alike?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        "#2200632V#0201FI see your point.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#2200633V#0301FDamn, I feel kinda stupid.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#2200634V#0106FI was so shocked by the content of the orbmail\x01",
            "that I failed to see right through it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x138,
        (
            "#2200635V#2P#2905FHmm...\x02\x03",
            "#2200636V#2901FAnd? What do you make of all of this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(500, 0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#2200637V#6P#0003FA few possibilities come to mind already...\x02\x03",
            "#2200638V#0001FFor example, what if Yin doesn't operate alone?\x01",
            "Their accomplice could have sent us the orbmail.\x02\x03",
            "#2200639VAnother possibility is that Yin intentionally wrote\x01",
            "them differently to throw us off.\x02\x03",
            "#2200640V#0006FI could list off an endless number of possibilities,\x01",
            "and quite frankly, it wouldn't be smart of us to\x01",
            "continue investigating based off of assumptions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        (
            "#2200641V#11P#2900FWell put.\x02\x03",
            "#2200642V#2904FHmm... How interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2200643V#6P#0005FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x138,
        "#2200644V#11P#2902FOh... You'll see.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    Sound(862, 0, 100, 0)
    OP_24(0x35D)
    EndChrThread(0x101, 0x3)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x35D)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_EC6 end

    def Function_5_1AE6(): pass

    label("Function_5_1AE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B1E")
    OP_82(0x0, 0xA, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0x14, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_5_1AE6")

    label("loc_1B1E")

    Return()

    # Function_5_1AE6 end

    SaveToFile()

Try(main)
