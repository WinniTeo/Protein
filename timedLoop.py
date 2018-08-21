import pymysql
from collectPaperInf import collectPaperInf

# Open database connection
db = pymysql.connect("localhost", "root", "user123", "papercrawler", charset = 'utf8' )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# 遍历paperlist数据库全部title
selectSql = "SELECT title FROM paperlist"
try:
    # Execute the SQL command
    cursor.execute(selectSql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
titles = cursor.fetchall()

for title in titles:
    title = title[0]
    # 获取最新的论文引用次数和引用论文标题
    crawlResult = collectPaperInf(title)
    newCiteNumber = crawlResult[0]
    newCitingPapersTitles = crawlResult[1]

    # 获取数据库中的论文引用次数
    selectSql = "SELECT citeNumber FROM paperlist WHERE title='" + title + "'"
    try:
        # Execute the SQL command
        cursor.execute(selectSql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    citeNumber = cursor.fetchone()
    citeNumber = citeNumber[0]

    # 判断引用数是否增加
    if newCiteNumber > citeNumber:
        # 当引用数增加，获取当前论文的ID
        selectSql = "SELECT ID FROM paperlist WHERE title='" + title + "'"
        try:
            # Execute the SQL command
            cursor.execute(selectSql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
        ID = cursor.fetchone()
        ID = str(ID[0])
        # 将最新的论文列表和旧的论文列表比较，将没有的添加进去，记住originalPaperID也需要一起比较
        for newCitingPapersTitle in newCitingPapersTitles:
            newCitingPapersTitle = newCitingPapersTitle[0]
            isExistSql = "SELECT title FROM citepaper WHERE title='" + newCitingPapersTitle + "' and originalPaperID=" + ID
            try:
                # Execute the SQL command
                cursor.execute(isExistSql)
                # Commit your changes in the database
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
            callback = cursor.fetchone()
            
            if not callback:
                # 当citepaper中没有此条记录时，将此记录插入citepaper中，同时更新paperList中的citeNumber字段
                insertSql = "insert into citepaper(title, originalPaperID)values('" + newCitingPapersTitle + "', " + ID + ")"
                updateSql = "UPDATE paperList SET citeNumber='" + str(newCiteNumber) + "' WHERE title='" + title + "'"
                try:
                    # Execute the SQL command
                    cursor.execute(insertSql)
                    cursor.execute(updateSql)
                    # Commit your changes in the database
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback() 
db.close()
                


