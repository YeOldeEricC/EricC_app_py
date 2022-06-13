# get dir of proj
import pathlib,os;
DIR = str(pathlib.Path().resolve());

# import the txt file + data
FILE_IN = open('%s/tmp/txt_test.txt' % DIR,'r');
DATA = FILE_IN.readlines();
FILE_IN.close();

# print(DATA);
TO_JS = '';
for ln in DATA :
	ln_str = '';
	for ch in ln :
		if ch != '\n' :
			ln_str += ch;
		if ch == '\\' :
			ln_str += '\\'
		# else :
		# 	ln_str += '\\n';
	TO_JS += ln_str;

# add a compression algorithm here
# -- CHOOSING TO DO HUFFMAN ENCODING --
def huffman(string) :
	lc = 0;
	symb_set = set();
	symb_cnt = {};
	ch_cnt = len(string);

	# makes set and dict of symbols and freq
	for ch in string :
		if ch not in symb_set :
			symb_set.add(ch);
			symb_cnt[ch] = 1;
		else :
			symb_cnt[ch] += 1;
		#print('%d - %s' % (lc,ch), end='\r');
		lc += 1;

	# reformats dict for freq and symbols
	cnt_symb = {};
	for i in symb_cnt :
		if symb_cnt[i] in cnt_symb :
			cnt_symb[symb_cnt[i]].append(i);
		else :
			cnt_symb[symb_cnt[i]] = [i];

	# dict to list for sorting
	list_to_sort = [];
	for i in cnt_symb :
		list_to_sort.append([i,cnt_symb[i]]);

	# sort list according to freq values
	list_to_sort.sort();
	freq_symb_list = list_to_sort;

	# non listed chars w/ probs
	freq_symb_full = [];
	for i in range(0,len(freq_symb_list)) :
		for ch in freq_symb_list[i][1] :
			freq_symb_full.append([freq_symb_list[i][0],ch]);

	#for i in range(0,len(freq_symb_full)) : print(i,freq_symb_full[i]);

	# turning above list into the huffman tree
	loop = 0;
	code_dict = {};
	current_level = freq_symb_full;
	while True :
		len_list = len(current_level);
		ind_list = range(0,len_list-1);
		next_level_probs = [];
		inds_and_probs = [];

		# attain the probs of pairs
		for i in ind_list :
			combined_prob = current_level[i][0]+current_level[i+1][0];
			inds_and_probs.append([i, i+1, combined_prob]);
			next_level_probs.append([combined_prob]);

		# finding minimum pair and their indecies in the char set
		ind = 0;
		min_prob = min(next_level_probs);
		min_pair = None;
		for prob in next_level_probs :
			if prob == min_prob :
				min_pair = inds_and_probs[ind];
				break;
			ind += 1;

		# which letter code is assigned an additional one or zero
		zero = str(current_level[min_pair[1]][1]);
		one = str(current_level[min_pair[0]][1]);

		# psuedo node for the tree to put back in the list
		node_id = '%s%s' % (zero, one);
		node = [min_pair[-1],node_id];
		#print('new node str -',node_id);

		# appending the additional 0/1 to th dictionary, adding a value if needed
		for ch_zero in zero :
			if ch_zero not in code_dict :
				code_dict[ch_zero] = '';
			code_dict[ch_zero] = '0' + code_dict[ch_zero];

		for ch_one in one :
			if ch_one not in code_dict :
				code_dict[ch_one] = '';
			code_dict[ch_one] = '1' + code_dict[ch_one];

		# updating the current_level list
		new_node_in = 0;
		new_level = [];
		ind_list = range(0,len_list);
		for i in ind_list :
			if new_node_in == 0 and i in [ind,ind+1] :
				new_level.append(node);
				# print(i,'new in',current_level[i])
				new_node_in = 1;
				continue;
			elif i not in [ind,ind+1] :
				new_level.append(current_level[i]);
				# print(i,'old in',current_level[i])
				continue;

		#print('loop -',loop);
		#print('inds to comb -', ind, ind+1);
		#print(code_dict);
		#for i in code_dict : print(i,code_dict[i]);
		#for i in new_level : print(i);

		# early break for testing purposes
		len_new_list = len(new_level);
		if len_new_list == 1 :
			outp_code = code_dict;
			break;
		loop += 1; #print();
		current_level = new_level;

	outp_code_alt = {};
	for i in outp_code :
		ind = outp_code[i];
		defn = i;
		outp_code_alt[ind] = defn;

	return [outp_code,outp_code_alt];

