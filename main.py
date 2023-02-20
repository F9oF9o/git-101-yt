#pseudo-code
#ตัวแปรที่ระบุสถานะของเกม
import random
from tkinter import * 
import time

Windows = Tk()

score = 0
lives = 3
words = ['tone','Father Gumpon','Brother Jeep','My wife Ja']

def update_clue(guess, secret_word, clue):
   #guess ไล่ไปทีละตัวอักษรใน secret_word ดูว่ามีตัวไหนบ้างตรงกับที่ทาย
   for i in range(len(secret_word)):
      #ถ้าทายตรงตัวไหน ก็อัพเดทเบาะแสตรงตำแหน่งนั้น
      if guess == secret_word[i]:
        clue[i] = guess
        win = ''.join(clue) == secret_word
   return win #ทายจนไม่เหลือ '?' ให้เป็นสถานะ True ถ้ายังเหลือให้เป็น False
#ตราบใจที่ยังมีคำให้ทายอยู่ และ ชีวิตยังเหลือ ---> เล่นต่อไป
while(len(words) > 0) and ((lives)>0 ):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word)) 
#ตราบในที่ยังทายคำนี้ไม่เสร็จหรือชีวิตยังไม่หมด
while True:
    print(clue)
    print('ชีวิตที่เหลือ : '+ str(lives))
    guess = input ('ทายตัวอักษรมาซิ: ') 
    #Chek ว่าตัวอักษรที่ทายอยู่ใน Secret_word ป่าว !?
    if guess in secret_word:
        win = update_clue(guess, secret_word, clue)
        if win: 
            print('เย้! คำนั้นก็คือ: '+secret_word)
            score = score+1
            print('score : '+ str(score))
        else: #ที่ guess มาไม่อยู่ใน secret_word
           print('ผิด! เอื้อก')
           lives = lives - 1
           if lives == 0:
              print('เจ้าแพ้แล้ว ' +secret_word)
              break
           
print('Final Score ' + str(score))
print('Game end!!!')