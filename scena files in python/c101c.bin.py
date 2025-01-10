from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c101c.bin",                # FileName
        "c101c",                    # MapName
        "c101c",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c101c",                  # 0
        "Receptionist Michel",    # 1
        "Arios",                  # 2
        "Bracer Scott",           # 3
        "Bracer Wenzel",          # 4
        "Bracer Lynn",            # 5
        "Bracer Aeolia",          # 6
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch27200.itc",                   # 02
        "chr/ch27300.itc",                   # 03
        "chr/ch32002.itc",                   # 04
        "chr/ch32102.itc",                   # 05
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

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    405,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-10729,  0,       51650,   270,  405,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-12170,  0,       51490,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5929,   150,     43069,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5869,   150,     40840,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  10, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  11, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_3B1",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_11AD",         # 05, 5
        "Function_6_136A",         # 06, 6
        "Function_7_15E2",         # 07, 7
        "Function_8_16B9",         # 08, 8
        "Function_9_19CC",         # 09, 9
        "Function_10_1D28",        # 0A, 10
        "Function_11_22BF",        # 0B, 11
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_368")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_3AF")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_3AF")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_398")
    Jump("loc_3AF")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A6")
    Jump("loc_3AF")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AF")

    label("loc_3AF")

    Return()

    # Function_1_350 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Return()

    # Function_2_3B0 end

    def Function_3_3B1(): pass

    label("Function_3_3B1")

    Call(0, 4)
    Return()

    # Function_3_3B1 end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_60C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(
        0x8,
        (
            "Hey there, sweeties. Y'all\x01",
            "heading out somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012FY-Yeah, we've got some work to deal with...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Oh, yeah?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sure, cool. Don't wanna stick my nose\x01",
            "into police affairs. Definitely wouldn't\x01",
            "end well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I dunno what y'all are up to, but I hope\x01",
            "it all works out for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0001FThanks, Michel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0203F(His suspicions have arisen.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0301F(Sharp as always.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_607")

    label("loc_558")


    ChrTalk(
        0x8,
        (
            "I'm sure the police have plenty of issues\x01",
            "to deal with, but it ain't our problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'd better not be lazy about it, though.\x01",
            "You're the ones who signed up for this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607")

    Jump("loc_11A9")

    label("loc_60C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627")
    Call(0, 5)
    Jump("loc_6A2")

    label("loc_627")


    ChrTalk(
        0x8,
        (
            "Yikes. And I really wanted to give Arios\x01",
            "the day off, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Little Shizuku's going to be disappointed,\x01",
            "isn't she?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A2")

    Jump("loc_11A9")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(
        0x8,
        (
            "It's about that time when all those tourists\x01",
            "start checking out the sights outside the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I sent Estelle and Joshua off to St. Ursula today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, you better take care of yourselves\x01",
            "out there, honies.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8B1")

    label("loc_79F")


    ChrTalk(
        0x8,
        "Arios is dealing with an extermination request...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lynn and Aeolia are assigned to\x01",
            "parade support...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Scott's taking care of...something, and\x01",
            "Wenzel? He's sitting around on standby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've had enough of this! We need double\x01",
            "the manpower for this kinda work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1")

    Jump("loc_11A9")

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_F8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6C")

    ChrTalk(
        0x8,
        "You sweeties did pretty well last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Managing to beat out the Brights is\x01",
            "no easy feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHaha. Yeah, it definitely wasn't\x01",
            "a walk in the park.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FWe had to pull out all the stops for that\x01",
            "win, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's all in good fun, anyway. I'm sure\x01",
            "it'll help those two mature as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, yeah, before I forget. Wanted to\x01",
            "tell you all that Arios is back from\x01",
            "that business trip of his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sadly, a request from City Hall came\x01",
            "as soon as he got back, so he's assigned\x01",
            "to guard duty at a conference there.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#0005FHuh, I could have sworn that the\x01",
            "police were in charge of City Hall security...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FYou are correct. Furthermore, the First Division\x01",
            "is usually tasked with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Guess this is what you'd call 'joint security.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heard there's a bunch of big boys from across the\x01",
            "continent coming to these conferences, so they need\x01",
            "some strong men to take care of all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FY-Yeah, that sounds plausible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FHell, if the Divine Blade of Wind is there, then\x01",
            "it's the safest place in the whole dang city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FSo, due to all these circumstances, the\x01",
            "police and the guild are cooperating.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 5)
    Jump("loc_F88")

    label("loc_D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(
        0x8,
        (
            "Oh, that reminds me. Estelle and Joshua\x01",
            "said they had some 'personal' business\x01",
            "they needed to take care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said they were going out to some\x01",
            "remote area, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Meh. Arios is back in town, so I'll give 'em\x01",
            "a chance to catch their breath.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F88")

    label("loc_E82")


    ChrTalk(
        0x8,
        (
            "Okay, so Arios is at City Hall. The Brights\x01",
            "are out taking care of private matters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Scott and Wenzel are at the IBC, while Lynn\x01",
            "and Aeolia should be at the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Boy, let me tell you, it is NOT easy\x01",
            "keeping track of all of these bracers!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F88")

    Jump("loc_11A9")

    label("loc_F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B7")

    ChrTalk(
        0x8,
        "Hey there, sweeties!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Arios got a request from HQ over in Leman,\x01",
            "so his return to Crossbell's a little delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Guess he wasn't able to make it for the\x01",
            "Anniversary Festival's first day, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I've half a mind to file a complaint\x01",
            "with HQ for this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11A9")

    label("loc_10B7")


    ChrTalk(
        0x8,
        (
            "Business trips are supposed to be suspended\x01",
            "for the duration of the festival. I wanted all\x01",
            "of our members to celebrate it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Sheesh, of all the times to try and\x01",
            "monopolize Arios... They better\x01",
            "believe I'm going to bust back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A9")

    TalkEnd(0x8)
    Return()

    # Function_4_3B5 end

    def Function_5_11AD(): pass

    label("Function_5_11AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E2")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "Hey, I know you JUST got back, but could\x01",
            "you give your favorite darling a bit of a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You see, I was just contacted by the\x01",
            "Ardent branch in Remiferia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#1403FIs this about what I think it is?\x02\x03",
            "#1400FVery well. Let's hear the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1366")

    label("loc_12E2")


    ChrTalk(
        0x9,
        (
            "#1403FDon't worry about us right now.\x02\x03",
            "#1400FYou've still got work to finish, right?\x01",
            "Focus on completing your own tasks first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1366")

    TalkEnd(0xFE)
    Return()

    # Function_5_11AD end

    def Function_6_136A(): pass

    label("Function_6_136A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F8")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "Michel told me that if I finish up all of my\x01",
            "assigned work now, I won't have to go on\x01",
            "that business trip next week!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Oh, Wenzel. You didn't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I merely stated that I enjoy going on trips\x01",
            "alone occasionally...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But since the hectic festival period is over,\x01",
            "I wanted you to spend time with your fiancee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Thanks, partner.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_15DE")

    label("loc_14F8")


    ChrTalk(
        0xFE,
        (
            "Think I'm going to spend the next week with Pearl,\x01",
            "just like Wenzel suggested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd better check up on her plans and make sure\x01",
            "she's able to do it, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I'm kinda nervous to see her again.\x01",
            "It's been too long...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DE")

    TalkEnd(0xFE)
    Return()

    # Function_6_136A end

    def Function_7_15E2(): pass

    label("Function_7_15E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1600")
    Call(0, 6)
    Jump("loc_16B5")

    label("loc_1600")


    ChrTalk(
        0xFE,
        (
            "Scott's been real busy with work and hasn't\x01",
            "been able to spend much time with his Pearl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As his friend, I thought I should try and grant\x01",
            "him a little bit of time for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B5")

    TalkEnd(0xFE)
    Return()

    # Function_7_15E2 end

    def Function_8_16B9(): pass

    label("Function_8_16B9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_174D")
    Jump("loc_1797")

    label("loc_174D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_176D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1797")

    label("loc_176D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_178D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1797")

    label("loc_178D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1797")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_19C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F4")

    ChrTalk(
        0xFE,
        (
            "Finally, this tedious parade\x01",
            "security is over!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being in a crowd that big is just as sweaty\x01",
            "and claustrophobic as you'd expect it to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FYeah, I bet. Thanks for taking care of it, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Appreciate it, Randy.\x01",
            "Anyway, I think I've earned me a nice rest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_19C4")

    label("loc_18F4")


    ChrTalk(
        0xFE,
        (
            "Oh, that reminds me. I thought I saw a familiar\x01",
            "face in the bustle of the crowd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmm. Might have just been my imagination.\x01",
            "Surely they wouldn't have come to Crossbell\x01",
            "without contacting me, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C4")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_16B9 end

    def Function_9_19CC(): pass

    label("Function_9_19CC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A60")
    Jump("loc_1AAA")

    label("loc_1A60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A80")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AAA")

    label("loc_1A80")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AAA")

    label("loc_1AA0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AAA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C77")

    ChrTalk(
        0xFE,
        (
            "Oh, it's Tio! You're just the sweetest\x01",
            "little angel, aren't you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm totally bushed from all this work. Wanna\x01",
            "be a sweetheart and cure my fatigue for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0211FI am not aware of the proper procedure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lemme tell you, then! A great, big, squishy\x01",
            "hug will cure me of all my ailments! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FYou do not have the proper authorization\x01",
            "to run hug.exe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're killing me!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D20")

    label("loc_1C77")


    ChrTalk(
        0xFE,
        (
            "*siiiiigh* This stiiiinks...\x01",
            "I missed the chance to eat, so I guess I'll just\x01",
            "get take-out from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been on a real Morges' hamburger\x01",
            "binge lately!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D20")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_19CC end

    def Function_10_1D28(): pass

    label("Function_10_1D28")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The bracers' shift schedule is posted.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E6A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            "Arios: Principality of Remiferia\x01",
            "Scott: On Standby\x01",
            "Wenzel: On Standby\x01",
            "Lynn: Resting (Long Lao)\x01",
            "Aeolia: Resting (Bakery)\x01",
            "Estelle: Cathedral\x01",
            "Joshua: Cathedral\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_22A8")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F76")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: On Standby\x01",
            "Scott: Resting (Long Lao)\x01",
            "Wenzel: Resting (Long Lao)\x01",
            "Lynn: On Standby\x01",
            "Aeolia: On Standby\x01",
            "Estelle: St. Ursula Medical College\x01",
            "Joshua: St. Ursula Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_22A8")

    label("loc_1F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_20AA")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Patrolling Outside the City\x01",
            "Scott: Patrolling Outside the City\x01",
            "Wenzel: Armory\x01",
            "Lynn: Administrative District\x01",
            "Aeolia: Administrative District\x01",
            "Estelle: St. Ursula Medical College\x01",
            "Joshua: St. Ursula Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_22A8")

    label("loc_20AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21AB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: City Hall\x01",
            "Scott: IBC\x01",
            "Wenzel: IBC\x01",
            "Lynn: Cathedral\x01",
            "Aeolia: Cathedral\x01",
            "Estelle: Private Business (Mountain Path Area)\x01",
            "Joshua: Private Business (Mountain Path Area)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_22A8")

    label("loc_21AB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "                     Whereabouts\x01",
            "━━━━━━━━━━━━━━━━\x01",
            "Arios: Leman Bracer HQ\x01",
            "Scott: Tangram Gate\x01",
            "Wenzel: Tangram Gate\x01",
            "Lynn: Armorica Village\x01",
            "Aeolia: Armorica Village\x01",
            "Estelle: Administrative District\x01",
            "Joshua: Administrative District\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_22A8")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_1D28 end

    def Function_11_22BF(): pass

    label("Function_11_22BF")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There are a large number of\x01",
            "requests posted for bracers.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_22BF end

    SaveToFile()

Try(main)
