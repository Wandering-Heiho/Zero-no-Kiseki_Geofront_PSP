from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c020b.bin",                # FileName
        "c020b",                    # MapName
        "c020b",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 0, 0, 1],
    )

    BuildStringList((
        "c020b",                  # 0
        "Chief Sergei",           # 1
        "Zeit",                   # 2
        "Oscar",                  # 3
        "Harold",                 # 4
        "Mr. Grimwood",           # 5
        "Tallys",                 # 6
        "Momo",                   # 7
        "CGF Guardsman",          # 8
        "CGF Guardsman",          # 9
        "CGF Guardsman",          # 10
        "CGF Guardsman",          # 11
        "CGF Guardsman",          # 12
        "CGF Guardsman",          # 13
        "CGF Guardsman",          # 14
        "車１",                   # 15
        "車２",                   # 16
        "SE制御",                 # 17
        "Central Square",         # 18
        "West Street",            # 19
        "Administrative District",# 20
        "Residential District",   # 21
        "Entertainment District", # 22
        "East Street",            # 23
        "Downtown District",      # 24
        "Harbor District",        # 25
        "IBC",                    # 26
        "Station Street",         # 27
        "Back Alley",             # 28
        "Ursula Road",            # 29
        "East Crossbell Highway", # 30
        "West Crossbell Highway", # 31
        "Mainz Mountain Path",    # 32
    ))

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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  2,  0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  3,  0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central Square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "West Street")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Administrative District")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential District")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "Downtown District")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Harbor District")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Station Street")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back Alley")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "Ursula Road")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_5E0",          # 00, 0
        "Function_1_5F0",          # 01, 1
        "Function_2_61F",          # 02, 2
        "Function_3_7B0",          # 03, 3
        "Function_4_90F",          # 04, 4
        "Function_5_1874",         # 05, 5
        "Function_6_1EE5",         # 06, 6
        "Function_7_2005",         # 07, 7
        "Function_8_202E",         # 08, 8
        "Function_9_2054",         # 09, 9
        "Function_10_2176",        # 0A, 10
        "Function_11_21CA",        # 0B, 11
        "Function_12_2380",        # 0C, 12
        "Function_13_252B",        # 0D, 13
        "Function_14_270C",        # 0E, 14
        "Function_15_27D9",        # 0F, 15
        "Function_16_2887",        # 10, 16
        "Function_17_2935",        # 11, 17
        "Function_18_29E3",        # 12, 18
        "Function_19_2A91",        # 13, 19
        "Function_20_2B31",        # 14, 20
        "Function_21_2C88",        # 15, 21
        "Function_22_2CFB",        # 16, 22
        "Function_23_2D74",        # 17, 23
        "Function_24_2DED",        # 18, 24
        "Function_25_2E60",        # 19, 25
        "Function_26_2E7A",        # 1A, 26
    ))


    def Function_0_5E0(): pass

    label("Function_0_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5EF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_5EF")

    Return()

    # Function_0_5E0 end

    def Function_1_5F0(): pass

    label("Function_1_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_603")
    OP_70(0x7, 0x0)
    Jump("loc_607")

    label("loc_603")

    OP_70(0x7, 0x1E)

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")
    OP_70(0x8, 0x0)
    Jump("loc_61E")

    label("loc_61A")

    OP_70(0x8, 0x1E)

    label("loc_61E")

    Return()

    # Function_1_5F0 end

    def Function_2_61F(): pass

    label("Function_2_61F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Obtained:\x01\x07\x02",
            "#56IEarth Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#57IWater Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#58IFire Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#59IWind Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#60ITime Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#61ISpace Sepith\x07\x00",
            " x80\x01\x07\x02",
            "#62IMirage Sepith\x07\x00",
            " x80.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_79E")

    label("loc_753")


    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "How'd you even get here? Don't you\x01",
            "have anything better to do?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_79E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_61F end

    def Function_3_7B0(): pass

    label("Function_3_7B0")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89A")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_830")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_895")

    label("loc_830")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_895")

    Jump("loc_903")

    label("loc_89A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Zzz... Zzz...\x01",
            "(The chest appears to be drooling in its sleep.)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_903")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7B0 end

    def Function_4_90F(): pass

    label("Function_4_90F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31252.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch07000.itc", 0x27)
    LoadChrToIndex("chr/ch05900.itc", 0x28)
    LoadChrToIndex("chr/ch09300.itc", 0x29)
    LoadChrToIndex("chr/ch00150.itc", 0x2A)
    LoadChrToIndex("chr/ch00151.itc", 0x2B)
    LoadChrToIndex("chr/ch00250.itc", 0x2C)
    LoadChrToIndex("chr/ch00251.itc", 0x2D)
    LoadChrToIndex("chr/ch00950.itc", 0x2E)
    LoadChrToIndex("chr/ch00951.itc", 0x2F)
    LoadChrToIndex("chr/ch00952.itc", 0x30)
    LoadChrToIndex("apl/ch50509.itc", 0x31)
    LoadChrToIndex("chr/ch00152.itc", 0x32)
    LoadChrToIndex("chr/ch24800.itc", 0x33)
    LoadChrToIndex("chr/ch20700.itc", 0x34)
    OP_68(33000, -2900, -19000, 0)
    MoveCamera(53, 15, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x102, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x103, 41000, -4000, -19000, 270)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, 41000, -4000, -19000, 270)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 41000, -4000, -19000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 41000, -4000, -19000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x15, 0x4)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xF, 4200, 500, -700, 120)
    SetChrPos(0x10, 4200, 500, -700, 120)
    SetChrPos(0x11, 4200, 500, -700, 120)
    SetChrPos(0x12, 4200, 500, -700, 120)
    SetChrPos(0x13, 6900, 0, -9000, 90)
    SetChrPos(0x14, 6400, 0, -7400, 90)
    SetChrPos(0x15, 4900, 0, -8600, 90)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5500, 3000, 14800, 180)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 9500, 3000, 14100, 180)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 8200, 3000, 14200, 180)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x33)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 8700, 3000, 17050, 180)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x34)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 8200, 3000, 17620, 180)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_78(0x10, 0x16)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x10, 0x4)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    OP_49()
    SetChrPos(0x16, -27000, 0, 3500, 0)
    OP_D3(0x16, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0xB5, 0xF0, 0x0, 0x20)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    LoadEffect(0x0, "event\\ev606_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")
    LoadEffect(0x2, "battle\\btgun00.eff")
    LoadEffect(0x3, "event\\eva03_00.eff")
    Sound(103, 0, 100, 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(450)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 16)
    Sleep(450)
    BeginChrThread(0x103, 3, 0, 17)
    Sleep(450)
    BeginChrThread(0x10A, 3, 0, 18)
    Sleep(450)
    BeginChrThread(0x8, 3, 0, 19)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(19400, 1000, -8600, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(47, 19, 0, 2500)
    SetCameraDistance(16500, 2500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x8, 3)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#5200140V#11P#0010FNo way! Weren't those guards from\x01",
            "Bellguard Gate?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200141V#0307F#11PYeah, they were! I recognize most of 'em!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5200142V#0108F#5PThey're acting just like the mafia...\x01",
            "Are they being controlled, too?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5200143V#12P#0201FThat seems most likely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#5200144V#6P#0610FO-Our main goal should be making\x01",
            "it back to headquarters!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_90(0x9, 18600, -1500, -17500, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    def lambda_FE0():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FE0)
    SetChrChip(0x0, 0x9, 0x1E, 0xC8)
    Sound(854, 0, 100, 0)

    def lambda_1001():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0xC80, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1001)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1067():
        OP_92(0xFE, 0x3458, 0xFFFFE0C0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1067)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    OP_68(16400, 1000, -8600, 1000)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_109C():
        OP_9D(0xFE, 0x3458, 0x0, 0xFFFFE0C0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_109C)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    WaitChrThread(0x9, 1)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_10FB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10FB)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(925, 0, 100, 0)
    WaitChrThread(0x9, 2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    OP_6F(0x1)
    Sound(2054, 255, 100, 0)

    ChrTalk(
        0x9,
        "#5202001V#1207F#11PWoof!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11E9():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11E9)
    Sleep(30)

    def lambda_11F9():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11F9)
    Sleep(30)

    def lambda_1209():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1209)
    Sleep(30)

    def lambda_1219():
        OP_93(0xFE, 0x10E, 0x258)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1219)
    WaitChrThread(0x10A, 2)
    Sleep(300)
    Fade(500)
    OP_68(-15000, 1500, 3500, 0)
    MoveCamera(53, 15, -5, 0)
    OP_6E(750, 0)
    SetCameraDistance(17500, 0)
    OP_68(-5000, 1500, 3500, 3000)
    MoveCamera(45, 15, -5, 3000)
    SetCameraDistance(14500, 3000)
    ClearMapObjFlags(0x10, 0x4)

    def lambda_128B():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xDAC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_128B)
    PlayEffect(0x3, 0x0, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x16, 0x40, 0, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(493, 0, 100, 0)
    OP_6F(0x79)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    Fade(250)
    OP_68(-2000, 1000, 3500, 0)
    MoveCamera(330, 27, 5, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(3400, 1000, -700, 1000)
    SetCameraDistance(16000, 1000)
    WaitChrThread(0x16, 1)

    def lambda_13AC():
        OP_9E(0xFE, 0xFFFFF830, 0xFFFFFA24, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_13AC)

    def lambda_13C7():
        OP_D3(0xFE, 0x0, 0x30D40, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_13C7)
    BeginChrThread(0x16, 3, 0, 6)
    Sound(495, 0, 100, 0)
    WaitChrThread(0x16, 1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    OP_24(0x1ED)
    SetMapObjFlags(0x10, 0x20)
    OP_71(0x10, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x10)
    OP_71(0x10, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x10)
    OP_68(4900, 1000, -1000, 1500)
    MoveCamera(330, 23, 0, 1500)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0xF, 3, 0, 21)
    Sleep(400)
    BeginChrThread(0x10, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0x11, 3, 0, 23)
    Sleep(400)
    BeginChrThread(0x12, 3, 0, 24)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)

    NpcTalk(
        0x101,
        "KeA",
        "#5200145V#1105FWhoa, they're here, too?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200146V#0010FDamn... They've cut us off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5200147V#1007FLet's retreat to Central Square for now!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(17400, 1000, -8600, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(20400, 1000, -8600, 7000)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 7)
    BeginChrThread(0x104, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x103, 3, 0, 10)
    BeginChrThread(0x10A, 3, 0, 11)
    BeginChrThread(0x8, 3, 0, 12)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xF, 3, 0, 5)
    Sleep(6000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x18, 0x2)

    def lambda_15E3():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_15E3)
    Sleep(50)

    def lambda_1600():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1600)
    Sleep(50)

    def lambda_161D():
        OP_97(0xFE, 0x9C40, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_161D)
    Sleep(3000)
    OP_6F(0x1)
    Fade(1000)
    OP_68(7500, 4000, 14200, 0)
    MoveCamera(42, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetCameraDistance(16000, 2000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x15, 0xFF)
    OP_64(0xA)
    OP_64(0xB)
    OP_64(0xC)
    OP_64(0xD)
    OP_64(0xE)

    ChrTalk(
        0xA,
        "#5200148V#5PWhat in the world is going on?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5200149V#5P#3601FIan, weren't those people...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5200150V#2205F#5PW-We have a major problem\x01",
            "on our hands!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    ChrTalk(
        0xC,
        (
            "#5200151V#2201F#11PMr. Hayworth! I advise you leave now!\x02\x03",
            "#5200152VEveryone, return home immediately!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    SetScenarioFlags(0x5C, 6)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_90F end

    def Function_5_1874(): pass

    label("Function_5_1874")

    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(956, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14100, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 15600, 0, -6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12100, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 14300, 0, -7300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12300, 0, -10700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 11300, 0, -8500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Return()

    # Function_5_1874 end

    def Function_6_1EE5(): pass

    label("Function_6_1EE5")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -4000, 0, 5500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1300, 0, 5000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 300, 0, 3700, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 2000, 0, 2300, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(230)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 5000, -30, 1000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_1EE5 end

    def Function_7_2005(): pass

    label("Function_7_2005")

    Sleep(100)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_2014():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2014)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_2005 end

    def Function_8_202E(): pass

    label("Function_8_202E")

    OP_93(0x104, 0x5A, 0x1F4)

    def lambda_203A():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_203A)
    WaitChrThread(0x104, 1)
    Return()

    # Function_8_202E end

    def Function_9_2054(): pass

    label("Function_9_2054")

    SetChrFlags(0x102, 0x20)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)

    def lambda_20B4():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20B4)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(600)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)

    def lambda_2120():
        OP_98(0xFE, 0x64, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2120)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x20)
    OP_93(0x102, 0x5A, 0x1F4)

    def lambda_215C():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_215C)
    WaitChrThread(0x102, 1)
    Return()

    # Function_9_2054 end

    def Function_10_2176(): pass

    label("Function_10_2176")

    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_2183():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2183)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_21B0():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21B0)
    WaitChrThread(0x103, 1)
    Return()

    # Function_10_2176 end

    def Function_11_21CA(): pass

    label("Function_11_21CA")

    SetChrChipByIndex(0x10A, 0x30)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x10A, 0x2E)
    SetChrSubChip(0x10A, 0x0)
    OP_93(0x10A, 0x5A, 0x1F4)

    def lambda_2366():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2366)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_11_21CA end

    def Function_12_2380(): pass

    label("Function_12_2380")

    SetChrChipByIndex(0x8, 0x31)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(100)
    SetChrSubChip(0x8, 0x7)
    Sleep(100)
    SetChrSubChip(0x8, 0x4)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(100)
    SetChrSubChip(0x8, 0x7)
    Sleep(100)
    SetChrSubChip(0x8, 0x4)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0x8, 0x1)
    Sleep(70)
    SetChrSubChip(0x8, 0x2)
    Sleep(70)
    SetChrSubChip(0x8, 0x3)
    Sleep(70)
    SetChrSubChip(0x8, 0x4)
    Sleep(500)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_2511():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2511)
    WaitChrThread(0x8, 1)
    Return()

    # Function_12_2380 end

    def Function_13_252B(): pass

    label("Function_13_252B")


    def lambda_2530():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2530)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1300)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2588():
        OP_92(0xFE, 0x4E20, 0xFFFFD120, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2588)
    WaitChrThread(0x9, 2)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_25E7():
        OP_9D(0xFE, 0x4E20, 0x3E8, 0xFFFFD120, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_25E7)
    Sleep(600)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)

    def lambda_2616():
        OP_92(0xFE, 0x5F50, 0xFFFFE890, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2616)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_263A():
        OP_9D(0xFE, 0x5F50, 0x0, 0xFFFFE890, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_263A)
    Sleep(400)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)

    def lambda_266D():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_266D)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_2687():
        OP_9D(0xFE, 0x8660, 0x44C, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2687)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    Sleep(50)
    SetChrSubChip(0x9, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_26C7():
        OP_9D(0xFE, 0xA1B8, 0x834, 0xFFFFE890, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26C7)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x9, 0x2)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_252B end

    def Function_14_270C(): pass

    label("Function_14_270C")


    def lambda_2711():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2711)

    def lambda_2722():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2722)
    Sleep(1000)

    def lambda_273F():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_273F)
    Sleep(500)
    OP_68(18000, -900, -19000, 4000)
    MoveCamera(25, 10, 5, 4000)
    WaitChrThread(0xFE, 1)

    def lambda_277C():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_277C)
    WaitChrThread(0xFE, 1)

    def lambda_279A():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_279A)
    WaitChrThread(0xFE, 1)

    def lambda_27B8():
        OP_95(0xFE, 20100, 0, -7400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27B8)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_14_270C end

    def Function_15_27D9(): pass

    label("Function_15_27D9")


    def lambda_27DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27DE)

    def lambda_27EF():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27EF)
    Sleep(1000)

    def lambda_280C():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_280C)
    WaitChrThread(0xFE, 1)

    def lambda_282A():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_282A)
    WaitChrThread(0xFE, 1)

    def lambda_2848():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2848)
    WaitChrThread(0xFE, 1)

    def lambda_2866():
        OP_95(0xFE, 20500, 0, -8700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2866)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_15_27D9 end

    def Function_16_2887(): pass

    label("Function_16_2887")


    def lambda_288C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_288C)

    def lambda_289D():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_289D)
    Sleep(1000)

    def lambda_28BA():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28BA)
    WaitChrThread(0xFE, 1)

    def lambda_28D8():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28D8)
    WaitChrThread(0xFE, 1)

    def lambda_28F6():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28F6)
    WaitChrThread(0xFE, 1)

    def lambda_2914():
        OP_95(0xFE, 18400, 0, -7300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2914)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_16_2887 end

    def Function_17_2935(): pass

    label("Function_17_2935")


    def lambda_293A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_293A)

    def lambda_294B():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_294B)
    Sleep(1000)

    def lambda_2968():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2968)
    WaitChrThread(0xFE, 1)

    def lambda_2986():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2986)
    WaitChrThread(0xFE, 1)

    def lambda_29A4():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29A4)
    WaitChrThread(0xFE, 1)

    def lambda_29C2():
        OP_95(0xFE, 18500, 0, -9200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29C2)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_17_2935 end

    def Function_18_29E3(): pass

    label("Function_18_29E3")


    def lambda_29E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29E8)

    def lambda_29F9():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29F9)
    Sleep(1000)

    def lambda_2A16():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A16)
    WaitChrThread(0xFE, 1)

    def lambda_2A34():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A34)
    WaitChrThread(0xFE, 1)

    def lambda_2A52():
        OP_95(0xFE, 18000, 0, -10500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A52)
    WaitChrThread(0xFE, 1)

    def lambda_2A70():
        OP_95(0xFE, 17100, 0, -9300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2A70)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x5A, 0x1F4)
    Return()

    # Function_18_29E3 end

    def Function_19_2A91(): pass

    label("Function_19_2A91")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)

    def lambda_2A9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A9E)

    def lambda_2AAF():
        OP_95(0xFE, 33000, -4000, -19000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AAF)
    Sleep(1000)

    def lambda_2ACC():
        OP_95(0xFE, 28000, -4000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ACC)
    WaitChrThread(0xFE, 1)

    def lambda_2AEA():
        OP_95(0xFE, 18000, -2000, -20000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AEA)
    WaitChrThread(0xFE, 1)

    def lambda_2B08():
        OP_95(0xFE, 18800, 0, -10600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B08)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    Return()

    # Function_19_2A91 end

    def Function_20_2B31(): pass

    label("Function_20_2B31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C87")

    def lambda_2B41():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2B41)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x2, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    Jump("Function_20_2B31")

    label("loc_2C87")

    Return()

    # Function_20_2B31 end

    def Function_21_2C88(): pass

    label("Function_21_2C88")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2C95():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C95)

    def lambda_2CAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CAF)
    WaitChrThread(0xFE, 1)

    def lambda_2CC4():
        OP_95(0xFE, 6300, 0, -3300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2CC4)
    WaitChrThread(0xF, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_21_2C88 end

    def Function_22_2CFB(): pass

    label("Function_22_2CFB")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2D08():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D08)

    def lambda_2D22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D22)
    WaitChrThread(0xFE, 1)

    def lambda_2D37():
        OP_95(0xFE, 7600, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D37)
    WaitChrThread(0x10, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 1, 0, 25)
    Return()

    # Function_22_2CFB end

    def Function_23_2D74(): pass

    label("Function_23_2D74")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2D81():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D81)

    def lambda_2D9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D9B)
    WaitChrThread(0xFE, 1)

    def lambda_2DB0():
        OP_95(0xFE, 5000, 0, -3500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DB0)
    WaitChrThread(0x11, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    BeginChrThread(0x18, 2, 0, 26)
    Return()

    # Function_23_2D74 end

    def Function_24_2DED(): pass

    label("Function_24_2DED")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2DFA():
        OP_95(0xFE, 5600, 0, -1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DFA)

    def lambda_2E14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E14)
    WaitChrThread(0xFE, 1)

    def lambda_2E29():
        OP_95(0xFE, 6400, 0, -2000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E29)
    WaitChrThread(0x12, 1)
    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    BeginChrThread(0xFE, 0, 0, 20)
    Return()

    # Function_24_2DED end

    def Function_25_2E60(): pass

    label("Function_25_2E60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E79")
    Sound(356, 0, 90, 0)
    Sleep(1200)
    Jump("Function_25_2E60")

    label("loc_2E79")

    Return()

    # Function_25_2E60 end

    def Function_26_2E7A(): pass

    label("Function_26_2E7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E93")
    Sound(957, 0, 80, 0)
    Sleep(1200)
    Jump("Function_26_2E7A")

    label("loc_2E93")

    Return()

    # Function_26_2E7A end

    SaveToFile()

Try(main)
