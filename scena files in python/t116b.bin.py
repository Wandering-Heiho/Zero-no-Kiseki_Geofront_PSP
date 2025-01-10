from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t116b.bin",                # FileName
        "t116b",                    # MapName
        "t116b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t116b",                  # 0
        "Elie",                   # 1
        "Tio",                    # 2
        "Randy",                  # 3
        "Wazy",                   # 4
        "Mafioso",                # 5
        "Mafioso",                # 6
        "KeA",                    # 7
        "KeA",                    # 8
        "SE制御",                 # 9
    ))

    AddCharChip((
        "chr/ch07700.itc",                   # 00
        "chr/ch07800.itc",                   # 01
        "chr/ch07900.itc",                   # 02
        "chr/ch08000.itc",                   # 03
        "apl/ch50363.itc",                   # 04
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

    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1600,    0,       -4699,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4000,    0,       1000,    270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4000,    0,       -1000,   270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-5120,   0,       -230,    1500,    -5120,   800,     -230,    0x007C, 0,  13, 0x0000)
    DeclActor(3780,    0,       3250,    1500,    4710,    2000,    3850,    0x007C, 0,  7,  0x0000)
    DeclActor(-1380,   0,       4940,    1500,    -1380,   1800,    4940,    0x007C, 0,  8,  0x0000)
    DeclActor(-4710,   0,       3940,    1500,    -4710,   1000,    3940,    0x007C, 0,  9,  0x0000)
    DeclActor(-4030,   0,       -3730,   1500,    -4030,   1200,    -3730,   0x007C, 0,  10, 0x0000)

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_3E4",          # 01, 1
        "Function_2_3F6",          # 02, 2
        "Function_3_49B",          # 03, 3
        "Function_4_6DB",          # 04, 4
        "Function_5_959",          # 05, 5
        "Function_6_BD7",          # 06, 6
        "Function_7_E0A",          # 07, 7
        "Function_8_E73",          # 08, 8
        "Function_9_EB7",          # 09, 9
        "Function_10_EF3",         # 0A, 10
        "Function_11_F4B",         # 0B, 11
        "Function_12_F87",         # 0C, 12
        "Function_13_14CF",        # 0D, 13
        "Function_14_38E2",        # 0E, 14
        "Function_15_38FF",        # 0F, 15
        "Function_16_391E",        # 10, 16
        "Function_17_393D",        # 11, 17
        "Function_18_3991",        # 12, 18
        "Function_19_39E5",        # 13, 19
        "Function_20_3AAF",        # 14, 20
        "Function_21_3B59",        # 15, 21
        "Function_22_3CFA",        # 16, 22
        "Function_23_3D35",        # 17, 23
        "Function_24_3E03",        # 18, 24
        "Function_25_3ED1",        # 19, 25
        "Function_26_3FA6",        # 1A, 26
        "Function_27_4021",        # 1B, 27
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_36C"),
        (1, "loc_378"),
        (2, "loc_384"),
        (3, "loc_390"),
        (4, "loc_39C"),
        (5, "loc_3A8"),
        (6, "loc_3B4"),
        (SWITCH_DEFAULT, "loc_3C0"),
    )


    label("loc_36C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_378")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_384")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_390")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_39C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3E3")

    Return()

    # Function_0_32C end

    def Function_1_3E4(): pass

    label("Function_1_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F5")
    Event(0, 12)

    label("loc_3F5")

    Return()

    # Function_1_3E4 end

    def Function_2_3F6(): pass

    label("Function_2_3F6")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    OP_66(0x0, 0x1)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_41E")
    OP_70(0x4, 0x78)
    Jump("loc_42A")

    label("loc_41E")

    SetMapObjFrame(0x4, "CA01", 0x1, 0x2)

    label("loc_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_436")
    Call(0, 26)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_43F")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Jump("loc_490")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_47D")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jump("loc_490")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_490")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    label("loc_49A")

    Return()

    # Function_2_3F6 end

    def Function_3_49B(): pass

    label("Function_3_49B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_653")

    ChrTalk(
        0xFE,
        (
            "#5308FThis room is covered with all sorts of\x01",
            "famous pieces of art...\x02\x03",
            "How exactly were they able to gather\x01",
            "all of this?\x02\x03",
            "#5303FAnd I'm still worried about the 'bomb'\x01",
            "Yin warned us about earlier...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0xFE,
        (
            "#5305FLloyd, are you all right?\x02\x03",
            "You went pale all of a sudden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5112FIt's nothing. Don't worry about me.\x02\x03",
            "#5108F(So neither Elie nor Wazy heard the\x01",
            "voice... What's going on here?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6D7")

    label("loc_653")


    ChrTalk(
        0xFE,
        (
            "#5308FI can't fathom how they were able to\x01",
            "gather together all of this.\x02\x03",
            "#5306FRevache's ties must run deeper than\x01",
            "we thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7")

    TalkEnd(0xFE)
    Return()

    # Function_3_49B end

    def Function_4_6DB(): pass

    label("Function_4_6DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")

    ChrTalk(
        0xFE,
        (
            "#5400FThe value of these exhibits is clear, but\x01",
            "many of them seem to be in poor taste.\x02\x03",
            "#5403FIt certainly suits the character of the\x01",
            "auction's sponsor.\x02\x03",
            "#5408FAt any rate, I am curious as to how we will\x01",
            "locate the 'bomb' Yin mentioned.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0xFE,
        (
            "#5400FLloyd, are you feeling okay?\x02\x03",
            "You look ill...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5112FIt's nothing. Don't worry about me.\x02\x03",
            "#5108F(So neither Tio nor Wazy heard the\x01",
            "voice... What's going on here?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_955")

    label("loc_8AC")


    ChrTalk(
        0xFE,
        (
            "#5403FNone of these exhibits stand out to me,\x01",
            "personally.\x02\x03",
            "#5408FI hoped that we would find a Mishy made\x01",
            "of gold somewhere among the exhibits...\x01",
            "How disappointing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_955")

    TalkEnd(0xFE)
    Return()

    # Function_4_6DB end

    def Function_5_959(): pass

    label("Function_5_959")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62")

    ChrTalk(
        0xFE,
        (
            "#5602FWhoa, that s'posed to be a valkyrie?\x01",
            "She's pretty cute, ain't she?\x02\x03",
            "#5606FAside from her, I don't see the appeal\x01",
            "in all this stuff.\x02\x03",
            "#5601FAnyway, we still gotta figure out what\x01",
            "we wanna do about that 'bomb' Yin\x01",
            "told us about.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0xFE,
        (
            "#5605FYou good, Lloyd?\x02\x03",
            "#5609FIf ya got a stomach ache, lemme know\x01",
            "and I'll give you a nice belly rub, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5112FI think I'll have to pass. I'm fine.\x02\x03",
            "#5108F(So neither Randy nor Wazy heard the\x01",
            "voice... What's going on here?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BD3")

    label("loc_B62")


    ChrTalk(
        0xFE,
        (
            "#5601FHe said 'bomb,' right?\x02\x03",
            "#5603FJudgin' by how he was talking, it\x01",
            "didn't sound the kind that goes boom.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD3")

    TalkEnd(0xFE)
    Return()

    # Function_5_959 end

    def Function_6_BD7(): pass

    label("Function_6_BD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6F")

    ChrTalk(
        0xFE,
        (
            "#5705FHmm. They certainly have quite the\x01",
            "event planned for tonight, don't they?\x02\x03",
            "#5704FSince I'm already breaking the rules,\x01",
            "I might as well take a souvenir with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5113FListen, you know I can't let that happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#5702FHaha. A joke, Lloyd, a joke. I'm not so\x01",
            "low that I would stoop to thievery.\x02\x03",
            "#5704FStill, you have to admit that most of\x01",
            "this stuff looks pretty fishy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E06")

    label("loc_D6F")


    ChrTalk(
        0xFE,
        (
            "#5702FJust because I'm the leader of a gang\x01",
            "doesn't mean I'm okay with theft.\x02\x03",
            "#5704FBesides, most of the things here are\x01",
            "a bit too shady for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E06")

    TalkEnd(0xFE)
    Return()

    # Function_6_BD7 end

    def Function_7_E0A(): pass

    label("Function_7_E0A")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a statue of a valkyrie, antique tableware, and\x01",
            "a variety of ominous masks.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_7_E0A end

    def Function_8_E73(): pass

    label("Function_8_E73")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a taxidermy of an endangered species.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_E73 end

    def Function_9_EB7(): pass

    label("Function_9_EB7")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A beautiful painting is on the ground.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_9_EB7 end

    def Function_10_EF3(): pass

    label("Function_10_EF3")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a pile of ancient books and an assortment of\x01",
            "other items.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_EF3 end

    def Function_11_F4B(): pass

    label("Function_11_F4B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He is completely unconscious.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_11_F4B end

    def Function_12_F87(): pass

    label("Function_12_F87")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3350, 1200, 0, 0)
    MoveCamera(43, 12, 0, 0)
    MoveCamera(46, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    SetChrPos(0x101, 6000, 0, 0, 270)
    SetChrPos(0xEF, 7350, 0, 600, 270)
    SetChrPos(0x151, 7000, 0, -600, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis065.itp")
    FadeToBright(1000, 0)
    OP_68(5940, 1200, 0, 6000)
    OP_6F(0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#3501445V#5105F#11PThis room must be...\x02",
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2044, 255, 75, 0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(
        0x102,
        (
            "#3501448V#5301F#11P...where they're storing the exhibits\x01",
            "for the auction's second half, yes.\x02\x03",
            "#3501449VThere's still so many of them, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1298")

    ChrTalk(
        0x103,
        (
            "#3501450V#5401F#11P...where they store the exhibits for\x01",
            "the second half of the auction.\x02\x03",
            "#3501451VThere is still quite a lot of them here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132E")

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(
        0x104,
        (
            "#3501452V#5601F#11P...where they're keepin' the stuff\x01",
            "for the second half of the auction.\x02\x03",
            "#3501453VStill a bunch of 'em, aren't there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132E")


    ChrTalk(
        0x151,
        (
            "#3501454V#5704F#11POnly the extremely valuable things\x01",
            "appear in the second half.\x02\x03",
            "#3501455V#5702FWe don't have too much time left.\x01",
            "Shall we split up and search?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501456V#5103F#11PLet's do it.\x02\x03",
            "#3501457V#5108FI have a feeling we're going to\x01",
            "find something in here...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 5130, 0, -200, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    RemoveParty(0x50, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_148B")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    RemoveParty(0x1, 0x0)
    Jump("loc_14BC")

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_14A6")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    RemoveParty(0x2, 0x0)
    Jump("loc_14BC")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_14BC")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    RemoveParty(0x3, 0x0)

    label("loc_14BC")

    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA6, 4)
    OP_29(0x47, 0x1, 0xE)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_F87 end

    def Function_13_14CF(): pass

    label("Function_13_14CF")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    OP_49()
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31150.itc", 0x20)
    LoadChrToIndex("chr/ch31151.itc", 0x21)
    LoadChrToIndex("chr/ch08100.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    LoadChrToIndex("apl/ch50365.itc", 0x25)
    LoadChrToIndex("apl/ch50368.itc", 0x26)
    LoadChrToIndex("apl/ch50369.itc", 0x27)
    LoadChrToIndex("chr/ch10800.itc", 0x29)
    LoadChrToIndex("chr/ch31053.itc", 0x2A)
    LoadChrToIndex("chr/ch31153.itc", 0x2B)
    LoadChrToIndex("chr/ch31052.itc", 0x2C)
    LoadChrToIndex("chr/ch31152.itc", 0x2D)
    LoadChrToIndex("chr/ch00000.itc", 0x2E)
    SoundLoad(924)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_158C")
    AddParty(0x1, 0xEF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_15BF")

    label("loc_158C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_15A8")
    AddParty(0x2, 0xEF, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Jump("loc_15BF")

    label("loc_15A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_15BF")
    AddParty(0x3, 0xEF, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_15BF")

    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(-3840, 1000, -210, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19330, 0)
    SetCameraDistance(18330, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, 700, 0, 2500, 0)
    SetChrPos(0xB, 1600, 0, -4700, 180)
    SetChrFlags(0x101, 0x8000)
    SetChrFlags(0xEF, 0x8000)
    SetChrFlags(0xB, 0x8000)
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05800.itp")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B41")
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#3501458V#5105F#11P(What's with this trunk?)\x02\x03",
            "#3501459V#5101F(This thing is massive. There has to\x01",
            "be something in it, right...?)\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(882, 0, 100, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3501460V#5000F#11P(Even if it's locked, I should be able\x01",
            "to handle it...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took out a lockpick from his detective tool kit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetCameraDistance(18030, 1500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    OP_6F(0x10)

    ChrTalk(
        0x101,
        (
            "#3501461V#5003F#11P(Good thing I decided to learn how to use\x01",
            "these during detective training...)\x02\x03",
            "#3501462V#5001F(I would have never guessed that I'd be\x01",
            "using it in a place like this, though.)\x02",
        )
    )

    CloseMessageWindow()
    Sound(833, 0, 100, 0)
    SetCameraDistance(17000, 3000)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(100)
    OP_A1(0x101, 0x3E8, 0x6, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(50)
    Sound(833, 0, 100, 0)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    OP_6F(0x10)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501463V#5002F#11P(Got it.)\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_71(0x4, 0x0, 0x28, 0x0, 0x0)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#3501464V#5005F#11PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-4500, 1000, 79640, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14860, 2500)
    SetChrPos(0x101, -3600, 0, 80000, 270)
    SetChrPos(0xEF, 700, 0, 82500, 0)
    SetChrPos(0xB, 1600, 0, 76700, 180)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrPos(0xF, -5000, -800, 79750, 90)
    OP_A7(0xE, 0x40, 0x40, 0x40, 0xFF, 0x0)
    SetChrFlags(0xF, 0x8)
    BeginChrThread(0xE, 0, 0, 14)
    OP_70(0x5, 0x28)
    OP_71(0x5, 0x28, 0x78, 0x0, 0x0)
    Sound(923, 0, 100, 0)

    def lambda_1ABE():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1ABE)
    WaitChrThread(0xE, 1)
    OP_79(0x5)
    OP_6F(0x10)
    OP_0D()
    SetChrSubChip(0x101, 0x9)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501465V#5011F#11P...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0xE, -5000, 50, 79750, 90)
    ClearChrFlags(0xE, 0x1)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x16)
    OP_68(-4260, 1000, 79730, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(9670, 0)
    SetCameraDistance(8670, 10000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sleep(2000)

    ChrTalk(
        0x101,
        (
            "#3501466V#5005F#30W#11P(Is this...a Rosenberg doll?)\x02\x03",
            "#3501467V#5008F(I know people have said they almost\x01",
            "look alive, but this is on another level...)\x02\x03",
            "#3501468V(What is going on here...?)\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    Sound(2026, 255, 70, 0)
    Sleep(300)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        "#3501469V#2S#80WMmm...      \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(150)
    EndChrThread(0xE, 0x0)
    OP_A1(0xE, 0x3E8, 0x4, 0x0, 0x5, 0x6, 0x7)
    Sound(820, 0, 100, 0)
    OP_A1(0xE, 0x3E8, 0x2, 0x9, 0xA)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x3, 0xD, 0xE, 0xF)
    BeginChrThread(0xE, 0, 0, 15)
    Sleep(1000)

    NpcTalk(
        0xF,
        "Doll?",
        "#3501470V#80W#5P...\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(2027, 255, 80, 0)
    Sleep(500)
    SetChrName("Doll?")

    AnonymousTalk(
        0xFF,
        "#3501471V#50W...Huh? Who are you?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(150)
    Fade(500)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x1)
    BeginChrThread(0xE, 0, 0, 16)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrFlags(0xE, 0x1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2000)
    SetCameraDistance(14000, 0)
    SetCameraDistance(19000, 800)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#3501472V#5007F#4S#11P#16AWHAT?!\x02",
    )

    OP_6F(0x10)
    Sleep(500)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1ED4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1ED4)

    def lambda_1EE1():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1EE1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    OP_68(-4260, 1000, 79730, 2000)
    MoveCamera(311, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(14360, 2000)

    def lambda_1F24():
        OP_95(0xFE, -3250, 0, 81490, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1F24)

    def lambda_1F3E():
        OP_95(0xFE, -2080, 0, 79080, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F3E)
    WaitChrThread(0xEF, 1)

    def lambda_1F5C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1F5C)
    WaitChrThread(0xEF, 1)

    def lambda_1F6D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F6D)
    WaitChrThread(0xB, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1FCA")

    ChrTalk(
        0x102,
        (
            "#3501473V#5301F#2PLloyd, what's wrong?\x02\x03",
            "#3501474V#5305F...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205F")

    label("loc_1FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2019")

    ChrTalk(
        0x103,
        (
            "#3501475V#5401F#2PWhat's wrong, Lloyd?\x02\x03",
            "#3501476V#5405F...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205F")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(
        0x104,
        (
            "#3501477V#5605F#2PWhat's up, dude?\x02\x03",
            "#3501478V#5601F...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_205F")


    ChrTalk(
        0xB,
        "#3501479V#5705F#12PA girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501480V#5011F#11P#30WY-You're...\x02\x03",
            "#3501481VWhy would you be...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "Girl",
        (
            "#3501482V#5805F#5P#30WWhat's wrong? Your eyes are\x01",
            "super-duper wide.\x02\x03",
            "#3501483V#5809FAhaha! You look pretty funny\x01",
            "like that, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501484V#5006F#11PI-I think it was warranted...\x02\x03",
            "#3501485V#5008FDid you get yourself stuck in there?\x01",
            "What's your name?\x02\x03",
            "#3501486V#5013FWait, do you know where your\x01",
            "mom and dad are?!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0xE,
        "Girl",
        (
            "#3501487V#5805F#5P#30W...?\x02\x03",
            "#3501488VMom? Dad?\x02\x03",
            "#3501489VWhat are those? The only thing I\x01",
            "know is that my name is KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501490V#5003F#11PAll you can remember is that your\x01",
            "name is KeA?\x02\x03",
            "#3501491V#5008FBut who are you...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_23BF")

    ChrTalk(
        0x102,
        (
            "#3501492V#5306F#2PH-Hey, Lloyd...\x02\x03",
            "#3501493V#5308FLook at her clothes. I find it hard to\x01",
            "believe that she's a guest's daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E8")

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2464")

    ChrTalk(
        0x103,
        (
            "#3501494V#5406F#2PLloyd, look.\x02\x03",
            "#3501495V#5411FJudging by her clothes, the odds that she\x01",
            "is the daughter of one of the auction's\x01",
            "guests are slim.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E8")

    label("loc_2464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_24E8")

    ChrTalk(
        0x104,
        (
            "#3501496V#5606F#2PYo, Lloyd...\x02\x03",
            "#3501497V#5601FI really doubt she's one of the guests'\x01",
            "kiddos with a getup like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E8")

    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3501498V#5006F#11PYeah, I got that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3501499V#5704F#12PAh, so that's it.\x02\x03",
            "#3501500VFriends, I think we found our mysterious bomb.\x02\x03",
            "#3501501V#5702FWe have a large suitcase with a Rosenberg\x01",
            "Studio doll inside...\x02\x03",
            "#3501502VJust imagine what would have happened if it\x01",
            "was taken to the auction and they opened its\x01",
            "lid in front of everyone...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501503V#5013F#11PYeah...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_26F2")

    ChrTalk(
        0x102,
        "#3501504V#5301F#2PI-I think I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2758")

    label("loc_26F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_271E")

    ChrTalk(
        0x103,
        "#3501505V#5401F#2PI see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2758")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2758")

    ChrTalk(
        0x104,
        "#3501506V#5603F#2PSo that's how it is, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_2758")


    NpcTalk(
        0xF,
        "KeA",
        (
            "#3501507V#5800F#5P#30WOh, your name is Lloyd?\x02\x03",
            "#3501508V#5803FLlooooyd. Lloyd...\x02\x03",
            "#3501509V#5809FHeehee. I like it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501510V#5012F#11PTh-Thanks...?\x02\x03",
            "#3501511V#5011FWait, my name isn't important!\x02\x03",
            "#3501512V#5013FKeA! Do you remember anything before\x01",
            "you were put in this suitcase?!\x02\x03",
            "#3501513VLike your home, or maybe even someone\x01",
            "you know?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(2028, 255, 85, 0)
    Sleep(300)

    NpcTalk(
        0xF,
        "KeA",
        "#3501514V#5811F#5PUmm...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    NpcTalk(
        0xF,
        "KeA",
        "#3501515V#5809F#5PNope! I can't remember a thing! Sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3501516V#5006F#11PYou've got to be kidding me...\x02\x03",
            "#3501517V#5013FStill, we can't leave you in a\x01",
            "place like this.\x02\x03",
            "#3501518VWe've got to get you out of--\x02",
        )
    )

    CloseMessageWindow()
    Sound(924, 2, 100, 0)
    Sleep(500)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3501519V#5010F#11PDamn it...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2AA8")

    ChrTalk(
        0x102,
        "#3501520V#5307F#2PThey're close!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B06")

    label("loc_2AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2AD5")

    ChrTalk(
        0x103,
        "#3501521V#5407F#2PAlarms!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B06")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2B06")

    ChrTalk(
        0x104,
        "#3501522V#5607F#2PThis ain't good!\x02",
    )

    CloseMessageWindow()

    label("loc_2B06")


    ChrTalk(
        0xB,
        "#3501523V#5703F#12POh, dear. It seems our time is up.\x02",
    )

    CloseMessageWindow()

    label("loc_2B41")

    Sound(103, 0, 70, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xC, 10000, 0, 80000, 270)
    SetChrPos(0xD, 10000, 0, 80000, 270)

    NpcTalk(
        0xC,
        "Man's Voice",
        "#3501524V#2SWhat the hell?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xC,
        "Man's Voice",
        "#3501525V#2SIntruders?! Seriously?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xD,
        "Man's Voice",
        "#3501526V#2SQuick! Check on the goods!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7509", 0)
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    OP_68(-2500, 1100, 0, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    OP_68(0, 1100, 0, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, -3250, 0, 1490, 0)
    SetChrPos(0xB, -2080, 0, -1080, 180)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0xC, 10000, 0, 0, 270)
    SetChrPos(0xD, 10000, 0, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrPos(0xE, -4850, -200, -250, 90)
    SetChrSubChip(0xE, 0x1C)
    SetChrPos(0xF, -4850, -800, -250, 90)
    OP_70(0x4, 0x78)
    SetMapObjFrame(0x4, "CA01", 0x0, 0x2)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x5)

    def lambda_2D41():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D41)

    def lambda_2D4E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2D4E)

    def lambda_2D5B():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D5B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_0D()
    BeginChrThread(0x10, 1, 0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2F0B")

    ChrTalk(
        0x104,
        "#3501527V#5611F#5PTake this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#3501535V#5707F#6PHyah!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x104, 3)
    Sleep(850)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6F(0x79)

    NpcTalk(
        0xF,
        "KeA",
        "#3501539V#5805F#5PWooooow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501532V#5001F#5PRandy, Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3501543V#5702F#11PYou're prepared for the worst,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3501534V#5601F#11PYep. If we don't start movin',\x01",
            "they'll catch us red-handed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A2")

    label("loc_2F0B")


    ChrTalk(
        0xB,
        "#3501528V#5707F#5PHyah!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 21)
    WaitChrThread(0xB, 3)
    Sleep(500)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_6F(0x79)

    NpcTalk(
        0xF,
        "KeA",
        "#3501531V#5805F#5PWooooow...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2FBB")

    ChrTalk(
        0x102,
        "#3501540V#5305F#5PH-He's fast.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FF4")

    label("loc_2FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2FF4")

    ChrTalk(
        0x103,
        "#3501541V#5405F#5PWhat incredible speed...\x02",
    )

    CloseMessageWindow()

    label("loc_2FF4")


    ChrTalk(
        0x101,
        "#3501542V#5013F#5PWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#3501533V#5706F#11PYou're prepared for the worst,\x01",
            "aren't you?\x02\x03",
            "#3501544V#5702FIf you aren't, we'll most likely\x01",
            "be overwhelmed and caught.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A2")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#3501545V#5003F#5PYou're right.\x02",
    )

    CloseMessageWindow()

    def lambda_30E4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30E4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3106")
    Sleep(100)

    def lambda_30FE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_30FE)

    label("loc_3106")

    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Sleep(300)
    OP_68(-3650, 1400, 0, 1500)
    SetCameraDistance(15060, 1500)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x7)
    Sleep(500)
    Sound(534, 0, 90, 0)
    Sound(804, 0, 100, 0)
    Fade(500)
    OP_A1(0x101, 0x7D0, 0x4, 0x7, 0x0, 0x1, 0x2)
    SetChrChipByIndex(0x101, 0x2E)
    SetChrSubChip(0x101, 0x0)
    OP_A1(0x101, 0x7D0, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4100, 1200, 0, 1500)
    SetCameraDistance(14300, 1500)
    Sleep(100)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_A1(0x101, 0x3E8, 0x4, 0x6, 0x7, 0x6, 0x5)

    ChrTalk(
        0x101,
        (
            "#3501546V#0000F#11PKeA. Will you come with us?\x02\x03",
            "#3501547VI promise that we will protect you\x01",
            "until the very end.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xF,
        "KeA",
        (
            "#3501548V#5800F#5P...?\x02\x03",
            "#3501549V#5810FI don't really know what's going on...\x01",
            "but I don't mind going with you!\x02\x03",
            "#3501550V#5809FI'm ready when you are, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501551V#0002F#11PGood girl.\x02",
    )

    CloseMessageWindow()
    OP_68(-4300, 1200, 0, 1000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-3650, 1400, 0, 1000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x101,
        "KeA",
        "#3501552V#5810F#5PHeeheehee!\x02",
    )

    CloseMessageWindow()
    OP_68(-920, 1400, 210, 1200)
    SetCameraDistance(16270, 1200)

    def lambda_3385():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3385)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_34D1")

    ChrTalk(
        0x101,
        (
            "#3501553V#0001F#5PYou two, let's change into some\x01",
            "more comfortable clothes. We'll\x01",
            "need to be as fast as possible.\x02\x03",
            "#3501554V#0003FAlso, we should contact Randy\x01",
            "and Tio, who are on standby.\x02\x03",
            "#3501561V#0007FWe're going to take this girl with\x01",
            "us and escape the mansion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3501556V#5307FUnderstood!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3744")

    label("loc_34D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_360B")

    ChrTalk(
        0x101,
        (
            "#3501553V#0001F#5PYou two, let's change into some\x01",
            "more comfortable clothes. We'll\x01",
            "need to be as fast as possible.\x02\x03",
            "#3501560V#0003FAlso, we should contact Randy\x01",
            "and Elie, who are on standby.\x02\x03",
            "#3501558V#0007FWe're going to take this girl with\x01",
            "us and escape the mansion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3501559V#5401FRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3744")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3744")

    ChrTalk(
        0x101,
        (
            "#3501553V#0001F#5PYou two, let's change into some\x01",
            "more comfortable clothes. We'll\x01",
            "need to be as fast as possible.\x02\x03",
            "#3501557V#0003FAlso, we should contact Elie\x01",
            "and Tio, who are on standby.\x02\x03",
            "#3501555V#0007FWe're going to take this girl with\x01",
            "us and escape the mansion!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3501562V#5607F#2PAye, aye!\x02",
    )

    CloseMessageWindow()

    label("loc_3744")


    ChrTalk(
        0xB,
        (
            "#3501563V#5702F#11PHaha... It looks to me like the\x01",
            "real party is just getting started.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16600, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x10, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x32, 0xFF, 0xFF)
    Call(0, 26)
    OP_32(0x4, 0x0, 0x1D)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0x439, 0xFF)
    OP_42(0x4, 0x5E7, 0xFF)
    OP_42(0x4, 0x64B, 0xFF)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x10E)
    SetChrChipPat(0x4, 0x6, 0x10E)
    AddCraft(0x4, 0x138)
    OP_42(0x4, 0x86, 0x0)
    OP_42(0x4, 0x77, 0x3)
    OP_42(0x4, 0x65, 0x4)
    OP_42(0x4, 0x6B, 0x5)
    OP_42(0x4, 0x7D, 0x6)
    OP_42(0x4, 0x71, 0x1)
    OP_42(0x4, 0x80, 0x2)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    SetChrChipPat(0x0, 0x1, 0x9A)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_388A")
    SetChrChipPat(0x1, 0x1, 0x1)
    LoadChrChipPat()
    Jump("loc_38B1")

    label("loc_388A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_38A0")
    SetChrChipPat(0x2, 0x1, 0x2)
    LoadChrChipPat()
    Jump("loc_38B1")

    label("loc_38A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_38B1")
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()

    label("loc_38B1")

    SetChrPos(0x0, -2520, 0, -200, 90)
    OP_70(0x1, 0x5)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xA6, 5)
    OP_29(0x47, 0x1, 0xF)
    OP_24(0x39C)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_14CF end

    def Function_14_38E2(): pass

    label("Function_14_38E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38FE")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_14_38E2")

    label("loc_38FE")

    Return()

    # Function_14_38E2 end

    def Function_15_38FF(): pass

    label("Function_15_38FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_391D")
    OP_A1(0xFE, 0x3E8, 0x5, 0x10, 0x11, 0x12, 0x11, 0x10)
    Sleep(3000)
    Jump("Function_15_38FF")

    label("loc_391D")

    Return()

    # Function_15_38FF end

    def Function_16_391E(): pass

    label("Function_16_391E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_393C")
    OP_A1(0xFE, 0x3E8, 0x5, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(3000)
    Jump("Function_16_391E")

    label("loc_393C")

    Return()

    # Function_16_391E end

    def Function_17_393D(): pass

    label("Function_17_393D")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_3953():
        OP_95(0xFE, 4570, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3953)

    def lambda_396D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_396D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_393D end

    def Function_18_3991(): pass

    label("Function_18_3991")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_39A7():
        OP_95(0xFE, 4570, 0, -800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39A7)

    def lambda_39C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39C1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_18_3991 end

    def Function_19_39E5(): pass

    label("Function_19_39E5")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_3A38():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A38)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    BeginChrThread(0xD, 3, 0, 24)
    Sleep(350)
    SetChrSubChip(0xFE, 0xE)
    Sleep(50)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_39E5 end

    def Function_20_3AAF(): pass

    label("Function_20_3AAF")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(1294, 255, 100, 0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_3ADC():
        OP_9D(0xFE, 0xDDE, 0x0, 0x35C, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ADC)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    OP_68(5430, 1400, 0, 200)
    SetCameraDistance(16900, 200)
    SetChrSubChip(0xFE, 0x1)
    Sound(532, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 25)
    Sleep(500)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_3AAF end

    def Function_21_3B59(): pass

    label("Function_21_3B59")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_3BAC():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BAC)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2094, 255, 100, 0)
    Sound(541, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0xE, 0xC)
    BeginChrThread(0xD, 3, 0, 24)
    OP_A1(0xFE, 0xDAC, 0x3, 0xA, 0x8, 0xC)
    Sleep(350)
    BeginChrThread(0xC, 3, 0, 22)
    OP_A1(0xFE, 0x9C4, 0x2, 0xD, 0x1)
    OP_6F(0x79)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3C31():
        OP_9D(0xFE, 0xA0A, 0x0, 0xFFFFF8B2, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C31)
    Sound(804, 0, 100, 0)
    WaitChrThread(0xFE, 1)

    def lambda_3C58():
        OP_9D(0xFE, 0xC3A, 0x0, 0xFFFFFC90, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C58)
    Sound(534, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_68(4300, 1400, 670, 150)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)
    SetChrSubChip(0xFE, 0x11)
    BeginChrThread(0xC, 3, 0, 23)
    OP_6F(0x79)
    OP_68(3130, 1400, 0, 1000)
    Sleep(500)
    OP_A1(0xFE, 0x3E8, 0x1, 0xD)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xC, 0)
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_21_3B59 end

    def Function_22_3CFA(): pass

    label("Function_22_3CFA")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x2C)
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)

    def lambda_3D1B():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D1B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_22_3CFA end

    def Function_23_3D35(): pass

    label("Function_23_3D35")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D7E():
        OP_96(0xFE, 0x1CAC, 0x3E8, 0x9B0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D7E)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_3DDA():
        OP_96(0xFE, 0x1CAC, 0x0, 0x9B0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DDA)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_23_3D35 end

    def Function_24_3E03(): pass

    label("Function_24_3E03")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E4C():
        OP_96(0xFE, 0x1E1E, 0x3E8, 0xFFFFF70E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E4C)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_3EA8():
        OP_96(0xFE, 0x1E1E, 0x0, 0xFFFFF70E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EA8)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_24_3E03 end

    def Function_25_3ED1(): pass

    label("Function_25_3ED1")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_3F21():
        OP_96(0xFE, 0x2094, 0x3E8, 0x62C, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F21)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_3F7D():
        OP_96(0xFE, 0x2094, 0x0, 0x62C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F7D)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_25_3ED1 end

    def Function_26_3FA6(): pass

    label("Function_26_3FA6")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xC, 7340, 0, 2480, 225)
    SetChrPos(0xD, 7590, 0, -1830, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_26_3FA6 end

    def Function_27_4021(): pass

    label("Function_27_4021")

    OP_25(0x39C, 0x5A)
    Sleep(1000)
    OP_25(0x39C, 0x50)
    Sleep(1000)
    OP_25(0x39C, 0x46)
    Sleep(1000)
    OP_25(0x39C, 0x3C)
    Sleep(1000)
    OP_25(0x39C, 0x32)
    Sleep(1000)
    OP_25(0x39C, 0x28)
    Sleep(1000)
    OP_25(0x39C, 0x1E)
    Sleep(1000)
    OP_25(0x39C, 0x14)
    Sleep(1000)
    OP_25(0x39C, 0xA)
    Sleep(1000)
    OP_24(0x39C)
    Return()

    # Function_27_4021 end

    SaveToFile()

Try(main)
