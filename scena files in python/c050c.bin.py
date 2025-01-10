from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c050c.bin",                # FileName
        "c050c",                    # MapName
        "c050c",                    # Location
        0x0026,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 2, 0, 3],
    )

    BuildStringList((
        "c050c",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Barker Bishy",           # 3
        "Eris",                   # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Central Square",         # 11
        "West Street",            # 12
        "Administrative District",# 13
        "Residential District",   # 14
        "Entertainment District", # 15
        "East Street",            # 16
        "Downtown District",      # 17
        "Harbor District",        # 18
        "IBC",                    # 19
        "Station Street",         # 20
        "Back Alley",             # 21
        "Ursula Road",            # 22
        "East Crossbell Highway", # 23
        "West Crossbell Highway", # 24
        "Mainz Mountain Path",    # 25
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch23500.itc",                   # 02
        "chr/ch23600.itc",                   # 03
        "chr/ch24200.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch26700.itc",                   # 06
        "chr/ch26900.itc",                   # 07
        "chr/ch31000.itc",                   # 08
        "chr/ch31100.itc",                   # 09
    ))

    DeclNpc(-2000,   0,       41700,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2000,    0,       41700,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16590,  0,       2980,    90,   277,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   7,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-14979,  0,       2980,    270,  405,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-14100,  0,       2549,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)

    DeclEvent(0x0000, 0, 24,  -0.10000000149011612,  43.849998474121094,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.05000000074505806,   -21.924999237060547,   0.10000000149011612,   1.0])

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  4,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  5,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  6,  0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "Central Square")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "West Street")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "Residential District")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "East Street")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "IBC")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "Station Street")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_54C",          # 00, 0
        "Function_1_604",          # 01, 1
        "Function_2_66B",          # 02, 2
        "Function_3_8A4",          # 03, 3
        "Function_4_9B0",          # 04, 4
        "Function_5_B3D",          # 05, 5
        "Function_6_CAB",          # 06, 6
        "Function_7_E2D",          # 07, 7
        "Function_8_1104",         # 08, 8
        "Function_9_144B",         # 09, 9
        "Function_10_19C8",        # 0A, 10
        "Function_11_1AB0",        # 0B, 11
        "Function_12_1BB2",        # 0C, 12
        "Function_13_1C6D",        # 0D, 13
        "Function_14_1D4F",        # 0E, 14
        "Function_15_26A8",        # 0F, 15
        "Function_16_26F6",        # 10, 16
        "Function_17_276D",        # 11, 17
        "Function_18_27A5",        # 12, 18
        "Function_19_2819",        # 13, 19
        "Function_20_2891",        # 14, 20
        "Function_21_290A",        # 15, 21
        "Function_22_29AD",        # 16, 22
        "Function_23_2D48",        # 17, 23
        "Function_24_40DD",        # 18, 24
        "Function_25_417A",        # 19, 25
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_58C"),
        (1, "loc_598"),
        (2, "loc_5A4"),
        (3, "loc_5B0"),
        (4, "loc_5BC"),
        (5, "loc_5C8"),
        (6, "loc_5D4"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_58C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_598")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_603")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_603")

    Return()

    # Function_0_54C end

    def Function_1_604(): pass

    label("Function_1_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66A")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_604")

    label("loc_66A")

    Return()

    # Function_1_604 end

    def Function_2_66B(): pass

    label("Function_2_66B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75A")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72D")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_74C")

    label("loc_72D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74C")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_74C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FB")

    label("loc_75A")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D3")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_7F2")

    label("loc_7D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_7F2")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FB")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81A")
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_841")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")
    SetChrFlags(0x9, 0x10)

    label("loc_83C")

    Jump("loc_88B")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_85B")
    OP_93(0xA, 0xB4, 0x0)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_88B")

    label("loc_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_86E")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_88B")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_886")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_88B")

    label("loc_886")

    ClearChrFlags(0xC, 0x80)

    label("loc_88B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    OP_C7(0x1, 0x1000)

    label("loc_8A3")

    Return()

    # Function_2_66B end

    def Function_3_8A4(): pass

    label("Function_3_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")
    OP_70(0x4, 0x0)
    Jump("loc_8BB")

    label("loc_8B7")

    OP_70(0x4, 0x1E)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CE")
    OP_70(0x5, 0x0)
    Jump("loc_8D2")

    label("loc_8CE")

    OP_70(0x5, 0x1E)

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5")
    OP_70(0x6, 0x0)
    Jump("loc_8E9")

    label("loc_8E5")

    OP_70(0x6, 0x1E)

    label("loc_8E9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_901")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_901")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    OP_1B(0x1, 0x0, 0x19)

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92C")
    OP_1B(0x1, 0x0, 0x17)

    label("loc_92C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -13000, -4000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_8A4 end

    def Function_4_9B0(): pass

    label("Function_4_9B0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9A")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_A30")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_A95")

    label("loc_A30")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A95")

    Jump("loc_B31")

    label("loc_A9A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I've spent my entire life on top of Revache's factory\x01",
            "and this is STILL the worst crime I've ever witnessed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B31")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9B0 end

    def Function_5_B3D(): pass

    label("Function_5_B3D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C27")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_BBD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_C22")

    label("loc_BBD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x397),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C22")

    Jump("loc_C9F")

    label("loc_C27")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can't even DO the quest that's useful for yet.\x01",
            "Baby... What is you doin'?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_C9F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B3D end

    def Function_6_CAB(): pass

    label("Function_6_CAB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D95")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x69, 1)"), scpexpr(EXPR_END)), "loc_D2B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_D90")

    label("loc_D2B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D90")

    Jump("loc_E21")

    label("loc_D95")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Damn tourists always wandering into places they\x01",
            "don't belong... Wait, how ARE you here right now?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_E21")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CAB end

    def Function_7_E2D(): pass

    label("Function_7_E2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0x8,
        (
            "We've got an important event today,\x01",
            "so don't try and ruin it for us. Capisce?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep wandering around here like that,\x01",
            "and I'm gonna throw you into a ditch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F61")

    label("loc_EEB")


    ChrTalk(
        0x8,
        "Huh? The hell you want, kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Keep wandering around here like that,\x01",
            "and I'm gonna throw you into a ditch.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F61")

    Jump("loc_1100")

    label("loc_F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1077")

    ChrTalk(
        0x8,
        "Hehe. I like how flashy festivals are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kinda blows that I gotta stand guard\x01",
            "here. Dumb tourists keep getting\x01",
            "lost in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I definitely would have heard something\x01",
            "if Colin had come this way. What a relief.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1072")

    ChrTalk(
        0x160,
        "#3308F(...)\x02",
    )

    CloseMessageWindow()

    label("loc_1072")

    Jump("loc_1100")

    label("loc_1077")


    ChrTalk(
        0x8,
        "Hehe. I like how flashy festivals are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kinda blows that I gotta stand guard\x01",
            "here. Dumb tourists keep getting\x01",
            "lost in the area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1100")

    TalkEnd(0xFE)
    Return()

    # Function_7_E2D end

    def Function_8_1104(): pass

    label("Function_8_1104")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1253")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_118E")

    ChrTalk(
        0x9,
        "Quit buzzin' around like flies, ya damn cops!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Piss off, will ya?!\x01",
            "I don't got any time to talk to ya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124E")

    label("loc_118E")


    ChrTalk(
        0x9,
        "Damn it. Gotta stay behind today of all days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "My luck blows.\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0x9,
        "The hell you want?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Piss off, will ya?!\x01",
            "I don't got any time to talk to ya.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_124E")

    Jump("loc_1447")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1366")

    ChrTalk(
        0x9,
        (
            "Hey, what the hell?\x01",
            "If you don't got any business here, then piss off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The boss don't got any time to\x01",
            "spare for the likes of ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(I definitely would have heard something\x01",
            "if Colin had come this way. What a relief.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_1361")

    ChrTalk(
        0x160,
        "#3308F(...)\x02",
    )

    CloseMessageWindow()

    label("loc_1361")

    Jump("loc_1447")

    label("loc_1366")


    ChrTalk(
        0x9,
        (
            "You bastards again?\x01",
            "I dunno if you got balls or if you're just\x01",
            "plain stupid showin' your faces here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "If you don't got any business here, then piss off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The boss don't got any time to\x01",
            "spare for the likes of ya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1447")

    TalkEnd(0xFE)
    Return()

    # Function_8_1104 end

    def Function_9_144B(): pass

    label("Function_9_144B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_145F")
    Call(0, 10)
    Jump("loc_19C4")

    label("loc_145F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(
        0xA,
        (
            "All right, it's time to rake in a bunch of\x01",
            "customers again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hahahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_14C6")


    ChrTalk(
        0xA,
        (
            "Phew... Nothin' beats a fresh cig\x01",
            "at the end of my shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My life feels complete.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1525")

    Jump("loc_19C4")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_175C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_END)), "loc_160E")

    ChrTalk(
        0xA,
        (
            "The parade was pretty damn noisy,\x01",
            "so I'd guess that a kiddo or three\x01",
            "passed by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Your pal Bishy wasn't really payin' attention.\x01",
            "A bunch of little kids aren't gonna earn me\x01",
            "mira, you feel me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1757")

    label("loc_160E")


    ChrTalk(
        0x101,
        (
            "#0001F(I really hope he didn't go into the Back Alley,\x01",
            "but this man might have seen Colin.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if he knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        "Hahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Not a damn clue.\x01",
            "Don't think I saw the kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FI see...\x01",
            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_1757")

    Jump("loc_19C4")

    label("loc_175C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_17C3")

    ChrTalk(
        0xA,
        (
            "All right, it's time to rake in a bunch of\x01",
            "customers again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hahahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_17C3")


    ChrTalk(
        0xA,
        (
            "Phew... Nothin' beats a fresh cig\x01",
            "at the end of my shift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My life feels complete.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1822")

    Jump("loc_19C4")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18CC")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "If you came all the way to Crossbell,\x01",
            "then you should party your ass off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "C'mon, get over here. I'll be your guide!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_18CF")

    label("loc_18CC")

    Call(0, 11)

    label("loc_18CF")

    Jump("loc_19C4")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_193F")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xA,
        (
            "No need to hold back!\x01",
            "You two are always welcome here!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_1942")

    label("loc_193F")

    Call(0, 12)

    label("loc_1942")

    Jump("loc_19C4")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_19C1")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "Don't be shy, mister. If you come in,\x01",
            "I'm sure it'll prove a fine story for your trip.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_19C4")

    label("loc_19C1")

    Call(0, 13)

    label("loc_19C4")

    TalkEnd(0xFE)
    Return()

    # Function_9_144B end

    def Function_10_19C8(): pass

    label("Function_10_19C8")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xA,
        (
            "No way, man. I swear that wasn't what I\x01",
            "was getting at when I approached you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm just sayin', man. You could be a star!\x01",
            "Just trust your pal here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "I don't have any intention of doing that!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_10_19C8 end

    def Function_11_1AB0(): pass

    label("Function_11_1AB0")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xA,
        (
            "Say, mister, it looks to me like you\x01",
            "aren't having the time of ya life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ain't that bad? You're in Crossbell,\x01",
            "so you gotta party your ass off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You'd be doing yourself a disservice\x01",
            "by NOT living it up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I-Is that right?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_11_1AB0 end

    def Function_12_1BB2(): pass

    label("Function_12_1BB2")

    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xA,
        (
            "Welcome, friends! I'm gonna show you\x01",
            "guys the time of your lives!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just leave everything to your\x01",
            "best bud Bishy.\x01",
            "Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "N-No thanks, we, uhh...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_12_1BB2 end

    def Function_13_1C6D(): pass

    label("Function_13_1C6D")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xA,
        (
            "Whoa. You'd be pretty dang\x01",
            "popular in my store!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Come on in. You know you wanna.\x01",
            "I'm sure it'll prove a fine story for your trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Haha... Y-You think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Well, um, I have a family, so...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_1C6D end

    def Function_14_1D4F(): pass

    label("Function_14_1D4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DDE")

    ChrTalk(
        0xB,
        "The Anniversary Festival ends today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I gotta work as hard as I can while the\x01",
            "mira is rolling in so easily.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E88")

    label("loc_1DDE")


    ChrTalk(
        0xB,
        "Glory to the Anniversary Festival!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A customer told me that today's\x01",
            "the anniversary of Crossbell's\x01",
            "birth as a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Huh, learn something new every day.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1E88")

    Jump("loc_26A4")

    label("loc_1E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1F7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EF8")

    ChrTalk(
        0xB,
        (
            "Oh, dear...\x01",
            "This won't do! Focus, Eris!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I need to concentrate on my work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F77")

    label("loc_1EF8")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "The parade was outstanding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was cheering as hard as I could\x01",
            "with the rest of the crowd!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1F77")

    Jump("loc_26A4")

    label("loc_1F7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_226C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_202A")

    ChrTalk(
        0xB,
        (
            "I had to go and check out\x01",
            "the parade for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, it's that kid who was walking\x01",
            "alongside the parade! Hard to\x01",
            "forget something that cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2267")

    label("loc_202A")


    ChrTalk(
        0x101,
        (
            "#0001F(Yeah, this person might know\x01",
            "something about Colin...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture and asked\x01",
            "if she knew anything about his disappearance.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xFE,
        "Hmm... Lemme think about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I probably saw a couple\x01",
            "of kids run by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, really?\x02\x03",
            "Did any of them resemble the child in this photo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... I'm not really sure, to be honest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not really good at using my head.\x01",
            "I just forget everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My brain is all hazy. I can't\x01",
            "even bother to remember.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FAh, okay...\x01",
            "Thanks for your cooperation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 21)

    label("loc_2267")

    Jump("loc_26A4")

    label("loc_226C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_235B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_22D7")

    ChrTalk(
        0xB,
        (
            "Oh, dear...\x01",
            "This won't do! Focus, Eris!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I need to concentrate on my work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2356")

    label("loc_22D7")

    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "The parade was outstanding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I was cheering as hard as I could\x01",
            "with the rest of the crowd!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2356")

    Jump("loc_26A4")

    label("loc_235B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(
        0xB,
        "Welcome. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Come have some fun with me, mister. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*yawn*... I'm totally spent.\x02",
    )

    CloseMessageWindow()
    Jump("loc_248D")

    label("loc_23D1")


    ChrTalk(
        0xB,
        "Welcome. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Come have some fun with me, mister. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Well?\x01",
            "I tried changing my image.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "From what I've seen, tourists tend to be\x01",
            "more receptive to this kind of look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_248D")

    Jump("loc_26A4")

    label("loc_2492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_257D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_24EB")

    ChrTalk(
        0xB,
        (
            "This festival is massive!\x01",
            "I'm going to rake in so much mira!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2578")

    label("loc_24EB")


    ChrTalk(
        0xB,
        (
            "I managed to pull in more sales than\x01",
            "any of the other girls yesterday!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "I love the Anniversary Festival!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_2578")

    Jump("loc_26A4")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2618")

    ChrTalk(
        0xB,
        (
            "The other girls and I are engaged\x01",
            "in a competition over total sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm determined to come out on top\x01",
            "by the end of the festival!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A4")

    label("loc_2618")


    ChrTalk(
        0xB,
        "Three cheers for the Anniversary Festival!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "There's so many customers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm on fire today! It's time to\x01",
            "set a daily record!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_26A4")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D4F end

    def Function_15_26A8(): pass

    label("Function_15_26A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26EF")
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        "Well, um, I have a family, so...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Jump("loc_26F2")

    label("loc_26EF")

    Call(0, 13)

    label("loc_26F2")

    TalkEnd(0xFE)
    Return()

    # Function_15_26A8 end

    def Function_16_26F6(): pass

    label("Function_16_26F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2766")
    OP_4B(0xA, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "N-No, we were...you know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "We've got places to be, sorry...\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_2769")

    label("loc_2766")

    Call(0, 12)

    label("loc_2769")

    TalkEnd(0xFE)
    Return()

    # Function_16_26F6 end

    def Function_17_276D(): pass

    label("Function_17_276D")

    TalkBegin(0xFE)

    ChrTalk(
        0xE,
        (
            "Oh, nooo! I'm being chased\x01",
            "by some nutcase!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_276D end

    def Function_18_27A5(): pass

    label("Function_18_27A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2812")
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xF,
        "I just came to watch the parade...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Wh-What are you talking about?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_2815")

    label("loc_2812")

    Call(0, 11)

    label("loc_2815")

    TalkEnd(0xFE)
    Return()

    # Function_18_27A5 end

    def Function_19_2819(): pass

    label("Function_19_2819")

    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x10,
        "Watch your mouth in front of my wife!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Outrageous!\x01",
            "You'd better watch yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_19_2819 end

    def Function_20_2891(): pass

    label("Function_20_2891")

    TalkBegin(0xFE)

    ChrTalk(
        0x11,
        (
            "I've heard some pretty unsettling\x01",
            "rumors about Crossbell's Back Alley.\x01",
            "Looks like they were substantiated...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2891 end

    def Function_21_290A(): pass

    label("Function_21_290A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AC")
    OP_29(0x46, 0x1, 0x4)

    ChrTalk(
        0x101,
        (
            "#0003F(All right, that's a wrap on the Back Alley\x01",
            "investigation.)\x02\x03",
            "#0001F(Let's try asking around Central Square\x01",
            "next!)\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)
    OP_1B(0x1, 0x0, 0x17)

    label("loc_29AC")

    Return()

    # Function_21_290A end

    def Function_22_29AD(): pass

    label("Function_22_29AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-23300, 2300, 1000, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -28300, 0, 1000, 90)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(-23300, 1300, 1000, 2500)

    def lambda_2A51():
        OP_96(0xFE, 0xFFFFA4FC, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A51)
    FadeToBright(1000, 0)
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
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(1084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3400282V#0001FIt's Lloyd.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1364, 255, 100, 0)
    Sleep(500)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400283V\x07\x05",
            "Yo, Randy here.\x01",
            "I made the rounds in East Street.\x02\x03",
            "#3400284VNo clues about the kiddo's location,\x01",
            "not even from the guild's receptionist.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3400285V\x07\x00",
            "#0008FAll right, understood.\x01",
            "I didn't have any luck in the Entertainment\x01",
            "District, either.\x02\x03",
            "#3400286V#0001FLet's continue the search for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Randy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3400287V\x07\x05",
            "Aye, aye, sir!\x07\x00\x02",
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
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -23900, 0, 1000, 90)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 0)
    OP_29(0x46, 0x1, 0x3)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_22_29AD end

    def Function_23_2D48(): pass

    label("Function_23_2D48")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    AddParty(0x5F, 0xFF, 0xFF)
    OP_68(18000, 1100, 1000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 15000, 0, 1000, 90)
    SetChrPos(0x160, 8000, 0, 1000, 90)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis056.itp")

    def lambda_2E05():
        OP_96(0xFE, 0x4650, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E05)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    NpcTalk(
        0x160,
        "Girl's Voice",
        "#3400288V#2PLong time no see.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400341V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()

    def lambda_2E94():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E94)
    Fade(500)
    SetChrPos(0x160, 13000, 0, 1000, 90)
    OP_68(17160, 1300, 1300, 0)
    MoveCamera(27, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 1600)

    def lambda_2EEE():
        OP_96(0xFE, 0x3EE4, 0x0, 0x3E8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2EEE)
    WaitChrThread(0x160, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_3121")

    ChrTalk(
        0x101,
        "#3400290V#11P#0002FOh, it's you, Renne.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x160,
        (
            "#3400291VGood day, Detective.\x02\x03",
            "#3400292VIt's been about a month since\x01",
            "we last met, hasn't it?\x02",
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

    ChrTalk(
        0x101,
        (
            "#3400293V#11P#0004FYeah, that sounds about right.\x02\x03",
            "#3400294V#0002FWhat's up? Did you come to visit\x01",
            "the antique shop again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400295V#3309F#5PIndeed. I've also come to take in the festival.\x02\x03",
            "#3400316V#3302FI quite enjoyed that lovely parade.\x01",
            "Were you able to watch it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3703")

    label("loc_3121")


    ChrTalk(
        0x101,
        "#3400297V#11P#0005FYou're...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Girl in Dress")

    AnonymousTalk(
        0xFF,
        (
            "#3400298VGood day, Detective.\x02\x03",
            "#3400299VIt's been about two months\x01",
            "since we last met, hasn't it?\x02",
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

    ChrTalk(
        0x101,
        (
            "#3400300V#11P#0005FAh...You're the girl from the doll studio.\x02\x03",
            "#3400301V#0002FLong time no see.\x01",
            "...Renne, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400302V#3306F#5PYou should really mind your manners. A lady's\x01",
            "name isn't something you just casually forget.\x02\x03",
            "#3400303V#3301FIt's your duty as a gentleman to\x01",
            "greet me as if we had just met\x01",
            "yesterday. Is that not correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400304V#11P#0012FHaha... Sorry about that, Renne.\x02\x03",
            "#3400305V#0000FSo, what are you doing in Crossbell City?\x02\x03",
            "#3400306V#0005FAre you all by yourself? Did you get lost\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400307V#3304F#5POf course not, silly. As if I could get lost.\x02\x03",
            "#3400308VI like to visit the antique shop here\x01",
            "from time to time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400309V#11P#0005FO-Oh, really?\x02\x03",
            "#3400310V#0001FIsn't it dangerous for a child to wander\x01",
            "around this part of town?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400311V#3309F#5PHehehe. Oh, you're so silly.\x01",
            "What could possibly be dangerous?\x02\x03",
            "#3400312V#3302FThe mister and miss by the club\x01",
            "are very kind to me.\x02\x03",
            "#3400313VEven those men wearing sunglasses\x01",
            "in the alley are super amusing.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400314V#11P#0011FY-You're joking, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400315V#3304F#5PMore importantly, I came to enjoy\x01",
            "the festivities today.\x02\x03",
            "#3400296V#3302FI quite enjoyed that lovely parade.\x01",
            "Were you able to watch it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3703")


    ChrTalk(
        0x101,
        (
            "#3400317V#11P#0006FAfraid not. I had to skip out on it.\x01",
            "I was busy taking care of a job.\x02\x03",
            "#3400318V#0008F(I'm worried about leaving her alone.)\x02\x03",
            "#3400319V(She's confident, but she's still a young girl.\x01",
            "I'd take her back to the studio if I wasn't in\x01",
            "the middle of an investigation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400320V#3305F#5P???\x02\x03",
            "#3400321V#3300FBy the way, Detective...\x01",
            "What are you doing all alone?\x02\x03",
            "#3400322VAre you playing another game of\x01",
            "hide-and-seek with someone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400323V#11P#0006FNo, not quite. I'm looking for a\x01",
            "missing child, actually.\x02\x03",
            "#3400324V#0000FHe supposedly disappeared during the\x01",
            "parade and has yet to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400325V#3300F#5POh, I see.\x02\x03",
            "#3400326VDo you have a photo? I might know him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400327V#11P#0002FThat's a good idea.\x01",
            "Mind giving it a look, then?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd showed Colin's picture to Renne.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)

    AnonymousTalk(
        0x160,
        (
            "#3400328V#3300F...\x02\x03",
            "#3400329V#3305F#30WOh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400330V#11P#0005FWhat's wrong?\x02\x03",
            "#3400331V#0000FDo you know him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    Sleep(300)

    ChrTalk(
        0x160,
        (
            "#3400332V#19B#23Z#5P#60WNo.\x02\x03",
            "#3400333V#2B#13Z#27B#45Z#58B#68ZRenne #60Whas never known #60Wthis child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400334V#11P#0006FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)

    ChrTalk(
        0x160,
        (
            "#3400335V#3303F#5PHowever... He's quite a cute boy, isn't he?\x02\x03",
            "#3400336V#3300FYou said you're looking for him, Detective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3400337V#11P#0000FYeah, my team split up to cover more ground.\x02\x03",
            "#3400338V#0008FI'd like to get him back to his parents ASAP,\x01",
            "but we haven't had much luck yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400339V#3304F#5PHeehee...\x02\x03",
            "#3400340V#3302FIf that's the case, then I'll grant\x01",
            "you a bit of my expertise.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3400289V#11P#0005FExpertise?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400342V#3302F#5PI told you before, did I not?\x01",
            "I'm quite skilled at hide-and-seek.\x02\x03",
            "#3400343VI'm sure it won't be much effort to\x01",
            "locate a sneaky little boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400344V#11P#0011FYeah, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3400345V#11P#0004F(Well, I was anxious about leaving her alone...\x01",
            "I guess she can accompany me for now.)\x02\x03",
            "#3400346V(If anything happens, I can always have\x01",
            "her wait for me at the SSS building.)\x02\x03",
            "#3400347V#0000FAll right. I'll be counting on you, Renne.\x02\x03",
            "#3400348VYou can assist me in my investigation\x01",
            "for a little bit, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x160,
        (
            "#3400349V#3304F#5PWhy, thank you.\x02\x03",
            "#3400350V#3302FIt's a pleasure to work with you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3400351V#11P#0002FYeah, likewise.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(18000, 1950, 1000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 18000, 0, 1000, 270)
    SetChrPos(0x1, 18000, 0, 1000, 270)
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetScenarioFlags(0xA2, 1)
    OP_29(0x46, 0x1, 0x5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_23_2D48 end

    def Function_24_40DD(): pass

    label("Function_24_40DD")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_40EC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_40EC)
    Sleep(50)

    def lambda_40FC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_40FC)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "Hey, don't just loiter around here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Beat it, or I'll beat ya!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_24_40DD end

    def Function_25_417A(): pass

    label("Function_25_417A")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FWait, I haven't finished my investigation\x01",
            "of the area yet...\x02\x03",
            "I should continue gathering more\x01",
            "information before I leave.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_25_417A end

    SaveToFile()

Try(main)
