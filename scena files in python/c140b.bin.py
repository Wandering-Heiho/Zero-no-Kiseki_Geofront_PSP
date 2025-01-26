from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c140b.bin",                # FileName
        "c140b",                    # MapName
        "c140b",                    # Location
        0x002E,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 1, 0, 2],
    )

    BuildStringList((
        "c140b",                  # 0
        "Wazy",                   # 1
        "Wald",                   # 2
        "Disguised Lloyd",        # 3
        "Abbas",                  # 4
        "Grace",                  # 5
        "Young Man in Blue",      # 6
        "Young Man in Blue",      # 7
        "Young Man in Blue",      # 8
        "Dino",                   # 9
        "Young Man in Red",       # 10
        "Young Man in Red",       # 11
        "Young Man in Red",       # 12
        "Young Man in Red",       # 13
        "Mafioso",                # 14
        "Mafioso",                # 15
        "Mafioso",                # 16
        "Mafioso",                # 17
        "Bat",                    # 18
        "BC141b",                 # 19
        "Central Square",         # 20
        "West Street",            # 21
        "Administrative District",# 22
        "Residential District",   # 23
        "Entertainment District", # 24
        "East Street",            # 25
        "Downtown District",      # 26
        "Harbor District",        # 27
        "IBC",                    # 28
        "Station Street",         # 29
        "Back Alley",             # 30
        "Ursula Road",            # 31
        "East Crossbell Highway", # 32
        "West Crossbell Highway", # 33
        "Mainz Mountain Path",    # 34
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 2, 13, 180)
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
        "BattleInfo_E4", 0x0002, 3, 6, 180, 0, 0, 55, 0, "BC141b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31000.dat", "ms31100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7507", "ed7403", "ATBonus_94"),
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
    DeclNpc(0,       0,       0,       0,    470,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  3,  0x0000)

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

    ScpFunction((
        "Function_0_658",          # 00, 0
        "Function_1_710",          # 01, 1
        "Function_2_734",          # 02, 2
        "Function_3_74C",          # 03, 3
        "Function_4_8E0",          # 04, 4
        "Function_5_3D8E",         # 05, 5
        "Function_6_3F1A",         # 06, 6
        "Function_7_4046",         # 07, 7
        "Function_8_40E3",         # 08, 8
        "Function_9_414E",         # 09, 9
        "Function_10_41B9",        # 0A, 10
        "Function_11_41F6",        # 0B, 11
        "Function_12_4233",        # 0C, 12
        "Function_13_4270",        # 0D, 13
        "Function_14_4286",        # 0E, 14
        "Function_15_42C7",        # 0F, 15
        "Function_16_431F",        # 10, 16
        "Function_17_437E",        # 11, 17
        "Function_18_439D",        # 12, 18
        "Function_19_7F14",        # 13, 19
        "Function_20_7F55",        # 14, 20
        "Function_21_7F96",        # 15, 21
    ))


    def Function_0_658(): pass

    label("Function_0_658")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_698"),
        (1, "loc_6A4"),
        (2, "loc_6B0"),
        (3, "loc_6BC"),
        (4, "loc_6C8"),
        (5, "loc_6D4"),
        (6, "loc_6E0"),
        (SWITCH_DEFAULT, "loc_6EC"),
    )


    label("loc_698")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_6F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F8")

    label("loc_70F")

    Return()

    # Function_0_658 end

    def Function_1_710(): pass

    label("Function_1_710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_724")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_733")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_733")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 18)

    label("loc_733")

    Return()

    # Function_1_710 end

    def Function_2_734(): pass

    label("Function_2_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747")
    OP_70(0x7, 0x0)
    Jump("loc_74B")

    label("loc_747")

    OP_70(0x7, 0x1E)

    label("loc_74B")

    Return()

    # Function_2_734 end

    def Function_3_74C(): pass

    label("Function_3_74C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_836")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_7CC")
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
    Jump("loc_831")

    label("loc_7CC")

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

    label("loc_831")

    Jump("loc_8D4")

    label("loc_836")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...What? I'm not on the clock, so screw off.\x01",
            "They don't pay me enough to make witty\x01",
            "remarks to players using debug.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_8D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_74C end

    def Function_4_8E0(): pass

    label("Function_4_8E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30800.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31700.itc", 0x20)
    LoadChrToIndex("chr/ch31800.itc", 0x21)
    LoadChrToIndex("chr/ch00400.itc", 0x22)
    LoadChrToIndex("chr/ch00450.itc", 0x23)
    LoadChrToIndex("chr/ch00451.itc", 0x24)
    LoadChrToIndex("chr/ch02100.itc", 0x25)
    LoadChrToIndex("apl/ch50019.itc", 0x26)
    LoadChrToIndex("chr/ch02150.itc", 0x27)
    LoadChrToIndex("chr/ch02151.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch31000.itc", 0x2E)
    LoadChrToIndex("chr/ch31001.itc", 0x2F)
    LoadChrToIndex("chr/ch31050.itc", 0x30)
    LoadChrToIndex("chr/ch31051.itc", 0x31)
    LoadChrToIndex("chr/ch31100.itc", 0x32)
    LoadChrToIndex("chr/ch31101.itc", 0x33)
    LoadChrToIndex("chr/ch31152.itc", 0x34)
    LoadChrToIndex("chr/ch31151.itc", 0x35)
    LoadChrToIndex("chr/ch08800.itc", 0x36)
    LoadChrToIndex("apl/ch50020.itc", 0x37)
    LoadChrToIndex("apl/ch50021.itc", 0x38)
    LoadChrToIndex("apl/ch50022.itc", 0x39)
    LoadChrToIndex("apl/ch50023.itc", 0x3A)
    LoadChrToIndex("apl/ch50024.itc", 0x3B)
    LoadChrToIndex("apl/ch50025.itc", 0x3C)
    LoadChrToIndex("apl/ch50027.itc", 0x3D)
    LoadChrToIndex("apl/ch50029.itc", 0x3E)
    LoadChrToIndex("chr/ch00456.itc", 0x3F)
    LoadChrToIndex("chr/ch06800.itc", 0x40)
    OP_68(18500, 500, -25000, 0)
    MoveCamera(32, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40500, 0)
    SetChrPos(0x0, -10000, 0, 5000, 0)
    SetChrPos(0x1, -10000, 0, 5000, 0)
    SetChrPos(0x2, -10000, 0, 5000, 0)
    SetChrPos(0x3, -10000, 0, 5000, 0)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x15, 1100, 0, 13000, 180)
    SetChrPos(0x16, 2500, 0, 13000, 180)
    SetChrPos(0x17, 1100, 0, 14400, 180)
    SetChrPos(0x18, 2500, 0, 14400, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    LoadEffect(0x0, "battle\\ms00000.eff")
    LoadEffect(0x1, "event\\eva01_01.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#0401187V\x07\x05",
            "Three days have passed since.\x02\x03",
            "#0401188VThe confrontation between the rival gangs has\x01",
            "fortunately died down.\x02\x03",
            "#0401189VThe Downtown District has been enveloped by a\x01",
            "tranquil atmosphere. An atmosphere so peaceful,\x01",
            "that it has become uncomfortable.\x02\x03",
            "#0401190VThen...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(27, 4, 0, 6000)
    SetCameraDistance(45500, 6000)
    PlayBGM("ed7302", 0)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_C58():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C58)
    Sleep(50)

    def lambda_C75():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_C75)
    Sleep(50)

    def lambda_C92():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_C92)
    Sleep(50)

    def lambda_CAF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CAF)
    OP_6F(0x50)
    Fade(1000)
    OP_68(1800, 1000, 2700, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(21500, 4000)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x10)

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401191V\x07\x00",
            "#5PTch... It's too quiet around here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401192V#5PWe went through all of that effort, and those\x01",
            "dumbasses still haven't torn each other apart?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x15, 500)

    NpcTalk(
        0x18,
        "Man in Shades",
        (
            "#0401193V#5PHaha... Don't you worry. Those guys\x01",
            "are doused in gasoline at this point.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        (
            "#0401194V#5POne small spark, and everything will be up in flames.\x01",
            "Those morons won't even know what hit 'em.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EC9():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_EC9)
    Sleep(100)

    def lambda_ED9():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_ED9)
    Sleep(50)
    TurnDirection(0x17, 0x16, 500)
    Sleep(300)

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401195V#2PViper or Testament. Doesn't matter which one.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401196V#2PAs soon as you see one, kick his ass.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401197V#6PAnd for your own sake, you'd better not get caught.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401198V#6PUse a slingshot for a Saber Viper, and just bash\x01",
            "one of those Testaments guys from behind.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401199V#1PGot it.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        "#0401200V#5PHaha. Let the hunt begin, boys.\x02",
    )

    CloseMessageWindow()
    OP_E5()

    def lambda_10B9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_10B9)
    Sleep(100)

    def lambda_10C9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_10C9)
    Sleep(50)

    def lambda_10D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_10D9)
    Sleep(50)

    def lambda_10E9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10E9)
    WaitChrThread(0x15, 2)

    def lambda_10FA():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10FA)
    WaitChrThread(0x16, 2)
    Sleep(100)

    def lambda_111B():
        OP_97(0xFE, 0x5DC, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_111B)
    WaitChrThread(0x18, 2)
    Sleep(100)

    def lambda_113C():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_113C)
    WaitChrThread(0x17, 2)
    Sleep(100)

    def lambda_115D():
        OP_97(0xFE, 0xBB8, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_115D)
    SetCameraDistance(23500, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x15, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x18, 0x1)
    OP_68(-19000, 2000, -10300, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x15, 10600, -6500, -31800, 135)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrChipByIndex(0xA, 0x36)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -19000, -1460, -5300, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetCameraDistance(21500, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_122C():
        OP_95(0xFE, -19000, 0, -10300, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_122C)
    WaitChrThread(0xA, 1)
    OP_6B(0xA)

    def lambda_124D():
        OP_95(0xFE, -12400, 0, -12800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_124D)
    MoveCamera(55, 33, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_1276():
        OP_95(0xFE, -12400, -3050, -23500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1276)
    MoveCamera(30, 23, 0, 3000)
    WaitChrThread(0xA, 1)

    def lambda_129F():
        OP_95(0xFE, -2800, -3950, -27800, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_129F)
    WaitChrThread(0xA, 1)

    def lambda_12BD():
        OP_95(0xFE, 8100, -6350, -37500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12BD)
    MoveCamera(55, 23, 0, 6000)
    WaitChrThread(0xA, 1)

    def lambda_12E6():
        OP_95(0xFE, 13600, -6500, -38400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12E6)
    Sleep(1700)
    OP_6B(0xFF)
    Fade(500)
    OP_68(11900, -5500, -38400, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(13600, -5500, -38400, 1500)
    MoveCamera(55, 19, 0, 1500)
    SetCameraDistance(19000, 1500)
    OP_A7(0x15, 0x37, 0x37, 0x37, 0xFF, 0x0)

    def lambda_1369():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1369)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_1382():
        OP_95(0xFE, 11100, -6500, -31800, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1382)
    WaitChrThread(0x15, 1)

    def lambda_13A0():
        OP_95(0xFE, 11900, -6500, -38400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13A0)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0x5A, 0x0)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)
    SetChrSubChip(0x15, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x15, 0x2)
    Sleep(300)
    SetChrFlags(0x15, 0x20)

    def lambda_13E8():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6A00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_13E8)
    SetChrSubChip(0x15, 0x3)
    PlayEffect(0x0, 0xFF, 0xA, 0x0, 200, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_E6()
    SetChrChipByIndex(0xA, 0x38)
    SetChrSubChip(0xA, 0x0)

    def lambda_1446():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1446)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(830, 0, 100, 0)

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0401201V#2P#4SGah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 2)
    WaitChrThread(0x15, 1)
    Sleep(300)

    def lambda_14AC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_14AC)
    SetChrSubChip(0xA, 0x1)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0xA, 0x2)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x20)

    def lambda_150A():
        OP_96(0xFE, 0x2CEC, 0xFFFFE69C, 0xFFFF6A00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_150A)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sleep(300)

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401202V#6PHaha... One tiny blue bunny down.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x17, 3, 0, 15)
    Sleep(400)
    BeginChrThread(0x16, 3, 0, 14)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 16)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x18, 3)

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401203VHaha... What a pathetic piece of trash.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        (
            "#0401204V#11PWe don't got time to waste. How 'bout\x01",
            "you rough him up a little bit?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401205V#11PJust be sure to not kill him.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401206V#6PBusiness is business. Hope you\x01",
            "don't hold a grudge against us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)

    def lambda_16E8():
        OP_96(0xFE, 0x3070, 0xFFFFE69C, 0xFFFF6B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_16E8)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrSubChip(0x15, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x15, 0x2)
    Sleep(500)
    StopBGM(0x5DC)
    Sound(1091, 255, 100, 0)

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0401207V#8AAs if I'd let you!\x02",
    )

    Sleep(800)
    MoveCamera(53, 17, 0, 500)
    SetCameraDistance(17000, 500)
    Fade(100)
    SetChrChipByIndex(0xA, 0x39)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)

    def lambda_17AF():
        TurnDirection(0xFE, 0x15, 1000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_17AF)
    Sleep(100)
    SetChrSubChip(0x15, 0x3)
    Sleep(50)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    PlayEffect(0x1, 0xFF, 0xA, 0x40, -300, 1000, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sound(830, 0, 100, 0)
    Sound(511, 0, 100, 0)
    OP_6F(0x50)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)

    def lambda_1824():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1824)

    def lambda_183D():
        OP_A6(0xFE, 0x0, 0x14, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_183D)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0xA, 2)
    WaitChrThread(0x15, 2)
    SetCameraDistance(18500, 500)
    PlayEffect(0x1, 0xFF, 0xA, 0x40, -300, 1000, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x3A)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x19, 0x3E)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 12400, -5800, -38400, 0)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    BeginChrThread(0x19, 3, 0, 17)
    Sound(511, 0, 100, 0)
    Sound(532, 0, 100, 0)

    def lambda_1949():
        OP_9C(0xFE, 0xFFFFE4A8, 0xFFFFE69C, 0xFFFFE4A8, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1949)
    SetChrChipByIndex(0x15, 0x3B)
    SetChrSubChip(0x15, 0x0)

    def lambda_196E():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_196E)

    def lambda_1987():
        OP_9D(0xFE, 0x2B5C, 0xFFFFE69C, 0xFFFF68D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1987)
    WaitChrThread(0x15, 1)

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401208V#6PWhat?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401209V#11PWhat the hell?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xA, 0x3C)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        "#0401210V#11PI'm a little surprised.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xA,
        "Young Man in Blue",
        (
            "#0401211V#11PI really didn't think we'd get you\x01",
            "to fall for the bait this easily.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Man in Shades",
        "#0401212VWh-Who the hell is this guy?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x800)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 13600, -6500, -38400, 270)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 13)
    BeginChrThread(0x101, 3, 0, 13)

    def lambda_1BA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1BA3)

    def lambda_1BB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BB4)
    Sound(534, 0, 100, 0)
    WaitChrThread(0xA, 2)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    WaitChrThread(0x101, 3)
    ClearChrFlags(0x101, 0x800)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0401213V#0006F#11PIf it were up to me, I'd be cuffing you and\x01",
            "taking you down to headquarters already.\x02\x03",
            "#0401214V#0001FBut I'm not sure how the department would\x01",
            "feel about using a sting operation as evidence.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401215V#6PD-Don't tell me he's...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401216V#11PHe's a cop?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 16050, -1100, -34600, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    NpcTalk(
        0x8,
        "Young Man's Voice",
        (
            "#0401217V#12PHaha. Not to worry, boys.\x01",
            "He's just a special helper.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 14500, -1600, -34000, 180)
    SetChrPos(0x103, 14400, -1600, -32700, 180)
    SetChrPos(0x104, 15600, -1300, -32299, 180)
    OP_68(15200, -500, -35200, 2000)
    MoveCamera(53, 13, 0, 2000)
    SetCameraDistance(18000, 2000)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)

    def lambda_1E8B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1E8B)
    Sleep(50)

    def lambda_1E9B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1E9B)
    Sleep(50)

    def lambda_1EAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1EAB)
    Sleep(50)

    def lambda_1EBB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1EBB)
    OP_6F(0x79)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)

    ChrTalk(
        0x104,
        (
            "#0401218V#5P#0309FDude, are you serious? How the\x01",
            "hell'd they fall for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401219V#5P#0202FLloyd's prediction was impeccable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401220V#5P#0101FAre you all right, Lloyd?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401221V#0004F#11PYeah, I'm fine.\x02\x03",
            "#0401222V#0000FPutting that shock-absorbing pad under my\x01",
            "hood was definitely a good call, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    OP_68(13600, -5500, -38400, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    Sleep(500)

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401223VDamn it...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        (
            "#0401224VIf the boss finds out that\x01",
            "we blew our cover like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401225V#0400F#6PWell, then, gentlemen. That raises the question...\x01",
            "What will be your next move?\x02\x03",
            "#0401226V#0404FSurrender peacefully now, and I may be merciful\x01",
            "towards your misdeeds...\x02\x03",
            "#0401227V#0402FOr, would you prefer us to hunt you down?\x01",
            "That may prove entertaining.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401228V#5PTch.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401229VQuick! Split up!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 12)
    Sleep(100)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    BeginChrThread(0x16, 3, 0, 11)
    Sleep(200)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 12)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 11)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#0401230V#6P#0007FG-Get back here!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_22F3():
        OP_9D(0xFE, 0x3DB8, 0xFFFFE69C, 0xFFFF6A00, 0x190, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_22F3)
    WaitChrThread(0x8, 1)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x3F)
    SetChrSubChip(0x8, 0x0)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_93(0x8, 0x5A, 0x1F4)

    ChrTalk(
        0x8,
        "#0401231V#0402F#5PTwo of you, come with me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401232V#6P#0005F...?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401233V#6P#0011FW-Wait!\x02\x03",
            "#0401234V#0013FCrap!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x8, 3)
    Fade(500)
    OP_68(13920, -500, -34160, 0)
    MoveCamera(53, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0401235V#5P#0101FWhat should we do, Lloyd?!\x02",
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
            "[Call Elie]\x01",       # 0
            "[Call Tio]\x01",        # 1
            "[Call Randy]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24E5"),
        (1, "loc_25AD"),
        (2, "loc_2666"),
        (SWITCH_DEFAULT, "loc_272B"),
    )


    label("loc_24E5")

    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401236V#0007F#11PCome with me, Elie!\x02\x03",
            "#0401237VRandy, Tio, I'll leave the other\x01",
            "group to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401243V#5P#0101FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401246V#5P#0302FLeave it to me, pal!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 5)
    Jump("loc_272B")

    label("loc_25AD")

    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401240V#0007F#11PHelp me out, Tio!\x02\x03",
            "#0401241VElie, Randy, I'll leave the other\x01",
            "group to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401247V#5P#0201FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401238V#5P#0101FUnderstood!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 6)
    Jump("loc_272B")

    label("loc_2666")

    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#0401244V#0007F#11PGive me a hand, Randy!\x02\x03",
            "#0401245VElie, Tio, I'll leave the other\x01",
            "group to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401239V#5P#0302FIt's showtime, baby!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401242V#5P#0201FRoger!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x45, 7)
    Jump("loc_272B")

    label("loc_272B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_68(-12000, -500, -18000, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    OP_EE(0x0, 0x1)
    SetChrPos(0x17, -12000, -3050, -24000, 0)
    SetChrPos(0x18, -12000, -3050, -24000, 0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x40)
    SetChrSubChip(0x10, 0x0)
    SetCameraDistance(17000, 2400)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 8)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 9)
    OP_6F(0x10)
    Fade(500)
    OP_68(-6200, 1000, -9000, 0)
    MoveCamera(30, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    OP_68(1800, 1000, 2100, 4000)
    MoveCamera(45, 23, 0, 4000)
    SetCameraDistance(20500, 4000)
    WaitChrThread(0x17, 3)
    TurnDirection(0x17, 0x18, 500)
    WaitChrThread(0x18, 3)
    OP_6F(0x79)

    NpcTalk(
        0x17,
        "Man in Shades",
        (
            "#0401248V#5PDamn it! I can't believe those little\x01",
            "brats from the police are involved!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        (
            "#0401249V#5PWe need to contact headquarters\x01",
            "and request backup!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        "#0401250V#4PH-Hold on!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        (
            "#0401251V#4PWe screwed up the plan big time.\x01",
            "What if the boss gets a whiff of this?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401252V#5PKh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401253V#5PIt doesn't matter! Anyway, we should at least--\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 1800, 0, 17500, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sleep(200)
    Sound(1807, 255, 100, 0)
    Sleep(500)

    NpcTalk(
        0x9,
        "Rough Voice",
        "#0401255VDidja think ya could get away so easily?!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xB, -3800, 50, -4600, 45)
    SetChrPos(0xD, -4100, 0, -6300, 45)
    SetChrPos(0xE, -5400, 0, -5600, 45)
    SetChrPos(0xF, -700, 0, -7900, 0)
    SetChrPos(0x11, 8200, 50, -4000, 315)
    SetChrPos(0x12, 8000, 50, -5800, 315)
    SetChrPos(0x13, 3700, 0, -7600, 0)
    SetChrPos(0x14, 4700, 0, -8400, 0)
    SetChrPos(0x10, 9600, 0, -5700, 315)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2C02():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_2C02)

    def lambda_2C0F():
        OP_96(0xFE, 0x708, 0x0, 0x1964, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C0F)
    Sleep(1000)
    OP_68(1800, 1000, 0, 3000)
    MoveCamera(35, 25, 0, 3000)
    SetCameraDistance(21500, 3000)

    def lambda_2C51():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_2C51)

    def lambda_2C5E():
        OP_96(0xFE, 0xFFFFFCE0, 0x32, 0xFFFFF9C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2C5E)

    def lambda_2C78():
        OP_96(0xFE, 0x1450, 0x32, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C78)

    def lambda_2C92():
        OP_96(0xFE, 0x1388, 0x32, 0xFFFFF510, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C92)
    Sleep(50)

    def lambda_2CAF():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CAF)

    def lambda_2CC9():
        OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFF5D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2CC9)
    Sleep(50)

    def lambda_2CE6():
        OP_96(0xFE, 0x12C, 0x0, 0xFFFFF0C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2CE6)

    def lambda_2D00():
        OP_96(0xFE, 0xA8C, 0x0, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2D00)

    def lambda_2D1A():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFEED0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2D1A)

    def lambda_2D34():
        OP_96(0xFE, 0x19C8, 0x0, 0xFFFFF574, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D34)
    Sleep(2000)

    NpcTalk(
        0x17,
        "Man in Shades",
        "#0401256V#6PWhat?!\x02",
    )

    WaitChrThread(0x9, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x14, 1)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)
    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Man in Shades",
        "#0401257V#5PWhen'd they get here?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5500, 1500, -8400, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_2F2F")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_2E65():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E65)
    Sleep(50)

    def lambda_2E82():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E82)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    ChrTalk(
        0x103,
        "#0401262V#12P#0204FCheckmate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401259V#6P#0300FYeah, that was easy enough. The ball's in\x01",
            "Lloyd and Mademois-Elie's court now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3102")

    label("loc_2F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3034")
    SetChrPos(0x104, -9300, 0, -11500, 45)
    SetChrPos(0x102, -8700, 0, -12300, 45)

    def lambda_2F5F():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F5F)
    Sleep(50)

    def lambda_2F7C():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F7C)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    OP_6F(0x10)

    ChrTalk(
        0x104,
        "#0401260V#6P#0300FThese boys aren't goin' anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401263V#12P#0100FYes, we have them surrounded.\x01",
            "It's in Lloyd's and Tio's hands now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3102")

    label("loc_3034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3102")
    SetChrPos(0x102, -9300, 0, -11500, 45)
    SetChrPos(0x103, -8700, 0, -12300, 45)

    def lambda_3064():
        OP_96(0xFE, 0xFFFFE764, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3064)
    Sleep(50)

    def lambda_3081():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0xFFFFDBAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3081)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x10)

    ChrTalk(
        0x103,
        "#0401258V#12P#0204FCheckmate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401261V#6P#0100FIndeed. It's up to Lloyd and Randy now.\x02",
    )

    CloseMessageWindow()

    label("loc_3102")

    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3128")
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3147")

    label("loc_3128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_313A")
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3147")

    label("loc_313A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3147")
    AddParty(0x3, 0xEF, 0xFF)

    label("loc_3147")

    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    AddParty(0x4, 0xFF, 0xFF)
    OP_32(0x4, 0x0, 0x8)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x1)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x1)
    OP_38(0x4, 0x83, 0x1)
    OP_38(0x4, 0x84, 0x1)
    OP_38(0x4, 0x85, 0x1)
    OP_42(0x4, 0x438, 0xFF)
    OP_42(0x4, 0x5DC, 0xFF)
    OP_42(0x4, 0x640, 0xFF)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0x10E)
    SetChrChipPat(0x4, 0x6, 0x10E)
    OP_42(0x4, 0x85, 0x0)
    OP_42(0x4, 0x76, 0x3)
    OP_42(0x4, 0x64, 0x4)
    OP_42(0x4, 0x6A, 0x5)
    OP_42(0x4, 0x7C, 0x6)
    OP_42(0x4, 0x70, 0x1)
    OP_42(0x4, 0x7F, 0x2)
    OP_68(10100, 800, -14500, 0)
    MoveCamera(15, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 41400, -300, -34700, 270)
    SetChrPos(0x15, 16600, -2500, -21900, 315)
    SetChrPos(0x16, 17600, -2500, -21100, 315)

    def lambda_3229():
        OP_96(0xFE, 0x2580, 0xFFFFFF38, 0xFFFFC5CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3229)
    Sleep(50)

    def lambda_3246():
        OP_96(0xFE, 0x2968, 0xFFFFFF38, 0xFFFFC8EC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3246)
    SetCameraDistance(21000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x10)
    OP_68(1800, 1000, 0, 2000)
    MoveCamera(35, 25, 0, 2000)
    SetCameraDistance(21500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(10100, 800, -14500, 0)
    MoveCamera(15, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401264V#2P(Damn. Those morons.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x16, 500)

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401265V#6P(Don't got much choice now...\x01",
            "We'll have to go from the back!)\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 5)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 6)
    Sleep(1200)
    Fade(500)
    OP_6B(0x15)
    OP_68(15450, 70, -20130, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)

    ChrTalk(
        0x105,
        "#0401266V#0402F#2PHeh. A valiant effort, but no dice.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401267V#5PH-How did you catch up?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401268V#1PTch... Jump for it!\x02",
    )

    CloseMessageWindow()
    OP_68(35000, -5500, -39000, 1500)
    MoveCamera(37, 19, 0, 1500)
    SetCameraDistance(18000, 1500)
    SetChrPos(0x101, 22600, -6500, -39300, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3500")
    SetChrPos(0x102, 21700, -6500, -38700, 90)
    Jump("loc_3539")

    label("loc_3500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_351F")
    SetChrPos(0x103, 21700, -6500, -38700, 90)
    Jump("loc_3539")

    label("loc_351F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3539")
    SetChrPos(0x104, 21700, -6500, -38700, 90)

    label("loc_3539")

    BeginChrThread(0x16, 3, 0, 7)
    Sleep(150)
    OP_93(0x15, 0xB4, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3561():
        OP_9D(0xFE, 0x8980, 0xFFFFE69C, 0xFFFF6AC8, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3561)
    WaitChrThread(0x15, 1)
    PlayEffect(0x2, 0xFF, 0x15, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x3D)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_6F(0x79)
    SetChrPos(0x105, 31200, -800, -34200, 180)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(33130, -5500, -38360, 1000)

    def lambda_3631():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3631)

    def lambda_363E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_363E)

    def lambda_364B():
        OP_96(0xFE, 0x7788, 0xFFFFE69C, 0xFFFF667C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_364B)
    Sleep(50)

    def lambda_3668():
        OP_96(0xFE, 0x7404, 0xFFFFE69C, 0xFFFF68D4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3668)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    ChrTalk(
        0x101,
        "#0401269V#6P#0001FThere's nowhere to run.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3713")

    ChrTalk(
        0x102,
        (
            "#0401270V#6P#0103FPhew... That was quite the wild goose\x01",
            "chase, wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A6")

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3756")

    ChrTalk(
        0x103,
        "#0401271V#6P#0202FMuch like moths to a flame...\x02",
    )

    CloseMessageWindow()
    Jump("loc_37A6")

    label("loc_3756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_37A6")

    ChrTalk(
        0x104,
        (
            "#0401272V#6P#0302FPoor guys have no idea what's about\x01",
            "to hit 'em!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A6")


    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401273V#11PArgh!\x02",
    )

    CloseMessageWindow()
    SetChrChip(0x0, 0x105, 0x1E, 0x12C)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)

    def lambda_37E1():
        OP_9D(0xFE, 0x79E0, 0xFFFFE69C, 0xFFFF6E4C, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37E1)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x105, 1)
    PlayEffect(0x2, 0xFF, 0x105, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x105, 0x3F)
    SetChrSubChip(0x105, 0x0)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChip(0x1, 0x105, 0x0, 0x0)
    Sleep(300)
    OP_93(0x105, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#0401274V#0404FYour cute little game of hide-and-seek\x01",
            "is over.\x02\x03",
            "#0401275V#0402FSurely you've realized your best option\x01",
            "is to surrender, no?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401276V#11PHeh heh heh...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x16,
        "Man in Shades",
        "#0401277VHahaha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x15, 0x30)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x34)
    SetChrSubChip(0x16, 0x1)
    Sound(531, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x16,
        "Man in Shades",
        (
            "#0401278VLook at you goddamned brats.\x01",
            "Where do you get off being so\x01",
            "cocky?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        (
            "#0401279V#11PNow you'll see what happens when you\x01",
            "force professionals to get serious!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Man in Shades",
        "#0401280V#11PBetter hope you live to regret it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401281V#6P#0013FKh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3B34")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    Jump("loc_3B73")

    label("loc_3B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3B56")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Jump("loc_3B73")

    label("loc_3B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3B73")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)

    label("loc_3B73")

    OP_0D()
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#0401282V#0404FHeh. Looks like they're itching for a fight.\x01",
            "Don't think we have much other choice.\x02\x03",
            "#0401283V#0402FI can continue to count on your support,\x01",
            "can't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401284V#6P#0000FFunnily enough, I almost said the\x01",
            "same thing. Let's do this!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_3CAA")

    ChrTalk(
        0x102,
        "#0401285V#6P#0107FThey're coming!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D06")

    label("loc_3CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_3CD9")

    ChrTalk(
        0x103,
        "#0401286V#6P#0207FIncoming!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D06")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_3D06")

    ChrTalk(
        0x104,
        "#0401287V#6P#0307FBring it on!\x02",
    )

    CloseMessageWindow()

    label("loc_3D06")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15500, 300)
    SetChrChipByIndex(0x15, 0x31)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)

    def lambda_3D36():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3D36)

    def lambda_3D50():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3D50)
    Sleep(300)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    Call(0, 18)
    Return()

    # Function_4_8E0 end

    def Function_5_3D8E(): pass

    label("Function_5_3D8E")

    ClearChrFlags(0x15, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_3DAD():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DAD)
    WaitChrThread(0xFE, 1)

    def lambda_3DCB():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DCB)
    WaitChrThread(0xFE, 1)

    def lambda_3DE9():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DE9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3E1A():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E1A)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 0x3D)
    SetChrSubChip(0x15, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)

    def lambda_3E5F():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E5F)
    WaitChrThread(0xFE, 1)

    def lambda_3E7D():
        OP_95(0xFE, 36500, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E7D)
    Sleep(1100)
    OP_6B(0xFF)
    Fade(500)
    OP_68(36500, 200, -34200, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    OP_68(39000, 200, -33710, 1000)
    MoveCamera(50, 17, 0, 1000)
    SetCameraDistance(17000, 1000)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Return()

    # Function_5_3D8E end

    def Function_6_3F1A(): pass

    label("Function_6_3F1A")

    ClearChrFlags(0x16, 0x4)
    OP_92(0xFE, 0x46B4, 0xFFFFA81C, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_3F39():
        OP_95(0xFE, 18100, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F39)
    WaitChrThread(0xFE, 1)

    def lambda_3F57():
        OP_95(0xFE, 22000, -2500, -22500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F57)
    WaitChrThread(0xFE, 1)

    def lambda_3F75():
        OP_95(0xFE, 22000, -3500, -28200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F75)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3FA6():
        OP_9D(0xFE, 0x55F0, 0xFFFFFDA8, 0xFFFF7F7C, 0xCE4, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FA6)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x3D)
    SetChrSubChip(0x16, 0x1)
    Sleep(50)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)

    def lambda_3FEB():
        OP_95(0xFE, 25200, -300, -32500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FEB)
    WaitChrThread(0xFE, 1)

    def lambda_4009():
        OP_95(0xFE, 35100, -800, -34200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4009)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_6_3F1A end

    def Function_7_4046(): pass

    label("Function_7_4046")

    OP_93(0x16, 0xB4, 0x2BC)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4065():
        OP_9D(0xFE, 0x87F0, 0xFFFFE69C, 0xFFFF6424, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4065)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x16, 1)
    PlayEffect(0x2, 0xFF, 0x16, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x3D)
    SetChrSubChip(0x16, 0x1)
    Sound(326, 0, 90, 0)
    Sleep(100)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    Return()

    # Function_7_4046 end

    def Function_8_40E3(): pass

    label("Function_8_40E3")

    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)

    def lambda_40F0():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40F0)
    WaitChrThread(0xFE, 1)

    def lambda_410E():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_410E)
    WaitChrThread(0xFE, 1)

    def lambda_412C():
        OP_95(0xFE, 1800, 0, 3000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_412C)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_8_40E3 end

    def Function_9_414E(): pass

    label("Function_9_414E")

    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)

    def lambda_415B():
        OP_95(0xFE, -12000, 0, -12000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_415B)
    WaitChrThread(0xFE, 1)

    def lambda_4179():
        OP_95(0xFE, 1800, 0, -5500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4179)
    WaitChrThread(0xFE, 1)

    def lambda_4197():
        OP_95(0xFE, 1800, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4197)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    Return()

    # Function_9_414E end

    def Function_10_41B9(): pass

    label("Function_10_41B9")


    def lambda_41BE():
        OP_95(0xFE, 20900, -6500, -37000, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_41BE)
    WaitChrThread(0x8, 1)

    def lambda_41DC():
        OP_95(0xFE, 20900, -5500, -33000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_41DC)
    WaitChrThread(0x8, 1)
    Return()

    # Function_10_41B9 end

    def Function_11_41F6(): pass

    label("Function_11_41F6")


    def lambda_41FB():
        OP_95(0xFE, 7200, -6500, -36300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41FB)
    WaitChrThread(0xFE, 1)

    def lambda_4219():
        OP_95(0xFE, 2200, -4750, -32900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4219)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_41F6 end

    def Function_12_4233(): pass

    label("Function_12_4233")


    def lambda_4238():
        OP_95(0xFE, 21500, -6500, -36500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4238)
    WaitChrThread(0xFE, 1)

    def lambda_4256():
        OP_95(0xFE, 21500, -4550, -30500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4256)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_4233 end

    def Function_13_4270(): pass

    label("Function_13_4270")

    OP_A1(0xFE, 0x7D0, 0x8, 0x7, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6)
    Sleep(50)
    SetChrSubChip(0xFE, 0x7)
    Return()

    # Function_13_4270 end

    def Function_14_4286(): pass

    label("Function_14_4286")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x16, 6000, -5100, -37200, 135)

    def lambda_42A6():
        OP_95(0xFE, 11100, -6450, -37200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_42A6)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x87, 0x1F4)
    Return()

    # Function_14_4286 end

    def Function_15_42C7(): pass

    label("Function_15_42C7")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x17, 21000, -5750, -33500, 180)

    def lambda_42E7():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_42E7)
    WaitChrThread(0x17, 1)

    def lambda_4305():
        OP_95(0xFE, 16300, -6500, -37800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4305)
    WaitChrThread(0x17, 1)
    Return()

    # Function_15_42C7 end

    def Function_16_431F(): pass

    label("Function_16_431F")

    ClearChrFlags(0xFE, 0x8)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0x18, 21000, -5750, -33500, 180)

    def lambda_433F():
        OP_95(0xFE, 21000, -6500, -37000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_433F)
    WaitChrThread(0x18, 1)

    def lambda_435D():
        OP_95(0xFE, 16300, -6500, -39500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_435D)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x13B, 0x1F4)
    Return()

    # Function_16_431F end

    def Function_17_437E(): pass

    label("Function_17_437E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439C")
    OP_A1(0xFE, 0xFA0, 0x8, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2)
    Jump("Function_17_437E")

    label("loc_439C")

    Return()

    # Function_17_437E end

    def Function_18_439D(): pass

    label("Function_18_439D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch30800.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31700.itc", 0x20)
    LoadChrToIndex("chr/ch31800.itc", 0x21)
    LoadChrToIndex("chr/ch00400.itc", 0x22)
    LoadChrToIndex("chr/ch00450.itc", 0x23)
    LoadChrToIndex("chr/ch00451.itc", 0x24)
    LoadChrToIndex("chr/ch02100.itc", 0x25)
    LoadChrToIndex("apl/ch50019.itc", 0x26)
    LoadChrToIndex("chr/ch02150.itc", 0x27)
    LoadChrToIndex("chr/ch02151.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00150.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch31000.itc", 0x2E)
    LoadChrToIndex("chr/ch31001.itc", 0x2F)
    LoadChrToIndex("chr/ch31053.itc", 0x30)
    LoadChrToIndex("chr/ch31100.itc", 0x31)
    LoadChrToIndex("chr/ch31101.itc", 0x32)
    LoadChrToIndex("chr/ch31153.itc", 0x33)
    LoadChrToIndex("chr/ch06000.itc", 0x34)
    LoadChrToIndex("apl/ch50010.itc", 0x35)
    LoadChrToIndex("apl/ch50015.itc", 0x36)
    LoadChrToIndex("apl/ch50028.itc", 0x37)
    LoadChrToIndex("apl/ch50027.itc", 0x38)
    LoadChrToIndex("apl/ch50363.itc", 0x39)
    LoadChrToIndex("chr/ch06800.itc", 0x3A)
    RemoveParty(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_4492")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_44B9")

    label("loc_4492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_44A8")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_44B9")

    label("loc_44A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_44B9")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_44B9")

    OP_68(33260, -5500, -37300, 0)
    MoveCamera(31, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrChipByIndex(0x15, 0x30)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x3)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 35200, -6500, -38200, 270)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 34800, -6500, -39900, 270)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 31200, -6500, -37300, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 30600, -6500, -39300, 90)
    SetChrFlags(0x101, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_45A9")
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_4606")

    label("loc_45A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_45DA")
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 29700, -6500, -38700, 90)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x104, 0x8)
    Jump("loc_4606")

    label("loc_45DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_4606")
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, 29700, -6500, -38700, 90)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x102, 0x8)

    label("loc_4606")

    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    def lambda_46D8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_46D8)
    WaitChrThread(0x15, 2)

    ChrTalk(
        0x15,
        "#0401288V#11P#50WGah...\x02",
    )

    CloseMessageWindow()

    def lambda_4712():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4712)
    WaitChrThread(0x16, 2)

    ChrTalk(
        0x16,
        "#0401289V#50WYou damned kids.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_93(0x15, 0x13B, 0x0)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x0)
    OP_52(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x39)
    SetChrSubChip(0x16, 0x1)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    OP_0D()
    Sleep(500)
    PlayBGM("ed7103", 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401290V#6P#0006FPhew... They were no pushovers,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_48A3")

    ChrTalk(
        0x102,
        (
            "#0401291V#3P#0101FOne appeared to be using a military-grade\x01",
            "firearm, too.\x02\x03",
            "#0401292VI think it may have been manufactured in\x01",
            "the Empire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BE")

    label("loc_48A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_493B")

    ChrTalk(
        0x103,
        (
            "#0401293V#3P#0201FThat man is brandishing an Erebonian-\x01",
            "manufactured military-grade pistol.\x02\x03",
            "#0401294VThe latest model, I might add.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BE")

    label("loc_493B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_49BE")

    ChrTalk(
        0x104,
        (
            "#0401295V#3P#0301FThat dude was usin' some fancy-lookin'\x01",
            "military-grade firearm.\x02\x03",
            "#0401296VFrom the Empire, I'd bet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BE")


    ChrTalk(
        0x8,
        (
            "#0401297V#0404FIn all likelihood it was smuggled across\x01",
            "the border.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(31420, -5500, -37250, 1200)
    MoveCamera(31, 19, 0, 1200)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#0401298V#5P#0402FAnd I must say, that was quite the\x01",
            "performance you put on.\x02\x03",
            "#0401299VWhat a marvelous performance--\x01",
            "especially how you sold that fall.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    ClearChrFlags(0x101, 0x800)

    def lambda_4B08():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B08)
    Sleep(100)
    OP_93(0xEF, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#0401300V#12P#0003FWell, your plan didn't give me much of\x01",
            "a choice, did it?\x02\x03",
            "#0401301V#0001FI wasn't about to let anybody else be the\x01",
            "bait and put themselves in harm's way.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_4C9F")
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#0401302V#5P#0106F*sigh* And so, you volunteered to take\x01",
            "the role of bait for yourself...\x02\x03",
            "#0401303V#0101FI was worried sick, you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        "#0401304V#12P#0006FS-Sorry, Elie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC7")

    label("loc_4C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_4DD0")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#0401305V#5P#0206FHowever, did you not volunteer yourself for\x01",
            "an incredibly dangerous role too easily?\x02\x03",
            "#0401306V#0211FI believe your attempt at earning the title of\x01",
            "'Zemuria's Nicest Man' has gone too far.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#0401307V#12P#0005FR-Really? That wasn't my intention...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EC7")

    label("loc_4DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_4EC7")
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#0401308V#5P#0304FMan, why else would ya volunteer for the\x01",
            "role of bait so easily?\x02\x03",
            "#0401309V#0302FYou're a real softie, y'know? Look how easily\x01",
            "you let yourself get used.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#0401310V#12P#0001FS-Sorry about that.\x02",
    )

    CloseMessageWindow()

    label("loc_4EC7")


    ChrTalk(
        0x8,
        (
            "#0401311V#5P#0402FThat softhearted nature of yours is\x01",
            "sure to cause problems in the future.\x02\x03",
            "#0401312V#0409FAlthough, I don't necessarily find that\x01",
            "part of you to be a turnoff.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F82():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F82)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 5)), scpexpr(EXPR_END)), "loc_4FA8")

    def lambda_4F9B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F9B)
    Jump("loc_4FD9")

    label("loc_4FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_END)), "loc_4FC3")

    def lambda_4FB6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4FB6)
    Jump("loc_4FD9")

    label("loc_4FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 7)), scpexpr(EXPR_END)), "loc_4FD9")

    def lambda_4FD1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4FD1)

    label("loc_4FD9")

    Sleep(300)

    ChrTalk(
        0x101,
        "#0401313V#12P#0011FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401314V#5P#0404FHeh...\x02\x03",
            "#0401315V#0402FI was able to exact my revenge, and it\x01",
            "was all thanks to your help.\x02\x03",
            "#0401316VI look forward to any future alliances\x01",
            "we may hold.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(1800, 900, 1500, 0)
    MoveCamera(30, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x1)
    SetChrChipByIndex(0x18, 0x38)
    SetChrSubChip(0x18, 0x1)
    SetChrPos(0x15, 1000, 0, 2000, 180)
    SetChrPos(0x16, 2600, 0, 2000, 180)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 2600, 0, 3500, 90)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 1000, 0, 3500, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x3A)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x9, 4500, 0, 2800, 270)
    SetChrPos(0x11, 5600, 0, 1900, 270)
    SetChrPos(0x12, 5100, 0, 400, 315)
    SetChrPos(0x13, 6900, 0, 2100, 270)
    SetChrPos(0x14, 6500, 0, 100, 315)
    SetChrPos(0x10, 8000, 0, 500, 315)
    SetChrPos(0x8, -900, 0, 2800, 90)
    SetChrPos(0xB, -2000, 0, 1900, 90)
    SetChrPos(0xD, -1500, 0, 400, 45)
    SetChrPos(0xE, -3300, 0, 2100, 90)
    SetChrPos(0xF, -2900, 0, 100, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x101, 1100, 0, -1200, 0)
    SetChrPos(0x102, 2500, 0, -1200, 0)
    SetChrPos(0x103, 800, 0, -2200, 0)
    SetChrPos(0x104, 2800, 0, -2200, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    MoveCamera(37, 25, 0, 3000)
    SetCameraDistance(19500, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x50)
    Sleep(500)

    ChrTalk(
        0x18,
        (
            "#0401317V#11P#30WYou cocky little... Where do you get\x01",
            "off running your mouths like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0401318V#5P#30WHaha... Now you've done it,\x01",
            "you sons of bitches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0401319V#5P#30WFrom this day on, you've made\x01",
            "an enemy of Revache!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#0401320V#6P#30WYou damn rookies will rue the day...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#0401321V#6P#30WAll of the diet members are on our payroll.\x01",
            "Don't think you'll be getting away with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401322V#12P#0001FIs that what you think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401323V#1604F#4PHaha...\x02",
    )

    CloseMessageWindow()
    MoveCamera(33, 25, 0, 700)
    SetCameraDistance(18500, 700)

    def lambda_5582():
        OP_96(0xFE, 0xC80, 0x0, 0xD48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5582)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x20)

    def lambda_55BD():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_55BD)

    def lambda_55D6():
        OP_98(0xFE, 0xC8, 0x1C2, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_55D6)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x9, 0x36)
    SetChrSubChip(0x9, 0x0)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    OP_6F(0x50)

    ChrTalk(
        0x17,
        "#0401324V#40W...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#0401325V#4P#1602FLooks like ya haven't taken your lesson\x01",
            "to heart yet...\x02\x03",
            "#0401326VNew plan. I'm gonna hang you dumbasses\x01",
            "upside down like a bunch of punching bags,\x01",
            "then beat the absolute piss outta ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#0401327V#40W...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    ChrTalk(
        0x101,
        (
            "#0401328V#6P#0007FHold on a minute! They're already\x01",
            "defenseless, there's no need--\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    ChrTalk(
        0x8,
        "#0401329V#0400FNot to worry. You can leave the rest to us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    def lambda_57BC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57BC)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0401330V#6P#0403FWald. Try not to get too carried away, okay?\x02\x03",
            "#0401331V#0400FThese guys are professionals, after all.\x02\x03",
            "#0401332VThey could bite back even stronger next time\x01",
            "if you mess with them too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401333V#4P#1603FTch.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x37)
    SetChrSubChip(0x9, 0x0)

    def lambda_58C4():
        OP_9D(0xFE, 0x6A4, 0x0, 0xDAC, 0x32, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_58C4)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x30)
    SetChrSubChip(0x17, 0x3)

    def lambda_58F3():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_58F3)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x17, 2)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x20)

    ChrTalk(
        0x17,
        "#0401334V#50W*gasp* *cough*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(37, 25, 0, 700)
    SetCameraDistance(19500, 700)
    Fade(250)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)

    def lambda_5968():
        OP_96(0xFE, 0x1068, 0x0, 0xAF0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5968)
    WaitChrThread(0x9, 1)
    OP_6F(0x50)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#0401335V#3P#0404FHeh. How about this, boys? Why don't we keep this\x01",
            "friendly little spat to ourselves?\x02\x03",
            "#0401336V#0402FI doubt pros like yourselves would want your bosses\x01",
            "to find out that you got your asses handed to you\x01",
            "by a bunch of rookie cops--even while taking them\x01",
            "seriously.\x02\x03",
            "#0401337V#0409FSuch a pathetic report wouldn't go over well,\x01",
            "would it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#0401338V#11PGh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0401339V#6PGet bent, asshole. You'd be two arge\x01",
            "under if we were taking it seriously.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 1800, 0, 20000, 180)
    SetChrFlags(0xC, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sleep(150)

    NpcTalk(
        0xC,
        "Woman's Voice",
        (
            "#0401340V#4POoooh, what's this? Now, I'm no lawyer, but\x01",
            "it's probably in your best interest to bow out.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(817, 0, 100, 0)
    FadeToDark(100, 16777215, -1)
    OP_0D()
    Sleep(100)
    FadeToBright(500, 16777215)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_5DD0():

        label("loc_5DD0")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DD0")

    QueueWorkItem2(0x8, 2, lambda_5DD0)

    def lambda_5DE2():

        label("loc_5DE2")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DE2")

    QueueWorkItem2(0xB, 2, lambda_5DE2)

    def lambda_5DF4():

        label("loc_5DF4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5DF4")

    QueueWorkItem2(0xD, 2, lambda_5DF4)

    def lambda_5E06():

        label("loc_5E06")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E06")

    QueueWorkItem2(0xE, 2, lambda_5E06)

    def lambda_5E18():

        label("loc_5E18")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E18")

    QueueWorkItem2(0xF, 2, lambda_5E18)

    def lambda_5E2A():

        label("loc_5E2A")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E2A")

    QueueWorkItem2(0x9, 2, lambda_5E2A)

    def lambda_5E3C():

        label("loc_5E3C")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E3C")

    QueueWorkItem2(0x11, 2, lambda_5E3C)

    def lambda_5E4E():

        label("loc_5E4E")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E4E")

    QueueWorkItem2(0x12, 2, lambda_5E4E)

    def lambda_5E60():

        label("loc_5E60")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E60")

    QueueWorkItem2(0x13, 2, lambda_5E60)

    def lambda_5E72():

        label("loc_5E72")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E72")

    QueueWorkItem2(0x14, 2, lambda_5E72)

    def lambda_5E84():

        label("loc_5E84")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_5E84")

    QueueWorkItem2(0x10, 2, lambda_5E84)
    Fade(500)
    OP_68(1800, 1000, 9000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0xC, 1800, 0, 15000, 180)
    ClearChrFlags(0xC, 0x8)
    SetChrPos(0x15, 1000, 0, 2000, 0)
    SetChrPos(0x16, 2600, 0, 2000, 0)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 2600, 0, 3500, 0)
    SetChrPos(0x18, 1000, 0, 3500, 0)
    OP_68(1800, 1000, 4000, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_5F45():
        OP_95(0xFE, 1800, 0, 6000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5F45)
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x35)
    SetChrSubChip(0xC, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(500)
    PlayEffect(0x0, 0xFF, 0xC, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    EndChrThread(0x8, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x10, 0x2)
    OP_6F(0x11)

    ChrTalk(
        0x101,
        "#0401341V#0011FGrace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0401342V#0105FWhat are you doing here?!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0xC,
        (
            "#0401343VTeehee! I've been keeping my eyes\x01",
            "peeled for my favorite new rookies\x01",
            "these past few days.\x02\x03",
            "#0401344VAnd, much to my expectations, what\x01",
            "an absolute FEAST of information\x01",
            "you've given me!\x02\x03",
            "#0401345VOh, boy! I'm dying to write up a\x01",
            "riveting tale in my next article\x01",
            "about this unlikely operation!\x02",
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
        0x15,
        "#0401346V#12PWhy, you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#0401347V#4PYou're just some bitch from a puny news agency!\x01",
            "You think you can take Revache on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0401348V#5P#2106FWell, our circumstances are more complicated than\x01",
            "I care for, so I won't reveal your names.\x02\x03",
            "#0401349V#2100FHowever! If you bad boys are caught pulling another\x01",
            "stunt like this again, I can't promise that your\x01",
            "group's going to be able to bail you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#0401350V#4PGah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#0401351V#2PFine, whatever.\x01",
            "We'll be going now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#0401352V#2PBut if you don't keep your word, lady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0401353V#5P#2104FDon't worry your pretty little head about that.\x02\x03",
            "#0401354V#2101FTo be fair, you're the ones that should be\x01",
            "worrying about keeping your promises.\x01",
            "Wouldn't wanna be in hot water, would we?\x02\x03",
            "#0401355VCross the line again, and a little birdy told\x01",
            "me the bracers might come get'cha!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        "#0401356V#2PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401357V#0005F...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0401358V#5P#2103FJust a little FYI: Arios was strongly considering\x01",
            "taking over this case.\x02\x03",
            "#0401359V#2100FNaturally, being the grand bracer he is, he was\x01",
            "totally up to his neck in requests. He figured\x01",
            "he'd leave it in your guys' hands this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401360V#0011FI-Is that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0401361V#0306FHe's keepin' tabs on us, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401362V#0211FThat appears to be the case.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#0401363V#6PO-Oh, hell no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#0401364V#6PAs if we'd ever be moronic enough to\x01",
            "make an enemy of Arios MacLaine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#0401365V#5PThere's no point in staying in this dump\x01",
            "any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#0401366V#5PWe're outta here!\x02",
    )

    CloseMessageWindow()
    Fade(250)

    def lambda_684F():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_684F)
    SetChrChipByIndex(0x18, 0x31)
    SetChrSubChip(0x18, 0x0)
    Sleep(350)

    def lambda_6873():

        label("loc_6873")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_6873")

    QueueWorkItem2(0xC, 2, lambda_6873)

    def lambda_6885():
        OP_96(0xFE, 0x9C4, 0x0, 0x189C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6885)
    SetChrChipByIndex(0x18, 0x32)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 21)
    Fade(250)

    def lambda_68B2():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_68B2)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 21)
    Fade(250)

    def lambda_68E9():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_68E9)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x15, 0x2F)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 3, 0, 21)
    Fade(250)

    def lambda_6920():
        OP_A6(0xFE, 0x0, 0x32, 0x15E, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6920)
    SetChrChipByIndex(0x16, 0x31)
    SetChrSubChip(0x16, 0x0)
    Sleep(350)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    BeginChrThread(0x16, 3, 0, 21)
    Sleep(2000)
    OP_68(1800, 1000, 2000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    EndChrThread(0xC, 0x2)

    def lambda_69B2():
        OP_95(0xFE, 1800, 0, 6000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_69B2)
    WaitChrThread(0xC, 1)

    def lambda_69D0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_69D0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x1)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)

    ChrTalk(
        0x8,
        (
            "#0401367V#3P#0406FOh, boy. 'Arios' is that Divine Blade of Wind\x01",
            "fellow, isn't he?\x02\x03",
            "#0401368V#0400FI've heard my fair share about his exploits,\x01",
            "but I didn't think the name alone would be\x01",
            "enough to send the mafia packing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#0401369V#1601FHah! To hell with this shit.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#0401370V#6P#1604FScrew it. Show's over, boys!\x02\x03",
            "#0401371V#1602FGet yer asses movin'. We're leavin'!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BAB():

        label("loc_6BAB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6BAB")

    QueueWorkItem2(0x101, 2, lambda_6BAB)

    def lambda_6BBD():

        label("loc_6BBD")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6BBD")

    QueueWorkItem2(0x102, 2, lambda_6BBD)

    def lambda_6BCF():

        label("loc_6BCF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6BCF")

    QueueWorkItem2(0x103, 2, lambda_6BCF)

    def lambda_6BE1():

        label("loc_6BE1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6BE1")

    QueueWorkItem2(0x104, 2, lambda_6BE1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(400, 10, -1, -1)
    SetChrName("Saber Vipers")

    AnonymousTalk(
        0xFF,
        "#0401372V#4SYEAH!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_6C41():

        label("loc_6C41")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C41")

    QueueWorkItem2(0x8, 2, lambda_6C41)

    def lambda_6C53():

        label("loc_6C53")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C53")

    QueueWorkItem2(0xB, 2, lambda_6C53)

    def lambda_6C65():

        label("loc_6C65")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C65")

    QueueWorkItem2(0xD, 2, lambda_6C65)

    def lambda_6C77():

        label("loc_6C77")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C77")

    QueueWorkItem2(0xE, 2, lambda_6C77)

    def lambda_6C89():

        label("loc_6C89")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C89")

    QueueWorkItem2(0xF, 2, lambda_6C89)

    def lambda_6C9B():

        label("loc_6C9B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6C9B")

    QueueWorkItem2(0x11, 2, lambda_6C9B)

    def lambda_6CAD():

        label("loc_6CAD")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6CAD")

    QueueWorkItem2(0x12, 2, lambda_6CAD)

    def lambda_6CBF():

        label("loc_6CBF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6CBF")

    QueueWorkItem2(0x13, 2, lambda_6CBF)

    def lambda_6CD1():

        label("loc_6CD1")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6CD1")

    QueueWorkItem2(0x14, 2, lambda_6CD1)

    def lambda_6CE3():

        label("loc_6CE3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6CE3")

    QueueWorkItem2(0x10, 2, lambda_6CE3)

    def lambda_6CF5():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6CF5)
    Sleep(500)

    def lambda_6D12():
        OP_96(0xFE, 0xFA0, 0x0, 0xFFFFFE0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6D12)
    Sleep(800)
    BeginChrThread(0x11, 3, 0, 19)
    WaitChrThread(0x12, 1)
    Sleep(1500)
    EndChrThread(0x12, 0x2)

    def lambda_6D40():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6D40)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 19)
    Sleep(1000)
    EndChrThread(0x14, 0x2)

    def lambda_6D6A():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6D6A)
    Sleep(600)
    EndChrThread(0x10, 0x2)

    def lambda_6D8B():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D8B)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x8, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xF, 0x2)

    def lambda_6E11():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6E11)
    Sleep(150)

    def lambda_6E21():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6E21)
    Sleep(50)

    def lambda_6E31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6E31)

    def lambda_6E3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_6E3E)
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0x8,
        (
            "#0401375V#5P#0404FI must say, I couldn't have done it\x01",
            "without your help.\x02\x03",
            "#0401376V#0400FOr, would 'mission accomplished' be\x01",
            "more appropriate for you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6EEE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EEE)
    Sleep(50)

    def lambda_6EFE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6EFE)
    Sleep(50)

    def lambda_6F0E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6F0E)
    Sleep(50)

    def lambda_6F1E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6F1E)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401403V#0005F#11PY-Yeah... I suppose so.\x02\x03",
            "#0401378V#0004FThough, I guess our original mission\x01",
            "was only to stop the initial fight...\x02\x03",
            "#0401379V#0000FAnyway, you shouldn't have a reason\x01",
            "to fight with Wald anymore, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#0401380V#5P#0405FHmm? What are you going on about, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401381V#0011F#11PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0401382V#5PWhether the mafia is involved or not, it is\x01",
            "not as though our relations with the Saber\x01",
            "Vipers are going to change overnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#0401383V#5PWe are still going to view each other as a\x01",
            "blight on our territory. That will not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401384V#5P#0404FSure, there probably won't be another\x01",
            "large conflict between us for a while...\x02\x03",
            "#0401385V#0402FBut, our regular scuffles are bound to\x01",
            "continue, no doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401386V#0001F#11PH-Hold on now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401387V#5P#0402FHeh. If you don't want our future fights to get\x01",
            "out of hand, you're more than welcome to stop\x01",
            "by and intervene when the time comes.\x02\x03",
            "#0401388VPerhaps you could even join in on our amicable\x01",
            "little disputes.\x02\x03",
            "#0401389V#0409FI'd welcome you with loving arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0401390V#0006F#11PU-Uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401391V#0106FI don't get the impression that he's\x01",
            "joking in the slightest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#0401392V#5P#0404FHeh... Well, then. I wish you sweet\x01",
            "dreams, everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x8,
        "#0401393V#5P#0402FLet's go.\x02",
    )

    CloseMessageWindow()

    def lambda_7449():

        label("loc_7449")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7449")

    QueueWorkItem2(0xD, 2, lambda_7449)

    def lambda_745B():

        label("loc_745B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_745B")

    QueueWorkItem2(0xE, 2, lambda_745B)

    def lambda_746D():

        label("loc_746D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_746D")

    QueueWorkItem2(0xF, 2, lambda_746D)
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xB,
        "#0401394V#5POur crusade has ended. Let us withdraw.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(50, 170, -1, -1)
    SetChrName("Testaments")

    AnonymousTalk(
        0xFF,
        "#0401395V#4SJa!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_750A():

        label("loc_750A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_750A")

    QueueWorkItem2(0x101, 2, lambda_750A)

    def lambda_751C():

        label("loc_751C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_751C")

    QueueWorkItem2(0x102, 2, lambda_751C)

    def lambda_752E():

        label("loc_752E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_752E")

    QueueWorkItem2(0x103, 2, lambda_752E)

    def lambda_7540():

        label("loc_7540")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7540")

    QueueWorkItem2(0x104, 2, lambda_7540)

    def lambda_7552():

        label("loc_7552")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7552")

    QueueWorkItem2(0xC, 2, lambda_7552)

    def lambda_7564():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7564)
    Sleep(500)

    def lambda_7581():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0xFFFFFE0C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7581)
    Sleep(800)
    BeginChrThread(0xB, 3, 0, 20)
    WaitChrThread(0xD, 1)
    Sleep(1500)
    EndChrThread(0xD, 0x2)

    def lambda_75AF():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_75AF)
    Sleep(100)
    EndChrThread(0xC, 0x2)

    def lambda_75D0():
        OP_95(0xFE, 1800, 0, 1000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_75D0)
    BeginChrThread(0xE, 3, 0, 20)
    Sleep(1000)
    EndChrThread(0xF, 0x2)

    def lambda_75F7():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_75F7)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    TurnDirection(0xC, 0x8, 500)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    Fade(500)
    OP_68(1800, 1000, -1200, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#0401397V#5P#0011F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401398V#5P#0203FWhat an incorrigible group of men.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0401399V#0300F#11PMeh, leave 'em be. They're just a bunch\x01",
            "of hot-headed dudes rarin' for a fight.\x01",
            "Nothin' you can really do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401400V#5P#0106F*sigh* For once, you might be right.\x02\x03",
            "#0401401V#0100FMore importantly, we've successfully\x01",
            "resolved our mission.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#0401402V#11P#0102FIsn't that right, Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401377V#6P#0000FY-Yeah, I guess so.\x02\x03",
            "#0401404V#0008FStill, I can't shake the feeling\x01",
            "this was a hollow victory.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#0401405V#2104FThat discomfort probably stems from the\x01",
            "fact that you rookies, once again, had to\x01",
            "rely on somebody else to finish the job!\x02\x03",
            "#0401406V#2100FHow was that? Did I nail it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1800, 1000, -100, 1000)

    def lambda_79AE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79AE)
    Sleep(100)

    def lambda_79BE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_79BE)

    def lambda_79CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_79CB)

    def lambda_79D8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79D8)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#0401407V#12P#0005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0401408V#5P#2101FDon't let it get to you!\x02\x03",
            "#0401409V#2103FThere's nothing wrong with accepting a little\x01",
            "help in times like these! How else are you\x01",
            "going to get the full picture?\x02\x03",
            "#0401410VOnly once you've understood this can you\x01",
            "truly call yourself a detective.\x02\x03",
            "#0401411V#2102FJust like your brother.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0401412V#12P#0005FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0401413V#2104F#5PHeehee. Well, I think it's time for me to\x01",
            "head on home now.\x02\x03",
            "#0401414V#2110FI gotta go exfoliate! You'd be surprised how\x01",
            "much I work to keep my skin this flawless!\x02\x03",
            "#0401415V#2109FAnyway, nighty-night!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_7C66():
        OP_95(0xFE, 1600, 0, 15000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7C66)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_68(2600, 1000, -1250, 1200)

    def lambda_7CAF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7CAF)
    Sleep(50)

    def lambda_7CBF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7CBF)
    Sleep(50)

    def lambda_7CCF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7CCF)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    ChrTalk(
        0x104,
        (
            "#0401416V#0300FYour brother must have been one\x01",
            "helluva dude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0401417V#11P#0100FJudging from what I've heard, it sounds\x01",
            "like he was a talented individual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0401418V#5P#0002FHaha...\x02\x03",
            "#0401419V#0004FThere aren't a whole lot of people that\x01",
            "would outrank him when it comes to\x01",
            "persistence and efficiency on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0401420V#12P#0200F...\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#0401421V#5P#0003FAt any rate, our mission is accomplished.\x02\x03",
            "#0401422V#0000FLet's return to the SSS building and give\x01",
            "Chief Sergei our report.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_439D end

    def Function_19_7F14(): pass

    label("Function_19_7F14")

    EndChrThread(0xFE, 0x2)

    def lambda_7F1D():
        OP_95(0xFE, 5100, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F1D)
    WaitChrThread(0xFE, 1)

    def lambda_7F3B():
        OP_95(0xFE, 8800, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F3B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_7F14 end

    def Function_20_7F55(): pass

    label("Function_20_7F55")

    EndChrThread(0xFE, 0x2)

    def lambda_7F5E():
        OP_95(0xFE, -1500, 0, 400, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F5E)
    WaitChrThread(0xFE, 1)

    def lambda_7F7C():
        OP_95(0xFE, -4200, 0, -8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F7C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_7F55 end

    def Function_21_7F96(): pass

    label("Function_21_7F96")


    def lambda_7F9B():
        OP_95(0xFE, 800, 0, 5000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F9B)
    WaitChrThread(0xFE, 1)

    def lambda_7FB9():
        OP_95(0xFE, 800, 0, 25000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7FB9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_7F96 end

    SaveToFile()

Try(main)
