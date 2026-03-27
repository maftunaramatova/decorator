# is_logged_in =True
#
# def login_required(funk):
#     def wrapper():
#         if is_logged_in:
#             return funk()
#         else:
#             print("Iltimos avval login qiling!")
#     return wrapper()
#
# @login_required
# def profile():
#     print("Bu sizning profilingiz!")
# profile()
# 08.07.2025-yil
# Mavzu:while loops


# sum=0
# i=1
# while i < 20:
#     sum+=i
#     i+=1
#
# else:
#     print(f"Tsikl to'xtadi !")
#     print(f"Yig'indi:{sum}!")
# ----------------------------------
#
# sum=0
# i=1
# while i < 100:
#     sum+=i
#     i+=1
#     print(f"Tsikl to'xtadi!")
    # print(f"Yig'indi:{sum}")
#
#10 ta masalalar to'plami:

#1-Masala:

# summa=0
# son=int(input("sonni kiriting(to'xtatish uchun 0 ni:"))
#
# while son !=0:
#     summa=summa+son
#     son=int(input("Sonni kiriting(to'xtatish uchun 0 ni :"))
# print(f"yig'indi:{summa}")

# # 2-Masala
# eng_katta = None
#
# while True:
#     son = int(input("Son kiriting (0 - yakunlash): "))
#     if son == 0:
#         break
#     if (eng_katta is None) or (son > eng_katta):
#         eng_katta = son
#
# if eng_katta is not None:
#     print("Eng katta son:", eng_katta)
# else:
#     print("Hech qanday son kiritilmadi.")

##3-Masala:
# parol_kiritng=input("Parol kiriting:")
# parol="python123"
#
# while parol:
#     if parol==parol_kiritng:
#         print(f"To'g'ri parol: {parol}")
#         break
#     else:
#         print(f"Notog'ri parol ")
#         break

##4-Masala:
# son=int(input("Butun son kiriting:"))
# raqamlar_soni=0
#
# if son == 0:
#     raqamlar_soni=1
# else:
#     son=abs(son)
#     while son >0:
#         son //=10
#         raqamlar_soni+=1
#
# print(f"Raqamlar soni :{raqamlar_soni}ga teng")


##5-Masala:
# son =int(input("Sonni kiriting:"))
# teskari=0
# while son >0:
#     qoldiq=son % 10
#     teskari=teskari *10+ qoldiq
#     son//=10
#     print("Teskari son:",teskari)


##6-Masala:
# son=int(input("Sonni kiriting:"))
#
# #False
# if son < 2:
#     print("Tub emas")
#
# else:
#     i = 2
#     tub = True
#     while i * i <= son:
#         if son % i == 0:
#             tub = False
#             break  ##To'xtatish
#         i += 1
#
#     if tub:
#         print("Tub son !")
#     else:
#         print("Tub emas ! ")

##7-Masala:
# total_letters = 0
#
# while True:
#     text = input("Matn kiriting ('stop' yozilsa to‘xtaydi): ")
#     if text.lower() == 'stop':
#         break
#     total_letters += sum(1 for char in text if char.isalpha())


##8-Masala:
# sum_odd = 0
#
# while True:
#     num = int(input("Son kiriting (0 kiritilsa to‘xtaydi): "))
#     if num == 0:
#         break
#     if num % 2 == 1:
#         sum_odd += num

##9-Masala:
# s=0
# yigindi=0
# harorat=int(input("haroratni kiriting(To'xtatish uchun -100 ni):"))
#
# while harorat!=-100:
#     yigindi+=harorat
#     s+=1
#     harorat=int(input("haroratni kiriting(To'xtatish uchun -100 ni):"))
# if s > 0:
#     print(f"O'rtacha harorat;{yigindi/s}")
# else:
#     print(f"hech qanday harorat kiritilmadi:")

##10-Masala:
# while True:
#     answer = input("Rozimisiz? (ha/yo'q deb yozing): ").strip().lower()
#     if answer == 'ha':
#         print("Rahmat!")
#         break

# # 50 ta masalalar to'plami:

# # 1-masala:
# boshlangich_vazn=int(input("Boshlang'ich vazningizni kiriting:"))
# maqsad_vazn=int(input("Maqsad vazningizni kiriting:"))
# haftalik_yoqotish=0.7
# joriy_vazn=boshlangich_vazn
# hafta=0
#
# while joriy_vazn > maqsad_vazn:
#     joriy_vazn-=haftalik_yoqotish
#     hafta+=1
# print(f"Maqsadga erishish uchun kerakli hafta soni:{hafta} !")



