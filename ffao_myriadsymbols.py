import random

def checkprime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def checktri(n):
    return int((n*8+1)**0.5) == (n*8+1)**0.5

def checksq(n):
    return int(n**0.5) == n**0.5

def checkfibonacci(n):
    return n in [0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]

def checkdiv3(n):
    return not n%3

def amodb(a,b):
    return lambda x: x%b == a%b

def countCondition(n, func):
    ret = 0
    for i in range(1,n+1):
        if func(i):
            ret += 1
    return ret

def cutOut(s, func):
    ret = ""
    disc = ""
    for i in range(1,len(s)+1):
        if not func(i):
            ret += s[i-1]
        else:
            disc += s[i-1]
   # print(disc)
    #print()
    return ret

def interleave(s, interleave, func):
    ret = ""
    j, k = 0, 0
    for i in range(1,len(s)+len(interleave)+1):
        if func(i):
            ret += interleave[j]
            j += 1
        else:
            ret += s[k]
            k += 1
    return ret

conditions = [(1,7),(1,3),(1,5),(1,4),(1,10),(5,6),(3,4),(5,5),(2,2),(1,5),(1,3),(4,9),(6,7),(3,4)]
lengths = []
chars = 10000
for i in conditions:
    lengths.append(countCondition(chars, amodb(i[0],i[1])))
    chars -= countCondition(chars, amodb(i[0],i[1]))
#print(lengths, chars)

finstring = "You're almost done! Congratulations on getting here and give yourself a pat on the back! However, unfortunately your journey isn't finished yet. "\
"Alright, now solve what everything before this leads up again now, amazingly encoded here!"

stringlist = ["" for i in range(14)]

#print(finstring)

stringlist[0] = "Hello. Welcome to a concept that's clearly not cribbing off another puzzle concept espoused by a guy of the name Charles, no sir. There aren't even 10000 puzzles in this... puzzle. "\
                "It is probably a little programming heavy though, but you probably knew that already. Anyway, I'm positively pleased that you found this message by looking at every seventh character. "\
                "Quite nice! You've used this message up, you won't need it anymore. Now, I will end my spiel with an absurd number of tildes, a character that doesn't appear in the rest of the text! "\
                "Look for the hashtags next"+"~"*(911-56)
stringlist[1] = "Good work! You performed the rite of CUTTING STUFF OUT! [ACHIEVEMENT UNLOCKED] The next symbol is the ampersand. "+"#"*2744
stringlist[2] = "This is the third message, not to be confused by the fourth message. To locate the fourth message, consider the periodicity of the dollar sign! Good luck!"+"&"*989
stringlist[3] = "This is the fourth message, not to be confused by the third message. I'm not going to say what the next symbol to cut out is."+"$"*1018
stringlist[4] = "Are you ready for all the challenges I'll throw in your way? Be prepared, as they say. "+"="*256
stringlist[5] = "Hehe, I don't have to start with the first character to start from! Maybe you had to retool your code (you ARE coding right? I hope so!) "\
                "to accomodate for this PLOT TWIST but I'm sure it was no challenge for a capable programmer like you. "+"%"*275
stringlist[6] = "This is the seventh message. Good work. But there are still more messages to decode. "+"Xx"*278+"X "
stringlist[7] = "Now you're getting the hang of this task. Good job! However, this is the last message for which you will receive a guide rail for which you can easily cut things. "\
                "And now, some random numbers that I've clearly typed. "+''.join([str(random.randint(0,9)) for _ in range(168)])
stringlist[8] = "This message is particularly large. I hope you decided that taking every other character wasn't an unreasonable task for me to do, because I just did it! Hohoho. The downside is that I do have to write"\
                " a lot more text. :\ Well let's do it. It's not like I have anything pressing in my life right now. (Actually, that's completely false. Why am I typing this? I guess as a destressor.) Anyway, well I "\
                "guess this isn't actually that much text, compared to the first few. This is a lot of typed text though, unlike in the beginning where I wanted to get your attention with lots of repeated copied and pasted"\
                " text. This might just be harder to extract out, eh? I have to meet a target in order to fill out the entire length. It's a bit annoying as you might be able to tell."
stringlist[9] = "Yep, same old same old. Take out every X symbols, all according to keikaku.* The onion keeps getting smaller, but it's still here. *TN: keikaku means plan."
stringlist[10] = "Oh so you want a bigger challenge than that? Well here, have a go with the next few! Bet "\
                "you can't find the next one! I've made it super small so that you won't be able to find it! Let's see how you do now."
stringlist[11] = "This is like finding 10 needles in a haystack."
stringlist[12] = "Man, picking out short strings is getting tough, eh?"
stringlist[13] = "I swear, I hope there aren't any more messages after this one. Pretty please??"

comp = finstring
for i in range(len(stringlist)-1,-1,-1):
    #print(len(stringlist[i]))
    comp = interleave(comp, stringlist[i], amodb(conditions[i][0],conditions[i][1]))

print(comp)

for i in range(14):
    comp = cutOut(comp, amodb(conditions[i][0],conditions[i][1]))
#print()
#print(comp)
