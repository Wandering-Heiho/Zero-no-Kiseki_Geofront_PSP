from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c010b.bin",                # FileName
        "c010b",                    # MapName
        "c010b",                    # Location
        0x0004,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 4, 0, 5],
    )

    BuildStringList((
        "c010b",                  # 0
        "Gina",                   # 1
        "Old Man Conte",          # 2
        "Pruna",                  # 3
        "Lenalee",                # 4
        "Haas",                   # 5
        "Coppe",                  # 6
        "Chief Sergei",           # 7
        "Ryu",                    # 8
        "Anri",                   # 9
        "Elie",                   # 10
        "Zeit",                   # 11
        "CGF Guardsman",          # 12
        "CGF Guardsman",          # 13
        "CGF Guardsman",          # 14
        "CGF Guardsman",          # 15
        "CGF Guardsman",          # 16
        "CGF Guardsman",          # 17
        "CGF Guardsman",          # 18
        "CGF Guardsman",          # 19
        "車１",                   # 20
        "車２",                   # 21
        "イベント用ＮＰＣ",       # 22
        "イベント用ＮＰＣ",       # 23
        "イベント用ＮＰＣ",       # 24
        "イベント用ＮＰＣ",       # 25
        "イベント用ＮＰＣ",       # 26
        "SE制御",                 # 27
        "Central Square",         # 28
        "West Street",            # 29
        "Administrative District",# 30
        "Residential District",   # 31
        "Entertainment District", # 32
        "East Street",            # 33
        "Downtown District",      # 34
        "Harbor District",        # 35
        "IBC",                    # 36
        "Station Street",         # 37
        "Back Alley",             # 38
        "Ursula Road",            # 39
        "East Crossbell Highway", # 40
        "West Crossbell Highway", # 41
        "Mainz Mountain Path",    # 42
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch26000.itc",                   # 04
        "chr/ch39200.itc",                   # 05
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

    DeclNpc(30000,   0,       -1799,   270,  261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(14130,   0,       340,     0,    261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  261,  0x0, 0,   5,   0,   0,   2,   0,   11,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 54,  -0.0,                  25.799999237060547,    -0.5,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.0,                   -12.899999618530273,   0.09999999403953552,   1.0])
    DeclEvent(0x0000, 0, 55,  -22.200000762939453,   8.229999542236328,     -0.5,                  4.0,                   [-0.35355374217033386, 0.35355305671691895,   0.0,                   0.0,                   -0.35355305671691895,  -0.35355374217033386,  0.0,                   0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.939151763916016,    10.758625030517578,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 56,  19.0,                  6.0,                   -0.5,                  16.0,                  [-1.5993946078651788e-07, 0.5,                   0.0,                   0.0,                   -0.25,                 -3.1987892157303577e-07, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.5000029802322388,    -9.499998092651367,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 57,  -6.429999828338623,    -21.1200008392334,     -4.199999809265137,    16.0,                  [-1.5993946078651788e-07, 0.5,                   0.0,                   0.0,                   -0.25,                 -3.1987892157303577e-07, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.280001163482666,    3.2149932384490967,    0.8399999737739563,    1.0])

    DeclActor(-270,    0,       -980,    800,     130,     1500,    -10,     0x007C, 0,  12, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "Central Square")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "West Street")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "Administrative District")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "Residential District")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "Entertainment District")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "East Street")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "Downtown District")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "Harbor District")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "IBC")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "Station Street")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "Back Alley")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "Ursula Road")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_8D8",          # 00, 0
        "Function_1_990",          # 01, 1
        "Function_2_9DD",          # 02, 2
        "Function_3_A08",          # 03, 3
        "Function_4_A24",          # 04, 4
        "Function_5_11E1",         # 05, 5
        "Function_6_1273",         # 06, 6
        "Function_7_12F8",         # 07, 7
        "Function_8_1469",         # 08, 8
        "Function_9_14F3",         # 09, 9
        "Function_10_157B",        # 0A, 10
        "Function_11_15F7",        # 0B, 11
        "Function_12_16A4",        # 0C, 12
        "Function_13_1851",        # 0D, 13
        "Function_14_1CD2",        # 0E, 14
        "Function_15_2717",        # 0F, 15
        "Function_16_2763",        # 10, 16
        "Function_17_283A",        # 11, 17
        "Function_18_3AC8",        # 12, 18
        "Function_19_3B0C",        # 13, 19
        "Function_20_3B53",        # 14, 20
        "Function_21_3B9A",        # 15, 21
        "Function_22_3E9A",        # 16, 22
        "Function_23_8385",        # 17, 23
        "Function_24_86FF",        # 18, 24
        "Function_25_87F3",        # 19, 25
        "Function_26_8B4A",        # 1A, 26
        "Function_27_8B81",        # 1B, 27
        "Function_28_94C1",        # 1C, 28
        "Function_29_950B",        # 1D, 29
        "Function_30_9558",        # 1E, 30
        "Function_31_95A5",        # 1F, 31
        "Function_32_95F2",        # 20, 32
        "Function_33_9643",        # 21, 33
        "Function_34_96BA",        # 22, 34
        "Function_35_984B",        # 23, 35
        "Function_36_9865",        # 24, 36
        "Function_37_A6C6",        # 25, 37
        "Function_38_A724",        # 26, 38
        "Function_39_A74A",        # 27, 39
        "Function_40_A789",        # 28, 40
        "Function_41_A7D3",        # 29, 41
        "Function_42_A81D",        # 2A, 42
        "Function_43_A863",        # 2B, 43
        "Function_44_A8A9",        # 2C, 44
        "Function_45_A929",        # 2D, 45
        "Function_46_A9A6",        # 2E, 46
        "Function_47_A9DE",        # 2F, 47
        "Function_48_AA16",        # 30, 48
        "Function_49_AA88",        # 31, 49
        "Function_50_AAFA",        # 32, 50
        "Function_51_AB16",        # 33, 51
        "Function_52_AB32",        # 34, 52
        "Function_53_AB4E",        # 35, 53
        "Function_54_AB6A",        # 36, 54
        "Function_55_AB86",        # 37, 55
        "Function_56_ABA2",        # 38, 56
        "Function_57_ABBE",        # 39, 57
        "Function_58_ABDA",        # 3A, 58
        "Function_59_AD51",        # 3B, 59
    ))


    def Function_0_8D8(): pass

    label("Function_0_8D8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_918"),
        (1, "loc_924"),
        (2, "loc_930"),
        (3, "loc_93C"),
        (4, "loc_948"),
        (5, "loc_954"),
        (6, "loc_960"),
        (SWITCH_DEFAULT, "loc_96C"),
    )


    label("loc_918")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_924")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_930")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_93C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_948")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_954")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_960")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_96C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_978")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_978")

    label("loc_98F")

    Return()

    # Function_0_8D8 end

    def Function_1_990(): pass

    label("Function_1_990")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DC")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_990")

    label("loc_9DC")

    Return()

    # Function_1_990 end

    def Function_2_9DD(): pass

    label("Function_2_9DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A07")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_2_9DD")

    label("loc_A07")

    Return()

    # Function_2_9DD end

    def Function_3_A08(): pass

    label("Function_3_A08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_A08")

    label("loc_A23")

    Return()

    # Function_3_A08 end

    def Function_4_A24(): pass

    label("Function_4_A24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD")
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    SetChrPos(0x1, -26950, -1160, -4340, 90)
    SetChrPos(0x2, -26950, -1160, -4340, 90)
    SetChrPos(0x3, -26950, -1160, -4340, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB9")
    SetChrPos(0x4, -26950, -1160, -4340, 90)
    SetChrPos(0x5, -26950, -1160, -4340, 90)
    Jump("loc_AD8")

    label("loc_AB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8")
    SetChrPos(0x4, -26950, -1160, -4340, 90)

    label("loc_AD8")

    Jump("loc_10DB")

    label("loc_ADD")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B64")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_B83")

    label("loc_B64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B83")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_B83")

    Jump("loc_10DB")

    label("loc_B88")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C33")
    SetChrPos(0x0, 11850, 0, 28440, 180)
    SetChrPos(0x1, 11850, 0, 28440, 180)
    SetChrPos(0x2, 11850, 0, 28440, 180)
    SetChrPos(0x3, 11850, 0, 28440, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0F")
    SetChrPos(0x4, 11850, 0, 28440, 180)
    SetChrPos(0x5, 11850, 0, 28440, 180)
    Jump("loc_C2E")

    label("loc_C0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2E")
    SetChrPos(0x4, 11850, 0, 28440, 180)

    label("loc_C2E")

    Jump("loc_10DB")

    label("loc_C33")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBA")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_CD9")

    label("loc_CBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD9")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_CD9")

    Jump("loc_10DB")

    label("loc_CDE")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D89")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D65")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_D84")

    label("loc_D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D84")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_D84")

    Jump("loc_10DB")

    label("loc_D89")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E34")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E10")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_E2F")

    label("loc_E10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2F")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_E2F")

    Jump("loc_10DB")

    label("loc_E34")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDF")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBB")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_EDA")

    label("loc_EBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDA")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_EDA")

    Jump("loc_10DB")

    label("loc_EDF")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8A")
    SetChrPos(0x0, 4040, 0, -21980, 0)
    SetChrPos(0x1, 4040, 0, -21980, 0)
    SetChrPos(0x2, 4040, 0, -21980, 0)
    SetChrPos(0x3, 4040, 0, -21980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F66")
    SetChrPos(0x4, 4040, 0, -21980, 0)
    SetChrPos(0x5, 4040, 0, -21980, 0)
    Jump("loc_F85")

    label("loc_F66")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F85")
    SetChrPos(0x4, 4040, 0, -21980, 0)

    label("loc_F85")

    Jump("loc_10DB")

    label("loc_F8A")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1035")
    SetChrPos(0x0, -13380, 0, 14530, 135)
    SetChrPos(0x1, -13380, 0, 14530, 135)
    SetChrPos(0x2, -13380, 0, 14530, 135)
    SetChrPos(0x3, -13380, 0, 14530, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1011")
    SetChrPos(0x4, -13380, 0, 14530, 135)
    SetChrPos(0x5, -13380, 0, 14530, 135)
    Jump("loc_1030")

    label("loc_1011")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")
    SetChrPos(0x4, -13380, 0, 14530, 135)

    label("loc_1030")

    Jump("loc_10DB")

    label("loc_1035")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DB")
    SetChrPos(0x0, 16840, 0, -3910, 270)
    SetChrPos(0x1, 16840, 0, -3910, 270)
    SetChrPos(0x2, 16840, 0, -3910, 270)
    SetChrPos(0x3, 16840, 0, -3910, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BC")
    SetChrPos(0x4, 16840, 0, -3910, 270)
    SetChrPos(0x5, 16840, 0, -3910, 270)
    Jump("loc_10DB")

    label("loc_10BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DB")
    SetChrPos(0x4, 16840, 0, -3910, 270)

    label("loc_10DB")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_1103")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1122")
    SetMapFlags(0x10000000)
    Event(0, 22)

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1136")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)
    Jump("loc_11C0")

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_114A")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 16)
    Jump("loc_11C0")

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_115E")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_11C0")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_1172")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 23)
    Jump("loc_11C0")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 4)), scpexpr(EXPR_END)), "loc_1186")
    ClearScenarioFlags(0x5C, 4)
    Event(0, 24)
    Jump("loc_11C0")

    label("loc_1186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_119D")
    ClearScenarioFlags(0x5C, 5)
    SetScenarioFlags(0x0, 0)
    Event(0, 25)
    Jump("loc_11C0")

    label("loc_119D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 6)), scpexpr(EXPR_END)), "loc_11B1")
    ClearScenarioFlags(0x5C, 6)
    Event(0, 27)
    Jump("loc_11C0")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 7)), scpexpr(EXPR_END)), "loc_11C0")
    ClearScenarioFlags(0x5C, 7)
    Event(0, 36)

    label("loc_11C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E0")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_11E0")

    Return()

    # Function_4_A24 end

    def Function_5_11E1(): pass

    label("Function_5_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11FD")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_120F")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_120F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_120F")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    OP_1B(0x4, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1272")
    OP_1B(0x0, 0x0, 0x32)
    OP_1B(0x1, 0x0, 0x33)
    OP_1B(0x2, 0x0, 0x34)
    OP_1B(0x4, 0x0, 0x35)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1272")

    Return()

    # Function_5_11E1 end

    def Function_6_1273(): pass

    label("Function_6_1273")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Oh, no! I'm totally late!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though I was shopping for dinner, I'm\x01",
            "still going to get chewed out at home... *sob*\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1273 end

    def Function_7_12F8(): pass

    label("Function_7_12F8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_138C")
    Jump("loc_13D6")

    label("loc_138C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13AC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D6")

    label("loc_13AC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13CC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D6")

    label("loc_13CC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13D6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xFE,
        "Oh? When did it get so late?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With how dangerous it's gotten\x01",
            "lately, I better hurry on home.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_12F8 end

    def Function_8_1469(): pass

    label("Function_8_1469")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If you wanna lose weight, then\x01",
            "you gotta do some exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like you better start jogging\x01",
            "tomorrow, then, sweetie.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1469 end

    def Function_9_14F3(): pass

    label("Function_9_14F3")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Wh-What? But I don't want to go on\x01",
            "runs by myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "C'mon, let's do it together! I'm sure\x01",
            "that'd make me work harder...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_14F3 end

    def Function_10_157B(): pass

    label("Function_10_157B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oops. It's already way past time to\x01",
            "close up shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want, you can have all of the\x01",
            "leftover balloons.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_157B end

    def Function_11_15F7(): pass

    label("Function_11_15F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168A")
    Sound(823, 0, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FMaking yourself feel right at home,\x01",
            "aren't you?\x02\x03",
            "Then again, you've probably lived here for\x01",
            "quite some time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 6)
    Jump("loc_16A0")

    label("loc_168A")


    NpcTalk(
        0xFE,
        "Black Cat",
        "Nyaon?\x02",
    )

    CloseMessageWindow()

    label("loc_16A0")

    TalkEnd(0xFE)
    Return()

    # Function_11_15F7 end

    def Function_12_16A4(): pass

    label("Function_12_16A4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　              Bell of Crossbell\x01",
            "This enormous bell was excavated in\x01",
            "Crossbell State in S1185. It is estimated to\x01",
            "have been forged during the Middle Ages,\x01",
            "using multiple metal alloys. When struck,\x01",
            "it emits a low, yet pleasant ring.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is theorized that the bell was created by\x01",
            "some influential person of the times, but its\x01",
            "true purpose remains shrouded in mystery.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_16A4 end

    def Function_13_1851(): pass

    label("Function_13_1851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-31880, 3900, -19510, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8410, 0)
    SetChrPos(0x101, -28730, 1300, -14730, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetCameraDistance(7410, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x7)
    Sleep(500)

    def lambda_1913():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1913)

    def lambda_192D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_192D)
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x7)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0003F#5PPhew...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#0002F#5PWhat a great view.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(9220, 3900, 27970, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26360, 0)
    OP_68(-9090, 3900, -24280, 12000)
    MoveCamera(45, 14, 0, 12000)
    OP_6E(700, 12000)
    SetCameraDistance(22320, 12000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-21610, 3900, -19830, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10170, 0)
    SetChrPos(0x101, -22170, 1300, -17820, 90)
    SetChrPos(0xD, -25810, 1300, -17860, 90)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    SetCameraDistance(9170, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#0002F#5PCrossbell's really grown. The town where Uncle\x01",
            "lives was by no means small, but compared to\x01",
            "this? It doesn't hold a candle.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        "#0008F#5PI'm finally home, aren't I?\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_68(-26650, 3900, -20900, 2000)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0005F#11PA cat?\x02\x03",
            "#0000FIf you're already at the SSS building, that must\x01",
            "mean you've been staying here way longer than\x01",
            "the Special Support Section has.\x02\x03",
            "#0012FSorry about barging into your home like this.\x01",
            "I'll go find somewhere else to think.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(823, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(9420, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x4A, 4)
    BeginChrThread(0xD, 0, 0, 2)
    OP_4C(0xD, 0xFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_1851 end

    def Function_14_1CD2(): pass

    label("Function_14_1CD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch20400.itc", 0x20)
    LoadChrToIndex("chr/ch20500.itc", 0x21)
    LoadChrToIndex("chr/ch20800.itc", 0x22)
    LoadChrToIndex("chr/ch23600.itc", 0x23)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_90(0x101, -18000, -8000, -21000, 225)
    OP_90(0x102, -16900, -8000, -22100, 225)
    OP_90(0x103, -17000, -8000, -20000, 225)
    OP_90(0x104, -15900, -8000, -21100, 225)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -28500, -8200, -20500, 180)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_1F7F():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1F7F)

    def lambda_1F99():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1F99)

    def lambda_1FB3():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1FB3)
    Sound(458, 0, 100, 0)

    def lambda_1FD4():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1FD4)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    Sleep(4400)

    def lambda_201D():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_201D)
    Sleep(200)

    def lambda_203A():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_203A)
    Sleep(200)

    def lambda_2057():
        OP_95(0xFE, -22000, -8200, -24000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2057)
    Sleep(200)

    def lambda_2074():
        OP_95(0xFE, -21900, -8200, -25600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2074)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25000, -4500, -16000, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(31000, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-25000, -7500, -16000, 8000)
    MoveCamera(30, 20, 0, 8000)
    SetCameraDistance(26000, 8000)
    PlaceName2(340, 40, "c_plac34", 0x0, 3000)
    WaitChrThread(0x101, 1)

    def lambda_213B():
        OP_95(0xFE, -28400, -8200, -25000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_213B)
    WaitChrThread(0x102, 1)

    def lambda_2159():
        OP_95(0xFE, -28500, -8200, -26100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2159)
    WaitChrThread(0x103, 1)

    def lambda_2177():
        OP_95(0xFE, -26700, -8200, -25200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2177)
    WaitChrThread(0x104, 1)

    def lambda_2195():
        OP_95(0xFE, -26800, -8200, -26300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2195)
    WaitChrThread(0x101, 1)

    def lambda_21B3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21B3)
    WaitChrThread(0x103, 1)

    def lambda_21C4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_21C4)
    WaitChrThread(0x102, 1)

    def lambda_21D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_21D5)
    WaitChrThread(0x104, 1)

    def lambda_21E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_21E6)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    EndChrThread(0x22, 0x1)
    Fade(500)
    OP_68(-27800, -7200, -24000, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0200001V#12P#0005FWasn't this an old office building?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0200002V#12P#0306FLooks kinda run-down, doesn't it?\x02\x03",
            "#0200003V#0301FCompared to that spiffy department\x01",
            "store over there, this place could be\x01",
            "from the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200004V#0206F#11PFrom my first impression, I would say that it\x01",
            "was built around 30 years ago. I am surprised\x01",
            "it has not been demolished yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0200005V#12P#0108FIs the Special Support Section's\x01",
            "main office really here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200006V#12P#0001FI'm pretty sure. I don't think I made any\x01",
            "wrong turns on the way here, anyway...\x02",
        )
    )

    CloseMessageWindow()
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)
    Sleep(150)

    NpcTalk(
        0xE,
        "Man's Voice",
        "#0200007V#2PHey, you guys are late.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x13B, 0x1F4)
    Sleep(50)
    OP_93(0x104, 0x13B, 0x1F4)

    def lambda_2513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2513)

    def lambda_2524():
        OP_95(0xFE, -28500, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2524)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 1)

    ChrTalk(
        0x101,
        "#0200008V#12P#0005FChief Sergei?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xE,
        (
            "#0200009VThat's my name. Now get your\x01",
            "asses inside.\x02\x03",
            "#0200010VI know you got questions, but don't\x01",
            "ask me what the Special Support\x01",
            "Section is just yet.\x02\x03",
            "#0200011VOnce we sit down, I'll answer any\x01",
            "questions you might have. Got it?\x01",
            "Good.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_93(0xE, 0x0, 0x1F4)

    def lambda_26BC():
        OP_95(0xFE, -28500, -8200, -20500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_26BC)
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)

    def lambda_26EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_26EC)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xE, 1)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1CD2 end

    def Function_15_2717(): pass

    label("Function_15_2717")

    Sound(803, 2, 100, 0)
    Sleep(4400)
    OP_25(0x323, 0x5A)
    Sleep(100)
    OP_25(0x323, 0x50)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_24(0x323)
    Return()

    # Function_15_2717 end

    def Function_16_2763(): pass

    label("Function_16_2763")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-26000, -6000, -18500, 0)
    MoveCamera(0, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, -24000, -8200, -20000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(-26000, -4500, -18500, 8000)
    MoveCamera(0, 25, 0, 8000)
    SetCameraDistance(15500, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2763 end

    def Function_17_283A(): pass

    label("Function_17_283A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20600.itc", 0x1E)
    LoadChrToIndex("chr/ch22200.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis008.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis014.itp")
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -28800, -8200, -22700, 180)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_295D():
        OP_95(0xFE, -28800, -8200, -27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_295D)
    SetCameraDistance(15500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC5")

    ChrTalk(
        0x101,
        (
            "#0200234V#5P#0004FMan... What a nice breeze.\x02\x03",
            "#0200235V#0002FCrossbell City emits a strong metropolis\x01",
            "vibe now, that's for sure. Everything was\x01",
            "way smaller three years ago...\x02\x03",
            "#0200236VI mean, the city where Uncle lives was by\x01",
            "no means small, but compared to this? It\x01",
            "doesn't hold a candle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF5")

    label("loc_2AC5")


    ChrTalk(
        0x101,
        "#0200234V#5P#0002FMan, what a nice breeze.\x02",
    )

    CloseMessageWindow()

    label("loc_2AF5")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2B0F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B0F)
    OP_68(-48800, -7300, -27000, 3000)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_6F(0x1)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#0200237V#0005FOh. I can see Bellheim Apartments from here.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1500)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    AnonymousTalk(
        0x101,
        (
            "#0200238V#0004FI bet everyone from back then has moved by now.\x02\x03",
            "#0200239V#0000FI think Cecile's family is still living there,\x01",
            "though...\x02\x03",
            "#0200240V#0005FThat reminds me. I should pay them a visit once\x01",
            "I find the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0200241V#11P#0003F#30W(It's been three years since then...)\x02\x03",
            "#0200242V(After Uncle's family took me in, I eventually\x01",
            "enrolled in the Crossbell Police Academy.)\x02\x03",
            "#0200243V(I studied and trained like a madman. After that,\x01",
            "I passed the detective qualification exam.)\x02\x03",
            "#0200244V#0008F(But, in the end...)\x02\x03",
            "#0200245V(...what did I actually want to accomplish after\x01",
            "becoming a detective?)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -14000, -4200, -17500, 225)
    SetChrFlags(0xF, 0x8)
    ClearChrFlags(0xF, 0x80)

    NpcTalk(
        0xF,
        "Boy's Voice",
        "#0200246V#2SHey!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(-27000, -5300, -26200, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrPos(0xF, -14000, -4200, -17500, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0x10, -13000, -4200, -16500, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    BeginChrThread(0xF, 3, 0, 18)
    BeginChrThread(0x10, 3, 0, 19)
    OP_68(-27000, -7300, -26200, 3500)
    OP_93(0x101, 0x5A, 0x1F4)
    OP_0D()
    Sleep(1000)

    def lambda_2F5F():
        OP_96(0xFE, 0xFFFF923C, 0xFFFFDFF8, 0xFFFF99A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F5F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)

    ChrTalk(
        0x101,
        "#0200247V#6P#0005FYou two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#0200248V#2PMan, we've been looking everywhere for you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0200249V#2PWe went to the police department,\x01",
            "but they told us you weren't around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#0200250V#11PThey told us about this place, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0200251V#11PThis IS it, right? Where the Special\x01",
            "Support Section works?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200252V#6P#0000FY-Yeah. This is the place.\x02\x03",
            "#0200253VDid you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#0200254V#2PW-Well, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0200255V#2PWe thought we oughta thank you\x01",
            "for today. Y'know, the right way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200256V#6P#0005FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0200257V#11PIf you all hadn't been there, those monsters\x01",
            "would have hurt us pretty bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#0200258V#11PSo, that's why we came to thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200259V#6P#0002FWow. I, uh...\x02\x03",
            "#0200260VThanks, you two. I appreciate the sentiment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0200261V#2PD-Don't forget, you guys still look\x01",
            "dumb next to someone like Arios!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0200262V#2PBut, y'know...compared to the rest of the CPD,\x01",
            "I guess you looked pretty cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#0200263V#2PYou just gotta work hard to catch up to him, now!\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xE1, 0x1F4)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0x10,
        "#0200264V#5PC-C'mon, Ryu!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0200265V#5PWe came to THANK him. Why are you\x01",
            "trying to lecture him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0200266V#6P#0009FHaha...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#0200267V#6P#0004FHe's right, though. We don't plan on\x01",
            "disappointing you, Ryu.\x02\x03",
            "#0200268V#0000FBy the way, where do you two live?\x02\x03",
            "#0200269VI can escort you guys home, if you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#0200270V#2POh, no worries! West Street is\x01",
            "right over there, so I'm good.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x10E, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#0200271V#11PI live in the Residential District,\x01",
            "but I should be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#0200272V#11PBut, um, could you tell Elie and Tio\x01",
            "that we stopped by, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0200273V#6P#0002FSure. I'll let them know.\x02\x03",
            "#0200274VBe safe on your way back, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#0200275V#2PWe will!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#0200276V#11PWell, then, see you later!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10, 3, 0, 20)
    Sleep(300)
    BeginChrThread(0xF, 3, 0, 20)
    Sleep(3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitChrThread(0x10, 3)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0xF, 3)
    SetChrFlags(0xF, 0x80)
    Fade(1000)
    SetChrPos(0x101, -28800, -8200, -26200, 90)
    OP_68(-28800, -7300, -27000, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)
    OP_68(-28940, -7300, -27520, 1500)

    def lambda_3740():
        OP_95(0xFE, -28800, -8200, -27000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3740)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#0200277V#5P#0012FYou really are a simple guy, Lloyd Bannings.\x02\x03",
            "#0200278V#0002FAll it took to lift your spirits was getting\x01",
            "thanked by some random kids...\x02\x03",
            "#0200279V#0004FI guess, in the end, everything depends on\x01",
            "how I choose to face my feelings.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#0200280V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30WWord of advice, Lloyd...\x02\x03",
            "#0200281VTo be a man, you have to be willing to tackle\x01",
            "the issues you're facing head-on.\x02\x03",
            "#0200282VFollow your heart and intuition, and grasp the\x01",
            "truth with your own two hands.\x02\x03",
            "#0200283VIf you can do that, you'll be able to see what\x01",
            "exactly it is that you want to do.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(500, 0)
    OP_0D()
    OP_C7(0x1, 0x800)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0200284V#5P#0004F...\x02\x03",
            "#0200285VYeah, he's right.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-27780, -7300, -22810, 2500)
    MoveCamera(32, 14, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_93(0x101, 0x0, 0x12C)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#0200286V#12P#0000FI'm not going to get anywhere\x01",
            "if I back out now.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(17000, 2000)

    def lambda_3A8E():
        OP_95(0xFE, -28800, -8200, -22700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A8E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x5C, 2)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_283A end

    def Function_18_3AC8(): pass

    label("Function_18_3AC8")


    def lambda_3ACD():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3ACD)
    WaitChrThread(0xF, 1)
    OP_93(0xF, 0x10E, 0x0)

    def lambda_3AF2():
        OP_96(0xFE, 0xFFFF9A70, 0xFFFFDFF8, 0xFFFF987C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3AF2)
    WaitChrThread(0xF, 1)
    Return()

    # Function_18_3AC8 end

    def Function_19_3B0C(): pass

    label("Function_19_3B0C")

    Sleep(300)

    def lambda_3B14():
        OP_95(0xFE, -21500, -8200, -24000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B14)
    WaitChrThread(0x10, 1)
    OP_93(0x10, 0x10E, 0x0)

    def lambda_3B39():
        OP_96(0xFE, 0xFFFF9C64, 0xFFFFDFF8, 0xFFFF9C64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B39)
    WaitChrThread(0x10, 1)
    Return()

    # Function_19_3B0C end

    def Function_20_3B53(): pass

    label("Function_20_3B53")

    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)

    def lambda_3B62():
        OP_96(0xFE, 0xFFFFAC04, 0xFFFFDFF8, 0xFFFFA240, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B62)
    WaitChrThread(0xFE, 1)

    def lambda_3B80():
        OP_95(0xFE, -14000, -4200, -17500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B80)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_3B53 end

    def Function_21_3B9A(): pass

    label("Function_21_3B9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_3DDD():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3DDD)

    def lambda_3DF7():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3DF7)

    def lambda_3E11():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3E11)
    Sound(457, 0, 100, 0)

    def lambda_3E32():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3E32)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Sleep(1500)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 4)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3B9A end

    def Function_22_3E9A(): pass

    label("Function_22_3E9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch50214.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    OP_68(-27460, 2300, -18410, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(-26090, 2300, -17520, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, -28800, 1300, -14000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -21800, 1300, -17700, 90)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0xA)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    FadeToBright(1000, 0)

    def lambda_3FD1():
        OP_96(0xFE, 0xFFFF8F80, 0x514, 0xFFFFBADC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FD1)

    def lambda_3FEB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FEB)
    WaitChrThread(0x101, 1)
    OP_71(0x7, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#2101547V#6P#0005F(Oh...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1178, 255, 90, 0)

    ChrTalk(
        0x11,
        "#2101548V#5P#30WLloyd?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    ReplaceBGM("ed7513", "ed7000")
    OP_68(-22610, 2300, -17660, 2000)

    def lambda_40A5():
        OP_96(0xFE, 0xFFFF9B38, 0x514, 0xFFFFBADC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40A5)
    WaitChrThread(0x101, 1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#2101549V#3P#0000FHey, Elie. How'd you know it was me?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1179, 255, 100, 0)
    OP_93(0x11, 0x10E, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x11,
        (
            "#2101550V#30WJust a hunch.\x02\x03",
            "#2101551V#30WI think I somehow knew you would\x01",
            "come.\x02",
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
        "#2101723V#6P#0004FSo you did...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_41FB():

        label("loc_41FB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_41FB")

    QueueWorkItem2(0x11, 2, lambda_41FB)

    def lambda_420D():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_420D)
    OP_68(-21800, 2800, -18300, 2500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x11, 0x2)
    Sleep(500)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 3300, 4000, 0)
    MoveCamera(18, 11, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)
    MoveCamera(42, 11, 0, 27000)
    SetCameraDistance(33000, 27000)

    def lambda_428C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_428C)
    OP_0D()
    Sleep(1000)

    AnonymousTalk(
        0x101,
        (
            "#2101553V#0002FBreathtaking as always...\x02\x03",
            "#2101554VIsn't that the IBC in the distance?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x11,
        (
            "#2101555V#0104F#30WYes, it is. I doubt you would find a night sky\x01",
            "as beautiful as Crossbell's even if you scoured\x01",
            "the entire continent.\x02\x03",
            "#2101556V#0108FYet, the more the lights of the city shine,\x01",
            "the more the stars seem to dim.\x02\x03",
            "#2101557VThe purity of starlight--the symbol of\x01",
            "Aidios' love.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4427():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4427)

    AnonymousTalk(
        0x101,
        "#2101558V#0001FElie...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x11,
        (
            "#2101559V#0106F#30WYou remember everything that happened\x01",
            "today, don't you?\x02\x03",
            "#2101560V#0108FWith Revache, Heiyue, and Dudley...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(40, 90, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#2101561V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "No matter what you do, you can't change\x01",
            "Crossbell's true nature.\x02\x03",
            "#2101562VRevache's iron grip is here to stay.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(120, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#2101563V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "I am merely referring to them as our\x01",
            "fellow business competitors.\x02\x03",
            "#2101564VState law protects competition between\x01",
            "businesses and free trade, you know.\x02\x03",
            "#2101565VDo you take offense with that, officers?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(180, 120, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#2101566V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "We're charged with maintaining a certain degree of\x01",
            "order in a city where justice has an uphill battle as is.\x02\x03",
            "#2101567VWe're expected to suppress major crimes and protect\x01",
            "the public from criminal organizations and foreign\x01",
            "intelligence agencies...\x02\x03",
            "#2101568VCan you possibly fathom the work that goes into that?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-18240, 1700, -17030, 0)
    MoveCamera(53, 7, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16500, 0)
    OP_68(-18240, 2500, -17030, 50000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#2101569V#5P#0103FTherein lies this city's darkness: the tragic truth\x01",
            "of the state called Crossbell.\x02\x03",
            "#2101570V#0108FWe're kept alive only by the will of the Empire\x01",
            "and the Republic, stripped of all pride, lied to and\x01",
            "deceived...\x02\x03",
            "#2101571VWe're drowning in false prosperity and frivolities\x01",
            "only because our captors allow it.\x02\x03",
            "#2101572V#0106FEveryone just surrenders to these circumstances\x01",
            "and accepts the status quo, blissfully ignorant...\x02\x03",
            "#2101573V#0101FThat's the city we live in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101641V#12P#0003FMaybe you're right.\x02\x03",
            "#2101575V#0000FBut you don't want to surrender just yet,\x01",
            "do you, Elie?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#2101677V#5P#0108F...\x02\x03",
            "#2101577V#0103FI once had a mother and father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101745V#12P#0005F'Once had'...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101579V#5P#0102FOh, I suppose putting it like that makes\x01",
            "it sound as if they've passed away.\x02\x03",
            "#2101580VThey're still very much alive.\x02\x03",
            "#2101581V#0104FWhat I mean to say is, they divorced when\x01",
            "I was little. My mother lives in the Empire\x01",
            "now, and my father in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101582V#12P#0003FI had no idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101583V#5P#0100FMy father was born and raised in the Republic.\x02\x03",
            "#2101584VHe moved to Crossbell City, met my mother...\x02\x03",
            "#2101585V...and after marrying into the MacDowell family,\x01",
            "he strove to become a politician.\x02\x03",
            "#2101586V#0103FImmediately after becoming a diet member, he\x01",
            "recognized the ugly, distorted reality of the city.\x02\x03",
            "#2101587VAs someone with a strong sense of justice, he\x01",
            "made it his duty to mend this broken city.\x02\x03",
            "#2101588VYear after year, he drafted reform bills, all in\x01",
            "the hopes of bringing change to the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101589V#12P#0002FThat's amaz--\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101590V#5P#0101FIt's not. In the end, his bills were never passed.\x02\x03",
            "#2101591V#0103FThe Imperial AND Republican factions both\x01",
            "shunned him, ridiculed him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x11,
        (
            "#2101592V#5P#0108FOne by one, his allies betrayed him, friends\x01",
            "left him, and he became the laughingstock\x01",
            "of the political world...\x02\x03",
            "#2101593VNot even my grandfather, as well respected\x01",
            "as he is for being neutral, was able to mend\x01",
            "his career...\x02\x03",
            "#2101594V#0106FCrossbell...brought my father to utter despair.\x02\x03",
            "#2101595VAnd then, one day, he quit--as a diet member,\x01",
            "as a husband, and...as my father. He decided\x01",
            "to leave everything behind for Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101596V#12P#0013F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101597V#5P#0108FMother couldn't stop him.\x02\x03",
            "#2101598VAnd, at the same time, she couldn't follow him\x01",
            "while dragging me along...\x02\x03",
            "#2101599V#0103FEventually, they settled on a divorce, and my\x01",
            "father was gone for good.\x02\x03",
            "#2101600V#0102FI always thought Mother hated him for what he\x01",
            "did, but I'm sure she was just heartbroken.\x02\x03",
            "#2101601VIt soon became apparent that living in Crossbell,\x01",
            "the state that robbed her of her love, would be\x01",
            "too much to bear...\x02\x03",
            "#2101602V#0104FMy mother left me behind in Crossbell and went to\x01",
            "live with her relatives in Erebonia. Then I was taken\x01",
            "in by Grandfather, who raised me to who I am now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101648V#12P#0008F...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-21800, 2300, -18300, 0)
    MoveCamera(300, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    MoveCamera(329, 33, 0, 80000)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#2101604V#5P#0102FIt was from that moment on that I vowed to follow\x01",
            "Grandfather down the path of politics.\x02\x03",
            "#2101605VIt's not as if I feel an urge to avenge my father or\x01",
            "anything like that.\x02\x03",
            "#2101606V#0104FI just... I couldn't accept reality.\x02\x03",
            "#2101607VHow could a family, so jubilant and loving, end up\x01",
            "in absolute shambles that quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101632V#6P#0006F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101609V#5P#0103FAfter I made my decision, Grandfather began to\x01",
            "help me. I studied abroad, all over the continent,\x01",
            "focusing on politics and economics.\x02\x03",
            "#2101610V#0108FHowever, the more I studied, the more I realized\x01",
            "that the gears of Crossbell were powered by\x01",
            "oppression.\x02\x03",
            "#2101611VOppression created by the Empire and the Republic.\x02\x03",
            "#2101612VOur justice, our national interests are intertwined\x01",
            "with Erebonia and Calvard, only serving to blur the\x01",
            "line between what we need and what they want.\x02\x03",
            "#2101613V#0103FThat was when I finally saw it for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101614V#6P#0001FCrossbell's barriers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101615V#5P#0108FYes. The same ones my father faced, and ones I'm\x01",
            "sure my grandfather faces, too.\x02\x03",
            "#2101616V#0100FDo you know who the leader of the Crossbell\x01",
            "State government is, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101617V#6P#0005FIsn't it Mayor MacDowell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101618V#5P#0104FWell, yes, but there's technically two people: the\x01",
            "Crossbell City Mayor and the Speaker of the Diet.\x02\x03",
            "#2101619VGrandfather and the Imperial Faction's Speaker\x01",
            "Hartmann jointly represent our government.\x02\x03",
            "#2101620VThat's how we operate, according to state law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101621V#6P#0006FSounds like I neglected some of my studies.\x02\x03",
            "#2101622V#0005FBut, wait. Why did Crossbell adopt such a\x01",
            "divided system in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101623V#5P#0103FThat's obvious.\x02\x03",
            "#2101624V#0101FIf two equal representatives continually hinder\x01",
            "things by butting heads, political reform is\x01",
            "nigh impossible.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#2101625V#6P#0011FNo way!\x02\x03",
            "#2101626V#0008FIs that really how things are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101627V#5P#0106FI'm afraid so. With two people on top, one side can\x01",
            "easily sabotage the other if they try to push some\x01",
            "sort of reform through.\x02\x03",
            "#2101628VThe fact that this happens is an ironic\x01",
            "inevitability, given Crossbell's founding.\x02\x03",
            "#2101629V#0108FSeventy years ago, Crossbell State was born from a\x01",
            "mutual agreement between Erebonia and Calvard...\x02\x03",
            "#2101630VIn fact, Crossbell's founders were none other than\x01",
            "Imperial and Republican lawyers.\x02\x03",
            "#2101631V#0103FSeeing the current state of Crossbell, I can't help\x01",
            "but think of it as a curse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101608V#6P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101633V#5P#0108FI was at a loss.\x02\x03",
            "#2101634VIf I were to continue into the world of politics,\x01",
            "that same curse would grab me by the neck and drag\x01",
            "me under, just like my father.\x02\x03",
            "#2101635V#0103FThat's why I decided on a new approach, one my\x01",
            "family hadn't yet tried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101636V#6P#0000FAnd that was the CPD?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101637V#5P#0104FYes. From there, I told myself I could observe\x01",
            "Crossbell's distortions without looking through\x01",
            "the muddied lens of politics.\x02\x03",
            "#2101638VI convinced myself that my experiences gained\x01",
            "here would be my weapon of choice on the day\x01",
            "I entered Crossbell's political arena...\x02\x03",
            "#2101639V#0108FThe reform that my father failed to achieve and\x01",
            "Grandfather is unable to pursue...\x02\x03",
            "#2101640V#0100FI thought that this new, unblemished perspective\x01",
            "could finally make it become a reality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101574V#6P#0000FI'm sure it can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101642V#5P#0108FPerhaps. But, in the back of my mind, I know that\x01",
            "joining the CPD might have only been an escape.\x02\x03",
            "#2101643V#0106FI knew that what happened today was inevitable.\x02\x03",
            "#2101644VBut still, the reality of things was even colder\x01",
            "and crueler than I had imagined.\x02\x03",
            "#2101645VWhen confronted with it...I was at a loss.\x02\x03",
            "#2101646V#0108FMaybe I'm incapable of doing anything on my\x01",
            "own, after all.\x02\x03",
            "#2101647VMaybe I'm just a broken little girl, abandoned by\x01",
            "her mother and father...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        "#2101603V#6P#0001F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        "#2101649V#6P#0004FSo what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101650V#0105F#5PHuh?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x11, 0x101, 400)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    OP_68(-21800, 2400, -18300, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#2101651V#12P#0000FYou really are a perfectionist, aren't you, Elie?\x02\x03",
            "#2101652V'Failure isn't an option. The only way forward is\x01",
            "to place everything on my shoulders here and now.'\x02\x03",
            "#2101653V...That's the way you've been thinking, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101654V#0101F#5P#40WTh-That's...not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101655V#12P#0006FLook. I agree. Today sucked. Being ridiculed,\x01",
            "having to hear that all of our efforts are in vain...\x02\x03",
            "#2101656V#0001FBut, think about it. Aren't those the things we\x01",
            "signed up for when we joined the SSS?\x02\x03",
            "#2101657V#0000FRemember, Elie... There may be barriers we\x01",
            "can't get over today, but that doesn't mean we\x01",
            "won't be able to get over them tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101658V#0105F#5P'Barriers we can't get over today'...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101659V#12P#0003FRight now, the one in front of us is the\x01",
            "threat letter case.\x02\x03",
            "#2101660V#0008FAnd even though the First Division has taken\x01",
            "control of the investigation from us...\x02\x03",
            "#2101661V#0001F...I say we continue investigating separately\x01",
            "from them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#2101662V#0101F#5PWh-What?!\x02\x03",
            "#2101663V#0108FBut there's nothing we can do about it, is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101664V#12P#0003FSure, the First Division may be phenomenal.\x02\x03",
            "#2101665VBut even so, it's obvious that they're stuck in a\x01",
            "cop's mindset, only adhering to traditional logic.\x02\x03",
            "#2101666V#0008FMaybe a new perspective is exactly what's\x01",
            "needed to crack this case.\x02\x03",
            "#2101667V#0000FAt least, that's how I feel about things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101668V#0105F#5PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101669V#12P#0004FJust like how you joined the CPD to gain\x01",
            "a new perspective on Crossbell, right?\x02\x03",
            "#2101670V#0000FShould we miraculously solve this case,\x01",
            "then...\x02\x03",
            "#2101671V...surely what you're aiming for isn't an\x01",
            "impossibility, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101672V#0105F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101673V#12P#0008FI'll admit that comparing our current investigation\x01",
            "to Crossbell's underlying issues is a bit of an\x01",
            "oversimplification.\x02\x03",
            "#2101674V#0003FBut what we need right now is the experience\x01",
            "of overcoming these kinds of obstacles.\x02\x03",
            "#2101675V#0000FThink about it. Clear the small barriers,\x01",
            "one by one...\x02\x03",
            "#2101676VIf we do that, then someday, we'll have the\x01",
            "power to get over the taller ones, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101576V#0108F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x5A, 0x12C)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#2101678V#0106F#5PIn these two months we've been together,\x01",
            "I've come to realize something.\x02\x03",
            "#2101679VYou have your own set of barriers you want to\x01",
            "overcome, don't you?\x02\x03",
            "#2101680V#0108FAnd if that's the case, how are you able to stay\x01",
            "so optimistic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101681V#12P#0005FWell, let's see...\x02\x03",
            "#2101682V#0000FMaybe it's because I have someone I'm trying to\x01",
            "catch up to.\x02\x03",
            "#2101683V#0012FThough, that in itself may present some issues...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101684V#0104F#5PI think I understand.\x02\x03",
            "#2101685V#0108FBut I'm not as strong as you are.\x02\x03",
            "#2101686VI'm just so...tired of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101687V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101688V#0106F#5P#30WI didn't come up here with the intention of\x01",
            "spilling everything about my past like I did.\x02\x03",
            "#2101689VI just couldn't keep it bottled up anymore.\x02\x03",
            "#2101690V#0108F#40WAt this rate, I'm only going to drag the team\x01",
            "down...\x02\x03",
            "#2101691VAnd if that's the case, I should probably--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101692V#12P#0004FElie.\x02",
    )

    CloseMessageWindow()

    def lambda_6FE3():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB7BC, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FE3)
    OP_68(-21800, 2300, -17700, 1300)
    MoveCamera(43, 15, 0, 1300)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x10)
    SetChrFlags(0x11, 0x2)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x11, 0x11)
    Fade(500)
    SetCameraDistance(14500, 500)
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x11, 0x12)
    Sleep(100)
    Sound(804, 0, 80, 0)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x11, 0x13)
    OP_0D()
    Sleep(300)

    def lambda_7070():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7070)
    WaitChrThread(0x11, 2)
    Sleep(500)

    ChrTalk(
        0x11,
        "#2101693V#0105F#5P#40W...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101694V#12P#0001FI... We need you, Elie.\x02\x03",
            "#2101695VYour profound knowledge, your negotiation skills,\x01",
            "your sharpshooting, your sense of justice...\x02\x03",
            "#2101696VIf we're going to stand up to this city, we're going\x01",
            "to need you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#2101697V#0108F#5P#40WB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101698V#12P#0004FLet me rephrase that.\x02\x03",
            "#2101699VWhile all of that's true, my point is this.\x02\x03",
            "#2101700V#0002FI'd be happy to have you by my\x01",
            "side, Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x11, 0x14)
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    SetChrSubChip(0x11, 0x15)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)

    ChrTalk(
        0x11,
        "#2101701V#0112F#5P#40WWh-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101702V#12P#0004FAll of us were a bit of a mess at the start, but\x01",
            "I think we've gotten pretty close over the past\x01",
            "two months.\x02\x03",
            "#2101703VEven when we're bombarded with the stress of daily\x01",
            "life, we make time for the small things, like\x01",
            "deciding whose turn it is to cook.\x02\x03",
            "#2101704V#0000FWe've come to place trust in each of each other's\x01",
            "individual strengths.\x02\x03",
            "#2101705VShouldn't we be grateful to have partners like that?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x8)
    SetChrSubChip(0x11, 0x18)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(500)

    ChrTalk(
        0x11,
        "#2101706V#0102F#5P#30WWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101707V#12P#0006FWe may still be rookies, sure.\x02\x03",
            "#2101708VIt's too early for us to underestimate Crossbell,\x01",
            "but it's also too early to let it beat us.\x02\x03",
            "#2101709V#0008FWe'll tackle each day head-on, do whatever we can,\x01",
            "and keep relentlessly confronting the status quo.\x02\x03",
            "#2101710V#0002FAnd if that somehow fails, we'll just come up with\x01",
            "a new plan.\x02\x03",
            "#2101711VNot just me, but Randy and Tio, too.\x02\x03",
            "#2101712VI've no doubt that the chief would do everything\x01",
            "in his power to help us out, as well.\x02\x03",
            "#2101713VHeck, even Zeit has our backs now.\x02\x03",
            "#2101714V#0009FBottom line: You're not alone, Elie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101715V#0112F#30W#5P...\x02\x03",
            "#2101716V#0104F#30WHeehee.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x6)
    SetChrSubChip(0x11, 0x16)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0x11, 0x17)
    Sleep(100)
    SetChrSubChip(0x101, 0x8)
    SetChrSubChip(0x11, 0x18)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#2101717V#0104F#5P#30WI'm not alone...?\x02\x03",
            "#2101718VYou're absolutely right.\x02\x03",
            "#2101719VI'm disappointed that I forgot something as\x01",
            "simple as that.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x101, 0x9)
    SetChrSubChip(0x11, 0x19)
    Sleep(120)
    SetChrSubChip(0x101, 0xA)
    SetChrSubChip(0x11, 0x1A)
    Sleep(120)
    SetChrSubChip(0x101, 0xB)
    SetChrSubChip(0x11, 0x1B)
    Sleep(120)
    SetChrSubChip(0x101, 0xC)
    SetChrSubChip(0x11, 0x1C)
    Sleep(120)
    SetChrSubChip(0x101, 0xD)
    SetChrSubChip(0x11, 0x1D)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#2101720V#0102F#5PThank you, Lloyd.\x02\x03",
            "#2101721VEven though it won't be easy to solve all my\x01",
            "problems...\x02\x03",
            "#2101722V#0109F...I do feel a little better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101552V#12P#0002FGlad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101724V#0113F#5P*sigh* Still...\x02\x03",
            "#2101725VApart from the lines that sounded like\x01",
            "they came straight out of a teen drama,\x01",
            "I was a bit surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101726V#12P#0006FUgh... I'm painfully aware of how cheesy\x01",
            "they were, okay?\x02\x03",
            "#2101727V#0005FBut what do you mean by surprised, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101728V#0113F#5PB-Because, well...\x02\x03",
            "#2101729VTalking about how I'm needed and telling\x01",
            "me that you want me by your side...\x02\x03",
            "#2101730VI thought you were confessing to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101731V#12P#0005FConfess...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(1087, 255, 100, 0)
    OP_68(-21800, 2400, -18300, 800)
    MoveCamera(37, 13, 0, 800)
    SetCameraDistance(15000, 800)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x11, 0x101, 0)
    Sound(804, 0, 100, 0)

    def lambda_7B7E():
        OP_96(0xFE, 0xFFFFAAD8, 0x514, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B7E)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#2101732V#12P#0011FW-Wait! Hold the phone! That wasn't my\x01",
            "intention at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101733V#0101F#5POh?\x02\x03",
            "#2101734VAre you implying I'm not worth confessing to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101735V#12P#0006FY-You know that's not it...\x02\x03",
            "#2101736V#0013FOh, come on! You're just teasing me now,\x01",
            "aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101737V#0104F#5PJust a small dose of payback.\x02\x03",
            "#2101738V#0102FYou should be a bit more self-aware, though.\x02\x03",
            "#2101739VHonestly, I don't know whether to call you a\x01",
            "natural smooth talker or an up-and-coming\x01",
            "womanizer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101740V#12P#0011FH-Hey! Hold on a second!\x02\x03",
            "#2101741VAre you still talking about me or did you\x01",
            "switch to Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101742V#0111F#5PYour denseness doesn't help your case\x01",
            "any, either.\x02\x03",
            "#2101743V#0113F*sigh* Good grief, Lloyd.\x02\x03",
            "#2101744V(I can't believe that words alone made me\x01",
            "get all flustered like that...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101578V#12P#0005FWhat'd you say? I missed that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101746V#0101F#5PN-Nothing.\x02\x03",
            "#2101747V#0106FI'm really sorry for leaving the chief's\x01",
            "report all up to you.\x02\x03",
            "#2101748V#0100FHave you come up with a plan about the\x01",
            "investigation yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#2101749V#12P#0006FNot yet.\x02\x03",
            "#2101750V#0000FRight now, the case hinges on figuring\x01",
            "out what Yin hopes to accomplish.\x02\x03",
            "#2101751VTomorrow, we can ask around and see if we\x01",
            "can't find some sort of lead based around that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#2101752V#0104F#5PThat's fine by me.\x02\x03",
            "#2101753V#0102FThanks to you, I have a feeling that I'll be\x01",
            "sleeping soundly tonight.\x02\x03",
            "#2101754VHow about we hold a meeting tomorrow morning,\x01",
            "after we get our much-needed rest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2101755V#12P#0002FSounds like a plan!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_END)), "loc_82A2")
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Elie learned \x07\x02",
            "[Star Blast 2]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_8341")

    label("loc_82A2")

    AddCraft(0x0, 0x14A)
    AddCraft(0x1, 0x14A)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Elie learned \x07\x02",
            "[Star Blast]\x07\x05",
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By spending 100 CP each, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_8341")

    OP_CA(0x1, 0xFF, 0x0)
    SetMapFlags(0x10000000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3E9A end

    def Function_23_8385(): pass

    label("Function_23_8385")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    def lambda_85C8():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_85C8)

    def lambda_85E2():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_85E2)

    def lambda_85FC():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_85FC)
    Sound(458, 0, 100, 0)

    def lambda_861D():
        OP_96(0xFE, 0x4E20, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_861D)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 15)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-16000, 2400, 17000, 0)
    MoveCamera(355, 35, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetCameraDistance(18500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 1)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_8385 end

    def Function_24_86FF(): pass

    label("Function_24_86FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    OP_68(-1000, 1500, 11000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_86FF end

    def Function_25_87F3(): pass

    label("Function_25_87F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28100.itc", 0x1E)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20500.itc", 0x20)
    LoadChrToIndex("chr/ch20800.itc", 0x21)
    LoadChrToIndex("chr/ch23600.itc", 0x22)
    SoundLoad(803)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(23, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    SetChrPos(0x0, -19000, -4200, -11700, 0)
    SetChrPos(0x1, -19000, -4200, -11700, 0)
    SetChrPos(0x2, -19000, -4200, -11700, 0)
    SetChrPos(0x3, -19000, -4200, -11700, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1B)
    OP_78(0x9, 0x1C)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x9, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1B, -23000, 0, -3000, 0)
    OP_D3(0x1B, 0x0, 0x15F90, 0x0, 0x0)
    OP_70(0x8, 0x0)
    SetChrPos(0x1C, 8000, 0, 3500, 0)
    OP_D3(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    OP_70(0x9, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_4B(0x1D, 0xFF)
    SetChrPos(0x1D, 5000, 0, -6300, 270)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -6800, 0, 4000, 270)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -8300, 0, 2500, 90)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    OP_4B(0x20, 0xFF)
    SetChrPos(0x20, -10300, 0, 10400, 0)
    SetChrChipByIndex(0x21, 0x22)
    SetChrSubChip(0x21, 0x0)
    OP_4B(0x21, 0xFF)
    SetChrPos(0x21, 0, 0, 15000, 315)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KThe same day, 8:45PM...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7516", 0)

    def lambda_8A71():
        OP_96(0xFE, 0xFFFFC568, 0x0, 0xFFFFE764, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8A71)

    def lambda_8A8B():
        OP_98(0xFE, 0xFFFFD508, 0x0, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8A8B)

    def lambda_8AA5():
        OP_9E(0xFE, 0x0, 0x1388, 0xFFFD40E0, 0x9C4, 0x1)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8AA5)
    OP_68(-1000, 1500, 11000, 5000)
    BeginChrThread(0x22, 1, 0, 26)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    EndChrThread(0x22, 0x1)
    OP_24(0x323)
    SetScenarioFlags(0x5C, 7)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_87F3 end

    def Function_26_8B4A(): pass

    label("Function_26_8B4A")

    Sound(803, 2, 80, 0)
    Sleep(5000)
    OP_25(0x323, 0x3C)
    Sleep(200)
    OP_25(0x323, 0x32)
    Sleep(200)
    OP_25(0x323, 0x28)
    Sleep(200)
    OP_25(0x323, 0x1E)
    Sleep(200)
    OP_25(0x323, 0x14)
    Sleep(200)
    OP_25(0x323, 0xA)
    Sleep(200)
    OP_24(0x323)
    Return()

    # Function_26_8B4A end

    def Function_27_8B81(): pass

    label("Function_27_8B81")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch31250.itc", 0x22)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch00150.itc", 0x26)
    LoadChrToIndex("chr/ch00151.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00251.itc", 0x29)
    LoadChrToIndex("chr/ch00950.itc", 0x2A)
    LoadChrToIndex("chr/ch00951.itc", 0x2B)
    OP_68(-21800, -1000, -2300, 0)
    MoveCamera(57, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_90(0x101, -33800, 0, -3300, 90)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, -35400, 0, -2300, 90)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    OP_90(0x103, -35600, 0, -4000, 90)
    OP_90(0x104, -33900, 0, -5000, 90)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    OP_90(0x10A, -37200, 0, -4600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    OP_90(0xE, -36400, 0, -5700, 90)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x20)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -37200, 0, -1600, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x13, 700, 0, -13500, 225)
    SetChrPos(0x14, 1700, 0, -14500, 225)
    SetChrPos(0x17, -600, 0, -16000, 270)
    SetChrPos(0x18, -600, 0, -17600, 270)
    SetChrPos(0x19, 1400, 0, -16800, 270)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_78(0x11, 0x1B)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    OP_49()
    SetChrPos(0x1B, 4000, 0, -11500, 0)
    OP_D3(0x1B, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x11, 0x1E)
    OP_70(0x11, 0x0)

    def lambda_8E47():
        OP_96(0xFE, 0xFFFFCA18, 0x0, 0xFFFFF31C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E47)
    Sleep(50)

    def lambda_8E64():
        OP_96(0xFE, 0xFFFFC9B4, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8E64)
    Sleep(100)

    def lambda_8E81():
        OP_96(0xFE, 0xFFFFC310, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8E81)
    Sleep(50)

    def lambda_8E9E():
        OP_96(0xFE, 0xFFFFC3D8, 0x0, 0xFFFFF704, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E9E)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 3, 0, 3)

    def lambda_8EDF():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFF9C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8EDF)
    Sleep(100)

    def lambda_8EFC():
        OP_96(0xFE, 0xFFFFBCD0, 0x0, 0xFFFFEE08, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8EFC)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_8F21():
        OP_96(0xFE, 0xFFFFBFF0, 0x0, 0xFFFFE9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8F21)
    OP_68(-13800, 0, -2300, 4000)
    MoveCamera(47, 25, 0, 4000)
    SetCameraDistance(19500, 4000)
    FadeToBright(2000, 0)
    BeginChrThread(0x22, 1, 0, 35)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    MoveCamera(40, 25, 0, 3000)
    OP_68(2280, 0, -11990, 3000)

    def lambda_9046():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9046)
    Sleep(50)

    def lambda_9056():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9056)
    Sleep(50)

    def lambda_9066():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9066)
    Sleep(50)

    def lambda_9076():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9076)
    Sleep(50)

    def lambda_9086():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9086)
    Sleep(50)

    def lambda_9096():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_9096)
    Sleep(50)

    def lambda_90A6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_90A6)
    OP_6F(0x41)
    Sleep(1000)
    Fade(500)
    OP_68(-13800, 0, -2300, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5200153V#5P#0010FCrap! What do we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200154V#5P#0107FWe can try cutting through the\x01",
            "Administrative District!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)

    ChrTalk(
        0x103,
        "#5200155V#6P#0207FNegative!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(12700, 900, 27800, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)

    def lambda_91E0():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_91E0)

    def lambda_91ED():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_91ED)

    def lambda_91FA():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_91FA)

    def lambda_9207():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9207)

    def lambda_9214():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9214)

    def lambda_9221():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_9221)
    SetChrPos(0x17, 11800, 0, 38800, 180)
    SetChrPos(0x18, 10900, 0, 40300, 180)
    SetChrPos(0x19, 12700, 0, 40600, 180)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x13, 11800, 0, 43800, 180)
    SetChrPos(0x14, 10900, 0, 45300, 180)
    SetChrPos(0x15, 12700, 0, 45600, 180)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_68(12700, 900, 21800, 4000)
    SetCameraDistance(18500, 4000)

    def lambda_92E8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_92E8)

    def lambda_9302():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9302)
    Sleep(50)

    def lambda_931F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_931F)

    def lambda_9339():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9339)
    Sleep(50)

    def lambda_9356():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9356)

    def lambda_9370():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9370)
    OP_6F(0x11)
    Sleep(1000)
    Fade(500)
    OP_68(-13800, 0, -2300, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_0D()
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x18, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_93(0x10A, 0x5A, 0x1F4)

    ChrTalk(
        0x10A,
        "#5200156V#6P#0607FThrough the Back Alley! Move!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#5200157V#11P#0007FGot it!\x02",
    )

    CloseMessageWindow()
    OP_68(-12500, 1000, 13000, 4000)
    MoveCamera(7, 20, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0x101, 3, 0, 28)
    BeginChrThread(0x104, 3, 0, 29)
    BeginChrThread(0x102, 3, 0, 30)
    BeginChrThread(0x103, 3, 0, 31)
    BeginChrThread(0x10A, 3, 0, 32)
    BeginChrThread(0xE, 3, 0, 33)
    BeginChrThread(0x12, 3, 0, 34)
    OP_6F(0x79)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0x12, 0xFF)
    SetScenarioFlags(0x5C, 2)
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_8B81 end

    def Function_28_94C1(): pass

    label("Function_28_94C1")

    OP_92(0x101, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_94D3():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94D3)
    WaitChrThread(0x101, 1)

    def lambda_94F1():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94F1)
    WaitChrThread(0x101, 1)
    Return()

    # Function_28_94C1 end

    def Function_29_950B(): pass

    label("Function_29_950B")

    Sleep(300)
    OP_92(0x104, 0xFFFFD314, 0x2EE0, 0x1F4)

    def lambda_9520():
        OP_95(0xFE, -11500, 0, 12000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9520)
    WaitChrThread(0x104, 1)

    def lambda_953E():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_953E)
    WaitChrThread(0x104, 1)
    Return()

    # Function_29_950B end

    def Function_30_9558(): pass

    label("Function_30_9558")

    Sleep(900)
    OP_92(0x102, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_956D():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_956D)
    WaitChrThread(0x102, 1)

    def lambda_958B():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_958B)
    WaitChrThread(0x102, 1)
    Return()

    # Function_30_9558 end

    def Function_31_95A5(): pass

    label("Function_31_95A5")

    Sleep(1200)
    OP_92(0x103, 0xFFFFCD9C, 0x2AF8, 0x1F4)

    def lambda_95BA():
        OP_95(0xFE, -12900, 0, 11000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_95BA)
    WaitChrThread(0x103, 1)

    def lambda_95D8():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_95D8)
    WaitChrThread(0x103, 1)
    Return()

    # Function_31_95A5 end

    def Function_32_95F2(): pass

    label("Function_32_95F2")

    Sleep(2500)

    def lambda_95FA():
        OP_95(0xFE, -12800, 0, 12000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_95FA)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(1500)
    OP_93(0x10A, 0x13B, 0x1F4)

    def lambda_9629():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9629)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_32_95F2 end

    def Function_33_9643(): pass

    label("Function_33_9643")

    Sleep(2000)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_9653():
        OP_95(0xFE, -11500, 0, 13300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9653)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0x5A, 0x1F4)
    Sound(531, 0, 100, 0)
    Sleep(1550)
    OP_93(0xE, 0x13B, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_9698():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9698)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_33_9643 end

    def Function_34_96BA(): pass

    label("Function_34_96BA")

    Sleep(3000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_96EC():
        OP_95(0xFE, -15300, 0, 8300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_96EC)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9730():
        OP_92(0xFE, 0xFFFFB690, 0x300C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9730)
    WaitChrThread(0x12, 2)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x2)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_9794():
        OP_9D(0xFE, 0xFFFFB690, 0x6A4, 0x300C, 0x898, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9794)
    Sleep(600)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)

    def lambda_97C3():
        OP_92(0xFE, 0xFFFFB690, 0x4F4C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_97C3)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_97E7():
        OP_9D(0xFE, 0xFFFFB690, 0x0, 0x4F4C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_97E7)
    Sleep(500)
    SetChrSubChip(0x12, 0x1)
    Sleep(50)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x3)
    Sleep(50)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_9829():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x3A98, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9829)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    Return()

    # Function_34_96BA end

    def Function_35_984B(): pass

    label("Function_35_984B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9864")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_35_984B")

    label("loc_9864")

    Return()

    # Function_35_984B end

    def Function_36_9865(): pass

    label("Function_36_9865")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch31252.itc", 0x22)
    LoadChrToIndex("chr/ch31251.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch00150.itc", 0x26)
    LoadChrToIndex("chr/ch00151.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00251.itc", 0x29)
    LoadChrToIndex("chr/ch00950.itc", 0x2A)
    LoadChrToIndex("chr/ch00951.itc", 0x2B)
    LoadChrToIndex("chr/ch00952.itc", 0x2C)
    LoadChrToIndex("apl/ch50509.itc", 0x2D)
    SetChrPos(0x101, 11300, 0, 35900, 180)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 12700, 0, 37800, 180)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 10600, 0, 36800, 180)
    SetChrPos(0x104, 12900, 0, 36300, 180)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 13100, 0, 39700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, 11500, 0, 39100, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 14800, 0, 38800, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x13, -2200, 0, -2600, 90)
    SetChrPos(0x17, -2100, 0, -4500, 90)
    SetChrPos(0x14, 0, 0, -12100, 45)
    SetChrPos(0x18, 400, 0, -13400, 45)
    SetChrPos(0x15, 11600, 500, 13800, 270)
    SetChrPos(0x16, 11600, 500, 13800, 270)
    SetChrPos(0x19, 14700, 0, 13800, 180)
    SetChrPos(0x1A, 11600, 500, 13800, 270)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_78(0x11, 0x1B)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x11, 0x4)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    OP_49()
    SetChrPos(0x1B, 12600, 0, 23500, 0)
    OP_D3(0x1B, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x12, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(0, 800, 4000, 0)
    MoveCamera(18, 22, 0, 0)
    OP_6E(860, 0)
    SetCameraDistance(28000, 0)

    def lambda_9B87():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B87)
    Sleep(50)

    def lambda_9BA4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BA4)
    Sleep(50)

    def lambda_9BC1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BC1)
    Sleep(50)

    def lambda_9BDE():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9BDE)
    Sleep(50)

    def lambda_9BFB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9BFB)
    Sleep(50)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)

    def lambda_9C20():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9C20)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)

    def lambda_9C4B():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF63C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_9C4B)
    MoveCamera(42, 22, 0, 9000)
    SetCameraDistance(33000, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x50)
    BeginChrThread(0x22, 1, 0, 35)
    Fade(500)
    OP_68(12700, 1000, -2200, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x22, 0x1)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x101,
        "#5200218V#5P#0006F*huff* *huff*\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#5200219V#6P#1105FYay! We're back!\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x13B, 0x2BC)
    Sleep(750)
    OP_93(0x103, 0xE1, 0x2BC)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#5200220V#5P#0202FThe Guardian Force appears to have\x01",
            "dispersed for now.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        "#5200221V#0302F#11PDid we shake 'em off, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xE, 500)

    ChrTalk(
        0x10A,
        "#5200222V#11P#0600FSergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200223V#5P#1003FRight.\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)
    OP_68(12400, 900, -1100, 1000)
    MoveCamera(45, 19, 0, 1000)
    SetCameraDistance(17000, 1000)
    OP_93(0x10A, 0xB4, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        (
            "#5200224V#1002F#5PListen up, everyone. From here on out, we're\x01",
            "splitting up.\x02\x03",
            "#5200225VTake East Street and get the hell\x01",
            "out of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9F49():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F49)
    Sleep(50)

    def lambda_9F59():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9F59)
    Sleep(50)

    def lambda_9F69():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9F69)
    Sleep(50)

    def lambda_9F79():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_9F79)
    OP_93(0x104, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#5200226V#12P#0005F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200227V#1003F#5PMost of the guardsmen running amok look like\x01",
            "they're from Bellguard Gate.\x02\x03",
            "#5200228VAnd if none of Sonya's subordinates are here,\x01",
            "we can assume that they're still sane.\x02\x03",
            "#5200229V#1001FAfter you reach the highway, contact Tangram\x01",
            "Gate and get them to come pick you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200230V#12P#0001FRoger. But, Chief, what about you two?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5200231V#1003F#5PDudley and I will stay here to throw 'em\x01",
            "off your track.\x02\x03",
            "#5200232V#1002FYou better believe I'll grab their attention\x01",
            "by the horns, all right.\x02",
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
        "#5200233V#12P#0007FWe can't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200234V#0307FWhat the hell is this, Chief?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200235V#5P#0604FRelax. For the two of us, pummeling\x01",
            "these ingrates and retreating will be\x01",
            "child's play.\x02\x03",
            "#5200236V#0607FNow, quit standing there like fools and\x01",
            "go! There's no time to waste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200237V#12P#0008FDudley...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#5200238V#5P#0101FLet's go!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#5200239V#1101F#11PChief! Be careful, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5200240V#1002F#5PWill do!\x02",
    )

    CloseMessageWindow()
    OP_68(15400, 900, -1100, 4000)

    def lambda_A3EA():

        label("loc_A3EA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A3EA")

    QueueWorkItem2(0xE, 2, lambda_A3EA)

    def lambda_A3FC():

        label("loc_A3FC")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A3FC")

    QueueWorkItem2(0x10A, 2, lambda_A3FC)
    BeginChrThread(0x104, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 38)
    BeginChrThread(0x12, 3, 0, 39)
    WaitChrThread(0x104, 3)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x10A, 0x2)
    OP_6F(0x1)
    EndChrThread(0x22, 0x1)
    Fade(1000)
    OP_68(10960, 900, 150, 0)
    MoveCamera(50, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_52(0x10A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MoveCamera(42, 11, 0, 8000)
    SetCameraDistance(16000, 8000)
    BeginChrThread(0x10A, 3, 0, 40)
    BeginChrThread(0xE, 3, 0, 41)
    BeginChrThread(0x1B, 3, 0, 37)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    BeginChrThread(0x13, 3, 0, 42)
    BeginChrThread(0x14, 3, 0, 43)
    BeginChrThread(0x15, 3, 0, 44)
    BeginChrThread(0x16, 3, 0, 45)
    BeginChrThread(0x17, 3, 0, 46)
    BeginChrThread(0x18, 3, 0, 47)
    BeginChrThread(0x19, 3, 0, 48)
    BeginChrThread(0x1A, 3, 0, 49)
    OP_6F(0x50)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1A, 3)

    ChrTalk(
        0xE,
        (
            "#5200241V#11P#1003FDudley.\x02\x03",
            "#5200242V#1002FTime to show this old fogey what the First\x01",
            "Division's ace detective is made of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200243V#0604F#5PHmph. Right back at you.\x02\x03",
            "#5200244V#0602FYou led those two in that legendary division,\x01",
            "didn't you? It's time to prove it, Sergei!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    RemoveParty(0x9, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_9865 end

    def Function_37_A6C6(): pass

    label("Function_37_A6C6")

    Sound(489, 0, 100, 0)
    ClearMapObjFlags(0x11, 0x4)

    def lambda_A6D7():
        OP_96(0xFE, 0x3138, 0x0, 0x34BC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A6D7)
    WaitChrThread(0x1B, 1)
    Sound(495, 0, 100, 0)
    SetMapObjFlags(0x11, 0x20)
    OP_71(0x11, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x11)
    OP_24(0x1E9)
    OP_71(0x11, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x11)
    Return()

    # Function_37_A6C6 end

    def Function_38_A724(): pass

    label("Function_38_A724")

    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_A730():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A730)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_A724 end

    def Function_39_A74A(): pass

    label("Function_39_A74A")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x22, 1, 0, 35)

    def lambda_A76A():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A76A)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0x12, 0x8)
    Return()

    # Function_39_A74A end

    def Function_40_A789(): pass

    label("Function_40_A789")

    Sleep(1500)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_A799():
        OP_95(0xFE, 11600, 0, 300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A799)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    SetChrChipByIndex(0x10A, 0x2A)
    SetChrSubChip(0x10A, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x10A, 0x2C)
    SetChrSubChip(0x10A, 0x0)
    Sound(531, 0, 100, 0)
    Return()

    # Function_40_A789 end

    def Function_41_A7D3(): pass

    label("Function_41_A7D3")

    Sleep(2500)
    OP_93(0xE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x3)
    Sleep(70)
    SetChrSubChip(0xE, 0x2)
    Sleep(70)
    SetChrSubChip(0xE, 0x1)
    Sleep(70)
    SetChrSubChip(0xE, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0xE, 0x1)
    Sleep(70)
    SetChrSubChip(0xE, 0x2)
    Sleep(70)
    SetChrSubChip(0xE, 0x3)
    Sleep(70)
    SetChrSubChip(0xE, 0x4)
    Return()

    # Function_41_A7D3 end

    def Function_42_A81D(): pass

    label("Function_42_A81D")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A82D():
        OP_96(0xFE, 0x12C0, 0x0, 0xFFFFF5D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A82D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_42_A81D end

    def Function_43_A863(): pass

    label("Function_43_A863")

    Sleep(3500)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A873():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFEA84, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A873)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_43_A863 end

    def Function_44_A8A9(): pass

    label("Function_44_A8A9")

    WaitChrThread(0x1B, 3)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A8BD():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A8BD)

    def lambda_A8D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A8D7)
    WaitChrThread(0xFE, 1)

    def lambda_A8EC():
        OP_95(0xFE, 8100, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A8EC)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_44_A8A9 end

    def Function_45_A929(): pass

    label("Function_45_A929")

    WaitChrThread(0x1B, 3)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A93A():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A93A)

    def lambda_A954():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A954)
    WaitChrThread(0xFE, 1)

    def lambda_A969():
        OP_95(0xFE, 9900, 0, 6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A969)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sound(531, 0, 100, 0)
    Return()

    # Function_45_A929 end

    def Function_46_A9A6(): pass

    label("Function_46_A9A6")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A9B6():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFEE6C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A9B6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_46_A9A6 end

    def Function_47_A9DE(): pass

    label("Function_47_A9DE")

    Sleep(3600)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_A9EE():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFE570, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A9EE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_47_A9DE end

    def Function_48_AA16(): pass

    label("Function_48_AA16")

    WaitChrThread(0x1B, 3)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_AA2A():
        OP_95(0xFE, 14700, 0, 8500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AA2A)

    def lambda_AA44():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AA44)
    WaitChrThread(0xFE, 1)

    def lambda_AA59():
        OP_95(0xFE, 13300, 0, 7100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AA59)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_48_AA16 end

    def Function_49_AA88(): pass

    label("Function_49_AA88")

    WaitChrThread(0x1B, 3)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)

    def lambda_AA9C():
        OP_95(0xFE, 10300, 0, 13800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AA9C)

    def lambda_AAB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AAB6)
    WaitChrThread(0xFE, 1)

    def lambda_AACB():
        OP_95(0xFE, 8900, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AACB)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_49_AA88 end

    def Function_50_AAFA(): pass

    label("Function_50_AAFA")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)
    Return()

    # Function_50_AAFA end

    def Function_51_AB16(): pass

    label("Function_51_AB16")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)
    Return()

    # Function_51_AB16 end

    def Function_52_AB32(): pass

    label("Function_52_AB32")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, 13060, 0, 27590, 180)
    EventEnd(0x4)
    Return()

    # Function_52_AB32 end

    def Function_53_AB4E(): pass

    label("Function_53_AB4E")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -26950, -1160, -4340, 90)
    EventEnd(0x4)
    Return()

    # Function_53_AB4E end

    def Function_54_AB6A(): pass

    label("Function_54_AB6A")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -270, 800, 22820, 180)
    EventEnd(0x4)
    Return()

    # Function_54_AB6A end

    def Function_55_AB86(): pass

    label("Function_55_AB86")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -21330, 0, 6200, 135)
    EventEnd(0x4)
    Return()

    # Function_55_AB86 end

    def Function_56_ABA2(): pass

    label("Function_56_ABA2")

    EventBegin(0x1)
    Call(0, 59)
    Sleep(50)
    SetChrPos(0x0, 14920, 0, 5200, 270)
    EventEnd(0x4)
    Return()

    # Function_56_ABA2 end

    def Function_57_ABBE(): pass

    label("Function_57_ABBE")

    EventBegin(0x1)
    Call(0, 58)
    Sleep(50)
    SetChrPos(0x0, -8420, -4200, -21200, 270)
    EventEnd(0x4)
    Return()

    # Function_57_ABBE end

    def Function_58_ABDA(): pass

    label("Function_58_ABDA")


    ChrTalk(
        0x101,
        (
            "#0000FIt's already night.\x02\x03",
            "KeA should be waiting for us back at\x01",
            "the SSS building. Come on, no detours.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACB4")

    ChrTalk(
        0x102,
        (
            "#0100FGood idea. Besides, we already finished\x01",
            "all of our required work for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD50")

    label("loc_ACB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD09")

    ChrTalk(
        0x103,
        (
            "#0200FCourse set for the Special Support Section\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD50")

    label("loc_AD09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AD50")

    ChrTalk(
        0x104,
        "#0300FAll righty! Let's go see KeDo's silly grin.\x02",
    )

    CloseMessageWindow()

    label("loc_AD50")

    Return()

    # Function_58_ABDA end

    def Function_59_AD51(): pass

    label("Function_59_AD51")


    ChrTalk(
        0x101,
        (
            "#0000FIt looks like Genten's closing up shop\x01",
            "for the night.\x02\x03",
            "Anyway, KeA should be waiting for us back\x01",
            "at the SSS building. Come on, no detours.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE55")

    ChrTalk(
        0x102,
        (
            "#0100FGood idea. Besides, we already finished\x01",
            "all of our required work for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEF1")

    label("loc_AE55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEAA")

    ChrTalk(
        0x103,
        (
            "#0200FCourse set for the Special Support Section\x01",
            "building.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEF1")

    label("loc_AEAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEF1")

    ChrTalk(
        0x104,
        "#0300FAll righty! Let's go see KeDo's silly grin.\x02",
    )

    CloseMessageWindow()

    label("loc_AEF1")

    Return()

    # Function_59_AD51 end

    SaveToFile()

Try(main)
