from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2000.bin",                # FileName
        "r2000",                    # MapName
        "r2000",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2000", "r0000_1", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -60, 1060, 3730, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2000",                  # 0
        "Harold's Car",           # 1
        "Bus",                    # 2
        "車",                     # 3
        "SE制御",                 # 4
        "To Crossbell City",      # 5
        "To Crossbell Cathedral", # 6
        "To Mainz Mining Village",# 7
    ))

    DeclNpc(8430,    0,       33990,   225,  197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 10,  0.0,                   7.0,                   -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.0,                  -2.3333334922790527,   0.20000001788139343,   1.0])

    DeclActor(11200,   0,       16200,   1500,    11200,   1500,    16200,   0x007C, 0,  8,  0x0000)
    DeclActor(-700,    0,       19910,   1800,    -700,    2000,    19910,   0x007C, 0,  9,  0x0000)
    DeclActor(-16960,  -2000,   50350,   1200,    -16960,  -2000,   50350,   0x007C, 0,  2,  0x0000)
    DeclActor(4200,    0,       36290,   2500,    4200,    1700,    36290,   0x007C, 0,  16, 0x0000)

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "To Crossbell City")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "To Crossbell Cathedral")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "To Mainz Mining Village")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")
    PlaceName(-1.0, 0.0, 19.5, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_2A0",          # 00, 0
        "Function_1_56D",          # 01, 1
        "Function_2_753",          # 02, 2
        "Function_3_767",          # 03, 3
        "Function_4_826",          # 04, 4
        "Function_5_948",          # 05, 5
        "Function_6_9DD",          # 06, 6
        "Function_7_FB6",          # 07, 7
        "Function_8_10A5",         # 08, 8
        "Function_9_132D",         # 09, 9
        "Function_10_1368",        # 0A, 10
        "Function_11_1FB9",        # 0B, 11
        "Function_12_1FFC",        # 0C, 12
        "Function_13_2AB9",        # 0D, 13
        "Function_14_2C43",        # 0E, 14
        "Function_15_2DA4",        # 0F, 15
        "Function_16_2E85",        # 10, 16
        "Function_17_2F16",        # 11, 17
    ))


    def Function_0_2A0(): pass

    label("Function_0_2A0")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 6)
    SetScenarioFlags(0xFB, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 13)

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2CD")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 5)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_2E5")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_2E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56C")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    SetScenarioFlags(0x7A, 0)

    label("loc_34B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    SetScenarioFlags(0x7A, 1)

    label("loc_361")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377")
    SetScenarioFlags(0x7A, 2)

    label("loc_377")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D")
    SetScenarioFlags(0x7A, 3)

    label("loc_38D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    SetScenarioFlags(0x7A, 4)

    label("loc_3A3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9")
    SetScenarioFlags(0x7A, 5)

    label("loc_3B9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    SetScenarioFlags(0x7A, 6)

    label("loc_3CF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    SetScenarioFlags(0x7A, 7)

    label("loc_3E5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")
    SetScenarioFlags(0x7B, 0)

    label("loc_3FB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    SetScenarioFlags(0x7B, 1)

    label("loc_411")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427")
    SetScenarioFlags(0x7B, 2)

    label("loc_427")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    SetScenarioFlags(0x7B, 3)

    label("loc_43D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_453")
    SetScenarioFlags(0x7B, 4)

    label("loc_453")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    SetScenarioFlags(0x7B, 5)

    label("loc_469")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47F")
    SetScenarioFlags(0x7B, 6)

    label("loc_47F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    SetScenarioFlags(0x7B, 7)

    label("loc_495")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_56C")

    label("loc_4D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_56C")

    label("loc_4E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_56C")

    label("loc_4FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_56C")

    label("loc_515")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52C")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_56C")

    label("loc_52C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_56C")

    label("loc_543")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_56C")

    label("loc_55A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    SetScenarioFlags(0x7C, 7)

    label("loc_56C")

    Return()

    # Function_0_2A0 end

    def Function_1_56D(): pass

    label("Function_1_56D")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_585")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_585")

    SetMapObjFlags(0x1, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    OP_66(0x1, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    OP_78(0x1, 0xA)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    SetChrPos(0xA, -1120, 0, 19360, 315)
    OP_D3(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    Jump("loc_60C")

    label("loc_607")

    OP_16(0x3, 0x4, 0x1, 0x0)

    label("loc_60C")

    OP_78(0x2, 0x8)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_653")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_653")
    ClearMapObjFlags(0x2, 0x4)
    OP_D3(0x8, 0x0, 0x36EE8, 0x0, 0x0)

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    Event(0, 15)

    label("loc_669")

    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_693")

    label("loc_68D")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6CA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)

    label("loc_6CA")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_727")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -16960, -2000, 50350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)

    label("loc_727")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_73F")
    OP_1B(0x2, 0x0, 0x11)
    Jump("loc_752")

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_752")
    OP_1B(0x2, 0x0, 0x11)

    label("loc_752")

    Return()

    # Function_1_56D end

    def Function_2_753(): pass

    label("Function_2_753")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_2_753 end

    def Function_3_767(): pass

    label("Function_3_767")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mainz Mining Village\x01",        # 0
            "Bus Stop (Doll Studio)\x01",      # 1
            "Leave\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FE")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_81E")

    label("loc_7FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    Call(0, 4)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_81E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_767 end

    def Function_4_826(): pass

    label("Function_4_826")

    Fade(1000)
    OP_68(10010, 600, 21560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 10190, 0, 16230, 0)
    SetChrPos(0x1, 9210, 0, 16200, 0)
    SetChrPos(0x2, 8170, 0, 16290, 0)
    SetChrPos(0x3, 7240, 0, 16350, 0)
    ClearChrFlags(0x9, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x9)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x9, -40, 0, 30670, 105)
    OP_D3(0x9, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_901():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_901)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x9, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_4_826 end

    def Function_5_948(): pass

    label("Function_5_948")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 10030, 0, 16580, 0)
    SetChrPos(0x1, 10030, 0, 16580, 0)
    SetChrPos(0x2, 10030, 0, 16580, 0)
    SetChrPos(0x3, 10030, 0, 16580, 0)
    OP_68(10030, 600, 16580, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_5_948 end

    def Function_6_9DD(): pass

    label("Function_6_9DD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAE")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4B")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A83")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_A9E")

    label("loc_A83")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACC")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_AE2")

    label("loc_ACC")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B10")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_B26")

    label("loc_B10")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_B26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B55")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_B6C")

    label("loc_B55")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_B6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9B")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_BB2")

    label("loc_B9B")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_BB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_BEE")

    label("loc_BDC")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_BEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1A")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_C2E")

    label("loc_C1A")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C66")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_C86")

    label("loc_C66")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB4")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_CCA")

    label("loc_CB4")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_CCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFC")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_D16")

    label("loc_CFC")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_D16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D50")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_D72")

    label("loc_D50")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_D72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA1")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_DB8")

    label("loc_DA1")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_DB8")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3C")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x1)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E8F"),
        (1, "loc_E9D"),
        (2, "loc_EAB"),
        (3, "loc_EB9"),
        (4, "loc_EC7"),
        (5, "loc_ED5"),
        (6, "loc_EE3"),
        (7, "loc_EF1"),
        (8, "loc_EFF"),
        (9, "loc_F0D"),
        (10, "loc_F1B"),
        (11, "loc_F29"),
        (SWITCH_DEFAULT, "loc_F37"),
    )


    label("loc_E8F")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_E9D")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EAB")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EB9")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EC7")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_ED5")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EE3")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EF1")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_EFF")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_F0D")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_F1B")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_F29")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F37")

    label("loc_F37")

    Jump("loc_F46")

    label("loc_F3C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F46")

    Jump("loc_FA9")

    label("loc_F4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F96")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_FA9")

    label("loc_F96")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA9")

    Jump("loc_9F7")

    label("loc_FAE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_9DD end

    def Function_7_FB6(): pass

    label("Function_7_FB6")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 2740, 0, 21060, 89)
    SetChrPos(0x1, 2740, 0, 21060, 89)
    SetChrPos(0x2, 2740, 0, 21060, 89)
    SetChrPos(0x3, 2740, 0, 21060, 89)
    SetChrPos(0x4, 2740, 0, 21060, 89)
    SetChrPos(0x5, 2740, 0, 21060, 89)
    Sleep(1)
    OP_68(2740, 600, 21060, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_108A")
    Sound(1502, 255, 100, 0)
    Jump("loc_1090")

    label("loc_108A")

    Sound(1503, 255, 100, 0)

    label("loc_1090")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_FB6 end

    def Function_8_10A5(): pass

    label("Function_8_10A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_10D8")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_132C")

    label("loc_10D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1110")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_132C")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1121")
    Call(0, 3)
    Jump("loc_132C")

    label("loc_1121")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_END)), "loc_11C6")

    ChrTalk(
        0x101,
        (
            "#0001FLet's not take the bus today.\x02\x03",
            "It's probably better if we hit the highway\x01",
            "on foot for this investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1326")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_123B")

    ChrTalk(
        0x101,
        (
            "#0001FI know our legs are still sore from yesterday,\x01",
            "but walking will do us good in the long run.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1326")

    label("loc_123B")


    ChrTalk(
        0x101,
        (
            "#0001FI know our legs are still sore from yesterday,\x01",
            "but walking will do us good in the long run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FI agree. Walking may do us some good.\x02\x03",
            "#0100FAfter all, we might stumble into clues\x01",
            "on the way there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201F...Fun.\x02",
    )

    CloseMessageWindow()

    label("loc_1326")

    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFF)

    label("loc_132C")

    Return()

    # Function_8_10A5 end

    def Function_9_132D(): pass

    label("Function_9_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1351")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)
    Jump("loc_1367")

    label("loc_1351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1367")
    Call(0, 12)

    label("loc_1367")

    Return()

    # Function_9_132D end

    def Function_10_1368(): pass

    label("Function_10_1368")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(3230, 900, 11740, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 1600, 0, 9670, 0)
    SetChrPos(0x102, 2680, 0, 8580, 0)
    SetChrPos(0x103, 840, 0, 8350, 0)
    SetChrPos(0x104, 1240, 120, 7280, 0)

    def lambda_143A():
        OP_95(0xFE, 3270, 0, 13110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_143A)

    def lambda_1454():
        OP_95(0xFE, 4430, 0, 12180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1454)

    def lambda_146E():
        OP_95(0xFE, 2180, 0, 11520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_146E)

    def lambda_1488():
        OP_95(0xFE, 2900, 0, 10410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1488)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 3000)
    OP_0D()
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#1200194V#0205F#12PThat...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_153B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_153B)
    Sleep(50)

    def lambda_154B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_154B)
    Sleep(50)

    def lambda_155B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_155B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x101,
        "#1200195V#0005F#5PWhat's wrong, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200196V#0105F#5PDo you hear something again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200197V#0201F#12PYes...\x01",
            "Increasing sensitivity levels!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1278, 255, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Sound(839, 0, 100, 0)
    Sleep(2000)
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
        "#1200198V#0007F#5PWhat the heck is that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#1200199V#0101F#5PIt was audible, albeit faint.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200200V#0303F#11PYup, that was definitely a wolf.\x02\x03",
            "#1200201V#0300FGood thing Tio Tot has sharp ears,\x01",
            "or we never woulda noticed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x103, 0x2)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 11)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    ChrTalk(
        0x103,
        "#1200202V#0203F#5P#40WPhew...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#1200203V#0201F#12PI was able to determine that the howl originated\x01",
            "in the direction of the mountain path.\x02\x03",
            "#1200204VApproximately 40 selge north-northwest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200205V#0001F#5PHmm... That's around the midpoint of\x01",
            "the path, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200206V#0305F#11PWell, crap. That can only mean one thing...\x02",
    )

    CloseMessageWindow()

    def lambda_19CC():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19CC)

    def lambda_19D9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19D9)
    Sleep(50)

    def lambda_19E9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19E9)

    def lambda_19F6():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19F6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x101, 0x102, 500)
    Sleep(800)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#1200207V#0006F#5PUmm, Elie, Tio...\x02\x03",
            "#1200208VI'm sorry. I know you suffered\x01",
            "more than enough yesterday.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    def lambda_1AF3():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AF3)

    ChrTalk(
        0x102,
        (
            "#1200209V#0104F#11PIt's okay, Lloyd. I understand.\x02\x03",
            "#1200210V#0100FFate is a cruel mistress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200211V#0204F#12PI will survive.\x02\x03",
            "#1200212V#0208FAlso, I felt as if that howl was\x01",
            "some kind of message...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BD3():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BD3)
    Sleep(50)

    def lambda_1BE3():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BE3)

    ChrTalk(
        0x101,
        "#1200213V#0005F#5PMessage? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1200214V#0301F#11PWhat? 'Cause it sounded menacing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#1200215V#0208F#12PI would not call it menacing. Rather,\x01",
            "it seemed filled with determination.\x02\x03",
            "#1200216V#0206FI am sorry. I am having difficulty finding\x01",
            "an appropriate way to describe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200217V#0003F#5PThat's okay.\x02\x03",
            "#1200218V#0001FAnyway, there's a good chance it'll try\x01",
            "to escape if the CGF steps in.\x02\x03",
            "#1200219VLet's see if we can track it down on\x01",
            "our own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#1200220V#0101F#5PYes. Tio's analysis has given us a solid lead.\x02\x03",
            "#1200221VWe'll be traveling on rough terrain, so we\x01",
            "should prepare before we leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#1200222V#0001F#5PDefinitely. Also, we should finish up any\x01",
            "support requests before meeting with\x01",
            "Mainz's mayor.\x02\x03",
            "#1200223VLet's begin searching the mountain path\x01",
            "once we've fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#1200224V#0302F#11PAll righty. Let's wrap things up and\x01",
            "have ourselves a fun hike, eh?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    SetChrPos(0x0, 1200, 0, 13100, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x64, 2)
    OP_29(0x40, 0x1, 0x1)
    EndChrThread(0xB, 0x1)
    OP_24(0x348)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_1368 end

    def Function_11_1FB9(): pass

    label("Function_11_1FB9")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_11_1FB9 end

    def Function_12_1FFC(): pass

    label("Function_12_1FFC")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(2110, 2900, 19980, 0)
    MoveCamera(32, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20380, 0)
    OP_68(2110, 900, 19980, 3000)
    SetChrPos(0x101, 2130, 0, 19420, 270)
    SetChrPos(0x102, 2130, 0, 17710, 270)
    SetChrPos(0x103, 3640, 0, 21250, 270)
    SetChrPos(0x104, 4200, 0, 19810, 270)
    SetChrPos(0x109, 3910, 0, 17590, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#4100251V#0000F#11PThis must be your assigned armored car,\x01",
            "right, Sergeant Major?\x02\x03",
            "#4100252VI remember getting a ride from you before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100253V#0504F#11PYes, this gal is mine.\x02\x03",
            "#4100254V#0502FThis CGF light-armored car can handle\x01",
            "any kind of terrain thrown at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4100255V#0306F#11PSeems like it'd bow out pretty quickly\x01",
            "if it got shot by a tank, though.\x02\x03",
            "#4100256V#0300FThe only thing this could defend against\x01",
            "is probably a gatling gun at best.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x104, 500)

    ChrTalk(
        0x109,
        (
            "#4100257V#0506F#12PUgh... You don't have to put it like that!\x02\x03",
            "#4100258V#0501FThat aside, our armored-cars are equipped\x01",
            "with the latest technology.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2336():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2336)
    Sleep(50)

    def lambda_2346():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2346)
    Sleep(50)

    def lambda_2356():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2356)
    Sleep(50)

    def lambda_2366():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2366)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#4100259V#0106F#6PWell, Crossbell doesn't have any tanks\x01",
            "of its own...\x02\x03",
            "#4100260V#0100FRelying on maneuverability might be\x01",
            "our best chance at defense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4100261V#0203F#5PThat is true. Also, correct me if I am wrong,\x01",
            "but Crossbell similarly does not own a single\x01",
            "patrol ship.\x02\x03",
            "#4100262V#0200FWith Crossbell's budget, I would imagine they\x01",
            "could stockpile ships by the dozen...\x02\x03",
            "#4100263VI assume this must be due to pressure from\x01",
            "Erebonia and Calvard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100264V#0506F#12PYes, exactly.\x02\x03",
            "#4100265V#0501FMore so Erebonia, actually. They ran into trouble\x01",
            "with Liberl's patrol ships 12 years ago, so they\x01",
            "take them much more seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4100266V#0103F#6PBesides, it wouldn't go over well if we ignored\x01",
            "them and sided with the opposition.\x02\x03",
            "#4100267V#0101FThis sort of speculation is always off and on\x01",
            "in the Empire. Same goes for the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4100268V#0003F#5PInteresting...\x02\x03",
            "#4100269V#0001FConsidering Crossbell's varied terrain,\x01",
            "airships would make patrols go a lot\x01",
            "smoother, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4100270V#0506F#12P*sigh* You're not wrong.\x02\x03",
            "#4100271V#0504FWell, I can't complain.\x02\x03",
            "#4100272V#0500FIf you ever need to travel by car,\x01",
            "I'd be happy to assist.\x02\x03",
            "#4100273VI can take you anywhere you need,\x01",
            "so long as I can drive there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can go anywhere in Crossbell State using\x01",
            "Noel's CGF vehicle for the duration of the day.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Examine the Guardian Force vehicle\x01",
            "and select your destination.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Furthermore, in the case that you leave the CGF\x01",
            "vehicle and travel by bus or on foot, you can\x01",
            "board it again at the location it was left.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Take care not to forget the location\x01",
            "the vehicle is left at.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you are going to the ruins on the outskirts\x01",
            "of the mountain path, you can select\x01",
            "'Mainz Mountain Path - Tunnel' as a shortcut.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 2850, 0, 18840, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 1)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_12_1FFC end

    def Function_13_2AB9(): pass

    label("Function_13_2AB9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-3190, 6260, 780, 0)
    MoveCamera(30, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17120, 0)
    OP_68(-3190, 2960, 780, 5000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFlags(0x1, 0x400)
    SetChrFlags(0xA, 0x8000)
    OP_78(0x1, 0xA)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_D3(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x79, 0xB4, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    Sound(485, 0, 100, 0)
    FadeToBright(1000, 0)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 70, 0, 17900, 0)

    def lambda_2BF9():
        OP_95(0xFE, 50, -2930, -8070, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BF9)
    OP_0D()
    Sleep(1100)
    BeginChrThread(0xA, 3, 0, 14)
    Sound(470, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)
    SetScenarioFlags(0x5D, 3)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2AB9 end

    def Function_14_2C43(): pass

    label("Function_14_2C43")

    OP_D3(0xFE, 0x0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x3E8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x7D0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0xBB8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0xFA0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1388, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1770, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1B58, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x1F40, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2328, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2710, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2AF8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x2EE0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x32C8, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x36B0, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    OP_D3(0xFE, 0x3A98, 0x2BF20, 0x0, 0x0)
    Sleep(50)
    Return()

    # Function_14_2C43 end

    def Function_15_2DA4(): pass

    label("Function_15_2DA4")

    EventBegin(0x0)
    Sleep(1000)
    OP_EE(0x0, 0x1)
    OP_68(14140, -670, 19290, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(23500, 5000)
    OP_6F(0x79)
    OP_EE(0x0, 0xA)
    Sound(828, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Check any bus stop sign to board an orbal bus.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This allows you to quickly reach your\x01",
            "destination and travel across Crossbell State.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_15_2DA4 end

    def Function_16_2E85(): pass

    label("Function_16_2E85")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "South: Crossbell City\x01",
            "East:  Crossbell Cathedral\x01",
            "Northwest: Mainz Mining Village - 311 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2E85 end

    def Function_17_2F16(): pass

    label("Function_17_2F16")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2FBF")

    ChrTalk(
        0x101,
        (
            "#0000FWait, why are we heading towards\x01",
            "the mountain path?\x02\x03",
            "#0003FWe still don't know what's going\x01",
            "on at St. Ursula. Now's not the\x01",
            "time for detours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301C")

    label("loc_2FBF")


    ChrTalk(
        0x101,
        (
            "#0003FKeA and the monster-filled road\x01",
            "are a bad mix.\x02\x03",
            "#0000FLet's not make any detours.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301C")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_17_2F16 end

    SaveToFile()

Try(main)
