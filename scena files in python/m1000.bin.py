from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1000.bin",                # FileName
        "m1000",                    # MapName
        "m1000",                    # Location
        0x006B,                     # MapIndex
        "ed7202",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 4000, 3000, -9000, 0, 0, 1, 107, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1000",                  # 0
        "Sergeant Major Seeker",  # 1
        "車",                     # 2
        "SE制御",                 # 3
        "To Ursula Road",         # 4
    ))

    AddCharChip((
        "chr/ch00800.itc",                   # 00
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

    DeclNpc(37250,   -13199,  98250,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  6.5,                   27.799999237060547,    -5.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6500000357627869,   -9.266666412353516,    1.0,                   1.0])
    DeclEvent(0x0000, 0, 13,  34.599998474121094,    85.44999694824219,     -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.4599997997283936,   -28.483333587646484,   2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 7,   34.599998474121094,    71.5999984741211,      -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.4599997997283936,   -23.866666793823242,   2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 8,   34.599998474121094,    104.0,                 -14.199999809265137,   56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.919999599456787,    -34.66666793823242,    2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 10,  6.5,                   7.0,                   -5.0,                  2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -0.6500000357627869,   -0.699999988079071,    0.5,                   1.0])

    DeclActor(36310,   -13200,  85240,   1200,    36310,   -11700,  85240,   0x007C, 0,  15, 0x0000)
    DeclActor(44360,   -13190,  93720,   1200,    44360,   -11190,  93720,   0x007C, 0,  5,  0x0000)
    DeclActor(5980,    -3710,   24960,   5000,    5980,    -3710,   24960,   0x007C, 0,  14, 0x0000)

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "To Ursula Road")
    PlaceName(45.29999923706055, 0.0, 95.25, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_414",          # 00, 0
        "Function_1_4CC",          # 01, 1
        "Function_2_54F",          # 02, 2
        "Function_3_74F",          # 03, 3
        "Function_4_DD1",          # 04, 4
        "Function_5_EC0",          # 05, 5
        "Function_6_ECE",          # 06, 6
        "Function_7_10A1",         # 07, 7
        "Function_8_145D",         # 08, 8
        "Function_9_14EE",         # 09, 9
        "Function_10_14F4",        # 0A, 10
        "Function_11_14FD",        # 0B, 11
        "Function_12_1871",        # 0C, 12
        "Function_13_187B",        # 0D, 13
        "Function_14_2DAB",        # 0E, 14
        "Function_15_3D17",        # 0F, 15
    ))


    def Function_0_414(): pass

    label("Function_0_414")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_454"),
        (1, "loc_460"),
        (2, "loc_46C"),
        (3, "loc_478"),
        (4, "loc_484"),
        (5, "loc_490"),
        (6, "loc_49C"),
        (SWITCH_DEFAULT, "loc_4A8"),
    )


    label("loc_454")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_460")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_46C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_478")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_484")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_490")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_49C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4B4")

    label("loc_4CB")

    Return()

    # Function_0_414 end

    def Function_1_4CC(): pass

    label("Function_1_4CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E2")
    SetMapFlags(0x10000000)
    Event(0, 9)

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F0")
    Jump("loc_536")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_END)), "loc_523")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 43020, -13200, 93370, 34)

    label("loc_51E")

    Jump("loc_536")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_END)), "loc_536")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_54E")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_54E")

    Return()

    # Function_1_4CC end

    def Function_2_54F(): pass

    label("Function_2_54F")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B6")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_5BB")

    label("loc_5B6")

    ModifyEventFlags(1, 3, 0x80)

    label("loc_5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CF")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_610")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFB, 0xC4, 0xA6, 0x14, 0x190, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    Jump("loc_62C")

    label("loc_610")

    SetMapObjFrame(0xFF, "allback", 0x2, "blue")
    SetMapObjFrame(0xFF, "sky", 0x2, "blue")

    label("loc_62C")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_662")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jump("loc_698")

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_67C")
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_698")

    label("loc_67C")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    OP_66(0x0, 0x1)

    label("loc_698")

    SetMapObjFlags(0x0, 0x4)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C7")
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_66(0x1, 0x1)

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FA")
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_66(0x1, 0x1)
    Jump("loc_6FF")

    label("loc_6FA")

    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_6FF")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_711")
    Jump("loc_74E")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_74E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_72B")
    Jump("loc_74E")

    label("loc_72B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_73D")
    Jump("loc_74E")

    label("loc_73D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_74E")
    OP_66(0x2, 0x1)

    label("loc_74E")

    Return()

    # Function_2_54F end

    def Function_3_74F(): pass

    label("Function_3_74F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_76E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F7")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DF")
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
    Jump("loc_7F2")

    label("loc_7DF")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F2")

    Jump("loc_76E")

    label("loc_7F7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    label("loc_7FF")

    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC9")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D66")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_8B9")

    label("loc_89E")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_8B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_8FD")

    label("loc_8E7")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_941")

    label("loc_92B")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_941")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_970")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_987")

    label("loc_970")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_9CD")

    label("loc_9B6")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_9CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_A09")

    label("loc_9F7")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_A09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A35")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_A49")

    label("loc_A35")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_A49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A81")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_AA1")

    label("loc_A81")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_AE5")

    label("loc_ACF")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_B31")

    label("loc_B17")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_B31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_B8D")

    label("loc_B6B")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_B8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_BD3")

    label("loc_BBC")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_BD3")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D57")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x0)
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
        (0, "loc_CAA"),
        (1, "loc_CB8"),
        (2, "loc_CC6"),
        (3, "loc_CD4"),
        (4, "loc_CE2"),
        (5, "loc_CF0"),
        (6, "loc_CFE"),
        (7, "loc_D0C"),
        (8, "loc_D1A"),
        (9, "loc_D28"),
        (10, "loc_D36"),
        (11, "loc_D44"),
        (SWITCH_DEFAULT, "loc_D52"),
    )


    label("loc_CAA")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CB8")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CC6")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CD4")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CE2")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CF0")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_CFE")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D0C")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D1A")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D28")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D36")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D44")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D52")

    label("loc_D52")

    Jump("loc_D61")

    label("loc_D57")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D61")

    Jump("loc_DC4")

    label("loc_D66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB1")
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
    Jump("loc_DC4")

    label("loc_DB1")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC4")

    Jump("loc_812")

    label("loc_DC9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_74F end

    def Function_4_DD1(): pass

    label("Function_4_DD1")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 42720, -13190, 92310, 215)
    SetChrPos(0x1, 42720, -13190, 92310, 215)
    SetChrPos(0x2, 42720, -13190, 92310, 215)
    SetChrPos(0x3, 42720, -13190, 92310, 215)
    SetChrPos(0x4, 42720, -13190, 92310, 215)
    SetChrPos(0x5, 42720, -13190, 92310, 215)
    Sleep(1)
    OP_68(42720, -11190, 92310, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA5")
    Sound(1502, 255, 100, 0)
    Jump("loc_EAB")

    label("loc_EA5")

    Sound(1503, 255, 100, 0)

    label("loc_EAB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_DD1 end

    def Function_5_EC0(): pass

    label("Function_5_EC0")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 3)
    Return()

    # Function_5_EC0 end

    def Function_6_ECE(): pass

    label("Function_6_ECE")

    TalkBegin(0xFE)

    ChrTalk(
        0x8,
        (
            "#0500FI'm locked and loaded!\x01",
            "Should we return to the\x01",
            "investigation now?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Resume\x01",                     # 0
            "Still Need To Prepare\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD9")

    ChrTalk(
        0x101,
        "#0000FYeah, let's get back to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0500FUnderstood!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    AddParty(0x8, 0xFF, 0xFF)
    OP_49()
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    FadeToBright(250, 0)
    OP_0D()
    Jump("loc_109D")

    label("loc_FD9")


    ChrTalk(
        0x8,
        (
            "#0503FOh, I see. We're dealing with an\x01",
            "extremely dangerous person, so we\x01",
            "should prepare as much as possible.\x02\x03",
            "#0501FI'll be on standby. Just call for me\x01",
            "when you're ready to enter the tower.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109D")

    TalkEnd(0xFE)
    Return()

    # Function_6_ECE end

    def Function_7_10A1(): pass

    label("Function_7_10A1")

    EventBegin(0x0)
    Fade(500)
    OP_68(34420, -11200, 71170, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14220, 0)
    SetChrPos(0x101, 34730, -13200, 70340, 350)
    SetChrPos(0x102, 33310, -13200, 70960, 35)
    SetChrPos(0x103, 36380, -13200, 71570, 305)
    SetChrPos(0x104, 36730, -13200, 73240, 260)
    SetChrPos(0x109, 34420, -13200, 73610, 170)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#0505FOh, are you heading\x01",
            "back into the city?\x02\x03",
            "#0500FSorry, guys. I've got to stand guard\x01",
            "so no civilians wander inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, is that right? We were kind\x01",
            "of wanting to check on all our\x01",
            "equipment before going back inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWell, nothin' we can do about it.\x02\x03",
            "#0300FNoel, looks like we gotta split up\x01",
            "for now. Don't worry. We'll be back\x01",
            "in a jiffy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0500FUnderstood. I'll wait over by my car until\x01",
            "you all return. Be careful, everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah, right back at you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_134E")
    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)

    label("loc_134E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1368")
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x1, 0x2, 0x1)

    label("loc_1368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1382")
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x2, 0x2, 0x1)

    label("loc_1382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D6(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_139C")
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x3, 0x2, 0x1)

    label("loc_139C")

    OP_32(0x8, 0xFC, 0x0)
    OP_32(0x8, 0xFE, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_49()
    OP_68(34730, -11200, 70340, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 34730, -13200, 70340, 170)
    SetChrPos(0x1, 34730, -13200, 70340, 170)
    SetChrPos(0x2, 34730, -13200, 70340, 170)
    SetChrPos(0x3, 34730, -13200, 70340, 170)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 43020, -13200, 93370, 34)
    BeginChrThread(0x8, 0, 0, 0)
    FadeToBright(250, 0)
    OP_0D()
    EventEnd(0x6)
    Return()

    # Function_7_10A1 end

    def Function_8_145D(): pass

    label("Function_8_145D")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0005FHmm, are we ready?\x02\x03",
            "#0000FIf we're going to investigate the tower,\x01",
            "we should let Sergeant Major Seeker know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 34460, -13190, 100280, 170)
    EventEnd(0x4)
    Return()

    # Function_8_145D end

    def Function_9_14EE(): pass

    label("Function_9_14EE")

    ClearMapFlags(0x10000000)
    Return()

    # Function_9_14EE end

    def Function_10_14F4(): pass

    label("Function_10_14F4")

    SetScenarioFlags(0x87, 6)
    ModifyEventFlags(0, 4, 0x80)
    Return()

    # Function_10_14F4 end

    def Function_11_14FD(): pass

    label("Function_11_14FD")

    EventBegin(0x0)
    OP_E0(0x1)
    OP_68(35980, -5200, 92810, 0)
    MoveCamera(22, 6, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(93640, 0)
    SetChrPos(0x101, 7280, -3700, 24800, 19)
    SetChrPos(0x102, 8330, -3700, 23560, 19)
    SetChrPos(0x103, 6260, -3700, 24230, 19)
    SetChrPos(0x104, 7250, -3700, 22830, 19)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 37250, -13200, 98250, 0)
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    BeginChrThread(0xA, 1, 0, 12)
    Fade(1000)
    OP_68(27780, -5200, 96400, 10000)
    PlaceName2(340, 40, "c_plac28", 0x0, 5000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(35000, -10600, 104630, 0)
    MoveCamera(25, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(32000, 0)
    OP_68(35000, -10600, 87130, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x8, 0x8000)
    OP_68(5190, -1800, 22500, 0)
    MoveCamera(20, 5, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21370, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_16DB")

    ChrTalk(
        0x101,
        "#2201048V#0005F#6PIs that what I think it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201049V#0105F#12PIsn't that one of the Guardian\x01",
            "Force's armored cars?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_16DB")


    ChrTalk(
        0x101,
        (
            "#2201050V#0000F#6PThere's Stargazer's Tower, so we\x01",
            "obviously went the right way.\x02\x03",
            "#2201051V#0005FWait, is that what I think it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201052V#0105F#12PA Guardian Force car? I think so.\x02",
    )

    CloseMessageWindow()

    label("loc_179D")


    ChrTalk(
        0x104,
        (
            "#2201053V#0303F#12PYup. That's one of the CGF's\x01",
            "fancy light-armored cars.\x02\x03",
            "#2201054V#0301FWhy's it in a place like this, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2201055V#0200F#6PLet us ask, then.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6500, -3700, 24300, 19)
    SetScenarioFlags(0x84, 1)
    EndChrThread(0xA, 0x1)
    OP_E0(0x0)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_11_14FD end

    def Function_12_1871(): pass

    label("Function_12_1871")

    Sleep(2000)
    Sound(866, 0, 100, 0)
    Return()

    # Function_12_1871 end

    def Function_13_187B(): pass

    label("Function_13_187B")

    EventBegin(0x0)
    Fade(1000)
    OP_68(37250, -12300, 98250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 3000)
    SetChrPos(0x101, 36650, -13200, 89750, 0)
    SetChrPos(0x102, 37850, -13200, 89750, 0)
    SetChrPos(0x103, 36650, -13200, 88450, 0)
    SetChrPos(0x104, 37850, -13200, 88450, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 37250, -13200, 98250, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrSubChip(0x8, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis202.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    OP_0D()
    OP_6F(0x79)
    Sound(1494, 255, 85, 0)
    Sleep(800)

    ChrTalk(
        0x8,
        (
            "#2201056V#0506F#11PWho would want to go inside a\x01",
            "place like Stargazer's Tower...?\x02\x03",
            "#2201057V#0508FMaybe some history buff got\x01",
            "curious and decided to trespass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201058V#1PHeeeey!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_68(37250, -12300, 97250, 3000)

    def lambda_1A84():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A84)
    Sleep(50)

    def lambda_1A9C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A9C)
    Sleep(50)

    def lambda_1AB4():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AB4)
    Sleep(50)

    def lambda_1ACC():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ACC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    ChrTalk(
        0x8,
        "#2201059V#0505F#5PWait, are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201060V#0000F#12PI knew it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201061V#0302F#12PWho woulda thought the next time we'd\x01",
            "meet would be in a place like this, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201062V#0505F#5PLloyd? Randy?\x02\x03",
            "#2201063V#0502FElie and Tio, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201064V#0102F#2PLong time no see,\x01",
            "Sergeant Major Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201065V#0204F#12PWe appreciate all the help\x01",
            "you gave us in Mainz.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#2201066VDon't mention it.\x02\x03",
            "#2201067VSo, what brings the SSS\x01",
            "to Stargazer's Tower?\x02\x03",
            "#2201068VThis isn't exactly a common\x01",
            "place for people to visit.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#2201069V#0006F#12PSorry, we've got something to take care of.\x02\x03",
            "#2201070V#0001FBut, uh, what's the deal\x01",
            "with the barricade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201071V#0506F#5PApparently, someone decided to destroy it\x01",
            "for who knows what reason.\x02\x03",
            "#2201072V#0501FThe whole point was to keep people from\x01",
            "entering the tower. Given its age, someone\x01",
            "could get really hurt in there.\x02\x03",
            "#2201073VAnyway, I found the barricade like this\x01",
            "during my regular patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201074V#0013F#12PYou don't say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201075V#0303F#12PHow convenient that it\x01",
            "was demolished today...\x02\x03",
            "#2201076V#0301FYeah, I think it was our perp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201077V#0103F#2PIt must have been.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2201078V#0505F#5PPerp? You'll have to fill me in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201079V#0001F#12PWell, here's the gist of it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd quickly explained the situation\x01",
            "to a confused Noel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#2201080V#0507F#5PAn assassin from the Eastern Quarter?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201081V#0103F#2PThat's right.\x02\x03",
            "#2201082V#0101FWe received a message from him saying\x01",
            "he'd be waiting for us in this tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201083V#0003F#12PI thought we might as well\x01",
            "take a look, but...\x02\x03",
            "#2201084V#0001FIt looks like he was serious\x01",
            "about waiting here for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201085V#0506F#5P*sigh* I can't believe\x01",
            "this is happening.\x02\x03",
            "#2201086V#0501FWell, what's your plan?\x02\x03",
            "#2201087VI assume you aren't here to fall for his bait,\x01",
            "so do you have anything up your sleeve?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201088V#0000F#12PEr, we were actually going\x01",
            "to do EXACTLY that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#2201089V#0505F#5PWh-What do you mean?\x02\x03",
            "#2201090V#0501FYou're dealing with an incredibly dangerous\x01",
            "criminal! This has got to be some kind of trap...\x02\x03",
            "#2201091VWe should contact Deputy Commander Baelz\x01",
            "and request backup for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201092V#0303F#12PNah. This guy's a pro.\x02\x03",
            "#2201093VIf we roll in with an army,\x01",
            "he'll just run away, y'know?\x02\x03",
            "#2201094V#0301FA smaller unit is the right call.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2201095V#0506F#5PTh-That's a fair point...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#2201096V#0503F#5PIn that case, I won't stop you.\x02\x03",
            "#2201097V#0507FHowever, since I'm responsible\x01",
            "here, allow me to assist!\x02",
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
        "#2201098V#0011F#12PY-You want to help?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201099V#0105F#2PSergeant Major, are you allowed to do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2201100V#0503F#5PAs you know, this tower is under\x01",
            "the Guardian Force's jurisdiction.\x02\x03",
            "#2201101VI would be neglecting my duty if I let you\x01",
            "wander into danger alone.\x02\x03",
            "#2201102V#0500FBesides, it's the least I can do, since\x01",
            "you're always looking after Fran.\x02\x03",
            "#2201103VSergeant Major Noel Seeker of the CGF\x01",
            "is locked, loaded, and ready to help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201104V#0006F#12PW-Wow. Thank you.\x02\x03",
            "#2201105V#0002FTo be honest, Fran's usually\x01",
            "the one taking care of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201106V#0304F#12PHey, the more the merrier, right?\x02\x03",
            "#2201107V#0302FI've heard Noel here is a beast in combat,\x01",
            "so let's use the help!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201108V#0204F#12PI concur.\x02\x03",
            "#2201109V#0202FHaving backup would improve our\x01",
            "combat capabilities immensely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201110V#0103F#2PThe question now is whether or not Yin will be put\x01",
            "on edge because we have a CGF officer with us...\x02\x03",
            "#2201111V#0100FSurely one person wouldn't be an issue?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201112V#0004F#12PYeah, I think we're safe.\x02\x03",
            "#2201113V#0000FI'm looking forward to working\x01",
            "with you, Sergeant Major.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2201114V#0502F#5PLikewise!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18250, 1000)
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
            "Noel has joined the party as a guest character.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "When there are more than four people in your party,\x01",
            "the extra members will act as a 'support members.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Support members remain outside of the front lines in\x01",
            "battle, but may occasionally appear in the battle order\x01",
            "bar to perform various attacks/buffs on their turn.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Party members can be swapped in and out under [TACTICS]\x01",
            "in the Camp Menu. You can set Noel as an attack member\x01",
            "by swapping her with Lloyd, Elie, Tio, or Randy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    AddParty(0x8, 0xFF, 0xFF)
    OP_49()
    OP_32(0x8, 0x0, 0x12)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x1)
    OP_38(0x8, 0x82, 0x1)
    OP_38(0x8, 0x83, 0x1)
    OP_38(0x8, 0x84, 0x1)
    OP_38(0x8, 0x85, 0x1)
    OP_38(0x8, 0x86, 0x1)
    OP_42(0x8, 0x44C, 0xFF)
    OP_42(0x8, 0x5E1, 0xFF)
    OP_42(0x8, 0x645, 0xFF)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    SetChrChipPat(0x8, 0x6, 0x122)
    AddCraft(0x8, 0x144)
    OP_42(0x8, 0x6E, 0x0)
    OP_42(0x8, 0x91, 0x4)
    OP_42(0x8, 0x7A, 0x3)
    OP_42(0x8, 0x7F, 0x2)
    OP_42(0x8, 0x65, 0x1)
    OP_42(0x8, 0x6B, 0x6)
    OP_42(0x8, 0xAC, 0x5)
    AddCraft(0x0, 0x12C)
    AddCraft(0x1, 0x12F)
    AddCraft(0x2, 0x132)
    AddCraft(0x3, 0x135)
    OP_CA(0x1, 0xFF, 0x0)
    OP_37()
    SetChrPos(0x0, 34150, -13190, 97220, 0)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x84, 2)
    OP_29(0x43, 0x1, 0x8)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_13_187B end

    def Function_14_2DAB(): pass

    label("Function_14_2DAB")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(7760, 1400, 36490, 0)
    MoveCamera(16, -4, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24350, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 4360, -3710, 22360, 19)
    SetChrPos(0x102, 5820, -3710, 23960, 19)
    SetChrPos(0x103, 7950, -3710, 23220, 19)
    SetChrPos(0x104, 6240, -3710, 21720, 19)
    OP_68(7890, -2300, 27250, 6000)
    MoveCamera(17, 4, 0, 6000)
    SetCameraDistance(20950, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#0001FStargazer's Tower... It's been a\x01",
            "while since we fought Yin here.\x02\x03",
            "#0003FOn second glance, this place\x01",
            "sure is beautiful, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0108FFrom the outside, absolutely.\x01",
            "From the inside, not so much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FWould it not be wise to conduct an\x01",
            "investigation of the entire tower\x01",
            "someday?\x02\x03",
            "#0203FLeaving mysteries like this unchecked\x01",
            "always leaves an unsavory taste in\x01",
            "my mouth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FConsiderin' the place is under\x01",
            "the CGF's jurisdiction, that might\x01",
            "be easier said than done, Tio Tot.\x02\x03",
            "#0301FOn top of that, you'd have to get the permission\x01",
            "of a dumbass who won't allow anything that\x01",
            "doesn't earn him a promotion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0003FWell, with all these problems to\x01",
            "deal with, we'll never get bored.\x02\x03",
            "#0000FAnyway, this spot would make a nice photo\x01",
            "for Grace's article.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3967")
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#6P#0000FDo you mind taking a few photos\x01",
            "for us, Elie?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0108FN-Not at all. Don't expect a masterpiece\x01",
            "from me, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#12P#0300FPssh. Relax, Mademois-Elie.\x02\x03",
            "Ya just gotta peek through that lens,\x01",
            "give it a lil' click, then bam, we good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    ChrTalk(
        0x102,
        (
            "#6P#0106F*sigh* If only capturing a great\x01",
            "photo were that simple...\x02\x03",
            "#0100FYou need to pay close attention to\x01",
            "your composition to ensure you've\x01",
            "captured everything in frame.\x02\x03",
            "The weather, wind speed, and lighting\x01",
            "can completely alter the impression\x01",
            "a photo gives.\x02\x03",
            "There are no second chances when\x01",
            "it comes to a picture-perfect moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FThe difference in quality between\x01",
            "amateur and professional photography\x01",
            "is immediately apparent.\x02\x03",
            "#0203FI imagine a simpleton would have difficulty\x01",
            "grasping any level of intricacy or nuance,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x104,
        "#12P#0306FDamn, Tio Tot. You implyin' something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FC-Calm down, everyone. We should\x01",
            "let Elie focus on taking the photo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FRight... I'll try to live up to your\x01",
            "expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x13, 0x1F4)
    OP_93(0x101, 0x13, 0x1F4)
    OP_93(0x103, 0x13, 0x1F4)
    OP_93(0x104, 0x13, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#0103FPhew... There we go. I took a\x01",
            "couple of extras, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FHey, it looks like you pulled through.\x02\x03",
            "Well? How'd they turn out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FI won't have an answer for you until\x01",
            "I've seen the developed photos.\x02\x03",
            "At the very least, I think they'll\x01",
            "get the job done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FIt would be a safe assumption to think\x01",
            "Elie has regained her photography skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FWell, I'm no picture-takin' guru,\x01",
            "but I'm sure they turned out fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FRight. We should keep our eyes\x01",
            "peeled for other scenic locations\x01",
            "we can take photos of.\x02\x03",
            "But anyway, let's get a move on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE0")

    label("loc_3967")

    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#6P#0000FWill you do the honors, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0100FOkay. Leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x13, 0x1F4)
    OP_93(0x101, 0x13, 0x1F4)
    OP_93(0x103, 0x13, 0x1F4)
    OP_93(0x104, 0x13, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#0103FPhew... I hope they turned out okay.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3AFD")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_3B14")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_3B2B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_3B42")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3B59")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_3B70")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_3B87")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3B9E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_3BB5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3BB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C82")

    ChrTalk(
        0x101,
        (
            "#6P#0000FGood job, Elie. You look like you're\x01",
            "getting the hang of it again.\x02\x03",
            "And now we've managed to meet Grace's\x01",
            "five-photo quota. Let's run these by her\x01",
            "when we get the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE0")

    label("loc_3C82")


    ChrTalk(
        0x101,
        (
            "#6P#0000FNice, Elie! You looked pretty confident\x01",
            "taking that picture.\x02\x03",
            "Shall we move on?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5980, -3710, 24960, 19)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x8)
    Sleep(500)
    OP_65(0x2, 0x1)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_2DAB end

    def Function_15_3D17(): pass

    label("Function_15_3D17")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F28")

    ChrTalk(
        0x103,
        "#0200FI suppose we are not allowed to enter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FThis is one of the Crossbell Guardian\x01",
            "Force's barricades, so yeah, probably not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FCan't say I'm surprised, though. Stargazer's\x01",
            "Tower was built way back in the Middle Ages.\x02\x03",
            "They'd be in a world of trouble if a\x01",
            "civilian entered and the floor collapsed,\x01",
            "or something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI've heard about this place, but this is\x01",
            "the first time I've seen it in person.\x02\x03",
            "If I'm right, this place has been\x01",
            "sealed for almost ten years now...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x87, 4)
    Jump("loc_3FAA")

    label("loc_3F28")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The road has been blocked by barricade.\x02\x03",
            "The sign on it indicates that it was placed by\x01",
            "the Crossbell Guardian Force.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3FAA")

    TalkEnd(0xFF)
    Return()

    # Function_15_3D17 end

    SaveToFile()

Try(main)
