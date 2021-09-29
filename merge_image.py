# import PIL module
from PIL import Image

psdFileName = 'PeaBot Skin 1'
rarityFileName = 'rarity1.txt'

def getLegImagePos(legsFileName):
	filepath = './Assets/Legs/' + legsFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getBodyImagePos(bodyFileName):
	filepath = './Assets/Body/face/' + bodyFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getMouthImagePos(mouthFileName):
	filepath = './Assets/Mouth/' + mouthFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getNoseImagePos(noseFileName):
	filepath = './Assets/Nose/' + noseFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getEyesImagePos(eyesFileName):
	filepath = './Assets/Eyes/Brows/' + eyesFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getAttitudeImagePos(attitudeFileName):
	filepath = './Assets/Attitude/' + attitudeFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getBadgeImagePos(badgeFileName):
	filepath = './Assets/Badge/' + badgeFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getHairImagePos(hairFileName):
	filepath = './Assets/Hair Accessory/' + hairFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getArmImagePos(armFileName):
	filepath = './Assets/Arm/' + armFileName + '.png'
	file = open(rarityFileName, 'r')
	Lines = file.readlines()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)
	
		
def mergeImageAndSave(id, bkgFileName, legsFileName, bodyFileName, mouthFileName, noseFileName, eyesFileName, attitudeFileName, badgeFileName, hairFileName, armFileName):
	file_bkg = f'Assets/{psdFileName}/Katakana/{bkgFileName}.png'
	file_legs = f'Assets/{psdFileName}/Legs/{legsFileName}.png'
	file_body = f'Assets/{psdFileName}/Body/face/{bodyFileName}.png'
	file_mouth = f'Assets/{psdFileName}/Mouth/{mouthFileName}.png'
	file_nose = f'Assets/{psdFileName}/Nose/{noseFileName}.png'
	file_eyes = f'Assets/{psdFileName}/Eyes/Brows/{eyesFileName}.png'
	file_attitude = f'Assets/{psdFileName}/Attitude/{attitudeFileName}.png'
	if badgeFileName != None:
		file_badge = f'Assets/{psdFileName}/Badge/{badgeFileName}.png'
	file_hair = f'Assets/{psdFileName}/Hair Accessory/{hairFileName}.png'
	file_arm = f'Assets/{psdFileName}/Arm/{armFileName}.png'
	
	img_bkg = Image.open(file_bkg).convert("RGBA")
	img_legs = Image.open(file_legs).convert("RGBA")
	img_body = Image.open(file_body).convert("RGBA")
	img_mouth = Image.open(file_mouth).convert("RGBA")
	img_nose = Image.open(file_nose).convert("RGBA")
	img_eyes = Image.open(file_eyes).convert("RGBA")
	img_attitude = Image.open(file_attitude).convert("RGBA")
	if badgeFileName != None:
		img_badge = Image.open(file_badge).convert("RGBA")
	img_hair = Image.open(file_hair).convert("RGBA")
	img_arm = Image.open(file_arm).convert("RGBA")

	tx, ty = getLegImagePos(legsFileName)
	img_bkg.paste(img_legs, (tx, ty), img_legs)

	tx, ty = getBodyImagePos(bodyFileName)
	img_bkg.paste(img_body, (tx, ty), img_body)

	tx, ty = getMouthImagePos(mouthFileName)
	img_bkg.paste(img_mouth, (tx, ty), img_mouth)

	tx, ty = getNoseImagePos(noseFileName)
	img_bkg.paste(img_nose, (tx, ty), img_nose)

	tx, ty = getEyesImagePos(eyesFileName)
	img_bkg.paste(img_eyes, (tx, ty), img_eyes)

	tx, ty = getAttitudeImagePos(attitudeFileName)
	img_bkg.paste(img_attitude, (tx, ty), img_attitude)

	if badgeFileName != None:
		tx, ty = getBadgeImagePos(badgeFileName)
		img_bkg.paste(img_badge, (tx, ty), img_badge)
	
	tx, ty = getHairImagePos(hairFileName)
	img_bkg.paste(img_hair, (tx, ty), img_hair)

	tx, ty = getArmImagePos(armFileName)
	img_bkg.paste(img_arm, (tx, ty), img_arm)
	
	img_bkg.save(f"GeneratedImages/new_{id}.png", format="png")

	

# def mergeImageAndSave1(image_idx, flag_name, eye, glass, mask, mouth, nose, access, hat):
# 	# Front Image
# 	file_flag = f'assets/CountryFlags/{flag_name}.png'
# 	file_eye = f'assets/Eyes/{eye}.png'
# 	file_glass = f'assets/Glasses/{glass}.png'
# 	file_mask = f'assets/Masks/{mask}.png'
# 	file_mouth = f'assets/Mouths/{mouth}.png'
# 	file_nose = f'assets/Noses/{nose}.png'
# 	file_access = f'assets/Accessories/{access}.png'
# 	file_hat = f'assets/Hats/{hat}.png'
	
# 	img_flag = Image.open(file_flag).convert("RGBA")
# 	img_eye = Image.open(file_eye).convert("RGBA")
# 	img_mouth = Image.open(file_mouth).convert("RGBA")

# 	img_flag.paste(img_eye, (0, 0), img_eye)
# 	img_flag.paste(img_mouth, (0, 0), img_mouth)

# 	if(glass != 0):
# 		img_glass = Image.open(file_glass).convert("RGBA")
# 		img_flag.paste(img_glass, (0, 0), img_glass)

# 	if(mask != 0):
# 		img_mask = Image.open(file_mask).convert("RGBA")
# 		img_flag.paste(img_mask, (0, 0), img_mask)

# 	if(nose != 0):
# 		img_nose = Image.open(file_nose).convert("RGBA")
# 		img_flag.paste(img_nose, (0, 0), img_nose)

# 	if(access != 0):
# 		img_access = Image.open(file_access).convert("RGBA")
# 		img_flag.paste(img_access, (0, 0), img_access)

# 	if(hat != 0):
# 		img_hat = Image.open(file_hat).convert("RGBA")
# 		img_flag.paste(img_hat, (0, 0), img_hat)

# 	# Save this image
# 	img_flag.save(f"GeneratedImages/new_{image_idx}.png", format="png")