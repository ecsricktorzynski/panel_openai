import os
import pandas as pd
import openai
openai.api_key = ""
pd.options.display.max_seq_items = 2000
pd.DataFrame(openai.Model.list()['data'])