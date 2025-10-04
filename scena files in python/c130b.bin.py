from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c130b.bin",                # FileName
        "c130b",                    # MapName
        "c130b",                    # Location
        0x001B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 0, 0, 1],
    )

    BuildStringList((
        "c130b",                  # 0
        "CGF Guardsman",          # 1
        "CGF Guardsman",          # 2
        "CGF Guardsman",          # 3
        "CGF Guardsman",          # 4
        "CGF Guardsman",          # 5
        "CGF Guardsman",          # 6
        "CGF Guardsman",          # 7
        "CGF Guardsman",          # 8
        "CGF Guardsman",          # 9
        "CGF Guardsman",          # 10
        "CGF Guardsman",          # 11
        "CGF Guardsman",          # 12
        "CGF Guardsman",          # 13
        "CGF Guardsman",          # 14
        "CGF Guardsman",          # 15
        "CGF Guardsman",          # 16
        "Chief Guillaume",        # 17
        "Security Guard Wang",    # 18
        "Security Guard Paul",    # 19
        "Cao",                    # 20
        "Lau",                    # 21
        "Grace",                  # 22
        "Reins",                  # 23
        "Lechter",                # 24
        "KeA",                    # 25
        "Arios",                  # 26
        "Chief Sergei",           # 27
        "Detective Dudley",       # 28
        "Zeit",                   # 29
        "Mr. Crois",              # 30
        "Mariabell",              # 31
        "Shizuku",                # 32
        "爆弾",                   # 33
        "爆弾",                   # 34
        "SE制御",                 # 35
        "BC130b",                 # 36
        "BC130b",                 # 37
        "BC130b",                 # 38
        "BC130b",                 # 39
        "BC130b",                 # 40
        "BC130b",                 # 41
        "Central Square",         # 42
        "West Street",            # 43
        "Administrative District",# 44
        "Residential District",   # 45
        "Entertainment District", # 46
        "East Street",            # 47
        "Downtown District",      # 48
        "Harbor District",        # 49
        "IBC",                    # 50
        "Station Street",         # 51
        "Back Alley",             # 52
        "Ursula Road",            # 53
        "East Crossbell Highway", # 54
        "West Crossbell Highway", # 55
        "Mainz Mountain Path",    # 56
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 14, 12, 180)
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
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_114", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 9, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 10, 12, 180)

    # monster count: 0

    # event battle count: 6

    BattleInfo(
        "BattleInfo_144", 0x00CA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31200.dat", "ms31200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_188", 0x00CA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1CC", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_210", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_254", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32600.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_104", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_298", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", "ms31200.dat", "ms31200.dat", "MonsterBattlePostion_124", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "Central Square")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "West Street")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "Administrative District")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "Residential District")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "Harbor District")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "IBC")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "Station Street")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "Back Alley")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "Ursula Road")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_A2C",          # 00, 0
        "Function_1_A81",          # 01, 1
        "Function_2_AA3",          # 02, 2
        "Function_3_C05",          # 03, 3
        "Function_4_114F",         # 04, 4
        "Function_5_11FB",         # 05, 5
        "Function_6_12AF",         # 06, 6
        "Function_7_1370",         # 07, 7
        "Function_8_1431",         # 08, 8
        "Function_9_1B6F",         # 09, 9
        "Function_10_1BD3",        # 0A, 10
        "Function_11_1C6F",        # 0B, 11
        "Function_12_1D0F",        # 0C, 12
        "Function_13_1DCB",        # 0D, 13
        "Function_14_1E56",        # 0E, 14
        "Function_15_1EE1",        # 0F, 15
        "Function_16_229B",        # 10, 16
        "Function_17_29E0",        # 11, 17
        "Function_18_3137",        # 12, 18
        "Function_19_322D",        # 13, 19
        "Function_20_3430",        # 14, 20
        "Function_21_3E08",        # 15, 21
        "Function_22_7E78",        # 16, 22
        "Function_23_7F59",        # 17, 23
        "Function_24_8033",        # 18, 24
        "Function_25_8071",        # 19, 25
        "Function_26_80A6",        # 1A, 26
        "Function_27_88E9",        # 1B, 27
        "Function_28_8983",        # 1C, 28
        "Function_29_8A1D",        # 1D, 29
        "Function_30_8A75",        # 1E, 30
        "Function_31_8ACD",        # 1F, 31
        "Function_32_8B25",        # 20, 32
        "Function_33_8B7D",        # 21, 33
        "Function_34_8BD5",        # 22, 34
        "Function_35_8C2D",        # 23, 35
        "Function_36_8C85",        # 24, 36
        "Function_37_8D03",        # 25, 37
        "Function_38_8D38",        # 26, 38
        "Function_39_8D67",        # 27, 39
        "Function_40_8D9C",        # 28, 40
        "Function_41_8DCB",        # 29, 41
        "Function_42_8DFA",        # 2A, 42
        "Function_43_8E29",        # 2B, 43
        "Function_44_8E58",        # 2C, 44
        "Function_45_8E87",        # 2D, 45
        "Function_46_8ECA",        # 2E, 46
        "Function_47_C1AF",        # 2F, 47
    ))


    def Function_0_A2C(): pass

    label("Function_0_A2C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A49")
    SetScenarioFlags(0x0, 0)
    Event(0, 3)

    label("loc_A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A5D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_A80")

    label("loc_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_A71")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_A80")

    label("loc_A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_A80")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 46)

    label("loc_A80")

    Return()

    # Function_0_A2C end

    def Function_1_A81(): pass

    label("Function_1_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A96")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_A96")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    Return()

    # Function_1_A81 end

    def Function_2_AA3(): pass

    label("Function_2_AA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28600.itc", 0x1E)
    OP_68(0, 2500, -26500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2300, 400, 6000, 180)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2300, 400, 6000, 180)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KSame day, 10PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7513", 0)
    OP_68(0, 7500, -20500, 10000)
    MoveCamera(0, -9, 0, 10000)
    SetCameraDistance(14000, 10000)
    FadeToBright(2000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 0)
    NewScene("c134B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_AA3 end

    def Function_3_C05(): pass

    label("Function_3_C05")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31200.itc", 0x26)
    LoadChrToIndex("chr/ch31250.itc", 0x27)
    LoadChrToIndex("chr/ch31251.itc", 0x28)
    LoadChrToIndex("chr/ch31253.itc", 0x29)
    LoadChrToIndex("chr/ch31252.itc", 0x2A)
    LoadChrToIndex("chr/ch0005C.itc", 0x2B)
    LoadChrToIndex("chr/ch00056.itc", 0x2C)
    LoadChrToIndex("chr/ch00352.itc", 0x2D)
    LoadChrToIndex("chr/ch00359.itc", 0x2E)
    LoadEffect(0x0, "battle\\ms00001.eff")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -22700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -700, 0, 4800, 180)
    SetChrPos(0x102, -1500, 0, 6600, 180)
    SetChrPos(0x103, 1500, 0, 6600, 180)
    SetChrPos(0x104, 700, 0, 4800, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2000, 0, -22900, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -2000, 0, -22900, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_78(0xD, 0x28)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    OP_49()
    SetChrPos(0x28, 900, 0, -22700, 0)
    OP_D3(0x28, 0x0, 0x0, 0x0, 0x0)
    OP_70(0xD, 0x0)
    OP_78(0xE, 0x29)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x4)
    OP_49()
    SetChrPos(0x29, -900, 0, -22700, 0)
    OP_D3(0x29, 0x0, 0x0, 0x0, 0x0)
    OP_70(0xD, 0x0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7513", "ed7000")
    SetCameraDistance(17500, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(963, 0, 100, 0)
    OP_71(0xD, 0x1, 0x19, 0x0, 0x0)
    Sleep(10)
    OP_71(0xE, 0x1, 0x19, 0x0, 0x0)
    OP_79(0xD)
    OP_71(0xD, 0x19, 0x28, 0x0, 0x20)
    OP_79(0xE)
    OP_71(0xE, 0x19, 0x28, 0x0, 0x20)
    Sound(140, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x10)
    Sound(115, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(400)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(200)

    def lambda_EEE():
        OP_96(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFB1E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EEE)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 5)
    Sleep(200)

    def lambda_F14():
        OP_96(0xFE, 0x640, 0x0, 0xFFFFB820, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F14)

    def lambda_F2E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F2E)

    def lambda_F3B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F3B)
    OP_79(0xC)
    PlayBGM("ed7404", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    OP_68(0, 900, -6500, 0)
    MoveCamera(40, 27, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_68(0, 900, -11500, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x11)
    OP_68(0, 800, -15500, 0)
    MoveCamera(25, 11, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x8, 1400, 0, -22900, 0)
    SetChrPos(0x9, -1400, 0, -22900, 0)
    SetChrPos(0x28, 600, 0, -22400, 0)
    SetChrPos(0x29, -600, 0, -22400, 0)
    Sleep(500)
    OP_68(0, 800, -20500, 1500)
    MoveCamera(50, 11, 0, 1500)
    SetCameraDistance(17500, 1500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 300)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1092():
        OP_96(0xFE, 0x514, 0x0, 0xFFFFAE5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1092)

    def lambda_10AC():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFAE5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10AC)
    Sleep(300)
    Battle("BattleInfo_144", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    Call(0, 8)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    OP_2C(0x4E, 0x1)
    Call(0, 16)

    label("loc_1102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1118")
    OP_2C(0x4E, 0x1)
    Call(0, 17)

    label("loc_1118")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112E")
    OP_2C(0x4E, 0x1)
    Call(0, 20)

    label("loc_112E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114B")
    OP_2C(0x4E, 0x3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_114B")

    Call(0, 21)
    Return()

    # Function_3_C05 end

    def Function_4_114F(): pass

    label("Function_4_114F")


    def lambda_1154():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFFC0B8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1154)
    Sleep(3500)
    Sound(1091, 255, 100, 0)
    WaitChrThread(0x101, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x18)
    SetChrChip(0x0, 0x101, 0x1E, 0x12C)
    Sound(854, 0, 100, 0)

    def lambda_119B():
        OP_9D(0xFE, 0xFFFFFB50, 0x0, 0xFFFFAD30, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119B)
    Sleep(450)
    SetChrSubChip(0x101, 0x19)
    Sound(533, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x101, 0x1A)
    BeginChrThread(0x9, 3, 0, 7)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2C)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)
    SetChrChip(0x1, 0x101, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x9, 3)
    Return()

    # Function_4_114F end

    def Function_5_11FB(): pass

    label("Function_5_11FB")


    def lambda_1200():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFC4A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1200)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x1)
    SetChrChip(0x0, 0x104, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_123E():
        OP_9D(0xFE, 0x4B0, 0x0, 0xFFFFB118, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_123E)
    Sleep(110)
    SetChrSubChip(0x104, 0x2)
    Sleep(110)
    SetChrSubChip(0x104, 0x3)
    Sleep(110)
    SetChrSubChip(0x104, 0x4)
    Sleep(110)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x15)
    Sleep(70)
    Sound(1373, 255, 100, 1)
    SetChrSubChip(0x104, 0x1D)
    BeginChrThread(0x8, 3, 0, 6)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    Sleep(300)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    WaitChrThread(0x8, 3)
    Return()

    # Function_5_11FB end

    def Function_6_12AF(): pass

    label("Function_6_12AF")

    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sleep(100)
    Sound(246, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)

    def lambda_1313():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1313)

    def lambda_132C():
        OP_9D(0xFE, 0x6A4, 0x0, 0xFFFF9AD4, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_132C)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Sound(514, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Return()

    # Function_6_12AF end

    def Function_7_1370(): pass

    label("Function_7_1370")

    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x0, 0xFF, 0x9, 0x0, 0, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sleep(100)
    Sound(246, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)

    def lambda_13D4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13D4)

    def lambda_13ED():
        OP_9D(0xFE, 0xFFFFF95C, 0x0, 0xFFFF9AD4, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13ED)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sound(514, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Return()

    # Function_7_1370 end

    def Function_8_1431(): pass

    label("Function_8_1431")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch26400.itc", 0x2D)
    LoadChrToIndex("chr/ch28600.itc", 0x2E)
    LoadChrToIndex("chr/ch00057.itc", 0x2F)
    LoadChrToIndex("chr/ch0035B.itc", 0x30)
    LoadChrToIndex("chr/ch00056.itc", 0x31)
    LoadChrToIndex("chr/ch00356.itc", 0x32)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -26700, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1100, 0, -28000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1100, 0, -28000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x18, 0x2D)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2E)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x2E)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -1300, 0, -18800, 180)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1300, 0, -18700, 180)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 800, 0, -17700, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    OP_78(0xD, 0x28)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    OP_49()
    SetChrPos(0x28, 700, 0, -21700, 0)
    OP_D3(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xD, 0x19, 0x28, 0x0, 0x20)
    OP_78(0xE, 0x29)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x4)
    OP_49()
    SetChrPos(0x29, -700, 0, -21700, 0)
    OP_D3(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xE, 0x19, 0x28, 0x0, 0x20)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    LoadEffect(0x0, "battle\\ms00001.eff")
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_68(0, 1000, -24000, 1500)
    OP_6F(0x1)

    NpcTalk(
        0x19,
        "Security Guards",
        "#5200904V#5P#NWhoa!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x18,
        "#5200906V#5PGood work, everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200907V#5P#0013FKeep it up, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200908V#11P#0301FNext wave is coming in hard!\x01",
            "Brace yourselves!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5200909V#11P#0207FWe should still have some time until\x01",
            "the bombs detonate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200910V#5P#0107FTake them through the gates, hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#5200911V#5PLeave it to us, miss! I'll disarm 'em in\x01",
            "no time flat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#5200912V#2PReady, Paul?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(
        0x1A,
        "#5200913V#1PY-Yeah!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1000, -21700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    BeginChrThread(0x18, 3, 0, 9)
    BeginChrThread(0x19, 3, 0, 10)
    Sleep(4000)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x8, -1200, -2800, -39500, 0)
    SetChrPos(0x9, 1200, -2800, -39500, 0)
    SetChrPos(0x10, 0, -2500, -38000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_68(0, -1800, -38000, 2000)
    OP_6F(0x1)
    ClearMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x4)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)

    ChrTalk(
        0x101,
        "#5200914V#0007FHere they come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200915V#0307FHold 'em back, no matter what!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -27000, 2000)
    MoveCamera(37, 17, 0, 2000)
    SetCameraDistance(15500, 2000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_1AEA():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AEA)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_1B0F():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B0F)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_1B31():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B31)
    OP_6F(0x79)
    Battle("BattleInfo_188", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    Return()

    # Function_8_1431 end

    def Function_9_1B6F(): pass

    label("Function_9_1B6F")


    def lambda_1B74():
        OP_95(0xFE, -1500, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B74)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x5A, 0x1F4)

    def lambda_1B99():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B99)

    def lambda_1BB3():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1BB3)
    Sound(964, 0, 100, 0)
    WaitChrThread(0x18, 1)
    Return()

    # Function_9_1B6F end

    def Function_10_1BD3(): pass

    label("Function_10_1BD3")

    Sleep(100)

    def lambda_1BDB():
        OP_95(0xFE, 1400, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BDB)
    Sleep(300)

    def lambda_1BF8():
        OP_95(0xFE, 700, 0, -20900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BF8)
    WaitChrThread(0x19, 1)
    OP_93(0x19, 0x10E, 0x1F4)
    WaitChrThread(0x1A, 1)

    def lambda_1C21():
        OP_96(0xFE, 0x578, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1C21)

    def lambda_1C3B():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD56C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C3B)

    def lambda_1C55():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1C55)
    WaitChrThread(0x19, 1)
    Return()

    # Function_10_1BD3 end

    def Function_11_1C6F(): pass

    label("Function_11_1C6F")

    Sound(1011, 255, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x1)

    def lambda_1C8C():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C8C)
    WaitChrThread(0x101, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(400)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x2)
    Sound(814, 0, 100, 0)

    def lambda_1CD2():
        OP_9D(0xFE, 0xFFFFFCE0, 0x0, 0xFFFF9C64, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CD2)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Return()

    # Function_11_1C6F end

    def Function_12_1D0F(): pass

    label("Function_12_1D0F")

    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)

    def lambda_1D2D():
        OP_96(0xFE, 0x384, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D2D)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    Sound(1320, 255, 100, 1)
    SetChrSubChip(0x104, 0x3)
    WaitChrThread(0x104, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(300)
    SetChrSubChip(0x104, 0x4)
    Sleep(300)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x2)
    Sound(814, 0, 100, 0)

    def lambda_1D8E():
        OP_9D(0xFE, 0x320, 0x0, 0xFFFF9E58, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D8E)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Return()

    # Function_12_1D0F end

    def Function_13_1DCB(): pass

    label("Function_13_1DCB")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1E1C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E1C)

    def lambda_1E35():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E35)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Return()

    # Function_13_1DCB end

    def Function_14_1E56(): pass

    label("Function_14_1E56")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1EA7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1EA7)

    def lambda_1EC0():
        OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EC0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_14_1E56 end

    def Function_15_1EE1(): pass

    label("Function_15_1EE1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -24200, 180)
    SetChrPos(0x104, 800, 0, -25500, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1800, -3800, -47500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1800, -3800, -47500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 900, -3500, -46000, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, -900, -3500, -46000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5200916V#5P#0000FWell, that went better than--\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#5200917V#0207F#11PSecond wave, incoming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200918V#5P#0010FTch...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    Fade(250)
    OP_68(0, -4000, -39000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(0, 0, -27000, 3000)
    MoveCamera(0, 17, 0, 3000)
    SetCameraDistance(17500, 3000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_21F0():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21F0)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_2212():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2212)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_2237():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2237)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2259():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2259)
    OP_6F(0x79)
    Battle("BattleInfo_1CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Return()

    # Function_15_1EE1 end

    def Function_16_229B(): pass

    label("Function_16_229B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch06300.itc", 0x2D)
    LoadChrToIndex("chr/ch31400.itc", 0x2E)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1100, -3800, -47500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1100, -3800, -47500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 0, -3300, -45500, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 1700, -3500, -46000, 0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -1700, -3500, -46000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10700, -7000, -70400, 0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 11800, -7000, -70400, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5200919V#5P#0013FTch. Even if we fall back into the\x01",
            "IBC, their assault won't let up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200920V#0101F#5PStill, we have to buy them enough time\x01",
            "to shut the gate somehow!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    Fade(1000)
    OP_68(11300, -6000, -70400, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(14500, 10000)

    ChrTalk(
        0x1B,
        (
            "#5200921V#11P#3209FThey seem to be having fun.\x02\x03",
            "#5200922V#3202FJudging by Yin's report, I assumed they would\x01",
            "be slowly beaten back, but look there.\x01",
            "They actually seem to be holding their own.\x02\x03",
            "#5200923VThey ARE full of surprises, aren't they?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(300)

    ChrTalk(
        0x1C,
        (
            "#5200924V#11PMaster Cao... They may be succeeding for the\x01",
            "moment, but endurance can only last for so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        (
            "#5200925V#11P#3204FYour point? If they die here, all it means is\x01",
            "that this was all they could amount to.\x01",
            "Their hope and potential would die with them.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1B,
        "#5200926V#11P#3210FAh, look. The next challengers approach.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    Fade(1000)
    OP_68(0, -3000, -39000, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 500, -28000, 3000)
    MoveCamera(35, 15, 0, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_28F7():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_28F7)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_291C():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_291C)
    SetChrChipByIndex(0x12, 0x2B)
    SetChrSubChip(0x12, 0x0)

    def lambda_293E():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_293E)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_2963():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2963)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2985():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2985)
    OP_0D()
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_6F(0x79)
    Battle("BattleInfo_210", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    Return()

    # Function_16_229B end

    def Function_17_29E0(): pass

    label("Function_17_29E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31352.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch32650.itc", 0x2D)
    LoadChrToIndex("chr/ch32651.itc", 0x2E)
    LoadChrToIndex("chr/ch06000.itc", 0x2F)
    LoadChrToIndex("chr/ch28100.itc", 0x30)
    LoadChrToIndex("chr/ch32600.itc", 0x31)
    LoadChrToIndex("chr/ch32654.itc", 0x32)
    LoadChrToIndex("apl/ch50314.itc", 0x33)
    LoadEffect(0x0, "event\\eva02_00.eff")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 2000, -3800, -44500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -2000, -3800, -44500, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x4)
    OP_90(0x10, 4300, -3000, -43800, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x4)
    OP_90(0x11, -4300, -3000, -43800, 0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 0, -2000, -42000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1D, 0x2F)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x30)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -17700, -4200, -72900, 45)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -17900, -4200, -71800, 45)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        (
            "#5200927V#5P#0208FHad the gate been attacked with this\x01",
            "much force, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200928V#5P#0007FI know...! Just continue to hold the line\x01",
            "and don't let them break through!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    Fade(1000)
    OP_68(-17800, -3300, -72300, 0)
    MoveCamera(20, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(14000, 10000)
    OP_63(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x1E, 0x1D, 500)

    ChrTalk(
        0x1E,
        "#5200929V#5PWh-What the heck is going on, Grace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1D,
        (
            "#5200930V#6P#2101FShut up and keep shooting!\x02\x03",
            "#5200931VOur only way of fighting the good fight is with\x01",
            "the pen and camera, okay? So stay with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)

    ChrTalk(
        0x1E,
        "#5200932V#5PY-Yes, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x2D, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x1E, 0x33)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    BeginChrThread(0x1E, 0, 0, 18)
    Sleep(500)

    ChrTalk(
        0x1D,
        (
            "#5200933V#6P#2103F(Don't worry, Special Support Section. I plan on\x01",
            "spinning this into the best damn article you will\x01",
            "ever read!)\x02\x03",
            "#5200934V#2101F(So don't go dying on me now! If you can't enjoy\x01",
            "the fruits of your labor, what's the point?!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    EndChrThread(0x1E, 0xFF)
    Fade(1000)
    OP_68(0, -500, -35000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(11500, 3000)

    def lambda_301C():
        OP_96(0xFE, 0x0, 0xFFFFF95C, 0xFFFF7748, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_301C)
    OP_0D()
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    WaitChrThread(0x17, 1)
    OP_6F(0x10)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x17, 0x4)
    Fade(250)
    OP_68(0, -1000, -35000, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_68(0, -500, -29000, 2000)
    MoveCamera(0, 15, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x17, 3, 0, 19)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_30CC():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_30CC)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_30EE():
        OP_98(0xFE, 0x1F4, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30EE)
    OP_6F(0x79)
    Sleep(700)
    Battle("BattleInfo_254", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x17, 0xFF)
    Return()

    # Function_17_29E0 end

    def Function_18_3137(): pass

    label("Function_18_3137")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    label("loc_3174")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_322C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31A2")
    Sleep(500)
    Jump("loc_31EA")

    label("loc_31A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31B9")
    Sleep(1500)
    Jump("loc_31EA")

    label("loc_31B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31D0")
    Sleep(2000)
    Jump("loc_31EA")

    label("loc_31D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31E7")
    Sleep(3000)
    Jump("loc_31EA")

    label("loc_31E7")

    Sleep(4000)

    label("loc_31EA")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Jump("loc_3174")

    label("loc_322C")

    Return()

    # Function_18_3137 end

    def Function_19_322D(): pass

    label("Function_19_322D")

    Sleep(400)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    Sound(854, 0, 100, 0)

    def lambda_3248():
        OP_9D(0xFE, 0x10CC, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3248)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x11, 0x2)
    SetChrFlags(0x11, 0x20)

    def lambda_3272():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3272)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_32A3():
        OP_9D(0xFE, 0x10CC, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_32A3)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_32CE():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_32CE)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_32FF():
        OP_9D(0xFE, 0x10CC, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_32FF)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_332A():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_332A)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_335B():
        OP_9D(0xFE, 0x10CC, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_335B)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_3386():
        OP_9D(0xFE, 0xFFFFEF34, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3386)
    WaitChrThread(0x10, 1)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x1)

    def lambda_33B2():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_33B2)
    Sound(854, 0, 100, 0)
    Sound(925, 0, 100, 0)

    def lambda_33CB():
        OP_9D(0xFE, 0x708, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_33CB)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x1)

    def lambda_33F4():
        OP_93(0xFE, 0x2D, 0x2BC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_33F4)

    def lambda_3401():
        OP_9D(0xFE, 0xFFFFF8F8, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3401)
    Sleep(300)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x11, 0x2)
    Sleep(100)
    SetChrSubChip(0x10, 0x3)
    SetChrSubChip(0x11, 0x3)
    Return()

    # Function_19_322D end

    def Function_20_3430(): pass

    label("Function_20_3430")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31350.itc", 0x29)
    LoadChrToIndex("chr/ch31351.itc", 0x2A)
    LoadChrToIndex("chr/ch31353.itc", 0x2B)
    LoadChrToIndex("chr/ch07400.itc", 0x2C)
    LoadChrToIndex("chr/ch00357.itc", 0x2D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1000, -3800, -47700, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1000, -3800, -47700, 0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    OP_90(0xA, 2300, -4500, -48500, 0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    OP_90(0xB, -2300, -4500, -48500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 0, -3300, -45500, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 1700, -3500, -46000, 0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -1700, -3500, -46000, 0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x13, 0, -3800, -46800, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1F, 0x2C)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -16800, -7500, -46500, 45)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "battle\\cr003301.eff")
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_381D")

    ChrTalk(
        0x101,
        "#5200935V#0010F#5PI-Isn't that Warrant Officer Mireille...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200936V#0106F#5PShe was taken over, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200937V#0201F#5PRandy! What are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200941V#0310F#5PWh-What... What the hell is this bullshit?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3904")

    label("loc_381D")


    ChrTalk(
        0x104,
        "#5200938V#0308F#5PN-No... It can't be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200939V#5P#0013FRandy? Do you know that guardsmen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200940V#0303F#5P...Yeah. Former coworker of mine, actually.\x02\x03",
            "#5200941V#0310FDamn it all! What the hell is this bullshit?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3904")

    Sleep(300)
    OP_68(800, 1000, -25000, 2000)
    MoveCamera(0, 30, 0, 2000)
    SetCameraDistance(14500, 2000)
    Sound(1301, 255, 100, 0)
    PlayEffect(0x0, 0xFF, 0x104, 0x0, 0, 600, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x7D0)
    Sleep(2000)
    OP_6F(0x79)
    Sound(1310, 255, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(17500, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    SetChrSubChip(0x104, 0x1)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_6F(0x10)
    Sleep(300)
    CancelBlur(0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    Fade(1000)
    OP_68(-16750, -6500, -46520, 0)
    MoveCamera(20, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(13500, 10000)

    ChrTalk(
        0x1F,
        (
            "#5200943V#5P#3502FBoy, oh, boy. They're having a tough time.\x02\x03",
            "#5200944V#3506FAt this rate, everything really might go\x01",
            "according to Old Man Giliath's plan.\x02\x03",
            "#5200945V#3510FWell, time to see how they'll respond.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1F, 0x87, 0x1F4)

    ChrTalk(
        0x1F,
        (
            "#5200946V#5P#3505FAaaaand, it would look like this next sortie\x01",
            "will be our final act.\x02\x03",
            "#5200947V#3504FBreak a leg, guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Fade(1000)
    OP_68(0, -3000, -39000, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 500, -28000, 3000)
    MoveCamera(35, 15, 0, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x20)

    def lambda_3C9E():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C9E)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x20)

    def lambda_3CC5():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3CC5)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x20)

    def lambda_3CEF():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3CEF)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x20)

    def lambda_3D16():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3D16)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_3D38():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3D38)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_3D5A():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3D5A)
    Sleep(50)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_3D7F():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D7F)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)

    def lambda_3DA1():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3DA1)
    OP_0D()
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    OP_6F(0x79)
    OP_32(0x3, 0xFE, 0x0)
    OP_32(0x3, 0x5, 0xC8)
    Battle("BattleInfo_298", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x13, 0xFF)
    Return()

    # Function_20_3430 end

    def Function_21_3E08(): pass

    label("Function_21_3E08")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x14)
    LoadChrToIndex("chr/ch00053.itc", 0x15)
    LoadChrToIndex("chr/ch00150.itc", 0x16)
    LoadChrToIndex("chr/ch00153.itc", 0x17)
    LoadChrToIndex("chr/ch00250.itc", 0x18)
    LoadChrToIndex("chr/ch00253.itc", 0x19)
    LoadChrToIndex("chr/ch00350.itc", 0x1A)
    LoadChrToIndex("chr/ch00353.itc", 0x1B)
    LoadChrToIndex("chr/ch31250.itc", 0x1C)
    LoadChrToIndex("chr/ch31251.itc", 0x1D)
    LoadChrToIndex("chr/ch31253.itc", 0x1E)
    LoadChrToIndex("chr/ch31252.itc", 0x1F)
    LoadChrToIndex("chr/ch31350.itc", 0x20)
    LoadChrToIndex("chr/ch31351.itc", 0x21)
    LoadChrToIndex("chr/ch31353.itc", 0x22)
    LoadChrToIndex("chr/ch31300.itc", 0x23)
    LoadChrToIndex("chr/ch00056.itc", 0x24)
    LoadChrToIndex("chr/ch00156.itc", 0x25)
    LoadChrToIndex("chr/ch00256.itc", 0x26)
    LoadChrToIndex("chr/ch00356.itc", 0x27)
    LoadChrToIndex("chr/ch02400.itc", 0x28)
    LoadChrToIndex("apl/ch50539.itc", 0x29)
    LoadChrToIndex("apl/ch50509.itc", 0x2A)
    LoadChrToIndex("apl/ch50506.itc", 0x2B)
    LoadChrToIndex("chr/ch00950.itc", 0x2C)
    LoadChrToIndex("chr/ch00951.itc", 0x2D)
    LoadChrToIndex("chr/ch08200.itc", 0x2E)
    LoadChrToIndex("chr/ch00051.itc", 0x2F)
    LoadChrToIndex("chr/ch00151.itc", 0x30)
    LoadChrToIndex("chr/ch00251.itc", 0x31)
    LoadChrToIndex("chr/ch00351.itc", 0x32)
    LoadChrToIndex("chr/ch02750.itc", 0x33)
    LoadChrToIndex("chr/ch02751.itc", 0x34)
    LoadChrToIndex("chr/ch02702.itc", 0x35)
    LoadChrToIndex("chr/ch08201.itc", 0x36)
    LoadChrToIndex("apl/ch50513.itc", 0x37)
    LoadChrToIndex("apl/ch50514.itc", 0x38)
    LoadChrToIndex("apl/ch50515.itc", 0x39)
    LoadChrToIndex("apl/ch50540.itc", 0x3A)
    LoadChrToIndex("apl/ch50545.itc", 0x3B)
    LoadEffect(0x0, "event\\ev500_00.eff")
    LoadEffect(0x1, "event\\eva03_00.eff")
    LoadEffect(0x2, "event\\ev609_00.eff")
    LoadEffect(0x3, "event\\ev609_01.eff")
    LoadEffect(0x4, "event\\eva04_00.eff")
    LoadEffect(0x5, "event\\eva03_00.eff")
    LoadEffect(0x6, "event\\ev001_00.eff")
    LoadEffect(0x7, "battle\\ms00001.eff")
    SoundLoad(840)
    OP_68(0, 800, -23700, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x15)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x17)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x19)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x1B)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x101, -800, 0, -22000, 180)
    SetChrPos(0x102, -1500, 0, -20700, 180)
    SetChrPos(0x103, 1500, 0, -19700, 180)
    SetChrPos(0x104, 800, 0, -21500, 180)
    SetChrChipByIndex(0x8, 0x1C)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1C)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 800, 0, -27500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -800, 0, -27500, 0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 3000, -150, -28700, 0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, -3000, -150, -28700, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 2100, 0, -26200, 315)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrPos(0x11, -2100, 0, -26200, 45)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 0, -300, -29500, 0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x13, 0, -1500, -34500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x21, 0x28)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x4)
    OP_90(0x21, 0, -10500, -71500, 0)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x4)
    OP_90(0x22, -700, -6700, -55800, 0)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x4)
    OP_90(0x23, 700, -6700, -55800, 0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -8400, 180)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01101.itp")
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 800, -25700, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)

    ChrTalk(
        0x8,
        (
            "#5200948V\x07\x02",
            "#30W...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5200949V\x07\x02",
            "#6P#35W...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B5")

    ChrTalk(
        0x101,
        "#5201001V#5P#0010F#N#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200951V#5P#0301F#N#40WDamn it. There's no end to 'em...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45AA")

    label("loc_43B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4445")

    ChrTalk(
        0x101,
        (
            "#5200952V#5P#0010F#N#40WI don't know how much longer I can\x01",
            "handle this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200953V#5P#0206F#N#40WLimit reached...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45AA")

    label("loc_4445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D7")

    ChrTalk(
        0x101,
        "#5200954V#5P#0008F#N#40WIt can't end like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5200955V#5P#0106F#N#40WTo accept defeat...in a place like this?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45AA")

    label("loc_44D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4558")

    ChrTalk(
        0x101,
        (
            "#5200956V#5P#0008F#N#40WThis can't be happening...\x01",
            "(No! I refuse to let this\x01",
            "be the end. It can't be!)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_45AA")

    label("loc_4558")


    ChrTalk(
        0x101,
        (
            "#5200957V#5P#0006F#N#40W(My legs can hardly support\x01",
            "my weight anymore.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_45AA")

    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    Sound(1957, 255, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x13,
        "Man's Voice",
        (
            "#5200958V\x07\x02",
            "Is that all? Well, I suppose you did put\x01",
            "up an admirable fight.\x02",
        )
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
    PlayBGM("ed7526", 0)
    Fade(500)
    OP_68(0, -500, -30500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x27)
    SetChrSubChip(0x104, 0x0)
    OP_68(0, 500, -26500, 3000)

    def lambda_46DD():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9B9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_46DD)
    Sleep(1000)
    BeginChrThread(0x12, 3, 0, 42)
    Sleep(1300)
    BeginChrThread(0x8, 3, 0, 43)
    BeginChrThread(0x9, 3, 0, 44)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 40)
    BeginChrThread(0x11, 3, 0, 41)
    OP_6F(0x1)
    Fade(500)
    OP_68(20, 1000, -23530, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    WaitChrThread(0x13, 1)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#5200959V\x07\x00",
            "#5P#0005F...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200960V#5P#0307F#5PLoggins? The hell, man?!\x01",
            "Why are you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5200961V\x07\x02",
            "#2POh, Randy. Don't misunderstand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5200962V\x07\x02",
            "#2PYour old coworker isn't here right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#5200963V\x07\x02",
            "#2PI'm merely borrowing his body so we\x01",
            "can have a little chat.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5200964V#5P#0101FTh-The way he talks...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200965V#5P#0205FN-No. This is impossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200966V#5P#0013FJoachim?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200967V\x07\x02",
            "#2PHaha! Very good, Bannings.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200968V\x07\x02",
            "#2PIt seems as though you've read my invitation.\x01",
            "How delightful.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200969V\x07\x02",
            "#2PI suppose this means that fool Ernest isn't\x01",
            "completely useless, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200970V\x07\x00",
            "#5P#0310FYou've got some nerve, pal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200971V#5P#0108FWhat are you planning?\x02\x03",
            "#5200972V#0110FIt's like you want Crossbell to plunge into\x01",
            "chaos! And for what?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200973V#5P#0007FJust what is the D∴G cult's goal?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200974V\x07\x02",
            "#2POh? If you wish to know that, I must insist\x01",
            "that you become my comrades.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200975V\x07\x02",
            "#2PCome, take a bit of Gnosis. You would gain\x01",
            "access to everything I know, of course.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x103,
        (
            "#5200976V\x07\x00",
            "#5P#0207FStop it! Stop making light of what you have done!\x02\x03",
            "#5200977V#0210F#30WY-You are nothing but a monster. A beast\x01",
            "that does nothing but commit atrocities!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200978V\x07\x02",
            "#2PA beast, am I? Now, Tio, it would be unfair to pin\x01",
            "the actions of every lodge on me.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200979V\x07\x02",
            "#2PThen again, I DID collect all of the experimental\x01",
            "data on our Gnosis prototype.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200980V\x07\x02",
            "#2PAnd with that, I was finally able to perfect\x01",
            "it in this ancient and holy land...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200981V\x07\x02",
            "#2P#4SOh, yes! All is according to fate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200982V\x07\x00",
            "#5P#0013FYou're insane...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200983V#5P#0301FYeah. The hell are you on about?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200984V\x07\x02",
            "#2PHahaha... It is none of my concern whether\x01",
            "or not fools who've yet to reach Wisdom can\x01",
            "comprehend my actions.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200985V\x07\x02",
            "#2PNow, I have one simple demand.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200986V\x07\x02",
            "#2PReturn to us our Lady KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#5200987V\x07\x00",
            "#5P#0105FWh-What do you want with her?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200988V#5P#0201FLady KeA?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200989V#5P#0013FAbsolutely not! What could you possibly\x01",
            "want with her, anyway?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200990V\x07\x02",
            "#2POh, do not misunderstand.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200991V\x07\x02",
            "#2PLady KeA is our Divine Child...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200992V\x07\x02",
            "#2PThat you happened to stumble upon her is\x01",
            "nothing more than happenstance.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200993V\x07\x02",
            "#2PI am just restoring her to her rightful place.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5200994V\x07\x00",
            "#5P#0010FNo more joking around, Joachim!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_52E7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_52E7)
    Fade(500)
    SetChrChipByIndex(0x101, 0x14)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    OP_0D()

    def lambda_531A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_531A)

    def lambda_5333():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5333)

    def lambda_534C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_534C)
    Fade(500)
    SetChrChipByIndex(0x102, 0x16)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x18)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x1A)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200995V#0007F#5PYou'd involve an innocent girl in your insane\x01",
            "fanaticism?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200996V#0110F#5PListen to what you just said! You're spouting\x01",
            "nothing but delusions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5200997V#5P#0307FGehenna'd freeze over before we'd hand\x01",
            "KeDo over to a rat bastard like you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200998V#0201F#5PLeave and never return!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5200999V\x07\x02",
            "#2PA shame. So our negotiations have fallen\x01",
            "short, then?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201000V\x07\x02",
            "#2PIf so, I'm more than happy to step over your\x01",
            "corpses on my way to retrieve my lady.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x2)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(190, 1000, -23260, 1000)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_55F1():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_55F1)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_5618():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5618)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5200950V\x07\x00",
            "#0010F#5PTch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5201002V#5P#0312FHeh. Bring it on, asshole.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201003V\x07\x02",
            "#2PVery well. I recommend you finish praying\x01",
            "to that goddess you love so much.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201004V\x07\x02",
            "#2PNow, then...prepare to die.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x20, 0x8)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    Sleep(300)
    StopBGM(0x1770)
    Sound(2041, 255, 100, 0)
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    Sleep(1200)
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
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x20, 0x8)
    OP_68(0, 700, -15500, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x8, 0x1C)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1C)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x8, 1500, 0, -28000, 0)
    SetChrPos(0x9, -1500, 0, -28000, 0)
    SetChrPos(0xA, 3000, -150, -29200, 0)
    SetChrPos(0xB, -3000, -150, -29200, 0)
    SetChrPos(0x10, 2600, 0, -26700, 315)
    SetChrPos(0x11, -2600, 0, -26700, 45)
    SetChrPos(0x12, 0, 0, -30000, 0)
    SetChrPos(0x13, 0, 0, -26500, 0)
    SetChrPos(0x101, -900, 0, -20800, 180)
    SetChrPos(0x102, -1600, 0, -19500, 180)
    SetChrPos(0x103, 1600, 0, -18500, 180)
    SetChrPos(0x104, 900, 0, -20300, 180)
    OP_68(0, 700, -22500, 2500)
    MoveCamera(0, 19, 0, 2500)
    SetCameraDistance(19500, 2500)
    SetChrChipByIndex(0x20, 0x36)
    SetChrSubChip(0x20, 0x0)

    def lambda_595B():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFAA10, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_595B)
    WaitChrThread(0x20, 1)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x37)
    SetChrSubChip(0x20, 0x4)
    Sound(804, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x20, 0x3)
    Sleep(100)
    SetChrSubChip(0x20, 0x2)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5201006V#0007F#5PK-KeA? What are you doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5201007V#0107F#5P#NNo! Get back!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201008V\x07\x02",
            "#6POh, Lady KeA...!\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7534", 0)
    SetCameraDistance(15000, 60000)

    ChrTalk(
        0x20,
        (
            "#5201009V\x07\x00",
            "#5P#1107FDon't hurt them!\x02\x03",
            "#5201010VIf you do...I'll never forgive you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201011V#0307F#11PWe're fine, KeDo! J-Just head back inside\x01",
            "like a good girl, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5201012V#0207F#11P#NRight! Go back and play with Shizuku!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201013V\x07\x02",
            "#6PI've come to usher you home, Lady KeA.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201014V\x07\x02",
            "#6PI beseech you. Forget this foolishness and\x01",
            "return to your rightful place.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201015V\x07\x02",
            "#6PThough you may not understand your role\x01",
            "in this yet, you remain our beloved--\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x20, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(931, 0, 80, 0)
    Sound(840, 2, 100, 0)
    SetChrSubChip(0x20, 0x2)
    Sleep(100)
    SetChrSubChip(0x20, 0x1)
    Sleep(100)
    SetChrSubChip(0x20, 0x0)
    Sleep(100)
    SetChrSubChip(0x20, 0x1)
    Sleep(100)
    SetChrSubChip(0x20, 0x2)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 39, 3)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    AnonymousTalk(
        0x20,
        (
            "#5201016V\x07\x0D",
            "Shut up! I don't care! Just promise me!\x02\x03",
            "#5201017VP-Promise me you won't do bad things to\x01",
            "them anymore!\x07\x00\x02",
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

    def lambda_5DB1():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5DB1)
    Sleep(50)

    def lambda_5DCD():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5DCD)

    def lambda_5DE6():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5DE6)

    def lambda_5DFF():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5DFF)
    Sleep(50)

    def lambda_5E1B():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5E1B)

    def lambda_5E34():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5E34)
    Sleep(50)

    def lambda_5E50():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5E50)

    def lambda_5E69():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5E69)
    Sleep(300)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201018V\x07\x02",
            "#6P...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5201083V\x07\x00",
            "#0005F#5P...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5201020V#0105F#5P#NKeA...?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x20,
        (
            "#5201021V\x07\x0D",
            "#5P#1115F...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201022V\x07\x02",
            "#6PHeh... Hahahaha...!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201023V\x07\x02",
            "#6PWorthy! You, my lady, are most worthy\x01",
            "of being our Divine Child!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201024V\x07\x02",
            "#6PVery well.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201025V\x07\x02",
            "#6PIf you come with me, my comrades will\x01",
            "stay their hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5201026V\x07\x0D",
            "#5P#1119FYou mean it?\x02\x03",
            "#5201027VYou won't do anything bad?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201028V\x07\x02",
            "#6PI swear it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201029V\x07\x02",
            "#6PNow, come this way.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5201030V\x07\x00",
            "#0007F#5PNo!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(270, 800, -21290, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 60000)
    SetChrSubChip(0x20, 0xA)
    SetChrPos(0x13, 0, 0, -26200, 0)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)

    def lambda_616B():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_616B)
    WaitChrThread(0x101, 1)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x14)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    TurnDirection(0x20, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#5201031V\x07\x0D",
            "#1117F#11PLloyd...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5201032V\x07\x00",
            "#5P#0010FNo! Listen to me, KeA! You're afraid\x01",
            "of the dark, right?\x02\x03",
            "#5201033VIf you leave us, won't you be lonely?\x02\x03",
            "#5201034VI'm begging you, don't listen to a word\x01",
            "he says! He's tricking you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5201035V\x07\x0D",
            "#1119F#11P#30WB-But...\x02\x03",
            "#5201036V#1118F...I don't have any memories.\x02\x03",
            "#5201037VI don't even know who I am.\x02\x03",
            "#5201038V#1120FIf I'm just a burden to you...why would\x01",
            "you want me to stay?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#5201039V\x07\x00",
            "#5P#0007FA burden? You've only been a blessing!\x02\x03",
            "#5201040V#0000FI want... No, we ALL want you to stay by\x01",
            "our side, for as long as you can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5201041V\x07\x0D",
            "#1117F#11P...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 39)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 38)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#5201042V\x07\x00",
            "#5P#0104FThat's right. You ARE a blessing. Because\x01",
            "of you, we've figured out who we want to\x01",
            "be, KeA. You've helped us mature!\x02\x03",
            "#5201043V#0102FWatching over you has allowed us to discover\x01",
            "our true meanings in life! And I mean that!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x103,
        (
            "#5201044V#5P#0204FIt is true.\x02\x03",
            "#5201045V#0208FSometimes, I could not understand why I\x01",
            "lived. What reason could there be...?\x02\x03",
            "#5201046V#0214FBut being with you, that has given me\x01",
            "the resolve to do anything!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)

    ChrTalk(
        0x104,
        (
            "#5201047V#0300F#5PThat's why, KeDo... That's why you shouldn't\x01",
            "sweat about the small stuff like this.\x02\x03",
            "#5201048VAll we want is for you to grow up happy, and to\x01",
            "keep that goofy, carefree smile on full blast.\x02\x03",
            "#5201049V#0309F'Cause that smile gives us the strength to push\x01",
            "forward! To overcome the struggles we face!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x13B, 0x190)
    Sleep(750)
    OP_93(0x20, 0x2D, 0x190)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#5201050V\x07\x0D",
            "#6P#1119F#40WElie... Tio, Randy...\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x4)
    SetChrChipByIndex(0x24, 0x34)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x24, -2600, 1000, -8300, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    def lambda_6800():
        OP_92(0xFE, 0xA28, 0xFFFFC43C, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6800)
    Sound(814, 0, 90, 0)

    def lambda_6819():
        OP_9D(0xFE, 0xA28, 0x0, 0xFFFFC43C, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6819)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)

    def lambda_6840():
        OP_92(0xFE, 0xFFFFF5D8, 0xFFFFA8E4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6840)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)
    SetChrSubChip(0x24, 0x0)
    Sleep(50)
    Sound(854, 0, 90, 0)

    def lambda_6875():
        OP_9D(0xFE, 0xFFFFF5D8, 0x0, 0xFFFFA8E4, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_6875)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)

    def lambda_68B1():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_68B1)
    SetChrChipByIndex(0x24, 0x35)
    SetChrSubChip(0x24, 0x0)
    WaitChrThread(0x24, 2)
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2053, 255, 100, 0)

    ChrTalk(
        0x24,
        (
            "#5201051V\x07\x00",
            "#6P#1200FGrrrrr...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x24, 500)
    Sleep(300)

    ChrTalk(
        0x20,
        (
            "#5201052V\x07\x0D",
            "#1116F#11P#40WAnd Zeit, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5201053V\x07\x00",
            "#5P#0004FWe're police officers, KeA.\x02\x03",
            "#5201054VIf your memories worry you, we can track them\x01",
            "down. We can find them for you.\x02\x03",
            "#5201055V#0008FSo, believe me when I say that there's no good\x01",
            "reason for you to listen to his lies.\x02\x03",
            "#5201056V#0001FJust...don't go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "#5201057V\x07\x0D",
            "#1116F#11P#40WLloyd...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetCameraDistance(15000, 800)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x2A, 1, 0, 45)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x20,
        (
            "#5201058V\x07\x00",
            "#1104F#11P#40W...Okay.\x02\x03",
            "#5201059V#1102FI'll stay with you. Forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201060V#5P#0002F...And ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5201061V#5P#0102FKeA...\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -23700, 1500)
    OP_6F(0x1)
    Sound(1956, 255, 100, 0)
    Sleep(150)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201062V\x07\x02",
            "#11PHeh heh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1959, 255, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201063V\x07\x02",
            "#11P#4SHAHAHAHAHAHA!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BBE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_6BBE)
    Sleep(50)

    def lambda_6BCE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6BCE)
    SetChrChipByIndex(0x24, 0x33)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x24, 2)

    def lambda_6C08():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFB244, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_6C08)
    Sleep(500)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201064V\x07\x02",
            "#11PWell done! I mean, tricking our Divine Child\x01",
            "with those meaningless gestures...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201065V\x07\x02",
            "#11PI can now see that entrusting her to you was\x01",
            "quite the blunder on my part!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201066V\x07\x02",
            "#11PSpecial Support Section! Prepare yourselves\x01",
            "to suffer a slow, painful death!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x2)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_68(160, 800, -23310, 1000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_6DC5():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6DC5)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_6DE7():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6DE7)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x20, 1)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#5201067V\x07\x00",
            "#0101F#5PUgh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5201068V#0202F#5P#NWell, at least his incessant rambling provided\x01",
            "us with a break!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#5201069V#0007F#5PStand back, KeA!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    ChrTalk(
        0x104,
        (
            "#5201070V#0307F#5PListen to Lloyd! We gotta get you back\x01",
            "inside, okay?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x21,
        "Man's Voice",
        "#5201071V#1PThat will be unnecessary.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
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
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0x13, 0xB4, 0x1F4)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201072V\x07\x02",
            "#5PWhat?!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5201073V#0105F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201074V#0005F#5PWhen did you...?!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -200, -28700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x8, 1500, 0, -29500, 0)
    OP_90(0x9, -1500, 0, -29500, 0)
    OP_90(0xA, 3000, -150, -30700, 0)
    OP_90(0xB, -3000, -150, -30700, 0)
    OP_90(0x10, 2600, 0, -28200, 315)
    OP_90(0x11, -2600, 0, -28200, 45)
    OP_90(0x12, 0, 0, -31500, 0)
    OP_90(0x13, 0, 0, -27700, 180)
    OP_68(0, -9500, -71500, 0)
    MoveCamera(33, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x10)
    SetChrChipByIndex(0xC, 0x1C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x1C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1C)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x1C)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    OP_90(0xC, -2100, -6340, -54200, 150)
    OP_90(0xD, -400, -7120, -57400, 180)
    OP_90(0xE, 1100, -4800, -47900, 190)
    OP_90(0xF, -600, -3100, -40800, 180)
    OP_90(0x14, 900, -6340, -54200, 190)
    OP_90(0x15, 1500, -5880, -52200, 190)
    OP_90(0x16, -900, -4400, -46100, 170)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x2A, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 24)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    WaitChrThread(0xC, 3)
    SetChrSubChip(0x21, 0x11)
    Sleep(130)
    SetChrSubChip(0x21, 0x12)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x21,
        (
            "#5201075VEight Leaves One Blade's second\x01",
            "form: Gale...\x02",
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
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 300)
    Sleep(100)
    SetChrSubChip(0x21, 0x13)
    Sleep(90)
    SetChrSubChip(0x21, 0x14)
    OP_6F(0x10)
    CancelBlur(0)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x14, 3)
    BeginChrThread(0x21, 3, 0, 26)
    WaitChrThread(0x21, 3)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Fade(250)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x9)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    SetCameraDistance(14000, 1000)
    OP_6F(0x10)
    SetChrSubChip(0x21, 0x17)
    Sleep(110)
    SetChrSubChip(0x21, 0x16)
    Sleep(110)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 900, -27500, 1000)
    SetCameraDistance(18500, 1000)
    MoveCamera(43, 23, 0, 1000)

    ChrTalk(
        0x21,
        "#5201076V#5P#1407F#4S#9AStrike!\x02",
    )

    SetChrSubChip(0x21, 0x15)
    Sound(532, 0, 100, 0)
    Sleep(70)
    PlayEffect(0x3, 0xFF, 0x21, 0x40, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(541, 0, 100, 0)
    Sleep(30)
    SetChrSubChip(0x21, 0x1D)
    OP_82(0x1F4, 0x0, 0xBB8, 0x384)
    Sound(816, 0, 100, 0)
    Sound(340, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 34)
    Sleep(10)
    BeginChrThread(0xB, 3, 0, 32)
    Sleep(10)
    BeginChrThread(0x9, 3, 0, 30)
    Sleep(10)
    BeginChrThread(0x13, 3, 0, 36)
    Sleep(10)
    BeginChrThread(0x12, 3, 0, 35)
    Sleep(10)
    BeginChrThread(0x8, 3, 0, 29)
    Sleep(10)
    BeginChrThread(0x10, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0xA, 3, 0, 31)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    CancelBlur(0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1100, -25500, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_90(0x13, 0, 0, -28100, 0)
    OP_68(0, 1100, -24500, 1500)
    OP_6F(0x1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5201077V#5P#0002FArios!\x02",
    )

    CloseMessageWindow()

    def lambda_7661():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7661)
    WaitChrThread(0x13, 2)
    Sleep(300)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201078V\x07\x02",
            "#2P#40WTh-The Divine Blade of Wind?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201079V\x07\x00",
            "#5P#0309FHoly hell! Great timing, dude!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5201080V#5P#0202FDid you have that planned?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x21, 0x20)
    ClearChrFlags(0x21, 0x2)
    SetChrSubChip(0x21, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    Sound(541, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x21,
        (
            "#5201081V#5P#1404FHaha. It wasn't my intention to appear at\x01",
            "the last minute. You can trust me on that.\x02\x03",
            "#5201082V#1402FAnd I didn't come alone, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201019V#5P#0005FWhat?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_90(0xD, -2700, -5300, -49800, 135)
    OP_90(0x15, 2200, -5000, -48600, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0x14, 0x1)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x2)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_90(0xC, 900, -4340, -46000, 180)
    OP_90(0x14, -1100, -4500, -46500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    Fade(500)
    OP_68(0, -3700, -47500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(15500, 3000)
    OP_0D()
    Sound(567, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 23)
    Sleep(500)
    Sound(845, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 22)
    Sleep(500)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)

    def lambda_7914():
        OP_96(0xFE, 0x2BC, 0xFFFFEE08, 0xFFFF4868, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7914)
    Sleep(100)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_7939():
        OP_96(0xFE, 0xFFFFFD44, 0xFFFFEDA4, 0xFFFF4674, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7939)
    WaitChrThread(0x23, 1)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    WaitChrThread(0x22, 1)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    Sound(531, 0, 100, 0)
    OP_6F(0x10)
    Sleep(300)

    ChrTalk(
        0x23,
        "#5201084V#11P#0601FDamn! He beat us to the punch again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#5201085V#5P#1004FPhew. Apologies, Dudley. Age is starting\x01",
            "to catch up with me, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5201086V#1110FIt's the chief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201087V#0002FAnd Detective Dudley, too!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)

    def lambda_7A6F():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7A6F)
    Sleep(50)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_7A94():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7A94)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 1100, -28700, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x22, 0x1)
    OP_90(0x22, -1100, -2500, -36700, 0)
    OP_90(0x23, 1100, -2500, -36700, 0)
    SetChrPos(0x102, -1600, 0, -20800, 180)
    SetChrPos(0x103, 1600, 0, -19300, 180)
    SetChrPos(0x104, 900, 0, -21400, 180)
    SetChrPos(0x20, 300, 0, -20300, 180)
    OP_68(0, 1100, -26700, 2000)

    def lambda_7B63():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7B63)
    Sleep(50)

    def lambda_7B80():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7B80)
    WaitChrThread(0x23, 1)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    Sound(531, 0, 100, 0)
    Sound(820, 0, 100, 0)

    def lambda_7BB2():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_7BB2)
    WaitChrThread(0x22, 1)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    TurnDirection(0x22, 0x13, 500)
    SetChrChipByIndex(0x22, 0x2A)
    SetChrSubChip(0x22, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    Sleep(500)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201088V\x07\x02",
            "#11P#40WI-Impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201089V\x07\x00",
            "#0309F#5P#NHah! Tryin' to impress us, Chief? Gotta\x01",
            "say, you aren't doing a half-bad job.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#5201090V#0102F#5P#NThank the Goddess you're safe! I was\x01",
            "worried after our separation.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x22,
        (
            "#5201091V#5P#1002FGood thing we ran into Arios when we\x01",
            "did. Luck must be on our side today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        (
            "#5201092V#0602F#11PTrue. We managed just fine...with a bit\x01",
            "of unexpected assistance, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5201093V#0005F#5P#NWhat do you mean?\x02\x03",
            "#5201094V#0000F...Oh, I see now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#5201095V#0202F#5P#NReinforcements!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(0, 100, -31700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x348)
    SetScenarioFlags(0x5C, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3E08 end

    def Function_22_7E78(): pass

    label("Function_22_7E78")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_7EDE():
        OP_9C(0xFE, 0xFFFFFC7C, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7EDE)

    def lambda_7EFB():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7EFB)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x0)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_22_7E78 end

    def Function_23_7F59(): pass

    label("Function_23_7F59")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_7FBF():
        OP_9C(0xFE, 0x384, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7FBF)

    def lambda_7FDC():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7FDC)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_7F59 end

    def Function_24_8033(): pass

    label("Function_24_8033")

    SetChrChipByIndex(0xC, 0x1D)
    SetChrSubChip(0xC, 0x0)

    def lambda_8040():
        OP_96(0xFE, 0xFFFFF7CC, 0xFFFFDB20, 0xFFFEFA48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8040)
    Sleep(1500)
    BeginChrThread(0x14, 3, 0, 25)
    WaitChrThread(0xC, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_24_8033 end

    def Function_25_8071(): pass

    label("Function_25_8071")

    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)

    def lambda_807E():
        OP_96(0xFE, 0x384, 0xFFFFDEA4, 0xFFFF0920, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_807E)
    WaitChrThread(0x14, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_25_8071 end

    def Function_26_80A6(): pass

    label("Function_26_80A6")

    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 180, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 180, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-2500, -8300, -66600, 500)
    MoveCamera(10, 19, 5, 500)
    SetCameraDistance(13500, 500)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    SetChrFlags(0x21, 0x20)
    ClearChrFlags(0x21, 0x1)
    SetChrChip(0x0, 0x21, 0x32, 0x1F4)
    ClearChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    OP_92(0x21, 0xFFFFF574, 0xFFFF0024, 0x0)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_81DE():
        OP_96(0xFE, 0xFFFFF574, 0xFFFFDC10, 0xFFFF0024, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_81DE)

    def lambda_81F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_81F8)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_822C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_822C)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    OP_6F(0x79)
    Sleep(350)
    OP_68(1200, -7700, -63700, 500)
    MoveCamera(20, 15, -7, 500)
    SetCameraDistance(13000, 500)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x8FC, 0xFFFF0BDC, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_8302():
        OP_96(0xFE, 0x8FC, 0xFFFFDECC, 0xFFFF0BDC, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8302)

    def lambda_831C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_831C)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_8350():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8350)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    OP_6F(0x79)
    Sleep(300)
    OP_68(0, -6100, -57500, 0)
    MoveCamera(180, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(0, -3700, -43500, 2000)
    MoveCamera(137, 37, -5, 2000)
    SetCameraDistance(15500, 2000)
    SetChrFlags(0x21, 0x800)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0xFFFFF95C, 0xFFFF234C, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_8459():
        OP_96(0xFE, 0xFFFFF95C, 0xFFFFE4A8, 0xFFFF2540, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8459)

    def lambda_8473():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8473)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_84A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_84A7)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x76C, 0xFFFF3990, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_8556():
        OP_96(0xFE, 0x76C, 0xFFFFE9BC, 0xFFFF3990, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8556)

    def lambda_8570():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8570)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x15, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_85A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_85A4)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(150)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0xFFFFF9C0, 0xFFFF522C, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_8653():
        OP_96(0xFE, 0xFFFFF9C0, 0xFFFFEF98, 0xFFFF522C, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8653)

    def lambda_866D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_866D)
    Sleep(100)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 27)
    Sleep(100)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x16, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_86AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_86AA)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x514, 0xFFFF6B90, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_8759():
        OP_96(0xFE, 0x514, 0xFFFFF5D8, 0xFFFF6B90, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8759)

    def lambda_8773():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_8773)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xF, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_87A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_87A7)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(300)
    OP_6F(0x79)
    ClearChrFlags(0x21, 0x800)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    SetChrChip(0x0, 0x21, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_881C():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFA04C, 0x157C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_881C)
    Sleep(250)
    Sound(854, 0, 100, 0)
    Fade(100)
    OP_68(0, 2900, -28000, 0)
    MoveCamera(48, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, 900, -24500, 500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    WaitChrThread(0x21, 1)
    Sound(58, 0, 100, 0)
    Sound(31, 0, 100, 0)

    def lambda_889C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_889C)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x1, 0x21, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)
    Return()

    # Function_26_80A6 end

    def Function_27_88E9(): pass

    label("Function_27_88E9")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_892D():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_892D)
    OP_82(0x190, 0x0, 0xBB8, 0x258)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_88E9 end

    def Function_28_8983(): pass

    label("Function_28_8983")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_89C7():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_89C7)
    OP_82(0x190, 0x0, 0xBB8, 0x258)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_28_8983 end

    def Function_29_8A1D(): pass

    label("Function_29_8A1D")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8A3B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8A3B)

    def lambda_8A54():
        OP_9C(0xFE, 0x5DC, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8A54)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_8A1D end

    def Function_30_8A75(): pass

    label("Function_30_8A75")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8A93():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8A93)

    def lambda_8AAC():
        OP_9C(0xFE, 0xFFFFFA24, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8AAC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_30_8A75 end

    def Function_31_8ACD(): pass

    label("Function_31_8ACD")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8AEB():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8AEB)

    def lambda_8B04():
        OP_9C(0xFE, 0xBB8, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8B04)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_31_8ACD end

    def Function_32_8B25(): pass

    label("Function_32_8B25")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8B43():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_8B43)

    def lambda_8B5C():
        OP_9C(0xFE, 0xFFFFF448, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8B5C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_8B25 end

    def Function_33_8B7D(): pass

    label("Function_33_8B7D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8B9B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_8B9B)

    def lambda_8BB4():
        OP_9C(0xFE, 0x1F40, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8BB4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_8B7D end

    def Function_34_8BD5(): pass

    label("Function_34_8BD5")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8BF3():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_8BF3)

    def lambda_8C0C():
        OP_9C(0xFE, 0xFFFFE0C0, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C0C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_34_8BD5 end

    def Function_35_8C2D(): pass

    label("Function_35_8C2D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8C4B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8C4B)

    def lambda_8C64():
        OP_9C(0xFE, 0x0, 0xFFFFFA24, 0xFFFFE890, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8C64)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_35_8C2D end

    def Function_36_8C85(): pass

    label("Function_36_8C85")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_8C9E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8C9E)

    def lambda_8CB7():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8CB7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_8CDC():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8CDC)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Sound(514, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_8C85 end

    def Function_37_8D03(): pass

    label("Function_37_8D03")

    SetChrChipByIndex(0x102, 0x30)
    SetChrSubChip(0x102, 0x0)

    def lambda_8D10():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D10)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x16)
    SetChrSubChip(0x102, 0x0)
    Return()

    # Function_37_8D03 end

    def Function_38_8D38(): pass

    label("Function_38_8D38")

    SetChrChipByIndex(0x103, 0x31)
    SetChrSubChip(0x103, 0x0)

    def lambda_8D45():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8D45)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x18)
    SetChrSubChip(0x103, 0x0)
    Return()

    # Function_38_8D38 end

    def Function_39_8D67(): pass

    label("Function_39_8D67")

    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x0)

    def lambda_8D74():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFBB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8D74)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1A)
    SetChrSubChip(0x104, 0x0)
    Return()

    # Function_39_8D67 end

    def Function_40_8D9C(): pass

    label("Function_40_8D9C")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8DA9():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8DA9)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_8D9C end

    def Function_41_8DCB(): pass

    label("Function_41_8DCB")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8DD8():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DD8)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_8DCB end

    def Function_42_8DFA(): pass

    label("Function_42_8DFA")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8E07():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8E07)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_8DFA end

    def Function_43_8E29(): pass

    label("Function_43_8E29")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8E36():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8E36)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_8E29 end

    def Function_44_8E58(): pass

    label("Function_44_8E58")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_8E65():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E65)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_8E58 end

    def Function_45_8E87(): pass

    label("Function_45_8E87")

    OP_25(0x348, 0x5A)
    Sleep(200)
    OP_25(0x348, 0x50)
    Sleep(200)
    OP_25(0x348, 0x46)
    Sleep(200)
    OP_25(0x348, 0x3C)
    Sleep(200)
    OP_25(0x348, 0x32)
    Sleep(200)
    OP_25(0x348, 0x28)
    Sleep(200)
    OP_25(0x348, 0x1E)
    Sleep(200)
    OP_25(0x348, 0x14)
    Sleep(200)
    OP_25(0x348, 0xA)
    Sleep(200)
    OP_24(0x348)
    Return()

    # Function_45_8E87 end

    def Function_46_8ECA(): pass

    label("Function_46_8ECA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50514.itc", 0x1E)
    LoadChrToIndex("apl/ch50515.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch02500.itc", 0x22)
    LoadChrToIndex("apl/ch50509.itc", 0x23)
    LoadChrToIndex("chr/ch00900.itc", 0x24)
    LoadChrToIndex("chr/ch00950.itc", 0x25)
    LoadChrToIndex("chr/ch00951.itc", 0x26)
    LoadChrToIndex("chr/ch08200.itc", 0x27)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    LoadChrToIndex("chr/ch05500.itc", 0x29)
    LoadChrToIndex("chr/ch08700.itc", 0x2A)
    LoadChrToIndex("apl/ch50011.itc", 0x2B)
    LoadChrToIndex("chr/ch00953.itc", 0x2C)
    LoadChrToIndex("chr/ch02750.itc", 0x2D)
    LoadChrToIndex("chr/ch02700.itc", 0x2E)
    LoadChrToIndex("chr/ch02702.itc", 0x2F)
    LoadChrToIndex("apl/ch50516.itc", 0x30)
    LoadChrToIndex("apl/ch50517.itc", 0x31)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    SoundLoad(806)
    OP_68(260, 1000, -25050, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -900, 0, -22200, 180)
    SetChrPos(0x102, -1600, 0, -21100, 180)
    SetChrPos(0x103, 1600, 0, -20100, 180)
    SetChrPos(0x104, 900, 0, -21700, 180)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x1)
    SetChrFlags(0x13, 0x8000)
    OP_90(0x13, 0, 0, -28100, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 0, 0, -24500, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    OP_90(0x22, -1300, 0, -27700, 0)
    TurnDirection(0x22, 0x13, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x25)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    OP_90(0x23, 1300, 0, -27700, 0)
    TurnDirection(0x23, 0x13, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x20, 0x27)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -20600, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x4)
    SetChrChipByIndex(0x24, 0x2D)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x24, -2600, 0, -22300, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x28)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 400, 0, 6000, 180)
    SetChrChipByIndex(0x26, 0x29)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -700, 0, 6500, 180)
    SetChrChipByIndex(0x27, 0x2A)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -1700, 0, 6500, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    OP_68(260, 1000, -23050, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5201121V#5P#0002FThe downtown boys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5201122V#5P#0202FThey are driving Joachim's forces back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201123V#5P#0309FWell, would you look at that. Not too bad\x01",
            "for fightin' professional soldiers, eh?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201124V\x07\x02",
            "#11PUnbelievable... How is this possible? It's\x01",
            "just a group of measly delinquents!\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
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

    def lambda_93C0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_93C0)

    def lambda_93CD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93CD)

    def lambda_93DA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_93DA)

    def lambda_93E7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_93E7)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5201216V\x07\x00",
            "#5P#0005FMy Enigma?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5201126V#5P#0102FThat must mean that they were able to\x01",
            "fix our communication systems!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
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
            "#5201127V\x07\x00",
            "#0001FThis is the Special Suppo--\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201128V\x07\x05",
            "Th-Thank goodness! Lloyd, you're alive!\x02\x03",
            "#5201129VEver since I heard that the Guardian Force\x01",
            "was after you, I've been in the dark!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5201130V\x07\x00",
            "#0002FFran? So you're safe, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201131V\x07\x05",
            "Yes! We've begun the counterattack!\x02\x03",
            "#5201132VAlso, the guild managed to patch up the\x01",
            "communications terminal that was taken\x01",
            "down during the chaos...\x02\x03",
            "#5201133VAlbeit limited, orbal communications are\x01",
            "back online!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5201134V\x07\x00",
            "#0000FThat's great news!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(1200)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(200)
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201135V\x07\x05",
            "Hah! And who, pray tell, do you think was\x01",
            "behind supplying them with the necessary\x01",
            "technical information?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5201136V\x07\x00",
            "#0005FIs that...Jona?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201137V\x07\x05",
            "From now on, call me Jona the Genius!\x02\x03",
            "#5201138VI've already restored the orbal network,\x01",
            "too, with a little bit of help from the IBC.\x02\x03",
            "#5201139VDon't let my hard work go to waste now!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5201140V\x07\x00",
            "#0014FHaha, we owe you!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201141V\x07\x05",
            "Officers should be en route, so hold on\x01",
            "for just a bit longer!\x02\x03",
            "#5201142VI'm going to try to contact my sister and\x01",
            "the guards at Tangram Gate, okay?\x02\x03",
            "#5201143VPlease be careful!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#5201144V\x07\x05",
            "Yeah! Remember, only losers die!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#5201145V\x07\x00",
            "#0000FWe'll keep that in mind!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_CA(0x0, 0x0, 0x3)
    Fade(250)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201146V\x07\x02",
            "#11PI-Impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5201147V\x07\x00",
            "#5P#1403FSo, the pieces finally slide into place.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Fade(500)
    OP_68(0, 1000, -26500, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)

    def lambda_9B76():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9B76)

    def lambda_9B83():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9B83)

    def lambda_9B90():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9B90)

    def lambda_9B9D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B9D)
    SetCameraDistance(14000, 1000)

    def lambda_9BB3():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9A70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_9BB3)
    WaitChrThread(0x21, 1)
    SetChrChipByIndex(0x21, 0x30)
    SetChrSubChip(0x21, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_6F(0x10)
    Sleep(500)

    ChrTalk(
        0x21,
        (
            "#5201148V#5P#1401FJoachim Guenter, high priest of D∴G.\x02\x03",
            "#5201149VDo you still intend on pursuing this folly?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201150V\x07\x02",
            "#6PHeheh. Folly, is it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201151V\x07\x02",
            "#6PMy force, including those morons in the mafia,\x01",
            "is almost 1,000 strong.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201152V\x07\x02",
            "#6POur stamina is inexhaustible, and\x01",
            "we have no need for sleep.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201153V\x07\x02",
            "#6PI can play the waiting game. After annihilating\x01",
            "those in our way, the Divine Child will be ours.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Joachim's Voice",
        (
            "#5201154V\x07\x02",
            "#6PHahaha! Please, look forward to what awaits!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1961, 255, 100, 0)
    SetChrSubChip(0x13, 0x0)
    PlayEffect(0x0, 0x0, 0x13, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    PlayEffect(0x1, 0xFF, 0x13, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)

    def lambda_9EC0():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_9EC0)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
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
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x3)
    SetChrSubChip(0x22, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x23,
        (
            "#5201156V\x07\x00",
            "#12P#0601FHe passed out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201157V#0013F#5P#NI don't know what to make of this.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#5201158V#0206F#11P#NWell, it would seem that Joachim is able to\x01",
            "control them from a remote location.\x02\x03",
            "#5201159V#0201FAnd to make matters worse, it very well may\x01",
            "be a considerable distance away.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#5201160V#0101F#5P#NCould he be manipulating the Guardian Force\x01",
            "in full from wherever he's hiding, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#5201161V#0301F#11P#NThat complicates things. Other than taking\x01",
            "the fight to Joachim, what options do we got?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x21,
        "#5201162V#5P#1404FI believe that I can help you, in that regard.\x02",
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
        "#5201213V#0011F#5P#NYou can?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -23870, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x21, 0x0, 0x190)
    OP_68(0, 1000, -23200, 1000)

    def lambda_A2EC():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFA1DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_A2EC)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#5201164V#11P#1403FMoments ago, Estelle and Joshua uncovered\x01",
            "the cult's lodge.\x02\x03",
            "#5201165V#1401FIt lies to the northeast of the Ancient\x01",
            "Battlefield.\x02\x03",
            "#5201166VTraces of the missing people have been\x01",
            "found, as well, indicating that they're\x01",
            "being held inside.\x02\x03",
            "#5201167V#1403FThey were investigating possible entry\x01",
            "points, last time I spoke to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201168V#0013F#5PThe Ancient Battlefield... That place again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5201169V#0101F#5PIt makes sense the lodge would be there,\x01",
            "given how many ruins are present in the\x01",
            "area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201170V#5P#0300FI say we go hit the son of a bitch where\x01",
            "the sun don't shine!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(110, 1000, -22710, 1000)

    def lambda_A59F():
        OP_95(0xFE, 1000, 0, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A59F)
    Sleep(150)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)

    def lambda_A5C4():
        OP_95(0xFE, -800, 0, -25400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_A5C4)
    WaitChrThread(0x23, 1)
    WaitChrThread(0x22, 1)
    OP_6F(0x1)

    ChrTalk(
        0x23,
        (
            "#5201171V#0606F#11PIt's not that simple, Orlando.\x02\x03",
            "#5201172V#0601FSupposedly, East Crossbell Highway has been\x01",
            "secured by a force the size of an army...\x02\x03",
            "#5201173VAnd it seems to consist primarily of the mafia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#5201174V#12P#1003FEither way, we're stretched thin. It'd be crazy\x01",
            "to recklessly charge into a fight against a guy\x01",
            "we don't really know anything about.\x02\x03",
            "#5201175V#1001FI don't know. If we had a car, we might be able\x01",
            "to break their line somehow, but fat chance.\x02\x03",
            "#5201176VMost of our police cars were stolen by guards\x01",
            "under his influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201177V#0010F#5PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5201178V#5P#0206FThey were thorough, if nothing else.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x25, 0x8)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)

    NpcTalk(
        0x25,
        "Man's Voice",
        "#5201179VPerhaps I can be of some assistance.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_A95D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A95D)

    def lambda_A96A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A96A)

    def lambda_A977():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A977)

    def lambda_A984():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A984)

    def lambda_A991():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A991)
    ClearChrFlags(0x25, 0x8)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetCameraDistance(15500, 3000)
    OP_68(0, 1000, 0, 3000)

    def lambda_A9D1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A9D1)
    Sleep(50)

    def lambda_A9EE():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_A9EE)

    def lambda_AA08():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_AA08)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#5201180V#0005FMr. Crois?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5201181V#1110FShizuku and Bell, too!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -10500, 0)
    MoveCamera(135, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 200, 0, -16100, 0)
    SetChrPos(0x102, 700, 0, -17300, 0)
    SetChrPos(0x103, -700, 0, -17900, 0)
    SetChrPos(0x104, 500, 0, -18400, 0)
    SetChrPos(0x20, -600, 0, -16500, 0)
    SetChrPos(0x22, 1900, 0, -16900, 0)
    SetChrPos(0x23, 2300, 0, -18300, 0)
    SetChrPos(0x21, -1800, 0, -18500, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, 1000, 0, -20300, 0)
    SetChrPos(0x25, 900, 0, -3400, 180)
    SetChrPos(0x26, -300, 0, -3200, 180)
    SetChrPos(0x27, -1000, 0, -3300, 180)
    SetCameraDistance(16000, 2500)

    def lambda_AB8D():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB8D)

    def lambda_ABA7():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_ABA7)

    def lambda_ABC1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_ABC1)
    Sleep(50)

    def lambda_ABDE():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABDE)

    def lambda_ABF8():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ABF8)

    def lambda_AC12():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AC12)

    def lambda_AC2C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_AC2C)

    def lambda_AC46():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_AC46)
    Sleep(50)

    def lambda_AC63():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AC63)

    def lambda_AC7D():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_AC7D)

    def lambda_AC97():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AC97)

    def lambda_ACB1():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_ACB1)
    Sleep(1000)
    Sound(115, 0, 100, 0)
    OP_71(0xC, 0x3C, 0x0, 0x0, 0x0)
    WaitChrThread(0x24, 1)
    SetChrChipByIndex(0x24, 0x2F)
    SetChrSubChip(0x24, 0x0)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x22, 1)
    WaitChrThread(0x23, 1)
    WaitChrThread(0x21, 1)
    OP_79(0xC)
    OP_6F(0x10)

    ChrTalk(
        0x26,
        (
            "#5201182V#6P#2904FLooks like you guys had fun.\x02\x03",
            "#5201183V#2901FBut, KeA, dear. I was worried sick about you!\x01",
            "Don't do anything rash like that again, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        (
            "#5201184V#6P#6001FTh-That's right! You dashed off and, and...!\x02\x03",
            "#5201185V#6008FDon't do that again, you dummy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5201186V#11P#1106FS-Sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "#5201187V#1404F#11PHaha...\x02\x03",
            "#5201188V#1402FI'm just glad you're safe, Shizuku.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x27,
        "#5201189V#6P#6010FYou, too, Father!\x02",
    )

    CloseMessageWindow()

    def lambda_AECF():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD3DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_AECF)
    WaitChrThread(0x22, 1)
    Sleep(300)

    ChrTalk(
        0x22,
        (
            "#5201190V#11P#1003FNice to meet you. I'm Sergei Lou,\x01",
            "chief of the Special Support Section.\x02\x03",
            "#5201191V#1000FSo, tell me about this assistance of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x25,
        (
            "#5201192V#6P#2804FWell, there's a limousine in the garage.\x02\x03",
            "#5201193V#2800FConsidering it's bulletproof and as fast\x01",
            "as an airship, I believe it would make\x01",
            "the ideal bulldozer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#5201194V#11P#1005FI'll be damned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#5201195V#11P#0602F#NThat's perfect!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    ChrTalk(
        0x21,
        (
            "#5201196V#1403F#11PIf that's our strategy, we need to decide on\x01",
            "who will actually be on board.\x02\x03",
            "#5201197V#1400FWe also need people to defend this place, too.\x01",
            "It cannot just be me, I'm afraid.\x02",
        )
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
    Fade(500)
    OP_68(680, 1100, -11430, 0)
    MoveCamera(123, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5201198V#11P#0003F...No.\x02\x03",
            "#5201199V#0001FEntrust Guenter's arrest to the SSS.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B295():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_B295)
    Sleep(50)

    def lambda_B2A5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_B2A5)
    Sleep(50)

    def lambda_B2B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_B2B5)

    ChrTalk(
        0x21,
        "#5201200V#11P#1405FWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#5201201V#11P#0605FAre you suggesting what I think you are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#5201202V#5P#1001FHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5201203V#11P#0006FWe have substantial reason to believe that\x01",
            "KeA is Joachim's sole target.\x02\x03",
            "#5201204V#0008FIf she's taken, we lose. No question. But...\x02\x03",
            "#5201205V#0000F...if we can protect KeA, while arresting him\x01",
            "in the process, victory is ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201206V#11P#0304FBasically, Lloyd's sayin' that if this place falls,\x01",
            "it's all over.\x02\x03",
            "#5201207V#0300FSo, our defense has gotta be on its A-game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5201208V#0104F#11PThis place should be like an iron wall, given that\x01",
            "Arios will be here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5201209V#6P#0202F#11P...but with Dudley, Chief Sergei, and the police\x01",
            "supplying backup, the IBC will be impenetrable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "#5201210V#11P#1404FYour reasoning is sound.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#5201211V#11P#0601FI-I understand. I really do, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "#5201212V#5P#1006F...that doesn't sort everything.\x02",
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

    def lambda_B6C1():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B6C1)
    Sleep(50)

    def lambda_B6D1():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B6D1)

    def lambda_B6DE():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B6DE)

    def lambda_B6EB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B6EB)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x101,
        "#5201163V#6P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#5201214V#5P#1003FYou've still got a problem on your hands.\x02\x03",
            "#5201215V#1001FCan any of you drive a car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201125V#6P#0011FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5201217V#12P#0106FNow that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x23,
        "#5201218V#11P#0607FIt's fine, Sergei. I can lend my--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#5201219V#5P#1003FNot happening. I want you to assume command\x01",
            "of the police force and help Arios.\x02\x03",
            "#5201220V#1002FI can go.\x02",
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
        0x102,
        "#5201221V#12P#0105FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201222V#12P#0305FYou can drive, Chief? Didn't think someone\x01",
            "your age was good with that kinda stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        (
            "#5201223V#5P#1004FDrive? Hell, I was the driving instructor\x01",
            "at the police academy.\x02\x03",
            "#5201224V#1002FSo, I'd rein in your surprise, Randy.\x01",
            "I can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5201225V#12P#0202FIntriguing. Your shrouded history continues\x01",
            "to reveal itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201226V#6P#0000FThank you. We'll leave the driving to you.\x02",
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x20)

    ChrTalk(
        0x20,
        "#5201227V#12P#1112FDo you really have to go?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BB59():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB59)
    Sleep(50)

    def lambda_BB69():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BB69)

    def lambda_BB76():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BB76)

    def lambda_BB83():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BB83)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#5201228V#0004F#5PYeah, we do. But you have nothing to worry about.\x02\x03",
            "#5201229V#0002FListen to me. Nothing will stop us from coming\x01",
            "back to you, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5201230V#5P#0109FThat's right.\x02\x03",
            "#5201231V#0102FWhen we get back, you can help me cook us\x01",
            "a huge meal. Does that sound good to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5201232V#12P#1110FUh-huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5201233V#11P#0202FExcellent. KeA's magic touch is\x01",
            "sure to invigorate any dish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5201234V#11P#0309FIt's a party, then. I'll bring the booze.\x02\x03",
            "#5201235VWe can invite everyone we know down to the\x01",
            "SSS building and have a grand ol' time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201236V#0009F#5PHaha, definitely.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(15000, 1200)
    OP_68(270, 1100, -11520, 1200)

    def lambda_BE13():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE13)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_6F(0x10)
    Fade(250)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x31)
    SetChrSubChip(0x20, 0x8)
    OP_0D()
    Sound(910, 0, 100, 0)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#5201237V#0006F#5PBe honest, KeA. You've been feeling\x01",
            "lonely for a long time, haven't you?\x02\x03",
            "#5201238V#0008FBecause of your amnesia, because of\x01",
            "not knowing who you are...\x02\x03",
            "#5201239V#0001FI'm sorry. I should have realized it sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "#5201240V#12P#1112F#40WLloyd...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    EndChrThread(0x101, 0x3)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x20, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x20, 0xC)
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    SetChrSubChip(0x20, 0xD)
    Sleep(500)

    ChrTalk(
        0x20,
        (
            "#5201241V#12P#1106F#30WYeah. It makes me pretty sad when I think\x01",
            "about it sometimes.\x02\x03",
            "#5201242V#1104FBut I wasn't ever alone. Not really.\x02\x03",
            "#5201243V#1108FTh-That's why...\x02\x03",
            "#5201244V#1112FThat's why you have to come back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5201245V#0002F#5PWe will. I promise!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_E3(0xA)
    OP_29(0x4E, 0x1, 0x2)
    OP_29(0x4E, 0x4, 0x10)
    OP_E3(0x3)
    OP_E3(0xB)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 2)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_8ECA end

    def Function_47_C1AF(): pass

    label("Function_47_C1AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1EB")
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    Jump("Function_47_C1AF")

    label("loc_C1EB")

    Return()

    # Function_47_C1AF end

    SaveToFile()

Try(main)
