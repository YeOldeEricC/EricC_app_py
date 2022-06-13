def colour_set(colour_tag) :
	tag_list = ['dark','light'];
	colours = {
		'dark' : '#110f14',
		'light' : '#dcdcdc',
	};
	if colour_tag not in tag_list :
		return colours['dark'];
	else :
		return colours[str(colour_tag)];