# stats_api

## API for Telos BP stats

A quick and dirty web API that provides handy BP data

Usage:  `http://<hostname/IP>:5000/<command>`

Available commands are:

**RAW PRODUCERS LIST**
command: none
URL:  `http://<hostname/IP>:5000/`
Returns:

    "goodblocktls" "174631790543.26547241210937500" "EOS7GbbU4Kg5Yyi1aRFqHiCHRKAJ7ABSf1oHHzfcHuMGCwgJA1qWC" "eosbarcelona" "166571254302.80160522460937500" "EOS5WPXXqDbSm2TdacCSJdm7JCe6uq6eJe9t4A1x8f4BMz5t2fmRb" "telosmiamibp" "165753602121.04574584960937500" "EOS6aaA2VnWhzYhmkV9gSRofCkS9GcLF8QpRpjybWPsrFjSRVNvxL" "telosuknodes" "162215479678.65426635742187500" "EOS8MteEY4nERBurBRRUVfcTyjNjAVER2P2WuQDE3so5Re91i1iv4" "votedutcheos" "161555856015.88775634765625000" "EOS7Nt4qswS6PgFnxd4SUdM5tEr86fbGr5yKoKcMPQcXwdJTMaY2S" "infinitybloc" "159311051374.52032470703125000" "EOS6YDmzf8T58d5j6DdEmxcFoSyPrnDCUvceETkZdSQHhiLqykkoK" "tlsvancouver" "157342921412.14065551757812500" "EOS5FhxNtX12oXngrXtHzgbMgG8BZSY26jr92WHRYr6yfGo6kYr4g" "caleosblocks" "157292111211.42877197265625000" "EOS5dE2h1zymNHqu9UFYj57F5qv8E3ghjSLxNSVoRjMCWeGZB4F6T" "telosdacnode" "153161205973.81835937500000000" "EOS8fBHWo89rNCj25nPwyszjoHMvG6D4CpJBEHco5uLbx6CmWXnAi" "eosiodetroit" "153036181130.11621093750000000" "EOS77fbWJwaNAWt8p2mdc1ADKnQZi3ww5QUNqJoQ9LVps7jWBPAtT" "eosmetaliobp" "150920950532.19528198242187500" "EOS5pHqKcDzoYFa42zX98tzBaaZHQ2nsfTyJ3e4VPyJg4Q2uB78fR" "telosmadrid1" "146486559062.42947387695312500" "EOS8LSnCvd5CaN6sa5wbsFtJ2ZyPfyvXDcP5jBhxvnn33xAracDh8" "tlsvenezuela" "145770956685.76547241210937500" "EOS8VeneRj2rAPtLdJuU9VM4MWeZYbRiqavBnrNQdeP2z7iC4tJrk" "kainosblkpro" "145554696220.47109985351562500" "EOS5EdaJGc9YqXhwdwf2SipjBuiCEBYY2r8S8odcEDexidrGSBbJk" "octagontelos" "141859932794.15405273437500000" "EOS688gt4GZ7ExeBzn1Z78X9ug583WqVPGMtDdbfmfnVnGPb7yiKG" "telosgreenbp" "140208130257.23913574218750000" "EOS71Jn2wt32tEru3xSaFjeMES2gXiXgGarmDeuotVUtM5Puf23b2" "bigironbptex" "135885048628.31762695312500000" "EOS6a3UUjj3MLYn4DfP2KJbu2ckfmBu4yoCM5uEM5zFcBioKKxLQU" "blindblocart" "134965661151.32611083984375000" "EOS5j9uxf9BF9JQSELSp14oeN93Ce5vuLwFoWCHwETq77x18JcPQH" "telosglobal1" "132210066748.50747680664062500" "EOS64HW2FWJ3M2DEmiH19JGHLt8wFqhWKWc3KCeMSsdENmrhMVUGT" "21zephyr1111" "131524194286.61589050292968750" "EOS84cTSUERQTgPEUwFd3ekZadSpM78ZWLPjDt9pTANRHDCCvQLGF" "telosnewyork" "131480636181.38735961914062500" "EOS7uh28mPLSuLsaA9eyNoiLNwky4KDU7sxwfCg9NZcsPhdKxBB2f" "telosvoyager" "128292342869.72482299804687500" "EOS7kJo3Ezsbc5Y4BeAhzfRtXQ1mUGeVamJAbA1LXkQcNtjFChi9Z" "teloscantons" "126832556800.61743164062500000" "EOS69ECgLTUWXk31ZSxrpno88MFqxXTN8JRMZXHGrMNWH53kqA1ZH" "eosdublinwow" "125701006263.78674316406250000" "EOS5HZShDd9tSteXWRYLZAgFk5eoikVs8x21HJkbaQWEosXZasegj" "theteloscope" "113887257709.35890197753906250" "EOS5AUGHMZqpcSwTQY2fMDrUS38j2FmbiKbTQmXAoQbtuAC6JyZcq" "tlosimperabp" "104783898282.63665771484375000" "EOS7mwQMibEXWdaA8MMHmMQH9qPX8W9YWpKTQi2HBkTDEbYSNbZdB" "cryptosuviio" "102446199273.44786071777343750" "EOS8XyVc6MNrtMRigjxNWdaK6bYoqXvddTbzPncnag6fyE7zi5fta" "eosphereiobp" "93061274765.36126708984375000" "EOS5fNhSCnuesLTDz61gMGqeZHrANx3mujc4Es7BaVyqarWVuUNza" "telosintasia" "84732952040.75854492187500000" "EOS5ha1vtA7nG4vzU4NjTkTUhZAEmQUnF2gjshg1qgPoWkXK9sPbe" "eosvibesbloc" "80928673354.19549560546875000" "EOS5ZiocwWSQhJxKv9zzcPaobe772WoLZDWGZzwnXbB4zRVbLkxt4" "telosgermany" "79214391633.17816162109375000" "EOS7XAWAKFmsvc85oMD42eo5fAQuaCPaViWXe2VQ1WATQoMCVEnyH" "atticlabtlbp" "78288069192.75415039062500000" "EOS7kbT3mBeUyQ2LRSNf3yanYei42w4TNpQgZhRbdALH3AuPALvHQ" "csxcommunity" "72855484647.38780212402343750" "EOS8HsrWJ9omjmwt26fieagCM95f2dsT2CyWuFQSFbp4jR7KyrZPF" "swedencornet" "65582137104.53025054931640625" "EOS56tC7rVHKnsFi5fhaPtbMF5nZuYRji6QhbtfDzxyxYsK8CLYF4" "nebulablocks" "64412266493.05771636962890625" "EOS59xrvESTgzoLHN7Cq6D7KX8tazr8FXTS4ZkZHD5qnqTCRXdGTG" "teloscentral" "64179394726.49243164062500000" "EOS74hEm6bB7txDUcmWck6gHnmfbP6atRynZR3fEsNozt7yweTKip" "eostribeprod" "61211289176.98981475830078125" "EOS5SCSeFbKSYsKoiAH8PKwWYbkzsJME5rs73gWbtEA4jPSSaJ1xJ" "eosvenezuela" "57832120832.97035980224609375" "EOS7pUMws312EjWwCcyMvV8hJiN5DFePdxsCknTJsrthp1an2AZXu" "telosafrique" "57240472723.55710601806640625" "EOS6f185z9wQEJ8cqj2jJCxDoiq7h61p5Y6uWqN3B8P2pHta8sQNp" "eossandiego1" "55729470591.71821594238281250" "EOS8Jug5NJM8bLAEnipPwy9HhvSy2knERLK5wve4r4Cdc18nJ9nJr" "telos1russia" "52939689482.77073669433593750" "EOS7ETnqeJ6vBmv9KVcttAn1opy8joQUpMSFbVbc3QDHLhdAGuqFD" "bpeosindexio" "50382106745.54789733886718750" "EOS6ERqjRoWdMS99iVkuMvGKV8ZYX7wSK1QeG8oxgMfYcoYjxWct5" "southafrica1" "49024609203.82810974121093750" "EOS7uUCaqFvVYwRM1NyL3DNjGSnL3j668weCrhU3UA1mBgNomVPB1" "telosunlimit" "46986586865.89434814453125000" "EOS85yGYKxN9Z4mbfVwYgs5Gv4wR4pkYDTSifw5AefJdPiofS3EUd" "eosgermanybp" "43162335531.30780792236328125" "EOS5rFXjYXdL2By97Uuea2aY8Fss4C9uUkEBVKyHvNKgdjXVx3ASn" "telawakeiobp" "38715938913.70986938476562500" "EOS7HjD87RMNuqujYbKi7YJrYqL4mX7xyAx26bn69DEYkUk21QooF" "teleclipse24" "37533440644.90110778808593750" "EOS8Mr8bWmY4uBZ5NzcGMJwqxkEKEf4EstqfzvCj6UVYeTv7Pmyo5" "beyondbtctls" "34103400755.86032867431640625" "EOS7KuyKJKTHPxyxCb11J6QKfxMYWxUZTqik3DJ5biGGVoWbQsTPn" "tokenika4tls" "27913079605.17485809326171875" "EOS7a6yZGncJ8EcLFhVMTBJYfreoXFWSG4XbCb4oW6khDfZK6Qk56" "jijiplannode" "27852696773.21006011962890625" "EOS5VZY7D94YqVyBWThoPLR5w7a7JScrnmpGvCKU2PzRtXPmVSSfd"

