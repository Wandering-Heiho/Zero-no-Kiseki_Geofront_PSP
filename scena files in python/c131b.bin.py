from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c131b.bin",                # FileName
        "c131b",                    # MapName
        "c131b",                    # Location
        0x001C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c131b",                  # 0
        "Receptionist Lanfei",    # 1
        "Security Guard Bills",   # 2
        "Receptionist Corinna",   # 3
        "Zeit",                   # 4
        "Randy",                  # 5
        "Chief Guillaume",        # 6
    ))

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch27900.itc",                   # 01
        "chr/ch30500.itc",                   # 02
        "chr/ch02708.itc",                   # 03
        "chr/ch00302.itc",                   # 04
        "chr/ch26400.itc",                   # 05
        "chr/ch02702.itc",                   # 06
    ))

    DeclNpc(0,       300,     31700,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(1190,    300,     4789,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-7300,   0,       23299,   180,  277,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5710,   0,       23809,   180,  277,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(7150,    0,       20149,   270,  261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)

    DeclEvent(0x0000, 0, 15,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  6,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  8,  0x0000)
    DeclActor(7670,    0,       13360,   1500,    7670,    1400,    13360,   0x007C, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_264",          # 00, 0
        "Function_1_31C",          # 01, 1
        "Function_2_3E4",          # 02, 2
        "Function_3_3EB",          # 03, 3
        "Function_4_463",          # 04, 4
        "Function_5_563",          # 05, 5
        "Function_6_7F3",          # 06, 6
        "Function_7_7F7",          # 07, 7
        "Function_8_C58",          # 08, 8
        "Function_9_C5C",          # 09, 9
        "Function_10_112F",        # 0A, 10
        "Function_11_1254",        # 0B, 11
        "Function_12_19CE",        # 0C, 12
        "Function_13_323F",        # 0D, 13
        "Function_14_3811",        # 0E, 14
        "Function_15_38B9",        # 0F, 15
    ))


    def Function_0_264(): pass

    label("Function_0_264")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2A4"),
        (1, "loc_2B0"),
        (2, "loc_2BC"),
        (3, "loc_2C8"),
        (4, "loc_2D4"),
        (5, "loc_2E0"),
        (6, "loc_2EC"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_2A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_2F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_304")

    label("loc_31B")

    Return()

    # Function_0_264 end

    def Function_1_31C(): pass

    label("Function_1_31C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378")
    ClearScenarioFlags(0x5F, 1)
    SetChrPos(0x0, 7670, 0, 16000, 270)
    SetChrPos(0x1, 7670, 0, 16000, 270)
    SetChrPos(0x2, 7670, 0, 16000, 270)
    SetChrPos(0x3, 7670, 0, 16000, 270)
    Event(0, 2)

    label("loc_378")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0xC, 0x80)

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3D2")
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xB, -1330, 300, 17250, 135)
    SetChrPos(0xD, 1180, 300, 11650, 270)
    SetChrPos(0x9, -1440, 300, 5330, 180)

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_3E3")
    SetChrChipByIndex(0xB, 0x6)
    SetChrSubChip(0xB, 0x0)

    label("loc_3E3")

    Return()

    # Function_1_31C end

    def Function_2_3E4(): pass

    label("Function_2_3E4")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_3E4 end

    def Function_3_3EB(): pass

    label("Function_3_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B")
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_431")

    label("loc_41B")

    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_431")

    OP_1B(0x0, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44E")
    OP_1B(0x0, 0x0, 0xE)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_462")
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x0, 0x10)

    label("loc_462")

    Return()

    # Function_3_3EB end

    def Function_4_463(): pass

    label("Function_4_463")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an orbment charging station here.\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_562")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_562")

    Return()

    # Function_4_463 end

    def Function_5_563(): pass

    label("Function_5_563")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_667")

    ChrTalk(
        0xFE,
        (
            "The guys attacking the front gate seem\x01",
            "to be setting up orbal bombs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you can push 'em back, we can grab\x01",
            "the bombs and try to defuse them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't get too crazy out there, okay? I'll be\x01",
            "praying that the Goddess watches over us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75B")

    ChrTalk(
        0xFE,
        "It looks like you guys went through the wringer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, don't worry about the IBC! The security\x01",
            "department lives for this kind of stuff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as you're with us, we won't let those\x01",
            "crazies lay a finger on you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7EF")

    label("loc_75B")


    ChrTalk(
        0xFE,
        (
            "The security department has created the\x01",
            "ultimate defensive formation outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, don't you worry! Leave the building's\x01",
            "protection to us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF")

    TalkEnd(0xFE)
    Return()

    # Function_5_563 end

    def Function_6_7F3(): pass

    label("Function_6_7F3")

    Call(0, 7)
    Return()

    # Function_6_7F3 end

    def Function_7_7F7(): pass

    label("Function_7_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DD")
    TalkBegin(0x8)

    ChrTalk(
        0x8,
        (
            "Ah, Detective Bannings. I've already heard\x01",
            "everything from Mr. Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Today sure hasn't been the best, has it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006FIt's our fault that everyone here was put\x01",
            "in danger. I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no! Please don't beat yourselves up\x01",
            "over this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Special Support Section or not, Mr. Crois\x01",
            "would have never let this kind of situation\x01",
            "go unchecked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the time being, let all of us here at the\x01",
            "International Bank of Crossbell help you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Jump("loc_C57")

    label("loc_9DD")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C54")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                    # 0
            "Shop (Equipment)\x01",        # 1
            "Shop (Consumables)\x01",      # 2
            "Leave\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A64")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84")
    OP_AF(0xB8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4F")

    label("loc_A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4")
    OP_AF(0xB9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C4F")

    label("loc_AA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB8")
    Jump("loc_C4F")

    label("loc_AB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_B89")

    ChrTalk(
        0x8,
        (
            "I still can't believe something like this actually\x01",
            "happened... In the city, no less!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Be careful, everyone! I'll be praying for your\x01",
            "success every second I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4F")

    label("loc_B89")


    ChrTalk(
        0x8,
        (
            "Special Support Section or not, Mr. Crois\x01",
            "would have never let this kind of situation\x01",
            "go unchecked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For the time being, let all of us here at the\x01",
            "International Bank of Crossbell help you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4F")

    Jump("loc_9EA")

    label("loc_C54")

    TalkEnd(0x8)

    label("loc_C57")

    Return()

    # Function_7_7F7 end

    def Function_8_C58(): pass

    label("Function_8_C58")

    Call(0, 9)
    Return()

    # Function_8_C58 end

    def Function_9_C5C(): pass

    label("Function_9_C5C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5B")

    ChrTalk(
        0xA,
        (
            "It's horrifying to think that half of the\x01",
            "Guardian Force has been brainwashed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "But, I'm sure we'll make it out all right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This IS the famous IBC. Something small\x01",
            "like this won't bring us to our knees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FYou certainly sound confident.\x02\x03",
            "#0004F(Talk about a lucky break. We're able to take\x01",
            "shelter in what is most likely the most secure\x01",
            "facility in all of Crossbell.)\x02\x03",
            "#0008F(We should get all of our equipment in order\x01",
            "while things are relatively calm.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_112B")

    label("loc_E5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                     # 0
            "Trade (Accessories)\x01",      # 1
            "Trade (Quartz)\x01",           # 2
            "Trade (Other)\x01",            # 3
            "Leave\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EEC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0C")
    OP_AF(0xBA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1126")

    label("loc_F0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2C")
    OP_AF(0xBB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1126")

    label("loc_F2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4C")
    OP_AF(0xBC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1126")

    label("loc_F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F60")
    Jump("loc_1126")

    label("loc_F60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1126")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(
        0xA,
        (
            "It's crazy to think that they'd go so far as to\x01",
            "attack the bank...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I don't want to put our lives on your shoulders\x01",
            "alone, but...we're counting on you. Please do\x01",
            "your best, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1126")

    label("loc_104C")


    ChrTalk(
        0xA,
        (
            "It's horrifying to think that half of the\x01",
            "Guardian Force has been brainwashed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "But, I'm sure we'll make it out all right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This IS the famous IBC. Something small\x01",
            "like this won't bring us to our knees.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1126")

    Jump("loc_E65")

    label("loc_112B")

    TalkEnd(0xA)
    Return()

    # Function_9_C5C end

    def Function_10_112F(): pass

    label("Function_10_112F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_11A5")

    ChrTalk(
        0xB,
        "#1201FGrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FCan we leave the interior to you, Zeit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1200FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1250")

    label("loc_11A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_11FB")

    ChrTalk(
        0xB,
        "#1201FGrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0005F(Zeit seems more excited than usual.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1250")

    label("loc_11FB")


    ChrTalk(
        0xB,
        "#1200FGrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FKeep an eye out for everyone in here,\x01",
            "okay, Zeit?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1250")

    TalkEnd(0xFE)
    Return()

    # Function_10_112F end

    def Function_11_1254(): pass

    label("Function_11_1254")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12E8")
    Jump("loc_1332")

    label("loc_12E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1308")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1332")

    label("loc_1308")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1328")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1332")

    label("loc_1328")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1332")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_END)), "loc_1728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166D")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x101,
        "#0001FWhat's the situation like, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0306FOh, we're sittin' ducks.\x02\x03",
            "#0301FI wouldn't be surprised if they're thinkin' up\x01",
            "a plan to sniff us out and eat us for dinner.\x02\x03",
            "Also, I'm startin' to understand why Mr. IBC\x01",
            "loves that fancy limo of his so much. Thing\x01",
            "could probably punch through a brick wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI bet.\x02\x03",
            "#0000FSorry, Zeit. Can we count on you to guard\x01",
            "the interior?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1200FWoof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0309FHah! Reliable pup as always, eh?\x02\x03",
            "#0304FWell, we've come this far. We might as well\x01",
            "prepare for the worst now.\x02\x03",
            "#0300FKnowing how the CGF operates, they'll likely\x01",
            "try storming the gates in waves.\x02\x03",
            "So, I'd recommend chillin' out and checkin'\x01",
            "our equipment and stuff while we still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYeah. Good idea, Randy.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1723")

    label("loc_166D")


    ChrTalk(
        0xC,
        (
            "#0303FKnowing how the CGF operates, they'll likely\x01",
            "try storming the gates in waves.\x02\x03",
            "#0300FSo, I'd recommend chillin' out and check your\x01",
            "equipment and stuff while we still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1723")

    Jump("loc_19C6")

    label("loc_1728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1927")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0x101,
        "#0001FAny change, Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0304FNot yet.\x02\x03",
            "#0300FBut damn, that limo could really move. We\x01",
            "totally gave those guys the slip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FYeah, we barely got away. We should be safe\x01",
            "for now, especially with Zeit here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#1200FWoof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#0306FAh, hell. I'd be more surprised if the hound\x01",
            "WASN'T here, to be honest. Given all that's\x01",
            "happened, y'know.\x02\x03",
            "#0300FHey, check on your supplies while we still\x01",
            "can. Might not get another chance like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FGot it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE4, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0xB, 0xFF)
    Jump("loc_19C6")

    label("loc_1927")


    ChrTalk(
        0xC,
        (
            "#0303FThe IBC's security team is keepin' watch\x01",
            "outside for any of those nutjobs.\x02\x03",
            "#0300FLet's try catchin' our breath, and then we\x01",
            "can focus on our plan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1254 end

    def Function_12_19CE(): pass

    label("Function_12_19CE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ACF")

    ChrTalk(
        0xFE,
        (
            "I've been briefed already. Sounds like\x01",
            "ya got yourselves a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You folks fully prepped and ready to go?\x01",
            "Make sure ya got your gear and formation\x01",
            "down pat, y'hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hang in there, Special Support Section!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 4)
    Jump("loc_226B")

    label("loc_1ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_226B")

    ChrTalk(
        0xD,
        (
            "Hey there. One heckuva situation\x01",
            "we've got on our hands, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 4)), scpexpr(EXPR_END)), "loc_1CC8")

    ChrTalk(
        0x101,
        (
            "#0005FGuillaume...?\x02\x03",
            "#0000FOh, that's right. You said you were stopping\x01",
            "by the Epstein Foundation's branch here in\x01",
            "the IBC today, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sure did. Was visitin' the branch over\x01",
            "on the fifth floor for that very reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Old Roberts and I were deep in discussion\x01",
            "over a new idea he had for an invention...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Never in all my years did I expect\x01",
            "somethin' this nutty to happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E54")

    label("loc_1CC8")


    ChrTalk(
        0x101,
        (
            "#0005FThe owner of that factory downtown...?\x02\x03",
            "#0005FWhat brought you here today, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I had to drag my ol' keister down to the\x01",
            "foundation branch here for some business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Old Roberts and I were deep in discussion\x01",
            "over a new idea he had for an invention,\x01",
            "but I hadn't realized how late it had gotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Gotta say, never in all my years did I expect\x01",
            "somethin' this nutty to happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E54")


    ChrTalk(
        0x101,
        (
            "#0003FI'm sorry, sir. This wouldn't have happened\x01",
            "if not for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Hahaha! Relax, kid. No one's blamin' you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And besides, I'm pretty sure this old geezer\x01",
            "can help you with this mighty pickle we've\x01",
            "got on our hands. You can count on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Got a whole workshop setup for ya here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "From orbment modification to weapon\x01",
            "reinforcement, you bet you can count\x01",
            "on me for all your needs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FThank you, sir! We will definitely take you up on\x01",
            "that offer.\x02\x03",
            "#0003F(Yeah... In addition to our equipment, we should\x01",
            "take a look at how our orbments are doing, too.)\x02\x03",
            "(After all, we have no way of knowing what's\x01",
            "going to happen next.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2258")
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By talking to Guillaume and selecting 'Customize,'\x01",
            "a list of possible upgrades will be displayed. If you\x01",
            "have the necessary materials, you can create it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Weapons and armor made by customizing are\x01",
            "stronger, cannot be bought at weapons shops,\x01",
            "and special effects may be added.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters may drop the necessary materials.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    label("loc_2258")

    SetScenarioFlags(0xEE, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xD)
    Return()

    label("loc_226B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26A4")

    ChrTalk(
        0xFE,
        (
            "Holy City of Arteria! How'd you get\x01",
            "yer hands on some Zemurian Ore?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ya got no idea what kinda treasure\x01",
            "yer holdin', kid! Where the hell\x01",
            "didja manage to find that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FUmmm... Is this chunk of rock really\x01",
            "that special?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is it ever?! That thing you're holdin' there is said\x01",
            "to be a relic of an ancient civilization! The best\x01",
            "weapons 'round are made outta that thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And this is just outta the rumor mill...but\x01",
            "apparently the foundation's figured out\x01",
            "how to refine that thing as of last year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you were to make a weapon outta this...\x01",
            "I'm sure your power would increase tenfold!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FS-So it's some type of ore, then?\x02\x03",
            "#0003FAnd it makes the best weapons? Given the\x01",
            "situation, I certainly wouldn't refuse\x01",
            "that kind of power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yer in luck, my friend! I just so happened\x01",
            "to draft up some blueprints for new\x01",
            "weapons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just say the word, and that Zemurian Ore's\x01",
            "gonna turn into some beefy armaments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figure one ore's good enough to make\x01",
            "a single weapon...probably. Anyway, ya\x01",
            "wanna give it a shot?!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 7)
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_26A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D87")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D82")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Talk")
    MenuCmd(1, 0, "Upgrade/Synthesize (Orbments)")
    MenuCmd(1, 0, "Customize (Equipment)")
    MenuCmd(1, 0, "Upgrade Staff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2780")
    MenuCmd(1, 0, "Craft Ultimate Weapon")

    label("loc_2780")

    MenuCmd(1, 0, "Leave")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27B3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_27B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27D9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_27D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "Oh, you folks heard about upgrading slots yet?\x02",
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regarding slot upgrading:\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you select [SLOT] and choose a slot that is\x01",
            "already opened, you can upgrade its level.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In addition to gaining the ability to set high-level\x01",
            "quartz, your maximum EP is also raised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_2937")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D7D")

    label("loc_2948")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2968")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D7D")

    label("loc_2968")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B84")

    ChrTalk(
        0xD,
        "You wanna upgrade that orbal staff of yours?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm ready when you folks are.\x01",
            "Wanna use the materials and strengthen it?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "[Yes]\x01",         # 0
            "[Cancel]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF8")

    ChrTalk(
        0x101,
        "#0000FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sounds good. Wanna do me a solid and\x01",
            "call old Roberts over for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FNo problem.\x01",
            "Coincidentally, I think he was\x01",
            "going down to talk to Tio.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 1)
    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_2AF8")


    ChrTalk(
        0xD,
        (
            "Oh, sure. Just let me know if you're itchin'\x01",
            "for an upgrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I'm all prepped and ready to go. Just gimme the word.\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D7D")

    label("loc_2B84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BAF")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BAA")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_2BAA")

    Jump("loc_2D7D")

    label("loc_2BAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BC3")
    Jump("loc_2D7D")

    label("loc_2BC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_2C97")

    ChrTalk(
        0xFE,
        (
            "I've been briefed already. Sounds like\x01",
            "ya got yourselves a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You folks fully prepped and ready to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hang in there, Special Support Section!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D7D")

    label("loc_2C97")


    ChrTalk(
        0xD,
        (
            "There just so happens to be a branch of the\x01",
            "Epstein Foundation up on the fifth floor.\x01",
            "They got some real nice facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just say the word if ya ever need some\x01",
            "help, folks. This geezer will give ya\x01",
            "everything he's got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7D")

    Jump("loc_26E8")

    label("loc_2D82")

    Jump("loc_323B")

    label("loc_2D87")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_323B")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Talk")
    MenuCmd(1, 0, "Upgrade/Synthesize (Orbments)")
    MenuCmd(1, 0, "Customize (Equipment)")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E18")
    MenuCmd(1, 0, "Craft Ultimate Weapon")

    label("loc_2E18")

    MenuCmd(1, 0, "Leave")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E4B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E71")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2E71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "Oh, you folks heard about upgrading slots yet?\x02",
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Regarding slot upgrading:\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you select [SLOT] and choose a slot that is\x01",
            "already opened, you can upgrade its level.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In addition to gaining the ability to set high-level\x01",
            "quartz, your maximum EP is also raised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_2FCF")

    OP_AF(0xAF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3236")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3000")
    OP_AF(0xAE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3236")

    label("loc_3000")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3026")
    Call(0, 13)
    TalkEnd(0xD)
    Return()

    label("loc_3026")

    Jump("loc_3236")

    label("loc_302B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_303F")
    Jump("loc_3236")

    label("loc_303F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3236")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_END)), "loc_314E")

    ChrTalk(
        0xFE,
        (
            "I've been briefed already. Sounds like\x01",
            "ya got yourselves a bit of a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You folks fully prepped and ready to go?\x01",
            "Make sure ya got your gear and formation\x01",
            "down pat, y'hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hang in there, Special Support Section!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_314E")


    ChrTalk(
        0xD,
        (
            "There just so happens to be a branch of the\x01",
            "Epstein Foundation up on the fifth floor.\x01",
            "They got some real nice facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just gimme a holler if ya ever need some\x01",
            "help, folks. This geezer will give ya\x01",
            "everything he's got!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    Jump("loc_2D91")

    label("loc_323B")

    TalkEnd(0xD)
    Return()

    # Function_12_19CE end

    def Function_13_323F(): pass

    label("Function_13_323F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "[A weapon for Lloyd]\x01",      # 0
            "[A weapon for Elie]\x01",       # 1
            "[A weapon for Tio]\x01",        # 2
            "[A weapon for Randy]\x01",      # 3
            "[Cancel]\x01",                  # 4
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_377E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_335B")

    ChrTalk(
        0xFE,
        "Time to put my back into it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna craft a masterpiece outta this\x01",
            "Zemurian Ore, just you wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3397")

    label("loc_335B")


    ChrTalk(
        0xFE,
        (
            "Just a little more...keep waiting...\x01",
            "keep...waiting...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3397")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_4B(0xD, 0xFF)
    OP_68(6020, 1500, 19170, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17100, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0x101, 5670, 0, 19810, 90)
    OP_93(0xD, 0x10E, 0x0)
    Sleep(1500)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "#2P#40WNow if I just adjust it like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2P...and... It's complete!\x01",
            "Take a gander at this!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x3F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x3F4, 1)
    Jump("loc_353F")

    label("loc_34B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x408),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x408, 1)
    Jump("loc_353F")

    label("loc_34E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3514")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x41C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x41C, 1)
    Jump("loc_353F")

    label("loc_3514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353F")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x430),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber(0x430, 1)

    label("loc_353F")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x396, 1)
    OP_DE(0x18, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36BA")

    ChrTalk(
        0x101,
        (
            "#0005FWhoa. You really did it.\x02\x03",
            "#0005FYou're a lifesaver. Thank you so much, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#2PNo problem, kid. I should be the one thankin' ya.\x01",
            "Dunno what a geezer like myself did to deserve\x01",
            "workin' with this, but it's been a dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2PIf ya need any more help, just say the word!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FWe will. Thanks for everything, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_376A")

    label("loc_36BA")


    ChrTalk(
        0xFE,
        (
            "#2PYou're honestly a gift from the Goddess\x01",
            "right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#2PAll righty, then. Just keep hangin' in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FDon't worry. We'll put your work to good\x01",
            "use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376A")

    OP_5A()
    SetScenarioFlags(0xF0, 0)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xA, 0x8000)
    EventEnd(0x5)
    Jump("loc_3810")

    label("loc_377E")


    ChrTalk(
        0xFE,
        (
            "Sounds like a plan. Just gimme a holler\x01",
            "if ya need any more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as this old geezer can do it,\x01",
            "I'll definitely make it happen!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3810")

    Return()

    # Function_13_323F end

    def Function_14_3811(): pass

    label("Function_14_3811")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FThe security guards are watching\x01",
            "the front gate...\x02\x03",
            "#0001FLet's restock our supplies and check on\x01",
            "our equipment while we have time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -460, 300, 4950, 0)
    EventEnd(0x4)
    Return()

    # Function_14_3811 end

    def Function_15_38B9(): pass

    label("Function_15_38B9")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FOur goal is to remove the orbal bombs at the front\x01",
            "gate and brave the Guardian Force's onslaught.\x02\x03",
            "#0001FIt's now or never. Everyone, to the front gate!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    EventEnd(0x4)
    Return()

    # Function_15_38B9 end

    SaveToFile()

Try(main)
