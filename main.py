import random
from merge_image import mergeImageAndSave
count = 3333

def getBackground():
  n = random.randrange(14)
  if n == 0:
    return 'Katakana Goma'
  elif n == 1:
    return 'Katakana Umi'
  elif n == 2:
    return 'Katakana Ichigo'
  elif n == 3:
    return 'Katakana Sakura'
  elif n == 4:
    return 'Katakana Midori'
  elif n == 5:
    return 'Katakana Kinako'
  elif n == 6:
    return 'Katakana Murasaki'
  elif n == 7:
    return 'Goma'
  elif n == 8:
    return 'Umi'
  elif n == 9:
    return 'Ichigo'
  elif n == 10:
    return 'Sakura'
  elif n == 11:
    return 'Midori'
  elif n == 12:
    return 'Kinako'
  elif n == 13:
    return 'Murasaki'

def getLegs():
  n = random.randrange(10000)
  if n < 500:
    return 'Samurai Legs'
  elif n < 1000:
    return 'Yakuza Legs'
  elif n < 1500:
    return 'Yellow Mules'
  elif n < 2000:
    return 'Good Pea Legs'
  elif n < 2500:
    return 'Girl Power Legs'
  elif n < 3000:
    return 'NYC Street Legs'
  elif n < 3500:
    return 'Pink Pumps'
  elif n < 4000:
    return 'Combat Boots'
  elif n < 4500:
    return 'Mint Pumps'
  elif n < 5000:
    return 'Bare'
  elif n < 5500:
    return 'Rugby Legs'
  elif n < 6000:
    return 'Socks'
  elif n < 6313:
    return 'Hard Working Legs'
  elif n < 6626:
    return 'Crypto Love Legs'
  elif n < 6939:
    return 'Limited Edition As You Know'
  elif n < 7252:
    return 'Monk Legs'
  elif n < 7564:
    return 'Death Metal Punk Boots'
  elif n < 7876:
    return 'Kpop Legs'
  elif n < 8188:
    return 'City Pop Legs'
  elif n < 8500:
    return 'Roller Skates'
  elif n < 8700:
    return 'Crypto Ojisan Legs'
  elif n < 8900:
    return 'Skeleton Legs'
  elif n < 9100:
    return 'Kabuki Legs'
  elif n < 9300:
    return 'Drag PVC Boots'
  elif n < 9500:
    return 'Drag Fishnet'
  elif n < 9667:
    return 'Geisha Legs'
  elif n < 9834:
    return 'Cyber Punk Legs'
  elif n < 10000:
    return 'Ghost Legs'

def getBody():
  n = random.randrange(10000)
  if n < 271:
    return 'Samurai Bod'
  elif n < 542:
    return 'Salaryman Bod'
  elif n < 813:
    return 'Yakuza Bod'
  elif n < 1094:
    return 'Insta Wife Bod'
  elif n < 1355:
    return 'School Girl Bod'
  elif n < 1626:
    return 'Sk8ter Bod'
  elif n < 1897:
    return 'Gangsta Bod'
  elif n < 2168:
    return 'Politician Bod'
  elif n < 2439:
    return 'Polite Bod'
  elif n < 2710:
    return 'Determined Bod'
  elif n < 2981:
    return 'Kinjiro Bod'
  elif n < 3252:
    return 'Casual Suit Bod'
  elif n < 3523:
    return 'Sporty Sensei Bod'
  elif n < 3794:
    return 'Footballer Bod'
  elif n < 4065:
    return 'Rugby Bod'
  elif n < 4336:
    return 'Ping Pong Bod'
  elif n < 4607:
    return 'Ghost Bod'
  elif n < 4878:
    return 'Matsuri Bod'
  elif n < 5149:
    return 'DJ Bod'
  elif n < 5420:
    return 'Prof. Saito Bod'
  elif n < 5690:
    return 'Hoodie'
  elif n < 5960:
    return 'A Walking Pea'
  elif n < 6230:
    return 'A Talking Pea'
  elif n < 6500:
    return 'A Marching Pea'
  elif n < 6727:
    return 'Sumo Bod'
  elif n < 6954:
    return 'Pinstripe Bod'
  elif n < 7181:
    return 'Monk Bod'
  elif n < 7408:
    return 'Medical Bod With Red Top'
  elif n < 7635:
    return 'Military Bod'
  elif n < 7862:
    return 'Navy Bod'
  elif n < 8089:
    return 'Barrister Bod'
  elif n < 8316:
    return 'Death Meal Punk Bod'
  elif n < 8544:
    return 'Kpop Bod'
  elif n < 8772:
    return 'Idol Bod'
  elif n < 9000:
    return 'City Pop Bod'
  elif n < 9175:
    return 'Geisha Bod'
  elif n < 9350:
    return 'Ninja Bod'
  elif n < 9525:
    return 'Cyber Punk Body Light'
  elif n < 9700:
    return 'Kabuki Bod'
  elif n < 9800:
    return 'Skeleton Bod'
  elif n < 9900:
    return 'Kappa Bod'
  elif n < 10000:
    return 'Otaku Bod'

