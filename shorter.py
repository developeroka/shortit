#!/usr/bin/env python3

import webbrowser
import argparse


def make_it_short():

    parser = argparse.ArgumentParser(description='Tool for going to your most wanted links with short keys')
    parser.add_argument('-set', metavar='url', dest='source', type=str,
                        help="""set your default short keys for wanted links"""
                        )
    parser.add_argument('-as', metavar='short key', dest='newkey', type=str,
                        help="""set your default short keys for wanted links"""
                        )
    parser.add_argument('-w', metavar='url', dest='wanted', type=str,
                        help="""the wanted url , 
                                sap >>> web.whatsapp.com  ,
                                lnkdin >>> linkedin.com   ,
                                tlgrm >>> web.telegram.com   ,
                                gogol >>> google.com """
                        )

    args = parser.parse_args()
    _new_url = args.source or None
    _url_shortkey = args.newkey or None
    _wanted_url = args.wanted or None

    urls = {"linkedin": "https://www.linkedin.com/feed/",
            "github": "https://github.com/",
            "sup": "https://web.whatsapp.com/",
            "telegram": "https://web.telegram.org/#/im",
            "gogol": "https://google.com/"}

    if _new_url:
        if _url_shortkey:
            urls[_url_shortkey] = _new_url
        else:
            print('you should send your shortkey with your wanted url')

    elif _wanted_url:
        webbrowser.open(urls[_wanted_url])


make_it_short()