# converting old string to huffman encoded binary
def str_to_huffman_bin(huffman_code, string_in) :
	bin_str_out = '';
	for ch in string_in :
		bin_str_out += huffman_code[ch];
	return bin_str_out;

# re-encoding binary to a string
def re_encode_bin(huffman_code, bin_str_in) :
	# the first part is just set up of the new char set

	# full character set available
	#								_____________
	# abcdefghijklmnopqrstuvwxyz	| 026 | 026 |
	# ABCDEFGHIJKLMNOPQRSTUVWXYZ	| 026 | 052 |
	# á”çðéđŋħí  łµ óþ ¶ßŧú ẃ»ý«	| 021 | 073 |
	# Á’ÇÐÉªŊĦÍ  Łº ÓÞΩ®§ŦÚ Ẃ Ý 	| 020 | 093 |
	# `1234567890-= 				| 013 | 106 |
	# ¬!£$%^&*()_+ 					| 012 | 118 |
	# []; #,./						| 007 | 125 |
	# {}:@~<>?						| 008 | 133 |
	#								|_____+_____|
	#						  total = 132
	#
	re_enc_char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZá”çðéđŋħíłµóþ¶ßŧúẃ»ý«Á’ÇÐÉªŊĦÍŁºÓÞΩ®§ŦÚẂÝ`1234567890-=¬!£$%^&*()_+[];#,./{}:'

	longest_code = 0;
	for i in huffman_code :
		if len(i) > longest_code :
			longest_code = len(i);

	n = 7; # re-encoding bit len per char
	i_list = range(0,2**n);
	bit_7_list = [];
	for i in i_list :
		b = bin(i)[2:];
		s = str(b).zfill(n);
		bit_7_list.append(s);

	re_enc_char_dict = {};
	for i in i_list :
		re_enc_char_dict[bit_7_list[i]] = re_enc_char_set[i];
	#for i in re_enc_char_dict : print(i,re_enc_char_dict[i]);

	# calculating stuff regarding the input string and the end of bit stream
	bin_len = len(bin_str_in);
	len_mod_7 = bin_len%7;
	trailing_1s = 7 - len_mod_7;
	bin_end = trailing_1s * '1';

	tmp_bin = bin_str_in + bin_end;
	i_list = range(1,int(len(tmp_bin)/7));

	new_enc_str = '';
	for i in i_list :
		I = i-1;
		J = i-1+n;
		bit_pattern = tmp_bin[I:J];
		enc_char = re_enc_char_dict[bit_pattern];
		new_enc_str += enc_char;
		#print(bit_pattern,enc_char);

	#print(new_enc_str);
	return [new_enc_str,trailing_1s];


huff_code_dict = huffman(TO_JS)[0];
alt_hcode_dict = huffman(TO_JS)[1];
#for i in huff_code_dict : print(i,huff_code_dict[i],len(huff_code_dict[i]));

huff_bin_str = str_to_huffman_bin(huff_code_dict,TO_JS);
#print('string converted to binary via huffman');
#print(tmp_str);

# diagnostic stuff
old_len = (8*len(TO_JS));
new_len = len(huff_bin_str);
len_diff = old_len - new_len;

code_bits = [len(huff_code_dict[i]) for i in huff_code_dict];
mean_bits = sum(code_bits)/len(code_bits)
mean_chars = new_len/len(TO_JS);
bef_aft_ratio = new_len/old_len;

print();
print('given 1ch == 8bits...');
print('before = %d bits' % old_len);
print('after = %d bits' % new_len);
print('reduction = %d' % len_diff);
print('average code length acc to dict = %f bits' % mean_bits);
print('average code length acc to chars = %f bits' % mean_chars);
print('ratio of lens = %f' % bef_aft_ratio);

# converting the huff bin to newly encoded string
# should be considerably shorter than the original
encoded_str = re_encode_bin(alt_hcode_dict,huff_bin_str);
# with the compressed txt put into js file, then need to write decompressor in js

OUTP = '''const TXT_TEST = '%s';
export {TXT_TEST};
const COMP_TXT = '%s';
const HUFF_CODE = %s;
const END_ONES = %d;
export {COMP_TXT,HUFF_CODE,END_ONES};
''' % (TO_JS,encoded_str[0],,encoded_str[1]);

# print into a JSON file
FILE_OUT = open('%s/tmp/test.js' % DIR, 'w');
FILE_OUT.write(OUTP);
FILE_OUT.close();
