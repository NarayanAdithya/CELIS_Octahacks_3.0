import pandas as pd
import re as re
from nltk.corpus import stopwords
df = pd.read_csv('web_dev_fin.csv',encoding= 'unicode_escape')
print("Original DataFrame:")
print(df)

#Remove same courses in the dataframe  
# sorting by first name 
df.sort_values("Title", inplace = True) 
  
# dropping ALL duplicte values 
df.drop_duplicates(subset ="Title", 
                     keep = 'first', inplace = True) 




def find_capital_word(str1):
    result = re.findall(r'\b[A-Z]\w+', str1)
    return result

df['tags']=df['Description'].apply(lambda cw : find_capital_word(cw))
print("\nExtract words starting with capital words from the sentences':")
print(df)

#We have Extracted all the capital words
#Removing the Stopwords
  
  
mystopwords=stopwords.words('English')+['Continue','Seperate','Use','Complete','Book','Step','REAL','ANY','Start','Real','Using','Grasp','Build','Create','The','Be','By','Learn','Guide','Manage','You','Get','Use','Make','Master','To','Understand','How','Become','Write']


                
def filter(tags):
    filtered_sentence = []
    for i in tags:
        if i not in mystopwords and i not in filtered_sentence:
                filtered_sentence.append(i) 
    return filtered_sentence
     


df['Tags_fin']=df['tags'].apply(lambda cw : filter(cw))
              
all_tags=[]
for i in df['Tags_fin']:
    for j in i:
        all_tags.append(j)


all_tags=set(all_tags)

all_tags=list(all_tags)


def check(x,i):
    if i in x:
        return 1
    else:
        return 0


for i in all_tags:
    df[i]=df['Tags_fin'].apply(lambda x:check(x,i) )   
    
df.drop('tags', axis=1, inplace=True)
df.to_csv('tag_gen.csv')
df['tag_vector'] = df.iloc[:,12:].values.tolist()




# compute Jaccard Index to get most similar movies to target movie


pd.reset_option('display.max_colwidth')

target_course = 'The Web Developer Bootcamp 2020'


target_tag_list = df[df.Title == target_course].Tags_fin.values[0]
course_Tags_fin_list_sim = df[['Title','HeadLine','Tags_fin']]
course_Tags_fin_list_sim['jaccard_sim'] = course_Tags_fin_list_sim.Tags_fin.map(lambda x: len(set(x).intersection(set(target_tag_list))) / len(set(x).union(set(target_tag_list))))
print(f'courses most similar to {target_course} based on Tags_fin:')
text = (course_Tags_fin_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(25)['Tags_fin'].values)
course_Tags_fin_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(10)


            

            