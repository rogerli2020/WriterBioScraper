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
	'www.cincinnati.com' : r'https://www\.cincinnati\.com/staff/(\d+)/([^/]+)/$',
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
}