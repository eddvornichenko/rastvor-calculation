import math

width = int(input("Введите ширину, мм: "))

height = int(input("Введите высоту, мм: "))

depth = int(input("Введите толщину, мм: "))

betonomeshalka_size = int(input("Введите объем бетономешалки, м3: "))

volume_mm = width*height*depth

volume_m = volume_mm / 100000000

betonomeshalka_volume = betonomeshalka_size - (betonomeshalka_size * 0.04)

sum_zames = round((volume_m / betonomeshalka_volume), 1)

# На 1 замес на 25 литров воды или 2,5 ведра
water_1 = 25

volume_water = math.ceil(water_1 * sum_zames)

# 1 замес - это один мешок объемом 25 кг.
cement_volume = 25
q_cement = sum_zames
kg_cement = round((sum_zames * cement_volume), 1)

# 1 замес - это 24 лопаты или 8 ведер. Одна тачка 30 лопат
shlak_1_lopata = 24
q_shlak_lopata = sum_zames * shlak_1_lopata
q_shlak_vedro = q_shlak_lopata / 3

# 1 тачка это 30 лопат

tachka_1 = 24 / 30
q_tachka = math.ceil(tachka_1 * sum_zames)

print(f'''

Объем заливки {volume_m} м3.
Количество замесов - {sum_zames} шт.

Для этого необходимо:
Вода - {volume_water} л.
Цемент - {q_cement} мешков или {kg_cement} кг.
Шлак - {q_tachka} тачек

''')