def getMouth():
  n = random.randrange(10000)
  if n < 361:
    return 'Samurai Mouth'
  elif n < 722:
    return 'Ojisan Mouth'
  elif n < 1083:
    return 'Yakuza Mouth'
  elif n < 1444:
    return 'Enhanced Lips'
  elif n < 1805:
    return 'Standard Mouth'
  elif n < 2166:
    return 'Pink Lips'
  elif n < 2527:
    return 'Cheeky Smile'
  elif n < 2888:
    return 'Only Wise Words'
  elif n < 3249:
    return 'Sarcasm'
  elif n < 3610:
    return 'Determined Mouth'
  elif n < 3971:
    return 'Noble Smile'
  elif n < 4332:
    return 'Positive Sensei Smile'
  elif n < 4693:
    return 'Military Mouth'
  elif n < 5054:
    return 'Fully Veneered'
  elif n < 5415:
    return 'Only Speak Justice'
  elif n < 5776:
    return 'Sumo Mouth'
  elif n < 6138:
    return 'Scream'
  elif n < 6500:
    return 'Local Mouth'
  elif n < 6857:
    return 'Soft Gangsta Lips'
  elif n < 7214:
    return 'Juicy Lips'
  elif n < 7571:
    return 'Brace Smile'
  elif n < 7928:
    return 'TOT'
  elif n < 8285:
    return 'Pre Veneers'
  elif n < 8642:
    return 'Otaku Mouth'
  elif n < 9000:
    return 'Grumpy Prof. Saito'
  elif n < 9233:
    return 'Been Told Not To Say'
  elif n < 9466:
    return 'Kappa Mouth'
  elif n < 9700:
    return 'Kabuki Mouth'
  elif n < 9850:
    return 'Geisha Mouth'
  elif n < 10000:
    return 'Skeleton Mouth'

def getNose():
  n = random.randrange(10000)
  if n < 714:
    return 'Standard Nose'
  elif n < 1428:
    return 'Yakuza Nose'
  elif n < 2142:
    return 'Little Nose'
  elif n < 2856:
    return 'Littlest Nose'
  elif n < 3570:
    return 'No Filter'
  elif n < 4285:
    return 'Big And Pointy'
  elif n < 5000:
    return 'Nosy'
  elif n < 5600:
    return 'Big Man Nose'
  elif n < 6200:
    return 'Determined Nose'
  elif n < 6800:
    return 'Strong Sensei Nose'
  elif n < 7400:
    return 'Pointy And Upward'
  elif n < 8000:
    return 'Otaku Nose'
  elif n < 8375:
    return 'Major Contour Nose'
  elif n < 8750:
    return 'Noble Nose'
  elif n < 9125:
    return 'Sumo Nose'
  elif n < 9500:
    return 'Challenger Nose'
  elif n < 9667:
    return 'High Cheekbones'
  elif n < 9834:
    return 'Kappa Nose'
  elif n < 10000:
    return 'Kabuki Nose'

