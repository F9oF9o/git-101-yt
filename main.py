#pseudo-code
#ตัวแปรที่ระบุสถานะของเกม
import random
score = 0
lives = 3
words = ['tone','Father Gumpon','Brother Jeep','My wife Ja']

#ตราบใจที่ยังมีคำให้ทายอยู่ และ ชีวิตยังเหลือ ---> เล่นต่อไป
while(len(words>0)) and (lives>0):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word)) 
#ตราบในที่ยังทายคำนี้ไม่เสร็จหรือชีวิตยังไม่หมด
while True:
    print(clue)
    print('ชีวิตที่เหลือ : '+ lives)
    guess = input ('ทายตัวอักษรมาซิ: ') 
    #Chek ว่าตัวอักษรที่ทายอยู่ใน Secret_word ป่าว !?
    if guess in secret_word:
        win = update_clue(guess, secret_word, clue)
        if win: 
            print('เย้! คำนั้นก็คือ: '+secret_word)
            score = score+1
             print('score : '+ score)
        else: #ที่ guess มาไม่อยู่ใน secret_word
           print('ผิด! เอื้อก')
           lives = lives -1
           if lives ==0:
              print('เจ้าแพ้แล้ว ' +secret_word)
              break
           
print('Final Score ' +score)
print('Game end!!!')