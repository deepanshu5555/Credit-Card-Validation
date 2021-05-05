from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def FrontUI():
    return render_template("index.html")
@app.route('/result',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
        num1 = request.form  
        num=num1["CreditCardNumber"]  
        res1 = luhn(num)
        res2 = checkVendor(num)
        dict1={
            "CreditCardNumber":num,
            "res_true":res1,
            "vendor":res2
        }
        if(res1):
            return render_template("result_data.html",result = dict1)
        else:
            return render_template("result_error.html",result=dict1)
def luhn(card_num):
    array = [i for i in card_num]
    for i in range(len(array)-2,-1,-2):
        array[i]=str(2*int(array[i]))
        n=array[i]
        while(int(n)>9):
            s=0
            for j in n:
                s=s+int(j)
                n=str(s)
        array[i]=n
    array_sum=0
    for i in array:
        array_sum+=int(i)
    print(array_sum)
    if(array_sum%10==0):
        return True
    else:
        return False

def checkVendor(card_num):
    if(card_num[:1]=='4'):
        return "VISA"
    elif(card_num[:1]=='5'):
        return "MasterCard"
    elif(card_num[:2]=="34"):
        return "American Express"
    elif(card_num[:2]=="60"):
        return "Discover"
    else:
        return "Citibank"

if __name__=="__main__":
    app.run(debug=True)
    

