from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ScpFunction((
        "Function_0_DC",           # 00, 0
        "Function_1_10A6",         # 01, 1
        "Function_2_25EB",         # 02, 2
        "Function_3_3661",         # 03, 3
        "Function_4_4572",         # 04, 4
        "Function_5_4E82",         # 05, 5
        "Function_6_588D",         # 06, 6
        "Function_7_66CD",         # 07, 7
        "Function_8_698B",         # 08, 8
        "Function_9_839A",         # 09, 9
        "Function_10_964F",        # 0A, 10
        "Function_11_A125",        # 0B, 11
        "Function_12_A276",        # 0C, 12
        "Function_13_A3E8",        # 0D, 13
        "Function_14_A58B",        # 0E, 14
        "Function_15_A787",        # 0F, 15
        "Function_16_AF19",        # 10, 16
        "Function_17_B25D",        # 11, 17
    ))


    def Function_0_DC(): pass

    label("Function_0_DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_16C")

    ChrTalk(
        0xFE,
        "Ah! That marks the end of my shopping!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What an absolutely delightful feeling it\x01",
            "is when things go according to plan!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_16C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1C2")

    ChrTalk(
        0xFE,
        "*yawn* G'morning, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hope all goes well for you today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276")

    ChrTalk(
        0xFE,
        (
            "The crowd in the Harbor District\x01",
            "was a bit overwhelming, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something about it was creepy, especially\x01",
            "considering the police showed up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2BF")

    label("loc_276")


    ChrTalk(
        0xFE,
        (
            "Something's up in the Harbor District.\x01",
            "I just hope no one got hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF")

    Jump("loc_10A2")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2D2")
    Jump("loc_10A2")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39B")

    ChrTalk(
        0xFE,
        (
            "I hear the diet's budget meeting was\x01",
            "postponed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And that comes as a surprise to...literally no\x01",
            "one. Same story, different year. I'm sure we\x01",
            "have nothing to worry about, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")

    ChrTalk(
        0xFE,
        (
            "I got to see Mishelam's spectacular fireworks\x01",
            "show on the last day of the festival, and boy,\x01",
            "did it blow me away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All the commotion going on that night\x01",
            "nearly ruined it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I actually had a stroke of luck? I can't\x01",
            "imagine the cost for spending a night there.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_583")

    label("loc_4D3")


    ChrTalk(
        0xFE,
        (
            "Did you hear about that huge uproar at\x01",
            "Mishelam? Happened on the last night\x01",
            "of the festival, no less!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad I decided to head back\x01",
            "home before all that went down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_583")

    Jump("loc_10A2")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")

    ChrTalk(
        0xFE,
        (
            "Mayor MacDowell gives off this gentle vibe,\x01",
            "sort of like a granddad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unlike most politicians, he's always so kind.\x01",
            "Surprisingly spry, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess he does always rely on that cane,\x01",
            "though. Maybe old age is finally starting\x01",
            "to catch up to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_70B")

    label("loc_6A5")


    ChrTalk(
        0xFE,
        (
            "Dad said Mayor MacDowell is going to retire\x01",
            "this year, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I don't want him to leave.\x02",
    )

    CloseMessageWindow()

    label("loc_70B")

    Jump("loc_10A2")

    label("loc_710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CF")

    ChrTalk(
        0xFE,
        (
            "I wonder what the Anniversary Festival will\x01",
            "be like this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The shops are all bustling about, trying to\x01",
            "finish their preparations. Hehe, I can't wait!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_823")

    label("loc_7CF")


    ChrTalk(
        0xFE,
        (
            "Just a little while longer till the greatest\x01",
            "festival ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait!\x02",
    )

    CloseMessageWindow()

    label("loc_823")

    Jump("loc_10A2")

    label("loc_828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_8B1")

    ChrTalk(
        0xFE,
        "Shopping has me a little behind schedule.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I swear, you peek into a shop, then, poof!\x01",
            "All your free time is gone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_983")

    ChrTalk(
        0xFE,
        "What's going on today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've already walked by five or six officers\x01",
            "just this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As far as I can tell, nothing major has happened\x01",
            "in the city lately. Just what are they up to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC4")

    ChrTalk(
        0xFE,
        (
            "*sigh* In the end, I missed out on getting those\x01",
            "Arc en Ciel tickets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My friend and I made sure we stood in line\x01",
            "bright and early, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...by the time we reached the front, they\x01",
            "were already sold out. And get this: we\x01",
            "were only five people behind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is UN-BE-LIEVABLE!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6D")

    label("loc_AC4")


    ChrTalk(
        0xFE,
        "Just thinking about it ticks me off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those tickets are too expensive\x01",
            "to begin with!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't afford one even if I smashed\x01",
            "my piggy bank to smithereens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6D")

    Jump("loc_10A2")

    label("loc_B72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(
        0xFE,
        (
            "They say that Armorican veggies\x01",
            "work wonders for your health!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard it makes your skin as smooth\x01",
            "as silk, too. Maybe I should try some.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCF")

    ChrTalk(
        0xFE,
        (
            "I'm planning to go visit my relatives on\x01",
            "West Street today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shame orbal buses don't run inside of\x01",
            "the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I mean, how inconvenient is that?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D3A")

    label("loc_CCF")


    ChrTalk(
        0xFE,
        (
            "Given the size of Crossbell City, wouldn't\x01",
            "it be nice if the buses actually ran routes\x01",
            "throughout it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    Jump("loc_10A2")

    label("loc_D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_DC4")

    ChrTalk(
        0xFE,
        "I just saw this massive green car!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it might've had the Crossbell Guardian\x01",
            "Force emblem on it, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A2")

    label("loc_DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(
        0xFE,
        (
            "I'm considering renting an apartment\x01",
            "with a friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're all so expensive, though!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems like I can't escape my parents'\x01",
            "clutches for a while now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F2B")

    label("loc_E84")


    ChrTalk(
        0xFE,
        (
            "Apparently, rent isn't getting any lower, due\x01",
            "to Crossbell's flourishing economy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I thought I could afford it by splitting\x01",
            "the rent, but I guess not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2B")

    Jump("loc_10A2")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_10A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102B")

    ChrTalk(
        0xFE,
        "My papa works for a really big company.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They even made something called\x01",
            "the orbal network not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thing is, my dad doesn't know how it works,\x01",
            "so he constantly runs into problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's hopeless!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10A2")

    label("loc_102B")


    ChrTalk(
        0xFE,
        "People say the orbal network is super helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you don't know how to use it,\x01",
            "it isn't helpful at all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A2")

    TalkEnd(0xFE)
    Return()

    # Function_0_DC end

    def Function_1_10A6(): pass

    label("Function_1_10A6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113A")
    Jump("loc_1184")

    label("loc_113A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_115A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1184")

    label("loc_115A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1184")

    label("loc_117A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1184")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12DE")

    ChrTalk(
        0xFE,
        (
            "It looks like the diet's long-winded budget meeting\x01",
            "finally wrapped up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A full outline is going to be available to the public\x01",
            "eventually. I'm curious to see how it turned out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hopefully, the diet members can get things through\x01",
            "their thick skulls and stop the gratuitous spending.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_12DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1376")

    ChrTalk(
        0xFE,
        (
            "Maybe the diet will actually be able to decide on\x01",
            "the city's budget today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm getting an ominous feeling it'll\x01",
            "take some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_149C")

    ChrTalk(
        0xFE,
        (
            "Have you heard rumors that the local\x01",
            "mafias are butting heads?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have a bad feeling about this. Whenever\x01",
            "that happened in the past, heads would roll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was under the impression Crossbell had\x01",
            "become relatively peaceful...but I guess I\x01",
            "can't hold my breath just yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_14AA")
    Jump("loc_25E3")

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F3")

    ChrTalk(
        0xFE,
        (
            "Toward the end of the mountain path to\x01",
            "Mainz, there's a detour that'll take you to\x01",
            "some old ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Legend goes, if you're there during a full\x01",
            "moon, the sound of a beautiful bell will\x01",
            "ring out through the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No one knows anything about it, except\x01",
            "that it was built in the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16D8")

    label("loc_15F3")


    ChrTalk(
        0xFE,
        (
            "Toward the end of the mountain path to\x01",
            "Mainz, there's a detour that'll take you to\x01",
            "these old ruins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Legend goes, if you're there during a full\x01",
            "moon, the sound of a beautiful bell will\x01",
            "ring out through the general area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D8")

    Jump("loc_25E3")

    label("loc_16DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186A")

    ChrTalk(
        0xFE,
        (
            "Starting tomorrow, the diet will be deciding\x01",
            "on the city's budget at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Drafting the city's budget is a great responsibility,\x01",
            "considering all of Crossbell's public programs\x01",
            "rely on government funding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd say it's almost tradition that they don't finish\x01",
            "the budget by the scheduled date at this point.\x01",
            "I wonder if this year will be any different.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1952")

    label("loc_186A")


    ChrTalk(
        0xFE,
        (
            "No matter the year, the diet can never come\x01",
            "to an agreement on the state's budget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems like the reason this year is a disagreement\x01",
            "between the mayor and speaker. Can't help but\x01",
            "wonder if this year will be any different.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1952")

    Jump("loc_25E3")

    label("loc_1957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A96")

    ChrTalk(
        0xFE,
        (
            "South of the city, there's a huge structure called\x01",
            "Stargazer's Tower. Historians figure it was built\x01",
            "during the Middle Ages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in those times, Crossbell was a hotbed of\x01",
            "trade and warfare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Story goes that an influential individual had the\x01",
            "tower built for studying the stars.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B47")

    label("loc_1A96")


    ChrTalk(
        0xFE,
        (
            "Historians say Stargazer's Tower was built for\x01",
            "the sole purpose of astrology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've heard no one has investigated in depth\x01",
            "before, so who knows what the real truth is?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B47")

    Jump("loc_25E3")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CA5")

    ChrTalk(
        0xFE,
        (
            "Dieter Crois, the IBC's CEO, has been one of\x01",
            "the leading figures in funding Crossbell's public\x01",
            "endeavors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, he's been able to maintain profits\x01",
            "while staying true to his philanthropic nature!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, I've heard Aidios doesn't grant people\x01",
            "multiple talents, but she sure went all out\x01",
            "with a man like Mr. Crois.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1D14")

    ChrTalk(
        0xFE,
        "I should probably head home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't stay here too long if you don't want\x01",
            "to get a cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1E0B")

    ChrTalk(
        0xFE,
        (
            "Talk of the town says that Arc en Ciel recruited\x01",
            "a new girl for a show they're putting together.\x01",
            "She's to be the co-star, no less!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the rumors that Ilya scouted her out herself\x01",
            "are true, she must be some kind of prodigy!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F36")

    ChrTalk(
        0xFE,
        (
            "If I had to pick Crossbell's greatest charm,\x01",
            "it'd have to be the city's liveliness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For example, when the festival arrives, kids\x01",
            "AND the elderly get all ecstatic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next month will celebrate Crossbell's 70th\x01",
            "Anniversary Festival. Is it even possible to\x01",
            "outdo last year's?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1FE1")

    ChrTalk(
        0xFE,
        "Arc en Ciel is easily Crossbell's pride and joy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They've become so famous, foreign\x01",
            "celebrities travel to Crossbell incognito\x01",
            "just to catch a show!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E3")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C4")

    ChrTalk(
        0xFE,
        (
            "I discovered this really bizarre antique\x01",
            "shop in the Back Alley a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weird trinkets and baubles lined the walls,\x01",
            "and this creepy old lady sized me up\x01",
            "suspiciously as I wandered in.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_213E")

    label("loc_20C4")


    ChrTalk(
        0xFE,
        (
            "I discovered this really bizarre antique\x01",
            "shop in the Back Alley a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Has that place always been there?\x02",
    )

    CloseMessageWindow()

    label("loc_213E")

    Jump("loc_25E3")

    label("loc_2143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_22FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(
        0xFE,
        "Let me tell you: Crossbellans love their gossip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One lap around the city will fill you in on loads\x01",
            "of interesting tidbits!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Be it an urban legend or foreign economics...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All kinds of news flies around this city.\x01",
            "Almost makes you think that we can't\x01",
            "keep a secret.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22F8")

    label("loc_2279")


    ChrTalk(
        0xFE,
        (
            "Gossiping is almost second-nature to most\x01",
            "Crossbellans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, perhaps that's because our history is\x01",
            "rooted in trade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F8")

    Jump("loc_25E3")

    label("loc_22FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_245B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FC")

    ChrTalk(
        0xFE,
        (
            "Crossbell has long been home to a nasty\x01",
            "group called Revache & Co.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A mafia. That's what they really are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Unfortunately, their influence is much stronger\x01",
            "than the CPD's. Getting involved with them\x01",
            "is your funeral.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2456")

    label("loc_23FC")


    ChrTalk(
        0xFE,
        (
            "Not even the cops can keep Revache in check.\x01",
            "I wouldn't provoke them, if I were you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    Jump("loc_25E3")

    label("loc_245B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_25E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2573")

    ChrTalk(
        0xFE,
        (
            "So the orbal factory was remodeled\x01",
            "into an orbal store, was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seems like everything--from houses\x01",
            "to stores--is getting an upgrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's great the city is improving, but I don't\x01",
            "trust myself to navigate an increasingly\x01",
            "hectic Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25E3")

    label("loc_2573")


    ChrTalk(
        0xFE,
        (
            "Just because I grew up in Crossbell\x01",
            "doesn't mean that I don't still get\x01",
            "lost amidst the ever-growing city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_1_10A6 end

    def Function_2_25EB(): pass

    label("Function_2_25EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26C5")

    ChrTalk(
        0xFE,
        (
            "Police officers were seen leaving\x01",
            "the airport a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard they were talking about explosives\x01",
            "or something. Either way, it sounded bad.\x01",
            "I should probably stay away from there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_26C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2757")

    ChrTalk(
        0xFE,
        (
            "Did you see them? Police cars were just\x01",
            "racing toward the airport!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I get the feeling something bad happened.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27B4")

    label("loc_2757")


    ChrTalk(
        0xFE,
        (
            "If the police are in that big a rush to get\x01",
            "somewhere, you just know something's\x01",
            "wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B4")

    Jump("loc_365D")

    label("loc_27B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_28BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286A")

    ChrTalk(
        0xFE,
        (
            "Have you heard about the accident over\x01",
            "in the Harbor District yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm going to have to keep a close eye\x01",
            "on my daughter for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28B6")

    label("loc_286A")


    ChrTalk(
        0xFE,
        (
            "Mimi, be a good girl and stay close to me.\x01",
            "It's not very safe out now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B6")

    Jump("loc_365D")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_28C9")
    Jump("loc_365D")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29DA")

    ChrTalk(
        0xFE,
        (
            "Now that orbal vehicles are becoming more and\x01",
            "more commonplace, our government should put\x01",
            "some effort into maintaining our roads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since Central Square produces a lot of\x01",
            "pedestrian traffic, our budget should\x01",
            "include measures to expand the road size.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1E")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "Ah! You're the little one who lives with the\x01",
            "Special Support Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want, I'm sure my daughter Mimi\x01",
            "would love to play with you sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FThat'd be awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002F(The way she effortlessly connects with others\x01",
            "must be something she was born with.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B7A")

    label("loc_2B1E")

    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        (
            "You're close to Mimi's age, aren't you? I hope\x01",
            "you two can become good friends.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7A")

    Jump("loc_365D")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C60")

    ChrTalk(
        0xFE,
        (
            "Traffic might be an issue during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tourists will likely be driving orbal cars into\x01",
            "Crossbell by the dozen. Sure would be nice if\x01",
            "everyone could stay cordial while they're here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_2C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D42")

    ChrTalk(
        0xFE,
        (
            "They say members of the media were\x01",
            "given free tickets to Arc en Ciel's private\x01",
            "performance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, they'll be experiencing\x01",
            "it before everyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Can't say I'm not envious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DBE")

    label("loc_2D42")


    ChrTalk(
        0xFE,
        (
            "Arc en Ciel's new show is so close, I can\x01",
            "hardly contain myself! If only I could see\x01",
            "that private performance, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBE")

    Jump("loc_365D")

    label("loc_2DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E1B")
    TurnDirection(0xFE, 0xB, 0)

    ChrTalk(
        0xFE,
        (
            "Hey, Mimi! It's getting dark, so we better\x01",
            "make our way home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_2E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F3A")

    ChrTalk(
        0xFE,
        (
            "The new Arc en Ciel show is called\x01",
            "'Golden Sun, Silver Moon,' right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I can't wait until I can get another\x01",
            "glimpse of the radiant Ilya Platiere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm running a little low on mira right now,\x01",
            "though, so I guess I'll have to settle for\x01",
            "photos of her instead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_2F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301B")

    ChrTalk(
        0xFE,
        (
            "I, like so many others, wasn't able to snag\x01",
            "tickets for Arc en Ciel's new show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tickets sold out almost immediately, and\x01",
            "I swear the line for the department store\x01",
            "was about 100 arge long!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3094")

    label("loc_301B")


    ChrTalk(
        0xFE,
        (
            "I really wanted Mimi to experience Ilya's\x01",
            "amazing acting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, well. I suppose I'll try again in a\x01",
            "month or so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3094")

    Jump("loc_365D")

    label("loc_3099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_31F2")

    ChrTalk(
        0xFE,
        (
            "To become a registered orbal driver, you\x01",
            "have to complete the proper applications\x01",
            "over at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'd be surprised how many people aren't\x01",
            "too great at driving. Minor car accidents are\x01",
            "relatively common now, sadly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In my opinion, the criteria to be given a license\x01",
            "should be much more strict. For public safety.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_333C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326B")

    ChrTalk(
        0xFE,
        "Were you just...dropped off by an orbal car?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Honestly, I'm pretty jealous.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3337")

    label("loc_326B")


    ChrTalk(
        0xFE,
        (
            "I'm pretty sure that particular car was created\x01",
            "by the Republic's Verne Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, if I remember correctly, it's the most\x01",
            "affordable model they currently sell. Man,\x01",
            "orbal cars sure are cool.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3337")

    Jump("loc_365D")

    label("loc_333C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_350E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3483")

    ChrTalk(
        0xFE,
        (
            "Now that orbal cars are getting more popular,\x01",
            "illegal parking has become a bigger issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When people park on the side of the highway,\x01",
            "they're being a pain for pedestrians and fellow\x01",
            "drivers, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like it or not, roads are for everyone. Owning\x01",
            "a car doesn't put you above the law.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3509")

    label("loc_3483")


    ChrTalk(
        0xFE,
        "Illegal parking is becoming a big problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Roads are meant to be used by everyone.\x01",
            "Why can't drivers just follow the rules?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3509")

    Jump("loc_365D")

    label("loc_350E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_35E3")

    ChrTalk(
        0xFE,
        (
            "I'm from the Urban Development Division.\x01",
            "One part of my job consists of surveying a\x01",
            "given day's traffic volume.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But since I have the day off, I'm spending my\x01",
            "free time with my little girl.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_365D")

    label("loc_35E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_365D")

    ChrTalk(
        0xFE,
        (
            "It's not very surprising how crowded Central Square\x01",
            "can get, given that it's the heart of the city and all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_365D")

    TalkEnd(0xFE)
    Return()

    # Function_2_25EB end

    def Function_3_3661(): pass

    label("Function_3_3661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_36DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C1")

    ChrTalk(
        0xFE,
        "The sunset is so pretty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I get to go home with Dad now!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36D7")

    label("loc_36C1")


    ChrTalk(
        0xFE,
        "Time to go home!\x02",
    )

    CloseMessageWindow()

    label("loc_36D7")

    Jump("loc_456E")

    label("loc_36DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388C")

    ChrTalk(
        0xFE,
        "Hiya, Special Support Section!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you guys have a lot of work today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FA decent amount. And, wait a second...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FFinally managed to remember our name,\x01",
            "eh, Mimi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whaaat? I've never said it wrong before!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FW-Well, you actually have. They were\x01",
            "minor mistakes, though. No big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0202FWatch out for cars while you play, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Okie dokie! Good luck, guys!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38A8")

    label("loc_388C")


    ChrTalk(
        0xFE,
        "Good luck today, guys!\x02",
    )

    CloseMessageWindow()

    label("loc_38A8")

    Jump("loc_456E")

    label("loc_38AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3919")

    ChrTalk(
        0xFE,
        "Dad's been really strict today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but I know he loves me, so I'll\x01",
            "listen to him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_3927")
    Jump("loc_456E")

    label("loc_3927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3979")

    ChrTalk(
        0xFE,
        "Is KeA not with you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aw, I wanted to play with her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B44")
    TurnDirection(0xFE, 0x153, 0)

    ChrTalk(
        0xFE,
        "Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Are you playing with the Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1104FHehehe. I guess so!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A3C")

    ChrTalk(
        0x102,
        "#0106FWell, we aren't exactly playing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB0")

    label("loc_3A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A7E")

    ChrTalk(
        0x103,
        "#0206FPlaying is not an apt descriptor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB0")

    label("loc_3A7E")


    ChrTalk(
        0x104,
        "#0306FNot sure if playin' is the right word.\x02",
    )

    CloseMessageWindow()

    label("loc_3AB0")


    ChrTalk(
        0x101,
        (
            "#0006FAre you sure about that? Maybe it was.\x02\x03",
            "It's way too easy to get distracted\x01",
            "with KeA around. We need to keep\x01",
            "ourselves in check.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B7F")

    label("loc_3B44")


    ChrTalk(
        0xFE,
        "Hey, play with me next time! Okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1109FOkaaay!\x02",
    )

    CloseMessageWindow()

    label("loc_3B7F")

    Jump("loc_456E")

    label("loc_3B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C24")

    ChrTalk(
        0xFE,
        (
            "That nice lady over there said she's running\x01",
            "a food stall during the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've never had popcorn before. I can't wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3CB7")

    ChrTalk(
        0xFE,
        (
            "Everyone in the city seems to be super busy\x01",
            "with festival stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's going to be so much fun! Why can't it start\x01",
            "already?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3CF9")

    ChrTalk(
        0xFE,
        "Please, Dad! Let me play just a little longer!\x02",
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3DB1")

    ChrTalk(
        0xFE,
        (
            "Dad said he wasn't able to get any tickets\x01",
            "for the Arc en Ciel show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm not mad about it. It's popular, so\x01",
            "I'm sure we'll be able to go some other time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_3DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_401C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA8")

    ChrTalk(
        0xFE,
        "It's Lloyd! Hiya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FHey there, Mimi. Glad to hear you finally\x01",
            "remembered my name!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Of course! You're Lloyd and everyone\x01",
            "else from the Special Sports Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106FN-No, that's not exactly right. It's the\x01",
            "Special SUPPORT Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FJust a moment. Why does she only\x01",
            "remember Lloyd's name?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303FProud of you, Lloyd. I never thought you'd be\x01",
            "able to leave a stronger impression than me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0011FI-Impression? What are you talking about?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4017")

    label("loc_3FA8")


    ChrTalk(
        0xFE,
        (
            "So, Special Sports Section, what are you\x01",
            "doing today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll be rooting for you guys, so do your best!\x02",
    )

    CloseMessageWindow()

    label("loc_4017")

    Jump("loc_456E")

    label("loc_401C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4078")

    ChrTalk(
        0xFE,
        "Wow! It's so pretty outside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Make sure to watch out for cars, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_4078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_41E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415A")

    ChrTalk(
        0xFE,
        (
            "Oh, hey, you're from that Special...something\x01",
            "or other!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do your best, okay? Make every day count!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FThanks, Mimi. We will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106F(She still can't get our name quite right...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_41DD")

    label("loc_415A")


    ChrTalk(
        0xFE,
        (
            "My father dreams of being able to buy\x01",
            "an orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looks at magazines to see what new\x01",
            "ones are coming out every day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DD")

    Jump("loc_456E")

    label("loc_41E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_43AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4385")

    ChrTalk(
        0xFE,
        "Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FHi there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're the, um...the Special...Special, um...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0200FThe Special Support Section. I suppose\x01",
            "it is a bit of a mouthful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The Special Sports Section? Got'cha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, have fun with work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0106FTh-That's not quite...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FIn her defense, we've only been a thing for,\x01",
            "like, a month. Let's just hope she learns to\x01",
            "remember us over time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_43AA")

    label("loc_4385")


    ChrTalk(
        0xFE,
        "Go, go, Special Sports Section!\x02",
    )

    CloseMessageWindow()

    label("loc_43AA")

    Jump("loc_456E")

    label("loc_43AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4438")

    ChrTalk(
        0xFE,
        (
            "Vrooom! Vrrrooommm! Hehe, there are\x01",
            "so many cars out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is the best spot in all of Crossbell\x01",
            "to look at cars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_4438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_456E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44EB")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Hiya! Are you tourists?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, you aren't? Dang.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just when I was about to give you\x01",
            "my deluxe tour of Crossbell City...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_456E")

    label("loc_44EB")


    ChrTalk(
        0xFE,
        (
            "I'm going to be a tour guide\x01",
            "when I grow up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to me, then, and I'll show you\x01",
            "all the super cool places in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456E")

    TalkEnd(0xFE)
    Return()

    # Function_3_3661 end

    def Function_4_4572(): pass

    label("Function_4_4572")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4611")

    ChrTalk(
        0xFE,
        (
            "Uh, like, really? No shade, but do you\x01",
            "think stuffing yourself after exercising\x01",
            "is, like, a good idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* You are being SO you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4693")

    ChrTalk(
        0xFE,
        (
            "Hmm... You know, your figure is starting\x01",
            "to look pretty fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Slay, girl! You're killing it on this diet!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4768")

    ChrTalk(
        0xFE,
        (
            "Ah, snacks are just so peak! Like, there is\x01",
            "nothing better than buying a bunch of\x01",
            "snacks and just digging in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* Whoa, what's with the\x01",
            "stink eye? You're kinda killing my vibe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_482E")

    ChrTalk(
        0xFE,
        (
            "Fam, don't you need to, like, watch your\x01",
            "weight? Your face looks like a watermelon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You're, like, totally going to regret it if you\x01",
            "don't get on that diet-and-exercise life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_48BD")

    ChrTalk(
        0xFE,
        "What is that? Are you snacking again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not cool! We're supposed to be in this\x01",
            "together, and you're stuffing your face!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_48BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_492A")

    ChrTalk(
        0xFE,
        (
            "We've been total besties for a while,\x01",
            "haven't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still no boys I should know about?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4979")

    ChrTalk(
        0xFE,
        "The Anniversary Festival's almost here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Got any plans?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A12")

    ChrTalk(
        0xFE,
        (
            "Wait a sec, didn't Arc en Ciel tickets, like, \x01",
            "go on sale a while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crap, I totally spaced on that! We'll never\x01",
            "get any now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4AC1")

    ChrTalk(
        0xFE,
        (
            "I think I saw the IBC CEO's limousine\x01",
            "cruising around the city the other day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ohmigosh. What. A. Man! No lie, he's\x01",
            "just straight up the total package.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4B34")

    ChrTalk(
        0xFE,
        "Like, what do you want to do today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wandering around Times like usual\x01",
            "sounds totally lame.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4BD8")

    ChrTalk(
        0xFE,
        (
            "I'm, like, totally bummed out. Arios is out\x01",
            "of town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Darn it. I hate it when he's gone. My eyes\x01",
            "can't feast on that absolute meal of a man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4C5D")

    ChrTalk(
        0xFE,
        (
            "If only I had a totally hunky man with his\x01",
            "own orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He could take me, like, anywhere my heart\x01",
            "desires.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4D20")

    ChrTalk(
        0xFE,
        (
            "Ohmigosh, did you hear that, like, some totally\x01",
            "creepy monsters attacked Armorica and Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That is so cray. Why the heck isn't the Guardian\x01",
            "Force, like, doing anything?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4E06")

    ChrTalk(
        0xFE,
        (
            "*squeal* Le-na-lee! Did you see that photo on\x01",
            "the front page of the Crossbell Times?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arios is SO hot! And he's, like, the coolest bracer\x01",
            "ever. The entire city loves him, but not as much\x01",
            "as I do, of course.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7E")

    label("loc_4E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4E7E")

    ChrTalk(
        0xFE,
        (
            "Looks like Arios the hunk\x01",
            "is back in the news again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like--on Aidios--I wish\x01",
            "he'd come save me, too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E7E")

    TalkEnd(0xFE)
    Return()

    # Function_4_4572 end

    def Function_5_4E82(): pass

    label("Function_5_4E82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4F31")

    ChrTalk(
        0xFE,
        (
            "B-But, you totally said I slimmed down?!\x01",
            "Don't I deserve to treat myself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waaait! Please don't give up on me!\x01",
            "I won't slack off anymore! I promise!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_4F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FD4")
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        "O-Oh, am I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All this jogging is finally starting to pay\x01",
            "off! Heck yes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(A little white lie to get her motivated\x01",
            "never hurts.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_5889")

    label("loc_4FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_50AB")

    ChrTalk(
        0xFE,
        (
            "Agh, you are SO not fair! Like, why would\x01",
            "you show off all that tasty food while I'm\x01",
            "in the middle of my diet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, just gimme a tiny bit! I even went\x01",
            "running this morning and everything!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_50AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_50B9")
    Jump("loc_5889")

    label("loc_50B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_516C")

    ChrTalk(
        0xFE,
        (
            "Omigosh, that is, like, totally horrible!\x01",
            "I can't believe you said that to my face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know I'm starting my diet today.\x01",
            "Aidios, please, bless my stomach.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_51F7")

    ChrTalk(
        0xFE,
        (
            "*munch* *munch* Y'know, isn't only two\x01",
            "meals a day kinda, like, overkill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tommorow! I'll start dieting...tomorrow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_51F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_527F")

    ChrTalk(
        0xFE,
        (
            "If we had boyfriends, we totally wouldn't\x01",
            "have time to be such close friends, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh* This totally sucks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_527F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_52CF")

    ChrTalk(
        0xFE,
        (
            "Hmm... Not really. I guess I'll just hit some\x01",
            "of the stalls.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_52CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_53A7")

    ChrTalk(
        0xFE,
        "Well, like, duh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arc en Ciel tickets sell out, like, the second\x01",
            "they go on sale to the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's totally possible we could've stood in a\x01",
            "super-long line only to still NOT get tickets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_53A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5446")

    ChrTalk(
        0xFE,
        (
            "It's always Arios this and Dieter that with\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, you've totally\x01",
            "got a thing for cool older guys, don't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_5446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_550D")

    ChrTalk(
        0xFE,
        "I would suggest we get tea from somewhere...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...but my wallet is, like, mega-low on mira.\x01",
            "Guess we're stuck with our usual routine of\x01",
            "window-shopping at the department store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_550D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_55E7")

    ChrTalk(
        0xFE,
        (
            "I know Arios is a super-popular bracer, but it\x01",
            "stinks that he's, like, always gone for jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our police force is as useful as an orbment\x01",
            "without quartz. I really wish he would stay\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_55E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_56AB")

    ChrTalk(
        0xFE,
        "Aren't orbal cars, like, insanely expensive?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's such a mood, though. I keep saying\x01",
            "I'll find myself a guy loaded with mira, but\x01",
            "just saying that won't get me anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_56AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_575F")

    ChrTalk(
        0xFE,
        (
            "Well, I think we can be chill, though.\x01",
            "We should be safe here in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, we have the lovely bracers just\x01",
            "over on East Street to watch over us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_575F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_57E9")

    ChrTalk(
        0xFE,
        "Get a load of this photo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These police officers back behind Arios\x01",
            "look totally awk. What are they, his\x01",
            "sidekicks?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5889")

    label("loc_57E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5889")

    ChrTalk(
        0xFE,
        (
            "Like, didn't the news say some police\x01",
            "people tried to help Arios, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sounds like the real hero blew up\x01",
            "their spot. Sucks to suck, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5889")

    TalkEnd(0xFE)
    Return()

    # Function_5_4E82 end

    def Function_6_588D(): pass

    label("Function_6_588D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598B")

    ChrTalk(
        0xFE,
        (
            "The smiles children give as I hand them a\x01",
            "freshly-inflated balloon never get old.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Trust me. It's much more satisfying than\x01",
            "you'd think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I'm old, I'd love to be known as the\x01",
            "'Old Balloon Man' to the kids.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A2E")

    label("loc_598B")


    ChrTalk(
        0xFE,
        (
            "The smiles that come from giving balloons\x01",
            "are precious things, let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I'm old, I'd love to be known as the\x01",
            "'Old Balloon Man' to the kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A2E")

    Jump("loc_66C9")

    label("loc_5A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B41")

    ChrTalk(
        0xFE,
        (
            "Balloons here! Freshly inflated! Excuse me,\x01",
            "would you like your very own balloon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure to be careful not to bring it\x01",
            "into a large crowd of people, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're made of rubber, so you'd be surprised\x01",
            "at how easily they pop!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5C03")

    label("loc_5B41")


    ChrTalk(
        0xFE,
        (
            "Since the balloons are just made out of rubber,\x01",
            "they pop pretty easily!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, the sound still manages to elicit a\x01",
            "reaction out of me. It almost sounds like an\x01",
            "explosion going off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C03")

    Jump("loc_66C9")

    label("loc_5C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5CCE")

    ChrTalk(
        0xFE,
        (
            "Whenever I hold balloons, all my worries\x01",
            "seem to float away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look here. See how silly this one is? Even\x01",
            "when you feel down, my balloons are sure\x01",
            "to bring your laughter back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_5CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5CDC")
    Jump("loc_66C9")

    label("loc_5CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5DB6")

    ChrTalk(
        0xFE,
        (
            "Get your very own balloon! That's right,\x01",
            "balloons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh? Is that firecracker of a girl not with\x01",
            "you today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Better make sure that you play with her\x01",
            "often, or else she'll likely start sulking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_5DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ED8")

    ChrTalk(
        0xFE,
        "Hello, little missy! Want one?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Someone your age must love balloons, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#1111FUm...not really? Why would I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Wh-What did you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've, uh, never met a kid who didn't\x01",
            "like balloons before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006F(What's she got against balloons?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5F22")

    label("loc_5ED8")


    ChrTalk(
        0xFE,
        (
            "My balloons usually light up the smiles\x01",
            "of all the kids who stop by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F22")

    Jump("loc_66C9")

    label("loc_5F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5FB7")

    ChrTalk(
        0xFE,
        (
            "Of course, I only inflate the balloons when\x01",
            "no one's watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If someone saw, the magic would be gone,\x01",
            "don'tcha think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_5FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B6")

    ChrTalk(
        0xFE,
        (
            "Did you know that gas is lighter than air?\x01",
            "That's why my balloons are able to float\x01",
            "oh-so gracefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey! Careful with open flames around here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the gas catches fire, it'll explode! Think of\x01",
            "the children, man!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_612F")

    label("loc_60B6")


    ChrTalk(
        0xFE,
        "Keep fire away from here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y'know, I wouldn't care to fly through the\x01",
            "sky like one of my balloons. Seems scary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_612F")

    Jump("loc_66C9")

    label("loc_6134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6195")

    ChrTalk(
        0xFE,
        "Well, then, let's call it a day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This career isn't as easy as you think.\x02",
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_6195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6282")

    ChrTalk(
        0xFE,
        (
            "Now that orbments are everywhere, gas-powered\x01",
            "machinery and tools are few and far between.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Orbal energy is great, don't get me wrong. I think\x01",
            "blowing up balloons is one of the only things left\x01",
            "that's gas-powered.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_6282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6309")

    ChrTalk(
        0xFE,
        "Balloons! Get your very own balloon here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Make sure not to accidentally let go, because\x01",
            "they'll fly, fly away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_6309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63B8")

    ChrTalk(
        0xFE,
        (
            "All right! Time to crank up the enthusiasm\x01",
            "and give out some freakin' balloons today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Central Square is usually ripe with tourists\x01",
            "during the morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_63B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6436")

    ChrTalk(
        0xFE,
        "Did you want a balloon, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heck, I don't mind if you aren't tourists! You\x01",
            "fit the bill well enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_6436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6549")

    ChrTalk(
        0xFE,
        (
            "Tourism is considered one of Crossbell's biggest\x01",
            "and most profitable industries. They even make\x01",
            "room in the state budget for it, believe it or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Distributing balloons is crucial to the industry.\x01",
            "It ignites the tourist's passion to explore, y'know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C9")

    label("loc_6549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_666B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6612")

    ChrTalk(
        0xFE,
        "Do you want a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh? No. They're not just for festivals.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I make my living by handing out these babies!\x01",
            "Crossbellans live for the sensational, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6666")

    label("loc_6612")


    ChrTalk(
        0xFE,
        "The flashier, the better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come one, come all! Take as many as\x01",
            "you'd like!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6666")

    Jump("loc_66C9")

    label("loc_666B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_66C9")

    ChrTalk(
        0xFE,
        "Would you like a balloon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Free of charge for tourists.\x01",
            "That's right: free!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66C9")

    TalkEnd(0xFE)
    Return()

    # Function_6_588D end

    def Function_7_66CD(): pass

    label("Function_7_66CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6858")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E5")

    ChrTalk(
        0xFE,
        (
            "Well, then, that wraps up my look-see of\x01",
            "possible food stall locations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm already here, I might as well do\x01",
            "a bit of sightseeing before I head back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, better do that now. I doubt I'll have\x01",
            "any free time during the festival.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6853")

    label("loc_67E5")


    ChrTalk(
        0xFE,
        "Now, where should I go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I'm only here for the day, I can't see\x01",
            "everything I'd like to, sadly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6853")

    Jump("loc_6987")

    label("loc_6858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6987")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68EB")

    ChrTalk(
        0xFE,
        (
            "During next month's Anniversary Festival, I get\x01",
            "to run a popcorn stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm lucky to have gotten a good spot.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6987")

    label("loc_68EB")


    ChrTalk(
        0xFE,
        (
            "I get to run a popcorn stall during next month's\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came to get the lay of the land, because\x01",
            "next month is going to be busy!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6987")

    TalkEnd(0xFE)
    Return()

    # Function_7_66CD end

    def Function_8_698B(): pass

    label("Function_8_698B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_699C")
    Jump("loc_8396")

    label("loc_699C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A40")
    OP_93(0xFE, 0xC5, 0x0)

    ChrTalk(
        0xFE,
        "*whistle* Keep your speed to a minimum, please!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Is today's traffic unusually calm, or is it\x01",
            "just my imagination?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_6ABC")

    label("loc_6A40")


    ChrTalk(
        0xFE,
        (
            "I oversee the city's traffic daily, but things feel\x01",
            "a bit desolate today. Then again, it might just\x01",
            "be my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ABC")

    Jump("loc_8396")

    label("loc_6AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6ACF")
    Jump("loc_8396")

    label("loc_6ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6ADD")
    Jump("loc_8396")

    label("loc_6ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DF1")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Hey, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know, I heard that things got a little heated\x01",
            "recently. Everything okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0008FWe're fine. Sorry. We didn't mean\x01",
            "to make you worry, Kate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_6C14")

    ChrTalk(
        0x102,
        (
            "#0100FRight. We're okay now.\x02\x03",
            "More importantly, how's the city been\x01",
            "faring lately?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF9")

    label("loc_6C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_6C72")

    ChrTalk(
        0x103,
        (
            "#0200FThings managed to work themselves out.\x02\x03",
            "That aside, how is the city?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CF9")

    label("loc_6C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_6CF9")

    ChrTalk(
        0x104,
        (
            "#0300FYeah, we're good. Got spotty for a minute,\x01",
            "but we pulled through.\x02\x03",
            "But enough about us. How's the city\x01",
            "holdin' up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CF9")


    ChrTalk(
        0xFE,
        (
            "Well, it's a lot quieter now that the festival\x01",
            "fever is starting to wear off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll miss it, but it sure makes my job easier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FI can sympathize with that.\x01",
            "(Does that mean Revache has been\x01",
            "laying low since our operation?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 0)
    Jump("loc_6EF9")

    label("loc_6DF1")


    ChrTalk(
        0xFE,
        "The city's a lot quieter now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The festival fever is starting to wear off.\x01",
            "I'll miss it, but my life's way less stressful now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Forget about me, though! I couldn't stop worrying\x01",
            "about you guys. The SSS is tough, but don't do\x01",
            "anything too risky, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF9")

    Jump("loc_8396")

    label("loc_6EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C4")

    ChrTalk(
        0xFE,
        (
            "Grrr! I found even more illegally parked cars\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support Section already towed a\x01",
            "bunch away yesterday, too! No fair!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FSorry, Kate. That's just how these things go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYeah, I s'pose it's impossible to completely\x01",
            "rid Crossbell of illegal parking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't it totally frustrating?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is for me, so that's why I'll teach these\x01",
            "punks a lesson they aren't likely to forget!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_715E")

    label("loc_70C4")


    ChrTalk(
        0xFE,
        (
            "Illegal parking is a crime, and crimes are\x01",
            "meant to be punished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police will have to crack down on this\x01",
            "if we want this nasty habit to end!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_715E")

    Jump("loc_8396")

    label("loc_7163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_72D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725C")
    OP_93(0xFE, 0xC5, 0x0)

    ChrTalk(
        0xFE,
        "*whistle* Keep your speed to a minimum, please!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "The CPD only succeeds with everyone's\x01",
            "combined efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All right, everyone! Let's give today\x01",
            "everything we've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FYou got it, Kate!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_72CB")

    label("loc_725C")


    ChrTalk(
        0xFE,
        (
            "The CPD only succeeds with everyone's\x01",
            "combined efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's give today everything we've got, guys!\x02",
    )

    CloseMessageWindow()

    label("loc_72CB")

    Jump("loc_8396")

    label("loc_72D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_END)), "loc_7593")

    ChrTalk(
        0xFE,
        (
            "Hey, everyone. Are you in the middle of an\x01",
            "investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, you could say that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000FOh, right. Kate, you mainly patrol\x01",
            "around the city, don't you?\x02\x03",
            "Does the word 'Yin' ring any bells?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yin? Sorry, can't say it does. Unless...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Isn't Yin the word people in the East use\x01",
            "for silver?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If so, it might refer to Arc en Ciel's new\x01",
            "show: 'Golden Sun, Silver Moon'!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006FY-You think? We'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Sorry, that's the only thing that came\x01",
            "to mind. I wish I could be of more help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A6B")

    label("loc_7593")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Lloyd! Randy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thanks for helping me with traffic control!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, sorry. That was way too informal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Detective Bannings and the Special Support\x01",
            "Section, thank you for your cooperation with\x01",
            "traffic control!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0002FC'mon, Kate. You really don't need to treat\x01",
            "us like that. We're friends.\x02\x03",
            "Besides, you've always had our backs, too.\x01",
            "Why wouldn't we return the favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I suppose you make a good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time I'm in a bind, I hope you four won't\x01",
            "mind bailing me out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FFor sure. Just give us a ring, and we'll\x01",
            "be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thanks, guys. You really saved me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Investigating again, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0003FYeah, you could say that.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0000FOh, right. Kate, you mainly patrol\x01",
            "around the city, don't you?\x02\x03",
            "Does the word 'Yin' ring any bells?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yin? Sorry, can't say it does. Unless...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "That's it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yin means silver, right? Might it refer to\x01",
            "Arc en Ciel's new show: Golden Sun, Silver\x01",
            "Moon?!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0006FY-You think? We'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Sorry, that's the only thing that came\x01",
            "to mind. I wish I could be of more help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6B")

    SetScenarioFlags(0x92, 1)
    Jump("loc_7BA6")

    label("loc_7A73")


    ChrTalk(
        0xFE,
        "Yin... Doesn't really ring a bell on its own...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm so sorry. I haven't been any help at all,\x01",
            "have I?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4B")

    ChrTalk(
        0x101,
        (
            "#0000FNo, please, don't worry about it. We've still\x01",
            "got a trusted informant to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BA6")

    label("loc_7B4B")


    ChrTalk(
        0x101,
        (
            "#0000FIt's fine, Kate. We think we've found a lead,\x01",
            "even if it is a bit of a stretch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BA6")

    Jump("loc_8396")

    label("loc_7BAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_80A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8011")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CBE")

    ChrTalk(
        0xFE,
        (
            "Lloyd! Randy!\x01",
            "Thanks for helping me with traffic control!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'm sorry. That was way too informal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Detective Bannings and the Special Support\x01",
            "Section, thank you for your cooperation with\x01",
            "traffic control!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E42")

    label("loc_7CBE")


    ChrTalk(
        0xFE,
        (
            "Hey, everyone! Let's work hard today to\x01",
            "whip this city into shape. You with me?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FAlways!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300F'Preciate the morning pep talk, Kate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Any time. And thanks for helping out\x01",
            "with this morning's traffic issue!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I'm sorry. That was way too informal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Detective Bannings and the Special Support\x01",
            "Section, thank you for your cooperation with\x01",
            "traffic control!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E42")


    ChrTalk(
        0x101,
        (
            "#0002FC'mon, Kate. You really don't need to treat\x01",
            "us like that. We're friends.\x02\x03",
            "Besides, you've always had our backs, too.\x01",
            "Why wouldn't we return the favor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Good point, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time I'm in a bind, I hope you four won't\x01",
            "mind bailing me out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FIt'd be our pleasure. Just give us a ring\x01",
            "and we'll be there, Kate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thanks, guys. You really saved me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, then, back to the job! You all do\x01",
            "your best, too, okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 0)
    Jump("loc_809F")

    label("loc_8011")


    ChrTalk(
        0xFE,
        (
            "Maybe the Anniversary Festival is the\x01",
            "cause of this spike in petty crimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't afford to daydream while on patrol.\x01",
            "Focus, Kate!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809F")

    Jump("loc_8396")

    label("loc_80A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8340")
    OP_93(0xFE, 0xC5, 0x0)

    ChrTalk(
        0xFE,
        "*whistle* Keep your speed to a minimum, please!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Public safety is only possible by adhering\x01",
            "to the law!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_81BE")

    ChrTalk(
        0xFE,
        (
            "Hey, everyone. Starting today's work?\x01",
            "Be sure to watch out for orbal cars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks for the heads-up, Kate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8338")

    label("loc_81BE")


    ChrTalk(
        0xFE,
        (
            "Oh, hello there-- Wait, Lloyd?!\x01",
            "Long time no see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FKate? Dang, it's been way too long! Thanks\x01",
            "again for everything you did for me at the\x01",
            "police academy.\x02\x03",
            "Are you on patrol right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nailed it. I primarily handle traffic control\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you heading out to work? Be sure\x01",
            "to watch out for orbal cars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0000FThanks for the heads-up, Kate.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)

    label("loc_8338")

    SetScenarioFlags(0x1, 1)
    Jump("loc_8396")

    label("loc_8340")

    OP_93(0xFE, 0xC5, 0x0)

    ChrTalk(
        0xFE,
        (
            "Slow down, please! Public safety is only\x01",
            "possible by adhering to the law!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8396")

    TalkEnd(0xFE)
    Return()

    # Function_8_698B end

    def Function_9_839A(): pass

    label("Function_9_839A")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8436")

    ChrTalk(
        0x101,
        (
            "#0004F(You know, I might have something here\x01",
            "that Coppe would like.)\x02\x03",
            "#0000F(I'm sure it'll be okay giving this to him.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_8436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9648")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_84AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9643")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Food")
    MenuCmd(1, 1, "Leave")
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F9")
    MenuCmd(3, 1, 0x1)

    label("loc_84F9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_852B")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_852B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_960E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_8569")
    MenuCmd(1, 1, "Snow Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8569")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8590")
    MenuCmd(1, 1, "Armorican Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8590")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_85B7")
    MenuCmd(1, 1, "Tiger Rockfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85B7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_85D9")
    MenuCmd(1, 1, "Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_85F6")
    MenuCmd(1, 1, "Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_85F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8618")
    MenuCmd(1, 1, "Raineater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8618")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8639")
    MenuCmd(1, 1, "Azelfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8639")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_8659")
    MenuCmd(1, 1, "Kasagin")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8659")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_867F")
    MenuCmd(1, 1, "Rainbow Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_867F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_869D")
    MenuCmd(1, 1, "Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_869D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_86BC")
    MenuCmd(1, 1, "Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_86D8")
    MenuCmd(1, 1, "Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_86FB")
    MenuCmd(1, 1, "Pearlglass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_8723")
    MenuCmd(1, 1, "Gluttonous Bass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8723")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8745")
    MenuCmd(1, 1, "Viperhead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8745")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8768")
    MenuCmd(1, 1, "Pythonhead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8768")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8788")
    MenuCmd(1, 1, "Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8788")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_87AB")
    MenuCmd(1, 1, "Queen Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_87D0")
    MenuCmd(1, 1, "Electric Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_87F6")
    MenuCmd(1, 1, "Demon Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_8818")
    MenuCmd(1, 1, "Arch Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8818")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_883C")
    MenuCmd(1, 1, "Gold Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_883C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_885F")
    MenuCmd(1, 1, "Noble Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_885F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_8883")
    MenuCmd(1, 1, "Serpenthead")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8883")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_88A4")
    MenuCmd(1, 1, "Cat Food")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88A4")

    MenuCmd(1, 1, "Cancel")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88EE")
    Jump("loc_95FF")

    label("loc_88EE")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x13, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "Nyannyan... ㈱\x02",
    )

    CloseMessageWindow()

    def lambda_89B4():

        label("loc_89B4")

        TurnDirection(0x0, 0x13, 0)
        Yield()
        Jump("loc_89B4")

    QueueWorkItem2(0x0, 1, lambda_89B4)

    def lambda_89C6():

        label("loc_89C6")

        TurnDirection(0x1, 0x13, 0)
        Yield()
        Jump("loc_89C6")

    QueueWorkItem2(0x1, 1, lambda_89C6)

    def lambda_89D8():

        label("loc_89D8")

        TurnDirection(0x2, 0x13, 0)
        Yield()
        Jump("loc_89D8")

    QueueWorkItem2(0x2, 1, lambda_89D8)

    def lambda_89EA():

        label("loc_89EA")

        TurnDirection(0x3, 0x13, 0)
        Yield()
        Jump("loc_89EA")

    QueueWorkItem2(0x3, 1, lambda_89EA)

    def lambda_89FC():

        label("loc_89FC")

        TurnDirection(0x4, 0x13, 0)
        Yield()
        Jump("loc_89FC")

    QueueWorkItem2(0x4, 1, lambda_89FC)

    def lambda_8A0E():

        label("loc_8A0E")

        TurnDirection(0x5, 0x13, 0)
        Yield()
        Jump("loc_8A0E")

    QueueWorkItem2(0x5, 1, lambda_8A0E)
    SetChrFlags(0x13, 0x8000)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x13, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_8A3A():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8A3A)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_8A61():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8A61)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_8A88():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8A88)
    WaitChrThread(0x13, 1)
    Sleep(2000)
    OP_93(0x13, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_8AB9():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8AB9)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_8AE0():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8AE0)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_8B07():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8B07)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x1)
    OP_93(0x13, 0x10E, 0x1F4)
    ClearChrFlags(0x13, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "Funya～...\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_8BD7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BCD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x70, 1)

    label("loc_8BCD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8C23")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C19")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_8C19")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_8C6F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C65")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x6A, 1)

    label("loc_8C65")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_8CBB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x6D, 1)

    label("loc_8CB1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8D07")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CFD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x73, 1)

    label("loc_8CFD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8D53")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D49")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x67, 1)

    label("loc_8D49")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8D9F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D95")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8A, 1)

    label("loc_8D95")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_8DEB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DE1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x85, 1)

    label("loc_8DE1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_8E37")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x99),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x99, 1)

    label("loc_8E2D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_8E83")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E79")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x82, 1)

    label("loc_8E79")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_8ECF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_8EC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_8F1B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x7F, 1)

    label("loc_8F11")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_8F67")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x76, 1)

    label("loc_8F5D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_8FB3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_8FA9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_8FFF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8B, 1)

    label("loc_8FF5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_904B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9041")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8D, 1)

    label("loc_9041")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_9097")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x8E, 1)

    label("loc_908D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9097")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_90E3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90D9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x83),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x83, 1)

    label("loc_90D9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_912F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9125")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA9, 1)

    label("loc_9125")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_912F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_917B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9171")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x81, 1)

    label("loc_9171")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_917B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_91C7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91BD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_91BD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_9213")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9209")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x9A, 1)

    label("loc_9209")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9213")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_925F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9255")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0x95, 1)

    label("loc_9255")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_925F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_92AB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA0, 1)

    label("loc_92A1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_92FA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3.\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_92F0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92FA")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9321")
    SetScenarioFlags(0x4B, 3)

    label("loc_9321")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9332")
    SetScenarioFlags(0x52, 1)

    label("loc_9332")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9343")
    SetScenarioFlags(0x52, 2)

    label("loc_9343")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9354")
    SetScenarioFlags(0x52, 3)

    label("loc_9354")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9365")
    SetScenarioFlags(0x52, 4)

    label("loc_9365")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9376")
    SetScenarioFlags(0x52, 5)

    label("loc_9376")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9387")
    SetScenarioFlags(0x52, 6)

    label("loc_9387")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_93A4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_93B7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_93CA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_93DD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_93F0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_9403")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9477")

    ChrTalk(
        0xFE,
        "Nyan Nyannyan... ♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    AddItemNumber(0xA6, 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_9477")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94BC")

    ChrTalk(
        0x102,
        "#0105FOh? You want us to have this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9570")

    label("loc_94BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94FE")

    ChrTalk(
        0x103,
        "#0205FAre you giving this to us?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9570")

    label("loc_94FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9570")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_954B")

    ChrTalk(
        0x104,
        "#0305FGivin' us a gift, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9570")

    label("loc_954B")


    ChrTalk(
        0x101,
        "#0005FYou want us to keep this?\x02",
    )

    CloseMessageWindow()

    label("loc_9570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95B1")

    ChrTalk(
        0x101,
        "#0000FThanks, Coppe. We'll use it well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_95F9")

    label("loc_95B1")


    ChrTalk(
        0x101,
        (
            "#0000FThanks, Coppe. Where in the world\x01",
            "did you find this, though?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95F9")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_95FF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_963E")

    label("loc_960E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9622")
    Jump("loc_963E")

    label("loc_9622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 10)

    label("loc_963E")

    Jump("loc_84AB")

    label("loc_9643")

    Jump("loc_964B")

    label("loc_9648")

    Call(1, 10)

    label("loc_964B")

    TalkEnd(0x13)
    Return()

    # Function_9_839A end

    def Function_10_964F(): pass

    label("Function_10_964F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A47")

    ChrTalk(
        0x102,
        (
            "#0105FOh? There's a cat up here?\x02\x03",
            "#0109FYou're too adorable!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_9771")

    ChrTalk(
        0x101,
        (
            "#0000FSeems like this has been his home for\x01",
            "far longer than it's been ours.\x02\x03",
            "#0004FActually, he's probably been here since\x01",
            "the Crossbell Times stopped using this\x01",
            "place as their main office.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_982D")

    label("loc_9771")


    ChrTalk(
        0x101,
        (
            "#0000FIt's possible he's been living here before\x01",
            "any of us moved in.\x02\x03",
            "#0004FActually, he's probably been here since\x01",
            "the Crossbell Times stopped using this\x01",
            "place as their main office.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982D")


    ChrTalk(
        0x104,
        "#0309FPsst, psst! What's your name, lil' fella?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)
    Sound(823, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#0200F...\x02\x03",
            "His name is Coppe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98B5")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_98B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98D5")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_98D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_98F5")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_98F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9915")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_9915")

    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#0102FIs that a name you just came up with,\x01",
            "Tio? It's really cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FNo, I was not the one who originally\x01",
            "named him.\x02\x03",
            "#0202FAnyway, I think it would be best if\x01",
            "we stick with Coppe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0304FNo complaints here!\x02\x03",
            "#0300FLet's try and bring the guy some food\x01",
            "every now and then, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)
    Jump("loc_A061")

    label("loc_9A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9A63")

    ChrTalk(
        0x13,
        "Nyao...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B5B")

    ChrTalk(
        0x13,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9B53")

    ChrTalk(
        0x10A,
        (
            "#0605F(I'm almost certain this cat used to belong\x01",
            "to the Crossbell News Service...)\x02\x03",
            "#0603F(So, it's under the SSS's care now?\x01",
            "I'll have to update this in the First\x01",
            "Division's files.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B53")

    SetScenarioFlags(0x0, 5)
    Jump("loc_9B6B")

    label("loc_9B5B")


    ChrTalk(
        0x13,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()

    label("loc_9B6B")

    Jump("loc_A061")

    label("loc_9B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_9B8E")

    ChrTalk(
        0x13,
        "Fumyaaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8B")

    ChrTalk(
        0x13,
        "Prrrrrr, nya-go.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BFB")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_9BFB")


    ChrTalk(
        0x109,
        (
            "#0502F(Awwww. It's so cute.)\x02\x03",
            "#0506F(A cat living on the rooftop... I wonder\x01",
            "if they'd let me keep a cat over at the\x01",
            "gate, too...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9CA1")

    label("loc_9C8B")


    ChrTalk(
        0x13,
        "Prrrrrr, nya-go.\x02",
    )

    CloseMessageWindow()

    label("loc_9CA1")

    Jump("loc_A061")

    label("loc_9CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EC1")

    ChrTalk(
        0x153,
        (
            "#1105FAh! A kitty!\x02\x03",
            "#1109FIt's so cute!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FOh, that's right. KeA hasn't been\x01",
            "on the roof yet, has she?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9DBC")

    ChrTalk(
        0x102,
        (
            "#0104FWell, everyone from the street can see it.\x02\x03",
            "#0100FIt would have been irresponsible of us to\x01",
            "put KeA's safety at risk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB6")

    label("loc_9DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9E4E")

    ChrTalk(
        0x103,
        (
            "#0204FIt IS completely visible from the street.\x02\x03",
            "#0202FIt would be immature of us to put KeA\x01",
            "out in the public eye so quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB6")

    label("loc_9E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9EB6")

    ChrTalk(
        0x104,
        (
            "#0302FCheck it out, Lloyd. Everyone down there\x01",
            "can see us. Had to consider KeDo's safety.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB6")

    SetScenarioFlags(0xAE, 6)
    SetScenarioFlags(0x6A, 3)
    Jump("loc_9F04")

    label("loc_9EC1")


    ChrTalk(
        0x153,
        "#1110FHere, kitty! Come here!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x153, 500)
    Sleep(300)

    ChrTalk(
        0x13,
        "Nyayayaa～... ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_9F04")

    Jump("loc_A061")

    label("loc_9F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9F27")

    ChrTalk(
        0x13,
        "Fumyaaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9F42")

    ChrTalk(
        0x13,
        "Nyaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9F5C")

    ChrTalk(
        0x13,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9F75")

    ChrTalk(
        0x13,
        "Nyao?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9F8F")

    ChrTalk(
        0x13,
        "Nyaon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9FAD")

    ChrTalk(
        0x13,
        "Fumyaaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9FCB")

    ChrTalk(
        0x13,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_9FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A00D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_9FF9")

    ChrTalk(
        0x13,
        "Nyanyanyanya～ ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_A008")

    label("loc_9FF9")


    ChrTalk(
        0x13,
        "Nyaa～～.\x02",
    )

    CloseMessageWindow()

    label("loc_A008")

    Jump("loc_A061")

    label("loc_A00D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_A03B")

    ChrTalk(
        0x13,
        "Nyanyanyanya～ ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_A03B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_A055")

    ChrTalk(
        0x13,
        "Nya-o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A061")

    label("loc_A055")


    ChrTalk(
        0x13,
        "Nyaon?\x02",
    )

    CloseMessageWindow()

    label("loc_A061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A124")

    ChrTalk(
        0x101,
        (
            "#0004F(Coppe's made the building his home\x01",
            "and refuses to go anywhere else.)\x02\x03",
            "#0000F(He's an adamant guy, so I guess\x01",
            "it'd be nice to bring him some food\x01",
            "every now and then.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_A124")

    Return()

    # Function_10_964F end

    def Function_11_A125(): pass

    label("Function_11_A125")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_A133")
    SetScenarioFlags(0x1, 4)

    label("loc_A133")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_A141")
    SetScenarioFlags(0x1, 4)

    label("loc_A141")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_A14F")
    SetScenarioFlags(0x1, 4)

    label("loc_A14F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_A15D")
    SetScenarioFlags(0x1, 4)

    label("loc_A15D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_A16B")
    SetScenarioFlags(0x1, 4)

    label("loc_A16B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_A179")
    SetScenarioFlags(0x1, 4)

    label("loc_A179")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_A187")
    SetScenarioFlags(0x1, 4)

    label("loc_A187")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_A195")
    SetScenarioFlags(0x1, 4)

    label("loc_A195")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_A1A3")
    SetScenarioFlags(0x1, 4)

    label("loc_A1A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_A1B1")
    SetScenarioFlags(0x1, 4)

    label("loc_A1B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_A1BF")
    SetScenarioFlags(0x1, 4)

    label("loc_A1BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_A1CD")
    SetScenarioFlags(0x1, 4)

    label("loc_A1CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_A1DB")
    SetScenarioFlags(0x1, 4)

    label("loc_A1DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_A1E9")
    SetScenarioFlags(0x1, 4)

    label("loc_A1E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_A1F7")
    SetScenarioFlags(0x1, 4)

    label("loc_A1F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_A205")
    SetScenarioFlags(0x1, 4)

    label("loc_A205")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_A213")
    SetScenarioFlags(0x1, 4)

    label("loc_A213")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_A221")
    SetScenarioFlags(0x1, 4)

    label("loc_A221")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_A22F")
    SetScenarioFlags(0x1, 4)

    label("loc_A22F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_A23D")
    SetScenarioFlags(0x1, 4)

    label("loc_A23D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_A24B")
    SetScenarioFlags(0x1, 4)

    label("loc_A24B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_A259")
    SetScenarioFlags(0x1, 4)

    label("loc_A259")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_A267")
    SetScenarioFlags(0x1, 4)

    label("loc_A267")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_A275")
    SetScenarioFlags(0x1, 4)

    label("loc_A275")

    Return()

    # Function_11_A125 end

    def Function_12_A276(): pass

    label("Function_12_A276")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A287")
    Jump("loc_A3E4")

    label("loc_A287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A3E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3CF")

    ChrTalk(
        0x103,
        (
            "#0202FZeit, would you mind watching after\x01",
            "KeA while we are out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#1200FGrrrrr... Woof!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A33E")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_A33E")


    ChrTalk(
        0x109,
        (
            "#0508F(Uh, I'm not exactly the biggest dog person.)\x02\x03",
            "#0505F(Though, I guess he's technically a wolf\x01",
            "and not just a really big dog.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A3E4")

    label("loc_A3CF")


    ChrTalk(
        0x14,
        "#1200FGrrrrr...\x02",
    )

    CloseMessageWindow()

    label("loc_A3E4")

    TalkEnd(0xFE)
    Return()

    # Function_12_A276 end

    def Function_13_A3E8(): pass

    label("Function_13_A3E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A3F9")
    Jump("loc_A587")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4FC")
    OP_93(0xFE, 0x0, 0x0)

    ChrTalk(
        0x15,
        (
            "#1110FYou're sooo warm, Zeit!\x02\x03",
            "#1109FLet's take a nap together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#1200FGrrrrrrr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#0509F(S-So precious!)\x02\x03",
            "#0502F(I'm starting to understand why\x01",
            "everyone loves KeA so much.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0012F(Yeah. She's a good kid.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A587")

    label("loc_A4FC")


    ChrTalk(
        0x15,
        (
            "#1110FOh, yeah! Have a nice trip, everyone!\x02\x03",
            "#1109FBeat up those stupid, dumb ghosts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0109FO-Oh, right. We'll do our best, KeA!\x02",
    )

    CloseMessageWindow()

    label("loc_A587")

    TalkEnd(0xFE)
    Return()

    # Function_13_A3E8 end

    def Function_14_A58B(): pass

    label("Function_14_A58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A68E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_A605")

    ChrTalk(
        0xFE,
        (
            "Graaaaaace! What are we going\x01",
            "to do about the manuscript?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, you gotta help me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A689")

    label("loc_A605")


    ChrTalk(
        0xFE,
        (
            "Sweet Aidios, there's no trace of that\x01",
            "woman anywhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll never be able to finish this article\x01",
            "on time without her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_A689")

    Jump("loc_A783")

    label("loc_A68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_A6EE")

    ChrTalk(
        0xFE,
        "Where are you, Grace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She better not be hanging\x01",
            "out in some bar again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A783")

    label("loc_A6EE")


    ChrTalk(
        0xFE,
        (
            "Honestly, how could someone like\x01",
            "Grace get as far as she has in life?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She's off doing who knows what\x01",
            "while the deadline is almost here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_A783")

    TalkEnd(0xFE)
    Return()

    # Function_14_A58B end

    def Function_15_A787(): pass

    label("Function_15_A787")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SoundLoad(803)
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    SetChrPos(0x101, 1420, 0, -14130, 0)
    SetChrPos(0x102, -290, 0, -16530, 45)
    SetChrPos(0x103, -700, 0, -14800, 90)
    SetChrPos(0x104, 1500, 0, -16379, 0)
    OP_68(-660, 3000, 3390, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16370, 0)
    MoveCamera(35, 3, 0, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-21970, 1900, 6540, 0)
    MoveCamera(351, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14980, 0)
    MoveCamera(356, 8, 0, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(19900, 3000, 6130, 0)
    MoveCamera(57, 4, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)
    MoveCamera(55, -2, 0, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-60, 5700, 23250, 0)
    MoveCamera(359, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11620, 0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_6F(0x79)
    OP_68(-5540, 4000, 5000, 10000)
    MoveCamera(24, 29, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(35000, 10000)
    Sleep(2000)
    PlaceName2(340, 200, "c_plac02", 0x0, 1500)
    OP_6F(0x79)
    EndChrThread(0x23, 0x1)

    ChrTalk(
        0x104,
        "#0300FWhew. This place is as busy as ever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0004FWell, that's no surprise, given how this\x01",
            "is more or less the heart of the city.\x02\x03",
            "#0000FJust look at these stores and restaurants.\x01",
            "You can get all your essentials here.\x02\x03",
            "It also acts as a hub leading to other\x01",
            "districts, if you're in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FAnd it's only gotten busier with the recent\x01",
            "surge in orbal vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0002FSure looks that way.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x23, 1, 0, 56)
    Fade(500)
    OP_68(190, 1500, -15740, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#0000FOkay, everyone. How about we drop by\x01",
            "the orbal store next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0305FYou mean that orbal factory the chief\x01",
            "mentioned?\x02\x03",
            "#0300FWord around town is that the whole place\x01",
            "got a huge makeover. Real fancy now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FIndeed. This new type of factory focuses\x01",
            "more on commercialized orbal products.\x02\x03",
            "#0200FThey have a formal contract with the CPD,\x01",
            "as well. We should be able to rely on them\x01",
            "for any of our orbal needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0104F#6PWe'll soon become regulars there,\x01",
            "if that's the case.\x02\x03",
            "#0100FSo, should we stop by there before\x01",
            "going to the other districts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000FYeah. It should be that corner building\x01",
            "over there.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Central Square includes a department store,\x01",
            "orbal factory, armory, and restaurant.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Since almost everything you need is available here,\x01",
            "it's a good idea to visit if you ever need to stock up.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Genten, the city's orbal store, is located on\x01",
            "Central Square's eastern side.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -290, 0, -16530, 45)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x44, 4)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_A787 end

    def Function_16_AF19(): pass

    label("Function_16_AF19")

    EventBegin(0x1)
    SetChrPos(0x18, -6460, -4200, -21000, 135)

    def lambda_AF31():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF31)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02C")

    ChrTalk(
        0x101,
        (
            "#0005FHold on, guys. The armory should be\x01",
            "right over there.\x02\x03",
            "#0000FThe chief seemed pretty adamant that\x01",
            "we check it out.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AFD8():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AFD8)

    def lambda_AFE5():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AFE5)

    def lambda_AFF2():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFF2)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#0100FShall we take a look?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B1CA")

    label("loc_B02C")


    ChrTalk(
        0x101,
        (
            "#0005FHold on, guys. The armory should be\x01",
            "right over there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B072():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B072)

    def lambda_B07F():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B07F)

    def lambda_B08C():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B08C)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B130")

    ChrTalk(
        0x103,
        (
            "#0203FIndeed it is.\x02\x03",
            "#0200FMaintaining weapon condition is not something\x01",
            "to take lightly. We should visit while we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1CA")

    label("loc_B130")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B18D")

    ChrTalk(
        0x104,
        (
            "#0305FLooks like it.\x02\x03",
            "#0300FShould probably stop by there first, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1CA")

    label("loc_B18D")


    ChrTalk(
        0x102,
        (
            "#0105FOh, I nearly forgot.\x02\x03",
            "#0100FShall we take a look?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1CA")

    SetScenarioFlags(0x1, 3)
    Jump("loc_B249")

    label("loc_B1D2")


    ChrTalk(
        0x101,
        (
            "#0000FThat armory the chief mentioned should\x01",
            "be right over there.\x02\x03",
            "He seemed pretty adamant that we check it\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B249")

    SetChrPos(0x0, -8660, -4200, -18220, 180)
    EventEnd(0x4)
    Return()

    # Function_16_AF19 end

    def Function_17_B25D(): pass

    label("Function_17_B25D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_68(-640, 1500, 12830, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 0, 0, 14500, 180)
    SetChrPos(0x19F, 750, 0, 13750, 270)
    SetChrPos(0x109, 750, 0, 12750, 315)
    SetChrPos(0x102, -1250, 0, 14250, 135)
    SetChrPos(0x103, -1500, 0, 13000, 90)
    SetChrPos(0x104, -1250, 0, 12000, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#0000FWell, we should probably hurry and pick out\x01",
            "Fran's present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FWe're almost out of time, Lloyd!\x02\x03",
            "#0300FFran's gonna show up at the\x01",
            "restaurant any minute now, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#0103FRandy's right, Lloyd. Since he invited\x01",
            "her, making her wait wouldn't be very\x01",
            "polite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        "#11PWh-What do we do, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI propose we divide into two teams.\x02\x03",
            "#0200FElie, Randy, and I will go to the restaurant\x01",
            "in advance.\x02\x03",
            "Once there, we will explain to Fran that this\x01",
            "so-called 'rendezvous' is slightly delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#0003FAnd in the meantime, Noel and I can help\x01",
            "Anton pick out a present.\x02\x03",
            "#0000FI think that'd be the most efficient course\x01",
            "of action at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PI can't thank you enough, everyone.\x01",
            "For everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19F,
        (
            "#11PI'm truly blessed to have met such\x01",
            "kind and charitable people...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#11P#0506FPlease don't start crying. I beg you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        (
            "#5P#0003FA-Anyway, let's go with Tio's plan.\x02\x03",
            "#0000FI'm counting on you guys.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B759():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B759)

    def lambda_B766():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B766)

    def lambda_B773():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B773)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x102,
        "#5P#0100FLeave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FTry to be brief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FBetter arrive with a present that'll knock\x01",
            "her dead! Y'know, with happiness.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B825():
        OP_97(0x103, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B825)
    Sleep(50)

    def lambda_B842():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B842)
    Sleep(50)

    def lambda_B85F():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B85F)

    def lambda_B879():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B879)

    def lambda_B886():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B886)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    def lambda_B8A7():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8A7)
    Sleep(50)

    def lambda_B8B7():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B8B7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    ChrTalk(
        0x101,
        (
            "#5P#0000FWe're running on borrowed time,\x01",
            "so let's get to the department store.\x02\x03",
            "Anton, keep your eyes peeled.\x01",
            "Sergeant Major, speak up if you\x01",
            "see something Fran might like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#0506F*sigh* I don't suppose I have\x01",
            "any other choice.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19F, 0x109, 500)

    ChrTalk(
        0x19F,
        "#11PI'm in your debt, dear sister!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10, 2700, 26140, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 800, 24000, 0)
    SetChrPos(0x109, 750, 800, 23250, 0)
    SetChrPos(0x19F, -750, 800, 22500, 0)

    def lambda_BA52():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA52)
    Sleep(50)

    def lambda_BA6F():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BA6F)
    Sleep(50)

    def lambda_BA8C():
        OP_97(0x19F, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_BA8C)
    OP_0D()
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    Sleep(750)

    def lambda_BAC2():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BAC2)
    Sleep(50)

    def lambda_BAD6():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BAD6)
    Sleep(50)

    def lambda_BAEA():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_BAEA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x19F, 0x1)
    EndChrThread(0x19F, 0x2)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_29(0x2A, 0x1, 0x3)
    NewScene("c0170", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_B25D end

    SaveToFile()

Try(main)
