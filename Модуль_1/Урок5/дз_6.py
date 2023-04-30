vidhuk_menu = ''
vidhuk_sportzal = ''
vidhuk_obslugovuvannia = ''
total_sale = 0
if vidhuk_menu:
    if len(vidhuk_menu) >= 60:
        total_sale = total_sale + 15
    else:
        total_sale = total_sale + 5
if vidhuk_sportzal:
    if len(vidhuk_sportzal) >= 60:
        total_sale = total_sale + 15
    else:
        total_sale = total_sale + 5
if vidhuk_obslugovuvannia:
    if len(vidhuk_obslugovuvannia) >= 60:
        total_sale = total_sale + 15
    else:
        total_sale = total_sale + 5
if not vidhuk_menu and vidhuk_sportzal and vidhuk_obslugovuvannia:
    total_sale = 0
    #не працює наступний рядок
    print('Залиште відгук про надані послуги та отримайте знижку на наступне відвідування!')
print('Загальний розмір знижки на наступне відвідування становить:' + ' ' + total_sale.__str__() + '%')
