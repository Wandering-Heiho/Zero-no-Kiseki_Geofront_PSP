from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t053b.bin",                # FileName
        "t053b",                    # MapName
        "t053b",                    # Location
        0x0040,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t053b",                  # 0
        "Baeckerei",              # 1
        "Kimmy",                  # 2
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
    ))

    DeclNpc(-129,    0,       3640,    225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-2009,   0,       2130,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_1D1",          # 02, 2
        "Function_3_1D2",          # 03, 3
        "Function_4_1D6",          # 04, 4
        "Function_5_44A",          # 05, 5
        "Function_6_57E",          # 06, 6
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_158"),
        (1, "loc_164"),
        (2, "loc_170"),
        (3, "loc_17C"),
        (4, "loc_188"),
        (5, "loc_194"),
        (6, "loc_1A0"),
        (SWITCH_DEFAULT, "loc_1AC"),
    )


    label("loc_158")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_164")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_170")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_17C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_188")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_194")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B8")

    label("loc_1CF")

    Return()

    # Function_0_118 end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Return()

    # Function_1_1D0 end

    def Function_2_1D1(): pass

    label("Function_2_1D1")

    Return()

    # Function_2_1D1 end

    def Function_3_1D2(): pass

    label("Function_3_1D2")

    Call(0, 4)
    Return()

    # Function_3_1D2 end

    def Function_4_1D6(): pass

    label("Function_4_1D6")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_446")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_253")
    OP_AF(0x56)
    Jump("loc_275")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_263")
    OP_AF(0x55)
    Jump("loc_275")

    label("loc_263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_273")
    OP_AF(0x57)
    Jump("loc_275")

    label("loc_273")

    OP_AF(0x55)

    label("loc_275")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_441")

    label("loc_284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298")
    Jump("loc_441")

    label("loc_298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")

    ChrTalk(
        0x8,
        (
            "You've got guts. No one in their right mind\x01",
            "goes outside at night, nowadays.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "C'mon, you buyin' something? And don't\x01",
            "give me any of those, 'Oh, we're just\x01",
            "looking around!' excuses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_441")

    label("loc_381")


    ChrTalk(
        0x8,
        "Tell me what you want and you got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Listen here. I could be spending time with my amazing\x01",
            "daughter, so if you really are 'just looking around,'\x01",
            "I'm not going to be a happy camper.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_441")

    Jump("loc_1E3")

    label("loc_446")

    TalkEnd(0x8)
    Return()

    # Function_4_1D6 end

    def Function_5_44A(): pass

    label("Function_5_44A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")
    OP_93(0xFE, 0x2D, 0x0)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        "Daddy, it's soooo late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's for dinner? I'm starving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, only your favorite, Kimmy!\x01",
            "My homemade hamburgers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Woohoo! I love those the mostest!\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_57A")

    label("loc_514")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "Daddy may be really strict to everyone else,\x01",
            "but he's super nice to me. I love him a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A")

    TalkEnd(0xFE)
    Return()

    # Function_5_44A end

    def Function_6_57E(): pass

    label("Function_6_57E")

    Return()

    # Function_6_57E end

    SaveToFile()

Try(main)
