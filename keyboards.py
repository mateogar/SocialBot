#-*. coding: utf-8 -*-
#authors: David Quesada López y Mateo García Fuentes
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import db
import translate
		
#Este inline no se está usando		
afterRate = InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text='Choose location', callback_data='init')],
					[InlineKeyboardButton(text="Choose type of establishments", callback_data='type')],
					[InlineKeyboardButton(text='Choose establishment', callback_data='establishment')],	
               ])#Volver a puntuacion, fotos etc


#KeyboardMarkups
def markupLocation(lang):
	text = translate.markupLocation(lang)
	return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=text[0], request_location=True)],[KeyboardButton(text=text[1])]], resize_keyboard=True, one_time_keyboard=True)

#InlineKeyboards
def settings(lang):
	text = translate.settingsBoard(lang)
	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text=text[0], callback_data='language')],
					[InlineKeyboardButton(text=text[1], callback_data='parameters')],
					[InlineKeyboardButton(text=text[2], callback_data='back')],	
               ])

def inlineEstablishment(lang):
	text = translate.inlineEstablishment(lang)
	return InlineKeyboardMarkup(inline_keyboard=[
                   	[InlineKeyboardButton(text=text[0], callback_data='bar')] + [InlineKeyboardButton(text=text[1], callback_data='cafe')],
					[InlineKeyboardButton(text=text[2], callback_data='food')]+ [InlineKeyboardButton(text=text[3], callback_data='night_club')],
					[InlineKeyboardButton(text=text[4], callback_data='restaurant')], [InlineKeyboardButton(text=text[5], callback_data='back')],
               ])

def inlineBack(lang):
	text = translate.back(lang)
	return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, callback_data='back')],])
	
def languages(lang):
	text = translate.back(lang)
	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text="English", callback_data='language English')]+[InlineKeyboardButton(text="Español", callback_data='language Espanol')],
					[InlineKeyboardButton(text=text, callback_data='sback')],	
               ])

def parameters(lang):
	text = translate.parameters(lang)
 	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text=text[0], callback_data='radius')],
					[InlineKeyboardButton(text=text[1], callback_data='price')],
					[InlineKeyboardButton(text=text[2], callback_data='open')],
					[InlineKeyboardButton(text=text[3], callback_data='sback')],	
               ])
               
def radius(lang):
	text = translate.back(lang)
	InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text='100', callback_data='meters 100')] + [InlineKeyboardButton(text='250', callback_data='meters 250')] + [InlineKeyboardButton(text='500', callback_data='meters 500')],
		[InlineKeyboardButton(text='1000', callback_data='meters 1000')] + [InlineKeyboardButton(text='2500', callback_data='meters 2500')] + [InlineKeyboardButton(text='5000', callback_data='meters 5000')], [InlineKeyboardButton(text=text, callback_data='sback')]])
               
def openE(lang):  
	text = translate.openE(lang)     
	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text=text[0], callback_data='bool true')]+[InlineKeyboardButton(text=text[1], callback_data='bool false')],
					[InlineKeyboardButton(text=text[2], callback_data='sback')],	
               ])      
               
def numE(lang):  
	text = translate.back(lang) 
	return InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text='5', callback_data='num 5')] + [InlineKeyboardButton(text='10', callback_data='num 10')],
		[InlineKeyboardButton(text='15', callback_data='num 15')] + [InlineKeyboardButton(text='20', callback_data='num 20')], 	
		[InlineKeyboardButton(text=text, callback_data='sback')]])   
		
def optionChanged(lang):  
	text = translate.optionChanged(lang) 
	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text=text[0], callback_data='sback')],
					[InlineKeyboardButton(text=text[1], callback_data='restart')],	
               ])       
               
def rating(lang):  
	text = translate.back(lang) 
	return InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text='0'+u'\u2b50\ufe0f', callback_data='0')] + [InlineKeyboardButton(text='1'+u'\u2b50\ufe0f', callback_data='1')] + [InlineKeyboardButton(text='2'+u'\u2b50\ufe0f', callback_data='2')],
		[InlineKeyboardButton(text='3'+u'\u2b50\ufe0f', callback_data='3')] + [InlineKeyboardButton(text='4'+u'\u2b50\ufe0f', callback_data='4')] + [InlineKeyboardButton(text='5'+u'\u2b50\ufe0f', callback_data='5')], [InlineKeyboardButton(text=text, callback_data='back')]])                 
		
		                   
def resultsKeyboard(resultList, lang, pos, lim):
	"""Keyboard that displays the results of a location query."""
	i = 0
	num = 0
	row = [] 
	keyboardRestaurant= []
	while (num < lim) and (pos < len(resultList)):
		lat = resultList[pos]["geometry"]["location"]["lat"]
		lng = resultList[pos]["geometry"]["location"]["lng"]
		loc = str(lat) + " " + str(lng)
		name = resultList[pos]["name"]
		if len(name) > 15:			
			i = -1
			keyboardRestaurant.append(row)
			row = [InlineKeyboardButton(text=name, callback_data=loc)]
			keyboardRestaurant.append(row)
			row = []
		elif i == 2:
			i = 0
			keyboardRestaurant.append(row)
			row = [InlineKeyboardButton(text=name, callback_data=loc)]
		else:
			row = row + [InlineKeyboardButton(text=name, callback_data=loc)]
		i += 1
		pos += 1
		num += 1
	keyboardRestaurant.append(row)
	text = translate.rkeyboard(lang)
	row = []
	if pos > lim:
		row = [InlineKeyboardButton(text=text[0], callback_data='previous')]
	if pos < len(resultList):
		row += [InlineKeyboardButton(text=text[1], callback_data='more')]
	if row != []:
		keyboardRestaurant.append(row)	
	row = [InlineKeyboardButton(text=text[2], callback_data='back')]
	keyboardRestaurant.append(row)
	markupRestaurant = InlineKeyboardMarkup(inline_keyboard = keyboardRestaurant)
	
	return markupRestaurant

def optionsKeyboard(loc, lang):
	"""Keyboard that shows the posible options for a displayed place."""
	kboard = []
	info = db.getPlaceData(loc)
	text = translate.optionsKeyboard(lang)
	loc = str(loc[0]) + " " + str(loc[1])
	res = [InlineKeyboardButton(text=text[0], callback_data="rating " + loc)] + [InlineKeyboardButton(text=text[1], callback_data="photo " + loc)]
	kboard.append(res)
	if info != None:
		if 'photos' in info:
			res = [InlineKeyboardButton(text=text[2], callback_data="show_photos " + loc)]	
			kboard.append(res)
	res = [InlineKeyboardButton(text=text[3], callback_data='back')]
	kboard.append(res)
	markupOptions = InlineKeyboardMarkup(inline_keyboard = kboard)
	return markupOptions
	
def photos(info, pos, lang):
	kboard = []
	res = []
	text = translate.photos(lang)
	if pos > 0:
		res = [InlineKeyboardButton(text=text[0], callback_data=str(pos-1))]
	if pos+1 < len(info['photos']):
		res += [InlineKeyboardButton(text=text[1], callback_data=str(pos+1))]
	kboard.append(res)
	res = [InlineKeyboardButton(text=text[2], callback_data='back')]
	kboard.append(res)
	markupPhotos = InlineKeyboardMarkup(inline_keyboard = kboard)
	return markupPhotos
	
def afterMap(lang):
	text = translate.optionChanged(lang)   
	return InlineKeyboardMarkup(inline_keyboard=[
					[InlineKeyboardButton(text=text[0], callback_data='settings')],
					[InlineKeyboardButton(text=text[1], callback_data='start')],	
               ])

