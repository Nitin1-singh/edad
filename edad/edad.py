import pandas as pd
class CreateSummary:
  def __init__(self,path):
    try:
      self.path = path
      self.ans = pd.read_csv(path)
      self.index = 0
      self.size = self.ans.columns.shape[0]
      self.resultArr = []
    except Exception as e:
      print("Error  = ",e)
  
  def messageForObject(self,index): 
    try:
      return f"""
      <li>Uniques values = {self.resultArr[index]["uniques"]}</li>
      <li>Most Occured values = {self.resultArr[index]["top"]}</li>
      """
    except Exception as e:
      print("Error = ",e)

  def messageNotForObject(self,index): 
    try:
      return f"""
      <li>Uniques values = {self.resultArr[index]["uniques"]}</li>
      <li>25% value = {self.resultArr[index]["25%"]}</li>
      <li>50% value = {self.resultArr[index]["50%"]}</li>
      <li>75% value = {self.resultArr[index]["75%"]}</li>
      <li>Min value = {self.resultArr[index]["min"]}</li>
      <li>Mean value = {self.resultArr[index]["mean"]}</li>
      <li>Max value = {self.resultArr[index]["max"]}</li>
    """
    except Exception as e:
      print("Error = ",e)
    
  def ending(self):
    try:
      return f"""<p>--------------------------------------------------------------</p>"""
    except Exception as e:
      print("Error = ",e)

  def fillVal(self):
    try:
      for i in self.ans.columns:
        if self.ans[i].dtype != object:
          summary = self.ans[i].describe().to_dict()
          uniques = self.ans[i].unique().shape[0]
          nullVal = self.ans[i].isnull().sum()
          nullPer = 0

          if nullVal != 0:
            nullPer = self.ans.shape[0] /  nullVal
          summary["uniques"] = uniques
          summary["nullVal"] = nullVal
          summary["nullPer"] = nullPer
          summary["col_name"] =  i
          summary["data_type"] = self.ans[i].dtype
          self.resultArr.append(summary)

        if self.ans[i].dtype == object :
          summary = self.ans[i].describe().to_dict()
          nullVal = self.ans[i].isnull().sum()
          uniques = self.ans[i].unique().shape[0]
          nullPer = 0

          if nullVal != 0:
            nullPer =self.ans.shape[0] /  nullVal
            
          summary["nullVal"] = nullVal
          summary["nullPer"] = nullPer
          summary["col_name"] =  i
          summary["data_type"] = self.ans[i].dtype
          summary["uniques"] = uniques
          self.resultArr.append(summary)
    except Exception as e:
      print("Error  = ",e)

  def generateHTML(self):
      try:
        index = self.index
        size = self.size

        if index >= size:
          print("Evaluating ------------> Done !")
          print("HTML File is Successfully Generated (^-^)")
          return ""
        elif index < size:
          print("Evaluating ------------>",self.resultArr[index]["col_name"])
          html  = f"""
          <div>
          <h4>Feature name = {self.resultArr[index]["col_name"]}</h4>
          <ul>
          <li>data type = {self.resultArr[index]["data_type"]}</li>
          <li>data count = {self.resultArr[index]["count"]}</li>
          <li>Missing value count = {self.resultArr[index]["nullVal"]}</li>
          <li>Missing value percentage = {self.resultArr[index]["nullVal"]}%</li>
          {
            self.messageNotForObject(index)
            if self.resultArr[index]["data_type"] != object
            else self.messageForObject(index)
          }
          </ul>
          {
            self.ending()
            if index != size-1
            else "<p><-------------------------------END OF File-------------------------------></p>"
          }
          </div>
          """
          html = html.replace("\n","")
          self.index = self.index+1
          return html + self.generateHTML()
      except Exception as e:
        print("Error  = ",e)

  def generateFile(self):
    try:
      self.fillVal()
      ans = self.generateHTML()
      self.index = 0
      html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Summary of {self.path}</title>
        </head>
        <body>
            {ans}
        </body>
        </html>
      """
      with open('index.html', 'w') as f:
        f.write(html_content)
    except Exception as e:
      print("Error  = ",e)
  
