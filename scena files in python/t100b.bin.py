from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t100b.bin",                # FileName
        "t100b",                    # MapName
        "t100b",                    # Location
        0x0041,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t100b",                  # 0
        "Stewardess Salsa",       # 1
        "Tourist",                # 2
        "Young Nobleman",         # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Garcia",                 # 6
        "Mafioso",                # 7
        "Mafioso",                # 8
        "Mafioso",                # 9
        "Mafioso",                # 10
        "Mafioso",                # 11
        "犬１",                   # 12
        "犬２",                   # 13
        "犬３",                   # 14
        "Chief Sergei",           # 15
        "Zeit",                   # 16
        "Cruise Ship",            # 17
        "Boat",                   # 18
        "SE制御",                 # 19
        "bt100b",                 # 20
        "To Theme Park",          # 21
        "To Residences",          # 22
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 11, 12, 180)
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

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0042, 27, 6, 0, 0, 0, 0, 0, "bt100b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02201.dat", "ms31900.dat", "ms31900.dat", "ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7404", "ed7000", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28400.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch23700.itc",                   # 04
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

    DeclNpc(-3740,   -4000,   -47180,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-3529,   -5000,   -56490,  180,  385,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5909,    -4000,   -50770,  86,   385,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5760,    -2000,   -28799,  90,   385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(6960,    -2000,   -28799,  270,  385,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
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

    DeclActor(-24500,  -4000,   -45660,  1200,    -24490,  -6000,   -38830,  0x007C, 0,  8,  0x0000)
    DeclActor(10350,   -3990,   -46410,  1200,    10350,   -2500,   -46410,  0x007C, 0,  76, 0x0000)

    PlaceName(-5.0, 0.0, 95.0, 0x0000, 0x0000, "To Theme Park")
    PlaceName(-95.0, 0.0, 20.0, 0x0000, 0x0000, "To Residences")
    PlaceName(1.0, 0.0, 17.5, 0x0000, 0x0052, "")

    ScpFunction((
        "Function_0_56C",          # 00, 0
        "Function_1_624",          # 01, 1
        "Function_2_65E",          # 02, 2
        "Function_3_704",          # 03, 3
        "Function_4_7F7",          # 04, 4
        "Function_5_8CF",          # 05, 5
        "Function_6_976",          # 06, 6
        "Function_7_A33",          # 07, 7
        "Function_8_A7D",          # 08, 8
        "Function_9_B5A",          # 09, 9
        "Function_10_2B7E",        # 0A, 10
        "Function_11_2BA2",        # 0B, 11
        "Function_12_2BD3",        # 0C, 12
        "Function_13_2BFB",        # 0D, 13
        "Function_14_2C23",        # 0E, 14
        "Function_15_2C4B",        # 0F, 15
        "Function_16_2C72",        # 10, 16
        "Function_17_2CDA",        # 11, 17
        "Function_18_2E7C",        # 12, 18
        "Function_19_2EAB",        # 13, 19
        "Function_20_2EDD",        # 14, 20
        "Function_21_2F1F",        # 15, 21
        "Function_22_2F61",        # 16, 22
        "Function_23_2F8A",        # 17, 23
        "Function_24_3094",        # 18, 24
        "Function_25_31C5",        # 19, 25
        "Function_26_31EE",        # 1A, 26
        "Function_27_3214",        # 1B, 27
        "Function_28_323F",        # 1C, 28
        "Function_29_32F0",        # 1D, 29
        "Function_30_34E2",        # 1E, 30
        "Function_31_3617",        # 1F, 31
        "Function_32_36B8",        # 20, 32
        "Function_33_37A3",        # 21, 33
        "Function_34_384B",        # 22, 34
        "Function_35_386B",        # 23, 35
        "Function_36_388B",        # 24, 36
        "Function_37_38AE",        # 25, 37
        "Function_38_38F1",        # 26, 38
        "Function_39_601F",        # 27, 39
        "Function_40_6039",        # 28, 40
        "Function_41_605E",        # 29, 41
        "Function_42_6093",        # 2A, 42
        "Function_43_60C5",        # 2B, 43
        "Function_44_613F",        # 2C, 44
        "Function_45_629A",        # 2D, 45
        "Function_46_62B2",        # 2E, 46
        "Function_47_6341",        # 2F, 47
        "Function_48_63BD",        # 30, 48
        "Function_49_644C",        # 31, 49
        "Function_50_64DC",        # 32, 50
        "Function_51_6558",        # 33, 51
        "Function_52_6739",        # 34, 52
        "Function_53_6767",        # 35, 53
        "Function_54_6874",        # 36, 54
        "Function_55_6984",        # 37, 55
        "Function_56_69AE",        # 38, 56
        "Function_57_69D8",        # 39, 57
        "Function_58_6A02",        # 3A, 58
        "Function_59_6A2C",        # 3B, 59
        "Function_60_6A56",        # 3C, 60
        "Function_61_6A80",        # 3D, 61
        "Function_62_6A9A",        # 3E, 62
        "Function_63_6AD9",        # 3F, 63
        "Function_64_6B18",        # 40, 64
        "Function_65_6B57",        # 41, 65
        "Function_66_6BA6",        # 42, 66
        "Function_67_6C6B",        # 43, 67
        "Function_68_6CF6",        # 44, 68
        "Function_69_6D81",        # 45, 69
        "Function_70_6DDD",        # 46, 70
        "Function_71_6E24",        # 47, 71
        "Function_72_6E6D",        # 48, 72
        "Function_73_6EBA",        # 49, 73
        "Function_74_6EFD",        # 4A, 74
        "Function_75_6F4A",        # 4B, 75
        "Function_76_6F8D",        # 4C, 76
    ))


    def Function_0_56C(): pass

    label("Function_0_56C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5AC"),
        (1, "loc_5B8"),
        (2, "loc_5C4"),
        (3, "loc_5D0"),
        (4, "loc_5DC"),
        (5, "loc_5E8"),
        (6, "loc_5F4"),
        (SWITCH_DEFAULT, "loc_600"),
    )


    label("loc_5AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_5F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_600")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_60C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_623")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_60C")

    label("loc_623")

    Return()

    # Function_0_56C end

    def Function_1_624(): pass

    label("Function_1_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    Event(0, 9)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_644")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 38)

    label("loc_644")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Return()

    # Function_1_624 end

    def Function_2_65E(): pass

    label("Function_2_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_667")

    label("loc_667")

    SetMapObjFlags(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_681")
    OP_65(0x0, 0x1)
    Jump("loc_6CB")

    label("loc_681")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -24490, -6000, -38830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6CB")

    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FD")
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)

    label("loc_6FD")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_65E end

    def Function_3_704(): pass

    label("Function_3_704")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E")

    ChrTalk(
        0xFE,
        (
            "The ship bound for Crossbell City\x01",
            "has just arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Passengers waiting to head back,\x01",
            "please be patient for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7F3")

    label("loc_79E")


    ChrTalk(
        0xFE,
        (
            "Passengers heading back to Crossbell City,\x01",
            "please make a single file line here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3")

    TalkEnd(0xFE)
    Return()

    # Function_3_704 end

    def Function_4_7F7(): pass

    label("Function_4_7F7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I was hoping I'd find a gorgeous, rich\x01",
            "woman while visiting, but I discovered\x01",
            "an unfortunate truth...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These women here are too much for\x01",
            "me to handle. That became abundantly\x01",
            "clear as the day went on.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_7F7 end

    def Function_5_8CF(): pass

    label("Function_5_8CF")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Hmph. About time we arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That jerry-built ship hardly left me any time\x01",
            "before the auction. I suppose that leaves\x01",
            "me no choice but to hurry there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_8CF end

    def Function_6_976(): pass

    label("Function_6_976")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I spent the whole day playing with my\x01",
            "friend at the theme park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We weren't planning to stay the whole day,\x01",
            "so it was shocking when we noticed that\x01",
            "the sun had already set!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_976 end

    def Function_7_A33(): pass

    label("Function_7_A33")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, no. It's almost time for the ferry\x01",
            "to leave! Let's hurry!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_A33 end

    def Function_8_A7D(): pass

    label("Function_8_A7D")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FAuction, smocktion. It's time for fishin'!\x02",
    )

    CloseMessageWindow()
    OP_68(-23140, -2400, -43580, 1500)
    MoveCamera(315, 36, 0, 1500)
    OP_6E(200, 1500)
    SetCameraDistance(50000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B55")
    OP_E0(0x2)
    MiniGame(0x6, 0x3, 0xFFFFA04C, 0xFFFFF060, 0xFFFF4912, 0x0, 0xFFFFA056, 0xFFFFE890, 0xFFFF6852)

    label("loc_B55")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_8_A7D end

    def Function_9_B5A(): pass

    label("Function_9_B5A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31050.itc", 0x1F)
    LoadChrToIndex("chr/ch31051.itc", 0x20)
    LoadChrToIndex("chr/ch31150.itc", 0x23)
    LoadChrToIndex("chr/ch31151.itc", 0x24)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00150.itc", 0x2C)
    LoadChrToIndex("chr/ch00151.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x2E)
    LoadChrToIndex("chr/ch00251.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("chr/ch00351.itc", 0x31)
    LoadChrToIndex("chr/ch00450.itc", 0x32)
    LoadChrToIndex("chr/ch00451.itc", 0x33)
    LoadChrToIndex("chr/ch02200.itc", 0x34)
    LoadChrToIndex("chr/ch02250.itc", 0x35)
    LoadChrToIndex("monster/ch67150.itc", 0x36)
    LoadChrToIndex("monster/ch67151.itc", 0x37)
    LoadChrToIndex("chr/ch00052.itc", 0x38)
    LoadChrToIndex("chr/ch00152.itc", 0x39)
    LoadChrToIndex("chr/ch00254.itc", 0x3A)
    LoadChrToIndex("chr/ch00352.itc", 0x3B)
    LoadChrToIndex("chr/ch00452.itc", 0x3C)
    LoadChrToIndex("chr/ch31052.itc", 0x3D)
    LoadChrToIndex("chr/ch31152.itc", 0x3E)
    LoadChrToIndex("chr/ch31952.itc", 0x3F)
    LoadChrToIndex("monster/ch67152.itc", 0x40)
    LoadChrToIndex("chr/ch00457.itc", 0x41)
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "battle\\mg040_00.eff")
    LoadEffect(0x4, "battle/btgun00.eff")
    LoadEffect(0x5, "event\\eva01_01.eff")
    SoundLoad(479)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x18)
    OP_49()
    SetChrPos(0x18, -5000, -5500, -38200, 0)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x0)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 17000, -5500, -63000, 270)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 300, -2000, -7520, 180)
    SetChrPos(0x102, 1240, -2000, -6340, 180)
    SetChrPos(0x103, -780, -2000, -5850, 180)
    SetChrPos(0x104, -1000, -2000, -4030, 180)
    SetChrPos(0x105, 610, -2000, -4000, 180)
    SetChrPos(0x133, 0, 0, 0, 0)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0x13, 0x36)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x36)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 0, -1300, 5000, 0)
    SetChrPos(0x11, 0, -1300, 5000, 0)
    SetChrPos(0x12, 0, -1300, 5000, 0)
    SetChrPos(0xE, 0, -1300, 5000, 0)
    SetChrPos(0xF, 0, -1300, 5000, 0)
    SetChrPos(0x13, 0, -1300, 5000, 0)
    SetChrPos(0x14, 0, -1300, 5000, 0)
    SetChrPos(0x15, 0, -1300, 5000, 0)
    SetChrPos(0xD, 0, -1300, 5000, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1013")
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_1755")

    label("loc_1013")

    OP_68(0, -800, -4970, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    Sound(475, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(0, -800, -6970, 1500)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501804V#0007F#11PHurry...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(1000, -500, -38550, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(35000, 0)
    MoveCamera(325, 17, 0, 4500)
    SetChrPos(0x101, 300, -2000, -7520, 180)
    SetChrPos(0x102, 1240, -2000, -6340, 180)
    SetChrPos(0x103, -780, -2000, -5850, 180)
    SetChrPos(0x104, -1000, -2000, -4030, 180)
    SetChrPos(0x105, 610, -2000, -4000, 180)

    def lambda_113A():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_113A)

    def lambda_114F():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_114F)

    def lambda_1164():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1164)

    def lambda_1179():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1179)

    def lambda_118E():
        OP_9B(0x0, 0xFE, 0x0, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_118E)
    Sound(477, 0, 100, 0)
    Sound(479, 2, 100, 0)

    def lambda_11AF():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_11AF)
    Sleep(3500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(1000)
    OP_68(0, -500, -27850, 0)
    MoveCamera(315, 13, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21570, 0)
    SetCameraDistance(17570, 2000)
    SetChrPos(0x101, 300, -2000, -18520, 180)
    SetChrPos(0x102, 1240, -2000, -17340, 180)
    SetChrPos(0x103, -780, -2000, -16850, 180)
    SetChrPos(0x104, -1000, -2000, -15030, 180)
    SetChrPos(0x105, 610, -2000, -15000, 180)

    def lambda_1271():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1271)

    def lambda_1286():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1286)

    def lambda_129B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_129B)

    def lambda_12B0():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12B0)

    def lambda_12C5():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12C5)
    EndChrThread(0x18, 0x1)
    SetChrPos(0x18, -5000, -5500, -38200, 0)

    def lambda_12EF():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_12EF)
    WaitChrThread(0x18, 1)
    SetMapObjFlags(0x0, 0x4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0x1A, 1, 0, 37)

    NpcTalk(
        0x101,
        "KeA",
        "#3501805V#5805F#5PAw, the boat went away...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3501806V#0201F#11PNo way... It was not supposed\x01",
            "to leave yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3501807V#0103F#11PThey might have decided to depart early\x01",
            "after hearing the uproar inside the resort.\x02\x03",
            "#3501808V#0108FI might have made the same decision,\x01",
            "if I was in their shoes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#3501809V#0401F#11PWell, from ours, it's the worst-case scenario.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Man's Voice",
        "#3501810V#3PFound 'em!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x10,
        "Man's Voice",
        "#3501811V#3PDon't let them get away!\x02",
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_158D():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_158D)

    def lambda_159A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_159A)
    Sleep(100)

    def lambda_15AA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15AA)

    def lambda_15B7():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15B7)
    Sleep(100)

    def lambda_15C7():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15C7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#3501852V#0013F#6PThey caught up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501813V#0307F#5PKeep on runnin' down the dock!\x02\x03",
            "#3501814VWe might get lucky and find a small\x01",
            "motorboat or somethin'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501815V#0007F#6PWill do!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22570, 3000)

    def lambda_16B6():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16B6)
    Sleep(100)

    def lambda_16D3():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16D3)
    Sleep(100)

    def lambda_16F0():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F0)
    Sleep(100)

    def lambda_170D():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_170D)
    Sleep(100)

    def lambda_172A():
        OP_97(0xFE, 0x2328, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_172A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    label("loc_1755")

    EndChrThread(0x1A, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A43")
    Fade(1000)
    SetChrPos(0x101, 14070, -4000, -46390, 180)
    SetChrPos(0x102, 13870, -4000, -42060, 180)
    SetChrPos(0x103, 14480, -4000, -43440, 180)
    SetChrPos(0x104, 14910, -4000, -45400, 180)
    SetChrPos(0x105, 13200, -4000, -44750, 180)
    OP_68(14000, -2800, -44500, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(14000, -1700, -58400, 3000)
    MoveCamera(0, 16, 0, 3000)
    SetCameraDistance(21390, 3000)

    def lambda_1816():
        OP_95(0xFE, 14020, -4000, -52980, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1816)

    def lambda_1830():
        OP_95(0xFE, 13510, -4000, -49680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1830)

    def lambda_184A():
        OP_95(0xFE, 14570, -4000, -50590, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_184A)

    def lambda_1864():
        OP_95(0xFE, 15240, -4000, -52410, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1864)

    def lambda_187E():
        OP_95(0xFE, 12940, -4000, -51750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_187E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(750)
    Fade(1000)
    OP_68(14000, -2800, -52500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    ChrTalk(
        0x104,
        "#3501816V#0310F#11PDamn, looks like my plan was a bust.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501817V#0008F#5PThere's not much time left...\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x32)
    SetChrSubChip(0x105, 0x0)
    OP_68(11810, -1400, -43680, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(14500, 1250)
    BeginChrThread(0x12, 3, 0, 20)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(2500)
    OP_6F(0x79)
    OP_0D()
    OP_68(10910, -1400, -52370, 1500)
    MoveCamera(35, 17, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(16000, 1500)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 22)
    BeginChrThread(0x102, 3, 0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 24)
    BeginChrThread(0x105, 3, 0, 26)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)

    label("loc_1A43")

    FadeToBright(1000, 0)
    OP_68(-11450, -2000, -50000, 0)
    MoveCamera(90, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(29000, 0)
    OP_68(-11450, -3500, -50000, 2000)
    MoveCamera(50, 16, 0, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x102, 3, 0, 28)
    BeginChrThread(0x104, 3, 0, 30)
    BeginChrThread(0x103, 3, 0, 29)
    BeginChrThread(0x105, 3, 0, 32)
    BeginChrThread(0x13, 3, 0, 33)
    BeginChrThread(0x11, 3, 0, 31)
    BeginChrThread(0x12, 3, 0, 34)
    BeginChrThread(0xE, 3, 0, 35)
    BeginChrThread(0xF, 3, 0, 36)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B16")
    Sleep(1)
    Jump("loc_1AFF")

    label("loc_1B16")

    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x101, -23200, -4000, -50300, 270)
    SetChrPos(0x102, -21660, -4000, -48980, 270)
    SetChrPos(0x103, -21820, -4000, -51340, 270)
    SetChrPos(0x104, -20110, -4000, -50710, 270)
    SetChrPos(0x105, -20210, -4000, -49230, 270)
    SetChrPos(0x10, -10750, -4000, -48500, 270)
    SetChrPos(0x11, -10750, -4000, -51500, 270)
    SetChrPos(0xE, -9750, -4000, -47000, 270)
    SetChrPos(0xF, -9750, -4000, -53000, 270)
    SetChrPos(0x13, -8400, -4000, -48500, 270)
    SetChrPos(0x14, -8400, -4000, -51500, 270)
    SetChrPos(0xD, -13000, -4000, -50000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0x13, 0x37)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x37)
    SetChrSubChip(0x14, 0x0)
    FadeToBright(1000, 0)
    OP_68(-30770, -3000, -50000, 0)
    MoveCamera(30, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(28860, 0)
    SetCameraDistance(19860, 2000)

    def lambda_1CD3():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CD3)

    def lambda_1CE8():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CE8)

    def lambda_1CFD():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1CFD)

    def lambda_1D12():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D12)

    def lambda_1D27():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D27)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_0D()
    OP_68(-24770, -3000, -50000, 2000)
    BeginChrThread(0x13, 0, 0, 18)
    BeginChrThread(0x14, 0, 0, 18)

    def lambda_1D70():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D70)

    def lambda_1D85():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1D85)

    def lambda_1D9A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1D9A)

    def lambda_1DAF():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1DAF)

    def lambda_1DC4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1DC4)

    def lambda_1DD9():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DD9)

    def lambda_1DEE():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DEE)
    Sleep(50)

    def lambda_1DFE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DFE)
    Sleep(50)

    def lambda_1E0E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E0E)
    Sleep(50)

    def lambda_1E1E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E1E)
    Sleep(50)

    def lambda_1E2E():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E2E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x3)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x13, 0, 0, 19)
    BeginChrThread(0x14, 0, 0, 19)
    OP_6F(0x79)
    Sleep(500)

    NpcTalk(
        0x101,
        "KeA",
        "#3501818V#5801F#5PThe bad men trapped us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501819V#0010F#6PIs this the end of the line...?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1854, 255, 100, 0)
    Sleep(800)

    NpcTalk(
        0xD,
        "Bold Voice",
        (
            "#3501820V#1POh, would you look at that?\x01",
            "The brats have nowhere else to run.\x02",
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(-24000, -3000, -49950, 4000)
    MoveCamera(40, 18, 0, 4000)

    def lambda_2015():
        OP_9B(0x0, 0xFE, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2015)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#3501821V#0001F#6PGarcia Rossi...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 45, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "#3501822VLong time no see, Special Support Section.\x02\x03",
            "#3501823VHeh. I was wondering why you in your fancy\x01",
            "getups looked so familiar.\x02\x03",
            "#3501824VHard to believe you actually got your grubby\x01",
            "hands on an invitation to the auction.\x01",
            "What's more, you had the balls to sneak in.\x02",
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
            "#3501825V#0004F#6PI don't remember seeing any rules against\x01",
            "police attending. Or did I miss that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501826V#3105F#11PHmph, I couldn't care less.\x02\x03",
            "#3501827V#3104FY'see, we don't turn away potential clients.\x02\x03",
            "#3501828V#3101FBut to be honest, I regret being as naive\x01",
            "as I was.\x02\x03",
            "#3501829VNever imagined you'd team up with Heiyue\x01",
            "to bring down our auction. Congrats.\x02",
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    NpcTalk(
        0x101,
        "KeA",
        "#3501830V#5805F#5PHey-you-eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501831V#0011F#6PWh-What are you talking about?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_24DE")

    ChrTalk(
        0x102,
        (
            "#3501832V#0103F#6PI assure you, we aren't connected\x01",
            "to Yin in any way, shape, or form.\x02\x03",
            "#3501833V#0101FWhy don't you ask your subordinates\x01",
            "for confirmation when they wake up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2664")

    label("loc_24DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_259A")

    ChrTalk(
        0x103,
        (
            "#3501834V#0203F#6PBut we are not connected to Yin...\x02\x03",
            "#3501835V#0211FYou can confirm that with your lackeys.\x01",
            "Granted, they might need some time to\x01",
            "wake up and readjust.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2664")

    label("loc_259A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2664")

    ChrTalk(
        0x104,
        (
            "#3501836V#0306F#6PMan, you seriously think we're connected to Yin?\x02\x03",
            "#3501837V#0301FI doubt you'll take my word for it, so try\x01",
            "askin' your grunts about it when they wake\x01",
            "up from their nap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2664")


    ChrTalk(
        0x105,
        (
            "#3501838V#0406F#5PIn actuality, I'd say we were the ones who\x01",
            "stopped him from crashing the party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501839V#3105F#11PHmm, that so?\x02\x03",
            "#3501840V#3104FWell, it's not like any of it matters anymore.\x02\x03",
            "#3501841VAll we gotta deal with is you making us\x01",
            "look like fools in front of our customers...\x02\x03",
            "#3501842V#3100FAnd trust me, we'll pay off that debt\x01",
            "in full. All right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501843V#0006F#6PI take it you won't surrender if\x01",
            "I pull out my badge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501844V#3104F#11PC'mon. The best part of the hunt\x01",
            "is hearing your prey scream when\x01",
            "you finally catch them.\x02\x03",
            "#3501845V#3100FDon't look too down...\x01",
            "I don't plan to kill you.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sleep(150)
    Sound(1857, 255, 100, 0)
    Fade(250)
    Sound(804, 0, 100, 0)
    BeginChrThread(0xD, 0, 0, 10)
    OP_0D()
    Sound(929, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7404", 0)
    Sleep(500)
    SetCameraDistance(18000, 20000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xD,
        (
            "#3501846V#3102F#11PI'll just toss you aside after crushing\x01",
            "a bone or two!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501847V#0110F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501848V#0201F#6PHe means business...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501849V#0301F#6PGeez, it ain't healthy to be doin'\x01",
            "all this at your age, old man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501850V#3104F#11PHeh, don't patronize me. Try your best to keep\x01",
            "me entertained, okay?\x02\x03",
            "#3501851V#3107FThe Killing Bear hasn't been on a hunt in ages!\x01",
            "Let's make this one to remember!!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501812V#0013F#6PCrap, here we go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#3501853V#0407F#5PHere he comes...!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16860, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_24(0x1DF)
    OP_C7(0x0, 0x4000)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_C7(0x1, 0x4000)
    EndChrThread(0xD, 0x0)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)
    Call(0, 38)
    Return()

    # Function_9_B5A end

    def Function_10_2B7E(): pass

    label("Function_10_2B7E")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2B86")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BA1")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_2B86")

    label("loc_2BA1")

    Return()

    # Function_10_2B7E end

    def Function_11_2BA2(): pass

    label("Function_11_2BA2")

    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)

    label("loc_2BB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BD2")
    OP_A1(0xFE, 0x3E8, 0x4, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_2BB5")

    label("loc_2BD2")

    Return()

    # Function_11_2BA2 end

    def Function_12_2BD3(): pass

    label("Function_12_2BD3")

    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2BDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BFA")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2BDB")

    label("loc_2BFA")

    Return()

    # Function_12_2BD3 end

    def Function_13_2BFB(): pass

    label("Function_13_2BFB")

    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2C03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C22")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2C03")

    label("loc_2C22")

    Return()

    # Function_13_2BFB end

    def Function_14_2C23(): pass

    label("Function_14_2C23")

    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2C2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C4A")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(1000)
    Jump("loc_2C2B")

    label("loc_2C4A")

    Return()

    # Function_14_2C23 end

    def Function_15_2C4B(): pass

    label("Function_15_2C4B")

    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2C53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C71")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(1000)
    Jump("loc_2C53")

    label("loc_2C71")

    Return()

    # Function_15_2C4B end

    def Function_16_2C72(): pass

    label("Function_16_2C72")

    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2C7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CD9")
    OP_A1(0xFE, 0x3E8, 0x1, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 80, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x2, 0x3)
    Sleep(1000)
    Jump("loc_2C7A")

    label("loc_2CD9")

    Return()

    # Function_16_2C72 end

    def Function_17_2CDA(): pass

    label("Function_17_2CDA")

    SetChrChipByIndex(0xFE, 0x3F)
    SetChrSubChip(0xFE, 0x0)

    label("loc_2CE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E7B")
    Sound(355, 0, 80, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 50, 850, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x1770, 0x3, 0x2, 0x3, 0x1)
    Sleep(1000)
    Jump("loc_2CE2")

    label("loc_2E7B")

    Return()

    # Function_17_2CDA end

    def Function_18_2E7C(): pass

    label("Function_18_2E7C")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EAA")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_2E8F")

    label("loc_2EAA")

    Return()

    # Function_18_2E7C end

    def Function_19_2EAB(): pass

    label("Function_19_2EAB")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EDC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_2EBE")

    label("loc_2EDC")

    Return()

    # Function_19_2EAB end

    def Function_20_2EDD(): pass

    label("Function_20_2EDD")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 13510, -3060, -32119, 90)

    def lambda_2EFB():
        OP_95(0xFE, 13210, -4000, -38990, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EFB)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 16)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_20_2EDD end

    def Function_21_2F1F(): pass

    label("Function_21_2F1F")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, 14500, -2080, -30160, 90)

    def lambda_2F3D():
        OP_95(0xFE, 14810, -4000, -37790, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F3D)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 0, 0, 17)
    WaitChrThread(0xFE, 0)
    Return()

    # Function_21_2F1F end

    def Function_22_2F61(): pass

    label("Function_22_2F61")

    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)

    def lambda_2F70():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F70)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_2F61 end

    def Function_23_2F8A(): pass

    label("Function_23_2F8A")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2F97():
        OP_95(0xFE, 12970, -4000, -48160, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F97)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Sleep(1000)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Sleep(200)
    OP_A1(0xFE, 0x3E8, 0x2, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_307A():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_307A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2F8A end

    def Function_24_3094(): pass

    label("Function_24_3094")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_30A1():
        OP_95(0xFE, 14350, -4000, -48920, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30A1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0x0, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xFE, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x3, 0xFF, 0xFF, 0x140, 14090, -4000, -40140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(1500)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_31AB():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31AB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_3094 end

    def Function_25_31C5(): pass

    label("Function_25_31C5")

    OP_93(0xFE, 0x0, 0x12C)
    Sleep(600)

    def lambda_31D4():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31D4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_31C5 end

    def Function_26_31EE(): pass

    label("Function_26_31EE")

    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_31FA():
        OP_95(0xFE, 5020, -4000, -50640, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31FA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_31EE end

    def Function_27_3214(): pass

    label("Function_27_3214")

    SetChrPos(0xFE, -5750, -4000, -50700, 270)

    def lambda_322A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_322A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3214 end

    def Function_28_323F(): pass

    label("Function_28_323F")

    SetChrPos(0xFE, -15280, -4000, -52250, 90)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)

    label("loc_3258")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32BB")
    Sleep(850)
    OP_A1(0xFE, 0x3E8, 0x1, 0x2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1200, 1300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x4)
    Jump("loc_3258")

    label("loc_32BB")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)

    def lambda_32D6():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32D6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_28_323F end

    def Function_29_32F0(): pass

    label("Function_29_32F0")

    SetChrPos(0xFE, -15780, -4000, -48270, 90)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_3309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_34AD")
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x1, 0x0, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x2, 0x1, 0xFE, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_33CF"),
        (1, "loc_3415"),
        (2, "loc_345B"),
        (SWITCH_DEFAULT, "loc_34A1"),
    )


    label("loc_33CF")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -6250, -4000, -50610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34A1")

    label("loc_3415")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -9950, -4000, -50630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34A1")

    label("loc_345B")

    PlayEffect(0x3, 0xFF, 0xFF, 0x140, -3370, -4000, -51680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34A1")

    label("loc_34A1")

    SetChrSubChip(0xFE, 0x4)
    Sleep(1200)
    Jump("loc_3309")

    label("loc_34AD")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_34C8():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34C8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_32F0 end

    def Function_30_34E2(): pass

    label("Function_30_34E2")

    SetChrPos(0xFE, -11920, -4000, -51900, 90)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)

    label("loc_34FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35D8")
    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_3521():
        OP_9B(0x1, 0xFE, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3521)
    Sound(532, 0, 80, 0)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x3, 0x4, 0x5)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFE, 0x140, 0, 750, 600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_3591():
        OP_A6(0xFE, 0x0, 0x28, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3591)
    WaitChrThread(0xFE, 1)
    Sleep(200)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFD170, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0xFA0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34FD")

    label("loc_35D8")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)

    def lambda_35FD():
        OP_97(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35FD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_34E2 end

    def Function_31_3617(): pass

    label("Function_31_3617")

    SetChrPos(0xFE, -9920, -4000, -51900, 270)

    label("loc_3628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36AF")
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Sleep(400)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_9D(0xFE, 0xFFFFDD28, 0xFFFFF060, 0xFFFF3544, 0x1F4, 0x1770)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)

    def lambda_3674():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3674)
    OP_A1(0xFE, 0x5DC, 0x4, 0x2, 0x4, 0x1, 0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3698")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36AA")
    Sleep(1)
    Jump("loc_3698")

    label("loc_36AA")

    Jump("loc_3628")

    label("loc_36AF")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_3617 end

    def Function_32_36B8(): pass

    label("Function_32_36B8")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -11560, -4000, -49320, 90)

    label("loc_36D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_375F")
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x3)

    def lambda_36F4():
        OP_9D(0xFE, 0xFFFFD6C0, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36F4)
    WaitChrThread(0xFE, 1)
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    Sleep(250)
    OP_A1(0xFE, 0x5DC, 0x2, 0xE, 0x3)
    Sleep(100)

    def lambda_3731():
        OP_9D(0xFE, 0xFFFFD2D8, 0xFFFFF060, 0xFFFF3F58, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3731)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36D8")

    label("loc_375F")

    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3789():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3789)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_32_36B8 end

    def Function_33_37A3(): pass

    label("Function_33_37A3")

    SetChrPos(0xFE, -8560, -4000, -49320, 270)

    label("loc_37B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3837")
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x4)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)

    def lambda_37D7():
        OP_9B(0x1, 0xFE, 0xB4, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37D7)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(400)

    def lambda_37F7():
        OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37F7)
    OP_A1(0xFE, 0x9C4, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    WaitChrThread(0xFE, 1)
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3832")
    Sleep(1)
    Jump("loc_3820")

    label("loc_3832")

    Jump("loc_37B4")

    label("loc_3837")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_37A3 end

    def Function_34_384B(): pass

    label("Function_34_384B")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -1840, -4000, -50740, 270)
    BeginChrThread(0xFE, 0, 0, 16)
    Return()

    # Function_34_384B end

    def Function_35_386B(): pass

    label("Function_35_386B")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -4610, -4000, -49060, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_35_386B end

    def Function_36_388B(): pass

    label("Function_36_388B")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -5870, -4000, -51790, 270)
    BeginChrThread(0xFE, 0, 0, 17)
    Return()

    # Function_36_388B end

    def Function_37_38AE(): pass

    label("Function_37_38AE")

    OP_25(0x1DF, 0x5A)
    Sleep(300)
    OP_25(0x1DF, 0x50)
    Sleep(300)
    OP_25(0x1DF, 0x46)
    Sleep(300)
    OP_25(0x1DF, 0x3C)
    Sleep(300)
    OP_25(0x1DF, 0x32)
    Sleep(300)
    OP_25(0x1DF, 0x28)
    Sleep(300)
    OP_25(0x1DF, 0x1E)
    Sleep(300)
    OP_25(0x1DF, 0x14)
    Sleep(300)
    OP_25(0x1DF, 0xA)
    Sleep(300)
    OP_24(0x1DF)
    Return()

    # Function_37_38AE end

    def Function_38_38F1(): pass

    label("Function_38_38F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31952.itc", 0x27)
    LoadChrToIndex("chr/ch31951.itc", 0x28)
    LoadChrToIndex("chr/ch31953.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00150.itc", 0x2C)
    LoadChrToIndex("chr/ch00151.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x2E)
    LoadChrToIndex("chr/ch00251.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("chr/ch00351.itc", 0x31)
    LoadChrToIndex("chr/ch00450.itc", 0x32)
    LoadChrToIndex("chr/ch00451.itc", 0x33)
    LoadChrToIndex("chr/ch02200.itc", 0x34)
    LoadChrToIndex("chr/ch02250.itc", 0x35)
    LoadChrToIndex("monster/ch67150.itc", 0x36)
    LoadChrToIndex("monster/ch67151.itc", 0x37)
    LoadChrToIndex("chr/ch02750.itc", 0x38)
    LoadChrToIndex("apl/ch50542.itc", 0x39)
    LoadChrToIndex("chr/ch02251.itc", 0x3A)
    LoadChrToIndex("chr/ch02252.itc", 0x3B)
    LoadChrToIndex("chr/ch02253.itc", 0x3C)
    LoadChrToIndex("chr/ch02254.itc", 0x3D)
    LoadChrToIndex("apl/ch50122.itc", 0x3E)
    LoadChrToIndex("chr/ch00357.itc", 0x3F)
    LoadChrToIndex("chr/ch02751.itc", 0x40)
    LoadChrToIndex("chr/ch02752.itc", 0x41)
    LoadChrToIndex("chr/ch00352.itc", 0x42)
    LoadChrToIndex("apl/ch50026.itc", 0x43)
    LoadChrToIndex("chr/ch31000.itc", 0x44)
    LoadEffect(0x0, "event\\ev305_00.eff")
    LoadEffect(0x1, "event\\ev306_00.eff")
    LoadEffect(0x2, "battle\\ms00001.eff")
    LoadEffect(0x3, "event\\ev314_00.eff")
    LoadEffect(0x4, "event\\ev315_00.eff")
    LoadEffect(0x5, "battle\\cr003300.eff")
    SoundLoad(930)
    SoundLoad(483)
    SetMapObjFlags(0x0, 0x4)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x1, 0x19)
    OP_49()
    SetChrPos(0x19, 17000, -5500, -63000, 270)
    OP_D3(0x19, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x400)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_70(0x1, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2E)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x32)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -26710, -4000, -49230, 90)
    SetChrPos(0x102, -28160, -4000, -48980, 90)
    SetChrPos(0x103, -29510, -4000, -50870, 90)
    SetChrPos(0x104, -26230, -4000, -50670, 90)
    SetChrPos(0x105, -28120, -4000, -51340, 90)
    SetChrPos(0x133, -29910, -4000, -49130, 90)
    SetChrChipByIndex(0x17, 0x40)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x4)
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0xE, 0x29)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0xD, 0x3C)
    SetChrSubChip(0xD, 0x3)
    SetChrChipByIndex(0x13, 0x3E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x3E)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x3E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, -20750, -4000, -51500, 270)
    SetChrPos(0x10, -17500, -4000, -48000, 270)
    SetChrPos(0xE, -18750, -4000, -50500, 270)
    SetChrPos(0x13, -19900, -4000, -47200, 270)
    SetChrPos(0x14, -17500, -4000, -52000, 270)
    SetChrPos(0x15, -19000, -4000, -50000, 270)
    SetChrPos(0xD, -21500, -4000, -50000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5046")
    OP_68(-24270, -3000, -50000, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18360, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19860, 2500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3501854V#0010F#6PHaaah... Haaaah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#3501855V#0406F#6PQuite the handful, wasn't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3501856V#11P#40WB-Boss...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501857V#11P#40WA-Are you all right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501858V#3104F#11P#40WHehehe... Hahahaha...\x02\x03",
            "#3501859V#3100FI was just planning to have an appetizer,\x01",
            "but that was the full course.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0xD, 0x1)
    Sleep(150)
    OP_68(-23830, -2900, -49830, 1000)
    Fade(250)
    BeginChrThread(0xD, 0, 0, 10)
    OP_0D()
    Sound(929, 0, 100, 0)
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
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_3FFC():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3FFC)

    def lambda_4015():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_4015)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x13, 0x36)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 19)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(531, 0, 100, 0)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)
    Sleep(500)

    def lambda_4064():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4064)

    def lambda_407D():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_407D)

    def lambda_4096():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4096)
    Sleep(250)
    Fade(500)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x14, 0x36)
    SetChrSubChip(0x14, 0x0)
    BeginChrThread(0x14, 0, 0, 19)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sound(531, 0, 100, 0)
    WaitChrThread(0x10, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0x14, 2)

    ChrTalk(
        0x133,
        "#3501860V#5805F#5PWow... The big man is already back up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501861V#0007F#6PTh-That can't be possible...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#3501862V#0401F#6P#NI thought Wald was strong, but he doesn't\x01",
            "even compare. Color me impressed...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#3501863V#0301F#6PAn absolute monster. That's what he is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501864V#3104F#11PHeh, what's with the trash talk?\x02\x03",
            "#3501865V#3102FA monster, you say? Funny you say that,\x01",
            "because aren't you the same as me...\x01",
            "Randolph Orlando?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0x12C)

    ChrTalk(
        0x104,
        "#3501866V#0310F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501867V#0005F#5PRandy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501868V#3102F#11PI was spot on, then.\x02\x03",
            "#3501869V#3104FYou come from one of the strongest jaeger corps\x01",
            "in western Zemuria, the Red Constellation.\x02\x03",
            "#3501870VThe Red Reaper, son of its infamous leader.\x01",
            "A kid given his own squadron, slaughtering\x01",
            "any foe who would stand in your way...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xD,
        (
            "#3501871V#3107F#11P#4SSon of the War God,\x01",
            "Randolph Orlando!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3501872V#0311F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501873V#0011F#6PSon of the War God?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3501874V#0208F#6P#NThe Red Constellation is one of the most\x01",
            "notorious jaeger corps in Zemuria...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#3501875V#0106F#6PNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501876V#0304F#5PHaha. Cat's outta the bag, eh?\x02\x03",
            "#3501877V#0312FYou must've studied, old man.\x01",
            "Got most of your facts straight.\x02\x03",
            "#3501878VThough, I wanna puke every time someone\x01",
            "calls me Son of the War God.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#3501879V#3102F#11PHeh. Can't help wondering how you ended\x01",
            "up in Crossbell. Must be quite the story.\x02\x03",
            "#3501880V#3104FYou know, when I was working for Zephyr,\x01",
            "the Red Constellation was always the biggest\x01",
            "pain in our ass.\x02\x03",
            "#3501881VIsn't this just perfect? How about we\x01",
            "have ourselves a little clash of destiny?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0xD,
        "#3501882V#3107F#11PYou and me! Right here, right now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3501883V#0311F#6PHave it your way...\x02",
    )

    CloseMessageWindow()
    OP_68(-23150, -3000, -49620, 1500)
    MoveCamera(44, 18, 0, 1500)
    SetChrChipByIndex(0x104, 0x31)
    SetChrSubChip(0x104, 0x0)

    def lambda_480A():
        OP_95(0xFE, -25200, -4000, -50000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_480A)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_93(0x104, 0x5A, 0x190)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#3501884V#0007F#6PHey, Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501885V#0303F#5P...Leave it to me, guys.\x02\x03",
            "#3501886V#0301FIf I take on this geezer, you might\x01",
            "be able to find an opening.\x02\x03",
            "#3501887V#0307FJust forget about me and focus on\x01",
            "gettin' out of here in one piece!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501888V#0010F#6PThat's not happening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501889V#0107F#6P#NR-Randy, you can't...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x103,
        "#3501890V#0201F#6P#NGet a hold of yourself!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrChipByIndex(0x104, 0x3F)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    Sound(1301, 255, 100, 0)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x1A, 1, 0, 72)
    MoveCamera(45, 18, 0, 2500)
    SetCameraDistance(15860, 2500)
    Sleep(200)
    PlayEffect(0x5, 0xFF, 0x104, 0x140, 0, 700, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(2000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    Sleep(300)
    Sound(1310, 255, 100, 0)
    SetCameraDistance(21360, 800)
    SetChrSubChip(0x104, 0x1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x0, 0x0, 0x104, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Sound(256, 0, 100, 0)
    OP_6F(0x79)
    Sound(325, 0, 100, 0)
    EndChrThread(0x1A, 0x1)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x101, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 58)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 59)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x133, 3, 0, 61)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x133, 3)
    Sleep(1300)

    ChrTalk(
        0xD,
        (
            "#3501892V#3104F#11PWar Cry...\x02\x03",
            "#3501893VA jaeger-exclusive technique that brings\x01",
            "out one's very own battle aura...\x02\x03",
            "#3501894V#3102FNow that's the spirit!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1858, 255, 100, 0)
    OP_68(-21510, -3000, -48550, 2500)
    SetCameraDistance(16860, 2500)
    Sleep(500)
    PlayEffect(0x5, 0xFF, 0xD, 0x140, 0, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    EndChrThread(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x3D)
    SetChrSubChip(0xD, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(2500)
    EndChrThread(0x101, 0x3)
    SetCameraDistance(21360, 800)
    SetChrSubChip(0xD, 0x4)
    BeginChrThread(0xD, 0, 0, 39)
    Sound(1840, 255, 100, 1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    CancelBlur(1000)
    PlayEffect(0x1, 0x1, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 40)

    ChrTalk(
        0x11,
        "#3501896V#11PU-Uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#3501897V#11PWe should probably back up...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 63)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 65)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 65)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    Sleep(500)
    OP_68(-25050, -3000, -48760, 1500)
    MoveCamera(45, 16, 0, 1500)
    OP_6E(540, 1500)
    SetCameraDistance(21360, 1500)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        "#3501898V#0410F#6PHmph... An incredible power, for sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3501899V#5801F#6P#NWooow, they're shining!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#3501900V#0010F#6PIf this keeps up...\x02",
    )

    CloseMessageWindow()
    Sound(846, 0, 100, 0)
    StopBGM(0x1388)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
    BeginChrThread(0x1A, 1, 0, 73)
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x133, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(1500)
    EndChrThread(0x101, 0x3)
    OP_82(0x0, 0x12C, 0x1770, 0x1F4)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    Sleep(750)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(750)
    EndChrThread(0x1A, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4F97():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F97)
    Sleep(50)

    def lambda_4FA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4FA7)
    Sleep(50)

    def lambda_4FB7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4FB7)
    Sleep(50)

    def lambda_4FC7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4FC7)
    Sleep(50)

    def lambda_4FD7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4FD7)
    Sleep(50)

    def lambda_4FE7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4FE7)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0x101,
        "#3501902V#0005F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501903V#0202F#6PHowling!\x02",
    )

    CloseMessageWindow()

    label("loc_5046")

    OP_68(-15500, -3000, -50000, 1500)
    MoveCamera(30, 26, 0, 1500)
    OP_6E(540, 1500)
    SetCameraDistance(19360, 1500)
    Sleep(500)
    SetChrPos(0x17, -5000, -4000, -50000, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    BeginChrThread(0x17, 3, 0, 43)
    WaitChrThread(0x17, 3)
    OP_68(-17000, -3000, -50000, 1000)
    OP_6F(0x79)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x14, 0x0)

    def lambda_50BC():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_50BC)

    def lambda_50D5():
        OP_A6(0xFE, 0x1E, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_50D5)
    Sound(847, 0, 100, 0)
    Sleep(250)
    Fade(500)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x3E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x3E)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0x13, 2)
    WaitChrThread(0x14, 2)
    BeginChrThread(0x17, 0, 0, 42)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x10, 0x13, 500)

    ChrTalk(
        0x10,
        "#3501905V#11PThe hell is that...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x14, 500)

    ChrTalk(
        0xE,
        "#3501906V#5PH-Hey! Don't be a chicken!\x02",
    )

    CloseMessageWindow()
    OP_64(0x11)
    OP_64(0x10)
    OP_64(0xE)
    Sound(2047, 255, 100, 0)

    ChrTalk(
        0x17,
        "#3501907V#1201FGRRRRRRRRR!\x02",
    )

    CloseMessageWindow()
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-17550, -3000, -50000, 1500)
    MoveCamera(45, 18, 0, 2500)
    SetCameraDistance(17860, 1000)
    Sound(2049, 255, 100, 0)
    BeginChrThread(0x17, 3, 0, 44)
    WaitChrThread(0x17, 3)
    OP_6F(0x79)
    OP_68(-18350, -3000, -50000, 1500)
    OP_6F(0x79)
    Fade(250)
    BeginChrThread(0xD, 0, 0, 10)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xD,
        "#3501911V#3110F#6PTch. Damn dog!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x1A, 1, 0, 74)
    Fade(1000)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-22770, -3000, -50000, 0)
    OP_68(-24270, -3000, -50000, 1200)
    MoveCamera(30, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19860, 0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x133, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501912V#0002F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501913V#0102F#6PIs that who I think it is...?!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x1A, 0x1)
    Fade(500)
    BeginChrThread(0x1A, 1, 0, 75)
    Sound(481, 0, 100, 0)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    SetChrBattleFlags(0x133, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    SetChrBattleFlags(0x17, 0x20)

    def lambda_5424():

        label("loc_5424")

        TurnDirection(0x101, 0x16, 500)
        Yield()
        Jump("loc_5424")

    QueueWorkItem2(0x101, 1, lambda_5424)

    def lambda_5436():

        label("loc_5436")

        TurnDirection(0x102, 0x16, 500)
        Yield()
        Jump("loc_5436")

    QueueWorkItem2(0x102, 1, lambda_5436)

    def lambda_5448():

        label("loc_5448")

        TurnDirection(0x103, 0x16, 500)
        Yield()
        Jump("loc_5448")

    QueueWorkItem2(0x103, 1, lambda_5448)

    def lambda_545A():

        label("loc_545A")

        TurnDirection(0x104, 0x16, 500)
        Yield()
        Jump("loc_545A")

    QueueWorkItem2(0x104, 1, lambda_545A)

    def lambda_546C():

        label("loc_546C")

        TurnDirection(0x105, 0x16, 500)
        Yield()
        Jump("loc_546C")

    QueueWorkItem2(0x105, 1, lambda_546C)

    def lambda_547E():

        label("loc_547E")

        TurnDirection(0x133, 0x16, 500)
        Yield()
        Jump("loc_547E")

    QueueWorkItem2(0x133, 1, lambda_547E)

    def lambda_5490():

        label("loc_5490")

        TurnDirection(0xD, 0x16, 500)
        Yield()
        Jump("loc_5490")

    QueueWorkItem2(0xD, 1, lambda_5490)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearMapObjFlags(0x1, 0x4)
    OP_D1(0x16, 0x1, "Null_Sheet")
    OP_68(2550, -2800, -63000, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(50000, 0)
    SetCameraDistance(27000, 2700)
    BeginChrThread(0x19, 3, 0, 69)
    SetChrPos(0x19, 35000, -5500, -63000, 270)
    BeginChrThread(0x19, 1, 0, 71)
    Sleep(1150)
    MoveCamera(309, 12, 0, 2700)
    Sleep(2800)
    Fade(500)
    SetChrPos(0x19, -26000, -5500, -63000, 270)
    OP_68(-32460, -2400, -57410, 0)
    MoveCamera(55, 30, 0, 0)
    SetCameraDistance(36000, 0)
    OP_68(-35310, -2400, -51820, 2500)
    MoveCamera(45, 12, 0, 2500)
    SetCameraDistance(19000, 2500)

    def lambda_5586():
        OP_9E(0xFE, 0xFFFF9A70, 0xFFFF30F8, 0x15F90, 0x2328, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5586)
    Sleep(1750)

    def lambda_55A4():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_55A4)
    Sleep(300)
    EndChrThread(0x19, 0x1)

    def lambda_55C5():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_55C5)
    Sleep(350)
    EndChrThread(0x19, 0x1)

    def lambda_55E6():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_55E6)
    WaitChrThread(0x19, 1)
    EndChrThread(0x19, 0x3)
    OP_82(0x0, 0x4B, 0x1194, 0x12C)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x133, 0x1)
    EndChrThread(0xD, 0x1)
    OP_93(0xD, 0x10E, 0x0)
    EndChrThread(0x1A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x16,
        (
            "#3501914V#1001F#5PCan you hurry it up? It's not\x01",
            "as if I have all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501915V#0000F#11PChief...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x133,
        "#3501916V#5810F#11POoooh, a boat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501917V#0202F#11PNice timing!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-22000, -3000, -50000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 1000)
    OP_0D()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xD,
        "#3501918V#3107F#4S#11PYOU AREN'T GETTING AWAY!\x02",
    )

    CloseMessageWindow()

    def lambda_5785():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5785)
    Sleep(50)

    def lambda_5795():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5795)
    Sleep(50)

    def lambda_57A5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57A5)
    Sleep(50)

    def lambda_57B5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57B5)
    Sleep(50)

    def lambda_57C5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57C5)
    Sleep(50)

    def lambda_57D5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_57D5)
    OP_68(-23250, -3000, -50000, 500)
    SetCameraDistance(17500, 500)
    Sound(1820, 255, 100, 0)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 54)
    OP_6F(0x79)
    SetCameraDistance(16500, 30000)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#3501920V#3110F#11PDamn it. You bastard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501921V#0311F#6PSorry to break it to ya, but it seems like\x01",
            "our 'clash of destiny' will have to wait.\x02\x03",
            "#3501922V#0303FMore importantly...were you aware of\x01",
            "what you guys were doin'?\x02\x03",
            "#3501923V#0301FTrying to auction off a freakin' kid...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#3501924V#3105F#11PWhat are you talking about?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501925V#0003F#6PThis girl was locked up in a trunk inside\x01",
            "the storeroom.\x02\x03",
            "#3501926V#0001FSurely you know what that means\x01",
            "for Revache & Co., right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x133,
        "#3501927V#5805F#2PHuh?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0xD,
        (
            "#3501928V#3107F#11PWhat the hell are you on about?!\x02\x03",
            "#3501929VThat trunk had a doll from the Rosenberg\x01",
            "Studio in it, not that kid...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#3501930V#0406F#6P#NMaybe so, but that doesn't change the fact.\x02\x03",
            "#3501931V#0402FDepending on how this whole debacle is\x01",
            "handled, it might be hard for you to get off\x01",
            "the hook, hmm? What a shame.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x16,
        (
            "#3501932V#1003F#2PSounds like the situation has gotten\x01",
            "more complicated than we thought.\x02\x03",
            "#3501933V#1001FHey, Revache. We'll need to have a\x01",
            "chat sometime soon.\x02\x03",
            "#3501934VI'll let you sort out this mess among\x01",
            "yourselves first, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#3501935V#3110F#11PGrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#3501936V#1007F#2PSpecial Support Section, retreat!\x01",
            "C'mon, move your asses!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501937V#0007F#5PYes, sir!\x02",
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
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x102, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_68(-33750, -2800, -50000, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19850, 0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x103, 3, 0, 48)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 47)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 51)
    Sleep(300)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1300)
    MoveCamera(30, 14, 0, 2500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    Sound(484, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(482, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 70)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x17, 3)
    Sleep(1000)
    OP_68(-30800, -2800, -50000, 3000)
    SetChrChipByIndex(0x10, 0x43)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x43)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x10, 0x1)
    SetChrFlags(0x11, 0x1)
    SetChrPos(0x10, -17970, -4000, -48470, 270)
    SetChrPos(0x11, -18820, -4000, -51400, 270)

    def lambda_5E73():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E73)

    def lambda_5E88():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5E88)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x10, 0x44)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x44)
    SetChrSubChip(0x11, 0x0)
    OP_6F(0x79)
    WaitChrThread(0x19, 3)

    ChrTalk(
        0x10,
        "#3501938V#11PDaaaaaamn it...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3501939V#11PDamn it! Aren't there any other boats?!\x02",
    )

    CloseMessageWindow()
    OP_68(-30800, -2800, -50000, 2000)
    MoveCamera(59, 14, 0, 2000)
    OP_6E(540, 2000)
    SetCameraDistance(16350, 2000)

    ChrTalk(
        0xD,
        "#3501940V#3110F#11P#50WOoooooooooohhh...\x02",
    )

    CloseMessageWindow()
    OP_6F(0x1)
    Sleep(500)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(56000, 4000)
    OP_82(0xC8, 0x0, 0x7D0, 0x5DC)

    ChrTalk(
        0xD,
        "#3501941V#3107F#4S#11P#14A#70WGYAHHHHHHHHHH!!!\x02",
    )

    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x3A2)
    OP_24(0x1E3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t112B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_38F1 end

    def Function_39_601F(): pass

    label("Function_39_601F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6038")
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Jump("Function_39_601F")

    label("loc_6038")

    Return()

    # Function_39_601F end

    def Function_40_6039(): pass

    label("Function_40_6039")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_605D")
    OP_82(0x0, 0x28, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_40_6039")

    label("loc_605D")

    Return()

    # Function_40_6039 end

    def Function_41_605E(): pass

    label("Function_41_605E")

    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6071")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6092")
    Sound(925, 0, 80, 0)
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_6071")

    label("loc_6092")

    Return()

    # Function_41_605E end

    def Function_42_6093(): pass

    label("Function_42_6093")

    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60C4")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("loc_60A6")

    label("loc_60C4")

    Return()

    # Function_42_6093 end

    def Function_43_60C5(): pass

    label("Function_43_60C5")

    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_60D0():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_60D0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x41)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    Sound(2058, 255, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Sound(925, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x2D)
    CancelBlur(750)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    Return()

    # Function_43_60C5 end

    def Function_44_613F(): pass

    label("Function_44_613F")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_6163():
        OP_9D(0xFE, 0xFFFFC0A5, 0xFFFFF060, 0xFFFF4372, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6163)
    Sleep(300)

    ChrTalk(
        0x10,
        "#3501909V#6PAaaah!\x05\x02",
    )

    BeginChrThread(0x10, 3, 0, 66)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    TurnDirection(0xFE, 0xE, 500)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_61CE():
        OP_9D(0xFE, 0xFFFFB35C, 0xFFFFF060, 0xFFFF3814, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61CE)
    Sleep(300)

    ChrTalk(
        0xE,
        "#3501910V#5PWhat the...?!\x05\x02",
    )

    BeginChrThread(0xE, 3, 0, 67)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 68)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_6249():
        OP_9D(0xFE, 0xFFFFC75C, 0xFFFFF060, 0xFFFF3CB0, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6249)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    Sound(925, 0, 100, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x1, 0x2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0x17, 0, 0, 42)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xE, 3)
    Return()

    # Function_44_613F end

    def Function_45_629A(): pass

    label("Function_45_629A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62B1")
    OP_A0(0xFE, 2000, 0x0, 0xFB)
    Jump("Function_45_629A")

    label("loc_62B1")

    Return()

    # Function_45_629A end

    def Function_46_62B2(): pass

    label("Function_46_62B2")

    SetChrFlags(0xFE, 0x4)

    def lambda_62BC():
        OP_95(0xFE, -30390, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62BC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_62EC():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62EC)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_6313():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6313)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_62B2 end

    def Function_47_6341(): pass

    label("Function_47_6341")

    SetChrFlags(0xFE, 0x4)

    def lambda_634B():
        OP_95(0xFE, -30390, -4000, -48700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_634B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_636E():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_636E)
    WaitChrThread(0xFE, 1)

    def lambda_638F():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_638F)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_47_6341 end

    def Function_48_63BD(): pass

    label("Function_48_63BD")

    SetChrFlags(0xFE, 0x4)

    def lambda_63C7():
        OP_95(0xFE, -30390, -4000, -51000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_63F7():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63F7)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_641E():
        OP_9D(0xFE, 0xFFFF6FA0, 0xFFFFEE08, 0xFFFF379C, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_641E)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_48_63BD end

    def Function_49_644C(): pass

    label("Function_49_644C")

    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_645E():
        OP_95(0xFE, -29700, -4000, -50000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_645E)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)
    Sound(804, 0, 100, 0)

    def lambda_6487():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6487)
    WaitChrThread(0xFE, 1)
    Sound(814, 0, 100, 0)

    def lambda_64AE():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF3CB0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64AE)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_644C end

    def Function_50_64DC(): pass

    label("Function_50_64DC")

    SetChrFlags(0xFE, 0x4)

    def lambda_64E6():
        OP_95(0xFE, -30300, -4000, -50250, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_64E6)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1)

    def lambda_6509():
        OP_9D(0xFE, 0xFFFF8396, 0xFFFFF380, 0xFFFF3DDC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6509)
    WaitChrThread(0xFE, 1)

    def lambda_652A():
        OP_9D(0xFE, 0xFFFF7388, 0xFFFFEE08, 0xFFFF41C4, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_652A)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_50_64DC end

    def Function_51_6558(): pass

    label("Function_51_6558")

    Sleep(1500)
    EndChrThread(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_656F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_656F)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_65B9():
        OP_9D(0xFE, 0xFFFFAC36, 0xFFFFF060, 0xFFFF44EE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65B9)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 0, 0, 41)

    def lambda_65FD():
        OP_95(0xFE, -25520, -4000, -48010, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65FD)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x40)
    SetChrSubChip(0xFE, 0x2)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_664C():
        OP_9D(0xFE, 0xFFFF92D2, 0xFFFFF380, 0xFFFF4B1A, 0x5DC, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_664C)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_669A():
        OP_9D(0xFE, 0xFFFF8454, 0xFFFFF380, 0xFFFF4B6A, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_669A)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x1)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_A1(0xFE, 0xFA0, 0x1, 0x2)
    Sound(854, 0, 100, 0)

    def lambda_66E1():
        OP_9D(0xFE, 0xFFFF7554, 0xFFFFEE08, 0xFFFF5AC4, 0x7D0, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66E1)
    OP_A1(0xFE, 0xFA0, 0x3, 0x3, 0x4, 0x0)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sound(925, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_51_6558 end

    def Function_52_6739(): pass

    label("Function_52_6739")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6766")

    def lambda_6749():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6749)
    WaitChrThread(0xFE, 2)
    Jump("Function_52_6739")

    label("loc_6766")

    Return()

    # Function_52_6739 end

    def Function_53_6767(): pass

    label("Function_53_6767")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x3B)
    SetChrSubChip(0xFE, 0x0)
    Sound(534, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(750)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrFlags(0xFE, 0x20)

    def lambda_67BA():
        OP_9B(0x0, 0xFE, 0x0, 0x546, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67BA)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    BeginChrThread(0xFE, 1, 0, 52)

    label("loc_67E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67F9")
    Sleep(1)
    Jump("loc_67E7")

    label("loc_67F9")

    Sleep(400)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x3C)
    SetChrSubChip(0xFE, 0x0)
    Sound(804, 0, 100, 0)

    def lambda_6817():
        OP_9D(0xFE, 0xFFFFAC04, 0xFFFFF060, 0xFFFF3CB0, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6817)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sleep(1350)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_6857():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6857)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x3D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_53_6767 end

    def Function_54_6874(): pass

    label("Function_54_6874")

    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)

    def lambda_688C():
        OP_9B(0x0, 0xFE, 0x0, 0x47E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_688C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x42)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0xFE, 1, 0, 52)
    OP_82(0x1F4, 0x0, 0x1770, 0x12C)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1000, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(834, 0, 100, 0)

    label("loc_6902")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6914")
    Sleep(1)
    Jump("loc_6902")

    label("loc_6914")

    EndChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x42)
    SetChrSubChip(0xFE, 0x0)
    Sound(532, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -23450, -3000, -50000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x4, 0x5)
    Call(0, 49)
    Return()

    # Function_54_6874 end

    def Function_55_6984(): pass

    label("Function_55_6984")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6991():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6991)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_55_6984 end

    def Function_56_69AE(): pass

    label("Function_56_69AE")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_69BB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69BB)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_56_69AE end

    def Function_57_69D8(): pass

    label("Function_57_69D8")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_69E5():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69E5)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_57_69D8 end

    def Function_58_6A02(): pass

    label("Function_58_6A02")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6A0F():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A0F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_58_6A02 end

    def Function_59_6A2C(): pass

    label("Function_59_6A2C")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6A39():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A39)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_59_6A2C end

    def Function_60_6A56(): pass

    label("Function_60_6A56")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6A63():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A63)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_60_6A56 end

    def Function_61_6A80(): pass

    label("Function_61_6A80")


    def lambda_6A85():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFED4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A85)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_61_6A80 end

    def Function_62_6A9A(): pass

    label("Function_62_6A9A")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6AB9():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AB9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_62_6A9A end

    def Function_63_6AD9(): pass

    label("Function_63_6AD9")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6AF8():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AF8)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x3)
    OP_64(0xFE)
    Return()

    # Function_63_6AD9 end

    def Function_64_6B18(): pass

    label("Function_64_6B18")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)

    def lambda_6B37():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B37)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_64_6B18 end

    def Function_65_6B57(): pass

    label("Function_65_6B57")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)

    def lambda_6B80():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B80)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x36)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 19)
    OP_64(0xFE)
    Return()

    # Function_65_6B57 end

    def Function_66_6BA6(): pass

    label("Function_66_6BA6")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -17000, -3000, -48000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_6C06():
        OP_9D(0xFE, 0xFFFFB1E0, 0xFFFFE0C0, 0xFFFF63C0, 0x5DC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C06)
    Sleep(1000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -19500, -5000, -42000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(927, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Return()

    # Function_66_6BA6 end

    def Function_67_6C6B(): pass

    label("Function_67_6C6B")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -18750, -3000, -50500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_6CCB():
        OP_9D(0xFE, 0xFFFFB636, 0xFFFFF060, 0xFFFF383C, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CCB)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_67_6C6B end

    def Function_68_6CF6(): pass

    label("Function_68_6CF6")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_82(0x64, 0x0, 0x1770, 0x1F4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, -20750, -3000, -51500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_6D56():
        OP_9D(0xFE, 0xFFFFADF8, 0xFFFFF060, 0xFFFF33F0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D56)
    WaitChrThread(0xFE, 1)
    OP_A1(0xFE, 0x9C4, 0x2, 0x2, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_68_6CF6 end

    def Function_69_6D81(): pass

    label("Function_69_6D81")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DDC")
    PlayEffect(0x4, 0xFF, 0xFE, 0x100, 0, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x14, 0x3E8, 0xA6)
    Sleep(166)
    Jump("Function_69_6D81")

    label("loc_6DDC")

    Return()

    # Function_69_6D81 end

    def Function_70_6DDD(): pass

    label("Function_70_6DDD")

    BeginChrThread(0x19, 2, 0, 69)

    def lambda_6DE8():
        OP_98(0xFE, 0x0, 0x0, 0x3A98, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6DE8)
    Sleep(1200)

    def lambda_6E05():
        OP_9E(0xFE, 0xFFFF0880, 0xFFFF7860, 0xFFFEA070, 0x2EE0, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6E05)
    WaitChrThread(0x19, 1)
    EndChrThread(0x19, 0x2)
    Return()

    # Function_70_6DDD end

    def Function_71_6E24(): pass

    label("Function_71_6E24")

    SetChrPos(0xFE, 35000, -5500, -63000, 270)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 35000, -5500, -63000)
    OP_9F(0x1, -17000, -5500, -63000)
    OP_9F(0x1, -28000, -5500, -63000)
    OP_9F(0x2, 0xFE, 10000, 0x6)
    Return()

    # Function_71_6E24 end

    def Function_72_6E6D(): pass

    label("Function_72_6E6D")

    Sound(930, 2, 0, 0)
    Sleep(100)
    OP_25(0x3A2, 0xA)
    Sleep(100)
    OP_25(0x3A2, 0x14)
    Sleep(100)
    OP_25(0x3A2, 0x1E)
    Sleep(100)
    OP_25(0x3A2, 0x28)
    Sleep(100)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x64)
    Return()

    # Function_72_6E6D end

    def Function_73_6EBA(): pass

    label("Function_73_6EBA")

    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x28)
    Sleep(200)
    OP_25(0x3A2, 0x1E)
    Sleep(200)
    OP_25(0x3A2, 0x14)
    Sleep(200)
    OP_25(0x3A2, 0xA)
    Sleep(200)
    OP_24(0x3A2)
    Return()

    # Function_73_6EBA end

    def Function_74_6EFD(): pass

    label("Function_74_6EFD")

    Sound(483, 2, 0, 0)
    Sleep(100)
    OP_25(0x1E3, 0xA)
    Sleep(100)
    OP_25(0x1E3, 0x14)
    Sleep(100)
    OP_25(0x1E3, 0x1E)
    Sleep(100)
    OP_25(0x1E3, 0x28)
    Sleep(100)
    OP_25(0x1E3, 0x32)
    Sleep(100)
    OP_25(0x1E3, 0x3C)
    Sleep(100)
    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x64)
    Return()

    # Function_74_6EFD end

    def Function_75_6F4A(): pass

    label("Function_75_6F4A")

    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x3C)
    Sleep(100)
    OP_25(0x1E3, 0x32)
    Sleep(100)
    OP_25(0x1E3, 0x28)
    Sleep(100)
    OP_25(0x1E3, 0x1E)
    Sleep(100)
    OP_25(0x1E3, 0x14)
    Sleep(100)
    OP_25(0x1E3, 0xA)
    Sleep(100)
    OP_24(0x1E3)
    Return()

    # Function_75_6F4A end

    def Function_76_6F8D(): pass

    label("Function_76_6F8D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Cruise Ship Schedule\x01\x01",
            " We'll be awaiting your next visit!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_76_6F8D end

    SaveToFile()

Try(main)
