# Simple Substitution Cipher Hacker

# http://inventwithpython.com/hacking (BSD Licensed)


import os, re, copy, pprint, pyperclip, simpleSubCipher, makeWordPatterns



if not os.path.exists("wordPatterns.py"):
    makeWordPatterns.main()  # create the wordPatterns.py file

import wordPatterns


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nonLettersOrSpacePattern = re.compile("[^A-Z\s]")


def main():
    message = "rsxwa  jia rpwslmsrj npqanaxj ilr faax wpnbmajamh jclxrypcnao jicptuiptj atcpba lxo jia cartmj py jia jclxrypcnljspx nlh ylscmh fa oarwcsfao lr ylfslx rpwslmsrn sx jia asuijaaxasuijsar eiax rpwslmsrn caqsqao sx axumlxo ypc jia yscrj jsna rsxwa jia rtbbcarrspx py jia blcsr wpnntxa sx  sj elr xpj lj yscrj calmszao jilj eilj ilo calmmh faax rtbbcarrao ypc uppo lxo lmm elr jia cpnlxjsw caqpmtjspxlch msfaclmsrn lxo closwlmsrn py  jp eiswi jia rpwslmsrjr ilo ljjlwiao jianramqar lr l nljjac py wptcra blcjmh fawltra jiah eaca jianramqar cpnlxjsw lxo caqpmtjspxlch lxo blcjmh fawltra fpji msfaclmr lxo rpwslmsrjr ilo l wpnnpx pfvawj sx oanpwclwh  farsoar jisr wpnnpx pfvawj jia jep ilo l wpnnpx wpxwabjspx py najipo sx caqpmtjspx jiah eaca fpji wljlrjcpbisrjr msfaclmsrn ilo wpxdtacao ltjpwclwh lxo ftcaltwclwh fh jilj najipo sx axumlxo lxo yclxwa lxo jiax mayj sxotrjch jp nlka eilj sj wptmo py jia xae bpmsjswlm wpxosjspxr fh jia txcautmljao lwjspx py wpnbajsjspx fajeaax sxosqsotlmr fcsaymh jia msfaclm bmlx elr jp wtj pyy jia ksxur ialo lxo malqa jia carj jp xljtca eiswi elr rtbbprao jp uclqsjlja jpelcor awpxpnsw ilcnpxsar eiax xpj carjclsxao fh jhclxxswlm upqacxnaxjr jia rpwslmsrjr eaca qach ylc lialo py jia msfaclmr sx jiasc lbbcawsljspx py jia bcabpxoaclxj snbpcjlxwa py sxotrjch aqax upsxu rp ylc lr jp nlsxjlsx esji ftwkma lxo nlcg jilj lmm rpwslm sxrjsjtjspxr eiljaqac eaca snbprao fh awpxpnsw wpxosjspxr lxo jilj jiaca elr ytxolnaxjlmmh pxmh pxa jhclxxh jia jhclxxh py wlbsjlm haj aqax jia rpwslmsrjr ilo rp ylc ypcnao jiasc bpmsjswlm ilfsjr sx jia msfaclm rwippm jilj jiah eaca dtsja osrbprao jp famsaqa jilj sy hpt wtj pyy jia ialo py ksxu wlbsjlm hpt nsuij agbawj jp raa jisxur wpna csuij npca pc marr rbpxjlxaptrmh  xp optfj jisr uaxaclm rjljanaxj riaer jia caqpmtjspxlcsar py  lr rsnbmac jilx jiah lbbalc px jiasc pex cawpcor bcptoipx elr ytmm py bcpbprlmr pxa py jian jia nsxsntn elua jtcxr ptj jp fa py jia qach yscrj snbpcjlxwa xpe jilj nc lxo ncr rsoxah eaff ilqa btj jia wlra ypc sj px lx sxqsxwsfma flrsr py sxotrjcslm ylwj lxo awpxpnsw jiapch mlrrlmma calmmh kxae rpnajisxu py jia xljtca py mle jia bclwjswa py upqacxnaxj lxo jia nsxo py jia upqacxsxu wmlrrar nlcg jiptui wacjlsxmh l fsj py l msfaclm yljlmsrj oso ia xpj rlh jilj ypcwa sr jia nsoesya py bcpucarr esjiptj cansxosxu tr jilj ypcwa sr adtlmmh jia nsoesya py wilpr lxo wilpr jia nsoesya py nlcjslm mle elr lj lmm aqaxjr xp famsaqac sx mlsrracylsca rpwslmsrn sxqpmqar jia sxjcpotwjspx py oarsux wpxjcsqlxwa lxo wppcosxljspx fh l xljspx wpxrwsptrmh raaksxu sjr pex wpmmawjsqa eamylca sxjp jia bcaraxj sxotrjcslm rwclnfma ypc bcsqlja ulsx lxo lr sj sr wmalc jilj jisr wlxxpj fa l rbpxjlxaptr cartmj py l qspmaxj pqacjicpe py jia agsrjsxu pcoac lxo lr jia rpwslmsrjr py  eaca xpj fmsxo sj eptmo fa snbprrsfma jp rtfrjlxjslja l wmlsn ypc ylfslx arrlhr lr jia yscrj jagjfppk py rpwslmsrn sx eiswi wljlrjcpbisrn sr cabtosljao lr l najipo py rpwslmsrn  jiacaypca ea ntrj xpj rlh jilj jia caqpmtjspxsrjr lxo sxjacxljspxlmsrjr py  famsaqao sx l oclnljsw pqacjicpe py jia wlbsjlmsrj rhrjan sx l rsxuma wpxqtmrspx ypmmpeao fh jia arjlfmsrinaxj py l xae ialqax l xae alcji lxo l xae itnlxsjh jiah eaca qsrspxlcsar xp optfj lmm bpmsjswlm soalmsrjr lca ftj jiah eaca dtsja lr bclwjswlm lr jia wpxracqljsqar lxo msfaclmr eip xpe famsaqa jilj jia jcstnbi py jiasc blcjh esmm rawtca jia ilbbsxarr lxo balwa py jia wptxjch lmm jia rlna sj elr lmnprj snbprrsfma jp sxotwa jian jp rbalk pc jisxk py jia rpwslmsrj rjlja py jia ytjtca sx jacnr py jia agsrjsxu itnlx nljacslm ypc sj jiah jlmkao py wpnntxar lxo npca qlutamh lxo marr esmmsxumh py waxjclm oablcjnaxjr jp wppcosxlja jia lwjsqsjsar py jia wpnntxar ftj sy hpt qaxjtcao jp bpsxj ptj jilj jiara lbblcaxjmh rjclxua lxo cpnlxjsw sxqaxjspxr eaca rsnbmh wsjh wpcbpcljspxr txoac jia mpwlm upqacxnaxj fplco jiah qaianaxjmh cabtosljao rtwi l wpxrjctwjspx lxo lwwtrao hpt py calosxu jia wpxosjspxr py jia bcaraxj rhrjan sxjp rpwslmsrn jiah ilo lmm jia pmo msfaclm nsrjctrj py upqacxnaxjr lxo ftcaltwclwh lxo lmm jia pmo jaxoaxwh py fptcuapsr caqpmtjspxsrjr jp sopmsza jia epcksxu wmlrr jiah ilo xp rtrbswspx py jia agjaxj jp eiswi jia qach agsrjaxwa py rpwsajh oabaxor px jia rksmmao epck py lonsxsrjcljpcr lxo agbacjr pc ipe ntwi esropn lxo rjcaxuji py wilclwjac sr cadtscao ypc jiasc wpxjcpm fh bpbtmlc cabcaraxjljsqar jiah lwjtlmmh famsaqao jilj eiax jiasc ayypcjr jicptuiptj atcpba ilo oanpxrjcljao jia awpxpnswr py rpwslmsrn jp jia bcpmajlcsljr py jia ucalj wlbsjlmr jia wch bcpmajlcslxr py lmm mlxor txsja eptmo fa carbpxoao jp lxo jilj wlbsjlmsrn eptmo ylmm faypca lx sxjacxljspxlm yaoacljspx py jia epcksxu wmlrrar py atcpba xpj sx jia raxra sx eiswi rpna ytjtca isrjpcslx esmm rtnnlcsza jep pc jicaa waxjtcsar sx eiswi raxra jiah nlh bcpqa csuij axptui ftj lr lx snnaoslja bclwjswlm bmlx py lwjspx mskamh jp fa wlccsao jicptui sx jeaxjh halcr fh rpwslmsrj rpwsajsar ipmosxu wpnbmajamh lxo osrolsxytmmh lmppy ycpn pcosxlch bpmsjswr sx ripcj jiah eaca cpnlxjsw lnljatcr lxo lr rtwi eaca axpcnptrmh axwptcluao lxo ymljjacao eiax nlcg lxo axuamr sxrsrjao px jia rwsaxjsysw wilclwjac py jiasc npqanaxj sx wpxjclrj jp jia tjpbslx rpwslmsrn py peax yptcsac rj rsnpx lxo jia nax py jia  bilra eiax jia aqaxjr py  sx blcsr jarjao jian bclwjswlmmh jiasc ipbamarr btfmsw sxwlblwsjh ypcwao jiasc pbbpxaxjr jp agjacnsxlja jian sx jia nprj lbblmmsxu nlrrlwca py npoacx jsnarlmm jia npca uilrjmh fawltra sj elr l nlrrlwca py jia sxxpwaxjr  btfmsw pbsxspx sx atcpba elr cawpxwsmao jp jia nlrrlwca fh jia trtlm bcpwarr py rmlxoacsxu jia qswjsnr xpe ilo atcpba faax bpmsjswlmmh aotwljao xp rmlxoacr eptmo ilqa faax xawarrlch ypc aqax ilo sj faax itnlxmh bprrsfma jilj lmm jia yaoaclmr npex opex esji nsjclsmmatrar sx blcsr eaca sxwaxoslcsar lxo lrrlrrsxr sj eptmo rjsmm ilqa faax dtarjspxlfma eiajiac sxosrwcsnsxlja nlrrlwca sr jia csuij elh jp oalm esji sxwaxoslcsar lxo lrrlrrsxr ftj jiaca wlx fa xp dtarjspx lr jp eilj ntrj fa opxa esji jpjlmmh sxwpnbajaxj upqacxpcr jia pxa jisxu jilj sr bpmsjswlmmh wacjlsx xpelolhr sr jilj sy l fpoh py nax tbraj jia agsrjsxu upqacxnaxj py l npoacx rjlja esjiptj rtyyswsaxj kxpemaoua lxo wlblwsjh jp wpxjsxta jia xawarrlch lxo ipxarj blcj py sjr epck lxo sy fasxu txlfma jp op jilj epck jianramqar jiah esmm xpj maj lxhpxa amra op sj asjiac jiasc agjacnsxljspx fawpnar l nljjac py snnaoslja xawarrsjh sj esmm lqlsm jian xpjisxu jilj jiah lsn isuiac jilx jiasc yljiacr oso jilj jiasc sxjaxjspxr lca uppo jiasc lwjspx bacrpxlmmh osrsxjacarjao lxo jiasc pbbpxaxjr ramysri lxo qaxlm cptjsxaacr eip eptmo jianramqar fa adtlmmh lj l mprr sy jiah ilo jp wcalja l xae pcoac sxrjalo py nacamh btmmsxu jia escar py lx pmo pxa lxhpxa eip mppkr lj jia bpcjclsjr py jia nanfacr py jia blcsr wpnntxa wlx raa lj l umlxwa jilj jiah wpnblcao qach ylqpclfmh sx lmm jia agjacxlm rsuxr py lnslfsmsjh lxo caysxanaxj esji lxh upqacxsxu fpoh jiax pc xpe sx bpeac sx atcpba ftj jiah wptmo xpj nlxlua jia ftrsxarr jiah jppk tbpx jianramqar lxo jisacr wptmo nlcgr oanpxrjcljspx jilj jiah eaca iacpar lxo nlcjhcr lxo jilj jisacr lxo isr lmmsar eaca clrwlmr oso xpj iamb sx jia malrj jiptui sj elr txoaxslfmh jia lfmarj opwtnaxj sx jia wpxymswj py npclm wmlbjclb jilj pfrwtcao jia calm srrtarrp lfma sxoaao lr l bsawa py msjacljtca jilj npca jilx jiscjh halcr lyjac sjr btfmswljspx sj rjctwk opex jia nlcdtsr oa ulmmsyaj lr sy sj ilo lbbalcao sx jia janbr pc oafljr py jia olh faypca sj elr lnslfma py jia yaoaclmr jp fa rp ntwi marr wlblfma py agjacnsxljsxu jisacr jilx ia elr py agjacnsxljsxu jian ftj raxjsnaxjlm lnslfsmsjh sr xpj fh sjramy l dtlmsyswljspx ypc lonsxsrjacsxu ucalj npoacx rjljar  xpe jia ylfslx rpwsajh fpcx sx  lxo calwisxu jia lua py osrwcajspx sx marr jilx jep halcr ilo xp nsxo jp fa agjacnsxljao nlcjhcopn elr oarwcsfao fh pxa py tr lr jia pxmh elh sx eiswi l nlx wlx fawpna ylnptr esjiptj lfsmsjh ytcjiac ea ilo xp smmtrspxr lr jp jia jcaljnaxj ea riptmo cawasqa sy mska jia blcsr yaoaclmr ea jaccsysao jia bcpbacjh wmlrrar faypca jiah eaca osrlfmao fh l mpxu racsar py nsxpc axuluanaxjr sx blcsr sx  pcosxlch rlxa bapbma iso jianramqar sx jiasc iptrar ypc eaakr txoac jia snbcarrspx jilj jia rjcaajr eaca xpj rlya jiah oso xpj qaxjtca ptj txjsm jiah clx l racsptr csrk py fasxu ripj lj rsuij fh jiasc pex blcjsrlxr sx jia pcuh py ntcoac lxo wctamjh jilj ypmmpeao jia osrwpqach jilj jia wpnntxa wptmo ysuij pxmh lr l clj ysuijr sx l wpcxac itnlx xljtca ilr xpj wilxuao rsxwa jiax sx  l ylfslx arrlhsrj rjppo pxa nlh npcxsxu sx jia cta oa csqpms lxo yptxo isnramy lmnprj jia pxmh rptm sx jia earj axo py blcsr eip olcao lbbalc jiaca jia wtmjtcao sxilfsjlxjr py jilj ramawj dtlcjac eaca isosxu sx jiasc iptrar lr faypca esji jiasc mlcoacr ytmm py ilnr lxo jiasc fljir ytmm py msqa ysri jp bcpqsrspx jian ypc l rsaua jiaca elr ntwi marr olxuac py l caqpmtjspx jilj olh jilx jiaca sr py bcsncpra ismm fawpnsxu lx lwjsqa qpmwlxp lj rsg pwmpwk jisr aqaxsxu lxo jia btcbpra py jia upqacxnaxj lxo sjr blcjh xaerblbacr sx nlxtylwjtcsxu jia rwlca jp ycsuijax jia fptcuapsrsa sxjp rtbbpcjsxu jian lj jia uaxaclm amawjspx vtrj jiax fausxxsxu elr pfqsptr pxa eptmo ilqa jiptuij jp jia osnnarj bpmsjswlm bacrbswlwsjh sx jia aqaxsxu jilj rlna arrlhsrj sx jia bmlwa oa ml caqpmtjspx rle l wcpeo py rsuijraacr lrranfmao jp esjxarr jia bcpnsrao sxrtccawjspx lxo jia jcppbr lxo jia bpmswa lrranfmao jp rlqa rpwsajh ycpn sj sj elr qach mska jclylmulc rdtlca sx  eiax jia rlna qspmaxj ylcwa elr axlwjao sx mpxopx pwwlrspxlmmh jia jcppbr cpoa opex rpna py jia rsuijraacr lxo jia bpmswa lccarjao rpna py jian axptui bacrpxr mprj jiasc janbac jp nlka l yae yaafma ljjanbjr lj cspj lxo jp rtbbmh lccarjr ypc jia npcxsxu blbacr xagj olh rpwsajh rlqao wlna ptj py sjr isosxu bmlwar rpmo jia ysri ycpn sjr fljir lxo jia ilnr ycpn sjr mlcoacr lj l rlwcsyswa jia ealjiac fasxu qach ipj lxo jia ilnr sx dtarjspxlfma wpxosjspx lxo qpjao ucljaytmmh ypc jia upqacxnaxj jilj ilo ycsuijaxao sj ptj py sjr raxrar esji lx snlusxlch caqpmtjspx lxo l csoswtmptr wpnbmpj axumlxo mltuiao lj jia blcsrslxr jiptui bmaxjh py axumsri qsrsjpcr ilo mayj blcsr jp lqpso jia jicaljaxao casux py jaccpc haj sx jia qach xagj npxji ptc pex bcpbacjsao wmlrrar sx wlscp jaccsysao fh jia xljspxlmsrj npqanaxj sx auhbj yamm sxjp l blcpghrn py wpelcoswa lxo wctamjh lxo wpnnsjjao jia oaxrilels ljcpwsjh wpnblcao jp eiswi jia nlrrlwca py umaxwpa elr l jcsyma jia wcaotmsjh eiswi lmmper sjramy jp fa bacrtloao fh casjacljspx py jia bsptr epco bcpucarr jilj ea msqa sx l uaxjmac lua jilx ptc yljiacr lxo jilj jia epcrj agjcansjsar py jaccpc lxo qaxualxwa lca marr jp fa lbbcaiaxoao ycpn ptc xaemh axcswiao ltjpnpfsmsrj wmlrrar jilx jiah eaca ycpn jia lcsrjpwclwsar py jia pmoac pcoacr sr xpj l ylfslx wilclwjacsrjsw jia ylfslx kxper jilj bcpbacjh opar xpj iarsjlja jp rippj lxo jilj xpe lr lmelhr jia txrtwwarrytm caqpmtjspxsrj nlh agbawj wlmtnxh bacvtch wctamjh vtoswslm lxo nsmsjlch nlrrlwca esjiptj nacwh lxo jia ylfslx opar xpj sxjaxo jp uaj jitr ilxomao sy ia wlx iamb sj sy jiaca sr jp fa lxh rippjsxu ia sxjaxor jp fa lj jia rjlja axo py jia utx lxo ia kxper jilj sj esmm jlka isn l uppo nlxh halcr jp uaj jiaca rjsmm ia jisxkr ia raar isr elhpc cljiac jia carj py isr elh ypc ia sr lmcaloh eamm px jia cplo  sj elr sx  jilj jia ylfslx rpwsajh lnso jia vaacr py jia wljlrjcpbisrjr jtcxao sjr flwk px jia flccswloar lxo nloa tb sjr nsxo jp jtcx iacpsw oayalj sxjp bcprlsw rtwwarr ea raj ptcramqar jep oaysxsja jlrkr yscrj jp bcpqsoa l blcmslnaxjlch bcpucln ypc l bcsna nsxsrjac wpxqacjao jp rpwslmsrn lr baam elr wpxqacjao jp ycaa jcloa lxo rawpxo jp nlka sj lr alrh lxo nljjacpywptcra ypc jia pcosxlch carbawjlfma axumsrinlx jp fa l rpwslmsrj lr jp fa l msfaclm pc l wpxracqljsqa"
    
    # Determine the possible valid ciphertext translations.

    print("Hacking...")

    letterMapping = hackSimpleSub(message)

    # Display the results to the user.

    print("Mapping:")

    pprint.pprint(letterMapping)

    print()

    print("Original ciphertext:")

    print(message)

    print()

    print("Copying hacked message to clipboard:")

    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)

    pyperclip.copy(hackedMessage)

    print(hackedMessage)


