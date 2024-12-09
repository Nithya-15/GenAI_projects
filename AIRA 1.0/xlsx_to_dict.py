import pandas as pd

# contributed by -  Navyamsh Gangavaram

def pdf_links_dict():
    df=pd.read_excel('TA.xlsx')
    df['Title']=df['Title']+'.pdf'
    title_url_dict=df.set_index('Title')['URL'].to_dict()
    return title_url_dict


