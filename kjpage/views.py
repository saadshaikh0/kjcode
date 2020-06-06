from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import requests
import json
import datetime
from operator import itemgetter
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import question,answer,Student
# Create your views here.
def home(request):
    u=request.META.get("HTTP_REFERER")
    # print(u.split("/"))
    print("////////")
    print(u)
    print("########")
    return render(request,"home.html")
@login_required
def code(request):
    x=re.split("^([0-9]{1,3})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{1,3}):([0-9]{1,3}):([0-9]{1,3})\)$",request.session["timer"])
    print(x)
    return render(request,"question.html",{"time":x})
@login_required
def postdata(request):
    
    input1="1\n2\nscout\nmortal"
    output1="b"
    input2="2\n2\nsaad\nzara\n3\nfaizan\nhammad\nkartik"
    output2="b\nb"
    input3="1\n500\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\naa\nab\nac\nad\nae\naf\nag\nah\nai\naj\nak\nal\nam\nan\nao\nap\naq\nar\nas\nat\nau\nav\naw\nax\nay\naz\nba\nbb\nbc\nbd\nbe\nbf\nbg\nbh\nbi\nbj\nbk\nbl\nbm\nbn\nbo\nbp\nbq\nbr\nbs\nbt\nbu\nbv\nbw\nbx\nby\nbz\nca\ncb\ncc\ncd\nce\ncf\ncg\nch\nci\ncj\nck\ncl\ncm\ncn\nco\ncp\ncq\ncr\ncs\nct\ncu\ncv\ncw\ncx\ncy\ncz\nda\ndb\ndc\ndd\nde\ndf\ndg\ndh\ndi\ndj\ndk\ndl\ndm\ndn\ndo\ndp\ndq\ndr\nds\ndt\ndu\ndv\ndw\ndx\ndy\ndz\nea\neb\nec\ned\nee\nef\neg\neh\nei\nej\nek\nel\nem\nen\neo\nep\neq\ner\nes\net\neu\nev\new\nex\ney\nez\nfa\nfb\nfc\nfd\nfe\nff\nfg\nfh\nfi\nfj\nfk\nfl\nfm\nfn\nfo\nfp\nfq\nfr\nfs\nft\nfu\nfv\nfw\nfx\nfy\nfz\nga\ngb\ngc\ngd\nge\ngf\ngg\ngh\ngi\ngj\ngk\ngl\ngm\ngn\ngo\ngp\ngq\ngr\ngs\ngt\ngu\ngv\ngw\ngx\ngy\ngz\nha\nhb\nhc\nhd\nhe\nhf\nhg\nhh\nhi\nhj\nhk\nhl\nhm\nhn\nho\nhp\nhq\nhr\nhs\nht\nhu\nhv\nhw\nhx\nhy\nhz\nia\nib\nic\nid\nie\nif\nig\nih\nii\nij\nik\nil\nim\nin\nio\nip\niq\nir\nis\nit\niu\niv\niw\nix\niy\niz\nja\njb\njc\njd\nje\njf\njg\njh\nji\njj\njk\njl\njm\njn\njo\njp\njq\njr\njs\njt\nju\njv\njw\njx\njy\njz\nka\nkb\nkc\nkd\nke\nkf\nkg\nkh\nki\nkj\nkk\nkl\nkm\nkn\nko\nkp\nkq\nkr\nks\nkt\nku\nkv\nkw\nkx\nky\nkz\nla\nlb\nlc\nld\nle\nlf\nlg\nlh\nli\nlj\nlk\nll\nlm\nln\nlo\nlp\nlq\nlr\nls\nlt\nlu\nlv\nlw\nlx\nly\nlz\nma\nmb\nmc\nmd\nme\nmf\nmg\nmh\nmi\nmj\nmk\nml\nmm\nmn\nmo\nmp\nmq\nmr\nms\nmt\nmu\nmv\nmw\nmx\nmy\nmz\nna\nnb\nnc\nnd\nne\nnf\nng\nnh\nni\nnj\nnk\nnl\nnm\nnn\nno\nnp\nnq\nnr\nns\nnt\nnu\nnv\nnw\nnx\nny\nnz\noa\nob\noc\nod\noe\nof\nog\noh\noi\noj\nok\nol\nom\non\noo\nop\noq\nor\nos\not\nou\nov\now\nox\noy\noz\npa\npb\npc\npd\npe\npf\npg\nph\npi\npj\npk\npl\npm\npn\npo\npp\npq\npr\nps\npt\npu\npv\npw\npx\npy\npz\nqa\nqb\nqc\nqd\nqe\nqf\nqg\nqh\nqi\nqj\nqk\nql\nqm\nqn\nqo\nqp\nqq\nqr\nqs\nqt\nqu\nqv\nqw\nqx\nqy\nqz\nra\nrb\nrc\nrd\nre\nrf\nrg\nrh\nri\nrj\nrk\nrl\nrm\nrn\nro\nrp\nrq\nrr\nrs\nrt\nru\nrv\nrw\nrx\nry\nrz\nsa\nsb\nsc\nsd\nse\nsf\nsg"
    output3="sh"
    input4="1\n50\nafu\najp\nank\narf\nava\nayv\nbcq\nbgl\nbkg\nbob\nbrw\nbvr\nbzm\ncdh\nchc\nckx\ncos\ncsn\ncwi\ndad\nddy\ndht\ndlo\ndpj\ndte\ndwz\neau\neep\neik\nemf\neqa\netv\nexq\nfbl\nffg\nfjb\nfmw\nfqr\nfum\nfyh\ngcc\ngfx\ngjs\ngnn\ngri\ngvd\ngyy\nhct\nhgo\nhkj"
    output4="aa"
    input5="1\n505\ndv\nhq\nll\npg\ntb\nww\naar\naem\naih\namc\napx\nats\naxn\nbbi\nbfd\nbiy\nbmt\nbqo\nbuj\nbye\ncbz\ncfu\ncjp\ncnk\ncrf\ncva\ncyv\ndcq\ndgl\ndkg\ndob\ndrw\ndvr\ndzm\nedh\nehc\nekx\neos\nesn\newi\nfad\nfdy\nfht\nflo\nfpj\nfte\nfwz\ngau\ngep\ngik\ngmf\ngqa\ngtv\ngxq\nhbl\nhfg\nhjb\nhmw\nhqr\nhum\nhyh\nicc\nifx\nijs\ninn\niri\nivd\niyy\njct\njgo\njkj\njoe\njrz\njvu\njzp\nkdk\nkhf\nkla\nkov\nksq\nkwl\nlag\nleb\nlhw\nllr\nlpm\nlth\nlxc\nmax\nmes\nmin\nmmi\nmqd\nmty\nmxt\nnbo\nnfj\nnje\nnmz\nnqu\nnup\nnyk\nocf\noga\nojv\nonq\norl\novg\nozb\npcw\npgr\npkm\npoh\npsc\npvx\npzs\nqdn\nqhi\nqld\nqoy\nqst\nqwo\nraj\nree\nrhz\nrlu\nrpp\nrtk\nrxf\nsba\nsev\nsiq\nsml\nsqg\nsub\nsxw\ntbr\ntfm\ntjh\ntnc\ntqx\ntus\ntyn\nuci\nugd\nujy\nunt\nuro\nuvj\nuze\nvcz\nvgu\nvkp\nvok\nvsf\nvwa\nvzv\nwdq\nwhl\nwlg\nwpb\nwsw\nwwr\nxam\nxeh\nxic\nxlx\nxps\nxtn\nxxi\nybd\nyey\nyit\nymo\nyqj\nyue\nyxz\nzbu\nzfp\nzjk\nznf\nzra\nzuv\nzyq\naacl\naagg\naakb\naanw\naarr\naavm\naazh\nabdc\nabgx\nabks\nabon\nabsi\nabwd\nabzy\nacdt\nacho\naclj\nacpe\nacsz\nacwu\nadap\nadek\nadif\nadma\nadpv\nadtq\nadxl\naebg\naefb\naeiw\naemr\naeqm\naeuh\naeyc\nafbx\naffs\nafjn\nafni\nafrd\nafuy\nafyt\nagco\naggj\nagke\nagnz\nagru\nagvp\nagzk\nahdf\nahha\nahkv\nahoq\nahsl\nahwg\naiab\naidw\naihr\nailm\naiph\naitc\naiwx\najas\najen\najii\najmd\najpy\najtt\najxo\nakbj\nakfe\nakiz\nakmu\nakqp\nakuk\nakyf\nalca\nalfv\naljq\nalnl\nalrg\nalvb\nalyw\namcr\namgm\namkh\namoc\namrx\namvs\namzn\nandi\nanhd\nanky\nanot\nanso\nanwj\naoae\naodz\naohu\naolp\naopk\naotf\naoxa\napav\napeq\napil\napmg\napqb\naptw\napxr\naqbm\naqfh\naqjc\naqmx\naqqs\naqun\naqyi\narcd\narfy\narjt\narno\narrj\narve\naryz\nascu\nasgp\naskk\nasof\nassa\nasvv\naszq\natdl\nathg\natlb\natow\natsr\natwm\nauah\nauec\nauhx\nauls\naupn\nauti\nauxd\navay\navet\navio\navmj\navqe\navtz\navxu\nawbp\nawfk\nawjf\nawna\nawqv\nawuq\nawyl\naxcg\naxgb\naxjw\naxnr\naxrm\naxvh\naxzc\naycx\naygs\naykn\nayoi\naysd\nayvy\nayzt\nazdo\nazhj\nazle\nazoz\nazsu\nazwp\nbaak\nbaef\nbaia\nbalv\nbapq\nbatl\nbaxg\nbbbb\nbbew\nbbir\nbbmm\nbbqh\nbbuc\nbbxx\nbcbs\nbcfn\nbcji\nbcnd\nbcqy\nbcut\nbcyo\nbdcj\nbdge\nbdjz\nbdnu\nbdrp\nbdvk\nbdzf\nbeda\nbegv\nbekq\nbeol\nbesg\nbewb\nbezw\nbfdr\nbfhm\nbflh\nbfpc\nbfsx\nbfws\nbgan\nbgei\nbgid\nbgly\nbgpt\nbgto\nbgxj\nbhbe\nbhez\nbhiu\nbhmp\nbhqk\nbhuf\nbhya\nbibv\nbifq\nbijl\nbing\nbirb\nbiuw\nbiyr\nbjcm\nbjgh\nbjkc\nbjnx\nbjrs\nbjvn\nbjzi\nbkdd\nbkgy\nbkkt\nbkoo\nbksj\nbkwe\nbkzz\nbldu\nblhp\nbllk\nblpf\nblta\nblwv\nbmaq\nbmel\nbmig\nbmmb\nbmpw\nbmtr\nbmxm\nbnbh\nbnfc\nbnix\nbnms\nbnqn\nbnui\nbnyd\nboby\nboft\nbojo\nbonj\nbore\nbouz\nboyu\nbpcp\nbpgk\nbpkf\nbpoa\nbprv\nbpvq\nbpzl\nbqdg\nbqhb\nbqkw\nbqor\nbqsm\nbqwh\nbrac\nbrdx\nbrhs\nbrln\nbrpi\nbrtd\nbrwy\nbsat\nbseo\nbsij\nbsme\nbspz\nbstu\nbsxp\nbtbk\nbtff\nbtja\nbtmv\nbtqq\nbtul\nbtyg\nbucb\nbufw\nbujr\nbunm\nburh\nbuvc\nbuyx"
    output5="ce"
    input6="1\n500\naotp\nbdoe\nbsit\nchdi\ncvxx\ndksm\ndznb\neohq\nfdcf\nfrwu\nggrj\ngvly\nhkgn\nhzbc\ninvr\njcqg\njrkv\nkgfk\nkuzz\nljuo\nlypd\nmnjs\nnceh\nnqyw\noftl\nouoa\npjip\npyde\nqmxt\nrbsi\nrqmx\nsfhm\nsucb\ntiwq\ntxrf\numlu\nvbgj\nvqay\nwevn\nwtqc\nxikr\nxxfg\nylzv\nzauk\nzpoz\naaejo\naated\nabhys\nabwth\naclnw\nadail\nadpda\naedxp\naesse\nafhmt\nafwhi\naglbx\nagzwm\nahorb\naidlq\naisgf\najhau\najvvj\nakkpy\nakzkn\nalofc\namczr\namrug\nangov\nanvjk\naokdz\naoyyo\napntd\naqcns\naqrih\nargcw\naruxl\nasjsa\nasymp\natnhe\naucbt\nauqwi\navfqx\navulm\nawjgb\nawyaq\naxmvf\naybpu\nayqkj\nazfey\naztzn\nbaiuc\nbaxor\nbbmjg\nbcbdv\nbcpyk\nbdesz\nbdtno\nbeiid\nbexcs\nbflxh\nbgarw\nbgpml\nbheha\nbhtbp\nbihwe\nbiwqt\nbjlli\nbkafx\nbkpam\nbldvb\nblspq\nbmhkf\nbmweu\nbnkzj\nbnzty\nbooon\nbpdjc\nbpsdr\nbqgyg\nbqvsv\nbrknk\nbrzhz\nbsoco\nbtcxd\nbtrrs\nbugmh\nbuvgw\nbvkbl\nbvywa\nbwnqp\nbxcle\nbxrft\nbygai\nbyuux\nbzjpm\nbzykb\ncaneq\ncbbzf\ncbqtu\nccfoj\nccuiy\ncdjdn\ncdxyc\ncemsr\ncfbng\ncfqhv\ncgfck\ncgtwz\nchiro\nchxmd\ncimgs\ncjbbh\ncjpvw\nckeql\ncktla\nclifp\nclxae\ncmlut\ncnapi\ncnpjx\ncoeem\ncoszb\ncphtq\ncpwof\ncqliu\ncradj\ncroxy\ncsdsn\ncssnc\ncthhr\nctwcg\ncukwv\ncuzrk\ncvolz\ncwdgo\ncwsbd\ncxgvs\ncxvqh\ncykkw\ncyzfl\nczoaa\ndacup\ndarpe\ndbgjt\ndbvei\ndcjyx\ndcytm\nddnob\ndeciq\nderdf\ndffxu\ndfusj\ndgjmy\ndgyhn\ndhncc\ndibwr\ndiqrg\ndjflv\ndjugk\ndkjaz\ndkxvo\ndlmqd\ndmbks\ndmqfh\ndnezw\ndntul\ndoipa\ndoxjp\ndpmee\ndqayt\ndqpti\ndrenx\ndrtim\ndsidb\ndswxq\ndtlsf\nduamu\nduphj\ndveby\ndvswn\ndwhrc\ndwwlr\ndxlgg\ndyaav\ndyovk\ndzdpz\ndzsko\neahfd\neavzs\nebkuh\nebzow\necojl\neddea\nedryp\neegte\neevnt\nefkii\nefzcx\negnxm\nehcsb\nehrmq\neighf\neivbu\nejjwj\nejyqy\neknln\nelcgc\nelrar\nemfvg\nemupv\nenjkk\nenyez\neomzo\nepbud\nepqos\neqfjh\nequdw\neriyl\nerxta\nesmnp\netbie\netqct\neuexi\neutrx\nevimm\nevxhb\newmbq\nexawf\nexpqu\neyelj\neytfy\nezian\nezwvc\nfalpr\nfbakg\nfbpev\nfcdzk\nfcstz\nfdhoo\nfdwjd\nfelds\nfezyh\nffosw\nfgdnl\nfgsia\nfhhcp\nfhvxe\nfikrt\nfizmi\nfjogx\nfkdbm\nfkrwb\nflgqq\nflvlf\nfmkfu\nfmzaj\nfnnuy\nfocpn\nforkc\nfpger\nfpuzg\nfqjtv\nfqyok\nfrniz\nfscdo\nfsqyd\nftfss\nftunh\nfujhw\nfuycl\nfvmxa\nfwbrp\nfwqme\nfxfgt\nfxubi\nfyivx\nfyxqm\nfzmlb\ngabfq\ngaqaf\ngbeuu\ngbtpj\ngcijy\ngcxen\ngdlzc\ngeatr\ngepog\ngfeiv\ngftdk\ngghxz\nggwso\nghlnd\ngiahs\ngipch\ngjdww\ngjsrl\ngkhma\ngkwgp\ngllbe\nglzvt\ngmoqi\ngndkx\ngnsfm\ngohab\ngovuq\ngpkpf\ngpzju\ngqoej\ngrcyy\ngrrtn\ngsgoc\ngsvir\ngtkdg\ngtyxv\ngunsk\ngvcmz\ngvrho\ngwgcd\ngwuws\ngxjrh\ngxylw\ngyngl\ngzcba\ngzqvp\nhafqe\nhaukt\nhbjfi\nhbxzx\nhcmum\nhdbpb\nhdqjq\nhefef\nhetyu\nhfitj\nhfxny\nhgmin\nhhbdc\nhhpxr\nhiesg\nhitmv\nhjihk\nhjxbz\nhklwo\nhlard\nhlpls\nhmegh\nhmtaw\nhnhvl\nhnwqa\nholkp\nhpafe\nhpozt\nhqdui\nhqsox\nhrhjm\nhrweb\nhskyq\nhsztf\nhtonu\nhudij\nhuscy\nhvgxn\nhvvsc\nhwkmr\nhwzhg\nhxobv\nhycwk\nhyrqz\nhzglo\nhzvgd\niakas\niayvh\nibnpw\nicckl\nicrfa\nidfzp\niduue\niejot\nieyji\nifndx\nigbym\nigqtb\nihfnq\nihuif\niijcu\niixxj\nijmry\nikbmn\nikqhc\nilfbr\niltwg\nimiqv\nimxlk\ninmfz\niobao\niopvd\nipeps\niptkh\niqiew\niqwzl\nirlua\nisaop\nispje\nitedt\nitsyi\niuhsx\niuwnm\nivlib\niwacq\niwoxf\nixdru\nixsmj\niyhgy\niywbn\nizkwc\nizzqr\njaolg\njbdfv\njbsak\njcguz\njcvpo\njdkkd\njdzes\njenzh\njfctw\njfrol\njggja\njgvdp\njhjye\njhyst\njinni\njjchx\njjrcm\njkfxb\njkurq\njljmf\njlygu\njmnbj\njnbvy\njnqqn\njoflc\njoufr\njpjag\njpxuv\njqmpk\njrbjz\njrqeo\njsezd\njstts\njtioh\njtxiw\njumdl\njvaya\njvpsp\njwene\njwtht\njxici\njxwwx\njylrm"
    output6="lh"
    input7="4\n2\nsaad\nfaizan\n3\nprtiksha\nshezy\nzeba\n3\nbhagesh\nxylo\nrealmadrid\n2\nred\nblue"
    output7="b\nc\nc\na"
    input8="1\n1\nshezaad"
    output8="b"
    input9="1\n500\napproval\nanalysis\nalarm\naware\nargument\nambiguous\nabsence\nassessment\nacid\narrow\naccompany\navailable\nachievement\nannual\naffect\nattraction\nadventure\nan\nangel\narena\nanalyst\nanger\nafford\nallow\nabsorb\nartificial\naddition\naid\nalive\nauthorise\nant\narrest\naddicted\nancestor\nair\nappendix\nassume\nabundant\nadd\nattack\nally\naspect\nage\nample\naccent\nadvertising\nambition\nadmire\nagenda\nanimal\nbrain\nbuttocks\nbudge\nbraid\nbeginning\nbless\nbeautiful\nbiscuit\nbar\nbring\nblank\nbay\nboy\nbrush\nbury\nbanana\nbehave\nbolt\nbuffet\nban\nbounce\nbill\nbeneficiary\nbattlefield\nbasketball\nback\nbudget\nbold\nblame\nbuy\nbackground\nbottom\nbark\nBible\nbag\nburst\nbitter\nboat\nbiography\nbrink\nbulb\nbiology\nbucket\nbeef\nbarrier\nbelt\nbulletin\nbacon\nbarrel\nbike\ncommand\ncell\ncare\nconfusion\ncontract\ncorrection\ncook\ncentral\ncredibility\ncustody\nchord\ncontent\ncheck\nchampagne\nchauvinist\ncollapse\ncupboard\ncontraction\ncoma\ncheat\ncourage\ncool\ncomplex\nclash\ncharge\ncoast\ncage\ncontext\nclub\nclear\ncalf\nconfession\ncritical\ncultivate\nconvulsion\nclock\ncomplication\nchange\ncheese\ncoverage\nchurch\ncrash\ncomment\ncry\ncertain\nconversation\ncentury\nclimate\nclaim\ncompetition\nquaint\nqualification\nquit\nqueen\nquarter\nqualify\nquarrel\nquality\nquota\nquantity\nquiet\nquest\nqueue\nquote\nquotation\nquestion\nqualified\ngrass\ngrief\ngain\nglacier\ngrain\nglove\nguide\ngrind\ngeneration\ngoat\ngalaxy\ngown\ngift\nglare\nground\nglimpse\ngrimace\nglance\ngirl\ngas\ngiant\nguerrilla\nguitar\ngallon\ngrip\ngod\nguideline\ngasp\ngreen\ngood\ngreat\ngirlfriend\ngrant\ngun\nglory\nglue\ngossip\ngradient\nglasses\ngutter\ngaffe\ngo\ngenuine\ngenetic\ngrace\nguarantee\ngraduate\ngem\ngregarious\ngarbage\ndegree\ndistrict\ndeer\ndetail\ndrawer\ndisaster\ndemonstration\ndollar\ndeprivation\ndismissal\ndress\ndemonstrator\ndo\ndeprive\nduty\ndisappointment\ndeposit\ndrive\ndifficulty\ndecay\ndoubt\ndistribute\ndominate\ndominant\ndip\ndish\ndaughter\ndiameter\ndirection\ndividend\ndeficiency\ndrawing\ndecade\ndanger\ndrama\nduke\ndistortion\ndespise\ndrink\ndistinct\ndentist\ndespair\ndrag\ndictionary\ndealer\ndeport\ndiet\ndeny\ndecoration\ndorm\nfence\nfavorable\nfastidious\nflawed\nfunctional\nfilm\nfee\nfortune\nfame\nforbid\nforestry\nfreight\nfolklore\nfuel\nflow\nfill\nfox\nfixture\nfeedback\nfear\nfeign\nflag\nfeed\nfraud\nfoundation\nfalsify\nfavourite\nflush\nflu\nfairy\nfork\nfly\nfood\nfirst\nfur\nfriend\nfolk\nfar\nfinal\nfoot\nfreighter\nforest\nfall\nfacility\nfinance\nfailure\nfamily\nfix\nfactory\nfeast\nleak\nloud\nlandowner\nlog\nlocation\nliterature\nlong\nloose\nlump\nlesson\nlatest\nlion\nleader\nliberty\nliability\nleft\nlounge\nlean\nlost\nloan\nlimit\nlayout\nlily\nletter\nlike\nleftovers\nlover\nlate\nlose\nlaw\nlay\nlight\nlooting\nleave\nlanguage\nlemon\nlip\nlead\nlandscape\nlaser\nloss\nlack\nlicense\nlearn\nlecture\nlaundry\nlineage\nloop\nlisten\nlink\njournal\njet\njudge\njurisdiction\njealous\njob\njungle\njoint\njump\njudgment\njaw\njoystick\njacket\njelly\njudicial\njunior\njewel\njoy\njail\njury\njust\njustify\njam\njockey\njustice\njoke\njest\nnervous\nnotice\nnuclear\nnavy\nnews\nnest\nnap\nnomination\nnationalist\nnotorious\nnonsense\nnuance\nneedle\nnonremittal\nneighborhood\nneck\nnotion\nnature\nnetwork\nnarrow\nneglect\nnote\nno\nnorm\nnecklace\nneutral\nnightmare\nnoise\nnerve\nnorth\nname\nneed\nnail\nnegligence\nnew\nneighbour\nnotebook\nnumber\nnose\nnet\nnun\nnormal\nnursery\nnut\nnational\nnovel\nnegotiation\nnoble\nnative\nnight\npolish\npacket\nprivate\npath\nperformance\npriority\nproportion\npride\nprosecute\nprogressive\nperforate\npneumonia\nplagiarize\npolite\npurpose\npig\npopulation\npeace\npen\npermission\nproclaim\nproud\npollution\nprovide\nportrait\nproposal\npassage\nphysical\nprovincial\nprecedent\npipe\npoison\npoint\npositive\nprinciple\npreoccupation\npay\nprotection\npool\nplant\nplatform\nplease\nproject\nprefer\npolicy\npray\npublisher\npartner\npit\nperformer\naa\nab\nac\nad\na\na"
    output9="ae"
     # "b\n",
            # "b\nb\n",
            # "sh\n",
            # "aa\n",
            # "ce\n",
            # "lh\n",
            # "b\nc\nc\na\n",
            # "b\n",
            # "ae\n",
    input_array=[
        # "1\n2\nscout\nmortal",
        # "2\n2\nsaad\nzara\n3\nfaizan\nhammad\nkartik",
        "1\n500\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\naa\nab\nac\nad\nae\naf\nag\nah\nai\naj\nak\nal\nam\nan\nao\nap\naq\nar\nas\nat\nau\nav\naw\nax\nay\naz\nba\nbb\nbc\nbd\nbe\nbf\nbg\nbh\nbi\nbj\nbk\nbl\nbm\nbn\nbo\nbp\nbq\nbr\nbs\nbt\nbu\nbv\nbw\nbx\nby\nbz\nca\ncb\ncc\ncd\nce\ncf\ncg\nch\nci\ncj\nck\ncl\ncm\ncn\nco\ncp\ncq\ncr\ncs\nct\ncu\ncv\ncw\ncx\ncy\ncz\nda\ndb\ndc\ndd\nde\ndf\ndg\ndh\ndi\ndj\ndk\ndl\ndm\ndn\ndo\ndp\ndq\ndr\nds\ndt\ndu\ndv\ndw\ndx\ndy\ndz\nea\neb\nec\ned\nee\nef\neg\neh\nei\nej\nek\nel\nem\nen\neo\nep\neq\ner\nes\net\neu\nev\new\nex\ney\nez\nfa\nfb\nfc\nfd\nfe\nff\nfg\nfh\nfi\nfj\nfk\nfl\nfm\nfn\nfo\nfp\nfq\nfr\nfs\nft\nfu\nfv\nfw\nfx\nfy\nfz\nga\ngb\ngc\ngd\nge\ngf\ngg\ngh\ngi\ngj\ngk\ngl\ngm\ngn\ngo\ngp\ngq\ngr\ngs\ngt\ngu\ngv\ngw\ngx\ngy\ngz\nha\nhb\nhc\nhd\nhe\nhf\nhg\nhh\nhi\nhj\nhk\nhl\nhm\nhn\nho\nhp\nhq\nhr\nhs\nht\nhu\nhv\nhw\nhx\nhy\nhz\nia\nib\nic\nid\nie\nif\nig\nih\nii\nij\nik\nil\nim\nin\nio\nip\niq\nir\nis\nit\niu\niv\niw\nix\niy\niz\nja\njb\njc\njd\nje\njf\njg\njh\nji\njj\njk\njl\njm\njn\njo\njp\njq\njr\njs\njt\nju\njv\njw\njx\njy\njz\nka\nkb\nkc\nkd\nke\nkf\nkg\nkh\nki\nkj\nkk\nkl\nkm\nkn\nko\nkp\nkq\nkr\nks\nkt\nku\nkv\nkw\nkx\nky\nkz\nla\nlb\nlc\nld\nle\nlf\nlg\nlh\nli\nlj\nlk\nll\nlm\nln\nlo\nlp\nlq\nlr\nls\nlt\nlu\nlv\nlw\nlx\nly\nlz\nma\nmb\nmc\nmd\nme\nmf\nmg\nmh\nmi\nmj\nmk\nml\nmm\nmn\nmo\nmp\nmq\nmr\nms\nmt\nmu\nmv\nmw\nmx\nmy\nmz\nna\nnb\nnc\nnd\nne\nnf\nng\nnh\nni\nnj\nnk\nnl\nnm\nnn\nno\nnp\nnq\nnr\nns\nnt\nnu\nnv\nnw\nnx\nny\nnz\noa\nob\noc\nod\noe\nof\nog\noh\noi\noj\nok\nol\nom\non\noo\nop\noq\nor\nos\not\nou\nov\now\nox\noy\noz\npa\npb\npc\npd\npe\npf\npg\nph\npi\npj\npk\npl\npm\npn\npo\npp\npq\npr\nps\npt\npu\npv\npw\npx\npy\npz\nqa\nqb\nqc\nqd\nqe\nqf\nqg\nqh\nqi\nqj\nqk\nql\nqm\nqn\nqo\nqp\nqq\nqr\nqs\nqt\nqu\nqv\nqw\nqx\nqy\nqz\nra\nrb\nrc\nrd\nre\nrf\nrg\nrh\nri\nrj\nrk\nrl\nrm\nrn\nro\nrp\nrq\nrr\nrs\nrt\nru\nrv\nrw\nrx\nry\nrz\nsa\nsb\nsc\nsd\nse\nsf\nsg",
        # "1\n50\nafu\najp\nank\narf\nava\nayv\nbcq\nbgl\nbkg\nbob\nbrw\nbvr\nbzm\ncdh\nchc\nckx\ncos\ncsn\ncwi\ndad\nddy\ndht\ndlo\ndpj\ndte\ndwz\neau\neep\neik\nemf\neqa\netv\nexq\nfbl\nffg\nfjb\nfmw\nfqr\nfum\nfyh\ngcc\ngfx\ngjs\ngnn\ngri\ngvd\ngyy\nhct\nhgo\nhkj",
       # "1\n505\ndv\nhq\nll\npg\ntb\nww\naar\naem\naih\namc\napx\nats\naxn\nbbi\nbfd\nbiy\nbmt\nbqo\nbuj\nbye\ncbz\ncfu\ncjp\ncnk\ncrf\ncva\ncyv\ndcq\ndgl\ndkg\ndob\ndrw\ndvr\ndzm\nedh\nehc\nekx\neos\nesn\newi\nfad\nfdy\nfht\nflo\nfpj\nfte\nfwz\ngau\ngep\ngik\ngmf\ngqa\ngtv\ngxq\nhbl\nhfg\nhjb\nhmw\nhqr\nhum\nhyh\nicc\nifx\nijs\ninn\niri\nivd\niyy\njct\njgo\njkj\njoe\njrz\njvu\njzp\nkdk\nkhf\nkla\nkov\nksq\nkwl\nlag\nleb\nlhw\nllr\nlpm\nlth\nlxc\nmax\nmes\nmin\nmmi\nmqd\nmty\nmxt\nnbo\nnfj\nnje\nnmz\nnqu\nnup\nnyk\nocf\noga\nojv\nonq\norl\novg\nozb\npcw\npgr\npkm\npoh\npsc\npvx\npzs\nqdn\nqhi\nqld\nqoy\nqst\nqwo\nraj\nree\nrhz\nrlu\nrpp\nrtk\nrxf\nsba\nsev\nsiq\nsml\nsqg\nsub\nsxw\ntbr\ntfm\ntjh\ntnc\ntqx\ntus\ntyn\nuci\nugd\nujy\nunt\nuro\nuvj\nuze\nvcz\nvgu\nvkp\nvok\nvsf\nvwa\nvzv\nwdq\nwhl\nwlg\nwpb\nwsw\nwwr\nxam\nxeh\nxic\nxlx\nxps\nxtn\nxxi\nybd\nyey\nyit\nymo\nyqj\nyue\nyxz\nzbu\nzfp\nzjk\nznf\nzra\nzuv\nzyq\naacl\naagg\naakb\naanw\naarr\naavm\naazh\nabdc\nabgx\nabks\nabon\nabsi\nabwd\nabzy\nacdt\nacho\naclj\nacpe\nacsz\nacwu\nadap\nadek\nadif\nadma\nadpv\nadtq\nadxl\naebg\naefb\naeiw\naemr\naeqm\naeuh\naeyc\nafbx\naffs\nafjn\nafni\nafrd\nafuy\nafyt\nagco\naggj\nagke\nagnz\nagru\nagvp\nagzk\nahdf\nahha\nahkv\nahoq\nahsl\nahwg\naiab\naidw\naihr\nailm\naiph\naitc\naiwx\najas\najen\najii\najmd\najpy\najtt\najxo\nakbj\nakfe\nakiz\nakmu\nakqp\nakuk\nakyf\nalca\nalfv\naljq\nalnl\nalrg\nalvb\nalyw\namcr\namgm\namkh\namoc\namrx\namvs\namzn\nandi\nanhd\nanky\nanot\nanso\nanwj\naoae\naodz\naohu\naolp\naopk\naotf\naoxa\napav\napeq\napil\napmg\napqb\naptw\napxr\naqbm\naqfh\naqjc\naqmx\naqqs\naqun\naqyi\narcd\narfy\narjt\narno\narrj\narve\naryz\nascu\nasgp\naskk\nasof\nassa\nasvv\naszq\natdl\nathg\natlb\natow\natsr\natwm\nauah\nauec\nauhx\nauls\naupn\nauti\nauxd\navay\navet\navio\navmj\navqe\navtz\navxu\nawbp\nawfk\nawjf\nawna\nawqv\nawuq\nawyl\naxcg\naxgb\naxjw\naxnr\naxrm\naxvh\naxzc\naycx\naygs\naykn\nayoi\naysd\nayvy\nayzt\nazdo\nazhj\nazle\nazoz\nazsu\nazwp\nbaak\nbaef\nbaia\nbalv\nbapq\nbatl\nbaxg\nbbbb\nbbew\nbbir\nbbmm\nbbqh\nbbuc\nbbxx\nbcbs\nbcfn\nbcji\nbcnd\nbcqy\nbcut\nbcyo\nbdcj\nbdge\nbdjz\nbdnu\nbdrp\nbdvk\nbdzf\nbeda\nbegv\nbekq\nbeol\nbesg\nbewb\nbezw\nbfdr\nbfhm\nbflh\nbfpc\nbfsx\nbfws\nbgan\nbgei\nbgid\nbgly\nbgpt\nbgto\nbgxj\nbhbe\nbhez\nbhiu\nbhmp\nbhqk\nbhuf\nbhya\nbibv\nbifq\nbijl\nbing\nbirb\nbiuw\nbiyr\nbjcm\nbjgh\nbjkc\nbjnx\nbjrs\nbjvn\nbjzi\nbkdd\nbkgy\nbkkt\nbkoo\nbksj\nbkwe\nbkzz\nbldu\nblhp\nbllk\nblpf\nblta\nblwv\nbmaq\nbmel\nbmig\nbmmb\nbmpw\nbmtr\nbmxm\nbnbh\nbnfc\nbnix\nbnms\nbnqn\nbnui\nbnyd\nboby\nboft\nbojo\nbonj\nbore\nbouz\nboyu\nbpcp\nbpgk\nbpkf\nbpoa\nbprv\nbpvq\nbpzl\nbqdg\nbqhb\nbqkw\nbqor\nbqsm\nbqwh\nbrac\nbrdx\nbrhs\nbrln\nbrpi\nbrtd\nbrwy\nbsat\nbseo\nbsij\nbsme\nbspz\nbstu\nbsxp\nbtbk\nbtff\nbtja\nbtmv\nbtqq\nbtul\nbtyg\nbucb\nbufw\nbujr\nbunm\nburh\nbuvc\nbuyx",
        "1\n500\naotp\nbdoe\nbsit\nchdi\ncvxx\ndksm\ndznb\neohq\nfdcf\nfrwu\nggrj\ngvly\nhkgn\nhzbc\ninvr\njcqg\njrkv\nkgfk\nkuzz\nljuo\nlypd\nmnjs\nnceh\nnqyw\noftl\nouoa\npjip\npyde\nqmxt\nrbsi\nrqmx\nsfhm\nsucb\ntiwq\ntxrf\numlu\nvbgj\nvqay\nwevn\nwtqc\nxikr\nxxfg\nylzv\nzauk\nzpoz\naaejo\naated\nabhys\nabwth\naclnw\nadail\nadpda\naedxp\naesse\nafhmt\nafwhi\naglbx\nagzwm\nahorb\naidlq\naisgf\najhau\najvvj\nakkpy\nakzkn\nalofc\namczr\namrug\nangov\nanvjk\naokdz\naoyyo\napntd\naqcns\naqrih\nargcw\naruxl\nasjsa\nasymp\natnhe\naucbt\nauqwi\navfqx\navulm\nawjgb\nawyaq\naxmvf\naybpu\nayqkj\nazfey\naztzn\nbaiuc\nbaxor\nbbmjg\nbcbdv\nbcpyk\nbdesz\nbdtno\nbeiid\nbexcs\nbflxh\nbgarw\nbgpml\nbheha\nbhtbp\nbihwe\nbiwqt\nbjlli\nbkafx\nbkpam\nbldvb\nblspq\nbmhkf\nbmweu\nbnkzj\nbnzty\nbooon\nbpdjc\nbpsdr\nbqgyg\nbqvsv\nbrknk\nbrzhz\nbsoco\nbtcxd\nbtrrs\nbugmh\nbuvgw\nbvkbl\nbvywa\nbwnqp\nbxcle\nbxrft\nbygai\nbyuux\nbzjpm\nbzykb\ncaneq\ncbbzf\ncbqtu\nccfoj\nccuiy\ncdjdn\ncdxyc\ncemsr\ncfbng\ncfqhv\ncgfck\ncgtwz\nchiro\nchxmd\ncimgs\ncjbbh\ncjpvw\nckeql\ncktla\nclifp\nclxae\ncmlut\ncnapi\ncnpjx\ncoeem\ncoszb\ncphtq\ncpwof\ncqliu\ncradj\ncroxy\ncsdsn\ncssnc\ncthhr\nctwcg\ncukwv\ncuzrk\ncvolz\ncwdgo\ncwsbd\ncxgvs\ncxvqh\ncykkw\ncyzfl\nczoaa\ndacup\ndarpe\ndbgjt\ndbvei\ndcjyx\ndcytm\nddnob\ndeciq\nderdf\ndffxu\ndfusj\ndgjmy\ndgyhn\ndhncc\ndibwr\ndiqrg\ndjflv\ndjugk\ndkjaz\ndkxvo\ndlmqd\ndmbks\ndmqfh\ndnezw\ndntul\ndoipa\ndoxjp\ndpmee\ndqayt\ndqpti\ndrenx\ndrtim\ndsidb\ndswxq\ndtlsf\nduamu\nduphj\ndveby\ndvswn\ndwhrc\ndwwlr\ndxlgg\ndyaav\ndyovk\ndzdpz\ndzsko\neahfd\neavzs\nebkuh\nebzow\necojl\neddea\nedryp\neegte\neevnt\nefkii\nefzcx\negnxm\nehcsb\nehrmq\neighf\neivbu\nejjwj\nejyqy\neknln\nelcgc\nelrar\nemfvg\nemupv\nenjkk\nenyez\neomzo\nepbud\nepqos\neqfjh\nequdw\neriyl\nerxta\nesmnp\netbie\netqct\neuexi\neutrx\nevimm\nevxhb\newmbq\nexawf\nexpqu\neyelj\neytfy\nezian\nezwvc\nfalpr\nfbakg\nfbpev\nfcdzk\nfcstz\nfdhoo\nfdwjd\nfelds\nfezyh\nffosw\nfgdnl\nfgsia\nfhhcp\nfhvxe\nfikrt\nfizmi\nfjogx\nfkdbm\nfkrwb\nflgqq\nflvlf\nfmkfu\nfmzaj\nfnnuy\nfocpn\nforkc\nfpger\nfpuzg\nfqjtv\nfqyok\nfrniz\nfscdo\nfsqyd\nftfss\nftunh\nfujhw\nfuycl\nfvmxa\nfwbrp\nfwqme\nfxfgt\nfxubi\nfyivx\nfyxqm\nfzmlb\ngabfq\ngaqaf\ngbeuu\ngbtpj\ngcijy\ngcxen\ngdlzc\ngeatr\ngepog\ngfeiv\ngftdk\ngghxz\nggwso\nghlnd\ngiahs\ngipch\ngjdww\ngjsrl\ngkhma\ngkwgp\ngllbe\nglzvt\ngmoqi\ngndkx\ngnsfm\ngohab\ngovuq\ngpkpf\ngpzju\ngqoej\ngrcyy\ngrrtn\ngsgoc\ngsvir\ngtkdg\ngtyxv\ngunsk\ngvcmz\ngvrho\ngwgcd\ngwuws\ngxjrh\ngxylw\ngyngl\ngzcba\ngzqvp\nhafqe\nhaukt\nhbjfi\nhbxzx\nhcmum\nhdbpb\nhdqjq\nhefef\nhetyu\nhfitj\nhfxny\nhgmin\nhhbdc\nhhpxr\nhiesg\nhitmv\nhjihk\nhjxbz\nhklwo\nhlard\nhlpls\nhmegh\nhmtaw\nhnhvl\nhnwqa\nholkp\nhpafe\nhpozt\nhqdui\nhqsox\nhrhjm\nhrweb\nhskyq\nhsztf\nhtonu\nhudij\nhuscy\nhvgxn\nhvvsc\nhwkmr\nhwzhg\nhxobv\nhycwk\nhyrqz\nhzglo\nhzvgd\niakas\niayvh\nibnpw\nicckl\nicrfa\nidfzp\niduue\niejot\nieyji\nifndx\nigbym\nigqtb\nihfnq\nihuif\niijcu\niixxj\nijmry\nikbmn\nikqhc\nilfbr\niltwg\nimiqv\nimxlk\ninmfz\niobao\niopvd\nipeps\niptkh\niqiew\niqwzl\nirlua\nisaop\nispje\nitedt\nitsyi\niuhsx\niuwnm\nivlib\niwacq\niwoxf\nixdru\nixsmj\niyhgy\niywbn\nizkwc\nizzqr\njaolg\njbdfv\njbsak\njcguz\njcvpo\njdkkd\njdzes\njenzh\njfctw\njfrol\njggja\njgvdp\njhjye\njhyst\njinni\njjchx\njjrcm\njkfxb\njkurq\njljmf\njlygu\njmnbj\njnbvy\njnqqn\njoflc\njoufr\njpjag\njpxuv\njqmpk\njrbjz\njrqeo\njsezd\njstts\njtioh\njtxiw\njumdl\njvaya\njvpsp\njwene\njwtht\njxici\njxwwx\njylrm",
        "4\n2\nsaad\nfaizan\n3\nprtiksha\nshezy\nzeba\n3\nbhagesh\nxylo\nrealmadrid\n2\nred\nblue",
        # "1\n1\nshezaad",
        # "1\n500\napproval\nanalysis\nalarm\naware\nargument\nambiguous\nabsence\nassessment\nacid\narrow\naccompany\navailable\nachievement\nannual\naffect\nattraction\nadventure\nan\nangel\narena\nanalyst\nanger\nafford\nallow\nabsorb\nartificial\naddition\naid\nalive\nauthorise\nant\narrest\naddicted\nancestor\nair\nappendix\nassume\nabundant\nadd\nattack\nally\naspect\nage\nample\naccent\nadvertising\nambition\nadmire\nagenda\nanimal\nbrain\nbuttocks\nbudge\nbraid\nbeginning\nbless\nbeautiful\nbiscuit\nbar\nbring\nblank\nbay\nboy\nbrush\nbury\nbanana\nbehave\nbolt\nbuffet\nban\nbounce\nbill\nbeneficiary\nbattlefield\nbasketball\nback\nbudget\nbold\nblame\nbuy\nbackground\nbottom\nbark\nBible\nbag\nburst\nbitter\nboat\nbiography\nbrink\nbulb\nbiology\nbucket\nbeef\nbarrier\nbelt\nbulletin\nbacon\nbarrel\nbike\ncommand\ncell\ncare\nconfusion\ncontract\ncorrection\ncook\ncentral\ncredibility\ncustody\nchord\ncontent\ncheck\nchampagne\nchauvinist\ncollapse\ncupboard\ncontraction\ncoma\ncheat\ncourage\ncool\ncomplex\nclash\ncharge\ncoast\ncage\ncontext\nclub\nclear\ncalf\nconfession\ncritical\ncultivate\nconvulsion\nclock\ncomplication\nchange\ncheese\ncoverage\nchurch\ncrash\ncomment\ncry\ncertain\nconversation\ncentury\nclimate\nclaim\ncompetition\nquaint\nqualification\nquit\nqueen\nquarter\nqualify\nquarrel\nquality\nquota\nquantity\nquiet\nquest\nqueue\nquote\nquotation\nquestion\nqualified\ngrass\ngrief\ngain\nglacier\ngrain\nglove\nguide\ngrind\ngeneration\ngoat\ngalaxy\ngown\ngift\nglare\nground\nglimpse\ngrimace\nglance\ngirl\ngas\ngiant\nguerrilla\nguitar\ngallon\ngrip\ngod\nguideline\ngasp\ngreen\ngood\ngreat\ngirlfriend\ngrant\ngun\nglory\nglue\ngossip\ngradient\nglasses\ngutter\ngaffe\ngo\ngenuine\ngenetic\ngrace\nguarantee\ngraduate\ngem\ngregarious\ngarbage\ndegree\ndistrict\ndeer\ndetail\ndrawer\ndisaster\ndemonstration\ndollar\ndeprivation\ndismissal\ndress\ndemonstrator\ndo\ndeprive\nduty\ndisappointment\ndeposit\ndrive\ndifficulty\ndecay\ndoubt\ndistribute\ndominate\ndominant\ndip\ndish\ndaughter\ndiameter\ndirection\ndividend\ndeficiency\ndrawing\ndecade\ndanger\ndrama\nduke\ndistortion\ndespise\ndrink\ndistinct\ndentist\ndespair\ndrag\ndictionary\ndealer\ndeport\ndiet\ndeny\ndecoration\ndorm\nfence\nfavorable\nfastidious\nflawed\nfunctional\nfilm\nfee\nfortune\nfame\nforbid\nforestry\nfreight\nfolklore\nfuel\nflow\nfill\nfox\nfixture\nfeedback\nfear\nfeign\nflag\nfeed\nfraud\nfoundation\nfalsify\nfavourite\nflush\nflu\nfairy\nfork\nfly\nfood\nfirst\nfur\nfriend\nfolk\nfar\nfinal\nfoot\nfreighter\nforest\nfall\nfacility\nfinance\nfailure\nfamily\nfix\nfactory\nfeast\nleak\nloud\nlandowner\nlog\nlocation\nliterature\nlong\nloose\nlump\nlesson\nlatest\nlion\nleader\nliberty\nliability\nleft\nlounge\nlean\nlost\nloan\nlimit\nlayout\nlily\nletter\nlike\nleftovers\nlover\nlate\nlose\nlaw\nlay\nlight\nlooting\nleave\nlanguage\nlemon\nlip\nlead\nlandscape\nlaser\nloss\nlack\nlicense\nlearn\nlecture\nlaundry\nlineage\nloop\nlisten\nlink\njournal\njet\njudge\njurisdiction\njealous\njob\njungle\njoint\njump\njudgment\njaw\njoystick\njacket\njelly\njudicial\njunior\njewel\njoy\njail\njury\njust\njustify\njam\njockey\njustice\njoke\njest\nnervous\nnotice\nnuclear\nnavy\nnews\nnest\nnap\nnomination\nnationalist\nnotorious\nnonsense\nnuance\nneedle\nnonremittal\nneighborhood\nneck\nnotion\nnature\nnetwork\nnarrow\nneglect\nnote\nno\nnorm\nnecklace\nneutral\nnightmare\nnoise\nnerve\nnorth\nname\nneed\nnail\nnegligence\nnew\nneighbour\nnotebook\nnumber\nnose\nnet\nnun\nnormal\nnursery\nnut\nnational\nnovel\nnegotiation\nnoble\nnative\nnight\npolish\npacket\nprivate\npath\nperformance\npriority\nproportion\npride\nprosecute\nprogressive\nperforate\npneumonia\nplagiarize\npolite\npurpose\npig\npopulation\npeace\npen\npermission\nproclaim\nproud\npollution\nprovide\nportrait\nproposal\npassage\nphysical\nprovincial\nprecedent\npipe\npoison\npoint\npositive\nprinciple\npreoccupation\npay\nprotection\npool\nplant\nplatform\nplease\nproject\nprefer\npolicy\npray\npublisher\npartner\npit\nperformer\naa\nab\nac\nad\na\na",
        ]
    output_array=[
            # "b\n",
            # "b\nb\n",
            "sh\n",
            # "aa\n",
            # "ce\n",
            "lh\n",
            "b\nc\nc\na\n",
            # "b\n",
            # "ae\n",
        ]
    if request.method=='POST':
        #request.POST['inputdata']
        code=request.POST['code']
        inputdata=request.POST['inputdata']
        lang=request.POST['lang']
        print(code,inputdata,lang)
        headers = {
        'authority': 'ide.geeksforgeeks.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ide.geeksforgeeks.org',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://ide.geeksforgeeks.org/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7',
        'cookie': '__gads=Test; __utmz=245605906.1574330848.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=245605906.76497464.1571747970.1571828951.1574330845.3; _ga=GA1.2.76497464.1571747970; _gid=GA1.2.244651628.1579195481; _gat=1; _gat_gtag_UA_144087254_1=1',
        }
        headers1 = {
        'authority': 'ide.geeksforgeeks.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ide.geeksforgeeks.org',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://ide.geeksforgeeks.org/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,mr;q=0.7',
        'cookie': '_ga=GA1.2.76497464.1571747970; __gads=ID=69b59c20a0673175:T=1579980593:S=ALNI_MZGcUMeT0oT_Ju6hBg47wbRJbX9Ow; _fbp=fb.1.1579980637697.984602587; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=d73878be-9fae-4d21-923c-30e9d9ace296; __uzmbj2=1584472415; __uzmcj2=6068813665416; __uzmdj2=1586501588; RT="z=1&dm=geeksforgeeks.org&si=1t43fz6buhm&ss=k7p7uki9&sl=0&tt=0"; __utma=245605906.76497464.1571747970.1586501588.1586874760.35; __utmz=245605906.1586874760.35.33.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1783487720.1587283177; _gat=1; authtoken=1ef5698200f0584083e462b8202c6e1d; _gat_gtag_UA_144087254_1=1; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; geeksforgeeks_consent_status=dismiss',
        }
       # print(type(code),type(inputdata))
        tc=[0]*3
        sample_output=""
        for i in range(3):
            data = {
            'lang': lang,
            'code': code,
            'input': input_array[i],
            'save': 'false'
            }

            response = requests.post('https://ide.geeksforgeeks.org/main.php', headers=headers, data=data)
            response=response.json()
            sid=response["sid"]

       

            data = {
            ' sid': sid,
            'requestType': 'fetchResults'
            }
        
            response = requests.post('https://ide.geeksforgeeks.org/submissionResult.php', headers=headers1, data=data)
            response=response.json()
            while(response["status"]!="SUCCESS"):
        
                response = requests.post('https://ide.geeksforgeeks.org/submissionResult.php', headers=headers1, data=data)
                response=response.json()

            if "rntError" not in response:
                output=response["output"]
                print(output)
                print(output_array[i])
                if output==output_array[i]:
                    tc[i]=1
                else:
                    tc[i]=0
            else:
                tc[i]=0
                output=response["rntError"]
                sample_output=output
                break
        print(tc)

        o=True
        

        input_from_textarea=request.POST["inputdata"]
        if len(input_from_textarea)>0:
            data = {
            'lang': lang,
            'code': code,
            'input': input_from_textarea,
            'save': 'false'
            }

            response = requests.post('https://ide.geeksforgeeks.org/main.php', headers=headers, data=data)
            response=response.json()
            sid=response["sid"]

       

            data = {
            ' sid': sid,
            'requestType': 'fetchResults'
            }
        
            response = requests.post('https://ide.geeksforgeeks.org/submissionResult.php', headers=headers1, data=data)
            response=response.json()
            while(response["status"]!="SUCCESS"):
        
                response = requests.post('https://ide.geeksforgeeks.org/submissionResult.php', headers=headers1, data=data)
                response=response.json()

            if "rntError" not in response:
                sample_output=response["output"]
            else:
                sample_output=response["rntError"]

        

        return JsonResponse({'output':tc,"result":o,"sample_output":sample_output})

