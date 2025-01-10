from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3001.bin",                # FileName
        "m3001",                    # MapName
        "m3001",                    # Location
        0x007B,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 19000, -24000, 48000, 0, 0, 1, 123, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3001",                  # 0
    ))

    DeclActor(-176250, -125000, 7500,    2000,    -176500, -123600, 7500,    0x007C, 0,  3,  0x0000)
    DeclActor(-176250, -125000, -7500,   2000,    -176500, -123600, -7500,   0x007C, 0,  4,  0x0000)
    DeclActor(-150000, -128000, 4000,    1200,    -150000, -126500, 4000,    0x007C, 0,  2,  0x0000)

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_119",          # 01, 1
        "Function_2_1C1",          # 02, 2
        "Function_3_2C1",          # 03, 3
        "Function_4_3F7",          # 04, 4
        "Function_5_51E",          # 05, 5
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    Return()

    # Function_0_118 end

    def Function_1_119(): pass

    label("Function_1_119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_END)), "loc_12B")
    OP_70(0xD, 0x1E)
    Jump("loc_12F")

    label("loc_12B")

    OP_70(0xD, 0x0)

    label("loc_12F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_END)), "loc_141")
    OP_70(0xE, 0x1E)
    Jump("loc_145")

    label("loc_141")

    OP_70(0xE, 0x0)

    label("loc_145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_161")
    OP_70(0xC, 0x62)
    ClearMapObjFlags(0xC, 0x2)
    Jump("loc_189")

    label("loc_161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17F")
    OP_70(0xC, 0x0)
    SetMapObjFlags(0xC, 0x2)
    Jump("loc_189")

    label("loc_17F")

    OP_70(0xC, 0x32)
    SetMapObjFlags(0xC, 0x2)

    label("loc_189")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BD")
    Sound(129, 1, 100, 0)
    Jump("loc_1C0")

    label("loc_1BD")

    OP_24(0x81)

    label("loc_1C0")

    Return()

    # Function_1_119 end

    def Function_2_1C1(): pass

    label("Function_2_1C1")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xF, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xF, 0x0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xF)
    OP_71(0xF, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0xF, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C0")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C0")

    Return()

    # Function_2_1C1 end

    def Function_3_2C1(): pass

    label("Function_3_2C1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_END)), "loc_30E")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever cannot be moved anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3F6")

    label("loc_30E")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Move it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EF")
    Fade(500)
    SetChrPos(0x0, -177540, -125000, 7320, 89)
    SetChrPos(0x1, -179090, -125000, 8210, 89)
    SetChrPos(0x2, -179330, -125000, 5940, 89)
    SetChrPos(0x3, -180460, -125000, 6800, 89)
    OP_68(-176830, -124000, 7360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xD)
    Sleep(500)
    SetScenarioFlags(0xF4, 2)
    Call(0, 5)

    label("loc_3EF")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3F6")

    Return()

    # Function_3_2C1 end

    def Function_4_3F7(): pass

    label("Function_4_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_END)), "loc_43A")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The lever cannot be moved anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_51D")

    label("loc_43A")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lever.\x01",
            "Move it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B")
    Fade(500)
    SetChrPos(0x0, -177400, -125000, -7380, 89)
    SetChrPos(0x1, -179030, -125000, -6250, 89)
    SetChrPos(0x2, -179260, -125000, -8750, 89)
    SetChrPos(0x3, -180450, -125000, -7750, 89)
    OP_68(-177030, -124000, -6650, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xE)
    Sleep(500)
    SetScenarioFlags(0xF4, 3)
    Call(0, 5)

    label("loc_51B")

    EventEnd(0x5)

    label("loc_51D")

    Return()

    # Function_4_3F7 end

    def Function_5_51E(): pass

    label("Function_5_51E")

    Fade(500)
    OP_68(-177510, -127000, 1020, 0)
    MoveCamera(45, 44, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59C")
    Sound(155, 2, 100, 0)
    OP_71(0xC, 0x32, 0x62, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x2)
    OP_79(0xC)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Jump("loc_5D4")

    label("loc_59C")

    Sound(155, 2, 100, 0)
    OP_71(0xC, 0x0, 0x32, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x2)
    Sleep(800)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    OP_79(0xC)

    label("loc_5D4")

    Sleep(1000)
    Return()

    # Function_5_51E end

    SaveToFile()

Try(main)
