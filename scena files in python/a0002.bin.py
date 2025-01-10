from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "a0002.bin",                # FileName
        "a0002",                    # MapName
        "a0002",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 25000, 500, 20, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0002",                  # 0
        "Dummy",                  # 1
        "Dummy",                  # 2
        "Dummy",                  # 3
        "Dummy",                  # 4
        "Dummy",                  # 5
        "Party Character",        # 6
        "NPC 1",                  # 7
        "NPC 2",                  # 8
        "Alternate Version 1",    # 9
        "Alternate Version 2",    # 10
        "Dummy",                  # 11
        "Dummy",                  # 12
        "Dummy",                  # 13
        "Dummy",                  # 14
        "Dummy",                  # 15
        "Dummy",                  # 16
        "Dummy",                  # 17
        "Dummy",                  # 18
        "Dummy",                  # 19
        "Dummy",                  # 20
        "Console",                # 21
    ))

    AddCharChip((
        "chr/ch40010.itc",                   # 00
        "chr/ch40011.itc",                   # 01
        "chr/ch40012.itc",                   # 02
        "chr/ch40013.itc",                   # 03
        "chr/ch40014.itc",                   # 04
        "chr/ch40015.itc",                   # 05
        "chr/ch40016.itc",                   # 06
        "chr/ch40017.itc",                   # 07
        "chr/ch40018.itc",                   # 08
        "chr/ch40018.itc",                   # 09
        "chr/ch40018.itc",                   # 0A
        "chr/ch40018.itc",                   # 0B
        "chr/ch40018.itc",                   # 0C
        "chr/ch40018.itc",                   # 0D
        "chr/ch40018.itc",                   # 0E
        "chr/ch40018.itc",                   # 0F
        "chr/ch40018.itc",                   # 10
        "chr/ch40018.itc",                   # 11
        "chr/ch40018.itc",                   # 12
        "chr/ch40018.itc",                   # 13
        "monster/ch60050.itc",               # 14
    ))

    DeclNpc(4000,    0,       4000,    180,  257,  0x0, 0,   0,   0,   0,   3,   0,   5,   255,  0)
    DeclNpc(8000,    0,       4000,    180,  257,  0x0, 0,   1,   0,   0,   3,   0,   6,   255,  0)
    DeclNpc(12000,   0,       4000,    180,  257,  0x0, 0,   2,   0,   0,   3,   0,   7,   255,  0)
    DeclNpc(16000,   0,       4000,    180,  257,  0x0, 0,   3,   0,   0,   3,   0,   8,   255,  0)
    DeclNpc(4000,    0,       8000,    180,  257,  0x0, 0,   4,   0,   0,   3,   0,   9,   255,  0)
    DeclNpc(8000,    0,       8000,    180,  257,  0x0, 0,   5,   0,   0,   3,   0,   10,  255,  0)
    DeclNpc(12000,   0,       8000,    180,  257,  0x0, 0,   6,   0,   0,   3,   0,   11,  255,  0)
    DeclNpc(16000,   0,       8000,    180,  257,  0x0, 0,   7,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(4000,    0,       12000,   180,  257,  0x0, 0,   8,   0,   0,   3,   0,   13,  255,  0)
    DeclNpc(8000,    0,       12000,   180,  257,  0x0, 0,   9,   0,   0,   3,   0,   14,  255,  0)
    DeclNpc(12000,   0,       12000,   180,  257,  0x0, 0,   10,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       12000,   180,  257,  0x0, 0,   11,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(4000,    0,       16000,   180,  257,  0x0, 0,   12,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(8000,    0,       16000,   180,  257,  0x0, 0,   13,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(12000,   0,       16000,   180,  257,  0x0, 0,   14,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       16000,   180,  257,  0x0, 0,   15,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(4000,    0,       20000,   180,  257,  0x0, 0,   16,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(8000,    0,       20000,   180,  257,  0x0, 0,   17,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(12000,   0,       20000,   180,  257,  0x0, 0,   18,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(16000,   0,       20000,   180,  257,  0x0, 0,   19,  0,   0,   3,   0,   4,   255,  0)
    DeclNpc(1000,    0,       4000,    180,  257,  0x0, 0,   20,  0,   255, 255, 0,   2,   255,  0)

    ScpFunction((
        "Function_0_370",          # 00, 0
        "Function_1_371",          # 01, 1
        "Function_2_372",          # 02, 2
        "Function_3_152E",         # 03, 3
        "Function_4_1636",         # 04, 4
        "Function_5_1642",         # 05, 5
        "Function_6_170B",         # 06, 6
        "Function_7_1845",         # 07, 7
        "Function_8_1985",         # 08, 8
        "Function_9_1BC2",         # 09, 9
        "Function_10_1DA1",        # 0A, 10
        "Function_11_2E65",        # 0B, 11
        "Function_12_438B",        # 0C, 12
        "Function_13_5873",        # 0D, 13
        "Function_14_6AAF",        # 0E, 14
    ))


    def Function_0_370(): pass

    label("Function_0_370")

    Return()

    # Function_0_370 end

    def Function_1_371(): pass

    label("Function_1_371")

    Return()

    # Function_1_371 end

    def Function_2_372(): pass

    label("Function_2_372")

    TalkBegin(0xFE)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    SetChrFlags(0x4, 0x8)
    SetChrFlags(0x5, 0x8)
    SetChrFlags(0x6, 0x8)
    SetChrFlags(0x7, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    OP_49()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ch00000 - ch01500\x01",      # 0
            "ch05000 - ch05900\x01",      # 1
            "ch06000 - ch06900\x01",      # 2
            "ch07000 - ch07900\x01",      # 3
            "ch20000 - ch21900\x01",      # 4
            "ch22000 - ch23900\x01",      # 5
            "ch24000 - ch25900\x01",      # 6
            "ch26000 - ch27900\x01",      # 7
            "ch28000 - ch29900\x01",      # 8
            "ch30000 - ch31900\x01",      # 9
            "ch40040 - ch40090\x01",      # 10
            "Cancel\x01",                 # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_531"),
        (1, "loc_655"),
        (2, "loc_783"),
        (3, "loc_8B1"),
        (4, "loc_9D6"),
        (5, "loc_D09"),
        (6, "loc_E74"),
        (7, "loc_FCD"),
        (8, "loc_1126"),
        (9, "loc_127F"),
        (10, "loc_13D8"),
        (SWITCH_DEFAULT, "loc_1487"),
    )


    label("loc_531")

    LoadChrToIndex("chr/ch00000.itc", 0x0)
    LoadChrToIndex("chr/ch00100.itc", 0x1)
    LoadChrToIndex("chr/ch00200.itc", 0x2)
    LoadChrToIndex("chr/ch00300.itc", 0x3)
    LoadChrToIndex("chr/ch00400.itc", 0x4)
    LoadChrToIndex("chr/ch00500.itc", 0x5)
    LoadChrToIndex("chr/ch00600.itc", 0x6)
    LoadChrToIndex("chr/ch00700.itc", 0x7)
    LoadChrToIndex("chr/ch00800.itc", 0x8)
    LoadChrToIndex("chr/ch00900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH00000 Lloyd")
    OP_8E(0x9, "CH00100 Elie")
    OP_8E(0xA, "CH00200 Tio")
    OP_8E(0xB, "CH00300 Randy")
    OP_8E(0xC, "CH00400 Wazy")
    OP_8E(0xD, "CH00500 Yin")
    OP_8E(0xE, "CH00600 Estelle")
    OP_8E(0xF, "CH00700 Joshua")
    OP_8E(0x10, "CH00800 Noel")
    OP_8E(0x11, "CH00900 Dudley")
    Jump("loc_1496")

    label("loc_655")

    LoadChrToIndex("chr/ch05000.itc", 0x0)
    LoadChrToIndex("chr/ch05100.itc", 0x1)
    LoadChrToIndex("chr/ch05200.itc", 0x2)
    LoadChrToIndex("chr/ch05300.itc", 0x3)
    LoadChrToIndex("chr/ch05400.itc", 0x4)
    LoadChrToIndex("chr/ch05500.itc", 0x5)
    LoadChrToIndex("chr/ch05600.itc", 0x6)
    LoadChrToIndex("chr/ch05700.itc", 0x7)
    LoadChrToIndex("chr/ch05800.itc", 0x8)
    LoadChrToIndex("chr/ch05900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH05000 KeA")
    OP_8E(0x9, "CH05100 Ilya")
    OP_8E(0xA, "CH05200 Rixia")
    OP_8E(0xB, "CH05300 Cecile")
    OP_8E(0xC, "CH05400 Shizuku")
    OP_8E(0xD, "CH05500 Mariabell")
    OP_8E(0xE, "CH05600 Dieter")
    OP_8E(0xF, "CH05700 Sonya")
    OP_8E(0x10, "CH05800 MacDowell")
    OP_8E(0x11, "CH05900 Ian")
    Jump("loc_1496")

    label("loc_783")

    LoadChrToIndex("chr/ch06000.itc", 0x0)
    LoadChrToIndex("chr/ch06100.itc", 0x1)
    LoadChrToIndex("chr/ch06200.itc", 0x2)
    LoadChrToIndex("chr/ch06300.itc", 0x3)
    LoadChrToIndex("chr/ch06400.itc", 0x4)
    LoadChrToIndex("chr/ch06500.itc", 0x5)
    LoadChrToIndex("chr/ch06600.itc", 0x6)
    LoadChrToIndex("chr/ch06700.itc", 0x7)
    LoadChrToIndex("chr/ch06800.itc", 0x8)
    LoadChrToIndex("chr/ch06900.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH06000 Grace")
    OP_8E(0x9, "CH06100 Jona")
    OP_8E(0xA, "CH06200 Marconi")
    OP_8E(0xB, "CH06300 Cao Lee")
    OP_8E(0xC, "CH06400 Pierre")
    OP_8E(0xD, "CH06500 Hartmann")
    OP_8E(0xE, "CH06600 Joerg")
    OP_8E(0xF, "CH06700 Domitri")
    OP_8E(0x10, "CH06800 Dino")
    OP_8E(0x11, "CH06900 Fran")
    Jump("loc_1496")

    label("loc_8B1")

    LoadChrToIndex("chr/ch07000.itc", 0x0)
    LoadChrToIndex("chr/ch07100.itc", 0x1)
    LoadChrToIndex("chr/ch07200.itc", 0x2)
    LoadChrToIndex("chr/ch07300.itc", 0x3)
    LoadChrToIndex("chr/ch07400.itc", 0x4)
    LoadChrToIndex("chr/ch07500.itc", 0x5)
    LoadChrToIndex("chr/ch40018.itc", 0x6)
    LoadChrToIndex("chr/ch40018.itc", 0x7)
    LoadChrToIndex("chr/ch40018.itc", 0x8)
    LoadChrToIndex("chr/ch40018.itc", 0x9)
    LoadChrToIndex("chr/ch40018.itc", 0xA)
    LoadChrToIndex("chr/ch40018.itc", 0xB)
    LoadChrToIndex("chr/ch40018.itc", 0xC)
    LoadChrToIndex("chr/ch40018.itc", 0xD)
    LoadChrToIndex("chr/ch40018.itc", 0xE)
    LoadChrToIndex("chr/ch40018.itc", 0xF)
    LoadChrToIndex("chr/ch40018.itc", 0x10)
    LoadChrToIndex("chr/ch40018.itc", 0x11)
    LoadChrToIndex("chr/ch40018.itc", 0x12)
    LoadChrToIndex("chr/ch40018.itc", 0x13)
    OP_8E(0x8, "CH07000 Oscar")
    OP_8E(0x9, "CH07100 Wendy")
    OP_8E(0xA, "CH07200 Colin")
    OP_8E(0xB, "CH07300 Kilika")
    OP_8E(0xC, "CH07400 Lechter")
    OP_8E(0xD, "CH07500 Cecile")
    OP_8E(0xE, "CH07600 KeA")
    OP_8E(0xF, "CH07700 KeA")
    OP_8E(0x10, "CH07800 Ilya")
    OP_8E(0x11, "CH07900 Ilya")
    Jump("loc_1496")

    label("loc_9D6")

    LoadChrToIndex("chr/ch20000.itc", 0x0)
    LoadChrToIndex("chr/ch20100.itc", 0x1)
    LoadChrToIndex("chr/ch20200.itc", 0x2)
    LoadChrToIndex("chr/ch20300.itc", 0x3)
    LoadChrToIndex("chr/ch20400.itc", 0x4)
    LoadChrToIndex("chr/ch20500.itc", 0x5)
    LoadChrToIndex("chr/ch20600.itc", 0x6)
    LoadChrToIndex("chr/ch20700.itc", 0x7)
    LoadChrToIndex("chr/ch20800.itc", 0x8)
    LoadChrToIndex("chr/ch20900.itc", 0x9)
    LoadChrToIndex("chr/ch21000.itc", 0xA)
    LoadChrToIndex("chr/ch21100.itc", 0xB)
    LoadChrToIndex("chr/ch21200.itc", 0xC)
    LoadChrToIndex("chr/ch21300.itc", 0xD)
    LoadChrToIndex("chr/ch21400.itc", 0xE)
    LoadChrToIndex("chr/ch21500.itc", 0xF)
    LoadChrToIndex("chr/ch21600.itc", 0x10)
    LoadChrToIndex("chr/ch21700.itc", 0x11)
    LoadChrToIndex("chr/ch21800.itc", 0x12)
    LoadChrToIndex("chr/ch21900.itc", 0x13)
    OP_8E(0x8, "CH20000 West Street - Old Man")
    OP_8E(0x9, "CH20100 West Street - Old Woman")
    OP_8E(0xA, "CH20200 West Street - Middle-Aged Man")
    OP_8E(0xB, "CH20300 West Street - Middle-Aged Woman")
    OP_8E(0xC, "CH20400 West Street - Young Man")
    OP_8E(0xD, "CH20500 West Street - Young Woman")
    OP_8E(0xE, "CH20600 West Street - Boy")
    OP_8E(0xF, "CH20700 West Street - Girl")
    OP_8E(0x10, "CH20800 East Street - Old Man")
    OP_8E(0x11, "CH20900 East Street - Old Woman")
    OP_8E(0x12, "CH21000 East Street - Middle-Aged Man")
    OP_8E(0x13, "CH21100 East Street - Middle-Aged Woman")
    OP_8E(0x14, "CH21200 East Street - Young Man")
    OP_8E(0x15, "CH21300 East Street - Young Woman")
    OP_8E(0x16, "CH21400 East Street - Boy")
    OP_8E(0x17, "CH21500 East Street - Girl")
    OP_8E(0x18, "CH21600 Noble - Old Man")
    OP_8E(0x19, "CH21700 Noble - Old Woman")
    OP_8E(0x1A, "CH21800 Noble - Middle-Aged Man")
    OP_8E(0x1B, "CH21900 Noble - Middle-Aged Woman")
    Jump("loc_1496")

    label("loc_D09")

    LoadChrToIndex("chr/ch22000.itc", 0x0)
    LoadChrToIndex("chr/ch22100.itc", 0x1)
    LoadChrToIndex("chr/ch22200.itc", 0x2)
    LoadChrToIndex("chr/ch22300.itc", 0x3)
    LoadChrToIndex("chr/ch22400.itc", 0x4)
    LoadChrToIndex("chr/ch22500.itc", 0x5)
    LoadChrToIndex("chr/ch22600.itc", 0x6)
    LoadChrToIndex("chr/ch22700.itc", 0x7)
    LoadChrToIndex("chr/ch22800.itc", 0x8)
    LoadChrToIndex("chr/ch22900.itc", 0x9)
    LoadChrToIndex("chr/ch23000.itc", 0xA)
    LoadChrToIndex("chr/ch23100.itc", 0xB)
    LoadChrToIndex("chr/ch23200.itc", 0xC)
    LoadChrToIndex("chr/ch23300.itc", 0xD)
    LoadChrToIndex("chr/ch23400.itc", 0xE)
    LoadChrToIndex("chr/ch23500.itc", 0xF)
    LoadChrToIndex("chr/ch23600.itc", 0x10)
    LoadChrToIndex("chr/ch23700.itc", 0x11)
    LoadChrToIndex("chr/ch23800.itc", 0x12)
    LoadChrToIndex("chr/ch23900.itc", 0x13)
    OP_8E(0x8, "CH22000 Noble - Young Man")
    OP_8E(0x9, "CH22100")
    OP_8E(0xA, "CH22200")
    OP_8E(0xB, "CH22300")
    OP_8E(0xC, "CH22400")
    OP_8E(0xD, "CH22500")
    OP_8E(0xE, "CH22600")
    OP_8E(0xF, "CH22700")
    OP_8E(0x10, "CH22800")
    OP_8E(0x11, "CH22900")
    OP_8E(0x12, "CH23000")
    OP_8E(0x13, "CH23100")
    OP_8E(0x14, "CH23200")
    OP_8E(0x15, "CH23300")
    OP_8E(0x16, "CH23400")
    OP_8E(0x17, "CH23500")
    OP_8E(0x18, "CH23600")
    OP_8E(0x19, "CH23700")
    OP_8E(0x1A, "CH23800")
    OP_8E(0x1B, "CH23900")
    Jump("loc_1496")

    label("loc_E74")

    LoadChrToIndex("chr/ch24000.itc", 0x0)
    LoadChrToIndex("chr/ch24100.itc", 0x1)
    LoadChrToIndex("chr/ch24200.itc", 0x2)
    LoadChrToIndex("chr/ch24300.itc", 0x3)
    LoadChrToIndex("chr/ch24400.itc", 0x4)
    LoadChrToIndex("chr/ch24500.itc", 0x5)
    LoadChrToIndex("chr/ch24600.itc", 0x6)
    LoadChrToIndex("chr/ch24700.itc", 0x7)
    LoadChrToIndex("chr/ch24800.itc", 0x8)
    LoadChrToIndex("chr/ch24900.itc", 0x9)
    LoadChrToIndex("chr/ch25000.itc", 0xA)
    LoadChrToIndex("chr/ch25100.itc", 0xB)
    LoadChrToIndex("chr/ch25200.itc", 0xC)
    LoadChrToIndex("chr/ch25300.itc", 0xD)
    LoadChrToIndex("chr/ch25400.itc", 0xE)
    LoadChrToIndex("chr/ch25500.itc", 0xF)
    LoadChrToIndex("chr/ch25600.itc", 0x10)
    LoadChrToIndex("chr/ch25700.itc", 0x11)
    LoadChrToIndex("chr/ch25800.itc", 0x12)
    LoadChrToIndex("chr/ch25900.itc", 0x13)
    OP_8E(0x8, "CH24000")
    OP_8E(0x9, "CH24100")
    OP_8E(0xA, "CH24200")
    OP_8E(0xB, "CH24300")
    OP_8E(0xC, "CH24400")
    OP_8E(0xD, "CH24500")
    OP_8E(0xE, "CH24600")
    OP_8E(0xF, "CH24700")
    OP_8E(0x10, "CH24800")
    OP_8E(0x11, "CH24900")
    OP_8E(0x12, "CH25000")
    OP_8E(0x13, "CH25100")
    OP_8E(0x14, "CH25200")
    OP_8E(0x15, "CH25300")
    OP_8E(0x16, "CH25400")
    OP_8E(0x17, "CH25500")
    OP_8E(0x18, "CH25600")
    OP_8E(0x19, "CH25700")
    OP_8E(0x1A, "CH25800")
    OP_8E(0x1B, "CH25900")
    Jump("loc_1496")

    label("loc_FCD")

    LoadChrToIndex("chr/ch26000.itc", 0x0)
    LoadChrToIndex("chr/ch26100.itc", 0x1)
    LoadChrToIndex("chr/ch26200.itc", 0x2)
    LoadChrToIndex("chr/ch26300.itc", 0x3)
    LoadChrToIndex("chr/ch26400.itc", 0x4)
    LoadChrToIndex("chr/ch26500.itc", 0x5)
    LoadChrToIndex("chr/ch26600.itc", 0x6)
    LoadChrToIndex("chr/ch26700.itc", 0x7)
    LoadChrToIndex("chr/ch26800.itc", 0x8)
    LoadChrToIndex("chr/ch26900.itc", 0x9)
    LoadChrToIndex("chr/ch27000.itc", 0xA)
    LoadChrToIndex("chr/ch27100.itc", 0xB)
    LoadChrToIndex("chr/ch27200.itc", 0xC)
    LoadChrToIndex("chr/ch27300.itc", 0xD)
    LoadChrToIndex("chr/ch27400.itc", 0xE)
    LoadChrToIndex("chr/ch27500.itc", 0xF)
    LoadChrToIndex("chr/ch27600.itc", 0x10)
    LoadChrToIndex("chr/ch27700.itc", 0x11)
    LoadChrToIndex("chr/ch27800.itc", 0x12)
    LoadChrToIndex("chr/ch27900.itc", 0x13)
    OP_8E(0x8, "CH26000")
    OP_8E(0x9, "CH26100")
    OP_8E(0xA, "CH26200")
    OP_8E(0xB, "CH26300")
    OP_8E(0xC, "CH26400")
    OP_8E(0xD, "CH26500")
    OP_8E(0xE, "CH26600")
    OP_8E(0xF, "CH26700")
    OP_8E(0x10, "CH26800")
    OP_8E(0x11, "CH26900")
    OP_8E(0x12, "CH27000")
    OP_8E(0x13, "CH27100")
    OP_8E(0x14, "CH27200")
    OP_8E(0x15, "CH27300")
    OP_8E(0x16, "CH27400")
    OP_8E(0x17, "CH27500")
    OP_8E(0x18, "CH27600")
    OP_8E(0x19, "CH27700")
    OP_8E(0x1A, "CH27800")
    OP_8E(0x1B, "CH27900")
    Jump("loc_1496")

    label("loc_1126")

    LoadChrToIndex("chr/ch28000.itc", 0x0)
    LoadChrToIndex("chr/ch28100.itc", 0x1)
    LoadChrToIndex("chr/ch28200.itc", 0x2)
    LoadChrToIndex("chr/ch28300.itc", 0x3)
    LoadChrToIndex("chr/ch28400.itc", 0x4)
    LoadChrToIndex("chr/ch28500.itc", 0x5)
    LoadChrToIndex("chr/ch28600.itc", 0x6)
    LoadChrToIndex("chr/ch28700.itc", 0x7)
    LoadChrToIndex("chr/ch28800.itc", 0x8)
    LoadChrToIndex("chr/ch28900.itc", 0x9)
    LoadChrToIndex("chr/ch29000.itc", 0xA)
    LoadChrToIndex("chr/ch29100.itc", 0xB)
    LoadChrToIndex("chr/ch29200.itc", 0xC)
    LoadChrToIndex("chr/ch29300.itc", 0xD)
    LoadChrToIndex("chr/ch29400.itc", 0xE)
    LoadChrToIndex("chr/ch29500.itc", 0xF)
    LoadChrToIndex("chr/ch29600.itc", 0x10)
    LoadChrToIndex("chr/ch29700.itc", 0x11)
    LoadChrToIndex("chr/ch29800.itc", 0x12)
    LoadChrToIndex("chr/ch29900.itc", 0x13)
    OP_8E(0x8, "CH28000")
    OP_8E(0x9, "CH28100")
    OP_8E(0xA, "CH28200")
    OP_8E(0xB, "CH28300")
    OP_8E(0xC, "CH28400")
    OP_8E(0xD, "CH28500")
    OP_8E(0xE, "CH28600")
    OP_8E(0xF, "CH28700")
    OP_8E(0x10, "CH28800")
    OP_8E(0x11, "CH28900")
    OP_8E(0x12, "CH29000")
    OP_8E(0x13, "CH29100")
    OP_8E(0x14, "CH29200")
    OP_8E(0x15, "CH29300")
    OP_8E(0x16, "CH29400")
    OP_8E(0x17, "CH29500")
    OP_8E(0x18, "CH29600")
    OP_8E(0x19, "CH29700")
    OP_8E(0x1B, "CH29800")
    OP_8E(0x1B, "CH29900")
    Jump("loc_1496")

    label("loc_127F")

    LoadChrToIndex("chr/ch30000.itc", 0x0)
    LoadChrToIndex("chr/ch30100.itc", 0x1)
    LoadChrToIndex("chr/ch30200.itc", 0x2)
    LoadChrToIndex("chr/ch30300.itc", 0x3)
    LoadChrToIndex("chr/ch30400.itc", 0x4)
    LoadChrToIndex("chr/ch30500.itc", 0x5)
    LoadChrToIndex("chr/ch30600.itc", 0x6)
    LoadChrToIndex("chr/ch30700.itc", 0x7)
    LoadChrToIndex("chr/ch30800.itc", 0x8)
    LoadChrToIndex("chr/ch30900.itc", 0x9)
    LoadChrToIndex("chr/ch31000.itc", 0xA)
    LoadChrToIndex("chr/ch31100.itc", 0xB)
    LoadChrToIndex("chr/ch31200.itc", 0xC)
    LoadChrToIndex("chr/ch31300.itc", 0xD)
    LoadChrToIndex("chr/ch31400.itc", 0xE)
    LoadChrToIndex("chr/ch31500.itc", 0xF)
    LoadChrToIndex("chr/ch31600.itc", 0x10)
    LoadChrToIndex("chr/ch31700.itc", 0x11)
    LoadChrToIndex("chr/ch31800.itc", 0x12)
    LoadChrToIndex("chr/ch31900.itc", 0x13)
    OP_8E(0x8, "CH30000")
    OP_8E(0x9, "CH30100")
    OP_8E(0xA, "CH30200")
    OP_8E(0xB, "CH30300")
    OP_8E(0xC, "CH30400")
    OP_8E(0xD, "CH30500")
    OP_8E(0xE, "CH30600")
    OP_8E(0xF, "CH30700")
    OP_8E(0x10, "CH30800")
    OP_8E(0x11, "CH30900")
    OP_8E(0x12, "CH31000")
    OP_8E(0x13, "CH31100")
    OP_8E(0x14, "CH31200")
    OP_8E(0x15, "CH31300")
    OP_8E(0x16, "CH31400")
    OP_8E(0x17, "CH31500")
    OP_8E(0x18, "CH31600")
    OP_8E(0x19, "CH31700")
    OP_8E(0x1A, "CH31800")
    OP_8E(0x1B, "CH31900")
    Jump("loc_1496")

    label("loc_13D8")

    LoadChrToIndex("chr/ch40040.itc", 0x0)
    LoadChrToIndex("chr/ch40041.itc", 0x1)
    LoadChrToIndex("chr/ch40042.itc", 0x2)
    LoadChrToIndex("chr/ch40043.itc", 0x3)
    LoadChrToIndex("chr/ch40044.itc", 0x4)
    LoadChrToIndex("chr/ch40045.itc", 0x5)
    LoadChrToIndex("chr/ch40046.itc", 0x6)
    LoadChrToIndex("chr/ch40047.itc", 0x7)
    LoadChrToIndex("chr/ch40048.itc", 0x8)
    LoadChrToIndex("chr/ch40049.itc", 0x9)
    OP_8E(0x8, "CH40040")
    OP_8E(0x9, "CH40041")
    OP_8E(0xA, "CH40042")
    OP_8E(0xB, "CH40043")
    OP_8E(0xC, "CH40044")
    OP_8E(0xD, "CH40045")
    OP_8E(0xE, "CH40046")
    OP_8E(0xF, "CH40047")
    OP_8E(0x10, "CH40048")
    OP_8E(0x11, "CH40049")
    Jump("loc_1496")

    label("loc_1487")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1496")

    label("loc_1496")

    OP_60(0x0)
    OP_57(0x0)
    OP_DB()
    LoadChrChipPat()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x11, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    ClearChrFlags(0x4, 0x8)
    ClearChrFlags(0x5, 0x8)
    ClearChrFlags(0x6, 0x8)
    ClearChrFlags(0x7, 0x8)
    OP_49()
    TalkEnd(0xFE)
    Return()

    # Function_2_372 end

    def Function_3_152E(): pass

    label("Function_3_152E")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1551")
    Sleep(100)
    Jump("loc_15ED")

    label("loc_1551")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1568")
    Sleep(200)
    Jump("loc_15ED")

    label("loc_1568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_157F")
    Sleep(300)
    Jump("loc_15ED")

    label("loc_157F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1596")
    Sleep(400)
    Jump("loc_15ED")

    label("loc_1596")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15AD")
    Sleep(500)
    Jump("loc_15ED")

    label("loc_15AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C4")
    Sleep(600)
    Jump("loc_15ED")

    label("loc_15C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DB")
    Sleep(700)
    Jump("loc_15ED")

    label("loc_15DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15ED")
    Sleep(800)

    label("loc_15ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1635")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_15ED")

    label("loc_1635")

    Return()

    # Function_3_152E end

    def Function_4_1636(): pass

    label("Function_4_1636")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_1636 end

    def Function_5_1642(): pass

    label("Function_5_1642")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#0000FLloyd\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0100FElie\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0200FTio\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0300FRandy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0400FWazy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0500FSergeant Major Seeker\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0600FDetective Dudley\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0700FYin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0800FEstelle\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0900FJoshua\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1642 end

    def Function_6_170B(): pass

    label("Function_6_170B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#1000FChief Sergei\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1100FKeA\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1200FZeit\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1300FCecile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1400FArios\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1500FShizuku\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1600FWald\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1700FIlya\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1800FRixia\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1900FReceptionist Fran\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2000FDeputy Commander Baelz\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2100FGrace\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2200FMr. Grimwood\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2300FJona\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2400FProfesser Guenter\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_170B end

    def Function_7_1845(): pass

    label("Function_7_1845")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#2500FMayor MacDowell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2600FSecretary Ernest\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2700FSpeaker Hartmann\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2800FMr. Crois\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2900FMariabell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3000FDon Marconi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3100FGarcia\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3200FCao\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3300FRenne\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3400FKilika\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3500FLechter\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3600FHarold\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3700FSophia\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3800FColin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3900FMeister Joerg\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_1845 end

    def Function_8_1985(): pass

    label("Function_8_1985")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "#5000FLloyd (formal)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5100FLloyd (formal, glasses)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5200FLloyd (loungewear)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5300FElie (formal)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5400FTio (formal)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5500FTio (loungewear)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5600FRandy (formal)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5700FWazy (formal)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5800FKeA (casual)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5900FCecile (casual)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6000FShizuku (street clothes)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6100FIlya (dancer)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6200FRixia (dancer)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6300FNoel (casual)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6400FFran (casual)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6500FMacDowell (loungewear)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6600FErnest (demon form)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6700FJoachim (high priest clothes)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6800FJoachim (high priest clothes, white hair)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_1985 end

    def Function_9_1BC2(): pass

    label("Function_9_1BC2")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")

    ChrTalk(
        0xFE,
        "#0000FLloyd\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0001F#1P＃1P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0002F#2P＃2P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0003F#3P＃3P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0004F#4P＃4P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0005F#5P＃5P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0006F#6P＃6P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0007F#7P＃7P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0008F#8P＃8P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#9P＃9P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#10P＃10P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#11P＃11P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#12P＃12P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#13P＃13P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#14P＃14P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#15P＃15P\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009F#16P＃16P\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_9_1BC2 end

    def Function_10_1DA1(): pass

    label("Function_10_1DA1")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E62")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Lloyd\x01",                      # 0
            "Elie\x01",                       # 1
            "Tio\x01",                        # 2
            "Randy\x01",                      # 3
            "Wazy\x01",                       # 4
            "Sergeant Major Seeker\x01",      # 5
            "Detective Dudley\x01",           # 6
            "Yin\x01",                        # 7
            "Estelle\x01",                    # 8
            "Joshua\x01",                     # 9
            "Cancel\x01",                     # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E6E"),
        (1, "loc_2024"),
        (2, "loc_21F2"),
        (3, "loc_23C2"),
        (4, "loc_2577"),
        (5, "loc_26F0"),
        (6, "loc_2878"),
        (7, "loc_29F2"),
        (8, "loc_2ADE"),
        (9, "loc_2CBB"),
        (SWITCH_DEFAULT, "loc_2E5D"),
    )


    label("loc_1E6E")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0003FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0004FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0006FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0007FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0008FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0009FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0010FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0011FConfused\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0012FStrained smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2024")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0106FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0107FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0108FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0109FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0110FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0111FGlare\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0112FShy, surprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0113FShy, eyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_21F2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0202FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0204FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0205FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0206FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0207FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0208FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0209FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0210FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0211FGlare\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0212FTeary joy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0213FTeary joy, eyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_23C2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0307FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0308FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0309FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0310FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0311FEnraged\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0312FEnraged, smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2577")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0402FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0404FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0405FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0406FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0407FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0409FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0410FPain\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_26F0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0502FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0503FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0504FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0506FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0507FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0508FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0509FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0510FPain\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2878")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0602FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0604FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0606FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0607FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0608FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0610FAnnoyed\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_29F2")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0702FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0707FYell\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2ADE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0801FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0802FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0803FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0804FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0806FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0807FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0808FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0809FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0810FCry, eyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0811FTeary joy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0812FTeary joy, eyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0813FAmazed\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2CBB")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#0900FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0901FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0902FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0903FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0904FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0905FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0906FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0907FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0908FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0909FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0910FEmotional\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#0911FTeary joy\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E5D")

    label("loc_2E5D")

    Jump("loc_1DAD")

    label("loc_2E62")

    EventEnd(0x1)
    Return()

    # Function_10_1DA1 end

    def Function_11_2E65(): pass

    label("Function_11_2E65")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4388")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Chief Sergei\x01",                # 0
            "KeA\x01",                         # 1
            "Zeit\x01",                        # 2
            "Cecile\x01",                      # 3
            "Arios\x01",                       # 4
            "Shizuku\x01",                     # 5
            "Wald\x01",                        # 6
            "Ilya\x01",                        # 7
            "Rixia\x01",                       # 8
            "Receptionist Fran\x01",           # 9
            "Deputy Commander Baelz\x01",      # 10
            "Grace\x01",                       # 11
            "Mr. Grimwood\x01",                # 12
            "Jona\x01",                        # 13
            "Professer Guenter\x01",           # 14
            "Cancel\x01",                      # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F8A"),
        (1, "loc_30E5"),
        (2, "loc_32CB"),
        (3, "loc_33D0"),
        (4, "loc_3538"),
        (5, "loc_3680"),
        (6, "loc_3792"),
        (7, "loc_38EB"),
        (8, "loc_3A44"),
        (9, "loc_3BAC"),
        (10, "loc_3D05"),
        (11, "loc_3E4D"),
        (12, "loc_3FA6"),
        (13, "loc_40C0"),
        (14, "loc_4259"),
        (SWITCH_DEFAULT, "loc_4383"),
    )


    label("loc_2F8A")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1003FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1006FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1007FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1009FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1010FPain\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_30E5")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1106FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1107FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1108FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1109FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1110FNeutral, mouth open\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1111FThoughtful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1112FAnxious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1113FSleep\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1114FNightmare\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_32CB")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1207FYell\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_33D0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1308FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1309FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3538")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1402FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1404FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1405FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1407FYell\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3680")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1502FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1508FSad\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3792")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1602FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1604FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1607FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1609FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_38EB")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1701FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1702FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1703FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1704FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1705FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1706FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1709FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3A44")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1801FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1802FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1803FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1804FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1806FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1808FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1809FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3BAC")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#1900FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1901FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1902FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1903FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1904FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1905FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1906FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#1909FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3D05")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2003FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2004FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2006FSigh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3E4D")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2106FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2109FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3FA6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2202FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2205FSurprise\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_40C0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2307FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2309FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2310FAnnoyed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2311FEyes closed, yell\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_4259")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2405FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2406FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2409FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_4383")

    Jump("loc_2E71")

    label("loc_4388")

    EventEnd(0x1)
    Return()

    # Function_11_2E65 end

    def Function_12_438B(): pass

    label("Function_12_438B")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4397")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5870")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Mayor MacDowell\x01",       # 0
            "Secretary Ernest\x01",      # 1
            "Speaker Hartmann\x01",      # 2
            "Mr. Crois\x01",             # 3
            "Mariabell\x01",             # 4
            "Don Marconi\x01",           # 5
            "Garcia\x01",                # 6
            "Cao\x01",                   # 7
            "Renne\x01",                 # 8
            "Kilika\x01",                # 9
            "Lechter\x01",               # 10
            "Harold\x01",                # 11
            "Sophia\x01",                # 12
            "Colin\x01",                 # 13
            "Meister Joerg\x01",         # 14
            "Cancel\x01",                # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_44B6"),
        (1, "loc_45E0"),
        (2, "loc_47B4"),
        (3, "loc_48CE"),
        (4, "loc_4A16"),
        (5, "loc_4B6F"),
        (6, "loc_4CB7"),
        (7, "loc_4E10"),
        (8, "loc_4F69"),
        (9, "loc_5150"),
        (10, "loc_5288"),
        (11, "loc_5407"),
        (12, "loc_5530"),
        (13, "loc_564F"),
        (14, "loc_5776"),
        (SWITCH_DEFAULT, "loc_586B"),
    )


    label("loc_44B6")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2503FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2507FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2509FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_45E0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2604FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2606FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2610FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2611FBad, neutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2612FBad, serious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2613FBad, eyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2614FBad, yell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2615FBad, eyes closed, yell\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_47B4")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2701FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2702FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2703FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2705FSurprise\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_48CE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2801FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2803FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2804FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2806FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2809FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_4A16")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#2900FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2901FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2902FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2903FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2904FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2905FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2906FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2909FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_4B6F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3003FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3004FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3007FYell\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_4CB7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3107FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3109FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_4E10")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3202FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3204FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3205FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3206FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3209FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_4F69")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3307FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3308FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3309FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3310FEyes closed, yell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3311FAmazed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3312FCry\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3313FCry, eyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3314FTeary joy\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_5150")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3402FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3404FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3405FSurprise\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_5288")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3502FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3503FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3504FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3506FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3507FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3509FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3510FThoughtful\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_5407")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3608FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3609FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_5530")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3701FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3707FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3708FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3709FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3710FGrief\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_564F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3802FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3809FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3810FDumbfounded\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3811FCry\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_5776")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#3900FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3901FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#3903FEyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_586B")

    label("loc_586B")

    Jump("loc_4397")

    label("loc_5870")

    EventEnd(0x1)
    Return()

    # Function_12_438B end

    def Function_13_5873(): pass

    label("Function_13_5873")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_587F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AAC")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Lloyd (formal)\x01",               # 0
            "Lloyd (formal, glasses)\x01",      # 1
            "Lloyd (loungewear)\x01",           # 2
            "Elie (formal)\x01",                # 3
            "Tio (formal)\x01",                 # 4
            "Tio (loungewear)\x01",             # 5
            "Randy (formal)\x01",               # 6
            "Wazy (formal)\x01",                # 7
            "KeA (casual)\x01",                 # 8
            "Cecile (casual)\x01",              # 9
            "Cancel\x01",                       # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_598C"),
        (1, "loc_5B42"),
        (2, "loc_5CF8"),
        (3, "loc_5EAE"),
        (4, "loc_607C"),
        (5, "loc_624C"),
        (6, "loc_641C"),
        (7, "loc_65D1"),
        (8, "loc_6759"),
        (9, "loc_693F"),
        (SWITCH_DEFAULT, "loc_6AA7"),
    )


    label("loc_598C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5003FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5004FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5006FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5007FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5008FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5009FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5010FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5011FConfused\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5012FStrained smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_5B42")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5106FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5107FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5108FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5109FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5110FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5111FConfused\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5112FStrained smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_5CF8")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5202FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5204FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5205FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5206FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5207FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5208FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5209FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5210FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5211FConfused\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5212FStrained smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_5EAE")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5307FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5308FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5309FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5310FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5311FGlare\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5312FShy, surprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5313FShy, eyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_607C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5402FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5404FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5405FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5406FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5407FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5408FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5409FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5410FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5411FGlare\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5412FTeary joy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5412FTeary joy, eyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_624C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5502FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5503FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5504FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5506FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5507FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5508FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5509FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5510FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5511FGlare\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5512FTeary joy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5512FTeary joy, eyes closed\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_641C")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5602FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5604FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5606FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5607FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5608FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5609FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5610FPain\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5611FEnraged\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5612FEnraged, smile\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_65D1")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5701FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5702FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5703FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5704FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5705FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5706FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5707FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5708FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5709FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5710FPain\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_6759")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5801FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5802FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5803FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5804FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5806FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5807FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5808FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5809FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5810FNeutral, mouth open\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5811FThoughtful\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5812FAnxious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5813FSleep\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5814FNightmare\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_693F")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05900.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#5900FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5901FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5902FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5903FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5904FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5905FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5906FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5908FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#5909FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AA7")

    label("loc_6AA7")

    Jump("loc_587F")

    label("loc_6AAC")

    EventEnd(0x1)
    Return()

    # Function_13_5873 end

    def Function_14_6AAF(): pass

    label("Function_14_6AAF")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7894")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Shizuku (street clothes)\x01",                       # 0
            "Ilya (dancer)\x01",                                  # 1
            "Rixia (dancer)\x01",                                 # 2
            "Noel (casual)\x01",                                  # 3
            "Fran (casual)\x01",                                  # 4
            "MacDowell (loungewear)\x01",                         # 5
            "Ernest (demon form)\x01",                            # 6
            "Joachim (high priest clothes)\x01",                  # 7
            "Joachim (high priest clothes, white hair)\x01",      # 8
            "Cancel\x01",                                         # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6BE7"),
        (1, "loc_6CF9"),
        (2, "loc_6E52"),
        (3, "loc_6FCF"),
        (4, "loc_7157"),
        (5, "loc_72B0"),
        (6, "loc_73DA"),
        (7, "loc_75B3"),
        (8, "loc_7721"),
        (SWITCH_DEFAULT, "loc_788F"),
    )


    label("loc_6BE7")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6000FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6001FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6002FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6005FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6008FSad\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_6CF9")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06100.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6100FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6101FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6102FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6103FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6104FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6105FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6106FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6109FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_6E52")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06200.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6200FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6201FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6202FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6203FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6204FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6205FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6206FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6208FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6209FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6210FSad laugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_6FCF")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06300.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6300FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6301FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6302FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6303FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6304FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6305FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6306FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6307FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6308FSad\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6309FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6310FPain\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_7157")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06400.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6400FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6401FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6402FSmile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6403FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6404FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6405FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6406FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6409FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_72B0")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06500.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6500FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6501FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6503FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6505FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6507FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6509FLaugh\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_73DA")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6600FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6601FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6603FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6604FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6605FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6606FSigh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6610FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6611FEvil, neutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6612FEvil, serious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6613FEvil, eyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6614FEvil, yell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6615FEvil, eyes closed, yell\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_75B3")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06700.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6700FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6701FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6703FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6704FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6705FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6707FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6709FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6710FShocked\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6711FAnnoyed\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_7721")

    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06800.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_57(0x3)
    SetChrName("Check Usage")

    AnonymousTalk(
        0xFF,
        "Bust position check\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0xFE,
        "#6800FNeutral\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6801FSerious\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6803FEyes closed\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6804FEyes closed, smile\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6805FSurprise\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6807FYell\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6809FLaugh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6810FShocked\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#6811FAnnoyed\x02",
    )

    CloseMessageWindow()
    Jump("loc_788F")

    label("loc_788F")

    Jump("loc_6ABB")

    label("loc_7894")

    EventEnd(0x1)
    Return()

    # Function_14_6AAF end

    SaveToFile()

Try(main)
