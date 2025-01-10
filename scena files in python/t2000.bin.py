from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2000.bin",                # FileName
        "t2000",                    # MapName
        "t2000",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 24450, 0, -890, 0, 0, 1, 89, 0, 2, 0, 4],
    )

    BuildStringList((
        "t2000",                  # 0
        "Guardsman Carter",       # 1
        "Guardsman Loggins",      # 2
        "Billy",                  # 3
        "Tourist",                # 4
        "Tourist",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist Kururu",         # 11
        "Bus",                    # 12
        "Warrant Officer Mireille",# 13
        "West Crossbell Highway", # 14
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch32300.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch20400.itc",                   # 06
        "chr/ch20000.itc",                   # 07
        "chr/ch20100.itc",                   # 08
        "chr/ch23600.itc",                   # 09
        "chr/ch34400.itc",                   # 0A
    ))

    DeclNpc(22430,   0,       4730,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(22239,   0,       -5489,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(19319,   0,       13449,   270,  385,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(13500,   0,       26299,   270,  385,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(21540,   200,     -11369,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(38529,   0,       -3880,   85,   385,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(19920,   200,     -11939,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(31100,   200,     -16420,  90,   385,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(30870,   0,       22549,   270,  385,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(30870,   0,       23530,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(26700,   200,     -16879,  135,  385,  0x0, 0,   10,  0,   0,   1,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(31260,   0,       27730,   1200,    31260,   1000,    27730,   0x007C, 0,  23, 0x0000)
    DeclActor(18980,   200,     -11720,  1200,    18980,   1700,    -11720,  0x007C, 0,  26, 0x0000)
    DeclActor(39780,   0,       1010,    1200,    39780,   2000,    1010,    0x007C, 0,  11, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  5,  0x0000)

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(5.0, 0.0, -0.800000011920929, 0x0000, 0x0052, "")
    PlaceName(30.850000381469727, 0.0, 27.90999984741211, 0x0000, 0x0055, "")
    PlaceName(39.75, 0.0, 2.5999999046325684, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_378",          # 00, 0
        "Function_1_430",          # 01, 1
        "Function_2_45B",          # 02, 2
        "Function_3_4B8",          # 03, 3
        "Function_4_56D",          # 04, 4
        "Function_5_666",          # 05, 5
        "Function_6_7E0",          # 06, 6
        "Function_7_8A8",          # 07, 7
        "Function_8_9C4",          # 08, 8
        "Function_9_A59",          # 09, 9
        "Function_10_1032",        # 0A, 10
        "Function_11_1121",        # 0B, 11
        "Function_12_112F",        # 0C, 12
        "Function_13_1DED",        # 0D, 13
        "Function_14_2A5E",        # 0E, 14
        "Function_15_2B2B",        # 0F, 15
        "Function_16_2BDB",        # 10, 16
        "Function_17_2CC4",        # 11, 17
        "Function_18_2D87",        # 12, 18
        "Function_19_2DF0",        # 13, 19
        "Function_20_2EBA",        # 14, 20
        "Function_21_2F4D",        # 15, 21
        "Function_22_2FEE",        # 16, 22
        "Function_23_3195",        # 17, 23
        "Function_24_325E",        # 18, 24
        "Function_25_3786",        # 19, 25
        "Function_26_4211",        # 1A, 26
    ))


    def Function_0_378(): pass

    label("Function_0_378")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3B8"),
        (1, "loc_3C4"),
        (2, "loc_3D0"),
        (3, "loc_3DC"),
        (4, "loc_3E8"),
        (5, "loc_3F4"),
        (6, "loc_400"),
        (SWITCH_DEFAULT, "loc_40C"),
    )


    label("loc_3B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_40C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_418")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_42F")

    Return()

    # Function_0_378 end

    def Function_1_430(): pass

    label("Function_1_430")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45A")
    OP_94(0xFE, 0x60D6, 0xFFFFB442, 0x7346, 0xFFFFC888, 0x3E8)
    Sleep(400)
    Jump("Function_1_430")

    label("loc_45A")

    Return()

    # Function_1_430 end

    def Function_2_45B(): pass

    label("Function_2_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_END)), "loc_467")
    Call(0, 3)

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_476")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    SetMapFlags(0x10000000)
    Event(0, 24)
    SetScenarioFlags(0x88, 1)
    Jump("loc_4B7")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_49F")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_4B7")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_4B7")

    Return()

    # Function_2_45B end

    def Function_3_4B8(): pass

    label("Function_3_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D0")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_559")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E3")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_559")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_559")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_559")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_559")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_520")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_559")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_533")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_559")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_54B")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_559")

    label("loc_54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_559")
    ClearChrFlags(0xB, 0x80)

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearChrFlags(0x12, 0x80)

    label("loc_56C")

    Return()

    # Function_3_4B8 end

    def Function_4_56D(): pass

    label("Function_4_56D")

    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CA")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    OP_66(0x2, 0x1)
    Jump("loc_5CF")

    label("loc_5CA")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5DD")
    Jump("loc_64E")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_64E")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_64E")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_607")
    Jump("loc_64E")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_64E")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_623")
    Jump("loc_64E")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_64E")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_645")
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_64E")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_64E")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661")
    OP_70(0x6, 0x0)
    Jump("loc_665")

    label("loc_661")

    OP_70(0x6, 0x1E)

    label("loc_665")

    Return()

    # Function_4_56D end

    def Function_5_666(): pass

    label("Function_5_666")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_750")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_6E6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_74B")

    label("loc_6E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_74B")

    Jump("loc_7D4")

    label("loc_750")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Getting over barriers wasn't enough, so you had\x01",
            "to go and start breaking boundaries, too?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7D4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_666 end

    def Function_6_7E0(): pass

    label("Function_6_7E0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x01",
            "Wait for a bus?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crossbell City - West Exit\x01",      # 0
            "Bus Stop (Police Academy)\x01",       # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_8A0")

    label("loc_880")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_8A0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_7E0 end

    def Function_7_8A8(): pass

    label("Function_7_8A8")

    Fade(1000)
    OP_68(27670, 1000, 21230, 0)
    MoveCamera(319, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 32119, 0, 25500, 270)
    SetChrPos(0x1, 32119, 0, 24000, 270)
    SetChrPos(0x2, 32119, 0, 22500, 270)
    SetChrPos(0x3, 32119, 0, 21000, 270)
    ClearChrFlags(0x13, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x13)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, 27000, 0, 4810, 0)
    OP_D3(0x13, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_0D()
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_97E():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_97E)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x13, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_8A8 end

    def Function_8_9C4(): pass

    label("Function_8_9C4")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 31190, 0, 26620, 265)
    SetChrPos(0x1, 31190, 0, 26620, 265)
    SetChrPos(0x2, 31190, 0, 26620, 265)
    SetChrPos(0x3, 31190, 0, 26620, 265)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_9C4 end

    def Function_9_A59(): pass

    label("Function_9_A59")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")

    Menu(
        0,
        32,
        26,
        1,
        (
            "Ride in Guardian Force car\x01",      # 0
            "Rest\x01",                            # 1
            "Leave\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC7")
    Sound(1500, 255, 100, 0)
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFF")
    MenuCmd(1, 1, "★City - Central Square")
    MenuCmd(3, 1, 0x0)
    Jump("loc_B1A")

    label("loc_AFF")

    MenuCmd(1, 1, "　City - Central Square")

    label("loc_B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    MenuCmd(1, 1, "★City - East Exit")
    MenuCmd(3, 1, 0x1)
    Jump("loc_B5E")

    label("loc_B48")

    MenuCmd(1, 1, "　City - East Exit")

    label("loc_B5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8C")
    MenuCmd(1, 1, "★City - West Exit")
    MenuCmd(3, 1, 0x2)
    Jump("loc_BA2")

    label("loc_B8C")

    MenuCmd(1, 1, "　City - West Exit")

    label("loc_BA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD1")
    MenuCmd(1, 1, "★City - South Exit")
    MenuCmd(3, 1, 0x3)
    Jump("loc_BE8")

    label("loc_BD1")

    MenuCmd(1, 1, "　City - South Exit")

    label("loc_BE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C17")
    MenuCmd(1, 1, "★City - North Exit")
    MenuCmd(3, 1, 0x4)
    Jump("loc_C2E")

    label("loc_C17")

    MenuCmd(1, 1, "　City - North Exit")

    label("loc_C2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C58")
    MenuCmd(1, 1, "★Tangram Gate")
    MenuCmd(3, 1, 0x5)
    Jump("loc_C6A")

    label("loc_C58")

    MenuCmd(1, 1, "　Tangram Gate")

    label("loc_C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")
    MenuCmd(1, 1, "★Bellguard Gate")
    MenuCmd(3, 1, 0x6)
    Jump("loc_CAA")

    label("loc_C96")

    MenuCmd(1, 1, "　Bellguard Gate")

    label("loc_CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE2")
    MenuCmd(1, 1, "★St. Ursula Medical College")
    MenuCmd(3, 1, 0x7)
    Jump("loc_D02")

    label("loc_CE2")

    MenuCmd(1, 1, "　St. Ursula Medical College")

    label("loc_D02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    MenuCmd(1, 1, "★Armorica Village")
    MenuCmd(3, 1, 0x8)
    Jump("loc_D46")

    label("loc_D30")

    MenuCmd(1, 1, "　Armorica Village")

    label("loc_D46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D78")
    MenuCmd(1, 1, "★Mainz Mining Village")
    MenuCmd(3, 1, 0x9)
    Jump("loc_D92")

    label("loc_D78")

    MenuCmd(1, 1, "　Mainz Mining Village")

    label("loc_D92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    MenuCmd(1, 1, "★Mainz Mountain Path - Tunnel")
    MenuCmd(3, 1, 0xA)
    Jump("loc_DEE")

    label("loc_DCC")

    MenuCmd(1, 1, "　Mainz Mountain Path - Tunnel")

    label("loc_DEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1D")
    MenuCmd(1, 1, "★Stargazer's Tower")
    MenuCmd(3, 1, 0xB)
    Jump("loc_E34")

    label("loc_E1D")

    MenuCmd(1, 1, "　Stargazer's Tower")

    label("loc_E34")

    MenuCmd(1, 1, "　Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB8")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F0B"),
        (1, "loc_F19"),
        (2, "loc_F27"),
        (3, "loc_F35"),
        (4, "loc_F43"),
        (5, "loc_F51"),
        (6, "loc_F5F"),
        (7, "loc_F6D"),
        (8, "loc_F7B"),
        (9, "loc_F89"),
        (10, "loc_F97"),
        (11, "loc_FA5"),
        (SWITCH_DEFAULT, "loc_FB3"),
    )


    label("loc_F0B")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F19")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F27")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F35")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F43")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F51")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F5F")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F6D")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F7B")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F89")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_F97")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_FA5")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_FB3")

    label("loc_FB3")

    Jump("loc_FC2")

    label("loc_FB8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC2")

    Jump("loc_1025")

    label("loc_FC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1012")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1025")

    label("loc_1012")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1025")

    Jump("loc_A73")

    label("loc_102A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_A59 end

    def Function_10_1032(): pass

    label("Function_10_1032")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 39720, 0, -990, 175)
    SetChrPos(0x1, 39720, 0, -990, 175)
    SetChrPos(0x2, 39720, 0, -990, 175)
    SetChrPos(0x3, 39720, 0, -990, 175)
    SetChrPos(0x4, 39720, 0, -990, 175)
    SetChrPos(0x5, 39720, 0, -990, 175)
    Sleep(1)
    OP_68(39720, 1000, -990, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1106")
    Sound(1502, 255, 100, 0)
    Jump("loc_110C")

    label("loc_1106")

    Sound(1503, 255, 100, 0)

    label("loc_110C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1032 end

    def Function_11_1121(): pass

    label("Function_11_1121")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_1121 end

    def Function_12_112F(): pass

    label("Function_12_112F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(
        0xFE,
        (
            "If you weren't aware, Bellguard Gate\x01",
            "secures Crossbell's border with the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 300)

    ChrTalk(
        0xFE,
        "Wait a minute... Randy, is that you?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FHey, man. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. It's good to see you again.\x01",
            "I wasn't expecting you to show up\x01",
            "here again, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, duty calls. Take it easy, okay?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 0)
    Jump("loc_1DE9")

    label("loc_1293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1338")

    ChrTalk(
        0xFE,
        "We have a drill planned for tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "'Cause of all the stress we stack up while\x01",
            "working, we take these opportunities to\x01",
            "blow off some steam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE9")

    label("loc_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1429")

    ChrTalk(
        0xFE,
        (
            "We received a report yesterday about\x01",
            "Tangram Gate's investigation of those\x01",
            "ruins off of Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The commander didn't give two hoots\x01",
            "about it, though. I wouldn't be surprised\x01",
            "if he tossed it in the trash.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE9")

    label("loc_1429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1613")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0xFE,
        "Randy, what brings you here today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHey, man. We're takin' over the reins of\x01",
            "that investigation you withdrew from.\x01",
            "Y'know, the one about the ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A-Are you pulling my leg...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FNope. From what I've heard, His Excellency\x01",
            "pushed everything onto Tangram Gate's plate.\x02\x03",
            "#0309FSorry, pal. We're gonna have to steal the\x01",
            "spotlight from ya.\x02\x03",
            "#0300FPass that along to the commander for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, how about you tell him yourself?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CD")

    label("loc_1613")


    ChrTalk(
        0xFE,
        (
            "Still... If you guys are cooperating with the\x01",
            "Tangram Gate troops, I can't help but feel\x01",
            "reassured about this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd appreciate it if you made up for our\x01",
            "ineptitude, Randy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CD")

    Jump("loc_1DE9")

    label("loc_16D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(
        0xFE,
        (
            "Work should start slowing down after\x01",
            "today...I hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE9")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_189C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183E")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0xFE,
        "Randy, how's the festival been treating you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FDunno. Work's been keepin' me busy.\x01",
            "Same as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, at least you guys get to walk\x01",
            "around Crossbell while on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Standing here all day can get pretty\x01",
            "painful on the legs, you know.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1897")

    label("loc_183E")


    ChrTalk(
        0xFE,
        (
            "Even if it was for work, I'd jump\x01",
            "at the chance to travel all over\x01",
            "Crossbell State.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1897")

    Jump("loc_1DE9")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_196A")

    ChrTalk(
        0xFE,
        (
            "*sigh* I bet the commander is in a nice,\x01",
            "cool room by now, having his fill of fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "WE'RE the ones who have to skip the\x01",
            "festivities and work. That guy just\x01",
            "infuriates me to no end...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE9")

    label("loc_196A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABE")

    ChrTalk(
        0xFE,
        (
            "Apparently, the commander up and\x01",
            "left a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before leaving, he told us that all we're\x01",
            "going to do is background-check tourists,\x01",
            "so just follow Warrant Officer Mireille's orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He may have a point, but would it kill\x01",
            "him to act like the Crossbell Guardian\x01",
            "Force commander every so often...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B2A")

    label("loc_1ABE")


    ChrTalk(
        0xFE,
        "I can't stand that man...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In every way except rank, Warrant\x01",
            "Officer Mireille runs Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B2A")

    Jump("loc_1DE9")

    label("loc_1B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1BCC")

    ChrTalk(
        0xFE,
        (
            "Over in the Knox Forest, you'll find\x01",
            "the police academy and the prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our unit is in charge of security over\x01",
            "there, too, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE9")

    label("loc_1BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C71")

    ChrTalk(
        0xFE,
        (
            "A little while ago, a pair of bracers\x01",
            "stopped by Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They looked young, but their skill\x01",
            "more than made up for that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D2E")

    label("loc_1C71")


    ChrTalk(
        0xFE,
        (
            "A little while ago, a pair of bracers\x01",
            "stopped by Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They might be young, but it was clear\x01",
            "that they were holding back. I definitely\x01",
            "wouldn't underestimate those two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2E")

    Jump("loc_1DE9")

    label("loc_1D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DE9")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0xFE,
        (
            "Randy, I genuinely didn't think that\x01",
            "you were ever going to come back\x01",
            "to Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, take your time. I'm not going\x01",
            "to be the one to kick you out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE9")

    TalkEnd(0xFE)
    Return()

    # Function_12_112F end

    def Function_13_1DED(): pass

    label("Function_13_1DED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(
        0xFE,
        "Hmm, I think I'm getting rusty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I want to be prepared for the\x01",
            "unexpected, I'm going to have to\x01",
            "give it my all during tonight's drill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5A")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F3C")

    ChrTalk(
        0xFE,
        (
            "So, you went and investigated the\x01",
            "entirety of those creepy ruins?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Geez, I admire your tenacity. I'd never\x01",
            "be able to pull off something like that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5A")

    label("loc_1F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A5")

    ChrTalk(
        0xFE,
        (
            "I was actually on the scouting team that\x01",
            "was looking into the Mainz ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The interior of that place was crawling\x01",
            "with ghosts, demons, you name it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It was like a living nightmare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 300)

    ChrTalk(
        0x101,
        (
            "#0000FAre you all right, Elie?\x01",
            "You look incredibly pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0112FI-I'm perfectly fine! Never been better!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2144")

    label("loc_20A5")


    ChrTalk(
        0xFE,
        (
            "Those ruins were full of monsters\x01",
            "none of us had ever seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I legitimately think we were lucky\x01",
            "that we withdrew before anything\x01",
            "bad happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2144")

    Jump("loc_2A5A")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2333")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(
        0xFE,
        (
            "The delivery truck arrived pretty late yesterday.\x01",
            "I probably shouldn't have, but I accidentally\x01",
            "chewed out Billy, the driver...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I just found it strange that he came late,\x01",
            "when he's usually so punctual... I guess\x01",
            "something must have happened to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I messed up.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_232E")

    label("loc_2279")


    ChrTalk(
        0xFE,
        (
            "Billy didn't tell me the reason he\x01",
            "ended up delivering so late, so I\x01",
            "kind of started yelling at him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to apologize next time I see\x01",
            "him. He didn't deserve that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232E")

    Jump("loc_2A5A")

    label("loc_2333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_23F2")

    ChrTalk(
        0xFE,
        (
            "We're receiving a shipment of packages\x01",
            "from Crossbell City today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're pretty busy, so I'm going to have\x01",
            "the delivery driver unload everything\x01",
            "right when he arrives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5A")

    label("loc_23F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2550")

    ChrTalk(
        0xFE,
        (
            "Occasionally, we see tourists from\x01",
            "Erebonia attempt to walk to the city,\x01",
            "staying on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The majority of them are spoiled rich\x01",
            "guys who don't understand how harsh\x01",
            "the highway can be... *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F(That sounds a lot like us when\x01",
            "we walked to Armorica Village.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(Please do not remind me.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25A9")

    label("loc_2550")


    ChrTalk(
        0xFE,
        (
            "Those wealthy Imperials are way too\x01",
            "optimistic and never fail to cause us\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A9")

    Jump("loc_2A5A")

    label("loc_25AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_262B")

    ChrTalk(
        0xFE,
        (
            "I just want to get a good night's rest.\x01",
            "All these tourists coming through here\x01",
            "have worked us to death...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5A")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_287D")
    TurnDirection(0x9, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2803")

    ChrTalk(
        0xFE,
        (
            "Randy, up for a spar next\x01",
            "time you stop by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FHuh? Why the hell do you wanna\x01",
            "do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, when you were stationed here,\x01",
            "I never once beat you in any of our\x01",
            "combat drills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about that rubs me the wrong\x01",
            "way. It's like you ran away without giving\x01",
            "me the chance to make things even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FYou're seriously hung up on that?\x02\x03",
            "#0300FFine, but I'm a lil' busy right now.\x01",
            "If I remember next time, I'm game.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2878")

    label("loc_2803")


    ChrTalk(
        0xFE,
        (
            "My reputation as a member of the CGF\x01",
            "hinges on this fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Randy...don't you forget about\x01",
            "our fight, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2878")

    Jump("loc_2A5A")

    label("loc_287D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298A")

    ChrTalk(
        0xFE,
        "Our commander is absent today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Actually, I guess it'd be better to say\x01",
            "that he's absent again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every single day, that guy is preoccupied\x01",
            "with entertaining politicians and the like...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0303F(Heh. Some things never change.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A5A")

    label("loc_298A")


    ChrTalk(
        0xFE,
        (
            "Day after day, all the commander thinks\x01",
            "about is wining and dining with other\x01",
            "influential people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without Warrant Officer Mireille here to\x01",
            "lead us, this unit would have broken up\x01",
            "a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5A")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DED end

    def Function_14_2A5E(): pass

    label("Function_14_2A5E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "After making so many deliveries\x01",
            "in the city, I almost forgot that we\x01",
            "deliver all the way out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm sure the CGF members are\x01",
            "waiting for their packages. Guess I\x01",
            "better get to it.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2A5E end

    def Function_15_2B2B(): pass

    label("Function_15_2B2B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "So this is one of the Guardian Force's\x01",
            "armored cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm, it's pretty sturdy, isn't it?\x01",
            "Though, I doubt it would last long\x01",
            "against one of the Empire's tanks.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2B2B end

    def Function_16_2BDB(): pass

    label("Function_16_2BDB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "People kept telling me that Crossbell\x01",
            "isn't safe for a woman traveling alone,\x01",
            "but look at me. I'm safe and sound.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I guess present-day Crossbell is\x01",
            "a lot safer than it used to be... I'm sure\x01",
            "I'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2BDB end

    def Function_17_2CC4(): pass

    label("Function_17_2CC4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I traveled here from Erebonia on foot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I've come this far, I don't see why I\x01",
            "shouldn't walk over to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Then again, maybe it would be a bit\x01",
            "too dangerous.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2CC4 end

    def Function_18_2D87(): pass

    label("Function_18_2D87")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "Geez, he's soooo late...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I should leave him behind\x01",
            "and head on to Crossbell City.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2D87 end

    def Function_19_2DF0(): pass

    label("Function_19_2DF0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I LOVE the railway. I even got\x01",
            "permission to take pictures of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pretty sure this is the CGF's freight line.\x01",
            "I wonder what kind of train will come...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe. I can hardly wait!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_2DF0 end

    def Function_20_2EBA(): pass

    label("Function_20_2EBA")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "We're on our way to tour the Empire.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After hearing about their magnificent\x01",
            "stores and architecture, we knew we\x01",
            "just had to visit.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2EBA end

    def Function_21_2F4D(): pass

    label("Function_21_2F4D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To be frank, visiting the Empire makes\x01",
            "me feel a little uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, everyone's heard about\x01",
            "the conflicts between Crossbell\x01",
            "and Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2F4D end

    def Function_22_2FEE(): pass

    label("Function_22_2FEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F1")

    ChrTalk(
        0xFE,
        (
            "Crossbellans not only have trains,\x01",
            "but buses, too... You guys sure\x01",
            "have it easy, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If only they built a train station and had\x01",
            "bus stops near my house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they did, I'd be coming to Crossbell\x01",
            "whenever I had the chance.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3191")

    label("loc_30F1")


    ChrTalk(
        0xFE,
        (
            "If only they built a train station and had\x01",
            "bus stops near my house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If they did, I'd be able to have all sorts\x01",
            "of fun in Crossbell whenever I want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3191")

    TalkEnd(0xFE)
    Return()

    # Function_22_2FEE end

    def Function_23_3195(): pass

    label("Function_23_3195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_325A")
    TalkBegin(0xFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a bus stop.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Due to the ongoing monster infestation, the\x01",
            "bus service has been temporarily suspended.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_325D")

    label("loc_325A")

    Call(0, 6)

    label("loc_325D")

    Return()

    # Function_23_3195 end

    def Function_24_325E(): pass

    label("Function_24_325E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(16650, 400, -10470, 0)
    MoveCamera(295, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(14930, 400, 890, 5000)
    MoveCamera(280, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac18", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(50970, 1000, -460, 4700)
    MoveCamera(315, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_365B")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_337A")
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x13)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    Jump("loc_3391")

    label("loc_337A")

    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x13)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)

    label("loc_3391")

    OP_49()
    SetChrPos(0x13, 63820, 0, -120, 0)
    OP_D3(0x13, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_33DA")
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_33F0")

    label("loc_33DA")

    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    label("loc_33F0")

    Sleep(2200)

    def lambda_33F8():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_33F8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_342A")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_3430")

    label("loc_342A")

    Sound(485, 0, 100, 0)

    label("loc_3430")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_345B")
    SetChrFlags(0x13, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_3492")

    label("loc_345B")

    SetChrPos(0x13, 40000, 0, 2500, 0)
    OP_D3(0x13, 0x0, 0x15F90, 0x0, 0x0)
    OP_71(0x5, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x5)
    OP_66(0x2, 0x1)

    label("loc_3492")

    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3577")
    SetChrPos(0x0, 31190, 0, 26620, 265)
    SetChrPos(0x1, 31190, 0, 26620, 265)
    SetChrPos(0x2, 31190, 0, 26620, 265)
    SetChrPos(0x3, 31190, 0, 26620, 265)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    ClearScenarioFlags(0x7E, 0)
    Jump("loc_3646")

    label("loc_3577")

    SetChrPos(0x0, 39720, 0, -990, 175)
    SetChrPos(0x1, 39720, 0, -990, 175)
    SetChrPos(0x2, 39720, 0, -990, 175)
    SetChrPos(0x3, 39720, 0, -990, 175)
    SetChrPos(0x4, 39720, 0, -990, 175)
    SetChrPos(0x5, 39720, 0, -990, 175)
    Sleep(1)
    OP_68(39720, 1000, -990, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3631")
    Sound(1502, 255, 100, 0)
    Jump("loc_3637")

    label("loc_3631")

    Sound(1503, 255, 100, 0)

    label("loc_3637")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_3646")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_377E")

    label("loc_365B")

    Sleep(2500)
    SetChrPos(0x0, 54820, 0, -130, 270)
    SetChrPos(0x1, 56020, 0, -1200, 270)
    SetChrPos(0x2, 56170, 0, 1010, 270)
    SetChrPos(0x3, 57750, 0, -190, 270)
    OP_0D()

    def lambda_36A8():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_36A8)

    def lambda_36C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_36C2)
    Sleep(100)

    def lambda_36D6():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_36D6)

    def lambda_36F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_36F0)
    Sleep(120)

    def lambda_3704():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3704)

    def lambda_371E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_371E)
    Sleep(90)

    def lambda_3732():
        OP_95(0xFE, 53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3732)

    def lambda_374C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_374C)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    WaitChrThread(0x0, 2)
    WaitChrThread(0x1, 2)
    WaitChrThread(0x2, 2)
    WaitChrThread(0x3, 2)
    Sleep(1000)
    Call(0, 3)

    label("loc_377E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_325E end

    def Function_25_3786(): pass

    label("Function_25_3786")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32600.itc", 0x1E)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 19360, 0, 15000, 180)
    SetChrPos(0x101, 18260, 0, 12300, 0)
    SetChrPos(0x102, 19500, 0, 11500, 4)
    SetChrPos(0x103, 21020, 0, 12290, 319)
    SetChrPos(0x104, 19360, 0, 13260, 0)
    OP_68(7070, 1000, 14810, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26990, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_68(18760, 1000, 13910, 6000)
    MoveCamera(319, 20, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(17860, 6000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#5P#0300FI think you were lookin' for this?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Randy handed the key to the armored car over\x01",
            "to Mireille and explained how they found it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    ChrTalk(
        0x14,
        (
            "#11PIt seriously ended up in a place like that?\x01",
            "I never would have found it, then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FWhat probably happened is that your\x01",
            "commander dropped it while he was\x01",
            "singing on the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P*sigh* That aside, I'm just relieved\x01",
            "that you were able to find it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PThanks to you, we can finally move\x01",
            "the armored car somewhere less\x01",
            "conspicuous to travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PI guess I'm in your debt...this time, Randy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#0304FDon't worry about it.\x02\x03",
            "#0309FBuuut, if you really want to make\x01",
            "things even, how 'bout goin' on a\x01",
            "date with me? It'd be a good time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PI don't know what I was expecting...\x01",
            "Idiots never change, do they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PWell, thank you for everything, SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FYou're welcome. If you ever need\x01",
            "anything from us, all you have to\x01",
            "do is submit a support request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11PI'll keep that in mind. Now, if you'll\x01",
            "excuse me.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19040, 1000, 12630, 4000)

    def lambda_3C93():
        OP_95(0xFE, 23200, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3C93)
    WaitChrThread(0x14, 1)

    def lambda_3CB1():
        OP_95(0xFE, 23200, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3CB1)

    def lambda_3CCB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CCB)
    Sleep(100)

    def lambda_3CDB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CDB)
    Sleep(100)

    def lambda_3CEB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3CEB)
    Sleep(100)

    def lambda_3CFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CFB)
    Sleep(100)

    def lambda_3D0B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D0B)
    Sleep(100)

    def lambda_3D1B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D1B)
    Sleep(100)

    def lambda_3D2B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D2B)
    Sleep(100)

    def lambda_3D3B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D3B)
    WaitChrThread(0x14, 1)

    def lambda_3D4C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D4C)
    Sleep(100)

    def lambda_3D5C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3D5C)
    Sleep(100)

    def lambda_3D6C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D6C)
    Sleep(100)

    def lambda_3D7C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D7C)

    ChrTalk(
        0x104,
        "#11P#0300FCase closed, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0106FI suppose so. I wasn't sure we would\x01",
            "find the key for a second there.\x02\x03",
            "#0108FIf a stranger picked it up, I don't know\x01",
            "what we would have done...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0000FConsidering where it was dropped,\x01",
            "I'd say we got lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#0203FI am inclined to agree.\x02\x03",
            "#0200FIncidents like this could be avoided\x01",
            "if the commander was a bit more\x01",
            "observant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0303FHe's always been an incompetent\x01",
            "jackass, even when I was stationed\x01",
            "here.\x02\x03",
            "#0301FIf we didn't find that key, Mireille\x01",
            "probably would've taken the heat\x01",
            "for losin' it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#0106FThat man is hopeless...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003F...No denying that.\x02\x03",
            "#0000FStill, at least we know that there are people\x01",
            "like the deputy commander and the warrant\x01",
            "officer doing honest work in the CGF.\x02\x03",
            "I'd like to think that most of the guardsmen\x01",
            "are following suit, despite everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#0304FGood point, Lloyd.\x02\x03",
            "#0300FWell, time to head out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#0000FYeah, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Important Item Retrieval]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-350, 1540, 12250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 18260, 0, 12300, 90)
    OP_29(0x19, 0x2, 0x1F)
    OP_29(0x19, 0x1, 0xA)
    OP_29(0x19, 0x4, 0x10)
    Sleep(500)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    EventEnd(0x5)
    Return()

    # Function_25_3786 end

    def Function_26_4211(): pass

    label("Function_26_4211")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erebonian Empire Border\x01",
            "       Bellguard Gate\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4211 end

    SaveToFile()

Try(main)
