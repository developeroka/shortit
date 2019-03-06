#!/usr/bin/env python3

import webbrowser
import argparse


def make_it_short():

    parser = argparse.ArgumentParser(description='Tool for going to your most wanted links with short keys')
    parser.add_argument('-w', metavar='url', dest='wanted', type=str,
                        help="""the wanted url , 
                                sap >>> web.whatsapp.com  ,
                                lnkdin >>> linkedin.com   ,
                                tlgrm >>> web.telegram.com   ,
                                gogol >>> google.com   ,
                                github >>> github.com """
                        )

    args = parser.parse_args()
    _wanted_url = args.wanted or None

    urls = {"linkedin": "https://www.linkedin.com/feed/",
            "github": "https://github.com/",
            "sup": "https://web.whatsapp.com/",
            "telegram": "https://web.telegram.org/#/im",
            "gogol": "https://google.com/"}

   
    if _wanted_url:
        webbrowser.open(urls[_wanted_url])


make_it_short()
