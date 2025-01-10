from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0510.bin",                # FileName
        "c0510",                    # MapName
        "c0510",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0510",                  # 0
        "Garcia",                 # 1
        "Threatening Letter",     # 2
        "イス",                   # 3
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(89500,   0,       60500,   1200,    89500,   1000,    60500,   0x007C, 0,  3,  0x0000)
    DeclActor(176000,  0,       52000,   1200,    176000,  1000,    52000,   0x007C, 0,  4,  0x0000)
    DeclActor(7500,    0,       60700,   1500,    7800,    1700,    60700,   0x007C, 0,  14, 0x0000)
    DeclActor(-57000,  0,       1000,    1500,    -57000,  1500,    1500,    0x007C, 0,  19, 0x0000)
    DeclActor(52500,   0,       57400,   1500,    52500,   1300,    57400,   0x007C, 0,  21, 0x0000)
    DeclActor(136000,  0,       62000,   1500,    136000,  1500,    62000,   0x007C, 0,  24, 0x0000)
    DeclActor(600,     0,       66000,   1500,    600,     1500,    66200,   0x007C, 0,  26, 0x0000)
    DeclActor(50000,   0,       62110,   1500,    50000,   400,     62110,   0x007C, 0,  5,  0x0000)
    DeclActor(160500,  0,       2500,    1200,    160500,  1500,    2500,    0x007C, 0,  7,  0x0000)
    DeclActor(-51500,  0,       -3500,   1200,    -51500,  1500,    -3500,   0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_33C",          # 00, 0
        "Function_1_398",          # 01, 1
        "Function_2_534",          # 02, 2
        "Function_3_57C",          # 03, 3
        "Function_4_6D3",          # 04, 4
        "Function_5_819",          # 05, 5
        "Function_6_87A",          # 06, 6
        "Function_7_927",          # 07, 7
        "Function_8_A27",          # 08, 8
        "Function_9_B27",          # 09, 9
        "Function_10_2565",        # 0A, 10
        "Function_11_25DB",        # 0B, 11
        "Function_12_2657",        # 0C, 12
        "Function_13_4305",        # 0D, 13
        "Function_14_47D9",        # 0E, 14
        "Function_15_48BB",        # 0F, 15
        "Function_16_4922",        # 10, 16
        "Function_17_498A",        # 11, 17
        "Function_18_4D87",        # 12, 18
        "Function_19_5184",        # 13, 19
        "Function_20_52CB",        # 14, 20
        "Function_21_562A",        # 15, 21
        "Function_22_56FA",        # 16, 22
        "Function_23_5CEF",        # 17, 23
        "Function_24_6363",        # 18, 24
        "Function_25_6425",        # 19, 25
        "Function_26_6842",        # 1A, 26
        "Function_27_6850",        # 1B, 27
        "Function_28_6B1D",        # 1C, 28
    ))


    def Function_0_33C(): pass

    label("Function_0_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x0, 1)
    Event(0, 12)
    Jump("loc_374")

    label("loc_35A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_374")
    Event(0, 13)

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_383")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 9)

    label("loc_383")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397")
    OP_C7(0x0, 0x1000)

    label("loc_397")

    Return()

    # Function_0_33C end

    def Function_1_398(): pass

    label("Function_1_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3AD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_END)), "loc_3BA")
    OP_65(0x2, 0x1)

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3C7")
    OP_65(0x3, 0x1)

    label("loc_3C7")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    OP_66(0x4, 0x1)

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_END)), "loc_3EA")
    OP_65(0x5, 0x1)

    label("loc_3EA")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400")
    OP_66(0x6, 0x1)

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_END)), "loc_412")
    OP_70(0x8, 0xA)
    Jump("loc_416")

    label("loc_412")

    OP_70(0x8, 0x0)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F")
    SetMapObjFrame(0xFF, "key_red", 0x0, 0x1)

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449")
    SetMapObjFrame(0xFF, "key_blue", 0x0, 0x1)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_END)), "loc_45B")
    OP_70(0x2, 0x2D)
    Jump("loc_47C")

    label("loc_45B")

    OP_70(0x2, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, -1000, 55000, 3000, 3000, 0)

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_494")
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    Jump("loc_49E")

    label("loc_494")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_END)), "loc_4C3")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    SetMapObjFrame(0xFF, "key0b", 0x1, 0x1)
    Jump("loc_4DA")

    label("loc_4C3")

    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetMapObjFrame(0xFF, "key0b", 0x0, 0x1)

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_4F5")
    SetMapObjFrame(0xFF, "key0a", 0x0, 0x1)
    Jump("loc_502")

    label("loc_4F5")

    SetMapObjFrame(0xFF, "key0a", 0x1, 0x1)

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515")
    OP_70(0x1C, 0x0)
    Jump("loc_519")

    label("loc_515")

    OP_70(0x1C, 0x1E)

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C")
    OP_70(0x1D, 0x0)
    Jump("loc_530")

    label("loc_52C")

    OP_70(0x1D, 0x1E)

    label("loc_530")

    Call(0, 2)
    Return()

    # Function_1_398 end

    def Function_2_534(): pass

    label("Function_2_534")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")
    SetMapObjFlags(0x1C, 0x4)
    Jump("loc_553")

    label("loc_54D")

    ClearMapObjFlags(0x1C, 0x4)

    label("loc_553")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_575")
    SetMapObjFlags(0x1D, 0x4)
    Jump("loc_57B")

    label("loc_575")

    ClearMapObjFlags(0x1D, 0x4)

    label("loc_57B")

    Return()

    # Function_2_534 end

    def Function_3_57C(): pass

    label("Function_3_57C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_666")
    Sound(14, 0, 100, 0)
    OP_71(0x1C, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_5FC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_661")

    label("loc_5FC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1C, 0x1E, 0x0, 0x0, 0x0)

    label("loc_661")

    Jump("loc_6C7")

    label("loc_666")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey! Your Gnosis sticking in places it doesn't belong.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_57C end

    def Function_4_6D3(): pass

    label("Function_4_6D3")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BD")
    Sound(14, 0, 100, 0)
    OP_71(0x1D, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_753")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_7B8")

    label("loc_753")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1D, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7B8")

    Jump("loc_80D")

    label("loc_7BD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "New from Revache: Marconi and cheese!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_80D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6D3 end

    def Function_5_819(): pass

    label("Function_5_819")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F")
    Call(0, 6)
    Jump("loc_876")

    label("loc_82F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Cooking Encyclopedia is on the shelf.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_876")

    TalkEnd(0xFF)
    Return()

    # Function_5_819 end

    def Function_6_87A(): pass

    label("Function_6_87A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Cooking Encyclopedia is on the shelf.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1BB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xF)
    Return()

    # Function_6_87A end

    def Function_7_927(): pass

    label("Function_7_927")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1F, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1F, 0x0)
    OP_71(0x1F, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1F)
    OP_71(0x1F, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1F, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_A0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_A26")

    Return()

    # Function_7_927 end

    def Function_8_A27(): pass

    label("Function_8_A27")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0A")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x20, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x20, 0x0)
    OP_71(0x20, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x20)
    OP_71(0x20, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x20, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_B0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B26")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_B26")

    Return()

    # Function_8_A27 end

    def Function_9_B27(): pass

    label("Function_9_B27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50208.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    LoadChrToIndex("apl/ch50209.itc", 0x24)
    OP_68(610, 1000, 55220, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(25770, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2600, 100, 58900, 270)
    SetChrPos(0x102, 2600, 100, 57500, 270)
    SetChrPos(0x103, -2900, 100, 57500, 90)
    SetChrPos(0x104, -2900, 100, 58900, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -300, 0, 61300, 180)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 300, 59700, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_78(0x1E, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 61700, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Bold Voice")

    AnonymousTalk(
        0xFF,
        "#2100700VHaha... I wouldn't know.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(610, 1000, 59730, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(610, 1000, 59730, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19420, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2100701V#5P#3104FYou think the don sent Ilya Platiere\x01",
            "a threat letter?\x02\x03",
            "#2100702V#5P#3100FHah. That's nothing more than conjecture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100703V#0003F#12PWe aren't claiming it as the\x01",
            "truth, of course.\x02\x03",
            "#2100704V#0001FHowever, we heard of a quarrel that took place\x01",
            "recently, and given that we're out of leads...\x02\x03",
            "#2100705V...we figured we might as well come ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100706V#5P#3104FYou talking about the don getting smacked\x01",
            "across the face?\x02\x03",
            "#2100707V#3100FJust a trivial matter at a party he was attending.\x02\x03",
            "#2100708VThe don drank a bit too much alcohol,\x01",
            "so he has almost no recollection of it.\x02\x03",
            "#2100709VI doubt he's holding a grudge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100710V#0005F#12POh... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100711V#4P#0103FThis is just another rumor we heard...\x02\x03",
            "#2100712V#0100F...but what about the proposal to have Ilya\x01",
            "perform at the Heimdallr Opera House?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100713V#5P#3100FYeah, that discussion happened.\x02\x03",
            "#2100714VRevache has many powerful connections,\x01",
            "so they were trying to leverage the idea.\x02\x03",
            "#2100715V#3104FBut knowing the don, I'm sure it was just\x01",
            "a ruse to bring her in as a special guest\x01",
            "to our annual party...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100716V#0005F#12PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100717V#0205F#6P#NSpecial guest?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#2100718V#5P#3101FNothing you need to know about.\x02\x03",
            "#2100719V#3104FWell, there you have it. We've got\x01",
            "nothing to do with it.\x02\x03",
            "#2100720V#3100FDo you understand now, kiddos?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100741V#0003F#12P...\x02\x03",
            "#2100722V#0001FJust in case, do you mind taking\x01",
            "a look at the letter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100723V#5P#3100FHuh? Sure, whatever.\x02\x03",
            "#2100724VHand it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100725V#0001F#12PHere you go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd passed the threat letter to Garcia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    AnonymousTalk(
        0x8,
        (
            "#2100726V#5P#3101FHuh? The hell's up with this guy?\x02\x03",
            "#2100727VHe seems dead set on interrupting\x01",
            "Ilya Platiere's performance...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1853, 255, 100, 0)

    ChrTalk(
        0x8,
        "#2100728V#5P#3105F...?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2100729V#0001F#12P(What was that just now?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100730V#4P#0101F(He looked like he noticed something.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100731V#5P#3101F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Garcia threw the threat letter back at Lloyd.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#2100732V#5P#3104FHmph, this is idiotic.\x02\x03",
            "#2100733V#3100FThreat letter? This reads like nothing\x01",
            "more than an overblown prank to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100734V#0005F#12PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100735V#3P#0301FThe hell you sayin', pal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100736V#4P#0101FYour reaction gave the impression that\x01",
            "you know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100737V#5P#3104FAre you trying to imply something, missy?\x02\x03",
            "#2100738VNothing in that phony letter rang any bells.\x02\x03",
            "#2100739V#3100FI can confirm that the don didn't write it\x01",
            "at the very least.\x02\x03",
            "#2100740VYou guys are on a fool's errand, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100721V#0001F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100742V#3P#0301F(Damn. It's obvious as hell that he knows\x01",
            "more than he's lettin' on...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100743V#6P#0201F#N(There is a low probability he will\x01",
            "reveal any information.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#2100744V#0003F#12PI understand.\x02\x03",
            "#2100745V#0000FGarcia, is there any way we could hear\x01",
            "the story directly from the don?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2100746V#5P#3105FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100747V#3P#0304FOh, right! If ya don't mind, we'd like to\x01",
            "hear it directly from the horse's mouth.\x02\x03",
            "#2100748V#0300FOr is he not in right now?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sound(1857, 255, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    Sound(1855, 255, 100, 0)

    ChrTalk(
        0x8,
        "#2100749V#5P#3109F#4S#11AHAHA!\x02",
    )

    Sleep(1600)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_68(0, 1000, 60500, 500)
    SetCameraDistance(18000, 500)
    OP_6F(0x11)
    Sleep(300)
    SetChrSubChip(0x8, 0x1)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(818, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_68(430, 1000, 59740, 1000)
    SetCameraDistance(18500, 1000)
    Sleep(800)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x104, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_6F(0x11)
    CancelBlur(300)
    Sleep(300)

    ChrTalk(
        0x103,
        "#2100750V#6P#0210F#NUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100751V#4P#0110F...!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrPos(0x8, -300, 0, 61300, 180)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#2100752V#5P#3103FDon't go getting cocky now, kiddos!\x02\x03",
            "#2100753VYou think the don has time to see a bunch\x01",
            "of irrelevant cops like you?!\x02\x03",
            "#2100754V#3102FA group of naive and helpless puppies that\x01",
            "he can crush in the palm of his hand?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100755V#0007F#12PW-Wait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100756V#3P#0301FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100757V#5P#3104FI can't believe I even bothered to meet\x01",
            "with you punks.\x02\x03",
            "#2100758VI figured it was a good opportunity, so I'll\x01",
            "be gracious and give you a warning.\x02\x03",
            "#2100759V#3102FNo matter what you do, you can't change\x01",
            "Crossbell's true nature.\x02\x03",
            "#2100760VRevache's iron grip is here to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100761V#0013F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100762V#4P#0101F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100763V#3P#0301FAwfully arrogant, aren't ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100764V#5P#3103FIf you understand, then get the hell outta here!\x02\x03",
            "#2100765VI don't have time to sit around having tea parties\x01",
            "with a bunch of little shits like you!\x02\x03",
            "#2100766V#3101FHowever, if you dare defy us again...\x01",
            "There will be no mercy. I will end you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 2000, 0, 58900, 315)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#2100767V#12P#0003FThanks for the warning, Garcia.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2100768V#0001F#11PLet's go, everyone. I think we've\x01",
            "gotten all we could here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    ChrTalk(
        0x102,
        "#2100769V#4P#0103FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100770V#0203F#5PRoger.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100771V#0303FHah. You didn't even bother\x01",
            "servin' us any tea.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 2000, 0, 57500, 270)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -2000, 0, 57500, 90)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -2000, 0, 58900, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_68(0, 1000, 56400, 4000)
    BeginChrThread(0x102, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_2219():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2219)
    WaitChrThread(0x104, 1)

    def lambda_2237():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2237)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x104, 1)

    def lambda_226A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_226A)

    ChrTalk(
        0x8,
        (
            "#2100772V#3105FWait just a moment.\x02\x03",
            "#2100773VYou there. Redhead.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0x0, 0x190)
    Sleep(300)

    ChrTalk(
        0x104,
        "#2100774V#0301FHuh? You talkin' to me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100775V#3101FThat shade of red...\x01",
            "I've seen it before...\x02\x03",
            "#2100776VNo...you couldn't be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100777V#0306FWhoa, whoa. Hold on there, gramps.\x02\x03",
            "#2100778VI love to be courted by buxom ladies, but\x01",
            "old men on the other hand... Catch my drift?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2100779V#3104FHmph. Well, no matter.\x02\x03",
            "#2100780V#3100FYou're an eyesore, so get lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100781V#0301FMake up your damn mind. Weren't you\x01",
            "the one that stopped me, pal?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_24DE():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_24DE)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_2505():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2505)
    Sleep(500)
    OP_0D()
    WaitChrThread(0x104, 1)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_B27 end

    def Function_10_2565(): pass

    label("Function_10_2565")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_2571():
        OP_95(0xFE, 2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2571)
    WaitChrThread(0xFE, 1)

    def lambda_258F():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258F)
    WaitChrThread(0xFE, 1)

    def lambda_25AD():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25AD)
    Sleep(500)

    def lambda_25CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25CA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_2565 end

    def Function_11_25DB(): pass

    label("Function_11_25DB")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_25E7():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25E7)
    WaitChrThread(0xFE, 1)

    def lambda_2605():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2605)
    WaitChrThread(0xFE, 1)

    def lambda_2623():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2623)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_2646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2646)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_25DB end

    def Function_12_2657(): pass

    label("Function_12_2657")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50421.itc", 0x1E)
    AddParty(0x9, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_32(0x9, 0x0, 0x22)
    RemoveCraft(0x9, 0xFFFF)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x81, 0x2)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x2)
    OP_38(0x9, 0x85, 0x2)
    OP_38(0x9, 0x86, 0x2)
    OP_42(0x9, 0x451, 0xFF)
    OP_42(0x9, 0x5E9, 0xFF)
    OP_42(0x9, 0x64D, 0xFF)
    AddCraft(0x9, 0xF0)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF2)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0xF4)
    AddCraft(0x9, 0x127)
    SetChrChipPat(0x9, 0x6, 0x127)
    AddCraft(0x9, 0x147)
    OP_42(0x9, 0x81, 0x0)
    OP_42(0x9, 0xA3, 0x3)
    OP_42(0x9, 0x87, 0x4)
    OP_42(0x9, 0x69, 0x5)
    OP_42(0x9, 0x66, 0x6)
    OP_42(0x9, 0x6C, 0x2)
    OP_42(0x9, 0x7B, 0x1)
    OP_68(0, 1100, 4800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -200, 0, -500, 0)
    SetChrPos(0x102, 200, 0, -500, 0)
    SetChrPos(0x103, -200, 0, -500, 0)
    SetChrPos(0x104, 200, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 0, 30, 4800, 0)
    StopBGM(0x7D0)
    WaitBGM()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KSame day, 11AM\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7302", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(21000, 4000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(700)
    OP_93(0x10A, 0x10F, 0x1F4)
    Sleep(1000)
    OP_93(0x10A, 0x0, 0x1F4)
    OP_6F(0x10)

    ChrTalk(
        0x10A,
        (
            "#4300132V#0608F#11PDamn it...\x01",
            "What in the hell is going on?\x02\x03",
            "#4300133V#0610FThat damned Revache...\x01",
            "What's their objective?!\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_28CE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_28CE)
    OP_68(110, 1100, 3690, 2000)
    MoveCamera(45, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_2900():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2900)

    def lambda_2911():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2911)
    Sleep(400)

    def lambda_292E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_292E)

    def lambda_293F():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_293F)
    Sleep(400)

    def lambda_295C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_295C)

    def lambda_296D():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_296D)
    Sleep(400)

    def lambda_298A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_298A)

    def lambda_299B():
        OP_96(0xFE, 0x2BC, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_299B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    ChrTalk(
        0x10A,
        "#4300134V#5P#0605FY-You guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300135V#12P#0000FLooks like I was right. Dudley was waiting\x01",
            "for us inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300136V#0301F#12PYo, Glasses.\x01",
            "The hell's goin' on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300137V#5P#0607FHmph. I could have sworn I just told you\x01",
            "to mind your own damn business!\x02\x03",
            "#4300138VThe SSS should be solely focused\x01",
            "on the drug investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300139V#0106F#12PPardon me, but is this really the\x01",
            "time to be saying that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300140V#12P#0201FIt is as I surmised. No one is currently\x01",
            "present inside, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300141V#5P#0610FUgh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x10A,
        (
            "#4300142V#5P#0603FI've been staking this place out for a while,\x01",
            "but I haven't seen a single person leave.\x02\x03",
            "#4300143VNot only that, but there aren't signs of\x01",
            "a struggle having occurred.\x02\x03",
            "#4300144V#0610FIf anything, I'm the one who wants to\x01",
            "know what the hell is going on in here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300145V#12P#0001FIf I recall, the First Division was tasked with\x01",
            "surveying Revache's movements, right?\x02\x03",
            "#4300146VAre you saying you don't know when\x01",
            "all of their members disappeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300147V#5P#0608F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    ChrTalk(
        0x10A,
        (
            "#4300148V#5P#0603FLast night, HQ received a note warning\x01",
            "us of a criminal threat.\x02\x03",
            "#4300149VIt stated that Crossbell Airport\x01",
            "had been rigged with explosives.\x02",
        )
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
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#4300150V#12P#0011FE-Explosives?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300151V#0105F#12PAre you being serious right now?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300152V#5P#0603FThe First Division was ordered to\x01",
            "drop all of their duties at once and\x01",
            "secure the airport.\x02\x03",
            "#4300153V#0601FAs per the top brass' orders, anyone\x01",
            "responsible for observing Revache's\x01",
            "movements had to leave their posts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300154V#12P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300155V#0306F#12PSo basically, they snuck out after\x01",
            "the First Division withdrew?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300156V#12P#0203FHow oddly suspicious.\x02\x03",
            "#4300157V#0211FHow accurate was the situation\x01",
            "described by the warning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300158V#5P#0603FWho knows?\x02\x03",
            "#4300159V#0608FDamn, what the hell are\x01",
            "the top brass thinking?\x02\x03",
            "#4300160VFor how long do they intend to continue\x01",
            "trampling on the CPD's pride?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300161V#0108F#12PDetective Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300162V#12P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#4300163V#12P#0003FIn any case, it's hard to grasp\x01",
            "the truth of the situation with\x01",
            "our current information.\x02\x03",
            "#4300164V#0001FWhy don't we conduct an investigation\x01",
            "of the building?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10A,
        "#4300165V#5P#0607FWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300166V#12P#0006FOf course, I realize that there's a delicate\x01",
            "relationship between the police and\x01",
            "Revache, as things stand.\x02\x03",
            "#4300167VIf we investigate their headquarters,\x01",
            "especially without a search warrant,\x01",
            "it could give them reason to retaliate...\x02\x03",
            "#4300168V#0001FI'm fully aware of the risks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300169V#0108F#12PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300170V#5P#0610FWell, then, why the hell are you suggesting\x01",
            "such a foolhardy plan?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300171V#12P#0003FBecause there's a strong possibility the\x01",
            "situation will escalate anyway.\x02\x03",
            "#4300172V#0001FLet me give you a report on our findings\x01",
            "between yesterday and this morning.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained that the blue pills are a drug\x01",
            "that was possibly manufactured by a foul cult\x01",
            "annihilated six years ago...\x02\x03",
            "He also explained how the people who made\x01",
            "use of the drug disappeared all at once.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x10A,
        (
            "#4300173V#5P#0605FU-Unbelievable...\x02\x03",
            "#4300174VI was aware of the cult's existence,\x01",
            "but I thought they were gone for good...\x02\x03",
            "#4300175V#0608FWell, actually...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300176V#12P#0001FThere are innocent human lives\x01",
            "on the line.\x02\x03",
            "#4300177VVital information regarding the missing\x01",
            "people could be waiting inside here.\x02\x03",
            "#4300178V#0003FIf you can't take the risk, Dudley,\x01",
            "then could you at least let us--\x02\x03",
            "#4300179V#0013FNo. Do me a favor this one time.\x01",
            "I'll be acting of my own accord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300180V#5P#0605F...\x02",
    )

    CloseMessageWindow()

    def lambda_38D0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_38D0)
    Sleep(100)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#4300181V#0306F#11PWhoa there, buddy. Don't think I'll let you\x01",
            "shoulder the responsibility on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300182V#0100F#11PIt's only natural we'll stick together.\x02\x03",
            "#4300183VEven if the SSS is forced to disband,\x01",
            "this isn't a situation we can overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300184V#12P#0204FYes, we share this road until the end.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB3, 0x1F4)

    ChrTalk(
        0x101,
        "#4300185V#5P#0000FThat we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300186V#5P#0603FHmph. I've seen that burning heart before.\x02\x03",
            "#4300187V#0602FThat reckless abandon... It's just like his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300199V#5P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_3AF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AF0)
    Sleep(50)

    def lambda_3B00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3B00)
    Sleep(50)

    def lambda_3B10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3B10)
    WaitChrThread(0x101, 2)
    Sound(1555, 255, 100, 0)
    Sleep(800)
    SetChrFlags(0x10A, 0x20)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 0x1E)
    SetChrSubChip(0x10A, 0x0)
    Sleep(130)
    SetChrSubChip(0x10A, 0x1)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x10A, 0x2)
    Sleep(130)
    SetChrSubChip(0x10A, 0x3)
    Sleep(130)
    SetChrSubChip(0x10A, 0x4)
    Sleep(130)
    SetChrSubChip(0x10A, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x10A,
        (
            "#4300190V#5P#0611F...Evidence obtained without a search warrant\x01",
            "isn't legally recognized. Surely you know that.\x02\x03",
            "#4300191VWhatever evidence those guys might have left\x01",
            "behind, we'd have to pretend we didn't see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300192V#12P#0006FThat's...fine, I suppose.\x02\x03",
            "#4300193V#0008FOur top priority should be confirming\x01",
            "the situation in Crossbell right now.\x02\x03",
            "#4300194V#0013FWe refuse to stay in the dark any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300195V#5P#0611FHmph. Look at you, acting all grown up.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1556, 255, 100, 0)
    Sleep(500)
    SetChrSubChip(0x10A, 0x1)
    Sleep(100)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sleep(600)

    ChrTalk(
        0x10A,
        (
            "#4300197V#5P#0604FAs long as you understand the circumstances,\x01",
            "I won't be the one to stop you.\x02\x03",
            "#4300198V#0602FYou may tag along, but don't slow me down.\x02",
        )
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#4300188V#12P#0011F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300200V#0105F#12PExcuse me... You're coming with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300201V#5P#0603FGiven the circumstances, do you really\x01",
            "think I could leave everything to some\x01",
            "rookies like you?\x02\x03",
            "#4300202V#0601FFrom now on, this operation will be\x01",
            "under my command.\x02\x03",
            "#4300203V#0607FI'll be taking full responsibility.\x01",
            "No questions! Understood?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300204V#12P#0002FDudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300205V#0300F#12POh, lighten up, sunshine. Those glasses\x01",
            "ain't hiding your true feelings from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300206V#12P#0204FHis actions seem to indicate a caring\x01",
            "nature deep down, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x0, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x10A,
        (
            "#4300207V#11P#0603FWhy don't you two shut up?!\x02\x03",
            "#4300208V#0601FAnyway, we should proceed with\x01",
            "our search.\x02\x03",
            "#4300209VReport anything suspicious or out\x01",
            "of the ordinary to me ASAP!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300210V#12P#0000FYes, sir!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Detective Dudley has joined the party.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can add him to the active party in\x01",
            "the [TACTICS] menu.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_D5(0x1E)
    OP_68(0, 1280, 2000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 0, 0, 2000, 0)
    SetChrPos(0x1, 0, 0, 2000, 0)
    SetChrPos(0x2, 0, 0, 2000, 0)
    SetChrPos(0x3, 0, 0, 2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC4, 1)
    OP_29(0x4C, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_2657 end

    def Function_13_4305(): pass

    label("Function_13_4305")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1400, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x102, -700, 0, 52300, 0)
    SetChrPos(0x101, 700, 0, 52300, 0)
    SetChrPos(0x103, -1100, 0, 51400, 0)
    SetChrPos(0x104, 1100, 0, 51400, 0)
    SetChrPos(0x10A, 0, 0, 53700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 1500, 55000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(0, 900, 53000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#4300211V#0001FThis is the reception room we were in\x01",
            "before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300212V#0301FAin't this furniture pointlessly flashy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300213V#5P#0601FHmph. It's hard to picture evidence of\x01",
            "a crime waiting in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x103)
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        "#4300214V#0101FTio... Did you figure something out?\x02",
    )

    CloseMessageWindow()

    def lambda_454B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_454B)
    Sleep(50)

    def lambda_455B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_455B)
    Sleep(50)
    TurnDirection(0x10A, 0x103, 500)

    ChrTalk(
        0x103,
        (
            "#4300215V#12P#0206FYes. Something about this room\x01",
            "continues to feel off.\x02\x03",
            "#4300216V#0201FIt almost feels like this room is\x01",
            "a puzzle, waiting to be solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300217V#5P#0005FYou think there's a trick to this room?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300218V#5P#0601FCan you elaborate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300219V#12P#0208FI believe there is some sort of mechanical\x01",
            "gimmick in here...\x02\x03",
            "#4300220V#0206FSorry. It might just be my imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300221V#0300FHaha, an analysis by Tio Tot being\x01",
            "wrong? I wouldn't bet on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300222V#5P#0000FI'm inclined to trust Tio's gut...\x01",
            "Let's search this room a bit more.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 52000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 2)
    EventEnd(0x5)
    Return()

    # Function_13_4305 end

    def Function_14_47D9(): pass

    label("Function_14_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47EB")
    Call(0, 17)
    Jump("loc_48BA")

    label("loc_47EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4801")
    Call(0, 15)
    Jump("loc_48BA")

    label("loc_4801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4817")
    Call(0, 16)
    Jump("loc_48BA")

    label("loc_4817")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are two sockets aligned on the wall.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0000FIf there are keyholes here, then there should\x01",
            "be keys hidden somewhere.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_48BA")

    Return()

    # Function_14_47D9 end

    def Function_15_48BB(): pass

    label("Function_15_48BB")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Carnelia key inserted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32E, 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_red", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_491F")
    Call(0, 18)
    Jump("loc_4921")

    label("loc_491F")

    EventEnd(0x3)

    label("loc_4921")

    Return()

    # Function_15_48BB end

    def Function_16_4922(): pass

    label("Function_16_4922")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Sapphirl key inserted.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32C, 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_blue", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4987")
    Call(0, 18)
    Jump("loc_4989")

    label("loc_4987")

    EventEnd(0x3)

    label("loc_4989")

    Return()

    # Function_16_4922 end

    def Function_17_498A(): pass

    label("Function_17_498A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 6700, 0, 60800, 90)
    SetChrPos(0x102, 5100, 30, 61000, 90)
    SetChrPos(0x103, 5100, 30, 60000, 90)
    SetChrPos(0x104, 5800, 0, 62000, 135)
    SetChrPos(0x10A, 6700, 0, 59100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#4300223V#0005FHmm, this picture frame...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300224V#12P#0601FHmph...I thought it fishy, as well.\x02\x03",
            "#4300225VLet's take a closer look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300226V#0001FRight.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(141, 0, 100, 0)
    Sleep(500)
    OP_74(0x8, 0xF)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_79(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#4300227V#6P#0105FOh, wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300228V#0304F#6PTio Tot's sixth sense saves the day!\x02\x03",
            "#4300229V#0305FThose two lil' guys definitely\x01",
            "look like keyholes to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300230V#6P#0203FThe question remains, where\x01",
            "are the respective keys?\x02\x03",
            "#4300231V#0202FIt is likely something will happen\x01",
            "after both sides are released.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D12")

    ChrTalk(
        0x101,
        (
            "#4300232V#0000F#5PAll right...\x01",
            "(Let's try the keys we found before.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D5D")

    label("loc_4D12")


    ChrTalk(
        0x101,
        (
            "#4300233V#0000F#5PAll right...\x01",
            "Let's give it a try when we find them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D5D")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6400, 0, 60800, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 3)
    OP_29(0x4C, 0x1, 0xE)
    EventEnd(0x5)
    Return()

    # Function_17_498A end

    def Function_18_4D87(): pass

    label("Function_18_4D87")

    EventBegin(0x0)
    Fade(1000)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 6700, 0, 60800, 90)
    SetChrPos(0x102, 5100, 30, 61000, 90)
    SetChrPos(0x103, 5100, 30, 60000, 90)
    SetChrPos(0x104, 5800, 0, 62000, 135)
    SetChrPos(0x10A, 6700, 0, 59100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_68(0, 1200, 57000, 1500)

    def lambda_4E3B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E3B)
    Sleep(50)

    def lambda_4E4B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4E4B)

    def lambda_4E58():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4E58)
    Sleep(50)

    def lambda_4E68():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E68)

    def lambda_4E75():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4E75)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x0, 0x2D, 0x0, 0x0)
    Sleep(2500)
    Sound(149, 0, 100, 0)
    OP_24(0x9B)
    OP_79(0x2)
    SetBarrier(0x2, 0x0, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#4300353V#5P#0105FT-To think that they created such a\x01",
            "device for just one room...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300354V#0006F#5PThat cluster of footprints leads me to\x01",
            "believe that room is used frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300355V#0603F#11PHmph, so Marconi has his own little\x01",
            "secret hideout, does he?\x02\x03",
            "#4300356V#0601FThis can only mean one thing: His\x01",
            "private quarters are further inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300357V#0303F#5PNow that you mention it, we haven't seen\x01",
            "the head honcho's office yet, have we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300358V#5P#0201FI am of the opinion that more clues\x01",
            "will turn up further in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300359V#0001F#5PAll right... Let's try going down, everyone.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6400, 0, 60800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0xC6, 0)
    OP_29(0x4C, 0x1, 0x19)
    EventEnd(0x5)
    Return()

    # Function_18_4D87 end

    def Function_19_5184(): pass

    label("Function_19_5184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5196")
    Call(0, 20)
    Jump("loc_52CA")

    label("loc_5196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_51A7")
    Call(0, 23)
    Jump("loc_52CA")

    label("loc_51A7")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a panel on the wall. It appears\x01",
            "to be a device that requires a password.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#0603FIt doesn't look like it'll open unless we\x01",
            "have the correct password.\x02\x03",
            "#0601FThere should be a clue somewhere...\x01",
            "Let's try inspecting the inside of the\x01",
            "building!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_52CA")

    Return()

    # Function_19_5184 end

    def Function_20_52CB(): pass

    label("Function_20_52CB")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57000, 1000, 700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -57000, 0, 700, 0)
    SetChrPos(0x102, -57000, 0, -1000, 0)
    SetChrPos(0x103, -58000, 0, -1400, 0)
    SetChrPos(0x104, -56000, 0, -1400, 0)
    SetChrPos(0x10A, -55700, 0, 700, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#4300234V#11P#0005FWhat is this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300235V#12P#0101FIt's...some kind of panel that\x01",
            "you can input letters into?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300236V#12P#0203FI believe this is a password-operated\x01",
            "device.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_5438():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5438)
    OP_6F(0x1)

    ChrTalk(
        0x103,
        (
            "#4300237V#11P#0202FThere seems to be some sort of iron\x01",
            "grate, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_548F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_548F)
    Sleep(50)

    def lambda_549F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_549F)
    Sleep(50)

    def lambda_54AF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_54AF)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#4300238V#0306FSomethin' about this isn't sittin' right\x01",
            "with me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300239V#0603F#11P#NIt doesn't look like it'll open unless we\x01",
            "have the correct password.\x02\x03",
            "#4300240V#0608FSurely someone's left a note behind\x01",
            "in case people forgot it.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#4300241V#0000F#11P#NA likely scenario... Let's try searching\x01",
            "for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -57000, 0, 400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0xC4, 4)
    EventEnd(0x5)
    Return()

    # Function_20_52CB end

    def Function_21_562A(): pass

    label("Function_21_562A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563C")
    Call(0, 22)
    Jump("loc_56F9")

    label("loc_563C")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a piece of paper stuck among\x01",
            "the swimsuit magazine's pages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "The title and author of the most\x01",
            "popular fairy tale at the library.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_56F9")

    Return()

    # Function_21_562A end

    def Function_22_56FA(): pass

    label("Function_22_56FA")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53720, 1200, 58520, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19480, 0)
    SetChrPos(0x101, 53900, 0, 59300, 225)
    SetChrPos(0x102, 53400, 0, 60300, 180)
    SetChrPos(0x103, 52400, 0, 60300, 180)
    SetChrPos(0x104, 53900, 0, 58200, 270)
    SetChrPos(0x10A, 54500, 0, 57200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A swimsuit magazine is sitting on the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#4300242V#5P#0005FThis looks like a magazine some of\x01",
            "the underlings were probably reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300243V#11P#0302FOh, damn! It's the newest issue of Hot Shot!\x01",
            "I haven't been able to pick up my copy yet.\x02\x03",
            "#4300244V#0309F*flip*...*flip*...\x01",
            "My, aren't you ladies smokin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300245V#5P#0111FRandy...you lecherous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300246V#0206F#5PI do not know what else you were\x01",
            "expecting from Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#4300247V#0606F#11PSheesh. Kids these days.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#4300248V#5P#0005FHold on a second...\x02\x03",
            "#4300249V#0001FWasn't there something stuck between\x01",
            "the pages a second ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300250V#11P#0301FHuh, what now?\x02\x03",
            "#4300251V#0305FOh. You're right.\x01",
            "There's some kinda memo stuck in here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a piece of paper stuck among\x01",
            "the swimsuit magazine's pages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "The title and author of the most\x01",
            "popular fairy tale at the library.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x10A)

    ChrTalk(
        0x102,
        "#4300252V#5P#0101FThis must be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300253V#0201F#5P...the password for the device earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300254V#0604F#11PHmm...\x01",
            "Indeed, it looks like it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300255V#5P#0000FAll right, let's go and try to crack the\x01",
            "password on the input device, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 54200, 30, 58200, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 5)
    OP_29(0x4C, 0x1, 0xF)
    EventEnd(0x5)
    Return()

    # Function_22_56FA end

    def Function_23_5CEF(): pass

    label("Function_23_5CEF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57000, 1000, 700, 0)
    MoveCamera(34, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -57000, 0, 700, 0)
    SetChrPos(0x102, -57000, 0, -1000, 0)
    SetChrPos(0x103, -58000, 0, -1400, 0)
    SetChrPos(0x104, -56000, 0, -1400, 0)
    SetChrPos(0x10A, -55700, 0, 700, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 8, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KPlease enter the two\x01",
            "passwords in order.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Lene and the Seven Little Dragons\x01",          # 0
            "The Story of Queen Charon\x01",                  # 1
            "Wanderer Aluze's Notebook\x01",                  # 2
            "Mark and the Witch of the Deep Forest\x01",      # 3
            "Riddell's Fairy Tales\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E86")
    ClearScenarioFlags(0x0, 0)

    label("loc_5E86")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Ali Bey\x01",            # 0
            "Shawn Arnham\x01",       # 1
            "Yoko Asshimar\x01",      # 2
            "Amanita Heim\x01",       # 3
            "Rachel Bran\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EE6")
    ClearScenarioFlags(0x0, 0)

    label("loc_5EE6")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_633C")
    Sound(87, 0, 100, 0)
    Sleep(300)
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_5F1B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F1B)
    Sleep(50)

    def lambda_5F2B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5F2B)
    Sleep(50)

    def lambda_5F3B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5F3B)
    Sleep(50)

    def lambda_5F4B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5F4B)
    Sleep(50)

    def lambda_5F5B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5F5B)
    OP_6F(0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(143, 0, 100, 0)
    Sleep(300)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-57000, 1000, 700, 2000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#4300256V#0000F#11PThere we go...\x01",
            "Looks like we hit the jackpot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300257V#11P#0102FDespite the elaborate mechanism,\x01",
            "they were a little too careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300258V#0306F#11PYeah, pretty sloppy of 'em to stick precious\x01",
            "info inside a swimsuit magazine.\x02\x03",
            "#4300259V#0301FI mean, wouldn't that be the first\x01",
            "thing intruders would go for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300260V#11P#0206FI do not think normal intruders would\x01",
            "immediately aim for a swimsuit magazine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300261V#11P#0604FWell, no matter how great the security system is,\x01",
            "it's useless if the users are all this incompetent.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#4300262V#5P#0600FLet's continue. It looks like there's something\x01",
            "up ahead.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62D0():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62D0)
    Sleep(150)

    def lambda_62E0():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62E0)
    Sleep(50)

    def lambda_62F0():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_62F0)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    ChrTalk(
        0x101,
        "#4300263V#6P#0000FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0xC4, 6)
    OP_29(0x4C, 0x1, 0x10)
    Jump("loc_6345")

    label("loc_633C")

    Sound(3, 0, 100, 0)
    Sleep(300)

    label("loc_6345")

    SetChrPos(0x0, -57000, 0, 400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_5CEF end

    def Function_24_6363(): pass

    label("Function_24_6363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6375")
    Call(0, 25)
    Jump("loc_6424")

    label("loc_6375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638B")
    Call(0, 28)
    Jump("loc_6424")

    label("loc_638B")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "An unnatural-looking gap is in the bookshelf.\x01",
            "It appears that a pressure-sensitive mechanism\x01",
            "has been hidden there.\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_6424")

    Return()

    # Function_24_6363 end

    def Function_25_6425(): pass

    label("Function_25_6425")

    EventBegin(0x0)
    Fade(1000)
    OP_68(135600, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 136300, 0, 60700, 0)
    SetChrPos(0x102, 135300, 0, 59400, 0)
    SetChrPos(0x103, 135300, 0, 60700, 0)
    SetChrPos(0x104, 136300, 0, 59400, 0)
    SetChrPos(0x10A, 137800, 0, 60000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#4300294V#0005F#12PHmm?\x02\x03",
            "#4300295V#0001FWhat's with this odd-looking gap?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300296V#12P#0105FDo you think someone may have borrowed\x01",
            "the book that was originally sitting there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300297V#6P#0201FNo...\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#4300298V#6P#0203FThere is a pressure-sensitive device\x01",
            "resting under it.\x02\x03",
            "#4300299V#0200FThe mechanism will probably release if we\x01",
            "put an object with a specific weight on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#4300300V#12P#0306FDamn, man...\x01",
            "We in some kinda spy novel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#4300301V#0603F#12PThe people running this place seem\x01",
            "fond of security tricks.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#4300302V#0601F#11PI'm sure this'll be easy enough. It's time to\x01",
            "investigate the building for any objects that\x01",
            "fit the bill!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#4300303V#5P#0000FUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 136300, 0, 60400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x6, 0x1)
    SetScenarioFlags(0xC5, 2)
    OP_29(0x4C, 0x1, 0x13)
    EventEnd(0x5)
    Return()

    # Function_25_6425 end

    def Function_26_6842(): pass

    label("Function_26_6842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684F")
    Call(0, 27)

    label("loc_684F")

    Return()

    # Function_26_6842 end

    def Function_27_6850(): pass

    label("Function_27_6850")

    EventBegin(0x0)
    Fade(1000)
    OP_68(200, 1200, 65200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 600, 0, 64700, 0)
    SetChrPos(0x102, -400, 0, 64700, 0)
    SetChrPos(0x103, -400, 30, 63500, 0)
    SetChrPos(0x104, 600, 30, 63500, 0)
    SetChrPos(0x10A, 1900, 0, 64000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a golden pedestal.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A10")

    ChrTalk(
        0x101,
        "#4300304V#0005F#11PIs this pedestal made of solid gold?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300305V#12P#0101FNo, I believe it's only gold-plated.\x02\x03",
            "#4300306V#0103FConsidering how rich they are, I wouldn't\x01",
            "put it past them to have a real one sitting\x01",
            "around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A10")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Take the pedestal with you.]\x01",      # 0
            "[Leave it where it is.]\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A80"),
        (1, "loc_6AF7"),
        (SWITCH_DEFAULT, "loc_6AFC"),
    )


    label("loc_6A80")

    Fade(500)
    SetMapObjFrame(0xFF, "key0a", 0x0, 0x1)
    Sound(51, 0, 100, 0)
    Sleep(100)
    Sound(50, 0, 100, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x32D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32D, 1)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0xC6, 5)
    Jump("loc_6AFC")

    label("loc_6AF7")

    Jump("loc_6AFC")

    label("loc_6AFC")

    SetScenarioFlags(0xC5, 3)
    SetChrPos(0x0, 200, 0, 64400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_6850 end

    def Function_28_6B1D(): pass

    label("Function_28_6B1D")

    EventBegin(0x0)
    Fade(1000)
    OP_68(135600, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 136300, 0, 60700, 0)
    SetChrPos(0x102, 135300, 0, 59400, 0)
    SetChrPos(0x103, 135300, 0, 60700, 0)
    SetChrPos(0x104, 136300, 0, 59400, 0)
    SetChrPos(0x10A, 137800, 0, 60000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SubItemNumber(0x32D, 1)
    Fade(500)
    SetMapObjFrame(0xFF, "key0b", 0x1, 0x1)
    Sound(51, 0, 100, 0)
    Sleep(100)
    Sound(50, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(141600, 1200, 60700, 1500)
    MoveCamera(45, 30, 0, 1500)
    OP_6F(0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(155, 2, 100, 0)

    def lambda_6C26():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C26)
    Sleep(50)

    def lambda_6C36():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6C36)

    def lambda_6C43():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C43)
    Sleep(50)

    def lambda_6C53():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C53)

    def lambda_6C60():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6C60)
    OP_79(0x0)
    Sound(149, 0, 100, 0)
    OP_24(0x9B)
    Sleep(500)
    Fade(500)
    OP_68(136170, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18910, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#4300307V#5P#0000FAll right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300308V#6P#0306FStill, though. Kinda weird choice for\x01",
            "a security mechanism, don'tcha think?\x02\x03",
            "#4300309V#0301FCoulda just used a key...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300310V#6P#0211FAdding to that, this device appears to\x01",
            "have cost an obscene amount of mira.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)

    ChrTalk(
        0x10A,
        (
            "#4300311V#0603F#11PPerhaps it's Marconi's personal tastes...\x02\x03",
            "#4300312V#0600FI've heard rumors that he's an avid\x01",
            "fan of new toys and odd novelties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300313V#6P#0106FI'm sure that proves a hassle for\x01",
            "the people working under him...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 136300, 0, 60400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x5, 0x1)
    SetScenarioFlags(0xC5, 4)
    OP_29(0x4C, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_28_6B1D end

    SaveToFile()

Try(main)
