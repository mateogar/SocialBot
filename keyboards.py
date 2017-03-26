#-*. coding: utf-8 -*-
#authors: David Quesada López y Mateo García Fuentes
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import db

#KeyboardMarkups
markupLocation = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Location', request_location=True)],], resize_keyboard=True, one_time_keyboard=True)

#InlineKeyboards
inlineEstablishment = InlineKeyboardMarkup(inline_keyboard=[
                   	[InlineKeyboardButton(text='Bar', callback_data='bar')] + [InlineKeyboardButton(text='Cafe', callback_data='cafe')],
					[InlineKeyboardButton(text='Food', callback_data='food')]+ [InlineKeyboardButton(text='Night club', callback_data='night_club')],
					[InlineKeyboardButton(text='Restaurant', callback_data='restaurant')], [InlineKeyboardButton(text='Back', callback_data='back')],
               ])
inlineBack = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Back', callback_data='back')],])


# Keyboard that displays the results of a location query
def resultsKeyboard(js):
	i = 0
	row = [] 
	keyboardRestaurant= []
	for j in js["results"]:
		loc = str(j["geometry"]["location"]["lat"]) + " " + str(j["geometry"]["location"]["lng"])
		if len(j["name"]) > 15:
			i = 0
			keyboardRestaurant.append(row)
			row = [InlineKeyboardButton(text=j["name"], callback_data=loc)]
			keyboardRestaurant.append(row)
			row = []
		elif i == 2:
			i = 0
			keyboardRestaurant.append(row)
			row = [InlineKeyboardButton(text=j["name"], callback_data=loc)]
		else:
			row = row + [InlineKeyboardButton(text=j["name"], callback_data=loc)]
		i += 1
	row = [InlineKeyboardButton(text='Back', callback_data='back')]
	keyboardRestaurant.append(row)
	markupRestaurant = InlineKeyboardMarkup(inline_keyboard = keyboardRestaurant)
	
	return markupRestaurant

# Keyboard that shows the posible options for a displayed place
def optionsKeyboard(loc):
	data = db.getPlaceData(loc)
	#cb = str(loc["lat"]) + " " + str(loc["lng"])
	res = [InlineKeyboardButton(text="Rate it", callback_data="rating")] + [InlineKeyboardButton(text="Send a photo", callback_data=loc)]
	res = res + [InlineKeyboardButton(text='Back', callback_data='back')]
	#if data != None:
	markupOptions = InlineKeyboardMarkup(inline_keyboard = [res])
	return markupOptions
	