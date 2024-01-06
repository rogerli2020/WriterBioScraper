"""
    This .py can be edited with the
    handle_regex_based_on_input(self, url)
    function in ManualIdentifier
    (\d+)
    ([^/]+)
"""

"""
PROBLEMATIC OUTLETS: 
	coffeeordie.com		It does not have a distinctive URL pattern for profile pages...
"""

domain_url_regex = {
    'www.cityandstateny.com': r'https://www\.cityandstateny\.com/voices/([^/]+)/(\d+)/?$',
    'www.columbiamissourian.com': r'https://www\.columbiamissourian\.com/users/profile/([^/]+)/?$',
    'www.bizjournals.com': r'https://www\.bizjournals\.com/([^/]+)/bio/(\d+)/([^/]+)/?$',
    'www.ledger-enquirer.com': r'https://www\.ledger-enquirer\.com/profile/([^/]+)/?$',
    'www.commentary.org': r'https://www\.commentary\.org/author/([^/]+)/?$',
    'www.commondreams.org': r'https://www\.commondreams\.org/author/([^/]+)$',
    'rollcall.com': r'https://rollcall\.com/author/([^/]+)/$',
    'www.somerset-kentucky.com': r'https://www\.somerset-kentucky\.com/users/profile/([^/]+)/$',
    'www.cincinnati.com': r'https://www\.cincinnati\.com/staff/(\d+)/([^/]+)/$',
    'www.milwaukiereview.com': r'https://www\.milwaukiereview\.com/users/profile/([^/]+)/$',
    'cleantechnica.com': r'https://cleantechnica\.com/author/([^/]+)/$',
    'www.clevelandbanner.com': r'https://www\.clevelandbanner\.com/users/profile/([^/]+)$',
    'www.clevescene.com': r'https://www\.clevescene\.com/author/([^/]+)$',
	'www.chicagobusiness.com' : r'https://www\.chicagobusiness\.com/staff/([^/]+)/([^/]+)$',
	'www.crainsdetroit.com' : r'https://www\.crainsdetroit\.com/staff/([^/]+)$',
	'crooksandliars.com' : r'https://crooksandliars\.com/team/([^/]+)$',
	'cruiseradio.net' : r'https://cruiseradio\.net/author/([^/]+)/$',
	'www.cruisetradenews.com' : r'https://www\.cruisetradenews\.com/author/([^/]+)/$',
	'www.currentaffairs.org' : r'https://www\.currentaffairs\.org/author/([^/]+)$',
	'www.custercountychief.com' : r'https://www\.custercountychief\.com/users/profile/([^/]+)/$',
	'cyberscoop.com' : r'https://cyberscoop\.com/author/([^/]+)/$',
	'www.dailycamera.com' : r'https://www\.dailycamera\.com/author/([^/]+)/$',
	'www.houstonchronicle.com' : r'https://www\.houstonchronicle\.com/author/([^/]+)/$',
	'www.milwaukiereview.com' : r'https://www\.milwaukiereview\.com/users/profile/([^/]+)/$',
	'www.clintonherald.com' : r'https://www\.clintonherald\.com/users/profile/([^/]+)/$',
	'www.cnet.com' : r'https://www\.cnet\.com/profiles/([^/]+)/$',
	'www.cnn.com' : r'https://www\.cnn\.com/profiles/([^/]+)$',
	'www.coastalpoint.com' : r'https://www\.coastalpoint\.com/users/profile/([^/]+)/$',
	'coffeeordie.com' : r'https://coffeeordie\.com/([^/]+)$',
	'wkuherald.com' : r'https://wkuherald\.com/staff_name/([^/]+)/$',
	'www.columbiadailyherald.com' : r'https://www\.columbiadailyherald\.com/staff/(\d+)/([^/]+)/$',
	'www.columbiatribune.com' : r'https://www\.columbiatribune\.com/staff/(\d+)/([^/]+)/$',
	'www.somerset-kentucky.com' : r'https://www\.somerset-kentucky\.com/users/profile/([^/]+)/$',
	'www.concordmonitor.com' : r'https://www\.concordmonitor\.com/Byline?byline=([^/]+)$',
	'www.connectradio.fm' : r'https://www\.connectradio\.fm/author/([^/]+)$',
	'www.ctpost.com' : r'https://www\.ctpost\.com/author/([^/]+)/$',
	'consequence.net' : r'https://consequence\.net/author/([^/]+)/$',
	'www.conwaydailysun.com' : r'https://www\.conwaydailysun\.com/users/profile/([^/]+)/$',
	'www.americastestkitchen.com' : r'https://www\.americastestkitchen\.com/authors/([^/]+)$',
	'www.thetimestribune.com' : r'https://www\.thetimestribune\.com/users/profile/([^/]+)/$',
	'www.cosmopolitan.com' : r'https://www\.cosmopolitan\.com/author/(\d+)/([^/]+)/$',
	'www.mycentraljersey.com' : r'https://www\.mycentraljersey\.com/staff/(\d+)/([^/]+)/$',
	'www.thenewsstar.com' : r'https://www\.thenewsstar\.com/staff/(\d+)/([^/]+)/$',
	'www.dailyherald.com' : r'https://www\.dailyherald\.com/newsroom/([^/]+)/$',
	'www.yourvalley.net' : r'https://www\.yourvalley\.net/stories/([^/]+),(\d+)$',
	'dailyinterlake.com' : r'https://dailyinterlake\.com/staff/([^/]+)/$',
	'www.dailyitem.com' : r'https://www\.dailyitem\.com/users/profile/([^/]+)/$',
	'www.dailykos.com' : r'https://www\.dailykos\.com/users/([^/]+)$',
	'www.dailylobo.com' : r'https://www\.dailylobo\.com/staff/([^/]+)$',
	'www.dailylocal.com' : r'https://www\.dailylocal\.com/author/([^/]+)/$',
	'dailynorthwestern.com' : r'https://dailynorthwestern\.com/staff_name/([^/]+)/$',
	'www.dailypress.com' : r'https://www\.dailypress\.com/author/([^/]+)/$',
	'www.northjersey.com' : r'https://www\.northjersey\.com/staff/(\d+)/([^/]+)/$',
	'www.bizjournals.com' : r'https://www\.bizjournals\.com/dallas/bio/(\d+)/([^/]+)$',
	'www.newstimes.com' : r'https://www\.newstimes\.com/author/([^/]+)/$',
	'www.nytimes.com' : r'https://www\.nytimes\.com/by/([^/]+)$',
	'www.bloomberg.com' : r'https://www\.bloomberg\.com/authors/([^/]+)$',
	'www.reuters.com' : r'https://www\.reuters\.com/authors/([^/]+)/$',
	'www.forbes.com' : r'https://www\.forbes\.com/sites/([^/]+)/$',
	'www.washingtonpost.com' : r'https://www\.washingtonpost\.com/people/([^/]+)/$',
	'www.wsj.com' : r'https://www\.wsj\.com/news/author/([^/]+)$',
	'www.latimes.com' : r'https://www\.latimes\.com/people/([^/]+)$',
	'www.theguardian.com' : r'https://www\.theguardian\.com/profile/([^/]+)$',
	'www.nbcnews.com' : r'https://www\.nbcnews\.com/author/([^/]+)$',
	'www.usatoday.com' : r'https://www\.usatoday\.com/staff/(\d+)/([^/]+)/$',
	'www.foxnews.com' : r'https://www\.foxnews\.com/person/([^/]+)$',
	'www.npr.org' : r'https://www\.npr\.org/people/(\d+)/([^/]+)$',
	'abcnews.go.com' : r'https://abcnews\.go\.com/author/([^/]+)$',
	'www.dailymail.co.uk' : r'https://www\.dailymail\.co\.uk/profile-(\d+)/kelsi-karruli\.html$',
	'theathletic.com' : r'https://theathletic\.com/author/([^/]+)/$',
	'www.businessinsider.com' : r'https://www\.businessinsider\.com/author/([^/]+)$',
	'www.politico.com' : r'https://www\.politico\.com/staff/([^/]+)$',
	'www.bostonglobe.com' : r'https://www\.bostonglobe\.com/about/staff-list/staff/([^/]+)$',
	'nypost.com' : r'https://nypost\.com/author/([^/]+)/$',
	'www.newyorker.com' : r'https://www\.newyorker\.com/contributors/([^/]+)$',
	'www.si.com' : r'https://www\.si\.com/author/([^/]+)$',
	'www.inquirer.com' : r'https://www\.inquirer\.com/author/([^/]+)/$',
	'www.axios.com' : r'https://www\.axios\.com/authors/([^/]+)$',
	'www.startribune.com' : r'https://www\.startribune\.com/([^/]+)/(\d+)/$',
	'www.buzzfeed.com' : r'https://www\.buzzfeed\.com/([^/]+)$',
	'www.vice.com' : r'https://www\.vice\.com/en/contributor/([^/]+)$',
	'www.aljazeera.com' : r'https://www\.aljazeera\.com/author/([^/]+)$',
	'people.com' : r'https://people\.com/author/([^/]+)/$',
	'www.ajc.com' : r'https://www\.ajc\.com/staff/([^/]+)/$',
	'www.newsweek.com' : r'https://www\.newsweek\.com/authors/([^/]+)$',
	'www.sfchronicle.com' : r'https://www\.sfchronicle\.com/author/([^/]+)/$',
	'www.seattletimes.com' : r'https://www\.seattletimes\.com/author/([^/]+)/$',
	'www.huffpost.com' : r'https://www\.huffpost\.com/author/([^/]+)$',
	'www.dallasnews.com' : r'https://www\.dallasnews\.com/author/([^/]+)/$',
	'www.propublica.org' : r'https://www\.propublica\.org/people/([^/]+)$',
	'www.wnyc.org' : r'https://www\.wnyc\.org/people/([^/]+)/$',
	'time.com' : r'https://time\.com/author/([^/]+)/$',
	'nymag.com' : r'https://nymag\.com/author/([^/]+)/$',
	'www.vogue.com' : r'https://www\.vogue\.com/contributor/([^/]+)$',
	'variety.com' : r'https://variety\.com/author/([^/]+)/$',
	'seekingalpha.com' : r'https://seekingalpha\.com/author/([^/]+)$',
	'www.foxbusiness.com' : r'https://www\.foxbusiness\.com/person/([^/]+)$',
	'www.tampabay.com' : r'https://www\.tampabay\.com/author/([^/]+)/$',
	'fortune.com' : r'https://fortune\.com/author/([^/]+)/$',
	'www.rollingstone.com' : r'https://www\.rollingstone\.com/author/([^/]+)/$',
	'thehill.com' : r'https://thehill\.com/author/([^/]+)/$',
	'www.sbnation.com' : r'https://www\.sbnation\.com/authors/([^/]+)$',
	'www.usnews.com' : r'https://www\.usnews\.com/topics/author/([^/]+)$',
	'www.azcentral.com' : r'https://www\.azcentral\.com/staff/(\d+)/([^/]+)/$',
	'www.freep.com' : r'https://www\.freep\.com/staff/(\d+)/([^/]+)/$',
	'www.entrepreneur.com' : r'https://www\.entrepreneur\.com/author/([^/]+)$',
	'wgntv.com' : r'https://wgntv\.com/author/([^/]+)/$',
	'www.theadvocate.com' : r'https://www\.theadvocate\.com/users/profile/([^/]+)/$',
	'www.jsonline.com' : r'https://www\.jsonline\.com/staff/(\d+)/([^/]+)/$',
	'www.theepochtimes.com' : r'https://www\.theepochtimes\.com/author/([^/]+)$',
	'www.thedailybeast.com' : r'https://www\.thedailybeast\.com/author/([^/]+)$',
	'ktla.com' : r'https://ktla\.com/author/([^/]+)/$',
	'www.wbur.org' : r'https://www\.wbur\.org/inside/staff/([^/]+)$',
	'www.postandcourier.com' : r'https://www\.postandcourier\.com/users/profile/([^/]+)/$',
	'www.fool.com' : r'https://www\.fool\.com/author/([^/]+)/$',
	'www.vox.com' : r'https://www\.vox\.com/authors/([^/]+)$',
	'www.hollywoodreporter.com' : r'https://www\.hollywoodreporter\.com/author/([^/]+)/$',
	'www.kqed.org' : r'https://www\.kqed\.org/author/([^/]+)$',
	'www.marketwatch.com' : r'https://www\.marketwatch\.com/author/([^/]+)$',
	'www.reviewjournal.com' : r'https://www\.reviewjournal\.com/staff/([^/]+)/$',
	'www.ksat.com' : r'https://www\.ksat\.com/team/([^/]+)/$',
	'www.science.org' : r'https://www\.science\.org/content/author/([^/]+)$',
	'www.nbcnewyork.com' : r'https://www\.nbcnewyork\.com/author/([^/]+)/$',
	'www.sportsnet.ca' : r'https://www\.sportsnet\.ca/author/([^/]+)/$',
	'abc7.com' : r'https://abc7\.com/about/newsteam/([^/]+)$',
	'www.wired.com' : r'https://www\.wired\.com/author/([^/]+)/$',
	'slate.com' : r'https://slate\.com/author/([^/]+)$',
	'www.billboard.com' : r'https://www\.billboard\.com/author/([^/]+)/$',
	'www.fastcompany.com' : r'https://www\.fastcompany\.com/user/([^/]+)$',
	'www.detroitnews.com' : r'https://www\.detroitnews\.com/staff/(\d+)/([^/]+)/$',
	'www.wgbh.org' : r'https://www\.wgbh\.org/people/([^/]+)$',
	'buffalonews.com' : r'https://buffalonews\.com/users/profile/([^/]+)/$',
	'abc7ny.com' : r'https://abc7ny\.com/about/newsteam/([^/]+)/$',
	'www.baltimoresun.com' : r'https://www\.baltimoresun\.com/author/([^/]+)/$',
	'www.autonews.com' : r'https://www\.autonews\.com/staff/([^/]+)$',
	'www.stltoday.com' : r'https://www\.stltoday\.com/users/profile/([^/]+)/$',
	's3.bleacherreport.com' : r'http://s3\.bleacherreport\.com/users/([^/]+)$',
	'www.washingtonexaminer.com' : r'https://www\.washingtonexaminer\.com/author/([^/]+)$',
	'www.pbs.org' : r'https://www\.pbs\.org/newshour/author/([^/]+)$',
	'www.mercurynews.com' : r'https://www\.mercurynews\.com/author/([^/]+)/$',
	'www.ocregister.com' : r'https://www\.ocregister\.com/author/([^/]+)/$',
	'www.nydailynews.com' : r'https://www\.nydailynews\.com/author/([^/]+)/$',
	'www.barrons.com' : r'https://www\.barrons\.com/authors/([^/]+)$',
	'6abc.com' : r'https://6abc\.com/about/newsteam/([^/]+)',
	'www.nytimes.com' : r'https://www\.nytimes\.com/wirecutter/authors/([^/]+)/$',
	'www.bustle.com' : r'https://www\.bustle\.com/profile/([^/]+)$',
	'www.local10.com' : r'https://www\.local10\.com/team/([^/]+)/$',
	'kdvr.com' : r'https://kdvr\.com/author/([^/]+)/$',
	'themessenger.com' : r'https://themessenger\.com/author/([^/]+)$',
	'www.nbcbayarea.com' : r'https://www\.nbcbayarea\.com/author/([^/]+)/$',
	'www.king5.com' : r'https://www\.king5\.com/article/about-us/team-bios/([^/]+)/([^/]+)',
	'www.digitaltrends.com' : r'https://www\.digitaltrends\.com/users/([^/]+)/$',
	'www.oregonlive.com' : r'https://www\.oregonlive\.com/staff/([^/]+)/posts\.html$',
	'www.cbsnews.com' : r'https://www\.cbsnews\.com/newyork/personality/([^/]+)/$',
	'www.pressherald.com' : r'https://www\.pressherald\.com/author/([^/]+)/$',
	'www.clickorlando.com' : r'https://www\.clickorlando\.com/team/([^/]+)/$',
	'www.popsugar.com' : r'https://www\.popsugar\.com/authors/([^/]+)$',
	'www.nola.com' : r'https://www\.nola\.com/users/profile/([^/]+)/$',
	'www.gq.com' : r'https://www\.gq\.com/contributor/([^/]+)$',
	'www.deseret.com' : r'https://www\.deseret\.com/authors/([^/]+)$',
	'abc7news.com' : r'https://abc7news\.com/about/newsteam/([^/]+)$',
	'www.ksl.com' : r'https://www\.ksl\.com/author/([^/]+)$',
	'www.newschannel5.com' : r'https://www\.newschannel5\.com/about-us/([^/]+)$',
	'www.denverpost.com' : r'https://www\.denverpost\.com/author/([^/]+)/$',
	'www.timesunion.com' : r'https://www\.timesunion\.com/author/([^/]+)/$',
	'www.ktvu.com' : r'https://www\.ktvu\.com/person/([^/]+)/([^/]+)$',
	'wjla.com' : r'https://wjla\.com/station/people/([^/]+)$',
	'www.ksdk.com' : r'https://www\.ksdk\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'www.kansascity.com' : r'https://www\.kansascity\.com/profile/(\d+)$',
	'www.click2houston.com' : r'https://www\.click2houston\.com/team/([^/]+)/$',
	'www.wfaa.com' : r'https://www\.wfaa\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'www.chronicle.com' : r'https://www\.chronicle\.com/author/([^/]+)$',
	'www.nbcboston.com' : r'https://www\.nbcboston\.com/author/([^/]+)/$',
	'www.salon.com' : r'https://www\.salon\.com/writer/([^/]+)$',
	'www.11alive.com' : r'https://www\.11alive\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'techcrunch.com' : r'https://techcrunch\.com/author/([^/]+)/$',
	'www.nbcwashington.com' : r'https://www\.nbcwashington\.com/author/([^/]+)/$',
	'www.atlantanewsfirst.com' : r'https://www\.atlantanewsfirst\.com/authors/([^/]+)/$',
	'wsvn.com' : r'https://wsvn\.com/author/([^/]+)/$',
	'www.nbcphiladelphia.com' : r'https://www\.nbcphiladelphia\.com/author/([^/]+)/$',
	'www.kare11.com' : r'https://www\.kare11\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'www.kxan.com' : r'https://www\.kxan\.com/author/([^/]+)/$',
	'www.nbclosangeles.com' : r'https://www\.nbclosangeles\.com/author/([^/]+)/$',
	'www.khou.com' : r'https://www\.khou\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'www.fox5ny.com' : r'https://www\.fox5ny\.com/person/([^/]+)/([^/]+)$',
	'triblive.com' : r'https://triblive\.com/author/([^/]+)/$',
	'www.nbcchicago.com' : r'https://www\.nbcchicago\.com/author/([^/]+)/$',
	'fox4kc.com' : r'https://fox4kc\.com/author/([^/]+)/$',
	'www.news9.com' : r'https://www\.news9\.com/talent/([^/]+)/([^/]+)$',
	'www.sltrib.com' : r'https://www\.sltrib\.com/author/articles/([^/]+)',
	'www.tennessean.com' : r'https://www\.tennessean\.com/staff/(\d+)/([^/]+)/$',
	'www.orlandosentinel.com' : r'https://www\.orlandosentinel\.com/author/([^/]+)/$',
	'www.indystar.com' : r'https://www\.indystar\.com/staff/(\d+)/([^/]+)/$',
	'www.harpersbazaar.com' : r'https://www\.harpersbazaar\.com/author/(\d+)/([^/]+)/$',
	'www.wkyc.com' : r'https://www\.wkyc\.com/article/about-us/team-bios/([^/]+)/?([^/]+)',
	'www.theverge.com' : r'https://www\.theverge\.com/authors/([^/]+)$',
	'www.staradvertiser.com' : r'https://www\.staradvertiser\.com/author/([^/]+)/$',
	'www.wsbtv.com' : r'https://www\.wsbtv\.com/author/([^/]+)/$',
	'www.eastbaytimes.com' : r'https://www\.eastbaytimes\.com/author/([^/]+)/$',
	'www.clickondetroit.com' : r'https://www\.clickondetroit\.com/team/([^/]+)/$',
	'www.nbcdfw.com' : r'https://www\.nbcdfw\.com/author/([^/]+)/$',
	'kffhealthnews.org' : r'https://kffhealthnews\.org/news/author/([^/]+)/$',
	'www.abc15.com' : r'https://www\.abc15\.com/staff/([^/]+)$',
	'www.sun-sentinel.com' : r'https://www\.sun-sentinel\.com/author/([^/]+)/$',
	'fox59.com' : r'https://fox59\.com/author/([^/]+)/$',
	'www.pennlive.com' : r'https://www\.pennlive\.com/staff/([^/]+)/posts\.html$',
	'www.elle.com' : r'https://www\.elle\.com/author/(\d+)/([^/]+)/$',
	'www.eenews.net' : r'https://www\.eenews\.net/meet-the-team/([^/]+)/$',
	'abc13.com' : r'https://abc13\.com/about/newsteam/([^/]+)',
	'www.wfmz.com' : r'https://www\.wfmz\.com/users/profile/([^/]+)/$',
	'kstp.com' : r'https://kstp\.com/news_team/([^/]+)',
	'www.refinery29.com' : r'https://www\.refinery29\.com/en-us/author/([^/]+)$',
	'www.wbez.org' : r'https://www\.wbez\.org/staff/(\d+)/([^/]+)',
	'www.kron4.com' : r'https://www\.kron4\.com/author/([^/]+)/$',
	'www.texasmonthly.com' : r'https://www\.texasmonthly\.com/contributors/([^/]+)',
	'mashable.com' : r'https://mashable\.com/author/([^/]+)$',
	'fox8.com' : r'https://fox8\.com/author/([^/]+)/$',
	'wisconsinwatch.org' : r'https://wisconsinwatch\.org/author/([^/]+)/$',
	'whyy.org' : r'https://whyy\.org/person/([^/]+)/$',
	'nationalpost.com' : r'https://nationalpost\.com/author/([^/]+)/$',
	'www.dispatch.com' : r'https://www\.dispatch\.com/staff/(\d+)/([^/]+)/$',
	'www.zdnet.com' : r'https://www\.zdnet\.com/meet-the-team/([^/]+)/$',
	'www.abqjournal.com' : r'https://www\.abqjournal\.com/users/profile/([^/]+)/$',
	'www.wcvb.com' : r'https://www\.wcvb\.com/news-team/([^/]+)$',
	'www.texastribune.org' : r'https://www\.texastribune\.org/about/staff/([^/]+)/$',
	'www.charlotteobserver.com' : r'https://www\.charlotteobserver\.com/profile/([^/]+)$',
	'www.fox29.com' : r'https://www\.fox29\.com/person/([^/]+)/([^/]+)',
	'www.thenation.com' : r'https://www\.thenation\.com/authors/([^/]+)/$',
	'omaha.com' : r'https://omaha\.com/users/profile/([^/]+)/$',
	'www.fox2detroit.com' : r'https://www\.fox2detroit\.com/person/([^/]+)/([^/]+)$',
	'www.8newsnow.com' : r'https://www\.8newsnow\.com/author/([^/]+)/$',
	'winknews.com' : r'https://winknews\.com/author/([^/]+)/$',
	'www.news4jax.com' : r'https://www\.news4jax\.com/team/([^/]+)/$',
	'fox2now.com' : r'https://fox2now\.com/author/([^/]+)/$',
	'www.tastingtable.com' : r'https://www\.tastingtable\.com/author/([^/]+)/$',
	'www.wkbn.com' : r'https://www\.wkbn\.com/author/([^/]+)/$',
	'www.statnews.com' : r'https://www\.statnews\.com/staff/([^/]+)/$',
	'www.nationalreview.com' : r'https://www\.nationalreview\.com/author/([^/]+)/$',
	'www.wfsb.com' : r'https://www\.wfsb\.com/authors/([^/]+)/$',
	'www.fox5dc.com' : r'https://www\.fox5dc\.com/person/([^/]+)/([^/]+)$',
	'www.csmonitor.com' : r'https://www\.csmonitor\.com/About/People/([^/]+)$',
	'www.northjersey.com' : r'https://www\.northjersey\.com/staff/(\d+)/([^/]+)/$',
	'www.wcnc.com' : r'https://www\.wcnc\.com/article/about-us/team-bios/([^/]+)/([^/]+)$',
	'www.wdrb.com' : r'https://www\.wdrb\.com/users/profile/([^/]+)/$',
	'www.woodtv.com' : r'https://www\.woodtv\.com/author/([^/]+)/$',
	'www.statesman.com' : r'https://www\.statesman\.com/staff/(\d+)/([^/]+)/$',
	'www.kcra.com' : r'https://www\.kcra\.com/news-team/([^/]+)$',
	'www.cosmopolitan.com' : r'https://www\.cosmopolitan\.com/author/(\d+)/([^/]+)/$',
	'www.kgw.com' : r'https://www\.kgw\.com/article/about-us/team-bios/([^/]+)/([^/]+)$',
	'www.kpbs.org' : r'https://www\.kpbs\.org/staff/([^/]+)$',
	'www.wishtv.com' : r'https://www\.wishtv\.com/meet-the-team/([^/]+)/$',
}