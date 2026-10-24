def minimum_boxes(cups, large_available, small_available):
    # Eng kam qutilar sonini saqlash uchun o'zgaruvchi. 
    # Boshida -1 qilib qo'yamiz (ya'ni: "hali quti topilmadi" degani).
    min_boxes = -1
    
    # 1. Katta qutilarni 0 tadan boshlab mavjud bo'lganigacha tekshirib chiqamiz (l)
    for l in range(large_available + 1):
        # Katta qutilarga ketgan chashkalarni ayirib, qoldiqni topamiz
        qoldiq = cups - (l * 6)
        
        # Agar qoldiq 0 dan kichik bo'lib ketsa, demak katta qutilar soni oshib ketdi
        if qoldiq < 0:
            break
            
        # 2. Qolgan chashkalar 4 talik kichik qutilarga to'liq (qoldiqsiz) sig'ishi kerak
        if qoldiq % 4 == 0:
            s = qoldiq // 4  # Kichik qutilar soni
            
            # 3. Agar kerakli kichik qutilar soni do'kondagidan oshmasa
            if s <= small_available:
                total_boxes = l + s  # Jami qutilar soni
                
                # 4. Topilgan quti soni eng birinchisi bo'lsa yoki oldingidan kam bo'lsa, saqlaymiz
                if min_boxes == -1 or total_boxes < min_boxes:
                    min_boxes = total_boxes
                    
    # Agar oxirigacha mos quti topilmasa -1 qaytadi, topilsa eng kichigi qaytadi
    return min_boxes


def can_pack(cups, large_available, small_available):
    # minimum_boxes funksiyasi -1 qaytarmasa, demak qadoqlash MUMKIN (True)
    # Agar -1 qaytarsa, imkonsiz (False)
    return minimum_boxes(cups, large_available, small_available) != -1

assert minimum_boxes(18, 3, 0) == 3
assert minimum_boxes(18, 2, 3) == 4
assert minimum_boxes(20, 2, 2) == 4
assert minimum_boxes(8, 2, 0) == -1
assert minimum_boxes(8, 0, 2) == 2
assert minimum_boxes(7, 5, 5) == -1
assert minimum_boxes(0, 0, 0) == 0

assert can_pack(18, 2, 3) == True
assert can_pack(8, 2, 0) == False
