import Interface as driver

driver.connect("test.db", False)
columns = {"name":"text","age":"real"}
driver.createTable("people",columns)
driver.insertRow("people",values=["Johnny",24])
driver.insertRow("people",values=["Stan",125])
driver.insertRow("people",values=["Pula",00])
print(driver.dump("people","age"))