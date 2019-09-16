from collections import OrderedDict
if __name__ == '__main__':
	
	s = 'ybzhgdrefvdnjyfoswjuslbpuvtvfgzvnpayvjwzxkdpnbdnrsodnqhpqspojipjwgxaltzoikuucixfsoueknofvsohtqtvxvihtsevdojscucxwnivgzjazfsznswxbjylqejlgpkppwezlxhfhwuphrnqfdiowmeikwdozhjwmcneixidypdikthxxvppjakeffvhpmsxijiolpybpntbiuehpwkobetpglwxexuoxgwdbcsfvskkczxluccfkrwmpvbknadmbivdrypxtlmbnvqvcnoyciqcfnpkenvwkkosvsnxiqibkirlikwsdcnqruirprxhlenlrxahfiyhfgvbwqehddnqdtfgzwbyudmirkqmzkhxcwqxxvyrtrrmsezyvuanpcjisbfywzqesxyxlulaxamyedjyautncorctzanmosfpuescfqhrydrsohttsohvpkqppxdjsefcnelearcrypndesagvybsnzikxjqyzsvcpiypmkjaihrouvcajsxxsnsavasoxgigbhfxhbtivoyoflmmjmtxrxrsezgzcfkqiczphapeugunnyhpzpeisgohuuuchqcjbhvzojsaiecebllqevoakkfsdwqfuaozouhdgnuludvdcojalzztzkfmqxagdrlcekwyxerosaeplyzgjxwbiowidwgdnmdekjinuseaswpvmnpolistdinevfcfzlognzzfrlfoogxhyiwrfeaplrryyvyygxwgqbpaxcgrzfbhcsmbxeinwgmkpgzbdnoxdppkdvewajsnujyrojmiuvimgpkbhjmxsgaalyyovdipfeyiaeybyyvhdyacyuljzhmhtnvoapcijurxjbjalunfhtbvaiffutjxpvaedxyvrrqckxecqkniienwmmtkpwmpqkvhjigzqmtuouuxwmhohxyauzuakyvaekvyrjuuqgtcfptsuczdbeeloffdqewalyyygokdxor'

	# Variable we need declarations
	dict={}
	s=list(s)
	list_value = []
	final_list = []
	flag = 0
	LIMIT_VALUE = 3
	
	# Create a dictionnary and set the letters as the dictionnary keys and the letters occurences as the dictionnary's value
	for letter in s:
		dict[letter]=s.count(letter)
	sorted_dict = sorted(dict, key=lambda k: (dict[k], k), reverse=True)
	
	# Let's get the first three most common letters
	for r in sorted_dict:
		flag+=1
		if flag <= LIMIT_VALUE:
			list_value.append(dict[r])
	
	# Sort by multiple criteria
	list_value = list(OrderedDict.fromkeys(list_value[:3]))
	print("list_value",list_value)
	for i in range(len(list_value)) : 
		list_key = [key for key,value in dict.items() if value == list_value[i]]
		print("list {}".format(list_key))
		
		if len(list_key)>1:
			list_key.sort()
		count = 0
		for j in range(len(list_key)):
			if count < LIMIT_VALUE:
				final_list.append(list_key[j])
				count += 1
	for i in range(len(final_list[:LIMIT_VALUE])):
		print(final_list[i],dict[final_list[i]])
		