def getEyes():
  n = random.randrange(10000)
  if n < 387:
    return 'Samurai Eyes'
  elif n < 774:
    return 'Standard Eyes'
  elif n < 1161:
    return 'Natural Lash Eyes'
  elif n < 1548:
    return 'Difficult But Warm Eyes'
  elif n < 1935:
    return 'Pretty But Tired Eyes'
  elif n < 2322:
    return 'Determined Eyes'
  elif n < 2709:
    return 'Noble Eyes'
  elif n < 3096:
    return 'Raised Brow'
  elif n < 3483:
    return 'No Judgement'
  elif n < 3870:
    return 'Military Eyes'
  elif n < 4256:
    return 'Not In A Good Mood'
  elif n < 4642:
    return 'Sharp Look'
  elif n < 5028:
    return 'Local Eyes'
  elif n < 5414:
    return 'Idol Eyes'
  elif n < 5800:
    return 'Sumo Eyes'
  elif n < 6122:
    return 'City Pop Eyes'
  elif n < 6444:
    return 'Kpop Eyes'
  elif n < 6766:
    return 'Ojisan Eyes'
  elif n < 7088:
    return 'Yakuza Eyes'
  elif n < 7410:
    return 'Georgina Eyes'
  elif n < 7732:
    return 'Wealth Attraction'
  elif n < 8054:
    return 'Beaten Eyes'
  elif n < 8377:
    return 'Otaku Eyes'
  elif n < 8700:
    return 'Baby Pumpkin Eyes'
  elif n < 8967:
    return 'Gangsta Eyes'
  elif n < 9234:
    return 'Kappa Eyes'
  elif n < 9500:
    return 'Kabuki Eyes'
  elif n < 9667:
    return 'Geisha Eyes'
  elif n < 9834:
    return 'Ghost Eyes'
  elif n < 10000:
    return 'Tired Prof. Saito Eyes'

def getAttitude():
  n = random.randrange(10000)
  if n < 250:
    return 'Having A Puff'
  elif n < 500:
    return 'Puff And Scars'
  elif n < 750:
    return 'Husbands Credit Card'
  elif n < 1000:
    return 'Rosy Cheeks'
  elif n < 1250:
    return 'Skateboard'
  elif n < 1500:
    return 'Shiny Peas'
  elif n < 1750:
    return 'Powerful Salute'
  elif n < 2000:
    return 'Up For A Slice'
  elif n < 2250:
    return 'Ninja Shuriken'
  elif n < 2500:
    return 'Greetings'
  elif n < 2750:
    return 'Peas Vs Humans'
  elif n < 3000:
    return 'Proper Salute'
  elif n < 3250:
    return 'Onigiri Rice Ball'
  elif n < 3500:
    return 'Just Some Scratches'
  elif n < 3750:
    return 'Hitodama'
  elif n < 4000:
    return 'Matsuri Thingy'
  elif n < 4250:
    return 'Idol Peace'
  elif n < 4500:
    return "Let’s Go"
  elif n < 4750:
    return 'Breezy'
  elif n < 5000:
    return 'Cocktail'
  elif n < 5250:
    return 'Green Tea'
  elif n < 5500:
    return 'Chopsticks'
  elif n < 5750:
    return 'Mask X'
  elif n < 6000:
    return 'Medical Mask'
  elif n < 6233:
    return 'Otaku Backpack'
  elif n < 6466:
    return 'That Fucking Husband'
  elif n < 6700:
    return 'Skeleton Greetings'
  elif n < 6933:
    return 'Okame L2 Mask'
  elif n < 7166:
    return 'Cheeky Okame Mask'
  elif n < 7400:
    return 'Kitsune Mask'
  elif n < 7633:
    return 'Maneki Neko Mask'
  elif n < 7866:
    return 'Gimp Mask Black'
  elif n < 8100:
    return 'Gimp Mask Red'
  elif n < 8333:
    return 'LGBTQ Flag'
  elif n < 8566:
    return 'Peace Flag'
  elif n < 8800:
    return 'Rebel For Life Flag'
  elif n < 9000:
    return 'Death Metal Punk Mask'
  elif n < 9200:
    return 'LOVE U'
  elif n < 9400:
    return 'Punched Face'
  elif n < 9600:
    return 'Smol Face'
  elif n < 9800:
    return 'VR Goggles'
  elif n < 9900:
    return 'Geisha Umbrella'
  elif n < 10000:
    return 'Cyber Punk Face'

