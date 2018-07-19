# parse docx
import docx
import re# parse docx

def parseDocx(fileName):
    # 获取文档对象
    docxFile = docx.Document(fileName)
    #提取标题
    paperTitles = []
    noSpot = []
    for perParagraph in docxFile.paragraphs:
        #每段文本的定义为text
        perParagraphText = perParagraph.text
        #提取后面带有数字的小数点
        rr = re.compile(r'\.\d')  #定义提取规则
        noSpot = rr.findall(perParagraphText)
        #将小数点及后面的数替换为空
        for each in noSpot:
            perParagraphText = perParagraphText.replace(str(each), '')
        # 用'.'将每一个论文信息分割开，存为一个lists    
        perParagraphText = perParagraphText.split('.')
        # print(perParagraphText[1])
        paperTitles.append(perParagraphText[1])
        # print(paperTitles)
    return paperTitles

if __name__ == '__main__':
    paperTitles = parseDocx("C:\\Users\\WinniTeo\\Desktop\\shixi\\doc\\Doc_Catalog1.docx")
    for each in paperTitles:
        print(each)