**Current BP Rank**
command: bprank
URL:  `http://<hostname/IP>:5000/bprank`
Returns:

    RANK BP VOTES DIFF
    1: goodblocktls 17,463,179 (0)
    2: eosbarcelona 16,657,125 (806,054)
    3: telosmiamibp 16,575,360 (81,765)
    4: telosuknodes 16,221,548 (353,812)
    5: votedutcheos 16,155,586 (65,962)
    6: infinitybloc 15,931,105 (224,481)
    7: tlsvancouver 15,734,292 (196,813)
    8: caleosblocks 15,729,211 (5,081)
    9: telosdacnode 15,316,121 (413,090)
    10: eosiodetroit 15,303,618 (12,503)
    11: eosmetaliobp 15,092,095 (211,523)
    12: telosmadrid1 14,648,656 (443,439)
    13: tlsvenezuela 14,577,096 (71,560)
    14: kainosblkpro 14,555,470 (21,626)
    15: octagontelos 14,185,993 (369,477)
    16: telosgreenbp 14,020,813 (165,180)
    17: bigironbptex 13,588,505 (432,308)
    18: blindblocart 13,496,566 (91,939)
    19: telosglobal1 13,221,007 (275,559) ****
    20: 21zephyr1111 13,152,419 (68,588)
    21: telosnewyork 13,148,064 (4,355)
    -------------------------
    22: telosvoyager 12,829,234 (318,830)
    23: teloscantons 12,683,256 (145,978)
    24: eosdublinwow 12,570,101 (113,155)
    25: theteloscope 11,388,726 (1,181,375)
    26: tlosimperabp 10,478,390 (910,336)
    27: cryptosuviio 10,244,620 (233,770)
    28: eosphereiobp 9,306,127 (938,493)
    29: telosintasia 8,473,295 (832,832)
    30: eosvibesbloc 8,092,867 (380,428)

