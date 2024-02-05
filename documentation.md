# Scraping Process Documentation

## Process for Discovering URLs (Google Search Method)

This process of obtaining URLs involves scraping Google search results.

This method has some drawbacks, such as the fact that it does not work with outlets that do not have distinct URL patterns for profile pages. Sometimes it also returns URLs that are not relevant (example: [https://www.wfsb.com/authors/associated-press/](https://www.wfsb.com/authors/associated-press/)).

**STEPS:**

1. For an outlet, obtain a profile page URL (e.g. [https://www.rollingstone.com/author/ct-jones/](https://www.rollingstone.com/author/ct-jones/))
2. Obtain a Regular Expression for the URL pattern. In this case,  the URL has the string field “ct-jones”, which can be replaced by some other strings that does not contain the slash character. This can be represented as r'[https://www](https://www/)\.rollingstone\.com/author/([^/]+)/$' in python regex format. After obtaining the regex, write it to the file .\assets\domain_profile_url_regex.py. The key should be the domain ([www.rollingstone.com](https://www.rollingstone.com/author/ct-jones/)) and the value is the regex.
    - This process can be done in bulks **automatically** with the script src\generate_regex_from_local_file.py.
        - The input file path of this script is .\regex.csv. This is a csv that does not have a header.
        - The first column is the outlet name, the second is the example URL, the third is the replaceable string fields in the URL with space delimiters, the fourth is the replaceable numeric string fields also with space delimiter. Note that some outlet names might contain the comma character which might throw the program off (the outlet name is not relevant to this script anyway so you can just delete those outlet names).
        - For some more complex regex you probably need to add them manually by editing the \assets\domain_profile_url_regex.py file.
3. After obtaining the regex and writing it to the file, you can start the process of scraping for Google Search results. First, obtain the substring that can be used to filter for all the profile page URLs for the outlet, in this case, it is [https://www.rollingstone.com/author/](https://www.rollingstone.com/author/ct-jones/). The goal is so that we search Google with the query “site:[https://www.rollingstone.com/author/](https://www.rollingstone.com/author/ct-jones/)” (Google probably supports more advanced query methods but this works well for most outlets). Write the substring ([https://www.rollingstone.com/author/](https://www.rollingstone.com/author/ct-jones/)) to the file .\input_info.txt. More than 1 line can be written to this file so you can do this process in bulks.
4. Run the script scrape_urls_from_google.py to automatically search and scrape for google search results. Note that the script will block when it detects a CAPTCHA until you pass the CAPTCHA.
5. After that, file(s) containing the HTML element(s) will be generated and saved under input\local_html.
6. Run the script capture_urls_from_local_htmls.py to obtain the URLs from the locally saved HTML elements. The script will give out warnings if it did not obtain any URLs from an element. The URLs with be saved to output\captured_urls.txt.

## Process for Discovering URLs (Web Crawler Method)

This is an alternative method if you want to discover URLs beyond what is returned by Google. The script has a -crawl option for crawling for profile URLs from assets\root_urls_for_crawling.txt. I find it to be pretty slow most of the time but it can be pretty fast if the starting URL contains a lot of profile links (e.g. a staff directory page). Currently it uses a weighted tree algorithm but more optimization might be needed. Also I haven’t used this functionality in a while so I probably broke it while implementing other functionalities.

## Process for Creating Scrapers (Manually)

This is a manual but somewhat streamlined process.

This process might have some drawbacks, such as the fact that it relies mostly only on CSS Selectors, which limits the possibilities of doing some more complicated scraping process.

TODO: the resulting social media links are often mislabeled but fixing it should be pretty easy.

1. Use the -adds (add scrapers) option for main.py
2. First, enter the outlet name and the URL.
3. Then, enter the CSS selectors for the name, title, description, social media links, pfp of the profile page. The CSS selectors can be obtained (in Chrome) by pressing F12, selecting the element, right click > Copy > Copy Selector. 
    - Make sure that for social media links, always select the <a/> element containig the HREF to the link.
    - Make sure that the CSS selector obtained is generalized (i.e. it does not rely on elements with id attributes that contains the name of the specific author. This is less of an issue with biography elements but can be more common with article elements.)
4. You’ll then have to enter the selectors for articles (single_article, single_article_title, etc).
    - single_article is not important, you can enter anything for this field or just edit the code to not include it.
    - as mentioned above, make sure the CSS selector obtained is generalized for all the articles so it does not rely on some id attributes of a single article element. One tip is to just delete the id attribute editing the element, and then copying the CSS selector after deleting the id field.
    - make sure you stick to only 1 article element, preferably something further down the list of articles.
    - make sure to select an <a/> element for single_article_url
5. The program will then ask you to enter a substring to be deleted from the article selectors. This is so you can get rid of the “:nth-child(X)” substring from the selectors so more than 1 articles can be scraped.
6. The program will then ask you to enter “post-selectors”. Most of the time it is not needed. Refer to the source code to see what it does.
7. Many outlets use the same template. To expedite the process, you can review the file assets\common_formats.json to check out the common templates. If you encounter an outlet that uses one of the common templates, you can just enter the key defined in the common_formats file (e.g. -gann, -blox, -daily, etc) while entering selectors information.
8. The information you entered are saved under ./assets/selectors.jsonl. You can edit them manually by opening the file.

## Process for Scraping URLs

TODO: This functionality could benefit a lot from multiprocessing which is not implemented yet. 

TODO: a mechanism for preventing and detecting CAPTCHA or rate limiting should be implemented.

1. Enter the URLs into ./assets/input_urls.txt
2. run the [main.py](http://main.py) with the option -scrape