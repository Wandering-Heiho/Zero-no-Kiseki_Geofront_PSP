from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1610.bin",                # FileName
        "t1610",                    # MapName
        "t1610",                    # Location
        0x0054,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 84, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1610",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_A4",           # 01, 1
        "Function_2_A5",           # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    Event(0, 2)
    Return()

    # Function_0_A0 end

    def Function_1_A4(): pass

    label("Function_1_A4")

    Return()

    # Function_1_A4 end

    def Function_2_A5(): pass

    label("Function_2_A5")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 1500, 50, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F")
    SetChrPos(0x1, 300, 50, 800, 90)

    label("loc_10F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E")
    SetChrPos(0x2, 300, 50, -800, 90)

    label("loc_12E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D")
    SetChrPos(0x3, -900, 50, 0, 90)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C")
    SetChrPos(0x4, -2100, 0, -800, 90)

    label("loc_16C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B")
    SetChrPos(0x5, -2100, 0, 800, 90)

    label("loc_18B")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "★[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_332")

    label("loc_205")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "★[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_332")

    label("loc_26B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "★[ 2F ]")
    MenuCmd(1, 0, "　[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_332")

    label("loc_2D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "　[ 4F ]")
    MenuCmd(1, 0, "　[ 3F ]")
    MenuCmd(1, 0, "　[ 2F ]")
    MenuCmd(1, 0, "★[ 1F ]")
    MenuCmd(1, 0, "　[Cancel]")
    MenuCmd(2, 0, 10, 10, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_332")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_3D6")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_392")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3D6")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CB")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(0, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3D6")

    label("loc_3CB")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_3D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_407"),
        (1, "loc_417"),
        (2, "loc_427"),
        (3, "loc_437"),
        (SWITCH_DEFAULT, "loc_447"),
    )


    label("loc_407")

    EventEnd(0x5)
    NewScene("t1650", 117, 0, 0)
    IdleLoop()
    Jump("loc_447")

    label("loc_417")

    EventEnd(0x5)
    NewScene("t1640", 117, 0, 0)
    IdleLoop()
    Jump("loc_447")

    label("loc_427")

    EventEnd(0x5)
    NewScene("t1630", 110, 0, 0)
    IdleLoop()
    Jump("loc_447")

    label("loc_437")

    EventEnd(0x5)
    NewScene("t1620", 117, 0, 0)
    IdleLoop()
    Jump("loc_447")

    label("loc_447")

    Jump("loc_4D2")

    label("loc_44C")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46E"),
        (1, "loc_487"),
        (2, "loc_4A0"),
        (3, "loc_4B9"),
        (SWITCH_DEFAULT, "loc_4D2"),
    )


    label("loc_46E")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1650", 117, 0, 0)
    IdleLoop()
    Jump("loc_4D2")

    label("loc_487")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1640", 117, 0, 0)
    IdleLoop()
    Jump("loc_4D2")

    label("loc_4A0")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1630", 110, 0, 0)
    IdleLoop()
    Jump("loc_4D2")

    label("loc_4B9")

    Sound(160, 0, 100, 0)
    Sleep(500)
    EventEnd(0x5)
    NewScene("t1620", 117, 0, 0)
    IdleLoop()
    Jump("loc_4D2")

    label("loc_4D2")

    Return()

    # Function_2_A5 end

    SaveToFile()

Try(main)
