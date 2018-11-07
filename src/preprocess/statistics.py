# -*- coding: utf-8 -*-

#处理MSRA数据集和CITY数据集合weibo数据集
def statisics_MSRA_CITYU_Weibo(fin_name):
    char_num = 0
    sent_num =0
    sent_char_num =0
    entity_num = 0
    entity_dict = dict()    
    with open(fin_name, "r", encoding="utf8", errors="ignore") as fin:
        num = 0        
        for line in fin.readlines():
            num += 1
            if len(line) > 3:
                char_num += 1
                sent_char_num += 1
                if line[2] == 'B':#遇到B标签即实体数量加一
                    entity_num += 1
                    entity_name = line[4:-1]
                    if entity_name in entity_dict:#统计各个实体数量
                        entity_dict[entity_name] += 1
                    else:
                        entity_dict[entity_name] = 1
            else:
                if line[0] == '\n' and sent_char_num > 0:
                    sent_num += 1
                    sent_char_num = 0
            if num % 100000 == 0:
                print("statisics:", num)   
    print("sent_num:", sent_num)
    print("char_num:", char_num)  
    print("entity_num:",entity_num)
    print(entity_dict)

#处理Finance和MIl数据集
def statisics_Finance_MIL(fin_name):
    char_num = 0
    sent_num =0
    sent_char_num =0
    entity_num = 0
    entity_dict = dict()    
    with open(fin_name, "r", encoding="utf8") as fin:
        num = 0        
        for line in fin.readlines():
            num += 1
            if len(line) > 3:
                temp = line[:-1].split('\t')
                char_num += len(temp[0])
                sent_char_num += len(temp[0])
                if temp[1][0] == 'I':
                    entity_num += 1
                    entity_name = temp[1][2:]
                    if entity_name in entity_dict:
                        entity_dict[entity_name] += 1
                    else:
                        entity_dict[entity_name] = 1
            else:
                if line[0] == '\n' and sent_char_num > 0:
                    sent_num += 1
                    sent_char_num = 0
            if num % 10000 == 0:
                print("statisics:", num)   
    print("sent_num:", sent_num)
    print("char_num:", char_num)  
    print("entity_num:",entity_num)
    print(entity_dict)

#处理Med数据集
def statisics_Med(fin_name):
    char_num = 0
    sent_num =0
    sent_char_num =0
    entity_num = 0
    entity_dict = dict()    
    with open(fin_name, "r", encoding="utf8") as fin:
        num = 0        
        for line in fin.readlines():
            num += 1
            if len(line) > 3:
                temp = line[:-1].split('\t')
                char_num += len(temp[0])
                sent_char_num += len(temp[0])
                if temp[1][0] == 'I':
                    entity_num += 1
                    entity_name = temp[1][2:]
                    if entity_name in entity_dict:
                        entity_dict[entity_name] += 1
                    else:
                        entity_dict[entity_name] = 1
                if temp[0][-1] == "。":
                    sent_num += 1
                    sent_char_num = 0
            if num % 10000 == 0:
                print("statisics:", num)   
    print("sent_num:", sent_num)
    print("char_num:", char_num)  
    print("entity_num:",entity_num)
    print(entity_dict)

#处理Weibo2nd数据集
def statisics_Weibo2nd(fin_name):
    char_num = 0
    sent_num =0
    sent_char_num =0
    entity_num = 0
    entity_dict = dict()    
    with open(fin_name, "r", encoding="utf8", errors="ignore") as fin:
        num = 0        
        for line in fin.readlines():
            num += 1
            if len(line) > 4:
                line = line[0] + line[2:]
                char_num += 1
                sent_char_num += 1
                if line[2] == 'B':
                    entity_num += 1
                    entity_name = line[4:-1]
                    if entity_name in entity_dict:
                        entity_dict[entity_name] += 1
                    else:
                        entity_dict[entity_name] = 1
            else:
                if line[0] == '\n' and sent_char_num > 0:
                    sent_num += 1
                    sent_char_num = 0
            if num % 100000 == 0:
                print("statisics:", num)   
    print("sent_num:", sent_num)
    print("char_num:", char_num)  
    print("entity_num:",entity_num)
    print(entity_dict)

#处理Weibocrfsuite数据集
def statisics_Weibocrfsuite(fin_name):
    char_num = 0
    sent_num =0
    sent_char_num =0
    entity_num = 0
    entity_dict = dict()    
    with open(fin_name, "r", encoding="utf8", errors="ignore") as fin:
        num = 0        
        for line in fin.readlines():
            num += 1
            if len(line) > 4:
                temp = line.split('\t')
                line = temp[0][0] + '\t' + temp[1]
                char_num += 1
                sent_char_num += 1
                if line[2] == 'B':
                    entity_num += 1
                    entity_name = line[4:]
                    if entity_name in entity_dict:
                        entity_dict[entity_name] += 1
                    else:
                        entity_dict[entity_name] = 1
            else:
                if line[0] == '\t' and sent_char_num > 0:
                    sent_num += 1
                    sent_char_num = 0
            if num % 100000 == 0:
                print("statisics:", num)   
    print("sent_num:", sent_num)
    print("char_num:", char_num)  
    print("entity_num:",entity_num)
    print(entity_dict)


def main():
#    fin_name = "msra_train_utf16.ner"
#    fin_name = "msra_truth_utf16.ner"
    
#    fin_name = "cityu_train_utf16.ner"
#    fin_name = "cityu_truth_utf16.ner"

#    fin_name = "weiboNER.conll.train"
#    fin_name = "weiboNER.conll.dev"
#    fin_name = "weiboNER.conll.test"
    
#    fin_name = "weiboNER_2nd_conll.train"
#    fin_name = "weiboNER_2nd_conll.dev"
#    fin_name = "weiboNER_2nd_conll.test"
#    statisics_Weibo2nd(fin_name)
    
#    fin_name = "crfsuite.weiboNER.charpos.conll.train" 
#    fin_name = "crfsuite.weiboNER.charpos.conll.dev"
    fin_name = "crfsuite.weiboNER.charpos.conll.test" 
    statisics_Weibocrfsuite(fin_name)
    
    
#    fin_name = "finance-ner.txt" 
    
#    fin_name = "mil-ner.txt" 
#    statisics_Finance_MIL(fin_name)
    
#    fin_name = "Med-ner.txt"    
#    statisics_Med(fin_name)
    

if __name__ == "__main__":
    main()