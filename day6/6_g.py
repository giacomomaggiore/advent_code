import sys
sys.setrecursionlimit(2005555000)


input = "grvrnvrnnjljbjqjpqjjvhhzwwrbwwbblrltrrpbbbbqnnqbbbbsvbvmbvmbbrsrqrzrllwbbbqzqrqnqrnrjnnjccdggwqqhrrjcjmjmllgrlglhlclmlvlvsshwwsggmfmdfddgdfftrrczrcczhzppgdgrdggghmmdwwqgggslglfgfcgccmjcjwjrwjrjcrjjsgjjvddpwpgpbbgwbgwwhnhfftbffhpfphhfqfrqfrfnfpprvrsrhrfrllfhhrsrhssvfsvsnvsnsswtwtlthllrjjwddtggzczgcchwcwppfbbdvdrdzrdrvrwwsbsfbssqfsfjsjcscttlztllgjjlbbdsdtssvvvwlvlqqnhqqtdqtddjcdcjjpbphhgtgtqtzqqzhqqtgtvtmvtvrvqrvvfmfmppzzbwwnddzttfpfrrlddbppfqppnwnswwdhwdwjjqljqqthtnhnddgmgcmgcmgcmmfmfttrzzfdzztllmjlllgcgbbcqcvccpnndbdjbjmmzbztzptzpprpddptpprhhvlvmlmpmmljjnnjsjfjjvgjjvzzfgfzfbftbftttgstgstgtpggflfcfqqtctltgltldlzdlzzmmlddnvddzfddppmnpptzptpvttwstwswvwrvvbfbjjjbmjjdvdvrvdddrwrhrzrqqhghhrwhwhrrmppsgpsgszzdfdfwwmtwtvwvgvffmqqqtqntqnnjcncbnbwnnzggrdrqqjbqjjwjqqqwlqwlwzlljhhfsfsqsrqqhwqqwbbqbvvlflrrlglbbjhhjmhjjcmcjcgczcfcgcqqczcnnvjnnlddmpmcppgvgjgddvrrnsnmnqmqgmmnppwgwcgwgssbddgtdgdgmdgmgvvmjmvmjmvvsfssdgdghdggbfbqbdbjbsbmmrpmrprggbllwrwpwtppzvppzsssdnsdnnvnhvvvzvfzfqqnnmlnltldtdvdbdblddsmmlccmlmvlmvmmcsctctrtsrstsbsrshsddlmddmppgsscttnrtrqqcvcwwlnlznnnvcnvvtnvnbnmbmvmppjgjdjtddmpdmdvvmgvvdqdlqlhhzccsggjdjsdsttctjctjtfjttppdzpzzbjbwwmwbblslzslzszlzrrcbrrfggvcczjjtbbdnnggbwblwlbwlwqqfvfqfddrrfccvlllhmhhhrthrthrrnbnzbbpzplphprrrnbbghhnshnhbblqqqvwwffnmnmhhtccpqpvqvbvnvvfnfsnffdjdllwffcddgcgrgjrggchcpcddtbbdtdmtdmmhhtphtpppclcpcvcjvcjjfqfzqqphpnhnrnhhpdhhtfhhbbmqmfmsmvssgqqfssqgglnnqmnmbnmbbllrdrgdrdvrdvdsvvnddgtgddcdqdsqdqbqqlhhwdhdgdcgcdchchrchhpvvpgvgrrfggwfwgmpddbhfngtrwswfszgsggnpsntjpslrpjqsffzrlnbnzdtqpqtjzwlhhgrsrbvnccnsjmzcbqgcbtbqlzhnpnhhrrvqwjwzzvrlcrmjhcscrqhpqmfzbnvcwwqhcjjlnggmpbwztzfswmsbjshnsgfmdlzvzczhrdwgwbghszpnbfpctrshbfhspsczcqcrrqcpwwpfzhjqtpqgjbztrpzrlgfdjbmlwdvlvnfmdzbwsbbhlbszvwcpztlchjrqbmsftltmqpfgdpmdgjvwqqtjsqlfqrwmsnlqgsbqfwsdnfvzthmbplvszfcmlptlcjpnfpjsphsmmjplwjqphgvzbtbjtpttqhlwtgnrjvmvsfsztmsqszzlhqqhfslsvhzgtsssfctzgsqbgdzlpwbsmpcnjqshhhcwqdsdzdhnjfqzqnqdlrpddcgrgldgqbjmdtwgppdczzrjvmcfqjbpjzbtjmgdphlbwnsnpfdqlhwvvmpwzsrztnwvtlbphljmjwsgbphgmwhdmfhpvsmvsjccjhfvqtvfmmlnggncltvtrgmbtfqsvfnlvcmjnjwzcrpjnsgntvhjbtdlptshbhhchqmsprhqzdnfpjqccdfvnzjtlbsmmwvzlwlvmsbrnhqctvtvbfhntdctjnrbcrrlmsnwbbjbcbbgrrhfqwzwwfgvsvgbwnttghtgpspzwzfhffsqjvwwttntnvlwftsfvtttgnprzrzsghvjrdtsfdvzswhmrfcdqsgvrlhzbnvbmjlqrftnnbtwqtvlvwznfbslhdqjbntdgpprfqchjvgvzjssdztjlzwfljjmfvzrbbtczggzqwrnqqgzzcbqjcpfqfrbwtdjrrvbszsjdjcpdfjscsvnltcgwvqsgnhbfgnfnddnpmbzbptrmvqzpvbdpfdvtlmgnnjwflgdbfnmvsdnmlvgcpwflwvdbtbfwtfpsmqsplnzwlwgvbjrhghwrnrswsggbqpdjcjrgbgnsqdvwzzwftvjqgjzzcdvpbbjzpphmbcqmrjvgqwfgrsnqvhwflmhgrlvbpwdcsrlqwfrwppqbrdhwqtvczpclpsbsjcptgblbbsqmbhjjgzwvlcnhnzcttmpjsgchmppgphqlzlcsqcgbbjgtjjvmttdztfdptzgvmpnqrcmpmcdlpnbztllvqbggqbqhlqvdwsrwzsjwfrqvcbvsgfdptmrzpvdfblmhlzrvpmsljlqqzrhlnmwncpfhvqlsbtrjbfcrnfvjvddrhdbbczjdsrdvzlbqrccssdzcpmdsqbprjppfzdwfdswptgzcmjqfhcwsqfqhvrslffqfbcvhdzljzrmtwmfdwzdhhjcmbjtvjhzzwfqhrcslztdbnlwmmhbbbgdscjcdzftnchqfnflnsdqjscfrqpnfbftpzvtmrwncqfqqflschpfnjsjlqcjdjgtwpqhgcnjdmnnvmmpwdspmnrgqrptqwcvbtdwpqlbtwpqgwgfrzlrhtvrvzhmhmwhfdsrhpcczqfltsgtgrfwcvlcvtlhqqwnrqgzpnzbfmzbdwqwbsfvbshrgzqdbgvrhzhzlbqsfzttmsnmrqmwgtzbvdqdrbgcpclzjrhdbjtpcdbbznjgtbwbqrnpvffdmwtrbhhstcmnjcwbbnmpbvmjprtzgcptmtrffwhvfgdljnrbbrblbfbgdwtjrtgqgrpvpgjqrjzczvvlspgdbzftqgqvgdqlglbgvgjdcztznszcwfqhmwbrbjcfstzdcmdsssqfhtzpdgmzjscvbdzgbhhgdqgvfwrzmhdrhlsvlzjjzbzdljcbhncppwrtptjgszlqsrqpzqcsgvdvzmgvwgsncnbffttslphcstqvfwbwzbflmshcbnhpljgqwmmwwzlgpbcqnrtqlwcjcrclfdrnnmvtbfdztdfvtqrsgdptfcfpzpsldhzmrngggfvdqggtlfqqwsldprcffsstnnpmsbbvghdbpprqbssnprdbqclzqtgsrczwcvqwrrfmmfwsndvtvqljwwglrgbphdvvwgctbbmtrbpzqtspgrlhmnhjcdwhwvssgspzjbcfjttjqbdpdmptfzzjcfqljpqddfssmffqprvbptfvdshsdmfmdtmlbnmbmjjjsgmlmwmgcwhbrbgchrstptvdlqgddfzddlzhwjmsvvcjwvqtzjtsctfmzchlbrvlgdzbvdlbfpvhptpltrdmcgjghcpwvwqqnrzdtnmgdncplhdpsgpnbprbgshffwwsdhpgqsbmwdtpnhhltlcqfrjtswcchzvlhdgrmjwhgwppdjqlgmdhwbllqvzrchgclmqdlghjsvmwlflmhhmdzbfjhjnvwphnjbclmdpgflqgtfsmsjslntfcmtbphnrgpdcqtjzjttdtgjmvhzsrfnrjqssvwpcslpfstbpfsrsntmftmdgsqrrsnddqfmchrhtlhmqndvvllnvltdzfphjqnvmcdsgfpcmjftgdpntjzplqljhtthvnbzbzwvfnqsjvnfwhmtbsspjslgfjvdgfjpwrsgqwntntjcqtdgnhnsfwhhqfwbwhdrftj"
#print(len(input))

def trova(stringa, n):
    temp = stringa[n:n+4]

    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if i != j and temp[i] == temp[j]:
                i = 0
                j = 0 
                return trova(input, n+1)
            j = j +1
        i = i + 1
    
    return n + 4

def trova_due(stringa, n):
    temp = stringa[n:n+14]

    i = 0
    while i < 14:
        j = 0
        while j < 14:
            if i != j and temp[i] == temp[j]:
                i = 0
                j = 0 
                return trova_due(input, n+1)
            j = j +1
        i = i + 1
    
    return n + 14   

print(trova_due(input,0))