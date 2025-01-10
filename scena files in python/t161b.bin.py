from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t161b.bin",                # FileName
        "t161b",                    # MapName
        "t161b",                    # Location
        0x0054,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 84, 0, 0, 0, 1],
    )

    BuildStringList((
        "t161b",                  # 0
    ))

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A8",           # 01, 1
        "Function_2_C1",           # 02, 2
        "Function_3_530",          # 03, 3
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Event(0, 2)
    Return()

    # Function_0_A4 end

    def Function_1_A8(): pass

    label("Function_1_A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C0")
    SetMapObjFrame(0xFF, "on_add", 0x0, 0x1)

    label("loc_C0")

    Return()

    # Function_1_A8 end

    def Function_2_C1(): pass

    label("Function_2_C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3")
    Call(0, 3)
    Jump("loc_1DE")

    label("loc_D3")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_13D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_15C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17B")
    SetChrPos(0x3, -900, 50, 800, 90)

    label("loc_17B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B9")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_1B9")

    SetChrPos(0x4, -900, 50, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_1DE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_256")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39B")

    label("loc_256")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "★[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39B")

    label("loc_2C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "★[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39B")

    label("loc_332")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "★[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(3, 0, 0x1)
    MenuCmd(3, 0, 0x2)
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39B")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_43F")

    label("loc_3C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FB")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_43F")

    label("loc_3FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_434")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_43F")

    label("loc_434")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_43F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_470"),
        (1, "loc_480"),
        (2, "loc_490"),
        (3, "loc_4A0"),
        (SWITCH_DEFAULT, "loc_4B0"),
    )


    label("loc_470")

    EventEnd(0x5)
    NewScene("t165B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4B0")

    label("loc_480")

    EventEnd(0x5)
    NewScene("t164B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4B0")

    label("loc_490")

    EventEnd(0x5)
    NewScene("t163B", 110, 0, 0)
    IdleLoop()
    Jump("loc_4B0")

    label("loc_4A0")

    EventEnd(0x5)
    NewScene("t162B", 117, 0, 0)
    IdleLoop()
    Jump("loc_4B0")

    label("loc_4B0")

    Jump("loc_52F")

    label("loc_4B5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D7"),
        (1, "loc_4ED"),
        (2, "loc_503"),
        (3, "loc_519"),
        (SWITCH_DEFAULT, "loc_52F"),
    )


    label("loc_4D7")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t165B", 117, 0, 0)
    IdleLoop()
    Jump("loc_52F")

    label("loc_4ED")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t164B", 117, 0, 0)
    IdleLoop()
    Jump("loc_52F")

    label("loc_503")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t163B", 110, 0, 0)
    IdleLoop()
    Jump("loc_52F")

    label("loc_519")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t162B", 117, 0, 0)
    IdleLoop()
    Jump("loc_52F")

    label("loc_52F")

    Return()

    # Function_2_C1 end

    def Function_3_530(): pass

    label("Function_3_530")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59A")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_59A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B9")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D8")
    SetChrPos(0x3, -900, 50, 800, 90)

    label("loc_5D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_5F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_616")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_616")

    SetChrPos(0x4, -900, 50, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Despite mashing the elevator buttons, nothing happens.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77A")

    ChrTalk(
        0x101,
        "#5100798V#0005F#6PIs it broken, maybe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5100799V#0203F#6PNo, that is not it. It appears that a locking\x01",
            "mechanism is in place.\x02\x03",
            "#5100800V#0200FWe will need some sort of authentication\x01",
            "card in order to release it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE6, 7)
    Jump("loc_7AD")

    label("loc_77A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's functions are locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7AD")

    Jump("loc_8D4")

    label("loc_7B2")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's functions are locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_846")

    ChrTalk(
        0x101,
        (
            "#5100801V#0000F#6P(Now, if we use the authentication card\x01",
            "we found earlier...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_846")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use Key Card\x01",      # 0
            "Cancel\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_894"),
        (1, "loc_8B6"),
        (SWITCH_DEFAULT, "loc_8D4"),
    )


    label("loc_894")

    Fade(250)
    SetMapObjFrame(0xFF, "on_add", 0x1, 0x1)
    Sound(72, 0, 100, 0)
    OP_0D()
    SetScenarioFlags(0xE3, 4)
    Jump("loc_8D4")

    label("loc_8B6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t162B", 0, 0, 0)
    IdleLoop()
    Jump("loc_8D4")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F7")
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    SetScenarioFlags(0x5C, 0)
    NewScene("t162B", 0, 0, 0)
    IdleLoop()

    label("loc_8F7")

    Return()

    # Function_3_530 end

    SaveToFile()

Try(main)
