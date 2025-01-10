from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c042c.bin",                # FileName
        "c042c",                    # MapName
        "c042c",                    # Location
        0x0023,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 35, 0, 2, 0, 3],
    )

    BuildStringList((
        "c042c",                  # 0
        "Troupe Leader Avan",     # 1
        "Ilya",                   # 2
        "Rixia",                  # 3
        "Nikolai",                # 4
        "Heinz",                  # 5
        "Sully",                  # 6
    ))

    AddCharChip((
        "chr/ch05100.itc",                   # 00
        "chr/ch05200.itc",                   # 01
        "chr/ch27500.itc",                   # 02
        "chr/ch24200.itc",                   # 03
        "chr/ch36800.itc",                   # 04
        "chr/ch10100.itc",                   # 05
    ))

    DeclNpc(-1480,   0,       15689,   45,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-209,    0,       15550,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1330,    0,       15699,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-68150,  0,       2150,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-66489,  0,       7329,    0,    261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(64569,   0,       4590,    315,  389,  0x0, 0,   5,   0,   0,   1,   0,   9,   255,  0)

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_244",          # 01, 1
        "Function_2_26F",          # 02, 2
        "Function_3_330",          # 03, 3
        "Function_4_331",          # 04, 4
        "Function_5_8CF",          # 05, 5
        "Function_6_BC3",          # 06, 6
        "Function_7_CE7",          # 07, 7
        "Function_8_DF8",          # 08, 8
        "Function_9_F86",          # 09, 9
        "Function_10_12C0",        # 0A, 10
        "Function_11_1408",        # 0B, 11
        "Function_12_3447",        # 0C, 12
        "Function_13_3D83",        # 0D, 13
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1CC"),
        (1, "loc_1D8"),
        (2, "loc_1E4"),
        (3, "loc_1F0"),
        (4, "loc_1FC"),
        (5, "loc_208"),
        (6, "loc_214"),
        (SWITCH_DEFAULT, "loc_220"),
    )


    label("loc_1CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_1FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_208")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_220")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_22C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_243")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_22C")

    label("loc_243")

    Return()

    # Function_0_18C end

    def Function_1_244(): pass

    label("Function_1_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26E")
    OP_94(0xFE, 0xF4D8, 0x532, 0x1054A, 0x15AE, 0x3E8)
    Sleep(300)
    Jump("Function_1_244")

    label("loc_26E")

    Return()

    # Function_1_244 end

    def Function_2_26F(): pass

    label("Function_2_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2B3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, -66690, 0, 4990, 0)
    SetChrPos(0xC, -66690, 0, 6530, 180)
    Jump("loc_32F")

    label("loc_2B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_32F")

    label("loc_2D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_30E")
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_32F")

    label("loc_30E")

    BeginChrThread(0x9, 2, 0, 13)
    BeginChrThread(0xA, 2, 0, 13)
    BeginChrThread(0x8, 2, 0, 13)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_32F")

    Return()

    # Function_2_26F end

    def Function_3_330(): pass

    label("Function_3_330")

    Return()

    # Function_3_330 end

    def Function_4_331(): pass

    label("Function_4_331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    Call(0, 11)
    Return()

    label("loc_35A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E1")

    ChrTalk(
        0x8,
        (
            "Considering how busy the crowds are,\x01",
            "I can understand how he got lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I pray he is quickly found.\x02",
    )

    CloseMessageWindow()
    Jump("loc_48E")

    label("loc_3E1")


    ChrTalk(
        0x8,
        (
            "Oh, Lloyd?\x01",
            "A little boy has gone missing, am I correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I would imagine the crowd from the parade\x01",
            "isn't doing you any favors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I hope you find him quickly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_48E")

    Jump("loc_8CB")

    label("loc_493")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_8CB")

    label("loc_4A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_7BC")

    ChrTalk(
        0x8,
        "Ilya's performances will resume tomorrow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We couldn't have asked for a worse time\x01",
            "for a stalker to start bothering her. I must\x01",
            "take action immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Could you please help us find this\x01",
            "stalker right away?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69F")
    TalkEnd(0xFE)
    EventBegin(0x0)
    StopBGM(0x5DC)
    Fade(500)
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    SetChrPos(0x8, -1480, 0, 15690, 180)
    SetChrPos(0xA, 1330, 0, 15700, 225)
    OP_93(0x9, 0xB4, 0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_0D()
    OP_29(0x1D, 0x1, 0x1)
    Call(0, 12)
    Return()

    label("loc_69F")


    ChrTalk(
        0x101,
        (
            "#0006FI'm sorry, sir. We still have a lot of\x01",
            "duties to tend to. We'll need to\x01",
            "take care of them first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ah, that's unfortunate. I suppose I\x01",
            "can't do much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope you'll find it in your heart to help\x01",
            "us catch this stalker if your schedule\x01",
            "becomes more free.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CB")

    label("loc_7BC")


    ChrTalk(
        0xFE,
        (
            "Well, it's a better plan than I could\x01",
            "come up with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I'm impressed Rixia could so readily\x01",
            "follow Ilya's ridiculous orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1700FHahaha. What'd you expect? It's Rixia!\x02\x03",
            "#1709FWhat'd I tell ya? These eyes never\x01",
            "betray me. I know talent when I see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CB")

    TalkEnd(0xFE)
    Return()

    # Function_4_331 end

    def Function_5_8CF(): pass

    label("Function_5_8CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F8")
    Call(0, 11)
    Return()

    label("loc_8F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_AA0")

    ChrTalk(
        0x9,
        (
            "#1704FPerhaps we should keep practicing.\x01",
            "Y'know what they say, there's no\x01",
            "time like the present.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0xA,
        "#1801FPlease wait a moment, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I agree! We must postpone for now.\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    ChrTalk(
        0x9,
        (
            "#1706FPshaw! What are you shaking in your boots for?\x01",
            "We gotta work off that boredom SOMEHOW.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(We probably should have accepted this\x01",
            "request more quickly.)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x1F4)
    OP_93(0x8, 0x87, 0x1F4)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    Jump("loc_BBF")

    label("loc_AA0")


    ChrTalk(
        0x9,
        (
            "#1700FOkay, the timing on the entrance for this\x01",
            "next scene should be a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#1800FRight. That'll make it easier for me to\x01",
            "join in and keep on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F(Looks like they're discussing the play.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100F(This should be their day off, yet they're\x01",
            "still going at it.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBF")

    TalkEnd(0xFE)
    Return()

    # Function_5_8CF end

    def Function_6_BC3(): pass

    label("Function_6_BC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEC")
    Call(0, 11)
    Return()

    label("loc_BEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_CE0")

    ChrTalk(
        0xA,
        (
            "#1803FI apologize for Ilya's complete and\x01",
            "utter lack of interest.\x02\x03",
            "#1808FI'm busy during the day, so I can't\x01",
            "deal with it, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#1801FA-Anyway... I hope you can lend\x01",
            "us your aid, everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE3")

    label("loc_CE0")

    Call(0, 5)

    label("loc_CE3")

    TalkEnd(0xFE)
    Return()

    # Function_6_BC3 end

    def Function_7_CE7(): pass

    label("Function_7_CE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D7E")

    ChrTalk(
        0xB,
        (
            "Sorry, but I don't even bother looking at the\x01",
            "audience when I'm performing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You might have better luck asking\x01",
            "Ilya or Plie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF4")

    label("loc_D7E")


    ChrTalk(
        0xB,
        "Hmm? A little boy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way... I'm so frazzled when I perform\x01",
            "that I don't bother looking at the audience.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_DF4")

    TalkEnd(0xFE)
    Return()

    # Function_7_CE7 end

    def Function_8_DF8(): pass

    label("Function_8_DF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_EEF")

    ChrTalk(
        0xC,
        (
            "Considering he's a child, I doubt he\x01",
            "made his way back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Operating the stage equipment is delicate,\x01",
            "so precision is key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As you might guess, I'm paying close attention\x01",
            "to my surroundings during the performance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F82")

    label("loc_EEF")


    ChrTalk(
        0xC,
        (
            "Now that we've got a day off, I'm going to\x01",
            "do a thorough inspection of the equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Doubt I'd have much time to get\x01",
            "it done otherwise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F82")

    TalkEnd(0xFE)
    Return()

    # Function_8_DF8 end

    def Function_9_F86(): pass

    label("Function_9_F86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1203")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1175")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1067")

    ChrTalk(
        0xFE,
        "O-Oh, you're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHey, Sully. How are you adjusting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sh-Sh-Shut your mouth.\x01",
            "Go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm in the middle of something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHaha. Such a stubborn girl.\x02",
    )

    CloseMessageWindow()
    Jump("loc_116D")

    label("loc_1067")


    ChrTalk(
        0xFE,
        "O-Oh, you're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYo. How's it hangin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sh-Sh-Shut up.\x01",
            "Go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm in the middle of something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000F*sigh* How stubborn can she be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0204FI have yet to see Lloyd incur\x01",
            "this much ire from one person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FUh, Tio...\x02",
    )

    CloseMessageWindow()

    label("loc_116D")

    SetScenarioFlags(0x0, 2)
    Jump("loc_11FE")

    label("loc_1175")


    ChrTalk(
        0xFE,
        (
            "I'm still trying to wrap my head\x01",
            "around all this stuff I gotta learn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My battle has only just begun!\x01",
            "Now buzz off. I'm busy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FE")

    Jump("loc_12BC")

    label("loc_1203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1215")
    Call(0, 10)
    Jump("loc_12BC")

    label("loc_1215")


    ChrTalk(
        0xFE,
        (
            "Practice is about to start, and then\x01",
            "we've got stuff to do in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Can't you tell I'm busy here?! Don't come\x01",
            "waltzing in here like it's no big deal!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BC")

    TalkEnd(0xFE)
    Return()

    # Function_9_F86 end

    def Function_10_12C0(): pass

    label("Function_10_12C0")


    ChrTalk(
        0x101,
        (
            "#0005FWas this kid always a part\x01",
            "of the troupe?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133D")

    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1372")

    label("loc_133D")


    ChrTalk(
        0xFE,
        (
            "The heck? You guys Ilya's\x01",
            "friends or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1372")


    ChrTalk(
        0xFE,
        (
            "Hmph. The theater isn't open to\x01",
            "the public right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just because you're friends, doesn't mean\x01",
            "I'll let you come and go as you please.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD2, 0)
    Return()

    # Function_10_12C0 end

    def Function_11_1408(): pass

    label("Function_11_1408")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-250, 1670, 13660, 0)
    MoveCamera(32, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14970, 0)
    SetChrPos(0x101, 260, 120, 13350, 346)
    SetChrPos(0x102, -850, 450, 12100, 346)
    SetChrPos(0x103, -840, 0, 13680, 346)
    SetChrPos(0x104, 300, 450, 12100, 346)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0x8, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_14E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14E7)
    Sleep(10)

    def lambda_14F7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14F7)
    Sleep(12)

    def lambda_1507():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1507)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5P#1705FHey there, my favorite lil' guy.\x01",
            "Always nice to see you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1809FLong time no see, everyone.\x01",
            "I'm so sorry. I think we were too\x01",
            "absorbed in our own conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHaha. My apologies as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POur enthusiasm becomes unchecked\x01",
            "during practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0102FIt's been a long time, everyone. I hear\x01",
            "everybody loves your new production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1704FHaha. Well, obviously! It's only\x01",
            "natural for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1802FI actually noticed that you came to watch\x01",
            "us on our opening day, Lloyd.\x02\x03",
            "#1809FI hope you enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0012FWeeeell, I only came because I was\x01",
            "accompanying Cecile.\x02\x03",
            "#0002FBut still, the play was phenomenal!\x02\x03",
            "I already knew Ilya was something else,\x01",
            "but I've become a huge fan of Rixia, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#1810FO-Oh, please... You're embarrassing me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    ChrTalk(
        0x9,
        "#5P#1705FWell, aren't you just the romantic?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#5P#1709FMaybe I should let Cecile know her lil'\x01",
            "bro is putting the moves on my co-star.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0011FOh, come on! You clearly know\x01",
            "you're fudging the truth!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        "#11P#1801FG-Geez, Ilya!\x02",
    )

    CloseMessageWindow()

    def lambda_194B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_194B)

    def lambda_1958():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1958)

    def lambda_1965():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1965)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    OP_64(0x103)
    OP_64(0x102)

    ChrTalk(
        0x103,
        (
            "#6P#0211FHow fortunate for you, Lloyd.\x02\x03",
            "The rest of us have not had the privilege\x01",
            "of watching the show, as our tickets are\x01",
            "for next week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0310FNot only that, but you got to watch\x01",
            "Arc en Ciel all alone with Cecile?!\x02\x03",
            "Watchin' a mesmerizing play in a\x01",
            "dimly lit theater, enjoying the vibes...\x01",
            "Yer killin' me, Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0104FIt's okay, you two. Calm down.\x02\x03",
            "#0111FSure, he may be a lecher for immediately\x01",
            "turning to Rixia within seconds of being\x01",
            "with Cecile...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0012FWhat'd I do to deserve this disrespect?!\x02\x03",
            "#0001FSure, I may have beaten you to the punch\x01",
            "on watching the play alone, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0111F*staaaaaaare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0211F*staaaaaaare*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FScrew you, you womanizing brat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006F(Please. I'm begging you. Stop.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1702FHahaha! My favorite lil' guy has it hard.\x02\x03",
            "#1709FI'm sure if I were to announce my candidacy,\x01",
            "we'd have plenty of fascinating reactions!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#12P#0006FMy life isn't your plaything.\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(200)

    ChrTalk(
        0xA,
        "#11P#1809FA...hahaha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNow, now. I think you've all had enough\x01",
            "fun already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDon't tease him too much, Ilya. I doubt\x01",
            "he can handle it for much longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1704FYeah, yeah. I'll relax.\x02\x03",
            "#1700FSo anyway... What brings you\x01",
            "guys here today?\x02\x03",
            "#1709FWe have a bit of time to relax, so would\x01",
            "you like to have some tea?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F1B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F1B)

    def lambda_1F28():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1F28)

    def lambda_1F35():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1F35)

    def lambda_1F42():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1F42)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0005FThanks, but no thanks. We're here\x01",
            "on business.\x02\x03",
            "#0001FYou sent us a support request, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)

    def lambda_202D():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_202D)

    def lambda_204A():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_204A)
    Sleep(800)

    ChrTalk(
        0x8,
        "#5PO-Oh, right! I had completely forgotten!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1805FSorry about this... It started with the\x01",
            "three of us discussing the matter.\x02\x03",
            "#1806FIt somehow just ended up turning into\x01",
            "another practice session, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0x9,
        "#5P#1705FHuh? What'cha guys talking about?\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_21AB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21AB)

    def lambda_21B8():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21B8)
    Sleep(300)

    ChrTalk(
        0x8,
        "#5PGet your head out of the clouds, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1801FWe're discussing the stalker you told\x01",
            "us about last night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1705FOhhhh... That little thing?\x01",
            "Did you really have to bug them about it?\x02\x03",
            "#1706FIt's not like there was any harm done, so\x01",
            "we may as well ignore the whole thing.\x02",
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
    Sleep(1200)

    ChrTalk(
        0x104,
        (
            "#12P#0305FM-Man, you gotta hand it to her.\x01",
            "Total nerves of steel to be unfazed\x01",
            "by a stalker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FThere's not a hint of worry on her...\x01",
            "(Which is amazing, because I know\x01",
            "I would be if I were in her shoes.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_242D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_242D)

    def lambda_243A():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_243A)

    def lambda_2447():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2447)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PI-I'm sorry. We may be calling them a\x01",
            "stalker, but it could just be an\x01",
            "overzealous fan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1806FRight. We only heard about it ourselves\x01",
            "last night, when Ilya told us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003F(Those two seem distraught over this.)\x02\x03",
            "#0001FPardon me, but could both of you\x01",
            "calm down, please?\x02\x03",
            "I'd appreciate if you gave us an\x01",
            "overview of the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#1805FOkay. Allow me to explain!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)
    Sleep(200)

    ChrTalk(
        0xA,
        "#11P#1801FWill that be okay, Ilya?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 400)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#5P#1703FWell, I suppose since he's here...\x01",
            "All right, Rixia, go ahead and tell 'em.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)

    ChrTalk(
        0xA,
        "#11P#1801FRight!\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xE1, 0x190)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    ChrTalk(
        0xA,
        (
            "#11P#1801FThe incident in question took place about\x01",
            "a week or two ago.\x02\x03",
            "#1803FA supposedly...suspicious individual, the\x01",
            "stalker, kept appearing around her home.\x02\x03",
            "#1801FThe stalker originally loitered outside\x01",
            "of the apartment, but has now been\x01",
            "spotted entering the residence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0001FHe's been observing the surroundings?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1700FThe thing is, neither Rixia nor I have\x01",
            "seen them for ourselves.\x02\x03",
            "#1703FAll I can say is, it kinda feels like a strange\x01",
            "presence when I'm alone. Almost like...\x01",
            "somebody's watching me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0205FGiven our culprit has yet to be revealed,\x01",
            "they likely are sharp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FIsn't Ilya's home address private\x01",
            "information, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYes, of course. We never reveal our\x01",
            "employees' addresses to the public,\x01",
            "for safety reasons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PEven so, our stalker has managed to\x01",
            "figure out where Ilya lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FAny witnesses? A description of the perp\x01",
            "would be real helpful right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1803FAccording to a bystander, they were described\x01",
            "as a short boy, maybe around 14 or 15\x01",
            "years old.\x02\x03",
            "#1801FTheir face was well hidden thanks to a hat,\x01",
            "so we don't have any further information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FJust some kid who's an obsessed\x01",
            "fan, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FFan or not, he's clearly gone too far.\x02\x03",
            "We can't deny the fact that the stalking\x01",
            "could escalate into something more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI feared as much, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWe trust your abilities, so we were hoping\x01",
            "you could put a stop to this before it goes\x01",
            "any further.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x9,
        "#5P#1705FOh, yeah. I just remembered something.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#5P#1705FDid you enter my apartment yesterday,\x01",
            "Rixia?\x02\x03",
            "#1700FKinda had a sneaking suspicion that some\x01",
            "of my stuff had been rearranged.\x01",
            "You're the only one with a spare key, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(200)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0x8, 0x9, 500)
    Sleep(800)

    ChrTalk(
        0xA,
        "#11P#1805FOh, no! That can only mean one thing, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PThis is bad. Really bad!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0005FD-Don't tell me he's already\x01",
            "broken into your house...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FIf it's true, then the situation is much more\x01",
            "dire than we initially thought it to be.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F77():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F77)
    Sleep(10)

    def lambda_2F87():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F87)

    def lambda_2F94():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F94)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#5PThere's no time to lose, then! Please do\x01",
            "something about this immediately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1706FMan, the troupe leader sure loves to\x01",
            "exaggerate. Not like I have anything\x01",
            "scandalous hiding in there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_306B():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_306B)

    def lambda_3078():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3078)
    Sleep(300)

    ChrTalk(
        0xA,
        "#11P#1801FYou're missing the point, Ilya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PSeriously!\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(800)
    OP_93(0x8, 0xB4, 0x190)
    OP_93(0xA, 0xE1, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5P*sigh* I really wish to avoid reaching the same\x01",
            "level of publicity we had with the Yin debacle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt'd turn out even worse if our culprit is nothing\x01",
            "more than a demented fan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it's possible, I'd like for you to have him\x01",
            "cease the stalking covertly... And if it's\x01",
            "not possible, then arrest him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PCould you help us, please?\x02",
    )

    CloseMessageWindow()
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",       # 0
            "[Decline]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32BB")
    OP_29(0x1D, 0x1, 0x2)
    Call(0, 12)
    Jump("loc_3446")

    label("loc_32BB")


    ChrTalk(
        0x101,
        (
            "#12P#0006FI'm sorry, sir. We still have a lot of\x01",
            "duties to tend to. We'll need to\x01",
            "take care of them first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAh, that's unfortunate. I suppose I\x01",
            "can't do much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDo you know when you'll be free?\x01",
            "I'd like for you to settle this as soon\x01",
            "as you possibly can.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7113", 0)
    SetChrPos(0x0, -400, 450, 11590, 0)
    SetChrPos(0x8, -1880, 10, 15240, 135)
    SetChrPos(0xA, -210, 0, 13820, 0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_29(0x1D, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)

    label("loc_3446")

    Return()

    # Function_11_1408 end

    def Function_12_3447(): pass

    label("Function_12_3447")


    ChrTalk(
        0x101,
        (
            "#12P#0000FI understand the situation, so we'll\x01",
            "accept your request.\x02\x03",
            "#0003FThis could grow into something more\x01",
            "dangerous if we let it continue to brew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThank you kindly! We'll be counting\x01",
            "on you to resolve this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FAt least we know where our stalker\x01",
            "likes to hang out, yeah?\x02\x03",
            "Figure if we stake out the area, this\x01",
            "scumbag's gonna walk right into our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1705FIf that's the plan, then do you wanna\x01",
            "borrow the key to my place?\x02\x03",
            "#1700FIt'd probably be a bit more convenient to use\x01",
            "my place as a base of operations, yeah?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#0005FAre you sure that's okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1700FFine by me, my friends!\x01",
            "I'll just keep Rixia's spare key on me.\x02\x03",
            "Oh, by the way. I live in an apartment\x01",
            "complex by the name of Villa-Raisins\x01",
            "over on West Street.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3857")

    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, so you live in those fancy\x01",
            "apartments, then. Which room\x01",
            "are you staying in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1702FOnly one on the tippity-top floor.\x02\x03",
            "Now don't go losing this, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3915")

    label("loc_3857")


    ChrTalk(
        0x101,
        (
            "#12P#0000FOh, so you live in those fancy\x01",
            "apartments, then.\x02\x03",
            "I think it was on the top floor, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#1702FRight you are. Pretty astute of you.\x02\x03",
            "Now don't go losing this, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3915")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x347),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x347, 1)

    ChrTalk(
        0x101,
        "#12P#0000FI'll be sure to keep it safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1803FI'm sorry, everyone. I would love to be able\x01",
            "to help you out with the case.\x02\x03",
            "#1801FHe probably recognizes me since I'm always\x01",
            "with Ilya. I'd probably chase them off.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A48():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A48)
    Sleep(8)

    def lambda_3A58():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A58)

    def lambda_3A65():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A65)
    Sleep(5)

    def lambda_3A75():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A75)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0000FDon't worry about it, Rixia. Leave the\x01",
            "investigation to the detectives.\x02\x03",
            "Just fall back with Ilya and the rest of\x01",
            "the troupe while we do our job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#1801FOkay, will do. Will you at least contact us\x01",
            "if you manage to catch the culprit?\x01",
            "I'll grab Ilya and come running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0002FHaha. Not a problem.\x01",
            "(Rixia becomes notably more vigilant with\x01",
            "matters concerning Ilya...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_3C13():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C13)

    def lambda_3C20():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C20)

    def lambda_3C2D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C2D)

    def lambda_3C3A():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C3A)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#5P#0001FAnyway, guys. Let's head there\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0101FYes, let's.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FTime for our enamored fan to\x01",
            "get himself a reality check!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Stalker Investigation!!!]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_29(0x1D, 0x1, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3447 end

    def Function_13_3D83(): pass

    label("Function_13_3D83")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DDD")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DB1")
    Sleep(400)
    Jump("loc_3DC3")

    label("loc_3DB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC3")
    Sleep(750)

    label("loc_3DC3")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("Function_13_3D83")

    label("loc_3DDD")

    Return()

    # Function_13_3D83 end

    SaveToFile()

Try(main)
