from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0013.bin",                # FileName
        "m0013",                    # MapName
        "m0013",                    # Location
        0x0067,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 103, 0, 3, 0, 4],
    )

    BuildStringList((
        "m0013",                  # 0
        "Boss",                   # 1
        "Jona's Voice",           # 2
        "Jona's Voice",           # 3
        "bm0012",                 # 4
        "bm0012",                 # 5
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 0, 0, 180)
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
    MonsterBattlePostion("MonsterBattlePostion_E4", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 6, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 8, 14, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_104", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7401", "ed7403", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_148", 0x0012, 22, 6, 0, 0, 1, 0, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77600.dat", 0, 0, 0, 0, 0, "ms67001.dat", 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_C4", "ed7402", "ed7403", "ATBonus_94"),
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x18500B4,    "BattleInfo_104", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 6,   0.0,                   -7.5,                  -1.0,                  56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.5,                   0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 5,   0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])
    DeclEvent(0x0000, 0, 15,  0.0,                   9.5,                   -1.0,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.75,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 16,  0.0,                   -10.5,                 -1.5,                  64.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.25,                  0.30000001192092896,   1.0])

    DeclActor(102770,  200,     -60,     1200,    102770,  1700,    -60,     0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_44C",          # 00, 0
        "Function_1_468",          # 01, 1
        "Function_2_487",          # 02, 2
        "Function_3_4A6",          # 03, 3
        "Function_4_4D0",          # 04, 4
        "Function_5_5E6",          # 05, 5
        "Function_6_839",          # 06, 6
        "Function_7_D96",          # 07, 7
        "Function_8_E45",          # 08, 8
        "Function_9_12E5",         # 09, 9
        "Function_10_6911",        # 0A, 10
        "Function_11_693E",        # 0B, 11
        "Function_12_6969",        # 0C, 12
        "Function_13_69C8",        # 0D, 13
        "Function_14_6A27",        # 0E, 14
        "Function_15_6AD1",        # 0F, 15
        "Function_16_6BF9",        # 10, 16
        "Function_17_6D39",        # 11, 17
    ))


    def Function_0_44C(): pass

    label("Function_0_44C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_467")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_44C")

    label("loc_467")

    Return()

    # Function_0_44C end

    def Function_1_468(): pass

    label("Function_1_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_486")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_468")

    label("loc_486")

    Return()

    # Function_1_468 end

    def Function_2_487(): pass

    label("Function_2_487")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_487")

    label("loc_4A5")

    Return()

    # Function_2_487 end

    def Function_3_4A6(): pass

    label("Function_3_4A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C0")
    Event(0, 9)

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4CF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 8)

    label("loc_4CF")

    Return()

    # Function_3_4A6 end

    def Function_4_4D0(): pass

    label("Function_4_4D0")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50A")
    SetChrFlags(0xB, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_51E")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51E")
    ClearChrFlags(0xB, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_51E")

    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xB, 0x100)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF")
    SetMapFlags(0x2000)
    SetMapFlags(0x8000000)
    OP_E0(0x2)
    Jump("loc_5B9")

    label("loc_5AF")

    ClearMapFlags(0x2000)
    ClearMapFlags(0x8000000)

    label("loc_5B9")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_5CD")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E5")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_5E5")

    Return()

    # Function_4_4D0 end

    def Function_5_5E6(): pass

    label("Function_5_5E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 0)), scpexpr(EXPR_END)), "loc_5F0")
    Return()

    label("loc_5F0")

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
        (1, "loc_6D3"),
        (SWITCH_DEFAULT, "loc_6EA"),
    )


    label("loc_6D3")

    Sleep(500)
    OP_90(0x0, 200, 0, -8530, 0)
    EventEnd(0x5)
    Return()

    label("loc_6EA")

    Battle("BattleInfo_104", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(200, 1000, -8530, 0)
    OP_90(0x0, 200, 0, -8530, 0)
    OP_90(0x1, 200, 0, -8530, 0)
    OP_90(0x2, 200, 0, -8530, 0)
    OP_90(0x3, 200, 0, -8530, 0)
    OP_90(0x4, 200, 0, -8530, 0)
    OP_90(0x5, 200, 0, -8530, 0)
    OP_90(0x6, 200, 0, -8530, 0)
    OP_90(0x7, 200, 0, -8530, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_7AC"),
        (1, "loc_7AF"),
        (SWITCH_DEFAULT, "loc_7B2"),
    )


    label("loc_7AC")

    EventEnd(0x5)
    Return()

    label("loc_7AF")

    OP_B7(0x0)
    Return()

    label("loc_7B2")

    EventBegin(0x1)
    SetChrFlags(0xB, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Exterminated monster in Geofront A Sector!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x79, 0)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_5_5E6 end

    def Function_6_839(): pass

    label("Function_6_839")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    LoadEffect(0x0, "event\\eva04_00.eff")
    OP_68(0, 700, -1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -700, 0, -7300, 0)
    SetChrPos(0x103, 700, 0, -7000, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 6000, 0, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x8, 0xFF)

    def lambda_95E():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_95E)
    Sleep(50)

    def lambda_97B():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFF704, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97B)
    SetCameraDistance(20000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#3300302V#12P#0000FAre we close?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300303V#0204F#12PYes. This is the final stretch.\x02\x03",
            "#3300304V#0202FThe room containing Control Terminal\x01",
            "3 should be somewhere near he--\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A65():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A65)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#3300305V#12P#4S#0007FTio!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x7D0)
    Fade(250)
    OP_68(0, 1700, -1000, 0)
    MoveCamera(50, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13500, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x1)

    def lambda_B2C():
        OP_9D(0xFE, 0x12C, 0x0, 0xFFFFFDA8, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2C)
    Sound(814, 0, 100, 0)
    Sound(1011, 255, 100, 0)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    BeginChrThread(0x8, 3, 0, 7)
    OP_68(0, 1500, -3000, 500)
    MoveCamera(40, 13, 0, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x2)

    def lambda_B96():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFEE08, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B96)
    Sound(854, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x2)

    def lambda_BC1():
        OP_9D(0xFE, 0x2BC, 0x0, 0xFFFFEC78, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BC1)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    Sleep(500)

    ChrTalk(
        0x103,
        "#3300306V#0207F#12PMy sensors did not pick it up...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300307V#0013F#6PDamn it. It must be in charge of this part\x01",
            "of the Geofront!\x02\x03",
            "#3300308V#0007FTio, can you move?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300309V#0205F#12PAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 900, 0, -5000, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#3300310V#0201F#12PYes... I am fine!\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_D45():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D45)
    Sleep(50)

    def lambda_D5D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D5D)
    Sleep(500)
    Battle("BattleInfo_148", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    Call(0, 8)
    Return()

    # Function_6_839 end

    def Function_7_D96(): pass

    label("Function_7_D96")

    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_DA3():
        OP_9D(0xFE, 0x0, 0x0, 0x0, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DA3)
    Sound(812, 0, 100, 0)
    WaitChrThread(0x8, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_4C(0x8, 0xFF)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x3E8)
    Sound(813, 0, 100, 0)
    Sleep(1000)
    CancelBlur(0)
    Return()

    # Function_7_D96 end

    def Function_8_E45(): pass

    label("Function_8_E45")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("monster/ch77650.itc", 0x22)
    LoadChrToIndex("chr/ch00056.itc", 0x23)
    LoadChrToIndex("chr/ch00256.itc", 0x24)
    OP_68(0, 1000, -4000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, -800, 0, -4000, 0)
    SetChrPos(0x103, 700, 0, -4200, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x101,
        "#3300311V#12P#0006FThat was unexpected.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3300312V#6P#0001FTio, are you okay? I know I had\x01",
            "to pull you back like that, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3300313V#0204F#11PI told you, I am fine.\x02\x03",
            "#3300314V#0202FWhat about you, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300315V#6P#0004FI'm all right. I guess Randy meant it\x01",
            "when he said these tonfas would be\x01",
            "really good for defense.\x02\x03",
            "#3300316V#0001FRegardless, that would have gone a\x01",
            "lot smoother if those two were here.\x02\x03",
            "#3300317V#0006FHonestly, being without them is making\x01",
            "me realize how much I rely on those two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300318V#0202F#11PHeehee...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300319V#6P#0011FD-Did I say something funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300320V#0204F#11PNo, not particularly. You just\x01",
            "reminded me of someone.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3300321V#0202F#5PControl Terminal 3 should be\x01",
            "past the door on the right.\x02\x03",
            "#3300322VWe should log in and contact Jona.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300323V#6P#0000FGot'cha. I've got your back.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_37()
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 0, 0, -4000, 0)
    SetScenarioFlags(0xA1, 2)
    OP_E0(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_E45 end

    def Function_9_12E5(): pass

    label("Function_9_12E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00202.itc", 0x1E)
    LoadChrToIndex("apl/ch50092.itc", 0x1F)
    LoadChrToIndex("apl/ch50011.itc", 0x20)
    LoadChrToIndex("apl/ch50324.itc", 0x21)
    LoadChrToIndex("apl/ch50326.itc", 0x22)
    LoadChrToIndex("apl/ch50218.itc", 0x23)
    LoadEffect(0x0, "event\\eva06_00.eff")
    SoundLoad(806)
    SoundLoad(840)
    SoundLoad(905)
    OP_68(101500, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 92000, 150, -300, 90)
    SetChrPos(0x103, 92000, 150, 300, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x13)
    SetChrFlags(0x9, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis041.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis042.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis020.itp")
    OP_68(97500, 1000, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    def lambda_1479():
        OP_96(0xFE, 0x1750C, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1479)

    def lambda_1493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1493)
    Sleep(400)

    def lambda_14A7():
        OP_96(0xFE, 0x1750C, 0x0, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14A7)

    def lambda_14C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14C1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3300324V#0005F#6PIs this it, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300325V#0202FYes. This is Control Terminal 3.\x02\x03",
            "#3300326VOur plan is to hack into the net from two\x01",
            "points: Control Terminal 8, which Jona has\x01",
            "appropriated, and this terminal.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3300327V#12P#0004FI think I understand.\x02\x03",
            "#3300328V#0000FShould I call Jona now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#3300329V#0203FYes, if you would.\x02\x03",
            "#3300330V#0200FElie and the others may have tried\x01",
            "to contact us, so please check my\x01",
            "Enigma for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300331V#12P#0000FWill do.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took Tio's Enigma.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_68(103000, 1000, 0, 3000)
    MoveCamera(55, 15, 0, 3000)
    SetCameraDistance(21000, 3000)
    OP_93(0x103, 0x5A, 0x1F4)

    def lambda_172F():
        OP_95(0xFE, 102000, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_172F)
    Sleep(200)
    OP_93(0x101, 0x5A, 0x1F4)

    def lambda_1753():
        OP_95(0xFE, 101200, 0, -1700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1753)
    WaitChrThread(0x103, 1)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 102300, 250, 0, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "open")
    Sound(72, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x1F4)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(902, 0, 100, 0)
    Sleep(2800)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3300332V#0000FJona? It's Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300333V\x07\x05",
            "Oh, you're already there?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#3300334V#0000FYeah. Tio is booting up\x01",
            "the terminal now.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300335V\x07\x05",
            "Good, goooood. I'll get mine\x01",
            "set up, too.\x02\x03",
            "#3300336VDo me a favor and turn the Enigma's\x01",
            "speaker mode on, okay?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3300337V#0005FSpeaker mode...? That's a thing?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x103, 0x2)
    Sleep(300)
    SetMessageWindowPos(120, 30, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#3300338V#0200FOn the back of the Enigma, there's\x01",
            "a little red switch. Flip it.\x02\x03",
            "#3300339VThat'll make the caller's voice\x01",
            "go through a mini-speaker.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#3300340V#0000FRight here?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd flipped the switch as instructed\x01",
            "and placed the Enigma on the table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    SetChrPos(0xA, 102600, -500, -1500, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sound(31, 0, 100, 0)
    Sound(42, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0xA,
        (
            "#3300341V\x07\x05",
            "#2PHey. Can you two hear me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300342V#6P#0000FWell, that's nifty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300343V#0203F#5PIt uses quite a bit more EP,\x01",
            "so I don't recommend using\x01",
            "it unless necessary.\x02\x03",
            "#3300344V#0200FJona. Everything is green\x01",
            "on my end.\x02\x03",
            "#3300345VHow about you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300346V\x07\x05",
            "#2PAlmost there. I've been moving the decoy\x01",
            "around as much as humanly possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300347V\x07\x05",
            "#2PI'll let ya know if Kitty shows up,\x01",
            "so keep your fingers on the keyboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300348V\x07\x00",
            "#0200F#5PAffirmative. We will stand\x01",
            "by until you give the signal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300349V\x07\x05",
            "#2PCool. Don't let me down, Tio!\x02",
        )
    )

    CloseMessageWindow()
    Sound(825, 0, 80, 0)
    StopBGM(0x1F40)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x103)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#3300350V#12P#0005FUm... So does that mean all of our\x01",
            "preparations are finished?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300351V#0204F#5PYes. All we need is Jona's signal.\x02\x03",
            "#3300352VOnce I start hacking, you can\x01",
            "leave everything to me.\x02\x03",
            "#3300353V#0211FDo you see why I opted to go\x01",
            "alone now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300354V#12P#0006FY-Yeah. I do.\x02\x03",
            "#3300355V#0000FBut still, the journey here wasn't exactly\x01",
            "the easiest thing in the world...\x02\x03",
            "#3300356VSo I'm glad I decided to tag along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300357V#0203F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300358V#12P#0012FUh, haha... (This is bad. I'm\x01",
            "terrible with awkward silences.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    ChrTalk(
        0x101,
        "#3300359V#6P#0005FOh, that's right. Mishy, wasn't it?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#3300360V#0002FYou know, that character you like so much.\x01",
            "He's even strapped to your Enigma.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300361V#0204FYes... I think you may be right.\x02\x03",
            "#3300362VI'm not really one to get\x01",
            "too attached to things, so...\x02\x03",
            "#3300363V#0202FIt's hard to believe I've held on to\x01",
            "that strap for all these years.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3300364V#12P#0005FYears? So you didn't buy it\x01",
            "when you came to Crossbell?\x02\x03",
            "#3300365VI assumed you did, since he's\x01",
            "practically Crossbell's mascot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300366V#0204F#5PNo. This was a gift.\x02\x03",
            "#3300367VFrom Guy, five years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#3300368V#12P#0011F#4S...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300369V#0203F#5PGuy Bannings...\x02\x03",
            "#3300370V#0202FHe was your brother, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300371V#12P#0008FUh, y-yeah, he was...\x01",
            "But, wait a second...\x02\x03",
            "#3300372V#0011FTio, you knew my brother?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300514V#0204F#5PYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300374V#12P#0006FI had no idea...\x02\x03",
            "#3300375V#0002FWhy didn't you tell me sooner?\x02\x03",
            "#3300376V#0005FYou're from Leman State, right?\x01",
            "How could you know Guy?\x02\x03",
            "#3300377VHe couldn't have come acr--\x02",
        )
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    FadeToDark(800, 0, -1)
    OP_C9(0x3, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(300)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3300378V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "'I'm going on a trip'? You can't just say\x01",
            "that and immediately walk out the door!\x02\x03",
            "#3300379VWhere are you even going?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3300380V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "The Principality of Remiferia.\x02\x03",
            "#3300381VDon't worry, I should be back in a\x01",
            "month or two.\x02\x03",
            "#3300382VWell, I can't dive into specifics, but it's\x01",
            "actually a trip where I'm in charge of\x01",
            "escorting this cute little girl back home.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_END)), "loc_2817")
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xAAFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3300383V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "Tio... I'm sorry, but have you\x01",
            "been to this hospital before?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 130, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#3300384V",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "Yes.\x02\x03",
            "#3300385VIt was about six years ago.\x02\x03",
            "#3300386VI wasn't planning to keep\x01",
            "it a secret, but...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Jump("loc_2833")

    label("loc_2817")

    FadeToBright(1000, 0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x3, 0x3)

    label("loc_2833")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300387V#12P#0005FNo way... That was you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300388V#0203F#5PYes.\x02\x03",
            "#3300389V#0202FI was only nine years old at the time.\x02\x03",
            "#3300390VGuy was the one who escorted me back\x01",
            "to my home in Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300391V#12P#0002FRemiferia...\x02\x03",
            "#3300392VThat's where you're from? Not Leman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300393V#0202F#5PThat's right.\x02\x03",
            "#3300394V#0204FIt may be my home country, but I harbor\x01",
            "no special feelings toward it...\x02\x03",
            "#3300395VAfter all, I have already abandoned\x01",
            "that place I used to call home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300521V#12P#0005FTio...\x02\x03",
            "#3300397V#0001FAre your parents okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300398V#0206F#5PI think so...?\x02\x03",
            "#3300399VEver since I left home three years ago,\x01",
            "I've hardly received any letters from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300400V#12P#0001F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300401V#0203F#5PDue to certain unavoidable circumstances,\x01",
            "I went missing at age five.\x02\x03",
            "#3300402VGuy was the one who rescued me...\x01",
            "After that, I was hospitalized at\x01",
            "St. Ursula for over half a year.\x02\x03",
            "#3300403V#0202FOnce I finally recovered, Guy insisted\x01",
            "on escorting me to my home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300404V#12P#0003FSo that's what happened.\x02\x03",
            "#3300405V#0008FBut if you were escorted back home,\x01",
            "why'd you leave again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300406V#0204F#5PHeehee...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_2CF6():
        OP_96(0xFE, 0x18ED4, 0xFA, 0xFFFFFF38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CF6)

    def lambda_2D10():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2D10)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x2)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300407V#0204F#5PLloyd.\x02\x03",
            "#3300408V#0202FYou know I'm a bit different from\x01",
            "regular people, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300409V#12P#0007FWhat?! Tio, you aren't...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300410V#0202F#5PIt's the truth. You know it is.\x02\x03",
            "#3300411V#0203FMy sensory reception is orders\x01",
            "of magnitude higher than\x01",
            "any normal person...\x02\x03",
            "#3300412VThe faint sounds an average ear\x01",
            "finds impossible to pick up...\x02\x03",
            "#3300413VThe flow of orbal waves no ordinary\x01",
            "person could ever perceive...\x02\x03",
            "#3300414VThe presence of elements modern\x01",
            "technology has trouble detecting...\x02\x03",
            "#3300415V#0208F#40WEven people's emotions and the\x01",
            "beat of their hearts...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300532V#12P#0005F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300417V#0208F#5PWhen I attended Sunday School, I was\x01",
            "always alone...\x02\x03",
            "#3300418VThe things the neighborhood children\x01",
            "saw and what I saw were worlds apart...\x02\x03",
            "#3300419VI wasn't oblivious to their prying eyes\x01",
            "and their private conversations about me.\x02\x03",
            "#3300420V#0206FI know my parents love me. I do. But\x01",
            "everything has its limits.\x02\x03",
            "#3300421VThe atmosphere at home just grew\x01",
            "tenser. That is when I began to realize...\x02\x03",
            "#3300422V#0202F...that it would have been better if I never\x01",
            "came home at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300423V#12P#0013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300424V#0204F#5PWithout even thinking of what I was doing,\x01",
            "I had bought a ticket out of Remiferia...\x02\x03",
            "#3300425V...and soon after was on the next train bound\x01",
            "for Crossbell from Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300426V#12P#0006FNo way...\x02\x03",
            "#3300427V#0008FYou really wanted to see my\x01",
            "brother again, didn't you, Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300428V#0208F#5P...I did.\x02\x03",
            "#3300429V#0206FWhen he bought me that strap as a gift,\x01",
            "Guy told me this...\x02\x03",
            "#3300430V#0202F'Rest easy, Tio. I know that you can find\x01",
            "happiness.'\x02\x03",
            "#3300431V'And if you have trouble finding it, just\x01",
            "give me a call.'\x02\x03",
            "#3300432V#0204F'Together, we'll send the source of your\x01",
            "sadness packing!'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300433V#12P#0012FHaha, yeah... That definitely sounds\x01",
            "like something that dolt would say.\x02\x03",
            "#3300434V#0008FBut, around that time, he...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300435V#0203F#5P...*nod*\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x20)

    def lambda_34F9():
        OP_96(0xFE, 0x18F9C, 0xFA, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34F9)

    def lambda_3513():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3513)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x103, 2)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300436V#0208F#5PAt the lowest point in my life, I met an Epstein\x01",
            "Foundation researcher by chance.\x02\x03",
            "#3300437VHe saw potential in my enhanced sensory reception\x01",
            "and recruited me for an orbal staff development\x01",
            "team that the foundation had just launched.\x02\x03",
            "#3300438V#0204FWith that, I transferred to Leman State and spent\x01",
            "three years as a foundation researcher.\x02\x03",
            "#3300439V#0202FThen, three months ago, I finally decided to return\x01",
            "to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300440V#12P#0001FTio...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(500)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 202200, 0, -1700, 0)
    SetChrPos(0x103, 202400, 250, 0, 90)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x9, 203100, 750, -1300, 0)
    SetCameraDistance(19000, 1500)
    SetChrFlags(0x101, 0x4)

    def lambda_37AE():
        OP_95(0xFE, 202200, 100, -400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37AE)
    Sleep(800)
    SetChrSubChip(0x103, 0x6)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    WaitChrThread(0x101, 1)
    OP_6F(0x10)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    SetChrSubChip(0x103, 0xB)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0xE)
    Sleep(100)
    SetChrSubChip(0x103, 0xD)
    Sleep(100)
    SetChrSubChip(0x103, 0xC)
    Sleep(500)

    ChrTalk(
        0x103,
        "#3300441V#0205F#5P#40WAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300442V#6P#0006FI'm so sorry. I'm sorry that my stupid\x01",
            "brother left us like he did...\x02\x03",
            "#3300443V#0008FNot honoring his promise to a girl...?\x01",
            "That's not like him at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300444V#0208F#5P#40WLloyd...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(806, 2, 100, 0)
    Sleep(500)
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)
    OP_0D()

    def lambda_3966():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3966)
    Sleep(150)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300445V#0005F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300446V#0200F#5PIt must be Jona.\x02",
    )

    CloseMessageWindow()
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#3300447V\x07\x05",
            "#6PThe kitten has been spotted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300448V\x07\x05",
            "#6PJust now, I noticed her nibbling\x01",
            "on the bait I threw out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300449V\x07\x05",
            "#6PI'm about to corner her, so gimme\x01",
            "all the support you can muster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300450V#0203F#5PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300451V#0003F#5PI guess I'm just along for the ride.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300452V#6P#0001FTio. Try not to go too crazy, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300453V#0202F#11PI will be careful. Do not worry.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x6)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x3)
    Sleep(1000)
    SetChrSubChip(0x103, 0x4)
    Sleep(100)
    SetChrSubChip(0x103, 0x5)
    Sound(1278, 255, 100, 0)
    Sleep(1000)
    Sound(1280, 255, 100, 0)
    Sleep(1500)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0x0, 0x103, 0x140, 0, 1250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(840, 2, 100, 0)
    BeginChrThread(0x103, 3, 0, 10)
    Sound(850, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x348)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis122.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis043.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis044.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis045.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_68(302400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(0, 0)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)

    AnonymousTalk(
        0x103,
        (
            "#3300456V#0203FBeginning concealment near the network\x01",
            "resource's second boundary domain.\x02\x03",
            "#3300457V#0200FStanding by for Kitty.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300458V\x07\x05",
            "Aye, aye, ma'am.\x02\x03",
            "#3300459VWhoa, are you serious?!\x02\x03",
            "#3300460VIt's her! Kitty already deactivated\x01",
            "all of our protections!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(905, 2, 100, 0)
    Sound(903, 0, 100, 0)
    OP_C9(0x1, 0x0, 0xFFFC0860, 0xFFFF8AD0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300461V\x07\x05",
            "Gahh! Do you know how tedious it was\x01",
            "to prepare that bait?! And now it's all...!\x02\x03",
            "#3300462VI-I don't believe this! How can\x01",
            "one person do all of this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300463V\x07\x00",
            "#0201FSettle down, Jona.\x02\x03",
            "#3300464VShe is likely trying to brute force her way\x01",
            "through with all her processing power.\x02\x03",
            "#3300465V#0203FPlease focus. Stay two steps ahead\x01",
            "and lead her toward my domain.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300466V\x07\x05",
            "Damn it, I'm not a machine!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x2, 0x0, 0xFFF97050, 0xFFFEEE90, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300467V\x07\x05",
            "She's passing through Control Terminal 4,\x01",
            "Control Terminal 17, City Hall's main terminal...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "#3300468V\x07\x05",
            "Here! I've caught her at Control Terminal 25!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis046.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis047.itp")
    SetMessageWindowPos(250, 110, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300469V\x07\x05",
            "She's entered your domain, Tio!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0x103,
        (
            "#3300470V\x07\x00",
            "#0202FAffirmative.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(904, 0, 100, 0)
    OP_C9(0x0, 0x0, 0xFFFE0430, 0xFFFE2B40, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x0, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(500)
    SetMessageWindowPos(300, 140, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#3300471V#0205FSo this is your archrival?\x02\x03",
            "#3300472VSh-She is fast... Extremely fast!\x02\x03",
            "#3300473V#0201FActivating Aeon system!\x01",
            "Initializing parallel processing!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1203, 255, 100, 0)
    Sleep(800)
    CreatePortrait(3, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x1, 0x0, 0xFFF97050, 0xFFFC5680, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x2, 0x0, 0x0, 0x0)
    OP_C9(0x2, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x2, 0x2, 0x0, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sound(907, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(0, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_C9(0x2, 0x0, 0xFFF8FB20, 0xFFFF7748, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x1, 0x4, 0x0, 0x0, 0x0)
    OP_C9(0x1, 0x0, 0xFFFF15A0, 0xFFFD67F0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x1, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis117.itp")
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis048.itp")
    Sleep(500)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300475V\x07\x05",
            "Confirming Kitty's presence...\x01",
            "Whoa, that's a strong current!\x02\x03",
            "#3300476VIf you keep it up, you won't even\x01",
            "need my help catching her!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#3300477V\x07\x00",
            "#0206FI disagree... Unlike you and Kitty,\x01",
            "I am not a true hacker.\x02\x03",
            "#3300478VIf my Aeon system does not last,\x01",
            "I will be easily overtaken.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300479V\x07\x05",
            "Damn it, then what do we do?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 150, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#3300480V\x07\x00",
            "#0203FIn preparation for that, raise your processing\x01",
            "output to max and block Kitty's exit.\x02\x03",
            "#3300481V#0201FI am predicting that Kitty will try to shift\x01",
            "over into your domain again.\x02\x03",
            "#3300482VChoose your timing carefully, because\x01",
            "I need you to capture her in 0.1 seconds.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300483V\x07\x05",
            "Oh, you've gotta be kidding me...\x01",
            "Screw it! I'm Jona freakin' Sacred!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 90, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#3300484V\x07\x00",
            "#0204FGet ready...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1281, 255, 100, 0)
    Sound(831, 0, 100, 0)
    Sound(506, 0, 100, 0)
    Sleep(2000)
    Sound(908, 0, 100, 0)
    FadeToDark(0, 16777215, -1)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x4, 0x0, 0x0, 0x0)
    CreatePortrait(1, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(1000)
    OP_C9(0x2, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x2, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_C9(0x3, 0x0, 0xFFFC5680, 0xFFFF9E58, 0x0)
    OP_C9(0x3, 0x1, 0x5DC, 0x5DC, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_C9(0x2, 0x0, 0xFFFEA070, 0xFFFE5250, 0x5DC)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x5DC)
    OP_C9(0x3, 0x1, 0x3E8, 0x3E8, 0x5DC)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    Sleep(1000)
    FadeToBright(0, 16777215)
    OP_0D()
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis049.itp")
    Sound(903, 0, 100, 0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    SetMessageWindowPos(200, 170, -1, -1)

    AnonymousTalk(
        0x103,
        "#3300486V#0201F#4SNow!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(907, 0, 100, 0)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis118.itp")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis116.itp")
    OP_C9(0x1, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x1, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    CreatePortrait(2, 0, 0, 480, 16, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    CreatePortrait(3, 0, 256, 480, 272, 0, 0, 512, 256, 0, 0, 480, 16, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetMessageWindowPos(250, 150, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300487V\x07\x05",
            scpstr(0x18),
            "#4S#1KTAKE THIS!!!\x02",
        )
    )

    Sleep(1600)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(906, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_24(0x389)
    OP_C9(0x0, 0x0, 0xFFF8AD00, 0xFFFD19D0, 0x0)
    OP_C9(0x0, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_C9(0x0, 0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x3E8)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFDCD8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x2328, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE0C0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1F40, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFE4A8, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1B58, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFEC78, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x1388, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x50)
    OP_CA(0x0, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x0, 0x0)
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300488V\x07\x05",
            "All right! I bagged myself a Kitty!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(202400, 1000, 0, 0)
    MoveCamera(310, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 202200, 0, -1700, 45)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sound(840, 2, 100, 0)
    StopBGM(0x1770)

    ChrTalk(
        0x101,
        "#3300489V#6P#0005FW-We won...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300490V#0204F#5P#30WYes. It looks that way.\x02\x03",
            "#3300491V#0208F#40WAh...\x02",
        )
    )

    CloseMessageWindow()
    StopEffect(0x0, 0x2)
    Sound(820, 0, 100, 0)
    OP_24(0x348)
    SetChrSubChip(0x103, 0x11)
    Sleep(150)
    SetChrSubChip(0x103, 0x12)
    Sleep(150)
    SetChrSubChip(0x103, 0x13)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4EDE():
        OP_95(0xFE, 202200, 100, -400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EDE)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x14)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x103, 0x15)

    ChrTalk(
        0x101,
        "#3300492V#6P#0007FT-Tio! Are you okay?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1272, 255, 70, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#3300493V#5P#0206F#40WI-I will be in a minute...\x02\x03",
            "#3300494VIncreasing the Aeon system's processing power\x01",
            "that much... The world is spinning around me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300495V#6P#0006F*sigh* Didn't I tell you not\x01",
            "to do anything crazy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetChrSubChip(0x103, 0x16)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0x17)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x19)
    Sleep(130)
    SetChrSubChip(0x103, 0x18)
    Sleep(130)
    SetChrSubChip(0x103, 0x17)
    Sleep(300)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    ChrTalk(
        0x103,
        "#3300496V#5P#0205F#30WLloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300497V#6P#0003F...Hey, Tio.\x02\x03",
            "#3300498V#0000FThat promise my brother made to you...\x01",
            "Allow me to keep it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#3300499V#5P#0200F#30WHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300500V#6P#0008F'And if you have trouble finding\x01",
            "it, just give me a call.'\x02\x03",
            "#3300501V'Together, we'll send the source\x01",
            "of your sadness packing!'\x02\x03",
            "#3300502V#0006FI hate to admit it, but my brother was amazing.\x02\x03",
            "#3300503VIn terms of power and the ability to take charge,\x01",
            "I'm nothing compared to him.\x02\x03",
            "#3300504V#0000FBut, I'll do my best to compensate.\x02\x03",
            "#3300505VHonoring his promise is the least\x01",
            "I can do to prove myself.\x02\x03",
            "#3300506VSo, what do you say...?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1E)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1C)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300507V#5P#0204F#30W...\x02\x03",
            "#3300508VHow mysterious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300509V#6P#0005FCome again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300510V#5P#0204FYou and Guy are almost nothing\x01",
            "alike, but, it's weird...\x02\x03",
            "#3300511VAt the same time, you two remind\x01",
            "me of each other.\x02\x03",
            "#3300512VThe way your spirit shines...\x01",
            "The way you look ahead with confidence...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300513V#6P#0005FMy brother and I...are similar?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1C)
    Sleep(100)
    SetChrSubChip(0x103, 0x1D)
    Sleep(100)
    SetChrSubChip(0x103, 0x1E)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3300373V#5P#0202FIn a lot of ways, yes.\x02\x03",
            "#3300515V#0204FBut, of course, you are a different person.\x02\x03",
            "#3300516VYou are who you are, Lloyd. And you are\x01",
            "not and can't be the same as Guy.\x02\x03",
            "#3300517V#0201FYou should know that better than anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300518V#6P#0008F...Yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300519V#5P#0204FThat aside...\x02\x03",
            "#3300520VIf you want to take over the promise,\x01",
            "then the details should change.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300396V#6P#0005FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_56B7():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_56B7)
    Fade(250)
    SetChrSubChip(0x103, 0xA)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300522V#11P#0202FYou don't need to worry about it now.\x01",
            "Not yet...\x02\x03",
            "#3300523VI would like you to make a promise that\x01",
            "is your own. Not Guy's.\x02\x03",
            "#3300524V#0204FWhatever you come up with will be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300525V#6P#0002FTio...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300526V#11P#0206FAnd... I'm not a child.\x02\x03",
            "#3300527VI loathe being treated like I'm someone\x01",
            "that needs to be helped and protected.\x02\x03",
            "#3300528V#0201FI'm a member of the SSS, just like you are...\x01",
            "Aren't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300529V#6P#0002FYou're right.\x02\x03",
            "#3300530V#0014FHaha, you're exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3300531V#11P#0209FHeehee.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300416V#6P#0005FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300533V#11P#0205F...?\x02\x03",
            "#3300534VIs there something on my face...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300535V#6P#0011FNo, it's just...\x02\x03",
            "#3300536V#0012FI think that's the first time I've\x01",
            "seen your genuine smile.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#3300537V#11P#0206FI-I wasn't smiling...!\x02\x03",
            "#3300538V#0208FI'm, um...exhausted. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3300539V#6P#0004FHaha, no need to be shy.\x02\x03",
            "#3300540V#0002FIt'd be a waste, in all honesty.\x02\x03",
            "#3300541VYour smile is adorable. If you showed it more\x01",
            "often, I'm sure you'd be crazy popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300542V#11P#0205FA-Adorable...?\x02\x03",
            "#3300543V#0211F*gulp*...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#3300544V\x07\x05",
            "#6PUm. *cough* *cough*\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    SetChrSubChip(0x103, 0x6)

    def lambda_5BE7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BE7)
    SetChrSubChip(0x103, 0x7)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3300545V#0005F#5PUh-oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300546V#11P#0205FJ-Jona?!\x02\x03",
            "#3300547V#0201FH-How long have you been listening?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300548V\x07\x05",
            "#6PUh... 'I think that's the first time I've seen your\x01",
            "genuine smile.' Somewhere around there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300549V\x07\x05",
            "#6PHaha! Can't say I was expecting to hear\x01",
            "a cheesy line like that today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300550V\x07\x05",
            "#6PWhat's more, you actually got\x01",
            "flustered over it! What's with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300551V\x07\x00",
            "#11P#0211FSpew any more nonsense and I will destroy\x01",
            "you with a 40-chain combo in Pom Party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300552V\x07\x05",
            "#6PThat's not even possible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#3300553V\x07\x05",
            "#6PWait... Actually, someone like you\x01",
            "might be able to pull that off.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 11)
    WaitChrThread(0x101, 3)
    Fade(500)
    OP_68(103000, 1000, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 101200, 0, -1700, 90)
    SetChrPos(0x103, 102300, 250, 0, 90)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x2)
    SetChrPos(0x9, 102600, 700, -1500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3300554V#6P#0001FThat reminds me, Jona.\x02\x03",
            "#3300555VDid you manage to find\x01",
            "out who Kitty is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300556V\x07\x05",
            "#2PHah! Who do you think I am?\x01",
            "I wasn't in the foundation for nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300557V\x07\x05",
            "#2PI managed to figure out her location.\x01",
            "I'm sending it to you right now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(824, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x0)

    def lambda_603C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_603C)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#3300558V\x07\x00",
            "#6P#0205F#6P...?\x02\x03",
            "#3300559VJona, what is with this\x01",
            "file you attached...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300560V\x07\x05",
            "#2PAn attachment? What the hell are you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300561V\x07\x05",
            "#2PThe log shouldn't contain anything like this!\x01",
            "It was just supposed to uncover her location...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300562V\x07\x00",
            "#6P#0201FWe should open it.\x02",
        )
    )

    CloseMessageWindow()
    Sound(850, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 10)
    Sleep(1200)
    EndChrThread(0x103, 0x3)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#3300563V#6P#0205FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300564V#6P#0013FThat's...!\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis123.itp")
    CreatePortrait(1, 112, 64, 368, 192, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis050.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300565V\x07\x05",
            "Wh-What the heck is THIS?!\x02\x03",
            "#3300566VWait just a damn minute!\x02\x03",
            "#3300567VThis couldn't be...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#3300568V\x07\x00",
            "#0206FIt appears the hackers became the\x01",
            "hacked. Maybe she wanted revenge?\x02\x03",
            "#3300569V#0208FNo... Perhaps we were dancing in\x01",
            "the palm of her hand from the start.\x02\x03",
            "#3300570V#0201FIf true, it is possible that the information\x01",
            "we obtained was simply a ruse.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3300571V\x07\x05",
            "Ughghhh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x103, 3, 0, 14)
    Sound(819, 0, 90, 0)
    Sound(514, 0, 70, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x2)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#3300572V#6P#0011FJona. You okay there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300573V\x07\x05",
            "#2P#2SDamn it... There's no way she should've\x01",
            "been able to mask her address..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300574V\x07\x05",
            "#2P#2SIf we could trace and analyze it, eventually\x01",
            "it'll lead back to the access point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#3300575V\x07\x05",
            "#2P#2SNo, that won't work... But what about...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3300576V#6P#0012FJona? Hey, can you hear me?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetMapObjFrame(0x3, "m00gim02", 0x2, "close")
    Sound(73, 0, 100, 0)
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x103, 101800, 0, 800, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(
        0x103,
        (
            "#3300577V#0206F#5PI would leave him alone.\x01",
            "For now, let's return to his place.\x02\x03",
            "#3300578V#0202FWe still need to retrieve our rightfully\x01",
            "earned memory quartz.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#3300579V#12P#0000FOh, I nearly forgot about that.\x02\x03",
            "#3300580VThat whole spectacle was enough\x01",
            "to make it slip my mind, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3300581V#0204F#5PHeehee...\x02\x03",
            "#3300582V#0202FThere should be an emergency\x01",
            "elevator near the exit.\x02\x03",
            "#3300583VWe'll take that and head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3300584V#12P#0002FLet's do it.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(100000, 2000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 100000, 0, 0, 270)
    SetChrPos(0x1, 100000, 0, 0, 270)
    SetScenarioFlags(0xA1, 3)
    OP_29(0x45, 0x1, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7300", 0)
    OP_24(0x326)
    OP_24(0x348)
    OP_24(0x389)
    EventEnd(0x5)
    Return()

    # Function_9_12E5 end

    def Function_10_6911(): pass

    label("Function_10_6911")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_693D")
    SetChrSubChip(0x103, 0x0)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    SetChrSubChip(0x103, 0x2)
    Sleep(70)
    SetChrSubChip(0x103, 0x1)
    Sleep(70)
    Jump("Function_10_6911")

    label("loc_693D")

    Return()

    # Function_10_6911 end

    def Function_11_693E(): pass

    label("Function_11_693E")


    def lambda_6943():
        OP_95(0xFE, 202200, 0, -1700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6943)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x5A, 0x190)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_11_693E end

    def Function_12_6969(): pass

    label("Function_12_6969")

    Sleep(1000)
    OP_C9(0x3, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_12_6969 end

    def Function_13_69C8(): pass

    label("Function_13_69C8")

    Sleep(300)
    OP_C9(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_13_69C8 end

    def Function_14_6A27(): pass

    label("Function_14_6A27")

    Sleep(300)
    OP_C9(0x0, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    OP_C9(0x1, 0x0, 0x4B0, 0xFFFFFBB4, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    OP_C9(0x1, 0x0, 0xFFFFFAEC, 0x4B0, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x640, 0xFFFFFB50, 0x1)
    OP_C9(0x1, 0x0, 0x640, 0xFFFFFB50, 0x1)
    Sleep(1)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1)
    OP_CA(0x0, 0xFF, 0x0)
    Return()

    # Function_14_6A27 end

    def Function_15_6AD1(): pass

    label("Function_15_6AD1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B73")

    ChrTalk(
        0x103,
        (
            "#0200FControl Terminal 3 should be past the\x01",
            "door on the right.\x02\x03",
            "We should log in and let Jona know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005FRight. Sorry about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BE2")

    label("loc_6B73")


    ChrTalk(
        0x103,
        (
            "#0203FControl Terminal 3 should be past the\x01",
            "door on the right.\x02\x03",
            "#0200FWe should log in and let Jona know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE2")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 6540, 180)
    EventEnd(0x4)
    Return()

    # Function_15_6AD1 end

    def Function_16_6BF9(): pass

    label("Function_16_6BF9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C8C")

    ChrTalk(
        0x101,
        (
            "#0005FCrap... That emergency elevator should\x01",
            "be somewhere around here, right?\x02\x03",
            "#0000FWe should take that to the surface.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF4")

    label("loc_6C8C")


    ChrTalk(
        0x103,
        (
            "#0203FThere should be an emergency\x01",
            "elevator near the exit.\x02\x03",
            "#0200FThat will save us a lot of time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF4")

    Sleep(50)
    OP_68(0, 0, -8290, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    SetChrPos(0x0, 0, 0, -8290, 0)
    EventEnd(0x4)
    Return()

    # Function_16_6BF9 end

    def Function_17_6D39(): pass

    label("Function_17_6D39")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The orbal terminal is down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_17_6D39 end

    SaveToFile()

Try(main)
