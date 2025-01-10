from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1120.bin",                # FileName
        "c1120",                    # MapName
        "c1120",                    # Location
        0x0017,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1120",                  # 0
        "KeA",                    # 1
        "Chief Sergei",           # 2
        "Detective Dudley",       # 3
        "Sergeant Major Seeker",  # 4
        "Deputy Commander Baelz", # 5
        "Grace",                  # 6
        "Mayor MacDowell",        # 7
        "Mariabell",              # 8
        "Mr. Crois",              # 9
        "Mr. Grimwood",           # 10
        "Wazy",                   # 11
        "Cecile",                 # 12
        "Speaker Hartmann",       # 13
        "Arios",                  # 14
        "Detective Emma",         # 15
        "Cameraman",              # 16
        "Opening Ceremony Guest", # 17
        "Opening Ceremony Guest", # 18
        "Opening Ceremony Guest", # 19
        "Opening Ceremony Guest", # 20
        "Opening Ceremony Guest", # 21
        "Opening Ceremony Guest", # 22
        "Opening Ceremony Guest", # 23
        "Opening Ceremony Guest", # 24
        "Opening Ceremony Guest", # 25
        "Opening Ceremony Guest", # 26
        "Opening Ceremony Guest", # 27
        "Receptionist Rebecca",   # 28
        "Receptionist Fran",      # 29
        "Inspector Donovan",      # 30
        "Detective Raymond",      # 31
        "Officer Franz",          # 32
        "Chief Jolich",           # 33
        "Officer Kate",           # 34
        "Helmer",                 # 35
        "Chairman Mors",          # 36
        "Vice Commissioner Pierre",# 37
        "Ilya",                   # 38
        "Rixia",                  # 39
        "Harold",                 # 40
        "Wendy",                  # 41
        "Miles",                  # 42
        "Leyte",                  # 43
        "Oscar",                  # 44
        "Jona",                   # 45
        "Chief Roberts",          # 46
        "Zeit",                   # 47
        "SE制御",                 # 48
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_678",          # 00, 0
        "Function_1_70D",          # 01, 1
        "Function_2_75A",          # 02, 2
        "Function_3_789",          # 03, 3
        "Function_4_842",          # 04, 4
        "Function_5_8FB",          # 05, 5
        "Function_6_1488",         # 06, 6
        "Function_7_14D2",         # 07, 7
        "Function_8_266A",         # 08, 8
        "Function_9_2884",         # 09, 9
        "Function_10_2893",        # 0A, 10
    ))


    def Function_0_678(): pass

    label("Function_0_678")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69B")
    Sleep(600)
    Jump("loc_6C4")

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B2")
    Sleep(400)
    Jump("loc_6C4")

    label("loc_6B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C4")
    Sleep(200)

    label("loc_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70C")
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
    Jump("loc_6C4")

    label("loc_70C")

    Return()

    # Function_0_678 end

    def Function_1_70D(): pass

    label("Function_1_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_721")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)
    Jump("loc_759")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_735")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_759")

    label("loc_735")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    Event(0, 10)

    label("loc_759")

    Return()

    # Function_1_70D end

    def Function_2_75A(): pass

    label("Function_2_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_776")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_788")

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_788")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_788")

    Return()

    # Function_2_75A end

    def Function_3_789(): pass

    label("Function_3_789")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_841")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B7")
    Sleep(500)
    Jump("loc_7FF")

    label("loc_7B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE")
    Sleep(200)
    Jump("loc_7FF")

    label("loc_7CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E5")
    Sleep(300)
    Jump("loc_7FF")

    label("loc_7E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7FC")
    Sleep(400)
    Jump("loc_7FF")

    label("loc_7FC")

    Sleep(600)

    label("loc_7FF")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 80, 0)
    Jump("Function_3_789")

    label("loc_841")

    Return()

    # Function_3_789 end

    def Function_4_842(): pass

    label("Function_4_842")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FA")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_870")
    Sleep(500)
    Jump("loc_8B8")

    label("loc_870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_887")
    Sleep(1000)
    Jump("loc_8B8")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_89E")
    Sleep(1500)
    Jump("loc_8B8")

    label("loc_89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B5")
    Sleep(2000)
    Jump("loc_8B8")

    label("loc_8B5")

    Sleep(2500)

    label("loc_8B8")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 80, 0)
    Jump("Function_4_842")

    label("loc_8FA")

    Return()

    # Function_4_842 end

    def Function_5_8FB(): pass

    label("Function_5_8FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch06500.itc", 0x1F)
    LoadChrToIndex("chr/ch05502.itc", 0x20)
    LoadChrToIndex("chr/ch05602.itc", 0x21)
    LoadChrToIndex("chr/ch05902.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("apl/ch50301.itc", 0x24)
    LoadChrToIndex("apl/ch50314.itc", 0x25)
    LoadChrToIndex("chr/ch07702.itc", 0x26)
    LoadChrToIndex("chr/ch27602.itc", 0x27)
    LoadChrToIndex("chr/ch27702.itc", 0x28)
    LoadChrToIndex("chr/ch27802.itc", 0x29)
    LoadChrToIndex("chr/ch27902.itc", 0x2A)
    LoadChrToIndex("chr/ch28102.itc", 0x2B)
    LoadChrToIndex("chr/ch28202.itc", 0x2C)
    SoundLoad(883)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -1460, 1100, 14620, 180)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 660, 750, 16490, 183)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -6600, 0, 9400, 55)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x17, -5600, 0, 9300, 55)
    OP_68(-800, 1500, 11800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26000, 0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KCrossbell Anniversary Festival, Opening Day\x02",
        )
    )

    Sleep(3000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(500)
    BeginChrThread(0x37, 0, 0, 6)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Dignified Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3100001VThis day marks Crossbell's 70th\x01",
            "anniversary as an autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3100002VThese 70 years haven't been without\x01",
            "struggle or times of turmoil.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x18, 0x27)
    SetChrChipByIndex(0x19, 0x28)
    SetChrChipByIndex(0x1A, 0x29)
    SetChrChipByIndex(0x1B, 0x2A)
    SetChrChipByIndex(0x1C, 0x2B)
    SetChrChipByIndex(0x1D, 0x2C)
    SetChrChipByIndex(0x1E, 0x27)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrChipByIndex(0x21, 0x2B)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrSubChip(0x21, 0x0)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -5800, 50, 7500, 0)
    SetChrPos(0xF, -4000, 50, 7500, 0)
    SetChrPos(0x10, -2300, 100, 7500, 0)
    SetChrPos(0x18, -500, 100, 7500, 0)
    SetChrPos(0x19, 1300, 50, 7500, 0)
    SetChrPos(0x11, 2900, 100, 7500, 0)
    SetChrPos(0x1A, -5800, 100, 5000, 0)
    SetChrPos(0x1B, -4000, 50, 5000, 0)
    SetChrPos(0x1C, -2300, 50, 5000, 0)
    SetChrPos(0x1D, -500, 50, 5000, 0)
    SetChrPos(0x1E, 1300, 100, 5000, 0)
    SetChrPos(0x1F, 2900, 100, 5000, 0)
    SetChrPos(0x20, -5800, 50, 2500, 0)
    SetChrPos(0x21, -4000, 50, 2500, 0)
    SetChrPos(0x22, -2400, 100, 2500, 0)
    OP_68(-1450, 2250, 14880, 0)
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    OP_6E(460, 3000)
    BeginChrThread(0x17, 0, 0, 4)
    FadeToBright(2000, 0)
    Sleep(3000)
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#3100003V#2503F#5PWars have raged, the Orbal Revolution began...\x02\x03",
            "#3100004V#2500FWhile Crossbell has had its hardships in the\x01",
            "name of progress, we now stand as the leader\x01",
            "of trade in Zemuria.\x02\x03",
            "#3100005VOur economy is thriving. We have the luxury of\x01",
            "peace in no short order due to the Non-Aggression\x01",
            "Pact signed in Liberl two years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-2400, 2500, 9100, 0)
    MoveCamera(59, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15500, 0)
    OP_68(-2400, 860, 9100, 6000)
    MoveCamera(59, 19, 0, 6000)
    OP_6E(580, 6000)
    SetCameraDistance(15500, 6000)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#3100006V#2503F#NHowever, the problems that arise from rapid\x01",
            "growth and development require us to adopt\x01",
            "new policies and legislation.\x02\x03",
            "#3100007V#2501FFor the prosperity of both Crossbell and our\x01",
            "neighboring countries...\x02\x03",
            "#3100008V...we must all tackle our ever-present issues\x01",
            "as one, moving towards the beautiful future!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-1550, 2080, 11590, 0)
    MoveCamera(31, 12, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    OP_68(-1550, 2080, 11590, 10000)
    MoveCamera(31, 15, 0, 10000)
    OP_6E(420, 10000)
    SetCameraDistance(23000, 10000)
    SetChrPos(0x20, -500, 0, 2400, 0)
    SetChrPos(0x21, 1300, 0, 2400, 0)
    SetChrPos(0x22, 2900, 0, 2400, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#3100009V#2509FHaving reached an incredible milestone like\x01",
            "our 70th anniversary, we have decided to\x01",
            "share our joy and commemorate this occasion.\x02\x03",
            "#3100010VThough only five days, this year is speculated\x01",
            "to be the busiest Anniversary Festival Crossbell\x01",
            "has ever experienced.\x02\x03",
            "#3100011VArc en Ciel is putting on a new production,\x01",
            "but do not let that distract you from all\x01",
            "the festivities and events planned!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    PlayBGM("ed7104", 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x17, 0, 0, 3)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#3100012V#2503FUnder the name of our great Goddess Aidios...\x02\x03",
            "#3100013V#2507F...at this time, I hereby declare the beginning of\x01",
            "Crossbell State's 70th Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    Sound(884, 0, 100, 0)
    Sleep(1000)
    OP_24(0x373)
    EndChrThread(0x37, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x17, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(2000)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x373)
    SetScenarioFlags(0x5C, 0)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_8FB end

    def Function_6_1488(): pass

    label("Function_6_1488")

    Sound(883, 2, 0, 0)
    OP_25(0x373, 0xA)
    Sleep(200)
    OP_25(0x373, 0x14)
    Sleep(200)
    OP_25(0x373, 0x1E)
    Sleep(200)
    OP_25(0x373, 0x28)
    Sleep(200)
    OP_25(0x373, 0x32)
    Sleep(200)
    OP_25(0x373, 0x3C)
    Sleep(200)
    OP_25(0x373, 0x46)
    Sleep(200)
    OP_25(0x373, 0x50)
    Sleep(200)
    OP_25(0x373, 0x5A)
    Sleep(200)
    OP_25(0x373, 0x64)
    Return()

    # Function_6_1488 end

    def Function_7_14D2(): pass

    label("Function_7_14D2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch05600.itc", 0x21)
    LoadChrToIndex("chr/ch05900.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("chr/ch02500.itc", 0x24)
    LoadChrToIndex("chr/ch00800.itc", 0x25)
    LoadChrToIndex("chr/ch05700.itc", 0x26)
    LoadChrToIndex("chr/ch00400.itc", 0x27)
    LoadChrToIndex("chr/ch07500.itc", 0x28)
    LoadChrToIndex("apl/ch50314.itc", 0x29)
    LoadChrToIndex("chr/ch00900.itc", 0x2A)
    LoadChrToIndex("chr/ch06900.itc", 0x2B)
    LoadChrToIndex("chr/ch30200.itc", 0x2C)
    LoadChrToIndex("chr/ch30300.itc", 0x2D)
    LoadChrToIndex("chr/ch30400.itc", 0x2E)
    LoadChrToIndex("chr/ch30500.itc", 0x2F)
    LoadChrToIndex("chr/ch30000.itc", 0x30)
    LoadChrToIndex("chr/ch30100.itc", 0x31)
    LoadChrToIndex("chr/ch25800.itc", 0x32)
    LoadChrToIndex("chr/ch30600.itc", 0x33)
    LoadChrToIndex("chr/ch29300.itc", 0x34)
    LoadChrToIndex("chr/ch20200.itc", 0x35)
    LoadChrToIndex("chr/ch10300.itc", 0x36)
    LoadChrToIndex("apl/ch50560.itc", 0x37)
    LoadChrToIndex("apl/ch50562.itc", 0x38)
    LoadChrToIndex("chr/ch07000.itc", 0x39)
    LoadChrToIndex("chr/ch26100.itc", 0x3A)
    LoadChrToIndex("chr/ch06100.itc", 0x3B)
    LoadChrToIndex("chr/ch20800.itc", 0x3C)
    LoadChrToIndex("chr/ch05100.itc", 0x3D)
    LoadChrToIndex("chr/ch05200.itc", 0x3E)
    LoadChrToIndex("apl/ch50518.itc", 0x3F)
    LoadChrToIndex("chr/ch09300.itc", 0x40)
    LoadChrToIndex("chr/ch06400.itc", 0x41)
    LoadEffect(0x0, "event\\eva02_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis106.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis107.itp")
    SetChrPos(0x101, -1500, 0, -3000, 0)
    SetChrPos(0x102, -1500, 0, -4300, 0)
    SetChrPos(0x103, -1500, 0, -5600, 0)
    SetChrPos(0x104, -1500, 0, -6900, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1500, 750, 13700, 180)
    SetChrChipByIndex(0x2A, 0x32)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -2500, 750, 15100, 180)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -6200, 0, 9400, 90)

    def lambda_1720():

        label("loc_1720")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_1720")

    QueueWorkItem2(0xD, 2, lambda_1720)
    SetChrChipByIndex(0x17, 0x29)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5200, 0, 9400, 90)

    def lambda_175A():

        label("loc_175A")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_175A")

    QueueWorkItem2(0x17, 2, lambda_175A)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 0, 7000, 0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, 1100, 0, 7000, 0)
    SetChrChipByIndex(0x2B, 0x3C)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 2200, 0, 7000, 0)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -3000, 0, 7000, 0)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -4100, 0, 7000, 0)
    SetChrChipByIndex(0x2C, 0x41)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -5200, 0, 7000, 0)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 5700, 0)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 1100, 0, 5700, 0)
    SetChrChipByIndex(0x2D, 0x3D)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 2200, 0, 5700, 0)
    SetChrChipByIndex(0x25, 0x2D)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrPos(0x25, -3000, 0, 5700, 0)
    SetChrChipByIndex(0x26, 0x2C)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x26, -4100, 0, 5700, 0)
    SetChrChipByIndex(0x16, 0x2F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -5200, 0, 5700, 0)
    SetChrChipByIndex(0x24, 0x2B)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, 0, 0, 4400, 0)
    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrPos(0x23, 1100, 0, 4400, 0)
    SetChrChipByIndex(0x2E, 0x3E)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 2200, 0, 4400, 0)
    SetChrChipByIndex(0x28, 0x31)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrPos(0x28, -3000, 0, 4400, 0)
    SetChrChipByIndex(0x29, 0x33)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x29, -4100, 0, 4400, 0)
    SetChrChipByIndex(0x27, 0x30)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrPos(0x27, -5200, 0, 4400, 0)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 0, 0, 3100, 0)
    SetChrChipByIndex(0x2F, 0x40)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    ClearChrBattleFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 1100, 0, 3100, 0)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 2200, 0, 3100, 0)
    SetChrChipByIndex(0x32, 0x36)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    ClearChrBattleFlags(0x32, 0x8000)
    SetChrPos(0x32, -3000, 0, 3100, 0)
    SetChrChipByIndex(0x31, 0x35)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    ClearChrBattleFlags(0x31, 0x8000)
    SetChrPos(0x31, -4100, 0, 3100, 0)
    SetChrChipByIndex(0x30, 0x3A)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrBattleFlags(0x30, 0x8000)
    SetChrPos(0x30, -5200, 0, 3100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 1800, 0)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 1100, 0, 1800, 0)
    SetChrChipByIndex(0x36, 0x3F)
    SetChrSubChip(0x36, 0x1)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    SetChrPos(0x36, 2200, 0, 1800, 270)
    SetChrChipByIndex(0x35, 0x34)
    SetChrSubChip(0x35, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrBattleFlags(0x35, 0x8000)
    SetChrPos(0x35, -3000, 0, 1800, 0)
    SetChrChipByIndex(0x34, 0x3B)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    ClearChrBattleFlags(0x34, 0x8000)
    SetChrPos(0x34, -4100, 0, 1800, 0)
    SetChrChipByIndex(0x33, 0x39)
    SetChrSubChip(0x33, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)
    SetChrPos(0x33, -5200, 0, 1800, 0)
    SetMapObjFrame(0xFF, "model05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model06", 0x0, 0x1)
    Sleep(1000)
    PlayBGM("ed7528", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x210), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            "#5301101V",
            scpstr(0x18),
            "#30WIn the wake of the D∴G cult incident, Crossbell\x01",
            "was left in disarray.\x02\x03",
            "#5301102VThe mafia and guardsmen being controlled\x01",
            "through an illegal drug...\x02\x03",
            "#5301103V...as well as the misconduct of many officials,\x01",
            "including Speaker Hartmann...\x02\x03",
            "#5301104VAll of it was made public by the Crossbell Times.\x01",
            "It was said to be the largest scandal in Crossbell's\x01",
            "history.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFAAAAAA, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    AnonymousTalk(
        0xFF,
        (
            "#5301105V",
            scpstr(0x18),
            "#30WMayor MacDowell responded by dismissing the\x01",
            "police commissioner and the Guardian Force\x01",
            "commander.\x02\x03",
            "#5301106VFollowing that, he demanded a full investigation\x01",
            "be conducted by Deputy Commander Baelz and\x01",
            "the chiefs of the CPD.\x02\x03",
            "#5301107VDetective Dudley, no longer held back by corruption,\x01",
            "was able to bring to light not only a connection between\x01",
            "the cult and members of the Imperial Faction, but also\x01",
            "one involving the Republican Faction.\x02\x03",
            "#5301108VArrests began to skyrocket. The citizens' unrest\x01",
            "and distrust towards Crossbell politics had reached\x01",
            "a boiling point.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFAAAAAA, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)

    AnonymousTalk(
        0xFF,
        (
            "#5301109V",
            scpstr(0x18),
            "#30WDuring this time, IBC CEO Dieter Crois took the\x01",
            "opportunity to declare his candidacy for mayor.\x02\x03",
            "#5301110VHe publicly pledged to heal the political system\x01",
            "and follow the ideals of Mayor MacDowell, who\x01",
            "had chosen not to seek reelection.\x02\x03",
            "#5301111VBefore leaving office, the mayor also announced\x01",
            "that special elections for the seats of the arrested\x01",
            "diet members would be held, as well.\x02\x03",
            "#5301112VCandidates from all backgrounds are expected\x01",
            "to vie for the spot of Speaker of the Diet.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xFF,
        (
            "#5301113V",
            scpstr(0x18),
            "#30WAnd, one month after the incident...\x02\x03",
            "#5301114VMayor MacDowell summoned us to\x01",
            "the City Hall's reception hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-1500, 1300, 3000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12500, 0)

    def lambda_22BB():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_22BB)

    def lambda_22C8():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_22C8)

    def lambda_22D5():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_22D5)

    def lambda_22E2():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22E2)

    def lambda_22EF():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_22EF)

    def lambda_22FC():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_22FC)

    def lambda_2309():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2309)

    def lambda_2316():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2316)

    def lambda_2323():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_2323)

    def lambda_2330():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_2330)

    def lambda_233D():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_233D)

    def lambda_234A():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_234A)

    def lambda_2357():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2357)

    def lambda_2364():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_2364)

    def lambda_2371():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_2371)

    def lambda_237E():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_237E)

    def lambda_238B():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_238B)

    def lambda_2398():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_2398)

    def lambda_23A5():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_23A5)

    def lambda_23B2():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_23B2)

    def lambda_23BF():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_23BF)

    def lambda_23CC():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_23CC)

    def lambda_23D9():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_23D9)

    def lambda_23E6():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_23E6)

    def lambda_23F3():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_23F3)

    def lambda_2400():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2400)
    BeginChrThread(0x36, 0, 0, 9)

    def lambda_2413():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_2413)

    def lambda_2420():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_2420)

    def lambda_242D():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_242D)
    BeginChrThread(0x8, 3, 0, 8)

    def lambda_2440():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2440)
    Sleep(50)

    def lambda_245D():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_245D)
    Sleep(50)

    def lambda_247A():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_247A)
    Sleep(50)

    def lambda_2497():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2497)
    BeginChrThread(0x17, 0, 0, 4)
    SetCameraDistance(11000, 3000)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_6F(0x10)
    Fade(1000)
    OP_68(-1500, 1000, 3000, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(-1500, 1000, 7000, 6000)
    SetCameraDistance(19500, 6000)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(-1500, 1450, 13100, 0)
    MoveCamera(47, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -2000, 750, 11700, 0)
    SetChrPos(0x102, -1000, 750, 11700, 0)
    SetChrPos(0x103, -3000, 750, 11700, 0)
    SetChrPos(0x104, 0, 750, 11700, 0)
    MoveCamera(42, 25, 0, 5000)
    SetCameraDistance(19000, 5000)
    OP_0D()
    Sleep(500)

    def lambda_25C8():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x3138, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25C8)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x38)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xE, 0x1)
    SetChrSubChip(0x101, 0x1)
    OP_0D()
    EndChrThread(0x17, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x104, 0x40)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x210), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t3510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_14D2 end

    def Function_8_266A(): pass

    label("Function_8_266A")

    Sleep(1000)

    def lambda_2672():

        label("loc_2672")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2672")

    QueueWorkItem2(0x8, 2, lambda_2672)

    def lambda_2684():

        label("loc_2684")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2684")

    QueueWorkItem2(0x13, 2, lambda_2684)

    def lambda_2696():

        label("loc_2696")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2696")

    QueueWorkItem2(0x35, 2, lambda_2696)

    def lambda_26A8():

        label("loc_26A8")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_26A8")

    QueueWorkItem2(0x34, 2, lambda_26A8)

    def lambda_26BA():

        label("loc_26BA")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_26BA")

    QueueWorkItem2(0x33, 2, lambda_26BA)
    Sleep(50)

    def lambda_26CF():

        label("loc_26CF")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_26CF")

    QueueWorkItem2(0x11, 2, lambda_26CF)

    def lambda_26E1():

        label("loc_26E1")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_26E1")

    QueueWorkItem2(0x2F, 2, lambda_26E1)

    def lambda_26F3():

        label("loc_26F3")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_26F3")

    QueueWorkItem2(0x12, 2, lambda_26F3)

    def lambda_2705():

        label("loc_2705")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2705")

    QueueWorkItem2(0x32, 2, lambda_2705)

    def lambda_2717():

        label("loc_2717")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2717")

    QueueWorkItem2(0x31, 2, lambda_2717)

    def lambda_2729():

        label("loc_2729")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2729")

    QueueWorkItem2(0x30, 2, lambda_2729)
    Sleep(50)

    def lambda_273E():

        label("loc_273E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_273E")

    QueueWorkItem2(0x24, 2, lambda_273E)

    def lambda_2750():

        label("loc_2750")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2750")

    QueueWorkItem2(0x23, 2, lambda_2750)

    def lambda_2762():

        label("loc_2762")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2762")

    QueueWorkItem2(0x2E, 2, lambda_2762)

    def lambda_2774():

        label("loc_2774")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2774")

    QueueWorkItem2(0x28, 2, lambda_2774)

    def lambda_2786():

        label("loc_2786")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2786")

    QueueWorkItem2(0x29, 2, lambda_2786)

    def lambda_2798():

        label("loc_2798")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2798")

    QueueWorkItem2(0x27, 2, lambda_2798)
    Sleep(50)

    def lambda_27AD():

        label("loc_27AD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_27AD")

    QueueWorkItem2(0xC, 2, lambda_27AD)

    def lambda_27BF():

        label("loc_27BF")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_27BF")

    QueueWorkItem2(0xB, 2, lambda_27BF)

    def lambda_27D1():

        label("loc_27D1")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_27D1")

    QueueWorkItem2(0x2D, 2, lambda_27D1)

    def lambda_27E3():

        label("loc_27E3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_27E3")

    QueueWorkItem2(0x25, 2, lambda_27E3)

    def lambda_27F5():

        label("loc_27F5")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_27F5")

    QueueWorkItem2(0x26, 2, lambda_27F5)

    def lambda_2807():

        label("loc_2807")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2807")

    QueueWorkItem2(0x16, 2, lambda_2807)
    Sleep(50)

    def lambda_281C():

        label("loc_281C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_281C")

    QueueWorkItem2(0x10, 2, lambda_281C)

    def lambda_282E():

        label("loc_282E")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_282E")

    QueueWorkItem2(0xF, 2, lambda_282E)

    def lambda_2840():

        label("loc_2840")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2840")

    QueueWorkItem2(0x2B, 2, lambda_2840)

    def lambda_2852():

        label("loc_2852")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2852")

    QueueWorkItem2(0x9, 2, lambda_2852)

    def lambda_2864():

        label("loc_2864")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2864")

    QueueWorkItem2(0xA, 2, lambda_2864)

    def lambda_2876():

        label("loc_2876")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2876")

    QueueWorkItem2(0x2C, 2, lambda_2876)
    Return()

    # Function_8_266A end

    def Function_9_2884(): pass

    label("Function_9_2884")

    Sleep(4000)
    SetChrSubChip(0x36, 0x0)
    Sleep(3000)
    SetChrSubChip(0x36, 0x2)
    Return()

    # Function_9_2884 end

    def Function_10_2893(): pass

    label("Function_10_2893")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30500.itc", 0x20)
    OP_68(-1290, 2250, 12000, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 5370, 4120, -7740, 325)
    SetChrPos(0x102, 4680, 4120, -6920, 325)
    SetChrPos(0x103, 6270, 4000, -6900, 325)
    SetChrPos(0x104, 7000, 4000, -7490, 325)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x15, -8150, 0, 7500, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -8150, 0, 5500, 0)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -8650, 0, 4500, 0)
    OP_68(-1290, 2250, 6000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(3380, 5620, -6500, 0)
    MoveCamera(10, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#0000FWhat is this place, Elie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FIt's the reception hall. They use it for\x01",
            "all kinds of diplomatic meetings.\x02\x03",
            "It would appear it's being used for some sort of\x01",
            "symposium sponsored by Grandfather today.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#0105FWhat is...?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x16, 0x8000)
    Fade(500)
    OP_68(-8150, 1500, 5000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(15490, 0)
    OP_68(-8150, 1500, 6000, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x15,
        (
            "#1400FI understand the plan.\x02\x03",
            "I'll proceed with guarding the area, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0600FHmph, understood.\x02\x03",
            "#0603FThe First Division is normally more than\x01",
            "sufficient for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#1404FHaha. I hope you don't hold this against me.\x02\x03",
            "#1400FI can't blame them for asking me. There are\x01",
            "a number of foreign dignitaries in attendance.\x02\x03",
            "I'm sure the guild's help was requested to provide\x01",
            "extra reassurance for their safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#0603FSpare me the explanation. I'm already aware of\x01",
            "the circumstances.\x02\x03",
            "#0600FSee to it that you won't cause any blunders,\x01",
            "Sir Divine Blade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#1404FI'll do my job well.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(5370, 5620, -7740, 0)
    MoveCamera(17, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x16, 0x8000)

    ChrTalk(
        0x104,
        (
            "#0306F(Haha. Watchin' them bicker back and forth might\x01",
            "be more entertainin' than an Arc en Ciel show!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005F(They really do make an oddly\x01",
            "entertaining duo, don't they?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200F(The two of them appear to be working\x01",
            "together to guard the symposium.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101F(We probably shouldn't get in their\x01",
            "way. Let's leave them to their work.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xAD, 7)
    NewScene("c1110", 102, 0, 0)
    IdleLoop()
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_10_2893 end

    SaveToFile()

Try(main)