def mcq(request):
    if request.user.is_authenticated:
        print("//////////////////")
        print(request.user.id)
        print("###############")
        q=question.objects.all()
        answers=[]
        symbols=["A","B","C","D"]
        for i in q:
            answers.append(list(zip(i.answer_set.all(),symbols)))


        m=list(zip(q,answers))
        print(q,answers)
        print(m)
        for i in m:
            
            print(i)
           
            for j in i[1]:
                
                print(j)
                
        x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])
        for i in x:
            print(i)

        return render(request,"mcq.html",{"values":m,"time":x})
    else:
        
        return redirect("/")

def mcqpost(request):
    if request.method=="POST":
        marks1=request.POST["marks"]
        print("################")
        print(marks1)
        print("###########")
        s,created=Student.objects.get_or_create(user_id=request.user.id)
        s.marks=marks1
        s.save()
        
    return redirect("/score/")
@login_required
def score(request):
    q=question.objects.all()
    s=Student.objects.get(user_id=request.user.id)
    correct=s.marks
    wrong=len(q)-correct
    result="PASS" if correct>wrong else "FAIL"
    x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])

    return render(request,"score.html",{"total":len(q),"c":correct,"w":wrong,"r":result,"time":x})

@login_required
def algo(request):
    x=re.split("^([0-9]{2})-([a-zA-Z]{3})-([0-9]{4})\s\(([0-9]{2}):([0-9]{2}):([0-9]{2})\)$",request.session["timer"])

    return render(request,"algorithm.html",{"time":x})

