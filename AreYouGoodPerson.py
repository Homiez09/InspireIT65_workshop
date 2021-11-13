""" 
ชื่อDiscord = ม.6 ภูมิ ภูมิระพี ระยอง 
ชื่อนามสกุล = นายภูมิระพี เสริญวณิชกุล
Email = phumrapeesoen1@gmail.com  
ชั้น = ม.6
"""

import random

Questions = ["รักพ่อแม่ไหม?", "เคยช่วยพ่อแม่รดน้ำต้นไม้ไหม?", "เคยช่วยคนตาบอดข้ามถนน?", "ให้อาหารปลาไหม?", "เคยช่วยครูยกของไหม?"]
random.shuffle(Questions) # เรียงข้อมูลที่อยู่ใน Questions ใหม่
LastQuesttion = "คุณรักสถาบันพระมหากษัตริย์ไหม?" # คำถามปั่น

def random_question():
    return random.shuffle(Questions)

def fake_check(point, vip):
    if point >= 3 or vip == 1:
        print("คุณเป็นคนดีมากกกกกกก")
    else:
        print("คุณเป็นคนที่ไม่ดี อย่าลืมทำความดีกด้วยล่ะ")

def get_point(ans):
    if ans == 1:
        return 1
    else:
        return 0

def question():
    point = 0
    for i in Questions:
        print(i, " (ใส่แค่ 1 หรือ 2)", "\n1.Yes\n2.No")
        ans = 3
        while ans > 2:
            ans = int(input(":"))
            point += get_point(ans)
        print("---------------------------------")
    epic_question(point)

# อันนี้ปั่นเฉยๆ 5555
def epic_question(point): # ไม่ว่าใน question() จะตอบยังไงถ้าตอบข้อนี้ว่า Yes ก็คือเป็นคนดี
    print(LastQuesttion, " (ใส่แค่ 1 หรือ 2)", "\n1.Yes\n2.No")
    vip = int(input(":"))
    print("---------------------------------")
    fake_check(point , vip)

def main():
    question()

if __name__ == "__main__":
    main()