from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c047b.bin",                # FileName
        "c047b",                    # MapName
        "c047b",                    # Location
        0x0025,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c047b",                  # 0
        "Proprietor Drake",       # 1
        "Cherry",                 # 2
        "Galetti",                # 3
        "Elinda",                 # 4
        "Raytarossa",             # 5
        "Old Man Rick",           # 6
    ))

    AddCharChip((
        "chr/ch20002.itc",                   # 00
        "chr/ch25800.itc",                   # 01
        "chr/ch25900.itc",                   # 02
        "chr/ch27000.itc",                   # 03
        "chr/ch27100.itc",                   # 04
        "chr/ch33302.itc",                   # 05
    ))

    DeclNpc(-899,    4000,    21299,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6199,    -1000,   8000,    270,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       -1000,   13649,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-6500,   -1000,   6000,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1350,    -949,    11500,   0,    261,  0x0, 0,   5,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(6699,    4269,    15750,   90,   261,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)

    DeclActor(-900,    4000,    20000,   2000,    -900,    5500,    21300,   0x007E, 0,  3,  0x0000)
    DeclActor(5240,    -1000,   8000,    1200,    6200,    500,     8000,    0x007E, 0,  5,  0x0000)
    DeclActor(-920,    -1000,   12050,   1700,    0,       500,     13650,   0x007E, 0,  7,  0x0000)
    DeclActor(-4500,   -1000,   6000,    1500,    -6500,   500,     6000,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_218",          # 00, 0
        "Function_1_2D0",          # 01, 1
        "Function_2_2D1",          # 02, 2
        "Function_3_2FB",          # 03, 3
        "Function_4_2FF",          # 04, 4
        "Function_5_625",          # 05, 5
        "Function_6_629",          # 06, 6
        "Function_7_85A",          # 07, 7
        "Function_8_85E",          # 08, 8
        "Function_9_999",          # 09, 9
        "Function_10_99D",         # 0A, 10
        "Function_11_A22",         # 0B, 11
        "Function_12_C37",         # 0C, 12
    ))


    def Function_0_218(): pass

    label("Function_0_218")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_258"),
        (1, "loc_264"),
        (2, "loc_270"),
        (3, "loc_27C"),
        (4, "loc_288"),
        (5, "loc_294"),
        (6, "loc_2A0"),
        (SWITCH_DEFAULT, "loc_2AC"),
    )


    label("loc_258")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_264")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_270")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_27C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_288")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_294")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2B8")

    label("loc_2CF")

    Return()

    # Function_0_218 end

    def Function_1_2D0(): pass

    label("Function_1_2D0")

    Return()

    # Function_1_2D0 end

    def Function_2_2D1(): pass

    label("Function_2_2D1")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -6000, -1000, 16000, 5000, 5000, 0)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    Return()

    # Function_2_2D1 end

    def Function_3_2FB(): pass

    label("Function_3_2FB")

    Call(0, 4)
    Return()

    # Function_3_2FB end

    def Function_4_2FF(): pass

    label("Function_4_2FF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_541")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A8")

    ChrTalk(
        0x8,
        (
            "I'm assuming you've all heard about\x01",
            "Gantz's unusual skill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can't even begin to imagine where he\x01",
            "forged his unbelievable intuition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C")

    label("loc_3A8")


    ChrTalk(
        0x8,
        (
            "Oh, you're back. How'd it go?\x01",
            "Were you able to meet with Gantz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FYeah, we did... Things didn't go as\x01",
            "expected, but it all worked out in\x01",
            "the end.\x02\x03",
            "#0000FWe appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0301FHis godlike gamblin' skills have\x01",
            "me scratching my head.\x02\x03",
            "#0306FThis ain't fair! Why haven't my powers\x01",
            "awakened from deep within?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FHow are you still hung up on that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211F...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_53C")

    Jump("loc_621")

    label("loc_541")


    ChrTalk(
        0x8,
        (
            "There's no mistaking it. Gantz certainly\x01",
            "is a frequent guest to this establishment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He's supposedly staying in the VIP room\x01",
            "on the top floor of Hotel Millenium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Why not go and pay him a visit if you need him?\x02",
    )

    CloseMessageWindow()

    label("loc_621")

    TalkEnd(0x8)
    Return()

    # Function_4_2FF end

    def Function_5_625(): pass

    label("Function_5_625")

    Call(0, 6)
    Return()

    # Function_5_625 end

    def Function_6_629(): pass

    label("Function_6_629")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_636")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_856")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",          # 0
            "Exchange\x01",      # 1
            "Leave\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_68B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    SetScenarioFlags(0x6D, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6AD")
    OP_AF(0x3F)
    Jump("loc_6AF")

    label("loc_6AD")

    OP_AF(0x3E)

    label("loc_6AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_851")

    label("loc_6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D2")
    Jump("loc_851")

    label("loc_6D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_76D")

    ChrTalk(
        0x9,
        (
            "Gantz has been coming here all\x01",
            "the time these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's almost as if he's a different person\x01",
            "altogether.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_851")

    label("loc_76D")


    ChrTalk(
        0x9,
        (
            "He's been acting sorta odd. Something\x01",
            "about him feels...different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Those wins are getting to his head... His ego\x01",
            "must be as big as an inflated Mishy balloon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I feel like he's become a totally different person.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_851")

    Jump("loc_636")

    label("loc_856")

    TalkEnd(0x9)
    Return()

    # Function_6_629 end

    def Function_7_85A(): pass

    label("Function_7_85A")

    Call(0, 8)
    Return()

    # Function_7_85A end

    def Function_8_85E(): pass

    label("Function_8_85E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8C8")

    ChrTalk(
        0xA,
        (
            "He used to pull off a full house at best,\x01",
            "so how the hell can he be that lucky now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_995")

    label("loc_8C8")


    ChrTalk(
        0xA,
        (
            "Gantz has been drawing nothing but\x01",
            "incredible hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I've watched him play, so I can pretty\x01",
            "confidently say that he isn't cheating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So how the hell is he that lucky?\x01",
            "I just don't get it!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_995")

    TalkEnd(0xA)
    Return()

    # Function_8_85E end

    def Function_9_999(): pass

    label("Function_9_999")

    Call(0, 10)
    Return()

    # Function_9_999 end

    def Function_10_99D(): pass

    label("Function_10_99D")

    TalkBegin(0xB)

    ChrTalk(
        0xB,
        (
            "Gantz's intuition and insight are beyond\x01",
            "comprehension...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've never experienced so many crushing\x01",
            "defeats in a row.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_10_99D end

    def Function_11_A22(): pass

    label("Function_11_A22")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB6")
    Jump("loc_B00")

    label("loc_AB6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B00")

    label("loc_AD6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B00")

    label("loc_AF6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B00")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9B")

    ChrTalk(
        0xC,
        "I, too, have foolishly challenged him before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I didn't sense that he was the least bit\x01",
            "inept.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C2F")

    label("loc_B9B")


    ChrTalk(
        0xC,
        (
            "I heard that Gantz used to be\x01",
            "a third-rate gambler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Is that really the truth, though? I failed to\x01",
            "get that impression from him at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_C2F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_A22 end

    def Function_12_C37(): pass

    label("Function_12_C37")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCB")
    Jump("loc_D15")

    label("loc_CCB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D15")

    label("loc_CEB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D0B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D15")

    label("loc_D0B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D15")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(
        0xD,
        (
            "It's dark out already? I'm having\x01",
            "such a good time, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I don't want to go home! I'm still on\x01",
            "a gambling high!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_C37 end

    SaveToFile()

Try(main)
