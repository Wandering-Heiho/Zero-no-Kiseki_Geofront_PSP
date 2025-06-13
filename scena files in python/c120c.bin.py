from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120c.bin",                # FileName
        "c120c",                    # MapName
        "c120c",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 10, 0, 11],
    )

    BuildStringList((
        "c120c",                  # 0
        "Cunha",                  # 1
        "Ozelle",                 # 2
        "Bishop",                 # 3
        "Old Man Quine",          # 4
        "Amisa",                  # 5
        "Grace",                  # 6
        "Reins",                  # 7
        "Cruise Ship Guide",      # 8
        "Mithra",                 # 9
        "Yaqi",                   # 10
        "Misa",                   # 11
        "BOA Officer",            # 12
        "Program Director",       # 13
        "BOA Clerk",              # 14
        "Roy",                    # 15
        "Roy",                    # 16
        "Meiling",                # 17
        "Meiling",                # 18
        "Chairman Mors",          # 19
        "Parla",                  # 20
        "Momo",                   # 21
        "Elsa",                   # 22
        "Detective Emma",         # 23
        "Anton",                  # 24
        "Ricky",                  # 25
        "Tourist",                # 26
        "Boy",                    # 27
        "Tourist",                # 28
        "Tourist",                # 29
        "Tourist",                # 30
        "Tourist",                # 31
        "Girl",                   # 32
        "Tourist",                # 33
        "Tourist",                # 34
        "Aretha",                 # 35
        "Stefan",                 # 36
        "Street Performer",       # 37
        "Singer",                 # 38
        "Wald",                   # 39
        "Luganov",                # 40
        "Jed",                    # 41
        "Huey",                   # 42
        "Slash",                  # 43
        "Kilika",                 # 44
        "Lechter",                # 45
        "Cruise Ship",            # 46
        "Estelle",                # 47
        "Joshua",                 # 48
        "Wazy",                   # 49
        "Abbas",                  # 50
        "Testament",              # 51
        "Testament",              # 52
        "Testament",              # 53
        "Testament",              # 54
        "Testament",              # 55
        "Viper",                  # 56
        "Viper",                  # 57
        "Viper",                  # 58
        "Viper",                  # 59
        "Viper",                  # 60
        "Guest",                  # 61
        "Guest",                  # 62
        "Guest",                  # 63
        "Guest",                  # 64
        "Guest",                  # 65
        "Guest",                  # 66
        "Guest",                  # 67
        "Guest",                  # 68
        "Guest",                  # 69
        "Guest",                  # 70
        "Young Man",              # 71
        "Young Man",              # 72
        "Officer",                # 73
        "Officer",                # 74
        "Zeit",                   # 75
        "SE制御",                 # 76
        "Central Square",         # 77
        "West Street",            # 78
        "Administrative District",# 79
        "Residential District",   # 80
        "Entertainment District", # 81
        "East Street",            # 82
        "Downtown District",      # 83
        "Harbor District",        # 84
        "IBC",                    # 85
        "Station Street",         # 86
        "Back Alley",             # 87
        "Ursula Road",            # 88
        "East Crossbell Highway", # 89
        "West Crossbell Highway", # 90
        "Mainz Mountain Path",    # 91
    ))

    AddCharChip((
        "chr/ch22100.itc",                   # 00
        "chr/ch25200.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "apl/ch50168.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch28100.itc",                   # 05
        "chr/ch06000.itc",                   # 06
        "chr/ch34600.itc",                   # 07
        "chr/ch27000.itc",                   # 08
        "chr/ch21200.itc",                   # 09
        "chr/ch22800.itc",                   # 0A
        "chr/ch23200.itc",                   # 0B
        "chr/ch27600.itc",                   # 0C
        "chr/ch27602.itc",                   # 0D
        "chr/ch32200.itc",                   # 0E
        "chr/ch32500.itc",                   # 0F
        "chr/ch24200.itc",                   # 10
        "chr/ch24600.itc",                   # 11
        "chr/ch22000.itc",                   # 12
        "chr/ch21000.itc",                   # 13
        "chr/ch24500.itc",                   # 14
        "chr/ch21900.itc",                   # 15
        "chr/ch23900.itc",                   # 16
        "chr/ch21300.itc",                   # 17
        "chr/ch20300.itc",                   # 18
        "chr/ch20600.itc",                   # 19
        "chr/ch20800.itc",                   # 1A
        "chr/ch20900.itc",                   # 1B
        "chr/ch21202.itc",                   # 1C
        "chr/ch21502.itc",                   # 1D
        "chr/ch20700.itc",                   # 1E
        "chr/ch30500.itc",                   # 1F
        "chr/ch37300.itc",                   # 20
        "chr/ch37400.itc",                   # 21
        "chr/ch02100.itc",                   # 22
        "chr/ch30800.itc",                   # 23
        "chr/ch31700.itc",                   # 24
        "chr/ch10400.itc",                   # 25
        "chr/ch27100.itc",                   # 26
    ))

    DeclNpc(-3519,   0,       8720,    90,   257,  0x0, 0,   0,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   257,  0x0, 0,   2,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  180,  277,  0x0, 0,   3,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(38439,   -2490,   -18079,  135,  261,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(180,     -680,    4130,    135,  389,  0x0, 0,   6,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1590,    -699,    3920,    135,  389,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(42450,   -2500,   2329,    235,  261,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(15300,   0,       12979,   180,  261,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(19780,   0,       -3299,   270,  261,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(19780,   0,       -6090,   270,  261,  0x0, 0,   38,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-16500,  0,       -9050,   180,  277,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(5539,    -699,    1009,    270,  261,  0x0, 0,   5,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-15890,  0,       -6059,   225,  261,  0x0, 0,   13,  0,   255, 255, 0,   26,  255,  0)
    DeclNpc(-17450,  0,       -9449,   135,  405,  0x0, 0,   9,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-15890,  0,       -6059,   225,  469,  0x0, 0,   28,  0,   255, 255, 0,   30,  255,  0)
    DeclNpc(-18590,  0,       -699,    225,  389,  0x0, 0,   4,   0,   0,   3,   0,   31,  255,  0)
    DeclNpc(-14390,  0,       -7840,   225,  469,  0x0, 0,   29,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-16149,  0,       -10960,  0,    277,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(-17540,  0,       -11369,  45,   405,  0x0, 0,   27,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(21450,   0,       3299,    0,    389,  0x0, 0,   30,  0,   0,   0,   0,   44,  255,  0)
    DeclNpc(21450,   0,       4690,    180,  389,  0x0, 0,   37,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-17799,  0,       13369,   180,  389,  0x0, 0,   31,  0,   0,   0,   0,   46,  255,  0)
    DeclNpc(-5380,   2000,    20700,   180,  261,  0x0, 0,   32,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(-6130,   2000,    22040,   180,  261,  0x0, 0,   33,  0,   0,   0,   0,   48,  255,  0)
    DeclNpc(-7289,   -9,      -8520,   270,  261,  0x0, 0,   16,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(-9149,   -9,      -8520,   90,   261,  0x0, 0,   17,  0,   0,   0,   0,   36,  255,  0)
    DeclNpc(-17909,  0,       920,     45,   261,  0x0, 0,   18,  0,   0,   9,   0,   37,  255,  0)
    DeclNpc(829,     -699,    1980,    90,   261,  0x0, 0,   19,  0,   0,   0,   0,   38,  255,  0)
    DeclNpc(300,     -699,    -1679,   90,   261,  0x0, 0,   20,  0,   0,   0,   0,   39,  255,  0)
    DeclNpc(1169,    -699,    -3099,   45,   261,  0x0, 0,   21,  0,   0,   0,   0,   40,  255,  0)
    DeclNpc(1870,    -699,    -3809,   45,   261,  0x0, 0,   22,  0,   0,   0,   0,   41,  255,  0)
    DeclNpc(40790,   -2500,   -1309,   315,  389,  0x0, 0,   23,  0,   0,   0,   0,   42,  255,  0)
    DeclNpc(40000,   -2500,   0,       135,  389,  0x0, 0,   9,   0,   0,   0,   0,   43,  255,  0)
    DeclNpc(27329,   0,       12109,   90,   389,  0x0, 0,   24,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(27329,   0,       10479,   90,   389,  0x0, 0,   25,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(8250,    100,     79,      270,  453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(8250,    100,     79,      270,  453,  0x0, 0,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(150,     0,       -9970,   180,  389,  0x0, 0,   34,  0,   0,   0,   0,   50,  255,  0)
    DeclNpc(-1929,   0,       -10229,  270,  389,  0x0, 0,   35,  0,   0,   0,   0,   51,  255,  0)
    DeclNpc(330,     0,       -11890,  0,    389,  0x0, 0,   36,  0,   0,   0,   0,   52,  255,  0)
    DeclNpc(-1399,   0,       -11710,  45,   405,  0x0, 0,   36,  0,   0,   0,   0,   54,  255,  0)
    DeclNpc(1450,    0,       -11210,  90,   405,  0x0, 0,   35,  0,   0,   0,   0,   55,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 58,  33.0,                  0.0,                   -3.5,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -11.0,                 -0.0,                  0.699999988079071,     1.0])
    DeclEvent(0x0000, 0, 65,  -10.0,                 22.5,                  1.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.3333334922790527,    -2.25,                 -0.20000000298023224,  1.0])
    DeclEvent(0x0000, 0, 66,  -20.0,                 -17.0,                 -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.0,                   5.6666669845581055,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 65,  -14.5,                 18.0,                  0.0,                   56.25,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.9000000953674316,    -6.0,                  -0.0,                  1.0])

    DeclActor(19200,   250,     20500,   2000,    19200,   1250,    20500,   0x007C, 0,  86, 0x0000)
    DeclActor(68620,   -2500,   15400,   1200,    68040,   -3500,   11820,   0x007C, 0,  56, 0x0000)
    DeclActor(34000,   -2500,   3400,    1500,    34000,   -1500,   3400,    0x007C, 0,  57, 0x0000)
    DeclActor(77440,   -2500,   19770,   1200,    77440,   -1000,   19770,   0x007C, 0,  85, 0x0000)
    DeclActor(-16630,  0,       -6860,   1200,    -15890,  1500,    -6060,   0x007E, 0,  25, 0x0000)
    DeclActor(-14890,  0,       -8480,   1200,    -14390,  1200,    -7840,   0x007E, 0,  32, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "Central Square")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "West Street")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "Administrative District")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "Residential District")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "East Street")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "Downtown District")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "Harbor District")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "IBC")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "Station Street")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "Back Alley")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "Ursula Road")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "Mainz Mountain Path")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_F78",          # 00, 0
        "Function_1_1030",         # 01, 1
        "Function_2_10A5",         # 02, 2
        "Function_3_11DF",         # 03, 3
        "Function_4_120A",         # 04, 4
        "Function_5_1235",         # 05, 5
        "Function_6_12D2",         # 06, 6
        "Function_7_12FD",         # 07, 7
        "Function_8_137A",         # 08, 8
        "Function_9_13A0",         # 09, 9
        "Function_10_13CB",        # 0A, 10
        "Function_11_1D94",        # 0B, 11
        "Function_12_2021",        # 0C, 12
        "Function_13_23BE",        # 0D, 13
        "Function_14_2C2F",        # 0E, 14
        "Function_15_3053",        # 0F, 15
        "Function_16_3342",        # 10, 16
        "Function_17_363D",        # 11, 17
        "Function_18_36A3",        # 12, 18
        "Function_19_3ACA",        # 13, 19
        "Function_20_3D3B",        # 14, 20
        "Function_21_4726",        # 15, 21
        "Function_22_4F7D",        # 16, 22
        "Function_23_56D7",        # 17, 23
        "Function_24_5DE8",        # 18, 24
        "Function_25_6380",        # 19, 25
        "Function_26_6395",        # 1A, 26
        "Function_27_6D3D",        # 1B, 27
        "Function_28_6E36",        # 1C, 28
        "Function_29_6ED5",        # 1D, 29
        "Function_30_72DF",        # 1E, 30
        "Function_31_7865",        # 1F, 31
        "Function_32_7898",        # 20, 32
        "Function_33_7CFD",        # 21, 33
        "Function_34_8A7A",        # 22, 34
        "Function_35_8B1B",        # 23, 35
        "Function_36_8D4B",        # 24, 36
        "Function_37_8EA2",        # 25, 37
        "Function_38_9142",        # 26, 38
        "Function_39_9450",        # 27, 39
        "Function_40_95A5",        # 28, 40
        "Function_41_97A6",        # 29, 41
        "Function_42_99F5",        # 2A, 42
        "Function_43_9A97",        # 2B, 43
        "Function_44_9B45",        # 2C, 44
        "Function_45_9C94",        # 2D, 45
        "Function_46_9F1A",        # 2E, 46
        "Function_47_A60A",        # 2F, 47
        "Function_48_ADFB",        # 30, 48
        "Function_49_B520",        # 31, 49
        "Function_50_B6D5",        # 32, 50
        "Function_51_B9C9",        # 33, 51
        "Function_52_BAAF",        # 34, 52
        "Function_53_BB8A",        # 35, 53
        "Function_54_BC57",        # 36, 54
        "Function_55_BD71",        # 37, 55
        "Function_56_BE6F",        # 38, 56
        "Function_57_BF66",        # 39, 57
        "Function_58_C7E3",        # 3A, 58
        "Function_59_D400",        # 3B, 59
        "Function_60_F5E4",        # 3C, 60
        "Function_61_F613",        # 3D, 61
        "Function_62_F665",        # 3E, 62
        "Function_63_F6B7",        # 3F, 63
        "Function_64_F704",        # 40, 64
        "Function_65_F796",        # 41, 65
        "Function_66_F8B2",        # 42, 66
        "Function_67_F9CE",        # 43, 67
        "Function_68_FA12",        # 44, 68
        "Function_69_FA42",        # 45, 69
        "Function_70_FA86",        # 46, 70
        "Function_71_FAB6",        # 47, 71
        "Function_72_FCD1",        # 48, 72
        "Function_73_131B6",       # 49, 73
        "Function_74_1323B",       # 4A, 74
        "Function_75_135D2",       # 4B, 75
        "Function_76_14387",       # 4C, 76
        "Function_77_14B20",       # 4D, 77
        "Function_78_178C2",       # 4E, 78
        "Function_79_1907F",       # 4F, 79
        "Function_80_19183",       # 50, 80
        "Function_81_1919F",       # 51, 81
        "Function_82_191C2",       # 52, 82
        "Function_83_198CE",       # 53, 83
        "Function_84_19EE1",       # 54, 84
        "Function_85_19F07",       # 55, 85
        "Function_86_19FBD",       # 56, 86
    ))


    def Function_0_F78(): pass

    label("Function_0_F78")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_FB8"),
        (1, "loc_FC4"),
        (2, "loc_FD0"),
        (3, "loc_FDC"),
        (4, "loc_FE8"),
        (5, "loc_FF4"),
        (6, "loc_1000"),
        (SWITCH_DEFAULT, "loc_100C"),
    )


    label("loc_FB8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FC4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FD0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FDC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FE8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_FF4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1000")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_100C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_1018")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_102F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1018")

    label("loc_102F")

    Return()

    # Function_0_F78 end

    def Function_1_1030(): pass

    label("Function_1_1030")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10A4")
    OP_95(0xFE, 17490, 0, 8720, 1000, 0x0)
    OP_95(0xFE, 17490, 0, -4030, 1000, 0x0)
    OP_95(0xFE, 12440, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, -8720, 1000, 0x0)
    OP_95(0xFE, -3520, 0, 8720, 1000, 0x0)
    Jump("Function_1_1030")

    label("loc_10A4")

    Return()

    # Function_1_1030 end

    def Function_2_10A5(): pass

    label("Function_2_10A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11DE")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, 1760, 5080, 38700, 10000, 0x0)
    Sleep(3000)
    OP_95(0xFE, 1760, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 8000, 0x0)
    OP_95(0xFE, -13000, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 8000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 8000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 8000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 8000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 8000, 0x0)
    Jump("Function_2_10A5")

    label("loc_11DE")

    Return()

    # Function_2_10A5 end

    def Function_3_11DF(): pass

    label("Function_3_11DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1209")
    OP_94(0xFE, 0xFFFFB9BA, 0x992, 0xFFFFB118, 0xFFFFF628, 0x3E8)
    Sleep(300)
    Jump("Function_3_11DF")

    label("loc_1209")

    Return()

    # Function_3_11DF end

    def Function_4_120A(): pass

    label("Function_4_120A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1234")
    OP_94(0xFE, 0xA5FA, 0xFFFFCAA4, 0x965A, 0xFFFFB73A, 0x320)
    Sleep(700)
    Jump("Function_4_120A")

    label("loc_1234")

    Return()

    # Function_4_120A end

    def Function_5_1235(): pass

    label("Function_5_1235")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D1")
    OP_95(0xFE, -17830, 0, -4570, 1000, 0x0)
    OP_95(0xFE, -13440, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 12710, 0, -9920, 1000, 0x0)
    OP_95(0xFE, 18920, 0, -4320, 1000, 0x0)
    OP_95(0xFE, 18920, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -13010, 0, 9980, 1000, 0x0)
    OP_95(0xFE, -17820, 0, 4570, 1000, 0x0)
    Jump("Function_5_1235")

    label("loc_12D1")

    Return()

    # Function_5_1235 end

    def Function_6_12D2(): pass

    label("Function_6_12D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12FC")
    OP_94(0xFE, 0x1F22, 0x546, 0x7D9, 0xFFFFF7FE, 0x3E8)
    Sleep(300)
    Jump("Function_6_12D2")

    label("loc_12FC")

    Return()

    # Function_6_12D2 end

    def Function_7_12FD(): pass

    label("Function_7_12FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1379")
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(6000)
    Jump("Function_7_12FD")

    label("loc_1379")

    Return()

    # Function_7_12FD end

    def Function_8_137A(): pass

    label("Function_8_137A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_139F")
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sleep(1000)
    Jump("Function_8_137A")

    label("loc_139F")

    Return()

    # Function_8_137A end

    def Function_9_13A0(): pass

    label("Function_9_13A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13CA")
    OP_94(0xFE, 0xFFFFB46A, 0x730, 0xFFFFBE92, 0xFFFFFD08, 0x3E8)
    Sleep(300)
    Jump("Function_9_13A0")

    label("loc_13CA")

    Return()

    # Function_9_13A0 end

    def Function_10_13CB(): pass

    label("Function_10_13CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15FD")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148D")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1460")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_147F")

    label("loc_1460")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147F")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_147F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_148D")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_155C")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_152F")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_154E")

    label("loc_152F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154E")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_154E")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15FD")

    label("loc_155C")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D5")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_15F4")

    label("loc_15D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F4")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_15F4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15FD")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16B3")
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x10)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x13, 1230, -690, 3680, 135)
    ClearChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x15, -18840, 0, -5150, 180)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    ClearChrFlags(0x15, 0x10)
    SetChrPos(0x21, 37750, -2500, 1640, 90)
    SetChrPos(0x22, 37750, -2500, 240, 90)
    SetChrFlags(0x25, 0x10)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 7780, 100, -80, 270)
    Jump("loc_1D34")

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1822")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x14, 0x0, 0x0)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x13, -10690, 0, -9230, 45)
    SetChrPos(0x21, 5840, 2000, 22000, 315)
    SetChrFlags(0x21, 0x10)
    SetChrPos(0x22, 5840, 2000, 23400, 270)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x24, 0x10)
    SetChrFlags(0x26, 0x10)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, 1470, -700, 1200, 90)
    SetChrPos(0x2E, 4490, 2000, 23330, 90)
    SetChrPos(0x2F, 6200, -260, 2760, 135)
    SetChrPos(0x30, 4150, -700, 980, 90)
    SetChrPos(0x31, 3660, -700, -1420, 225)
    SetChrPos(0x32, 4330, 2000, 21140, 45)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2F, 0x10)
    SetChrFlags(0x30, 0x10)
    ClearChrFlags(0x31, 0x10)
    ClearChrFlags(0x32, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x13, -17390, 0, -9830, 135)
    ClearChrFlags(0x13, 0x10)

    label("loc_17FB")

    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 135)
    Jump("loc_1D34")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19D5")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x2D, 0x80)
    BeginChrThread(0x2D, 0, 0, 8)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    SetChrChipByIndex(0x15, 0xC)
    SetChrSubChip(0x15, 0x0)
    BeginChrThread(0x15, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C2")
    SetChrFlags(0x15, 0x10)
    Jump("loc_18C7")

    label("loc_18C2")

    ClearChrFlags(0x1A, 0x10)

    label("loc_18C7")

    SetChrPos(0x21, 5840, 2000, 22000, 0)
    SetChrPos(0x22, 5840, 2000, 23400, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_193C")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x10)
    SetChrPos(0x16, 17000, 0, -8570, 45)
    SetChrPos(0x13, 15160, 0, -9180, 315)
    Jump("loc_19A4")

    label("loc_193C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198A")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    Jump("loc_19A4")

    label("loc_198A")

    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0x13, -18110, 0, -5400, 135)

    label("loc_19A4")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1F, -15840, 0, 5890, 270)
    SetChrPos(0x20, -14160, -10, 7230, 270)
    Jump("loc_1D34")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A91")
    ClearChrFlags(0x2C, 0x80)
    BeginChrThread(0x2C, 0, 0, 7)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x21, 12500, 0, 11930, 0)
    SetChrPos(0x22, 10900, 0, 11720, 90)
    SetChrFlags(0x22, 0x10)
    SetChrFlags(0x25, 0x10)
    OP_93(0x27, 0x13B, 0x0)
    SetChrFlags(0x27, 0x10)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x1A, -16250, 0, -10660, 315)
    SetChrPos(0x13, -19060, 0, -5540, 0)
    SetChrPos(0x23, -14280, 0, 7050, 315)
    BeginChrThread(0x23, 0, 0, 0)
    Jump("loc_1D34")

    label("loc_1A91")

    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x1B, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1D34")
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrFlags(0x2F, 0x80)
    SetChrBattleFlags(0x2F, 0x8000)
    SetChrFlags(0x30, 0x80)
    SetChrBattleFlags(0x30, 0x8000)
    SetChrFlags(0x31, 0x80)
    SetChrBattleFlags(0x31, 0x8000)
    SetChrFlags(0x32, 0x80)
    SetChrBattleFlags(0x32, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x1A, -12260, 0, -10460, 45)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -14190, 0, -10860, 45)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, -7110, 0, -9730, 45)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -7510, 0, -8540, 45)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x26, -4900, 2000, 22900, 120)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrPos(0x27, -4900, 2000, 24200, 120)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 13300, 0, 12600, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 13500, 0, 11300, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -4500, 0, 14100, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, -2700, -350, 6100, 45)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrPos(0x25, -2000, -500, 5350, 45)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_4B(0x23, 0xFF)
    BeginChrThread(0x23, 0, 0, 0)
    SetChrPos(0x23, -3150, 0, 15000, 135)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 2700, -400, 5500, 0)

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1D48")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 74)
    Jump("loc_1D6B")

    label("loc_1D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1D5C")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 78)
    Jump("loc_1D6B")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_1D6B")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 83)

    label("loc_1D6B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D93")
    SetChrPos(0x0, -19600, 0, -27950, 0)

    label("loc_1D93")

    Return()

    # Function_10_13CB end

    def Function_11_1D94(): pass

    label("Function_11_1D94")

    ClearMapObjFlags(0x4, 0x10)
    OP_66(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DC5")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE2")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1DE2")

    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E1A")
    ClearMapObjFlags(0x5, 0x4)
    Jump("loc_1EE6")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E28")
    Jump("loc_1EE6")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1E93")
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E8E")
    OP_65(0x4, 0x1)

    label("loc_1E8E")

    Jump("loc_1EE6")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EAB")
    ClearMapObjFlags(0xD, 0x4)
    OP_65(0x5, 0x1)
    Jump("loc_1EE6")

    label("loc_1EAB")

    ClearMapObjFlags(0x5, 0x4)
    OP_65(0x5, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_71(0x9, 0x12C, 0x12C, 0x0, 0x0)

    label("loc_1EE6")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 68040, -3500, 11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E1(0x13DE4, 0x0, 0x71E8)
    OP_E1(0x13C54, 0x0, 0xD1B0)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 27000, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -18500, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_11_1D94 end

    def Function_12_2021(): pass

    label("Function_12_2021")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_20D9")

    ChrTalk(
        0xFE,
        "You hear the news yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're wrapping up the festivities with a candy\x01",
            "scavenger hunt today.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "I can't wait!\x01",
            "I NEED to participate!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BA")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2166")

    ChrTalk(
        0xFE,
        "Ugh. Those thugs are back at it again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're nothin' more than a bunch of kids desperately\x01",
            "crying for attention.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BA")

    label("loc_2166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_21E3")

    ChrTalk(
        0xFE,
        (
            "They're fine with anybody participating\x01",
            "in today's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I might give it a try, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23BA")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2238")

    ChrTalk(
        0xFE,
        (
            "It looks pretty fun. I've gotta find a\x01",
            "good spot to sit!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B4")

    label("loc_2238")


    ChrTalk(
        0xFE,
        (
            "Hmm... I can't see the stage well with\x01",
            "all of these other people around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I can find a better seat.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_22B4")

    Jump("loc_23BA")

    label("loc_22B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2312")

    ChrTalk(
        0xFE,
        (
            "I'm looking forward to seeing what they'll do in\x01",
            "today's performance!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23BA")

    label("loc_2312")


    ChrTalk(
        0xFE,
        (
            "Yesterday's concert was incredibly thrilling!\x01",
            "I've still got goosebumps all over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm definitely one to get weak at the\x01",
            "knees over tourist attractions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_23BA")

    TalkEnd(0xFE)
    Return()

    # Function_12_2021 end

    def Function_13_23BE(): pass

    label("Function_13_23BE")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_241C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243C")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C26")

    label("loc_243C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2450")
    Jump("loc_2C26")

    label("loc_2450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C26")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_258E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24CB")

    ChrTalk(
        0xFE,
        (
            "Would you all like to eat my final dish for the\x01",
            "Anniversary Festival?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2589")

    label("loc_24CB")


    ChrTalk(
        0xFE,
        (
            "Mishelam tends to get pretty crowded during the\x01",
            "Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm surprised how busy the park in the Harbor District is.\x01",
            "Looks like I better cook up a bunch of noodles.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2589")

    Jump("loc_2C26")

    label("loc_258E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25FF")

    ChrTalk(
        0xFE,
        (
            "This crappy song is driving away business!\x01",
            "What'd I do to deserve this? Aidios, have mercy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C26")

    label("loc_25FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A9F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26CE")

    ChrTalk(
        0xFE,
        "Oh, thank heavens! The thief was caught!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you know what they say: If you can't do the time,\x01",
            "don't do the crime.\x01",
            "They'd better think long and hard over what they did!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_26CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291A")

    ChrTalk(
        0x101,
        (
            "#0000FExcuse me, could we ask you a few questions?\x02\x03",
            "We're investigating the recent string of thefts\x01",
            "in the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, yeah. I've heard about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If he touches my noodles, I'm gonna get brutal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003FLeave the apprehension to us. We're just curious\x01",
            "to know if you have any information regarding\x01",
            "their appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... Their appearance, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nope, I haven't got a clue. I wouldn't be able to\x01",
            "tell with a crowd like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FI know what you mean. Well, regardless,\x01",
            "thank you for your time.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xB)
    Jump("loc_29FC")

    label("loc_291A")


    ChrTalk(
        0xFE,
        (
            "Anyone who repeatedly commits crimes in the\x01",
            "middle of a festival is scum, in my opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If he touches my noodles, I'm gonna get brutal!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0000F(I don't think this stall is about to be targeted\x01",
            "any time soon...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FC")

    Jump("loc_2A9A")

    label("loc_2A01")


    ChrTalk(
        0xFE,
        (
            "There's been multiple instances of food stalls\x01",
            "having their mira stolen since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is outrageous. I'll catch the sleazeball myself.\x02",
    )

    CloseMessageWindow()

    label("loc_2A9A")

    Jump("loc_2C26")

    label("loc_2A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B84")

    ChrTalk(
        0xFE,
        (
            "They say an old coot's food stall is sure to lose\x01",
            "to those fancy popcorn and gelato stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah? Well, I didn't ask for your damn opinion! I opened\x01",
            "this stall because I believe in the quality of my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C26")

    label("loc_2B84")


    ChrTalk(
        0xFE,
        (
            "Come taste the best noodles in all of\x01",
            "Crossbell for yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Think I'm yanking your chain?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll see! My noodles are unlike any\x01",
            "you've ever had!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C26")

    Jump("loc_23CB")

    label("loc_2C2B")

    TalkEnd(0xFE)
    Return()

    # Function_13_23BE end

    def Function_14_2C2F(): pass

    label("Function_14_2C2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CC6")

    ChrTalk(
        0xFE,
        "Lotta people with families out here today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I figure they're all going to Mishelam,\x01",
            "since it's the last day of the festival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_304F")

    label("loc_2CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2DF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D40")

    ChrTalk(
        0xFE,
        "There are definitely health benefits to walking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But walking can be exhausting at times.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DEE")

    label("loc_2D40")


    ChrTalk(
        0xFE,
        (
            "Utilizing back alleys and secret pathways in my\x01",
            "delivery route is perfect for times like these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not going to get done in by some orbal\x01",
            "delivery car drivers!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2DEE")

    Jump("loc_304F")

    label("loc_2DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2E45")

    ChrTalk(
        0xFE,
        "Ugh, I've gotta pick up the pace on these deliveries.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF2")

    label("loc_2E45")


    ChrTalk(
        0xFE,
        (
            "Sounds like my deliveries are going to get delayed\x01",
            "due to the traffic restrictions from the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna finish as much of them as I can before\x01",
            "it starts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2EF2")

    Jump("loc_304F")

    label("loc_2EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F6E")

    ChrTalk(
        0xFE,
        (
            "If they have that much energy left in the tank,\x01",
            "then why don't they come and help me work?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD3")

    label("loc_2F6E")


    ChrTalk(
        0xFE,
        "There was a disturbance at the park earlier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I guess those thugs were back at it again.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2FD3")

    Jump("loc_304F")

    label("loc_2FD8")


    ChrTalk(
        0xFE,
        (
            "I can't seem to catch a break, even though\x01",
            "it's the Anniversary Festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why does this always happen to me?\x02",
    )

    CloseMessageWindow()

    label("loc_304F")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C2F end

    def Function_15_3053(): pass

    label("Function_15_3053")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3173")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30CC")

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel sorry for my granddaughter, but\x01",
            "I don't care for those fancy attractions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_316E")

    label("loc_30CC")


    ChrTalk(
        0xFE,
        (
            "That damned IBC... Look what they did to my\x01",
            "fishing spot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know anything about this 'Mishelam,'\x01",
            "but those guys are startin' to piss me off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_316E")

    Jump("loc_333E")

    label("loc_3173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31BD")

    ChrTalk(
        0xFE,
        "This noise is unbearable. I can't take this anymore...\x02",
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_31BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3204")

    ChrTalk(
        0xFE,
        (
            "Don't wanna.\x01",
            "I don't care about no stinkin' parade.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_324D")

    ChrTalk(
        0xFE,
        (
            "This is how I've decided to spend my\x01",
            "remaining years.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_324D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_32C6")

    ChrTalk(
        0xFE,
        (
            "Sounds like the IBC is responsible for that blasted\x01",
            "orbal ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How dare they. I despise them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_333E")

    label("loc_32C6")


    ChrTalk(
        0xFE,
        "Aaaaarghhhhh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "SHADDAP! YOU'RE TOO DAMN LOUD!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm tryin' to fish over here! Can't you fools see that?!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_333E")

    TalkEnd(0xFE)
    Return()

    # Function_15_3053 end

    def Function_16_3342(): pass

    label("Function_16_3342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_33DD")

    ChrTalk(
        0xFE,
        "Mishelam... Sounds nice. I'd like to visit it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But there's no point in asking my grandpa\x01",
            "to come with me when he's like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3639")

    label("loc_33DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3442")

    ChrTalk(
        0xFE,
        "What's with all the ruckus?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Looks like somethin' is going on near the stage.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3639")

    label("loc_3442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_34C5")

    ChrTalk(
        0xFE,
        (
            "I've heard rumors that the parade is going to\x01",
            "be amazing this year!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, wanna come to the parade with me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3639")

    label("loc_34C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3552")

    ChrTalk(
        0xFE,
        "I was looking forward to playing with Grandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh* I hate when he gets like this... He's as\x01",
            "stubborn as a mule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3639")

    label("loc_3552")

    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "C'mon, Grandpa! Let's walk around for a bit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm fine, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's this place I wanna check out. Please,\x01",
            "you gotta take me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I'm fine, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ugh, what a stubborn old man.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x10)

    label("loc_3639")

    TalkEnd(0xFE)
    Return()

    # Function_16_3342 end

    def Function_17_363D(): pass

    label("Function_17_363D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "*click* *flash*\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "These photos should work well\x01",
            "for showcasing Crossbell's culture. ♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_363D end

    def Function_18_36A3(): pass

    label("Function_18_36A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 0)), scpexpr(EXPR_END)), "loc_3853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_376B")

    ChrTalk(
        0xD,
        (
            "#2100FOh, yeah, that reminds me. Be sure to take\x01",
            "plenty of photos and fork 'em over to\x01",
            "me later.\x02\x03",
            "#2109FI'm countin' on ya for some quality shots! ♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_384E")

    label("loc_376B")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        (
            "#2100FNow, where was I? It's time to go and\x01",
            "check out the hottest spots at the\x01",
            "Anniversary Festival!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 300)

    ChrTalk(
        0xD,
        "#2109FOff we go, Reins! You'd better keep up with me!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 300)

    ChrTalk(
        0xE,
        "G-Got it, ma'am!\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 6)

    label("loc_384E")

    Jump("loc_3AC6")

    label("loc_3853")


    ChrTalk(
        0xD,
        (
            "#2100FHowdy, friends. Excellent work yesterday!\x02\x03",
            "#2109FI just added the finishing touches to an exciting\x01",
            "article about yesterday's race!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#0006FReally, Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306FShe's turnin' it into an article, eh? Can't say I\x01",
            "didn't see that one comin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#2104FYou bet'cha! We're featuring it in an extra-special\x01",
            "issue of the Crossbell Times that we'll be\x01",
            "publishing on the final day of the festival!\x02\x03",
            "#2100FYour ventures always make for superb stories,\x01",
            "so I'll be keeping a close eye on you! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F(She's building us up just to\x01",
            "tear us down, isn't she?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#0200F(That has been the pattern thus far, yes.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 0)

    label("loc_3AC6")

    TalkEnd(0xFE)
    Return()

    # Function_18_36A3 end

    def Function_19_3ACA(): pass

    label("Function_19_3ACA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B59")

    ChrTalk(
        0xFE,
        (
            "The ship to Mishelam will be arriving at\x01",
            "this dock soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We appreciate the patience of those who have\x01",
            "been waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D37")

    label("loc_3B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BE7")

    ChrTalk(
        0xFE,
        "*sigh* I wanna have fun with my family, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll submit a vacation request after\x01",
            "the Anniversary Festival...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D37")

    label("loc_3BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C5E")

    ChrTalk(
        0xFE,
        (
            "The ship will be departing for\x01",
            "Mishelam shortly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, promptly make your way onto the ship.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D37")

    label("loc_3C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3CE8")

    ChrTalk(
        0xFE,
        (
            "The ship to Mishelam will be arriving at\x01",
            "this dock in approximately five minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We thank you for your patience.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D37")

    label("loc_3CE8")


    ChrTalk(
        0xFE,
        "Boarding for the ship to Mishelam has begun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Promptly board, please!\x02",
    )

    CloseMessageWindow()

    label("loc_3D37")

    TalkEnd(0xFE)
    Return()

    # Function_19_3ACA end

    def Function_20_3D3B(): pass

    label("Function_20_3D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D65")
    Call(0, 82)
    Return()

    label("loc_3D65")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4722")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DC3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE3")
    OP_AF(0x7D)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_471D")

    label("loc_3DE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DF7")
    Jump("loc_471D")

    label("loc_3DF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F34")

    ChrTalk(
        0xFE,
        "Hey, I heard you guys caught the thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nice job. You have my gratitude.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1C6, 1)

    ChrTalk(
        0xFE,
        (
            "Here, take this. Just a little something to\x01",
            "show my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100FThank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBD, 1)
    Jump("loc_471D")

    label("loc_3F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_400F")

    ChrTalk(
        0xFE,
        (
            "Heehee. Hello there. Welcome\x01",
            "to Mithra's Gelato Stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My gelato is the finest in all the land.\x01",
            "It's even the official gelato of the\x01",
            "Remiferian royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Would you like to try some?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 4)
    Jump("loc_471D")

    label("loc_400F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_41F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4149")

    ChrTalk(
        0xFE,
        "Today's the last day of the Anniversary Festival.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here's a special little something from me:\x01",
            "Instructions on how to make my famous\x01",
            "and delicious gelato!\x02",
        )
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
            "Received the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the recipe for ",
            scpstr(SCPSTR_CODE_ITEM, 0x1C7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x13)
    Jump("loc_41EB")

    label("loc_4149")


    ChrTalk(
        0xFE,
        "Today's the last day of the Anniversary Festival...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That means that Mithra the gelato nomad will\x01",
            "disappear, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Now's your last chance to buy it.\x02",
    )

    CloseMessageWindow()

    label("loc_41EB")

    Jump("loc_471D")

    label("loc_41F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_427F")

    ChrTalk(
        0xFE,
        (
            "I'd heard the parade was going to be large,\x01",
            "but that was far beyond my expectation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Crossbellans sure are gaudy, eh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_471D")

    label("loc_427F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_458C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4307")

    ChrTalk(
        0xFE,
        "Anyway, the parade's going to start soon, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm looking forward to seeing a surge in business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_4307")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A6")

    ChrTalk(
        0xFE,
        (
            "Who would have thought I'd get targeted\x01",
            "in the middle of serving customers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How did I manage to screw up so badly?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_43A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4439")

    ChrTalk(
        0xFE,
        (
            "Crossbell easily has the most exciting\x01",
            "festival out of anywhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost sad that all festivals\x01",
            "must come to an end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4587")

    label("loc_4439")


    ChrTalk(
        0xFE,
        (
            "People across the continent have their\x01",
            "sights set on visiting Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They'll do all the things they ever dreamt of\x01",
            "doing, then continue with their lives\x01",
            "without skipping a beat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, what a fascinating place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Out of all of my visits to Crossbell,\x01",
            "this has easily been the most exciting\x01",
            "out of all of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_4587")

    Jump("loc_471D")

    label("loc_458C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_468E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4626")

    ChrTalk(
        0xFE,
        (
            "You had it pretty hard yesterday,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You do know that your chivalrous deeds have\x01",
            "spread across the city, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4689")

    label("loc_4626")


    ChrTalk(
        0xFE,
        "Well, if it ain't the heroes of the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How 'bout it? I'll even give you a discount.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_4689")

    Jump("loc_471D")

    label("loc_468E")


    ChrTalk(
        0xFE,
        (
            "Our gelato is the finest in all the land. We're\x01",
            "even the official gelato of the Remiferian\x01",
            "royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Would you like to try some?\x02",
    )

    CloseMessageWindow()

    label("loc_471D")

    Jump("loc_3D72")

    label("loc_4722")

    TalkEnd(0xFE)
    Return()

    # Function_20_3D3B end

    def Function_21_4726(): pass

    label("Function_21_4726")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4733")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F79")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4784")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47A4")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F74")

    label("loc_47A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47B8")
    Jump("loc_4F74")

    label("loc_47B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F74")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4842")

    ChrTalk(
        0xFE,
        "You wanna try some steak?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The festival's almost over, so why not live a little?\x02",
    )

    CloseMessageWindow()
    Jump("loc_48FF")

    label("loc_4842")


    ChrTalk(
        0xFE,
        "It's the last day of the festival, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We're feeling a little down about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suppose this is how people must feel when\x01",
            "they have to part with something important.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_48FF")

    Jump("loc_4F74")

    label("loc_4904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_493F")

    ChrTalk(
        0xFE,
        (
            "Oh?\x01",
            "It's pretty loud over by the stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F74")

    label("loc_493F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49C8")

    ChrTalk(
        0xFE,
        "Hey there. Would you like to try a skewer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I promise it's the tastiest steak skewer you'll\x01",
            "ever try!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E96")

    label("loc_49C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E24")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6F")

    ChrTalk(
        0x101,
        (
            "#0000FSorry to bother you, but do you mind if we\x01",
            "ask you a few questions?\x02\x03",
            "We're investigating the recent string of thefts\x01",
            "around the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O-Oh, yeah. That.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My sister and I take turns running the stall,\x01",
            "so I think we'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be a bit more concerned if I was on my own.\x01",
            "It'd give the thief a perfect chance to sneak in\x01",
            "and take my stuff when I'm not around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0101FDo you happen to recall anyone acting\x01",
            "suspiciously around the area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "A-Actually, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw some hooligans in red tracksuits\x01",
            "come here a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I felt a little anxious because I'd never\x01",
            "seen them around before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#0300FNah, those ain't the guys we're looking for.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0203FI do not believe those delinquents would\x01",
            "resort to stealing.\x02\x03",
            "#0200FRegardless, do not hesitate to report any\x01",
            "issues that they may cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "S-Sure, thanks.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xC)
    Jump("loc_4E1F")

    label("loc_4D6F")


    ChrTalk(
        0xFE,
        (
            "Can't you see we're busy serving tons of\x01",
            "customers? I don't know anything about\x01",
            "suspicious people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be praying to Aidios to ward any thieves\x01",
            "away from our stall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E1F")

    Jump("loc_4E96")

    label("loc_4E24")


    ChrTalk(
        0xFE,
        "We came to Crossbell's festival from out East.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everything's going swimmingly, just\x01",
            "as I hoped it would.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E96")

    Jump("loc_4F74")

    label("loc_4E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4F11")

    ChrTalk(
        0xFE,
        "My little sister's a pro at bringing in customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "She's been a massive boon to our business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F74")

    label("loc_4F11")


    ChrTalk(
        0xFE,
        "Hey there, would you like to try a skewer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're easy on the teeth and tasty, to boot.\x02",
    )

    CloseMessageWindow()

    label("loc_4F74")

    Jump("loc_4733")

    label("loc_4F79")

    TalkEnd(0xFE)
    Return()

    # Function_21_4726 end

    def Function_22_4F7D(): pass

    label("Function_22_4F7D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56D3")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FDB")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4FDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FFB")
    OP_AF(0x7C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56CE")

    label("loc_4FFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_500F")
    Jump("loc_56CE")

    label("loc_500F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56CE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_50C6")

    ChrTalk(
        0xFE,
        "Huh? Is that man sponsoring the performance?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kinda surprised he's a perfectly normal old guy.\x01",
            "Woulda expected someone more eccentric.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56CE")

    label("loc_50C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_51A2")

    ChrTalk(
        0xFE,
        (
            "Trying to beat the heat? We've got drink combos\x01",
            "for sale today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come and try one. It'll soothe your\x01",
            "parched throat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come onnnn, you know you wanna try it.\x01",
            "Our drink combos are a great price!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56CE")

    label("loc_51A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5430")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_52AF")

    ChrTalk(
        0xFE,
        "They managed to catch that darn thief, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a relief. Now we can run our business with\x01",
            "a little peace of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's always trouble brewin' in Crossbell.\x01",
            "Letting down your guard during a festival\x01",
            "is asking for trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_52AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53D5")

    ChrTalk(
        0xFE,
        (
            "Representatives from the Business Owners' Association\x01",
            "dropped by to warn us about thieves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell's still lackin' in the 'public order'\x01",
            "department, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be watching my stall like a hawk. I can't afford\x01",
            "to have anything stolen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_542B")

    label("loc_53D5")


    ChrTalk(
        0xFE,
        "The police look like they're on edge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What's going on? Some kinda accident?\x02",
    )

    CloseMessageWindow()

    label("loc_542B")

    Jump("loc_56CE")

    label("loc_5430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5570")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_54B0")

    ChrTalk(
        0xFE,
        "If you're gonna buy something, then get to it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you go any slower, the sun'll start settin'!\x02",
    )

    CloseMessageWindow()
    Jump("loc_556B")

    label("loc_54B0")


    ChrTalk(
        0xFE,
        "Hey, you. I bet you're feeling pretty hungry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got just the thing for you.\x01",
            "Nothing beats the taste of grilled steak on a stick!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Live a little! You're at a festival!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_556B")

    Jump("loc_56CE")

    label("loc_5570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5603")

    ChrTalk(
        0xFE,
        "You're at a festival! It's time to eat a skewer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Double the meat, double the fun!\x01",
            "Come on down and get some tasty\x01",
            "skewers!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56CE")

    label("loc_5603")


    ChrTalk(
        0xFE,
        (
            "Nothing better than a good, old-fashioned festival.\x01",
            "I love me some festivals!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You're at a festival! It's time to eat a skewer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about it, sir? I can see\x01",
            "you salivating over my meat!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_56CE")

    Jump("loc_4F8A")

    label("loc_56D3")

    TalkEnd(0xFE)
    Return()

    # Function_22_4F7D end

    def Function_23_56D7(): pass

    label("Function_23_56D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_576F")

    ChrTalk(
        0xFE,
        "It sounds like the thief was successfully stopped!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hahaha! Fantastic news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can finally relax and enjoy the festival.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DE4")

    label("loc_576F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_581A")

    ChrTalk(
        0xFE,
        (
            "Mors is a great orator. I love listening to his\x01",
            "fantastic speeches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wanna know something funny? He actually\x01",
            "gets nervous before he gives a speech!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE4")

    label("loc_581A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_5904")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_587D")

    ChrTalk(
        0xFE,
        "Huh? What's going on?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That performance is a little too loud...\x02",
    )

    CloseMessageWindow()
    Jump("loc_58FF")

    label("loc_587D")


    ChrTalk(
        0xFE,
        (
            "Wow, those bracers never cease to amaze me with\x01",
            "how quickly they work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, now everyone's sure to enjoy the festival.\x02",
    )

    CloseMessageWindow()

    label("loc_58FF")

    Jump("loc_5DE4")

    label("loc_5904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5CE1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_59D2")
    OP_93(0xFE, 0x87, 0x0)

    ChrTalk(
        0xFE,
        "Isn't it satisfying after a long day of hard work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh, that's the stuff. You want some alcohol, too?\x01",
            "It'll be my treat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "You know I can't. I'm still a minor!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CDC")

    label("loc_59D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_5A7F")

    ChrTalk(
        0xFE,
        "Nothing suspicious going on around here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... We haven't figured out the thief's motives,\x01",
            "so all we can do for now is continue to make\x01",
            "rounds.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CDC")

    label("loc_5A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B30")

    ChrTalk(
        0xFE,
        (
            "We have to alert the people running the stalls.\x01",
            "I wouldn't want them to become victims.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, maybe one more round would be a good idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5BCE")

    label("loc_5B30")


    ChrTalk(
        0xFE,
        "Back in my day, we used to fight off thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This jerkwad is doing a great job of ruining the festival.\x01",
            "There'll be HELL to pay when we catch him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BCE")

    Jump("loc_5CDC")

    label("loc_5BD3")


    ChrTalk(
        0xFE,
        (
            "Is NOTHING safe from the hands of this jerkwad?\x01",
            "They stole all of poor Mithra's mira! How low can\x01",
            "they get?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Where do they get off thinking they can ruin the\x01",
            "atmosphere for everybody? The festival hasn't\x01",
            "been nearly as enjoyable because of their actions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CDC")

    Jump("loc_5DE4")

    label("loc_5CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5D6A")

    ChrTalk(
        0xFE,
        (
            "Have you seen this man's granddaughter?\x01",
            "She's super cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Isn't she just the cutest?! I'd love to play with her!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DE4")

    label("loc_5D6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7C")
    Call(0, 33)
    Jump("loc_5DE4")

    label("loc_5D7C")


    ChrTalk(
        0xFE,
        "Parla used to be my idol back in the day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha! I'm brimming with jealousy!\x01",
            "Damn you, Mors!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE4")

    TalkEnd(0xFE)
    Return()

    # Function_23_56D7 end

    def Function_24_5DE8(): pass

    label("Function_24_5DE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5E7D")

    ChrTalk(
        0xFE,
        (
            "Good morning, everyone! Our chairman\x01",
            "has a few words he'd like to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    ChrTalk(
        0xFE,
        "If you would, Mr. Chairman!\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_5FFD")

    label("loc_5E7D")


    ChrTalk(
        0xFE,
        "Erm... I have some terrible news for everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This joyous festival must come to an\x01",
            "end today!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "We've prepared something special\x01",
            "for this day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Our chairman has a few words he'd\x01",
            "like to say.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x1A, 500)

    ChrTalk(
        0xFE,
        "If you would, Mr. Chairman!\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x0)
    SetScenarioFlags(0x1, 2)

    label("loc_5FFD")

    Jump("loc_637C")

    label("loc_6002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6079")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_6071")

    ChrTalk(
        0xFE,
        (
            "Whoa! What the heck are you\x01",
            "imbeciles doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Get off the stage! Immediately!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6074")

    label("loc_6071")

    Call(0, 53)

    label("loc_6074")

    Jump("loc_637C")

    label("loc_6079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6123")

    ChrTalk(
        0xFE,
        (
            "Which team is going to score the\x01",
            "most points?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Join in on today's performance!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why don't our brave folks in the audience\x01",
            "raise their hands?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_637C")

    label("loc_6123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_61F0")

    ChrTalk(
        0xFE,
        (
            "Yesterday was painful, but things seem to be\x01",
            "operating more smoothly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Everybody's having a good time, so I think it's safe to\x01",
            "say we made up for yesterday's blunder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6293")

    label("loc_61F0")


    ChrTalk(
        0xFE,
        (
            "The next street performance is bound to be exciting.\x01",
            "They're a professional escape artist!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If I could get a volunteer from the audience, please!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x14, 0x10)

    label("loc_6293")

    Jump("loc_637C")

    label("loc_6298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6310")

    ChrTalk(
        0xFE,
        "We still need time to prepare for the quiz tournament...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Sit tight for a little longer, please!\x02",
    )

    CloseMessageWindow()
    Jump("loc_637C")

    label("loc_6310")


    ChrTalk(
        0xFE,
        (
            "Hey there, mister!\x01",
            "Please wait a little longer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We're preparing for the Happy Quiz Tournament!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_637C")

    TalkEnd(0xFE)
    Return()

    # Function_24_5DE8 end

    def Function_25_6380(): pass

    label("Function_25_6380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6391")
    Call(0, 30)
    Jump("loc_6394")

    label("loc_6391")

    Call(0, 26)

    label("loc_6394")

    Return()

    # Function_25_6380 end

    def Function_26_6395(): pass

    label("Function_26_6395")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63DE")
    Call(0, 77)
    Return()

    label("loc_63DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6407")
    Call(0, 75)
    Return()

    label("loc_6407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6495")
    TalkBegin(0x15)

    ChrTalk(
        0x15,
        "Roy and Meiling saved my hide back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Roy likes to pretend he's lazy, but we all know he\x01",
            "tries his hardest.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Jump("loc_6D3C")

    label("loc_6495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6792")
    TalkBegin(0x15)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6550")

    ChrTalk(
        0xFE,
        "You have my thanks, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... That blasted thief gave stall owners a ton\x01",
            "of grief. I should compensate them, or else\x01",
            "it wouldn't feel right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_6550")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_6624")

    ChrTalk(
        0xFE,
        (
            "The Anniversary Festival usually has its fair share\x01",
            "of problems, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...this is unprecedented. There's nothing\x01",
            "we can do about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm sorry, everybody. We're counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_6624")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_671B")

    ChrTalk(
        0xFE,
        (
            "At this rate, the stall owners may resort to\x01",
            "shutting their businesses down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't want that to happen. We've all been waiting\x01",
            "a long time for the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm begging you. There has to be something\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_678A")

    label("loc_671B")


    ChrTalk(
        0xFE,
        (
            "*sigh* We've been trying our hardest to warn\x01",
            "people, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We can't tackle this problem on our own.\x02",
    )

    CloseMessageWindow()

    label("loc_678A")

    TalkEnd(0x15)
    Jump("loc_6D3C")

    label("loc_6792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_69C2")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_682F")
    Jump("loc_6879")

    label("loc_682F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_684F")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6879")

    label("loc_684F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_686F")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6879")

    label("loc_686F")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6879")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6940")

    ChrTalk(
        0x15,
        "*sigh* I have to say, this year is absolutely packed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm up to my neck in work. Not much I can\x01",
            "do about it while I'm all by my lonesome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B6")

    label("loc_6940")


    ChrTalk(
        0x15,
        "The chairman's son manages an enterprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "On the other hand, his grandson Roy enjoys\x01",
            "being a contrarian.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_69B6")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)
    Jump("loc_6D3C")

    label("loc_69C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x15)
    ClearChrFlags(0x15, 0x10)
    TurnDirection(0x15, 0x0, 0)
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6A56")
    Jump("loc_6AA0")

    label("loc_6A56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A76")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AA0")

    label("loc_6A76")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6A96")
    OP_52(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AA0")

    label("loc_6A96")

    OP_52(0x15, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AA0")

    OP_52(0x15, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B8D")

    ChrTalk(
        0x15,
        (
            "Greetings. This is the Crossbell Business\x01",
            "Owners' Association's tent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "We welcome all citizens to participate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We also host the raffle giveaway. Why not\x01",
            "give it a try?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 5)
    Jump("loc_6D35")

    label("loc_6B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_6C23")

    ChrTalk(
        0x15,
        (
            "Apparently, the heads of our organization used to\x01",
            "own street stalls, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I can easily imagine how they were\x01",
            "back in the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D35")

    label("loc_6C23")


    ChrTalk(
        0x15,
        (
            "Apparently, the heads of our organization used to\x01",
            "own street stalls, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I heard they used to compete with each other.\x01",
            "Feels like that's the kind of relationship most\x01",
            "people in this business have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha. I can easily imagine how they were\x01",
            "back in the day.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_6D35")

    SetChrSubChip(0x15, 0x0)
    TalkEnd(0x15)

    label("loc_6D3C")

    Return()

    # Function_26_6395 end

    def Function_27_6D3D(): pass

    label("Function_27_6D3D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "I quite enjoy the scenery around here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This spot seemed good to take a rest.\x01",
            "I'm a little bit tired from visiting stalls all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once you manage to break away from the\x01",
            "crowds, Crossbell's atmosphere is actually\x01",
            "very pleasant.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_6D3D end

    def Function_28_6E36(): pass

    label("Function_28_6E36")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Crossbell and Armorica are great, but they've\x01",
            "each got their pros and cons, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I think I'll buy some presents for the kids back home.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_6E36 end

    def Function_29_6ED5(): pass

    label("Function_29_6ED5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_702C")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F82")

    ChrTalk(
        0xFE,
        "Oh? The thief was already captured?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Wow. They got caught a lot faster\x01",
            "than I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "O-Oh... That's great news.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_7020")

    label("loc_6F82")


    ChrTalk(
        0xFE,
        (
            "I was worried that they'd cause more\x01",
            "damage, so this is quite relieving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is great news... Guess I'd better\x01",
            "get back to manning the tent, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7020")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_72DB")

    label("loc_702C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_70E9")

    ChrTalk(
        0xFE,
        (
            "Let's see...\x01",
            "I think I'll go visit Mithra one more time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think the ice cream stall that was targeted\x01",
            "will be hit again...but still. I'm kind of worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72DB")

    label("loc_70E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_71E7")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7194")

    ChrTalk(
        0xFE,
        "I'll keep patrolling the area.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A serial thief has been targeting stalls...\x01",
            "I'm sure stall owners are worried they're next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_71DB")

    label("loc_7194")


    ChrTalk(
        0xFE,
        (
            "A simple patrol is the least I can do to\x01",
            "help ease their worries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71DB")

    OP_93(0xFE, 0x10E, 0x0)
    Jump("loc_72DB")

    label("loc_71E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_72DB")

    ChrTalk(
        0xFE,
        (
            "I only tagged along because Meiling told me\x01",
            "she wanted to try out all the different types of food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not interested in the Business Owners'\x01",
            "Association. Get real!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, Grandpa. Can't you tell Dad\x01",
            "to shut up about it?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72DB")

    TalkEnd(0xFE)
    Return()

    # Function_29_6ED5 end

    def Function_30_72DF(): pass

    label("Function_30_72DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_74B9")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_737C")
    Jump("loc_73C6")

    label("loc_737C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_739C")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73C6")

    label("loc_739C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73BC")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_73C6")

    label("loc_73BC")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73C6")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743F")

    ChrTalk(
        0x17,
        "What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Today's your last chance to exchange prizes.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_74AD")

    label("loc_743F")


    ChrTalk(
        0x17,
        (
            "I'm only helping because they're short\x01",
            "a few pairs of hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "Hahaha. I get carried away too easily.\x02",
    )

    CloseMessageWindow()

    label("loc_74AD")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_7864")

    label("loc_74B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7732")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7556")
    Jump("loc_75A0")

    label("loc_7556")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7576")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75A0")

    label("loc_7576")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7596")
    OP_52(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75A0")

    label("loc_7596")

    OP_52(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_75A0")

    OP_52(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_764C")

    ChrTalk(
        0x17,
        "Whoa, look at all the people...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Probably would have been a good idea to help\x01",
            "guide 'em around or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7726")

    label("loc_764C")


    ChrTalk(
        0x17,
        "Man, those bracers never fail to impress me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Or rather, there's an impressive amount\x01",
            "of people...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Is it because of the parade? Probably would have\x01",
            "been a good idea to help guide 'em around or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7726")

    SetChrSubChip(0x17, 0x0)
    TalkEnd(0x17)
    Jump("loc_7864")

    label("loc_7732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7864")
    TalkBegin(0x17)
    SetChrSubChip(0x17, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_77D8")

    ChrTalk(
        0x17,
        (
            "Damn it! Just thinking about it pisses me off!\x01",
            "Why should I have to help out?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "I want nothing to do with being a merchant!\x02",
    )

    CloseMessageWindow()
    Jump("loc_785D")

    label("loc_77D8")


    ChrTalk(
        0x17,
        (
            "You guys hear about all those incidents\x01",
            "of theft already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "I-I guess I could look after the store.\x01",
            "It's the least I can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_785D")

    SetChrSubChip(0x17, 0x2)
    TalkEnd(0x17)

    label("loc_7864")

    Return()

    # Function_30_72DF end

    def Function_31_7865(): pass

    label("Function_31_7865")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7894")

    ChrTalk(
        0xFE,
        "Woow! Look at all the stores!\x02",
    )

    CloseMessageWindow()

    label("loc_7894")

    TalkEnd(0xFE)
    Return()

    # Function_31_7865 end

    def Function_32_7898(): pass

    label("Function_32_7898")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x19)
    ClearChrFlags(0x19, 0x10)
    TurnDirection(0x19, 0x0, 0)
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_792C")
    Jump("loc_7976")

    label("loc_792C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_794C")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7976")

    label("loc_794C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_796C")
    OP_52(0x19, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7976")

    label("loc_796C")

    OP_52(0x19, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x19, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7976")

    OP_52(0x19, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x19, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_79F5")

    ChrTalk(
        0x19,
        "Hewwo, do you need any hewp?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "You can exchange for pwizes with me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CF5")

    label("loc_79F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7AB1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7A5D")

    ChrTalk(
        0x19,
        "Oooh! There was a pawade?!\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    ChrTalk(
        0x19,
        "That's weally cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AAC")

    label("loc_7A5D")


    ChrTalk(
        0x19,
        "Bwacers are sooo cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "They found out who the bad guys\x01",
            "were so fast!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AAC")

    Jump("loc_7CF5")

    label("loc_7AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7CF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7C2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_7B65")

    ChrTalk(
        0x19,
        "You're super-duper cool, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "The way you said hewwo to those other\x01",
            "guys in the unifowms was also vewy cool!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("loc_7C29")

    label("loc_7B65")


    ChrTalk(
        0x19,
        "You and your fwiends are weally cool, mister!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "The cute doggie was even cooler, though!\x02",
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

    label("loc_7C29")

    Jump("loc_7CF5")

    label("loc_7C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7CA9")

    ChrTalk(
        0x19,
        "I'm hewping wook after the stowe wight now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "If you need any hewp, you can count on me,\x01",
            "okaaay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CF5")

    label("loc_7CA9")


    ChrTalk(
        0x19,
        "My bwother and I are hewping watch the stowe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "Hewwo! How awe you?\x02",
    )

    CloseMessageWindow()

    label("loc_7CF5")

    SetChrSubChip(0x19, 0x0)
    TalkEnd(0x19)
    Return()

    # Function_32_7898 end

    def Function_33_7CFD(): pass

    label("Function_33_7CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D46")
    Call(0, 77)
    Return()

    label("loc_7D46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D6F")
    Call(0, 75)
    Return()

    label("loc_7D6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7E30")

    ChrTalk(
        0xFE,
        "Phew... The festival's finally almost over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I hate greeting people, though. I'm bad at it.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x14, 0xFF)
    TurnDirection(0x14, 0xFE, 500)

    ChrTalk(
        0x14,
        (
            "Just hurry up and make it\x01",
            "snappy, Mr. Chairman!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    OP_93(0x14, 0x10E, 0x0)
    Jump("loc_8A76")

    label("loc_7E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_804C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7E86")

    ChrTalk(
        0xFE,
        (
            "Oh, we meet again!\x01",
            "Can you please stop this violence?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8047")

    label("loc_7E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7EB4")

    ChrTalk(
        0xFE,
        "Ah, it's you again.\x02",
    )

    CloseMessageWindow()

    label("loc_7EB4")


    ChrTalk(
        0xFE,
        (
            "In fact, some bracers apprehended the thief for us\x01",
            "earlier in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha! What a relief! We can finally go back\x01",
            "to enjoying the festival again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8044")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FAE")

    ChrTalk(
        0x101,
        (
            "#0005F(I guess the bracers beat us\x01",
            "to the punch.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FE9")

    label("loc_7FAE")


    ChrTalk(
        0x101,
        "#0005F(Thefts...? First time I'm hearing about this.)\x02",
    )

    CloseMessageWindow()

    label("loc_7FE9")


    ChrTalk(
        0x104,
        (
            "#0306F(Damn it... We ended up looking like a bunch of\x01",
            "fools in front of the bracers.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8044")

    SetScenarioFlags(0x1, 4)

    label("loc_8047")

    Jump("loc_8A76")

    label("loc_804C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_871B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_811B")

    ChrTalk(
        0xFE,
        (
            "Oh, don't worry! You helped us out, too.\x01",
            "I'm just glad we can all enjoy the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hahaha! What a relief! I'm glad to have the\x01",
            "companionship of some fine young people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8716")

    label("loc_811B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_83BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F7")

    ChrTalk(
        0xFE,
        (
            "Stalls in Central Square and the Administrative,\x01",
            "Entertainment, and Harbor Districts were targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It may be wise to question some of the\x01",
            "stalls that haven't been robbed, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0005FWe'll give it a shot. We might be able to get\x01",
            "a clearer picture that way.\x02\x03",
            "#0001FWe'll return as soon as we've finished investigating.\x01",
            "Please sit tight in the meantime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Will do. We'll contact you right away if there are\x01",
            "any new developments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_83B8")

    label("loc_82F7")


    ChrTalk(
        0xFE,
        (
            "Stalls in Central Square and the Administrative,\x01",
            "Entertainment, and Harbor Districts were targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Might be a good idea to question some of the\x01",
            "stores that haven't been robbed, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B8")

    Jump("loc_8716")

    label("loc_83BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_86CB")

    ChrTalk(
        0x1A,
        (
            "The Business Owners' Association cannot allow for any\x01",
            "more stalls to be terrorized by the thief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Not only that, but it'll start affecting the customers\x01",
            "who have come to enjoy the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Will you please apprehend the thief for us?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85CC")
    EventBegin(0x0)
    Fade(500)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 198)
    SetChrPos(0x15, -16920, 0, -9360, 198)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    OP_0D()
    Call(0, 76)
    Return()

    label("loc_85CC")


    ChrTalk(
        0x101,
        (
            "#0006FSorry, no can do. Our schedule is completely\x01",
            "packed at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Is that so? A shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Well, please come by again if you're up for the task.\x01",
            "I'd like to resolve this before the thief has a\x01",
            "chance to strike again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x1A, 0x13B, 0x0)
    OP_93(0x15, 0x87, 0x0)
    Jump("loc_8716")

    label("loc_86CB")


    ChrTalk(
        0xFE,
        "This is a huge problem...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is no time to enjoy the festival.\x02",
    )

    CloseMessageWindow()

    label("loc_8716")

    Jump("loc_8A76")

    label("loc_871B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8857")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x16, 0xFF)

    ChrTalk(
        0xFE,
        "Well, if it isn't Roy. I'm surprised you've come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Eh, Meiling wanted me to come play with her. Do\x01",
            "me a solid and keep it a secret from my old man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, sure. I don't think he'd complain, though.\x01",
            "It IS a festival, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Take the time to enjoy yourselves today.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_8A76")

    label("loc_8857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8A76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A02")
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0x13,
        "Long time no see, Parla!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "I gotta say, Mors hit it out of the park with this one.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Who would've thought that he would have\x01",
            "gotten together with our favorite idol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Oh, my. There you go with the exaggerations again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Ease up on the sorbet and booze, or it'll go\x01",
            "straight to your stomach, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Haha, you two lovebirds never change.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x1A, 0xFF)
    OP_4C(0x1B, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_8A76")

    label("loc_8A02")


    ChrTalk(
        0xFE,
        "My friend is going out of control with his spending.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know what'll do him some good?\x01",
            "A swift backhand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A76")

    TalkEnd(0xFE)
    Return()

    # Function_33_7CFD end

    def Function_34_8A7A(): pass

    label("Function_34_8A7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A98")
    Call(0, 33)
    Jump("loc_8B17")

    label("loc_8A98")


    ChrTalk(
        0xFE,
        (
            "I'm friends with all of the people in the\x01",
            "Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heehee. I can count on them\x01",
            "to never change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B17")

    TalkEnd(0xFE)
    Return()

    # Function_34_8A7A end

    def Function_35_8B1B(): pass

    label("Function_35_8B1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8BAA")

    ChrTalk(
        0xFE,
        (
            "Ahem! My kid asked me to do it.\x01",
            "What am I going to do, say no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think we'll spend our whole day at the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D47")

    label("loc_8BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8C1B")

    ChrTalk(
        0xFE,
        "Wahhh, that person is soooo scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "L-Listen, son. Thank them so we\x01",
            "can get on our way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D47")

    label("loc_8C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8C83")

    ChrTalk(
        0xFE,
        "Oh, man, the parade's gonna start soon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I've loved them ever since I was a kid!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D47")

    label("loc_8C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8CE3")

    ChrTalk(
        0xFE,
        (
            "Oh, boy... The lady at that stall is more\x01",
            "beautiful than my wife, isn't she?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D47")

    label("loc_8CE3")


    ChrTalk(
        0xFE,
        (
            "Okay, I've decided! Today's the day I'm going to\x01",
            "check out what food every stall has to offer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D47")

    TalkEnd(0xFE)
    Return()

    # Function_35_8B1B end

    def Function_36_8D4B(): pass

    label("Function_36_8D4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8D9A")

    ChrTalk(
        0xFE,
        "We get to ride that huge boat to Mishelam!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yaaaaay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E9E")

    label("loc_8D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8DDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_8DD4")

    ChrTalk(
        0x22,
        "Sorry! Thanks for telling me!\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DD7")

    label("loc_8DD4")

    Call(0, 50)

    label("loc_8DD7")

    Jump("loc_8E9E")

    label("loc_8DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8E51")

    ChrTalk(
        0xFE,
        "Hip hip hooray! I love festivals!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not only that, but a festival means\x01",
            "there's a parade, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E9E")

    label("loc_8E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8E77")

    ChrTalk(
        0xFE,
        "What's wrong, Dad?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E9E")

    label("loc_8E77")


    ChrTalk(
        0xFE,
        "Yaaay! The festival is soooo fun!\x02",
    )

    CloseMessageWindow()

    label("loc_8E9E")

    TalkEnd(0xFE)
    Return()

    # Function_36_8D4B end

    def Function_37_8EA2(): pass

    label("Function_37_8EA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8F23")

    ChrTalk(
        0xFE,
        (
            "Looks like a lot of people are heading out to\x01",
            "Mishelam today.\x01",
            "I think I'll go with the flow and join them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913E")

    label("loc_8F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9026")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8FCF")

    ChrTalk(
        0xFE,
        (
            "They managed to apprehend the thief at\x01",
            "Central Square?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of a sicko would go around doing stuff\x01",
            "like that during a celebration?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9021")

    label("loc_8FCF")


    ChrTalk(
        0xFE,
        (
            "What's with all of the stall owners looking disturbed?\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9021")

    Jump("loc_913E")

    label("loc_9026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_90DA")

    ChrTalk(
        0xFE,
        "Ice cream, juice, popcorn, and a grilled skewer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing better than a festival. Walking\x01",
            "down the street with everybody puts me in\x01",
            "a cheery mood!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_913E")

    label("loc_90DA")


    ChrTalk(
        0xFE,
        "The festival is here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why aren't you out there having fun? You've gotta\x01",
            "enjoy yourselves!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_913E")

    TalkEnd(0xFE)
    Return()

    # Function_37_8EA2 end

    def Function_38_9142(): pass

    label("Function_38_9142")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_91EF")

    ChrTalk(
        0xFE,
        (
            "Don't let his appearance fool you. The chairman of\x01",
            "the Business Owners' Association is a highly capable\x01",
            "man. I'm looking forward to hearing him speak.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_944C")

    label("loc_91EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9233")

    ChrTalk(
        0xFE,
        (
            "Wh-Wh-What?!\x01",
            "What's the matter with you people?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_944C")

    label("loc_9233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_92C3")

    ChrTalk(
        0xFE,
        (
            "The duo from earlier was amazing, but\x01",
            "this singer is no slouch, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't decide who I want to give my points to!\x02",
    )

    CloseMessageWindow()
    Jump("loc_944C")

    label("loc_92C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9335")

    ChrTalk(
        0xFE,
        "Wow, that performance was incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They're going to rake in a ton of points, for sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_944C")

    label("loc_9335")


    ChrTalk(
        0xFE,
        (
            "The Happy Quiz Tournament sponsored by the\x01",
            "Business Owners' Association is beginning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The grand prize is an all-expenses paid trip to Mishelam!\x01",
            "You can also win gift certificates provided by the\x01",
            "Business Owners' Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This won't be one you'll want to miss!\x02",
    )

    CloseMessageWindow()

    label("loc_944C")

    TalkEnd(0xFE)
    Return()

    # Function_38_9142 end

    def Function_39_9450(): pass

    label("Function_39_9450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9492")

    ChrTalk(
        0xFE,
        "Ooh, it's the chairman!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "You can do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A1")

    label("loc_9492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9503")

    ChrTalk(
        0xFE,
        "Wait, what?! Aren't those the thugs from earlier?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What do you guys think you're doing?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A1")

    label("loc_9503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9553")

    ChrTalk(
        0xFE,
        "We were told we could participate, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wanna try it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A1")

    label("loc_9553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9575")

    ChrTalk(
        0xFE,
        "You can do it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A1")

    label("loc_9575")


    ChrTalk(
        0xFE,
        "Don't worry, I've got this in the bag!\x02",
    )

    CloseMessageWindow()

    label("loc_95A1")

    TalkEnd(0xFE)
    Return()

    # Function_39_9450 end

    def Function_40_95A5(): pass

    label("Function_40_95A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_95DB")

    ChrTalk(
        0xFE,
        "Aw, the festival's almost over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_95DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9604")

    ChrTalk(
        0xFE,
        "Wh-What's happening?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_9604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9668")

    ChrTalk(
        0xFE,
        (
            "I'm jealous of her... Not only is she beautiful,\x01",
            "but she also has a great voice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_9668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9737")

    ChrTalk(
        0xFE,
        (
            "The Business Owners' Association is sponsoring\x01",
            "today's performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no way I'm missing this!\x01",
            "Apparently, all of the participants get coupons\x01",
            "for discounts at the food stalls!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A2")

    label("loc_9737")


    ChrTalk(
        0xFE,
        "Ooh, these prizes are great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This looks totally worth it...\x01",
            "I'm definitely going to participate!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A2")

    TalkEnd(0xFE)
    Return()

    # Function_40_95A5 end

    def Function_41_97A6(): pass

    label("Function_41_97A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9827")

    ChrTalk(
        0xFE,
        "That dude's pretty cool for an old man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's apparently the head of the Business Owners' Association.\x02",
    )

    CloseMessageWindow()
    Jump("loc_99F1")

    label("loc_9827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_98BA")

    ChrTalk(
        0xFE,
        (
            "All these people came outta nowhere after\x01",
            "the parade ended!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do you think they're here because the\x01",
            "parade got them excited?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F1")

    label("loc_98BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9937")

    ChrTalk(
        0xFE,
        (
            "Hmm, I still have some time until the parade starts...\x01",
            "I think I'll take a look around while I still can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F1")

    label("loc_9937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9976")

    ChrTalk(
        0xFE,
        "Aren't you being a little too greedy, Mama?\x02",
    )

    CloseMessageWindow()
    Jump("loc_99F1")

    label("loc_9976")


    ChrTalk(
        0xFE,
        (
            "I can't wait to see what's in store for today!\x01",
            "You think they'll be able to outdo yesterday's\x01",
            "incredible performance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F1")

    TalkEnd(0xFE)
    Return()

    # Function_41_97A6 end

    def Function_42_99F5(): pass

    label("Function_42_99F5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        "At long last, it is time I depart for Mishelam. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Granted, I've only been waiting ten minutes.\x01",
            "Doesn't mean it hasn't felt like an eternity! ㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_99F5 end

    def Function_43_9A97(): pass

    label("Function_43_9A97")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, man, I'm so nervous... My girlfriend\x01",
            "and I are headed to Mishelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's basically become a tradition to go there\x01",
            "on the last day of the festival, right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_9A97 end

    def Function_44_9B45(): pass

    label("Function_44_9B45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9BC6")

    ChrTalk(
        0xFE,
        "Hmm, do we bring him back some ice cream, or...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I don't know... Dad might like noodles better.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C90")

    label("loc_9BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9C2B")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "N-Now, hold on just a minute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The parade was fantastic!\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C90")

    label("loc_9C2B")


    ChrTalk(
        0xFE,
        "I'm going out with my mom today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been quite a while since I\x01",
            "last spent time with her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C90")

    TalkEnd(0xFE)
    Return()

    # Function_44_9B45 end

    def Function_45_9C94(): pass

    label("Function_45_9C94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9CFA")

    ChrTalk(
        0xFE,
        (
            "I absolutely must bring my husband a\x01",
            "souvenir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm... What are my options?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F16")

    label("loc_9CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9DA6")

    ChrTalk(
        0xFE,
        (
            "It's a shame I wasn't able to watch Arc en Ciel,\x01",
            "but at least I was able to enjoy the parade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should invite my husband to come\x01",
            "with us next year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F16")

    label("loc_9DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_9E06")

    ChrTalk(
        0xFE,
        "Where would you like to go next, Momo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you want to go to that store?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F16")

    label("loc_9E06")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        (
            "My husband didn't want to do the shopping,\x01",
            "so I brought Momo to take care of it with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I tried to get him to come with us, since we\x01",
            "don't get to spend much time as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not exactly the biggest fan of all this\x01",
            "commotion, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    SetScenarioFlags(0x1, 7)

    label("loc_9F16")

    TalkEnd(0xFE)
    Return()

    # Function_45_9C94 end

    def Function_46_9F1A(): pass

    label("Function_46_9F1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A0BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_9FF0")

    ChrTalk(
        0xFE,
        (
            "*sigh* I've only been keeping watch of\x01",
            "the park here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's frustrating we can't do anything about\x01",
            "what's going on at Mishelam. Even the\x01",
            "First Division has to look the other way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0BA")

    label("loc_9FF0")


    ChrTalk(
        0xFE,
        "There are tons of people headed to Mishelam today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0001F(Looks like they're aware of what\x01",
            "the Schwarze Auction is really about.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0101F(Well, they ARE the First Division...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_A0BA")

    Jump("loc_A606")

    label("loc_A0BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 6)), scpexpr(EXPR_END)), "loc_A2B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_A15F")

    ChrTalk(
        0xFE,
        (
            "Do not alarm any of the citizens by letting them\x01",
            "find out that I'm acting as a guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try not to speak too much to me. Thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2B1")

    label("loc_A15F")


    ChrTalk(
        0xFE,
        (
            "Do not alarm any of the citizens by letting them\x01",
            "find out that I'm acting as a guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Try not to speak too much to me. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0003F(Come to think of it, I didn't even notice them\x01",
            "come in during yesterday's performance.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F(Creepin' around kinda seems like it'd be\x01",
            "the First Division's forte, don't ya think?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)

    label("loc_A2B1")

    Jump("loc_A606")

    label("loc_A2B6")


    ChrTalk(
        0xFE,
        (
            "Oh, it's the SSS...\x01",
            "What might you all be doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#0005FYou're one of the detectives from the First\x01",
            "Division, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300FYou actin' as security for the festival around\x01",
            "here or somethin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, yes. The crowds are completely vulnerable\x01",
            "during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not to mention, there are plenty of influential\x01",
            "and wealthy people here. We can't ignore\x01",
            "the possibility of a terrorist attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FYou must be under tremendous pressure knowing\x01",
            "the safety of these people rests in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Naturally. We don't have the luxury to\x01",
            "stand around behaving carefree like\x01",
            "the lot of you.\x02",
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
        0x103,
        "#0200F(I am detecting slight hints of animosity.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 6)

    label("loc_A606")

    TalkEnd(0xFE)
    Return()

    # Function_46_9F1A end

    def Function_47_A60A(): pass

    label("Function_47_A60A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A74E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_A697")

    ChrTalk(
        0xFE,
        (
            "Not only have I realized my lack of talent, but\x01",
            "now I lose my wallet? This sucks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What the heck do I do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A749")

    label("loc_A697")


    ChrTalk(
        0xFE,
        (
            "I was considering returning home to Liberl\x01",
            "today, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't seem to find my wallet anywhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What the heck do I do?\x01",
            "Have I done something to anger Aidios?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_A749")

    Jump("loc_ADF7")

    label("loc_A74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A8C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_A7F1")

    ChrTalk(
        0xFE,
        (
            "I've already given up living the life\x01",
            "of a poet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't been here for long, but I'm considering\x01",
            "returning to Liberl already...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8C2")

    label("loc_A7F1")


    ChrTalk(
        0xFE,
        (
            "People's refusal to acknowledge my existence as\x01",
            "I read my magnificent poetry... It stings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Am I not the creative genius I once thought\x01",
            "I was?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've already given up living the life\x01",
            "of a poet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_A8C2")

    Jump("loc_ADF7")

    label("loc_A8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AB2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_A99E")

    ChrTalk(
        0xFE,
        (
            "Nobody around here wants to listen to me\x01",
            "serenade their ears with my beautiful poetry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn it! I'd cry tears of joy if I could get a single\x01",
            "person to stay and listen at this point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB25")

    label("loc_A99E")


    ChrTalk(
        0xFE,
        (
            "Hey, you. How would you like to hear the poetry\x01",
            "of a man blessed by Aidios Herself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Travel shamelessly and live with kindness...\x01",
            "The transience of the world will echo through your life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well? What'd you think? Amazing, right?!\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0003F(That was supposed to be poetry?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_AB25")

    Jump("loc_ADF7")

    label("loc_AB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AD38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_ABD7")

    ChrTalk(
        0xFE,
        (
            "In order to change one's self, the change\x01",
            "must come from within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I get what it's trying to say, but how do I\x01",
            "actually approach the problem?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD33")

    label("loc_ABD7")


    ChrTalk(
        0xFE,
        "I've been in Crossbell for three days now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city rages on, but I continue to stand by idly.\x01",
            "Was I not supposed to change? Why have I\x01",
            "not yet changed?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A gentle light shines down from the skies,\x01",
            "so on these wasted days... Anton is\x01",
            "out here, trying his best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, nothing beats a good poem.\x01",
            "That cheered me up a little bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_AD33")

    Jump("loc_ADF7")

    label("loc_AD38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_ADF4")

    ChrTalk(
        0xFE,
        (
            "I don't have a job. I don't have a girlfriend.\x01",
            "Damn, my life is a meaningless facade...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aidios, won't you please bless me with\x01",
            "pleasant memories during my travels?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADF7")

    label("loc_ADF4")

    Call(0, 49)

    label("loc_ADF7")

    TalkEnd(0xFE)
    Return()

    # Function_47_A60A end

    def Function_48_ADFB(): pass

    label("Function_48_ADFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AEDB")
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "No one likes a downer, Anton. You always\x01",
            "let your bad habits get a hold of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You know how it goes, anyway. You're just\x01",
            "going to unexpectedly find it after you've\x01",
            "long forgotten about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51C")

    label("loc_AEDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B0C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_AFB5")
    OP_93(0x20, 0x87, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hey, Anton. Check this out!\x01",
            "Doesn't this performance look fun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Supposedly anyone can participate.\x01",
            "Wanna go and sing together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It might lighten up that cruddy mood of yours.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0C2")

    label("loc_AFB5")


    ChrTalk(
        0xFE,
        (
            "Anton's been standing here all day trying to\x01",
            "read his poems to strangers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It went about as poorly as you'd expect.\x01",
            "He's been completely stricken with grief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come on, bud. Wanna check out some of the food stalls?\x01",
            "You're probably getting pretty hungry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_B0C2")

    Jump("loc_B51C")

    label("loc_B0C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B1F0")

    ChrTalk(
        0xFE,
        (
            "Anton came up to me this morning and said\x01",
            "that he wanted to try being a street poet all\x01",
            "of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's Anton, though. We already know how this is\x01",
            "going to end. I bet he'll give up by the end of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm barely paying attention to what he's doing,\x01",
            "as per usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51C")

    label("loc_B1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B41A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_B2D8")
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "I'm sure he'll call on me once he's decided\x01",
            "what he wants to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knows how long it'll be, though?\x01",
            "In the meantime, that bench is looking comfy.\x01",
            "I think I'll take myself a nice little nap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B415")

    label("loc_B2D8")


    ChrTalk(
        0xFE,
        (
            "Poor guy had his heart broken pretty badly.\x01",
            "He figured he'd become a poet as an outlet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To his credit, he's lasted a lot longer than I was\x01",
            "expecting. Anton's a fickle guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, regardless of whether this all works out...\x01",
            "Anton hasn't taken into consideration how\x01",
            "he'll pay for his living expenses.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)

    label("loc_B415")

    Jump("loc_B51C")

    label("loc_B41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_B508")

    ChrTalk(
        0xFE,
        (
            "We're a ways away from Liberl. I've been\x01",
            "accompanying him all over the continent\x01",
            "during his soul search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's never a dull day with Anton around.\x01",
            "Who knows what misadventures we'll get\x01",
            "ourselves into this time?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B51C")

    label("loc_B508")

    Call(0, 49)
    TurnDirection(0x20, 0x0, 0)
    OP_93(0x20, 0xB4, 0x0)
    SetScenarioFlags(0x2, 2)

    label("loc_B51C")

    TalkEnd(0xFE)
    Return()

    # Function_48_ADFB end

    def Function_49_B520(): pass

    label("Function_49_B520")

    OP_4B(0x1F, 0xFF)
    OP_4B(0x20, 0xFF)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)

    ChrTalk(
        0x1F,
        (
            "I've been soul searching for a while now...\x01",
            "Pretty far away from home at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "I like that Crossbell is bustling all the time.\x01",
            "It makes me want to stay busy, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1F,
        (
            "Hey, Ricky. Don't you think I'll be able\x01",
            "to figure out my life's calling in a place\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        "I don't know, man. Not my place to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x20,
        (
            "I get you're impatient, but, Anton...\x01",
            "You seriously need to calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    SetScenarioFlags(0x2, 1)
    OP_4C(0x1F, 0xFF)
    OP_4C(0x20, 0xFF)
    Return()

    # Function_49_B520 end

    def Function_50_B6D5(): pass

    label("Function_50_B6D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B8C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_B73E")

    ChrTalk(
        0x2E,
        (
            "#1601FWatch where you're goin'.\x01",
            "Just about kicked you as hard as I could.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8C0")

    label("loc_B73E")

    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)

    ChrTalk(
        0x2E,
        (
            "#1601FHey, you punk. Did I say you could\x01",
            "bump into me?\x02\x03",
            "#1607FYa dropped your wallet, moron.\x01",
            "Get it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Oh. It's my wallet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x22,
        "Sweet, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        "Oh, no...\x02",
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
        "#0005F(Wh-What's he doing?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0306F(Yeah, gettin' involved is a hard pass\x01",
            "from me.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x21, 0xFF)
    OP_4C(0x22, 0xFF)

    label("loc_B8C0")

    Jump("loc_B9C5")

    label("loc_B8C5")


    ChrTalk(
        0x2E,
        (
            "#1600FYou punks workin' right now?\x02\x03",
            "#1602FHaha... Must suck bein' cops at a time like this.\x01",
            "Thanks for keepin' the streets safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#0006F*sigh* If you actually feel bad for us, then\x01",
            "could you please not make our job any\x01",
            "harder than it needs to be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9C5")

    TalkEnd(0xFE)
    Return()

    # Function_50_B6D5 end

    def Function_51_B9C9(): pass

    label("Function_51_B9C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BA55")

    ChrTalk(
        0x2F,
        "Woohoo! I get to sing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Yer all welcome to join me! Again, yer all\x01",
            "welcome to join me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "Waaaaaaaaahooooooooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BAAB")

    label("loc_BA55")


    ChrTalk(
        0x2F,
        "Gahahahaha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "Would ya take a look at that?!\x01",
            "How's a squirt runnin' a stall?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAAB")

    TalkEnd(0xFE)
    Return()

    # Function_51_B9C9 end

    def Function_52_BAAF(): pass

    label("Function_52_BAAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BB31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_BB29")
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x30,
        "If Luganov wants to sing, he's gonna sing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "Just stand back and listen, idiot.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_BB2C")

    label("loc_BB29")

    Call(0, 53)

    label("loc_BB2C")

    Jump("loc_BB86")

    label("loc_BB31")


    ChrTalk(
        0x30,
        "What's with the cops lookin' all jittery?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "You guys dealin' with somethin'?\x02",
    )

    CloseMessageWindow()

    label("loc_BB86")

    TalkEnd(0xFE)
    Return()

    # Function_52_BAAF end

    def Function_53_BB8A(): pass

    label("Function_53_BB8A")

    OP_4B(0x30, 0xFF)
    OP_4B(0x14, 0xFF)

    ChrTalk(
        0x14,
        "What in the hell are you guys doing?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Get off the stage! Right this instant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x30,
        "Shut it, dumbass!\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    TurnDirection(0x14, 0x30, 500)
    Sleep(300)

    ChrTalk(
        0x14,
        "Ack! What are you doing?!\x02",
    )

    CloseMessageWindow()
    OP_64(0x14)
    OP_93(0x14, 0x0, 0x0)
    SetScenarioFlags(0x2, 4)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x30, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_53_BB8A end

    def Function_54_BC57(): pass

    label("Function_54_BC57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BCB9")

    ChrTalk(
        0x31,
        "I'm tellin' ya to back off!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "I'll send ya flyin' if you get in the way!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD6D")

    label("loc_BCB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_BCE9")

    ChrTalk(
        0x31,
        "Where we headed today, Wald?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD6D")

    label("loc_BCE9")


    ChrTalk(
        0x31,
        "You look like yer rarin' to go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "Where we headed today, Wald?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "Maybe we can get a sick view at the top\x01",
            "of the hill!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)

    label("loc_BD6D")

    TalkEnd(0xFE)
    Return()

    # Function_54_BC57 end

    def Function_55_BD71(): pass

    label("Function_55_BD71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BDF2")

    ChrTalk(
        0x32,
        (
            "I bet this kid thinks he's real tough\x01",
            "bumpin' into Wald. Screw him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        "He tryin' to get himself killed?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BE6B")

    label("loc_BDF2")


    ChrTalk(
        0x32,
        (
            "Holy crap!\x01",
            "That chick running the stall is hot as hell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x32,
        (
            "Hey, honey! You wanna have a good time\x01",
            "with me later?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6B")

    TalkEnd(0xFE)
    Return()

    # Function_55_BD71 end

    def Function_56_BE6F(): pass

    label("Function_56_BE6F")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FThe Anniversary Festival is great,\x01",
            "but the reel party is right here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63790, 0, 7940, 1500)
    MoveCamera(45, 23, 0, 1500)
    OP_6E(280, 1500)
    SetCameraDistance(29000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Try fishing?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF61")
    OP_E0(0x2)
    MiniGame(0x6, 0x1, 0x10BE4, 0xFFFFF63C, 0x4074, 0xB4, 0x109C8, 0xFFFFF254, 0x2E2C)

    label("loc_BF61")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_56_BE6F end

    def Function_57_BF66(): pass

    label("Function_57_BF66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6FB")
    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#0100F#6PWhat should we do, Lloyd?\x02\x03",
            "Are we ready to ride the ship to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#0003F#11PLet's see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Not ready yet]\x01",            # 0
            "[Depart for Mishelam]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C0C5"),
        (1, "loc_C362"),
        (SWITCH_DEFAULT, "loc_C6F6"),
    )


    label("loc_C0C5")


    ChrTalk(
        0x101,
        (
            "#0000F#11PWe'll have to let go of any remaining work once\x01",
            "we depart for Mishelam.\x02\x03",
            "The ship leaves frequently enough that we can\x01",
            "board once we're sure we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#0100F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#0202F#1PI believe it to be pertinent for us to shop and\x01",
            "upgrade any equipment before we depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0300F#6PSounds good. We'll head back here once we're\x01",
            "all spruced up and ready to roll.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you wish to ride the ship,\x01",
            "please consult the schedule.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Additionally, any outstanding support requests\x01",
            "from the festival period will be automatically\x01",
            "terminated once you depart for Mishelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    EventEnd(0x5)
    Jump("loc_C6F6")

    label("loc_C362")


    ChrTalk(
        0x101,
        (
            "#0000F#11POkay... Let's wait for the ship to come.\x02\x03",
            "#0006FIt's a little late for me to say this, but doesn't\x01",
            "our attire seem a bit...casual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0106F#6PYou're not wrong...\x02\x03",
            "#0108FSomething more on the formal side may have\x01",
            "been more appropriate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#0303F#6PWell, we don't know if we'll even be crashing the\x01",
            "party yet. Finding some duds can wait.\x02\x03",
            "#0300FWe'll probably mix right in with the tourists that\x01",
            "came to check out the theme park, so chill out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#0203F#5PWhile that may be true, I also agree that\x01",
            "our attire is slightly too informal.\x02\x03",
            "#0202FShould we not have come fully dressed\x01",
            "in Mishy pajamas?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C5D8():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5D8)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#0012F#11PUh, denied. We would have stood out far too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0109F#12PJust because Mishy is the park's mascot, doesn't\x01",
            "mean it's an excuse to wear those in public.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_65(0x0, 0x1)
    Call(0, 59)
    Jump("loc_C6F6")

    label("loc_C6F6")

    Jump("loc_C7E2")

    label("loc_C6FB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell City Cruise Ship Schedule\x01\x01",
            "The pride of Mishelam, Mishelam Wonderland,\x01",
            "is now open for all to enjoy! Come on down and\x01",
            "experience the greatest theme park of all time!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_C7E2")

    Return()

    # Function_57_BF66 end

    def Function_58_C7E3(): pass

    label("Function_58_C7E3")

    EventBegin(0x0)
    Fade(1000)
    OP_68(34650, -1200, -280, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14510, 0)
    SetChrPos(0x101, 35000, -2500, 0, 90)
    SetChrPos(0x102, 33600, -2500, -800, 90)
    SetChrPos(0x103, 34000, -2500, 800, 90)
    SetChrPos(0x104, 32600, -2500, 0, 90)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#3500085V#0008F#5PAll right, we're here.\x02\x03",
            "#3500086V#0001FLet's wait here until the next ship to Mishelam\x01",
            "gets here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500087V#0100F#6PThere should be a ship every 30 minutes\x01",
            "or so at this time of the day...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)

    def lambda_C942():

        label("loc_C942")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_C942")

    QueueWorkItem2(0x101, 1, lambda_C942)

    def lambda_C954():

        label("loc_C954")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_C954")

    QueueWorkItem2(0x102, 1, lambda_C954)

    def lambda_C966():

        label("loc_C966")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_C966")

    QueueWorkItem2(0x104, 1, lambda_C966)

    def lambda_C978():
        OP_95(0xFE, 34000, -2500, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C978)
    WaitChrThread(0x103, 1)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#3500088V#0200F#5PApparently, the frequency is increased to once every\x01",
            "20 minutes for the duration of the festival.\x02\x03",
            "#3500089VAccording to the schedule, the last one leaves at\x01",
            "half past midnight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500090V#0005F#12PWow, they operate that late?\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)

    def lambda_CA9E():
        OP_95(0xFE, 34000, -2500, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CA9E)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    def lambda_CAC8():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CAC8)

    def lambda_CAD5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CAD5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    ChrTalk(
        0x104,
        (
            "#3500091V#0304F#6PMakes sense to me. You'd probs be out pretty\x01",
            "late into night if you're spendin' the whole day at\x01",
            "the park, then sharin' a meal with a sexy lady.\x02\x03",
            "#3500092V#0300FThose hotels cost a pretty mira, too. Ain't no\x01",
            "way most people are payin' the price.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#3500093V#0106F#6PI would assume most of the hotels are fully\x01",
            "booked for the duration of the festival, too.\x02\x03",
            "#3500094V#0100FWhat should we do, Lloyd?\x02\x03",
            "#3500095VAre we ready to ride the ship to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x101,
        "#3500096V#0003F#11PLet's see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xA3, 4)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Not ready yet]\x01",            # 0
            "[Depart for Mishelam]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CD58"),
        (1, "loc_D02B"),
        (SWITCH_DEFAULT, "loc_D3FF"),
    )


    label("loc_CD58")


    ChrTalk(
        0x101,
        (
            "#3500097V#0000F#11PWe'll have to let go of any remaining work once\x01",
            "we depart for Mishelam.\x02\x03",
            "#3500098VThe ship leaves frequently enough that we can\x01",
            "board once we're sure we're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500099V#0100F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500100V#0202F#1PI believe it to be pertinent for us to shop and\x01",
            "upgrade any equipment before we depart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500101V#0300F#6PSounds good. We'll head back here once we're\x01",
            "all spruced up and ready to roll.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you wish to ride the ship,\x01",
            "please consult the schedule.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Additionally, any outstanding support requests\x01",
            "from the festival period will be automatically\x01",
            "terminated once you depart for Mishelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, 34000, -2500, 0, 270)
    ModifyEventFlags(0, 0, 0x80)
    OP_66(0x0, 0x1)
    EventEnd(0x5)
    Jump("loc_D3FF")

    label("loc_D02B")


    ChrTalk(
        0x101,
        (
            "#3500102V#0000F#11POkay... Let's wait for the ship to come.\x02\x03",
            "#3500103V#0006FIt's a little late for me to say this, but doesn't\x01",
            "our attire seem a bit...casual?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500104V#0106F#6PYou're not wrong...\x02\x03",
            "#3500105V#0108FSomething more on the formal side may have\x01",
            "been more appropriate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500106V#0303F#6PWell, not like we can't enter the party the way\x01",
            "we are now, right?\x02\x03",
            "#3500107V#0300FWe'll probably mix right in with the tourists that\x01",
            "came to check out the theme park, so chill out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    ChrTalk(
        0x103,
        (
            "#3500108V#0203F#5PWhile that may be true, I also agree that our attire\x01",
            "is slightly too informal.\x02\x03",
            "#3500109V#0202FShould we not have come fully dressed\x01",
            "in Mishy pajamas?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D2D3():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D2D3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3500110V#0012F#11PUh, denied. We would have stood out far too much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500111V#0109F#12PJust because Mishy is the park's mascot, doesn't\x01",
            "mean it's an excuse to wear those in public.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Call(0, 59)
    Jump("loc_D3FF")

    label("loc_D3FF")

    Return()

    # Function_58_C7E3 end

    def Function_59_D400(): pass

    label("Function_59_D400")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x32)
    LoadChrToIndex("chr/ch07300.itc", 0x33)
    SoundLoad(479)
    OP_93(0xF, 0x87, 0x0)
    OP_4B(0xF, 0xFF)
    OP_4B(0x21, 0xFF)
    OP_4B(0x22, 0xFF)
    OP_4B(0x28, 0xFF)
    OP_4B(0x29, 0xFF)
    SetChrPos(0x21, 41400, -2500, -3400, 0)
    SetChrPos(0x22, 40300, -2500, -3400, 0)
    SetChrPos(0x28, 41400, -2500, -4700, 0)
    SetChrPos(0x29, 40300, -2500, -4700, 0)
    SetChrPos(0x101, 40300, -2500, -6000, 0)
    SetChrPos(0x102, 41400, -2500, -6000, 0)
    SetChrPos(0x103, 40300, -2500, -7300, 0)
    SetChrPos(0x104, 41400, -2500, -7300, 0)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrChipByIndex(0x44, 0xE)
    SetChrChipByIndex(0x45, 0xF)
    SetChrChipByIndex(0x46, 0x10)
    SetChrChipByIndex(0x47, 0x11)
    SetChrChipByIndex(0x48, 0x12)
    SetChrChipByIndex(0x49, 0x13)
    SetChrChipByIndex(0x4A, 0x14)
    SetChrChipByIndex(0x4B, 0x15)
    SetChrChipByIndex(0x4C, 0x16)
    SetChrChipByIndex(0x4D, 0x17)
    SetChrSubChip(0x44, 0x0)
    SetChrSubChip(0x45, 0x0)
    SetChrSubChip(0x46, 0x0)
    SetChrSubChip(0x47, 0x0)
    SetChrSubChip(0x48, 0x0)
    SetChrSubChip(0x49, 0x0)
    SetChrSubChip(0x4A, 0x0)
    SetChrSubChip(0x4B, 0x0)
    SetChrSubChip(0x4C, 0x0)
    SetChrSubChip(0x4D, 0x0)
    ClearChrFlags(0x44, 0x4)
    ClearChrFlags(0x45, 0x4)
    ClearChrFlags(0x46, 0x4)
    ClearChrFlags(0x47, 0x4)
    ClearChrFlags(0x48, 0x4)
    ClearChrFlags(0x49, 0x4)
    ClearChrFlags(0x4A, 0x4)
    ClearChrFlags(0x4B, 0x4)
    ClearChrFlags(0x4C, 0x4)
    ClearChrFlags(0x4D, 0x4)
    SetChrPos(0x44, 48000, -2500, -1250, 270)
    SetChrPos(0x45, 48000, -2500, -2250, 270)
    SetChrPos(0x46, 48000, -2500, -1250, 270)
    SetChrPos(0x47, 48000, -2500, -2250, 270)
    SetChrPos(0x48, 48000, -2500, -1250, 270)
    SetChrPos(0x49, 48000, -2500, -2250, 270)
    SetChrPos(0x4A, 48000, -2500, -1250, 270)
    SetChrPos(0x4B, 48000, -2500, -2250, 270)
    SetChrPos(0x4C, 48000, -2500, -1250, 270)
    SetChrPos(0x4D, 48000, -2500, -2250, 270)
    OP_A7(0x44, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x45, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x46, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x47, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x48, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrChipByIndex(0x34, 0x32)
    SetChrSubChip(0x34, 0x0)
    SetChrPos(0x34, 33000, -2500, -1500, 90)
    SetChrFlags(0x34, 0x8000)
    ClearChrFlags(0x34, 0x80)
    ClearChrBattleFlags(0x34, 0x8000)
    SetChrChipByIndex(0x33, 0x33)
    SetChrSubChip(0x33, 0x0)
    SetChrPos(0x33, 33000, -2500, -1500, 90)
    SetChrFlags(0x33, 0x8000)
    ClearChrFlags(0x35, 0x80)
    OP_78(0x9, 0x35)
    OP_49()
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    SetChrPos(0x35, 51800, -3850, -4000, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03500.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    OP_68(35100, 1000, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7518", 0)
    FadeToBright(1000, 0)
    OP_68(35100, 0, -7650, 3000)
    OP_6F(0x1)
    OP_0D()

    NpcTalk(
        0x34,
        "Carefree Voice",
        "#3500112VHmm... Probably somewhere around here?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D8AA():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8AA)

    def lambda_D8B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D8B7)
    Sleep(100)

    def lambda_D8C7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D8C7)

    def lambda_D8D4():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D8D4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_D951():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_D951)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3500113V#0005F#6P(You think he's a tourist?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500114V#0100F#12P(Likely. He certainly plays the part.)\x02",
    )

    CloseMessageWindow()
    OP_93(0x34, 0x2D, 0x1F4)
    Sleep(200)
    TurnDirection(0x34, 0x101, 500)
    Sleep(200)
    OP_68(39450, -1300, -5400, 2000)

    def lambda_DA04():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_DA04)
    WaitChrThread(0x34, 1)
    OP_6F(0x79)
    Sleep(200)

    NpcTalk(
        0x34,
        "Carefree Young Man",
        (
            "#3500115V#3500F#5PHey, you youngins.\x02\x03",
            "#3500116VYou care if I ask you a quick question?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500117V#0000F#12PNo, go right ahead.\x02\x03",
            "#3500118VYou look like you're a tourist. Are you\x01",
            "lost, by any chance?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x34,
        "Carefree Young Man",
        (
            "#3500119V#3506F#5PYeah. The town's a bit too large, don'tcha think?\x02\x03",
            "#3500120V#3500FI'm trying to get to Mishelam.\x01",
            "Am I at the right place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#3500121V#0005F#12PYeah, you are.\x02\x03",
            "#3500122V#0000FWe're also waiting to take the ship\x01",
            "out to Mishelam.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x34,
        "Carefree Young Man",
        (
            "#3500123V#3502F#5PNice, I was right on the mark.\x02\x03",
            "#3500124V#3504FSuppose I'll join you guys in the lineup.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x34,
        "Carefree Young Man",
        "#3500125V#3505F#5PWhoops. I haven't given you my name yet.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Carefree Young Man")

    AnonymousTalk(
        0xFF,
        (
            "#3500126VThe name's Lechter. Lechter Arundel.\x02\x03",
            "#3500127VI just got here pretty recently.\x01",
            "Took the train out from Heimdallr.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        "#3500128V#0005F#12PThe Imperial capital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3500129V#0100F#12PDo you live in the Empire, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3500130V#0300F#12PI gotta give you props, my man.\x01",
            "You're lookin' hella stylish.\x02\x03",
            "#3500131VThat sunglasses and shirt combo has you\x01",
            "lookin' all play and no work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#3500132V#3509F#5PYeah, well. Crossbell's famous for its\x01",
            "resort, y'know?\x02\x03",
            "#3500133VYou know what they say... When in Crossbell,\x01",
            "do as the Crossbellans do. I'm all fired up\x01",
            "to play my part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500134V#0206F#6PI think you are getting fired up for the\x01",
            "wrong reasons...\x02\x03",
            "#3500135V#0202FI assume you are here to visit the theme\x01",
            "park?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x34,
        (
            "#3500136V#3505F#5PTheme park?\x02\x03",
            "#3500137V#3501FThe hell's that? Do they have something\x01",
            "that interesting at Mishelam?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500138V#0012F#12PYeah. I've never been there before, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500139V#0109F#12PMishelam started as a wellness resort,\x01",
            "but has recently become more famous\x01",
            "for its other activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x34,
        (
            "#3500140V#3500F#5POh, I get it.\x02\x03",
            "#3500141V#3506FAnyway, I'm here to attend as a representative.\x02\x03",
            "#3500142VMaybe I shoulda given myself some more time to\x01",
            "check out the other stuff. Sounds fun.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#3500143V#0001F#12PAttend...as a representative?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x34, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x34, 0x5A, 0x1F4)

    ChrTalk(
        0x34,
        "#3500144V#3502F#6POh, the ship is here.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_93(0xF, 0xB4, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0x35, 126220, -3850, -50690, 315)
    OP_D3(0x35, 0x0, 0x4CE78, 0x0, 0x0)
    BeginChrThread(0x53, 1, 0, 64)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x0, 0x1)
    OP_68(59280, 17600, -8870, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(51010, 0)
    OP_68(59280, 8000, -8870, 10000)

    def lambda_E4A4():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_E4A4)
    OP_0D()
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetMapObjFrame(0xFF, "yuragi01_add", 0x1, 0x1)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_93(0x101, 0x2D, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x103, 0x2D, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x34, 0x2D, 0x0)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    OP_D3(0x35, 0x0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0x35, 54800, -3850, -4000, 0)
    Sound(476, 0, 100, 0)
    Sound(477, 0, 100, 0)

    def lambda_E578():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_E578)
    WaitChrThread(0x35, 1)
    OP_82(0x32, 0x0, 0xBB8, 0x1F4)
    Sound(478, 0, 100, 0)
    OP_71(0x9, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x12D, 0x168, 0x0, 0x20)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x9)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    Sleep(500)
    BeginChrThread(0x44, 3, 0, 60)
    Sleep(280)
    BeginChrThread(0x45, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x46, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x47, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x48, 3, 0, 60)
    Sleep(150)
    BeginChrThread(0x49, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4A, 3, 0, 60)
    Sleep(50)
    BeginChrThread(0x4B, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x4C, 3, 0, 60)
    Sleep(180)
    BeginChrThread(0x4D, 3, 0, 60)
    Sleep(5000)
    BeginChrThread(0x21, 3, 0, 61)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 62)
    Sleep(800)
    BeginChrThread(0x28, 3, 0, 61)
    Sleep(200)
    BeginChrThread(0x29, 3, 0, 62)
    Sleep(2000)
    EndChrThread(0x44, 0x3)
    EndChrThread(0x45, 0x3)
    EndChrThread(0x46, 0x3)
    EndChrThread(0x47, 0x3)
    EndChrThread(0x48, 0x3)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)
    EndChrThread(0x4C, 0x3)
    EndChrThread(0x4D, 0x3)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x80)
    SetChrBattleFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x80)
    SetChrBattleFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x80)
    SetChrBattleFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x80)
    SetChrBattleFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x80)
    SetChrBattleFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x80)
    SetChrBattleFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x80)
    SetChrBattleFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x80)
    SetChrBattleFlags(0x4D, 0x8000)
    EndChrThread(0x53, 0x1)
    OP_0D()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)
    OP_0D()

    ChrTalk(
        0x34,
        (
            "#3500145V#3504F#6PCool-looking boat, isn't it?\x02\x03",
            "#3500146V#3500FI'd better haul myself up there and get a\x01",
            "front-row seat on the deck.\x02\x03",
            "#3500147V#3509FI'll catch you guys later! ♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x34, 3, 0, 63)
    Sleep(500)

    def lambda_E7F0():

        label("loc_E7F0")

        TurnDirection(0x101, 0x34, 300)
        Yield()
        Jump("loc_E7F0")

    QueueWorkItem2(0x101, 1, lambda_E7F0)

    def lambda_E802():

        label("loc_E802")

        TurnDirection(0x102, 0x34, 300)
        Yield()
        Jump("loc_E802")

    QueueWorkItem2(0x102, 1, lambda_E802)

    def lambda_E814():

        label("loc_E814")

        TurnDirection(0x103, 0x34, 300)
        Yield()
        Jump("loc_E814")

    QueueWorkItem2(0x103, 1, lambda_E814)

    def lambda_E826():

        label("loc_E826")

        TurnDirection(0x104, 0x34, 300)
        Yield()
        Jump("loc_E826")

    QueueWorkItem2(0x104, 1, lambda_E826)
    WaitChrThread(0x34, 3)
    SetChrFlags(0x34, 0x80)
    SetChrBattleFlags(0x34, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    WaitChrThread(0x21, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x28, 3)
    WaitChrThread(0x29, 3)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(39290, 0, -7600, 0)
    MoveCamera(60, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11230, 0)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#3500148V#0106F#5PI didn't think it was possible, but that man might\x01",
            "be more easygoing than you, Randy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    ChrTalk(
        0x104,
        (
            "#3500149V#0303F#2PWhat's that supposed to mean?\x02\x03",
            "#3500150V#0301FDo I really look like some sorta\x01",
            "hedonist to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3500151V#0211F#6PI would be more shocked if someone\x01",
            "failed to get that impression of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500152V#0012F#6PThey both may be pleasure seekers, but they\x01",
            "seem to go about it in their own ways.\x02\x03",
            "#3500153V#0000FRather than being interested in nightlife and\x01",
            "hitting on women, he gives off an air of\x01",
            "complete freedom.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    ChrTalk(
        0x104,
        (
            "#3500154V#0309F#11PYou felt it, too?\x02\x03",
            "#3500155V#0300FWonder what a guy like him is doin' here\x01",
            "all alone. He looked about my age, too.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)

    NpcTalk(
        0x33,
        "Woman's Voice",
        "#3500156VOh, what a coincidence.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_EC6E():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC6E)

    def lambda_EC7B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC7B)
    Sleep(100)

    def lambda_EC8B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EC8B)

    def lambda_EC98():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EC98)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Fade(500)
    OP_68(37000, -1300, -5750, 0)
    OP_68(38150, -1300, -5750, 2000)
    MoveCamera(360, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15600, 0)
    OP_93(0x101, 0x13B, 0x0)
    OP_93(0x102, 0x13B, 0x0)
    OP_93(0x103, 0x13B, 0x0)
    OP_93(0x104, 0x13B, 0x0)

    def lambda_ED15():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_ED15)
    WaitChrThread(0x33, 1)
    TurnDirection(0x33, 0x101, 500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#3500157V#0005F#12PYou're here, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#3500158V#0305F#12PWhoa! Well, if it ain't my favorite gal, Kilika?!\x02",
    )

    CloseMessageWindow()
    OP_68(39450, -1300, -5400, 2000)

    def lambda_EDBF():
        OP_95(0xFE, 39030, -2500, -4320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_EDBF)
    WaitChrThread(0x33, 1)
    OP_6F(0x79)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    AnonymousTalk(
        0x33,
        (
            "#3500159VHaha. Thank you for your assistance\x01",
            "the other day.\x02\x03",
            "#3500160VHave all of you gathered here to go\x01",
            "to Mishelam?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    ChrTalk(
        0x102,
        "#3500161V#0100F#12PYes, we have. How about you, Kilika?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        (
            "#3500162V#3404F#5PI have both business and personal\x01",
            "matters to attend to there.\x02\x03",
            "#3500163V#3400FMore importantly... Who might that flashy\x01",
            "gentleman have been?\x02\x03",
            "#3500164VA friend of yours, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500165V#0004F#12PNope, that was our first time meeting him.\x02\x03",
            "#3500166V#0000FIt sounded like he came here from Erebonia's\x01",
            "capital to do some sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        (
            "#3500167V#3405F#5PHmm... Heimdallr...\x02\x03",
            "#3500168V#3404FHeh. I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500169V#0005F#12P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#3500170V#0205F#6PAre you acquainted with him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x33,
        (
            "#3500171V#3404F#5PI am not. That unique aura of his has merely\x01",
            "piqued my interest in him.\x02\x03",
            "#3500172V#3400FAnyway, I shall board now.\x01",
            "You should all do so as well.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(35100, 0, -7650, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9710, 0)

    def lambda_F1D6():

        label("loc_F1D6")

        TurnDirection(0x101, 0x33, 300)
        Yield()
        Jump("loc_F1D6")

    QueueWorkItem2(0x101, 1, lambda_F1D6)

    def lambda_F1E8():

        label("loc_F1E8")

        TurnDirection(0x102, 0x33, 300)
        Yield()
        Jump("loc_F1E8")

    QueueWorkItem2(0x102, 1, lambda_F1E8)

    def lambda_F1FA():

        label("loc_F1FA")

        TurnDirection(0x103, 0x33, 300)
        Yield()
        Jump("loc_F1FA")

    QueueWorkItem2(0x103, 1, lambda_F1FA)

    def lambda_F20C():

        label("loc_F20C")

        TurnDirection(0x104, 0x33, 300)
        Yield()
        Jump("loc_F20C")

    QueueWorkItem2(0x104, 1, lambda_F20C)
    OP_93(0x33, 0x41, 0x1F4)

    def lambda_F225():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_F225)
    WaitChrThread(0x33, 1)
    OP_93(0x33, 0x5A, 0x0)

    def lambda_F245():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_F245)
    Sleep(2000)

    def lambda_F25D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_F25D)
    WaitChrThread(0x33, 1)
    WaitChrThread(0x33, 2)
    SetChrFlags(0x33, 0x80)
    SetChrBattleFlags(0x33, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#3500173V#0309F#12PMaaan, she's one cool chick. Not to mention, hot.\x01",
            "I can't get enough of her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3500174V#0000F#6PI know she said she was going there for\x01",
            "business, but do you guys think she's\x01",
            "headed for the theme park?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#3500175V#0100F#5PConsidering she works in the entertainment\x01",
            "industry, I'd wager as much.\x02",
        )
    )

    CloseMessageWindow()
    Sound(475, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#3500176V#0205F#12PThe ship appears to be departing soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3500177V#0000F#6PYeah, we should hop on.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(9210, 2000)
    OP_6F(0x10)
    OP_0D()
    OP_4C(0xF, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_68(35920, 400, -3820, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16670, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    OP_71(0x9, 0x1F, 0x5A, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(1000)
    Sound(478, 0, 100, 0)
    OP_79(0x9)
    Sound(477, 0, 100, 0)
    Sleep(200)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_F586():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_F586)
    WaitChrThread(0x35, 1)

    def lambda_F5A4():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_F5A4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x35, 1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearScenarioFlags(0x5A, 2)
    OP_24(0x1DF)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_D400 end

    def Function_60_F5E4(): pass

    label("Function_60_F5E4")


    def lambda_F5E9():
        OP_9B(0x0, 0xFE, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F5E9)

    def lambda_F5FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F5FE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_60_F5E4 end

    def Function_61_F613(): pass

    label("Function_61_F613")


    def lambda_F618():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F618)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_F638():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F638)
    Sleep(3000)

    def lambda_F650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F650)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_61_F613 end

    def Function_62_F665(): pass

    label("Function_62_F665")


    def lambda_F66A():
        OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F66A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_F68A():
        OP_9B(0x0, 0xFE, 0x0, 0x1FA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F68A)
    Sleep(3500)

    def lambda_F6A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F6A2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_62_F665 end

    def Function_63_F6B7(): pass

    label("Function_63_F6B7")

    OP_95(0xFE, 42770, -2500, -2020, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)

    def lambda_F6D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F6D7)
    Sleep(1700)

    def lambda_F6EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F6EF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_63_F6B7 end

    def Function_64_F704(): pass

    label("Function_64_F704")

    Sound(479, 2, 0, 0)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x64)
    Sleep(8000)
    OP_25(0x1DF, 0x5A)
    Sleep(100)
    OP_25(0x1DF, 0x50)
    Sleep(100)
    OP_25(0x1DF, 0x46)
    Sleep(100)
    OP_25(0x1DF, 0x3C)
    Sleep(100)
    OP_25(0x1DF, 0x32)
    Sleep(100)
    OP_25(0x1DF, 0x28)
    Sleep(100)
    OP_25(0x1DF, 0x1E)
    Sleep(100)
    OP_25(0x1DF, 0x14)
    Sleep(100)
    OP_25(0x1DF, 0xA)
    Sleep(100)
    OP_24(0x1DF)
    Return()

    # Function_64_F704 end

    def Function_65_F796(): pass

    label("Function_65_F796")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-13700, 3000, 22500, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -13700, 2000, 21800, 135)
    SetChrPos(0x102, -13700, 2000, 23100, 135)
    SetChrPos(0x103, -15100, 2000, 21800, 135)
    SetChrPos(0x104, -15100, 2000, 23100, 135)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3200083V#0013F#5PThat's...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_65_F796 end

    def Function_66_F8B2(): pass

    label("Function_66_F8B2")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-19100, 1500, -13300, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -18400, 0, -13300, 45)
    SetChrPos(0x102, -19700, 0, -13300, 45)
    SetChrPos(0x103, -19700, 0, -14600, 45)
    SetChrPos(0x104, -18400, 0, -14600, 45)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#3200083V#0013F#5PThat's...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 72)
    Return()

    # Function_66_F8B2 end

    def Function_67_F9CE(): pass

    label("Function_67_F9CE")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1930, 0, 14500, 4000, 0x0)
    OP_95(0xFE, 3230, 500, 17000, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_67_F9CE end

    def Function_68_FA12(): pass

    label("Function_68_FA12")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 4400, 70, 16149, 4000, 0x0)
    TurnDirection(0xFE, 0x37, 500)
    Return()

    # Function_68_FA12 end

    def Function_69_FA42(): pass

    label("Function_69_FA42")

    OP_95(0xFE, 250, 0, 14720, 4000, 0x0)
    OP_95(0xFE, 1230, 0, 14880, 4000, 0x0)
    OP_95(0xFE, 2230, 200, 16400, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_69_FA42 end

    def Function_70_FA86(): pass

    label("Function_70_FA86")

    OP_95(0xFE, 800, 0, 12080, 4000, 0x0)
    OP_95(0xFE, 3400, 0, 15350, 4000, 0x0)
    TurnDirection(0xFE, 0x38, 500)
    Return()

    # Function_70_FA86 end

    def Function_71_FAB6(): pass

    label("Function_71_FAB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FCD0")

    def lambda_FAC6():
        OP_9D(0xFE, 0xF14, 0x0, 0x2F58, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_FAC6)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrSubChip(0x3A, 0x0)

    def lambda_FAF7():
        OP_9D(0xFE, 0x17DE, 0x0, 0x2D64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_FAF7)
    OP_A0(0x3A, 2000, 0x0, 0x5)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrChipByIndex(0x3F, 0x2C)
    SetChrSubChip(0x3F, 0x0)

    def lambda_FB2B():
        OP_9D(0xFE, 0x1234, 0x0, 0x2E72, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_FB2B)
    Sound(814, 0, 100, 0)
    Sound(541, 0, 100, 0)
    OP_A0(0x3F, 2000, 0x0, 0x3)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_FB98():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x32, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_FB98)
    OP_A0(0x3F, 2000, 0x4, 0x5)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_FBC4():
        OP_A0(0x3A, 4000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_FBC4)

    def lambda_FBD1():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_FBD1)
    OP_9D(0x3A, 0xC8A, 0x0, 0x2F58, 0x32, 0x7D0)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_FC36():

        label("loc_FC36")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_FC36")

    QueueWorkItem2(0x3A, 2, lambda_FC36)

    def lambda_FC54():

        label("loc_FC54")

        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        Yield()
        Jump("loc_FC54")

    QueueWorkItem2(0x3F, 2, lambda_FC54)
    Sleep(1500)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_FC8D():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_FC8D)

    def lambda_FCAA():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_FCAA)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    Jump("Function_71_FAB6")

    label("loc_FCD0")

    Return()

    # Function_71_FAB6 end

    def Function_72_FCD1(): pass

    label("Function_72_FCD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    LoadChrToIndex("chr/ch02152.itc", 0x21)
    LoadChrToIndex("chr/ch02151.itc", 0x22)
    LoadChrToIndex("chr/ch30800.itc", 0x23)
    LoadChrToIndex("chr/ch31700.itc", 0x24)
    LoadChrToIndex("chr/ch30900.itc", 0x25)
    LoadChrToIndex("chr/ch31800.itc", 0x26)
    LoadChrToIndex("chr/ch00400.itc", 0x27)
    LoadChrToIndex("chr/ch02100.itc", 0x28)
    LoadChrToIndex("chr/ch06700.itc", 0x29)
    LoadChrToIndex("chr/ch30850.itc", 0x2A)
    LoadChrToIndex("chr/ch30950.itc", 0x2B)
    LoadChrToIndex("chr/ch30852.itc", 0x2C)
    LoadChrToIndex("chr/ch30952.itc", 0x2D)
    LoadChrToIndex("apl/ch50307.itc", 0x2E)
    LoadChrToIndex("apl/ch50309.itc", 0x2F)
    LoadChrToIndex("apl/ch50390.itc", 0x30)
    LoadChrToIndex("chr/ch00601.itc", 0x31)
    LoadChrToIndex("chr/ch00701.itc", 0x32)
    LoadEffect(0x0, "event\\eva01_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")
    LoadEffect(0x2, "battle\\cr313100.eff")
    OP_68(3210, 1480, 11840, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x38, 0x27)
    SetChrSubChip(0x38, 0x0)
    OP_90(0x38, 3200, 600, 17150, 180)
    SetChrFlags(0x38, 0x8000)
    ClearChrFlags(0x38, 0x4)
    ClearChrFlags(0x38, 0x80)
    ClearChrBattleFlags(0x38, 0x8000)
    OP_4B(0x2E, 0xFF)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    OP_90(0x2E, 5900, 800, 17600, 180)
    SetChrFlags(0x2E, 0x8000)
    ClearChrFlags(0x2E, 0x4)
    SetChrFlags(0x2E, 0x40)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrChipByIndex(0x39, 0x29)
    SetChrSubChip(0x39, 0x0)
    OP_90(0x39, 2100, 900, 17800, 180)
    SetChrFlags(0x39, 0x8000)
    ClearChrFlags(0x39, 0x80)
    ClearChrBattleFlags(0x39, 0x8000)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)
    SetChrPos(0x3A, 2000, 0, 12000, 90)
    SetChrFlags(0x3A, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    ClearChrBattleFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3B, 0x26)
    SetChrSubChip(0x3B, 0x0)
    SetChrPos(0x3B, 0, 0, 13500, 135)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x3B, 0x80)
    ClearChrBattleFlags(0x3B, 0x8000)
    SetChrChipByIndex(0x3C, 0x25)
    SetChrSubChip(0x3C, 0x0)
    SetChrPos(0x3C, -800, 0, 10600, 90)
    SetChrFlags(0x3C, 0x8000)
    ClearChrFlags(0x3C, 0x80)
    ClearChrBattleFlags(0x3C, 0x8000)
    SetChrChipByIndex(0x3D, 0x25)
    SetChrSubChip(0x3D, 0x0)
    SetChrPos(0x3D, 500, 0, 9290, 45)
    SetChrFlags(0x3D, 0x8000)
    ClearChrFlags(0x3D, 0x80)
    ClearChrBattleFlags(0x3D, 0x8000)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrPos(0x3F, 5000, 0, 12000, 270)
    SetChrFlags(0x3F, 0x8000)
    ClearChrFlags(0x3F, 0x80)
    ClearChrBattleFlags(0x3F, 0x8000)
    SetChrChipByIndex(0x40, 0x24)
    SetChrSubChip(0x40, 0x0)
    SetChrPos(0x40, 8400, 0, 13500, 250)
    SetChrFlags(0x40, 0x8000)
    ClearChrFlags(0x40, 0x80)
    ClearChrBattleFlags(0x40, 0x8000)
    SetChrChipByIndex(0x41, 0x23)
    SetChrSubChip(0x41, 0x0)
    SetChrPos(0x41, 9100, 0, 11600, 270)
    SetChrFlags(0x41, 0x8000)
    ClearChrFlags(0x41, 0x80)
    ClearChrBattleFlags(0x41, 0x8000)
    SetChrChipByIndex(0x42, 0x24)
    SetChrSubChip(0x42, 0x0)
    SetChrPos(0x42, 7900, 0, 9700, 315)
    SetChrFlags(0x42, 0x8000)
    ClearChrFlags(0x42, 0x80)
    ClearChrBattleFlags(0x42, 0x8000)
    SetChrChipByIndex(0x43, 0x23)
    SetChrSubChip(0x43, 0x0)
    SetChrPos(0x43, 5100, 0, 9000, 0)
    SetChrFlags(0x43, 0x8000)
    ClearChrFlags(0x43, 0x80)
    ClearChrBattleFlags(0x43, 0x8000)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x0)
    SetChrPos(0x36, -3800, 2000, 20900, 90)
    ClearChrFlags(0x36, 0x4)
    SetChrFlags(0x36, 0x8000)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x0)
    SetChrPos(0x37, -4900, 2000, 22200, 90)
    ClearChrFlags(0x37, 0x4)
    SetChrFlags(0x37, 0x8000)
    OP_52(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Sleep(10)
    PlayBGM("ed7517", 0)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x3F,
        "#3200084V#11PGimme everything you got, ya blue bastard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        "#3200085VI don't need you to tell me that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        "#3200086VLet's do this!\x02",
    )

    CloseMessageWindow()
    OP_52(0x3A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x3B, 2, 0, 71)
    Sleep(3500)
    Fade(500)
    OP_68(-3180, 1310, 11540, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, -9000, 0, 11410, 90)
    SetChrPos(0x104, -9300, 0, 10010, 90)
    SetChrPos(0x102, -10000, 0, 11410, 90)
    SetChrPos(0x103, -10300, 0, 10010, 90)
    OP_0D()

    ChrTalk(
        0x102,
        (
            "#3200087V#0105FAren't those the delinquents...?\x01",
            "What exactly are they doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3200088V#0200FI am not sure, but I do not sense any\x01",
            "danger coming from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200089V#0305FYeah, doesn't seem like their regular\x01",
            "ol' throwdowns to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200090V#0006FWe should still ask them what's going on.\x02\x03",
            "#3200091V#0001FFortunately for us, Wazy and Wald are here,\x01",
            "so I don't think things will get out of hand...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 20, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3200092VHey! What the heck do you guys think\x01",
            "you're doing?!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(5160, 940, 14220, 0)
    MoveCamera(62, 13, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    OP_68(4760, 1660, 17450, 2000)
    MoveCamera(50, 13, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(23500, 2000)
    EndChrThread(0x3B, 0xFF)
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3A, 0x2D)
    SetChrChipByIndex(0x3F, 0x2C)

    def lambda_1046E():
        OP_A0(0x3A, 5000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_1046E)

    def lambda_1047B():
        OP_A0(0x3F, 2000, 0x0, 0x2)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_1047B)
    SetChrPos(0x3F, 3790, 0, 11880, 270)
    SetChrPos(0x3A, 2340, 0, 12120, 90)
    SetChrSubChip(0x3A, 0x5)
    PlayEffect(0x0, 0xFF, 0x3F, 0xC0, 0, 1000, 800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(894, 0, 100, 0)

    def lambda_104EB():

        label("loc_104EB")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_104EB")

    QueueWorkItem2(0x3A, 2, lambda_104EB)

    def lambda_10509():

        label("loc_10509")

        OP_A6(0xFE, 0x0, 0x19, 0x96, 0x5DC)
        Yield()
        Jump("loc_10509")

    QueueWorkItem2(0x3F, 2, lambda_10509)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    ClearChrFlags(0x37, 0x80)
    ClearChrBattleFlags(0x37, 0x8000)

    def lambda_1053B():
        OP_95(0xFE, 4200, 2000, 20900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_1053B)
    Sleep(50)

    def lambda_10558():
        OP_95(0xFE, 3400, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_10558)
    WaitChrThread(0x36, 1)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)

    def lambda_1057E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x36, 2, lambda_1057E)
    WaitChrThread(0x37, 1)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)

    def lambda_10597():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x37, 2, lambda_10597)

    def lambda_105A4():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_105A4)
    Sleep(50)

    def lambda_105B4():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_105B4)
    Sleep(50)
    TurnDirection(0x39, 0x36, 500)
    OP_0D()

    ChrTalk(
        0x2E,
        "#3200093V#1605F#12PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "#3200094V#0405F#12POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200095V#0806FWe got a call about some hooligans causing\x01",
            "problems, so we came here as fast as we could...\x02\x03",
            "#3200096V#0801FAren't you those Testaments and Saber Viper\x01",
            "dudes from the Downtown District?\x02\x03",
            "#3200097VYou better cut it out right now!\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x3A, 0xFF)
    EndChrThread(0x3F, 0xFF)
    SetChrChipByIndex(0x3F, 0x2A)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x2B)
    SetChrSubChip(0x3A, 0x0)

    def lambda_10716():
        OP_9D(0xFE, 0x7D0, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_10716)

    def lambda_10733():
        OP_9D(0xFE, 0x1388, 0x0, 0x2EE0, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_10733)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x3A, 0)
    WaitChrThread(0x3F, 0)

    def lambda_1075E():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3F, 0, lambda_1075E)

    def lambda_1076B():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x40, 0, lambda_1076B)

    def lambda_10778():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x41, 0, lambda_10778)

    def lambda_10785():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_10785)

    def lambda_10792():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x43, 0, lambda_10792)

    def lambda_1079F():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3A, 0, lambda_1079F)

    def lambda_107AC():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3B, 0, lambda_107AC)

    def lambda_107B9():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3C, 0, lambda_107B9)

    def lambda_107C6():
        TurnDirection(0xFE, 0x36, 500)
        ExitThread()

    QueueWorkItem(0x3D, 0, lambda_107C6)

    ChrTalk(
        0x2E,
        "#3200098V#1601F#12PThe hell's up with this chick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#3200099V#0903FPardon us. We're with the Bracer Guild.\x02\x03",
            "#3200100V#0901FWe received a message claiming that a fight\x01",
            "had broken out, so we're here to intervene.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x3F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x41, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x40, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x3C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_68(4440, 2550, 18850, 2000)
    MoveCamera(37, 13, 0, 2000)
    OP_6E(480, 2000)
    SetCameraDistance(23630, 2000)
    Sleep(2000)

    ChrTalk(
        0x2E,
        "#3200101V#1605F#12PThe guild?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        (
            "#3200102V#0404F#6P#NYou're Joshua and Estelle Bright...\x02\x03",
            "#3200103V#0400FHeh. I've seen your faces in magazines.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x36,
        (
            "#3200104V#0806F#5PYeah, yeah. The pleasure's all mine.\x02\x03",
            "#3200105V#0800FYou two are the leaders of these goons, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        (
            "#3200106V#0404F#6P#NEssentially.\x02\x03",
            "#3200107V#0400FI'm Wazy, leader of the Testaments, and this\x01",
            "here is Wald, leader of the Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x37,
        (
            "#3200108V#0903F#5PThat matches the contents of the report.\x02\x03",
            "#3200109V#0900FIt doesn't look like you're fighting,\x01",
            "so what exactly are you guys up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        (
            "#3200110V#0404F#6P#NDon't mind us. We're just having some fun.\x02\x03",
            "#3200111VSeeing as how it's the Anniversary Festival,\x01",
            "we thought we'd try something a little different\x01",
            "from the usual routine.\x02\x03",
            "#3200112V#0402FAnyway, we're partaking in a series of one-on-one\x01",
            "battles to determine an overall victor.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x36,
        (
            "#3200113V#0805F#5PA series of battles?\x01",
            "What are you guys talking about?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x39, 0x36, 500)

    ChrTalk(
        0x39,
        (
            "#3200114V#6PBoth teams will nominate five members to engage\x01",
            "in one-on-one battles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x39,
        "#3200115V#6PThe last pairing to compete will be Wazy and Wald.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x39,
        (
            "#3200116V#6PWe have determined the losing side will have to\x01",
            "cover the victor's meal expenses for the remainder\x01",
            "of the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200117V#0805F#5POh, that makes perfect sense! You guys are just\x01",
            "having a friendly exhibition match.\x02\x03",
            "#3200118V#0809FThat sounds fun, so I guess I can let it slide--\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x36,
        (
            "#3200119V#0806F#5PAs if!\x02\x03",
            "#3200120V#0801FI don't care if it's a friendly match.\x01",
            "That doesn't make it okay to do it\x01",
            "out here!\x02\x03",
            "#3200121VMove your butts somewhere else!\x01",
            "You're annoying everybody else\x01",
            "trying to enjoy the festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#3200122V#1603F#12PHah! Fat chance!\x02\x03",
            "#3200123V#1601FYou know... I don't give a damn if you're\x01",
            "bracers or whatever, but you guys keep\x01",
            "acting like you're hot shit!\x02\x03",
            "#3200124VDon't get so damn cocky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200125V#0803F#5PNow you listen here, bub... You're the\x01",
            "idiot who's too cocky!\x02\x03",
            "#3200126V#0801FAll I did was try to knock some common\x01",
            "sense into that thick skull of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#3200127V#1600F#12PYou bitch...\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x0, 0x1F4)
    OP_68(5860, 2550, 20980, 2000)

    def lambda_111BE():

        label("loc_111BE")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_111BE")

    QueueWorkItem2(0x36, 2, lambda_111BE)

    def lambda_111D0():

        label("loc_111D0")

        TurnDirection(0xFE, 0x2E, 500)
        Yield()
        Jump("loc_111D0")

    QueueWorkItem2(0x37, 2, lambda_111D0)
    OP_95(0x2E, 6200, 2000, 20800, 2000, 0x0)
    TurnDirection(0x2E, 0x36, 500)
    EndChrThread(0x36, 0x2)
    EndChrThread(0x37, 0x2)

    ChrTalk(
        0x2E,
        (
            "#3200128V#1604F#11PSounds like you're asking to get your\x01",
            "ass kicked.\x02\x03",
            "#3200129V#1602FI don't mind taking you and yer little\x01",
            "black-haired friend on, if that's what'cha\x01",
            "want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200130V#0806F#6PW-Well...\x02\x03",
            "#3200131V#0808FHow should we handle this, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#3200132V#0903F#5PEverybody's watching us now.\x02\x03",
            "#3200133V#0900FDon't make any rash decisions.\x01",
            "It'd reflect poorly on the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#3200134V#0802F#6PYeah, I figured as much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        (
            "#3200135V#1607F#11PWhat the hell are you guys whisperin'\x01",
            "about over there?!\x02\x03",
            "#3200136VAren't you ready to piss yourselves facin'\x01",
            "Wald Wales, the Demon Smasher?!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6010, 2550, 21180, 800)
    SetCameraDistance(23800, 800)
    OP_95(0x38, 3500, 1100, 18200, 1800, 0x0)
    TurnDirection(0x38, 0x2E, 500)
    OP_6F(0x1)

    ChrTalk(
        0x38,
        (
            "#3200137V#0406F#6P#NSettle down, Wald.\x02\x03",
            "#3200138V#0400FIf that girl knows her martial arts,\x01",
            "she might even be able to take you\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x2E, 0x38, 500)

    ChrTalk(
        0x2E,
        "#3200139V#1605F#11PWhat'd you say?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x36, 0x38, 500)
    Sleep(150)

    ChrTalk(
        0x36,
        "#3200140V#0800F#5PYou could tell?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x38, 0x36, 500)
    Sleep(150)

    ChrTalk(
        0x38,
        (
            "#3200141V#0404F#12P#NEh. It was just a hunch.\x02\x03",
            "#3200142V#0402FLet's not ignore your friend over there, either.\x01",
            "He's actually far stronger than you, isn't he?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x38, 500)
    Sleep(150)

    ChrTalk(
        0x37,
        (
            "#3200143V#0902F#5PHaha... I've still got a lot of training ahead\x01",
            "of me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200144V#0806F#5PThat was pretty rude of you to say!\x01",
            "Sure, Joshua IS stronger than me...\x02\x03",
            "#3200145V#0801F...but it still pisses me off to hear you\x01",
            "say it straight to my face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#3200146V#0904F#5PNow, now. You know that being a bracer comes\x01",
            "down to more than just brute strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    TurnDirection(0x2E, 0x36, 500)
    Sleep(1000)
    Sound(1807, 255, 100, 0)
    Sleep(500)

    ChrTalk(
        0x2E,
        (
            "#3200147V#1602F#11PHaha... You're tellin' me this girlie\x01",
            "could beat me in a fight?\x02\x03",
            "#3200148V#1607FHA! You think you're so tough?\x01",
            "Prove it!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(5680, 2550, 20990, 1000)
    SetCameraDistance(21320, 1000)

    def lambda_118D1():

        label("loc_118D1")

        TurnDirection(0xFE, 0x2E, 600)
        Yield()
        Jump("loc_118D1")

    QueueWorkItem2(0x36, 0, lambda_118D1)
    OP_99(0x2E, 0x36, 0x3E8, 0xBB8, 0x0)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x2E)
    SetChrSubChip(0x2E, 0x0)
    SetChrFlags(0x2E, 0x20)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x37,
        "#3200149V#0901F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#3200150V#0804F#6PIt's okay. This'll be a piece of cake!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(4190, 2920, 19620, 0)
    MoveCamera(359, 8, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(25000, 1000)
    SetChrChipByIndex(0x3F, 0x23)
    SetChrSubChip(0x3F, 0x0)
    SetChrChipByIndex(0x3A, 0x25)
    SetChrSubChip(0x3A, 0x0)
    OP_93(0x36, 0x5A, 0x0)

    def lambda_119CD():

        label("loc_119CD")

        TurnDirection(0xFE, 0x2E, 300)
        Yield()
        Jump("loc_119CD")

    QueueWorkItem2(0x37, 0, lambda_119CD)
    SetChrChipByIndex(0x2E, 0x30)
    SetChrSubChip(0x2E, 0x0)
    SetChrPos(0x2E, 5300, 2300, 20900, 270)
    Sound(804, 0, 100, 0)
    OP_D3(0x2E, 0x0, 0x0, 0x15F90, 0x0)
    Sound(1648, 255, 100, 0)
    Sound(534, 0, 100, 0)
    ClearChrFlags(0x2E, 0x1)
    ClearChrFlags(0x2E, 0x100)

    def lambda_11A27():
        OP_9D(0xFE, 0x9C4, 0x7D0, 0x526C, 0x7D0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_11A27)
    OP_D3(0x2E, 0x0, 0x0, 0x57E40, 0x384)
    SetChrChipByIndex(0x2E, 0x2F)
    SetChrSubChip(0x2E, 0x0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sound(819, 0, 100, 0)
    Sound(834, 0, 100, 0)
    OP_9D(0x2E, 0x7D0, 0x7D0, 0x5334, 0x190, 0x7D0)
    PlayEffect(0x1, 0xFF, 0x2E, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x64, 0x5DC, 0x96)
    Sound(819, 0, 100, 0)
    CancelBlur(0)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x2E, 0x1)
    Sleep(500)
    EndChrThread(0x37, 0x0)

    ChrTalk(
        0x2E,
        "#3200152V#1605F#11PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "#3200153V#0406F#6PDon't say I didn't warn you.\x02",
    )

    CloseMessageWindow()
    OP_68(4320, 2270, 18840, 3000)
    MoveCamera(359, 7, 0, 3000)
    OP_6E(380, 3000)
    SetCameraDistance(25000, 3000)
    OP_63(0x3F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x40, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x41, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x3F)
    OP_64(0x40)
    OP_64(0x41)
    OP_64(0x3A)
    OP_64(0x3B)
    OP_64(0x3C)

    ChrTalk(
        0x40,
        "#3200154V#11PSh-She took down Wald?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3F,
        "#3200155V#5PWhat the hell's up with that chick?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3B,
        "#3200156V#5PThat was amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x3A,
        "#3200157V#5PAre all bracers this strong?!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2720, 2400, 21470, 0)
    MoveCamera(336, 12, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(25000, 0)
    OP_63(0x2E, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2E)

    ChrTalk(
        0x36,
        "#3200158V#0805F#12PHey there, buddy. You all right?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x2E, 0x2)

    def lambda_11D73():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_11D73)
    WaitChrThread(0x2E, 2)
    Sound(1808, 255, 100, 0)

    ChrTalk(
        0x2E,
        "#3200159V#1604F#11PHahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_11DBB():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_11DBB)
    SetChrSubChip(0x2E, 0x1)
    Sound(1809, 255, 100, 0)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x2E,
        "#3200160V#1609F#4S#11P#NHAHAHAHAHAHA!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2450, 2500, 22450, 800)
    SetCameraDistance(26180, 800)
    Sound(804, 0, 100, 0)
    Sound(534, 0, 100, 0)
    SetChrFlags(0x2E, 0x100)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)

    def lambda_11E54():
        TurnDirection(0xFE, 0x36, 800)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_11E54)
    OP_9C(0x2E, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrFlags(0x2E, 0x1)
    Sound(808, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x2E,
        (
            "#3200161V#1604F#5PMy bad.\x01",
            "I wasn't takin' you seriously.\x02\x03",
            "#3200162V#1601FDon't you think yer takin' me a little\x01",
            "too lightly, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#3200163V#0801F#12P...!\x02",
    )

    CloseMessageWindow()
    OP_68(3100, 2500, 22470, 800)
    SetCameraDistance(24870, 800)
    BeginChrThread(0x36, 3, 0, 73)
    SetChrChipByIndex(0x2E, 0x21)
    SetChrSubChip(0x2E, 0x0)
    Sleep(90)
    SetChrSubChip(0x2E, 0x1)
    Sleep(90)
    SetChrSubChip(0x2E, 0x2)
    Sleep(90)

    def lambda_11F67():

        label("loc_11F67")

        TurnDirection(0xFE, 0x36, 100)
        Yield()
        Jump("loc_11F67")

    QueueWorkItem2(0x37, 2, lambda_11F67)
    SetChrFlags(0x2E, 0x20)
    Sound(1789, 255, 100, 0)
    Sound(532, 0, 100, 0)

    def lambda_11F8A():
        OP_96(0xFE, 0xAF0, 0x7D0, 0x529E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11F8A)
    SetChrSubChip(0x2E, 0x3)
    Sleep(70)
    SetChrSubChip(0x2E, 0x4)
    WaitChrThread(0x2E, 1)
    SetChrSubChip(0x2E, 0x5)
    ClearChrFlags(0x2E, 0x20)
    PlayEffect(0x2, 0xFF, 0x2E, 0x140, 0, 100, 1300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    Sound(895, 0, 100, 0)
    Sound(834, 0, 100, 0)
    Sleep(800)
    WaitChrThread(0x36, 3)

    ChrTalk(
        0x36,
        "#3200165V#0807F#12PWh-Whoa there!\x02",
    )

    CloseMessageWindow()
    Sound(1780, 255, 100, 0)

    ChrTalk(
        0x37,
        "#3200166V#0901F#5PGet back, Estelle!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x37, 0x2)
    SetChrChipByIndex(0x37, 0x32)
    SetChrSubChip(0x37, 0x3)

    def lambda_1207A():
        OP_9D(0xFE, 0x157C, 0x7D0, 0x5078, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_1207A)
    Sound(814, 0, 100, 0)

    def lambda_1209D():

        label("loc_1209D")

        TurnDirection(0xFE, 0x2E, 1000)
        Yield()
        Jump("loc_1209D")

    QueueWorkItem2(0x37, 2, lambda_1209D)
    WaitChrThread(0x37, 0)
    PlayEffect(0x1, 0xFF, 0x37, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)
    Sleep(100)
    OP_95(0x38, 3150, 1600, 19150, 2000, 0x0)
    TurnDirection(0x38, 0x37, 500)
    EndChrThread(0x37, 0x2)

    ChrTalk(
        0x38,
        (
            "#3200167V#0404F#6PSettle down, you guys.\x02\x03",
            "#3200168V#0400FAren't you getting a little too carried away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#3200169V#0903F#11PYeah, I agree.\x02\x03",
            "#3200170V#0901FI think it's probably meaningless to apologize\x01",
            "at this point, though.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x6)
    Sleep(90)
    SetChrSubChip(0x2E, 0x7)
    Sleep(90)
    Fade(250)
    SetChrChipByIndex(0x2E, 0x20)
    SetChrSubChip(0x2E, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x2E,
        (
            "#3200171V#1602F#5PHaha... I got you all pissed off, didn't I?\x02\x03",
            "#3200172V#1604FI get it. You're a strong guy.\x02\x03",
            "#3200173V#1601FI love beatin' the piss out of guys like you\x01",
            "more than anythin' else!\x02\x03",
            "#3200174VCome on! Pull out that weapon of yours, punk!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        "#3200175V#0901F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        (
            "#3200176V#0801F#12PH-Hey! Cool your jets, Joshua!\x02\x03",
            "#3200177VI'm totally fine. You don't need to\x01",
            "get all serious!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1086, 255, 100, 0)

    NpcTalk(
        0x101,
        "Lloyd's Voice",
        "#3200178VHold it right there!\x02",
    )

    CloseMessageWindow()
    OP_63(0x37, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x38, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x36, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(20, 1750, 13750, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -2450, 0, 13210, 90)
    SetChrPos(0x104, -2720, 0, 11440, 90)
    SetChrPos(0x102, -4470, 0, 12520, 90)
    SetChrPos(0x103, -4720, 0, 10900, 90)
    BeginChrThread(0x101, 0, 0, 67)
    BeginChrThread(0x104, 0, 0, 68)
    BeginChrThread(0x102, 0, 0, 69)
    BeginChrThread(0x103, 0, 0, 70)

    def lambda_124E6():

        label("loc_124E6")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_124E6")

    QueueWorkItem2(0x36, 0, lambda_124E6)

    def lambda_124F8():

        label("loc_124F8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_124F8")

    QueueWorkItem2(0x37, 0, lambda_124F8)

    def lambda_1250A():

        label("loc_1250A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1250A")

    QueueWorkItem2(0x38, 0, lambda_1250A)

    def lambda_1251C():

        label("loc_1251C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1251C")

    QueueWorkItem2(0x2E, 0, lambda_1251C)

    def lambda_1252E():

        label("loc_1252E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1252E")

    QueueWorkItem2(0x39, 0, lambda_1252E)

    def lambda_12540():

        label("loc_12540")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12540")

    QueueWorkItem2(0x3F, 0, lambda_12540)

    def lambda_12552():

        label("loc_12552")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12552")

    QueueWorkItem2(0x40, 0, lambda_12552)

    def lambda_12564():

        label("loc_12564")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12564")

    QueueWorkItem2(0x41, 0, lambda_12564)

    def lambda_12576():

        label("loc_12576")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12576")

    QueueWorkItem2(0x42, 0, lambda_12576)

    def lambda_12588():

        label("loc_12588")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12588")

    QueueWorkItem2(0x43, 0, lambda_12588)

    def lambda_1259A():

        label("loc_1259A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1259A")

    QueueWorkItem2(0x3A, 0, lambda_1259A)

    def lambda_125AC():

        label("loc_125AC")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_125AC")

    QueueWorkItem2(0x3B, 0, lambda_125AC)

    def lambda_125BE():

        label("loc_125BE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_125BE")

    QueueWorkItem2(0x3C, 0, lambda_125BE)
    OP_68(4220, 2200, 18860, 4000)
    MoveCamera(328, 17, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(26000, 4000)
    WaitChrThread(0x101, 0)
    EndChrThread(0x36, 0x0)
    EndChrThread(0x37, 0x0)
    EndChrThread(0x38, 0x0)
    EndChrThread(0x2E, 0x0)
    EndChrThread(0x39, 0x0)

    ChrTalk(
        0x38,
        "#3200179V#0405F#11PWell, if it isn't the SSS.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#3200180V#0805F#11POh, it's you guys. What are you doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200181V#0003F#6PI've heard about the situation already.\x02\x03",
            "#3200182V#0001FPlease, I urge both of you to calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#3200183V#1601F#5P#NHah! As if I could!\x02\x03",
            "#3200184V#1604FThose bracers are pretty damn good!\x02\x03",
            "#3200185V#1607FI'd heard rumors, but who woulda thought\x01",
            "they'd get me all riled up like this?!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#3200186V#0006F#6PThis is precisely why I'm telling you to\x01",
            "calm down, Wald...\x02\x03",
            "#3200187V#0001FFirst off, you're in a public space.\x02\x03",
            "#3200188VIf you're dead set on conducting your matches,\x01",
            "couldn't you at least do everybody a favor and\x01",
            "relocate to somewhere more quiet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        (
            "#3200189V#0406F#11PNo deal.\x02\x03",
            "#3200190V#0402FIsn't it a bit cruel to cut us off right\x01",
            "as things were starting to get exciting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200191V#0011F#6PWazy?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        (
            "#3200192V#0402F#11PWald's totally lost his cool, and those\x01",
            "bracers are just trying to do their job.\x02\x03",
            "#3200193V#0409FShouldn't they stick to their guns and\x01",
            "fight each other?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2E, 0x36, 500)
    Sleep(300)

    ChrTalk(
        0x2E,
        "#3200194V#1602F#6PHaha! Damn straight!\x02",
    )

    CloseMessageWindow()

    def lambda_12A62():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_12A62)
    Sleep(50)

    def lambda_12A72():
        TurnDirection(0xFE, 0x2E, 400)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_12A72)
    Sleep(300)

    ChrTalk(
        0x36,
        (
            "#3200195V#0803F#12PIt's a little embarrassing, but I'm actually\x01",
            "kinda peeved, too.\x02\x03",
            "#3200196V#0801FIf we both feel the same way, then why\x01",
            "don't we settle it. Right here, right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#3200197V#1607F#6PBring it on, girlie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200198V#0006F#6PEnough already!\x02\x03",
            "#3200199V#0013FJoshua! Are you going to continue standing there\x01",
            "in silence, or are you going to help me out?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x37,
        (
            "#3200200V#0908F#12PSorry, Lloyd. I can't let this one slide\x01",
            "so easily, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#3200201V#0011F#6PReally?!\x02",
    )

    CloseMessageWindow()

    def lambda_12C72():

        label("loc_12C72")

        TurnDirection(0xFE, 0x37, 400)
        Yield()
        Jump("loc_12C72")

    QueueWorkItem2(0x38, 0, lambda_12C72)
    Sleep(300)

    ChrTalk(
        0x38,
        (
            "#3200202V#0404F#6PI guess I'll be Wald's backup, then.\x02\x03",
            "#3200203V#0402FYou may be strong, but I'm willing to bet you'd run\x01",
            "into trouble trying to take those two on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#3200204V#1603F#5P#NWhatever. Suit yourself!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#3200205V#0007F#6PWhy is everybody in this city\x01",
            "so freaking stubborn?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#3200206V#0106F#5P(Th-This is spiraling out of control very quickly.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#3200207V#0211F#5P(There is no doubt their dispute will cause a\x01",
            "large disturbance for the citizens.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#3200208V#0303F#6P#NY'know...\x02\x03",
            "#3200209V#0300FIf you're itchin' for a fight that badly,\x01",
            "then why not settle it some other way?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x36, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x37, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x38, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4180, 1700, 17780, 1500)

    def lambda_12F8C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12F8C)
    Sleep(50)

    def lambda_12F9C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_12F9C)

    def lambda_12FA9():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x37, 0, lambda_12FA9)
    Sleep(50)

    def lambda_12FB9():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12FB9)

    def lambda_12FC6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12FC6)
    Sleep(50)

    def lambda_12FD6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x38, 0, lambda_12FD6)

    def lambda_12FE3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x2E, 0, lambda_12FE3)
    Sleep(50)

    def lambda_12FF3():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_12FF3)
    OP_6F(0x1)

    ChrTalk(
        0x101,
        "#3200210V#0005F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x38,
        "#3200211V#0405F#5P#NHmm?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#3200212V#0306F#6PIt'd be pretty crappy to harbor a grudge\x01",
            "durin' the festival, no?\x02\x03",
            "#3200213V#0302FWhy not try settlin' this in a more friendly\x01",
            "fashion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#3200214V#1601F#5P#NA friendly fashion? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x36,
        "#3200215V#0805F#11P#NUmm... I'm not sure I follow you, Randy.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x104,
        "#3200216V#0304F#6PBoy, do I have an idea for you...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(29500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_72_FCD1 end

    def Function_73_131B6(): pass

    label("Function_73_131B6")

    Sleep(350)
    SetChrChip(0x0, 0x36, 0x1E, 0x12C)
    SetChrChipByIndex(0x36, 0x31)
    SetChrSubChip(0x36, 0x3)

    def lambda_131CE():
        OP_9D(0xFE, 0x189C, 0x7D0, 0x5078, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_131CE)
    Sound(814, 0, 100, 0)
    WaitChrThread(0x36, 0)
    PlayEffect(0x1, 0xFF, 0x36, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x36, 0x1E)
    SetChrSubChip(0x36, 0x0)
    Sleep(150)
    SetChrChip(0x1, 0x36, 0x0, 0x0)
    Return()

    # Function_73_131B6 end

    def Function_74_1323B(): pass

    label("Function_74_1323B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -11990, -3000, -9930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 2340, -3000, -8610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 19600, -3000, -4370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(885)
    LoadChrToIndex("chr/ch20000.itc", 0x28)
    LoadChrToIndex("chr/ch20100.itc", 0x29)
    LoadChrToIndex("chr/ch20200.itc", 0x2A)
    LoadChrToIndex("chr/ch20300.itc", 0x2B)
    LoadChrToIndex("chr/ch20800.itc", 0x2C)
    LoadChrToIndex("chr/ch20900.itc", 0x2D)
    LoadChrToIndex("chr/ch21200.itc", 0x2E)
    LoadChrToIndex("chr/ch21300.itc", 0x2F)
    LoadChrToIndex("chr/ch21800.itc", 0x30)
    LoadChrToIndex("chr/ch21900.itc", 0x31)
    SetChrChipByIndex(0x44, 0x28)
    SetChrChipByIndex(0x45, 0x29)
    SetChrChipByIndex(0x46, 0x2A)
    SetChrChipByIndex(0x47, 0x2B)
    SetChrChipByIndex(0x48, 0x2C)
    SetChrChipByIndex(0x49, 0x2D)
    SetChrChipByIndex(0x4A, 0x2E)
    SetChrChipByIndex(0x4B, 0x2F)
    SetChrChipByIndex(0x4C, 0x30)
    SetChrChipByIndex(0x4D, 0x31)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0x46, 0x80)
    ClearChrBattleFlags(0x46, 0x8000)
    ClearChrFlags(0x47, 0x80)
    ClearChrBattleFlags(0x47, 0x8000)
    ClearChrFlags(0x48, 0x80)
    ClearChrBattleFlags(0x48, 0x8000)
    ClearChrFlags(0x49, 0x80)
    ClearChrBattleFlags(0x49, 0x8000)
    ClearChrFlags(0x4A, 0x80)
    ClearChrBattleFlags(0x4A, 0x8000)
    ClearChrFlags(0x4B, 0x80)
    ClearChrBattleFlags(0x4B, 0x8000)
    ClearChrFlags(0x4C, 0x80)
    ClearChrBattleFlags(0x4C, 0x8000)
    ClearChrFlags(0x4D, 0x80)
    ClearChrBattleFlags(0x4D, 0x8000)
    SetChrFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x8000)
    SetChrFlags(0x46, 0x8000)
    SetChrFlags(0x47, 0x8000)
    SetChrFlags(0x48, 0x8000)
    SetChrFlags(0x49, 0x8000)
    SetChrFlags(0x4A, 0x8000)
    SetChrFlags(0x4B, 0x8000)
    SetChrFlags(0x4C, 0x8000)
    SetChrFlags(0x4D, 0x8000)
    SetChrPos(0x44, 43420, -2500, 1510, 181)
    SetChrPos(0x45, 43370, -2500, -2450, 1)
    SetChrPos(0x46, 42230, -2500, 320, 91)
    SetChrPos(0x47, 41700, -2500, -920, 91)
    SetChrPos(0x48, 39850, -2500, 200, 91)
    SetChrPos(0x49, 39820, -2500, -930, 1)
    SetChrPos(0x4A, 37910, -2500, 70, 91)
    SetChrPos(0x4B, 35970, -2500, -690, 91)
    SetChrPos(0x4C, 34150, -2500, 300, 91)
    SetChrPos(0x4D, 32689, -2500, -390, 91)
    SetChrPos(0x0, 14720, -1000, -920, 135)
    SetChrPos(0x1, 14720, -1000, -920, 135)
    SetChrPos(0x2, 14720, -1000, -920, 135)
    SetChrPos(0x3, 14720, -1000, -920, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x1)
    OP_71(0x9, 0xF1, 0x12C, 0x0, 0x20)
    SetMapObjFrame(0x9, "wave00", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_68(8160, 2600, -2060, 0)
    MoveCamera(21, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_68(39180, 3000, -8560, 10000)
    MoveCamera(71, 11, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(26500, 10000)
    Sound(885, 2, 90, 0)
    FadeToBright(1000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c047C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_74_1323B end

    def Function_75_135D2(): pass

    label("Function_75_135D2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 315)
    SetChrPos(0x15, -16920, 0, -9360, 135)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#0000FExcuse us, but we're with the\x01",
            "Crossbell Police Department.\x02\x03",
            "We're here to respond to your support request.\x01",
            "We're looking for the Business Owners' Association's\x01",
            "tent. Is this the correct place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x1A, 0xC6, 0x1F4)
    OP_93(0x15, 0xC6, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A,
        "#11POh, you've arrived.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PI'm surprised... Who would have thought that\x01",
            "you'd be the ones to handle the task?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWell, word about the Special Support Section\x01",
            "has been spreading these days.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_END)), "loc_13AA6")

    ChrTalk(
        0x102,
        "#12P#0100FThank you for your cooperation, Mors.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x1A, 500)
    Sleep(300)

    ChrTalk(
        0x15,
        "#5PAre these your friends, Chairman Mors?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x15, 500)
    Sleep(300)

    ChrTalk(
        0x1A,
        (
            "#11PWell... Once upon a time, this young man sat\x01",
            "across from me on a train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FYeah, that was actually the day I started\x01",
            "working on the force.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1399B():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1399B)

    def lambda_139A8():
        OP_93(0xFE, 0xC6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_139A8)
    Sleep(300)

    ChrTalk(
        0x1A,
        (
            "#11PAh, yes. It was, wasn't it?\x01",
            "Anyway, I've interacted with these fine folks\x01",
            "a few times since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe have a bit of a difficult situation on our hands.\x01",
            "My apologies, members of the SSS.\x01",
            "Could you please lend me your strength?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13CCF")

    label("loc_13AA6")

    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        "#6P#0205FAre you acquainted with Lloyd?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#0000FYeah, we happened to sit across from each\x01",
            "other on the train to Crossbell the day I started\x01",
            "working with you guys.\x02\x03",
            "I had no idea that he was the chairman of the\x01",
            "Business Owners' Association at the time.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13BC7():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13BC7)

    def lambda_13BD4():
        OP_93(0xFE, 0xF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13BD4)
    Sleep(300)

    ChrTalk(
        0x1A,
        (
            "#11PJust as I was unaware that the young man\x01",
            "across from me was poised to become a\x01",
            "fine detective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe have a bit of a difficult situation on our hands.\x01",
            "My apologies, members of the SSS.\x01",
            "Could you please lend me your strength?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CCF")


    ChrTalk(
        0x101,
        (
            "#12P#0004FYou can count on us, sir.\x02\x03",
            "#0001FLet's see... I believe the request mentioned\x01",
            "something about a recent theft?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0301FYeah, wasn't there a bunch of 'em?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PY-Yes, it's as you say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PThere have been four different reports of\x01",
            "theft since yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PEvery last one of the stalls was robbed\x01",
            "for everything they had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PThe Business Owners' Association manages all\x01",
            "of the stalls being run during the festival,\x01",
            "so we hear every report that comes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PI've finished organizing the reports, and have\x01",
            "determined that only food stalls are being targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe don't have any clues to go off of, so the best\x01",
            "thing we can do is to warn the other stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0101FThat's unfortunate. The stall owners already have\x01",
            "enough to worry about during the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI would imagine that you are worried about the\x01",
            "damage becoming more widespread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PYes, and that's why I've called you all here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PIt is my duty to ensure that the thief is caught before\x01",
            "they can cause any more damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWith the way things are going, customers\x01",
            "who have come from far and wide to enjoy\x01",
            "the festival could be affected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PMay I count on you to apprehend the thief?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Accept]\x01",      # 0
            "[Refuse]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141F8")
    OP_29(0x20, 0x1, 0x1)
    Call(0, 76)
    Return()

    label("loc_141F8")


    ChrTalk(
        0x101,
        (
            "#12P#0006FI'm sorry, sir. I'd love to help, but our\x01",
            "schedule is packed at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PAh, really? There's not much I can do about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PPlease don't forget about me if you find yourself\x01",
            "with more time. I would like to resolve this before\x01",
            "the thief can inflict any more damage.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_135D2 end

    def Function_76_14387(): pass

    label("Function_76_14387")


    ChrTalk(
        0x101,
        (
            "#12P#0001FUnderstood. This is a serious predicament.\x01",
            "We'll begin investigating immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PThank goodness... I already feel a little relieved!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PI'm counting on all of you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0304FRest assured, my man. You're in good hands.\x02\x03",
            "#0301FHey, Lloyd. Any plans on how to tackle this?\x01",
            "We don't have any clues to work off of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0003FHmm... There's not enough information to go\x01",
            "off yet, so I don't think there's any point in\x01",
            "trying to analyze the situation.\x02\x03",
            "#0001FExcuse me. Do you mind telling us which stalls\x01",
            "were targeted? I'd like to speak with the owners.\x02\x03",
            "We may be able to collect information from them\x01",
            "before we proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PAh, I see. That makes sense to me.\x01",
            "I've recorded the names down here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PMay I read them to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FYes, that's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PFirst is Nardol's Burgers in Central Square,\x01",
            "followed by Chroma's Juice Stand in\x01",
            "the Administrative District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PNext, we have Palate Pizza in the Entertainment\x01",
            "District and Mithra's Gelato in the Harbor District.\x01",
            "Were you able to get all of that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0103F*scritch* *scratch* Okay, so four stalls in\x01",
            "total, and they're all in different districts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FYou failed to find a single clue despite there\x01",
            "being four victims?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FRegardless, let's see what we can dig up\x01",
            "from the owners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWill you be here on standby?\x01",
            "We'll return after we've made our rounds.\x02\x03",
            "#0005FOh, yeah. Let me give you my contact information.\x01",
            "Don't hesitate to call us if there are any new\x01",
            "developments.\x02\x03",
            "#0001FWe don't know when the thief will strike again,\x01",
            "so communication is key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PUnderstood. We'll wait here for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PWe're counting on you, everyone!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Serial Theft Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x15, 0x10)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_65(0x4, 0x1)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    OP_29(0x20, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_76_14387 end

    def Function_77_14B20(): pass

    label("Function_77_14B20")

    EventBegin(0x0)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-19540, 2500, -12620, 0)
    MoveCamera(63, 27, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -17180, 0, -12000, 14)
    SetChrPos(0x102, -18640, 0, -13090, 14)
    SetChrPos(0x103, -18260, 0, -11760, 14)
    SetChrPos(0x104, -17580, 0, -13190, 14)
    SetChrPos(0x1A, -15910, 0, -10370, 194)
    SetChrPos(0x15, -16920, 0, -9360, 194)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A,
        (
            "#11POh, you're back already.\x01",
            "Were you able to find anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0000FWe actually managed to gather\x01",
            "a lot of information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FShall we begin organizing it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#0200FGood idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0300FTake it away, Lloyd.\x02",
    )

    CloseMessageWindow()

    def lambda_14CDB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14CDB)

    def lambda_14CE8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14CE8)

    def lambda_14CF5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14CF5)

    def lambda_14D02():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14D02)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0001FOkay, got it. Let's start going through\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    OP_68(-18800, 2400, -13110, 0)
    MoveCamera(39, 34, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21870, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    SetChrPos(0x101, -15680, 0, -12000, 280)
    SetChrPos(0x102, -19550, 0, -12530, 100)
    SetChrPos(0x103, -19450, 0, -11230, 100)
    SetChrPos(0x104, -18070, 0, -13540, 55)
    SetChrPos(0x1A, -16760, 0, -10660, 145)
    SetChrPos(0x15, -18000, 0, -10000, 145)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#0003FAhem... Let's start by clarifying all of\x01",
            "the information we've obtained.\x02\x03",
            "#0001FAccording to the stalls' reports, the method\x01",
            "used to steal the mira from them was...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Stolen by threat of deadly weapon]\x01",          # 0
            "[Stolen by pretending to be a customer]\x01",      # 1
            "[Stolen while owner is distracted]\x01",           # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_150D1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x104,
        (
            "#12P#0301FPretty sure they all said they were hit while they\x01",
            "were in the middle of dealin' with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FCommitting the crime while the owners were\x01",
            "busy serving customers to avoid detection...\x02\x03",
            "#0200FA crafty method, I must say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FYeah, it doesn't matter how cautious you\x01",
            "are if you're too busy to notice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15249")

    label("loc_150D1")


    ChrTalk(
        0x104,
        "#12P#0305FWere you payin' attention, pal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThe owners declared that they were\x01",
            "preoccupied serving customers when\x01",
            "the thief struck.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#11P#0005FOh, you're right. They totally did say that.\x02\x03",
            "#0003FSo, the thief was able to slip in unnoticed\x01",
            "while the owners were busy.\x02\x03",
            "#0001FBeing cautious won't help you if you're\x01",
            "too busy to notice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15249")


    ChrTalk(
        0x1A,
        (
            "#5PRight, I had heard the same.\x01",
            "Does their cowardice know no bounds?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FLet's not forget our thievin' friend managed to\x01",
            "hit up four of 'em in a row.\x02\x03",
            "#0301FProbably off gloatin' to their friends about their\x01",
            "epic heist right about now, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FYeah... But, don't crimes like these normally\x01",
            "follow a pattern? We should be able to discern\x01",
            "one if we keep looking.\x02\x03",
            "Judging from what I've heard, I get the feeling\x01",
            "there's a pattern behind their actions.\x02\x03",
            "#0003FNow that I've pieced together the information,\x01",
            "the criminal's motive is...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Harassment]\x01",               # 0
            "[Financial problems]\x01",       # 1
            "[For their enjoyment]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15629")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x102,
        (
            "#6P#0101FI get the feeling that the thief was doing\x01",
            "it for their own enjoyment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FCommitting a series of crimes in rapid\x01",
            "succession leads me to believe that they\x01",
            "were not motivated by a lack of mira.\x02\x03",
            "Rather, I believe they were seeking thrills\x01",
            "and getting enjoyment out of stealing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A29")

    label("loc_15629")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1586C")

    ChrTalk(
        0x102,
        (
            "#6P#0105FDo you think they were harassing the stall owners?\x01",
            "The criminals could have been seeking enjoyment\x01",
            "from tormenting them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FI do not think so.\x01",
            "The logical course of action is to repeatedly target\x01",
            "one stall if they were trying to harass someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0006FY-You're right. They never targeted the same stall\x01",
            "twice, so I doubt that was their intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FGiven that they hit up a bunch of 'em in a row,\x01",
            "I don't think they were in it for the money.\x02\x03",
            "#0301FThey were probably screwin' around and\x01",
            "tryin' to have some fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A29")

    label("loc_1586C")


    ChrTalk(
        0x102,
        (
            "#6P#0105FCould they have been motivated by financial\x01",
            "problems? I'm not getting that impression, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0301FI'm with ya. Hittin' up a bunch of stalls in a\x01",
            "short period of time makes me think they were\x01",
            "doin' it to screw with all of the stall owners.\x02\x03",
            "#0303FThere are plenty of bigger fish to fry\x01",
            "if they needed some serious cash.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0005FY-Yeah, you're right.\x02\x03",
            "#0003FOur criminal probably gets their thrills\x01",
            "from stealing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A29")


    ChrTalk(
        0x15,
        (
            "#5PIt's utterly ridiculous that someone would\x01",
            "commit so many thefts for a reason like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PWhat kind of criminal is responsible for this tomfoolery?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FHmm... I think I have an idea of what the\x01",
            "criminal might be like.\x02\x03",
            "#0001FThe criminal is...\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[A professional pickpocketer]\x01",      # 0
            "[A youthful duo]\x01",                   # 1
            "[A group of bandits]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16021")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15BD5")
    OP_2C(0x20, 0x2)

    label("loc_15BD5")


    ChrTalk(
        0x101,
        "#11P#0001FI'm fairly certain it's a pair of younger thieves.\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(
        0x104,
        "#12P#0305FHow do ya figure? There weren't any witnesses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0000FThink about it for a second. Each stall was\x01",
            "robbed in the middle of serving a customer.\x02\x03",
            "Didn't the descriptions of the customer they\x01",
            "served sound eerily similar to one another?\x02\x03",
            "#0003FThe stalls in the Administrative and Harbor\x01",
            "Districts both described him as a 'young,\x01",
            "carefree-looking man.'\x02\x03",
            "Meanwhile, the stalls in Central Square and the\x01",
            "Entertainment District described him as a\x01",
            "'talkative young man.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FThose were the only profiles recounted by the\x01",
            "stall owners at the moment of the theft.\x02\x03",
            "#0200FIt is far too unlikely to be a coincidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FYeah, that's why I'm thinking our criminals\x01",
            "are a pair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FI think I get what you're saying...\x02\x03",
            "While one of them garnered the attention of the\x01",
            "stall owner, the other went and stole the mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FYeah, makes sense if you assume that\x01",
            "they were alternatin' roles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1659A")

    label("loc_16021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160B9")

    ChrTalk(
        0x101,
        (
            "#11P#0001FI believe it was the work of a\x01",
            "professional pickpocketer.\x02\x03",
            "Their technique was too adept\x01",
            "to be executed by amateurs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16137")

    label("loc_160B9")


    ChrTalk(
        0x101,
        (
            "#11P#0001FI think it may have been a larger group of thieves.\x02\x03",
            "Their technique was too adept to be executed\x01",
            "by amateurs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16137")


    ChrTalk(
        0x102,
        (
            "#6P#0103FOr so you'd think...\x02\x03",
            "#0100FBut remember, the stall owners were busy at the\x01",
            "time of the theft. You don't necessarily have to\x01",
            "be skilled at stealing to pull it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0005FTh-That's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0203FI am concerned, though.\x02\x03",
            "#0200FEach stall was targeted while they were\x01",
            "preoccupied with customers, correct?\x02\x03",
            "Does the description of the customer in each\x01",
            "recounting not sound similar to you?\x02\x03",
            "#0203FThe customers described in the Administrative and\x01",
            "Harbor Districts were young and carefree-looking men.\x02\x03",
            "And the customers described in Central Square and\x01",
            "the Entertainment District were talkative young men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0305FWell, when ya put it that way...\x02\x03",
            "#0301FSomethin' smells fishy. Kinda odd for their\x01",
            "descriptions to be that similar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FYeah, it's more than a coincidence that the crimes\x01",
            "were committed while the owners were serving\x01",
            "customers that matched the same profile.\x02\x03",
            "#0003FI'd be willing to bet our thieves work as a duo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FI think I get what you're saying...\x02\x03",
            "#0101FWhile one of them garnered the attention of the\x01",
            "stall owner, the other went and stole the goods?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1659A")


    ChrTalk(
        0x1A,
        (
            "#5PWe absolutely cannot let this continue to\x01",
            "happen. Please, find them before they\x01",
            "strike again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PYeah, I agree with the chairman!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PHow are you going to find them, though?\x01",
            "The city is packed with people right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PIt's hopeless, isn't it? The best we can do is\x01",
            "alert the shopkeepers to stay on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FI disagree. I think we have enough information on\x01",
            "how they operate to devise a countermeasure\x01",
            "to stop them from stealing again.\x02\x03",
            "#0001FHey, guys. Where do you think our friend\x01",
            "is going to strike next?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(
        0x102,
        (
            "#6P#0101FI think it's safe to exclude any stores that have\x01",
            "already been targeted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FSooner or later, they're going to get caught with\x01",
            "their hands in the cookie jar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FIt is highly probable that they will focus on stalls\x01",
            "that have yet to be targeted and will strike while\x01",
            "they are serving a customer.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A2F")
    OP_2C(0x20, 0x1)

    ChrTalk(
        0x101,
        (
            "#11P#0003F(It's a good thing we interviewed a few shopkeepers\x01",
            "that were unscathed, too.)\x02\x03",
            "#0001F(I'm pretty certain the one that is most likely\x01",
            "to be targeted is...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16AF0")

    label("loc_16A2F")


    ChrTalk(
        0x101,
        (
            "#11P#0003F(Maybe I should have asked a few stalls that\x01",
            "weren't targeted for information, too.)\x02\x03",
            "#0001F(Oh, well. Judging from what we saw, the next\x01",
            "stall most likely to be targeted is...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AF0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Central Square's sweets stall]\x01",                    # 0
            "[Administrative District's omelet rice stall]\x01",      # 1
            "[Entertainment District's ice cream stall]\x01",         # 2
            "[Harbor District's noodle stall]\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16BD8"),
        (1, "loc_1717F"),
        (2, "loc_17423"),
        (3, "loc_176C3"),
        (SWITCH_DEFAULT, "loc_178C1"),
    )


    label("loc_16BD8")

    OP_2C(0x20, 0x2)

    ChrTalk(
        0x1A,
        "#5PWhat about the sweets stall in Central Square?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FYeah, and for good reason.\x02\x03",
            "#0003FThe Administrative District will be filled\x01",
            "with officers because of today's parade.\x02\x03",
            "The Entertainment and Harbor Districts\x01",
            "are relatively open areas compared to\x01",
            "Central Square.\x02\x03",
            "#0001FConsidering they need to secure an easily\x01",
            "accessible escape route, Central Square\x01",
            "is the most logical location.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(15)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(12)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#0305FWhy would they need an escape route?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0001FThe shopkeepers that were already stolen from\x01",
            "are going to be more aware of their surroundings.\x02\x03",
            "#0003FEven if we've got an experienced thief on\x01",
            "our hands, they're far more likely to get\x01",
            "caught at this point.\x02\x03",
            "#0000FThey'll need to make a quick getaway\x01",
            "if they get caught in the act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0105FYou know, now that you mention it...\x02\x03",
            "#0100FIsn't the burger stall also located at the\x01",
            "intersection between a few of the districts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FThe sweets shop in Central Square is within\x01",
            "proximity of the Back Alley and the Administrative\x01",
            "District.\x02\x03",
            "That area decidedly has the highest number\x01",
            "of escape routes available, so the thieves\x01",
            "are likely to target that stall next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FGood thinkin', Tio Tot!\x02\x03",
            "#0300FSince it's come down to this, let's stake it all\x01",
            "on the thieves targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0xE)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 4)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_178C1")

    label("loc_1717F")


    ChrTalk(
        0x1A,
        (
            "#5PWhat about the omelette stall over in\x01",
            "the Administrative District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "With the parade happening today,\x01",
            "that area will be unusually congested.\x02\x03",
            "#0001FThe thieves may be able to use the crowd\x01",
            "as a cover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0101FWon't there be additional police officers for\x01",
            "security purposes, though?\x02\x03",
            "#0103FI'd imagine it's going to be risky to try and\x01",
            "commit a crime in front of a gathering\x01",
            "of law enforcement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FWh-Whoops. I hadn't considered that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FProbably a better idea to keep an\x01",
            "eye on one stall, yeah?\x02\x03",
            "#0300FLet's stake it all on the thieves\x01",
            "targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x11)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 1)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_178C1")

    label("loc_17423")


    ChrTalk(
        0x1A,
        (
            "#5PWhat about the ice cream stall over in the\x01",
            "Entertainment District?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "I recall the stall being located right\x01",
            "in front of Arc en Ciel.\x02\x03",
            "#0001FThey could easily weave through the crowds\x01",
            "at the beginning or end of a performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0205FDoes that not fit the operating procedure of\x01",
            "a singular thief, though?\x02\x03",
            "#0200FMixing in with the crowd is not quite the same as\x01",
            "distracting the stall owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FWh-Whoops. I hadn't considered that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FProbably a better idea to keep an\x01",
            "eye on one stall, yeah?\x02\x03",
            "#0300FLet's stake it all on the thieves\x01",
            "targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x12)
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_178C1")

    label("loc_176C3")


    ChrTalk(
        0x1A,
        "#5PWhat about the noodle stall in the Harbor District?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#0003FHmm... You might be right.\x02\x03",
            "#0001FIt's the stall closest to this tent...\x01",
            "But they might know how obvious it'd be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#0103FI know we assumed they're thrill seekers, but that\x01",
            "might be too much of a risk for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0006FWh-Whoops. I hadn't considered that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0303FProbably a better idea to keep an\x01",
            "eye on one stall, yeah?\x02\x03",
            "#0300FLet's stake it all on the thieves\x01",
            "targeting 'em next!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x20, 0x1, 0x13)
    StopBGM(0x7D0)
    WaitBGM()
    Call(0, 83)
    Jump("loc_178C1")

    label("loc_178C1")

    Return()

    # Function_77_14B20 end

    def Function_78_178C2(): pass

    label("Function_78_178C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch23600.itc", 0x29)
    LoadChrToIndex("chr/ch30000.itc", 0x2A)
    LoadChrToIndex("chr/ch02708.itc", 0x2B)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_68(-20590, 2500, -12420, 0)
    MoveCamera(64, 28, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20320, 0)
    SetChrPos(0x101, -19640, 0, -10290, 90)
    SetChrPos(0x102, -18810, 0, -12750, 20)
    SetChrPos(0x103, -19720, 0, -11730, 65)
    SetChrPos(0x104, -17130, 0, -12710, 335)
    SetChrPos(0x1A, -15910, 0, -10370, 245)
    SetChrPos(0x15, -16920, 0, -9360, 200)
    SetChrPos(0x4E, -17790, 0, -11400, 20)
    SetChrPos(0x4F, -18560, 0, -10890, 20)
    SetChrPos(0x50, -19300, 0, -3440, 20)
    SetChrPos(0x51, -20380, 0, -3260, 20)
    SetChrPos(0x52, -15180, 0, -11440, 300)
    SetChrChipByIndex(0x4E, 0x28)
    SetChrSubChip(0x4E, 0x0)
    SetChrChipByIndex(0x4F, 0x29)
    SetChrSubChip(0x4F, 0x0)
    SetChrChipByIndex(0x50, 0x2A)
    SetChrSubChip(0x50, 0x0)
    SetChrChipByIndex(0x51, 0x2A)
    SetChrSubChip(0x51, 0x0)
    SetChrChipByIndex(0x52, 0x2B)
    SetChrSubChip(0x52, 0x0)
    ClearChrFlags(0x4E, 0x80)
    ClearChrBattleFlags(0x4E, 0x8000)
    ClearChrFlags(0x4F, 0x80)
    ClearChrBattleFlags(0x4F, 0x8000)
    ClearChrFlags(0x50, 0x80)
    ClearChrBattleFlags(0x50, 0x8000)
    ClearChrFlags(0x51, 0x80)
    ClearChrBattleFlags(0x51, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A3F")
    ClearChrFlags(0x52, 0x80)
    ClearChrBattleFlags(0x52, 0x8000)

    label("loc_17A3F")

    BeginChrThread(0x4E, 0, 0, 79)
    BeginChrThread(0x4F, 0, 0, 79)
    OP_52(0x4E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x4E,
        (
            "#11PYou're just a bunch of spineless cops.\x01",
            "The hell do you think you can do to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        (
            "#5PYa think you can just walk all over us,\x01",
            "the Black Emperors?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BC5")

    ChrTalk(
        0x52,
        "#11P#1207FGrrrrrrrrowl!\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)

    def lambda_17B68():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_17B68)

    def lambda_17B75():
        TurnDirection(0xFE, 0x52, 500)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_17B75)
    Sleep(200)
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x4E,
        (
            "#11PEeek!\x01",
            "W-We're sorry!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BC5")


    ChrTalk(
        0x15,
        (
            "#5PI'm relieved that we were able to retrieve the mira...\x01",
            "I must say, though. These hooligans aren't quite as\x01",
            "rough around the edges as I was expecting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0306FYou said it, bud.\x02\x03",
            "#0300FOne punch from the downtown delinquents,\x01",
            "and they'd be cryin' like a bunch of pansies.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x4E, 0x0)
    EndChrThread(0x4F, 0x0)
    OP_63(0x4E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x4F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_17D1F():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_17D1F)

    def lambda_17D3C():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_17D3C)
    Sleep(1200)
    OP_63(0x4E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    OP_63(0x4F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0005FWow, that quieted them down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0105FDo you think it's possible they really\x01",
            "were threatened by them?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17DFD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_17DFD)

    def lambda_17E0A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_17E0A)
    Sleep(200)

    ChrTalk(
        0x4E,
        (
            "#11PWh-Wh-Who'd ever get scared by guys\x01",
            "like that?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        (
            "#5PYou makin' fun of us or somethin'?!\x01",
            "We'd have no trouble takin' 'em on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0200FBingo.\x02\x03",
            "It all makes sense now. They were made fools of,\x01",
            "so they were resorting to petty crimes as a means\x01",
            "of venting their frustration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PSo that's what it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PThey've disrupted the festival, and for what?\x01",
            "Some selfish, self-pitying reason?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17FB4():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_17FB4)

    def lambda_17FC1():
        OP_93(0xFE, 0x37, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_17FC1)
    Sleep(300)
    SetCameraDistance(19210, 1600)
    OP_95(0x1A, -16880, 0, -10300, 1000, 0x0)

    def lambda_17FEE():
        OP_93(0xFE, 0xF5, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_17FEE)
    OP_93(0x1A, 0xF5, 0x190)
    Sleep(300)

    ChrTalk(
        0x1A,
        (
            "#11PYou'd better listen up, you whippersnappers.\x01",
            "I'll have you answer for your crimes, you hear me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x4E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x4F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    ChrTalk(
        0x4E,
        (
            "#12PUgh...\x01",
            "(What's with this old geezer?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x4F,
        (
            "#6P*gulp*\x01",
            "(He's givin' us a real scary look...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x50,
        "Voice",
        (
            "#4POh, there you are. You're the\x01",
            "Special Support Section, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-19920, 2500, -11390, 2500)
    MoveCamera(53, 31, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(20320, 2500)

    def lambda_18174():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_18174)

    def lambda_18181():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_18181)

    def lambda_1818E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1818E)

    def lambda_1819B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1819B)

    def lambda_181A8():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_181A8)

    def lambda_181B5():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_181B5)

    def lambda_181C2():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_181C2)

    def lambda_181CF():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_181CF)

    def lambda_181DC():
        OP_95(0xFE, -19300, 0, -7440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_181DC)

    def lambda_181F6():
        OP_95(0xFE, -20380, 0, -7260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_181F6)
    Sleep(2500)

    ChrTalk(
        0x50,
        "#11PSorry we're late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x51,
        "#5PWe're here to take away the thieves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#0001FThanks. Sorry for calling you out here\x01",
            "during such a busy period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x50,
        "#11PNot a problem. It's our job, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x50,
        "#11PAre these two the guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#0001FYeah. If you would escort them to HQ, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x51,
        "#5PRight. You can count on us.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x4E, -19770, 0, -6410, 341)
    SetChrPos(0x4F, -20770, 0, -6710, 0)
    SetChrPos(0x1A, -18220, 0, -9760, 315)
    SetChrPos(0x15, -18050, 0, -8480, 315)
    SetChrPos(0x50, -19220, 0, -7200, 341)
    SetChrPos(0x51, -21370, 0, -7320, 26)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x50,
        "#11PHey, move it along!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x4E,
        "#11PWhoa! Don't push me!\x02",
    )

    CloseMessageWindow()

    def lambda_18415():

        label("loc_18415")

        TurnDirection(0xFE, 0x51, 400)
        Yield()
        Jump("loc_18415")

    QueueWorkItem2(0x1A, 1, lambda_18415)

    def lambda_18427():

        label("loc_18427")

        TurnDirection(0xFE, 0x50, 400)
        Yield()
        Jump("loc_18427")

    QueueWorkItem2(0x15, 1, lambda_18427)

    def lambda_18439():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18439)

    def lambda_18446():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18446)

    def lambda_18453():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_18453)

    def lambda_18460():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_18460)
    Sleep(100)

    def lambda_18470():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_18470)

    def lambda_18485():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_18485)

    def lambda_1849A():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_1849A)

    def lambda_184AF():
        OP_9B(0x0, 0xFE, 0x5, 0x2328, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_184AF)
    Sleep(6000)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x15, 0x1)
    OP_68(-20430, 2500, -11880, 2000)
    MoveCamera(69, 29, 0, 2000)
    OP_6E(420, 2000)
    SetCameraDistance(20320, 2000)

    def lambda_184FD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_184FD)

    def lambda_1850A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1850A)

    def lambda_18517():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18517)

    def lambda_18524():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18524)
    BeginChrThread(0x1A, 1, 0, 80)
    Sleep(100)
    BeginChrThread(0x15, 1, 0, 81)
    Sleep(300)
    SetChrFlags(0x4E, 0x80)
    SetChrBattleFlags(0x4E, 0x8000)
    SetChrFlags(0x4F, 0x80)
    SetChrBattleFlags(0x4F, 0x8000)
    SetChrFlags(0x50, 0x80)
    SetChrBattleFlags(0x50, 0x8000)
    SetChrFlags(0x51, 0x80)
    SetChrBattleFlags(0x51, 0x8000)

    ChrTalk(
        0x15,
        "#5PPhew... Looks like it's case closed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FThey didn't look like they were from Crossbell,\x01",
            "so I figure they won't be in jail for more than\x01",
            "three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#0306FCrossbell's pretty soft on the foreigners, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PHaha. Yes, well, the joke is on them. They'll be\x01",
            "sitting in a jail cell staring at a stone wall, while\x01",
            "the rest of us are out here enjoying the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PNot to mention...I had a bit of fun striking a bit\x01",
            "of fear into their hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#0205FI must say, your charade was spectacular.\x01",
            "They were completely fooled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PHaha. It comes with the experience of\x01",
            "being a veteran trader.\x01",
            "I'm used to having to put on airs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0000FIt's definitely a side of you I've never seen before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_18ADC")

    ChrTalk(
        0x1A,
        (
            "#11PEither way, I think I put on quite the performance,\x01",
            "if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "#11PThank you for resolving the issue, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PIndeed. We're truly in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PPlease allow for the Business Owners' Association\x01",
            "to present you its utmost gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0000FOh, no--you don't have to do that. We're\x01",
            "happy to have solved the case before any\x01",
            "more damage was dealt.\x02\x03",
            "You know where to find us if you ever run into\x01",
            "any other problems. We'd be happy to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PA fine plan, indeed. I shall do so if the need\x01",
            "ever arises again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0100FWith pleasure. We'd be happy to be\x01",
            "of service to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    Jump("loc_18F6E")

    label("loc_18ADC")


    ChrTalk(
        0x101,
        (
            "#6P#0006FI'm sorry, everyone. Looks like my\x01",
            "deduction was a little off the mark.\x02\x03",
            "They almost managed to slip away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#0106FWe feel terribly sorry, and after you put\x01",
            "your faith in us, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PNo, no. That's quite all right. You were able to\x01",
            "resolve it, and that's what matters.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x87, 0x190)

    ChrTalk(
        0x1A,
        (
            "#11PNot to mention, that excellent police dog of yours...\x01",
            "Zeit was his name, I believe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PYou considered a worst-case scenario, and\x01",
            "masterfully deployed him. I was impressed\x01",
            "to see that level of reasoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#0012FHa...hahaha... Well, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x52,
        "#11P#1203FGrrrrrowl...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x52, 400)
    Sleep(300)

    ChrTalk(
        0x103,
        "#6P#0203FHe says we still have a long road ahead of us.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#12P#0306FAw, shucks. We really screwed that one up.\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A, 0xE1, 0x190)
    OP_63(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x15,
        (
            "#5PIt's all right. You still tried to help us. On behalf\x01",
            "of the Business Owners' Association, allow us\x01",
            "to thank you for your service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "#11PWe may rely on you again when the time\x01",
            "comes. Please lend us your strength\x01",
            "when it does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#0100FWe'd be glad to be of service again.\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)

    label("loc_18F6E")

    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Quest \x07\x02",
            "[Serial Theft Investigation]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18030, 0, -11890, 18)
    SetChrPos(0x1A, -16379, 0, -10840, 315)
    SetChrPos(0x15, -17390, 0, -9830, 135)
    OP_4C(0x1A, 0xFF)
    OP_4C(0x15, 0xFF)
    SetChrPos(0x16, -17350, 0, -4670, 270)
    SetChrPos(0x13, -18560, 0, -4340, 90)
    SetChrFlags(0x52, 0x80)
    SetChrBattleFlags(0x52, 0x8000)
    OP_49()
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x20, 0x4, 0x10)
    SetScenarioFlags(0x2, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_178C2 end

    def Function_79_1907F(): pass

    label("Function_79_1907F")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_190BF"),
        (1, "loc_190CB"),
        (2, "loc_190D7"),
        (3, "loc_190E3"),
        (4, "loc_190EF"),
        (5, "loc_190FB"),
        (6, "loc_19107"),
        (SWITCH_DEFAULT, "loc_19113"),
    )


    label("loc_190BF")

    OP_A0(0xFE, 2450, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_190CB")

    OP_A0(0xFE, 2550, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_190D7")

    OP_A0(0xFE, 2600, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_190E3")

    OP_A0(0xFE, 2400, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_190EF")

    OP_A0(0xFE, 2650, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_190FB")

    OP_A0(0xFE, 2350, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_19107")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_19113")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_1911F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19182")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_19152"),
        (1, "loc_1915E"),
        (2, "loc_1916A"),
        (SWITCH_DEFAULT, "loc_19176"),
    )


    label("loc_19152")

    OP_93(0xFE, 0x2D, 0x1F4)
    Jump("loc_19176")

    label("loc_1915E")

    OP_93(0xFE, 0x10E, 0x1F4)
    Jump("loc_19176")

    label("loc_1916A")

    OP_93(0xFE, 0x87, 0x1F4)
    Jump("loc_19176")

    label("loc_19176")

    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("loc_1911F")

    label("loc_19182")

    Return()

    # Function_79_1907F end

    def Function_80_19183(): pass

    label("Function_80_19183")

    OP_95(0xFE, -16940, 0, -10040, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_80_19183 end

    def Function_81_1919F(): pass

    label("Function_81_1919F")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, -17600, 0, -9230, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_81_1919F end

    def Function_82_191C2(): pass

    label("Function_82_191C2")

    EventBegin(0x0)
    OP_4B(0x10, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(12800, 2510, 10130, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrPos(0x101, 14260, 10, 10900, 0)
    SetChrPos(0x102, 15680, 10, 9480, 0)
    SetChrPos(0x103, 15680, 10, 10900, 0)
    SetChrPos(0x104, 14260, 10, 9480, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#12P#0309F'Mithra's Gelato,' eh?\x01",
            "Damn, she's one fine lady!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0006FCan't you take it down a few notches, Randy?\x01",
            "We're not here to flirt with her.\x02\x03",
            "#0001FLet's just focus on the questioning, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#0100FExcuse us, ma'am. We're here with the Crossbell\x01",
            "police. May we take a few moments to ask\x01",
            "you about what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PYeah. You're talking about the theft, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PHe managed to pull a fast one on me\x01",
            "while I was serving a customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#0200FHe struck while you were busy, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PYeah, I was busy serving some carefree-looking\x01",
            "foreigner that was trying his hardest to hit on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PWhile I was warding away his persistent\x01",
            "flirting, I thought I felt someone sneaking\x01",
            "around behind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PBut, it was too little, too late. By the time\x01",
            "I noticed, the register had already been\x01",
            "emptied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#0001FThat means you don't know the full details\x01",
            "of the execution, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThat's correct. I made the terrible mistake of\x01",
            "not witnessing the crime.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198AB")
    OP_68(13510, 2510, 9070, 1200)
    MoveCamera(45, 24, 0, 1200)

    def lambda_1968C():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1968C)

    def lambda_19699():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19699)

    def lambda_196A6():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_196A6)

    def lambda_196B3():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_196B3)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#6P#0003FI think we've heard everything she has to offer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#0300FYeah, sounds 'bout right. Wanna head back\x01",
            "and sort through the details?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_198A5")

    ChrTalk(
        0x102,
        (
            "#0100FWe haven't heard from the Business Owners'\x01",
            "Association, so we can assume that no other\x01",
            "stalls have been victimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#0203FThat should be the case, yes.\x02\x03",
            "#0200FThough, perhaps it would be prudent\x01",
            "to conduct one more round of the food\x01",
            "stalls, just to be sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198A5")

    OP_29(0x20, 0x1, 0xD)

    label("loc_198AB")

    OP_5A()
    SetChrPos(0x0, 14780, 10, 10480, 0)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_82_191C2 end

    def Function_83_198CE(): pass

    label("Function_83_198CE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(806)
    OP_68(-12140, 2500, 10400, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(31380, 0)
    SetChrPos(0x101, -2510, -700, 2200, 315)
    SetChrPos(0x102, -3310, -700, 3000, 315)
    SetChrPos(0x103, -3710, -700, 1390, 315)
    SetChrPos(0x104, -4520, -700, 2180, 315)
    SetChrPos(0x44, -10280, 0, 11510, 0)
    SetChrPos(0x45, 1440, 0, 10420, 45)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x45, 0x4)
    SetChrChipByIndex(0x44, 0x18)
    SetChrSubChip(0x44, 0x0)
    SetChrChipByIndex(0x45, 0x9)
    SetChrSubChip(0x45, 0x0)
    ClearChrFlags(0x44, 0x80)
    ClearChrBattleFlags(0x44, 0x8000)
    ClearChrFlags(0x45, 0x80)
    ClearChrBattleFlags(0x45, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The members of the SSS traveled to the designated\x01",
            "district to conduct their stakeout.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-12140, 1500, 10400, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x44, 1, 0, 84)
    OP_0D()
    OP_6F(0x1)

    AnonymousTalk(
        0x101,
        (
            "#0001F...\x02\x03",
            "It doesn't look like this is our guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x44, 0x1)
    OP_64(0x9)
    OP_64(0x44)
    Sleep(200)
    OP_95(0x44, 1370, 0, 11710, 1500, 0x0)
    Sleep(1800)
    OP_95(0x45, -10170, 0, 10420, 1500, 0x0)
    OP_95(0x45, -10170, 0, 11550, 1500, 0x0)
    BeginChrThread(0x9, 1, 0, 84)
    Sleep(150)
    BeginChrThread(0x45, 1, 0, 84)
    Sleep(2500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x45, 0x1)
    OP_64(0x9)
    OP_64(0x45)
    Sleep(200)
    OP_95(0x45, -14300, 0, 13120, 1500, 0x0)
    OP_95(0x45, -14300, 2000, 23040, 1500, 0x0)
    SetChrFlags(0x44, 0x80)
    SetChrBattleFlags(0x44, 0x8000)
    SetChrFlags(0x45, 0x80)
    SetChrBattleFlags(0x45, 0x8000)

    AnonymousTalk(
        0x104,
        "#0306F'Fraid you're right.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x103,
        "#0200FAnd it has already been an hour...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x101,
        (
            "#0001FI don't get it. If they were coming, they should\x01",
            "have shown up by now...\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-4170, 1840, 1020, 0)
    MoveCamera(3, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13040, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x87, 0x190)
    Sleep(50)

    def lambda_19C39():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19C39)

    def lambda_19C46():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19C46)

    def lambda_19C53():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_19C53)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#11P#0003FYes, sir! Lloyd Bannings spea--\x02\x03",
            "#0005FThe thief appeared?!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#11P#0001FC-Central Square? Got it!\x02\x03",
            "We'll be there right away!\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#11P#0006FSorry, guys. It looks like my deductions\x01",
            "were a little off target.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#0101FIt's fine. Let's hurry, Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#0001FR-Right. Let's go!\x02",
    )

    CloseMessageWindow()

    def lambda_19E3E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19E3E)

    def lambda_19E4B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19E4B)

    def lambda_19E58():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19E58)

    def lambda_19E65():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19E65)
    Sleep(300)

    def lambda_19E75():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19E75)

    def lambda_19E8A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19E8A)

    def lambda_19E9F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19E9F)

    def lambda_19EB4():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19EB4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_198CE end

    def Function_84_19EE1(): pass

    label("Function_84_19EE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19F06")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_84_19EE1")

    label("loc_19F06")

    Return()

    # Function_84_19EE1 end

    def Function_85_19F07(): pass

    label("Function_85_19F07")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "        Lupinus River - Lighthouse 1\x01\x01",
            "Unauthorized entry is strictly prohibited.\x01",
            "                                 - City Hall\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_85_19F07 end

    def Function_86_19FBD(): pass

    label("Function_86_19FBD")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A sign is affixed to the locked door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   Heiyue Trading, Ltd. - Crossbell Branch\x01",
            "If you have business with us, please knock.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_86_19FBD end

    SaveToFile()

Try(main)
