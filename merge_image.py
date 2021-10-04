# import PIL module
from PIL import Image

psdFileName = 'PeaBot Skin 3'
rarityFileName = 'rarity3.txt'

def getLegImagePos(legsFileName):
	filepath = './Assets/Legs/' + legsFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getBodyImagePos(bodyFileName):
	filepath = './Assets/Body/face/' + bodyFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getMouthImagePos(mouthFileName):
	filepath = './Assets/Mouth/' + mouthFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getNoseImagePos(noseFileName):
	filepath = './Assets/Nose/' + noseFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getEyesImagePos(eyesFileName):
	filepath = './Assets/Eyes/Brows/' + eyesFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getAttitudeImagePos(attitudeFileName):
	filepath = './Assets/Attitude/' + attitudeFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getBadgeImagePos(badgeFileName):
	filepath = './Assets/Badge/' + badgeFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getHairImagePos(hairFileName):
	filepath = './Assets/Hair Accessory/' + hairFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
	for line in Lines:
		if filepath in line:
			newstr = line.replace("(" + filepath + ")", '')
			tx = newstr.split()[0]
			ty = newstr.split()[1]
			return int(tx), int(ty)

def getArmImagePos(armFileName):
	filepath = './Assets/Arm/' + armFileName + '.png'
	file = open(rarityFileName, 'r', encoding='utf-8')
	Lines = file.readlines()
	file.close()
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
	img_legs_mask = Image.open(file_legs).convert("RGBA")
	img_legs = Image.open(file_legs).convert("RGB")
	img_body_mask = Image.open(file_body).convert("RGBA")
	img_body = Image.open(file_body).convert("RGB")
	img_mouth_mask = Image.open(file_mouth).convert("RGBA")
	img_mouth = Image.open(file_mouth).convert("RGB")
	img_nose_mask = Image.open(file_nose).convert("RGBA")
	img_nose = Image.open(file_nose).convert("RGB")
	img_eyes_mask = Image.open(file_eyes).convert("RGBA")
	img_eyes = Image.open(file_eyes).convert("RGB")
	img_attitude_mask = Image.open(file_attitude).convert("RGBA")
	img_attitude = Image.open(file_attitude).convert("RGB")
	if badgeFileName != None:
		img_badge_mask = Image.open(file_badge).convert("RGBA")
		img_badge = Image.open(file_badge).convert("RGB")
	img_hair_mask = Image.open(file_hair).convert("RGBA")
	img_hair = Image.open(file_hair).convert("RGB")
	img_arm_mask = Image.open(file_arm).convert("RGBA")
	img_arm = Image.open(file_arm).convert("RGB")

	tx, ty = getLegImagePos(legsFileName)
	img_bkg.paste(img_legs, (tx, ty), img_legs_mask)

	tx, ty = getBodyImagePos(bodyFileName)
	img_bkg.paste(img_body, (tx, ty), img_body_mask)

	tx, ty = getMouthImagePos(mouthFileName)
	img_bkg.paste(img_mouth, (tx, ty), img_mouth_mask)


	tx, ty = getNoseImagePos(noseFileName)
	img_bkg.paste(img_nose, (tx, ty), img_nose_mask)

	tx, ty = getEyesImagePos(eyesFileName)
	img_bkg.paste(img_eyes, (tx, ty), img_eyes_mask)

	tx, ty = getAttitudeImagePos(attitudeFileName)
	img_bkg.paste(img_attitude, (tx, ty), img_attitude_mask)

	if badgeFileName != None:
		tx, ty = getBadgeImagePos(badgeFileName)
		img_bkg.paste(img_badge, (tx, ty), img_badge_mask)
	
	tx, ty = getHairImagePos(hairFileName)
	img_bkg.paste(img_hair, (tx, ty), img_hair_mask)

	tx, ty = getArmImagePos(armFileName)
	img_bkg.paste(img_arm, (tx, ty), img_arm_mask)
	
	img_bkg.save(f"GeneratedImages/new_{id}.png", format="png")