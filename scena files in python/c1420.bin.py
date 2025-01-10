from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1420.bin",                # FileName
        "c1420",                    # MapName
        "c1420",                    # Location
        0x002F,                     # MapIndex
        "ed7116",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 47, 0, 5, 0, 6],
    )

    BuildStringList((
        "c1420",                  # 0
        "Wald",                   # 1
        "Luganov",                # 2
        "Jed",                    # 3
        "Huey",                   # 4
        "Slash",                  # 5
        "Koki",                   # 6
        "Dino",                   # 7
        "Wald",                   # 8
        "Luganov",                # 9
        "Huey",                   # 10
        "ドラム缶",               # 11
        "叩かれたドラム缶",       # 12
        "bc1420",                 # 13
    ))

    ATBonus("ATBonus_94", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 12, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0002, 6, 6, 180, 0, 0, 0, 0, "bc1420", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02100.itc",                   # 00
        "apl/ch50018.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch30800.itc",                   # 03
        "chr/ch31700.itc",                   # 04
        "chr/ch30802.itc",                   # 05
        "chr/ch31702.itc",                   # 06
        "apl/ch50019.itc",                   # 07
    ))

    DeclNpc(16829,   1000,    -600,    315,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(17079,   1000,    -2579,   225,  261,  0x0, 0,   3,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(12189,   0,       -5269,   270,  261,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(18700,   4000,    -8210,   315,  261,  0x0, 0,   4,   0,   0,   2,   0,   20,  255,  0)
    DeclNpc(1779,    0,       -5260,   90,   261,  0x0, 0,   3,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   2,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(17600,   1100,    -180,    270,  261,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(14000,   699,     3279,    270,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(8250,    200,     -6360,   270,  389,  0x0, 0,   6,   0,   255, 255, 0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  13.130000114440918,    -0.0,                  0.0,                   16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.565000057220459,    0.0,                   -0.0,                  1.0])

    DeclActor(19430,   1000,    70,      1000,    20000,   2500,    -40,     0x007C, 0,  33, 0x0000)

    ScpFunction((
        "Function_0_3A4",          # 00, 0
        "Function_1_45C",          # 01, 1
        "Function_2_487",          # 02, 2
        "Function_3_4FC",          # 03, 3
        "Function_4_527",          # 04, 4
        "Function_5_552",          # 05, 5
        "Function_6_BBC",          # 06, 6
        "Function_7_C2D",          # 07, 7
        "Function_8_1458",         # 08, 8
        "Function_9_2CF6",         # 09, 9
        "Function_10_2ECB",        # 0A, 10
        "Function_11_33E5",        # 0B, 11
        "Function_12_3748",        # 0C, 12
        "Function_13_3830",        # 0D, 13
        "Function_14_3976",        # 0E, 14
        "Function_15_3ADE",        # 0F, 15
        "Function_16_47C0",        # 10, 16
        "Function_17_4924",        # 11, 17
        "Function_18_587C",        # 12, 18
        "Function_19_59C4",        # 13, 19
        "Function_20_5A3A",        # 14, 20
        "Function_21_6C6F",        # 15, 21
        "Function_22_6F2B",        # 16, 22
        "Function_23_6FEE",        # 17, 23
        "Function_24_705B",        # 18, 24
        "Function_25_73F3",        # 19, 25
        "Function_26_860D",        # 1A, 26
        "Function_27_875D",        # 1B, 27
        "Function_28_968E",        # 1C, 28
        "Function_29_9848",        # 1D, 29
        "Function_30_991F",        # 1E, 30
        "Function_31_9E3A",        # 1F, 31
        "Function_32_B973",        # 20, 32
        "Function_33_CF45",        # 21, 33
    ))


    def Function_0_3A4(): pass

    label("Function_0_3A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3E4"),
        (1, "loc_3F0"),
        (2, "loc_3FC"),
        (3, "loc_408"),
        (4, "loc_414"),
        (5, "loc_420"),
        (6, "loc_42C"),
        (SWITCH_DEFAULT, "loc_438"),
    )


    label("loc_3E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_3F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_3FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_408")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_414")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_420")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_42C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_438")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_444")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_444")

    label("loc_45B")

    Return()

    # Function_0_3A4 end

    def Function_1_45C(): pass

    label("Function_1_45C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_486")
    OP_94(0xFE, 0x38C2, 0xFFFFF1B4, 0x4902, 0xFFFFF984, 0x3E8)
    Sleep(300)
    Jump("Function_1_45C")

    label("loc_486")

    Return()

    # Function_1_45C end

    def Function_2_487(): pass

    label("Function_2_487")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FB")
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 20920, 4000, 760, 1000, 0x0)
    OP_93(0xFE, 0x10E, 0xC8)
    Sleep(2500)
    OP_95(0xFE, 20920, 4000, -8210, 1000, 0x0)
    OP_95(0xFE, 18700, 4000, -8210, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0xC8)
    Sleep(4500)
    Jump("Function_2_487")

    label("loc_4FB")

    Return()

    # Function_2_487 end

    def Function_3_4FC(): pass

    label("Function_3_4FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_526")
    OP_94(0xFE, 0x2DAA, 0xFFFFEF98, 0x2526, 0xFFFFDA8A, 0x3E8)
    Sleep(300)
    Jump("Function_3_4FC")

    label("loc_526")

    Return()

    # Function_3_4FC end

    def Function_4_527(): pass

    label("Function_4_527")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_551")
    OP_94(0xFE, 0x1266, 0xC94, 0x636, 0xFFFFF43E, 0x3E8)
    Sleep(300)
    Jump("Function_4_527")

    label("loc_551")

    Return()

    # Function_4_527 end

    def Function_5_552(): pass

    label("Function_5_552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_568")
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_577")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5C7")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 17200, 1000, 0, 45)
    SetChrPos(0xB, 10340, 0, -9190, 315)
    OP_93(0xD, 0xE1, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x7)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_BBB")

    label("loc_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_613")
    SetChrPos(0xD, 16360, 990, -40, 90)
    SetChrPos(0xB, 9090, 0, -4900, 315)
    SetChrPos(0xC, 8109, 0, -3920, 135)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BBB")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_65A")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 16180, 3180, -8260, 315)
    SetChrPos(0xE, 12190, 0, -5270, 270)
    OP_93(0xD, 0xE1, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_BBB")

    label("loc_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6C6")
    SetChrPos(0xA, 16360, 990, -40, 90)
    SetChrPos(0xB, 9090, 0, -4900, 315)
    SetChrPos(0xC, 8109, 0, -3920, 135)
    OP_93(0xD, 0x87, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_6C1")

    Jump("loc_BBB")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_739")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 8000, 0, -200, 270)
    SetChrPos(0xE, 6200, 0, -200, 90)
    SetChrPos(0xB, 11180, 0, -7240, 315)
    OP_93(0xC, 0x2D, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x10)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734")
    SetChrFlags(0xB, 0x10)

    label("loc_734")

    Jump("loc_BBB")

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_793")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 12600, 0, 4190, 135)
    SetChrPos(0xC, 7520, 0, -4660, 180)
    SetChrPos(0xD, 17920, 1000, 1070, 225)
    SetChrFlags(0xA, 0x10)
    Jump("loc_BBB")

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7F2")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x8, 11640, 0, 270, 270)
    SetChrPos(0xA, 10370, 0, 1010, 135)
    SetChrPos(0xC, 10260, 0, -800, 45)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_BBB")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_846")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 3640, 0, 2640, 225)
    SetChrPos(0xE, 17110, 1000, -40, 90)
    BeginChrThread(0xD, 0, 0, 4)
    Jump("loc_BBB")

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8A3")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xD, 9090, 0, -4900, 315)
    SetChrPos(0xE, 8109, 0, -3920, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89E")
    SetChrFlags(0xD, 0x10)

    label("loc_89E")

    Jump("loc_BBB")

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8ED")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xB, 5260, 0, -1000, 0)
    SetChrPos(0xC, 5260, 0, 600, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_BBB")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_944")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3840, 0, -200, 90)
    BeginChrThread(0xE, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93F")
    SetChrFlags(0xE, 0x10)

    label("loc_93F")

    Jump("loc_BBB")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9BB")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xA, 16390, 1000, 410, 135)
    SetChrPos(0x9, 16200, 1000, -1090, 45)
    SetChrPos(0xB, 5260, 0, -1000, 0)
    SetChrPos(0xC, 5260, 0, 600, 180)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_BBB")

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9F5")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 6170, 0, -890, 315)
    SetChrPos(0xD, 5200, 0, 80, 135)
    Jump("loc_BBB")

    label("loc_9F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A84")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 8290, 0, 10, 270)
    SetChrPos(0xB, 6500, 0, 10, 90)
    SetChrPos(0xC, 10490, 0, -7280, 315)
    SetChrPos(0xD, 3640, 0, 2640, 225)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0xD, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6D")
    SetChrFlags(0xA, 0x10)

    label("loc_A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F")
    SetChrFlags(0xB, 0x10)

    label("loc_A7F")

    Jump("loc_BBB")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_ABC")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 15960, 1000, 350, 135)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BBB")

    label("loc_ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_ACA")
    Jump("loc_BBB")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B5C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x9, 12600, 0, 3440, 315)
    SetChrPos(0xA, 11540, 0, 4580, 135)
    SetChrPos(0xD, 16360, 990, -40, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")
    SetChrFlags(0xD, 0x10)

    label("loc_B31")

    Jump("loc_B57")

    label("loc_B36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_B4D")
    SetChrFlags(0x9, 0x10)
    Jump("loc_B57")

    label("loc_B4D")

    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_B57")

    Jump("loc_BBB")

    label("loc_B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B74")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BBB")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B87")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_BBB")

    label("loc_B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B9F")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x10)
    Jump("loc_BBB")

    label("loc_B9F")

    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, 12540, 0, 2950, 225)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_BBB")

    Return()

    # Function_5_552 end

    def Function_6_BBC(): pass

    label("Function_6_BBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_BDB")

    label("loc_BD5")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_BDB")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_BEE")
    Jump("loc_C06")

    label("loc_BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_C06")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2C")
    OP_66(0x0, 0x1)

    label("loc_C2C")

    Return()

    # Function_6_BBC end

    def Function_7_C2D(): pass

    label("Function_7_C2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DE9")

    ChrTalk(
        0x8,
        (
            "#1601FDon't think you can come in here and screw\x01",
            "around just 'cause it's the Anniversary Festival.\x02\x03",
            "#1607FWhat the HELL do you think you were\x01",
            "doin' behind my seat?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FOh, nothing in particular.\x02\x03",
            "#0005F(I just want to know how that man\x01",
            "managed to stick the riddle back\x01",
            "here without Wald realizing...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou should consider following your\x01",
            "own advice. Please try to restrain\x01",
            "yourselves during the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1454")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E62")

    ChrTalk(
        0x8,
        "#1601FEveryone's a critic, eh? Well, screw you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Let's not overstay our welcome.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_E62")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x0, 750)
    Sleep(750)

    ChrTalk(
        0x8,
        (
            "#1600FHey, punks. Watch yourselves...\x02\x03",
            "#1607F...or are ya lookin' for a fight? 'Cause\x01",
            "I'll give ya one you won't ever forget!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FWhoa, let's calm down!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FWho pissed in your cereal, bud?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(If he's in this sour of a mood, maybe\x01",
            "we shouldn't stick around much longer.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I am certain Wazy is more than capable\x01",
            "of calming him down. Allow him to do it.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)

    label("loc_100F")

    Jump("loc_1454")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1025")
    Call(0, 12)
    Jump("loc_1454")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 2)), scpexpr(EXPR_END)), "loc_1148")

    ChrTalk(
        0x8,
        (
            "#1603FThose damn black suits sure love sneakin'\x01",
            "around where they don't belong...\x02\x03",
            "#1604FHah. Sucks for 'em, 'cause I've been sendin'\x01",
            "my boys out on patrols, too.\x02\x03",
            "#1602FIf I ever catch 'em settin' foot in the Downtown\x01",
            "District, I'll make 'em all my fleshy punchin' bags.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1454")

    label("loc_1148")


    ChrTalk(
        0x8,
        (
            "#1600FThose black suits have been creepin' me\x01",
            "the hell out lately.\x02\x03",
            "They're the reason I've been sendin' my\x01",
            "boys on regular patrols 'round our turf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FBlack suits? You talkin' about Revache?\x02\x03",
            "#0303FYeah, I guess they have been makin'\x01",
            "moves these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#1603FScrew them. Those cowards love\x01",
            "sneakin' around behind our backs\x01",
            "instead of facin' us like REAL men.\x02\x03",
            "#1602FSoon as we catch one of those snakes, they're\x01",
            "friggin' dead meat. Oh, I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FC'mon, Wald. Please don't escalate this into\x01",
            "something bigger than it needs to be, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FBut Lloyd, we can't turn a blind eye to all of\x01",
            "the larger crimes they've been committing.\x02\x03",
            "I'm sure the fight between the mafias will\x01",
            "only continue to escalate if it's already become\x01",
            "this fierce...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 2)

    label("loc_1454")

    TalkEnd(0xFE)
    Return()

    # Function_7_C2D end

    def Function_8_1458(): pass

    label("Function_8_1458")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14EC")
    Jump("loc_1536")

    label("loc_14EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_150C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1536")

    label("loc_150C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1536")

    label("loc_152C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1536")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_156C")
    Call(0, 9)
    Jump("loc_2CEE")

    label("loc_156C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_15DD")

    ChrTalk(
        0xF,
        (
            "#1601FAre you guys outta your goddamn minds?\x01",
            "Don't think you can just hang out here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E0")

    label("loc_15DD")

    Call(0, 11)

    label("loc_15E0")

    Jump("loc_2CEE")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_19DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_163D")

    ChrTalk(
        0xF,
        (
            "#1601FGet lost, or I'll use your heads as\x01",
            "batting practice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D5")

    label("loc_163D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_17EB")

    ChrTalk(
        0x101,
        (
            "#0001FWe heard about an internal dispute within\x01",
            "the Saber Vipers, Wald...\x02\x03",
            "Have things started to settle down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1600FA bunch of pigs like you have NO\x01",
            "reason to be sticking yer noses\x01",
            "in OUR business.\x02\x03",
            "#1601FGet lost, or I'll use your heads as\x01",
            "batting practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303F(Whew! Someone's in a dandy mood!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(I never thought I'd see the day where Wald\x01",
            "has trouble controlling his subordinates...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19D2")

    label("loc_17EB")


    ChrTalk(
        0x101,
        (
            "#0005F(Is it just me, or is everyone acting a\x01",
            "little...off today?)\x02\x03",
            "#0001FDid something happen to the Vipers, Wald?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1600FA bunch of pigs like you have NO\x01",
            "reason to be sticking yer noses\x01",
            "in OUR business.\x02\x03",
            "#1603FIt was just a stupid argument between\x01",
            "a couple of my boys.\x02\x03",
            "#1601FNow get lost, or I'll use your heads as\x01",
            "batting practice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305F(A throwdown within the Vipers, eh?\x01",
            "Didn't see that one comin'.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(Likewise. Wald usually rules them\x01",
            "with an iron fist.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D2")

    SetScenarioFlags(0x0, 0)

    label("loc_19D5")

    Jump("loc_2CEE")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A8A")

    ChrTalk(
        0xF,
        (
            "#1600FWatch yourselves, punks. You're on my\x01",
            "turf, and I don't like it one bit.\x02\x03",
            "Besides, you four have nothin' to do\x01",
            "with this. Go ahead and scram.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8D")

    label("loc_1A8A")

    Call(0, 13)

    label("loc_1A8D")

    Jump("loc_2CEE")

    label("loc_1A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B31")

    ChrTalk(
        0xF,
        (
            "#1600FTch...\x02\x03",
            "Whose turf do ya think this is?! Don't go\x01",
            "thinkin' you can just waltz in here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001F(He seems more angry than usual...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CEE")

    label("loc_1B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_END)), "loc_1CD8")
    SetChrSubChip(0xF, 0x0)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BDB")
    Jump("loc_1C25")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BFB")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C25")

    label("loc_1BFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C1B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C25")

    label("loc_1C1B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C25")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#1604FHeh. You look like you have guts.\x02\x03",
            "#1602FYou ain't too bad, shrimp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#1110FI'm no shrimp! I'm a girl, and my\x01",
            "name is KeA!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1CD8")

    Call(0, 10)

    label("loc_1CDB")

    Jump("loc_2CEE")

    label("loc_1CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CEE")
    Jump("loc_2CEE")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CFF")
    Call(0, 14)
    Jump("loc_2CEE")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(
        0xF,
        (
            "#1600FBunch of cops and government dogs have been\x01",
            "wanderin' around the Downtown District.\x02\x03",
            "They must have balls of steel if they think they\x01",
            "can look down on us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF5")

    label("loc_1DBC")


    ChrTalk(
        0xF,
        (
            "#1603FYou again?\x02\x03",
            "#1600FDon't start thinkin' you can just show\x01",
            "up on my turf unannounced like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FDid you wake up on the wrong side of the bed,\x01",
            "or is your foul mood justified?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1603FEverything sucks. There's been all sorts of cops\x01",
            "and government dogs runnin' around the area\x01",
            "claimin' they gotta get ready for the festival.\x02\x03",
            "#1601FScrew those assholes! I'm about ready to\x01",
            "kick all of 'em outta here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FI feel ya, dude. We've been gettin' way too\x01",
            "many damn support requests, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAll we can do is grit our teeth and\x01",
            "bear it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FF5")

    Jump("loc_2CEE")

    label("loc_1FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_233F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2184")

    ChrTalk(
        0xF,
        (
            "#1601FAre you comparin' the two of us?\x02\x03",
            "#1607FKeep lettin' that big head of yours grow,\x01",
            "and I'll have to smash it to bits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001FWald, we were just trying to--\x01",
            "(Actually, on second thought... Showing\x01",
            "him sympathy might damage his pride.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(He does seem to be getting angrier\x01",
            "and angrier. Perhaps overstaying our\x01",
            "welcome is not the brightest idea.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_233A")

    label("loc_2184")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2232")

    ChrTalk(
        0xF,
        "#1600FHey, go buy somethin' for me.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "You're sending me out on an\x01",
            "errand already?!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xD)

    ChrTalk(
        0xD,
        "Y-Yes, sir! I'll be right back!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_2232")


    ChrTalk(
        0xF,
        "#1600FYo, Koki. You feelin' okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah, I'm totally fine! Sorry for\x01",
            "making you guys worry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1600FThink you said you were goin' down\x01",
            "to the hospital tomorrow, yeah?\x02\x03",
            "Better not do anythin' dumb before\x01",
            "you recover. You hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Will do, sir!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2336")

    OP_4C(0xD, 0xFF)

    label("loc_233A")

    Jump("loc_2CEE")

    label("loc_233F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23E5")

    ChrTalk(
        0xF,
        (
            "#1600FKoki's been havin' to visit the hospital\x01",
            "for a while 'cause of that incident.\x02\x03",
            "#1601FThose mobsters are so damn full\x01",
            "of themselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2492")

    label("loc_23E5")


    ChrTalk(
        0xF,
        (
            "#1600FKoki was discharged from the hospital,\x01",
            "but he's still goin' back there for regular\x01",
            "check-ups.\x02\x03",
            "#1601FScrew those guys.\x02\x03",
            "Revache must think they're hot shit...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2492")

    Jump("loc_2CEE")

    label("loc_2497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2572")

    ChrTalk(
        0xF,
        (
            "#1600FThis ain't over yet. I still got a score\x01",
            "to settle.\x02\x03",
            "#1601FIf they try to pull anythin' else, I'll personally\x01",
            "tear each and every one of 'em apart.\x01",
            "You four punks better remember that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_282D")

    label("loc_2572")


    ChrTalk(
        0xF,
        "#1600FOh, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHuh. It doesn't seem like you're in\x01",
            "a bad mood today, Wald.\x02\x03",
            "Oh, and by the way... Thanks for\x01",
            "cooperating with us back then.\x01",
            "You really helped us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYour underling that got sent to the hospital's\x01",
            "already back, yeah? That's some awesome\x01",
            "news, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1603FYeah, but I still haven't settled the score\x01",
            "with those Revache punks yet.\x02\x03",
            "Only reason I didn't murder 'em was 'cause\x01",
            "I went along with you and Wazy.\x02\x03",
            "#1600FThe next time I see those goddamned\x01",
            "assholes on my turf...\x02\x03",
            "#1601FI'll beat 'em to a bloody pulp. Somebody's\x01",
            "gotta knock some sense into 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FHow unnecessarily violent of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FNot very cool-headed, is he?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_282D")

    Jump("loc_2CEE")

    label("loc_2832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_29D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28E6")

    ChrTalk(
        0xF,
        (
            "#1600FI'll pay back each and every one of those\x01",
            "Testaments for what they did.\x02\x03",
            "#1601FDon't even think about gettin' in my way\x01",
            "either, or I'll crush ya!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D3")

    label("loc_28E6")


    ChrTalk(
        0xF,
        (
            "#1600FThose hooded freaks were hangin' around\x01",
            "our turf again, were they?\x02\x03",
            "#1603F...I'll pay back each and every one of those\x01",
            "Testaments for what they did.\x02\x03",
            "#1601FDon't even think about gettin' in my way\x01",
            "either, or I'll crush ya!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_29D3")

    Jump("loc_2CEE")

    label("loc_29D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2AA2")

    ChrTalk(
        0xF,
        (
            "#1600FI don't give a damn about how your dumb\x01",
            "investigation turns out.\x02\x03",
            "#1602FHaha. Not much longer till it starts\x01",
            "rainin' blood 'round these parts, so\x01",
            "ya better strap yourselves in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CEE")

    label("loc_2AA2")


    ChrTalk(
        0xF,
        (
            "#1600FJust gotta scratch that itch to rampage,\x01",
            "y'know?\x02\x03",
            "I don't give a damn about how your dumb\x01",
            "investigation turns out.\x02\x03",
            "#1602FHaha. Not much longer till it starts\x01",
            "rainin' blood 'round these parts, so\x01",
            "ya better strap yourselves in.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEB")

    ChrTalk(
        0xF,
        (
            "#1603F...Oh, yeah.\x02\x03",
            "#1601FHey, ladies. How long ya plannin' to\x01",
            "stick around the Downtown District?\x02\x03",
            "#1602FIf ya like hangin' around the area so much,\x01",
            "then ya'd better be prepared to deal with\x01",
            "any thugs that come your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F(What a heavy-handed statement.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(I guess that's his own special way\x01",
            "of warning us?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 4)

    label("loc_2CEB")

    SetScenarioFlags(0x0, 0)

    label("loc_2CEE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_1458 end

    def Function_9_2CF6(): pass

    label("Function_9_2CF6")

    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrSubChip(0xF, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xD,
        "S-Sorry, Wald!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We've looked everywhere, but\x01",
            "we can't find Dino!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1601FDamn it all...\x02\x03",
            "#1603F...The hell is that friggin' idiot doin'?\x02\x03",
            "#1601FSurely he didn't run off and do somethin'\x01",
            "stupid, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBF")

    ChrTalk(
        0x10A,
        (
            "#0600F(I haven't seen Wald Wales in quite some time,\x01",
            "but I get the impression he's changed a bit.)\x02\x03",
            "#0603F(At the very least, he takes better care of his\x01",
            "subordinates than he did back then...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2EBF")

    OP_64(0xD)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_2CF6 end

    def Function_10_2ECB(): pass

    label("Function_10_2ECB")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(17000, 2000, -290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 15520, 990, -630, 90)
    SetChrPos(0xEF, 15520, 990, 320, 90)
    SetChrPos(0x153, 16170, 1000, -1660, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    ChrTalk(
        0xF,
        (
            "#1600FThe cops, eh?\x02\x03",
            "#1602FHey, punk. You up for a fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWhy do you always have to be so hostile?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3033")

    ChrTalk(
        0x102,
        (
            "#0100FBut anyway, are you having a party?\x01",
            "You know the festival ended not that\x01",
            "long ago, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310C")

    label("loc_3033")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3095")

    ChrTalk(
        0x103,
        (
            "#0200FI see an excessive amount of alcohol.\x01",
            "Are you engaged in a party?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_310C")

    label("loc_3095")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_310C")

    ChrTalk(
        0x104,
        (
            "#0306FYo. You throwin' a party? Looks like\x01",
            "somebody wanted to keep that festive\x01",
            "spirit alive, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310C")

    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x153)

    ChrTalk(
        0x153,
        (
            "#1111F*stare*\x02\x03",
            "#1110FHey, Lloyd. Are you friends with this guy?\x02\x03",
            "#1109FHis hair looks like a chicken! Ahahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FHey, KeA! You can't just yell that out!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x153, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3263")
    Jump("loc_32AD")

    label("loc_3263")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3283")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32AD")

    label("loc_3283")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32A3")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32AD")

    label("loc_32A3")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32AD")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#1609FHahaha! You sure got some guts, kid.\x02\x03",
            "#1602FListen up, kid. My hair ain't just some\x01",
            "ordinary chicken.\x02\x03",
            "#1607FIt's the almighty phoenix!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1110FO...kay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(If you're so proud of your hair, then\x01",
            "why didn't you name your gang the\x01",
            "Saber Phoenixes?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 5)
    EventEnd(0x5)
    Return()

    # Function_10_2ECB end

    def Function_11_33E5(): pass

    label("Function_11_33E5")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xF, 0xFF)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x101, 11500, 0, -750, 90)
    SetChrPos(0x102, 11500, 0, 750, 90)
    SetChrPos(0x103, 10000, 0, -750, 90)
    SetChrPos(0x104, 10000, 0, 750, 90)
    FadeToBright(1000, 0)
    OP_68(16940, 2500, -170, 3000)
    MoveCamera(45, 30, 0, 3000)
    SetCameraDistance(14000, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#1603FHe's nowhere to be found? Wanna run that\x01",
            "by me again?\x02\x03",
            "#1601F'Cause if I remember correctly, I ORDERED\x01",
            "you to bring him to me. Need your ears\x01",
            "cleaned or somethin'?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Y-Yeah, about that... Apparently, Dino never\x01",
            "made it home...\x02",
        )
    )

    CloseMessageWindow()
    Fade(200)
    SetChrChipByIndex(0xF, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 17200, 1000, -180, 270)
    Sound(819, 0, 100, 0)
    Sleep(500)
    OP_82(0xC8, 0x0, 0x1388, 0x1F4)

    ChrTalk(
        0xF,
        "#1607F#4S#11PThen start lookin' for him, ya dumbass!\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_98(0xD, 0xFFFFFF38, 0x0, 0x0, 0x1F4, 0x0)

    ChrTalk(
        0xD,
        "S-Sure thing, boss!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xF, 0x1)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 17600, 1100, -180, 270)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_64(0xD)
    Fade(500)
    OP_68(10750, 1250, 0, 0)
    MoveCamera(46, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#0008F#6P(Dino? Is he the one that's on\x01",
            "the First Division's list?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301F#6P(I dunno, but it sounds like he might\x01",
            "be missing, too.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 11500, 0, 0, 90)
    SetChrPos(0xD, 16360, 990, -40, 90)
    OP_4C(0xF, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xCD, 4)
    EventEnd(0x5)
    Return()

    # Function_11_33E5 end

    def Function_12_3748(): pass

    label("Function_12_3748")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "#1602FHeh. Time to end this thing with a bang...\x02\x03",
            "Ya find a good place yet, Jed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Almost! Huey's checkin' out a few\x01",
            "places right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm thinkin' the Times' rooftop's\x01",
            "lookin' pretty good.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_12_3748 end

    def Function_13_3830(): pass

    label("Function_13_3830")

    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    SetChrSubChip(0xF, 0x0)

    ChrTalk(
        0xF,
        "#1600FJed. Go to the hospital. Now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Nah. I'm good, boss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The doctors seein' me like this\x01",
            "would be an embarrassment to\x01",
            "the Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#1601FDon't make me repeat myself, ya dumbass.\x01",
            "Get your ass to the hospital, or I'll send you\x01",
            "there on a stretcher myself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...Sorry. I'll go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_13_3830 end

    def Function_14_3976(): pass

    label("Function_14_3976")

    SetChrSubChip(0xF, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xF,
        (
            "#1604FYesterday was pretty lively, eh?\x02\x03",
            "#1602FThinkin' about hittin' up another place\x01",
            "today, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, hell yeah! I'll tag along, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Gahaha! We're goin' balls to\x01",
            "the walls again!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD1")

    ChrTalk(
        0x102,
        "#0106F(I've got a bad feeling about this...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Agreed. Can't they go one day without\x01",
            "causing an uproar?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3AD1")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_3976 end

    def Function_15_3ADE(): pass

    label("Function_15_3ADE")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3B70")

    ChrTalk(
        0x9,
        (
            "This sucks. Wald told us to keep\x01",
            "it down for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm so friggin' BOOORED! I just\x01",
            "wanna get up and sing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_3B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3BF4")

    ChrTalk(
        0x9,
        (
            "#4SWhoooaaaaaoooooooh! Gonna join in\x01",
            "on the fiiiiiight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Gonna beatcha down, beatcha dooown!\x01",
            "Just waaaaatch!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_3BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3CC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3C3F")

    ChrTalk(
        0x9,
        (
            "Not much Wald can do about a\x01",
            "one-on-one fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CC2")

    label("loc_3C3F")


    ChrTalk(
        0x9,
        (
            "If both people wanna throw down,\x01",
            "then who's to stop them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The Saber Vipers are all about the\x01",
            "survival of the fittest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3CC2")

    Jump("loc_47B1")

    label("loc_3CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3D6A")

    ChrTalk(
        0x9,
        "#4SGo, go, gooooooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Unbelievable! It's unbeeeleeevable!\x01",
            "Jed's down for the count, yeah, yeah!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "A fight's a fight, and that's finaaal!\x02",
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_3D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3DD9")

    ChrTalk(
        0x9,
        "Hey, what the hell's up with these bad vibes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ooh, ooh! I got just the thing! Singing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EE9")

    ChrTalk(
        0x9,
        "Okay, check this out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Festivaaaaaaals are the beeeeest!\x01",
            "Lemme eat...some cotton can-DYYYYYY!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006F(Was that supposed to be a song?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4010")

    label("loc_3EE9")


    ChrTalk(
        0x9,
        "#4SH-Hey! Waaaait! I'm not done singin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "The festival's endin' todaaaaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Dude! I should totally make a new\x01",
            "festive song to cap it off!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#0200FAre you not too late already?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4010")

    Jump("loc_47B1")

    label("loc_4015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4026")
    Call(0, 14)
    Jump("loc_47B1")

    label("loc_4026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_40B5")

    ChrTalk(
        0x9,
        "#4S...WOOOHOOOOO! Yeah, yeeeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "All my guys, beat 'em down, beat 'em down!\x01",
            "Leave 'em to me, guys! They're just clowns!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_40B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_419C")

    ChrTalk(
        0x9,
        "What? Get outta my way, dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm testing out the mic today. Wanna taste\x01",
            "of this bad boy?\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x9,
        (
            "Hey, hey, hey, hey, HEY!\x01",
            "Hey, hey, hey, hey, HEY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4S...Oooohooo! Heeeeey! I'm feeling it today!\x02",
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_419C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_42BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4232")

    ChrTalk(
        0x9,
        (
            "Oh, oh, yeah, yeah! ...Huh? Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wald's pretty pissed today, so you might\x01",
            "wanna leave him alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B5")

    label("loc_4232")

    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Oh, come on, Jed. Can't we\x01",
            "just have the meeting later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh, yeah! Uh, oh, yeah! Get ready for\x01",
            "a killer new song!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_42B5")

    Jump("loc_47B1")

    label("loc_42BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_433F")

    ChrTalk(
        0x9,
        "#4SYeah, yeah, yeah, YEEEEAAAH!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Eyes on me, getcho' eyes on me! I'm\x01",
            "hungry like a beast, so you better flee!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_433F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_458A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43DB")

    ChrTalk(
        0x9,
        (
            "You ×××× home, pal. You finally ××××.\x01",
            "Buddy, we ×××× ya. Ain't ×××× whack!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#4SYeeeeeaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4585")

    label("loc_43DB")


    ChrTalk(
        0x9,
        (
            "You ×××× home, pal. You finally ××××.\x01",
            "Buddy, we ×××× ya. Ain't ×××× whack!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#4SYEEEEEAAAAAH!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Ugh. I wish he'd turn the mic down a bit.\x01",
            "It doesn't help that his lyrics are totally\x01",
            "incomprehensible, either.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(I believe this is...to celebrate the return\x01",
            "of his friend from St. Ursula...? Possibly?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(A-Are you familiar with this type\x01",
            "of music, Tio?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4585")

    Jump("loc_47B1")

    label("loc_458A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_460C")

    ChrTalk(
        0x9,
        "#4SHey, hey, yeeeaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A hundred times over, a hundred times again...\x01",
            "Time to return the favor, y'dig?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_460C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_46A5")

    ChrTalk(
        0x9,
        (
            "I'mma crush those hooded Testaments\x01",
            "jerkwads if they do anythin' cowardly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't let our little chat get to your heads,\x01",
            "ya dogs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B1")

    label("loc_46A5")


    ChrTalk(
        0x9,
        (
            "The only guys dumb enough to take us on\x01",
            "around here are the Testaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not like I give a damn, though. They're\x01",
            "gonna bite the dust soon enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Get off your high horses, ya punks.\x01",
            "We can always turn you into our\x01",
            "punchin' bags if ya step outta line.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_47B1")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_15_3ADE end

    def Function_16_47C0(): pass

    label("Function_16_47C0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4854")
    Jump("loc_489E")

    label("loc_4854")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4874")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_489E")

    label("loc_4874")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4894")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_489E")

    label("loc_4894")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_489E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0x10,
        "Aaaaah! That's the stuff!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If yer not drinkin' scotch, then yer\x01",
            "doin' it WRONG!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_47C0 end

    def Function_17_4924(): pass

    label("Function_17_4924")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_499D")

    ChrTalk(
        0xFE,
        "The cops, eh? This is our turf. Scram.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Or are ya hungry for one of Wald's\x01",
            "knuckle sandwiches?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5878")

    label("loc_499D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A22")

    ChrTalk(
        0xA,
        (
            "Screw Dino. I'm gonna kick his ass\x01",
            "when I find him.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#4SGet outta here! No cops allowed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5878")

    label("loc_4A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A65")

    ChrTalk(
        0xA,
        "While I was gone, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "That sonuvabitch!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5878")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4AB6")

    ChrTalk(
        0xA,
        (
            "I don't want yer stinkin' paws around\x01",
            "here, ya dogs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB9")

    label("loc_4AB6")

    Call(0, 13)

    label("loc_4AB9")

    Jump("loc_5878")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4B43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4B3B")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xA,
        (
            "Guess Wald's the only one who can\x01",
            "decide... Damn it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#4SStop bein' cocky, ya moron!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    Jump("loc_4B3E")

    label("loc_4B3B")

    Call(0, 18)

    label("loc_4B3E")

    Jump("loc_5878")

    label("loc_4B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4BCA")
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "Those hooded asswipes have been runnin'\x01",
            "free rein for two years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Heh. Not for much longer, though.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_5878")

    label("loc_4BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4BDB")
    Call(0, 12)
    Jump("loc_5878")

    label("loc_4BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4BEC")
    Call(0, 14)
    Jump("loc_5878")

    label("loc_4BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_4C8B")

    ChrTalk(
        0xA,
        (
            "Those blue bastards are gonna get what's\x01",
            "coming to 'em...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just like Wald said. We're gonna settle\x01",
            "the score with 'em one day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C8E")

    label("loc_4C8B")

    Call(0, 19)

    label("loc_4C8E")

    Jump("loc_5878")

    label("loc_4C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4EE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 7)), scpexpr(EXPR_END)), "loc_4D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4CF8")

    ChrTalk(
        0xA,
        (
            "Hey, get outta the way! We're tryin'\x01",
            "to train here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D51")

    label("loc_4CF8")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "#4SC'mon! One more!\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xB,
        "Y-Yeah! Take this!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_64(0xB)
    OP_4C(0xB, 0xFF)

    label("loc_4D51")

    Jump("loc_4D67")

    label("loc_4D56")

    TurnDirection(0xA, 0x0, 0)
    Call(0, 19)
    OP_93(0xA, 0x10E, 0x0)

    label("loc_4D67")

    Jump("loc_4EE4")

    label("loc_4D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4E44")

    ChrTalk(
        0xA,
        (
            "Today's a big day, so Wald told us to\x01",
            "get some mornin' training in to prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Slash and Huey have been dog-tired lately.\x01",
            "As soon as we finish trainin', the two of 'em\x01",
            "are down for the count.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EE4")

    label("loc_4E44")

    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        "Put your heart into it, Huey! C'mon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Remember how ya got yer ass handed\x01",
            "to ya by those blue bastards?! C'mon,\x01",
            "ya gotta get motivated!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xB, 0xFF)

    label("loc_4EE4")

    Jump("loc_5878")

    label("loc_4EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4F4E")

    ChrTalk(
        0xA,
        "Comin' all close to our turf like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I never liked 'em anyway.\x02",
    )

    CloseMessageWindow()
    Jump("loc_500B")

    label("loc_4F4E")


    ChrTalk(
        0xA,
        (
            "Been seein' that black van comin'\x01",
            "into the area these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Screw those guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Don't think they're tryin' to claim the downtown\x01",
            "for themselves, but I still don't like 'em.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_500B")

    Jump("loc_5878")

    label("loc_5010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_51EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_50B5")

    ChrTalk(
        0xA,
        "I used to be an orphan before I came here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Any mention of government officials, police,\x01",
            "and all you other dogs makes me wanna puke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51EA")

    label("loc_50B5")


    ChrTalk(
        0xA,
        (
            "When ya think about it, neither the government\x01",
            "nor the police do jack to help anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Look at this dump. They don't give a\x01",
            "rat's ass about the Downtown District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "But still, you guys keep stickin' your noses\x01",
            "around here whenever ya feel like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ugh. No one likes you, okay? Just leave.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_51EA")

    Jump("loc_5878")

    label("loc_51EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_546E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5336")

    ChrTalk(
        0xA,
        (
            "If you think we'll just forgive you for what\x01",
            "you did to Wald, you better think again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I won't hesitate to wring you punks out\x01",
            "at the first chance I get!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5331")

    ChrTalk(
        0x104,
        (
            "#0306FI think you're blowin' this a little outta\x01",
            "proportion, man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0103F(They're as intense as ever, aren't they?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5331")

    Jump("loc_5469")

    label("loc_5336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53C5")

    ChrTalk(
        0xA,
        "The cops? The hell are you doin' here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Quit bein' so loud. You're jackin' up\x01",
            "our team meeting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5469")

    label("loc_53C5")

    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xA,
        (
            "What's up with Slash and Huey?\x01",
            "They're totally outta steam these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Guess that calls for more training.\x01",
            "Can't have anyone outta shape, can we?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)

    label("loc_5469")

    Jump("loc_5878")

    label("loc_546E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5508")

    ChrTalk(
        0xA,
        (
            "The Downtown District's our turf, got it?\x01",
            "We won't let your ego run loose here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "And that goes double for the Testaments.\x02",
    )

    CloseMessageWindow()
    Jump("loc_560E")

    label("loc_5508")


    ChrTalk(
        0xA,
        (
            "We see those jackasses from the government\x01",
            "around here sometimes, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "They say it's for a 'redevelopment survey.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Heh. Bunch of dumbasses. We sent them\x01",
            "packin' real quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Damn suits. They can piss off outta here\x01",
            "and go straight to hell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_560E")

    Jump("loc_5878")

    label("loc_5613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_576E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5665")

    ChrTalk(
        0xA,
        (
            "I can't believe the mafia was behind\x01",
            "all that crap...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5769")

    label("loc_5665")


    ChrTalk(
        0xA,
        "Damn it! How'd we fall for their trap?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Man, I screwed up real bad.\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hah! You've got another thing comin' if\x01",
            "you think I'm gonna thank you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Why would I thank a bunch of cops\x01",
            "for doin' their damn jobs for once?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5769")

    Jump("loc_5878")

    label("loc_576E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5801")

    ChrTalk(
        0xA,
        (
            "Those rotten blue bastards... Prepare\x01",
            "yourselves while you still can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You'll wish you never laid\x01",
            "yer filthy hands on Koki!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5878")

    label("loc_5801")


    ChrTalk(
        0xA,
        "We don't like talkin' to a bunch of dogs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The four of ya are a bunch of incompetent\x01",
            "pups, anyway. Now scram!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5878")

    TalkEnd(0xFE)
    Return()

    # Function_17_4924 end

    def Function_18_587C(): pass

    label("Function_18_587C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xA,
        "Don't go pushin' your luck, Dino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yer still a total newbie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "What's got your panties in a bunch? All I said\x01",
            "was that I was bored of bein' a guard dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Lemme in on your training sessions, Jed.\x01",
            "I need to see some action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(Is it just me, or is this guy\x01",
            "totally playing with fire?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_18_587C end

    def Function_19_59C4(): pass

    label("Function_19_59C4")


    ChrTalk(
        0xA,
        (
            "Fine. Time to crank up the intensity\x01",
            "of our training from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Talk shit, get hit. That simple.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 7)
    Return()

    # Function_19_59C4 end

    def Function_20_5A3A(): pass

    label("Function_20_5A3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A73")

    ChrTalk(
        0xB,
        "Where'd that damn kid run off to?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C6B")

    label("loc_5A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5B00")

    ChrTalk(
        0xB,
        "Dino didn't show his face again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hah. 'Course he didn't. He totally doesn't\x01",
            "have the balls to c'mere again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB0")

    label("loc_5B00")


    ChrTalk(
        0xB,
        (
            "Dino ran outta here cacklin'\x01",
            "like a freak...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "And of course, he didn't show up today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Fine, then. We'll beat the tar outta\x01",
            "that punk the next time we see him!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5BB0")

    Jump("loc_6C6B")

    label("loc_5BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5C68")

    ChrTalk(
        0xB,
        (
            "That little punk thinks he can just\x01",
            "take Jed's position like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Damn it all! I wish Wald didn't stop me,\x01",
            "'cause I woulda beaten his ass into\x01",
            "next week!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C6B")

    label("loc_5C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_5D18")

    ChrTalk(
        0xB,
        (
            "Jed's the second strongest outta all of us,\x01",
            "and he's also one of the group's leaders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Who the hell does Dino think he is?!\x01",
            "He'll pay for this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D1B")

    label("loc_5D18")

    Call(0, 21)

    label("loc_5D1B")

    Jump("loc_6C6B")

    label("loc_5D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5DD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5D7D")

    ChrTalk(
        0xB,
        "Huh? What's with you guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Get lost, or else I'll make ya!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DCE")

    label("loc_5D7D")


    ChrTalk(
        0xB,
        "Heh. Dino again, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "He's been pissin' me off real bad lately!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)

    label("loc_5DCE")

    Jump("loc_6C6B")

    label("loc_5DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5E32")

    ChrTalk(
        0xB,
        "Something was wrong with yesterday's race!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We need a do-over!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5EF4")

    label("loc_5E32")


    ChrTalk(
        0xB,
        (
            "Damn it! How'd Wald lose to someone?\x01",
            "It doesn't make any sense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I bet Wazy was holding him back.\x01",
            "That's gotta be it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "There's no way Wald woulda lost\x01",
            "fightin' at full strength!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_5EF4")

    Jump("loc_6C6B")

    label("loc_5EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F0A")
    Call(0, 22)
    Jump("loc_6C6B")

    label("loc_5F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_609C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_5FE3")

    ChrTalk(
        0xB,
        (
            "We've been buttin' heads with the Testaments\x01",
            "more and more these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Damn it. I wanna take 'em down, but\x01",
            "fightin' that huge baldy of theirs would\x01",
            "be pretty exhausting...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FE6")

    label("loc_5FE3")

    Call(0, 23)

    label("loc_5FE6")

    Jump("loc_6097")

    label("loc_5FEB")


    ChrTalk(
        0xB,
        (
            "Wald's been trainin' us early\x01",
            "in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Heh. A decisive battle with those blue bastards\x01",
            "is just what the doc ordered! They can fight\x01",
            "us whenever, wherever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6097")

    Jump("loc_6C6B")

    label("loc_609C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6158")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6126")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 0)), scpexpr(EXPR_END)), "loc_611E")

    ChrTalk(
        0xB,
        (
            "Oh, don't worry. We're gonna smash your\x01",
            "faces in at some point, too. Ya better\x01",
            "watch out!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6121")

    label("loc_611E")

    Call(0, 23)

    label("loc_6121")

    Jump("loc_6153")

    label("loc_6126")

    OP_4B(0xA, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xB,
        "Y-YEAH!\x02",
    )

    CloseMessageWindow()
    OP_64(0xB)
    OP_4C(0xA, 0xFF)

    label("loc_6153")

    Jump("loc_6C6B")

    label("loc_6158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_62DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6210")

    ChrTalk(
        0xB,
        (
            "Man, more cops keep comin' around here,\x01",
            "and it's startin' to piss me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Listen up, ya punks! Don't get ahead of\x01",
            "yourselves, or I'll end ya! Got it?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D7")

    label("loc_6210")


    ChrTalk(
        0xB,
        (
            "We got into a fight with some cop over\x01",
            "on East Street yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "He started it, though!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Don't screw with us, 'kay?! You might be\x01",
            "cops, but we ain't afraid to lay waste to\x01",
            "you dogs!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_62D7")

    Jump("loc_6C6B")

    label("loc_62DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_634E")

    ChrTalk(
        0xB,
        (
            "Some chick moved into Lotus Heights\x01",
            "all by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hahaha... What a dumb bitch.\x02",
    )

    CloseMessageWindow()
    Jump("loc_642E")

    label("loc_634E")


    ChrTalk(
        0xB,
        (
            "You guys hear some chick moved into\x01",
            "Lotus Heights all by herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Can ya guys believe it?! A girl, moving\x01",
            "to the Downtown District alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Gahaha... I scoped her out real quick, too.\x01",
            "She looks dumb as hell!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_642E")

    Jump("loc_6C6B")

    label("loc_6433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_65E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_64BC")

    ChrTalk(
        0xB,
        (
            "Now that Koki's back, the Testaments\x01",
            "are finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Look out, ya blue bastards!\x01",
            "We're gonna destroy you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E0")

    label("loc_64BC")


    ChrTalk(
        0xB,
        "Oh, hell yeah! Koki's back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And now that he is, we can finally call\x01",
            "him a true member of the Saber Vipers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Dude, we can totally go and beat\x01",
            "the hell outta the Testaments now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FCalm down. Don't do anything rash.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FThey are literally incapable of learning.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_65E0")

    Jump("loc_6C6B")

    label("loc_65E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 6)), scpexpr(EXPR_END)), "loc_669D")

    ChrTalk(
        0xB,
        (
            "Damn those blue bastards, messin'\x01",
            "with us like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Look at what they did to my boy!\x01",
            "I'm friggin' PISSED we didn't beat\x01",
            "'em when we had the chance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC0")

    label("loc_669D")


    ChrTalk(
        0xB,
        (
            "I'm so goddamn mad! I knew we shoulda\x01",
            "taken 'em out while we had the chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Back when we were loading Koki into\x01",
            "the ambulance, we ran into a bunch of\x01",
            "blue bastards, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They were cryin' about how one of their\x01",
            "guys was knocked out, too, so the\x01",
            "ambulance took him along with Koki.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_6883")

    ChrTalk(
        0x101,
        (
            "#0005FOh, right. I guess the guy from the\x01",
            "Testaments rode in the same ambulance\x01",
            "as your friend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69FA")

    label("loc_6883")


    ChrTalk(
        0x101,
        "#0005FSo they were taken at the same time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FAin't that one hell of a coincidence?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xB,
        "Wh-What's it matter to you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We took care of Koki through the night,\x01",
            "then called an ambulance in the morning.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    ChrTalk(
        0x102,
        (
            "#0105FRight, I suppose the Testaments were\x01",
            "essentially in the same situation. It makes\x01",
            "it sound like you fought each other...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_69FA")


    ChrTalk(
        0x102,
        (
            "#0105FBut in that case, wouldn't you have known\x01",
            "that the Testaments got hurt, too?\x02\x03",
            "#0100FThey even claimed that his wounds were\x01",
            "the result of your signature nail bats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hah! That's pretty obviously one of\x01",
            "their dirty tricks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They ain't afraid of gettin' down and dirty.\x01",
            "Those brainiacs are always trying\x01",
            "to make us look bad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Son of a bitch! I know we decided to retreat,\x01",
            "but we shoulda totally beat the hell outta 'em\x01",
            "right there!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 6)

    label("loc_6BC0")

    Jump("loc_6C6B")

    label("loc_6BC5")


    ChrTalk(
        0xB,
        (
            "I don't care what you say! The Testaments\x01",
            "are behind this, and that's that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If Wald would just give us the orders, we'd\x01",
            "bring 'em all into a world of hurt!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C6B")

    TalkEnd(0xFE)
    Return()

    # Function_20_5A3A end

    def Function_21_6C6F(): pass

    label("Function_21_6C6F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        "Th-The hell's the matter with Dino?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Huh? B-But it was one-on-one...and Wald\x01",
            "told us to quit your bitchin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You think I can just ignore this?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0001FSomething happen, guys?\x02",
    )

    CloseMessageWindow()

    def lambda_6DA0():
        TurnDirection(0xB, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6DA0)

    def lambda_6DAD():
        TurnDirection(0xC, 0x0, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6DAD)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)

    ChrTalk(
        0xB,
        "Yeah, you could say that. Dino, that idiot...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Dino challenged one of our leaders,\x01",
            "Jed, to a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It was totally insane, too. They kept\x01",
            "tradin' blows until it was decided by\x01",
            "an elbow to the jaw...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "He's just a newbie, yet he somehow\x01",
            "managed to take down Jed?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Impossible! I'll never forgive that bastard!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 7)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0xC, 0x87, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_21_6C6F end

    def Function_22_6F2B(): pass

    label("Function_22_6F2B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xB,
        "Am I gettin' a steak skewer, or an omelet rice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yo, you try the tri-color ice cream yet?\x01",
            "The stuff's amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y-You stupid or somethin'?!\x01",
            "Ice cream's for pansies!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_22_6F2B end

    def Function_23_6FEE(): pass

    label("Function_23_6FEE")


    ChrTalk(
        0xB,
        (
            "Damn, it's that giant blue bastard's\x01",
            "fault. I don't get his deal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "We'll take 'em down someday!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 0)
    Return()

    # Function_23_6FEE end

    def Function_24_705B(): pass

    label("Function_24_705B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_70EF")
    Jump("loc_7139")

    label("loc_70EF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_710F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7139")

    label("loc_710F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_712F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7139")

    label("loc_712F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7139")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_71DE")

    ChrTalk(
        0x11,
        "Huuuh? The cops are here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "You here to shut us down? Well, screw you!\x01",
            "Don't get in the way of our party!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73EB")

    label("loc_71DE")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0x11, 0x0)

    ChrTalk(
        0xC,
        (
            "Hey, listen to this. I tried messin' with that\x01",
            "Rixia chick a lil' while ago. Y'know, figured\x01",
            "I'd tap her with my bat or somethin'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...but, damn, she dodged it like it was nothin'!\x01",
            "Never seen someone so agile before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hah! I couldn't catch her even if I wanted to!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Won't lie... The same thing happened to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I tried threatenin' her, but she didn't\x01",
            "even flinch. The hell's up with her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(Well, she IS a dancer. It's no wonder she\x01",
            "was able to outmaneuver these guys.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_73EB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_24_705B end

    def Function_25_73F3(): pass

    label("Function_25_73F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_744A")

    ChrTalk(
        0xC,
        "Dino still hasn't come back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "The hell is that kid doin'?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8609")

    label("loc_744A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7556")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_74D4")

    ChrTalk(
        0xC,
        (
            "Man, Dino was actin' like a\x01",
            "total freak for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He was amped up, and\x01",
            "his eyes were bloodshot...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7551")

    label("loc_74D4")


    ChrTalk(
        0xC,
        (
            "Hahaha! Friggin' Dino, man!\x01",
            "Did he seriously--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I-I dunno if I can say it, especially\x01",
            "in fronta Wald...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7551")

    Jump("loc_8609")

    label("loc_7556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_7632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7598")

    ChrTalk(
        0xC,
        "*sigh* Why'd it have to come to this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_762D")

    label("loc_7598")


    ChrTalk(
        0xC,
        "Holy Aidios, it's tense in here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is it just me, or does Wald have a totally\x01",
            "scary-lookin' aura around him? He looks\x01",
            "SUPER pissed off...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_762D")

    Jump("loc_8609")

    label("loc_7632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_76C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_76BA")

    ChrTalk(
        0xC,
        "When'd Dino become so disrespectful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And how the hell'd he take down Jed?\x01",
            "Nothin' makes sense anymore!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76BD")

    label("loc_76BA")

    Call(0, 21)

    label("loc_76BD")

    Jump("loc_8609")

    label("loc_76C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_778A")

    ChrTalk(
        0xC,
        "The cops are here at a time like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Get the HELL outta here! If you stick\x01",
            "your noses in our business, I'll kill ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#0501F(What is this delinquent so worked up about?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8609")

    label("loc_778A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7951")

    ChrTalk(
        0xC,
        "This is some damn good booze.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Think I should shotgun it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FHe's old enough to drink...right?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_785F")

    ChrTalk(
        0x102,
        (
            "#0100FI think so. There's no harm in\x01",
            "him drinking then, is there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_794C")

    label("loc_785F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78E3")

    ChrTalk(
        0x103,
        (
            "#0203FJudging by his appearance, I believe so.\x01",
            "He may also be intoxicated, but not\x01",
            "to a dangerous degree.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_794C")

    label("loc_78E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_794C")

    ChrTalk(
        0x104,
        (
            "#0304FYeah, probably. No harm in gettin' plastered\x01",
            "every once in a while, is there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_794C")

    Jump("loc_8609")

    label("loc_7951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7A02")

    ChrTalk(
        0xC,
        (
            "It's tradition for the Saber Vipers to\x01",
            "throw a huge party on the last day\x01",
            "of the festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll wreck you if you try and ruin our fun.\x01",
            "You got it, punk?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8609")

    label("loc_7A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7A5B")

    ChrTalk(
        0xC,
        "So, when's the next race?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Count me in for the next one!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B22")

    label("loc_7A5B")


    ChrTalk(
        0xC,
        (
            "Yesterday's chase battle was pretty\x01",
            "friggin' awesome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Huey and I didn't get a lick of sleep last\x01",
            "night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We were out bein' doofuses late into\x01",
            "the night without realizin' it! Gahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7B22")

    Jump("loc_8609")

    label("loc_7B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B38")
    Call(0, 22)
    Jump("loc_8609")

    label("loc_7B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7C97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_7C00")

    ChrTalk(
        0xC,
        (
            "Is it time for us to go to war with those\x01",
            "blue bastards? It's about damn time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually...I'm kinda tired. Can we do it\x01",
            "another day? I need some shut-eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C03")

    label("loc_7C00")

    Call(0, 26)

    label("loc_7C03")

    Jump("loc_7C92")

    label("loc_7C08")


    ChrTalk(
        0xC,
        (
            "Hell yeah! Is it time for us to go to war\x01",
            "with those blue bastards?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Bring it on! They've been rubbin' me\x01",
            "the wrong way lately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C92")

    Jump("loc_8609")

    label("loc_7C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7DA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 2)), scpexpr(EXPR_END)), "loc_7D53")

    ChrTalk(
        0xC,
        (
            "What's the matter with that big dude?\x01",
            "He's always lecturin' us like we're in\x01",
            "Sunday School when we run into him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ugh... Why am I so exhausted?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D56")

    label("loc_7D53")

    Call(0, 26)

    label("loc_7D56")

    Jump("loc_7DA1")

    label("loc_7D5B")


    ChrTalk(
        0xC,
        "*gasp* N-No more... I give up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Luganov is way too strong!\x02",
    )

    CloseMessageWindow()

    label("loc_7DA1")

    Jump("loc_8609")

    label("loc_7DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7E01")

    ChrTalk(
        0xC,
        "Hey, guys! Wanna go a few rounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Gahaha. Man, I'm bored!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7EAA")

    label("loc_7E01")


    ChrTalk(
        0xC,
        "What's up, guys? Goin' on a raid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Gahaha! C'mon, I'll be yer opponent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haven't fought those blue bastards\x01",
            "in a while, have we? Man, talk\x01",
            "about boring.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7EAA")

    Jump("loc_8609")

    label("loc_7EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8012")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7F2B")

    ChrTalk(
        0xC,
        (
            "A girl living all alone in the Downtown\x01",
            "District?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Isn't that friggin' hilarious?! Gahaha!\x02",
    )

    CloseMessageWindow()
    Jump("loc_800D")

    label("loc_7F2B")


    ChrTalk(
        0xC,
        (
            "Some chick moved into Lotus Heights\x01",
            "all by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "She must be dumb as hell! What kinda\x01",
            "sane chick would move here alone?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, and her rack... Sweet, merciful Aidios,\x01",
            "don't even get me started on that RACK!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_800D")

    Jump("loc_8609")

    label("loc_8012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8218")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_80BC")

    ChrTalk(
        0xC,
        (
            "Noticed some chick I'd never seen before\x01",
            "walkin' around the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We got ourselves a new chest--err, face--\x01",
            "in the Downtown District?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8213")

    label("loc_80BC")


    ChrTalk(
        0xC,
        (
            "Noticed some chick I'd never seen before\x01",
            "walkin' around the streets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Gahaha! She a dumbass?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would LITERALLY quit the Vipers RIGHT NOW\x01",
            "if she'd let me orbal motorboat them titties once.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0106F(How very...mature of him.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8213")

    Jump("loc_8609")

    label("loc_8218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_84A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_828F")

    ChrTalk(
        0xC,
        "Hah! Mark my words!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're gonna beat the hell outta the\x01",
            "Testaments one of these days!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_849E")

    label("loc_828F")


    ChrTalk(
        0xC,
        (
            "Hmm? Didn't we fight you\x01",
            "guys earlier?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "Oh, yeah, totally! You guys kicked\x01",
            "our asses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hah! You better mark my words, 'cause\x01",
            "I'll be sure to kick your asses twice as\x01",
            "hard...eventually!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#0206F(Is he attempting to fight us yet again?\x01",
            "His physical capabilities far surpass\x01",
            "his mental capacity.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(These are the kind of guys to forget\x01",
            "stuff within three minutes. Trust me.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_849E")

    Jump("loc_8609")

    label("loc_84A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8512")

    ChrTalk(
        0xC,
        "Those blue bastards are obviously the culprit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "They're nothin' but a bunch of maggots!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8609")

    label("loc_8512")


    ChrTalk(
        0xC,
        (
            "Hey there, buds. Why do ya look like\x01",
            "somebody just killed your parents?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Gahaha. You doubtin' what Wald says?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Trust me. Badasses like us aren't cowardly\x01",
            "enough to ambush somebody in the dark.\x01",
            "It was obviously those blue bastards!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8609")

    TalkEnd(0xFE)
    Return()

    # Function_25_73F3 end

    def Function_26_860D(): pass

    label("Function_26_860D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_86AB")

    ChrTalk(
        0xC,
        (
            "We got our asses handed to us while\x01",
            "Wald was gone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He's gonna be so pissed at us. Maaan,\x01",
            "weren't we supposed to be unstoppable?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8759")

    label("loc_86AB")


    ChrTalk(
        0xC,
        (
            "All right, fine. Whatever. You won. I just\x01",
            "hate how preachy that big dude is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can't understand half the crap he says!\x01",
            "Man, this whole situation has made me BEAT.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8759")

    SetScenarioFlags(0x8F, 2)
    Return()

    # Function_26_860D end

    def Function_27_875D(): pass

    label("Function_27_875D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_87F6")

    ChrTalk(
        0xD,
        (
            "Maybe I should try lookin' for\x01",
            "Dino one last time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But man, Wald's going to put that kid\x01",
            "on a stretcher when he comes back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_87F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_END)), "loc_8860")

    ChrTalk(
        0xD,
        "Wh-Who do you think you are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Who said you could come in here\x01",
            "right now?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8863")

    label("loc_8860")

    Call(0, 11)

    label("loc_8863")

    Jump("loc_968A")

    label("loc_8868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_88CC")

    ChrTalk(
        0xD,
        (
            "Jed got sent to the hospital\x01",
            "'cause of Dino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "The hell happened to that kid?\x02",
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_88CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_896D")

    ChrTalk(
        0xD,
        (
            "Jed's one of the more senior dudes in\x01",
            "our group, and he usually trains us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "How'd Dino absolutely destroy him?\x01",
            "Somethin' ain't adding up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_896D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8A5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_89D8")

    ChrTalk(
        0xD,
        (
            "Dino's on the bottom rung of the Viper\x01",
            "ladder, and he's usually a total pansy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A59")

    label("loc_89D8")


    ChrTalk(
        0xD,
        "Dino's been creepin' me out these days.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Why would he say somethin' like that?\x01",
            "It's totally outta character for him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8A59")

    Jump("loc_968A")

    label("loc_8A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8B3C")

    ChrTalk(
        0xD,
        (
            "We're havin' a party today. We usually\x01",
            "set aside one day a week to throw one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I should probably bring somethin' out\x01",
            "for Dino to eat later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FYou hold them WEEKLY? Isn't that\x01",
            "way too often?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_8B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8BA3")

    ChrTalk(
        0xD,
        "Ugh... Guard duty is such a drag.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "What are all the older guys up to right now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_8BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8C79")

    ChrTalk(
        0xD,
        (
            "Dino's on the lowest rung of the Vipers\x01",
            "ladder, so he's guardin' the base for\x01",
            "the entire festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Poor guy. Maybe I'll switch places with\x01",
            "him for a day so he can go have some fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D49")

    label("loc_8C79")

    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "Got you a little gift, bud.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just ran off to buy it a few minutes ago,\x01",
            "so eat it while it's still hot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Is that...takoyaki?! Oh, baby, takoyaki just\x01",
            "screams Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0xE, 0xFF)

    label("loc_8D49")

    Jump("loc_968A")

    label("loc_8D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8D84")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_8D74")
    Call(0, 28)
    Jump("loc_8D77")

    label("loc_8D74")

    Call(0, 29)

    label("loc_8D77")

    Jump("loc_8D7F")

    label("loc_8D7C")

    Call(0, 28)

    label("loc_8D7F")

    Jump("loc_968A")

    label("loc_8D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8FC7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 3)), scpexpr(EXPR_END)), "loc_8E44")

    ChrTalk(
        0xD,
        (
            "M-Man, today's morning training has me\x01",
            "beat. Two days in a row is asking a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Guess I'm havin' a lazy day today.\x01",
            "People need their rest, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E47")

    label("loc_8E44")

    Call(0, 29)

    label("loc_8E47")

    Jump("loc_8FC2")

    label("loc_8E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8EDC")

    ChrTalk(
        0xD,
        "Dino still can't handle morning training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I can't blame him, either. Wald and the\x01",
            "other guys are all freakishly strong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FC2")

    label("loc_8EDC")


    ChrTalk(
        0xD,
        (
            "Sheesh... Morning training feels like\x01",
            "a hike through Gehenna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, yeah! It's about time we start teaching\x01",
            "Dino our fighting style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Then again, he's kind of a crybaby. Would\x01",
            "he even last a minute in a real fight?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_8FC2")

    Jump("loc_968A")

    label("loc_8FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9043")

    ChrTalk(
        0xD,
        (
            "We've been taking turns patrollin' our turf\x01",
            "since last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Huey and Slash are out today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_911D")

    label("loc_9043")


    ChrTalk(
        0xD,
        (
            "We all started taking turns patrolling in\x01",
            "groups of two or three as of last week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "These legs were hardened--no, SCULPTED--\x01",
            "from being an errand boy. Patrolling? Pssh.\x01",
            "That's not even close to a challenge.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_911D")

    Jump("loc_968A")

    label("loc_9122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_91B3")

    ChrTalk(
        0xD,
        (
            "The older guys look pretty tense lately,\x01",
            "and it's looking like I might get roped\x01",
            "into whatever has 'em on edge, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9281")

    label("loc_91B3")


    ChrTalk(
        0xD,
        "The older guys look pretty tense lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You guys shoulda seen Jed when I bought\x01",
            "the wrong stuff from the city yesterday.\x01",
            "He was sooooooo mad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "A...haha... I got dragged into their mess.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_9281")

    Jump("loc_968A")

    label("loc_9286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_94C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_939D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_930A")

    ChrTalk(
        0xD,
        (
            "(Wh-What the hell did you guys do\x01",
            "to Wald?!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "(I've never seen him this pissed before!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9398")

    label("loc_930A")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "#1601FGo buy me some booze, Koki.\x02\x03",
            "#1607FYou deaf, kid? Move yer ass!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(
        0xD,
        "S-S-Sure thing, Wald!\x02",
    )

    CloseMessageWindow()
    OP_64(0xD)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)

    label("loc_9398")

    Jump("loc_94C3")

    label("loc_939D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9429")

    ChrTalk(
        0xD,
        (
            "Guard duty is tough, lemme tell you.\x01",
            "It's basically training for the newbies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I sure hope Dino doesn't screw it up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_94C3")

    label("loc_9429")


    ChrTalk(
        0xD,
        "Is Dino ready for guard duty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I've gotta go to the hospital tomorrow.\x01",
            "I sure hope the doc can patch me up\x01",
            "quick so I can go right back home.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_94C3")

    Jump("loc_968A")

    label("loc_94C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9547")

    ChrTalk(
        0xD,
        (
            "I don't wanna worry Wald any more\x01",
            "than I already have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "You seriously think I can sleep at a hospital?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_9547")


    ChrTalk(
        0xD,
        "Ow, ow owww... This friggin' hurts.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FSo, how's the injury?\x02\x03",
            "Wasn't it going to take about\x01",
            "a month to heal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yeah. It's fine, though. I'm more pissed about\x01",
            "how I was dragged to the hospital against\x01",
            "my own will! I can't sleep in those hellholes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0306FWell, uh, at least you're feelin' better, eh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_968A")

    TalkEnd(0xFE)
    Return()

    # Function_27_875D end

    def Function_28_968E(): pass

    label("Function_28_968E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9792")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9719")

    ChrTalk(
        0xD,
        (
            "D-Damn it. How dare they get all\x01",
            "high and mighty on me like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'll get 'em back sooner or later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_978D")

    label("loc_9719")


    ChrTalk(
        0xD,
        (
            "D-Damn it. How dare they get all\x01",
            "high and mighty on me like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Grr... I'm so pissed! This means war!\x02",
    )

    CloseMessageWindow()

    label("loc_978D")

    Jump("loc_9847")

    label("loc_9792")


    ChrTalk(
        0xD,
        (
            "I bumped into some jerkwads from the\x01",
            "Testaments when I was on patrol earlier.\x01",
            "We gotta do somethin' about those blue bastards!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "We've got a meeting today, so shove off.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_9847")

    Return()

    # Function_28_968E end

    def Function_29_9848(): pass

    label("Function_29_9848")


    ChrTalk(
        0xD,
        (
            "A four-on-four without a leader?\x01",
            "Kinda weird, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Screw you guys! I'll never forget\x01",
            "your faces!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200FHave we done something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FNah. Pretty sure he's just tryin' to show off.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 3)
    Return()

    # Function_29_9848 end

    def Function_30_991F(): pass

    label("Function_30_991F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_9A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_999B")

    ChrTalk(
        0xE,
        (
            "I managed to snatch up Jed's\x01",
            "position in the Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hahaha! Bow down to my true power!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A2A")

    label("loc_999B")


    ChrTalk(
        0xE,
        "Huuuh? Whaddaya want from me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "You got a bone to pick with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Wouldn't mind thrashin' you guys\x01",
            "if that's the case. Hahahaha!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9A2A")

    Jump("loc_9E36")

    label("loc_9A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9AB4")
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xE,
        (
            "Hurry up and train with me already,\x01",
            "Jed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Or...are you scared I'll take you\x01",
            "down, ya coward?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_9AB7")

    label("loc_9AB4")

    Call(0, 18)

    label("loc_9AB7")

    Jump("loc_9E36")

    label("loc_9ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9B2C")

    ChrTalk(
        0xE,
        "Man... Wald's so friggin' cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh* I hope I can get as\x01",
            "strong as him soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BDD")

    label("loc_9B2C")


    ChrTalk(
        0xE,
        "So this is Wald's seat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Man, everything about Wald\x01",
            "is too cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's my dream to become strong\x01",
            "enough for him to recognize me\x01",
            "as a top member of the Vipers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9BDD")

    Jump("loc_9E36")

    label("loc_9BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9C45")

    ChrTalk(
        0xE,
        "Koki's always so nice to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Heh... *sniff* I'm glad I'm friends\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E36")

    label("loc_9C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_9D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9CA7")

    ChrTalk(
        0xE,
        "Where'd everyone go?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I haven't seen anybody around\x01",
            "all morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D6E")

    label("loc_9CA7")


    ChrTalk(
        0xE,
        "Where the heck did they all go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "They're late...\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xE, 0x0, 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Eeek! Wh-What the heck are you\x01",
            "doing?! You scared me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I-I-I'm not afraid to beat you up!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_9D6E")

    Jump("loc_9E36")

    label("loc_9D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9E01")
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "Huh? H-Hey! You can't just come in\x01",
            "here whenever you like!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "I-I'll beat you up! So back up, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E36")

    label("loc_9E01")


    ChrTalk(
        0xE,
        "Koki's back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Hooray! Thank you, Aidios!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_9E36")

    TalkEnd(0xFE)
    Return()

    # Function_30_991F end

    def Function_31_9E3A(): pass

    label("Function_31_9E3A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1E)
    LoadChrToIndex("chr/ch31750.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch02150.itc", 0x21)
    LoadChrToIndex("chr/ch02152.itc", 0x22)
    LoadChrToIndex("chr/ch02151.itc", 0x23)
    LoadChrToIndex("apl/ch50030.itc", 0x24)
    OP_68(1400, 1000, 0, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 2400, 0, -700, 90)
    SetChrPos(0x102, 2400, 0, 700, 90)
    SetChrPos(0x103, 1100, 0, -700, 90)
    SetChrPos(0x104, 1100, 0, 700, 90)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 17650, 1050, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrPos(0x9, 12600, 0, 3000, 315)
    SetChrPos(0xA, 11400, 0, 3800, 135)
    SetChrPos(0xB, 12600, 0, -4300, 270)
    SetChrPos(0xC, 11000, 0, -4300, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x12, 16000, 1000, 1600, 0)
    OP_D3(0x12, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x13, 16000, 1000, 1600, 0)
    OP_D3(0x13, 0x0, 0xAFC8, 0x0, 0x0)
    LoadEffect(0x0, "battle\\ms00001.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    ClearMapFlags(0x10000000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_68(3400, 1000, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#0400428V#0101FThis place is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400429V#6P#0211F...far too noisy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400430V#6P#0001FYou were right. They turned it into a music venue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400431V#0309FDamn. They actually transformed this dusty\x01",
            "old building into a hangout spot? I'm impressed.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Rough Voice",
        "#0400432VHeh. It's about damn time.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(14700, 1100, 0, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(26500, 2500)

    def lambda_A296():

        label("loc_A296")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A296")

    QueueWorkItem2(0x9, 2, lambda_A296)

    def lambda_A2A8():

        label("loc_A2A8")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_A2A8")

    QueueWorkItem2(0xA, 2, lambda_A2A8)

    def lambda_A2BA():

        label("loc_A2BA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A2BA")

    QueueWorkItem2(0xB, 2, lambda_A2BA)

    def lambda_A2CC():

        label("loc_A2CC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A2CC")

    QueueWorkItem2(0xC, 2, lambda_A2CC)
    OP_6F(0x79)

    NpcTalk(
        0x9,
        "Young Man in Red",
        (
            "#0400433V#11PY-You've sure got some stones\x01",
            "showing your faces here!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Red",
        (
            "#0400434V#11PI can't believe you guys actually showed up.\x01",
            "You got a death wish or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3AD():
        OP_95(0xFE, 10800, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3AD)
    Sleep(50)

    def lambda_A3CA():
        OP_95(0xFE, 10800, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3CA)
    Sleep(50)

    def lambda_A3E7():
        OP_95(0xFE, 9500, 0, -700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3E7)
    Sleep(50)

    def lambda_A404():
        OP_95(0xFE, 9500, 0, 700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A404)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    Sound(1805, 255, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "#0400435VLooks like those blue bastards told you most\x01",
            "of the details already.\x02\x03",
            "#0400436VWhat are you here for, then? Gonna arrest us?\x02",
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
            "#0400437V#0003FNot at all. We were hoping to ask for\x01",
            "your cooperation in our investigation.\x02\x03",
            "#0400438V#0001FIf you don't mind, why exactly do you\x01",
            "want to destroy the Testaments?\x02\x03",
            "#0400439VWe've heard their side of the story,\x01",
            "so we'd like to hear yours now.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A672():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A672)
    Sleep(100)

    def lambda_A682():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A682)
    Sleep(50)

    def lambda_A692():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A692)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x104,
        "#0400440V#0305FHuh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400441V#0205FIs the Testaments' statement not sufficient\x01",
            "enough to explain their feud?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400442V#5P#0003FNo, it's not. The truth can easily change\x01",
            "depending on who you talk to and what\x01",
            "they claim they saw.\x02\x03",
            "#0400443VThe actual truth can only be brought to light\x01",
            "once everyone's account has been thoroughly\x01",
            "cross-examined and scrutinized.\x02\x03",
            "#0400444V#0000FDoing so is one of my duties as a detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400445V#0300FNow I got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400446V#0203FSo essentially, we need to analyze the\x01",
            "case from various angles, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400447V#1604F#12PHeh. You're a weirdo, that's for sure.\x02\x03",
            "#0400448V#1602FWouldn't it make things a hell of a lot\x01",
            "easier to just assume we're the baddies?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    NpcTalk(
        0x9,
        "Young Man in Red",
        "#0400449V#5PW-Wald!\x02",
    )

    CloseMessageWindow()

    def lambda_A9B1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A9B1)
    Sleep(50)

    def lambda_A9C1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A9C1)
    Sleep(50)

    def lambda_A9D1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A9D1)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x8,
        (
            "#0400450V#1603F#12PListen up, you punk-ass detective.\x02\x03",
            "#0400451VEven if I DID have the info you're\x01",
            "lookin' for and was willin' to give\x01",
            "it up...\x02\x03",
            "#0400452V#1600F...what's in it for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400453V#0005FWell...\x02\x03",
            "#0400454V#0001FI'm guessing you won't be satisfied\x01",
            "with just learning the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400455V#1604F#12PHaha. Hell no I won't.\x02\x03",
            "#0400456VSee, I'm the kinda guy who lives off\x01",
            "of kickin' asses and takin' names.\x02\x03",
            "#0400457V#1602FHow 'bout this? If ya can cool down\x01",
            "my bloodlust right here, right now,\x01",
            "I'll spill the beans!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(14200, 1000, 0, 1000)
    MoveCamera(57, 19, 0, 1000)
    SetCameraDistance(27500, 1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    Sound(808, 0, 100, 0)
    SetChrPos(0x8, 16800, 1000, 0, 270)
    Sleep(500)
    Fade(250)

    def lambda_AC56():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AC56)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_ACA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_ACA4)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_ACCC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_ACCC)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_ACF4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_ACF4)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_AD1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AD1C)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0400458V#5P#0011F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400459V#0301FTch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400460V#1602F#12PLet's have ourselves a lil' brawl.\x01",
            "My gang versus yours. Kick our asses\x01",
            "and you'll get all the info you need.\x02\x03",
            "#0400461VNot a bad deal, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0400462V#0007FAbsolutely not.\x02\x03",
            "#0400463VSelf-defense is a different story, but willingly\x01",
            "participating in meaningless fights is out of\x01",
            "the question!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400464V#1604F#12PNo need to be such a killjoy, kid.\x02\x03",
            "#0400465V#1602FIf you're that afraid of gettin' pummeled,\x01",
            "how about you just leave the two ladies\x01",
            "here instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400466V#0001F...!\x02",
    )

    CloseMessageWindow()

    def lambda_AF6F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF6F)
    Sleep(50)

    def lambda_AF7F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AF7F)
    Sleep(50)

    def lambda_AF8F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AF8F)
    WaitChrThread(0x104, 2)

    ChrTalk(
        0x103,
        "#0400467V#0201F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400468V#0101F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400469V#0301FYou're pushin' your luck.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x4)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    OP_0D()

    def lambda_B02A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B02A)

    def lambda_B037():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B037)

    def lambda_B044():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B044)

    def lambda_B051():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B051)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)

    NpcTalk(
        0x9,
        "Young Man in Red",
        "#0400470V#5PFor real, Boss?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Young Man in Red",
        "#0400471VI dunno... Isn't that kinda scummy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400472V#1600F#12PShut up, you morons.\x02\x03",
            "#0400473V#1604FWhat's the big deal? Just leave 'em\x01",
            "with us for the next two hours while\x01",
            "the two of you go on a lil' walk.\x02\x03",
            "#0400474VDo it, and I'll tell you everything.\x02\x03",
            "#0400475V#1602FHahaha... Sound good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400476V#0013F...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#0400477V#0004FActually, I have a better idea.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(14700, 1100, -300, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)

    def lambda_B28D():
        OP_96(0xFE, 0x2D50, 0x0, 0xFFFFFDA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B28D)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0400478V#6P#0001FMe and you, one-on-one. There shouldn't be\x01",
            "anything wrong with a friendly scrimmage.\x02\x03",
            "#0400479VIf I win, you tell me everything you know\x01",
            "about the case.\x02\x03",
            "#0400480VIs that good enough for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400481V#1605F#12P...\x02",
    )

    CloseMessageWindow()

    def lambda_B3BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B3BB)
    Sleep(100)

    def lambda_B3CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B3CB)
    Sleep(50)

    def lambda_B3DB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B3DB)
    WaitChrThread(0x102, 2)

    ChrTalk(
        0x102,
        "#0400482V#0105FW-Wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400483V#0305FDamn, dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400484V#3P#0206FA reckless idea, I must say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400485V#1601F#12PAre you outta your goddamn mind?\x02\x03",
            "#0400486VRed over there looks like he'd stand a chance,\x01",
            "but you? You look like a twig compared to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400487V#6P#0003FAs I said, I'm a detective. I've been\x01",
            "through some pretty intense training.\x02\x03",
            "#0400488V#0000FI doubt I'll lose to some two-bit street\x01",
            "delinquent like you.\x02",
        )
    )

    CloseMessageWindow()
    Sound(1809, 255, 100, 0)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x8,
        "#0400489V#1609F#4SHahahahahaha!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(1810, 255, 100, 0)
    OP_68(15500, 1500, 0, 1000)
    MoveCamera(43, 17, 0, 1000)
    SetCameraDistance(21000, 1000)

    def lambda_B61A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B61A)

    def lambda_B627():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B627)

    def lambda_B634():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B634)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_B649():
        OP_96(0xFE, 0x3DB8, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B649)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Sleep(800)
    StopBGM(0xBB8)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(80)
    SetChrSubChip(0x8, 0x3)
    SetCameraDistance(23000, 1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 1000, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(826, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x12C)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)

    def lambda_B70D():
        OP_9D(0xFE, 0x3C8C, 0x3E8, 0x1F40, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B70D)

    def lambda_B72A():
        OP_D3(0xFE, 0x0, 0xAFC8, 0xFFFFB1E0, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B72A)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x13, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)

    def lambda_B75C():
        OP_9D(0xFE, 0x3E80, 0x1C2, 0x157C, 0x64, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B75C)

    def lambda_B779():
        OP_D3(0xFE, 0x0, 0x20F58, 0xFFFEA070, 0x190)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B779)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x13, 1)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    Sleep(200)
    OP_6F(0x10)
    Fade(500)
    CancelBlur(0)
    Sleep(500)

    ChrTalk(
        0x103,
        "#0400491V#0210F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400492V#0013F...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#0400493V#11P#1604FDidn't think there'd be another guy\x01",
            "stupid enough to challenge me to\x01",
            "a fight.\x02\x03",
            "#0400494V#1602FSure, kid! I'll accept your fight!\x02\x03",
            "#0400495VI'm Wald Wales, the Demon Smasher,\x01",
            "and leader of the Saber Vipers!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#0400496V#11P#1607F#4SIf you think you can take me down,\x01",
            "then show me what ya got!\x02",
        )
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x103, 0x8)
    SetChrBattleFlags(0x104, 0x8)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x12, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 32)
    Return()

    # Function_31_9E3A end

    def Function_32_B973(): pass

    label("Function_32_B973")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1E)
    LoadChrToIndex("chr/ch31750.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch02150.itc", 0x21)
    LoadChrToIndex("chr/ch02152.itc", 0x22)
    LoadChrToIndex("chr/ch02153.itc", 0x23)
    LoadChrToIndex("chr/ch02154.itc", 0x24)
    LoadChrToIndex("chr/ch00056.itc", 0x25)
    ClearChrBattleFlags(0x102, 0x8)
    ClearChrBattleFlags(0x103, 0x8)
    ClearChrBattleFlags(0x104, 0x8)
    OP_68(14700, 1100, -300, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 11600, 0, -600, 90)
    SetChrPos(0x102, 10800, 0, 700, 90)
    SetChrPos(0x103, 9500, 0, -700, 90)
    SetChrPos(0x104, 9500, 0, 700, 90)

    def lambda_BA3D():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BA3D)

    def lambda_BA4A():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA4A)

    def lambda_BA57():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BA57)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 15800, 1000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    SetChrPos(0x9, 12600, 0, 3000, 315)
    SetChrPos(0xA, 11400, 0, 3800, 135)
    SetChrPos(0xB, 12600, 0, -4300, 270)
    SetChrPos(0xC, 11000, 0, -4300, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)

    def lambda_BB39():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BB39)

    def lambda_BB46():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BB46)

    def lambda_BB53():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BB53)

    def lambda_BB60():
        TurnDirection(0xFE, 0x8, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BB60)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    OP_78(0x0, 0x12)
    OP_78(0x1, 0x13)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_49()
    SetChrPos(0x12, 16000, 1000, 1600, 0)
    OP_D3(0x12, 0x0, 0xAFC8, 0x0, 0x0)
    SetChrPos(0x13, 16000, 450, 5500, 0)
    OP_D3(0x13, 0x0, 0x20F58, 0xFFFEA070, 0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC0F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC0F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC25"),
        (1, "loc_BC3A"),
        (SWITCH_DEFAULT, "loc_BC47"),
    )


    label("loc_BC25")

    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    Jump("loc_BC47")

    label("loc_BC3A")

    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x3)
    Jump("loc_BC47")

    label("loc_BC47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC58")
    SetScenarioFlags(0x4E, 6)

    label("loc_BC58")

    SetCameraDistance(22500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_BC83"),
        (1, "loc_BDC6"),
        (SWITCH_DEFAULT, "loc_C10B"),
    )


    label("loc_BC83")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#0400497V#6P#0010F*pant*...*pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400498V#12P#1601FHaha... Not bad, kid.\x02\x03",
            "#0400512V#1604FWoulda been nicer if we coulda gone\x01",
            "at it for real, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0400513V#12P#1602F...my showdown with that pretty boy's almost\x01",
            "here, so I'll let'cha off the hook this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10B")

    label("loc_BDC6")

    OP_2C(0x3E, 0x3)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        "#0400501V#0105F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0400502V#5P#0205FHe won...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0400503V#5P#0309FWay to go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400504V#6P#0007F*pant* *pant*... How about that?!\x02",
    )

    CloseMessageWindow()

    def lambda_BE70():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE70)
    WaitChrThread(0x8, 2)

    ChrTalk(
        0x8,
        (
            "#0400505V#1603F#11PLooks like you ain't all talk, after all.\x02\x03",
            "#0400506VI wasn't expectin' you to be able to\x01",
            "keep me busy like that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Young Man in Red",
        "#0400507V#5PW-Wald...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    NpcTalk(
        0xB,
        "Young Man in Red",
        "#0400508VDamn you! You'll pay for that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400509V#1600F#11PShut up, you dumbasses.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_BFBA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BFBA)
    SetChrSubChip(0x8, 0x2)
    Sound(808, 0, 100, 0)
    Sleep(50)
    Fade(250)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0400510V#6P#0001FUgh...\x01",
            "(This guy's a real monster...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400511V#1604F#12PEither way, not bad for a warmup round.\x02\x03",
            "#0400499VFor a second there, I considered goin' all\x01",
            "out, but...\x02\x03",
            "#0400500V#1602FMy showdown with that pretty boy's almost\x01",
            "here, so I'll let'cha off the hook this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C10B")

    label("loc_C10B")


    ChrTalk(
        0x101,
        "#0400514V#6P#0006FHow thoughtful of you.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0400515V#6P#0001FSo, mind filling us in on the details\x01",
            "of the incident now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400516V#1602F#12PHeh. Sure, whatever.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(14700, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(26500, 0)

    def lambda_C20D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C20D)

    def lambda_C21A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C21A)

    def lambda_C227():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C227)

    def lambda_C234():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C234)

    def lambda_C241():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C241)

    def lambda_C24E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C24E)

    def lambda_C25B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C25B)
    SetChrChipByIndex(0x8, 0x7)
    SetChrSubChip(0x8, 0x0)

    def lambda_C270():
        OP_96(0xFE, 0x4268, 0x3E8, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C270)
    Sleep(500)

    def lambda_C28D():
        OP_96(0xFE, 0x2A30, 0x0, 0xFFFFFD44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C28D)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sound(819, 0, 100, 0)
    SetChrPos(0x8, 17650, 1050, 0, 270)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#0400517V#1603F#12PIt all happened five nights ago.\x02\x03",
            "#0400518V#1601FOne of my boys was ambushed by one of\x01",
            "those blue bastards.\x02\x03",
            "#0400519VHappened not too far away from Ignis, too.\x02",
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
        "#0400520V#0005F...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0400521V#0105FD-Did it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400522V#1602F#12PHmph. Well, those cowards claimed that\x01",
            "one of their own was attacked the same\x01",
            "way...\x02\x03",
            "#0400523V'Course, that's just something they\x01",
            "pulled out of their asses.\x02\x03",
            "#0400524V#1603FUs Saber Vipers like to throw down,\x01",
            "but we fight like men.\x02\x03",
            "#0400525V#1601FYou really think we'd bitch out and\x01",
            "jump somebody in the dark?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400526V#0003F...\x02\x03",
            "#0400527V#0001FWhat were the extent of your\x01",
            "follower's injuries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400528V#1603F#12PBeaten till his bones started to fracture.\x01",
            "He's in the hospital now. Said it'll be a\x01",
            "month or so till he's fully recovered.\x02\x03",
            "#0400529VAnd unlike the blue bastard, he didn't pass\x01",
            "out right after the pummeling started...\x02\x03",
            "#0400530V#1601FHe took a helluva worse beating than him,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0400531V#0008FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0400532V#0301FYou guys definitely sure the Testaments\x01",
            "are the perps?\x02\x03",
            "#0400533VYou said he didn't pass out immediately,\x01",
            "right? Can't he give us his statement?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(50)
    OP_64(0x9)
    OP_64(0xA)
    OP_64(0xB)
    OP_64(0xC)

    ChrTalk(
        0x101,
        (
            "#0400534V#0005F...?\x02\x03",
            "#0400535VDid he even see the attackers at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400536V#1603F#12PGuess not.\x02\x03",
            "#0400537V#1601FBut it was definitely those blue bastards.\x01",
            "I'd bet my life on it.\x02\x03",
            "#0400538VAfter all, he was sniped by one of their\x01",
            "rocks.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0400539V#0101FA rock?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0400540V#0201FAre you referring to the stones they\x01",
            "launch with their slingshots?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0400541V#1603F#12PDamn right I am.\x02\x03",
            "#0400542VThe shot knocked the wind outta him,\x01",
            "so the cowards took the chance to rush\x01",
            "in and kick his ass.\x02\x03",
            "#0400543V#1601FHe hung on for a bit, but not for long...\x01",
            "Isn't it obvious who's the culprit now?\x02",
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

    ChrTalk(
        0x8,
        (
            "#0400544V#1604F#12PHaha... That's all I got to tell you.\x02\x03",
            "#0400545V#1600FI said it before, and I'll say it again:\x01",
            "I couldn't care less about the little\x01",
            "details.\x02\x03",
            "#0400546VI'm going to put an end to him AND\x01",
            "his blue bastards. Nothing else matters\x01",
            "at this point.\x02\x03",
            "#0400547V#1602FWanna interfere? Be my guest.\x02\x03",
            "#0400548VIn the end, I'm going to crush everyone\x01",
            "who gets in my way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0400549V#0003FYou made your point.\x02\x03",
            "#0400550V#0000FAnyway, thanks for your cooperation.\x01",
            "I'm sure your statement will be key in\x01",
            "solving this case.\x02\x03",
            "#0400551VWe'll contact you if we discover any\x01",
            "new leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0400552V#1604F#12PKnock yourself out, kid.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x9, 12540, 0, 2950, 225)
    SetChrPos(0xA, 12190, 0, -5270, 270)
    SetChrPos(0xB, 18700, 4000, -8210, 315)
    SetChrPos(0xC, 1780, 0, -5260, 90)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_68(10000, 1000, 0, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, 10000, 0, 0, 270)
    SetChrPos(0x1, 10000, 0, 0, 270)
    SetChrPos(0x2, 10000, 0, 0, 270)
    SetChrPos(0x3, 10000, 0, 0, 270)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetScenarioFlags(0x42, 3)
    OP_29(0x3E, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_32_B973 end

    def Function_33_CF45(): pass

    label("Function_33_CF45")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(19530, 2000, 1510, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 19690, 1000, 770, 135)
    SetChrPos(0x102, 18360, 1000, 2260, 135)
    SetChrPos(0x103, 18160, 1000, 1260, 135)
    SetChrPos(0x104, 19350, 1000, 2060, 135)
    SetChrPos(0x9, 14700, 1000, -3550, 270)
    EndChrThread(0x9, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A card is affixed to the back of the speaker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x101,
        "#11P#0005FFound it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200F9-7-14-9-19... If we match those numbers\x01",
            "to their respective letter in the alphabet,\x01",
            "it spells out I-G-N-I-S.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0300F'Examine the central box that rudely\x01",
            "resounds...' Guess this big ol'\x01",
            "speaker is pretty rude, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FIndeed, but we still haven't found\x01",
            "the statue.\x02\x03",
            "What does the next message say, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#0003FOh, right...\x02",
    )

    CloseMessageWindow()

    def lambda_D205():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D205)

    def lambda_D212():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D212)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(700)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　For the next key, locate the entrance\x01",
            "　leading to the white falcon. A place\x01",
            "　where time is carried away!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0006F'Leading to the white falcon'? He sure\x01",
            "isn't holding back on these riddles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0100FIsn't the white falcon Liberl's national bird?\x01",
            "You know, the country responsible for the\x01",
            "Non-Aggression Pact.\x02\x03",
            "I find it borderline impossible that this clue\x01",
            "isn't related to them in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0303FYeah, but we can't just pack our bags\x01",
            "and fly to Liberl, can we?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#0012FDefinitely not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI am certainly not in support of\x01",
            "that plan, either.\x02\x03",
            "#0200FIf we analyze the patterns within the\x01",
            "clues given to us thus far, our next\x01",
            "target will be local.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#2P#1601FHey, punks. The hell do you think\x01",
            "you're doin'?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D5F1():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D5F1)

    def lambda_D5FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D5FE)

    def lambda_D60B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D60B)

    def lambda_D618():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D618)
    Sleep(300)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    BeginChrThread(0x9, 0, 0, 1)
    OP_68(15660, 2000, 1080, 3000)
    MoveCamera(41, 21, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(21520, 3000)
    Sleep(3000)

    ChrTalk(
        0x101,
        (
            "#0000FSorry, Wald. We didn't mean to\x01",
            "walk in here unannounced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FWe have finished our task, so\x01",
            "you may be at ease.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x4)

    def lambda_D6FA():
        OP_95(0xFE, 14200, 1000, 580, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D6FA)

    ChrTalk(
        0x8,
        (
            "#1607FYeah? Finished? I'll show you\x01",
            "who's FINISHED!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHahaha... Let's get outta here before\x01",
            "Wald pops a friggin' vein!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1250, 1000, -150, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    EndChrThread(0x8, 0x1)
    SetChrPos(0x0, 1250, 0, -150, 270)
    SetChrPos(0x8, 11640, 0, 270, 270)
    SetChrPos(0xA, 10370, 0, 1010, 135)
    SetChrPos(0xC, 10260, 0, -800, 45)
    SetChrFlags(0x8, 0x4)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x0, 0x1)
    OP_29(0x22, 0x1, 0x3)
    ClearScenarioFlags(0xBF, 1)
    SetScenarioFlags(0x0, 7)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_CF45 end

    SaveToFile()

Try(main)
