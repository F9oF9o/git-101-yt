#pseudo-code
#ตัวแปรที่ระบุสถานะของเกม
score = 0
lives = 3
words = ['tone','Father Gumpon','Brother Jeep','My wife Ja']

#ตราบใจที่ยังมีคำหายทายอยู่
while(ยังมีคำให้ทาย) and (ชีวิตยังเหลือ):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    secret_word = คำสุ่ม
    clue = ['?','?'...]