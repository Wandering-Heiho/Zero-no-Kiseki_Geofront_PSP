from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 6, 0, 7],
    )

    BuildStringList((
        "t1520",                  # 0
        "Chief Ursuline",         # 1
        "Marone",                 # 2
        "Medical Intern Chaleur", # 3
        "Medical Intern Lytton",  # 4
        "Medical Intern Gwen",    # 5
        "Nurse Meifa",            # 6
        "Doctor Belldine",        # 7
        "Chief Ursuline",         # 8
        "Cecile",                 # 9
    ))

    AddCharChip((
        "apl/ch50146.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch32800.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "chr/ch29500.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch29300.itc",                   # 06
        "chr/ch05300.itc",                   # 07
        "chr/ch32900.itc",                   # 08
    ))

    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5199,   0,       17700,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-47439,  0,       55720,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3630,    0,       54689,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(202830,  0,       340,     0,    389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-98839,  0,       53500,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(94459,   0,       52029,   90,   389,  0x0, 0,   8,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  19, 0x0000)

    ScpFunction((
        "Function_0_228",          # 00, 0
        "Function_1_2E0",          # 01, 1
        "Function_2_341",          # 02, 2
        "Function_3_3A2",          # 03, 3
        "Function_4_3CD",          # 04, 4
        "Function_5_3F8",          # 05, 5
        "Function_6_40B",          # 06, 6
        "Function_7_6AC",          # 07, 7
        "Function_8_7F5",          # 08, 8
        "Function_9_E2A",          # 09, 9
        "Function_10_1CC0",        # 0A, 10
        "Function_11_1F25",        # 0B, 11
        "Function_12_221A",        # 0C, 12
        "Function_13_27AE",        # 0D, 13
        "Function_14_28E1",        # 0E, 14
        "Function_15_2B51",        # 0F, 15
        "Function_16_2CA6",        # 10, 16
        "Function_17_3893",        # 11, 17
        "Function_18_3B90",        # 12, 18
        "Function_19_4014",        # 13, 19
    ))


    def Function_0_228(): pass

    label("Function_0_228")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_268"),
        (1, "loc_274"),
        (2, "loc_280"),
        (3, "loc_28C"),
        (4, "loc_298"),
        (5, "loc_2A4"),
        (6, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2BC"),
    )


    label("loc_268")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_274")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_280")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_28C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_298")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C8")

    label("loc_2DF")

    Return()

    # Function_0_228 end

    def Function_1_2E0(): pass

    label("Function_1_2E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_340")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_2E0")

    label("loc_340")

    Return()

    # Function_1_2E0 end

    def Function_2_341(): pass

    label("Function_2_341")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_341")

    label("loc_3A1")

    Return()

    # Function_2_341 end

    def Function_3_3A2(): pass

    label("Function_3_3A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CC")
    OP_94(0xFE, 0x3124A, 0x1CC, 0x31BC8, 0xE1A, 0x3E8)
    Sleep(400)
    Jump("Function_3_3A2")

    label("loc_3CC")

    Return()

    # Function_3_3A2 end

    def Function_4_3CD(): pass

    label("Function_4_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F7")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_4_3CD")

    label("loc_3F7")

    Return()

    # Function_4_3CD end

    def Function_5_3F8(): pass

    label("Function_5_3F8")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_5_3F8 end

    def Function_6_40B(): pass

    label("Function_6_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44B")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_475")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 203030, 0, 4610, 0)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4CF")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4E8")
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_6AB")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_507")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_54D")
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    Jump("loc_6AB")

    label("loc_54D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_566")
    ClearChrFlags(0xB, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A0")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BF")
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5E3")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xC, 0, 0, 3)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_61E")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 154520, 0, 53680, 90)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_648")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_672")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x9, 98920, 0, 10770, 270)
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_6AB")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 5)
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_6AB")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6AB")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0x8, 0, 0, 5)

    label("loc_6AB")

    Return()

    # Function_6_40B end

    def Function_7_6AC(): pass

    label("Function_7_6AC")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6D8")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6E6")
    Jump("loc_79A")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_701")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_71C")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_71C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_72E")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_740")
    OP_65(0x0, 0x1)
    Jump("loc_79A")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_79A")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_769")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_784")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)
    Jump("loc_79A")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_79A")
    SetMapObjFrame(0xFF, "BED01", 0x1, 0x1)

    label("loc_79A")

    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F4")

    label("loc_7DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_7F4")

    Return()

    # Function_7_6AC end

    def Function_8_7F5(): pass

    label("Function_8_7F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_E26")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_E26")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_822")
    Jump("loc_E26")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_830")
    Jump("loc_E26")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_932")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5")

    ChrTalk(
        0xFE,
        "Mmm... Good morning...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "W-Wait a second! I'm supposed\x01",
            "to already be in the exam room!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_92D")

    label("loc_8C5")


    ChrTalk(
        0xFE,
        (
            "Chaleur HAS to have been waiting\x01",
            "for me for a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, crap, oh, crap! What do I do?!\x02",
    )

    CloseMessageWindow()

    label("loc_92D")

    Jump("loc_E26")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_9E1")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97D")

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "J-Just five more minutes...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9CA")

    label("loc_97D")


    ChrTalk(
        0xFE,
        (
            "Give me fiv--no, fifteen minutes,\x01",
            "and I'll get up, all right...? Zzz...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_E26")

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9EF")
    Jump("loc_E26")

    label("loc_9EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AE9")
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whoa... This must be the new orbal\x01",
            "scalpel the others have been talking\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm. We've really come a long way,\x01",
            "haven't we? I still remember the days we\x01",
            "used old-fashioned metal scalpels...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_E26")

    label("loc_AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AF7")
    Jump("loc_E26")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B05")
    Jump("loc_E26")

    label("loc_B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B13")
    Jump("loc_E26")

    label("loc_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B21")
    Jump("loc_E26")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_B2F")
    Jump("loc_E26")

    label("loc_B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE3")

    ChrTalk(
        0xFE,
        "Uggghhhhh...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "A-Am I reading the clock correctly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OH SWEET AIDIOS! I'm supposed\x01",
            "to be in the exam room already!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C67")

    label("loc_BE3")


    ChrTalk(
        0xFE,
        (
            "I was up ALL night, so I think I fell\x01",
            "into a legitimate coma...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I better hurry or Doctor Gailey\x01",
            "will have my head! Again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C67")

    Jump("loc_E26")

    label("loc_C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(
        0xFE,
        "Mmmmm... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThere's no need to wake her up.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E26")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_DFC")
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")

    ChrTalk(
        0xFE,
        "Mmmmm... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "LOOK OUT! IT'S GONNA BLOW!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mmmmm... Zzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FWh-What kind of dream is that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x136,
        (
            "#1302FChief Ursuline is constantly doing something\x01",
            "or another around the hospital. We should\x01",
            "let her get some sleep, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DE5")

    label("loc_DD0")


    ChrTalk(
        0xFE,
        "Mmmmm... Zzz...\x02",
    )

    CloseMessageWindow()

    label("loc_DE5")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_E26")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_E26")
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "Zzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_E26")

    TalkEnd(0xFE)
    Return()

    # Function_8_7F5 end

    def Function_9_E2A(): pass

    label("Function_9_E2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F19")

    ChrTalk(
        0xFE,
        (
            "Oh, weren't you the girl that was\x01",
            "carried to Cecile's room yesterday...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203FI am sorry to have been a bother.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* It was stressful, all right. But I'm\x01",
            "just glad you're looking better now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F91")

    label("loc_F19")


    ChrTalk(
        0xFE,
        (
            "If you start feeling under the weather\x01",
            "again, come see us right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "After all, we're a hospital, aren't we?\x02",
    )

    CloseMessageWindow()

    label("loc_F91")

    Jump("loc_1CBC")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(
        0xFE,
        "Is it already this late?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I better finish cleaning up before\x01",
            "my shift ends...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10C1")

    ChrTalk(
        0xFE,
        (
            "Doctor Guenter lives in the men's\x01",
            "dormitory, too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's always a lazy bum in the morning,\x01",
            "so I have to make sure to give him a\x01",
            "good scolding before he starts work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_10C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1195")

    ChrTalk(
        0xFE,
        (
            "Chief Ursuline actually went to the research\x01",
            "ward on time for once, to my surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She usually stays there all night and comes\x01",
            "back in the morning... I wonder if she was\x01",
            "tired yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_1195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(
        0xFE,
        (
            "A little girl? I don't think she ran\x01",
            "through here, but I'm not sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Have you tried searching the hospital?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_13C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131D")

    ChrTalk(
        0xFE,
        (
            "Apparently, Cirone likes to dry\x01",
            "bedsheets on the roof around\x01",
            "this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I caught a glimpse of her staring up\x01",
            "at the sky on the balcony over there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She should really be more careful\x01",
            "if she's going to be up there...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13C0")

    label("loc_131D")


    ChrTalk(
        0xFE,
        (
            "I don't know if Cirone is just naive or\x01",
            "what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the very least, I wish she would be\x01",
            "a tad more wary of the men who tend\x01",
            "to step out onto the balcony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C0")

    Jump("loc_1CBC")

    label("loc_13C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1472")

    ChrTalk(
        0x9,
        (
            "Chief Ursuline had to lead a faculty\x01",
            "meeting this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It was an earlier one, so I bet she'll be\x01",
            "yawning a lot next time I see her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14F7")

    label("loc_1472")


    ChrTalk(
        0x9,
        (
            "Between you and me, Chief Ursuline\x01",
            "is constantly exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wouldn't put it past her to start\x01",
            "dozing off in her meeting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    Jump("loc_1CBC")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AB")

    ChrTalk(
        0xFE,
        (
            "It's soooo quiet... I guess the\x01",
            "entire staff has left already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh! This must be my chance to\x01",
            "clean every nook and cranny in\x01",
            "here, right?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_163C")

    label("loc_15AB")


    ChrTalk(
        0xFE,
        (
            "Hehehe, if that's the case...I'll make\x01",
            "this entire place shine before everyone\x01",
            "comes back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sweep* *scrub* *sweep* *scrub* *sweep*...!\x02",
    )

    CloseMessageWindow()

    label("loc_163C")

    Jump("loc_1CBC")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1711")

    ChrTalk(
        0xFE,
        (
            "Can't you read? This is the women's dormitory!\x01",
            "No men allowed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I wish that was the rule. Unfortunately,\x01",
            "you can't get to the research ward without\x01",
            "going through the dormitories.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17E0")

    ChrTalk(
        0xFE,
        (
            "*sweep* *sweep*... The hospital dormitories\x01",
            "are quite pretty, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since hospital staff work so late, these\x01",
            "rooms don't see much use. I prefer it\x01",
            "like this, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_17E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1907")

    ChrTalk(
        0xFE,
        (
            "I saw Lytton come back to his room a little\x01",
            "while ago. He must be taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After last month's attack, he took some\x01",
            "time to recover, but Doctor Guenter put\x01",
            "him right back to work once he did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess there's no harm in\x01",
            "resting when you can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1967")

    label("loc_1907")


    ChrTalk(
        0xFE,
        (
            "Hmm, I should probably go grab\x01",
            "a bite to eat. All this cleaning really\x01",
            "gets a girl hungry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    Jump("loc_1CBC")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_19D8")

    ChrTalk(
        0xFE,
        (
            "Chief Ursuline just sprinted out of\x01",
            "her room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Must've overslept again, like always.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_19D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1AB9")

    ChrTalk(
        0xFE,
        (
            "I finished cleaning up the dormitory like\x01",
            "I do everyday, but after finding a speck\x01",
            "of dirt, I just had to do another round.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's the women's dormitory, isn't it?\x01",
            "It HAS to be super clean for everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_1AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1B62")

    ChrTalk(
        0xFE,
        (
            "All right, this should be clean enough...\x01",
            "But I might have missed a spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I saw a small bit of dirt, and it\x01",
            "is driving me up the wall...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBC")

    label("loc_1B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1C6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1E")

    ChrTalk(
        0xFE,
        (
            "All the men should be out of their\x01",
            "rooms by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for any of them, they'll probably\x01",
            "be working hard in the hospital or research ward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C65")

    label("loc_1C1E")


    ChrTalk(
        0xFE,
        (
            "Speaking of which, I'm going to work just as hard\x01",
            "at cleaning! ☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C65")

    Jump("loc_1CBC")

    label("loc_1C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1CBC")

    ChrTalk(
        0xFE,
        "*sweep* *sweep*...*scrub* *scrub*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Cleaning is my liiiiiife! ☆\x02",
    )

    CloseMessageWindow()

    label("loc_1CBC")

    TalkEnd(0xFE)
    Return()

    # Function_9_E2A end

    def Function_10_1CC0(): pass

    label("Function_10_1CC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1CD1")
    Jump("loc_1F21")

    label("loc_1CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1CDF")
    Jump("loc_1F21")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1CED")
    Jump("loc_1F21")

    label("loc_1CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1CFB")
    Jump("loc_1F21")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1D09")
    Jump("loc_1F21")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D17")
    Jump("loc_1F21")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D25")
    Jump("loc_1F21")

    label("loc_1D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D33")
    Jump("loc_1F21")

    label("loc_1D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DE4")

    ChrTalk(
        0xFE,
        (
            "Chief Ursuline is out working in the\x01",
            "hospital, and I'm here in the dorms...\x01",
            "Can't say this happens often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This might be my chance for a\x01",
            "quick power nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F21")

    label("loc_1DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DF2")
    Jump("loc_1F21")

    label("loc_1DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E00")
    Jump("loc_1F21")

    label("loc_1E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1E0E")
    Jump("loc_1F21")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1EFC")

    ChrTalk(
        0xFE,
        (
            "I could have sworn that Chief Ursuline\x01",
            "would be late today, but lo and behold,\x01",
            "she somehow made it to work on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Immersing herself in her research until\x01",
            "dawn... No wonder she never makes it\x01",
            "to meetings on time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F21")

    label("loc_1EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1F0A")
    Jump("loc_1F21")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1F18")
    Jump("loc_1F21")

    label("loc_1F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F21")

    label("loc_1F21")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CC0 end

    def Function_11_1F25(): pass

    label("Function_11_1F25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1F36")
    Jump("loc_2216")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1FD5")

    ChrTalk(
        0xFE,
        (
            "I wanted to take it easy when I\x01",
            "got back to my room today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...tests are coming up, so I should\x01",
            "probably study for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2216")

    label("loc_1FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FE3")
    Jump("loc_2216")

    label("loc_1FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1FF1")
    Jump("loc_2216")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1FFF")
    Jump("loc_2216")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_200D")
    Jump("loc_2216")

    label("loc_200D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_201B")
    Jump("loc_2216")

    label("loc_201B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20B1")

    ChrTalk(
        0xFE,
        "*yawn*... Finally, a break.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's not like I have any plans, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should pick up fishing, like\x01",
            "Doctor Guenter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2216")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20BF")
    Jump("loc_2216")

    label("loc_20BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20CD")
    Jump("loc_2216")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_21D5")

    ChrTalk(
        0xFE,
        (
            "Honestly, it's hard to figure out what\x01",
            "Doctor Guenter is thinking most of\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At first, I thought he was handing off\x01",
            "some of his work to me to help me\x01",
            "with my studies...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I'm starting to think he just didn't\x01",
            "want to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2216")

    label("loc_21D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21E3")
    Jump("loc_2216")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_21F1")
    Jump("loc_2216")

    label("loc_21F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_21FF")
    Jump("loc_2216")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_220D")
    Jump("loc_2216")

    label("loc_220D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2216")

    label("loc_2216")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F25 end

    def Function_12_221A(): pass

    label("Function_12_221A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2414")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2346")

    ChrTalk(
        0xFE,
        (
            "Doctor Gailey Reutzel and...\x01",
            "Doctor Lago Nixon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Turns out that a lot of these textbooks\x01",
            "were written by St. Ursula doctors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You wouldn't think it, but this place is\x01",
            "actually a cutting-edge research facility.\x01",
            "It's filled with insanely smart people, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_240F")

    label("loc_2346")


    ChrTalk(
        0xFE,
        (
            "Oh, right. Is Doctor Guenter listed\x01",
            "as an author on any of these...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Joachim Guenter... Joachim Guenter...\x01",
            "Huh, I guess not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, he never struck me as the kinda\x01",
            "guy to publish a book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240F")

    Jump("loc_27AA")

    label("loc_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2422")
    Jump("loc_27AA")

    label("loc_2422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_24C8")

    ChrTalk(
        0xFE,
        (
            "I have some free time until evening,\x01",
            "so I should probably study...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might as well put those medical textbooks\x01",
            "I brought from home to good use.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AA")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24D6")
    Jump("loc_27AA")

    label("loc_24D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_24E4")
    Jump("loc_27AA")

    label("loc_24E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_24F2")
    Jump("loc_27AA")

    label("loc_24F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2500")
    Jump("loc_27AA")

    label("loc_2500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_250E")
    Jump("loc_27AA")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_251C")
    Jump("loc_27AA")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25B3")

    ChrTalk(
        0xFE,
        (
            "This evening, my practical training session\x01",
            "is being held in one of the exam rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll show that professor what I'm made of!\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AA")

    label("loc_25B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2769")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E4")

    ChrTalk(
        0xFE,
        (
            "I'm taking the day off, but I can't\x01",
            "neglect my studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll keep studying until\x01",
            "it's time to go get lunch with my\x01",
            "roommate, Flora.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My practical training is coming up next\x01",
            "month, and if I want to impress all the\x01",
            "professors, I have to start preparing now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2764")

    label("loc_26E4")


    ChrTalk(
        0xFE,
        (
            "If there's any chance at getting a good\x01",
            "evaluation on my next practical training,\x01",
            "I have to start studying hard right now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2764")

    Jump("loc_27AA")

    label("loc_2769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2777")
    Jump("loc_27AA")

    label("loc_2777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2785")
    Jump("loc_27AA")

    label("loc_2785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2793")
    Jump("loc_27AA")

    label("loc_2793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_27A1")
    Jump("loc_27AA")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_27AA")

    label("loc_27AA")

    TalkEnd(0xFE)
    Return()

    # Function_12_221A end

    def Function_13_27AE(): pass

    label("Function_13_27AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2859")

    ChrTalk(
        0xFE,
        (
            "I had the day off yesterday, but because\x01",
            "of Cirone and her hijinx, I'm absolutely\x01",
            "exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* I swear, that girl is bad for my heart.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_28DD")

    label("loc_2859")


    ChrTalk(
        0xFE,
        (
            "Well, while she was romping around the city,\x01",
            "I was able to let off some steam. So, I guess it\x01",
            "was a pretty nice day after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DD")

    TalkEnd(0xFE)
    Return()

    # Function_13_27AE end

    def Function_14_28E1(): pass

    label("Function_14_28E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28F2")
    Jump("loc_2B4D")

    label("loc_28F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2900")
    Jump("loc_2B4D")

    label("loc_2900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_290E")
    Jump("loc_2B4D")

    label("loc_290E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2990")

    ChrTalk(
        0xFE,
        (
            "I have the night shift, so I'm planning to\x01",
            "take an early nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you understand that, get out of my room.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B4D")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_299E")
    Jump("loc_2B4D")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_29AC")
    Jump("loc_2B4D")

    label("loc_29AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C7")
    Call(0, 15)
    Jump("loc_2A40")

    label("loc_29C7")


    ChrTalk(
        0xFE,
        (
            "*sigh* I accidentally slept for\x01",
            "way too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This wouldn't have happened if\x01",
            "I worked before taking the nap...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A40")

    Jump("loc_2B4D")

    label("loc_2A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A53")
    Jump("loc_2B4D")

    label("loc_2A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2AF0")

    ChrTalk(
        0xFE,
        (
            "You know, it's not very polite to enter\x01",
            "someone's room without their permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If this isn't an emergency, would you\x01",
            "kindly scram?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B4D")

    label("loc_2AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2AFE")
    Jump("loc_2B4D")

    label("loc_2AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B0C")
    Jump("loc_2B4D")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2B1A")
    Jump("loc_2B4D")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2B28")
    Jump("loc_2B4D")

    label("loc_2B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2B36")
    Jump("loc_2B4D")

    label("loc_2B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2B44")
    Jump("loc_2B4D")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2B4D")

    label("loc_2B4D")

    TalkEnd(0xFE)
    Return()

    # Function_14_28E1 end

    def Function_15_2B51(): pass

    label("Function_15_2B51")


    ChrTalk(
        0xFE,
        (
            "I keep trying to read this book I bought\x01",
            "about a doctor, but I can't get into it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I think it would have been\x01",
            "much better if it talked about his medical\x01",
            "experience... Oh, well, fiction is fiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Here. I don't really want it anymore.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x2CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CE, 1)
    SetScenarioFlags(0x9D, 0)
    Return()

    # Function_15_2B51 end

    def Function_16_2CA6(): pass

    label("Function_16_2CA6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2EC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC4")
    Call(0, 18)
    Jump("loc_2EC2")

    label("loc_2CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD5")

    ChrTalk(
        0x10,
        (
            "#1304FWell, I should probably give Michael\x01",
            "my undivided attention.\x02\x03",
            "#1300FAfter all, he's going to get lonely, with\x01",
            "Shizuku being gone for the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FEver the big sister, Cecile.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DCD")

    ChrTalk(
        0x10A,
        "#0608F(Wait, wasn't she his...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_2DCD")

    SetScenarioFlags(0x0, 4)
    Jump("loc_2EC2")

    label("loc_2DD5")


    ChrTalk(
        0x10,
        (
            "#1304FMaybe Michael would enjoy it if I read\x01",
            "him a picture book...\x02\x03",
            "#1302FGood thing I always keep the picture\x01",
            "books I read to Lloyd on hand. I never\x01",
            "know when I'm going to need them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Did you really have to share that?)\x02",
    )

    CloseMessageWindow()

    label("loc_2EC2")

    Jump("loc_388F")

    label("loc_2EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2ED5")
    Jump("loc_388F")

    label("loc_2ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF0")
    Call(0, 17)
    Jump("loc_30B5")

    label("loc_2EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302C")

    ChrTalk(
        0x10,
        (
            "#1300FOh, that's right. I'm going for a walk with\x01",
            "Shizuku around the hospital grounds.\x02\x03",
            "#1304FBecause of Shizuku's outstanding hearing,\x01",
            "she usually notices rabbits and birds that I\x01",
            "would normally never catch.\x02\x03",
            "#1300FIt may be a part of the job, but I can't\x01",
            "help but look forward to our walks.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_30B5")

    label("loc_302C")


    ChrTalk(
        0x10,
        (
            "#1300FEvery walk with Shizuku is its own little\x01",
            "adventure.\x02\x03",
            "It may be a part of the job, but I\x01",
            "can't help but look forward to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B5")

    Jump("loc_388F")

    label("loc_30BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_3595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D5")
    Call(0, 17)
    Jump("loc_3590")

    label("loc_30D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_END)), "loc_3177")

    ChrTalk(
        0x10,
        "#1309FHeehee. Welcome back, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FBy the way, Cecile...\x02\x03",
            "#0000FWas Ilya the person you were on\x01",
            "the phone with yesterday?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3348")

    label("loc_3177")


    ChrTalk(
        0x10,
        (
            "#1306FThat's right. Because I'm staying at\x01",
            "the St. Ursula dormitories, we haven't\x01",
            "had too many opportunities to hang out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FYeah, I suppose so.\x02\x03",
            "#0001FStill, Cecile, don't push yourself\x01",
            "too hard, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1309FOh, you. I'm not pushing myself too hard.\x02\x03",
            "Chatting with a friend on the phone\x01",
            "is one of the ways I relax, Lloyd.\x02\x03",
            "#1302FActually, I did just that last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWait...are you talking about Ilya?\x01",
            "You know, from Arc en Ciel?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3348")


    ChrTalk(
        0x10,
        (
            "#1305FOh, you know her?\x02\x03",
            "#1300FThat's odd. When did I tell you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0011FCrap!\x02\x03",
            "(I can't reveal anything about the investigation,\x01",
            "no matter how much I might trust her...)\x02\x03",
            "#0012FUh, funny story... Didn't you tell me about her\x01",
            "on the phone, a long time ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1303FHmmm...\x02\x03",
            "#1300FNow that you mention it, I DO\x01",
            "remember telling you about her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(Oh, thank you, Aidios...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 1)
    Jump("loc_3590")

    label("loc_34DB")


    ChrTalk(
        0x10,
        (
            "#1306F*sigh* What a shame.\x02\x03",
            "I was planning on having you two\x01",
            "meet and it was going to be a big,\x01",
            "grand surprise...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0012FH-Hahaha...\x01",
            "(Sorry, Cecile. I've already met her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3590")

    Jump("loc_388F")

    label("loc_3595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_388F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B0")
    Call(0, 17)
    Jump("loc_388F")

    label("loc_35B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381C")

    ChrTalk(
        0x10,
        (
            "#1306FThat's right. Because I'm staying at\x01",
            "the St. Ursula dormitories, we haven't\x01",
            "had too many opportunities to hang out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FHaha, I'm sorry to hear that.\x02\x03",
            "#0001FStill, Cecile, don't push yourself\x01",
            "too hard, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1309FOh, you. I'm not pushing myself too hard.\x02\x03",
            "Chatting with a friend on the phone\x01",
            "is one of the ways I relax, Lloyd.\x02\x03",
            "#1302FActually, I did just that last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0009FIs that right?\x02\x03",
            "#0000FDo I know said friend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1304FHeehee... Maybe, maybe not.\x02\x03",
            "#1302FYou aren't exactly well versed in popular\x01",
            "culture, so I'd be surprised if you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F...?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 0)
    Jump("loc_388F")

    label("loc_381C")


    ChrTalk(
        0x10,
        (
            "#1304FIf she's giving it her all, then I need to\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Who in the world is she talking about?)\x02",
    )

    CloseMessageWindow()

    label("loc_388F")

    TalkEnd(0xFE)
    Return()

    # Function_16_2CA6 end

    def Function_17_3893(): pass

    label("Function_17_3893")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        "#1302FHello, everyone!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_396E")

    ChrTalk(
        0x101,
        "#0005FIs this your dorm room, Cecile?\x02",
    )

    CloseMessageWindow()
    Jump("loc_39A4")

    label("loc_396E")


    ChrTalk(
        0x101,
        (
            "#0005FSo this really was your room,\x01",
            "huh, Cecile?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39A4")


    ChrTalk(
        0x10,
        (
            "#1300FYes it is.\x02\x03",
            "#1304FThough, I only use it about half of the time.\x01",
            "I often find myself falling asleep in what I\x01",
            "like to call the hospital's 'nap room.'\x02",
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
        "#0106FCecile, that's not healthy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0208FClassic case of overwork.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FC'mon, girl. You've gotta take\x01",
            "better care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1309FSettle down, you worrywarts.\x01",
            "I won't overdo it, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    SetScenarioFlags(0xAE, 5)
    EventEnd(0x5)
    Return()

    # Function_17_3893 end

    def Function_18_3B90(): pass

    label("Function_18_3B90")

    EventBegin(0x0)
    Fade(500)
    OP_68(153900, 1000, 53760, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BF0")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 150600, 0, 53680, 90)

    label("loc_3BF0")

    SetChrPos(0x101, 153000, 0, 54180, 90)
    SetChrPos(0x102, 153000, 0, 53180, 90)
    SetChrPos(0x103, 151800, 0, 53180, 90)
    SetChrPos(0x104, 151800, 0, 54180, 90)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0x5A, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        "#1308F...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Cecile stares at the framed photograph on her shelf.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCF")

    ChrTalk(
        0x101,
        (
            "#0005FCecile...?\x01",
            "(Wait, I know that photo...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CFB")

    label("loc_3CCF")


    ChrTalk(
        0x101,
        (
            "#0005FCecile...\x01",
            "(I know that photo...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D3C")

    ChrTalk(
        0x10A,
        "#0608F(This woman must have been his...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEC, 6)

    label("loc_3D3C")

    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x10, 0x10E, 0x1F4)

    ChrTalk(
        0x10,
        (
            "#1302FOh, I wasn't expecting you all.\x02\x03",
            "#1305FHmm...? If my eyes don't deceive\x01",
            "me, you all are in a bit of a rush.\x01",
            "Is something wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FWell, you could say that. We're in the\x01",
            "middle of an investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FAre you taking a break, Cecile?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#1304FI was just about to, yes.\x02\x03",
            "It's clear that whatever you're doing\x01",
            "is important, but don't overdo it.\x02\x03",
            "#1300FIf you do, I'll have no choice but to\x01",
            "hospitalize each and every one of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FM-Message received.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FWe'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0309F(Oh, man... What I wouldn't give for Cecile\x01",
            "to forcibly restrain me!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0206F(I knew you were going to say that.)\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 153000, 0, 53680, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_400E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_400E")

    SetScenarioFlags(0xEC, 5)
    EventEnd(0x5)
    Return()

    # Function_18_3B90 end

    def Function_19_4014(): pass

    label("Function_19_4014")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A framed photograph of Cecile, Lloyd, and a muscular man with\x01",
            "a determined look on his face sits on the shelf.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_415A")

    AnonymousTalk(
        0x101,
        (
            "#0008F(So she still has this photo, too...)\x02\x03",
            "(I always keep it on me, but Cecile\x01",
            "went and framed it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41D2")

    label("loc_415A")


    AnonymousTalk(
        0x101,
        (
            "#0005F(A photo of me, Cecile, and Guy?)\x02\x03",
            "#0003F(If that's here, that must mean that\x01",
            "this is Cecile's room, right?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D2")

    SetScenarioFlags(0x69, 5)

    label("loc_41D5")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_19_4014 end

    SaveToFile()

Try(main)
