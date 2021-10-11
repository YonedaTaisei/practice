# 変更した
"""studentlist=["浅村","松木"]
count=0

for i in studentlist:
    print("{}さんの試験結果を入力してください".format(i))
    network=int(input("ネットワークの得点？　＞＞"))
    databese=int(input("データベースの得点？　＞＞"))
    security=int(input("セキュリティの得点？　＞＞"))
    if i == "浅村":
        asamurasukoa=[network,databese,security]
        asamuragoukei=

#関数の定義。
def hello():
    print("こんにちは.工藤です。 ")
#関数の呼び出し。
hello()

def input_scores():
    name=""#関数内部で宣言された関数　ローカル関数
    print("{}さんの試験結果を入力してください。".format(name))
name="麻木"
input_scores()
name="松田"
input_scores()

def hello(name):
    print("こんにちは.{}です。".format(name))

hello("浅木")
hello("松田")


def profile(name,age,hobby):
    print("私の名前は{}です。".format(name))
    print("年齢は{}です。".format(age))
    print("趣味は{}です。".format(hobby))

profile("田中","２１","サッカー")
"""

# def input_scores(name):
#      print("{}さんの試験結果を入力してください。".format(name))
#      network=int(input("ネットワークの得点？　＞＞"))
#      databese=int(input("データベースの得点？　＞＞"))
#      security=int(input("セキュリティの得点？　＞＞"))
#      scores=[network,databese,security]



# def calc_avrage(scores):
#      avg=sum(scores)/len(scores)
#      print("平均点は{}です。".format(avg))

# # input_scores("浅木")
# calc_avrage([80,90,100])


# def plus(x,y):
#     answer = x + y
#     return answer

# answer = plus(100,500)
# print("足し算の答えは{}です。".format(answer))



# name="松田"  #グローバル変数

# def change_name():
#     global name
#     name="浅木"

# def hello():
#     print("こんにちは"+name+"さん")

# change_name()

# hello()


def is_leapyear(year):

    #400で割れるのは閏年　または４で割り切れて且つ100で割り切れる年は閏年ではない
    return True or False

flag = is_leapyear(int(input("西暦を入力してください　＞＞")))

if()