**Current BP Rotation**
command: rotation
URL:  `http://<hostname/IP>:5000/rotation`
Returns:

    Rotated Out: telosglobal1
    Rotated In: telosvoyager
    Next Rotate: 2019-01-19T03:04:05.000 UTC

**Current TLOS price**
command: price
URL:  `http://<hostname/IP>:5000/price`
Returns:

    TLOS/EOS: $0.04 | EOS/USD: $2.50 | TLOS/USD: $0.10

**All of the Above**

command: all URL: `http://<hostname/IP>:5000/all` Returns: 
RANK BP VOTES DIFF 
1: goodblocktls 17,463,179 (0) 
2: eosbarcelona 16,657,125 (806,054) 
3: telosmiamibp 16,575,360 (81,765) 
4: telosuknodes 16,221,548 (353,812) 
5: votedutcheos 16,155,586 (65,962) 
6: infinitybloc 15,931,105 (224,481) 7: tlsvancouver 15,734,292 (196,813) 8: caleosblocks 15,729,211 (5,081) 9: telosdacnode 15,316,121 (413,090) 10: eosiodetroit 15,303,618 (12,503) 11: eosmetaliobp 15,092,095 (211,523) 12: telosmadrid1 14,648,656 (443,439) 13: tlsvenezuela 14,577,096 (71,560) 14: kainosblkpro 14,555,470 (21,626) 15: octagontelos 14,185,993 (369,477) 16: telosgreenbp 14,020,813 (165,180) 17: bigironbptex 13,588,505 (432,308) 18: blindblocart 13,496,566 (91,939) 19: telosglobal1 13,221,007 (275,559) **** 20: 21zephyr1111 13,152,419 (68,588) 21: telosnewyork 13,148,064 (4,355)

22: telosvoyager 12,829,234 (318,830)
23: teloscantons 12,683,256 (145,978)
24: eosdublinwow 12,570,101 (113,155)
25: theteloscope 11,388,726 (1,181,375)
26: tlosimperabp 10,478,390 (910,336)
27: cryptosuviio 10,244,620 (233,770)
28: eosphereiobp 9,306,127 (938,493)
29: telosintasia 8,473,295 (832,832)
30: eosvibesbloc 8,092,867 (380,428)

-----------------------
Rotated Out: telosglobal1
Rotated In: telosvoyager
Next Rotate: 2019-01-19T03:04:05.000 UTC

------------------------
TLOS/EOS: $0.04 | EOS/USD: $2.50 | TLOS/USD: $0.10
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI3OTM3NjIwOF19
-->