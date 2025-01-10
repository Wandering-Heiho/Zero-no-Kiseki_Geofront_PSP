from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1400.bin",                # FileName
        "c1400",                    # MapName
        "c1400",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1400",                  # 0
        "Dino",                   # 1
        "Old Lady Paola",         # 2
        "Vaan",                   # 3
        "Ruze",                   # 4
        "Canon",                  # 5
        "Huey",                   # 6
        "Slash",                  # 7
        "Kienz",                  # 8
        "Sister Hatina",          # 9
        "Koki",                   # 10
        "Young Man in Blue",      # 11
        "Young Man in Blue",      # 12
        "Young Man in Blue",      # 13
        "Young Man in Blue",      # 14
        "Young Man in Red",       # 15
        "Young Man in Red",       # 16
        "Young Man in Red",       # 17
        "Young Man in Red",       # 18
        "Wazy",                   # 19
        "Wald",                   # 20
        "Abbas",                  # 21
        "Grace",                  # 22
        "Ryan",                   # 23
        "Vesse",                  # 24
        "Azel",                   # 25
        "Jed",                    # 26
        "BC1400",                 # 27
        "BC1400",                 # 28
        "BC1400",                 # 29
        "BC1400",                 # 30
        "Central Square",         # 31
        "West Street",            # 32
        "Administrative District",# 33
        "Residential District",   # 34
        "Entertainment District", # 35
        "East Street",            # 36
        "Downtown District",      # 37
        "Harbor District",        # 38
        "IBC",                    # 39
        "Station Street",         # 40
        "Back Alley",             # 41
        "Ursula Road",            # 42
        "East Crossbell Highway", # 43
        "West Crossbell Highway", # 44
        "Mainz Mountain Path",    # 45
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 3, 10, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_144", 0x0002, 3, 6, 180, 0, 0, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms30800.dat", "ms31700.dat", "ms30900.dat", "ms31800.dat", 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_188", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1CC", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", 0, 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_210", 0x0022, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", "ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", "MonsterBattlePostion_124", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch30800.itc",                   # 06
        "chr/ch31800.itc",                   # 07
        "chr/ch25500.itc",                   # 08
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(45090,   -2500,   -21969,  180,  405,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(45099,   -2500,   -23700,  0,    405,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-17750,  0,       -9270,   225,  405,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(1590,    0,       6789,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 37,  -19.450000762939453,   -6.659999847412109,    -0.7099999785423279,   16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.862500190734863,     3.3299999237060547,    0.1420000046491623,    1.0])

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  6,  0x0000)
    DeclActor(-13130,  0,       -7750,   1500,    -13130,  1500,    -7750,   0x007C, 0,  39, 0x0000)
    DeclActor(48640,   -2100,   -22590,  1500,    48640,   -600,    -22590,  0x007C, 0,  38, 0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  40, 0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Administrative District")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential District")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Harbor District")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Station Street")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back Alley")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "Ursula Road")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")
    PlaceName(-97.75, 0.0, 93.1500015258789, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_990",          # 00, 0
        "Function_1_A48",          # 01, 1
        "Function_2_A73",          # 02, 2
        "Function_3_B4C",          # 03, 3
        "Function_4_B95",          # 04, 4
        "Function_5_10F8",         # 05, 5
        "Function_6_1231",         # 06, 6
        "Function_7_13B3",         # 07, 7
        "Function_8_2369",         # 08, 8
        "Function_9_252E",         # 09, 9
        "Function_10_2806",        # 0A, 10
        "Function_11_2CE3",        # 0B, 11
        "Function_12_3756",        # 0C, 12
        "Function_13_41E5",        # 0D, 13
        "Function_14_429B",        # 0E, 14
        "Function_15_4374",        # 0F, 15
        "Function_16_4532",        # 10, 16
        "Function_17_4627",        # 11, 17
        "Function_18_4C36",        # 12, 18
        "Function_19_5CF9",        # 13, 19
        "Function_20_5E7F",        # 14, 20
        "Function_21_60BF",        # 15, 21
        "Function_22_615E",        # 16, 22
        "Function_23_669A",        # 17, 23
        "Function_24_6877",        # 18, 24
        "Function_25_6D65",        # 19, 25
        "Function_26_871A",        # 1A, 26
        "Function_27_C723",        # 1B, 27
        "Function_28_C759",        # 1C, 28
        "Function_29_C78F",        # 1D, 29
        "Function_30_C7EA",        # 1E, 30
        "Function_31_C84F",        # 1F, 31
        "Function_32_C895",        # 20, 32
        "Function_33_C8DF",        # 21, 33
        "Function_34_C920",        # 22, 34
        "Function_35_DC62",        # 23, 35
        "Function_36_F76E",        # 24, 36
        "Function_37_107CE",       # 25, 37
        "Function_38_108F1",       # 26, 38
        "Function_39_10A2D",       # 27, 39
        "Function_40_10A93",       # 28, 40
        "Function_41_10B8B",       # 29, 41
        "Function_42_112BA",       # 2A, 42
        "Function_43_11584",       # 2B, 43
        "Function_44_119BE",       # 2C, 44
        "Function_45_11E23",       # 2D, 45
        "Function_46_134B5",       # 2E, 46
        "Function_47_14208",       # 2F, 47
        "Function_48_14220",       # 30, 48
        "Function_49_14238",       # 31, 49
        "Function_50_149FB",       # 32, 50
        "Function_51_1545A",       # 33, 51
        "Function_52_15C6C",       # 34, 52
        "Function_53_15C81",       # 35, 53
        "Function_54_15C96",       # 36, 54
        "Function_55_15CAB",       # 37, 55
        "Function_56_15CC0",       # 38, 56
        "Function_57_15CE6",       # 39, 57
        "Function_58_15D37",       # 3A, 58
        "Function_59_15D88",       # 3B, 59
        "Function_60_15DD9",       # 3C, 60
        "Function_61_15E2A",       # 3D, 61
    ))


    def Function_0_990(): pass

    label("Function_0_990")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9D0"),
        (1, "loc_9DC"),
        (2, "loc_9E8"),
        (3, "loc_9F4"),
        (4, "loc_A00"),
        (5, "loc_A0C"),
        (6, "loc_A18"),
        (SWITCH_DEFAULT, "loc_A24"),
    )


    label("loc_9D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_9DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_9E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_9F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A00")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A0C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A18")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A24")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A30")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A47")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A30")

    label("loc_A47")

    Return()

    # Function_0_990 end

    def Function_1_A48(): pass

    label("Function_1_A48")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A72")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_A48")

    label("loc_A72")

    Return()

    # Function_1_A48 end

    def Function_2_A73(): pass

    label("Function_2_A73")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B4B")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_A73")

    label("loc_B4B")

    Return()

    # Function_2_A73 end

    def Function_3_B4C(): pass

    label("Function_3_B4C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B94")
    Sleep(4000)
    OP_95(0xFE, -6960, -3800, -27910, 1000, 0x0)
    Sleep(4000)
    OP_95(0xFE, -13650, -3010, -25240, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x12C)
    Sleep(1900)
    Jump("Function_3_B4C")

    label("loc_B94")

    Return()

    # Function_3_B4C end

    def Function_4_B95(): pass

    label("Function_4_B95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C72")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_C3B")

    label("loc_C1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3B")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_C3B")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C72")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C91")
    Event(0, 41)
    Jump("loc_CDB")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    Event(0, 35)
    Jump("loc_CDB")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC2")
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_CDB")

    label("loc_CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDB")
    Event(0, 36)

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CEF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 26)
    Jump("loc_CFE")

    label("loc_CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_CFE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 43)

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D1B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_10E0")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D66")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_10E0")

    label("loc_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_D8C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_D87")
    SetChrFlags(0x8, 0x80)

    label("loc_D87")

    Jump("loc_10E0")

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D9F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_10E0")

    label("loc_D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DB7")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_10E0")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_DD9")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_10E0")

    label("loc_DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E3A")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11340, 0, 1320, 225)
    OP_93(0x8, 0x2D, 0x0)
    TurnDirection(0xA, 0x10, 0)
    TurnDirection(0xB, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1C")
    SetChrFlags(0x8, 0x10)

    label("loc_E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E35")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_E35")

    Jump("loc_10E0")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_EB5")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_E78")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    Jump("loc_EB0")

    label("loc_E78")

    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)

    label("loc_EB0")

    Jump("loc_10E0")

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_EF4")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xD, 2820, 0, -2350, 45)
    SetChrPos(0xE, 3020, 0, -950, 45)
    Jump("loc_10E0")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_F37")
    SetChrPos(0xA, 1220, 0, -1610, 135)
    SetChrPos(0xB, 2410, 0, -2740, 315)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F32")
    SetChrFlags(0xA, 0x10)

    label("loc_F32")

    Jump("loc_10E0")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_F98")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -11120, -220, -14560, 45)
    SetChrPos(0xB, -11150, -820, -15530, 45)
    SetChrPos(0xD, 5010, 0, -7740, 0)
    SetChrPos(0xE, 4090, 0, -6750, 45)
    Jump("loc_10E0")

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_FFD")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    OP_93(0x8, 0x13B, 0x0)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_FF8")
    SetChrFlags(0x11, 0x10)

    label("loc_FF8")

    Jump("loc_10E0")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1052")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_10E0")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_10B2")
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_109C")
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    Jump("loc_10AD")

    label("loc_109C")

    SetChrPos(0x8, 48000, -2100, -22500, 270)

    label("loc_10AD")

    Jump("loc_10E0")

    label("loc_10B2")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10E0")
    SetChrFlags(0xA, 0x10)

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F7")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_10F7")

    Return()

    # Function_4_B95 end

    def Function_5_10F8(): pass

    label("Function_5_10F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1139")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_116C")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_115E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_116C")

    label("loc_115E")

    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117F")
    OP_70(0x7, 0x0)
    Jump("loc_1183")

    label("loc_117F")

    OP_70(0x7, 0x1E)

    label("loc_1183")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_119B")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B9")
    ClearMapObjFlags(0x4, 0x10)

    label("loc_11B9")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D1")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_11D1")

    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EF")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120B")
    Jump("loc_1210")

    label("loc_120B")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_1210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1230")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_1230")

    Return()

    # Function_5_10F8 end

    def Function_6_1231(): pass

    label("Function_6_1231")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131B")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_12B1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1316")

    label("loc_12B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1316")

    Jump("loc_13A7")

    label("loc_131B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No wonder no one trusts the police these days.\x01",
            "They're out here stealing from us treasure chests!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_13A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1231 end

    def Function_7_13B3(): pass

    label("Function_7_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C9")
    Call(0, 34)
    Jump("loc_2368")

    label("loc_13C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E4")
    Call(0, 10)
    Jump("loc_2368")

    label("loc_13E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_151D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(
        0x8,
        (
            "You going in?\x01",
            "Everybody's totally shocked right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hahaha! Just you wait. By tomorrow, I'll be\x01",
            "the great leader of the Vipers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1518")

    label("loc_1489")


    ChrTalk(
        0x8,
        "Haha. I can't believe I did that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I never liked him anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "All he did was boss me around the whole time.\x01",
            "Well, not anymore!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1518")

    Jump("loc_2365")

    label("loc_151D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_170B")
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B0")

    ChrTalk(
        0xFE,
        (
            "I, uh...ran into a tourist with a real cruddy\x01",
            "attitude on the last day of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I-I tried my hardest to rough him up,\x01",
            "but I ended up getting my butt kicked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm supposed to be a member of the fearsome\x01",
            "Vipers, and yet...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A5")

    ChrTalk(
        0x101,
        (
            "#0003FS-Sounds unfortunate...\x01",
            "(Doesn't look like fighting is his forte.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1111F???\x01",
            "(That guy looks funny!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    SetScenarioFlags(0xD8, 2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F4")

    label("loc_16B0")


    ChrTalk(
        0xFE,
        (
            "I'm supposed to be a member of the fearsome\x01",
            "Vipers, and yet...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F4")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2365")

    label("loc_170B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_174F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1747")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_1731")
    Call(0, 8)
    Jump("loc_1742")

    label("loc_1731")

    TurnDirection(0x8, 0x0, 0)
    Call(0, 9)
    OP_93(0x8, 0x2D, 0x0)

    label("loc_1742")

    Jump("loc_174A")

    label("loc_1747")

    Call(0, 8)

    label("loc_174A")

    Jump("loc_2365")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1844")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_17B0")

    ChrTalk(
        0x8,
        (
            "I sure hope I get to join in on the\x01",
            "beatdowns someday...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B3")

    label("loc_17B0")

    Call(0, 9)

    label("loc_17B3")

    Jump("loc_183F")

    label("loc_17B8")


    ChrTalk(
        0x8,
        (
            "I wish they would let me join them\x01",
            "in their morning scrimmages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heh. Just you wait! One day, I'll be\x01",
            "just as strong as Wald!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183F")

    Jump("loc_2365")

    label("loc_1844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_19D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18E9")

    ChrTalk(
        0xFE,
        (
            "Now that I'm a member of the Vipers,\x01",
            "I'm not gonna go to some lame festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, for the record, I'm not sad about it,\x01",
            "all right?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19CF")

    label("loc_18E9")


    ChrTalk(
        0xFE,
        (
            "More and more people are getting into the\x01",
            "festive mood, now that the festival is near.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "H-Hah. What a bunch of losers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Us Saber Vipers go hard! We're not gonna\x01",
            "prance around some festival like a bunch\x01",
            "of sissies!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19CF")

    Jump("loc_2365")

    label("loc_19D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A58")

    ChrTalk(
        0x8,
        "I'm not gonna let you fool me again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Just piss off already! You're gonna\x01",
            "bother the other members!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B14")

    label("loc_1A58")


    ChrTalk(
        0x8,
        "Hey, good work!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Wait, it's just you guys again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I swear to Aidios, you're doing this\x01",
            "on purpose now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FI promise you it wasn't intentional.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B14")

    Jump("loc_2365")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BAC")

    ChrTalk(
        0x8,
        (
            "I managed to greet Wald with all my might!\x01",
            "Kinda weird, though. All I got was a simple\x01",
            "'s'up' in response.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C24")

    label("loc_1BAC")


    ChrTalk(
        0x8,
        "Wald just got back a minute ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "S'up! Good job out there!\x01",
            "Nice, I managed to greet him with all my might!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C24")

    Jump("loc_1DC5")

    label("loc_1C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF5")

    ChrTalk(
        0xFE,
        (
            "Oh, yeah. I heard some weird banging\x01",
            "noise earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have no idea where it was coming from, though.\x01",
            "Didn't sound like it was coming from Ignis.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D43")

    label("loc_1CF5")


    ChrTalk(
        0x8,
        (
            "Don't get in the way of the other members!\x01",
            "They're all hella busy today!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D43")

    Jump("loc_1DC5")

    label("loc_1D48")


    ChrTalk(
        0x8,
        "Hey, good work out there!\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Wait, it's just you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Man, stop confusing me like that!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1DC5")

    Jump("loc_2365")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E63")
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0x8,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Don't 'Hello!' me! We taught you how to\x01",
            "greet us, now put your back into it!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        "S-S'UP!\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_4C(0x11, 0xFF)
    Jump("loc_2365")

    label("loc_1E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1F79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F04")

    ChrTalk(
        0x8,
        "I'm about to go visit someone at the hospital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "D-Don't even think about trying to stop\x01",
            "me, okay?! I'll kick your ass if you do!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F74")

    label("loc_1F04")


    ChrTalk(
        0x8,
        "Ugh... Koki got done in by the Testaments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He stuck out his neck for me all the time...\x01",
            "*sniff*...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F74")

    Jump("loc_2365")

    label("loc_1F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FD2")

    ChrTalk(
        0x8,
        (
            "G-Get outta here already!\x01",
            "There's no way I'll trust you now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215E")

    label("loc_1FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 6)), scpexpr(EXPR_END)), "loc_2047")

    ChrTalk(
        0x8,
        "H-How dare you do that to Wald!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "G-Get outta here already!\x01",
            "There's no way I'll trust you now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D2")

    label("loc_2047")


    ChrTalk(
        0x8,
        (
            "I-I can't believe you were an even\x01",
            "match with Wald...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys must have pulled some kinda\x01",
            "underhanded trick. You can't fool me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D2")


    ChrTalk(
        0x101,
        "#0003F(Man, this kid never lets up...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Yeah, you probably shattered his worldview\x01",
            "after matchin' up to his role model.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_215E")

    Jump("loc_2365")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_21F9")

    ChrTalk(
        0x8,
        "Wald gave the okay for you to enter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll let you in, but if I catch you trying to\x01",
            "pull any funny business...you're finished!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_22DA")

    NpcTalk(
        0xFE,
        "Young Man in Red",
        (
            "Hey, you got somethin' you wanna\x01",
            "say to me?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Young Man in Red",
        "Quit starin' and get the hell outta here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Looks like we're out of luck. Let's go\x01",
            "pay the other gang a visit.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2365")

    label("loc_22DA")


    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "Wh-What are you looking at?!\x01",
            "You got a problem with me?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "Get the hell outta here!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2365")
    SetScenarioFlags(0x53, 4)

    label("loc_2365")

    TalkEnd(0xFE)

    label("loc_2368")

    Return()

    # Function_7_13B3 end

    def Function_8_2369(): pass

    label("Function_8_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2420")

    ChrTalk(
        0x8,
        (
            "I'm sure I'll be getting my\x01",
            "own bat sooner or later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You better watch out! Once I get my hands\x01",
            "on one, neither you nor the Testaments will\x01",
            "be able to stop me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252D")

    label("loc_2420")


    ChrTalk(
        0x8,
        (
            "*woosh*...*woosh*...!\x01",
            "Take this!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "Wh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'm working on my fighting skills.\x01",
            "Don't interrupt me when I'm in the zone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305FDoin' a lil' mental training, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "H-Hey, it's not like I wanna! They\x01",
            "haven't given me a bat yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_252D")

    Return()

    # Function_8_2369 end

    def Function_9_252E(): pass

    label("Function_9_252E")


    ChrTalk(
        0x8,
        (
            "Wh-What the hell's up with you guys?!\x01",
            "You have the guts to show your faces here?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I-I-I-I'll take you guys down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FUh... Still on guard duty?\x01",
            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Screw you! Don't mock me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I'll definitely be a part of the next fight.\x01",
            "You just wait and see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0205FOn that note...I fail to recall your\x01",
            "presence at the practice session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Jed made me stay behind while he\x01",
            "went to fight with everybody else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, but he's already back! I wasn't\x01",
            "lonely or anything, I swear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303FUh, sure. Don't sweat it, dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FI hope you'll be able to train with\x01",
            "everybody soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "Wh-What the hell's your problem?!\x01",
            "Didn't I just tell you to not mock me?!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0x91, 0)
    Return()

    # Function_9_252E end

    def Function_10_2806(): pass

    label("Function_10_2806")

    EventBegin(0x0)
    Fade(500)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x8,
        "Young Man in Red",
        "Y-You guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FThose clothes...\x02\x03",
            "#0001FIs this place supposed to be\x01",
            "the Saber Vipers' home base?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3P#0200F'Ignis'...\x02\x03",
            "I believe this was once a warehouse,\x01",
            "now remodeled into a venue.\x02\x03",
            "#0203FThey do not pay taxes, so I am unaware\x01",
            "of the specifics.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29D7():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29D7)
    WaitChrThread(0x8, 1)

    NpcTalk(
        0x8,
        "Young Man in Red",
        "D-Don't just ignore me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "I may be a rookie, but I'm still a proud\x01",
            "member of the Saber Vipers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0005FOh, sorry about that.\x02\x03",
            "#0000FWe were hoping to have a discussion\x01",
            "with your boss...\x02\x03",
            "Do you think you could let us in?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "You want to see Wald?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "Hah! There's no way a bunch of dogs\x01",
            "could ever dream of meeting him!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "Feel free to get the HELL outta here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0003F(He's dead set on not letting us in.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Probably not a good idea to\x01",
            "bust in there, either...)\x02\x03",
            "(Wanna check up on the other\x01",
            "gang first?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(That sounds like a good idea to me.\x01",
            "We can return here afterwards.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x52, 7)
    EventEnd(0x5)
    Return()

    # Function_10_2806 end

    def Function_11_2CE3(): pass

    label("Function_11_2CE3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D77")
    Jump("loc_2DC1")

    label("loc_2D77")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D97")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC1")

    label("loc_2D97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DB7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DC1")

    label("loc_2DB7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DC1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2E44")

    ChrTalk(
        0x9,
        (
            "Oh, dear. It's become quite dark,\x01",
            "hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I must return home soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2EA5")

    ChrTalk(
        0x9,
        "O-Oh... Could you speak up, please?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "My hearing isn't what it used to be.\x02",
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_2EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F1C")

    ChrTalk(
        0x9,
        (
            "I saw a butterfly take flight\x01",
            "a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Spring has really started to\x01",
            "settle in, hasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_2F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_302E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC7")

    ChrTalk(
        0xFE,
        (
            "Those little delinquents have been\x01",
            "behaving peculiarly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My ears aren't what they used to be,\x01",
            "so I can't quite make out their words.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3029")

    label("loc_2FC7")


    ChrTalk(
        0xFE,
        (
            "Those boys in the red tracksuits have\x01",
            "been behaving strangely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What has them acting up?\x02",
    )

    CloseMessageWindow()

    label("loc_3029")

    Jump("loc_374E")

    label("loc_302E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3073")

    ChrTalk(
        0x9,
        (
            "*yawn*...\x01",
            "The weather is absolutely lovely today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30DA")

    ChrTalk(
        0x9,
        "Zzz... Oh! That was close!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I sometimes can't help but doze off\x01",
            "on warmer days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_30DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3169")

    ChrTalk(
        0x9,
        (
            "I have trouble walking, so I often\x01",
            "have to stop and rest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That just makes me happier\x01",
            "to see the kids running around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3201")

    ChrTalk(
        0x9,
        (
            "Hmm... I wonder what I should\x01",
            "cook for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sometimes you have to indulge yourself\x01",
            "in a particularly delicious meal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32B8")

    ChrTalk(
        0x9,
        "Oh, could I help you kids with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some people came by earlier to try and\x01",
            "ask a question of dear old me, but my\x01",
            "hearing isn't quite what it used to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_32B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3370")

    ChrTalk(
        0x9,
        "Oh, dearie! It's those kids in the tracksuits...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I often see them around these parts, but\x01",
            "I can't help but feel that something may\x01",
            "have happened to those boys.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3468")

    ChrTalk(
        0x9,
        (
            "I do believe it's been about twenty years\x01",
            "since the Crossbell Station was built.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I remember there being a gigantic\x01",
            "celebration to usher it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "These days, we even have an airport!\x01",
            "Life sure is much more convenient now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3468")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_34E9")

    ChrTalk(
        0x9,
        "The youngsters are as energetic as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We're all basking in the sun's warmth.\x01",
            "Today will be fantastic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_34E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_35B1")

    ChrTalk(
        0x9,
        (
            "Those kids with the tracksuits pass\x01",
            "through here often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "These old ears of mine couldn't make out\x01",
            "what all the fuss was about, but I'm just\x01",
            "glad everyone's enjoying themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_35B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_3671")

    ChrTalk(
        0x9,
        "Oh, is something going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A group of those kids had gathered here\x01",
            "a short while ago, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "These old ears of mine couldn't make out\x01",
            "what all the fuss was about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_3671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_36FB")

    ChrTalk(
        0x9,
        (
            "Oh, dearie...\x01",
            "Could I help you children with something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry, but my ears aren't quite what\x01",
            "they used to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374E")

    label("loc_36FB")


    ChrTalk(
        0x9,
        "Ah, yet another lovely day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I think I shall soak in some of the rays.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_374E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_2CE3 end

    def Function_12_3756(): pass

    label("Function_12_3756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3853")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_37E6")

    ChrTalk(
        0xFE,
        "Hahaha! Was there another fight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That sounds way cooler than the sister's\x01",
            "snoozefest lessons!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_384E")

    label("loc_37E6")


    ChrTalk(
        0xFE,
        "Hahaha! Was there another fight?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That sounds way cooler than the sister's\x01",
            "snoozefest lessons!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384E")

    Jump("loc_41E1")

    label("loc_3853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_38EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_38E6")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Man, my deadbeat dad craps away his\x01",
            "entire day drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, whatever. I might go get\x01",
            "some food scraps.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_38E9")

    label("loc_38E6")

    Call(0, 13)

    label("loc_38E9")

    Jump("loc_41E1")

    label("loc_38EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_396E")

    ChrTalk(
        0xA,
        (
            "Haven't heard a peep out of our friendly\x01",
            "neighborhood hoodrats today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hahaha! I'm so bored without 'em!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E1")

    label("loc_396E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A33")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "That big dude with the weird haircut\x01",
            "kinda scares the hell outta me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I get some bad vibes from their group...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Promise me you'll never go near them.\x01",
            "Okay, Ruze?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_41E1")

    label("loc_3A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3A9F")

    ChrTalk(
        0xFE,
        (
            "I think that sister just went into\x01",
            "Jingo's place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hahaha! Now's our chance to hide!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E1")

    label("loc_3A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3AB0")
    Call(0, 14)
    Jump("loc_41E1")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3AF4")

    ChrTalk(
        0xA,
        "Hehehe... Time to ruin the class again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF7")

    label("loc_3AF4")

    Call(0, 15)

    label("loc_3AF7")

    Jump("loc_41E1")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B4B")

    ChrTalk(
        0xA,
        "My old man's a deadbeat drunk... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hahahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA6")

    label("loc_3B4B")


    ChrTalk(
        0xA,
        (
            "Hahaha!\x01",
            "What do you wanna play today, Ruze?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You wanna beat up some old boxes?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3BA6")

    Jump("loc_41E1")

    label("loc_3BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C40")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Then again, my old man can't\x01",
            "seem to do anything but drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "We might wake him up if we make too much noise.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_3C43")

    label("loc_3C40")

    Call(0, 16)

    label("loc_3C43")

    Jump("loc_41E1")

    label("loc_3C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C99")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "Hehehe... Wanna try catching some rats next?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_3D03")

    label("loc_3C99")


    ChrTalk(
        0xA,
        "I just dropped a bunch of newts into this drain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "*sploosh* *sploosh*!\x01",
            "Ahahahaha!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3D03")

    Jump("loc_41E1")

    label("loc_3D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D6F")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "Oh, crap! Come on, Ruze. We gotta hide!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Are they going to fight again?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_41E1")

    label("loc_3D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2E")

    ChrTalk(
        0xA,
        (
            "My old man's still drinking life away\x01",
            "in his room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "It's already noon, and he's still at it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hahaha. All he ever does is drink alcohol.\x01",
            "What a loser!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E8D")

    label("loc_3E2E")


    ChrTalk(
        0xA,
        "My old man's STILL drinking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hahaha. All he ever does is drink alcohol\x01",
            "What a loser!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E8D")

    Jump("loc_41E1")

    label("loc_3E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3ED1")

    ChrTalk(
        0xA,
        "My old man's a deadbeat drunk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Wahooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41E1")

    label("loc_3ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F39")

    ChrTalk(
        0xA,
        "Those hoodrats never let up, do they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "They off fighting someone again?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F9D")

    label("loc_3F39")


    ChrTalk(
        0xA,
        (
            "Huh...? I definitely thought they'd be fighting\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "The heck happened to them?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3F9D")

    Jump("loc_41E1")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_40C0")
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404F")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xA,
        (
            "Hehehe. That was a close call. I have a feeling\x01",
            "that today's going to be the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You might want to stay inside today, Ruze.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40B7")

    label("loc_404F")


    ChrTalk(
        0xFE,
        (
            "Those hoodrats are going to be back any\x01",
            "second now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe...\x01",
            "We sure cut it close this time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B7")

    OP_4C(0xB, 0xFF)
    Jump("loc_41E1")

    label("loc_40C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4130")

    ChrTalk(
        0xA,
        "What do you wanna play next?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You wanna bust open the pipes\x01",
            "and flood the area? Hahaha!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E1")

    label("loc_4130")


    ChrTalk(
        0xA,
        "Oh, you guys are from the city.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "You'd better watch your backs down here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There's a bunch of hoodrats around here,\x01",
            "and they're itchin' for a fight.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_41E1")

    TalkEnd(0xFE)
    Return()

    # Function_12_3756 end

    def Function_13_41E5(): pass

    label("Function_13_41E5")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "I haven't eaten anything today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sniff*... I'm so hungry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Oh, fine. Want me to go\x01",
            "get some scraps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey, you.\x01",
            "Give us some food!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Feed us!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_41E5 end

    def Function_14_429B(): pass

    label("Function_14_429B")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "That damn sister always annoys\x01",
            "the heck outta me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Why does she even bother coming every week?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Who knows?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Does it even matter? You're just going to\x01",
            "chase her away anyway, right?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_429B end

    def Function_15_4374(): pass

    label("Function_15_4374")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    ChrTalk(
        0xA,
        "Are you seriously back again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This sister sure doesn't\x01",
            "know when to give up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Yes, yes. Whatever you kids say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Let's get a move on, kiddos.\x01",
            "We have a lesson to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'll see to it that both of you properly\x01",
            "pay attention to today's lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hahaha! You really can't take a hint, can you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "*sigh* I think I'll have to teach you a lesson\x01",
            "on how to speak with your elders.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_15_4374 end

    def Function_16_4532(): pass

    label("Function_16_4532")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "The Anniversary Festival?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hey Ruze, you got anybody that\x01",
            "can take you there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "No, not really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heehee...\x01",
            "You're all I've got, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Dang, that sucks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Maybe I'll force my dad to man up\x01",
            "and take us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_4532 end

    def Function_17_4627(): pass

    label("Function_17_4627")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4706")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_46AB")

    ChrTalk(
        0xFE,
        "You guys are really strong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If...I'm ever in trouble again, I hope\x01",
            "you guys save me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F1")

    label("loc_46AB")


    ChrTalk(
        0xFE,
        (
            "Heehee.\x01",
            "You guys are really strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You still lost, though.\x02",
    )

    CloseMessageWindow()

    label("loc_46F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4701")
    OP_93(0xFE, 0x2D, 0x0)

    label("loc_4701")

    Jump("loc_4C32")

    label("loc_4706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_47A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_479A")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        (
            "That waitress at the Wong Wao\x01",
            "is sooooooo nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Maybe I can get her to give\x01",
            "me some of her food...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_479D")

    label("loc_479A")

    Call(0, 13)

    label("loc_479D")

    Jump("loc_4C32")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_47FA")

    ChrTalk(
        0xB,
        "I saw the boss of those boys in blue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I wonder what he's up to.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_47FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_482D")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xB,
        "Yeah, I got it.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_4C32")

    label("loc_482D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_48BB")

    ChrTalk(
        0xFE,
        (
            "You know, Jingo hasn't shown up for\x01",
            "any of the sister's lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sure must be hard on the sister\x01",
            "to deal with her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_48BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_48CC")
    Call(0, 14)
    Jump("loc_4C32")

    label("loc_48CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_494A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4942")

    ChrTalk(
        0xB,
        (
            "That poor sister can't seem to catch\x01",
            "a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "She's always being toyed with\x01",
            "by Vaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4945")

    label("loc_4942")

    Call(0, 15)

    label("loc_4945")

    Jump("loc_4C32")

    label("loc_494A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_49B0")

    ChrTalk(
        0xB,
        "Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you keep talking while running,\x01",
            "you're going to run out of breath!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_49B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A10")

    ChrTalk(
        0xB,
        (
            "Hey, what are you guys going to do\x01",
            "during the Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A13")

    label("loc_4A10")

    Call(0, 16)

    label("loc_4A13")

    Jump("loc_4C32")

    label("loc_4A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A60")

    ChrTalk(
        0xB,
        "Prepare to meet your doom, Mr. Newt!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*sploosh*!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4AB6")

    ChrTalk(
        0xB,
        "I'm hungry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I wonder if anybody left food sitting around...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B14")

    ChrTalk(
        0xB,
        "Heeheehee...at least Vaan has a dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "He's kind of a deadbeat, though.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4B38")

    ChrTalk(
        0xB,
        "Hahaha! Wait up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4B7A")

    ChrTalk(
        0xB,
        "Oh, I give up already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I just wanna play.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C32")

    label("loc_4B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_4BD8")
    OP_4B(0xA, 0xFF)
    OP_93(0xFE, 0x87, 0x0)

    ChrTalk(
        0xB,
        "Hey, what were they like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Were they really that scary?\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_4C32")

    label("loc_4BD8")


    ChrTalk(
        0xB,
        (
            "Those scary guys seem scarier\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You cityfolk better watch yourselves.\x02",
    )

    CloseMessageWindow()

    label("loc_4C32")

    TalkEnd(0xFE)
    Return()

    # Function_17_4627 end

    def Function_18_4C36(): pass

    label("Function_18_4C36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4D01")

    ChrTalk(
        0xC,
        "*yaawn* I'm starting to get a little sleepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I managed to get a ton of work done today.\x01",
            "I need to get home before it gets dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I gotta be up bright and early tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CF5")

    label("loc_4D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D63")

    ChrTalk(
        0xC,
        (
            "I hope those traders were pleased.\x01",
            "Haha. I'm looking forward to this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E39")

    label("loc_4D63")


    ChrTalk(
        0xC,
        "Welp. Time to do some more cleaning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I gathered a bunch of scrap metal I found lying\x01",
            "around and sold it to some traders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hope those traders managed to find something\x01",
            "shiny in that pile of junk.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4E39")

    Jump("loc_5CF5")

    label("loc_4E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4ED3")

    ChrTalk(
        0xC,
        (
            "What's with all the yelling I've been hearing?\x01",
            "I dunno about you, but I'm starting to get\x01",
            "a little bit anxious about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F3A")

    label("loc_4ED3")


    ChrTalk(
        0xC,
        (
            "What the heck are we supposed to do\x01",
            "about those delinquents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm feeling kinda anxious...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4F3A")

    Jump("loc_5CF5")

    label("loc_4F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FFC")

    ChrTalk(
        0xC,
        (
            "I like all the different shapes in the pavement.\x01",
            "They're relaxing to look at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm staring at it all day when I clean, and\x01",
            "I somehow manage to never get bored of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CF5")

    label("loc_4FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_518B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5071")
    TurnDirection(0xC, 0x153, 0)

    ChrTalk(
        0xC,
        "You just leave the cleaning to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I've cleaned up a mess or two in my time!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5186")

    label("loc_5071")


    ChrTalk(
        0xC,
        (
            "Hey there, everyone!\x01",
            "Isn't the weather awesome today?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 0)

    ChrTalk(
        0xC,
        (
            "Oh, hey. I haven't seen your face around these parts.\x01",
            "You wanna give me a hand with this cleaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. I hope you're up for it, but it's actually\x01",
            "kinda dangerous. Lotta glass shards lying around.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5186")

    Jump("loc_5CF5")

    label("loc_518B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_52F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5210")

    ChrTalk(
        0xC,
        "Boy, I sure do love festivals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How can I not be excited when the\x01",
            "Anniversary Festival is so close?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F2")

    label("loc_5210")


    ChrTalk(
        0xC,
        (
            "Just hearing the phrase 'Anniversary Festival'\x01",
            "is enough to get me going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I can't contain myself! I'm so excited!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Boy, I sure do love festivals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How can I not? Everybody is so\x01",
            "happy during the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_52F2")

    Jump("loc_5CF5")

    label("loc_52F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_53B8")

    ChrTalk(
        0xC,
        (
            "I wouldn't be able to tell you a thing when it\x01",
            "comes to complicated situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But I am pretty good at cleaning!\x01",
            "Let me tell you, I can clean up a mean spill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5491")

    label("loc_53B8")


    ChrTalk(
        0xC,
        (
            "Y'know, a couple of those guys from the\x01",
            "Testaments greeted me this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I noticed them patrolling the area a lot\x01",
            "more these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Apparently, they don't want the mafia\x01",
            "meddling in their affairs.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5491")

    Jump("loc_5CF5")

    label("loc_5496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_564C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5546")

    ChrTalk(
        0xC,
        "Huh. You guys don't work for the government?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I've been seeing more politicians in the area\x01",
            "lately, so I mistook you for one.\x01",
            "Sorry about that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5647")

    label("loc_5546")


    ChrTalk(
        0xC,
        (
            "Good morning!\x01",
            "Are you guys with the government?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I clean this place every day, so you\x01",
            "won't find as much as a speck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Haha. Everything's squeaky clean today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I bet you could even lay on the ground and\x01",
            "roll around without getting dirty!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5647")

    Jump("loc_5CF5")

    label("loc_564C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_56C5")

    ChrTalk(
        0xC,
        "I like to greet that wolf every morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I feel like he can understand what I'm saying.\x02",
    )

    CloseMessageWindow()
    Jump("loc_577D")

    label("loc_56C5")


    ChrTalk(
        0xC,
        (
            "Y'know, there's a white wolf that comes\x01",
            "through here every morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He seems pretty smart, and his\x01",
            "mane looks so cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. I bet he's watching out\x01",
            "for any baddies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_577D")

    Jump("loc_5CF5")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_587C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5820")

    ChrTalk(
        0xC,
        (
            "I pretty much spend my whole day\x01",
            "cleaning this street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha. Check out how clean it is!\x01",
            "I bet you could eat lunch off of it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5877")

    label("loc_5820")


    ChrTalk(
        0xC,
        "Oh, hey there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Check this out!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Isn't this street so freakin' clean?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5877")

    Jump("loc_5CF5")

    label("loc_587C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_59FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_58F8")

    ChrTalk(
        0xC,
        (
            "Some traders come by here every once\x01",
            "in a blue moon to buy nails and other\x01",
            "scrap metal from us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59FA")

    label("loc_58F8")


    ChrTalk(
        0xC,
        (
            "I like to carry this bag around to store\x01",
            "any scraps I manage to find.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The traders check out what I've picked\x01",
            "up, and end up buying some of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And at the end of the day, the streets are cleaner.\x01",
            "Now that's killing two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_59FA")

    Jump("loc_5CF5")

    label("loc_59FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A62")

    ChrTalk(
        0xC,
        (
            "*sweep, sweep*...\x01",
            "I'm going to clean the heck outta this street today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD8")

    label("loc_5A62")


    ChrTalk(
        0xC,
        "Hey there! Isn't it a fine morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Looking at the great morning sun always\x01",
            "makes me want to try harder.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5AD8")

    Jump("loc_5CF5")

    label("loc_5ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5B5F")

    ChrTalk(
        0xC,
        (
            "I think a fight broke out around here\x01",
            "a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The heck were they fighting about, anyway?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C0B")

    label("loc_5B5F")


    ChrTalk(
        0xC,
        (
            "I think a fight broke out around here\x01",
            "a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I saw a bunch of broken glass and some\x01",
            "blood splatters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "My chest tightened up just looking at it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5C0B")

    Jump("loc_5CF5")

    label("loc_5C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_5C8D")

    ChrTalk(
        0xC,
        (
            "There's a lotta noise coming\x01",
            "from the next street over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "What in Aidios' name is going on over there?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CF5")

    label("loc_5C8D")


    ChrTalk(
        0xC,
        (
            "Um... Will you guys help me pick\x01",
            "up some trash?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks! Every city's gotta\x01",
            "look its cleanest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF5")

    TalkEnd(0xFE)
    Return()

    # Function_18_4C36 end

    def Function_19_5CF9(): pass

    label("Function_19_5CF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5D8E")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "Sweet. All is cool in the plaza.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "This is more than enough, Slash.\x01",
            "Let's hurry up and report back\x01",
            "to Wald!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_5E7B")

    label("loc_5D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5E07")

    ChrTalk(
        0xD,
        "Haven't seen that chick around here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Damn! And just when I thought I'd\x01",
            "go and talk to her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E7B")

    label("loc_5E07")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "Yeah, I feel you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We gotta give those guys a pummeling\x01",
            "they'll never forget!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E73")
    SetScenarioFlags(0x53, 4)

    label("loc_5E73")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_5E7B")

    TalkEnd(0xFE)
    Return()

    # Function_19_5CF9 end

    def Function_20_5E7F(): pass

    label("Function_20_5E7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5F6B")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "Hey, come to think of it. I haven't\x01",
            "seen that chick around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I think I remember her sayin' practice\x01",
            "was pretty tough. Maybe that's why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Who are they even talking about?)\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_60BB")

    label("loc_5F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_604B")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_5FB5")

    ChrTalk(
        0xE,
        "Damn! Is that chick not coming today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_603E")

    label("loc_5FB5")


    ChrTalk(
        0xE,
        "Guess not, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Y'know, she IS always bitchin'\x01",
            "about her practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hahaha! What the hell's she practicin' for, anyway?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_603E")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_60BB")

    label("loc_604B")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        "As if I even give a damn! Hahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Wald's already pissed enough as it is!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B3")
    SetScenarioFlags(0x53, 4)

    label("loc_60B3")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_60BB")

    TalkEnd(0xFE)
    Return()

    # Function_20_5E7F end

    def Function_21_60BF(): pass

    label("Function_21_60BF")

    TalkBegin(0xFE)

    ChrTalk(
        0xF,
        (
            "How the hell do you expect us to turn\x01",
            "a blind eye to something like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Well... I guess I can't ignore Wazy's\x01",
            "orders, either.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615A")
    SetScenarioFlags(0x53, 4)

    label("loc_615A")

    TalkEnd(0xFE)
    Return()

    # Function_21_60BF end

    def Function_22_615E(): pass

    label("Function_22_615E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6476")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "My word. I can't believe the police are getting\x01",
            "into fights with a group of delinquents!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FOh, I wouldn't really call it fighting.\x01",
            "It's more like self-defense lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care how you spin it. You\x01",
            "should never resort to violence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104FWe're teaching them proper sportsmanlike\x01",
            "conduct through these mock battles.\x02\x03",
            "#0100FWe've been coming regularly to help\x01",
            "rehabilitate them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Oh, is that what this is all about?\x01",
            "My mistake, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To be able to open the hearts\x01",
            "of these young ruffians...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a splendid achievement!\x01",
            "I feel I must learn from your example.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(How characteristic of Elie to effortlessly\x01",
            "persuade someone.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300F(Haha. Saved us a scoldin', too.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 5)
    SetScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6471")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_6471")

    Jump("loc_6696")

    label("loc_6476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6522")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "To be able to open the hearts\x01",
            "of these young ruffians...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a splendid achievement!\x01",
            "I feel I must learn from your example.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_651D")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_651D")

    Jump("loc_6696")

    label("loc_6522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_65F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_65EE")

    ChrTalk(
        0x10,
        (
            "These kids never seem to bring\x01",
            "any love for learning whenever\x01",
            "I give them a lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "They hardly ever show up to Sunday School,\x01",
            "so I came here directly to help them out...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65F1")

    label("loc_65EE")

    Call(0, 15)

    label("loc_65F1")

    Jump("loc_6696")

    label("loc_65F6")


    ChrTalk(
        0x10,
        (
            "I've been coming here more regularly to\x01",
            "teach Sunday School lessons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Now, if only I could get the children to\x01",
            "actually take the time to listen to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6696")

    TalkEnd(0xFE)
    Return()

    # Function_22_615E end

    def Function_23_669A(): pass

    label("Function_23_669A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_674C")

    ChrTalk(
        0x11,
        (
            "Listen up. First, we gotta teach you\x01",
            "the greetin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Whenever Wald or any of the other\x01",
            "senior members come up to ya,\x01",
            "you hit them with a 'S'up.' Got it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6873")

    label("loc_674C")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x11,
        "You're still a total newbie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "We gotta make sure you got all\x01",
            "the rules down, one-by-one.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    ChrTalk(
        0x11,
        (
            "Listen up. First, we gotta teach you\x01",
            "the greetin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Whenever Wald or any of the other\x01",
            "senior members come up to ya,\x01",
            "you hit them with a 'S'up.' Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "S-S'up!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_6873")

    TalkEnd(0xFE)
    Return()

    # Function_23_669A end

    def Function_24_6877(): pass

    label("Function_24_6877")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4950, -1840, -23330, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-14810, 2000, -9650, 5000)
    MoveCamera(44, 27, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(24500, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(11430, 2000, 960, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    ClearMapObjFlags(0x5, 0x1000)
    OP_68(38910, 2200, -19760, 7000)
    MoveCamera(32, 17, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(30920, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(2190, 2000, -10020, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(48000, 5000)
    OP_0D()
    PlaceName2(340, 200, "c_plac10", 0x0, 0)
    OP_6F(0x10)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "#0305FDamn, there's a neighborhood down here?\x01",
            "This place really a part of Crossbell City?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x102,
        "#0108FYes, it is. This is the Downtown District.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0001FYeah, I haven't really visited these parts, either.\x02\x03",
            "This place is supposedly the remnants of a\x01",
            "development project from long ago.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        (
            "#0200FAccording to the records, many citizens still\x01",
            "inhabit the area.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0003FInteresting. I didn't know that.\x02\x03",
            "#0000FAt any rate, this place is still within our jurisdiction.\x01",
            "Let's do a quick sweep of the area.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Downtown District is a run-down area\x01",
            "found at the city's outskirts.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "While home to some useful facilities, they are\x01",
            "unavailable in the earlier stages of the game.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Be sure to check back every once in a while\x01",
            "as the story progresses.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetScenarioFlags(0x45, 1)
    EventEnd(0x5)
    Return()

    # Function_24_6877 end

    def Function_25_6D65(): pass

    label("Function_25_6D65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30900.itc", 0x20)
    LoadChrToIndex("chr/ch30950.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x23)
    LoadChrToIndex("chr/ch31850.itc", 0x25)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("apl/ch50014.itc", 0x2A)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1700, 1000, 8700, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1100, 0, 8000, 180)
    SetChrPos(0x102, 2300, 0, 8000, 180)
    SetChrPos(0x103, 1100, 0, 9400, 180)
    SetChrPos(0x104, 2300, 0, 9400, 180)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -1500, 0, -3700, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1500, 0, -6700, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 0, -5600, 90)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 3600, 0, -3700, 270)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 3600, 0, -6700, 270)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 4600, 0, -5400, 270)
    ClearMapFlags(0x10000000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00001.itp")
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400001V#5P#0013FLook, over there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400002V#5P#0305FCheck it out. Looks like things\x01",
            "are 'bout to get heated.\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(1100, 900, -5200, 3000)
    MoveCamera(55, 23, 0, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x16,
        "#0400003V#2PHey, ya blue bastards.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400004V#2PKeep up that ego and yer\x01",
            "gonna get murdered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0400005V#11PHah. Ya damn bugs have been gettin' on\x01",
            "our nerves for far too long!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0400006V#11PPretty ballsy of you to pull this\x01",
            "underhanded crap on us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400007V#6PHmph. This is precisely why you\x01",
            "neanderthals are so annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400008V#6PWe don't need to rely on underhanded tactics\x01",
            "to take care of bums like yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0400009V#3PA-And, besides. You were the ones who\x01",
            "sent one of our boys to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0400010V#3PWhat's the saying? 'An eye for an eye, a\x01",
            "tooth for a tooth'? I hope you're prepared\x01",
            "for the judgment I'm going to pass on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400011V#2PFine by us, ya blue bastards!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400012V#2PWald doesn't need to be here\x01",
            "for us to kick your asses!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x12,
        (
            "#0400013V#6PYou took the words right out of my mouth.\x01",
            "Wazy's presence is unnecessary for us to\x01",
            "take out the trash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400014V#6PPrepare for the crusade, everyone! It's time\x01",
            "we eliminate these Saber Viper scumbags!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Sound(1086, 255, 100, 0)
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x101,
        "Voice",
        "#0400015V#4SHOLD IT!\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    OP_0D()
    Fade(500)
    OP_68(1100, 1000, 800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 600, 0, 7000, 180)
    SetChrPos(0x102, 1800, 0, 9300, 180)
    SetChrPos(0x103, 600, 0, 9300, 180)
    SetChrPos(0x104, 1800, 0, 7000, 180)
    OP_68(1100, 1000, -3200, 2500)
    SetCameraDistance(17500, 2500)

    def lambda_76FE():
        OP_95(0xFE, 600, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76FE)
    Sleep(50)

    def lambda_771B():
        OP_95(0xFE, 1800, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_771B)
    Sleep(50)

    def lambda_7738():
        OP_96(0xFE, 0x258, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7738)
    Sleep(50)

    def lambda_7755():
        OP_96(0xFE, 0x708, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7755)
    OP_0D()

    def lambda_7770():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7770)

    def lambda_777D():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_777D)
    Sleep(50)

    def lambda_778D():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_778D)

    def lambda_779A():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_779A)

    def lambda_77A7():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_77A7)

    def lambda_77B4():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_77B4)
    Sleep(50)

    def lambda_77C4():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_77C4)

    def lambda_77D1():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_77D1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    ChrTalk(
        0x16,
        "#0400016V#2PThe hell...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400017V#6PNever seen 'em around before...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x101,
        (
            "#0400018VCease your fighting immediately!\x02\x03",
            "#0400019VYour thoughtless actions are causing\x01",
            "a disturbance for all of the residents\x01",
            "living here!\x02",
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
        0x17,
        "#0400020V#11PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0400021V#6PWho do you think you are to show up\x01",
            "out of nowhere and tell us what to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400022V#5P#0306F(The downside of not havin' a uniform...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400023V#5P#0108F(How do we proceed?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400024V#5P#0003F(Hmm...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Reveal your Detective Notebook]\x01",                 # 0
            "[Stop them without revealing your identity]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7AB4"),
        (1, "loc_7B8A"),
        (SWITCH_DEFAULT, "loc_7EB2"),
    )


    label("loc_7AB4")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    def lambda_7AC7():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AC7)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0400025V#5P#0007FWe're with the CPD's Special Support Section.\x02\x03",
            "#0400036VWe've received a request from residents of\x01",
            "the area to intervene.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB2")

    label("loc_7B8A")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#0400027V#6PI see. You're just a bunch of damn do-gooder\x01",
            "bracers, aren't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400028V#6PHaven't seen your faces around before.\x01",
            "You rookies, or somethin'?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_7C61():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C61)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400029V#5P#0011FN-No, we aren't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400030V#5P#0206FMistaken for bracers again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400031V#2PTch. You guild dogs are always gettin'\x01",
            "in our way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400032V#2PWe're not gonna let you interfere with our\x01",
            "fight this time!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D5D():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D5D)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0400033V#5P#0013FH-Hold on just a second!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_7DB9():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DB9)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0400034V#5P#0007FYou've got it all wrong. We're not bracers!\x02\x03",
            "#0400035VWe're with the CPD's Special Support\x01",
            "Section.\x02\x03",
            "#0400026VWe've received a request from residents\x01",
            "of the area to intervene.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EB2")

    label("loc_7EB2")

    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x16,
        "#0400037V#2P#4SWHAT?! You're police officers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0400038V#11PHahahahahahaha!\x01",
            "Ain't no way in hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#0400039V#6PThere's no way they'd respond to a request\x01",
            "like that. The cops NEVER come here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400040V#6PAt least come up with a more\x01",
            "convincing lie than that!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400041V#5P#0003FW-We're being serious!\x02\x03",
            "#0400042V#0013FRegardless, that doesn't change the fact\x01",
            "that you're disturbing the other residents!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400043V#5P#0300FIf you're so intent on handin' out ass-kickings,\x01",
            "then why not take it outside the city?\x02\x03",
            "#0400044VI'm sure you guys could use the exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400045V#2PHeh. Ya got guts, I'll give ya that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400046V#2PThinkin' you can waltz into the Downtown\x01",
            "District and run your mouth like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400047V#6PWe have our own code we follow here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400048V#6PKeep pushin' your luck, and you're\x01",
            "going get sent to an early grave.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#0400049V#5P#0013FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400050V#5P#0306FThis ain't lookin' too hot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400051V#5P#0211FAre there no other conclusions to this\x01",
            "situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400052V#5P#0101F*sigh* I suppose we have no other choice.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#0400053V#2PHaha, what do we have here? I didn't\x01",
            "notice how cute those two chicks were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400054V#2PYou tryin' to act cool\x01",
            "so you can impress 'em?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0400055V#11PHey! Why don't you babes ditch these losers\x01",
            "and hang out with some real men?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x16, 500)
    Sleep(200)

    ChrTalk(
        0x12,
        (
            "#0400056V#6PAre you out of your minds? This isn't\x01",
            "the time to hit on women.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x17, 500)
    Sleep(200)

    ChrTalk(
        0x13,
        (
            "#0400057V#6PWhy don't we rid ourselves of these nuisances\x01",
            "first? We can continue our fight after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#0400058V#6PAre you okay with that, red plagues?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x12, 500)
    Sleep(200)

    ChrTalk(
        0x16,
        "#0400059V#2PHah. Fine by us!\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x16,
        "#0400060V#2PTake 'em down, boys!\x02",
    )

    CloseMessageWindow()

    def lambda_86E1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_86E1)
    Sleep(50)
    OP_93(0x13, 0x2D, 0x1F4)
    StopBGM(0x3E8)
    Battle("BattleInfo_144", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CA(0x1, 0xFF, 0x0)
    Call(0, 26)
    Return()

    # Function_25_6D65 end

    def Function_26_871A(): pass

    label("Function_26_871A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30853.itc", 0x20)
    LoadChrToIndex("chr/ch30900.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch30953.itc", 0x23)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch31753.itc", 0x26)
    LoadChrToIndex("chr/ch31850.itc", 0x28)
    LoadChrToIndex("chr/ch31853.itc", 0x29)
    LoadChrToIndex("chr/ch00400.itc", 0x2A)
    LoadChrToIndex("chr/ch02100.itc", 0x2B)
    LoadChrToIndex("chr/ch06700.itc", 0x2C)
    LoadChrToIndex("chr/ch00050.itc", 0x2D)
    LoadChrToIndex("chr/ch00150.itc", 0x2E)
    LoadChrToIndex("chr/ch00250.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("apl/ch50015.itc", 0x31)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1100, 1000, -4200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2E)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 600, 0, -1800, 180)
    SetChrPos(0x102, 1800, 0, 0, 180)
    SetChrPos(0x103, 600, 0, 0, 180)
    SetChrPos(0x104, 1800, 0, -1800, 180)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x3)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x3)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 45)
    SetChrPos(0x13, -1500, 0, -3700, 45)
    SetChrPos(0x14, -1500, 0, -6700, 45)
    SetChrPos(0x15, -2600, 0, -5600, 45)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x3)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 315)
    SetChrPos(0x17, 3600, 0, -3700, 315)
    SetChrPos(0x18, 3600, 0, -6700, 315)
    SetChrPos(0x19, 4600, 0, -5400, 315)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    OP_68(1100, 1000, -3200, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    def lambda_8A6A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8A6A)
    WaitChrThread(0x13, 2)

    ChrTalk(
        0x13,
        "#0400061V#6PD-Damn... These guys ain't no amateurs.\x02",
    )

    CloseMessageWindow()

    def lambda_8AC0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8AC0)
    WaitChrThread(0x16, 2)

    ChrTalk(
        0x16,
        (
            "#0400062VTh-Those two chicks... I thought\x01",
            "they were just their groupies!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B2B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8B2B)
    WaitChrThread(0x12, 2)

    ChrTalk(
        0x12,
        (
            "#0400063V#6PWhat's with her staff?\x01",
            "That thing nearly fried me!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B8C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_8B8C)
    WaitChrThread(0x17, 2)

    ChrTalk(
        0x17,
        (
            "#0400064V#2PWhat the hell?! Stop screwin' with us!\x01",
            "You guys are just bracers, aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400065V#5P#0006FI told you already. We're police officers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400066V#1P#0106F*sigh* There's no convincing them,\x01",
            "is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400067VFine. Have it your way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400068VNo point in goin' easy on 'em. There's no\x01",
            "way yer beatin' us at full force!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8D0F():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8D0F)
    SetChrSubChip(0x16, 0x2)
    Sound(808, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x17, 3, 0, 27)
    SetChrSubChip(0x16, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    OP_64(0x18)
    OP_64(0x19)
    OP_0D()
    WaitChrThread(0x17, 3)

    ChrTalk(
        0x12,
        "#0400069V#6PLet's do this, men!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#0400070V#6PWe must show them the true power of the\x01",
            "Testaments, even if they are bracers!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DDE():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8DDE)
    SetChrSubChip(0x12, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x13, 3, 0, 28)
    SetChrSubChip(0x12, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x0)
    OP_64(0x14)
    OP_64(0x15)
    OP_0D()
    WaitChrThread(0x13, 3)

    ChrTalk(
        0x101,
        "#0400071V#5P#0013FUgh...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrPos(0x1B, 15500, -1000, -10500, 315)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    StopBGM(0xBB8)
    Sound(1804, 255, 100, 0)

    NpcTalk(
        0x1B,
        "Rough Voice",
        (
            "#0400072V#1PWhat in the absolute hell do\x01",
            "you guys think you're doin'?\x02",
        )
    )

    CloseMessageWindow()
    Sound(1427, 255, 100, 0)

    NpcTalk(
        0x1A,
        "Cool Voice",
        "#0400073V#5PYou can fall back now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    Fade(500)
    OP_68(8300, 900, -12000, 0)
    MoveCamera(173, 27, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1B, 0x8)
    OP_90(0x1B, 12500, -1000, -16500, 315)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -9100, 0, -11800, 60)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 700, 0, -2300, 180)
    SetChrPos(0x104, 1700, 0, -2300, 180)
    SetChrPos(0x102, 2000, 0, -700, 180)
    SetChrPos(0x103, 400, 0, -700, 180)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x12, -1600, 0, -4700, 45)
    SetChrPos(0x13, -2400, 0, -3100, 45)
    SetChrPos(0x14, -3700, 0, -4300, 45)
    SetChrPos(0x15, -2700, 0, -5500, 45)
    SetChrPos(0x16, 4000, 0, -4700, 315)
    SetChrPos(0x17, 4800, 0, -3100, 315)
    SetChrPos(0x18, 6100, 0, -4300, 315)
    SetChrPos(0x19, 5100, 0, -5500, 315)

    def lambda_91C5():

        label("loc_91C5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_91C5")

    QueueWorkItem2(0x16, 2, lambda_91C5)

    def lambda_91D7():

        label("loc_91D7")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_91D7")

    QueueWorkItem2(0x17, 2, lambda_91D7)

    def lambda_91E9():

        label("loc_91E9")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_91E9")

    QueueWorkItem2(0x18, 2, lambda_91E9)

    def lambda_91FB():

        label("loc_91FB")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_91FB")

    QueueWorkItem2(0x19, 2, lambda_91FB)

    def lambda_920D():

        label("loc_920D")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_920D")

    QueueWorkItem2(0x12, 2, lambda_920D)

    def lambda_921F():

        label("loc_921F")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_921F")

    QueueWorkItem2(0x13, 2, lambda_921F)

    def lambda_9231():

        label("loc_9231")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9231")

    QueueWorkItem2(0x14, 2, lambda_9231)

    def lambda_9243():

        label("loc_9243")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_9243")

    QueueWorkItem2(0x15, 2, lambda_9243)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetMapObjFrame(0xFF, "light", 0x1, 0x1)
    MoveCamera(163, 27, 0, 3000)
    SetCameraDistance(16500, 3000)

    def lambda_929E():
        OP_95(0xFE, 8300, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_929E)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x40)
    OP_6F(0x10)

    ChrTalk(
        0x16,
        "#0400074V#1PW-Wald...?!\x02",
    )

    CloseMessageWindow()

    def lambda_92E2():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_92E2)
    Sleep(2000)
    Fade(500)
    OP_68(-5700, 900, -9300, 0)
    MoveCamera(210, 30, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1B, 0x1)
    MoveCamera(200, 30, 0, 1500)
    SetCameraDistance(15000, 1500)

    def lambda_934A():
        OP_95(0xFE, -5700, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_934A)

    def lambda_9364():
        OP_95(0xFE, -6500, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_9364)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x40)
    OP_6F(0x10)

    ChrTalk(
        0x12,
        "#0400075V#2PWazy... You came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400076V#0005F(Oh, these guys must be...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400077V#0301F(Looks like our head honchos have\x01",
            "entered the battlefield.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_942D():
        OP_95(0xFE, -500, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_942D)
    Sleep(50)

    def lambda_944A():
        OP_95(0xFE, -1100, 0, -6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_944A)
    Sleep(1000)

    def lambda_9467():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_9467)
    Sleep(1000)
    Fade(500)
    OP_68(1200, 800, -4800, 0)
    MoveCamera(180, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1C, 2)
    OP_6F(0x10)

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400078V#5P#1604FHaha. You guys been havin' fun\x01",
            "while I was passed out?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400079V#11P#1602FSo... Anyone care to explain what the\x01",
            "hell's goin' on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400080V#3PUhh... How do we put this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400081V#3PWe were tryin' to teach them blue bastards\x01",
            "a lesson. Then these four chumps came\x01",
            "outta nowhere and interrupted our fight.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_967D():
        OP_9B(0x1, 0xFE, 0x0, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_967D)
    WaitChrThread(0x1B, 1)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x31)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_96B8():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_96B8)

    def lambda_96D1():
        OP_96(0xFE, 0xFA0, 0x1C2, 0xFFFFEDA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_96D1)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x20)

    ChrTalk(
        0x16,
        "#0400082V#3P*gulp*...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400083V#11P#1601FYou moron. Didn't I tell you to use that\x01",
            "damn head of yours before you start shit?\x02\x03",
            "#0400084VAre you dumbasses tryin' to piss all over\x01",
            "my reputation by takin' up fights in public?\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400085V#3PN-No, sir! That wasn't our intention!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0400086V#3PWe'd never do anything to piss all\x01",
            "over your reputation, Wald!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        "#0400087V#11P#1600FEnough.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)

    def lambda_98C1():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFEA84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_98C1)

    def lambda_98DB():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_98DB)

    def lambda_98F4():
        OP_9D(0xFE, 0xFA0, 0x0, 0xFFFFEDA4, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_98F4)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x16,
        "#0400088V#3P*cough* *cough*...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)

    def lambda_995F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_995F)
    Sleep(100)

    def lambda_996F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_996F)
    WaitChrThread(0x1C, 2)

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400089V#5P#0403FAnd what do you all have to say\x01",
            "for yourselves?\x02\x03",
            "#0400090V#0400FDo you intend to disobey my orders?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400091V#4PHear us out, Wazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#0400092V#4PTh-They started taunting us,\x01",
            "that's why we--\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Bald Man",
        "#0400093V#5PDo not make excuses.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Bald Man",
        (
            "#0400094V#5PWazy's will is absolute. Spare us\x01",
            "the unnecessary explanation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#0400095V#4PYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#0400096V#4PW-We'll reflect upon our actions.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Cool Boy",
        "#0400097V#5P#0404FIt's fine. As long as you guys understand.\x02",
    )

    CloseMessageWindow()

    def lambda_9B87():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_9B87)
    Sleep(160)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    OP_0D()
    TurnDirection(0x1B, 0x1A, 500)

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400098V#5P#1602FHaha... You guys haven't changed a bit.\x01",
            "You freakin' disgust me, dude.\x02\x03",
            "#0400099VMakin' your men dress up in those\x01",
            "creepy-ass threads... You think you're\x01",
            "a cult leader or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9C95():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_9C95)
    Sleep(100)

    def lambda_9CA5():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_9CA5)
    WaitChrThread(0x1C, 2)

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400100V#11P#0402FHeh. I didn't force anyone to wear these\x01",
            "garments.\x02\x03",
            "#0400101VYou're not much better than I am. Look at you,\x01",
            "taking your anger out on your subordinates.\x01",
            "Is that any way for a leader to act?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        "#0400141V#5P#1602FHahaha...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Cool Boy",
        "#0400142V#11P#0404FHeh heh heh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400104V#12P#0001F(What's with these two?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400105V#0101F#6P#N(I can't gauge their relationship...)\x02",
    )

    CloseMessageWindow()
    OP_5A()

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400106V#2P#0404FAnyway, why don't we set aside our\x01",
            "differences for now?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EBE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_9EBE)
    Sleep(50)

    def lambda_9ECE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_9ECE)
    Sleep(50)

    def lambda_9EDE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_9EDE)
    WaitChrThread(0x1C, 2)
    Sleep(300)

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400107V#11P#0402FAre you guys actually police officers?\x02\x03",
            "#0400108VHeh. You definitely don't look the part,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400109V#5P#1604FHah. They ain't half bad at fightin', though.\x02\x03",
            "#0400110V#1602F'Specially the redhead. His body is built like\x01",
            "an ox.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400111V#6P#0306FCute compliment. Wouldn't say I'm as ripped\x01",
            "as you, though.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        (
            "#0400112V#5P#1602FAs for the two ladies with ya,\x01",
            "there's no way you can convince\x01",
            "me they're police officers.\x02\x03",
            "#0400113VI gotta admit they're good lookin'\x01",
            "gals, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400114V#0103F#6P#NHow flattering...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#0400115V#0211F#12P#N...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#0400116V#12P#0003FIt's true, though. We're the CPD's\x01",
            "new recruits.\x02\x03",
            "#0400117V#0001FWe're the Special Support Section:\x01",
            "a division that was just established.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400118V#11P#0405FOh, you're the ones that appeared in today's\x01",
            "issue of the Crossbell Times, then?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_A316")

    ChrTalk(
        0x101,
        "#0400119V#12P#0011FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400120V#0106F#6P#NLeave it to the Crossbell Times to be on\x01",
            "top of things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A434")

    label("loc_A316")

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
        (
            "#0400121V#12P#0005FIf we're in the most recent issue of the\x01",
            "Crossbell Times, then that means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400122V#6P#0105F#NCould it be? Did they report\x01",
            "on our rescue efforts?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A434")

    TurnDirection(0x1B, 0x1A, 500)
    Sleep(300)

    NpcTalk(
        0x1B,
        "Rough Young Man",
        "#0400123V#5P#1605FHuh? These guys pull off somethin' big?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Cool Boy",
        (
            "#0400124V#11P#0404FI think they're supposed to be\x01",
            "those poser bracers in the news.\x02\x03",
            "#0400125V#0402FOh, I'm sorry. I suppose your so-called\x01",
            "'contributions' helped with the rescue\x01",
            "effort to some extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400126V#12P#0013FUgh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "Cool Boy",
        "#0400127V#11P#0404FHeh. I'll stop teasing you poor guys.\x02",
    )

    CloseMessageWindow()
    Sleep(450)
    Sound(1435, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Cool Boy")

    AnonymousTalk(
        0xFF,
        (
            "#0400128VMy name's Wazy. Wazy Hemisphere.\x02\x03",
            "#0400129VI suppose you could call me the leader\x01",
            "of the Testaments.\x02",
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

    NpcTalk(
        0x1C,
        "Bald Man",
        "#0400130V#11PWhy the uncertainty?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1C, 500)

    ChrTalk(
        0x1A,
        (
            "#0400131V#6P#0402FYou suit the image of a leader far\x01",
            "more than I do.\x02\x03",
            "#0400132V#0409FThat shiny bald head of yours fits\x01",
            "the role perfectly.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Bald Man",
        "#0400133V#11P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1B,
        "Rough Young Man",
        "#0400134V#5P#1603FEnough screwin' around.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x13B, 0x1F4)
    Sleep(300)
    Sound(1805, 255, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Rough Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#0400135VWald. Wald Wales.\x02\x03",
            "#0400136VLeader of the Saber Vipers.\x02",
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
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400137V#12P#0003FSo you're Wazy and Wald, then?\x02\x03",
            "#0400138V#0000FAllow me to formally introduce myself.\x01",
            "I'm Lloyd Bannings of the Crossbell\x01",
            "police's Special Support Section.\x02\x03",
            "#0400139VI imagine that you don't intend on\x01",
            "escalating the conflict any further.\x02\x03",
            "#0400140VIs it fine if I leave the rest to you two?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x1B,
        "#0400102V#5P#1604FHahaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#0400103V#11P#0404FHeh heh heh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    SetCameraDistance(17500, 1000)
    Sound(1809, 255, 100, 0)
    Sound(1431, 255, 100, 1)

    ChrTalk(
        0x1B,
        "#0400143V#1P#1609F#4S#1KHahahahaha!\x02",
    )


    ChrTalk(
        0x1A,
        "#2P#0409F#4S#1KHahahahaha!\x02",
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0400145V#12P#0013FWh-What's so funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0400146V#11P#0404FOh, it's nothing. I was just thinking\x01",
            "about how silly you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#0400147V#5P#1602FYou think we plan on de-escalatin'\x01",
            "the situation?\x02\x03",
            "#0400148VHaha... What kinda dumbass train\x01",
            "of thought is that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400149V#12P#0005FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0400150V#11P#0404FThe only reason we stopped them is because\x01",
            "we haven't finished our preparations.\x02\x03",
            "#0400151V#0402FWe plan on having the ultimate showdown\x01",
            "once we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#0400152V#5P#1602FAnd it ain't gonna be the child's play you saw.\x02\x03",
            "#0400153VWhich one of us is gonna be left standin'?\x01",
            "We ain't stoppin' until one side's totally dead!\x02",
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
        "#0400154V#12P#0007F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400155V#6P#0301FYou hearin' this? You guys really tryin'\x01",
            "to kill each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#0400156V#5P#1604FHaha, don't know why you're actin'\x01",
            "all surprised.\x02\x03",
            "#0400157V#1602FThough it's pretty obvious which one\x01",
            "of us'll get their asses handed to 'em\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0400158V#11P#0400FI couldn't agree more.\x02\x03",
            "#0400159V#0404FAt any rate, this is none of your business.\x02\x03",
            "#0400160V#0402FEspecially not for a bunch of government dogs,\x01",
            "much less total greenhorns like yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400161V#12P#0013FTch...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)
    Sound(1807, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x1B,
        "#0400162V#11P#1602FHaha... Roll out, boys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0400163V#3PY-Yeah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x12, 500)
    Sleep(300)
    Sound(1429, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x1A,
        "#0400164V#5P#0400FLet's get going, too.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1C,
        "Bald Man",
        "#0400165V#5PYes, sir.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 10000)
    BeginChrThread(0x1B, 3, 0, 29)
    BeginChrThread(0x1A, 3, 0, 30)
    OP_6F(0x10)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1A, 3)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    Fade(1000)
    OP_68(1200, 900, -1500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 500, 0, -2200, 180)
    SetChrPos(0x104, 1900, 0, -2200, 180)
    SetChrPos(0x102, 1900, 0, -800, 180)
    SetChrPos(0x103, 500, 0, -800, 180)
    OP_0D()

    ChrTalk(
        0x101,
        "#0400166V#5P#0001F...\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#0400167V#5P#0106FThey're a handful.\x02\x03",
            "#0400168V#0101FI don't think they were joking, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#0400169V#2P#0301FYeah. They keep this up, and it won't be\x01",
            "much longer till this place's a war zone.\x02\x03",
            "#0400170VWon't be seein' anything other than\x01",
            "blood and bones around these parts.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0400171V#1P#0206FWe have technically completed the\x01",
            "mission assigned to us by the chief.\x02\x03",
            "#0400172V#0200FThis problem is beyond the scope\x01",
            "of our mission, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400173V#5P#0003FI disagree.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400174V#6P#0001FOur mission isn't complete--I don't\x01",
            "want to stop now.\x02\x03",
            "#0400175VIf we let those guys have their way,\x01",
            "then how will we ever regain the\x01",
            "trust of the citizens?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B4CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B4CB)

    def lambda_B4D8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B4D8)

    def lambda_B4E5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B4E5)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x103,
        "#0400176V#1P#0203FA convincing argument.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400177V#5P#0103FHe's right.\x02\x03",
            "#0400178V#0101FWe already know their intentions,\x01",
            "so why don't we devise a plan to\x01",
            "stop them in their tracks?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400179V#2P#0306FBit of a tall order, ain't it?\x02\x03",
            "#0400180V#0301FWe can't just get 'em to stop with some\x01",
            "cheesy one-liner. They'll just laugh\x01",
            "their asses off at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400181V#6P#0008FYeah, you're not wrong...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Request support from HQ]\x01",      # 0
            "[Handle it ourselves]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B6F5"),
        (1, "loc_B9E7"),
        (SWITCH_DEFAULT, "loc_BE38"),
    )


    label("loc_B6F5")


    ChrTalk(
        0x101,
        (
            "#0400182V#6P#0006FOur best move is to report to HQ and\x01",
            "notify them to patrol downtown more\x01",
            "frequently.\x02\x03",
            "#0400183V#0001FThere's nothing we can do to stop them\x01",
            "if they break out into a full-blown\x01",
            "conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400184V#5P#0100FHaving officers patrol the area may help\x01",
            "deter them from fighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400185V#2P#0306FEh. You guys sure it'll go down that way?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400186V#1P#0203FPatrols in the Downtown District are at a\x01",
            "historic low, according to the database.\x02\x03",
            "#0400200V#0200FAll for the purpose of reducing the budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400188V#6P#0005FAre you serious?!\x02\x03",
            "#0400189V#0008FDamn it! It's as if they've decided to sweep\x01",
            "the issue under the rug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400190V#5P#0106FIf that's the case, then our suggestion will\x01",
            "only fall on deaf ears.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE38")

    label("loc_B9E7")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0400191V#6P#0008FI doubt we'd receive any support if we\x01",
            "sent in a request to headquarters.\x02\x03",
            "#0400192VOur best bet is to rely on our own strength\x01",
            "and search for a solution together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400193V#5P#0105FShouldn't we at least inform HQ about\x01",
            "what's happening?\x02\x03",
            "#0400194VThey might send more frequent patrols\x01",
            "to help maintain order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400195V#6P#0003FI doubt it.\x02\x03",
            "#0400196VThink about what happened. Those guys\x01",
            "aren't scared of the police at all. They'll\x01",
            "keep stirring up trouble regardless.\x02\x03",
            "#0400197V#0001FI think headquarters is intentionally avoiding\x01",
            "the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400198V#5P#0101FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400199V#1P#0203FIndeed. Downtown patrols are at a historic\x01",
            "low, according to the database.\x02\x03",
            "#0400187V#0200FAll for the purpose of reducing the budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400201V#2P#0301FSounds like you hit the nail on head.\x02\x03",
            "#0400202V#0306FDoesn't that kinda put us in a tough\x01",
            "spot, though?\x02\x03",
            "#0400203V#0300FWhy not just confront each group head\x01",
            "on, beat their asses, and make sure they\x01",
            "don't step out of line?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400204V#6P#0006FI'm going to pretend I didn't hear that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE38")

    label("loc_BE38")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400205V#6P#0005FHold on a second.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0400206V#6P#0008FThere's something I don't get.\x01",
            "Why are they trying to wipe\x01",
            "each other out in the first place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0400207V#5P#0105FI'm...not actually sure, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400208V#2P#0305FAin't it obvious? They're a bunch of heated\x01",
            "hooligans tryin' to take control of some\x01",
            "territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400209V#6P#0003FI don't think that's the case. If it were that\x01",
            "simple, then they wouldn't have to resort to\x01",
            "an all-out war.\x02\x03",
            "#0400210V#0008FIt'd make more sense if they were competing\x01",
            "over a vested interest, but they're just a\x01",
            "simple gang of delinquents.\x02\x03",
            "#0400211V#0013FWhat could have possibly happened for them\x01",
            "to want to completely annihilate one another?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x103,
        "#0400212V#1P#0205FI am impressed by your deduction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400213V#5P#0100FLikewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400214V#2P#0302FHeh. I get it now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0400215V#6P#0011FWhat's wrong? Did I say something strange?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400216V#5P#0104FNot especially. I'm just coming to the realization\x01",
            "that you're truly qualified to be a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400217V#2P#0300FNo kiddin'. You're definitely analyzing this\x01",
            "from angles I never woulda even considered.\x02\x03",
            "#0400218VOne quick glance at the leaders' relationships,\x01",
            "and they look pretty chummy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400219V#1P#0203FThere is a strong possibility that a hidden\x01",
            "motive is driving the conflict.\x02\x03",
            "#0400220V#0201FA motive only known by the delinquents and\x01",
            "serious enough that they would want to\x01",
            "eliminate each other without a second thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400221V#6P#0000FY-Yeah, that was my thought process.\x02\x03",
            "#0400222VWell. There's only one thing left to do, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400223V#2P#0304FYou know it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400224V#5P#0100FShall we pay the Saber Vipers and\x01",
            "Testaments a visit?\x02\x03",
            "#0400225VWhich of the two should we speak\x01",
            "to first?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    SetMapObjFrame(0xFF, "h_kage", 0x1, 0x1)
    OP_68(1200, 2000, -1500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 1200, 0, -1500, 180)
    SetChrPos(0x1, 1200, 0, -1500, 180)
    SetChrPos(0x2, 1200, 0, -1500, 180)
    SetChrPos(0x3, 1200, 0, -1500, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x42, 0)
    OP_29(0x3E, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_26_871A end

    def Function_27_C723(): pass

    label("Function_27_C723")


    def lambda_C728():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_C728)
    SetChrSubChip(0x17, 0x2)
    Sleep(80)
    SetChrSubChip(0x17, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Return()

    # Function_27_C723 end

    def Function_28_C759(): pass

    label("Function_28_C759")


    def lambda_C75E():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C75E)
    SetChrSubChip(0x13, 0x2)
    Sleep(80)
    SetChrSubChip(0x13, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    OP_0D()
    Return()

    # Function_28_C759 end

    def Function_29_C78F(): pass

    label("Function_29_C78F")

    OP_93(0x1B, 0x87, 0x1F4)
    ClearChrFlags(0x1B, 0x4)

    def lambda_C7A0():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_C7A0)
    Sleep(1600)
    BeginChrThread(0x19, 3, 0, 31)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(900)
    BeginChrThread(0x16, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 31)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    Return()

    # Function_29_C78F end

    def Function_30_C7EA(): pass

    label("Function_30_C7EA")

    BeginChrThread(0x1C, 3, 0, 32)
    OP_93(0x1A, 0xF0, 0x1F4)

    def lambda_C7FC():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_C7FC)
    Sleep(2400)
    BeginChrThread(0x15, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 33)
    Sleep(800)
    BeginChrThread(0x12, 3, 0, 33)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 33)
    StopBGM(0x1F40)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    Return()

    # Function_30_C7EA end

    def Function_31_C84F(): pass

    label("Function_31_C84F")

    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)

    def lambda_C85D():
        OP_95(0xFE, 6100, 0, -7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C85D)
    WaitChrThread(0xFE, 1)

    def lambda_C87B():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C87B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_C84F end

    def Function_32_C895(): pass

    label("Function_32_C895")

    OP_93(0x1C, 0x14A, 0x1F4)

    def lambda_C8A1():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE4A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C8A1)
    WaitChrThread(0x1C, 1)
    Sleep(400)
    OP_93(0x1C, 0xF0, 0x1F4)

    def lambda_C8C9():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_C8C9)
    Return()

    # Function_32_C895 end

    def Function_33_C8DF(): pass

    label("Function_33_C8DF")

    EndChrThread(0xFE, 0x2)

    def lambda_C8E8():
        OP_95(0xFE, -3700, 0, -7400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8E8)
    WaitChrThread(0xFE, 1)

    def lambda_C906():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C906)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_C8DF end

    def Function_34_C920(): pass

    label("Function_34_C920")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00150.itc", 0x1E)
    LoadChrToIndex("apl/ch50017.itc", 0x1F)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_END)), "loc_CAC6")

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400371V#11PY-You again?!\x02",
    )

    CloseMessageWindow()

    def lambda_CA3C():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CA3C)
    WaitChrThread(0x8, 1)

    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "#0400372V#11PWe already told ya. Wald's never gonna\x01",
            "talk to a bunch of dogs like you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE7D")

    label("loc_CAC6")


    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400373V#11PY-You're those cops!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400374V#6P#0005FThose clothes...\x02\x03",
            "#0400375V#0001FIs this place supposed to be\x01",
            "the Saber Vipers' home base?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400376V#6P#0203F'Ignis'...\x02\x03",
            "#0400377V#0200FI believe this was once a warehouse\x01",
            "that is now remodeled into a venue.\x02\x03",
            "#0400378VThey do not pay taxes, so I am unaware\x01",
            "of the specifics.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC32():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CC32)
    WaitChrThread(0x8, 1)

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400379V#11PD-Don't just ignore me!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "#0400380V#11PI may be a rookie, but I'm a proud\x01",
            "member of the Vipers all the same!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400381V#6P#0006FOh, sorry about that.\x02\x03",
            "#0400382V#0001FWe were hoping to have a discussion\x01",
            "with your boss...\x02\x03",
            "#0400383VDo you think you could let us in?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400384V#11PYou want to see Wald?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        (
            "#0400385V#11PHah! There's no way a bunch of dogs\x01",
            "could ever dream of meeting him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400386V#6P#0011FBut...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400387V#11PNo means no!\x02",
    )

    CloseMessageWindow()

    label("loc_CE7D")


    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400388V#11PGet the HELL outta here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400389V#6P#0001F(This might end up being a bit of a problem.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400390V#0300F#6P(Gotta admit. For a delinquent,\x01",
            "he's a cute bright-eyed kid.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    ChrTalk(
        0x102,
        "#0400391V#0102F#5PHello. May I have your name, please?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_CFF7():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CFF7)

    def lambda_D004():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D004)

    def lambda_D011():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D011)
    WaitChrThread(0x101, 2)

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400392V#11PM-Me?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Young Man in Red",
        "#0400393V#11PI-I'm Dino.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400394V#0104F#5PDino, is it?\x02\x03",
            "#0400395V#0100FYou're tasked with keeping watch\x01",
            "in case any suspicious individuals\x01",
            "try to enter, right, Dino?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400396V#11PTh-That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400397V#11PWald personally assigned this job to me.\x01",
            "I can't have any of those Testaments\x01",
            "jerks breakin' in here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400398V#11PI-I definitely wasn't forced into\x01",
            "this post by the other members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400399V#0103F#5POf course not. It's a very important job.\x02\x03",
            "#0400400V#0101FBut, we aren't members of the Testaments.\x02\x03",
            "#0400401VThere shouldn't be any problems for you\x01",
            "to let us in, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400402V#11PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400403V#11PI saw you messing with the rest of\x01",
            "our guys earlier! If I let you in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400404V#0109F#5PYes, we may have engaged in combat with\x01",
            "them, but a spar that small is basically a\x01",
            "greeting to your men, right?\x02\x03",
            "#0400405V#0102FBesides, your boss has already long\x01",
            "moved on from the issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400406V#11PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400407V#0106F#5PHmm, if you still aren't willing to\x01",
            "trust us, then...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D471():

        label("loc_D471")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_D471")

    QueueWorkItem2(0x101, 2, lambda_D471)

    def lambda_D483():

        label("loc_D483")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_D483")

    QueueWorkItem2(0x103, 2, lambda_D483)
    OP_68(45330, -1500, -22310, 1000)

    def lambda_D4A6():
        OP_96(0xFE, 0xB02C, 0xFFFFF63C, 0xFFFFA81C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D4A6)
    WaitChrThread(0x102, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0x8,
        "#0400408V#11PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400409V#6P#0005FW-Wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400410V#6P#0205FElie?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(1174, 255, 100, 0)
    Fade(250)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#0400411V#5P#0100FHere, take it. You can hold on to\x01",
            "my pistol while we go inside.\x02\x03",
            "#0400412VThis is incredibly precious to me.\x01",
            "I hope you'll take good care of it\x01",
            "until I return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400413V#11PHnnngh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400414V#11PF-Fine! You can stop already.\x01",
            "You don't have to take it this far!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400415V#11PI'll go and ask Wald if you can enter!\x01",
            "You'd better not sneak in while I'm gone!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_D76A():
        OP_95(0xFE, 48000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D76A)
    Sleep(800)
    Fade(100)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x8, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_D7BE():
        OP_95(0xFE, 50000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D7BE)

    def lambda_D7D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D7D8)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    OP_68(44610, -1500, -22020, 1200)

    def lambda_D817():
        OP_96(0xFE, 0xAAB4, 0xFFFFF63C, 0xFFFFAA74, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D817)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        "#0400416V#0302F#6PDamn, that was a ballsy move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400417V#6P#0206FI was utterly frightened for a moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400418V#12P#0004FThat was impressive, Elie.\x02\x03",
            "#0400419V#0002FI don't think I'd be able to pull off\x01",
            "a negotiation like that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(
        0x102,
        (
            "#0400420V#0104F#5PI'm quite familiar with these situations,\x01",
            "so feel free to rely on me.\x02\x03",
            "#0400421V#0108FI don't think that approach would work\x01",
            "on someone like Wald, though.\x02\x03",
            "#0400422V#0101FYou'd be better off speaking to him in\x01",
            "a similar manner as you did with Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400423V#12P#0000FYeah, I know. Thanks.\x02",
    )

    CloseMessageWindow()
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_DA92():
        OP_95(0xFE, 46200, -2400, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DA92)

    def lambda_DAAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_DAAC)

    def lambda_DABD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DABD)
    Sleep(50)

    def lambda_DACD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DACD)
    Sleep(50)

    def lambda_DADD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DADD)
    Sleep(50)

    def lambda_DAED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DAED)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)

    ChrTalk(
        0x8,
        "#0400424V#11PWald gave the okay for you to enter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400425V#11PI'll let you in, but if I catch you trying to\x01",
            "pull any funny business...you're finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400426V#0109F#6PHeehee, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400427V#6P#0002FIf you'll excuse us, then.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x42, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_C920 end

    def Function_35_DC62(): pass

    label("Function_35_DC62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50010.itc", 0x1F)
    LoadEffect(0x0, "event\\eva02_00.eff")
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 44400, -2500, -23600, 270)
    SetChrPos(0x102, 44400, -2500, -22200, 270)
    SetChrPos(0x103, 45800, -2500, -23600, 270)
    SetChrPos(0x104, 45800, -2500, -22200, 270)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")

    def lambda_DD6D():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD6D)
    Sleep(50)

    def lambda_DD8A():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD8A)
    Sleep(50)

    def lambda_DDA7():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDA7)
    Sleep(50)

    def lambda_DDC4():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DDC4)
    SetCameraDistance(19500, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_DDF4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DDF4)
    WaitChrThread(0x102, 1)

    def lambda_DE05():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DE05)
    WaitChrThread(0x103, 1)

    def lambda_DE16():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DE16)
    WaitChrThread(0x104, 1)

    def lambda_DE27():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DE27)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    ChrTalk(
        0x102,
        (
            "#0400553V#1P#0108FI'm confused about something.\x02\x03",
            "#0400554V#0101FMembers of both groups were assaulted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400555V#2P#0203FIs it possible they were being untruthful?\x01",
            "I did not suspect they were lying, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400556V#6P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DF85():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DF85)

    def lambda_DF92():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DF92)

    def lambda_DF9F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DF9F)
    WaitChrThread(0x103, 2)

    ChrTalk(
        0x102,
        "#0400557V#1P#0105FIs something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400558V#5P#0301FFeelin' the effects of the fight\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400559V#6P#0000FOh, no, that's not it.\x02\x03",
            "#0400560VI'm fine. He was going easy on me.\x02\x03",
            "#0400561V#0003FI was thinking that something doesn't add up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400562V#2P#0205FHow so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400563V#6P#0003FWell...\x02\x03",
            "#0400564V#0008FFive nights ago, members from both groups\x01",
            "were assaulted at the same time, but in\x01",
            "different locations.\x02\x03",
            "#0400565VEven if they had coincidentally attacked each\x01",
            "other simultaneously...\x02\x03",
            "#0400566V#0001FWith this many people involved, how likely\x01",
            "would it be for them to be oblivious of\x01",
            "each other's movements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400567V#1P#0101FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400568V#5P#0303FNo kiddin'.\x02\x03",
            "#0400569V#0301FNeither of 'em are pros at covert operations,\x01",
            "so chances of that are slim as hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400570V#2P#0201FWhat if one group was ambushed and then\x01",
            "retaliated in kind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400571V#1P#0103FThat wouldn't explain it, either.\x02\x03",
            "#0400572V#0108FThey would have taken precautionary\x01",
            "measures to avoid facing retaliation\x01",
            "from the enemy.\x02\x03",
            "#0400573VNot to mention, both sides had supposedly\x01",
            "been ambushed.\x02\x03",
            "#0400574V#0101FIsn't that right, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400575V#6P#0003FYeah, there's definitely something going on\x01",
            "behind the scenes.\x02\x03",
            "#0400576V#0008FWe're still missing the most critical piece\x01",
            "of this puzzle.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    SetChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)

    NpcTalk(
        0x1D,
        "Woman's Voice",
        "#0400577VHeh heh, looks like you guys could use a hand.\x02",
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
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_E5BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E5BE)

    def lambda_E5CB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E5CB)

    def lambda_E5D8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E5D8)

    def lambda_E5E5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E5E5)
    WaitChrThread(0x101, 2)
    Fade(500)
    OP_68(33700, -1400, -23600, 0)
    MoveCamera(313, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 39300, -2500, -24200, 270)
    SetChrPos(0x102, 39300, -2500, -23000, 270)
    SetChrPos(0x103, 40800, -2500, -24200, 270)
    SetChrPos(0x104, 40800, -2500, -23000, 270)
    ClearChrFlags(0x1D, 0x8)
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    OP_68(38200, -1400, -23600, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_E69D():
        OP_95(0xFE, 36700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E69D)
    WaitChrThread(0x1D, 1)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#0400578V#12P#0005FAren't you...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400579V#0105F...from the Crossbell Times?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("Woman")

    AnonymousTalk(
        0xFF,
        (
            "#0400580VHowdy, everyone. We meet again.\x02\x03",
            "#0400581VCha-ching! Just scored myself a money shot!\x02",
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

    def lambda_E7E2():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA1DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E7E2)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_E853():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA5C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E853)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_E8C4():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_E8C4)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    ChrTalk(
        0x101,
        "#0400582V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400583V#12P#0211FThis is an infringement on our right to privacy.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1D,
        "Woman",
        (
            "#0400584V#2109F#5PI can't help it. Take pictures for as long\x01",
            "as I have, and your camera develops a\x01",
            "mind of its own!\x02\x03",
            "#0400585V#2102FWho knows? Maybe I'll feature you in\x01",
            "my next article.\x02\x03",
            "#0400586VYou guys should take what you can get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400587V#12P#0001FI don't think it works that way.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_EB08")

    ChrTalk(
        0x102,
        (
            "#0400588V#0101FDo you intend to make a mockery\x01",
            "of us again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9E")

    label("loc_EB08")


    ChrTalk(
        0x102,
        (
            "#0400589V#0103FWe heard you had some choice things\x01",
            "to say about us in your article.\x02\x03",
            "#0400590V#0101FDo you intend to make a mockery\x01",
            "of us again?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB9E")

    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()
    Sleep(300)

    NpcTalk(
        0x1D,
        "Woman",
        (
            "#0400591V#2109F#5PHaha, what can I say? You guys seem to\x01",
            "be a hit with the readers.\x02\x03",
            "#0400592V#2100FMore importantly, I see you managed to\x01",
            "drag some juicy information out of those\x01",
            "hoodlums.\x02\x03",
            "#0400593VI've been conducting a little investigation\x01",
            "of my own. So, how about it? Care to share\x01",
            "the goods with your friend here?\x02\x03",
            "#0400594VI'll take you out for a nice meal in return\x01",
            "as thanks for all the lovely reference\x01",
            "material you've been giving me. My treat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400595V#12P#0003FKh...\x02\x03",
            "#0400596V#0001FWhat makes you think we'd be willing\x01",
            "to share classified information with a\x01",
            "civilian?\x02\x03",
            "#0400597VLet alone a member of the media.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1D,
        "Woman",
        (
            "#0400598V#2106F#5POh, phooey. Don't sweat the details.\x02\x03",
            "#0400599VAnd here I was, thinking that I could treat\x01",
            "everyone to some great Eastern cuisine.\x02\x03",
            "#0400600V#2102FAnd offer you the 'critical piece of the puzzle'\x01",
            "for dessert.\x02",
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
        "#0400601V#12P#0005F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400602V#0303FSo that's what you were playin' at.\x01",
            "Trying to reel us in with the ol' give\x01",
            "and take.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1D,
        "Woman",
        (
            "#0400603V#2104F#5PBingo. ♪\x02\x03",
            "#0400604V#2100FI'll be at Long Lao Tavern & Inn near the\x01",
            "East Street exit. Don't be shy, now!\x02\x03",
            "#0400605VI'll head there first and drink all by my\x01",
            "lonesome until you arrive.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_F0F4():
        OP_95(0xFE, 35700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_F0F4)
    WaitChrThread(0x1D, 1)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1D, 0x5A, 0x1F4)

    NpcTalk(
        0x1D,
        "Woman",
        (
            "#0400606V#5P#2105FCome to think of it. I haven't introduced myself\x01",
            "yet, have I?\x02\x03",
            "#0400607V#2100FI'm Grace Lynn, a reporter for the Crossbell Times.\x02\x03",
            "#0400608V#2109FThink of me as the older sister you never had!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_F213():
        OP_95(0xFE, 25700, -2500, -23600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_F213)
    Sleep(3000)
    Fade(1000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 39400, -2500, -24600, 270)
    SetChrPos(0x102, 39400, -2500, -23200, 270)
    SetChrPos(0x103, 40800, -2500, -24600, 270)
    SetChrPos(0x104, 40800, -2500, -23200, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitChrThread(0x1D, 1)
    ClearChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)

    ChrTalk(
        0x101,
        (
            "#0400609V#11P#0001FGrace Lynn. A reporter from the\x01",
            "Crossbell Times...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xE1, 0x190)

    ChrTalk(
        0x104,
        (
            "#0400610V#5P#0300FHer offer sounds shady, but damn, that's\x01",
            "one fine carrot danglin' from her stick.\x02\x03",
            "#0400611VMight be worth seein' what her deal is.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F3FF():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F3FF)
    Sleep(100)

    def lambda_F40F():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F40F)
    Sleep(50)

    def lambda_F41F():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F41F)
    WaitChrThread(0x101, 2)

    ChrTalk(
        0x101,
        (
            "#0400612V#6P#0006FY-Yeah...\x02\x03",
            "#0400613V#0001FI'd like to hear what information she has to offer,\x01",
            "but I'm not interested in her bribery attempt.\x02\x03",
            "#0400614VWe can't rely on headquarters to assist us,\x01",
            "so we should take any help we can get for\x01",
            "the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0400615V#1P#0103FIndeed. I'd imagine her curiosity as a reporter\x01",
            "has led her to research the matter extensively.\x02\x03",
            "#0400616V#0101FWe'd best be careful to not let any sensitive\x01",
            "information slip from our mouths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400617V#2P#0203FI agree.\x02\x03",
            "#0400618V#0211FShe gave off the impression that she\x01",
            "was ready to pounce the moment any\x01",
            "of us slipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400619V#6P#0002F(Ouch. Talk about a harsh assessment.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(40100, -500, -23900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 40100, -2500, -23900, 270)
    SetChrPos(0x1, 40100, -2500, -23900, 270)
    SetChrPos(0x2, 40100, -2500, -23900, 270)
    SetChrPos(0x3, 40100, -2500, -23900, 270)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x42, 4)
    OP_29(0x3E, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_35_DC62 end

    def Function_36_F76E(): pass

    label("Function_36_F76E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-19000, 1000, -10300, 0)
    MoveCamera(60, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -19700, 0, -11000, 45)
    SetChrPos(0x102, -18300, 0, -11000, 315)
    SetChrPos(0x103, -19700, 0, -9600, 135)
    SetChrPos(0x104, -18300, 0, -9600, 225)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(70, 30, 0, 3000)
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
            "#4300074V#5P#0303FDamn it. That bad feeling was right on the money.\x02\x03",
            "#4300075V#0301FHow the hell do so many people up and disappear?\x01",
            "They get kidnapped, or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#4300076V#6P#0206FThere is too little information to come to a conclusion.\x01",
            "All we can do is hypothesize at the moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_FA90")

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
    Jump("loc_FB42")

    label("loc_FA90")


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

    label("loc_FB42")


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
            "#4300081V#5P#0301FWhat's the plan, Lloyd?\x02\x03",
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
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_FFCA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FFCA)
    Sleep(50)

    def lambda_FFDA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FFDA)
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
        "#4300109V#5P#0301FWhat's poindexter's deal?\x02",
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
            "#4300113V#5P#0300FWe'd better go check it out, then. Better than\x01",
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
    SetChrPos(0x0, -19000, 0, -10000, 180)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_36_F76E end

    def Function_37_107CE(): pass

    label("Function_37_107CE")

    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088C")

    ChrTalk(
        0xF,
        "Hold it right there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Sorry, but we're closed at the moment.\x01",
            "Wazy is in the middle of a meeting with\x01",
            "an important guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Please take your leave.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_108CF")

    label("loc_1088C")


    ChrTalk(
        0xF,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Feel free to return at a later time\x01",
            "when we're open.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108CF")

    Sleep(50)
    SetChrPos(0x0, -19660, 0, -10600, 180)
    OP_93(0xF, 0xE1, 0x0)
    OP_4C(0xF, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_107CE end

    def Function_38_108F1(): pass

    label("Function_38_108F1")

    TalkBegin(0xFF)
    OP_4B(0x8, 0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Loud music can be heard blaring from inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        "H-Hey, you there! You're not allowed in here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Get lost!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A1E")
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0001F(I've got a weird feeling about this...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 0)

    label("loc_10A1E")

    OP_93(0x8, 0xE1, 0x1F4)
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_38_108F1 end

    def Function_39_10A2D(): pass

    label("Function_39_10A2D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "               Neinvalli\x01",
            "Temporarily closed for today.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_10A2D end

    def Function_40_10A93(): pass

    label("Function_40_10A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AB6")
    Call(0, 42)
    Jump("loc_10B8A")

    label("loc_10AB6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "           Maison Imelda\x01",
            "～ Currently Unmanaged ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B87")

    ChrTalk(
        0x101,
        (
            "#0001FEverything's covered in dust. Doesn't look\x01",
            "like anybody's lived here for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 7)

    label("loc_10B87")

    TalkEnd(0xFF)

    label("loc_10B8A")

    Return()

    # Function_40_10A93 end

    def Function_41_10B8B(): pass

    label("Function_41_10B8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    OP_71(0x4, 0xF, 0xF, 0x0, 0x0)
    OP_68(43800, -490, -23000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 49400, -2500, -23600, 270)
    SetChrPos(0x102, 49400, -2500, -22200, 270)
    SetChrPos(0x103, 50800, -2500, -23600, 270)
    SetChrPos(0x104, 50800, -2500, -22200, 270)
    SetChrPos(0x1A, 34870, -2490, -22900, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_10C6A():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10C6A)

    def lambda_10C84():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10C84)
    Sleep(50)

    def lambda_10C98():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10C98)

    def lambda_10CB2():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10CB2)
    Sleep(50)

    def lambda_10CC6():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10CC6)

    def lambda_10CE0():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10CE0)
    Sleep(50)

    def lambda_10CF4():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10CF4)

    def lambda_10D0E():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10D0E)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_10D35():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10D35)
    WaitChrThread(0x102, 1)

    def lambda_10D46():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D46)
    WaitChrThread(0x103, 1)

    def lambda_10D57():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10D57)
    WaitChrThread(0x104, 1)

    def lambda_10D68():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10D68)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)

    ChrTalk(
        0x104,
        "#0301FThe hell is going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0108FI'm not fully aware of the situation,\x01",
            "but it seems Dino really is missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003F#6PYeah, and they all seemed distraught, too...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)

    NpcTalk(
        0x1A,
        "Cool Voice",
        "Hey. You guys got a moment to chat?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(42800, -490, -23000, 2000)

    def lambda_10ED9():
        OP_97(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10ED9)

    def lambda_10EF3():
        TurnDirection(0x101, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10EF3)
    Sleep(50)

    def lambda_10F03():
        TurnDirection(0x102, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F03)
    Sleep(50)

    def lambda_10F13():
        TurnDirection(0x103, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10F13)
    Sleep(50)

    def lambda_10F23():
        TurnDirection(0x104, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_10F23)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x1A, 1)

    ChrTalk(
        0x103,
        "#0205F#11PWhat are you doing here, Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0404FI'm curious to see how the Vipers are doing.\x02\x03",
            "#0400FI heard their newest member went missing\x01",
            "this morning.\x02\x03",
            "#0406FWell, I thought something might happen after\x01",
            "that last thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0305F#11PHey... You know somethin' we don't?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#0402FEssentially.\x02\x03",
            "#0409FWhy don't we relocate, first? You're all welcome\x01",
            "to join me at Trinity.\x02\x03",
            "I'd be more than happy to tell you what I know,\x01",
            "as long as you're willing to hear me out.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)
    OP_97(0x1A, 0xFFFFE890, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x8000)

    ChrTalk(
        0x101,
        (
            "#0006F#11PWazy's the only person we can rely on for\x01",
            "more information regarding the Saber\x01",
            "Vipers right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F#11PIndeed... We don't have any clear details,\x01",
            "other than something odd having happened.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_71(0x4, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x10)
    OP_68(43500, -490, -22900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 43500, -2490, -22900, 270)
    SetChrPos(0x1, 43500, -2490, -22900, 270)
    SetChrPos(0x2, 43500, -2490, -22900, 270)
    SetChrPos(0x3, 43500, -2490, -22900, 270)
    SetScenarioFlags(0xD0, 5)
    OP_29(0x4C, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_41_10B8B end

    def Function_42_112BA(): pass

    label("Function_42_112BA")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, 3600, -20130, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19680, 0)
    SetChrPos(0x101, 34840, 2450, -21150, 0)
    SetChrPos(0x102, 35840, 2450, -21150, 315)
    SetChrPos(0x103, 33840, 2450, -21150, 45)
    SetChrPos(0x104, 32840, 2450, -21150, 45)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "           Maison Imelda\x01",
            "～ Currently Unmanaged ～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#11P#0000FThis looks like the apartment\x01",
            "Imelda was talking about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#0100FIt certainly looks unmanaged,\x01",
            "and it's covered in dust, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#0200FShall we enter the premises?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0000FYeah, hold on a sec. I'll unlock the door.\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(200)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5P#0003FOkay, it's unlocked.\x02\x03",
            "#0001FStay on guard, everyone. There may be\x01",
            "monsters roaming around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300FAll right! Let's kick some ass and take\x01",
            "some names!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 34840, 2450, -20500, 0)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    SetScenarioFlags(0x6E, 6)
    EventEnd(0x5)
    Return()

    # Function_42_112BA end

    def Function_43_11584(): pass

    label("Function_43_11584")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    Call(0, 44)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 45)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    LoadChrToIndex("chr/ch30951.itc", 0x32)
    LoadChrToIndex("chr/ch31851.itc", 0x33)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 46)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117C1")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x4)
    OP_2C(0x12, 0x5)
    Call(0, 49)
    Jump("loc_1186A")

    label("loc_117C1")

    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch00153.itc", 0x27)
    LoadChrToIndex("chr/ch00253.itc", 0x28)
    LoadChrToIndex("chr/ch00353.itc", 0x29)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x3)
    Call(0, 50)

    label("loc_1186A")

    Call(0, 51)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Testaments Training]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118ED")
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    Jump("loc_1190B")

    label("loc_118ED")

    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)

    label("loc_1190B")

    SetChrPos(0x0, 130, 0, -5310, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x21, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119AA")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)

    label("loc_119AA")

    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x1, 0x5)
    SetScenarioFlags(0x0, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_11584 end

    def Function_44_119BE(): pass

    label("Function_44_119BE")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetCameraDistance(20640, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x1C,
        "#5PThe objective is a four-on-four battle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PThe Testaments will fight the Special Support\x01",
            "Section with all of their might!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 40, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#5SJa!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    ChrTalk(
        0x1F,
        (
            "Let's see you cops spill the beans on\x01",
            "your self-defense techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Yeah! And then we're going to go all out\x01",
            "and pummel you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "If you don't take this seriously, you're going\x01",
            "to get beaten to a pulp. Get ready!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHaha. You guys got spunk, that's\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FWe'll put our skills to the test to see how\x01",
            "well we can control the tide of battle.\x02\x03",
            "#0001FWe'd better not hold back, or it could\x01",
            "hardly be called training.\x02\x03",
            "Let's give them everything we've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0101FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0201FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#5P#4SAll right, then. Let us begin the battle!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x3E8)
    Battle("BattleInfo_188", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_44_119BE end

    def Function_45_11E23(): pass

    label("Function_45_11E23")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrPos(0x21, 10500, -230, -14120, 314)
    SetChrPos(0xD, 11110, -680, -15910, 314)
    SetChrPos(0xE, 12100, -550, -14490, 314)
    SetChrPos(0x11, 13530, -1180, -16690, 314)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x3)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0003FPhew... I think this is enough.\x02\x03",
            "#0000FIs everyone okay?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_95(0x101, -880, 0, -4000, 1000, 0x0)
    Sleep(300)

    ChrTalk(
        0x1F,
        "#5PY-You got us good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PDamn, you guys are as tough as nails.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x20,
        (
            "#5PHow come we couldn't take you down with\x01",
            "a relentless assault like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FIt's all thanks to the techniques we learn\x01",
            "to suppress a target.\x02\x03",
            "It requires extensive training, and can even\x01",
            "prove effective on small groups.\x02\x03",
            "#0003FA detective has to not only protect himself,\x01",
            "but also those around him.\x02\x03",
            "We undergo extensive training to stay calm,\x01",
            "no matter the level of stress.\x02\x03",
            "#0000FYou'd all do well to train how to protect\x01",
            "yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)
    OP_64(0x20)
    OP_64(0x1E)
    OP_64(0x1F)
    Sleep(300)

    ChrTalk(
        0xF,
        (
            "#5PHeh. You cops are more than just\x01",
            "talk, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PLet that be a lesson learned for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#5PWe may have been defeated this time, but\x01",
            "I feel like I can take them on next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FHah. All it took was a bit of roughhousin'\x01",
            "to get 'em to cozy up to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWe could have maybe gone a bit easier\x01",
            "on them, though. Oh, well. It'll be a\x01",
            "good learning experience for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0200FI do not suspect there will be any problems\x01",
            "based on their demeanor.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        "#4PBullshit.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_1255C():

        label("loc_1255C")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_1255C")

    QueueWorkItem2(0x0, 1, lambda_1255C)

    def lambda_1256E():

        label("loc_1256E")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_1256E")

    QueueWorkItem2(0x1, 1, lambda_1256E)

    def lambda_12580():

        label("loc_12580")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_12580")

    QueueWorkItem2(0x2, 1, lambda_12580)

    def lambda_12592():

        label("loc_12592")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_12592")

    QueueWorkItem2(0x3, 1, lambda_12592)

    def lambda_125A4():

        label("loc_125A4")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_125A4")

    QueueWorkItem2(0xF, 1, lambda_125A4)

    def lambda_125B6():

        label("loc_125B6")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_125B6")

    QueueWorkItem2(0x1F, 1, lambda_125B6)

    def lambda_125C8():

        label("loc_125C8")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_125C8")

    QueueWorkItem2(0x1E, 1, lambda_125C8)

    def lambda_125DA():

        label("loc_125DA")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_125DA")

    QueueWorkItem2(0x20, 1, lambda_125DA)

    def lambda_125EC():

        label("loc_125EC")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_125EC")

    QueueWorkItem2(0x1C, 1, lambda_125EC)
    Sleep(800)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(8710, 2000, -11680, 0)
    MoveCamera(136, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_0D()

    ChrTalk(
        0x101,
        "#11P#0005F#NOh, the Saber Vipers are here?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#11P#0105F#NWhy did they come here?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x21, 0, 0, 52)
    BeginChrThread(0xD, 0, 0, 53)
    BeginChrThread(0xE, 0, 0, 54)
    BeginChrThread(0x11, 0, 0, 55)
    OP_68(3520, 2000, -6230, 4000)
    MoveCamera(152, 19, 0, 4000)

    ChrTalk(
        0xE,
        "#5PHahaha. What are you guys up to?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PWhat kinda cops break out into a fight in\x01",
            "the middle of the Downtown District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PHahaha! Those blue bastards look like\x01",
            "they got their asses handed to 'em!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xF,
        "#12PWh-What the hell did you just say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#6PY-You're the last people I want to hear\x01",
            "that from!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        (
            "#6PYou want a piece of us? We'll take you on.\x01",
            "Right here, right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#11PChill out, guys. There's somethin' I wanna\x01",
            "get straight with first.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x21, 0)
    OP_68(1780, 700, -7220, 3500)
    MoveCamera(172, 22, 0, 3500)
    OP_95(0x21, 4910, -10, -7940, 2000, 0x0)
    OP_95(0x21, 2029, -10, -7760, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)
    OP_93(0xF, 0xE1, 0x1F4)

    ChrTalk(
        0x21,
        (
            "#5PThe hell is the meaning of all this? You\x01",
            "called us out here for a fight, didn't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5PYou wanted to take us on in a four-on-four\x01",
            "battle without our leaders participatin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5PYou've been actin' all pretentious, and now you're\x01",
            "foolin' around with the cops?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PYou have arrived at just the right time.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x12C)
    Sleep(400)

    ChrTalk(
        0x1C,
        (
            "#11PLet us begin the duel between the SSS\x01",
            "and the Saber Vipers!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_12C4F():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12C4F)

    def lambda_12C5C():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12C5C)

    def lambda_12C69():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12C69)

    def lambda_12C76():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12C76)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_12D13():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_12D13)

    def lambda_12D28():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_12D28)

    def lambda_12D3D():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12D3D)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x21)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0x11)
    Sleep(100)

    ChrTalk(
        0xD,
        "#5PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0011FWait, WHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#5PWh-What the hell do you mean by that?!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x5A, 0x190)
    Sleep(400)

    ChrTalk(
        0x1C,
        (
            "#11PUse this opportunity to learn some\x01",
            "much-needed self-defense techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PYou will need the training to protect yourselves\x01",
            "against the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PWhat better way to learn is there than to fight?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetMessageWindowPos(130, 115, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#40W...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    ChrTalk(
        0x11,
        (
            "#6PSo, what you're sayin' is...the cops are\x01",
            "out here to train us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHaha, get a load of this guy! He sounds\x01",
            "insane!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHow are THEY gonna train us?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xD, 500)
    TurnDirection(0x101, 0x21, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#12PHe must be trippin'. There's nothing\x01",
            "a bunch of useless cops can teach us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#12PTraining from cops? Nice joke!\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    ChrTalk(
        0x21,
        (
            "#4S#12PLet's show 'em that the Vipers can wipe\x01",
            "the floor with some no-good cops!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(5)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0xD,
        "#5PLet's kick their asses!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI'm gettin' excited... I'm gonna beat\x01",
            "'em to a pulp!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x101, 400)
    BeginChrThread(0x21, 2, 0, 56)
    Sleep(10)
    BeginChrThread(0xD, 2, 0, 56)
    Sleep(8)
    BeginChrThread(0xE, 2, 0, 56)
    Sleep(12)
    BeginChrThread(0x11, 2, 0, 56)
    Fade(250)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(750, 700, -5890, 3000)
    OP_93(0x1C, 0x0, 0x1F4)

    def lambda_1318E():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1318E)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#12P#0011FHold on, this isn't what we had planned...\x02\x03",
            "#0006FActually, forget it. They're not going\x01",
            "to listen to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FYou sure fighting 'em back-to-back is\x01",
            "a good idea? You got a plan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0006FThere's not much we can do, other than fight.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0001FElie, Tio. Are you going to be fine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FYes, I'll manage.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0201FSeconded. We will go all out if\x01",
            "we must.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FLet's give them everything we've got!\x01",
            "We can't lose here. Our reputation\x01",
            "is at stake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PTake your places, Special Support Section\x01",
            "and the Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11P#4SLet the battle commence!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x21, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x11, 0x2)
    StopBGM(0x3E8)
    Battle("BattleInfo_1CC", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_45_11E23 end

    def Function_46_134B5(): pass

    label("Function_46_134B5")

    OP_68(-360, 2000, -2190, 0)
    MoveCamera(154, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0x21, 3150, 0, -4000, 270)
    SetChrPos(0xD, 4080, 0, -4770, 270)
    SetChrPos(0xE, 4550, 0, -3310, 270)
    SetChrPos(0x11, 5260, 0, -4350, 270)
    SetChrPos(0xF, 4610, 0, -8510, 315)
    SetChrPos(0x1F, 5940, 0, -10170, 315)
    SetChrPos(0x20, 5790, 0, -8490, 315)
    SetChrPos(0x1E, 4910, 0, -10200, 315)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    OP_29(0x12, 0x1, 0x2)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0006FPhew... Made it by the skin of our teeth.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "#5PGoddamn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#5PDamn cops...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x21,
        (
            "#5PYou kiddin' me? How the hell'd\x01",
            "we lose to 'em?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x21,
        "#5P#4SWe're no better than those blue bastards!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PHaha! I don't believe this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PDoesn't this mean we're just as weak\x01",
            "as those hooded freaks?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#0106FAre you really concerned about that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FThey really are sworn rivals.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2040, 2000, -6710, 0)
    MoveCamera(98, 32, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    OP_0D()

    ChrTalk(
        0xF,
        "#11PL-Let me state one thing.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "#11PThe Testaments will never falter to\x01",
            "the likes of those Saber Viper scum!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#11PYou imbeciles lack the mental capacity\x01",
            "to outwit us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11PY-You said it! They can't hope to compete\x01",
            "with us!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_139C1():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_139C1)
    Sleep(8)

    def lambda_139D1():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_139D1)
    Sleep(2)

    def lambda_139E1():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_139E1)
    Sleep(5)

    def lambda_139F1():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_139F1)
    Sleep(200)

    ChrTalk(
        0x11,
        "#6PThe hell was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6PYou're askin' for an ass kickin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005F#NEveryone, calm down!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#12P#0206F#NYou are all far too quick to anger.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x1C,
        "#12PEveryone still appears to be full of energy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#12PLet us engage in combat one final time.\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_13BE6():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13BE6)

    def lambda_13BF3():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13BF3)

    def lambda_13C00():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13C00)

    def lambda_13C0D():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13C0D)

    def lambda_13C1A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_13C1A)

    def lambda_13C27():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_13C27)

    def lambda_13C34():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_13C34)

    def lambda_13C41():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_13C41)

    def lambda_13C4E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13C4E)

    def lambda_13C5B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13C5B)

    def lambda_13C68():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13C68)

    def lambda_13C75():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13C75)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#0011F#NHuh?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x11,
        "#5PAnother battle?\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(200)

    ChrTalk(
        0x1C,
        "#12PThe rules are simple.\x02",
    )

    CloseMessageWindow()
    OP_68(660, 2000, -3670, 3000)
    MoveCamera(173, 31, 0, 3000)
    OP_6E(340, 3000)
    SetCameraDistance(33840, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x1C,
        (
            "#11PWhoever is able to bring the police officers to\x01",
            "their knees first will be deemed victorious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PAre these terms agreeable for everyone?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(10, 0, -1, -1)
    SetChrName("Testaments")

    AnonymousTalk(
        0xFF,
        "#60W...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)
    SetMessageWindowPos(20, 150, -1, -1)
    SetChrName("Saber Vipers")

    AnonymousTalk(
        0xFF,
        "#60W...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#12P#0011FThis is ridiculous! Why do you keep dragging\x01",
            "us further into this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x13B, 0x190)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#5PDo you think it to be that simple?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PYou will take it more seriously if it feels\x01",
            "like your life is on the line, correct?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13F02():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_13F02)

    def lambda_13F0F():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13F0F)

    def lambda_13F1C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13F1C)

    def lambda_13F29():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_13F29)
    Sleep(200)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x21,
        "#6P#5SLet's get 'em!\x02",
    )

    CloseMessageWindow()

    def lambda_13F64():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13F64)

    def lambda_13F71():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13F71)

    def lambda_13F7E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_13F7E)

    def lambda_13F8B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_13F8B)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x32)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x32)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0xF, 1, 0, 48)
    BeginChrThread(0x1F, 1, 0, 47)
    BeginChrThread(0x1E, 1, 0, 47)
    BeginChrThread(0x20, 1, 0, 47)

    ChrTalk(
        0xF,
        "#5S#5PYou'd better not hold us back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6P#4SHell yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5P#4SI will take them down!\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(640, 2000, -2860, 2000)
    MoveCamera(171, 26, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(34010, 2000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_6F(0x79)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x20, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0003FThis isn't looking good. They're all caught up\x01",
            "in a frenzy. I don't think we can stop them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FGuess there ain't nothin' to do but fight!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(300)

    ChrTalk(
        0x1C,
        "#5P#4SAll right#500W, #20Wlet the battle commence!\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_210", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_46_134B5 end

    def Function_47_14208(): pass

    label("Function_47_14208")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_47_14208 end

    def Function_48_14220(): pass

    label("Function_48_14220")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_48_14220 end

    def Function_49_14238(): pass

    label("Function_49_14238")

    OP_68(3950, 2000, -4170, 0)
    MoveCamera(127, 27, -1, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    SetCameraDistance(23720, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-500, 2000, -2270, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0006F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FMade it out alive, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FWe are victorious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0103FThat was intense.\x02",
    )

    CloseMessageWindow()
    OP_A6(0xF, 0xC8, 0x0, 0x3, 0xBB8)

    ChrTalk(
        0xF,
        (
            "#5PI-I can't believe they took all of us\x01",
            "on at the same time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0xC8, 0x0, 0x3, 0xBB8)

    ChrTalk(
        0x21,
        "#5PDamn it... How'd they beat us?\x02",
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(200)
    SetChrSubChip(0x21, 0x1)
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    Sound(804, 0, 100, 0)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#11PDo you understand now? Relying on brute force\x01",
            "alone is not enough to carry you through a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PYou possess a strong offense, but your\x01",
            "defense is far too lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PTo put it in simpler terms,\x01",
            "you are all inexperienced.\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    ChrTalk(
        0x21,
        "#5PWha...?!\x02",
    )

    CloseMessageWindow()
    Fade(200)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    Sleep(500)
    Fade(200)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x13B, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x13B, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    OP_93(0x20, 0x13B, 0x0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#5PWh-Why's this dude lecturin' us\x01",
            "all of a sudden?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PI don't get it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0004FYou guys are plenty strong. I wouldn't mind\x01",
            "teaching you the basics.\x02\x03",
            "#0000FWould you like to learn some of our defense\x01",
            "tactics?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#5PHell nah. I ain't gettin' taught by no\x01",
            "stinkin' pigs.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0x21,
        "#5PWe're leavin, boys.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("Vipers")

    AnonymousTalk(
        0xFF,
        "#4SY-Yeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_148C7():

        label("loc_148C7")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_148C7")

    QueueWorkItem2(0x0, 1, lambda_148C7)

    def lambda_148D9():

        label("loc_148D9")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_148D9")

    QueueWorkItem2(0x1, 1, lambda_148D9)

    def lambda_148EB():

        label("loc_148EB")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_148EB")

    QueueWorkItem2(0x2, 1, lambda_148EB)

    def lambda_148FD():

        label("loc_148FD")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_148FD")

    QueueWorkItem2(0x3, 1, lambda_148FD)

    def lambda_1490F():

        label("loc_1490F")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1490F")

    QueueWorkItem2(0xF, 1, lambda_1490F)

    def lambda_14921():

        label("loc_14921")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_14921")

    QueueWorkItem2(0x1F, 1, lambda_14921)

    def lambda_14933():

        label("loc_14933")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_14933")

    QueueWorkItem2(0x1E, 1, lambda_14933)

    def lambda_14945():

        label("loc_14945")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_14945")

    QueueWorkItem2(0x20, 1, lambda_14945)

    def lambda_14957():

        label("loc_14957")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_14957")

    QueueWorkItem2(0x1C, 1, lambda_14957)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    ChrTalk(
        0xE,
        (
            "#6PThat big dude always sounds like he's\x01",
            "full of it. I don't get him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#4PHah. Like I'd ever listen to him!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_49_14238 end

    def Function_50_149FB(): pass

    label("Function_50_149FB")

    OP_68(810, 1500, -4230, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#0010F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0310F#NDamn it... We lost.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x21,
        "#6P*pant*...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    ChrTalk(
        0xE,
        (
            "#6P#4SHahaha! Serves ya right!\x01",
            "We wiped the floor with you!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_93(0xF, 0x0, 0x190)
    Sleep(400)

    ChrTalk(
        0xF,
        (
            "#11PHold on a minute! It was all thanks to\x01",
            "my highly effective attacks!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14D1D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_14D1D)
    Sleep(10)

    def lambda_14D2D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14D2D)
    Sleep(5)

    def lambda_14D3D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_14D3D)
    Sleep(180)

    def lambda_14D4D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_14D4D)
    Sleep(14)

    def lambda_14D5D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14D5D)
    Sleep(8)

    def lambda_14D6D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_14D6D)
    Sleep(12)

    def lambda_14D7D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_14D7D)

    ChrTalk(
        0x1F,
        (
            "#11PY-Yeah, don't take all the credit\x01",
            "for yourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#11PYou guys aren't nearly as strong as\x01",
            "you think you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6PThe hell did you say to us?!\x01",
            "W-Well... I guess ya did help us out\x01",
            "back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PThere will be no declared victor, then.\x02",
    )

    CloseMessageWindow()

    def lambda_14E8C():

        label("loc_14E8C")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14E8C")

    QueueWorkItem2(0x101, 1, lambda_14E8C)

    def lambda_14E9E():

        label("loc_14E9E")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14E9E")

    QueueWorkItem2(0xF, 1, lambda_14E9E)

    def lambda_14EB0():

        label("loc_14EB0")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14EB0")

    QueueWorkItem2(0x1F, 1, lambda_14EB0)

    def lambda_14EC2():

        label("loc_14EC2")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14EC2")

    QueueWorkItem2(0x1E, 1, lambda_14EC2)

    def lambda_14ED4():

        label("loc_14ED4")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14ED4")

    QueueWorkItem2(0x20, 1, lambda_14ED4)

    def lambda_14EE6():

        label("loc_14EE6")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14EE6")

    QueueWorkItem2(0x21, 1, lambda_14EE6)

    def lambda_14EF8():

        label("loc_14EF8")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14EF8")

    QueueWorkItem2(0xD, 1, lambda_14EF8)

    def lambda_14F0A():

        label("loc_14F0A")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14F0A")

    QueueWorkItem2(0xE, 1, lambda_14F0A)

    def lambda_14F1C():

        label("loc_14F1C")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_14F1C")

    QueueWorkItem2(0x11, 1, lambda_14F1C)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x11, 0x1)

    ChrTalk(
        0x1C,
        (
            "#11PThe Special Support Section did well to\x01",
            "try and survive three consecutive battles\x01",
            "in a row.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        "#11PDo you all think you could have achieved that?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("Saber Vipers")

    AnonymousTalk(
        0xFF,
        "#30W...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    ChrTalk(
        0x1C,
        (
            "#11PDo you understand now? Relying on brute force\x01",
            "alone is not enough to carry you through a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PYou possess a strong offensive, but\x01",
            "your defense is far too lacking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#11PTo put it in simpler terms,\x01",
            "you are all inexperienced.\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    ChrTalk(
        0x21,
        "#5PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWh-Why's this dude lecturin' us\x01",
            "all of a sudden?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#6PI don't get it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0004FYou guys are plenty strong. I wouldn't mind\x01",
            "teaching you the basics.\x02\x03",
            "#12P#0000FWe may have lost, but would you like to\x01",
            "learn some of our defense tactics?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#5PHell nah. I ain't gettin' taught by no\x01",
            "stinkin' pigs.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    ChrTalk(
        0x21,
        "#5PWe're leavin, boys.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("Vipers")

    AnonymousTalk(
        0xFF,
        "#4SY-Yeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_15325():

        label("loc_15325")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_15325")

    QueueWorkItem2(0x0, 1, lambda_15325)

    def lambda_15337():

        label("loc_15337")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_15337")

    QueueWorkItem2(0x1, 1, lambda_15337)

    def lambda_15349():

        label("loc_15349")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_15349")

    QueueWorkItem2(0x2, 1, lambda_15349)

    def lambda_1535B():

        label("loc_1535B")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1535B")

    QueueWorkItem2(0x3, 1, lambda_1535B)

    def lambda_1536D():

        label("loc_1536D")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1536D")

    QueueWorkItem2(0xF, 1, lambda_1536D)

    def lambda_1537F():

        label("loc_1537F")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1537F")

    QueueWorkItem2(0x1F, 1, lambda_1537F)

    def lambda_15391():

        label("loc_15391")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_15391")

    QueueWorkItem2(0x1E, 1, lambda_15391)

    def lambda_153A3():

        label("loc_153A3")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_153A3")

    QueueWorkItem2(0x20, 1, lambda_153A3)

    def lambda_153B5():

        label("loc_153B5")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_153B5")

    QueueWorkItem2(0x1C, 1, lambda_153B5)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    ChrTalk(
        0xE,
        (
            "#6PThat big dude always sounds like he's\x01",
            "full of it. I don't get him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PHah, like I'd ever listen to him!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_50_149FB end

    def Function_51_1545A(): pass

    label("Function_51_1545A")

    Sleep(2500)
    WaitChrThread(0xE, 1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)

    ChrTalk(
        0xF,
        "#11PThey're as dimwitted as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "#12PI-I don't think I'd ever be able to pull off those\x01",
            "techniques at the level they did, even if\x01",
            "I spent my entire life training for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5PYeah, I hear you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1E,
        "#6PWell, it was a good learning experience.\x02",
    )

    CloseMessageWindow()

    def lambda_155A0():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_155A0)

    def lambda_155AD():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_155AD)
    Sleep(20)

    def lambda_155BD():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_155BD)
    Sleep(10)

    def lambda_155CD():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_155CD)
    Sleep(100)

    def lambda_155DD():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_155DD)
    Sleep(20)

    def lambda_155ED():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_155ED)

    def lambda_155FA():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_155FA)
    Sleep(18)

    def lambda_1560A():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1560A)

    def lambda_15617():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_15617)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0003FI'm glad that you all looked like you managed\x01",
            "to enjoy yourselves. I hope it wasn't a waste\x01",
            "of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0103FAgreed. That was exhausting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PWe will be taking our leave.\x01",
            "If you will excuse us, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PIf you would like to take a rest, then\x01",
            "why not come to our bar later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "#5PI hope that exercise served as\x01",
            "adequate training for you, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x87, 0x190)
    Sleep(400)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#12P#0305FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0005F...?\x02",
    )

    CloseMessageWindow()

    def lambda_1581C():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1581C)
    Sleep(10)

    def lambda_1582C():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1582C)

    def lambda_15839():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_15839)
    Sleep(12)

    def lambda_15849():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_15849)
    Sleep(400)

    ChrTalk(
        0x1C,
        "#5P#4SThe battle is over. Let us withdraw!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("Testaments")

    AnonymousTalk(
        0xFF,
        "#5SJa!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_158B6():

        label("loc_158B6")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_158B6")

    QueueWorkItem2(0x0, 1, lambda_158B6)

    def lambda_158C8():

        label("loc_158C8")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_158C8")

    QueueWorkItem2(0x1, 1, lambda_158C8)

    def lambda_158DA():

        label("loc_158DA")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_158DA")

    QueueWorkItem2(0x2, 1, lambda_158DA)

    def lambda_158EC():

        label("loc_158EC")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_158EC")

    QueueWorkItem2(0x3, 1, lambda_158EC)
    OP_68(-4030, 2000, -6480, 5500)
    MoveCamera(228, 29, -1, 5500)
    OP_6E(500, 5500)
    SetCameraDistance(21190, 5500)
    BeginChrThread(0x1C, 1, 0, 61)
    Sleep(1100)
    BeginChrThread(0xF, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1F, 1, 0, 61)
    Sleep(400)
    BeginChrThread(0x20, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1E, 1, 0, 61)
    Sleep(3800)
    StopBGM(0x1388)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Fade(800)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_68(-1140, 2000, -2670, 0)
    MoveCamera(228, 29, -1, 0)
    OP_6E(520, 0)
    SetCameraDistance(16580, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7101", 0)

    ChrTalk(
        0x101,
        (
            "#6P#0005FAbbas planned this all from the start,\x01",
            "didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0106FHe even managed to get the Saber Vipers\x01",
            "to play along.\x02\x03",
            "#0100FIt certainly seems like he orchestrated it\x01",
            "from the very beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0306FHe managed to play us like a fiddle, eh?\x01",
            "Screw that guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0206FIndeed... I am utterly exhausted.\x02\x03",
            "#0200FHowever, the delinquents may straighten\x01",
            "their attitude as a result of his speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYou're right. We managed to accomplish\x01",
            "our goal, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15BB5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15BB5)

    def lambda_15BC2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15BC2)

    def lambda_15BCF():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15BCF)

    def lambda_15BDC():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15BDC)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#6P#0000FI think it's safe to say we've wrapped up\x01",
            "everything we need to do. Let's head out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0100FReady when you are.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_51_1545A end

    def Function_52_15C6C(): pass

    label("Function_52_15C6C")

    OP_95(0x21, 5880, -10, -9390, 2000, 0x0)
    Return()

    # Function_52_15C6C end

    def Function_53_15C81(): pass

    label("Function_53_15C81")

    OP_95(0xD, 6450, 0, -11270, 2000, 0x0)
    Return()

    # Function_53_15C81 end

    def Function_54_15C96(): pass

    label("Function_54_15C96")

    OP_95(0xE, 7550, 0, -9860, 2000, 0x0)
    Return()

    # Function_54_15C96 end

    def Function_55_15CAB(): pass

    label("Function_55_15CAB")

    OP_95(0x11, 7860, 0, -11350, 2000, 0x0)
    Return()

    # Function_55_15CAB end

    def Function_56_15CC0(): pass

    label("Function_56_15CC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15CE5")
    OP_63(0xFE, 0xC8, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_56_15CC0")

    label("loc_15CE5")

    Return()

    # Function_56_15CC0 end

    def Function_57_15CE6(): pass

    label("Function_57_15CE6")

    OP_95(0xFE, 4400, 0, -3520, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_57_15CE6 end

    def Function_58_15D37(): pass

    label("Function_58_15D37")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_58_15D37 end

    def Function_59_15D88(): pass

    label("Function_59_15D88")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_59_15D88 end

    def Function_60_15DD9(): pass

    label("Function_60_15DD9")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_60_15DD9 end

    def Function_61_15E2A(): pass

    label("Function_61_15E2A")

    OP_95(0xFE, 390, 0, -7500, 2000, 0x0)
    OP_95(0xFE, -5110, 0, -8500, 2000, 0x0)
    OP_95(0xFE, -10460, 0, -11450, 2000, 0x0)
    OP_95(0xFE, -15990, 0, -11600, 2000, 0x0)
    Return()

    # Function_61_15E2A end

    SaveToFile()

Try(main)
