from bs4 import BeautifulSoup
import requests
import csv
import matplotlib.pyplot as plt

count_lists=list()
fields = ['Div_Count','Span_Count','Link_Count','Para_Count',
            'List_Count','Img_Count','Link','Article']  #change here

filename = "samsung_prism.csv"  
mydict_list =[]
            

def scrapUrl(s):
  articleAmar_url=s #place new article links here
  amar_re=requests.get(articleAmar_url)

  amarContent=amar_re.content
  amarSoup=BeautifulSoup(amarContent,'html.parser')
  #print(amarSoup.prettify)

  #find div tag of article
  amarTitle=amarSoup.title
  print(amarTitle.text)

  amar_div=amarSoup.find_all('div')
  div_count=0
  for divs in amar_div:
    if (divs!=""):
      div_count=div_count+1
     ## print("Div Text:{}".format(divs.text))

  count_lists.append(div_count)

  print("div count:",count_lists)

  amar_span=amarSoup.findAll('span')
  span_count=0
  for spans in amar_span:
    if(spans !=""):
      span_count=span_count+1
      ##print("spans_data: {}".format(spans.text))

  print("span_count",span_count)
  count_lists.append(span_count)

  #find content of anchor tag and inner text 
  amar_anchor=amarSoup.findAll('a')
  link_count=0
  text_ref=[]
  for anchors in amar_anchor:
    if(anchors!='#'):
      link_count=link_count+1
      text_anc=anchors.get_text()
      text_ref=anchors.get('href')
      #print(type(text_ref))
     ## print("Links: {}".format(text_ref))

  print("Link count",link_count)
  count_lists.append(link_count)
  #find paragraph in article 
  amar_para=amarSoup.findAll('p')
  para_count=0
  for para in amar_para:
    if(para.text!=""):
      para_count=para_count+1
     ## print(para.text)
  print("Para_count",para_count)
  count_lists.append(para_count)

  amar_li=amarSoup.findAll('li')
  list_count=0
  for lists in amar_li:
    if(lists!=""):
      list_count=list_count+1
      ##print("List_data: {}".format(lists.text))
  print("list_count",list_count)
  count_lists.append(list_count)

  #image count 
  img_count=0
  for img in amarSoup.find_all('img'):
    img_count+=1
    ##print(img)
  print("Imgae Count",img_count)
  count_lists.append(img_count)

  count_lists
  tags=["div","span","link","para","list","img"]

  fig=plt.figure(figsize = (10, 5))
  plt.bar(tags, count_lists, color ='red',width = 0.4)
  plt.xlabel("Tags Name")
  plt.ylabel("Tags Count")
  plt.title(line)
  plt.show()
  count_lists.clear()
  
  case = {'Div_Count':div_count,'Span_Count':span_count,
              'Link_Count':link_count,'Para_Count':para_count,
              'List_Count':list_count,'Img_Count':img_count,'Link':s,'Article':"YES"}#changed here

  mydict_list.append(case)




file1 = open('/content/testingArt.txt', 'r')  #Put your text file here
count = 0

while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
 
    # if line is empty
    # end of file is reached
    if not line:
        break
    #print("Line{}: {}".format(count, line.strip()))
    scrapUrl(line.strip())

 
    
 
file1.close()

with open(filename,'w',newline='')as csvfile:
      writer = csv.DictWriter(csvfile,fieldnames = fields)
      writer.writeheader() 
      writer.writerows(mydict_list)  




# baseUrl=input('Enter URL')

# scrapUrl(baseUrl)

# count_lists
# tags=["div","span","link","para","list","img"]

# fig=plt.figure(figsize = (10, 5))
# plt.bar(tags, count_lists, color ='red',width = 0.4)
# plt.xlabel("Tags Name")
# plt.ylabel("Tags Count")
# plt.title(baseUrl)
# plt.show()
