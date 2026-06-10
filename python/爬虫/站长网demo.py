from lxml import etree
import requests

def get_page():
    urls = ['https://sc.chinaz.com/tupian/meinvtupian.html']
    page_sum = int(input('输入页数'))
    if page_sum>=2:
        for i in range(2,page_sum+1):
            url=f'https://sc.chinaz.com/tupian/meinvtupian_{i}.html'
            urls.append(url)
    j=1
    for url in urls:
        print(f'开始爬取第{j}页')
        get_img(urls[j-1])
        print(f'第{j}页爬取完成')
        j+=1
    print(f'爬取完成，共爬取{j-1}页,{(j-1)*40}张图片')

def get_img(url):
    response=requests.get(url)
    response.encoding="utf-8"
    html_tree=etree.HTML(response.text)
    img_src_list=html_tree.xpath("//img[@class='lazy']/@data-original")
    img_name_list=html_tree.xpath("//img[@class='lazy']/@alt")
    img_dict = [{'name':img_name,'src':f'https:{img_src}'} for img_name,img_src in zip(img_name_list,img_src_list)]
    print(img_dict)
    for img_dict_item in img_dict:
        res=requests.get(img_dict_item['src'])
        last_name=img_dict_item['src'].split('.')[-1]
        with open(f'images/{img_dict_item["name"]}.{last_name}','wb') as f:
            f.write(res.content)


if __name__=='__main__':
    get_page()

