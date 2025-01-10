from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c050b.bin",                # FileName
        "c050b",                    # MapName
        "c050b",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 3, 0, 4],
    )

    BuildStringList((
        "c050b",                  # 0
        "Barker Bishy",           # 1
        "Eris",                   # 2
        "Chief Sergei",           # 3
        "Zeit",                   # 4
        "Imelda",                 # 5
        "CGF Guardsman",          # 6
        "CGF Guardsman",          # 7
        "CGF Guardsman",          # 8
        "CGF Guardsman",          # 9
        "CGF Guardsman",          # 10
        "CGF Guardsman",          # 11
        "Mafioso",                # 12
        "Mafioso",                # 13
        "イベント用ＮＰＣ",       # 14
        "イベント用ＮＰＣ",       # 15
        "イベント用ＮＰＣ",       # 16
        "SE制御",                 # 17
        "Central Square",         # 18
        "West Street",            # 19
        "Administrative District",# 20
        "Residential District",   # 21
        "Entertainment District", # 22
        "East Street",            # 23
        "Downtown District",      # 24
        "Harbor District",        # 25
        "IBC",                    # 26
        "Station Street",         # 27
        "Back Alley",             # 28
        "Ursula Road",            # 29
        "East Crossbell Highway", # 30
        "West Crossbell Highway", # 31
        "Mainz Mountain Path",    # 32
    ))

    AddCharChip((
        "chr/ch26700.itc",                   # 00
        "chr/ch26900.itc",                   # 01
        "chr/ch31000.itc",                   # 02
        "chr/ch31100.itc",                   # 03
    ))

    DeclNpc(-7590,   0,       2980,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   1,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  5,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  6,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  7,  0x0000)

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
        "Function_0_588",          # 00, 0
        "Function_1_640",          # 01, 1
        "Function_2_6A7",          # 02, 2
        "Function_3_6C3",          # 03, 3
        "Function_4_879",          # 04, 4
        "Function_5_8D7",          # 05, 5
        "Function_6_A1D",          # 06, 6
        "Function_7_B68",          # 07, 7
        "Function_8_CC8",          # 08, 8
        "Function_9_DFE",          # 09, 9
        "Function_10_F03",         # 0A, 10
        "Function_11_FDA",         # 0B, 11
        "Function_12_11D8",        # 0C, 12
        "Function_13_1BEF",        # 0D, 13
        "Function_14_1D96",        # 0E, 14
        "Function_15_1ED7",        # 0F, 15
        "Function_16_2086",        # 10, 16
        "Function_17_21EF",        # 11, 17
        "Function_18_229B",        # 12, 18
        "Function_19_22ED",        # 13, 19
        "Function_20_230C",        # 14, 20
        "Function_21_2326",        # 15, 21
    ))


    def Function_0_588(): pass

    label("Function_0_588")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C8"),
        (1, "loc_5D4"),
        (2, "loc_5E0"),
        (3, "loc_5EC"),
        (4, "loc_5F8"),
        (5, "loc_604"),
        (6, "loc_610"),
        (SWITCH_DEFAULT, "loc_61C"),
    )


    label("loc_5C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_5F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_604")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_610")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_61C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_628")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_628")

    label("loc_63F")

    Return()

    # Function_0_588 end

    def Function_1_640(): pass

    label("Function_1_640")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A6")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_640")

    label("loc_6A6")

    Return()

    # Function_1_640 end

    def Function_2_6A7(): pass

    label("Function_2_6A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C2")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_6A7")

    label("loc_6C2")

    Return()

    # Function_2_6A7 end

    def Function_3_6C3(): pass

    label("Function_3_6C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A0")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_79B")

    label("loc_77C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79B")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_79B")

    Jump("loc_838")

    label("loc_7A0")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_838")

    label("loc_819")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_838")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_838")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_855")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)
    Jump("loc_878")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_869")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_878")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_878")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 12)

    label("loc_878")

    Return()

    # Function_3_6C3 end

    def Function_4_879(): pass

    label("Function_4_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C")
    OP_70(0x4, 0x0)
    Jump("loc_890")

    label("loc_88C")

    OP_70(0x4, 0x1E)

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    OP_70(0x5, 0x0)
    Jump("loc_8A7")

    label("loc_8A3")

    OP_70(0x5, 0x1E)

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    OP_70(0x6, 0x0)
    Jump("loc_8BE")

    label("loc_8BA")

    OP_70(0x6, 0x1E)

    label("loc_8BE")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D6")
    OP_1B(0x2, 0x0, 0x15)

    label("loc_8D6")

    Return()

    # Function_4_879 end

    def Function_5_8D7(): pass

    label("Function_5_8D7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C1")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_957")
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
    Jump("loc_9BC")

    label("loc_957")

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

    label("loc_9BC")

    Jump("loc_A11")

    label("loc_9C1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You didn't earn that and you know it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_A11")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8D7 end

    def Function_6_A1D(): pass

    label("Function_6_A1D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B07")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_A9D")
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
    Jump("loc_B02")

    label("loc_A9D")

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

    label("loc_B02")

    Jump("loc_B5C")

    label("loc_B07")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The real Tio would be disappointed in you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_B5C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A1D end

    def Function_7_B68(): pass

    label("Function_7_B68")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C52")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x69, 1)"), scpexpr(EXPR_END)), "loc_BE8")
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
    Jump("loc_C4D")

    label("loc_BE8")

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

    label("loc_C4D")

    Jump("loc_CBC")

    label("loc_C52")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If I catch you using debug again,\x01",
            "I'm gonna whoop your de-butt.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_CBC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B68 end

    def Function_8_CC8(): pass

    label("Function_8_CC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(
        0x8,
        "Hey, why not come hang out with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You're missin' out. I know how to\x01",
            "make ya happy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFA")

    label("loc_D38")


    ChrTalk(
        0x8,
        "You guys look like a bunch of cool cats.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Nice, nice. You guys are gonna\x01",
            "make the chicks at our shop\x01",
            "real happy if you come on in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Don't be shy, now. Step right in.\x01",
            "Hahahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DFA")

    TalkEnd(0xFE)
    Return()

    # Function_8_CC8 end

    def Function_9_DFE(): pass

    label("Function_9_DFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E7E")

    ChrTalk(
        0x9,
        "I'm feeling extra motivated today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Heehee. I'm going to spend all my time\x01",
            "reeling in more customers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EFF")

    label("loc_E7E")


    ChrTalk(
        0x9,
        "Teehee, I'm Eris. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey there, sir. Do you wanna\x01",
            "hang out with a girl like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I've always got time for you~.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_EFF")

    TalkEnd(0xFE)
    Return()

    # Function_9_DFE end

    def Function_10_F03(): pass

    label("Function_10_F03")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    OP_68(0, 1950, 42500, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, -2000, 0, 42000, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 2000, 0, 42000, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_68(0, 1950, 45500, 8000)
    MoveCamera(0, 13, 0, 8000)
    SetCameraDistance(21000, 8000)
    FadeToBright(2000, 0)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_F03 end

    def Function_11_FDA(): pass

    label("Function_11_FDA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch26800.itc", 0x1E)
    SetChrPos(0x101, -3800, 0, 6400, 0)
    SetChrPos(0x102, -3800, 0, 6400, 0)
    SetChrPos(0x103, -3800, 0, 6400, 0)
    SetChrPos(0x104, -3800, 0, 6400, 0)
    OP_68(-10000, 2450, 800, 0)
    MoveCamera(325, 15, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(12500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x15, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 15000, 0, 2000, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, -15000, 0, 500, 90)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, -15400, 0, -500, 90)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)

    def lambda_10EF():
        OP_98(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10EF)
    Sleep(50)

    def lambda_110C():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_110C)
    Sleep(50)

    def lambda_1129():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1129)
    OP_68(6000, 2450, 800, 9000)
    SetCameraDistance(14500, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(2000)
    OP_68(0, 1950, 42500, 0)
    MoveCamera(0, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 1950, 45500, 7000)
    MoveCamera(0, 13, 0, 7000)
    SetCameraDistance(21000, 7000)
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_FDA end

    def Function_12_11D8(): pass

    label("Function_12_11D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31252.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch09000.itc", 0x29)
    LoadChrToIndex("chr/ch00150.itc", 0x2A)
    LoadChrToIndex("chr/ch00151.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00950.itc", 0x2E)
    LoadChrToIndex("chr/ch00951.itc", 0x2F)
    LoadChrToIndex("chr/ch00952.itc", 0x30)
    LoadChrToIndex("apl/ch50509.itc", 0x31)
    LoadChrToIndex("chr/ch00152.itc", 0x32)
    LoadChrToIndex("chr/ch31353.itc", 0x33)
    LoadChrToIndex("chr/ch31352.itc", 0x34)
    LoadChrToIndex("apl/ch50515.itc", 0x35)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "battle\\btgun00.eff")
    LoadEffect(0x2, "event\\eva03_00.eff")
    LoadEffect(0x3, "battle\\ms00001.eff")
    OP_68(8500, 900, 700, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, 30000, 0, 700, 270)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 33800, 0, 1300, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 32600, 0, 400, 270)
    SetChrPos(0x104, 31600, 0, 1700, 270)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 38700, 0, 1700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 39500, 0, 300, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 35400, 0, 300, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0xD, 33000, 0, 700, 270)
    SetChrPos(0xE, 34100, 0, 1800, 270)
    SetChrPos(0xF, 34200, 0, -200, 270)
    SetChrPos(0x10, 30000, 0, 700, 270)
    SetChrPos(0x11, 31100, 0, 1800, 270)
    SetChrPos(0x12, 31200, 0, -200, 270)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2300, 0, 2200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2600, 0, -1100, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xC, 5600, 800, 6400, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    def lambda_1500():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1500)
    Sleep(50)

    def lambda_151D():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_151D)
    Sleep(50)

    def lambda_153A():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_153A)
    Sleep(50)

    def lambda_1557():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1557)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 3, 0, 2)

    def lambda_1598():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1598)
    Sleep(50)

    def lambda_15B5():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_15B5)
    Sleep(50)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)

    def lambda_15DA():
        OP_96(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15DA)

    def lambda_15F4():

        label("loc_15F4")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_15F4")

    QueueWorkItem2(0x8, 2, lambda_15F4)

    def lambda_1606():

        label("loc_1606")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1606")

    QueueWorkItem2(0x9, 2, lambda_1606)
    OP_68(2500, 900, 700, 6000)
    MoveCamera(47, 17, -5, 6000)
    SetCameraDistance(14500, 6000)
    FadeToBright(2000, 0)
    BeginChrThread(0x18, 1, 0, 20)
    OP_6F(0x79)
    BeginChrThread(0xC, 3, 0, 18)
    Sleep(1000)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x18, 0x1)

    ChrTalk(
        0x8,
        "#5200158V#11PIs this a festival or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200159V#11PWhat a weird crowd.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)

    ChrTalk(
        0xC,
        (
            "#5200160V#5PWhat's with all the commotion?\x01",
            "It's too damn noisy!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1720():

        label("loc_1720")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1720")

    QueueWorkItem2(0xC, 2, lambda_1720)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)

    def lambda_176E():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_176E)
    Sleep(50)

    def lambda_178B():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_178B)
    Sleep(50)

    def lambda_17A8():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17A8)
    Sleep(50)

    def lambda_17C5():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_17C5)
    Sleep(50)

    def lambda_17E2():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_17E2)
    Sleep(50)

    def lambda_17FF():
        OP_98(0xFE, 0xFFFF63C0, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17FF)
    Sleep(750)

    def lambda_181C():

        label("loc_181C")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_181C")

    QueueWorkItem2(0x8, 2, lambda_181C)
    Sleep(50)

    def lambda_1831():

        label("loc_1831")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1831")

    QueueWorkItem2(0x9, 2, lambda_1831)
    Sleep(2500)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_187C():
        OP_98(0xFE, 0xFFFFFDA8, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_187C)
    Sleep(50)

    def lambda_1899():
        OP_98(0xFE, 0xFFFFFDA8, 0x0, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1899)
    Sleep(150)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x29)
    SetChrSubChip(0xC, 0x0)
    Sound(819, 0, 100, 0)
    Sound(926, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    def lambda_18E9():
        OP_98(0xFE, 0x0, 0x0, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18E9)
    BeginChrThread(0xC, 3, 0, 19)

    ChrTalk(
        0xC,
        "#5200161V#5P#14AUwaaahhh!\x02",
    )

    Sleep(2000)

    ChrTalk(
        0x8,
        "#5200162V#11P#18AWh-What the hell just happened?\x02",
    )

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0xB, 0x8)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xA, 1)
    OP_64(0xC)
    OP_64(0x9)
    OP_64(0x8)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Fade(500)
    OP_68(-13500, 900, 700, 0)
    MoveCamera(50, 33, -5, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_EE(0x0, 0x1)
    SetChrChipByIndex(0x10A, 0x30)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, -22000, 0, 1400, 90)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x4)
    SetChrPos(0xA, -22300, 0, -200, 90)
    SetChrPos(0xD, 5000, 0, 700, 270)
    SetChrPos(0xE, 6100, 0, 1800, 270)
    SetChrPos(0xF, 6200, 0, -200, 270)
    SetChrPos(0x10, 0, 0, 700, 270)
    SetChrPos(0x11, 1100, 0, 1800, 270)
    SetChrPos(0x12, 1200, 0, -200, 270)

    def lambda_1A94():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A94)
    BeginChrThread(0x10, 3, 0, 17)
    Sleep(50)

    def lambda_1AB7():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AB7)
    BeginChrThread(0x11, 3, 0, 17)
    Sleep(50)

    def lambda_1ADA():
        OP_98(0xFE, 0xFFFFB9B0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1ADA)
    BeginChrThread(0x12, 3, 0, 17)
    Sleep(50)

    def lambda_1AFD():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1AFD)
    BeginChrThread(0xD, 3, 0, 16)
    Sleep(50)

    def lambda_1B20():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B20)
    BeginChrThread(0xE, 3, 0, 16)
    Sleep(50)

    def lambda_1B43():
        OP_98(0xFE, 0xFFFFB5C8, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1B43)
    BeginChrThread(0xF, 3, 0, 16)
    OP_0D()
    Sleep(900)
    OP_68(-18500, 900, 700, 1500)
    MoveCamera(40, 23, -5, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    BeginChrThread(0xA, 3, 0, 15)
    Sleep(50)
    BeginChrThread(0x10A, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(3500)
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_EE(0x0, 0xA)
    EndChrThread(0x10A, 0x3)
    EndChrThread(0xA, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0xB, 0x8)
    SetScenarioFlags(0x5C, 2)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_11D8 end

    def Function_13_1BEF(): pass

    label("Function_13_1BEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D95")
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18900, 0, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18000, 0, -1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -19100, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -20000, 0, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -19400, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -18200, 0, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -17700, 0, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Jump("Function_13_1BEF")

    label("loc_1D95")

    Return()

    # Function_13_1BEF end

    def Function_14_1D96(): pass

    label("Function_14_1D96")

    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    label("loc_1DE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ED6")
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    Jump("loc_1DE4")

    label("loc_1ED6")

    Return()

    # Function_14_1D96 end

    def Function_15_1ED7(): pass

    label("Function_15_1ED7")

    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    label("loc_1F25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2085")
    SetChrSubChip(0xA, 0x5)
    Sleep(150)
    SetChrSubChip(0xA, 0x6)
    Sleep(100)
    SetChrSubChip(0xA, 0x7)
    Sound(531, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x0)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0xA, 0x5)
    Sleep(150)
    SetChrSubChip(0xA, 0x6)
    Sleep(100)
    SetChrSubChip(0xA, 0x7)
    Sound(531, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0x4)
    Sleep(100)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x0)
    Sleep(70)
    SetChrSubChip(0xA, 0x1)
    Sleep(70)
    SetChrSubChip(0xA, 0x2)
    Sleep(70)
    SetChrSubChip(0xA, 0x3)
    Sleep(70)
    SetChrSubChip(0xA, 0x4)
    Sleep(600)
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    Jump("loc_1F25")

    label("loc_2085")

    Return()

    # Function_15_1ED7 end

    def Function_16_2086(): pass

    label("Function_16_2086")

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2092")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21EE")

    def lambda_20A2():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20A2)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(356, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("loc_2092")

    label("loc_21EE")

    Return()

    # Function_16_2086 end

    def Function_17_21EF(): pass

    label("Function_17_21EF")

    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2242():
        OP_9C(0xFE, 0x5DC, 0x0, 0x0, 0x12C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2242)

    def lambda_225F():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_225F)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_17_21EF end

    def Function_18_229B(): pass

    label("Function_18_229B")

    ClearMapObjFlags(0x0, 0x10)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_22BB():
        OP_96(0xFE, 0x15E0, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_22BB)

    def lambda_22D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_22D5)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0xE1, 0x1F4)
    Return()

    # Function_18_229B end

    def Function_19_22ED(): pass

    label("Function_19_22ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_230B")
    OP_A1(0xFE, 0xFA0, 0x8, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_19_22ED")

    label("loc_230B")

    Return()

    # Function_19_22ED end

    def Function_20_230C(): pass

    label("Function_20_230C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2325")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_20_230C")

    label("loc_2325")

    Return()

    # Function_20_230C end

    def Function_21_2326(): pass

    label("Function_21_2326")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2472")

    ChrTalk(
        0x104,
        (
            "#0301FRevache & Co... They still seem to be\x01",
            "hangin' in there ever since the auction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FThey appeared to be laying low\x01",
            "after the incident with KeA, but...\x02\x03",
            "...it's looking like business is back to\x01",
            "usual with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FWell, it was a strange string of events...\x01",
            "Let's not bother them for now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 2)
    Jump("loc_24DD")

    label("loc_2472")


    ChrTalk(
        0x101,
        (
            "#0001F(Revache's building is up ahead.)\x02\x03",
            "(Let's stay away for now. We wouldn't\x01",
            "want to provoke them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DD")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Return()

    # Function_21_2326 end

    SaveToFile()

Try(main)