def getBlankCipherletterMapping():
    # Returns a dictionary value that is a blank cipherletter mapping.

    return {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": [],
        "P": [],
        "Q": [],
        "R": [],
        "S": [],
        "T": [],
        "U": [],
        "V": [],
        "W": [],
        "X": [],
        "Y": [],
        "Z": [],
    }


def addLettersToMapping(letterMapping, cipherword, candidate):
    # The letterMapping parameter is a "cipherletter mapping" dictionary

    # value that the return value of this function starts as a copy o
    # The cipherword parameter is a string value of the ciphertext word.

    # The candidate parameter is a possible English word that the

    # cipherword could decrypt to.

    # This function adds the letters of the candidate as potential

    # decryption letters for the cipherletters in the cipherletter

    # mapping.

    letterMapping = copy.deepcopy(letterMapping)

    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])

    return letterMapping


def intersectMappings(mapA, mapB):
    # To intersect two maps, create a blank map, and then add only the

    # potential decryption letters if they exist in BOTH maps.

    intersectedMapping = getBlankCipherletterMapping()

    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just

        # copy the other map entirely.

        if mapA[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapB[letter])

        elif mapB[letter] == []:
            intersectedMapping[letter] = copy.deepcopy(mapA[letter])

        else:
            # If a letter in mapA[letter] exists in mapB[letter], add

            # that letter to intersectedMapping[letter].

            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectedMapping[letter].append(mappedLetter)

    return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
    # Cipher letters in the mapping that map to only one letter are

    # "solved" and can be removed from the other letters.

    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'

    # maps to ['N'], then we know that 'B' must map to 'N', so we can

    # remove 'N' from the list of what 'A' could map to. So 'A' then maps

    # to ['M']. Note that now that 'A' maps to only one letter, we can

    # remove 'M' from the list of letters for every other

    # letter. (This is why there is a loop that keeps reducing the map.)

    letterMapping = copy.deepcopy(letterMapping)

    loopAgain = True

    while loopAgain:
        # First assume that we will not loop again:

        loopAgain = False

        # solvedLetters will be a list of uppercase letters that have one

        # and only one possible mapping in letterMapping

        solvedLetters = []

        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        # If a letter is solved, than it cannot possibly be a potential

        # decryption letter for a different ciphertext letter, so we

        # should remove it from those other lists.

        for cipherletter in LETTERS:
            for s in solvedLetters:
                if (
                    len(letterMapping[cipherletter]) != 1
                    and s in letterMapping[cipherletter]
                ):
                    letterMapping[cipherletter].remove(s)

                    if len(letterMapping[cipherletter]) == 1:
                        # A new letter is now solved, so loop again.

                        loopAgain = True

    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()

    cipherwordList = nonLettersOrSpacePattern.sub("", message.upper()).split()

    for cipherword in cipherwordList:
        # Get a new cipherletter mapping for each ciphertext word.

        newMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)

        if wordPattern not in wordPatterns.allPatterns:
            continue  # This word was not in our dictionary, so continue.

        # Add the letters of each candidate to the mapping.

        for candidate in wordPatterns.allPatterns[wordPattern]:
            newMap = addLettersToMapping(newMap, cipherword, candidate)

        # Intersect the new mapping with the existing intersected mapping.

        intersectedMap = intersectMappings(intersectedMap, newMap)

    # Remove any solved letters from the other lists.

    return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,

    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping.

    key = ["x"] * len(LETTERS)

    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.

            keyIndex = LETTERS.find(letterMapping[cipherletter][0])

            key[keyIndex] = cipherletter

        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), "_")

            ciphertext = ciphertext.replace(cipherletter.upper(), "_")

    key = "".join(key)

    # With the key we've created, decrypt the ciphertext.

    return simpleSubCipher.decryptMessage(key, ciphertext)


if __name__ == "__main__":
    main()
