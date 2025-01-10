from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r307b.bin",                # FileName
        "r307b",                    # MapName
        "r307b",                    # Location
        0x0065,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -62000, 0, -2000, 0, 0, 1, 101, 0, 0, 0, 1],
    )

    BuildStringList((
        "r307b",                  # 0
        "車１",                   # 1
        "To Old Armorica Road",   # 2
        "To Sun Fort",            # 3
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-36150,  100,     -11590,  1200,    -36150,  1100,    -11590,  0x007C, 0,  2,  0x0000)
    DeclActor(26000,   3100,    -16000,  1200,    26000,   4100,    -16000,  0x007C, 0,  3,  0x0000)
    DeclActor(26000,   3100,    16000,   1200,    26000,   4100,    16000,   0x007C, 0,  4,  0x0000)
    DeclActor(37500,   3100,    16000,   1200,    37500,   4100,    16000,   0x007C, 0,  5,  0x0000)

    PlaceName(-95.0, 0.0, -6.0, 0x0000, 0x0000, "To Old Armorica Road")
    PlaceName(82.0, 0.0, -34.0, 0x0000, 0x0000, "To Sun Fort")

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_194",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_3A1",          # 03, 3
        "Function_4_552",          # 04, 4
        "Function_5_6F9",          # 05, 5
        "Function_6_860",          # 06, 6
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_193")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_193")

    Return()

    # Function_0_184 end

    def Function_1_194(): pass

    label("Function_1_194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7")
    OP_70(0x0, 0x0)
    Jump("loc_1AB")

    label("loc_1A7")

    OP_70(0x0, 0x1E)

    label("loc_1AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE")
    OP_70(0x1, 0x0)
    Jump("loc_1C2")

    label("loc_1BE")

    OP_70(0x1, 0x1E)

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5")
    OP_70(0x2, 0x0)
    Jump("loc_1D9")

    label("loc_1D5")

    OP_70(0x2, 0x1E)

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC")
    OP_70(0x3, 0x0)
    Jump("loc_1F0")

    label("loc_1EC")

    OP_70(0x3, 0x1E)

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_1FF")

    Return()

    # Function_1_194 end

    def Function_2_200(): pass

    label("Function_2_200")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_280")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_2E5")

    label("loc_280")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2E5")

    Jump("loc_395")

    label("loc_2EA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You find a Mishy plush inside of the chest.\x01",
            "A lone tear rolls down its cheek as it is\x01",
            "disappointed in you for breaking the game.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_395")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_200 end

    def Function_3_3A1(): pass

    label("Function_3_3A1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_421")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_486")

    label("loc_421")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_486")

    Jump("loc_546")

    label("loc_48B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's bad enough I'm wasting a week inserting all\x01",
            "of these chest messages. On top of it, I have to\x01",
            "write unique ones for cheating jerks like you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_546")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3A1 end

    def Function_4_552(): pass

    label("Function_4_552")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x66, 1)"), scpexpr(EXPR_END)), "loc_5D2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_637")

    label("loc_5D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_637")

    Jump("loc_6ED")

    label("loc_63C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ironic that in a game starring police detectives\x01",
            "that uphold the law, there are players like you\x01",
            "who just want to break all the rules.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_552 end

    def Function_5_6F9(): pass

    label("Function_5_6F9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x107, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E3")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E7, 1)"), scpexpr(EXPR_END)), "loc_779")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x107, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_7DE")

    label("loc_779")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Found ",
            scpstr(SCPSTR_CODE_ITEM, 0x5E7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x01",
            "Can't hold any more, so left it behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7DE")

    Jump("loc_854")

    label("loc_7E3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You don't have to go back to the SSS\x01",
            "building but you can't stay here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_854")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6F9 end

    def Function_6_860(): pass

    label("Function_6_860")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-27000, 700, 0, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1KMidnight...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x6, 0x8)
    OP_49()
    SetChrPos(0x8, -45000, 100, -5200, 0)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x78)
    OP_11(0x22, 0x2F, 0x5B, 0xF, 0x64, 0x0)
    PlayBGM("ed7203", 0)
    Sound(496, 0, 100, 0)
    OP_68(-17000, 700, 0, 6000)
    MoveCamera(55, 27, 0, 6000)
    SetCameraDistance(30000, 6000)
    FadeToBright(2000, 0)
    PlaceName2(340, 200, "c_plac27", 0x0, 2000)

    def lambda_98B():
        OP_9E(0xFE, 0xFFFFC180, 0xFFFEA070, 0xEA60, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_98B)
    OP_6F(0x79)
    Sound(458, 0, 100, 0)
    Sleep(500)
    Sound(485, 0, 100, 0)
    Fade(500)
    EndChrThread(0x8, 0x1)
    OP_68(37200, 900, -5000, 0)
    MoveCamera(57, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x8, 18000, 0, -5000, 0)
    OP_D3(0x8, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(41700, 900, -8500, 7000)
    MoveCamera(357, 33, 0, 7000)
    SetCameraDistance(35000, 7000)

    def lambda_A37():
        OP_96(0xFE, 0x80E8, 0x64, 0xFFFFEC78, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A37)
    WaitChrThread(0x8, 1)

    def lambda_A55():
        OP_9E(0xFE, 0x80E8, 0xFFFFC568, 0x13880, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A55)
    WaitChrThread(0x8, 1)

    def lambda_A74():
        OP_9E(0xFE, 0xCD78, 0xFFFFD314, 0xFFFEC780, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A74)
    WaitChrThread(0x8, 1)

    def lambda_A93():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A93)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x8, 1)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_860 end

    SaveToFile()

Try(main)