# #2-Masala:
# balandlik=int(input("Daraxt balandlikni kiriting"))
# maqsad=int(input("Daraxt o'sishi uchun maqsad balandlig:"))
# yillik_osish=1.2
# yil=0
#
# while balandlik < maqsad:
#     balandlik*=yillik_osish
#     yil+=1
# print(f"Maqsadga erishish uchun kerakli yil soni ")


##3-Masala:
# energiya=int(input("Elektr energiyani kiriting:"))
# kunlik_sarf=int(input("Elektr kunlik sarfi:"))
# kun=0
#
# while energiya >= kunlik_sarf:
#     energiya -= kunlik_sarf
#     kun+=1
# print(f"Energiya yetadigan kunlar soni:",kun)

##4-Masala:
# pages_written=0
# pages_per_day=2
# edit_per_week=1
# total_pages=100
# days=0
#
# while pages_written < total_pages:
#     pages_written+=pages_per_day
#     days+=1
#     if days % 7 == 0:
#         pages_written-=edit_per_week
# print(f"Kitobni tugatish uchun {days}kun kerak ")

##5-Masala:
# suv=5000
# kunlik_sarf=200
# kun=0
#
# while suv > 0:
#     suv-=kunlik_sarf
#     kun+=1
#
# print("Ombor bo'shaydigan kunlar soni:",kunlik_sarf)

##6-Masala:
# pul=10_000_000
# kunlik_sarf=250_000
# kun=0
#
# while pul >= kunlik_sarf:
#     pul-=kunlik_sarf
#     kun+=1
# print(f"Sayohat davom etadigan kunlar soni:",kun)

##7-Masala:
# observed=0
# per_night=50
# goal=1000
# nights=0
#
# while observed < goal:
#     observed+=per_night
#     nights+=1
# print(f"Katalogni to'ldirish uchun :{nights} kecha kerak!")

##8-Masala:
# joriy_ball=0
# har_oyin_uchun=25
# maqsad=500
# oyinlar=0
#
# while joriy_ball < maqsad:
#     joriy_ball += har_oyin_uchun
#     oyinlar += 1
# print(f"Maqsadga erishish uchun {oyinlar} o'yin kerak !")

##9-Masala:
# umumiy_gisht_soni=1_000
# kunlik_miqdor=50
# kunlar_soni=0
# qoyilgan_gisht=0
#
# while qoyilgan_gisht < umumiy_gisht_soni:
#     qoyilgan_gisht +=kunlik_miqdor
#     kunlar_soni+=1
# print(f"Uy qurilish tugashiga kunlar soni:{kunlar_soni} ga teng")

##10-Masala:
# boshlagich_harorat=30
# soat=0
#
# while boshlagich_harorat >0:
#     boshlagich_harorat -=2
#     soat+=1
# print(f"Natija; {soat} ga teng")



##11-Masala:
# income_per_film = 2_000_000
# goal = 50_000_000
# films = 0
# collected = 0
#
# while collected < goal:
#     collected+=income_per_film
#     films+=1
#
# print(f"Maqsadga erishish uchun :{films} film kerak !")

# #12-masala
# file_size = 100
# speed = 2
# downloaded = 0
# seconds = 0
#
# while downloaded < file_size:
#     downloaded += speed
#     seconds += 1
# print(f"Yuklash {seconds} soniyada tugaydi.")

##13-Masala:
# meva = 500
# kunlik_yigim = 20
# kun = 0
#
# while meva > 0:
#     meva -= kunlik_yigim
#     kun += 1
# print(f"Bog': {kun} kundan keyin bo'shaydi.")

##14-masala:
# value=20_000_000
# depreciation=0.10
# goal_value=5_000_000
# years=0
#
# while value > goal_value:
#     value *=(1-depreciation)
#     years+=1
# print(f"Qiymat {goal_value}so'm bo'guncha {years} yil kerak")

##15-Masala:
# def yugurish_kunlari(maqsad,km,kunlik_km):
#     masofa=0
#     kun=0
#     while masofa < maqsad:
#         masofa += kunlik_km
#         kun += 1
#     return kun
#
# print(yugurish_kunlari(200,10,5))


##16-Masala:
# def iqlim_oshish_yillari(maqsad,yillik_osish):
#     sath=0
#     yillar=0
#     while sath < maqsad:
#         sath +=yillik_osish
#         yillar +=1
#     return yillar
#
# print(iqlim_oshish_yillari(100,20))


##17-Masala:
# video_revenue=50_000
# goal_revenue=1_000_000
# video=0
# earnings=0
#
# while earnings < goal_revenue:
#     earnings += video_revenue
#     video +=1
#
# print(f"Maqsadga erishish uchun : {video} video olishingiz kerak !")

##18-Masala:
# def test_final_day(target_test,daily_test):
#     tests=0
#     days=0
#     while tests < target_test:
#         tests += daily_test
#         days +=1
#     return days
# print(test_final_day(5000,100))

