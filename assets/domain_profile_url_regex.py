"""
How to create Regex?
    Escape . with \.
    Replace numeric fields with (\d+)
    Replace string fields with ([^/]+)
    End regex with $
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
}