@login_required
def submit(request):
    S=Student.objects.get(user_id=request.user.id)
    time=datetime.datetime.strptime(request.session["timer"],"%d-%b-%Y (%H:%M:%S)")
    time_calc=time-datetime.datetime.now()

    mins=time_calc.seconds//60
    seconds = time_calc.seconds%60
    mins_diff=60-mins-1
    sec_diff=60-seconds
    total_diff=f"{mins_diff} : {sec_diff}"
    print(time_calc,mins,seconds)
    print(total_diff)
    S.time=total_diff
    S.save()
    points=request.POST["point"]
    S.marks=points
    S.save()
    return redirect("leaderboard")
@login_required
def thankyou(request):
    return HttpResponse("Thankyou for your response")
@login_required
def leaderboard(request):
    s=Student.objects.all()
    win=[]
    k=1
    import re
    for i in s:
        if i.time!="":
            a=re.findall("([0123456789]+)\s:\s([0123456789]+)",i.time)
            print(a, i.time)
            win.append([k,i.user.first_name+" "+i.user.last_name,i.time,int(a[0][0]),int(a[0][1]),i.marks])
    print(win)
    win_calc=sorted(win,key=itemgetter(5),reverse=True)   
    for i in win_calc:
        i[0]=k
        k+=1
    print(win_calc)    
    return render(request,"leaderboard.html",{"students":win_calc})