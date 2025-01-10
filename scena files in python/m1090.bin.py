from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1090.bin",                # FileName
        "m1090",                    # MapName
        "m1090",                    # Location
        0x0072,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 2000, 0, 0, 0, 1, 114, 0, 1, 0, 2],
    )

    BuildStringList((
        "m1090",                  # 0
        "SE制御",                 # 1
        "bm1050",                 # 2
        "bm1060",                 # 3
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 0, 0, 180)
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

    # monster count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm1050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70001.dat", "ms70001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_128", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm1060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70001.dat", "ms70001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
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
        "monster/ch70050.itc",               # 10
        "monster/ch70050.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-8109,   -270,    2080,    0x185010E,    "BattleInfo_E4", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 3,   -8.109999656677246,    -0.27000001072883606,  0.07999999821186066,   4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   2.0274999141693115,    0.06750000268220901,   -0.03999999910593033,  1.0])

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_2B5",          # 01, 1
        "Function_2_2C5",          # 02, 2
        "Function_3_374",          # 03, 3
        "Function_4_BBE",          # 04, 4
        "Function_5_128B",         # 05, 5
        "Function_6_1301",         # 06, 6
        "Function_7_138B",         # 07, 7
        "Function_8_1429",         # 08, 8
        "Function_9_14E2",         # 09, 9
        "Function_10_15A8",        # 0A, 10
        "Function_11_15EB",        # 0B, 11
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B4")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_298")

    label("loc_2B4")

    Return()

    # Function_0_298 end

    def Function_1_2B5(): pass

    label("Function_1_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2C4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_2C4")

    Return()

    # Function_1_2B5 end

    def Function_2_2C5(): pass

    label("Function_2_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_306")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDA, 0xB5, 0xAB, 0xA, 0xC8, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "red")
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    Jump("loc_322")

    label("loc_306")

    SetMapObjFrame(0xFF, "allback", 0x2, "blue")
    SetMapObjFrame(0xFF, "sky", 0x2, "blue")

    label("loc_322")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_344")
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_35D")

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358")
    ClearChrFlags(0x9, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_358")

    SetChrFlags(0x9, 0x8000)

    label("loc_35D")

    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x9, 0x100)
    Sound(132, 1, 70, 0)
    Return()

    # Function_2_2C5 end

    def Function_3_374(): pass

    label("Function_3_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_54E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_END)), "loc_387")
    Return()

    label("loc_387")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_46A"),
        (SWITCH_DEFAULT, "loc_481"),
    )


    label("loc_46A")

    Sleep(500)
    OP_90(0x0, -15230, 0, -1400, 89)
    EventEnd(0x5)
    Return()

    label("loc_481")

    Battle("BattleInfo_128", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-15230, 1000, -1400, 0)
    OP_90(0x0, -15230, 0, -1400, 89)
    OP_90(0x1, -15230, 0, -1400, 89)
    OP_90(0x2, -15230, 0, -1400, 89)
    OP_90(0x3, -15230, 0, -1400, 89)
    OP_90(0x4, -15230, 0, -1400, 89)
    OP_90(0x5, -15230, 0, -1400, 89)
    OP_90(0x6, -15230, 0, -1400, 89)
    OP_90(0x7, -15230, 0, -1400, 89)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_543"),
        (1, "loc_546"),
        (SWITCH_DEFAULT, "loc_549"),
    )


    label("loc_543")

    EventEnd(0x5)
    Return()

    label("loc_546")

    OP_B7(0x0)
    Return()

    label("loc_549")

    Jump("loc_71A")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_END)), "loc_558")
    Return()

    label("loc_558")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is prowling around.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Leave alone]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_63B"),
        (SWITCH_DEFAULT, "loc_652"),
    )


    label("loc_63B")

    Sleep(500)
    OP_90(0x0, -15230, 0, -1400, 89)
    EventEnd(0x5)
    Return()

    label("loc_652")

    Battle("BattleInfo_E4", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-15230, 1000, -1400, 0)
    OP_90(0x0, -15230, 0, -1400, 89)
    OP_90(0x1, -15230, 0, -1400, 89)
    OP_90(0x2, -15230, 0, -1400, 89)
    OP_90(0x3, -15230, 0, -1400, 89)
    OP_90(0x4, -15230, 0, -1400, 89)
    OP_90(0x5, -15230, 0, -1400, 89)
    OP_90(0x6, -15230, 0, -1400, 89)
    OP_90(0x7, -15230, 0, -1400, 89)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_714"),
        (1, "loc_717"),
        (SWITCH_DEFAULT, "loc_71A"),
    )


    label("loc_714")

    EventEnd(0x5)
    Return()

    label("loc_717")

    OP_B7(0x0)
    Return()

    label("loc_71A")

    FadeToDark(0, 0, -1)
    OP_68(-9050, 2800, -1080, 0)
    MoveCamera(51, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15070, 0)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster in Stargazer's Tower!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xA, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_878")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -8340, 1080, 1560, 180)
    SetChrPos(0x102, -6440, 1080, 180, 252)
    SetChrPos(0x103, -7160, 1080, -2060, 324)
    SetChrPos(0x104, -9520, 1080, -2060, 36)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_862")
    SetChrPos(0x10A, -10240, 1080, 180, 108)
    Jump("loc_873")

    label("loc_862")

    SetChrPos(0x109, -10240, 1080, 180, 108)

    label("loc_873")

    Jump("loc_8BC")

    label("loc_878")

    SetChrPos(0x101, -8340, 1080, 1550, 180)
    SetChrPos(0x102, -6340, 1080, -450, 270)
    SetChrPos(0x103, -8340, 1080, -2450, 0)
    SetChrPos(0x104, -10340, 980, -450, 90)

    label("loc_8BC")

    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D")

    ChrTalk(
        0x101,
        "#5P#0005FA craft book? It looks pretty beat up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_949")

    label("loc_90D")


    ChrTalk(
        0x101,
        "#5P#0000FThis craft book looks as old as the last one.\x02",
    )

    CloseMessageWindow()

    label("loc_949")


    ChrTalk(
        0x103,
        (
            "#12P#0203FThis book contains details on\x01",
            "combining crafts during battle.\x02\x03",
            "#0202FIf I am reading this correctly, it resembles\x01",
            "Randy and Elie's fighting styles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#0305FHuh, would you look at that?\x02\x03",
            "#0300FIt might take a lil' bit of practice to\x01",
            "use, but how 'bout it, Mademois-Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#0100FSure, we can give it a try.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF1")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_AF1")

    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x14E)
    AddCraft(0x3, 0x14E)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie and Randy learned \x07\x02",
            "[Riot Star]\x07\x05",
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
    SetScenarioFlags(0x79, 3)
    SetScenarioFlags(0xD8, 7)
    OP_29(0x32, 0x4, 0x10)
    OP_29(0x32, 0x4, 0x2)
    OP_29(0x32, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE(0x20, 0x0)
    EventEnd(0x5)
    Return()

    # Function_3_374 end

    def Function_4_BBE(): pass

    label("Function_4_BBE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    FadeToBright(1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(7310, 1950, -3420, 0)
    MoveCamera(45, 9, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(38570, 0)
    OP_68(1970, 1950, 1920, 6000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-4280, 4050, 3570, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(37330, 0)
    OP_68(-4280, 650, 3570, 6000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x102, 3, 0, 6)
    BeginChrThread(0x103, 3, 0, 7)
    BeginChrThread(0x104, 3, 0, 8)
    BeginChrThread(0x109, 3, 0, 9)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-5470, 2650, -240, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25390, 0)
    SetCameraDistance(20390, 4000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x102,
        "#2201340V#0105F#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#2201341V#0501F#6PWe finally made it to the top...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#2201342V#0307F#6PWhere the hell did that\x01",
            "bastard run off to?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#2201343V#0007F#5PTio, scan the area!\x02",
    )

    CloseMessageWindow()

    def lambda_E5B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E5B)

    def lambda_E68():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E68)
    Sleep(100)

    def lambda_E78():
        OP_93(0xFE, 0x64, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E78)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        "#2201344V#0201F#12PRoger!\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x3E8)
    Sleep(150)
    Sound(1203, 255, 100, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0x8, 2, 0, 10)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    EndChrThread(0x8, 0x1)

    ChrTalk(
        0x103,
        "#2201345V#0205F#12PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#2201346V#0001F#5PDid you find him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#2201347V#0208F#12PI am detecting a weak signal, but\x01",
            "it is coming from the ground floor.\x02\x03",
            "#2201348V#0206FHe must have jumped directly off\x01",
            "the roof.\x02",
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#2201349V#0011F#5PJumped?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#2201350V#0105F#5PImpossible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#2201351V#0301F#1PTch, he's a monster, all right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#2201352V#0506F#6PWell, this was an unexpected\x01",
            "turn of events...\x02\x03",
            "#2201353V#0501FThis Yin isn't someone to be\x01",
            "taken lightly.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(19890, 2000)
    OP_6F(0x79)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 11)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x8, 0x0)
    OP_24(0x348)
    SetScenarioFlags(0x5D, 0)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_BBE end

    def Function_5_128B(): pass

    label("Function_5_128B")

    SetChrPos(0xFE, -2570, 0, 14660, 0)
    OP_95(0xFE, -6880, 0, 13090, 4000, 0x0)
    OP_95(0xFE, -11050, 0, 10090, 4000, 0x0)
    OP_95(0xFE, -13850, 0, 5760, 4000, 0x0)
    OP_95(0xFE, -13760, 0, 1000, 4000, 0x0)
    OP_95(0xFE, -4030, 1530, -60, 4000, 0x0)
    Return()

    # Function_5_128B end

    def Function_6_1301(): pass

    label("Function_6_1301")

    SetChrPos(0xFE, 1350, 0, 15180, 0)
    OP_95(0xFE, -2570, 0, 14660, 4000, 0x0)
    OP_95(0xFE, -6880, 0, 13090, 4000, 0x0)
    OP_95(0xFE, -11050, 0, 10090, 4000, 0x0)
    OP_95(0xFE, -13850, 0, 5760, 4000, 0x0)
    OP_95(0xFE, -13760, 0, 1000, 4000, 0x0)
    OP_95(0xFE, -4730, 1420, 1310, 4000, 0x0)
    Return()

    # Function_6_1301 end

    def Function_7_138B(): pass

    label("Function_7_138B")

    SetChrPos(0xFE, 3560, 0, 18520, 0)
    OP_95(0xFE, 1350, 0, 15180, 4000, 0x0)
    OP_95(0xFE, -2570, 0, 14660, 4000, 0x0)
    OP_95(0xFE, -6880, 0, 13090, 4000, 0x0)
    OP_95(0xFE, -11050, 0, 10090, 4000, 0x0)
    OP_95(0xFE, -13850, 0, 5760, 4000, 0x0)
    OP_95(0xFE, -13760, 0, 1000, 4000, 0x0)
    OP_95(0xFE, -5300, 1270, -1140, 4000, 0x0)
    Return()

    # Function_7_138B end

    def Function_8_1429(): pass

    label("Function_8_1429")

    SetChrPos(0xFE, 450, 0, 21060, 0)
    OP_95(0xFE, 3560, 0, 18520, 4000, 0x0)
    OP_95(0xFE, 1350, 0, 15180, 4000, 0x0)
    OP_95(0xFE, -2570, 0, 14660, 4000, 0x0)
    OP_95(0xFE, -6880, 0, 13090, 4000, 0x0)
    OP_95(0xFE, -11050, 0, 10090, 4000, 0x0)
    OP_95(0xFE, -13850, 0, 5760, 4000, 0x0)
    OP_95(0xFE, -13760, 0, 1000, 4000, 0x0)
    OP_95(0xFE, -6480, 1080, 920, 4000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Return()

    # Function_8_1429 end

    def Function_9_14E2(): pass

    label("Function_9_14E2")

    SetChrPos(0xFE, -3390, -1070, 21000, 0)
    OP_95(0xFE, 450, 0, 21060, 4000, 0x0)
    OP_95(0xFE, 3560, 0, 18520, 4000, 0x0)
    OP_95(0xFE, 1350, 0, 15180, 4000, 0x0)
    OP_95(0xFE, -2570, 0, 14660, 4000, 0x0)
    OP_95(0xFE, -6880, 0, 13090, 4000, 0x0)
    OP_95(0xFE, -11050, 0, 10090, 4000, 0x0)
    OP_95(0xFE, -13850, 0, 5760, 4000, 0x0)
    OP_95(0xFE, -13760, 0, 1000, 4000, 0x0)
    OP_95(0xFE, -6210, 1080, -370, 4000, 0x0)
    Return()

    # Function_9_14E2 end

    def Function_10_15A8(): pass

    label("Function_10_15A8")

    OP_25(0x348, 0x5A)
    Sleep(100)
    OP_25(0x348, 0x50)
    Sleep(100)
    OP_25(0x348, 0x46)
    Sleep(100)
    OP_25(0x348, 0x3C)
    Sleep(100)
    OP_25(0x348, 0x32)
    Sleep(100)
    OP_25(0x348, 0x28)
    Sleep(100)
    OP_25(0x348, 0x1E)
    Sleep(100)
    OP_25(0x348, 0x14)
    Sleep(100)
    OP_25(0x348, 0xA)
    Sleep(100)
    OP_24(0x348)
    Return()

    # Function_10_15A8 end

    def Function_11_15EB(): pass

    label("Function_11_15EB")

    OP_25(0x84, 0x3C)
    Sleep(100)
    OP_25(0x84, 0x32)
    Sleep(100)
    OP_25(0x84, 0x28)
    Sleep(100)
    OP_25(0x84, 0x1E)
    Sleep(100)
    OP_25(0x84, 0x14)
    Sleep(100)
    OP_25(0x84, 0xA)
    Sleep(100)
    OP_24(0x84)
    Return()

    # Function_11_15EB end

    SaveToFile()

Try(main)
