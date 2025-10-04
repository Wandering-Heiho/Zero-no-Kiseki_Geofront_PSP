from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0300.bin",                # FileName
        "c0300",                    # MapName
        "c0300",                    # Location
        0x002A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0300",                  # 0
        "Old Man Rays",           # 1
        "Pentos",                 # 2
        "Cindy",                  # 3
        "Creil",                  # 4
        "Joanna",                 # 5
        "Lechter",                # 6
        "Sunita",                 # 7
        "Marie",                  # 8
        "Helmer",                 # 9
        "Ryu",                    # 10
        "Anri",                   # 11
        "Momo",                   # 12
        "Central Square",         # 13
        "West Street",            # 14
        "Administrative District",# 15
        "Residential District",   # 16
        "Entertainment District", # 17
        "East Street",            # 18
        "Downtown District",      # 19
        "Harbor District",        # 20
        "IBC",                    # 21
        "Station Street",         # 22
        "Back Alley",             # 23
        "Ursula Road",            # 24
        "East Crossbell Highway", # 25
        "West Crossbell Highway", # 26
        "Mainz Mountain Path",    # 27
    ))

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch22100.itc",                   # 02
        "chr/ch33300.itc",                   # 03
        "chr/ch25700.itc",                   # 04
        "chr/ch34400.itc",                   # 05
        "chr/ch39000.itc",                   # 06
        "apl/ch50392.itc",                   # 07
    ))

    DeclNpc(-12850,  -5900,   -31489,  315,  261,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(32279,   0,       -4369,   270,  257,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(2349,    0,       -30700,  45,   389,  0x0, 0,   2,   0,   0,   2,   0,   8,   255,  0)
    DeclNpc(-15039,  -6000,   -17110,  45,   389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-21469,  -6000,   -33240,  315,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5500,   -6000,   -41360,  270,  439,  0x0, 0,   7,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-15609,  0,       4480,    315,  453,  0x0, 0,   5,   0,   0,   3,   0,   25,  255,  0)
    DeclNpc(-15859,  0,       3849,    45,   453,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-1000,   0,       610,     90,   449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(449,     0,       610,     90,   449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(5360,    3000,    17690,   0,    449,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 32,  -24.110000610351562,   -33.16999816894531,    -6.5,                  0.0,                   [1.0,                  0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0])
    DeclEvent(0x0000, 0, 24,  0.38999998569488525,   -33.59000015258789,    0.0,                   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.039000000804662704, 11.196666717529297,    -0.0,                  1.0])

    DeclActor(-2700,   -6500,   -38000,  2000,    -2700,   -5500,   -38000,  0x007C, 0,  12, 0x0000)
    DeclActor(17650,   0,       -800,    2000,    17650,   1500,    -800,    0x007C, 0,  33, 0x0000)
    DeclActor(0,       0,       -770,    2000,    0,       1500,    -770,    0x007C, 0,  34, 0x0000)
    DeclActor(-24000,  -6000,   -33500,  2000,    -24000,  -4500,   -33500,  0x007C, 0,  31, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "Central Square")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "West Street")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "Administrative District")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "Residential District")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "Entertainment District")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "East Street")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "Downtown District")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "Harbor District")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "Station Street")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "Back Alley")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "Ursula Road")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")
    PlaceName(185.89999389648438, 0.0, -144.17999267578125, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_648",          # 00, 0
        "Function_1_700",          # 01, 1
        "Function_2_761",          # 02, 2
        "Function_3_78C",          # 03, 3
        "Function_4_7B7",          # 04, 4
        "Function_5_B11",          # 05, 5
        "Function_6_DF8",          # 06, 6
        "Function_7_22F3",         # 07, 7
        "Function_8_37E9",         # 08, 8
        "Function_9_3B3E",         # 09, 9
        "Function_10_4433",        # 0A, 10
        "Function_11_4568",        # 0B, 11
        "Function_12_4F4C",        # 0C, 12
        "Function_13_5087",        # 0D, 13
        "Function_14_5B45",        # 0E, 14
        "Function_15_5B9A",        # 0F, 15
        "Function_16_5BEF",        # 10, 16
        "Function_17_5C44",        # 11, 17
        "Function_18_5C7B",        # 12, 18
        "Function_19_6110",        # 13, 19
        "Function_20_628A",        # 14, 20
        "Function_21_72E1",        # 15, 21
        "Function_22_77E2",        # 16, 22
        "Function_23_7F53",        # 17, 23
        "Function_24_7F83",        # 18, 24
        "Function_25_8474",        # 19, 25
        "Function_26_8F54",        # 1A, 26
        "Function_27_8F93",        # 1B, 27
        "Function_28_8FD0",        # 1C, 28
        "Function_29_93D1",        # 1D, 29
        "Function_30_98F8",        # 1E, 30
        "Function_31_99B6",        # 1F, 31
        "Function_32_9CDA",        # 20, 32
        "Function_33_9CDB",        # 21, 33
        "Function_34_9D2E",        # 22, 34
        "Function_35_A04F",        # 23, 35
        "Function_36_AE51",        # 24, 36
        "Function_37_AE70",        # 25, 37
        "Function_38_AEA0",        # 26, 38
    ))


    def Function_0_648(): pass

    label("Function_0_648")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_688"),
        (1, "loc_694"),
        (2, "loc_6A0"),
        (3, "loc_6AC"),
        (4, "loc_6B8"),
        (5, "loc_6C4"),
        (6, "loc_6D0"),
        (SWITCH_DEFAULT, "loc_6DC"),
    )


    label("loc_688")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_694")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6E8")

    label("loc_6FF")

    Return()

    # Function_0_648 end

    def Function_1_700(): pass

    label("Function_1_700")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_760")
    OP_95(0xFE, 2630, 0, -4370, 1000, 0x0)
    OP_95(0xFE, 240, 0, -7350, 1000, 0x0)
    OP_95(0xFE, 240, -750, -48720, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 35280, 0, -4370, 45)
    Jump("Function_1_700")

    label("loc_760")

    Return()

    # Function_1_700 end

    def Function_2_761(): pass

    label("Function_2_761")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_78B")
    OP_94(0xFE, 0xD20, 0xFFFF8FDA, 0x546, 0xFFFF842C, 0x3E8)
    Sleep(300)
    Jump("Function_2_761")

    label("loc_78B")

    Return()

    # Function_2_761 end

    def Function_3_78C(): pass

    label("Function_3_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_94(0xFE, 0xFFFFC7AC, 0x1658, 0xFFFFBBEA, 0x3F2, 0x3E8)
    Sleep(300)
    Jump("Function_3_78C")

    label("loc_7B6")

    Return()

    # Function_3_78C end

    def Function_4_7B7(): pass

    label("Function_4_7B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_879")
    SetChrPos(0x0, 230, -750, -38720, 0)
    SetChrPos(0x1, 230, -750, -38720, 0)
    SetChrPos(0x2, 230, -750, -38720, 0)
    SetChrPos(0x3, 230, -750, -38720, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84C")
    SetChrPos(0x4, 230, -750, -38720, 0)
    SetChrPos(0x5, 230, -750, -38720, 0)
    Jump("loc_86B")

    label("loc_84C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86B")
    SetChrPos(0x4, 230, -750, -38720, 0)

    label("loc_86B")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_948")

    label("loc_879")

    SetChrPos(0x0, 24330, 0, -4050, 270)
    SetChrPos(0x1, 24330, 0, -4050, 270)
    SetChrPos(0x2, 24330, 0, -4050, 270)
    SetChrPos(0x3, 24330, 0, -4050, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F2")
    SetChrPos(0x4, 24330, 0, -4050, 270)
    SetChrPos(0x5, 24330, 0, -4050, 270)
    Jump("loc_911")

    label("loc_8F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_911")
    SetChrPos(0x4, 24330, 0, -4050, 270)

    label("loc_911")

    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_948")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_985")

    label("loc_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_985")
    Event(0, 20)

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_994")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AA")
    Event(0, 35)

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9D4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -10850, -6000, -24740, 315)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_AE1")

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9E2")
    Jump("loc_AE1")

    label("loc_9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9FA")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_AE1")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A08")
    Jump("loc_AE1")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A20")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_AE1")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A38")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_AE1")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A46")
    Jump("loc_AE1")

    label("loc_A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A68")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A63")
    SetChrFlags(0xB, 0x10)

    label("loc_A63")

    Jump("loc_AE1")

    label("loc_A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A76")
    Jump("loc_AE1")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AA7")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA2")
    ClearChrFlags(0xE, 0x80)

    label("loc_AA2")

    Jump("loc_AE1")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AB5")
    Jump("loc_AE1")

    label("loc_AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AC8")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_AE1")

    label("loc_AC8")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE1")
    SetChrFlags(0xB, 0x10)

    label("loc_AE1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF9")
    OP_C7(0x1, 0x1000)

    label("loc_AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B10")
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_B10")

    Return()

    # Function_4_7B7 end

    def Function_5_B11(): pass

    label("Function_5_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_B2A")

    label("loc_B26")

    OP_65(0x0, 0x1)

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6B")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BCC")

    label("loc_B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BA7")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_BCC")

    label("loc_BA7")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_BCC")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFrame(0xF, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_BF3")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C01")
    Jump("loc_C37")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_C15")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C23")
    Jump("loc_C37")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C37")
    ClearMapObjFlags(0xF, 0x4)
    Jump("loc_C37")

    label("loc_C37")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    OP_70(0x0, 0xA)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0xD, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C95")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA8")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBB")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CCE")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE1")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_CE1")

    ModifyEventFlags(0, 0, 0x80)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D00")
    OP_70(0x1, 0x0)
    OP_66(0x3, 0x1)

    label("loc_D00")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1A")
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5A")
    OP_1B(0x1, 0x0, 0x1E)

    label("loc_D5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x7)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D79")
    Jump("loc_D7E")

    label("loc_D79")

    ModifyEventFlags(0, 1, 0x80)

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD6")
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -7830, -6000, -41810, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF2")
    Jump("loc_DF7")

    label("loc_DF2")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_DF7")

    Return()

    # Function_5_B11 end

    def Function_6_DF8(): pass

    label("Function_6_DF8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8C")
    Jump("loc_ED6")

    label("loc_E8C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EAC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ED6")

    label("loc_EAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ED6")

    label("loc_ECC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ED6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F6B")

    ChrTalk(
        0x8,
        (
            "I reckon you all should head back early.\x01",
            "Crossbellan nights are known to be chilly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB9")

    label("loc_F6B")


    ChrTalk(
        0x8,
        "Oh, no, the sun's setting already...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I've got to head home soon.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FB9")

    Jump("loc_22EB")

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_102B")

    ChrTalk(
        0x8,
        (
            "I feel like Bond used to be more\x01",
            "of an upstanding gentleman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "What's happened to him?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EB")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1073")

    ChrTalk(
        0x8,
        "The diet should wrap up soon, at this rate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1143")

    label("loc_1073")


    ChrTalk(
        0x8,
        (
            "The Imperial Faction takes orders from the Empire, and the\x01",
            "Republican Faction bends to the Republic's every whim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's as if the two major powers are playing a game\x01",
            "of tug-of-war with Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1143")

    Jump("loc_22EB")

    label("loc_1148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1240")

    ChrTalk(
        0xFE,
        (
            "A man by the name of Bond lives in the mansion\x01",
            "over there. I think he works in securities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I heard he made some kind of big\x01",
            "mistake after the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He was awfully depressed about it for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EB")

    label("loc_1240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_12B0")

    ChrTalk(
        0x8,
        "Hoho, weather's splendid today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hey there, young lady.\x01",
            "Care to bask in the sun with me?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EB")

    label("loc_12B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_151D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1391")

    ChrTalk(
        0x8,
        (
            "Justice isn't an attractive enough platform by\x01",
            "itself to be able to push through new reforms\x01",
            "in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For better or worse, we have to entrust that\x01",
            "task to the more sly and cunning folks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1518")

    label("loc_1391")


    ChrTalk(
        0x8,
        (
            "The Crossbell Diet members are said to be\x01",
            "cunning individuals. Perhaps too cunning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To make matters even more complicated,\x01",
            "Crossbellan politics are interfered with by the\x01",
            "ulterior motives of the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The occasional young man with a strong sense of\x01",
            "justice and hopes of changing Crossbell gets\x01",
            "elected to the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Alas, it never goes well for the lad.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1518")

    Jump("loc_22EB")

    label("loc_151D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_171E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15FB")

    ChrTalk(
        0x8,
        (
            "Been seeing a lotta folks delivering pizzas around\x01",
            "here while I've been lounging around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's apparently in vogue to partake in fancier activities\x01",
            "these days. Not for this old man, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1719")

    label("loc_15FB")


    ChrTalk(
        0x8,
        (
            "Everybody seems to be into ordering food\x01",
            "these days. Whatever happened to good,\x01",
            "old-fashioned home cooking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Been seeing a lotta folks delivering pizzas around\x01",
            "here while I've been lounging around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everything looks fancy and stylish compared\x01",
            "to when I was a youngster.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1719")

    Jump("loc_22EB")

    label("loc_171E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_19CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1812")

    ChrTalk(
        0x8,
        "Oh, really? So you all know that girl, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was dozing off, so I thought it was a dream.\x01",
            "I suppose this old man was wrong, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Where in the world did that mysterious little lass\x01",
            "come from, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C8")

    label("loc_1812")


    ChrTalk(
        0x8,
        "I met a mysterious little girl yesterday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On her was a frilly and elegant dress,\x01",
            "and she had beautiful purple hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I didn't notice her until she was\x01",
            "standing right in front of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, the little lass seemed to disappear\x01",
            "right after she gave me a short greeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FDoesn't that sound like the girl we saw\x01",
            "at Rosenberg Studio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FI believe her name was Renne. She must\x01",
            "visit the city on occasion.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19C8")

    Jump("loc_22EB")

    label("loc_19CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A65")

    ChrTalk(
        0x8,
        "The diet's budget meeting draws near.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell's politicians and diet members are\x01",
            "about to get a whole lot more busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9A")

    label("loc_1A65")


    ChrTalk(
        0x8,
        "It's a splendid day today, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Representative Campbell just took off in an\x01",
            "unbelievably luxurious orbal vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Y'know, come to think of it, the diet meeting\x01",
            "should be happening any day now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell's politicians and members of the diet\x01",
            "are about to get a whole lot more busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B9A")

    Jump("loc_22EB")

    label("loc_1B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1D87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C3D")

    ChrTalk(
        0xFE,
        "I still think about that terrible accident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were whisperings of a young lass who\x01",
            "had lost her eyesight in the crash.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D82")

    label("loc_1C3D")


    ChrTalk(
        0xFE,
        "It had to have been four or five years ago...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A delivery truck lost control on the main\x01",
            "street and caused a serious accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The truck exploded into a massive fireball.\x01",
            "I had never seen something so horrific in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The explosion was so massive that bystanders\x01",
            "were caught up in the blast radius.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1D82")

    Jump("loc_22EB")

    label("loc_1D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E03")

    ChrTalk(
        0x8,
        (
            "It's dangerous for kids to wander the city alone.\x01",
            "Heck, I'd say adults have to be careful, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0E")

    label("loc_1E03")


    ChrTalk(
        0x8,
        (
            "I've noticed our neighbor's daughter\x01",
            "wandering outside of her home by\x01",
            "herself quite often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Who knows where those tiny feet of hers\x01",
            "are taking her to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's dangerous for kids to wander the city alone.\x01",
            "You can never be too careful, you hear?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F0E")

    Jump("loc_22EB")

    label("loc_1F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_204F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F70")

    ChrTalk(
        0x8,
        (
            "Hoho, peaceful day, isn't it?\x01",
            "Doesn't get much better than this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204A")

    label("loc_1F70")


    ChrTalk(
        0x8,
        "On a bit of a morning walk are we, youngsters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you're up and about this early,\x01",
            "I'd recommend going to visit the IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That building is truly a sight to behold\x01",
            "when it's shrouded by the morning fog.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_204A")

    Jump("loc_22EB")

    label("loc_204F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20EA")

    ChrTalk(
        0x8,
        (
            "The Residential District has the lowest crime\x01",
            "rate in all of Crossbell City. Your afternoon\x01",
            "naps are sure to go uninterrupted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D5")

    label("loc_20EA")


    ChrTalk(
        0x8,
        (
            "The Residential District has the lowest crime\x01",
            "rate in all of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, probably because most politicians\x01",
            "and bankers live here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm sure the police takes note of all the\x01",
            "important citizens that live here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21D5")

    Jump("loc_22EB")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2274")

    ChrTalk(
        0x8,
        "Out on a walk, youngsters?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you've made it to the quiet Residential District.\x01",
            "Perfect place for a nice stroll, I always say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EB")

    label("loc_2274")


    ChrTalk(
        0x8,
        "*yawn*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, the sun's warmth feels so pleasant today...\x01",
            "Feels perfect for basking in a little sunshine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22EB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_DF8 end

    def Function_7_22F3(): pass

    label("Function_7_22F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_24A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_237E")

    ChrTalk(
        0x9,
        "The elections are just a month away.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's no wonder the pork-barreling politics\x01",
            "have ramped up lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249F")

    label("loc_237E")


    ChrTalk(
        0x9,
        (
            "This year's budget is looking a lot more\x01",
            "generous than it has in previous years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Public projects should get more funding now,\x01",
            "which will likely help the diet's approval\x01",
            "ratings with the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In other words, they're pork-barreling.\x01",
            "It's all just placating to voters.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_249F")

    Jump("loc_37E5")

    label("loc_24A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2509")

    ChrTalk(
        0x9,
        "Haven't seen many police officers around today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Where have they all gone to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_2509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_267A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25D3")

    ChrTalk(
        0x9,
        (
            "Representative Campbell supposedly has\x01",
            "his own plans in store for the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, considering his opponent is Speaker Hartmann,\x01",
            "things are looking a little grim for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2675")

    label("loc_25D3")


    ChrTalk(
        0x9,
        (
            "Representative Campbell has an intense uphill\x01",
            "battle ahead of him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, the current power of the Imperial\x01",
            "Faction won't be shaken so easily.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2675")

    Jump("loc_37E5")

    label("loc_267A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_280E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(
        0x9,
        "We've got an election year on our hands.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Will Mayor MacDowell run for reelection?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2809")

    label("loc_26ED")


    ChrTalk(
        0x9,
        (
            "The mayoral election only occurs once\x01",
            "every five years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'd better choose our candidate carefully.\x01",
            "Whoever is elected will run Crossbell for\x01",
            "the next half-decade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I hope the diet's budget session actually moves along\x01",
            "this time. They're always stuck in a stalemate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2809")

    Jump("loc_37E5")

    label("loc_280E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_28C6")

    ChrTalk(
        0x9,
        (
            "Remember how the mayor's secretary was arrested?\x01",
            "He's finally been sent to prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Who would have expected something so\x01",
            "unthinkable to happen? Sheesh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_298C")

    label("loc_28C6")


    ChrTalk(
        0x9,
        "By the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Remember how the mayor's secretary was arrested?\x01",
            "He's finally been sent to prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Rumors say that the man hasn't muttered a word.\x01",
            "Goodness, what a despicable man...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_298C")

    Jump("loc_37E5")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2A7A")

    ChrTalk(
        0x9,
        "Oh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Weren't you just inside of the Geofront a moment ago?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I don't think kids like yourselves should be playing\x01",
            "inside of there. Please don't ever go there again.\x01",
            "It can be quite dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B44")

    ChrTalk(
        0x9,
        (
            "I've made sure to invest plenty of mira into\x01",
            "the IBC's very own Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. As an investor, I receive tons of\x01",
            "free Mishy merchandise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(I am seething with envy...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2C0D")

    ChrTalk(
        0x9,
        (
            "Mayor MacDowell has been trying to reach\x01",
            "across to both sides of the aisle lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He's getting old, but he continues to chug along.\x01",
            "You can't help but respect a man like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_2C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2E31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CFA")

    ChrTalk(
        0x9,
        (
            "There are three types of tickets you can\x01",
            "purchase for Arc en Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tickets for S section seats go for two-hundred\x01",
            "times their regular value at auctions.\x01",
            "They're exceedingly popular, as you might imagine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2C")

    label("loc_2CFA")


    ChrTalk(
        0x9,
        (
            "Arc en Ciel's tickets are famous for their\x01",
            "insane prices and scarcity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There are three different types of seats\x01",
            "in sections B, A, and S.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Apparently, the troupe has prepared exclusive\x01",
            "seats for their most distinguished visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Only sponsors and special guests may\x01",
            "use them, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E2C")

    Jump("loc_37E5")

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2F61")

    ChrTalk(
        0x9,
        (
            "There's been a pizza delivery man coming\x01",
            "around here fairly often recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I always see him run towards that road down there\x01",
            "with a pizza in hand. Here's the catch, though.\x01",
            "There aren't even any houses on that side of the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Who the heck is ordering all of these pizzas?\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_316F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_304A")

    ChrTalk(
        0x9,
        (
            "Are you trying to go to Crossbell Cathedral or Mainz?\x01",
            "Exiting from the Residential District's northern gate\x01",
            "will take you there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I suppose any self-respecting citizen would know\x01",
            "that already, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_316A")

    label("loc_304A")


    ChrTalk(
        0x9,
        (
            "The Residential District is situated in\x01",
            "the far northwestern part of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you continue along this road, you can leave\x01",
            "Crossbell City via the northern gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You'll come across a mountain path that'll\x01",
            "take you to Crossbell Cathedral and the\x01",
            "mining village, Mainz.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_316A")

    Jump("loc_37E5")

    label("loc_316F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_343C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3256")

    ChrTalk(
        0x9,
        (
            "I would imagine being forty stories above\x01",
            "ground would have a breathtaking view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. Looks like we're about to birth\x01",
            "yet another sightseeing attraction.\x01",
            "I can't wait to see the completed project.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3437")

    label("loc_3256")


    ChrTalk(
        0x9,
        (
            "The new City Hall that's under construction\x01",
            "is supposedly going to be the most modern\x01",
            "building in all of Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's said it will be forty stories above ground\x01",
            "once completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not only will it serve as the new City Hall,\x01",
            "but I've heard there are plans to lease office\x01",
            "and restaurant spaces in the building, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm a businessman, so it's only natural for me\x01",
            "to have found a way to participate in the project.\x01",
            "I can't wait for that beauty to be completed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3437")

    Jump("loc_37E5")

    label("loc_343C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_364D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3504")

    ChrTalk(
        0x9,
        (
            "Representative Campbell is an influential\x01",
            "politician who serves as the leader of the\x01",
            "Republican Faction of the diet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Speaker Hartmann is said to be his\x01",
            "main opponent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3648")

    label("loc_3504")


    ChrTalk(
        0x9,
        (
            "Hey, do you have any idea who lives in that\x01",
            "enormous mansion on the corner of the street?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's the home of Representative Campbell,\x01",
            "leader of the diet's Republican Faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "An extravagant orbal car stops by his house\x01",
            "some mornings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'd imagine it's his chauffeur coming to escort\x01",
            "him to his office.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3648")

    Jump("loc_37E5")

    label("loc_364D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36DE")

    ChrTalk(
        0x9,
        (
            "The only people that live on this street are\x01",
            "Crossbell's upper-class families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I would know, after all. I'm one of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E5")

    label("loc_36DE")


    ChrTalk(
        0x9,
        (
            "Ahem... The only people that live on this street\x01",
            "are Crossbell's upper-class families.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Owning land in Crossbell is expensive,\x01",
            "so these mansions cost a pretty mira.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Only the upper-class of Crossbell could ever\x01",
            "dream to live in this part of town.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_37E5")

    TalkEnd(0xFE)
    Return()

    # Function_7_22F3 end

    def Function_8_37E9(): pass

    label("Function_8_37E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_388F")

    ChrTalk(
        0xA,
        "Has Creil's husband really gone missing?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "Oh, no... I'm worried about them.\x01",
            "I should probably go check up on Creil.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xA)
    Jump("loc_3B3A")

    label("loc_388F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_391C")

    ChrTalk(
        0xA,
        "I'd better finish sweeping so I can brew some tea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Father's returned home today.\x01",
            "I'd like to sit and relax with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3A")

    label("loc_391C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_39BD")

    ChrTalk(
        0xA,
        (
            "Actually, now that I think about it...\x01",
            "Where in the world has Anri run off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Father just told him he wasn't\x01",
            "allowed outside right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B3A")

    label("loc_39BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3A7C")

    ChrTalk(
        0xA,
        (
            "Have you read the latest edition of the\x01",
            "Crossbell Times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "My brother is in it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Father was angry beyond belief once he read it.\x01",
            "I bet Anri did something stupid.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B3A")

    label("loc_3A7C")


    ChrTalk(
        0xA,
        (
            "Grandmother ordered me to take care of\x01",
            "all of the cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*yawn*... I'm still sleepy, but I don't\x01",
            "think I can brush this off to the side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Cleaning first, napping second.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3B3A")

    TalkEnd(0xFE)
    Return()

    # Function_8_37E9 end

    def Function_9_3B3E(): pass

    label("Function_9_3B3E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3BCE")

    ChrTalk(
        0xB,
        (
            "Sophia's husband is an honest and hard-\x01",
            "working man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He always wakes up at the crack of dawn\x01",
            "to go to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C81")

    label("loc_3BCE")


    ChrTalk(
        0xB,
        "Oh, my. What lovely weather we're having.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        (
            "I saw Harold speed off in his orbal car\x01",
            "earlier this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I got the impression that he was in a hurry.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_3C81")

    Jump("loc_442F")

    label("loc_3C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4102")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E09")

    ChrTalk(
        0xFE,
        (
            "Oh, I remember you all.\x01",
            "You came to our house with Sunita earlier, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you all acquainted with my husband, perhaps?\x01",
            "Care to join me for some tea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FThanks, but we'll have to pass this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI hope you continue to take good care\x01",
            "of Marie for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Marie?\x01",
            "Who are you talking about?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 3)
    Jump("loc_3E70")

    label("loc_3E09")


    ChrTalk(
        0xFE,
        (
            "Last time I checked, no one by that name\x01",
            "lives here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have no idea who you're referring to.\x02",
    )

    CloseMessageWindow()

    label("loc_3E70")

    Jump("loc_40FD")

    label("loc_3E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 1)), scpexpr(EXPR_END)), "loc_3F1F")

    ChrTalk(
        0xFE,
        "Oh, I didn't notice that Sunita already left.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's been taking off a lot more than usual,\x01",
            "lately. Must have stumbled upon something interesting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40FD")

    label("loc_3F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F99")

    ChrTalk(
        0xB,
        "I'm taking care of the housework at the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've been studying on how to improve\x01",
            "at cleaning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40FD")

    label("loc_3F99")


    ChrTalk(
        0xB,
        "My parents owned a mansion when I was growing up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It was filled with maids and butlers, so I never had a\x01",
            "chance to learn how to do housework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Getting married has been an adventure.\x01",
            "I'm constantly discovering new things I\x01",
            "missed out on during my sheltered childhood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No complaints from me, though.\x01",
            "I'm loving every second of my life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_40FD")

    Jump("loc_442F")

    label("loc_4102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4187")

    ChrTalk(
        0xB,
        (
            "Have you ever met Sophia from up the street?\x01",
            "She's such a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I strive to be like her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4282")

    label("loc_4187")


    ChrTalk(
        0xB,
        "Sophia from up the street is an incredible cook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Not only that, but she even helps out her\x01",
            "husband with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "How can she handle all of that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I can't even begin to understand the first\x01",
            "thing about my husband's line of work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_4282")

    Jump("loc_442F")

    label("loc_4287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4316")

    ChrTalk(
        0xB,
        (
            "I've heard that if you put love into watering\x01",
            "your flowers, they'll bloom beautifully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I hope they grow up splendidly!\x02",
    )

    CloseMessageWindow()
    Jump("loc_442F")

    label("loc_4316")


    ChrTalk(
        0xB,
        "Oh, my... The flowers are looking thirsty.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        (
            "I've been taking care of this flower bed\x01",
            "for the last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Come and admire my babies. They're especially\x01",
            "beautiful, now that they're in full bloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Could it be? Am I a professional at\x01",
            "watering flowers?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_442F")

    TalkEnd(0xFE)
    Return()

    # Function_9_3B3E end

    def Function_10_4433(): pass

    label("Function_10_4433")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4471")

    ChrTalk(
        0xC,
        (
            "...\x01",
            "I'd better go ask about this later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4564")

    label("loc_4471")


    ChrTalk(
        0xC,
        "?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0105FWhat's wrong, Joanna?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 750)

    ChrTalk(
        0xC,
        (
            "Nothing, my lady... It's just that, a new edition of\x01",
            "the Crossbell Times was to be released today,\x01",
            "but it hasn't arrived yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'd better go ask about this later.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x13B, 0x2EE)
    SetChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4564")

    TalkEnd(0xFE)
    Return()

    # Function_10_4433 end

    def Function_11_4568(): pass

    label("Function_11_4568")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E3D")
    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50357.itc", 0x1E)
    OP_68(-6130, -4250, -41410, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, -4900, -6000, -40150, 225)
    SetChrPos(0x153, -5500, -6000, -39860, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4611")
    SetChrPos(0x102, -5250, -6000, -39000, 180)
    Jump("loc_4658")

    label("loc_4611")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4637")
    SetChrPos(0x103, -5250, -6000, -39000, 180)
    Jump("loc_4658")

    label("loc_4637")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4658")
    SetChrPos(0x104, -5250, -6000, -39000, 180)

    label("loc_4658")

    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x153,
        "#1110F#5PHey, it's the weirdo from last time!\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Sleep(300)
    Fade(500)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x1E)
    ClearChrFlags(0xD, 0x2)
    OP_93(0xD, 0x0, 0x1F4)
    StopEffect(0x8, 0x2)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#3509FYo, missy. We meet again! ♪\x02\x03",
            "#3502FC'mere! How've you been?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lechter gave KeA a pat on the head.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x153,
        "#1105F#5PHeehee, that tickles!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FYou're still in Crossbell, Lechter...\x02\x03",
            "#0006FAnd to no one's surprise, you're still fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_484B")

    ChrTalk(
        0x102,
        (
            "#0111F#5PI have no polite way to phrase this,\x01",
            "but just exactly who are you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492E")

    label("loc_484B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48CC")

    ChrTalk(
        0x103,
        (
            "#0211F#5PI cannot think of a polite way to ask this, so I\x01",
            "will ask you directly: Who and what are you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492E")

    label("loc_48CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_492E")

    ChrTalk(
        0x104,
        (
            "#0301F#5PHey, pal. What's your angle?\x01",
            "I mean, you gotta be hidin' something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492E")


    ChrTalk(
        0xD,
        (
            "#3510FWhaddaya mean? I'm me! I'm just a simple\x01",
            "Erebonian--and the rest of my profile is\x01",
            "redacted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(I don't think that's going to fool anyone...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1109F#5PHehehe!\x01",
            "I knew it. You're a total weirdo!\x02\x03",
            "#1110FI don't mind, though.\x01",
            "Did you know, mister? I can't remember anything.\x02\x03",
            "#1108FThe first thing I remember is seeing Lloyd.\x01",
            "I don't really get it, but it feels like I've\x01",
            "been lost in a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3505FI see. I didn't know that, missy.\x02\x03",
            "#3504FThat ain't so bad, though, is it?\x01",
            "That's probably what you'd call 'happiness.'\x02\x03",
            "#3500FIt's a great word. You should remember it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1105F#5PHappy-ness?\x02\x03",
            "#1104FHmm, I don't really get it.\x01",
            "It's okay, though. I'm having fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x153,
        (
            "#1109F#5PYep. Still don't really get it,\x01",
            "but I'll remember it, mister!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3509FHahaha, what's that even supposed to mean? ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Those two are somehow on the same wavelength...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D12")

    ChrTalk(
        0x102,
        (
            "#0109F#5P(W-Well, it seems like KeA's\x01",
            "taken a liking to him...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DD5")

    label("loc_4D12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D83")

    ChrTalk(
        0x103,
        (
            "#0202F#5P(I am conflicted. If KeA approves of him, does\x01",
            "that make him an okay person?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DD5")

    label("loc_4D83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4DD5")

    ChrTalk(
        0x104,
        "#0302F#5P(How bad can the dude really be if KeDo likes him?)\x02",
    )

    CloseMessageWindow()

    label("loc_4DD5")

    Sleep(150)
    SetChrPos(0x0, -4900, -6000, -40050, 225)
    SetChrChipByIndex(0xD, 0x7)
    SetChrFlags(0xD, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_93(0xD, 0x10E, 0x0)
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -7830, -6000, -41810, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    SetScenarioFlags(0xB7, 6)
    EventEnd(0x5)
    Jump("loc_4F48")

    label("loc_4E3D")


    ChrTalk(
        0xD,
        (
            "#3510FAnyway, isn't the Residential District great?\x01",
            "It's nice and peaceful here--perfect for fishing.\x02\x03",
            "#3507FShould I pull out some earthworms or use red\x01",
            "flies as bait?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FI wouldn't know. Test it out yourself.\x01",
            "Whatever you do, just leave me out of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F48")

    TalkEnd(0xFE)
    Return()

    # Function_11_4568 end

    def Function_12_4F4C(): pass

    label("Function_12_4F4C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x322, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F99")
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked tightly.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5084")

    label("loc_4F99")

    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02\x03",
            "The door can be unlocked with the Geofront B Sector key.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Unlock\x01",      # 0
            "Don't\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5042"),
        (1, "loc_507F"),
        (SWITCH_DEFAULT, "loc_5084"),
    )


    label("loc_5042")

    Sound(809, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door was unlocked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x86, 1)
    Jump("loc_5084")

    label("loc_507F")

    Jump("loc_5084")

    label("loc_5084")

    EventEnd(0x3)
    Return()

    # Function_12_4F4C end

    def Function_13_5087(): pass

    label("Function_13_5087")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3000, -5500, -38000, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, -1000, -6500, -38000, 270)
    SetChrPos(0x102, -1000, -6500, -38000, 270)
    SetChrPos(0x103, -1000, -6500, -38000, 270)
    SetChrPos(0x104, -1000, -6500, -38000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapFlags(0x10000000)
    MoveCamera(55, 35, 0, 6000)
    SetCameraDistance(24000, 6000)
    FadeToBright(2000, 0)
    Sleep(1000)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    BeginChrThread(0x104, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(1500)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(102, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x101, 3)
    Fade(500)
    OP_68(-4800, -4900, -37000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2201012V#6P#0003FStill, I can't believe he'd live in\x01",
            "a place like this...\x02\x03",
            "#2201013V#0001FI don't think we can sweep this one under the rug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#2201014V#6P#0106FRight, he looked young enough to still\x01",
            "be attending Sunday School, too.\x02\x03",
            "#2201015V#0101FHow old is he, Tio?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_530F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_530F)
    Sleep(50)

    def lambda_531F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_531F)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#2201016V#11P#0200FI believe he is 13 years old.\x02\x03",
            "#2201017VOne year younger than I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201018V#12P#0001FIt'd be ideal if the foundation took him back under\x01",
            "their care, but I don't know how viable that is...\x02\x03",
            "#2201019V#0008FYou mentioned something about suffering a\x01",
            "heavy loss, so maybe we shouldn't notify them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201020V#0306F#5PMeh, I say leave the kid alone.\x02\x03",
            "#2201021V#0300FSeemed like he could take care of\x01",
            "himself well enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201022V#11P#0203FRest assured, Jona is a prodigy when\x01",
            "it comes to the orbal network.\x02\x03",
            "#2201023V#0202FHe has a few screws loose, but I know\x01",
            "I can rely on his assistance for any issues\x01",
            "that do not lie within my area of expertise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201024V#12P#0006FHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_55FB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55FB)
    Sleep(50)

    def lambda_560B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_560B)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#2201025V#6P#0104FYou're worried about him, too, huh?\x02\x03",
            "#2201026V#0100FWell, let's just keep him in the back of our\x01",
            "minds for the time being.\x02\x03",
            "#2201027VIt'd be wise of us to pay him a visit every\x01",
            "once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201028V#12P#0000FYeah, sounds like a plan to me.\x02\x03",
            "#2201029V#0003FAnyway, now that we've moved past that,\x01",
            "what should we do about Yin?\x02\x03",
            "#2201030V#0001FIt sounds like he's waiting for us at\x01",
            "Stargazer's Tower...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_5909")

    ChrTalk(
        0x103,
        (
            "#2201031V#0201F#5PKeep in mind that the last time we tried to\x01",
            "enter, the CGF had barricaded the tower off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201032V#0304F#5PC'mon guys, don't be such wimps.\x01",
            "Why don't we just hop the damn thing?\x02\x03",
            "#2201033V#0300FAnd if it comes to it, we can just call up\x01",
            "Deputy Commander Baelz for her permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A0F")

    label("loc_5909")


    ChrTalk(
        0x103,
        (
            "#2201034V#0201F#5POur destination is the tower we saw\x01",
            "from Ursula Road, correct?\x02\x03",
            "#2201035VHow exactly do we get there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201036V#0300F#5PPretty sure there's a side road on the\x01",
            "highway that leads into the forest...\x02\x03",
            "#2201037VShould be right past that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0F")


    ChrTalk(
        0x102,
        (
            "#2201038V#6P#0103FIndeed...\x02\x03",
            "#2201039V#0101FAt any rate, we should double-check our\x01",
            "supplies before we get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2201040V#12P#0001FRight. We can't ignore the possibility\x01",
            "that this is all an elaborate trap.\x02\x03",
            "#2201041VLet's prepare for the worst\x01",
            "before hitting the highway.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -4800, -6000, -36700, 0)
    SetScenarioFlags(0x83, 7)
    EventEnd(0x5)
    Return()

    # Function_13_5087 end

    def Function_14_5B45(): pass

    label("Function_14_5B45")


    def lambda_5B4A():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B4A)

    def lambda_5B64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B64)
    WaitChrThread(0xFE, 1)

    def lambda_5B79():
        OP_95(0xFE, -4800, -6000, -35400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B79)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x1F4)
    Return()

    # Function_14_5B45 end

    def Function_15_5B9A(): pass

    label("Function_15_5B9A")


    def lambda_5B9F():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B9F)

    def lambda_5BB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BB9)
    WaitChrThread(0xFE, 1)

    def lambda_5BCE():
        OP_95(0xFE, -5600, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BCE)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_15_5B9A end

    def Function_16_5BEF(): pass

    label("Function_16_5BEF")


    def lambda_5BF4():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BF4)

    def lambda_5C0E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C0E)
    WaitChrThread(0xFE, 1)

    def lambda_5C23():
        OP_95(0xFE, -4100, -6000, -36700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5C23)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xB4, 0x1F4)
    Return()

    # Function_16_5BEF end

    def Function_17_5C44(): pass

    label("Function_17_5C44")


    def lambda_5C49():
        OP_95(0xFE, -4800, -6000, -38000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C49)

    def lambda_5C63():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C63)
    WaitChrThread(0xFE, 1)
    OP_93(0x101, 0x59, 0x1F4)
    Return()

    # Function_17_5C44 end

    def Function_18_5C7B(): pass

    label("Function_18_5C7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_4B(0x9, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(90, 2000, 3870, 0)
    MoveCamera(18, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25500, 0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    FadeToBright(1000, 0)
    OP_68(11790, 2000, -24490, 7000)
    MoveCamera(67, 22, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(21000, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-16190, -3900, -16880, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(-28000, -3400, -29760, 5000)
    MoveCamera(0, 22, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(23000, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-14640, 2000, -35510, 0)
    MoveCamera(26, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(29000, 5000)
    OP_0D()
    PlaceName2(100, 200, "c_plac09", 0x0, 0)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EF5")
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#0004FThis is Crossbell's northwestern district.\x02\x03",
            "#0000FIt's been home to upper-class families\x01",
            "for as long as I can remember.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x104,
        "#0305FNothin' but big-ass mansions around here.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#0109FY-Yeah...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0205F...?\x01",
            "(Elie is acting strange.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5EF5")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Residential District is a quiet district\x01",
            "in the northwest part of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are no special facilities, but the large mansions\x01",
            "are home to various affluent people living their lives.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It would be a good idea to stop by these\x01",
            "homes occasionally while patrolling the city.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x6, 0x1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60CE")
    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_610A")

    label("loc_60CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_610A")
    OP_68(230, 1250, -38720, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)

    label("loc_610A")

    SetScenarioFlags(0x44, 7)
    EventEnd(0x5)
    Return()

    # Function_18_5C7B end

    def Function_19_6110(): pass

    label("Function_19_6110")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17500, -1500, -6700, 0)
    MoveCamera(30, 7, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(55000, 0)
    SetChrPos(0x0, -22900, 0, -7500, 0)
    SetChrPos(0x1, -22900, 0, -7500, 0)
    SetChrPos(0x2, -22900, 0, -7500, 0)
    SetChrPos(0x3, -22900, 0, -7500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -1000, 0, -25000, 180)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 1500, 0, -35000, 0)
    SetChrFlags(0xA, 0x8000)

    def lambda_61E5():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_61E5)

    def lambda_61FF():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_61FF)
    OP_68(17500, -2500, -6700, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-29000, -3000, -28500, 0)
    MoveCamera(355, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(22000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_6110 end

    def Function_20_628A(): pass

    label("Function_20_628A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-11000, -5000, -24500, 0)
    MoveCamera(15, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -11000, -6000, -25500, 0)
    SetChrPos(0x102, -10000, -6000, -24500, 270)
    SetChrPos(0x103, -12000, -6000, -24500, 90)
    SetChrPos(0x104, -11000, -6000, -23500, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(25, 25, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#4300073V#0106FI can't believe how many people are\x01",
            "missing at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300074V#0303FDamn it. That bad feeling was right on the money.\x02\x03",
            "#4300075V#0301FHow the hell do so many people up and disappear?\x01",
            "They get kidnapped, or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300076V#6P#0206FThere is too little information to\x01",
            "come to a conclusion. All we can do\x01",
            "is hypothesize at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_65A9")

    ChrTalk(
        0x101,
        (
            "#4300077V#12P#0003FThe five people missing may only be the tip\x01",
            "of the iceberg.\x02\x03",
            "#4300079V#0001FOdds are, several people living in Crossbell City\x01",
            "have already disappeared...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665B")

    label("loc_65A9")


    ChrTalk(
        0x101,
        (
            "#4300078V#12P#0003FThe four people missing may only be the tip\x01",
            "of the iceberg.\x02\x03",
            "#4300079V#0001FOdds are, several people living in Crossbell City\x01",
            "have already disappeared...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665B")


    ChrTalk(
        0x102,
        (
            "#4300080V#0108FAs much as I hate to admit it, you might be right...\x01",
            "How many people have gone missing at this point?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#4300081V#0301FWhat's the plan, Lloyd?\x02\x03",
            "#4300082VIt'd probably be a bit of a pain in the ass to\x01",
            "search for them one at a time, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300083V#12P#0006FYeah, we're going to need a stronger\x01",
            "effort than just the four of us.\x02\x03",
            "#4300084V#0008FAnd since the First Division is being pressured\x01",
            "by the top brass, they won't be able to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300085V#6P#0202FWould it be possible to consult with Inspector\x01",
            "Donovan from the Second Division?\x02\x03",
            "#4300086VHe has lent his assistance in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#4300087V#12P#0003FNo, I don't think that'll work, either.\x02\x03",
            "#4300088V#0001FI can only imagine that the Second Division\x01",
            "is being pressured as well, given Detective\x01",
            "Dudley came to us for help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#4300089V#6P#0206FI see. That certainly makes sense...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300090V#0108FSo, the circumstances in the Metropolitan\x01",
            "Division should be about the same...\x02\x03",
            "#4300091V#0106FBeing able to utilize that division's manpower\x01",
            "would have been a great asset...\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6AE3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6AE3)
    Sleep(50)

    def lambda_6AF3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6AF3)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300092V\x07\x00",
            "#0001FYes, Special Support Section,\x01",
            "Lloyd Bannings speaking.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300093V\x07\x05",
            "Hey, rookies!\x02\x03",
            "#4300094VWhat the hell have you four\x01",
            "been up to?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300095V\x07\x00",
            "#0011FOh...\x02\x03",
            "#4300096V#0001FIs that you, Detective Dudley?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300097V\x07\x05",
            "You're damn right it's me!\x02\x03",
            "#4300098VYou guys didn't go sticking your noses into\x01",
            "Revache's business, did you?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300099V\x07\x00",
            "#0005FN-No, not exactly...\x02\x03",
            "#4300100V#0003FWe're focused on the drug investigation\x01",
            "right now.\x02\x03",
            "#4300101V#0001FWhy? Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#4300102V\x07\x05",
            "Why else would I be calling?!\x01",
            "Their office is--\x02\x03",
            "#4300103VAhem! Forget I said anything.\x02\x03",
            "#4300104VIf it doesn't concern you, then don't do anything\x01",
            "rash. Carry on with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#4300105V\x07\x00",
            "#0005FAh...\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#4300106V#12P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300107V#0101FWas that Detective Dudley on the\x01",
            "other end? What's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300108V#12P#0006FWell...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd told Elie and the others about\x01",
            "his conversation with Dudley.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0x104,
        "#4300109V#0301FWhat's poindexter's deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300110V#6P#0206FHis change in demeanor is suspicious.\x02\x03",
            "#4300111V#0201FClearly something must have happened\x01",
            "with Revache, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300112V#12P#0003FYeah, most likely.\x02",
    )

    CloseMessageWindow()
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
        0x104,
        (
            "#4300113V#0300FWe'd better go check it out, then. Better than\x01",
            "standin' around here twiddlin' our thumbs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#4300114V#0103FTrue, but we were told to not interfere in\x01",
            "the conflict. Our hands are tied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300115V#6P#0202FIf the mafia is connected to the missing persons\x01",
            "case, then that is our probable cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#4300116V#12P#0001FI agree. Let's hurry to Revache & Co.!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -11500, -6000, -24000, 135)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_20_628A end

    def Function_21_72E1(): pass

    label("Function_21_72E1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(17650, 2000, -2150, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    SetChrPos(0x101, 17020, 0, -2660, 0)
    SetChrPos(0x102, 17020, 0, -4100, 0)
    SetChrPos(0x103, 18450, 0, -2660, 0)
    SetChrPos(0x104, 18450, 0, -4100, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FI think this is the vacant house.\x01",
            "It has the right address.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x101, 17570, 0, -1480, 1000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)
    Sound(810, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#5P#0003FIt doesn't look like anybody's here.\x02",
    )

    CloseMessageWindow()
    OP_68(22460, 2000, 7120, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(620, 3000)
    SetCameraDistance(26390, 3000)
    Sleep(3300)

    ChrTalk(
        0x104,
        (
            "#5P#0300FDoesn't matter how you look at it.\x01",
            "Thing's an empty mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FAgreed. I am unable to detect any\x01",
            "presences from within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0100FI think this house has been abandoned for\x01",
            "a little over ten years.\x02\x03",
            "I remember hearing rumors about this house\x01",
            "being haunted back when I was a child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0005FOh, really?\x02\x03",
            "#0003F(Elie and I are around the same age, but\x01",
            "I've never heard of this rumor at all...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(17650, 2000, -2150, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FAt any rate, I think we've successfully\x01",
            "verified the vacancy.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775E")

    ChrTalk(
        0x104,
        (
            "#0300FSweet. I think that just about covers\x01",
            "all of the inspections, yeah?\x02\x03",
            "How 'bout we go hit up the lovely lady\x01",
            "back at City Hall now, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x3, 0x1, 0x1E)
    Jump("loc_778E")

    label("loc_775E")


    ChrTalk(
        0x104,
        "#0300FCool, let's move on to the next one.\x02",
    )

    CloseMessageWindow()

    label("loc_778E")

    Sleep(200)
    SetChrPos(0x0, 17510, 0, -2090, 180)
    SetChrPos(0x1, 17510, 0, -2090, 180)
    SetChrPos(0x2, 17510, 0, -2090, 180)
    SetChrPos(0x3, 17510, 0, -2090, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_21_72E1 end

    def Function_22_77E2(): pass

    label("Function_22_77E2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch25800.itc", 0x1E)
    OP_68(-25370, -3900, -33010, 0)
    MoveCamera(342, 18, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(32990, 0)
    SetChrPos(0x101, -23330, -6000, -35420, 315)
    SetChrPos(0x102, -22290, -6000, -34420, 315)
    SetChrPos(0x103, -22140, -6000, -36580, 315)
    SetChrPos(0x104, -21140, -6000, -35430, 315)
    SetChrPos(0x10, -30260, -5500, -27540, 45)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B5")

    ChrTalk(
        0x102,
        "#11P#0105F(Oh...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_78CB")

    label("loc_78B5")


    ChrTalk(
        0x102,
        "#11P#0103FUmm...\x02",
    )

    CloseMessageWindow()

    label("loc_78CB")

    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#0100FExcuse me, Lloyd. Were you looking\x01",
            "to visit this house, perchance?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    TurnDirection(0x104, 0x102, 500)
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5P#0000FYep. After all, the kitten's owner\x01",
            "might live here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#0200FIt is possible that a child around the\x01",
            "suspected age could be here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FI don't think that's the case...\x01",
            "O-Oh, right...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(800)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#0100FWhat if nobody's home? We should ring\x01",
            "the doorbell first, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0005FY-Yeah, good call.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0300FWhat's up, Mademois-Elie? You're actin'\x01",
            "kinda funny...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-27380, -3400, -31750, 0)
    MoveCamera(350, 39, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(26410, 0)
    SetChrPos(0x101, -27840, -6000, -30320, 315)
    SetChrPos(0x103, -26850, -6000, -31330, 315)
    SetChrPos(0x104, -26030, -6000, -30540, 315)
    SetChrPos(0x102, -25060, -6000, -31540, 315)
    OP_70(0x1, 0xA)
    ClearChrFlags(0x10, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_95(0x101, -28480, -5500, -29370, 1000, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0005F#11P(Wow, there's an orbal doorbell...\x01",
            "They must be well off.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(801, 0, 100, 0)
    Sleep(1000)
    Sound(811, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000F#11PExcuse me, this is the CPD.\x02\x03",
            "Would we be able to speak with you for a bit?\x01",
            "It won't take more than a minute.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Man's Voice",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#1P#N#2SAh, yes. I'll be there in just a moment.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 1, 0, 23)
    OP_96(0x101, 0xFFFF9340, 0xFFFFE890, 0xFFFF8990, 0x3E8, 0x0)
    Sleep(800)
    ClearMapObjFlags(0x7, 0x10)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x7)
    OP_95(0x10, -28690, -5500, -28740, 1000, 0x0)
    Sleep(300)

    ChrTalk(
        0x10,
        "#5PI am Helmer, this family's butler.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PI believe you said you were with the police, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#12PYeah, no need to feel alarmed, though.\x01",
            "It's nothing too important.\x02\x03",
            "Does this household happen to own a pet cat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PA cat...you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PNo, I'm afraid not. This residence does not\x01",
            "own any pets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PWhile I may be fond of cats, the master and\x01",
            "my lady are more of the dog type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F#12PO-Oh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306F#12PSwing and a miss.\x02",
    )

    CloseMessageWindow()
    OP_68(-24190, -3400, -32159, 3000)
    Sleep(3000)
    WaitChrThread(0x102, 1)

    ChrTalk(
        0x102,
        "#0106F#11P(Phew... I need to be more careful.)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22430, -6000, -35200, 135)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    OP_49()
    OP_D5(0x1E)
    SetChrFlags(0x10, 0x80)
    OP_70(0x1, 0x0)
    OP_70(0x7, 0x0)
    OP_29(0x8, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_77E2 end

    def Function_23_7F53(): pass

    label("Function_23_7F53")

    OP_96(0x102, 0xFFFFA772, 0xFFFFE890, 0xFFFF7AB8, 0x7D0, 0x0)
    OP_95(0x102, -21500, -6000, -33240, 3000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_23_7F53 end

    def Function_24_7F83(): pass

    label("Function_24_7F83")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xE, 0xFF)
    OP_68(-240, 1200, -33240, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20370, 0)
    SetChrPos(0x101, -750, 0, -32800, 180)
    SetChrPos(0x102, 890, 0, -31800, 180)
    SetChrPos(0x103, -800, 0, -31210, 180)
    SetChrPos(0x104, 800, 0, -33280, 180)
    SetChrPos(0xE, -19170, -5600, -15790, 315)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)

    def lambda_803A():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_803A)

    def lambda_804F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_804F)

    def lambda_8064():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8064)

    def lambda_8079():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8079)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(800)
    EndChrThread(0x103, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        "#0200F#11PHmm? Look...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_8131():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8131)

    def lambda_813E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_813E)
    Sleep(10)

    def lambda_814E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_814E)
    Sleep(300)
    OP_5A()
    OP_68(-17990, -3520, -17700, 4000)
    MoveCamera(0, 22, 0, 4000)
    SetCameraDistance(18500, 4000)
    Sleep(4000)
    ClearMapObjFlags(0xB, 0x10)
    OP_71(0xB, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0xB)
    OP_95(0xE, -17970, -5610, -17000, 3000, 0x0)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_71(0xB, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0xB)
    Sleep(300)
    OP_68(-11490, -3520, -24200, 3500)
    OP_95(0xE, -11470, -6000, -23510, 3000, 0x0)
    Sleep(300)
    OP_93(0xE, 0xE1, 0x1F4)
    Sleep(200)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xE,
        "Marie... Oh, Marie!\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x12C)
    Sleep(200)

    ChrTalk(
        0xE,
        "Where could you have run off to this time?\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xE,
        "Marie, come out!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-6190, -3520, -17670, 2500)
    MoveCamera(20, 22, 0, 1000)
    OP_95(0xE, -7080, -6000, -21580, 4000, 0x0)

    def lambda_82B5():
        OP_95(0xFE, -6360, -2410, -12820, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_82B5)
    Sleep(1800)
    Fade(800)
    OP_68(-240, 1200, -33240, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20370, 0)
    OP_93(0x0, 0x13B, 0x0)
    OP_93(0x1, 0x13B, 0x0)
    OP_93(0x2, 0x13B, 0x0)
    OP_93(0x3, 0x13B, 0x0)
    OP_0D()

    ChrTalk(
        0x104,
        "#11P#0300FDidn't we talk to that lil' missy earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0105FWhat's a little girl like her doing\x01",
            "wandering out on her own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah. What's going on, though?\x01",
            "She's acting sorta strange...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xE, 0x1)
    SetChrPos(0x0, 190, 0, -33400, 180)
    SetChrPos(0xE, -15610, 100, 4480, 315)
    BeginChrThread(0xE, 0, 0, 3)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x4)
    OP_4C(0xE, 0xFF)
    SetMapObjFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    EndChrThread(0x9, 0x0)
    SetChrPos(0x9, 35280, 0, -4370, 45)
    BeginChrThread(0x9, 0, 0, 1)
    SetScenarioFlags(0x70, 1)
    ModifyEventFlags(0, 1, 0x80)
    Sleep(800)
    EventEnd(0x5)
    Return()

    # Function_24_7F83 end

    def Function_25_8474(): pass

    label("Function_25_8474")

    OP_4B(0xE, 0xFF)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-15490, 900, 2940, 0)
    MoveCamera(52, 28, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, -15850, 0, 1880, 0)
    SetChrPos(0x102, -15980, 0, 170, 0)
    SetChrPos(0x103, -14220, 0, 1940, 0)
    SetChrPos(0x104, -14350, 0, 240, 0)
    SetChrPos(0xE, -15080, 0, 4800, 270)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 0, 0, 26)

    ChrTalk(
        0xE,
        "#5PWhere has she gone off to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005FExcuse me, are you searching for something?\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)

    ChrTalk(
        0xE,
        "#5PYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FAre you looking for a kitten by any chance?\x01",
            "One like this?\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd produced the kitten from his jacket pocket.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_63(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xE,
        "#5P#4SMarie!\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xE, 0xFFFFC2E8, 0x0, 0xA14, 0x1B58, 0x0)
    Sleep(400)
    OP_96(0xE, 0xFFFFC518, 0x0, 0x12C0, 0xBB8, 0x0)
    OP_93(0xE, 0xE1, 0x1F4)
    Sleep(200)
    Fade(500)
    ClearChrFlags(0xF, 0x80)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xE,
        "#5POh, thank goodness! You're safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5POh, you silly girl! Where'd you run off to?\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(300)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#12P#0000FI suppose that makes matters easier, then.\x01",
            "You must be her owner, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    OP_63(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    def lambda_87B0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87B0)
    OP_96(0xF, 0xFFFFC040, 0x0, 0x1040, 0x1770, 0x0)

    def lambda_87D1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87D1)
    OP_96(0xF, 0xFFFFC180, 0x0, 0x12D4, 0x1770, 0x0)

    def lambda_87F2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_87F2)
    OP_96(0xF, 0xFFFFC40A, 0x0, 0x14FA, 0x1770, 0x0)

    def lambda_8813():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8813)
    Sleep(300)
    OP_93(0xE, 0xB4, 0x1F4)
    TurnDirection(0xF, 0xE, 300)

    ChrTalk(
        0xE,
        "#5PN-Not exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PMarie is actually a stray cat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#0200FShe is stray? Even though she had a collar?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PMarie may be a stray, but she's still mine!\x01",
            "That's why I went and gave her a collar.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x104,
        "#11P#0306FHuh, can't say I saw that comin'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PTh-The truth is...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xE1, 0x12C)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PI wanted to keep Marie at my house,\x01",
            "but Father would never allow that.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xE,
        "#5PAfter all, Marie...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x0, 0x12C, 0xBB8, 0x320)

    ChrTalk(
        0xE,
        (
            "#5P#4SM-Marie tore up all of Father's important\x01",
            "work papers!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0xE, 0x13B, 0x1F4)
    BeginChrThread(0xE, 0, 0, 27)

    ChrTalk(
        0xE,
        "#5P*sob* I saw her do it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PMarie came in through the window and\x01",
            "took an afternoon nap in Father's study...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PAfter she woke up, she tore all of his\x01",
            "papers to shreds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P*sob* I'm so sorry, Father!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F...\x02\x03",
            "I think it would have been better if you had\x01",
            "explained the situation to your father as\x01",
            "soon as it happened.\x02\x03",
            "#0000FThe kitten sped off somewhere once she\x01",
            "finished ripping up the documents, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P*sob*... *nod*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FSo you started searching for Marie\x01",
            "because you were worried about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P*sniff*... *nod*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0104FPhew. I'd say that's case closed, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FThose were quality deductions, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FWell, I s'pose kittens will do as they\x01",
            "please, y'know?\x02\x03",
            "Damn near impossible to get them\x01",
            "to behave how you want, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FYeah. You're probably thinking that there's\x01",
            "no hope of keeping Marie at your house.\x02\x03",
            "#0000FIf you love her so much, then why not try\x01",
            "explaining the circumstances to your father?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0xE, 0x0)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xE, 0x101, 500)
    Sleep(600)

    ChrTalk(
        0x102,
        (
            "#12P#0100FThat would be best. Don't worry-- we'll\x01",
            "be by your side.\x02\x03",
            "Let's go speak to your father together,\x01",
            "shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P...*nods*\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0350", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_8474 end

    def Function_26_8F54(): pass

    label("Function_26_8F54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8F92")
    OP_95(0xE, -16110, 0, 4800, 1000, 0x0)
    Sleep(500)
    OP_95(0xE, -13570, 0, 4800, 1000, 0x0)
    Sleep(500)
    Jump("Function_26_8F54")

    label("loc_8F92")

    Return()

    # Function_26_8F54 end

    def Function_27_8F93(): pass

    label("Function_27_8F93")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FCF")
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(1200)
    OP_A6(0xE, 0x0, 0xF, 0x3E8, 0xBB8)
    Sleep(2200)
    Jump("Function_27_8F93")

    label("loc_8FCF")

    Return()

    # Function_27_8F93 end

    def Function_28_8FD0(): pass

    label("Function_28_8FD0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1400, 1700, -2500, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(12300, 0)
    SetChrPos(0x101, 0, 0, -2800, 0)
    SetChrPos(0x102, -1200, 0, -2800, 0)
    SetChrPos(0x103, -1200, 0, -4250, 0)
    SetChrPos(0x104, 0, 0, -4250, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#6P#0100FThis is the house of Representative\x01",
            "Campbell, who sent the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FWe're searching for someone important, right?\x01",
            "It sounded like the representative was freaking out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 400)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#12P#0305FHey, doesn't Mademois-Elie's gramps live\x01",
            "'round these parts?\x02\x03",
            "#0300FYou happen to know this Campbell guy?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91AF():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91AF)

    def lambda_91BC():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91BC)

    def lambda_91C9():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_91C9)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5P#0103FWell, about as much as fellow neighbors\x01",
            "would know each other.\x02\x03",
            "#0100FRepresentative Campbell is an ambitious man.\x01",
            "He's so driven by his passion for politics that\x01",
            "he often brushes aside everything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI see. That matches the way I had envisioned\x01",
            "him in my head.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92FE():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92FE)
    Sleep(100)

    def lambda_930E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_930E)

    def lambda_931B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_931B)

    def lambda_9328():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9328)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#11P#0000FEither way, he's requesting our assistance.\x01",
            "Let's try asking about it if he's home.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -480, 0, -2810, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_29(0x2D, 0x1, 0x0)
    OP_70(0x0, 0xA)
    OP_65(0x2, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_8FD0 end

    def Function_29_93D1(): pass

    label("Function_29_93D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_948D")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000FWhoops... We have the kitten with us.\x02\x03",
            "It's probably not the best idea to leave\x01",
            "the city with her in tow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    label("loc_948D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9596")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954B")

    ChrTalk(
        0x101,
        (
            "#0000FThis is the city's north exit.\x02\x03",
            "We have no reason to leave the city right now.\x01",
            "Let's focus on working within the city limits for\x01",
            "the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9580")

    label("loc_954B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9580")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_9596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_963F")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FWe'll need to leave Crossbell City via the\x01",
            "eastern gate to get to Armorica Village.\x02\x03",
            "C'mon, let's head for East Street.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_963F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9717")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0000FWe'll need to leave Crossbell City via the\x01",
            "southern gate to get to St. Ursula Medical College.\x02\x03",
            "Let's head to Central Square. We\x01",
            "can get to Station Street from there.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_9717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9805")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97BA")

    ChrTalk(
        0x101,
        (
            "#0000FWe aren't supposed to leave the city.\x02\x03",
            "KeA's safety is our top priority, and we can't\x01",
            "do anything to jeopardize that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_97EF")

    label("loc_97BA")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_97EF")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_9805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A6")

    ChrTalk(
        0x101,
        (
            "#0003FThis is the city's north exit.\x02\x03",
            "We already have our hands full with the\x01",
            "Heiyue case, so let's deal with that first.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_98E1")

    label("loc_98A6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There's no reason to leave the city right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_98E1")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)

    label("loc_98F7")

    Return()

    # Function_29_93D1 end

    def Function_30_98F8(): pass

    label("Function_30_98F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99B5")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0000FWhoops... We have the kitten with us.\x02\x03",
            "It's probably not the best idea to wander\x01",
            "the city with her in tow.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 20930, 0, -3610, 270)
    EventEnd(0x4)
    Return()

    label("loc_99B5")

    Return()

    # Function_30_98F8 end

    def Function_31_99B6(): pass

    label("Function_31_99B6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F7")
    Call(0, 22)
    SetScenarioFlags(0x46, 2)
    Jump("loc_9B14")

    label("loc_99F7")


    ChrTalk(
        0x102,
        (
            "#0109FHey, Lloyd. We just spoke with the person\x01",
            "that lives here, right? Shouldn't we move\x01",
            "on to a different residence?\x02\x03",
            "We shouldn't bother them if we don't have\x01",
            "any pressing concerns.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FYeah, you're right...\x01",
            "(Yeah, I suppose there's no need to bother\x01",
            "them any further.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B14")

    TalkEnd(0xFF)
    Return()

    label("loc_9B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CA0")

    ChrTalk(
        0x101,
        "#0005FW-Whoa. This mansion is really impressive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0105FIt looks like the gate is closed, though.\x02\x03",
            "#0109FH-Hey, Lloyd. Wouldn't it be rude to\x01",
            "loiter in front of someone's house\x01",
            "if we don't have any business here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah, you're right. Whoever lives here\x01",
            "must be pretty famous.\x02\x03",
            "It'd be wise to not intrude on them so\x01",
            "suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0108F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 2)
    Jump("loc_9CD6")

    label("loc_9CA0")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You have no reason to visit this mansion.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9CD6")

    TalkEnd(0xFF)
    Return()

    # Function_31_99B6 end

    def Function_32_9CDA(): pass

    label("Function_32_9CDA")

    Return()

    # Function_32_9CDA end

    def Function_33_9CDB(): pass

    label("Function_33_9CDB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D04")
    Call(0, 21)
    Jump("loc_9D2A")

    label("loc_9D04")

    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9D2A")

    TalkEnd(0xFF)
    Return()

    # Function_33_9CDB end

    def Function_34_9D2E(): pass

    label("Function_34_9D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D4F")
    Call(0, 28)
    Return()

    label("loc_9D4F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FBC")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EFE")

    ChrTalk(
        0x102,
        (
        "#0105FI believe Representative Campbell\x01",
        "lives in this mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FRepresentative Campbell? Who's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0103FHe's the leader of the Republican Faction\x01",
            "of the diet. You'd be surprised how far his\x01",
            "influence can reach.\x02\x03",
            "#0100FIt'd be wise for us to not bother him if we\x01",
            "don't have any business here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FGood call. I think I'll pass on meeting him until\x01",
            "we have a reason to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FB4")

    label("loc_9EFE")


    ChrTalk(
        0x101,
        (
            "#0005FHaven't we heard about this place from Elie, already?\x02\x03",
            "#0001FI believe she said this was Representative\x01",
            "Campbell's home. The leader of the Republican\x01",
            "Faction of the diet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FB4")

    SetScenarioFlags(0x46, 3)
    Jump("loc_A04B")

    label("loc_9FBC")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the home of Representative Campbell,\x01",
            "the leader of the Republican Faction.\x01",
            "There is no reason to speak with him right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A04B")

    TalkEnd(0xFF)
    Return()

    # Function_34_9D2E end

    def Function_35_A04F(): pass

    label("Function_35_A04F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-18070, 2300, 9900, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13550, 0)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    LoadChrToIndex("chr/ch20700.itc", 0x20)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, -16860, 0, 16000, 180)
    SetChrPos(0xEF, -17740, 0, 17160, 180)
    SetChrPos(0x153, -18240, 0, 15330, 180)
    SetChrPos(0x11, -15230, 0, 1710, 0)
    SetChrPos(0x12, -16050, 0, 120, 0)
    SetChrPos(0x13, -15630, 0, -920, 0)
    OP_68(-18070, 2300, 7120, 3000)
    SetCameraDistance(13550, 3000)
    BeginChrThread(0x153, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x0, 3, 0, 36)
    Sleep(100)
    BeginChrThread(0x1, 3, 0, 36)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x153, 3)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x153,
        "#1105F#5PHey, someone's coming!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(300)
    BeginChrThread(0x13, 3, 0, 37)
    Sleep(1000)

    def lambda_A1F8():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A1F8)
    Sleep(50)

    def lambda_A208():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A208)
    Sleep(50)

    def lambda_A218():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A218)

    ChrTalk(
        0x101,
        "#0000F#5POh, it's just you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11PYo, guys! What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11PHello, how are you doing?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2E1")

    ChrTalk(
        0x102,
        (
            "#0109F#5PHello, you three.\x02\x03",
            "#0102FAre you headed off somewhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C1")

    label("loc_A2E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A35D")

    ChrTalk(
        0x103,
        (
            "#0202F#5PHello there.\x02\x03",
            "#0205FAre you children planning on going\x01",
            "out on the highway by yourselves?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C1")

    label("loc_A35D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3C1")

    ChrTalk(
        0x104,
        (
            "#0309F#5PYou kids are as spunky as ever.\x02\x03",
            "#0300FWhere you guys headin' off to?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C1")


    ChrTalk(
        0x13,
        (
            "#11PUmm, Sunday School at the Crossbell\x01",
            "Cathedral is about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004F#5PAh, that's not too far away. You'll probably\x01",
            "be fine on your own, then.\x02\x03",
            "#0002FThat being said, you all must live close\x01",
            "to each other if you have Sunday School\x01",
            "at the same time, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11PI'd gotten so caught up in playing with Ryu\x01",
            "and Zeit that I accidentally ended up\x01",
            "skipping school...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(
        0x11,
        (
            "#5PPsh, it's not like it's your fault.\x01",
            "How could we refuse an invitation\x01",
            "to play with a freakin' giant wolf?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110F#5PZeit's the cutest!\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x153, 500)

    ChrTalk(
        0x11,
        (
            "#11PWait a second now, I don't think\x01",
            "I've ever seen you around before.\x01",
            "What's your name, girl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1101F#5PI'm not 'girl.' I'm KeA!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11PKeA, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11PMy name's Anri, the energetic guy\x01",
            "right here is named Ryu, and the shy\x01",
            "girl over there is Momo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PU-Umm...it's nice to\x01",
            "meet you, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109F#5PYeah, nice to meet you, too!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)

    ChrTalk(
        0x11,
        (
            "#5PYo, we don't exactly have the time\x01",
            "for this right now, do we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIf we don't get going, Sister Marble\x01",
            "is going to destroy us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#11PAh, you're right! Sorry, Lloyd.\x01",
            "You see, we gotta--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#5PI understand, don't worry.\x01",
            "Don't be late now, okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 500)

    ChrTalk(
        0x11,
        "#11PWouldn't dream of it! See ya later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PGoodbye.\x02",
    )

    CloseMessageWindow()
    OP_68(-18980, 2300, 8820, 3000)
    BeginChrThread(0x11, 3, 0, 38)
    Sleep(100)
    BeginChrThread(0x12, 3, 0, 38)
    Sleep(150)
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(2000)

    def lambda_A8EF():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A8EF)

    def lambda_A8FC():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A8FC)

    def lambda_A909():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A909)
    OP_6F(0x79)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#0000F#11PThat's right. Sister Marble is still teaching\x01",
            "Sunday School.\x02\x03",
            "#0005FWait, did the Residential District and West Street\x01",
            "always have classes at the same time?\x02\x03",
            "Elie and I would have known each other for a while\x01",
            "now if that were the case.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB39")

    ChrTalk(
        0x102,
        (
            "#0104F#5PI'm sure the school's structure and scheduling\x01",
            "has changed from when we were attending.\x02\x03",
            "#0100FThey probably had to adjust the quotas to\x01",
            "match Crossbell's rapidly growing population.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F#11PSounds plausible, but I wonder\x01",
            "if it's actually true...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD27")

    label("loc_AB39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC3A")

    ChrTalk(
        0x103,
        (
            "#0204F#5PI am no expert, but it is entirely possible that\x01",
            "the school's structure may have changed from\x01",
            "when you were attending.\x02\x03",
            "#0202FThat is the protocol when a city's population\x01",
            "experiences a boom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#11PMakes sense...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AD27")

    label("loc_AC3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD27")

    ChrTalk(
        0x104,
        (
            "#0300F#5PI don't know squat about it, but the schedule\x01",
            "woulda changed a lil' from when you were\x01",
            "attendin', yeah?\x02\x03",
            "Must have to do with the population\x01",
            "growin' outta control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F#11PYeah, that sounds likely...\x02",
    )

    CloseMessageWindow()

    label("loc_AD27")


    ChrTalk(
        0x153,
        "#1100F#12P...Are we still going to the bus stop?\x02",
    )

    CloseMessageWindow()

    def lambda_AD62():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AD62)
    Sleep(50)

    def lambda_AD72():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_AD72)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0012F#5POh, I almost forgot.\x01",
            "Let's get going, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xBD, 2)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    SetChrPos(0x0, -16860, 0, 13000, 180)
    SetChrPos(0x1, -16860, 0, 13000, 180)
    SetChrPos(0x2, -16860, 0, 13000, 180)
    OP_68(-16860, 2000, 13000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_35_A04F end

    def Function_36_AE51(): pass

    label("Function_36_AE51")


    def lambda_AE56():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE56)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_AE51 end

    def Function_37_AE70(): pass

    label("Function_37_AE70")


    def lambda_AE75():
        OP_98(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE75)
    WaitChrThread(0xFE, 1)

    def lambda_AE93():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE93)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_37_AE70 end

    def Function_38_AEA0(): pass

    label("Function_38_AEA0")


    def lambda_AEA5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEA5)
    WaitChrThread(0xFE, 1)

    def lambda_AEB6():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEB6)
    Sleep(6000)

    def lambda_AED3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AED3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_38_AEA0 end

    SaveToFile()

Try(main)
