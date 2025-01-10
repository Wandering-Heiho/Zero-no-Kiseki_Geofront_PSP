from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "a0000.bin",                # FileName
        "a0000",                    # MapName
        "a0000",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("a0000", "a0000_1", "a0000_2", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 45, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0000",                  # 0
        "Npl03",                  # 1
        "Randy",                  # 2
        "br2000",                 # 3
        "bm0113",                 # 4
        "br2000",                 # 5
        "bt3000",                 # 6
        "bm0112",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "bm3060",                 # 10
        "bm3070",                 # 11
        "Map Label 1",            # 12
        "Map Label 3",            # 13
    ))

    ATBonus("ATBonus_94", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_C4", 100, 1,   2,   3,   70,  89,  99)

    MonsterBattlePostion("MonsterBattlePostion_D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_100", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_104", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_108", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_10C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_110", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_114", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_138", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_13C", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_140", 11, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_144", 12, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_148", 5, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_14C", 2, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 14, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_154", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_198", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_19C", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B0", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_1B4", 0x0010, 3, 6, 45, 3, 3, 30, 0, "br2000", "Sepith_C4", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, "ms65000.dat", 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 9

    BattleInfo(
        "BattleInfo_1F8", 0x0042, 50, 6, 0, 0, 1, 0, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60001.dat", "ms60001.dat", "ms60001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_F4", "ed7405", "ed7403", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_23C", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_134", "MonsterBattlePostion_134", "ed7400", "ed7403", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_280", 0x0062, 40, 6, 60, 0, 0, 0, 0, "bt3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75400.dat", "ms75400.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_F4", "ed7405", "ed7000", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2C4", 0x0042, 50, 6, 0, 0, 1, 0, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "MonsterBattlePostion_174", "MonsterBattlePostion_F4", "ed7405", "ed7403", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_308", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_34C", 0x0010, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, "ms65000.dat", 0, "MonsterBattlePostion_D4", "MonsterBattlePostion_F4", "ed7400", "ed7403", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_390", 0x0010, 3, 6, 45, 3, 1, 30, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", "ms61600.dat", "ms69600.dat", 0, 0, 0, 0, "ms70100.dat", "MonsterBattlePostion_194", "MonsterBattlePostion_194", "ed7001", "ed7403", "ATBonus_B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch40000.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "chr/ch20100.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch20300.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch20600.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
    ))

    DeclNpc(-4000,   2000,    0,       135,  261,  0x0, 0,   3,   0,   0,   11,  0,   14,  255,  0)
    DeclNpc(-17989,  0,       -22840,  135,  261,  0x0, 0,   13,  0,   0,   11,  0,   14,  255,  0)

    DeclMonster(10000,   -14000,  0,       0x1010000,    "BattleInfo_1B4", 4,   5,   0xFFFF, 0,  1)

    DeclActor(2000,    0,       400000,  2000,    2000,    1000,    400000,  0x007C, 0,  2,  0x0000)

    PlaceName(10.0, 1.0, 2.0, 0x0000, 0x0000, "Map Label 1")
    PlaceName(-10.0, 1.0, 2.0, 0x0000, 0x0000, "Map Label 3")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_578",          # 01, 1
        "Function_2_5DA",          # 02, 2
        "Function_3_A59",          # 03, 3
        "Function_4_AE4",          # 04, 4
        "Function_5_B09",          # 05, 5
        "Function_6_B27",          # 06, 6
        "Function_7_168F",         # 07, 7
        "Function_8_18B4",         # 08, 8
        "Function_9_1D90",         # 09, 9
        "Function_10_1E3F",        # 0A, 10
        "Function_11_1EF7",        # 0B, 11
        "Function_12_1FAF",        # 0C, 12
        "Function_13_1FBF",        # 0D, 13
        "Function_14_1FFE",        # 0E, 14
        "Function_15_22C9",        # 0F, 15
        "Function_16_22F1",        # 10, 16
        "Function_17_2306",        # 11, 17
        "Function_18_2489",        # 12, 18
        "Function_19_248C",        # 13, 19
        "Function_20_248F",        # 14, 20
        "Function_21_2492",        # 15, 21
        "Function_22_2495",        # 16, 22
        "Function_23_2498",        # 17, 23
        "Function_24_249B",        # 18, 24
        "Function_25_249E",        # 19, 25
        "Function_26_24A1",        # 1A, 26
        "Function_27_257B",        # 1B, 27
        "Function_28_2623",        # 1C, 28
        "Function_29_279C",        # 1D, 29
        "Function_30_2B65",        # 1E, 30
        "Function_31_2FAA",        # 1F, 31
        "Function_32_33C2",        # 20, 32
        "Function_33_3754",        # 21, 33
        "Function_34_4195",        # 22, 34
        "Function_35_4258",        # 23, 35
        "Function_36_44D1",        # 24, 36
        "Function_37_46B2",        # 25, 37
        "Function_38_4B1E",        # 26, 38
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571")
    Call(0, 2)

    label("loc_571")

    SetScenarioFlags(0x5A, 0)
    Event(0, 6)
    Return()

    # Function_0_564 end

    def Function_1_578(): pass

    label("Function_1_578")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 5000, 0, 9000, 4000, 2000, 30000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 4000, 0, 8000, 4000, 2000, 30000)
    SetBarrier(0x2, 0x0, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x8)
    OP_63(0x9, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_1_578 end

    def Function_2_5DA(): pass

    label("Function_2_5DA")

    ClearMapFlags(0x80)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_32(0x0, 0xFB, 0x0)
    OP_32(0x1, 0xFB, 0x0)
    OP_32(0x2, 0xFB, 0x0)
    OP_32(0x3, 0xFB, 0x0)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x5, 0xFB, 0x0)
    OP_32(0x6, 0xFB, 0x0)
    OP_32(0x7, 0xFB, 0x0)
    OP_32(0x8, 0xFB, 0x0)
    OP_32(0x9, 0xFB, 0x0)
    OP_DE(0x0, 0x0)
    AddMira(2000)
    AddSepith(0xFF, 100)
    AddItemNumber(0x3E8, 1)
    AddItemNumber(0x3E9, 1)
    AddItemNumber(0x3EA, 1)
    AddItemNumber(0x3ED, 1)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    OP_42(0x0, 0x640, 0xFF)
    OP_42(0x1, 0x640, 0xFF)
    OP_42(0x2, 0x640, 0xFF)
    OP_42(0x3, 0x640, 0xFF)
    OP_42(0x8, 0x640, 0xFF)
    OP_42(0x9, 0x640, 0xFF)
    OP_42(0x6, 0x640, 0xFF)
    OP_42(0x7, 0x640, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x1, 0x5DC, 0xFF)
    OP_42(0x2, 0x5DC, 0xFF)
    OP_42(0x3, 0x5DC, 0xFF)
    OP_42(0x8, 0x5DC, 0xFF)
    OP_42(0x9, 0x5DC, 0xFF)
    OP_42(0x6, 0x5DC, 0xFF)
    OP_42(0x7, 0x5DC, 0xFF)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x1, 0x3FC, 0xFF)
    OP_42(0x2, 0x410, 0xFF)
    OP_42(0x3, 0x424, 0xFF)
    OP_42(0x9, 0x451, 0xFF)
    OP_42(0x8, 0x44C, 0xFF)
    AddCraft(0x0, 0x14A)
    AddCraft(0x1, 0x14A)
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    AddCraft(0x0, 0x14B)
    AddCraft(0x2, 0x14B)
    AddCraft(0x0, 0x14C)
    AddCraft(0x3, 0x14C)
    AddCraft(0x1, 0x14D)
    AddCraft(0x2, 0x14D)
    AddCraft(0x1, 0x14E)
    AddCraft(0x3, 0x14E)
    AddCraft(0x2, 0x14F)
    AddCraft(0x3, 0x14F)
    AddCraft(0x6, 0x150)
    AddCraft(0x7, 0x150)
    AddCraft(0x0, 0x154)
    AddCraft(0x0, 0x155)
    AddCraft(0x0, 0x156)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0x97)
    AddCraft(0x0, 0x98)
    AddCraft(0x0, 0x99)
    AddCraft(0x0, 0x9A)
    AddCraft(0x0, 0xFA)
    AddCraft(0x0, 0xFB)
    AddCraft(0x0, 0x12C)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xA1)
    AddCraft(0x1, 0xA2)
    AddCraft(0x1, 0xA3)
    AddCraft(0x1, 0xA4)
    AddCraft(0x1, 0xFF)
    AddCraft(0x1, 0x100)
    AddCraft(0x1, 0x12F)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0xAB)
    AddCraft(0x2, 0xAC)
    AddCraft(0x2, 0xAD)
    AddCraft(0x2, 0xAE)
    AddCraft(0x2, 0x104)
    AddCraft(0x2, 0x105)
    AddCraft(0x2, 0x132)
    SetScenarioFlags(0x5A, 2)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0xB5)
    AddCraft(0x3, 0xB6)
    AddCraft(0x3, 0xB7)
    AddCraft(0x3, 0xB8)
    AddCraft(0x3, 0x109)
    AddCraft(0x3, 0x10A)
    AddCraft(0x3, 0x135)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x10E)
    AddCraft(0x4, 0x138)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0x113)
    AddCraft(0x5, 0x13B)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0xD5)
    AddCraft(0x6, 0xD6)
    AddCraft(0x6, 0x118)
    AddCraft(0x6, 0x13E)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x11D)
    AddCraft(0x7, 0x141)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    AddCraft(0x8, 0x144)
    AddCraft(0x9, 0xF0)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF2)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0x127)
    AddCraft(0x9, 0x147)
    SetChrChipPat(0x0, 0x6, 0xFA)
    SetChrChipPat(0x2, 0x6, 0x104)
    SetChrChipPat(0x1, 0x6, 0xFF)
    SetChrChipPat(0x3, 0x6, 0x109)
    SetChrChipPat(0x6, 0x6, 0x118)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x81, 0x2)
    OP_38(0x0, 0x82, 0x2)
    OP_38(0x0, 0x83, 0x2)
    OP_38(0x0, 0x84, 0x2)
    OP_38(0x0, 0x85, 0x2)
    OP_38(0x0, 0x86, 0x2)
    AddItemNumber(0x6A, 1)
    AddItemNumber(0x6D, 1)
    AddItemNumber(0x70, 1)
    AddItemNumber(0x73, 1)
    AddItemNumber(0x76, 1)
    AddItemNumber(0x79, 1)
    RemoveCraft(0x0, 0xA)
    RemoveCraft(0x0, 0xB)
    RemoveCraft(0x0, 0xC)
    RemoveCraft(0x0, 0xD)
    RemoveCraft(0x0, 0xE)
    RemoveCraft(0x0, 0x14)
    RemoveCraft(0x0, 0x15)
    RemoveCraft(0x0, 0x16)
    RemoveCraft(0x0, 0x17)
    RemoveCraft(0x0, 0x18)
    RemoveCraft(0x0, 0x19)
    RemoveCraft(0x0, 0x1E)
    RemoveCraft(0x0, 0x1F)
    RemoveCraft(0x0, 0x20)
    RemoveCraft(0x0, 0x21)
    RemoveCraft(0x0, 0x22)
    RemoveCraft(0x0, 0x28)
    RemoveCraft(0x0, 0x29)
    RemoveCraft(0x0, 0x2A)
    RemoveCraft(0x0, 0x2B)
    RemoveCraft(0x0, 0x2C)
    RemoveCraft(0x0, 0x32)
    RemoveCraft(0x0, 0x33)
    RemoveCraft(0x0, 0x34)
    RemoveCraft(0x0, 0x3C)
    RemoveCraft(0x0, 0x48)
    RemoveCraft(0x0, 0x3E)
    RemoveCraft(0x0, 0x46)
    RemoveCraft(0x0, 0x47)
    RemoveCraft(0x0, 0x50)
    RemoveCraft(0x0, 0x51)
    RemoveCraft(0x0, 0x52)
    RemoveCraft(0x0, 0x53)
    RemoveCraft(0x0, 0x58)
    RemoveCraft(0x0, 0x59)
    RemoveCraft(0x0, 0x5A)
    RemoveCraft(0x0, 0x60)
    RemoveCraft(0x0, 0x61)
    RemoveCraft(0x0, 0x62)
    RemoveCraft(0x0, 0x63)
    RemoveCraft(0x0, 0x64)
    RemoveCraft(0x0, 0x68)
    RemoveCraft(0x0, 0x69)
    RemoveCraft(0x0, 0x6A)
    RemoveCraft(0x0, 0x70)
    RemoveCraft(0x0, 0x71)
    RemoveCraft(0x0, 0x72)
    RemoveCraft(0x0, 0x78)
    RemoveCraft(0x0, 0x79)
    RemoveCraft(0x0, 0x7A)
    RemoveCraft(0x0, 0x73)
    RemoveCraft(0x0, 0x80)
    RemoveCraft(0x0, 0x81)
    RemoveCraft(0x0, 0x82)
    RemoveCraft(0x0, 0x83)
    RemoveCraft(0x0, 0x84)
    RemoveCraft(0x0, 0x85)
    RemoveCraft(0x1, 0x50)
    RemoveCraft(0x1, 0x51)
    RemoveCraft(0x1, 0x52)
    RemoveCraft(0x1, 0x53)
    RemoveCraft(0x1, 0x58)
    RemoveCraft(0x1, 0x59)
    RemoveCraft(0x1, 0x5A)
    RemoveCraft(0x1, 0x60)
    RemoveCraft(0x1, 0x61)
    RemoveCraft(0x1, 0x62)
    RemoveCraft(0x1, 0x63)
    RemoveCraft(0x1, 0x64)
    RemoveCraft(0x1, 0x68)
    RemoveCraft(0x1, 0x69)
    RemoveCraft(0x1, 0x6A)
    RemoveCraft(0x1, 0x70)
    RemoveCraft(0x1, 0x71)
    RemoveCraft(0x1, 0x72)
    RemoveCraft(0x1, 0x78)
    RemoveCraft(0x1, 0x79)
    RemoveCraft(0x1, 0x7A)
    RemoveCraft(0x1, 0x73)
    RemoveCraft(0x1, 0x80)
    RemoveCraft(0x1, 0x81)
    RemoveCraft(0x1, 0x82)
    RemoveCraft(0x1, 0x83)
    RemoveCraft(0x1, 0x84)
    RemoveCraft(0x1, 0x85)
    RemoveCraft(0x2, 0x1E)
    RemoveCraft(0x2, 0x1F)
    RemoveCraft(0x2, 0x20)
    RemoveCraft(0x2, 0x21)
    RemoveCraft(0x3, 0x28)
    RemoveCraft(0x3, 0x29)
    RemoveCraft(0x3, 0x2A)
    RemoveCraft(0x3, 0x2B)
    RemoveCraft(0x6, 0x32)
    RemoveCraft(0x6, 0x33)
    RemoveCraft(0x6, 0x34)
    RemoveCraft(0x6, 0x3C)
    RemoveCraft(0x7, 0x48)
    RemoveCraft(0x7, 0x3E)
    RemoveCraft(0x7, 0x46)
    RemoveCraft(0x7, 0x47)
    Return()

    # Function_2_5DA end

    def Function_3_A59(): pass

    label("Function_3_A59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AE3")

    label("loc_A64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9D")
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_AA5")

    label("loc_A9D")

    Sleep(100)
    Jump("loc_A64")

    label("loc_AA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ADE")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD6")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_70(0x5, 0x78)
    Jump("loc_ADE")

    label("loc_AD6")

    Sleep(1)
    Jump("loc_AA5")

    label("loc_ADE")

    Jump("Function_3_A59")

    label("loc_AE3")

    Return()

    # Function_3_A59 end

    def Function_4_AE4(): pass

    label("Function_4_AE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B08")
    SetMapObjFrame(0x3, "motest06", 0x2, "play")
    Sleep(1000)
    Jump("Function_4_AE4")

    label("loc_B08")

    Return()

    # Function_4_AE4 end

    def Function_5_B09(): pass

    label("Function_5_B09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B26")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    Jump("Function_5_B09")

    label("loc_B26")

    Return()

    # Function_5_B09 end

    def Function_6_B27(): pass

    label("Function_6_B27")

    SetMapFlags(0x80)

    AnonymousTalk(
        0x101,
        (
            "ああああううううう\x01",
            "012345678901234567890123456789012345678901234567890123456789\x01",
            "English text test! Yeah! both languages are supported by this patch!\x02",
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1683")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Map Select\x01",                  # 0
            "Character Rooms\x01",             # 1
            "Battle Tests\x01",                # 2
            "Minigames\x01",                   # 3
            "Movies\x01",                      # 4
            "Quest-Related Tests\x01",         # 5
            "Pathing Test\x01",                # 6
            "Shop Tests\x01",                  # 7
            "KeA; Dog; Playthrough\x01",       # 8
            "Event Jump 1\x01",                # 9
            "Event Jump 2\x01",                # 10
            "Event Jump 3\x01",                # 11
            "General Dialogue Flags\x01",      # 12
            "Quest Flags\x01",                 # 13
            "Get; Reset\x01",                  # 14
            "Test\x01",                        # 15
        )
    )

    MenuCmd(4, 0, 0x3)
    MenuEnd(0x0)
    MenuCmd(4, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D31"),
        (1, "loc_D39"),
        (2, "loc_D41"),
        (3, "loc_D49"),
        (4, "loc_D51"),
        (5, "loc_EDA"),
        (6, "loc_148A"),
        (7, "loc_1498"),
        (8, "loc_14A5"),
        (9, "loc_15DD"),
        (10, "loc_15E8"),
        (11, "loc_15F3"),
        (12, "loc_15FE"),
        (13, "loc_1606"),
        (14, "loc_160E"),
        (15, "loc_1616"),
        (SWITCH_DEFAULT, "loc_1674"),
    )


    label("loc_D31")

    Call(1, 0)
    Jump("loc_167E")

    label("loc_D39")

    Call(0, 9)
    Jump("loc_167E")

    label("loc_D41")

    Call(0, 8)
    Jump("loc_167E")

    label("loc_D49")

    Call(0, 7)
    Jump("loc_167E")

    label("loc_D51")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "ed7_ev01\x01",      # 0
            "Missing\x01",       # 1
            "ed7_ev03\x01",      # 2
            "ed7_ev04\x01",      # 3
            "ed7_ev05\x01",      # 4
            "ed7_ev06\x01",      # 5
            "ed7_ev07\x01",      # 6
            "ed7_op\x01",        # 7
            "ed7_ed\x01",        # 8
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x0)
    OP_60(0x1)
    OP_C7(0x0, 0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DF7"),
        (1, "loc_E0F"),
        (2, "loc_E19"),
        (3, "loc_E31"),
        (4, "loc_E49"),
        (5, "loc_E61"),
        (6, "loc_E79"),
        (7, "loc_E91"),
        (8, "loc_EA7"),
        (SWITCH_DEFAULT, "loc_EBD"),
    )


    label("loc_DF7")

    PlayMovie(0x0, "ed7_ev01.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E0F")

    UseItem(0x2D6, 0xFF)
    Jump("loc_EBD")

    label("loc_E19")

    PlayMovie(0x0, "ed7_ev03.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E31")

    PlayMovie(0x0, "ed7_ev04.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E49")

    PlayMovie(0x0, "ed7_ev05.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E61")

    PlayMovie(0x0, "ed7_ev06.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E79")

    PlayMovie(0x0, "ed7_ev07.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_E91")

    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_EA7")

    PlayMovie(0x0, "ed7_ed.pmf", 0x2, 0x0)
    Jump("loc_EBD")

    label("loc_EBD")

    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C7(0x1, 0x10)
    FadeToBright(10, 0)
    Jump("loc_167E")

    label("loc_EDA")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Terminal\x01",                                      # 0
            "Report\x01",                                        # 1
            "Main: Prologue Main 2 (Begin)\x01",                 # 2
            "Main: Geofront Search (End)\x01",                   # 3
            "Side: Lost Item Search (Begin)\x01",                # 4
            "Side: Lost Item Search (End)\x01",                  # 5
            "Key: Support Request Explanation (Begin)\x01",      # 6
            "Key: Support Request Explanation (End)\x01",        # 7
            "get_note_fish\x01",                                 # 8
            "Give DP\x01",                                       # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_101B"),
        (1, "loc_130F"),
        (2, "loc_1337"),
        (3, "loc_135B"),
        (4, "loc_1377"),
        (5, "loc_13BE"),
        (6, "loc_13CE"),
        (7, "loc_13DE"),
        (8, "loc_13EE"),
        (9, "loc_147B"),
        (SWITCH_DEFAULT, "loc_1485"),
    )


    label("loc_101B")

    OP_57(0x0)
    OP_E3(0xA)
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_102B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FC")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_105E"),
        (1, "loc_1070"),
        (2, "loc_12C2"),
        (SWITCH_DEFAULT, "loc_12F7"),
    )


    label("loc_105E")

    OP_2B(0x0, 0x1, 0x2, 0x3, 0xB, 0xFFFF)
    Jump("loc_12F7")

    label("loc_1070")

    OP_E3(0x7)
    Sleep(500)
    Sound(2061, 255, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_1225")
    OutputDebugInt(0xDE)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            "Well, then, allow me to go over\x01",
            "your completed reports...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11BE")
    SetMapFlags(0x40000000)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        "Congratulations on ranking up.\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (1, "loc_111E"),
        (SWITCH_DEFAULT, "loc_1149"),
    )


    label("loc_111E")


    AnonymousTalk(
        0xFF,
        "14th Class... Great work, Lloyd!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1149")

    label("loc_1149")

    ClearMapFlags(0x40000000)

    AnonymousTalk(
        0xFF,
        (
            "I'll make sure your bonuses get transferred\x01",
            "to you right away!\x02\x03",
            "Thank you, and keep up the good work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1220")

    label("loc_11BE")

    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            "Thanks for this, everyone.\x02\x03",
            "If you finish more support requests,\x01",
            "please let me know!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1220")

    Jump("loc_12A0")

    label("loc_1225")

    OutputDebugInt(0x6F)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            "Hi, everyone! It seems there's nothing\x01",
            "you have to report now.\x02\x03",
            "When you do, please let me know, all right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_12A0")

    OP_E3(0x8)
    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        (
            "Testing\x01",
            "Testing\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_12C2")

    SetChrName("Fran")

    AnonymousTalk(
        0xFF,
        "I have not gone over the reports yet\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_12F7")

    Jump("loc_102B")

    label("loc_12FC")

    OP_E3(0x6)
    OP_E3(0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1485")

    label("loc_130F")

    OP_57(0x0)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_29(0x2, 0x4, 0x10)
    OP_29(0x5, 0x4, 0x10)
    OP_E3(0x3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1485")

    label("loc_1337")

    PlayBGM("ed7400", 0)
    OP_29(0x3C, 0x4, 0x2)
    OP_29(0x3C, 0x4, 0x80)
    OP_29(0x3C, 0x1, 0x0)
    OP_29(0x3D, 0x4, 0x2)
    OP_29(0x3D, 0x1, 0x0)
    Jump("loc_1485")

    label("loc_135B")

    StopBGM(0x2710)
    Sleep(3000)
    PlayBGM("ed7205", 0)
    OP_29(0x3C, 0x1, 0x1)
    OP_29(0x3C, 0x4, 0x10)
    Jump("loc_1485")

    label("loc_1377")

    StopBGM(0xFA0)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    Sound(901, 0, 100, 0)
    PlayBGM("ed7205", 0)
    OP_29(0x2, 0x4, 0x2)
    OP_29(0x2, 0x1, 0x0)
    Jump("loc_1485")

    label("loc_13BE")

    OP_29(0x2, 0x1, 0x1)
    OP_29(0x2, 0x4, 0x10)
    Jump("loc_1485")

    label("loc_13CE")

    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x1, 0x0)
    Jump("loc_1485")

    label("loc_13DE")

    OP_29(0x1, 0x1, 0x1)
    OP_29(0x1, 0x4, 0x10)
    Jump("loc_1485")

    label("loc_13EE")

    Sound(3, 1, 100, 0)
    Sleep(5000)
    OP_24(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141F")

    ChrTalk(
        0x0,
        "FISH_COUNT > 0\x02",
    )

    CloseMessageWindow()

    label("loc_141F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1447")

    ChrTalk(
        0x0,
        "FISH_MAXSIZE > 30\x02",
    )

    CloseMessageWindow()

    label("loc_1447")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1476")

    ChrTalk(
        0x0,
        "BATTLE_NOTE_MONSCOUNT > 2\x02",
    )

    CloseMessageWindow()

    label("loc_1476")

    Jump("loc_1485")

    label("loc_147B")

    OP_2C(0x1, 0x5A)
    Jump("loc_1485")

    label("loc_1485")

    Jump("loc_167E")

    label("loc_148A")

    NewScene("a0004", 0, 0, 0)
    IdleLoop()
    Jump("loc_167E")

    label("loc_1498")

    OP_60(0x0)
    OP_57(0x0)
    Call(0, 17)
    Jump("loc_167E")

    label("loc_14A5")

    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D2")
    MenuCmd(1, 1, "Set KeA to support role")
    Jump("loc_14EC")

    label("loc_14D2")

    MenuCmd(1, 1, "Set KeA to escort role")

    label("loc_14EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150A")
    MenuCmd(1, 1, "Enable Zeit")
    Jump("loc_151A")

    label("loc_150A")

    MenuCmd(1, 1, "Disable Zeit")

    label("loc_151A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1544")
    MenuCmd(1, 1, "Playthrough: subsequent")
    Jump("loc_155C")

    label("loc_1544")

    MenuCmd(1, 1, "Playthrough: initial")

    label("loc_155C")

    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1586"),
        (1, "loc_15A4"),
        (2, "loc_15BE"),
        (SWITCH_DEFAULT, "loc_15D8"),
    )


    label("loc_1586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1598")
    SetScenarioFlags(0x5A, 3)
    Jump("loc_159B")

    label("loc_1598")

    ClearScenarioFlags(0x5A, 3)

    label("loc_159B")

    AddParty(0x32, 0xFF, 0xFF)
    Jump("loc_15D8")

    label("loc_15A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B6")
    SetScenarioFlags(0x5A, 2)
    Jump("loc_15B9")

    label("loc_15B6")

    ClearScenarioFlags(0x5A, 2)

    label("loc_15B9")

    Jump("loc_15D8")

    label("loc_15BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D0")
    SetScenarioFlags(0x5A, 4)
    Jump("loc_15D3")

    label("loc_15D0")

    ClearScenarioFlags(0x5A, 4)

    label("loc_15D3")

    Jump("loc_15D8")

    label("loc_15D8")

    Jump("loc_167E")

    label("loc_15DD")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 0)
    Jump("loc_167E")

    label("loc_15E8")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 1)
    Jump("loc_167E")

    label("loc_15F3")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 2)
    Jump("loc_167E")

    label("loc_15FE")

    Call(2, 3)
    Jump("loc_167E")

    label("loc_1606")

    Call(2, 54)
    Jump("loc_167E")

    label("loc_160E")

    Call(0, 28)
    Jump("loc_167E")

    label("loc_1616")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_1659")

    ChrTalk(
        0x0,
        "EXTRA is enabled\x02",
    )

    Jump("loc_166F")

    label("loc_1659")


    ChrTalk(
        0x0,
        "EXTRA is disabled\x02",
    )


    label("loc_166F")

    Jump("loc_167E")

    label("loc_1674")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_167E")

    Jump("loc_BCF")

    label("loc_1683")

    OP_60(0x0)
    OP_57(0x0)
    OP_DB()
    ClearMapFlags(0x80)
    Return()

    # Function_6_B27 end

    def Function_7_168F(): pass

    label("Function_7_168F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1699")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18A6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Slot Machine\x01",                  # 0
            "Fishing\x01",                       # 1
            "Roulette\x01",                      # 2
            "Poker (medals)\x01",                # 3
            "Poker (head-to-head)\x01",          # 4
            "Blackjack (medals)\x01",            # 5
            "Blackjack (head-to-head)\x01",      # 6
            "Get medals\x01",                    # 7
            "Cancel\x01",                        # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_176E"),
        (1, "loc_1795"),
        (2, "loc_17BC"),
        (3, "loc_17E3"),
        (4, "loc_180A"),
        (5, "loc_1831"),
        (6, "loc_1858"),
        (7, "loc_187F"),
        (SWITCH_DEFAULT, "loc_188D"),
    )


    label("loc_176E")

    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_1795")

    MiniGame(0x6, 0x1, 0x0, 0x0, 0x0, 0x0, 0xFFFFFF38, 0x0, 0xFFFFF768)
    Jump("loc_1897")

    label("loc_17BC")

    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_17E3")

    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_180A")

    MiniGame(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_1831")

    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_1858")

    MiniGame(0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1897")

    label("loc_187F")

    OP_50(0x4B, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1897")

    label("loc_188D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1897")

    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1699")

    label("loc_18A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_7_168F end

    def Function_8_18B4(): pass

    label("Function_8_18B4")

    PlayBGM("ed7001", 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D82")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BTL_TEST_01 Test\x01",                  # 0
            "BTL_TEST_02 Ailments\x01",              # 1
            "BTL_TEST_03 Outside\x01",               # 2
            "BTL_TEST_04 Personal Use\x01",          # 3
            "BTL_TEST_05 Someone's Use\x01",         # 4
            "BTL_TEST_06 Someone's Use 2\x01",       # 5
            "BTL_MONSSET Party Choice\x01",          # 6
            "BTL_TEST_07 Final Boss\x01",            # 7
            "Self: Ll&Ra Vs: Wazy&Wald ①\x01",      # 8
            "Self: Ll&Ra Vs: Wazy&Wald ②\x01",      # 9
            "Self: Ll&Ra Vs: Est&Josh ①\x01",       # 10
            "Self: Ll&Ra Vs: Est&Josh ②\x01",       # 11
            "Self: Est&Josh Vs: Wazy&Wald\x01",      # 12
            "Self: Est&Josh Vs: Monsters\x01",       # 13
            "Self: Yin Vs: Mafia\x01",               # 14
            "With KeA\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AC8"),
        (1, "loc_1ADD"),
        (2, "loc_1AF2"),
        (3, "loc_1B07"),
        (4, "loc_1B1C"),
        (5, "loc_1B31"),
        (6, "loc_1B46"),
        (7, "loc_1B5B"),
        (8, "loc_1B70"),
        (9, "loc_1BB9"),
        (10, "loc_1C02"),
        (11, "loc_1C48"),
        (12, "loc_1C91"),
        (13, "loc_1CD4"),
        (14, "loc_1D17"),
        (15, "loc_1D5A"),
        (SWITCH_DEFAULT, "loc_1D73"),
    )


    label("loc_1AC8")

    Battle("BattleInfo_1B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1ADD")

    Battle("BattleInfo_1F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1AF2")

    Battle("BattleInfo_23C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1B07")

    Battle("BattleInfo_280", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1B1C")

    Battle("BattleInfo_2C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1B31")

    Battle("BattleInfo_308", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1B46")

    Battle("BattleInfo_34C", 0x0, 0x0, 0x0, 0x1, 0xFF)
    Jump("loc_1D73")

    label("loc_1B5B")

    Battle("BattleInfo_390", 0x30200010, 0x0, 0x4, 0xA, 0xFF)
    Jump("loc_1D73")

    label("loc_1B70")

    ClearScenarioFlags(0x5C, 0)
    Sleep(1000)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1D73")

    label("loc_1BB9")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x190, 0x0)
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1D73")

    label("loc_1C02")

    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1D73")

    label("loc_1C48")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x190, 0x0)
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1D73")

    label("loc_1C91")

    Battle(0xFFFFFFFF, 0x30200002, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1D73")

    label("loc_1CD4")

    Battle(0xFFFFFFFF, 0x30200003, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30063700, 0x30063700, 0x30063700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1D73")

    label("loc_1D17")

    Battle(0xFFFFFFFF, 0x30200004, "", 0x30000500, 0x0, 0x0, 0x0, 0x30031900, 0x30031100, 0x30031100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1D73")

    label("loc_1D5A")

    AddParty(0x52, 0xFF, 0xFF)
    Battle("BattleInfo_1B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1D73")

    label("loc_1D73")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18C2")

    label("loc_1D82")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_8_18B4 end

    def Function_9_1D90(): pass

    label("Function_9_1D90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E31")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "NPCs\x01",                   # 0
            "Battle Characters\x01",      # 1
            "Monsters\x01",               # 2
            "Cancel\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DF8"),
        (1, "loc_1E06"),
        (2, "loc_1E14"),
        (SWITCH_DEFAULT, "loc_1E22"),
    )


    label("loc_1DF8")

    NewScene("a0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E2C")

    label("loc_1E06")

    NewScene("a0001", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E2C")

    label("loc_1E14")

    NewScene("a0003", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E2C")

    label("loc_1E22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E2C")

    Jump("loc_1D9A")

    label("loc_1E31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_9_1D90 end

    def Function_10_1E3F(): pass

    label("Function_10_1E3F")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E7F"),
        (1, "loc_1E8B"),
        (2, "loc_1E97"),
        (3, "loc_1EA3"),
        (4, "loc_1EAF"),
        (5, "loc_1EBB"),
        (6, "loc_1EC7"),
        (SWITCH_DEFAULT, "loc_1ED3"),
    )


    label("loc_1E7F")

    OP_A0(0xFE, 1450, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1E8B")

    OP_A0(0xFE, 1550, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1E97")

    OP_A0(0xFE, 1600, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EA3")

    OP_A0(0xFE, 1400, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EAF")

    OP_A0(0xFE, 1650, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EBB")

    OP_A0(0xFE, 1350, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EC7")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1ED3")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF6")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_1EDF")

    label("loc_1EF6")

    Return()

    # Function_10_1E3F end

    def Function_11_1EF7(): pass

    label("Function_11_1EF7")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1F37"),
        (1, "loc_1F43"),
        (2, "loc_1F4F"),
        (3, "loc_1F5B"),
        (4, "loc_1F67"),
        (5, "loc_1F73"),
        (6, "loc_1F7F"),
        (SWITCH_DEFAULT, "loc_1F8B"),
    )


    label("loc_1F37")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F43")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F4F")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F5B")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F67")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F73")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F7F")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F8B")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1F97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FAE")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1F97")

    label("loc_1FAE")

    Return()

    # Function_11_1EF7 end

    def Function_12_1FAF(): pass

    label("Function_12_1FAF")

    TalkBegin(0xFF)

    ChrTalk(
        0x0,
        "Hey\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_12_1FAF end

    def Function_13_1FBF(): pass

    label("Function_13_1FBF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FFD")
    OP_9D(0xFE, 0x2BC, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    OP_9D(0xFE, 0x12C0, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    Jump("Function_13_1FBF")

    label("loc_1FFD")

    Return()

    # Function_13_1FBF end

    def Function_14_1FFE(): pass

    label("Function_14_1FFE")

    TalkBegin(0xFE)
    PlayBGM("ed7001", 0)
    VolumeBGM(0x1E, 0x0)
    RemoveParty(0x8, 0xFF)
    AddParty(0x37, 0xFF, 0xFF)
    TurnDirection(0xFE, 0x102, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BD(0x0, 0x63)"), scpexpr(EXPR_END)), "loc_20D1")

    ChrTalk(
        0x101,
        (
            "#0000F#NNo, don't worry about it.\x02\x03",
            "I understand#4RCrossbell# some of it from the letter...\x01",
            "Besides, even then#4RCrossbell#,\x01",
            "home#4RCrossbell# is home#4RCrossbell#.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20EE")

    label("loc_20D1")


    ChrTalk(
        0x138,
        "#0000FThis is Mariabell\x02",
    )

    CloseMessageWindow()

    label("loc_20EE")


    ChrTalk(
        0xFE,
        "Oh, my dear Elie\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x0,
        "Party 0 message\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1,
        "Party 1 message\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "Is this a message from Support Member Noel?\x01",
            "Toggle window.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#00FHe's he's he's never forgiven himself for that,\x01",
            "but he still overcame it to walk the\x01",
            "path of a bracer.\x02\x03",
            "#10FHe never stopped moving forward and\x01",
            "always did what he could to protect the\x01",
            "people most important to him.\x02\x03",
            "Even in the army, he's still striding\x01",
            "forward, day by day, even if he's\x01",
            "uncertain.\x02\x03",
            "#00FSo, Estelle, what will you do?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_14_1FFE end

    def Function_15_22C9(): pass

    label("Function_15_22C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F0")
    OP_94(0xFE, 0xFFFFD8F0, 0xFFFFD8F0, 0x2710, 0x2710, 0x157C)
    Jump("Function_15_22C9")

    label("loc_22F0")

    Return()

    # Function_15_22C9 end

    def Function_16_22F1(): pass

    label("Function_16_22F1")

    OP_95(0x0, -2000, 0, 22400, 4000, 0x0)
    Return()

    # Function_16_22F1 end

    def Function_17_2306(): pass

    label("Function_17_2306")

    SetChrName("Shopkeep")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "Which shop?\x02",
        )
    )


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Weapon Shop\x01",            # 0
            "Item Shop\x01",              # 1
            "Factory\x01",                # 2
            "Inn\x01",                    # 3
            "Ingredient Shop\x01",        # 4
            "Casino\x01",                 # 5
            "Exchange Shop\x01",          # 6
            "Upgrade Shop\x01",           # 7
            "Hidden Movie Test\x01",      # 8
            "Hidden Menu Test\x01",       # 9
            "Cancel\x01",                 # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_60(0x1)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23F9"),
        (1, "loc_2401"),
        (2, "loc_2409"),
        (3, "loc_2411"),
        (4, "loc_2419"),
        (5, "loc_2421"),
        (6, "loc_2429"),
        (7, "loc_2431"),
        (8, "loc_2439"),
        (9, "loc_2471"),
        (SWITCH_DEFAULT, "loc_2479"),
    )


    label("loc_23F9")

    Call(0, 18)
    Jump("loc_247E")

    label("loc_2401")

    Call(0, 19)
    Jump("loc_247E")

    label("loc_2409")

    Call(0, 20)
    Jump("loc_247E")

    label("loc_2411")

    Call(0, 21)
    Jump("loc_247E")

    label("loc_2419")

    Call(0, 22)
    Jump("loc_247E")

    label("loc_2421")

    Call(0, 23)
    Jump("loc_247E")

    label("loc_2429")

    Call(0, 24)
    Jump("loc_247E")

    label("loc_2431")

    Call(0, 25)
    Jump("loc_247E")

    label("loc_2439")

    OP_C7(0x0, 0x10)
    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C7(0x1, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Jump("loc_247E")

    label("loc_2471")

    Call(0, 26)
    Jump("loc_247E")

    label("loc_2479")

    Jump("loc_247E")

    label("loc_247E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_2306 end

    def Function_18_2489(): pass

    label("Function_18_2489")

    OP_AF(0x0)
    Return()

    # Function_18_2489 end

    def Function_19_248C(): pass

    label("Function_19_248C")

    OP_AF(0x14)
    Return()

    # Function_19_248C end

    def Function_20_248F(): pass

    label("Function_20_248F")

    OP_AF(0xA)
    Return()

    # Function_20_248F end

    def Function_21_2492(): pass

    label("Function_21_2492")

    OP_AF(0x32)
    Return()

    # Function_21_2492 end

    def Function_22_2495(): pass

    label("Function_22_2495")

    OP_AF(0x81)
    Return()

    # Function_22_2495 end

    def Function_23_2498(): pass

    label("Function_23_2498")

    OP_AF(0x3E)
    Return()

    # Function_23_2498 end

    def Function_24_249B(): pass

    label("Function_24_249B")

    OP_AF(0xA4)
    Return()

    # Function_24_249B end

    def Function_25_249E(): pass

    label("Function_25_249E")

    OP_AF(0xAE)
    Return()

    # Function_25_249E end

    def Function_26_24A1(): pass

    label("Function_26_24A1")

    MenuCmd(0, 2)
    MenuCmd(1, 2, "Item 01")
    MenuCmd(1, 2, "Item 02")
    MenuCmd(1, 2, "Item 03")
    MenuCmd(1, 2, "Item 04")
    MenuCmd(1, 2, "Item 05")
    MenuCmd(1, 2, "Item 06")
    MenuCmd(1, 2, "Item 07")
    MenuCmd(1, 2, "Item 08")
    MenuCmd(1, 2, "Item 09")
    MenuCmd(1, 2, "Item 10")
    MenuCmd(1, 2, "Item 11")
    MenuCmd(1, 2, "Item 12")
    MenuCmd(1, 2, "Item 13")
    MenuCmd(1, 2, "Item 14")
    MenuCmd(1, 2, "Item 15")
    MenuCmd(1, 2, "Item 16")
    MenuCmd(3, 2, 0x1)
    MenuCmd(3, 2, 0x8)
    MenuCmd(3, 2, 0x5)
    MenuCmd(3, 2, 0xE)
    MenuCmd(3, 2, 0xF)
    MenuCmd(3, 2, 0x9)
    MenuCmd(2, 2, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x2)
    Return()

    # Function_26_24A1 end

    def Function_27_257B(): pass

    label("Function_27_257B")

    EventBegin(0x1)

    ChrTalk(
        0x0,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()
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
        10,
        32,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    WaitChrThread(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2611")
    MiniGame(0x6, 0x1, 0x4B834, 0xFFFFFFBA, 0x4BB4, 0x5A, 0xFFFFFF38, 0x0, 0xFFFFF768)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_2622")

    label("loc_2611")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2622")
    EventEnd(0x1)

    label("loc_2622")

    Return()

    # Function_27_257B end

    def Function_28_2623(): pass

    label("Function_28_2623")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_262D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_278E")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Standard Equipment\x01",                        # 0
            "Arts & Crafts\x01",                             # 1
            "Detective Notebook / Combat Notebook\x01",      # 2
            "Recipe Notebook / Cooking\x01",                 # 3
            "Fish\x01",                                      # 4
            "Upgrade-Related\x01",                           # 5
            "Event Items\x01",                               # 6
            "DP Set\x01",                                    # 7
            "Other\x01",                                     # 8
            "Random Test\x01",                               # 9
            "Cancel\x01",                                    # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_272F"),
        (1, "loc_2737"),
        (2, "loc_273F"),
        (3, "loc_2747"),
        (4, "loc_274F"),
        (5, "loc_2757"),
        (6, "loc_275F"),
        (7, "loc_2767"),
        (8, "loc_276F"),
        (9, "loc_2777"),
        (SWITCH_DEFAULT, "loc_277F"),
    )


    label("loc_272F")

    Call(0, 29)
    Jump("loc_2789")

    label("loc_2737")

    Call(0, 30)
    Jump("loc_2789")

    label("loc_273F")

    Call(0, 31)
    Jump("loc_2789")

    label("loc_2747")

    Call(0, 32)
    Jump("loc_2789")

    label("loc_274F")

    Call(0, 33)
    Jump("loc_2789")

    label("loc_2757")

    Call(0, 34)
    Jump("loc_2789")

    label("loc_275F")

    Call(0, 35)
    Jump("loc_2789")

    label("loc_2767")

    Call(0, 36)
    Jump("loc_2789")

    label("loc_276F")

    Call(0, 37)
    Jump("loc_2789")

    label("loc_2777")

    Call(0, 38)
    Jump("loc_2789")

    label("loc_277F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2789")

    Jump("loc_262D")

    label("loc_278E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_28_2623 end

    def Function_29_279C(): pass

    label("Function_29_279C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B57")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Prologue Equipment (Lv. 3)\x01",         # 0
            "Ch. 1 Equipment (Lv. 7)\x01",            # 1
            "Ch. 2 Equipment (Lv. 16)\x01",           # 2
            "Ch. 3 Equipment (Lv. 22)\x01",           # 3
            "Ch. 4 Equipment (Lv. 29)\x01",           # 4
            "Finale Equipment (Lv. 34)\x01",          # 5
            "Final Boss Equipment (Lv. 44)\x01",      # 6
            "Cancel\x01",                             # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28B2"),
        (1, "loc_28E9"),
        (2, "loc_2921"),
        (3, "loc_2959"),
        (4, "loc_2991"),
        (5, "loc_29C9"),
        (6, "loc_29FE"),
        (SWITCH_DEFAULT, "loc_2B48"),
    )


    label("loc_28B2")

    Call(1, 46)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of prologue.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_28E9")

    Call(1, 49)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of chapter 1.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_2921")

    Call(1, 52)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of chapter 2.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_2959")

    Call(1, 55)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of chapter 3.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_2991")

    Call(1, 60)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of chapter 4.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_29C9")

    Call(1, 63)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for start of finale.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_29FE")

    AddItemNumber(0x1F5, 5)
    AddItemNumber(0x1F5, 30)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F9, 20)
    AddItemNumber(0x1FB, 5)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x1FE, 2)
    AddItemNumber(0x200, 5)
    AddItemNumber(0x201, 30)
    AddItemNumber(0x203, 30)
    AddItemNumber(0x204, 30)
    AddItemNumber(0x205, 30)
    AddItemNumber(0x190, 20)
    AddItemNumber(0x192, 20)
    AddItemNumber(0x195, 20)
    AddItemNumber(0x1C8, 20)
    AddItemNumber(0x1C9, 20)
    OP_42(0x0, 0x51, 0x3)
    OP_42(0x0, 0x50, 0x4)
    OP_42(0x1, 0x49, 0x3)
    OP_42(0x1, 0x58, 0x4)
    OP_42(0x2, 0x42, 0x3)
    OP_42(0x2, 0x56, 0x4)
    OP_42(0x3, 0x4F, 0x3)
    OP_42(0x3, 0x57, 0x4)
    OP_42(0x0, 0x81, 0x0)
    OP_42(0x0, 0x6C, 0x2)
    OP_42(0x0, 0x99, 0x1)
    OP_42(0x0, 0xAA, 0x6)
    OP_42(0x0, 0x75, 0x4)
    OP_42(0x0, 0x66, 0x5)
    OP_42(0x0, 0x7E, 0x3)
    OP_42(0x1, 0xA2, 0x0)
    OP_42(0x1, 0x6C, 0x4)
    OP_42(0x1, 0xA1, 0x5)
    OP_42(0x1, 0xAE, 0x6)
    OP_42(0x1, 0xA0, 0x1)
    OP_42(0x1, 0x66, 0x2)
    OP_42(0x1, 0x78, 0x3)
    OP_42(0x2, 0x66, 0x0)
    OP_42(0x2, 0xA6, 0x3)
    OP_42(0x2, 0x98, 0x2)
    OP_42(0x2, 0x87, 0x1)
    OP_42(0x2, 0x97, 0x6)
    OP_42(0x2, 0xA5, 0x5)
    OP_42(0x2, 0xA3, 0x4)
    OP_42(0x3, 0x9B, 0x0)
    OP_42(0x3, 0x9C, 0x4)
    OP_42(0x3, 0x6C, 0x3)
    OP_42(0x3, 0x75, 0x1)
    OP_42(0x3, 0x93, 0x2)
    OP_42(0x3, 0xB0, 0x6)
    OP_42(0x3, 0x7E, 0x5)
    OP_42(0x6, 0x6B, 0x0)
    OP_42(0x7, 0x6B, 0x0)
    Call(1, 68)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Equipment for final boss battle.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2B52")

    label("loc_2B48")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B52")

    Jump("loc_27A6")

    label("loc_2B57")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_29_279C end

    def Function_30_2B65(): pass

    label("Function_30_2B65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9C")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Unlock minimal orbment slots\x01",          # 0
            "Unlock all orbment slots level 1\x01",      # 1
            "Unlock all orbment slots level 2\x01",      # 2
            "Unlearn all arts\x01",                      # 3
            "Learn all arts for 4 members\x01",          # 4
            "Get all quartz\x01",                        # 5
            "Reset crafts\x01",                          # 6
            "Learn all crafts for 10 members\x01",       # 7
            "Learn level 2 combos\x01",                  # 8
            "Cancel\x01",                                # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CAF"),
        (1, "loc_2D0E"),
        (2, "loc_2D65"),
        (3, "loc_2DBC"),
        (4, "loc_2E25"),
        (5, "loc_2EA6"),
        (6, "loc_2ECC"),
        (7, "loc_2EF8"),
        (8, "loc_2F40"),
        (SWITCH_DEFAULT, "loc_2F8D"),
    )


    label("loc_2CAF")

    Call(1, 29)
    OP_38(0x0, 0x80, 0x1)
    OP_38(0x1, 0x80, 0x1)
    OP_38(0x2, 0x80, 0x1)
    OP_38(0x3, 0x80, 0x1)
    OP_38(0x4, 0x80, 0x1)
    OP_38(0x5, 0x80, 0x1)
    OP_38(0x6, 0x80, 0x1)
    OP_38(0x7, 0x80, 0x1)
    OP_38(0x8, 0x80, 0x1)
    OP_38(0x9, 0x80, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Set only center slot of orbments.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2D0E")

    Call(1, 29)
    OP_38(0x0, 0x7F, 0x1)
    OP_38(0x1, 0x7F, 0x1)
    OP_38(0x2, 0x7F, 0x1)
    OP_38(0x3, 0x7F, 0x1)
    OP_38(0x4, 0x7F, 0x1)
    OP_38(0x5, 0x7F, 0x1)
    OP_38(0x6, 0x7F, 0x1)
    OP_38(0x7, 0x7F, 0x1)
    OP_38(0x8, 0x7F, 0x1)
    OP_38(0x9, 0x7F, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All slots set to level 1.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2D65")

    Call(1, 29)
    OP_38(0x0, 0x7F, 0x2)
    OP_38(0x1, 0x7F, 0x2)
    OP_38(0x2, 0x7F, 0x2)
    OP_38(0x3, 0x7F, 0x2)
    OP_38(0x4, 0x7F, 0x2)
    OP_38(0x5, 0x7F, 0x2)
    OP_38(0x6, 0x7F, 0x2)
    OP_38(0x7, 0x7F, 0x2)
    OP_38(0x8, 0x7F, 0x2)
    OP_38(0x9, 0x7F, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All slots set to level 2.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2DBC")

    Call(1, 30)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Unlearned all arts.\x01",
            "Once quartz is changed,\x01",
            "arts will be reset according to quartz.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2E25")

    Call(1, 30)
    Call(1, 31)
    Call(1, 32)
    Call(1, 33)
    Call(1, 34)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Learned all arts for 4 members.\x01",
            "Once quartz is changed,\x01",
            "arts will be reset according to quartz.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2EA6")

    Call(1, 86)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all quartz.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2ECC")

    Call(1, 35)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Unlearned all crafts.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2EF8")

    Call(1, 35)
    Call(1, 36)
    Call(1, 37)
    Call(1, 38)
    Call(1, 39)
    Call(1, 40)
    Call(1, 41)
    Call(1, 42)
    Call(1, 43)
    Call(1, 44)
    Call(1, 45)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Learned all crafts.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2F40")

    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Learned all level 2 combo crafts.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2F97")

    label("loc_2F8D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F97")

    Jump("loc_2B6F")

    label("loc_2F9C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_30_2B65 end

    def Function_31_2FAA(): pass

    label("Function_31_2FAA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B4")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Detective Notebook: reset\x01",                             # 0
            "Detective Notebook: complete all\x01",                      # 1
            "Detective Notebook: complete main quests\x01",              # 2
            "Detective Notebook: complete side quests\x01",              # 3
            "Detective Notebook: side quests (reception only)\x01",      # 4
            "Detective Notebook: fail side quests\x01",                  # 5
            "Combat Notebook: reset\x01",                                # 6
            "Combat Notebook: fill out (all monsters)\x01",              # 7
            "Cancel\x01",                                                # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3133"),
        (1, "loc_316A"),
        (2, "loc_31B3"),
        (3, "loc_31FA"),
        (4, "loc_3241"),
        (5, "loc_329A"),
        (6, "loc_32E8"),
        (7, "loc_3344"),
        (SWITCH_DEFAULT, "loc_33A5"),
    )


    label("loc_3133")

    Call(1, 69)
    Call(1, 70)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reset the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_316A")

    Call(1, 71)
    Call(1, 72)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Completed all quests in the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_31B3")

    Call(1, 71)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Completed main quests in the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_31FA")

    Call(1, 72)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Completed side quests in the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_3241")

    Call(1, 70)
    Call(1, 73)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Completed reception-only side quests in the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_329A")

    Call(1, 70)
    Call(1, 73)
    Call(1, 74)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Failed all side quests in the Detective Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_32E8")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reset the Combat Notebook.\x01",
            "Please use the [F8] menu > page 6 > MonsNote.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_3344")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Filled out the Combat Notebook.\x01",
            "Please use the [F8] menu > page 6 > MonsNote.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_33AF")

    label("loc_33A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33AF")

    Jump("loc_2FB4")

    label("loc_33B4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_31_2FAA end

    def Function_32_33C2(): pass

    label("Function_32_33C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3746")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Recipe Notebook: reset\x01",                         # 0
            "Recipe Notebook: fill out\x01",                      # 1
            "Recipe Notebook: fill out (regular only)\x01",       # 2
            "Recipe Notebook: fill out (supreme only)\x01",       # 3
            "Recipe Notebook: fill out (peculiar only)\x01",      # 4
            "Get 50x each ingredient\x01",                        # 5
            "Get 10x all food items\x01",                         # 6
            "Get 1x all peculiar food items\x01",                 # 7
            "Cancel\x01",                                         # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3523"),
        (1, "loc_3568"),
        (2, "loc_35B4"),
        (3, "loc_3600"),
        (4, "loc_364C"),
        (5, "loc_3698"),
        (6, "loc_36C9"),
        (7, "loc_36FC"),
        (SWITCH_DEFAULT, "loc_3737"),
    )


    label("loc_3523")

    OP_B0(0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reset the all recipes in the Cooking Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_3568")

    Call(1, 75)
    Call(1, 76)
    Call(1, 77)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Filled out all recipes in the Cooking Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_35B4")

    Call(1, 75)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Filled out 'regular' recipes in the Cooking Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_3600")

    Call(1, 76)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Filled out 'supreme' recipes in the Cooking Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_364C")

    Call(1, 77)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Filled out 'failure' recipes in the Cooking Notebook.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_3698")

    Call(1, 78)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got 50 of all ingredients.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_36C9")

    Call(1, 79)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got 50 of all cooking items.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_36FC")

    Call(1, 80)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got 1 of all peculiar cooking items.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3741")

    label("loc_3737")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3741")

    Jump("loc_33CC")

    label("loc_3746")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_32_33C2 end

    def Function_33_3754(): pass

    label("Function_33_3754")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_375E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4187")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Fishing Notebook: reset\x01",                    # 0
            "Fishing Notebook: complete (all fish)\x01",      # 1
            "Get all fishing rods\x01",                       # 2
            "Get all fish bait\x01",                          # 3
            "Get all fish\x01",                               # 4
            "Get a certain fish\x01",                         # 5
            "Get a certain fish (x5)\x01",                    # 6
            "Discard all fish\x01",                           # 7
            "Rockfish check\x01",                             # 8
            "Cancel\x01",                                     # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_387D"),
        (1, "loc_38D6"),
        (2, "loc_3933"),
        (3, "loc_3975"),
        (4, "loc_3A13"),
        (5, "loc_3AAC"),
        (6, "loc_3D8B"),
        (7, "loc_406A"),
        (8, "loc_40E7"),
        (SWITCH_DEFAULT, "loc_4178"),
    )


    label("loc_387D")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reset Fishing Notebook.\x01",
            "Please use the [F5] menu > page 6 > FishNote.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4182")

    label("loc_38D6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Completed Fishing Notebook.\x01",
            "Please use the [F5] menu > page 6 > FishNote.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4182")

    label("loc_3933")

    AddItemNumber(0x32, 1)
    AddItemNumber(0x33, 1)
    AddItemNumber(0x34, 1)
    AddItemNumber(0x35, 1)
    AddItemNumber(0x37, 1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all fishing rods.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4182")

    label("loc_3975")

    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    AddItemNumber(0x188, 10)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x18A, 10)
    AddItemNumber(0x18B, 10)
    AddItemNumber(0x18C, 10)
    AddItemNumber(0x18D, 10)
    AddItemNumber(0x15E, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all fish bait.\x01",
            "Also got fish that can be used as bait.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4182")

    label("loc_3A13")

    AddItemNumber(0x15E, 10)
    AddItemNumber(0x15F, 10)
    AddItemNumber(0x160, 10)
    AddItemNumber(0x161, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x163, 10)
    AddItemNumber(0x164, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x166, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16A, 10)
    AddItemNumber(0x16B, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    AddItemNumber(0x16E, 10)
    AddItemNumber(0x16F, 10)
    AddItemNumber(0x170, 10)
    AddItemNumber(0x171, 10)
    AddItemNumber(0x172, 10)
    AddItemNumber(0x173, 10)
    AddItemNumber(0x174, 10)
    AddItemNumber(0x175, 10)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all fish.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4182")

    label("loc_3AAC")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Snow Crab\x01",           # 0
            "Armorican Carp\x01",      # 1
            "Tiger Rockfish\x01",      # 2
            "Rockeater\x01",           # 3
            "Carp\x01",                # 4
            "Raineater\x01",           # 5
            "Azelfish\x01",            # 6
            "Kasagin\x01",             # 7
            "Rainbow Trout\x01",       # 8
            "Trout\x01",               # 9
            "Salmon\x01",              # 10
            "Eel\x01",                 # 11
            "[→next]\x01",            # 12
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3B94"),
        (1, "loc_3B9E"),
        (2, "loc_3BA8"),
        (3, "loc_3BB2"),
        (4, "loc_3BBC"),
        (5, "loc_3BC6"),
        (6, "loc_3BD0"),
        (7, "loc_3BDA"),
        (8, "loc_3BE4"),
        (9, "loc_3BEE"),
        (10, "loc_3BF8"),
        (11, "loc_3C02"),
        (12, "loc_3C0C"),
        (SWITCH_DEFAULT, "loc_3D7C"),
    )


    label("loc_3B94")

    AddItemNumber(0x15E, 1)
    Jump("loc_3D7C")

    label("loc_3B9E")

    AddItemNumber(0x15F, 1)
    Jump("loc_3D7C")

    label("loc_3BA8")

    AddItemNumber(0x160, 1)
    Jump("loc_3D7C")

    label("loc_3BB2")

    AddItemNumber(0x161, 1)
    Jump("loc_3D7C")

    label("loc_3BBC")

    AddItemNumber(0x162, 1)
    Jump("loc_3D7C")

    label("loc_3BC6")

    AddItemNumber(0x163, 1)
    Jump("loc_3D7C")

    label("loc_3BD0")

    AddItemNumber(0x164, 1)
    Jump("loc_3D7C")

    label("loc_3BDA")

    AddItemNumber(0x165, 1)
    Jump("loc_3D7C")

    label("loc_3BE4")

    AddItemNumber(0x166, 1)
    Jump("loc_3D7C")

    label("loc_3BEE")

    AddItemNumber(0x167, 1)
    Jump("loc_3D7C")

    label("loc_3BF8")

    AddItemNumber(0x168, 1)
    Jump("loc_3D7C")

    label("loc_3C02")

    AddItemNumber(0x169, 1)
    Jump("loc_3D7C")

    label("loc_3C0C")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Pearlglass\x01",           # 0
            "Gluttonous Bass\x01",      # 1
            "Viperhead\x01",            # 2
            "Pythonhead\x01",           # 3
            "Catfish\x01",              # 4
            "Queen Crab\x01",           # 5
            "Electric Eel\x01",         # 6
            "Demon Catfish\x01",        # 7
            "Arch Crab\x01",            # 8
            "Gold Salmon\x01",          # 9
            "Noble Carp\x01",           # 10
            "Serpenthead\x01",          # 11
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3CFF"),
        (1, "loc_3D09"),
        (2, "loc_3D13"),
        (3, "loc_3D1D"),
        (4, "loc_3D27"),
        (5, "loc_3D31"),
        (6, "loc_3D3B"),
        (7, "loc_3D45"),
        (8, "loc_3D4F"),
        (9, "loc_3D59"),
        (10, "loc_3D63"),
        (11, "loc_3D6D"),
        (SWITCH_DEFAULT, "loc_3D77"),
    )


    label("loc_3CFF")

    AddItemNumber(0x16A, 1)
    Jump("loc_3D77")

    label("loc_3D09")

    AddItemNumber(0x16B, 1)
    Jump("loc_3D77")

    label("loc_3D13")

    AddItemNumber(0x16C, 1)
    Jump("loc_3D77")

    label("loc_3D1D")

    AddItemNumber(0x16D, 1)
    Jump("loc_3D77")

    label("loc_3D27")

    AddItemNumber(0x16E, 1)
    Jump("loc_3D77")

    label("loc_3D31")

    AddItemNumber(0x16F, 1)
    Jump("loc_3D77")

    label("loc_3D3B")

    AddItemNumber(0x170, 1)
    Jump("loc_3D77")

    label("loc_3D45")

    AddItemNumber(0x171, 1)
    Jump("loc_3D77")

    label("loc_3D4F")

    AddItemNumber(0x172, 1)
    Jump("loc_3D77")

    label("loc_3D59")

    AddItemNumber(0x173, 1)
    Jump("loc_3D77")

    label("loc_3D63")

    AddItemNumber(0x174, 1)
    Jump("loc_3D77")

    label("loc_3D6D")

    AddItemNumber(0x175, 1)
    Jump("loc_3D77")

    label("loc_3D77")

    Jump("loc_3D7C")

    label("loc_3D7C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4182")

    label("loc_3D8B")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Snow Crab\x01",           # 0
            "Armorican Carp\x01",      # 1
            "Tiger Rockfish\x01",      # 2
            "Rockeater\x01",           # 3
            "Carp\x01",                # 4
            "Raineater\x01",           # 5
            "Azelfish\x01",            # 6
            "Kasagin\x01",             # 7
            "Rainbow Trout\x01",       # 8
            "Trout\x01",               # 9
            "Salmon\x01",              # 10
            "Eel\x01",                 # 11
            "[→next]\x01",            # 12
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3E73"),
        (1, "loc_3E7D"),
        (2, "loc_3E87"),
        (3, "loc_3E91"),
        (4, "loc_3E9B"),
        (5, "loc_3EA5"),
        (6, "loc_3EAF"),
        (7, "loc_3EB9"),
        (8, "loc_3EC3"),
        (9, "loc_3ECD"),
        (10, "loc_3ED7"),
        (11, "loc_3EE1"),
        (12, "loc_3EEB"),
        (SWITCH_DEFAULT, "loc_405B"),
    )


    label("loc_3E73")

    AddItemNumber(0x15E, 5)
    Jump("loc_405B")

    label("loc_3E7D")

    AddItemNumber(0x15F, 5)
    Jump("loc_405B")

    label("loc_3E87")

    AddItemNumber(0x160, 5)
    Jump("loc_405B")

    label("loc_3E91")

    AddItemNumber(0x161, 5)
    Jump("loc_405B")

    label("loc_3E9B")

    AddItemNumber(0x162, 5)
    Jump("loc_405B")

    label("loc_3EA5")

    AddItemNumber(0x163, 5)
    Jump("loc_405B")

    label("loc_3EAF")

    AddItemNumber(0x164, 5)
    Jump("loc_405B")

    label("loc_3EB9")

    AddItemNumber(0x165, 5)
    Jump("loc_405B")

    label("loc_3EC3")

    AddItemNumber(0x166, 5)
    Jump("loc_405B")

    label("loc_3ECD")

    AddItemNumber(0x167, 5)
    Jump("loc_405B")

    label("loc_3ED7")

    AddItemNumber(0x168, 5)
    Jump("loc_405B")

    label("loc_3EE1")

    AddItemNumber(0x169, 5)
    Jump("loc_405B")

    label("loc_3EEB")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Pearlglass\x01",           # 0
            "Gluttonous Bass\x01",      # 1
            "Viperhead\x01",            # 2
            "Pythonhead\x01",           # 3
            "Catfish\x01",              # 4
            "Queen Crab\x01",           # 5
            "Electric Eel\x01",         # 6
            "Demon Catfish\x01",        # 7
            "Arch Crab\x01",            # 8
            "Gold Salmon\x01",          # 9
            "Noble Carp\x01",           # 10
            "Serpenthead\x01",          # 11
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3FDE"),
        (1, "loc_3FE8"),
        (2, "loc_3FF2"),
        (3, "loc_3FFC"),
        (4, "loc_4006"),
        (5, "loc_4010"),
        (6, "loc_401A"),
        (7, "loc_4024"),
        (8, "loc_402E"),
        (9, "loc_4038"),
        (10, "loc_4042"),
        (11, "loc_404C"),
        (SWITCH_DEFAULT, "loc_4056"),
    )


    label("loc_3FDE")

    AddItemNumber(0x16A, 5)
    Jump("loc_4056")

    label("loc_3FE8")

    AddItemNumber(0x16B, 5)
    Jump("loc_4056")

    label("loc_3FF2")

    AddItemNumber(0x16C, 5)
    Jump("loc_4056")

    label("loc_3FFC")

    AddItemNumber(0x16D, 5)
    Jump("loc_4056")

    label("loc_4006")

    AddItemNumber(0x16E, 5)
    Jump("loc_4056")

    label("loc_4010")

    AddItemNumber(0x16F, 5)
    Jump("loc_4056")

    label("loc_401A")

    AddItemNumber(0x170, 5)
    Jump("loc_4056")

    label("loc_4024")

    AddItemNumber(0x171, 5)
    Jump("loc_4056")

    label("loc_402E")

    AddItemNumber(0x172, 5)
    Jump("loc_4056")

    label("loc_4038")

    AddItemNumber(0x173, 5)
    Jump("loc_4056")

    label("loc_4042")

    AddItemNumber(0x174, 5)
    Jump("loc_4056")

    label("loc_404C")

    AddItemNumber(0x175, 5)
    Jump("loc_4056")

    label("loc_4056")

    Jump("loc_405B")

    label("loc_405B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4182")

    label("loc_406A")

    SubItemNumber(0x15E, 1)
    SubItemNumber(0x15F, 1)
    SubItemNumber(0x160, 1)
    SubItemNumber(0x161, 1)
    SubItemNumber(0x162, 1)
    SubItemNumber(0x163, 1)
    SubItemNumber(0x164, 1)
    SubItemNumber(0x165, 1)
    SubItemNumber(0x166, 1)
    SubItemNumber(0x167, 1)
    SubItemNumber(0x168, 1)
    SubItemNumber(0x169, 1)
    SubItemNumber(0x16A, 1)
    SubItemNumber(0x16B, 1)
    SubItemNumber(0x16C, 1)
    SubItemNumber(0x16D, 1)
    SubItemNumber(0x16E, 1)
    SubItemNumber(0x16F, 1)
    SubItemNumber(0x170, 1)
    SubItemNumber(0x171, 1)
    SubItemNumber(0x172, 1)
    SubItemNumber(0x173, 1)
    SubItemNumber(0x174, 1)
    SubItemNumber(0x175, 1)
    Jump("loc_4182")

    label("loc_40E7")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4148")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You have one or more rockfish.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4173")

    label("loc_4148")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You don't have any rockfish.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4173")

    Jump("loc_4182")

    label("loc_4178")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4182")

    Jump("loc_375E")

    label("loc_4187")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_33_3754 end

    def Function_34_4195(): pass

    label("Function_34_4195")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_419F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_424A")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "U-Material\x01",        # 0
            "Divine Cloth\x01",      # 1
            "Zemurian Ore\x01",      # 2
            "T-Material\x01",        # 3
            "Cancel\x01",            # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4213"),
        (1, "loc_421D"),
        (2, "loc_4227"),
        (3, "loc_4231"),
        (SWITCH_DEFAULT, "loc_423B"),
    )


    label("loc_4213")

    AddItemNumber(0x38E, 10)
    Jump("loc_4245")

    label("loc_421D")

    AddItemNumber(0x395, 10)
    Jump("loc_4245")

    label("loc_4227")

    AddItemNumber(0x396, 10)
    Jump("loc_4245")

    label("loc_4231")

    AddItemNumber(0x397, 10)
    Jump("loc_4245")

    label("loc_423B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4245")

    Jump("loc_419F")

    label("loc_424A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_34_4195 end

    def Function_35_4258(): pass

    label("Function_35_4258")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44C3")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Research Ward Access Card\x01",      # 0
            "All SSS room decorations\x01",       # 1
            "All books\x01",                      # 2
            "That book series\x01",               # 3
            "Crossbell State Map\x01",            # 4
            "Crossbell City Map\x01",             # 5
            "Map Jump On\x01",                    # 6
            "Map Jump Off\x01",                   # 7
            "GAMESTART_ON\x01",                   # 8
            "Cancel\x01",                         # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_435F"),
        (1, "loc_4369"),
        (2, "loc_4396"),
        (3, "loc_43E1"),
        (4, "loc_442C"),
        (5, "loc_4436"),
        (6, "loc_4462"),
        (7, "loc_446D"),
        (8, "loc_4478"),
        (SWITCH_DEFAULT, "loc_4480"),
    )


    label("loc_435F")

    AddItemNumber(0x335, 1)
    Jump("loc_448A")

    label("loc_4369")

    AddItemNumber(0x350, 1)
    AddItemNumber(0x351, 1)
    AddItemNumber(0x352, 1)
    AddItemNumber(0x353, 1)
    AddItemNumber(0x354, 1)
    AddItemNumber(0x355, 1)
    AddItemNumber(0x356, 1)
    AddItemNumber(0x357, 1)
    Jump("loc_448A")

    label("loc_4396")

    AddItemNumber(0x2C6, 1)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_448A")

    label("loc_43E1")

    SubItemNumber(0x2C6, 99)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_448A")

    label("loc_442C")

    AddItemNumber(0x5, 1)
    Jump("loc_448A")

    label("loc_4436")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "That item doesn't exist.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_448A")

    label("loc_4462")

    OP_C7(0x0, 0x1000)
    Jump("loc_448A")

    label("loc_446D")

    OP_C7(0x1, 0x1000)
    Jump("loc_448A")

    label("loc_4478")

    SetScenarioFlags(0x5A, 0)
    Jump("loc_448A")

    label("loc_4480")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_448A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44BE")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got item(s).\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_44BE")

    Jump("loc_4262")

    label("loc_44C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_35_4258 end

    def Function_36_44D1(): pass

    label("Function_36_44D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A4")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "0 DP\x01",        # 0
            "15 DP\x01",       # 1
            "30 DP\x01",       # 2
            "55 DP\x01",       # 3
            "70 DP\x01",       # 4
            "90 DP\x01",       # 5
            "110 DP\x01",      # 6
            "130 DP\x01",      # 7
            "150 DP\x01",      # 8
            "195 DP\x01",      # 9
            "224 DP\x01",      # 10
            "265 DP\x01",      # 11
            "294 DP\x01",      # 12
            "324 DP\x01",      # 13
            "380 DP\x01",      # 14
            "Cancel\x01",      # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_45C3"),
        (1, "loc_45D1"),
        (2, "loc_45DF"),
        (3, "loc_45ED"),
        (4, "loc_45FB"),
        (5, "loc_4609"),
        (6, "loc_4617"),
        (7, "loc_4625"),
        (8, "loc_4633"),
        (9, "loc_4641"),
        (10, "loc_464F"),
        (11, "loc_465D"),
        (12, "loc_466B"),
        (13, "loc_4679"),
        (14, "loc_4687"),
        (SWITCH_DEFAULT, "loc_4695"),
    )


    label("loc_45C3")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_45D1")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_45DF")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_45ED")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x37), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_45FB")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4609")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4617")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4625")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4633")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4641")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_464F")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_465D")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x109), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_466B")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x126), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4679")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x144), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4687")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x17C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469F")

    label("loc_4695")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_469F")

    Jump("loc_44DB")

    label("loc_46A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_36_44D1 end

    def Function_37_46B2(): pass

    label("Function_37_46B2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B10")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Remove all items\x01",                   # 0
            "Get standard items\x01",                 # 1
            "Get all equipment\x01",                  # 2
            "Get all accessories\x01",                # 3
            "Get all consumables\x01",                # 4
            "Get lots of sepith\x01",                 # 5
            "Set sepith to 0\x01",                    # 6
            "Get lots of quartz\x01",                 # 7
            "All members to brink of death\x01",      # 8
            "All achievements reset\x01",             # 9
            "Get all achievements\x01",               # 10
            "All of Crossbell\x01",                   # 11
            "Cancel\x01",                             # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4819"),
        (1, "loc_4849"),
        (2, "loc_48C0"),
        (3, "loc_4903"),
        (4, "loc_492E"),
        (5, "loc_496D"),
        (6, "loc_4998"),
        (7, "loc_49C3"),
        (8, "loc_49E9"),
        (9, "loc_4A3F"),
        (11, "loc_4A69"),
        (SWITCH_DEFAULT, "loc_4B01"),
    )


    label("loc_4819")

    SubItemNumber(0x270F, 99)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Removed all held items.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4849")

    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got standard items.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_48C0")

    Call(1, 81)
    Call(1, 82)
    Call(1, 83)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all equipment (weapons and armor).\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4903")

    Call(1, 84)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all accessories.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_492E")

    Call(1, 85)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all consumables (potions and tools).\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_496D")

    AddSepith(0xFF, 5000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got lots of sepith.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4998")

    SubSepith(0xFF, 9999)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Removed all sepith.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_49C3")

    Call(1, 86)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Got all quartz.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_49E9")

    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    OP_32(0x4, 0x2, 0x1)
    OP_32(0x5, 0x2, 0x1)
    OP_32(0x6, 0x2, 0x1)
    OP_32(0x7, 0x2, 0x1)
    OP_32(0x8, 0x2, 0x1)
    OP_32(0x9, 0x2, 0x1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Set all HP to 1.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4A3F")

    OP_DE(0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Reset achievements.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4A69")

    SetScenarioFlags(0xF8, 0)
    SetScenarioFlags(0xF8, 1)
    SetScenarioFlags(0xF8, 2)
    SetScenarioFlags(0xF8, 3)
    SetScenarioFlags(0xF8, 4)
    SetScenarioFlags(0xF8, 5)
    SetScenarioFlags(0xF8, 6)
    SetScenarioFlags(0xF8, 7)
    SetScenarioFlags(0xF9, 0)
    SetScenarioFlags(0xF9, 1)
    SetScenarioFlags(0xF9, 2)
    SetScenarioFlags(0xF9, 3)
    SetScenarioFlags(0xF9, 4)
    SetScenarioFlags(0xF9, 5)
    SetScenarioFlags(0xF9, 6)
    SetScenarioFlags(0xF9, 7)
    SetScenarioFlags(0xFA, 0)
    SetScenarioFlags(0xFA, 1)
    SetScenarioFlags(0xFA, 2)
    SetScenarioFlags(0xFA, 3)
    SetScenarioFlags(0xFA, 4)
    SetScenarioFlags(0xFA, 5)
    SetScenarioFlags(0xFA, 6)
    SetScenarioFlags(0xFA, 7)
    SetScenarioFlags(0xFB, 0)
    SetScenarioFlags(0xFB, 1)
    SetScenarioFlags(0xFB, 2)
    SetScenarioFlags(0xFB, 3)
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Now able to travel around Crossbell.\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4B0B")

    label("loc_4B01")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B0B")

    Jump("loc_46BC")

    label("loc_4B10")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_37_46B2 end

    def Function_38_4B1E(): pass

    label("Function_38_4B1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B98")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Loop sound\x01",      # 0
            "Stop sound\x01",      # 1
            "Cancel\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B76"),
        (1, "loc_4B81"),
        (SWITCH_DEFAULT, "loc_4B89"),
    )


    label("loc_4B76")

    Sound(479, 1, 100, 0)
    Jump("loc_4B93")

    label("loc_4B81")

    OP_24(0x1DF)
    Jump("loc_4B93")

    label("loc_4B89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B93")

    Jump("loc_4B28")

    label("loc_4B98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_38_4B1E end

    SaveToFile()

Try(main)