def getBadge():
  n = random.randrange(100)
  if n < 2:
    return 'Key Citizen Badge'
  else:
    return None

def getHair():
  n = random.randrange(10000)
  if n < 271:
    return 'Straw Hat'
  elif n < 542:
    return 'Straightened Damaged Hair'
  elif n < 813:
    return 'Beret'
  elif n < 1094:
    return 'Dirty Money Hat'
  elif n < 1355:
    return 'Noble Hair'
  elif n < 1626:
    return 'Gold Standard 7-3 Parting Hair'
  elif n < 1897:
    return 'Fly'
  elif n < 2168:
    return 'Soft Hair'
  elif n < 2439:
    return 'Strong Sensei Hair'
  elif n < 2710:
    return 'That Famous Long Hair'
  elif n < 2981:
    return 'Nice Smelling Hair'
  elif n < 3252:
    return 'Challenger Hair'
  elif n < 3523:
    return 'Edo Headband'
  elif n < 3794:
    return 'Green Fluff'
  elif n < 4065:
    return 'Idol Hair'
  elif n < 4336:
    return 'Visual Kei'
  elif n < 4607:
    return 'Joe Hair'
  elif n < 4878:
    return 'Blonde Sided Hair'
  elif n < 5149:
    return 'Pig Tails'
  elif n < 5420:
    return 'Ginza Hat'
  elif n < 5690:
    return 'Daikanyama Hat'
  elif n < 5960:
    return 'Roppongi Hat'
  elif n < 6230:
    return 'Odaiba Hat'
  elif n < 6500:
    return 'Ikebukuro Hat'
  elif n < 6667:
    return 'Major Comb Over'
  elif n < 6834:
    return 'Marunouchi Hat'
  elif n < 7000:
    return 'Sun Visor'
  elif n < 7167:
    return 'Samurai Hair'
  elif n < 7334:
    return 'Monk Hat'
  elif n < 7500:
    return 'Military Hat'
  elif n < 7667:
    return 'Navy Hat'
  elif n < 7834:
    return 'Sumo Hair'
  elif n < 8000:
    return 'Ping Pong Ready'
  elif n < 8167:
    return 'City Pop Hair'
  elif n < 8334:
    return 'Otaku Pony'
  elif n < 8500:
    return 'Punk Red Mohican'
  elif n < 8667:
    return 'Punk Green Mohican'
  elif n < 8834:
    return 'Dreadlocks'
  elif n < 9000:
    return 'Lost Property'
  elif n < 9175:
    return 'That Barrister Thingy'
  elif n < 9350:
    return 'Leaf On Head'
  elif n < 9525:
    return 'Rockabilly'
  elif n < 9700:
    return 'Turban Hair'
  elif n < 9800:
    return 'Maiko San Hair'
  elif n < 9900:
    return 'Ghost Hair'
  elif n < 10000:
    return 'Cosplay Hair'
  
