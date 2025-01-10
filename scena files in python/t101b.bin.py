from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t101b.bin",                # FileName
        "t101b",                    # MapName
        "t101b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "t101b",                  # 0
        "Emmy",                   # 1
        "Zell",                   # 2
        "Gabrion",                # 3
        "Lughman",                # 4
        "Invitee",                # 5
        "犬１",                   # 6
        "犬２",                   # 7
        "犬３",                   # 8
        "犬４",                   # 9
        "Lechter",                # 10
        "Black Kitten",           # 11
        "Kilika",                 # 12
        "Mafioso 1",              # 13
        "Mafioso 2",              # 14
        "Doven Kaiser 1",         # 15
        "SE制御",                 # 16
        "bt101b",                 # 17
        "bt101b",                 # 18
        "bt101b",                 # 19
        "BT101b",                 # 20
        "To Speaker's Mansion",   # 21
        "To Hotel Delphinia",     # 22
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_CC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_D0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_D8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_DC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_E0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_E4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_EC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_F4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_104", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_108", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_10C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 0, 0, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_114", 0x000A, 27, 6, 0, 0, 0, 0, 0, "BT101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, 0, "MonsterBattlePostion_B4", "MonsterBattlePostion_D4", "ed7509", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_158", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7509", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_19C", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31900.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7509", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E0", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31102.dat", "ms31900.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_F4", "MonsterBattlePostion_D4", "ed7509", "ed7000", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22302.itc",                   # 00
        "chr/ch22202.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch27600.itc",                   # 04
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
        "monster/ch67151.itc",               # 1A
        "chr/ch31051.itc",                   # 1B
        "chr/ch31151.itc",                   # 1C
        "chr/ch31951.itc",                   # 1D
    ))

    DeclNpc(2279,    -3700,   -12430,  180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3660,    -3700,   -12430,  180,  469,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1970,   -2000,   34720,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2400,    -1799,   55840,   0,    385,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   26,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  0.0,                   6.0,                   -2.799999952316284,    225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.0,                  0.5600000023841858,    1.0])

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "To Speaker's Mansion")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ScpFunction((
        "Function_0_544",          # 00, 0
        "Function_1_5FC",          # 01, 1
        "Function_2_65D",          # 02, 2
        "Function_3_6BE",          # 03, 3
        "Function_4_6DA",          # 04, 4
        "Function_5_76E",          # 05, 5
        "Function_6_796",          # 06, 6
        "Function_7_9E6",          # 07, 7
        "Function_8_BC5",          # 08, 8
        "Function_9_F4E",          # 09, 9
        "Function_10_10AC",        # 0A, 10
        "Function_11_11D2",        # 0B, 11
        "Function_12_1221",        # 0C, 12
        "Function_13_18D8",        # 0D, 13
        "Function_14_191A",        # 0E, 14
        "Function_15_195C",        # 0F, 15
        "Function_16_199E",        # 10, 16
        "Function_17_19E0",        # 11, 17
        "Function_18_19FC",        # 12, 18
        "Function_19_1A1B",        # 13, 19
        "Function_20_1A40",        # 14, 20
        "Function_21_1A5A",        # 15, 21
        "Function_22_1E8E",        # 16, 22
        "Function_23_29FF",        # 17, 23
    ))


    def Function_0_544(): pass

    label("Function_0_544")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_584"),
        (1, "loc_590"),
        (2, "loc_59C"),
        (3, "loc_5A8"),
        (4, "loc_5B4"),
        (5, "loc_5C0"),
        (6, "loc_5CC"),
        (SWITCH_DEFAULT, "loc_5D8"),
    )


    label("loc_584")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_590")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_59C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E4")

    label("loc_5FB")

    Return()

    # Function_0_544 end

    def Function_1_5FC(): pass

    label("Function_1_5FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_5FC")

    label("loc_65C")

    Return()

    # Function_1_5FC end

    def Function_2_65D(): pass

    label("Function_2_65D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BD")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_65D")

    label("loc_6BD")

    Return()

    # Function_2_65D end

    def Function_3_6BE(): pass

    label("Function_3_6BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D9")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_6BE")

    label("loc_6D9")

    Return()

    # Function_3_6BE end

    def Function_4_6DA(): pass

    label("Function_4_6DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6F7")
    Jump("loc_724")

    label("loc_6F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_END)), "loc_724")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_724")
    Event(0, 23)

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_748")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2450, -3800, -10800, 90)
    Jump("loc_76D")

    label("loc_748")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xA, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)

    label("loc_76D")

    Return()

    # Function_4_6DA end

    def Function_5_76E(): pass

    label("Function_5_76E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_786")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_78F")

    label("loc_78F")

    Sound(126, 1, 80, 0)
    Return()

    # Function_5_76E end

    def Function_6_796(): pass

    label("Function_6_796")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_82A")
    Jump("loc_874")

    label("loc_82A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_84A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_874")

    label("loc_84A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_874")

    label("loc_86A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_874")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_8A7")
    Jump("loc_9DE")

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_8B5")
    Jump("loc_9DE")

    label("loc_8B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_8C3")
    Jump("loc_9DE")

    label("loc_8C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_8D1")
    Jump("loc_9DE")

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_9B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EC")
    Call(0, 8)
    Jump("loc_9B4")

    label("loc_8EC")


    ChrTalk(
        0xFE,
        (
            "Oh, Zell... He may act like a gentleman every\x01",
            "so often, but he has much to improve on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the time I'm done with him, he'll be the\x01",
            "coolest, most proper gentleman to ever\x01",
            "walk the continent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B4")

    Jump("loc_9DE")

    label("loc_9B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_9C7")
    Jump("loc_9DE")

    label("loc_9C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_9D5")
    Jump("loc_9DE")

    label("loc_9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9DE")

    label("loc_9DE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_796 end

    def Function_7_9E6(): pass

    label("Function_7_9E6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7A")
    Jump("loc_AC4")

    label("loc_A7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A9A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC4")

    label("loc_A9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC4")

    label("loc_ABA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AC4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_AF7")
    Jump("loc_BBD")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B05")
    Jump("loc_BBD")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B13")
    Jump("loc_BBD")

    label("loc_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B21")
    Jump("loc_BBD")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C")
    Call(0, 8)
    Jump("loc_B93")

    label("loc_B3C")


    ChrTalk(
        0xFE,
        (
            "Huh...? Emmy, did you catch a cold\x01",
            "or something? Your face is as red\x01",
            "as an apple.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B93")

    Jump("loc_BBD")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_BBD")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_BB4")
    Jump("loc_BBD")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BBD")

    label("loc_BBD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_9E6 end

    def Function_8_BC5(): pass

    label("Function_8_BC5")

    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C59")
    Jump("loc_CA3")

    label("loc_C59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C79")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA3")

    label("loc_C79")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C99")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA3")

    label("loc_C99")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA3")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D5C")
    Jump("loc_DA6")

    label("loc_D5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D7C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA6")

    label("loc_D7C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DA6")

    label("loc_D9C")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA6")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x8,
        (
            "Listen up, Zell. Since you're my fiance,\x01",
            "you have to be more aware of how I\x01",
            "feel at any given moment, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Achoo...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aren't you feeling a bit chilly, Emmy?\x01",
            "We've been talking by the waterside almost\x01",
            "all day, and it's not the warmest outside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "How about we head back to the mansion,\x01",
            "and I'll whip you up a hot bowl of soup?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "O-Oh, okay. *blush*\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_BC5 end

    def Function_9_F4E(): pass

    label("Function_9_F4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_FBC")

    ChrTalk(
        0xFE,
        (
            "Whoa, what the heck?! Why are\x01",
            "there monsters in Mishelam?!\x01",
            "This isn't some show, is it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A8")

    label("loc_FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_FCA")
    Jump("loc_10A8")

    label("loc_FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_FD8")
    Jump("loc_10A8")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_FE6")
    Jump("loc_10A8")

    label("loc_FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1083")

    ChrTalk(
        0xFE,
        (
            "Hmm. I see you dressed to impress.\x01",
            "Or, at least, attempted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By chance, were you also invited to\x01",
            "Speaker Hartmann's place tonight?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A8")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1091")
    Jump("loc_10A8")

    label("loc_1091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_109F")
    Jump("loc_10A8")

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10A8")

    label("loc_10A8")

    TalkEnd(0xFE)
    Return()

    # Function_9_F4E end

    def Function_10_10AC(): pass

    label("Function_10_10AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_10BD")
    Jump("loc_11CE")

    label("loc_10BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_10CB")
    Jump("loc_11CE")

    label("loc_10CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_10D9")
    Jump("loc_11CE")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_10E7")
    Jump("loc_11CE")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_11A9")

    ChrTalk(
        0xFE,
        (
            "Did you notice all the black suits guarding\x01",
            "Speaker Hartmann's place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess when you're essentially Crossbell's boss,\x01",
            "your security can't be anything short of perfect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CE")

    label("loc_11A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_11B7")
    Jump("loc_11CE")

    label("loc_11B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_11C5")
    Jump("loc_11CE")

    label("loc_11C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11CE")

    label("loc_11CE")

    TalkEnd(0xFE)
    Return()

    # Function_10_10AC end

    def Function_11_11D2(): pass

    label("Function_11_11D2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, I should be off. Showing up late\x01",
            "won't earn me any favors...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_11D2 end

    def Function_12_1221(): pass

    label("Function_12_1221")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("monster/ch67152.itc", 0x25)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(420, -500, 6130, 0)
    MoveCamera(309, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19430, 0)
    SetChrPos(0x101, 390, -1800, 11210, 180)
    SetChrPos(0x102, 1320, -1800, 11960, 180)
    SetChrPos(0x103, -1280, -1800, 13280, 180)
    SetChrPos(0x104, -280, -2000, 14780, 180)
    SetChrPos(0x105, -2040, -2000, 15280, 180)
    SetChrPos(0x133, -1620, -1800, 6940, 135)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0xD, 27210, -2000, 1000, 270)
    SetChrPos(0xE, 25090, -2000, 250, 270)
    SetChrPos(0xF, 28070, -2000, -1440, 270)
    SetChrPos(0x10, 29870, -2000, -300, 270)
    BeginChrThread(0xD, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0xE, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0xF, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0x10, 0, 0, 17)
    ModifyEventFlags(0, 0, 0x80)
    FadeToBright(1000, 0)
    SetCameraDistance(16930, 1500)

    def lambda_14DD():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14DD)

    def lambda_14F2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14F2)

    def lambda_1507():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1507)

    def lambda_151C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_151C)

    def lambda_1531():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1531)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Sound(836, 0, 100, 0)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_15DE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15DE)
    Sleep(50)

    def lambda_15EE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15EE)
    Sleep(50)

    def lambda_15FE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15FE)
    Sleep(50)

    def lambda_160E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_160E)
    Sleep(50)

    def lambda_161E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_161E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Fade(1000)
    OP_68(19350, -500, -880, 0)
    MoveCamera(300, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(32759, 0)
    OP_68(14350, -500, -880, 3000)
    SetCameraDistance(16680, 3000)
    MoveCamera(318, 15, 0, 3000)
    BeginChrThread(0xD, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x10, 3, 0, 16)
    BeginChrThread(0x17, 1, 0, 20)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(1780, -500, 5030, 0)
    MoveCamera(318, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20680, 0)
    OP_68(2740, -500, 3670, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18660, 0)
    OP_68(1900, -500, 4600, 2000)
    OP_93(0x101, 0x87, 0x0)
    OP_93(0x102, 0x87, 0x0)
    OP_93(0x103, 0x87, 0x0)
    OP_93(0x104, 0x87, 0x0)
    OP_93(0x105, 0x87, 0x0)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    EndChrThread(0x17, 0x1)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3501779V#0007F#11PNo way! They're letting their war hounds\x01",
            "run around in the residential area?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#3501780V#5805F#5PThat's a lot of doggies!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        "#3501781V#0307F#5P#NLook out!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 19)
    BeginChrThread(0xF, 3, 0, 19)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 19)
    BeginChrThread(0x10, 3, 0, 19)
    Sleep(200)
    Sound(814, 0, 100, 0)
    SetCameraDistance(14660, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    Battle("BattleInfo_114", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 21)
    Return()

    # Function_12_1221 end

    def Function_13_18D8(): pass

    label("Function_13_18D8")


    def lambda_18DD():
        OP_95(0xFE, 3400, -1800, 2640, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18DD)
    WaitChrThread(0xFE, 1)

    def lambda_18FB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18FB)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_13_18D8 end

    def Function_14_191A(): pass

    label("Function_14_191A")


    def lambda_191F():
        OP_95(0xFE, 4100, -1800, -110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_191F)
    WaitChrThread(0xFE, 1)

    def lambda_193D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_193D)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_14_191A end

    def Function_15_195C(): pass

    label("Function_15_195C")


    def lambda_1961():
        OP_95(0xFE, 6240, -1800, -410, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1961)
    WaitChrThread(0xFE, 1)

    def lambda_197F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_197F)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_15_195C end

    def Function_16_199E(): pass

    label("Function_16_199E")


    def lambda_19A3():
        OP_95(0xFE, 5390, -1800, 2470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19A3)
    WaitChrThread(0xFE, 1)

    def lambda_19C1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19C1)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_16_199E end

    def Function_17_19E0(): pass

    label("Function_17_19E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19FB")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_17_19E0")

    label("loc_19FB")

    Return()

    # Function_17_19E0 end

    def Function_18_19FC(): pass

    label("Function_18_19FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A1A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_18_19FC")

    label("loc_1A1A")

    Return()

    # Function_18_19FC end

    def Function_19_1A1B(): pass

    label("Function_19_1A1B")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_19_1A1B end

    def Function_20_1A40(): pass

    label("Function_20_1A40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A59")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_20_1A40")

    label("loc_1A59")

    Return()

    # Function_20_1A40 end

    def Function_21_1A5A(): pass

    label("Function_21_1A5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x25)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_68(780, -500, 4500, 0)
    MoveCamera(312, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19960, 0)
    SetChrPos(0x101, 1870, -1800, 3670, 90)
    SetChrPos(0x102, -430, -1800, 3700, 90)
    SetChrPos(0x103, -1240, -1800, 5800, 90)
    SetChrPos(0x104, -440, -1800, 8090, 90)
    SetChrPos(0x105, 610, -1800, 5940, 90)
    SetChrPos(0x133, 1770, -1800, 2390, 90)
    ClearChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(18460, 2000)
    OP_6F(0x10)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#3501782V#0108F#5PI-I can't believe it...\x02\x03",
            "#3501783V#0110FUnleashing their war hounds in the middle\x01",
            "of all these tourists? Are they insane?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501784V#0211F#5PI doubt they care anymore.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x13B, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#3501785V#0003F#6PWe still have to make our way through\x01",
            "the Mishelam Center and get to the dock.\x02\x03",
            "#3501786V#0013FIf we see any citizens caught up in this,\x01",
            "protect them at all costs! Understood?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D7F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D7F)

    def lambda_1D8C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D8C)
    Sleep(100)

    def lambda_1D9C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D9C)

    def lambda_1DA9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1DA9)

    def lambda_1DB6():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_1DB6)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)

    ChrTalk(
        0x104,
        "#3501787V#0306F#11PEasier said than done, man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#3501788V#0402F#5PHaha. Cops sure have it hard.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x25)
    SetChrPos(0x0, 500, -1800, 1800, 90)
    SetScenarioFlags(0xA7, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_21_1A5A end

    def Function_22_1E8E(): pass

    label("Function_22_1E8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch39100.itc", 0x1F)
    LoadChrToIndex("chr/ch07300.itc", 0x20)
    OP_68(0, -2700, -18800, 0)
    MoveCamera(315, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19700, 0)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 0, -3800, -14800, 180)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 1000, -3800, -14500, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 4850, -1800, -1450, 270)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_90(0x0, 25500, -2000, -3000, 270)
    OP_90(0x1, 25500, -2000, -3000, 270)
    OP_90(0x2, 25500, -2000, -3000, 270)
    OP_90(0x3, 25500, -2000, -3000, 270)
    OP_90(0x4, 25500, -2000, -3000, 270)
    OP_90(0x5, 25500, -2000, -3000, 270)
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
    FadeToBright(1000, 0)
    OP_68(0, -2700, -14800, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x11,
        (
            "#3501954V#3504F#11PAnd there they go.\x02\x03",
            "#3501955V#3500FDang, I was really wanting to spend a\x01",
            "bit more time hanging out 'round here...\x02\x03",
            "#3501956V#3509FGuess I'll have to hold back for now.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)

    NpcTalk(
        0x13,
        "Woman's Voice",
        (
            "#3501957V#3PHold back? From my point of view,\x01",
            "you already spent all of your time goofing off.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2164():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2164)
    OP_93(0x11, 0x0, 0x1F4)
    WaitChrThread(0x12, 1)
    Fade(1000)
    OP_68(0, -700, -6800, 0)
    OP_68(0, -2700, -13800, 9000)

    def lambda_21A3():
        OP_95(0xFE, 0, -1800, -1190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_21A3)
    WaitChrThread(0x13, 1)

    def lambda_21C1():
        OP_95(0xFE, 0, -3800, -12250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_21C1)
    WaitChrThread(0x13, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#3501958V#3404F#11PYou, who serves as the link connecting the\x01",
            "Blood and Iron Chancellor and Hartmann...\x02\x03",
            "#3501959V#3400FDespite serving such an important role,\x01",
            "you've acted quite improperly during this\x01",
            "whole situation, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3501960V#3510F#6PHuh? What are you talking about?\x02\x03",
            "#3501961VIt's not like I gave them a helping hand\x01",
            "upfront. Unlike a certain someone.\x02\x03",
            "#3501962V#3502FYou sure that's okay, though? Kind of\x01",
            "a major interference of domestic affairs,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#3501963V#3405F#11PThat chakram technique was\x01",
            "most impressive, yes.\x02\x03",
            "#3501964V#3404FPerhaps the infamous assassin, Yin,\x01",
            "made an appearance tonight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3501965V#3501F#6PYeah, yeah. Way to brush it off.\x02\x03",
            "#3501966V#3504FEh, whatever. My main objective was\x01",
            "to make contact with you, after all.\x02\x03",
            "#3501967V#3500FThe honorable Kilika Rouran,\x01",
            "division chief of the Rocksmith Agency...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#3501968V#3400F#11PHehe. Sharp, aren't you?\x02\x03",
            "#3501969V#3404FAs expected of a second secretary for the\x01",
            "Imperial government...\x02\x03",
            "#3501970V#3402FNo, perhaps it's more appropriate to address you\x01",
            "by your primary position... Captain Lechter Arundel\x01",
            "of the Imperial Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3501971V#3502F#6PGuess we've figured each other out, then.\x01",
            "That should make things easier.\x02\x03",
            "#3501972V#3504FHow about we head on back to the hotel lounge\x01",
            "and have ourselves a nice chat?\x02\x03",
            "#3501973V#3500FWe can talk about fun stuff. Y'know, like the\x01",
            "intelligence war being waged in Crossbell, the\x01",
            "future plans of our respective countries...\x02\x03",
            "#3501974VMaybe the Non-Aggression Pact, too? Of course,\x01",
            "rules regarding this coming age of the orbal net\x01",
            "need to be discussed as well. Sound good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#3501975V#3402F#11PYes. Let us begin.\x02\x03",
            "#3501976V#3404FThe era of sabotage and terrorism that constantly\x01",
            "alters the world stage is now over.\x02\x03",
            "#3501977VFor the sake of preventing any more tragic\x01",
            "accidents from occurring in Crossbell...\x02\x03",
            "#3501978V#3401F...a new order must be forged, no matter how\x01",
            "insignificant our power may seem.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(18700, 3000)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x7E, 0x3C)
    Sleep(100)
    OP_25(0x7E, 0x32)
    Sleep(100)
    OP_25(0x7E, 0x28)
    Sleep(100)
    OP_25(0x7E, 0x1E)
    Sleep(100)
    OP_25(0x7E, 0x14)
    Sleep(100)
    OP_25(0x7E, 0xA)
    Sleep(100)
    OP_25(0x7E, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("e3010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_1E8E end

    def Function_23_29FF(): pass

    label("Function_23_29FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A49")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)

    label("loc_2A49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A61")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)

    label("loc_2A61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A79")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_2A79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A91")
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)

    label("loc_2A91")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2AC3"),
        (1, "loc_2AD0"),
        (2, "loc_2ADD"),
        (SWITCH_DEFAULT, "loc_2AEA"),
    )


    label("loc_2AC3")

    SetChrChipByIndex(0x14, 0x1B)
    SetChrChipByIndex(0x15, 0x1C)
    Jump("loc_2AEA")

    label("loc_2AD0")

    SetChrChipByIndex(0x14, 0x1B)
    SetChrChipByIndex(0x15, 0x1D)
    Jump("loc_2AEA")

    label("loc_2ADD")

    SetChrChipByIndex(0x14, 0x1C)
    SetChrChipByIndex(0x15, 0x1D)
    Jump("loc_2AEA")

    label("loc_2AEA")

    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x16, 1, 0, 3)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_68(32650, -200, -50, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 32650, -2000, 700, 270)
    SetChrPos(0x1, 32900, -2000, -800, 270)
    SetChrPos(0x2, 34150, -2000, 700, 270)
    SetChrPos(0x3, 34400, -2000, -800, 270)
    SetChrPos(0x133, 35900, -2000, -50, 270)
    SetChrPos(0x14, 26150, -2000, -50, 90)
    SetChrPos(0x15, 24150, -2000, -800, 90)
    SetChrPos(0x16, 25150, -2000, 700, 90)

    def lambda_2BF6():
        OP_98(0x14, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2BF6)
    Sleep(50)

    def lambda_2C13():
        OP_98(0x15, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2C13)
    Sleep(50)

    def lambda_2C30():
        OP_98(0x16, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2C30)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x14, 1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2C6F"),
        (1, "loc_2C8E"),
        (2, "loc_2CAD"),
        (SWITCH_DEFAULT, "loc_2CCC"),
    )


    label("loc_2C6F")

    Battle("BattleInfo_158", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_2CCC")

    label("loc_2C8E")

    Battle("BattleInfo_19C", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_2CCC")

    label("loc_2CAD")

    Battle("BattleInfo_1E0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_2CCC")

    label("loc_2CCC")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CEE")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    label("loc_2CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D06")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    label("loc_2D06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D1E")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    label("loc_2D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D36")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_2D36")

    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x16, 0x2)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_68(33150, -200, -50, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37000, 0)
    SetChrPos(0x0, 33150, -2000, -50, 270)
    SetChrPos(0x1, 33150, -2000, -50, 270)
    SetChrPos(0x2, 33150, -2000, -50, 270)
    SetChrPos(0x3, 33150, -2000, -50, 270)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_29FF end

    SaveToFile()

Try(main)
