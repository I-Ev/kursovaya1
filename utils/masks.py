def get_masked_num(number):
    """Определяет счет или карта передана и возвращает
    маскированный номер, шаблон для счета и карты разный """
    num = str(number).split(" ")[-1]
    if len(num) == 16:
        return f"{num[:4]} {num[4:6]}** **** {num[-4:]}"
    if len(num) == 20:
        return f"**{num[-4:]}"
    else:
        print("Что-то непонятное")
        return None