##19-Masala:
# def product_expertion_date(starting_number,daily_sales):
#     residue = starting_number
#     days =0
#     while residue >0:
#         residue -=daily_sales
#     return days
# print(product_expertion_date(2000,150))

##20-Masala:
# def space_distance_time(goal,hourly_distance):
#     distance =0
#     hours =0
#     while distance < goal:
#         distance += hourly_distance
#         hours += 1
#     return hours
# print(space_distance_time( 1000,50_000))


##21-Masala:
# capitale=10_00_000
# rate=0.07
# withdraw_per_year=400_000
# goal=20_000_000
# years=0
#
# while capitale < goal:
#     capitale *=(1+ rate)
#     capitale -=withdraw_per_year
#     years +=1
#     if capitale < 10_000_000:
#         print("Maqsadga yetib bo'lmaydi")
#         break
# else:
#     print(f"{goal} so'mga erishish uchun {years}yil kerak")


##22-Masala:
# def epidemic_spread(beginner,hanging_rate,recovery,goal):
#     sick_people=beginner
#     days=0
#     while sick_people < goal:
#         sick_people *=(1 + hanging_rate)
#         sick_people -= recovery
#         days +=1
#         if sick_people < 0:
#             sick_people=0
#         return days
# print(epidemic_spread(1000,0.15,50,5000))

##23-Masala:
# def waste_collection_day(daily_waste,weekly_repeat,goal):
#     waste=0
#     day=0
#     while waste < goal:
#         waste += daily_waste
#         day += 1
#         if day % 7 == 0:
#             waste -= weekly_repeat
#     return day
# print(waste_collection_day(2,0.5,10))

##24-Masala:
# def kredit_tolov_muddati(kredit,yillik_foiz,oylik_tolov):
#     oylik_foiz=yillik_foiz / 12/100
#     oylar=0
#     while kredit >0:
#         kredit +=kredit * oylik_foiz
#         kredit-=oylik_tolov
#         oylar +=1
#         if kredit < 0:
#             kredit=0
#     return oylar
# print(kredit_tolov_muddati(50_000_000,12,1_000_000))


##25-Masala:
# charge=4000
# use_per_hour=150
# recharge_every=3
# recharge=50
# hours=0
# while charge > 0:
#     charge -= use_per_hour
#     hours += 1
#     if hours % recharge_every ==0:
#         charge += recharge
# print(f"Batareya tugaguncha {hours} soat ishlaydi")

##26-Masala:
# trees=10_000
# year=0
# while trees > 5000:
#     cut = trees * 0.05
#     trees -=cut
#     trees=200
#     year += 1
#
# print(f"5000 tagacha kamyishi uchun yillar soni :{year} ")


##27-Masala:
# fuel = 50
# per_km=0.1
# bonus_every=100
# bonus=2
# distance=0
# while fuel > 0 and distance < 600:
#     fuel -=per_km
#     distance +=1
#     if distance % bonus_every == 0:
#         fuel +=bonus
# print(f"Yonilgi tugashidan keyin : {distance} km bosib o'tdi")

##28-Masala:
# trafik=10
# kun=0
#
# while trafik >0:
#     trafik -=0.5
#     kun += 1
#     if kun % 7 ==0:
#         trafik += 1
#
# print(f"Trafikingiz tugashiga : {kun} kun bor")

##29-Masala:
# mahsulotlar=5000
# kun = 0
#
# while mahsulotlar >0:
#     kun += 1
#     mahsulotlar -=200
#     if kun % 5 == 0:
#         mahsulotlar +=300
# print(f"Ombor bo'shashigacha: {kun} kun kerak  bo'ladi !")

##30-Masala:
# hujayralar= 100
# soat =0
#
# while hujayralar < 500:
#     soat += 1
#     hujayralar *= 1.2
#     if soat % 3 ==0 :
#         hujayralar-=10
#     if hujayralar < 0:
#         hujayralar = 0
#
# print(f"Hujayralar 500 taga yetishi uchun: {soat} soat kerak bo'ladi")

##31-Masala:
# qarz=5_000_000
# hafta=0
#
# while qarz > 0:
#     hafta += 1
#     qarz -=200_000
#     if hafta % 4 == 0:
#         qarz += qarz * 0.1
#     if qarz < 0:
#         qarz=0
#
# print(f"Qarzni to'liq to'lash uchun : {hafta} hafta kerak bo'ladi !")

##32-Masala:
# masofa=0
# tezlik=80
# soat=0
#
# while masofa < 1000:
#     masofa += tezlik
#     soat += 1
#     if soat % 2 == 0:
#         tezlik += 10
#
# print(f"Avtomobil 1000 km yo'lni :{soat} soatda bosib o'tadi !")