def getArm():
  n = random.randrange(10000)
  if n < 333:
    return 'Samurai Sword'
  elif n < 666:
    return 'Tattooed Arm'
  elif n < 1000:
    return 'Standard Arm'
  elif n < 1333:
    return 'School Bag'
  elif n < 1666:
    return 'Low Battery Watch'
  elif n < 2000:
    return 'Doctors Bag'
  elif n < 2333:
    return 'Rugby Arm'
  elif n < 2666:
    return 'Ping Pong Arm'
  elif n < 3000:
    return 'Matsuri Fan Arm'
  elif n < 3333:
    return 'Singer Arm'
  elif n < 3666:
    return 'Otaku Treasure'
  elif n < 4000:
    return 'Walkieman'
  elif n < 4333:
    return 'Game Controller'
  elif n < 4666:
    return 'Gameboi'
  elif n < 5000:
    return 'Electric Guitar'
  elif n < 5333:
    return 'Guitar'
  elif n < 5666:
    return 'Medical Kit'
  elif n < 6000:
    return 'Maiko San Bag'
  elif n < 6250:
    return 'Jolly Expensive Arm'
  elif n < 6500:
    return 'Fine Gold 1000G'
  elif n < 6750:
    return 'Officials Trumpet'
  elif n < 7000:
    return 'Monk Kit'
  elif n < 7250:
    return 'Pilot Mask'
  elif n < 7500:
    return 'Wheel'
  elif n < 7750:
    return 'Toting Dead Fish'
  elif n < 8000:
    return 'Sack Of ETH'
  elif n < 8250:
    return 'Sack Of BTC'
  elif n < 8500:
    return 'Sack Of XTZ'
  elif n < 8667:
    return 'Geisha Fan'
  elif n < 8834:
    return 'Hardest Workers Arm'
  elif n < 9000:
    return 'Skeleton Arm'
  elif n < 9167:
    return 'Baby Calf Bag'
  elif n < 9334:
    return 'Human Bag'
  elif n < 9500:
    return 'Leave No Trace At All'
  elif n < 9600:
    return 'Walkie With A Cat'
  elif n < 9700:
    return 'Walkie Time But This Cat'
  elif n < 9800:
    return 'Walkie With A Dog'
  elif n < 9900:
    return 'Walkie Time But This Dog'
  elif n < 10000:
    return 'Walkie With A Ferret'

if __name__ == '__main__':
  for i in range(count):
    bkgFileName = getBackground()
    legsFileName = getLegs()
    bodyFileName = getBody()
    mouthFileName = getMouth()
    noseFileName = getNose()
    eyesFileName = getEyes()
    attitudeFileName = getAttitude()
    badgeFileName = getBadge()
    hairFileName = getHair()
    armFileName = getArm()
    flag = False
    try:
      file = open("temp.txt", 'r')
      Lines = file.readlines()
      file.close()
      writeString = "(%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s)\n" % (bkgFileName, legsFileName, bodyFileName, mouthFileName, noseFileName, eyesFileName, attitudeFileName, badgeFileName, hairFileName, armFileName)
      for line in Lines:
        if line == writeString:
          flag = True
          break  
    except IOError:
      print("Error: File does not appear to exist.")
    if flag == False:
      f = open("temp.txt", "w")
      f.write("(%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s) (%s)\n" % (bkgFileName, legsFileName, bodyFileName, mouthFileName, noseFileName, eyesFileName, attitudeFileName, badgeFileName, hairFileName, armFileName))
      f.close()
      mergeImageAndSave(i, bkgFileName, legsFileName, bodyFileName, mouthFileName, noseFileName, eyesFileName, attitudeFileName, badgeFileName, hairFileName, armFileName)
  # bkgFileName = 'Goma'
  # legsFileName = 'Skeleton Legs'
  # bodyFileName = 'Kabuki Bod'
  # mouthFileName = 'Enhanced Lips'
  # noseFileName = 'High Cheekbones'
  # eyesFileName = 'Difficult But Warm Eyes'
  # attitudeFileName = 'Maneki Neko Mask'
  # badgeFileName = None
  # hairFileName = 'Cosplay Hair'
  # armFileName = 'Electric Guitar'
  # mergeImageAndSave(16, bkgFileName, legsFileName, bodyFileName, mouthFileName, noseFileName, eyesFileName, attitudeFileName, badgeFileName, hairFileName, armFileName)


