# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:33:52 2018

@author: Taleb
"""

import justext
import time
def HtmlClean(rawtext):
    #Takes the input as a string with html tags included
    #Checks each paragraph for whether it's meaningful text or not
    #Outputs the text as a string with html tags and nav elements removed
    paragraphs = justext.justext(rawtext,justext.get_stoplist("English"))
    return ' '.join([p.text for p in paragraphs if not p.is_boilerplate])


import pandas as pd
#df.to_csv(repo_path+'text.csv')
df=pd.read_json(path_or_buf="small_earthquake_with_HTML_tags.json",orient='records',lines=True)


df.originalUrl[1]
df
