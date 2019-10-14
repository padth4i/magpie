#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__vowels = {
	"അ": "a", "ആ": "ā", "ഇ": "i", "ഈ": "ī", "ഉ": "u", "ഊ": "ū", "ഋ": "ṛu",
	"എ": "e", "ഏ": "ē", "ഐ": "ai", "ഒ": "o", "ഓ": "ō", "ഔ": "au"
}

__compounds = {
	"ക്ക": "kk", "ഗ്ഗ": "gg", "ങ്ങ": "ṅṅ",
	"ക്ക": "kk", "ച്ച": "cc", "ജ്ജ": "jj", "ഞ്ഞ": "ññ",
	"ട്ട": "ṭṭ", "ണ്ണ": "ṇṇ",
	"ത്ത": "tt", "ദ്ദ": "dd", "ദ്ധ": "d'dh", "ന്ന": "nn",
	"ന്ത": "nt", "ങ്ക": "ṅk", "ണ്ട": "nd", "ബ്ബ": "bb",
	"പ്പ": "pp", "മ്മ": "mm",
	"യ്യ": "yy", "ല്ല": "ll", "വ്വ": "vv", "ശ്ശ": "s'sh", "സ്സ": "s's",
	"ക്സ": "ks", "ഞ്ച": "ñc", "ക്ഷ": "kṣ", "മ്പ": "mp", "റ്റ": "ṟṟ", "ന്റ": "nṟ", "ന്ത": "nt",
	"ന്ത്യ": "nty"
}

__consonants = {
	"ക": "k", "ഖ": "kh", "ഗ": "g", "ഘ": "gh", "ങ": "ṅ",
	"ച": "c", "ഛ": "ch", "ജ": "j", "ഝ": "jh", "ഞ": "ñ",
	"ട": "ṭ", "ഠ": "ṭh", "ഡ": "ḍ", "ഢ": "ḍh", "ണ": "ṇ",
	"ത": "t", "ഥ": "th", "ദ": "d", "ധ": "dh", "ന": "n",
	"പ": "p", "ഫ": "ph", "ബ": "b", "ഭ": "bh", "മ": "m",
	"യ": "y", "ര": "r", "ല": "l", "വ": "v",
	"ശ": "ś", "ഷ": "ṣ", "സ": "s","ഹ": "h",
	"ള": "ḷ", "ഴ": "ḻ", "റ": "ṟ"
}

__chil = {
	"ൽ": "l", "ൾ": "ḷ", "ൺ": "ṇ",
	"ൻ": "n", "ർ": "r", "ൿ": "k"
}

__modifiers = {
	"ു്": "u", "ാ": "ā", "ി": "i", "ീ": "ī",
	"ു": "u", "ൂ": "ū", "ൃ": "ṛ",
	"െ": "e", "േ": "ē", "ൈ": "ai",
	"ൊ": "o", "ോ": "ō","ൌ": "au", "ൗ": "au",
	"ഃ": "ḥ", "്യ": "ya"
}


# ______ transliterate a malayalam string to english phonetically
def transliterate(input):
	# replace zero width non joiners
	input = re.sub(r'\xE2\x80\x8C', '', input)
		# replace modified compounds first
	input = _replaceModifiedGlyphs(__compounds, input)
		# replace modified non-compounds
	input = _replaceModifiedGlyphs(__vowels, input)
	input = _replaceModifiedGlyphs(__consonants, input)

	v = ''
	# replace unmodified compounds
	for k, v in __compounds.items():
		input = re.sub( k + '്([\\w])', v + '\1', input )	# compounds ending in chandrakkala but not at the end of the word
		input = input.replace( k + '്', v + 'u' )	# compounds ending in chandrakkala have +'u' pronunciation
		input = input.replace( k, v + 'a' )	# compounds not ending in chandrakkala have +'a' pronunciation

	# glyphs not ending in chandrakkala have +'a' pronunciation
	for k, v in __consonants.items():
		input = re.sub( k + '(?!്)', v + 'a', input )

	# glyphs ending in chandrakkala not at the end of a word
	for k, v in __consonants.items():
		input = re.sub( k + "്(?![\\s\)\.;,\"'\/\\\%\!])", v, input )

	# remaining glyphs ending in chandrakkala will be at end of words and have a +'u' pronunciation
	for k, v in __consonants.items():
		input = input.replace( k + "്", v + 'u' )

	# remaining consonants
	for k, v in __consonants.items():
		input = input.replace( k, v )

	# vowels
	for k, v in __vowels.items():
		input = input.replace( k, v )

	# chillu glyphs
	for k, v in __chil.items():
		input = input.replace( k, v )

	# anusvaram 'am' at the end
	input = input.replace( 'ം', 'ṁ')

	# replace any stray modifiers that may have been left out
	for k, v in __modifiers.items():
		input = input.replace( k, v )

	return input

# ______ replace modified glyphs
def _replaceModifiedGlyphs(glyphs, input):

	# see if a given set of glyphs have modifiers trailing them
	exp = re.compile( '((' + '|'.join(glyphs.keys()) + ')(' + '|'.join(__modifiers.keys()) + '))' )
	matches = exp.findall(input)

	# if yes, replace the glpyh with its roman equivalent, and the modifier with its
	if matches != None:
		for match in matches:
			input = input.replace( match[0], glyphs[match[1]] + __modifiers[ match[2] ]);

	return input

mal = input()
print(transliterate(mal))

