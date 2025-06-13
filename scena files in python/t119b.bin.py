from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t119b.bin",                # FileName
        "t119b",                    # MapName
        "t119b",                    # Location
        0x0094,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 148, 0, 1, 0, 2],
    )

    BuildStringList((
        "t119b",                  # 0
        "Nikita",                 # 1
    ))

    AddCharChip((
        "chr/ch26800.itc",                   # 00
    ))

    DeclNpc(67760,   0,       17290,   0,    401,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)

    ScpFunction((
        "Function_0_E4",           # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1DC",          # 02, 2
        "Function_3_27B",          # 03, 3
        "Function_4_403",          # 04, 4
        "Function_5_4B9",          # 05, 5
        "Function_6_6F9",          # 06, 6
        "Function_7_7AF",          # 07, 7
        "Function_8_A6F",          # 08, 8
        "Function_9_B1E",          # 09, 9
        "Function_10_BA6",         # 0A, 10
        "Function_11_C0F",         # 0B, 11
    ))


    def Function_0_E4(): pass

    label("Function_0_E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_124"),
        (1, "loc_130"),
        (2, "loc_13C"),
        (3, "loc_148"),
        (4, "loc_154"),
        (5, "loc_160"),
        (6, "loc_16C"),
        (SWITCH_DEFAULT, "loc_178"),
    )


    label("loc_124")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_130")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_13C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_148")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_154")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_160")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_16C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_178")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_184")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_19B")

    Return()

    # Function_0_E4 end

    def Function_1_19C(): pass

    label("Function_1_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1B0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_1BF")

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1BF")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1CD")
    Jump("loc_1DB")

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)

    label("loc_1DB")

    Return()

    # Function_1_19C end

    def Function_2_1DC(): pass

    label("Function_2_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1E5")

    label("loc_1E5")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD")
    OP_1B(0x2, 0x0, 0x8)

    label("loc_1FD")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21A")
    OP_1B(0x0, 0x0, 0x4)
    Jump("loc_22D")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D")
    OP_1B(0x0, 0x0, 0xA)

    label("loc_22D")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F")
    OP_1B(0x1, 0x0, 0x6)
    Jump("loc_262")

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_262")
    OP_1B(0x1, 0x0, 0xB)

    label("loc_262")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27A")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_27A")

    Return()

    # Function_2_1DC end

    def Function_3_27B(): pass

    label("Function_3_27B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_358")

    ChrTalk(
        0xFE,
        (
            "James told me he would win me jewelry\x01",
            "at the auction, but then he went and\x01",
            "crushed my hopes and dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have to find another lonely\x01",
            "guest while I still can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* Typical men...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3FF")

    label("loc_358")


    ChrTalk(
        0xFE,
        (
            "If James actually used his head, this\x01",
            "whole mess could have been avoided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I better search for another\x01",
            "unaccompanied guest before the\x01",
            "auction starts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF")

    TalkEnd(0xFE)
    Return()

    # Function_3_27B end

    def Function_4_403(): pass

    label("Function_4_403")

    EventBegin(0x0)
    Fade(1000)
    OP_68(57500, 1400, 16000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, 57310, 0, 16379, 270)
    SetChrPos(0xEF, 58340, 0, 15070, 270)
    SetChrPos(0x105, 59150, 0, 16640, 270)
    SetChrPos(0x133, 61160, 0, 16030, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_403 end

    def Function_5_4B9(): pass

    label("Function_5_4B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(57500, 1400, 16000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, 57310, 0, 16379, 270)
    SetChrPos(0xEF, 58340, 0, 15070, 270)
    SetChrPos(0x105, 59150, 0, 16640, 270)
    SetChrPos(0x133, 61160, 0, 16030, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#3501591V#0010F#11P(Not good...)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        "#3501592V#5805F#5P(That guy is suuuuper big.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_624")

    ChrTalk(
        0x102,
        (
            "#3501593V#0101F#11P(There's no way we'll be able to escape\x01",
            "through the front door while he's there...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CC")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_67D")

    ChrTalk(
        0x103,
        (
            "#3501594V#0206F#11P(Escape through the front door is\x01",
            "now a negative.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CC")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(
        0x104,
        (
            "#3501595V#0306F#11P(Damn. Looks like the front door\x01",
            "is a no-go.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CC")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 56900, 0, 16200, 270)
    SetScenarioFlags(0xA6, 7)
    OP_29(0x47, 0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_4B9 end

    def Function_6_6F9(): pass

    label("Function_6_6F9")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57500, 1400, 16000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, -57310, 0, 16379, 90)
    SetChrPos(0xEF, -58340, 0, 15070, 90)
    SetChrPos(0x105, -59150, 0, 16640, 90)
    SetChrPos(0x133, -61160, 0, 16030, 90)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 3)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_6F9 end

    def Function_7_7AF(): pass

    label("Function_7_7AF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(-57500, 1400, 16000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, -57310, 0, 16379, 90)
    SetChrPos(0xEF, -58340, 0, 15070, 90)
    SetChrPos(0x105, -59150, 0, 16640, 90)
    SetChrPos(0x133, -61160, 0, 16030, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#3501609V#0010F#5P(The front door isn't an option\x01",
            "with those two there.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "KeA",
        (
            "#3501610V#5805F#6P(Look at him, Lloyd.)\x02\x03",
            "#3501611V#5809F(That old man is as round as a ball!\x01",
            "Heehee, he looks so silly!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3501612V#0006F#5P*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#3501613V#0409F#5P(Haha! I think I like this one!)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_9A7")

    ChrTalk(
        0x102,
        "#3501614V#0102F#5P(Well, she's not wrong.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A48")

    label("loc_9A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_9F4")

    ChrTalk(
        0x103,
        "#3501615V#0204F#5P(She is objectively correct, you know.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_A48")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_A48")

    ChrTalk(
        0x104,
        (
            "#3501616V#0309F#5P(Haha. He's definitely a big boy, that's\x01",
            "for sure.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A48")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56900, 0, 16200, 90)
    SetScenarioFlags(0xA7, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_7_7AF end

    def Function_8_A6F(): pass

    label("Function_8_A6F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0003FThere's no time to waste. We have\x01",
            "to get this girl to safety, ASAP.\x02\x03",
            "#0001FThe entrance is straight ahead. Let's\x01",
            "try to make our exit there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 64000, 2000, 25100, 180)
    EventEnd(0x4)
    Return()

    # Function_8_A6F end

    def Function_9_B1E(): pass

    label("Function_9_B1E")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0004FThanks to Lechter, the front door is\x01",
            "short on guards...\x02\x03",
            "#0000FThis is our chance! It's now or never!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -64000, 2000, 25100, 180)
    EventEnd(0x4)
    Return()

    # Function_9_B1E end

    def Function_10_BA6(): pass

    label("Function_10_BA6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0013F(The entrance is too risky. We'll have\x01",
            "to find another way out now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 57500, 0, 16000, 90)
    EventEnd(0x4)
    Return()

    # Function_10_BA6 end

    def Function_11_C0F(): pass

    label("Function_11_C0F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#0013F(With both Don Marconi and\x01",
            "Garcia at the front door, we'll have\x01",
            "to find another exit to take...)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -57500, 0, 16000, 270)
    EventEnd(0x4)
    Return()

    # Function_11_C0F end

    SaveToFile()

Try(main)
