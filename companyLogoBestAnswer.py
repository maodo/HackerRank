from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
if __name__ == '__main__':
    s = 'ybzhgdrefvdnjyfoswjuslbpuvtvfgzvnpayvjwzxkdpnbdnrsodnqhpqspojipjwgxaltzoikuucixfsoueknofvsohtqtvxvihtsevdojscucxwnivgzjazfsznswxbjylqejlgpkppwezlxhfhwuphrnqfdiowmeikwdozhjwmcneixidypdikthxxvppjakeffvhpmsxijiolpybpntbiuehpwkobetpglwxexuoxgwdbcsfvskkczxluccfkrwmpvbknadmbivdrypxtlmbnvqvcnoyciqcfnpkenvwkkosvsnxiqibkirlikwsdcnqruirprxhlenlrxahfiyhfgvbwqehddnqdtfgzwbyudmirkqmzkhxcwqxxvyrtrrmsezyvuanpcjisbfywzqesxyxlulaxamyedjyautncorctzanmosfpuescfqhrydrsohttsohvpkqppxdjsefcnelearcrypndesagvybsnzikxjqyzsvcpiypmkjaihrouvcajsxxsnsavasoxgigbhfxhbtivoyoflmmjmtxrxrsezgzcfkqiczphapeugunnyhpzpeisgohuuuchqcjbhvzojsaiecebllqevoakkfsdwqfuaozouhdgnuludvdcojalzztzkfmqxagdrlcekwyxerosaeplyzgjxwbiowidwgdnmdekjinuseaswpvmnpolistdinevfcfzlognzzfrlfoogxhyiwrfeaplrryyvyygxwgqbpaxcgrzfbhcsmbxeinwgmkpgzbdnoxdppkdvewajsnujyrojmiuvimgpkbhjmxsgaalyyovdipfeyiaeybyyvhdyacyuljzhmhtnvoapcijurxjbjalunfhtbvaiffutjxpvaedxyvrrqckxecqkniienwmmtkpwmpqkvhjigzqmtuouuxwmhohxyauzuakyvaekvyrjuuqgtcfptsuczdbeeloffdqewalyyygokdxor'
    [print(*c) for c in OrderedCounter(sorted(s)).most_common(3)]