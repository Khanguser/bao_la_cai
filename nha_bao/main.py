from guizero import App, Text, Picture, Box

app = App(title="Báo thanh niên", width=500, height=500, bg="white")

header_box = Box(app)
Text(header_box, text="140 tờ trúng xổ số miền Nam ngày 8 tháng 10: Đại lý đổi thưởng ngay", size=20, color="black")

greeting = Text(app, text = "Vừa có kết quả xổ số miền Nam ngày 8 tháng 10 chiều nay, một đại lý vé\n"
                             "số ở Vĩnh Long cho biết đã bán trúng 140 tờ và đổi thưởng ngay cho\n"
                             "khách.\n",
                             color="black", font="Arial", size=15)
picture = Picture(app, image = "images/ve_so.png", width=200, height=150)
greeting2 = Text(app, text = "Kết quả xổ số miền Nam thứ tư mở thưởng chiều nay ghi nhận đài Đồng Nai\n"
                              "có dãy số trúng độc đắc là 362384 và đài Cần Thơ với dãy số trúng độc\n" 
                              "đắc là 046439.\n"
                              "Hình ảnh những cọc vé số trúng thưởng được dân mạng quan tâm. Nhiều\n"
                              "người để lại bình luận chúc mừng chủ nhân những tờ vé may mắn cũng như\n"
                              "hy vọng sớm được trúng số.\n"
                              "Gần đây, phía đại lý vé số Phát Tài ở xã Đức Hòa (Tây Ninh) thông báo đã\n"
                              "bán trúng 14 tờ giải tám cho khách, thuộc xổ số Bến Tre ngày 7 tháng 10.\n"
                              "Cụ thể, những tờ vé có hai số cuối là 93, trong khi đó giải độc đắc của đài\n"
                              "Bến Tre mở thưởng hôm đó thuộc về những tờ có dãy số 973204.\n",
                              color="black", font="Arial", size = 14)
app.display()