# this will be the mass library of functions that
# could/will be used in the app

# OPENER/LOADER, PARSER AND CONVERTER FOR FORMATTED TXT
#
# Notes + info for the text file formatting & manipulation
#
# ## TXT FILE TAGSET ##
# DOC = [? ... ?] // document tag -- this is only a maybe
# MAJ = [# ... #] // major tag
# MIN = [= ... =] // minor/detail tag
# COM = [- ... -] // comment tag -- haven't yet had any need of it
#
# ## MAJOR TAGS ##
# TTL 			- title
# HDR 			- header
# TXT 			- text
# EQN 			- equation
# REF 			- references
# PLT 			- plot
# IMG 			- image
# CODE 			- code (monospaced font)
# CODE/LANG 		- code w/ syntax highlighting for language
# END 			- end of article
# AUTH 			- author article was written by
# DATE 			- date of article writing -- date after author name
# SEARCH_TERMS 	- relevent search terms of article -- these at end
# ________________________________________________________
# -- note: all above END are 'within' article tags, rest  |
# --       are for authoring info and search parameters.  |
# --													  |
# --   so: if END used in wrong place, need to produce 	  |
# --       an error message saying as such.				  |
# ________________________________________________________|
#
# ## MINOR/DETAIL TAGS ##
# PS 				- paragraph separator

def txt_parser(str_in) :
	tagset = {
		tag_types: {
			T_S: "[",
			T_E: "]",
			COM: "-",
			DOC: "?",
			MAJ: "#",
			MIN: "=",
			SEP: " "
		},
		DOC: {
			tmp: "..."
		},
		MAJ: {
			title: "TTL",
			header: "HDR",
			text: "TXT",
			equation: "EQN",
			references: "REF",
			plot: "PLT",
			image: "IMG",
			code: "CODE",
			code_w_lang: "CODE/",
			end: "END",
			author: "AUTH",
			date: "DATE",
			search_terms: "SEARCH_TERMS"
		},
		MIN: {
			para_sep: "PS"
		}
	};

	return 0;

def make_huffman_code(str_in) :
	return 0;

def huffman_encode_str(huffman_code, str_in) :
	return 0;

def re_encode_bin(bin_str_in) :
	return 0;