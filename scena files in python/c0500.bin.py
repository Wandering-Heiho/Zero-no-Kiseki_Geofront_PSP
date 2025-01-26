from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0500.bin",                # FileName
        "c0500",                    # MapName
        "c0500",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0500",                  # 0
        "Mafioso",                # 1
        "Mafioso",                # 2
        "Barker Bishy",           # 3
        "Eris",                   # 4
        "Officer Franz",          # 5
        "Garcia",                 # 6
        "Grace",                  # 7
        "Mafioso",                # 8
        "Mafioso",                # 9
        "Mafioso",                # 10
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
        "chr/ch26700.itc",                   # 00
        "chr/ch26900.itc",                   # 01
        "chr/ch31000.itc",                   # 02
        "chr/ch31100.itc",                   # 03
        "chr/ch31900.itc",                   # 04
        "chr/ch30000.itc",                   # 05
    ))

    DeclNpc(-2000,   0,       41700,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(2000,    0,       41700,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-7590,   0,       2980,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-6170,   0,       1399,    90,   261,  0x0, 0,   1,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(1090,    0,       41770,   180,  389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -0.10000000149011612,  43.849998474121094,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.05000000074505806,   -21.924999237060547,   0.10000000149011612,   1.0])

    DeclActor(-3210,   5800,    22030,   1200,    -3210,   6800,    22030,   0x007C, 0,  4,  0x0000)
    DeclActor(-10590,  5900,    9660,    1200,    -10590,  6900,    9660,    0x007C, 0,  5,  0x0000)
    DeclActor(11410,   0,       7030,    1200,    11410,   1000,    7030,    0x007C, 0,  6,  0x0000)
    DeclActor(-11950,  0,       3000,    3500,    -11940,  1500,    3060,    0x007C, 0,  19, 0x0000)
    DeclActor(19100,   0,       4000,    3500,    19100,   1500,    4000,    0x007C, 0,  20, 0x0000)

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
    PlaceName(106.0, 0.0, -10.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_5CC",          # 00, 0
        "Function_1_684",          # 01, 1
        "Function_2_6EB",          # 02, 2
        "Function_3_A09",          # 03, 3
        "Function_4_C65",          # 04, 4
        "Function_5_DCC",          # 05, 5
        "Function_6_F6C",          # 06, 6
        "Function_7_10C0",         # 07, 7
        "Function_8_11EB",         # 08, 8
        "Function_9_12BD",         # 09, 9
        "Function_10_241E",        # 0A, 10
        "Function_11_26A1",        # 0B, 11
        "Function_12_3C1B",        # 0C, 12
        "Function_13_3EAE",        # 0D, 13
        "Function_14_409A",        # 0E, 14
        "Function_15_417B",        # 0F, 15
        "Function_16_4197",        # 10, 16
        "Function_17_4266",        # 11, 17
        "Function_18_430B",        # 12, 18
        "Function_19_43C6",        # 13, 19
        "Function_20_447D",        # 14, 20
        "Function_21_44F6",        # 15, 21
        "Function_22_494E",        # 16, 22
        "Function_23_5C11",        # 17, 23
        "Function_24_72F2",        # 18, 24
        "Function_25_7318",        # 19, 25
        "Function_26_735F",        # 1A, 26
        "Function_27_73A6",        # 1B, 27
        "Function_28_73CF",        # 1C, 28
        "Function_29_8C8C",        # 1D, 29
        "Function_30_8CF9",        # 1E, 30
        "Function_31_8D28",        # 1F, 31
        "Function_32_8D54",        # 20, 32
        "Function_33_9299",        # 21, 33
        "Function_34_9C78",        # 22, 34
        "Function_35_A036",        # 23, 35
        "Function_36_A3A2",        # 24, 36
        "Function_37_A46A",        # 25, 37
        "Function_38_ADB1",        # 26, 38
    ))


    def Function_0_5CC(): pass

    label("Function_0_5CC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_60C"),
        (1, "loc_618"),
        (2, "loc_624"),
        (3, "loc_630"),
        (4, "loc_63C"),
        (5, "loc_648"),
        (6, "loc_654"),
        (SWITCH_DEFAULT, "loc_660"),
    )


    label("loc_60C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_618")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_624")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_630")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_63C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_648")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_654")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_660")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_66C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_683")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_66C")

    label("loc_683")

    Return()

    # Function_0_5CC end

    def Function_1_684(): pass

    label("Function_1_684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EA")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_684")

    label("loc_6EA")

    Return()

    # Function_1_684 end

    def Function_2_6EB(): pass

    label("Function_2_6EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DA")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AD")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_7CC")

    label("loc_7AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CC")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_7CC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87B")

    label("loc_7DA")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_853")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_872")

    label("loc_853")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_872")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_872")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    Event(0, 22)
    Jump("loc_942")

    label("loc_8A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C2")
    Event(0, 28)
    Jump("loc_942")

    label("loc_8C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E1")
    Event(0, 32)
    Jump("loc_942")

    label("loc_8E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_905")
    Event(0, 33)
    Jump("loc_942")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91B")
    Event(0, 33)
    Jump("loc_942")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_931")
    Event(0, 33)
    Jump("loc_942")

    label("loc_931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Event(0, 33)

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_951")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 23)

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_95F")
    ClearChrFlags(0xC, 0x80)

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_977")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_9D9")

    label("loc_977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9D9")
    SetChrPos(0xB, 3630, 0, 2500, 180)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, -1100, 0, 37580, 135)
    SetChrPos(0x10, 880, 0, 37580, 270)
    SetChrPos(0x11, 320, 0, 36160, 315)

    label("loc_9D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F1")
    OP_C7(0x1, 0x1000)

    label("loc_9F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A08")
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_A08")

    Return()

    # Function_2_6EB end

    def Function_3_A09(): pass

    label("Function_3_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A25")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A41")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A79")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_A8B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E")
    OP_70(0x4, 0x0)
    Jump("loc_AA2")

    label("loc_A9E")

    OP_70(0x4, 0x1E)

    label("loc_AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB5")
    OP_70(0x5, 0x0)
    Jump("loc_AB9")

    label("loc_AB5")

    OP_70(0x5, 0x1E)

    label("loc_AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")
    OP_70(0x6, 0x0)
    Jump("loc_AD0")

    label("loc_ACC")

    OP_70(0x6, 0x1E)

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEC")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_AFE")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AFE")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_AFE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_B16")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2E")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B41")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7E")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B91")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA8")
    OP_1B(0x2, 0x0, 0x25)

    label("loc_BA8")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC0")
    OP_1B(0x1, 0x0, 0x26)

    label("loc_BC0")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BD6")
    Jump("loc_C43")

    label("loc_BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C43")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BF0")
    Jump("loc_C43")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_BFE")
    Jump("loc_C43")

    label("loc_BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_C1F")
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x5, 0x0, 0x11)
    Jump("loc_C43")

    label("loc_C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_C43")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x6, 0x0, 0x12)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5F")
    Jump("loc_C64")

    label("loc_C5F")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_C64")

    Return()

    # Function_3_A09 end

    def Function_4_C65(): pass

    label("Function_4_C65")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4F")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_CE5")
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
    Jump("loc_D4A")

    label("loc_CE5")

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

    label("loc_D4A")

    Jump("loc_DC0")

    label("loc_D4F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The last thing I want to do is hurt you...\x01",
            "but it's still on the list.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_DC0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C65 end

    def Function_5_DCC(): pass

    label("Function_5_DCC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB6")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x397, 1)"), scpexpr(EXPR_END)), "loc_E4C")
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
    Jump("loc_EB1")

    label("loc_E4C")

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

    label("loc_EB1")

    Jump("loc_F60")

    label("loc_EB6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A treasure chest walked into a bar.\x01",
            "Obviously it was a mimic and immediately slaughtered.\x01",
            "Poor thing didn't even get a drink...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_F60")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_DCC end

    def Function_6_F6C(): pass

    label("Function_6_F6C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1056")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x69, 1)"), scpexpr(EXPR_END)), "loc_FEC")
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
    Jump("loc_1051")

    label("loc_FEC")

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

    label("loc_1051")

    Jump("loc_10B4")

    label("loc_1056")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "So ya finally figured out how\x01",
            "to get to me, did ya?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10B4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F6C end

    def Function_7_10C0(): pass

    label("Function_7_10C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1166")

    ChrTalk(
        0x8,
        (
            "The hell do you think you're doing, brats?\x01",
            "You don't got any business here. Scram.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe. Unless, you came here for\x01",
            "some of the boss' love?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E7")

    label("loc_1166")


    ChrTalk(
        0x8,
        (
            "Hey, kids. The exit is thataway.\x01",
            "Now that you know, piss off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'd hate to see somethin' bad happen\x01",
            "to ya, so get lost.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E7")

    TalkEnd(0xFE)
    Return()

    # Function_7_10C0 end

    def Function_8_11EB(): pass

    label("Function_8_11EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(
        0xFE,
        (
            "You pests plannin' on loitering\x01",
            "around here for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B9")

    label("loc_123A")


    ChrTalk(
        0x9,
        (
            "You tellin' me that you have\x01",
            "business with Revache & Co?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmph, doesn't sound like you're\x01",
            "here to meet with the boss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B9")

    TalkEnd(0xFE)
    Return()

    # Function_8_11EB end

    def Function_9_12BD(): pass

    label("Function_9_12BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_140E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1368")

    ChrTalk(
        0xA,
        (
            "Heh heh heh... Are there any good\x01",
            "customers ripe for the picking here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'll show 'em the happiest place\x01",
            "in all of Crossbell!\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1409")

    label("loc_1368")


    ChrTalk(
        0xA,
        (
            "When'd it get dark? I didn't\x01",
            "notice the sun setting.\x01",
            "Today's been a weird one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, whatever. I think I'll open up shop.\x01",
            "After all, time is money.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1409")

    Jump("loc_241A")

    label("loc_140E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(
        0xFE,
        (
            "The heck...? The street's all quiet\x01",
            "again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Makes me feel like this normally\x01",
            "lively street's been stained with\x01",
            "somethin' ugly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Man, it's just too quiet.\x02",
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_14C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_END)), "loc_166B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15B2")

    ChrTalk(
        0xA,
        (
            "(Rumor has it that guy was in a jaeger corps.\x01",
            "I've always heard that jaegers live to die...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(Sonuva Bishy, I've gotta get a hold of myself!\x01",
            "Touching this issue's only gonna bring bad luck.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1666")

    label("loc_15B2")


    ChrTalk(
        0xA,
        (
            "(That rough-looking gentleman was one\x01",
            "of them head honchos at Revache, yeah?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "(You guys up to no good? You're gonna\x01",
            "have trouble escaping if you catch\x01",
            "his attention.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1666")

    Jump("loc_174B")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(
        0xFE,
        (
            "Why the heck's it so quiet today?\x01",
            "Barely anybody's passed through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna start cryin' if I don't get any\x01",
            "customers soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174B")

    label("loc_1704")


    ChrTalk(
        0xFE,
        (
            "Why the heck's it so quiet today?\x01",
            "Maybe it's just my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_241A")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1832")

    ChrTalk(
        0xA,
        (
            "Ah! Hey, you! Mister! You over there!\x01",
            "I got some real excitin' news for ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We've started a brand new service!\x01",
            "A two-hour session is just 1,000 mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How 'bout it, mister?\x01",
            "Wanna take a small peek?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_1832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_19A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18CE")

    ChrTalk(
        0xA,
        "It's finally here... The diet's 'boutta start!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This and the Anniversary Festival are\x01",
            "the best times of the year!\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A2")

    label("loc_18CE")


    ChrTalk(
        0xA,
        "It's finally here... The diet's 'boutta start!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The festival's pretty damn profitable, but\x01",
            "the diet sessions bring in a helluva lotta\x01",
            "customers, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Time to line my pockets with mira!\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19A2")

    Jump("loc_241A")

    label("loc_19A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A57")

    ChrTalk(
        0xA,
        (
            "I may be a scary-lookin' dude, but\x01",
            "I promise I'm all barker and no bite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Our pretty ladies are ready to give ya\x01",
            "the time of your life! Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1A57")


    ChrTalk(
        0xA,
        (
            "We're all gathered together to throw a\x01",
            "nice little party for our newcomers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We had three new chicks join the team.\x01",
            "Tryin' to get 'em used to workin' here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hahaha!\x01",
            "We're givin' our fine customers the\x01",
            "best treat today!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B42")

    Jump("loc_241A")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C4A")

    ChrTalk(
        0xFE,
        (
            "Phew... I'm beat.\x01",
            "One of our girls ended up quittin' her\x01",
            "job yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heheheh. No harm done. There's plenty\x01",
            "of fish in this fine sea of women.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway... How 'bout it, mister?\x01",
            "Did ya know we're havin' a\x01",
            "happy hour special today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_1C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CFA")

    ChrTalk(
        0xA,
        (
            "Oh? Ya come here to have a good time,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wouldn't loiter 'round these parts\x01",
            "at a time like this.\x01",
            "One little mistake could cost ya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAC")

    label("loc_1CFA")


    ChrTalk(
        0xA,
        "Good day, pals...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What's the matter, mister?\x01",
            "Gotta say, you ain't lookin' too hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "C'mon, I know just the remedy for you.\x01",
            "Now, come! Follow your friend, Bishy!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1DAC")

    Jump("loc_241A")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1F17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E4E")

    ChrTalk(
        0xA,
        (
            "What's goin' on in this city?\x01",
            "Mutts won't stop barking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It'd help my sanity if those bad dudes\x01",
            "kept down the noise a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F12")

    label("loc_1E4E")


    ChrTalk(
        0xA,
        (
            "Those bad dudes have been makin'\x01",
            "a racket lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Man, I'm in a pickle here.\x01",
            "Our store is right next to that building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How the hell am I supposed to\x01",
            "attract customers like this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F12")

    Jump("loc_241A")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FC4")

    ChrTalk(
        0xFE,
        (
            "Hey, c'mere.\x01",
            "Check out this necklace I just bought.\x01",
            "Ain't it shiny as hell?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha ha! I love bein' a barker!\x01",
            "One of the best decisions I ever made!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2031")

    ChrTalk(
        0xA,
        (
            "The store's suffered a bit of a heavy loss...\x01",
            "Can't ya cut us some slack?! Damn!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FC")

    label("loc_2031")


    ChrTalk(
        0xFE,
        "Just had a bracer come into the shop...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Didn't say much, but he walked out\x01",
            "with one of the girls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The jackass didn't even book a reservation\x01",
            "with her! Can't he cut us some damn slack?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_20FC")

    Jump("loc_241A")

    label("loc_2101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_21DC")

    ChrTalk(
        0xFE,
        "We gotta lotta ladies workin' here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kinda hard to get customers comin' in\x01",
            "all day, but they still get paid damn well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some of 'em receive payment in advance.\x01",
            "Man, everyone's a greedy ass...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_21DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_22CD")

    ChrTalk(
        0xA,
        (
            "Good day, all.\x01",
            "See all the tourists today, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I gotta reel 'em into the store and use\x01",
            "my services to make 'em all real happy.\x01",
            "I'd be real happy, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "How 'bout it, guys? Let's all\x01",
            "become happy together!\x01",
            "Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_22CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_235C")

    ChrTalk(
        0xA,
        (
            "Yo, I wouldn't head too deep\x01",
            "into that alley there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Bad dudes back there, ya hear?\x01",
            "Hehe. Worse than us, even.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235F")

    label("loc_235C")

    Call(0, 10)

    label("loc_235F")

    Jump("loc_241A")

    label("loc_2364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 2)), scpexpr(EXPR_END)), "loc_2417")

    ChrTalk(
        0xA,
        (
            "I sure wish they'd find another\x01",
            "alley to do business in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If a person like me was caught back there,\x01",
            "my ass'd get kicked so hard, it'd be gone!\x01",
            "Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_241A")

    label("loc_2417")

    Call(0, 10)

    label("loc_241A")

    TalkEnd(0xFE)
    Return()

    # Function_9_12BD end

    def Function_10_241E(): pass

    label("Function_10_241E")


    ChrTalk(
        0xA,
        (
            "You fine folks tourists, by any chance?\x01",
            "You free right now? How 'bout comin'\x01",
            "into my humble shop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Leave it to Bishy! I'll introduce\x01",
            "you to a real wonderful place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "C'mon, don't be shy. Follow me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWhat a disgustingly enthusiastic man...\x01",
            "And in such an unlawful line of business...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x103, 500)
    Sleep(500)

    ChrTalk(
        0xA,
        "Oh, man. You guys brought a kid with ya?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Ah, whatever. It's fine.\x01",
            "I'll overlook her this one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This ain't a good place for kids to\x01",
            "be in, little lady.\x01",
            "You haven't realized that yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0201F(*glare*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Haha... I can tell Tio doesn't enjoy being\x01",
            "treated as a child one bit.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 2)
    Return()

    # Function_10_241E end

    def Function_11_26A1(): pass

    label("Function_11_26A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2774")

    ChrTalk(
        0xB,
        (
            "The CPD has been going in and out\x01",
            "of the Back Alley all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sometimes I can't help but wonder\x01",
            "if they're really the good guys. It's not\x01",
            "like police corruption doesn't exist.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2863")

    label("loc_2774")


    ChrTalk(
        0xB,
        (
            "The police have been investigating\x01",
            "the Back Alley lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's because of that place over there.\x01",
            "I wouldn't go there, if I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Are the police actually the good guys?\x01",
            "Aren't they in the pockets of those\x01",
            "black suits?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2863")

    Jump("loc_3C17")

    label("loc_2868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2917")

    ChrTalk(
        0xB,
        (
            "I need to come up with a catchphrase\x01",
            "that'll pull me ahead of my rivals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm, hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Geez, you idiots!\x01",
            "You're breaking my concentration!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EA")

    label("loc_2917")


    ChrTalk(
        0xB,
        "Heyyy there, I'm Eris! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hey there, time. Wanna have some fun?\x01",
            "I can show you a good mister! ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "...Hmmm. That seemed wrong. I feel\x01",
            "like I messed up the lines again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29EA")

    Jump("loc_3C17")

    label("loc_29EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AA0")

    ChrTalk(
        0xB,
        (
            "Nooo! I'm going to pull in less sales\x01",
            "than my rivals if this keeps up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm... This isn't looking too great.\x01",
            "I've gotta come up with more ideas!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2AA0")


    ChrTalk(
        0xB,
        (
            "Hmm, the Back Alley feels a little\x01",
            "ominous today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I snuck a peek into that alleyway over there,\x01",
            "but I was met with the glares of those men\x01",
            "in black suits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "What's their deal? I should probably\x01",
            "quit working for the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2B8C")

    Jump("loc_3C17")

    label("loc_2B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C31")

    ChrTalk(
        0xB,
        (
            "I managed to book my first reservation!\x01",
            "I'm sooo happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Okay, I've gotta keep working as hard as\x01",
            "I can until that reservation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D09")

    label("loc_2C31")


    ChrTalk(
        0xB,
        (
            "Hehe. A customer requested me by\x01",
            "name today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Isn't that great? You're jealous, aren't you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not really sure why, but we end up getting\x01",
            "way more reservations during the diet session.\x01",
            "Hehe, lucky me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D09")

    Jump("loc_3C17")

    label("loc_2D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DE0")

    ChrTalk(
        0xB,
        (
            "The Anniversary Festival may have ended,\x01",
            "but I'm still full of energy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heheh. Look out, girls! This gal's going to use\x01",
            "her adult charms to blow you out of the\x01",
            "water next month!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA3")

    label("loc_2DE0")


    ChrTalk(
        0xB,
        (
            "I snagged a few more customers during the\x01",
            "festival compared to my rivals.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        "Haha! I am victorious! Take that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "This is the first time I've come out on top!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2EA3")

    Jump("loc_3C17")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F65")

    ChrTalk(
        0xB,
        (
            "That sister gave me the steepest furrowed\x01",
            "eyebrows I'd ever seen in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hah, feel free to keep it up.\x01",
            "You're the one that's gonna look like a grandma.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AE")

    label("loc_2F65")


    ChrTalk(
        0xB,
        (
            "My shoulders have been kinda stiff lately,\x01",
            "so I went to the church for some meds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The sister looked pretty disappointed\x01",
            "when I told her I was a hostess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not only that, but she had the audacity\x01",
            "to start lecturing me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sweet Aidios, what was her deal?! Do people\x01",
            "really think hostesses are brainless bimbos?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30AE")

    Jump("loc_3C17")

    label("loc_30B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3166")

    ChrTalk(
        0xB,
        (
            "Drunk customers can get pretty clingy.\x01",
            "They can't seem to leave me alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* Can't say I'm too proud over how\x01",
            "poor last night's sales were...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_326D")

    label("loc_3166")


    ChrTalk(
        0xB,
        (
            "*yawn*...\x01",
            "I'm so sleepy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had to deal with an awfully persistent\x01",
            "customer last night. He was definitely\x01",
            "a little too much on the handsy side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh* Just my luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's starting to look like my rivals might\x01",
            "end up overtaking me this month.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_326D")

    Jump("loc_3C17")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_32FC")

    ChrTalk(
        0xB,
        (
            "Teehee. It's almost time for\x01",
            "business to start booming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hey there, I'm Eris! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "All right, it's crunch time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C17")

    label("loc_32FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_348F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33A6")

    ChrTalk(
        0xB,
        (
            "Business always gets driven away when\x01",
            "the police conduct a stakeout around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Sheesh. I wish they'd hurry up and\x01",
            "go somewhere else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348A")

    label("loc_33A6")


    ChrTalk(
        0xB,
        (
            "The police just came by to\x01",
            "gather some information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm guessing it has to do with the recent\x01",
            "disturbance in one of the nearby shops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "C'mon, ask what you want. Just, please...\x01",
            "Don't get in the way of business!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_348A")

    Jump("loc_3C17")

    label("loc_348F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3518")

    ChrTalk(
        0xB,
        "My shoulders have been so stiff lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think I might go to the church and see\x01",
            "if they have a remedy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3611")

    label("loc_3518")


    ChrTalk(
        0xB,
        (
            "All of my rivals' sales have\x01",
            "been skyrocketing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I feel screwed. My shoulders start\x01",
            "killing me when my workload increases...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* Yeah, I think it's about time I\x01",
            "go to the church and see if they have\x01",
            "any meds that'll help me out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3611")

    Jump("loc_3C17")

    label("loc_3616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3682")

    ChrTalk(
        0xB,
        (
            "I'd stay away from those people,\x01",
            "if I were you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sigh* I screwed up today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3740")

    label("loc_3682")


    ChrTalk(
        0xB,
        (
            "I accidentally started talking to one of\x01",
            "the black suits walking by just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "They glared at me with the eyes of a devil.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*sigh* Those guys are just\x01",
            "as scary as they look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3740")

    Jump("loc_3C17")

    label("loc_3745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_37D0")

    ChrTalk(
        0xB,
        (
            "Well, I dunno. I'm not exactly the\x01",
            "brightest orbal lamp on the street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Arrrgh! What am I supposed to do?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_385E")

    label("loc_37D0")


    ChrTalk(
        0xB,
        (
            "If I let things keep going this way,\x01",
            "my rivals are going to outpace me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I need to somehow think of a\x01",
            "way to beat them, and fast!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_385E")

    Jump("loc_3C17")

    label("loc_3863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38B1")

    ChrTalk(
        0xB,
        (
            "They're so inconsiderate.\x01",
            "It really ticks me off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394F")

    label("loc_38B1")


    ChrTalk(
        0xB,
        (
            "Those black suits caused a huge\x01",
            "commotion last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wasn't able to reel in a single\x01",
            "customer because of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oooh, now I'm really mad!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_394F")

    Jump("loc_3C17")

    label("loc_3954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_39F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_39EC")

    ChrTalk(
        0xB,
        (
            "I've been competing for sales with\x01",
            "my rival gals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "B-But, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-It's looking like I'm going to lose this month!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39EF")

    label("loc_39EC")

    Call(0, 12)

    label("loc_39EF")

    Jump("loc_3C17")

    label("loc_39F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 3)), scpexpr(EXPR_END)), "loc_3C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B84")

    ChrTalk(
        0xFE,
        (
            "I guess a promise doesn't mean\x01",
            "much coming from Randy Orlando.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So much for the good time I was\x01",
            "promised. I totally got stood up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FOh, yeah... Think I was busy chattin'\x01",
            "up this stunnin' babe at the bar that day.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(
        0xFE,
        (
            "Grrr... You're such a jerk, Randy!\x01",
            "You big, dumb liar!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 1)
    Jump("loc_3C0F")

    label("loc_3B84")

    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(
        0xFE,
        (
            "Grrr... You're such a jerk, Randy!\x01",
            "You big, dumb liar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're going to make me really mad\x01",
            "if you don't come to our store!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0F")

    Jump("loc_3C17")

    label("loc_3C14")

    Call(0, 12)

    label("loc_3C17")

    TalkEnd(0xFE)
    Return()

    # Function_11_26A1 end

    def Function_12_3C1B(): pass

    label("Function_12_3C1B")

    TurnDirection(0xFE, 0x104, 0)

    ChrTalk(
        0xFE,
        "Ah. Found you, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You haven't come by to play with us lately...\x01",
            "What could be more important than us?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHaha. My bad, sweetie. My hands are\x01",
            "kinda tied right now. Sorta in the middle\x01",
            "of a career change.\x02\x03",
            "How's life been treatin' you,\x01",
            "my dearest Eris?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm... I guess I'm the same as usual.\x01",
            "I'm always working as hard as I can to\x01",
            "beat my rivals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Randy, will you pleeease come\x01",
            "play with us again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FYou leave me no choice, ma'am.\x01",
            "Maybe I could make some time to--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109FYes. Hello, Randy? Care to not hit on\x01",
            "hostesses while with a minor? PLEASE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(Has Randy always been this, uh...\x01",
            "amorous?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 3)
    Return()

    # Function_12_3C1B end

    def Function_13_3EAE(): pass

    label("Function_13_3EAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4021")

    ChrTalk(
        0xFE,
        (
            "The First Division put me on watch\x01",
            "to keep citizens from wandering in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "B-But isn't this place Revache & Co.?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Th-This is really bad...\x01",
            "Am I really going to be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI'm sorry, Franz...\x01",
            "We're leaving guard duty to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, if those dudes manage to return,\x01",
            "then take that as a signal to get the\x01",
            "hell outta there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4096")

    label("loc_4021")


    ChrTalk(
        0xFE,
        (
            "Man, I'm just a rookie. I only joined\x01",
            "the force this year...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wasn't expecting to be this stressed yet...\x02",
    )

    CloseMessageWindow()

    label("loc_4096")

    TalkEnd(0xFE)
    Return()

    # Function_13_3EAE end

    def Function_14_409A(): pass

    label("Function_14_409A")

    TurnDirection(0x11C, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_40FC")

    ChrTalk(
        0x11C,
        "#1200FWoof! Woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Doesn't look like this is the right way.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_417A")

    label("loc_40FC")


    ChrTalk(
        0x11C,
        "#1200FWoof! Woof!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FNot this way, either?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FIt does seem so.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_417A")

    Return()

    # Function_14_409A end

    def Function_15_417B(): pass

    label("Function_15_417B")

    EventBegin(0x1)
    Call(0, 14)
    Sleep(50)
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_15_417B end

    def Function_16_4197(): pass

    label("Function_16_4197")

    EventBegin(0x1)

    ChrTalk(
        0x11C,
        "#1200FWoof, woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI should've known. He didn't\x01",
            "go this way, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FIt appears he made it a priority\x01",
            "to use maximum discretion.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 4620, 180)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    EventEnd(0x4)
    Return()

    # Function_16_4197 end

    def Function_17_4266(): pass

    label("Function_17_4266")

    EventBegin(0x1)

    ChrTalk(
        0x11C,
        "#1200FWoof, woof!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI don't think this is the way.\x02\x03",
            "#0001FIf he left the antique shop and\x01",
            "went for another round of drinks...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 5660, 790, 4890, 180)
    EventEnd(0x4)
    Return()

    # Function_17_4266 end

    def Function_18_430B(): pass

    label("Function_18_430B")

    EventBegin(0x2)

    ChrTalk(
        0x11C,
        "#1200FWoof, woof!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0005FHuh. Not this way, either?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FWe should try investigating\x01",
            "another route.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    Fade(500)
    SetChrPos(0x0, -10220, 1950, 5940, 180)
    OP_31(0x1)
    OP_0D()
    EventEnd(0x3)
    Return()

    # Function_18_430B end

    def Function_19_43C6(): pass

    label("Function_19_43C6")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff* *sniff*\x02\x03",
            "Woof!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, Zeit? It sounds like he's got a hit.\x01",
            "Our guy must have passed by here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYes. I advise we continue in this\x01",
            "direction.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_19_43C6 end

    def Function_20_447D(): pass

    label("Function_20_447D")

    TalkBegin(0xFF)

    ChrTalk(
        0x11C,
        (
            "#1200F*sniff* *sniff*\x02\x03",
            "Grrrrowl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FIsn't this...the wrong way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FZeit seems to think so.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_20_447D end

    def Function_21_44F6(): pass

    label("Function_21_44F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-10190, 1950, 2170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(5680, 1950, 2170, 6000)
    MoveCamera(0, 10, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(16500, 6000)
    PlaceName2(340, 200, "c_plac08", 0x0, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47E2")

    AnonymousTalk(
        0x103,
        "#0205FWhat is this place?\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0303FThis is the infamous Back Alley of Crossbell.\x02\x03",
            "#0300FThough it's only an extension of the Entertain-\x01",
            "ment District, it's got its fair share of pubs\x01",
            "and night clubs you can waste the night away at.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0000FYou sound like you're awfully familiar\x01",
            "with this area, Randy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0302FOf course, man. Didn't I tell you before?\x02\x03",
            "#0309FThe clubs 'round here have a TON of sexy chicks,\x01",
            "dude...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#0106FAll right, you can stop talking now.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0012F(Haha... Randy seems pretty addicted\x01",
            "to these kind of places...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_47E2")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Back Alley is an alleyway that\x01",
            "connects to the Central Square.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can find stores such as Garante Jazz Bar\x01",
            "and Imelda Antique Shop here.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "While the prices may be expensive, you\x01",
            "can purchase many useful items here.\x01",
            "Try visiting when you have the chance.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x47, 3)
    EventEnd(0x5)
    Return()

    # Function_21_44F6 end

    def Function_22_494E(): pass

    label("Function_22_494E")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    OP_68(0, 1000, 45000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -800, -100, 40500, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 800, -100, 40500, 270)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 0, 200, 44500, 180)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    OP_68(0, 3000, 43000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(19000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac12", 0x0, 0)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 900, 35500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x8, -800, 0, 40500, 90)
    SetChrPos(0x9, 800, 0, 40500, 270)
    OP_0D()

    ChrTalk(
        0x101,
        "#2100646V#12P#0001F(So, this is the Revache & Co. building...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100647V#0101F(It's not exactly in the safest part of\x01",
            "the city, either.)\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    Sleep(150)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C15():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4C15)
    Sleep(50)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        "#2100648V#5PWho the hell are you guys?\x02",
    )

    CloseMessageWindow()

    def lambda_4C58():
        OP_95(0xFE, 700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C58)
    Sleep(150)

    def lambda_4C75():
        OP_95(0xFE, -700, 0, 37500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C75)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#2100649V#5PThis isn't a place for kids like\x01",
            "you to screw around in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100650V#5PGo ahead and piss o--\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#2100651V#5PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100652V#5PAren't you those guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100653V#12P#0205FCould it be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100654V#12P#0302FHeh. Think we're about to get reacquainted\x01",
            "with a dear felon of ours.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        "#2100655V#11PWhat? Who are these guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100656V#5PIt's those damn dogs with the police!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100657V#5PThey're the ones that spoiled our\x01",
            "plans in the Downtown District!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x9,
        "#2100658V#5PThe hell did you just say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100659V#12P#0003FIt seems our reputation\x01",
            "precedes us.\x02\x03",
            "#2100660V#0000FWe've come here to perform an\x01",
            "official investigation today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100661V#5PWhat are you going on about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100662V#12P#0000FWe'd appreciate you introducing us\x01",
            "to your leader.\x02\x03",
            "#2100663VWe'd like to ask him some questions\x01",
            "regarding a certain incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100664V#5PAre you out of your damn minds?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100665V#5PA bunch of dogs like you talking to the don?!\x01",
            "Just how cocky have you runts become?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100666V#0103FRest assured, he isn't a suspect.\x01",
            "He's just a person of interest.\x02\x03",
            "#2100667V#0100FHe, of course, isn't obligated to speak\x01",
            "with us, so we won't force the issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100668V#12P#0300FCan you at least let the boss know\x01",
            "we're here? Appreciate it, boys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100669V#5PD-Damn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2100670V#5PThanks, Arnaud. Your screw up has made\x01",
            "them become way more arrogant.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "#2100671V#11PHey, man. The hell's the plan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100672V#11PThese sons of bitches have the wrong idea.\x01",
            "Sounds like we should teach 'em some\x01",
            "manners, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100673V#5PHah. Sounds good to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100674V#12P#0308F(No good, eh?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100675V#6P#0006F(Yeah, it's a bust. We've got no\x01",
            "choice but to retreat for now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    StopBGM(0xBB8)
    Sleep(500)

    NpcTalk(
        0xD,
        "Bold Voice",
        "#2100676V#4PStep aside.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    Fade(500)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_EE(0x0, 0x5)
    OP_68(0, 1000, 36000, 4000)
    SetCameraDistance(20000, 4000)
    PlayBGM("ed7302", 0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5541():

        label("loc_5541")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_5541")

    QueueWorkItem2(0x8, 2, lambda_5541)

    def lambda_5553():

        label("loc_5553")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_5553")

    QueueWorkItem2(0x9, 2, lambda_5553)

    def lambda_5565():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5565)

    def lambda_5576():
        OP_95(0xFE, 0, 0, 37000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5576)
    WaitChrThread(0xD, 2)
    Sleep(1500)

    def lambda_5597():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5597)
    Sleep(100)

    def lambda_55B4():
        OP_96(0xFE, 0x514, 0x0, 0x92E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55B4)

    ChrTalk(
        0x8,
        "#2100677V#1PGah, Boss?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#2100678V#2PTh-This one's all yours!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        "#2100679V#5P#3104FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100680V#6P#0013F(H-He's massive...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100681V#0201F#6P#N(Wald was fairly large, but he\x01",
            "pales in comparison to this...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#2100682V#0301F#12P(This guy's a mountain...)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Giant Man in Suit",
        (
            "#2100683V#5P#3100FHeh... You're those brats with the\x01",
            "police, then?\x02\x03",
            "#2100684VI've heard the stories already, but you're\x01",
            "younger than I thought you'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100685V#6P#0003FI'm Lloyd Bannings of the\x01",
            "Special Support Section.\x02\x03",
            "#2100686V#0001FAnd you are?\x02",
        )
    )

    CloseMessageWindow()
    Sound(1854, 255, 90, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Giant Man in Suit")

    AnonymousTalk(
        0xFF,
        (
            "#2100687VGarcia Rossi.\x02\x03",
            "#2100688VI'm the general manager of sales\x01",
            "at Revache & Co.\x02\x03",
            "#2100689VHahaha... I suppose most of the\x01",
            "employees stick to 'Boss,' though.\x02",
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
        "#2100690V#6P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100691V#0301F#12P(Oh, damn. I wasn't expectin' a big shot\x01",
            "like him comin' out here to greet us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100692V#6P#0101F(Yes. He's likely Marconi's right-hand man.)\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#2100693V#5P#3103FCome inside.\x02\x03",
            "#2100694VI'll listen to what you have to say.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A6E():
        OP_95(0xFE, 0, 200, 44500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5A6E)
    Sleep(2000)

    def lambda_5A8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5A8B)

    ChrTalk(
        0x101,
        "#2100695V#6P#0005FHuh? What?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 2)
    WaitChrThread(0xD, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)

    def lambda_5ACE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5ACE)
    Sleep(100)
    OP_93(0x9, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#2100696V#5PHah. Go on. You'd better listen\x01",
            "to what the boss says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#2100697V#5PGet your asses in there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100698V#11PDon't even think about\x01",
            "disrespecting the boss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#2100699V#11PUnless you're fine with shortening\x01",
            "your lifespans.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_EE(0x0, 0xA)
    ModifyEventFlags(0, 0, 0x80)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_494E end

    def Function_23_5C11(): pass

    label("Function_23_5C11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 0, 300, 45000, 180)
    SetChrPos(0x102, -400, 300, 45000, 180)
    SetChrPos(0x103, 400, 300, 45000, 180)
    SetChrPos(0x104, 0, 300, 45000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 0, 41700, 45)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 0, 41700, 315)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    ClearMapObjFlags(0x2, 0x10)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    SetCameraDistance(19000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_5D74():

        label("loc_5D74")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5D74")

    QueueWorkItem2(0x8, 2, lambda_5D74)

    def lambda_5D86():

        label("loc_5D86")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5D86")

    QueueWorkItem2(0x9, 2, lambda_5D86)

    def lambda_5D98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D98)

    def lambda_5DA9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DA9)
    Sleep(600)

    def lambda_5DC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DC6)

    def lambda_5DD7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DD7)
    Sleep(400)

    def lambda_5DF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5DF4)

    def lambda_5E05():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E05)
    Sleep(600)

    def lambda_5E22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5E22)

    def lambda_5E33():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E33)
    Sleep(600)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    Sleep(4500)
    Fade(1000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_68(0, 1100, 6500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 0, 0, 9000, 180)
    SetChrPos(0x102, 0, 0, 9000, 180)
    SetChrPos(0x103, 0, 0, 9000, 180)
    SetChrPos(0x104, 0, 0, 9000, 180)
    BeginChrThread(0x101, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x104, 3, 0, 27)
    OP_68(0, 1100, 3500, 5000)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x101,
        "#2100782V#6P#0008FThat went well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#2100783V#6P#0206FHe was treating us like children.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100784V#0301FTch... I can't stand that bastard.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2100785V#6P#0005FThat reminds me, Randy...\x02\x03",
            "#2100786VHe stopped you for some reason.\x01",
            "What was up with that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#2100787V#11P#0306FBeats me.\x02\x03",
            "#2100788V#0301FAnyway, that monster definitely\x01",
            "ain't bluffin'.\x02\x03",
            "#2100789VI doubt we'd even be able to put a scratch\x01",
            "on him with the way we are now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2100790V#6P#0001FYou think?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2100791V#12P#0203FI definitely sensed that he was\x01",
            "far beyond our reach...\x02\x03",
            "#2100792V#0201FHe seemed largely unconcerned about\x01",
            "our actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100793V#6P#0006FRight. I got that impression, too.\x02\x03",
            "#2100794V#0001FEven for someone with connections with\x01",
            "the diet, he didn't seem fazed at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2100795V#0108F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6315():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6315)
    Sleep(100)
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x101,
        "#2100796V#6P#0005FElie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2100797V#2P#0305FWhat's up?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    ChrTalk(
        0x102,
        (
            "#2100798V#0103F#5POh, umm... It's nothing.\x02\x03",
            "#2100799V#0101FMore importantly, how will we proceed?\x02\x03",
            "#2100800VI'm sure you're already hard at work trying\x01",
            "to connect all the dots, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100801V#6P#0005FYou mean regarding the threat letter\x01",
            "sent to Ilya? Y-Yeah...\x02\x03",
            "#2100802V#0003FI don't think we can take everything Garcia\x01",
            "told us at face value. That being said...\x02\x03",
            "#2100803V#0001F...I think there's a low likelihood that Revache\x01",
            "is connected to this incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6582():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6582)
    Sleep(50)

    def lambda_6592():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6592)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x102,
        "#2100804V#0105F#5PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100805V#12P#0205FBut... He clearly reacted to the threat\x01",
            "letter once he saw it, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#2100806V#6P#0004FI never said he didn't. I think his reaction\x01",
            "was because he noticed something.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd pulled out the threat letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
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

    AnonymousTalk(
        0x101,
        "#2100807V#0000FPerhaps what Garcia reacted to was...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFF9B9B9B, 0x1F4, 0x0)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat did Garcia react to?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[The letter's handwriting]\x01",      # 0
            "[The sender's name]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6880"),
        (1, "loc_69F4"),
        (SWITCH_DEFAULT, "loc_6A30"),
    )


    label("loc_6880")


    AnonymousTalk(
        0x101,
        "#2100808V#0001F...the letter's handwriting.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#2100809V#0203FHandwriting certainly varies\x01",
            "from person to person.\x02\x03",
            "#2100810V#0200FHowever, Garcia reacted toward\x01",
            "reading the end of the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#2100811V#0006FO-Oh, right.\x02\x03",
            "#2100812V#0008FThen I think it would have to be\x01",
            "the sender's name at the end.\x02\x03",
            "#2100813V#0001FThat's what drew his reaction.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6A30")

    label("loc_69F4")

    OP_2C(0x42, 0x2)

    AnonymousTalk(
        0x101,
        "#2100814V#0001F...the name of the sender.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_6A30")

    label("loc_6A30")


    AnonymousTalk(
        0x104,
        "#2100815V#0301FThat Yin dude.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#2100816V#0101FYou think there's a chance Yin\x01",
            "is involved with Revache?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#2100817V#0003FYin conspiring with Revache wouldn't\x01",
            "explain Garcia's reaction to the letter.\x02\x03",
            "#2100818V#0001FIt was almost as if he was sure this had\x01",
            "nothing to do with them once he saw it.\x02\x03",
            "#2100819VDon't you think so?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#2100820V#0105FOh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#2100821V#0300FYeah, that's a good way to describe\x01",
            "the look on that ugly mug of his.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#2100822V#0203FWe can deduce that while Yin has no\x01",
            "ties to Revache, it is still a name they\x01",
            "are familiar with.\x02\x03",
            "#2100823V#0201FIs that an appropriate hypothesis?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#2100824V#0004FYeah, something along those lines.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2100825V#0103F#5PIf that's the case...\x02\x03",
            "#2100826V#0101F...I think we should consult with someone\x01",
            "who is more familiar with Revache.\x02\x03",
            "#2100827VMr. Grimwood comes to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100841V#6P#0000FYeah, that's a great idea.\x02\x03",
            "#2100829V#0006FIf we're as close to the truth as we think\x01",
            "we are, then it might be a good idea to\x01",
            "discuss it with Grace, too. Although...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2100830V#11P#0306FWe give that woman any scrap of meat\x01",
            "and before you know it, she'll be pinin'\x01",
            "for the whole damn meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2100831V#12P#0200FThe situation would grow into a colossal\x01",
            "scandal for Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100832V#6P#0003FI was hoping you'd all talk me down\x01",
            "from that idea, to be honest.\x02\x03",
            "#2100833V#0000FWe should try questioning any other\x01",
            "people that come to mind, as well.\x02\x03",
            "#2100834VWho knows? Maybe someone unexpected\x01",
            "will be the key to finding a new lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100835V#0104F#5PYes, maybe so...\x02\x03",
            "#2100836V#0102FHeehee...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#2100837V#6P#0005FWhat's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2100838V#0104F#5POh, no. It's nothing.\x02\x03",
            "#2100839V#0100FShall we begin gathering\x01",
            "information?\x02\x03",
            "#2100840VWe're free to visit wherever we'd like,\x01",
            "but we'll have to visit the law office\x01",
            "at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2100828V#6P#0000FRight. Let's do our rounds and visit\x01",
            "Mr. Grimwood once we're ready.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    OP_CA(0x1, 0xFF, 0x0)
    SetMapObjFlags(0x2, 0x10)
    OP_68(0, 1950, 2600, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2600, 180)
    SetChrPos(0x1, 0, 0, 2600, 180)
    SetChrPos(0x2, 0, 0, 2600, 180)
    SetChrPos(0x3, 0, 0, 2600, 180)
    SetChrPos(0x8, -2000, 0, 41700, 1800)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x9, 2000, 0, 41700, 180)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0x80, 7)
    OP_29(0x42, 0x1, 0x4)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    EventEnd(0x5)
    Return()

    # Function_23_5C11 end

    def Function_24_72F2(): pass

    label("Function_24_72F2")


    def lambda_72F7():
        OP_95(0xFE, 0, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72F7)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_24_72F2 end

    def Function_25_7318(): pass

    label("Function_25_7318")

    Sleep(700)

    def lambda_7320():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7320)
    WaitChrThread(0x102, 1)

    def lambda_733E():
        OP_95(0xFE, -1000, 0, 2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_733E)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_25_7318 end

    def Function_26_735F(): pass

    label("Function_26_735F")

    Sleep(1300)

    def lambda_7367():
        OP_95(0xFE, 0, 0, 4700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7367)
    WaitChrThread(0x103, 1)

    def lambda_7385():
        OP_95(0xFE, 1000, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7385)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_26_735F end

    def Function_27_73A6(): pass

    label("Function_27_73A6")

    Sleep(2500)

    def lambda_73AE():
        OP_95(0xFE, 0, 0, 3100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_73AE)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_27_73A6 end

    def Function_28_73CF(): pass

    label("Function_28_73CF")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    OP_68(0, 1000, 42000, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -900, 0, 3600, 0)
    SetChrPos(0x102, 2150, 0, 2800, 0)
    SetChrPos(0x103, 2650, 0, 2200, 0)
    SetChrPos(0x104, -1100, 0, 2800, 0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0xD, -8000, 0, 1000, 90)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 5000, 0, -300, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -2700, 0, 41000, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 2000, 0, 39000, 45)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -750, 0, 42000, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 3000, 0, 40000, 225)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 750, 0, 42000, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    BeginChrThread(0x8, 3, 0, 29)
    BeginChrThread(0x9, 3, 0, 30)
    BeginChrThread(0x10, 3, 0, 31)
    SetCameraDistance(19000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(1000)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0x10, 0x3)
    OP_68(0, 1100, 6500, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(15500, 0)
    OP_68(0, 1100, 4500, 4000)
    Sleep(2000)

    def lambda_761F():
        OP_96(0xFE, 0x73A, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_761F)
    Sleep(300)

    def lambda_763C():
        OP_96(0xFE, 0x5AA, 0x0, 0x898, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_763C)
    Sleep(400)

    def lambda_7659():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xE10, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7659)
    Sleep(300)

    def lambda_7676():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xAF0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7676)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_64(0x9)
    OP_64(0x10)

    ChrTalk(
        0x102,
        (
            "#4200264V#6P#0101FJust like I thought. There are more\x01",
            "guards posted here than usual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200265V#0301F#6PThey're lookin' way more pissed\x01",
            "than I was expectin', too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200266V#6P#0206FImpatient, excited, vigilant, anxious...\x02\x03",
            "#4200267V#0201FI am detecting a wide range of emotions\x01",
            "from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200268V#6P#0001FThere's no mistaking it. They must be on\x01",
            "high alert for any retaliation from Heiyue.\x02\x03",
            "#4200269V#0006FThis isn't going to be easy.\x02\x03",
            "#4200270VFor now, ascertaining Garcia's\x01",
            "movements should be--\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    StopBGM(0x7D0)

    NpcTalk(
        0xD,
        "Bold Voice",
        "#4200271V#4PWhy the hell are you here?\x02",
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    Fade(500)
    OP_68(-4400, 1000, 1400, 0)
    MoveCamera(301, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 800, 0, 2800, 270)
    SetChrPos(0x102, 1800, 0, 2700, 270)
    SetChrPos(0x103, 2100, 0, 1700, 270)
    SetChrPos(0x104, -600, 0, 3200, 225)
    ClearChrFlags(0xD, 0x8)
    OP_68(-1400, 1000, 1400, 3000)

    def lambda_79FD():
        OP_95(0xFE, -3000, 0, 1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_79FD)
    Sleep(700)

    def lambda_7A1A():
        OP_96(0xFE, 0xC8, 0x0, 0x708, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A1A)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#4200272V#12P#0005FGarcia Rossi...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200273V#0301FDamn, that monster managed to\x01",
            "conceal his presence?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1852, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "#4200274VHmph. It's you guys.\x02\x03",
            "#4200275VYou have the audacity to show your faces\x01",
            "around here after all the shit you've\x01",
            "put us through?\x02",
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
            "#4200286V#12P#0013FTch...\x02\x03",
            "#4200277V#0003F...I won't make any excuses.\x02\x03",
            "#4200278V#0001FOur deal with you only concerns\x01",
            "KeA and KeA alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200279V#3104F#5PThen we're understood.\x02\x03",
            "#4200280V#3102FIf you use our deal as an excuse to come\x01",
            "waltzing into our territory, I'm going to\x01",
            "beat the ever-loving hell out of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200281V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200282V#0306FWell, aren't we a dangerous old dude?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200283V#3103F#5PI'm fully aware of why you're snooping\x01",
            "around.\x02\x03",
            "#4200284VHowever, you won't be getting a single\x01",
            "word out of me on that matter.\x02\x03",
            "#4200285V#3101FIf you understand, then get lost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4200276V#12P#0013FTch.\x02",
    )

    CloseMessageWindow()

    def lambda_7E29():

        label("loc_7E29")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_7E29")

    QueueWorkItem2(0x101, 2, lambda_7E29)

    def lambda_7E3B():

        label("loc_7E3B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_7E3B")

    QueueWorkItem2(0x102, 2, lambda_7E3B)

    def lambda_7E4D():

        label("loc_7E4D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_7E4D")

    QueueWorkItem2(0x103, 2, lambda_7E4D)

    def lambda_7E5F():

        label("loc_7E5F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_7E5F")

    QueueWorkItem2(0x104, 2, lambda_7E5F)

    def lambda_7E71():
        OP_95(0xFE, 200, 0, 1800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7E71)
    Sleep(400)

    def lambda_7E8E():
        OP_96(0xFE, 0x44C, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E8E)
    WaitChrThread(0xD, 1)

    def lambda_7EAC():
        OP_95(0xFE, 200, 0, 6800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7EAC)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    Fade(1000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_68(0, 500, 11500, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 400, 0, 1800, 0)
    SetChrPos(0x102, 1300, 0, 2700, 0)
    SetChrPos(0x103, 1600, 0, 1700, 0)
    SetChrPos(0x104, -1000, 0, 2900, 0)
    SetChrPos(0xD, 0, 0, 6000, 0)

    def lambda_7F66():
        OP_96(0xFE, 0x0, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7F66)
    OP_0D()

    def lambda_7F81():
        OP_96(0xFE, 0x0, 0x0, 0xE10, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F81)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        (
            "#4200287V#6P#0003FPlease, just tell me one thing.\x02\x03",
            "#4200288V#0001FIf, hypothetically, you were to attack\x01",
            "an armed enemy stronghold...\x02\x03",
            "#4200289V...would you attack from the vanguard,\x01",
            "leaving everything to brute strength?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 1)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#4200290V#5P#3104FHah. An honest jaeger like myself would\x01",
            "never adopt such a poor strategy.\x02\x03",
            "#4200291VI'd wait until the conditions were favorable\x01",
            "and wreak the most havoc while minimizing\x01",
            "casualties.\x02\x03",
            "#4200292V#3100FWouldn't you do the same...Son of the War God?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200293V#6P#0303FDon't you ever call me that again.\x02\x03",
            "#4200294V#0301F...But yes, that's how jaegers operate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4200295V#6P#0000FIs that so?\x02\x03",
            "#4200296V#0004FThank you.\x01",
            "I appreciate the answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#4200297V#5P#3100FHeh... You're a strange kid.\x02\x03",
            "#4200298V#3103FBut anyway, you'd better not come\x01",
            "in here unprepared. You hear me?\x02\x03",
            "#4200299V#3101FI promise you'll be torn to shreds.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_832E():
        OP_96(0xFE, 0x0, 0x0, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_832E)
    Sleep(1000)
    OP_68(0, 500, 6100, 3000)
    MoveCamera(0, 16, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20470, 3000)
    Sleep(2000)
    StopBGM(0xFA0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)

    ChrTalk(
        0x101,
        (
            "#4200300V#0006F#5PSomething sure seemed off with him.\x02\x03",
            "#4200301V#0001FHe looked like he was tense, but also\x01",
            "a little worn out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4200302V#0106F#11PSo it wasn't just me, then.\x02\x03",
            "#4200303V#0108FHe said a few nasty things, but I felt like\x01",
            "it didn't have the usual bite to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4200304V#0206F#11PHe expressed signs of fatigue.\x01",
            "I can relate with him on that front...\x02\x03",
            "#4200305V#0201FWhat in the world happened to Revache?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4200306V#0308F#5PDoesn't suit 'em, makin' faces like that.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)

    NpcTalk(
        0xE,
        "Woman's Voice",
        (
            "#4200307V#1PHahaha... Wouldn't you guys like to know\x01",
            "the reason for their glum faces?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1100, 2100, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 0, 0, 3600, 90)
    SetChrPos(0x102, 1800, 0, 2700, 90)
    SetChrPos(0x103, 2100, 0, 1700, 90)
    SetChrPos(0x104, -1000, 0, 2900, 90)

    def lambda_870D():

        label("loc_870D")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_870D")

    QueueWorkItem2(0x101, 2, lambda_870D)

    def lambda_871F():

        label("loc_871F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_871F")

    QueueWorkItem2(0x102, 2, lambda_871F)

    def lambda_8731():

        label("loc_8731")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8731")

    QueueWorkItem2(0x103, 2, lambda_8731)

    def lambda_8743():

        label("loc_8743")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_8743")

    QueueWorkItem2(0x104, 2, lambda_8743)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x4)

    def lambda_875F():
        OP_96(0xFE, 0x0, 0x0, 0x2BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_875F)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x0, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#4200308V#0005F#11PG-Grace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4200309V#5P#0306FWoman, you have a knack for appearin'\x01",
            "in the most random places, don'tcha?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xE,
        (
            "#4200310VWhat can I say? My reporter's spirit\x01",
            "guides me to the juiciest of scoops!\x02\x03",
            "#4200311VAnyway. Let's proceed with the usual\x01",
            "give-and-take session, shall we? ♪\x02\x03",
            "#4200312VI'll be anxiously awaiting your arrival\x01",
            "at the jazz bar! ㈱\x02",
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
    OP_93(0xE, 0x10E, 0x1F4)
    OP_68(-2790, 1100, 3330, 3000)

    def lambda_8974():
        OP_95(0xFE, -10300, 0, 2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8974)
    WaitChrThread(0xE, 1)

    def lambda_8992():
        OP_95(0xFE, -10300, 1500, 5400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8992)
    Sleep(500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    WaitChrThread(0xE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_89DE():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_89DE)
    Sleep(500)

    def lambda_89FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_89FB)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xE, 2)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_68(-30, 1100, 3120, 2500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#4200313V#12P#0106FHow should we proceed?\x02",
    )

    CloseMessageWindow()

    def lambda_8AD2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8AD2)
    Sleep(50)
    OP_93(0x104, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#4200314V#5P#0006FIf she plans to talk, we'll hear her out.\x02\x03",
            "#4200315V#0001FWe should be cautious around her.\x01",
            "I don't want us accidentally leaking\x01",
            "anything to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4200316V#12P#0211FDuly noted.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(0, 1950, 2600, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2600, 180)
    SetChrPos(0x1, 0, 0, 2600, 180)
    SetChrPos(0x2, 0, 0, 2600, 180)
    SetChrPos(0x3, 0, 0, 2600, 180)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetScenarioFlags(0xC2, 5)
    OP_29(0x4B, 0x1, 0x3)
    OP_1B(0x2, 0x0, 0x25)
    EventEnd(0x5)
    Return()

    # Function_28_73CF end

    def Function_29_8C8C(): pass

    label("Function_29_8C8C")

    OP_93(0x8, 0xCD, 0x1F4)

    def lambda_8C98():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8C98)
    WaitChrThread(0x8, 1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_93(0x8, 0x19, 0x1F4)

    def lambda_8CDD():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8CDD)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    Return()

    # Function_29_8C8C end

    def Function_30_8CF9(): pass

    label("Function_30_8CF9")

    Sleep(1500)

    label("loc_8CFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D27")
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x9)
    Sleep(2500)
    Jump("loc_8CFC")

    label("loc_8D27")

    Return()

    # Function_30_8CF9 end

    def Function_31_8D28(): pass

    label("Function_31_8D28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D53")
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3500)
    OP_64(0x10)
    Sleep(2500)
    Jump("Function_31_8D28")

    label("loc_8D53")

    Return()

    # Function_31_8D28 end

    def Function_32_8D54(): pass

    label("Function_32_8D54")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 900, 40500, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_EE(0x0, 0x5)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    OP_68(0, 900, 35500, 4000)
    SetCameraDistance(20000, 4000)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#4300117V#0101F#6PThere's not a single person on guard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300118V#12P#0306FThey had a whole damn army out here\x01",
            "when we visited yesterday.\x02\x03",
            "#4300119V#0301FNo signs of a struggle here, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300120V#0008F#6PYeah, it's possible that Heiyue got\x01",
            "their retribution, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8F64():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F64)
    Sleep(50)

    def lambda_8F74():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8F74)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    ChrTalk(
        0x101,
        "#4300121V#11P#0005FTio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4300122V#0105F#11PWhat's the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300123V#6P#0203FIt is too quiet.\x02\x03",
            "#4300124V#0201FI cannot feel the presence of anyone\x01",
            "inside the building...\x02",
        )
    )

    CloseMessageWindow()
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
        "#4300125V#11P#0011FWhat?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#4300126V#6P#0206FMore accurately, I detect a singular\x01",
            "person inside.\x02\x03",
            "#4300127V#0208FI cannot detect anyone else, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#4300128V#11P#0301FYou serious? The hell happened to 'em?\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#4300129V#0003F#6PIt's probably safe to assume Dudley's\x01",
            "the person waiting inside for us.\x02\x03",
            "#4300130V#0013FAll right...\x01",
            "Just to make sure, let's check it out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_922C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_922C)
    Sleep(50)

    def lambda_923C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_923C)
    Sleep(50)

    def lambda_924C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_924C)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        "#4300131V#0101F#6PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_EE(0x0, 0xA)
    SetScenarioFlags(0xC4, 0)
    EventEnd(0x5)
    Return()

    # Function_32_8D54 end

    def Function_33_9299(): pass

    label("Function_33_9299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92B5")
    Call(0, 35)
    Return()

    label("loc_92B5")

    Jump("loc_92D6")

    label("loc_92BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92D6")
    Call(0, 34)
    Return()

    label("loc_92D6")

    EventBegin(0x1)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x0, -500, 0, 34000, 0)
    SetChrPos(0x1, 500, 0, 33750, 0)
    SetChrPos(0x2, -500, 0, 32500, 0)
    SetChrPos(0x3, 500, 0, 32250, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9369")
    SetChrPos(0x4, -500, 0, 31000, 0)

    label("loc_9369")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9388")
    SetChrPos(0x5, 500, 0, 30750, 0)

    label("loc_9388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_940D")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_END)), "loc_9400")

    NpcTalk(
        0x8,
        "Man in Suit",
        (
            "We're not letting you in here,\x01",
            "you pissants.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Man in Suit",
        "Piss off!\x02",
    )

    CloseMessageWindow()

    label("loc_9400")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_9BAA")

    label("loc_940D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94E1")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_END)), "loc_94D4")

    ChrTalk(
        0x8,
        (
            "What kinda business do a bunch of\x01",
            "damn cops like you have here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Get the hell outta here already.\x01",
            "Take one step closer and you're\x01",
            "on private property. Got it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D4")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_9BAA")

    label("loc_94E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97DC")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977A")

    ChrTalk(
        0x8,
        "Huh? Oh, it's just a bunch of dogs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Piss off. Take one step closer and\x01",
            "you're on private property. Got it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "Oh... Wait a minute.\x01",
            "I recognize that face... You guys are...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 400)
    Sleep(300)

    ChrTalk(
        0x8,
        "Damn. Yeah, you're those...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x68, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96C6")

    ChrTalk(
        0x101,
        (
            "#0001F(Pretty safe to assume this building\x01",
            "belongs to the mafia.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(I think we should leave...\x01",
            "It'd be a bad idea to provoke them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9772")

    label("loc_96C6")


    ChrTalk(
        0x101,
        (
            "#0001F(They're here again...)\x02\x03",
            "(Pretty safe to assume this building\x01",
            "belongs to the mafia.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(I think we should leave...\x01",
            "It'd be a bad idea to provoke them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9772")

    SetScenarioFlags(0x88, 0)
    Jump("loc_97CF")

    label("loc_977A")


    ChrTalk(
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmph. You'd better make yourselves\x01",
            "scarce if you don't wanna get hurt!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97CF")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Jump("loc_9BAA")

    label("loc_97DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A00")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_985D")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_985D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9876")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_9876")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    AnonymousTalk(
        0x101,
        "#0001F(Security seems pretty tight today.)\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0301F(Yeah, and they're a lil' more\x01",
            "pissed off than I'd imagined.)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0101F(Well, they DID just raid Heiyue.)\x02\x03",
            "(They're probably on edge worrying\x01",
            "about a possible retaliation.)\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0200F(I sense a great deal of tension and\x01",
            "pain radiating throughout the alley.\x01",
            "I would advise against approaching them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_1B(0x2, 0x0, 0x25)
    SetScenarioFlags(0xC8, 7)
    Jump("loc_9BAA")

    label("loc_9A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BAA")
    OP_68(250, 2950, 35310, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A81")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_9A81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A9A")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_9A9A")

    OP_68(250, 1950, 35310, 3000)
    Sleep(3200)

    AnonymousTalk(
        0x101,
        (
            "#0005FHuh?\x01",
            "There are no guards...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        "#0200FIndeed...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        (
            "#0301FYou think they're hidin' inside?\x02\x03",
            "Either way, we'd be better off\x01",
            "keepin' our distance for now.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        (
            "#0101FRight. It doesn't look like there's\x01",
            "any information to gain over there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 0)

    label("loc_9BAA")

    OP_68(90, 1950, 4620, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 90, 0, 4620, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BFC")
    Jump("loc_9C17")

    label("loc_9BFC")

    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)

    label("loc_9C17")

    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C5C")
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_9C5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C75")
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_9C75")

    EventEnd(0x4)
    Return()

    # Function_33_9299 end

    def Function_34_9C78(): pass

    label("Function_34_9C78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x101, -500, 0, 31000, 0)
    SetChrPos(0x102, 500, 0, 30750, 0)
    SetChrPos(0x103, -500, 0, 29500, 0)
    SetChrPos(0x104, 500, 0, 29250, 0)

    def lambda_9D0D():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D0D)
    Sleep(50)

    def lambda_9D2A():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9D2A)
    Sleep(50)

    def lambda_9D47():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D47)
    Sleep(50)

    def lambda_9D64():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D64)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Man in Suit",
        "Yo, kids.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    NpcTalk(
        0x8,
        "Man in Suit",
        "You got some business here or something?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Man in Suit",
        (
            "Can't let you kids past here. It's private\x01",
            "property up ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(What's with these guys?)\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(0, 1500, 1000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 0, 0, 2340, 180)
    SetChrPos(0x102, -1000, 0, 1750, 135)
    SetChrPos(0x103, 1000, 0, 1750, 225)
    SetChrPos(0x104, 0, 0, 0, 0)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -24330, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    OP_4B(0xB, 0xFF)
    OP_0D()

    ChrTalk(
        0x104,
        "#0301FThey definitely ain't your friendly neighbors.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, I think they're with the mafia.\x02\x03",
            "#0001FI'd like to investigate when we get the\x01",
            "chance, but...we're still just rookies.\x01",
            "For now, we shouldn't press our luck.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 2340, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x46, 6)
    EventEnd(0x5)
    Return()

    # Function_34_9C78 end

    def Function_35_A036(): pass

    label("Function_35_A036")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(0, 1950, 33810, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15150, 0)
    SetChrPos(0x101, -500, 0, 31000, 0)
    SetChrPos(0x102, 500, 0, 30750, 0)
    SetChrPos(0x103, -500, 0, 29500, 0)
    SetChrPos(0x104, 500, 0, 29250, 0)

    def lambda_A0CB():
        OP_98(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A0CB)
    Sleep(50)

    def lambda_A0E8():
        OP_98(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A0E8)
    Sleep(50)

    def lambda_A105():
        OP_98(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A105)
    Sleep(50)

    def lambda_A122():
        OP_98(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A122)
    OP_68(0, 1950, 37000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Hold it, you brats.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x8,
        "What business do you have past here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Huh? What's this, a police badge?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "These the punks that caught\x01",
            "Fabio and the others?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Hold on a sec! You're messin' with me, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "They're just a bunch of rookies, aren't they?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Pretty safe to assume this building\x01",
            "belongs to the mafia.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(I think we should leave...\x01",
            "It'd be a bad idea to provoke them.)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1950, 2340, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x0, 0, 0, 2340, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, -6170, 0, 1400, 90)
    BeginChrThread(0xB, 0, 0, 1)
    SetScenarioFlags(0x68, 0)
    EventEnd(0x5)
    Return()

    # Function_35_A036 end

    def Function_36_A3A2(): pass

    label("Function_36_A3A2")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    def lambda_A3B1():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A3B1)
    Sleep(50)

    def lambda_A3C1():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A3C1)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "Yo, don't just come hanging around\x01",
            "wherever you damn please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You kiddies better get the hell outta here.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrPos(0x0, -100, 0, 41020, 180)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_36_A3A2 end

    def Function_37_A46A(): pass

    label("Function_37_A46A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6DE")

    ChrTalk(
        0x101,
        "#0001FHold on a sec. Just past here is...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A540")

    ChrTalk(
        0x102,
        (
            "#0101FRevache & Co...\x02\x03",
            "We may have come to an agreement\x01",
            "with them, but it'd still be unwise\x01",
            "to needlessly show up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A649")

    label("loc_A540")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5BC")

    ChrTalk(
        0x103,
        (
            "#0203FRevache & Co...\x02\x03",
            "We may have brokered a deal with them,\x01",
            "but I advise we avoid them for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A649")

    label("loc_A5BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A649")

    ChrTalk(
        0x104,
        (
            "#0301FRevache & Co...\x02\x03",
            "We might have struck a deal with these lowlifes,\x01",
            "but we still shouldn't pop in here unannounced.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A649")


    ChrTalk(
        0x153,
        (
            "#1111F???\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, don't worry about it, KeA.\x02\x03",
            "#0003F(Let's get out of here. It's way\x01",
            "too risky to bring KeA here.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xC9, 1)
    Jump("loc_A748")

    label("loc_A6DE")


    ChrTalk(
        0x101,
        (
            "#0001F(Past here is Revache & Co.)\x02\x03",
            "(Though we reached a deal with\x01",
            "them, we shouldn't provoke them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A97A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A913")

    ChrTalk(
        0x104,
        (
            "#0301FRevache & Co...\x01",
            "They've recovered since our scuffle, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FThey've been behaving themselves after\x01",
            "the incident with KeA.\x02\x03",
            "#0101FUnfortunately, it looks like business is back\x01",
            "to usual after we bargained for that deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FA lot has happened this last month...\x01",
            "Let's continue to avoid them for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A90B")

    ChrTalk(
        0x109,
        (
            "#0501F(I had heard rumors, but Lloyd and\x01",
            "the others must really have it rough...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A90B")

    SetScenarioFlags(0xC9, 2)
    Jump("loc_A97A")

    label("loc_A913")


    ChrTalk(
        0x101,
        (
            "#0001F(Past here is Revache & Co.)\x02\x03",
            "(We shouldn't push our luck. Let's avoid\x01",
            "this place for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9DC")

    ChrTalk(
        0x101,
        (
            "#0001F(They've really stepped up security...\x01",
            "We should stay away for now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA5B")

    ChrTalk(
        0x101,
        (
            "#0001F(Garcia's attitude seemed a little\x01",
            "strange...)\x02\x03",
            "(For now, we should listen to what\x01",
            "Grace has to say.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC36")
    TurnDirection(0x13D, 0x0, 500)

    ChrTalk(
        0x13D,
        (
            "#2105FAh, are you guys conducting a secret\x01",
            "infiltration into Revache?\x02\x03",
            "#2103FIt's a little reckless, but I'm not one to judge...\x02\x03",
            "#2109FI've learned, if you guys are set on doing\x01",
            "something, there's no stopping you. Make\x01",
            "sure to give me that big scoop afterwards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FNo...we should stop for now.\x01",
            "(At least, I don't want to do\x01",
            "this in front of Grace...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FI'm still worried about Gantz...\x01",
            "Let's hurry to the casino.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AC83")

    label("loc_AC36")


    ChrTalk(
        0x101,
        (
            "#0003F(Gantz is our top priority right now.\x01",
            "Let's hurry to the casino.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACFD")

    ChrTalk(
        0x101,
        (
            "#0001F(You can tell Revache is worked up\x01",
            "about something new today...\x01",
            "No reason for me to visit them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AD9D")

    ChrTalk(
        0x101,
        (
            "#0001F(There doesn't seem to be a lookout right now,\x01",
            "but it's beyond my jurisdiction to go any further...)\x02\x03",
            "(I shouldn't go any closer.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD9D")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Return()

    # Function_37_A46A end

    def Function_38_ADB1(): pass

    label("Function_38_ADB1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0001FI'm worried about what Bickson said...\x01",
            "Let's head to the casino ASAP.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 20170, 0, 940, 274)
    EventEnd(0x4)
    Return()

    # Function_38_ADB1 end

    SaveToFile()

Try(main)
