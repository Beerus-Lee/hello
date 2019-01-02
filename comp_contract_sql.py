#!/usr/bin/python3

#城市编码和拼音
city_code_spell = "长春:220100:CCBK8888:Changchun,天津:120000:TJBK8888:Tianjin,大连:210200:DLBK8888:Dalian,沈阳:210100:SYBK8888:Shenyang,丹东:210600:HLDBK8888:Dandong,青岛:370200:QDBK8888:Qingdao,济南:370101:JNBK8888:Jinan,西安:610100:XABK8888:Xian,杭州:330100:HZBK8888:Hangzhou"

#版式 contract_type 1：合同, 2：定金, 3：意向金
#标签 create_tag  0 缺省, 1 特许经营非空白合同，2 意向协议非空白
#            目前属于1的类型有： 1）特许经营合同合订本  2）住商不动产加盟合同合订本
#            目前属于2的类型有： 1）特许经营合同意向协议 2）特许经营意向协议 3）住商不动产加盟意向协议
form_1 = {"form_key":7,"contract_type":1,"product_name":"优铭家-特许经营合同之补充协议","brand":"Aoli","create_tag":0}

format_types = [form_1]

#组装sql
city_codes = city_code_spell.split(",")

my_open = open("/Users/lichao/Desktop/导入协议模版数据.txt", 'w+')
for city_info in city_codes:
    city = city_info.split(":")
    city_code = city[1]
    company = city[2]
    city_name = city[3]
    print("#城市："+str(city[0]))
    sql ="insert into contract_category (city_code, company, form_key, contract_type, product_name, city_name, brand, brand_type, create_tag) values "
    for form in format_types:
        # 品牌类型德佑分为两种 公司组织编码BK8888结尾是翻德佑，其他是德佑；协议板式写其他品牌的为翻保留类型，保留类型目前没有
        # 品牌类型：1 德佑 2 翻德佑 3 保留。4 翻保留'
        if form["brand"] == "Deyou":
            if company[-6:] == "BK8888":
                brand_type = 2
            else:
                brand_type = 1
        else:
            brand_type = 4
        sql = sql + "('"+str(city_code)+"','"+str(company)+"','"+str(form["form_key"])+"',"+str(form["contract_type"])+",'"+str(form["product_name"])+"','"+str(city_name)+"','"+str(form["brand"])+"',"+str(brand_type)+","+str(form["create_tag"])+"),"
    sql = sql[0:len(sql)-1] +";"
    my_open.write(sql+"\n")
    print(sql)
my_open.close()
