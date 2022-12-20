import requests
import bs4

def getPrice(productURL):
    req=requests.get(productURL)
    req.raise_for_status()

    soup=bs4.BeautifulSoup(req.text, 'html.parser')
    elems=soup.select('.offer-price')
    return elems[0].text.strip()

price=getPrice('https://www.amazon.com.au/What-Paul-Meant-Wills-Gary/dp/0143112635/ref=pd_sim_14_2/355-6481899-5221628?_encoding=UTF8&pd_rd_i=0143112635&pd_rd_r=922e9bb7-1ce2-41da-a96b-91edcdf710e5&pd_rd_w=zxE5A&pd_rd_wg=SGSHV&pf_rd_p=55d1bb5b-2eeb-474c-99fd-28efe0d279ff&pf_rd_r=BD2Y9DRM8CTEAE5EJXYZ&psc=1&refRID=BD2Y9DRM8CTEAE5EJXYZ')
print(price)
