from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c100b.bin",                # FileName
        "c100b",                    # MapName
        "c100b",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 1, 0, 2],
    )

    BuildStringList((
        "c100b",                  # 0
        "Zeit",                   # 1
        "Receptionist Michel",    # 2
        "SE制御",                 # 3
        "Central Square",         # 4
        "West Street",            # 5
        "Administrative District",# 6
        "Residential District",   # 7
        "Entertainment District", # 8
        "East Street",            # 9
        "Downtown District",      # 10
        "Harbor District",        # 11
        "IBC",                    # 12
        "Station Street",         # 13
        "Back Alley",             # 14
        "Ursula Road",            # 15
        "East Crossbell Highway", # 16
        "West Crossbell Highway", # 17
        "Mainz Mountain Path",    # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "West Street")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "Administrative District")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "Residential District")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "East Street")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "Downtown District")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "Harbor District")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "IBC")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "Station Street")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "Back Alley")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "Ursula Road")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_35C",          # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_388",          # 02, 2
        "Function_3_3A9",          # 03, 3
        "Function_4_B40",          # 04, 4
        "Function_5_B84",          # 05, 5
        "Function_6_BC8",          # 06, 6
        "Function_7_C0C",          # 07, 7
        "Function_8_C50",          # 08, 8
        "Function_9_CE4",          # 09, 9
        "Function_10_D0A",         # 0A, 10
        "Function_11_D5A",         # 0B, 11
    ))


    def Function_0_35C(): pass

    label("Function_0_35C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_35C")

    label("loc_377")

    Return()

    # Function_0_35C end

    def Function_1_378(): pass

    label("Function_1_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_387")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)

    label("loc_387")

    Return()

    # Function_1_378 end

    def Function_2_388(): pass

    label("Function_2_388")

    SetMapObjFrame(0xFF, "guild02a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "guild02b", 0x0, 0x1)
    Return()

    # Function_2_388 end

    def Function_3_3A9(): pass

    label("Function_3_3A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch09100.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    OP_68(-18700, 700, 13700, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    OP_90(0x101, -29700, -300, 13700, 90)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, -31700, -300, 14800, 90)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    OP_90(0x103, -30900, -300, 15900, 90)
    OP_90(0x104, -30900, -300, 13300, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -33000, -300, 15200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -7600, 330, 14000, 225)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "guild02a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "guild02b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "guild01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "guild01b", 0x0, 0x1)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 8)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    Fade(500)
    OP_68(-9600, 2700, 12000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-9600, 700, 12000, 3000)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x8, 3)
    OP_6F(0x1)

    ChrTalk(
        0x102,
        "#5200245V#0108F#6POh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200246V#6P#0301FDamn. They got hit hard.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Shizuku",
        "#5200247V#5P#6008FF-Father...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)

    def lambda_65C():
        OP_96(0xFE, 0xFFFFDF30, 0xFFFFFF6A, 0x3390, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_65C)

    def lambda_676():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_676)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        "#5200248V#11POh, it's you guys?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Shizuku",
        "#5200249V#5P#6005FMr. Michel?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200250V#6P#0002FThank goodness...\x01",
            "How's the situation here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200251V#11PI'm fine, fortunately.\x01",
            "I managed to make my escape during\x01",
            "the attack and hid until they finished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200252V#11PI snuck back into the guildhouse\x01",
            "after they left, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200253V#11PI doubt they've left the city already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5200254V#6P#0013FYeah, there's a commotion in the middle\x01",
            "of the Administrative District.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd gave a brief explanation of the\x01",
            "current situation to Michel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x9,
        "#5200255V#11PI see. So that's what's going on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200256V#11PY'know, it's about time for the bracers\x01",
            "to return to the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5200257V#11PI'll send in reinforcements immediately upon\x01",
            "their return, so make haste for the highway!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200258V#11PI'll leave Shizuku in your care!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5200259V#6P#0300FRoger that, pal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5200260V#6P#0000FYeah, leave it to us!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x104,
        "Shizuku",
        (
            "#5200261V#5P#6010FMr. Michel...\x01",
            "Please be careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5200262V#11PYep. The same goes to you, little one!\x02",
    )

    CloseMessageWindow()
    OP_68(-7600, 700, 10000, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_AD4():

        label("loc_AD4")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_AD4")

    QueueWorkItem2(0x9, 2, lambda_AD4)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x11)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xA, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3A9 end

    def Function_4_B40(): pass

    label("Function_4_B40")


    def lambda_B45():
        OP_95(0xFE, -14700, -300, 13700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B45)
    WaitChrThread(0x101, 1)

    def lambda_B63():
        OP_95(0xFE, -10300, -300, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B63)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_4_B40 end

    def Function_5_B84(): pass

    label("Function_5_B84")


    def lambda_B89():
        OP_95(0xFE, -15900, -300, 13300, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B89)
    WaitChrThread(0x104, 1)

    def lambda_BA7():
        OP_95(0xFE, -11500, -300, 9900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA7)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_5_B84 end

    def Function_6_BC8(): pass

    label("Function_6_BC8")


    def lambda_BCD():
        OP_95(0xFE, -16700, -300, 14800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BCD)
    WaitChrThread(0x102, 1)

    def lambda_BEB():
        OP_95(0xFE, -12300, -300, 11400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEB)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_6_BC8 end

    def Function_7_C0C(): pass

    label("Function_7_C0C")


    def lambda_C11():
        OP_95(0xFE, -15900, -300, 15900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C11)
    WaitChrThread(0x103, 1)

    def lambda_C2F():
        OP_95(0xFE, -11500, -300, 12500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C2F)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_7_C0C end

    def Function_8_C50(): pass

    label("Function_8_C50")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_C7F():
        OP_95(0xFE, -18000, -300, 14200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C7F)
    WaitChrThread(0x8, 1)

    def lambda_C9D():
        OP_95(0xFE, -13600, -300, 10800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C9D)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x8, 0x5A, 0x1F4)
    Return()

    # Function_8_C50 end

    def Function_9_CE4(): pass

    label("Function_9_CE4")

    OP_93(0xFE, 0x87, 0x1F4)

    def lambda_CF0():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CF0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_CE4 end

    def Function_10_D0A(): pass

    label("Function_10_D0A")

    OP_93(0xFE, 0x87, 0x1F4)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_D40():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D40)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_D0A end

    def Function_11_D5A(): pass

    label("Function_11_D5A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D73")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_D5A")

    label("loc_D73")

    Return()

    # Function_11_D5A end

    SaveToFile()

Try(main)