##33-Masala:
# harorat=90
# daqiqa=0
#
# while harorat > 50:
#     daqiqa += 1
#     harorat -= 2
#     if daqiqa % 5 == 0:
#         harorat +=3
#
# print(f"Suv harorati 50 C  ga tushishi uchun : {daqiqa} daqiqa kerak bo'ladi")

##34-Masala:
# yuk=10.0
# kun=0
#
# while yuk >0:
#     kun += 1
#     yuk -= 0.8
#     if kun % 3 == 0:
#         yuk += 0.5
#     if yuk < 0:
#         yuk = 0
#
# print(f"Yuk tugashi uchun : {kun} kun kerak bo'ladi !")

##35-Masala:
# oqilgan=0
# kun=0
#
# while oqilgan < 1000:
#     kun += 1
#     oqilgan += 50
#     if kun % 7 == 0:
#         oqilgan -=20
#     if oqilgan < 0 :
#         oqilgan = 0
#
# print(f"Kursni tugatish uchun: {kun} kun kerak bo'ladi !")

##36-Masala:
# ifloslanish = 50
# kun = 0
#
# while ifloslanish < 100:
#     kun += 1
#     ifloslanish += 10
#     if kun % 4 == 0:
#         ifloslanish -=15
#     if ifloslanish < 0:
#         ifloslanish=0
#
# print(f"Havo ifloslanishi 100 PM2.5 ga yetishi uchun : {kun} kun kerak bo'ladi !")


##37-Masala:
# hosil=2000
# kun=0
#
# while hosil >0:
#     kun += 1
#     hosil -= 100
#     if kun % 7 == 0:
#         hosil += 50
#     if hosil < 0:
#         hosil=0
#
# print(f"Hosil tugashi uchun : {kun} kun kerak bo'ladi")

##39-Masala:
# masofa = 0
# kun = 0
#
# while masofa < 0:
#     kun += 1
#     masofa += 5
#     if kun % 3 ==0:
#         masofa -= 2
#
# print(f"Sportchi 100 km yugurishi uchun kunlar soni: {kun} ga teng")

##40-Masala:
# energiya = 10000
# kun = 0
#
# while energiya > 0:
#     kun += 1
#     energiya -= 500
#     if kun % 7 == 0:
#         energiya += 200
#
# print(f"Energiya tugashigacha kunlar soni : {kun} ga teng")


##41-Masala:
# sahifa = 0
# soat = 100
#
# while sahifa < 2000:
#     soat += 100
#     if soat % 20 == 0:
#         sahifa += 1
#
# print(f"Kerakli soat soni : {soat} ga teng")

##42-Masala:
# harorat = 20
# kun = 1
#
# while harorat < 0:
#     harorat += 10
#     if kun % 4 >= 2:
#         kun += 0
#
# print(f"Kun sonini  : {kun} ga teng")

##43-Masala:
# balance = 1_000_000
# years = 0
#
# while balance > 2_000_000:
#     years += 1
#     balance *= 1.08
#     balance -= 200_000
#
# print(f"Yillar soni {years} ga teng")


##44-Masala:
# packaging = 5000
# hour = 200
#
# while packaging < 0:
#     hour -= 200_000
#     hour = 3
#     hour += 50_000
#
# print(f"kerakli soat : {hour} ga teng")

##45-Masala:
# speed = 50
# hour = 2
#
# while speed < 20 :
#     hour -= 2
#     hour = 5
#     hour += 3
#
# print(f"soat soni : {hour} ga teng ")


##46-Masala:

# employee = 50_000
# years = 0
#
# while employee < 100 :
#     years *= 1.1
#     years = 0.5
#     years  -= 5
#
# print (f"Yillar soni : {years} ga teng")


##47-Masala:

# length = 1000_000_000
# days = 50_000
#
# while length < 0:
#     days -= 50
#     days = 7
#     days += 10
#
# print(f"Kun soni : {days} ga teng")

##48-Masala:
# voice = 80_000
# moments = 3
#
# while voice < 50 :
#     moments -= 3
#     moments =4
#     moments += 5
#
# print(f"Kerakli daqiqa soni : {moments} ga teng")

##49-Masala:
# quality = 100_000
# days = 5
#
# while quality < 50 :
#     days -= 5
#     days = 3
#     days += 10
#
# print(f"Kun soni: {days} ga teng")


##50-Masala:
# progress = 0
# days = 2
#
# while progress > 100 :
#     days += 2
#     days = 7
#     days += 1
#
# print(f"Kun soni : {days} ga teng")




# elif yosh <= 61:
# print("3000 so'm")
#
# else:
# print("Hech qanday yosh kiritilmadi")




