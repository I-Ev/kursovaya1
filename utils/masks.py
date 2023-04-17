def get_masked_num(something):
    """Определяет счет или карта передана и возвращает
    маскированный номер, шаблон для счета и карты разный """
    parts = str(something).rsplit(" ", 1)
    num = parts[1]
    if len(num) == 16:
        return f"{str(parts[0])} {num[:4]} {num[4:6]}** **** {num[-4:]}"
        # return f"{num[0:(len(num)-1)]} {num[:4]} {num[4:6]}** **** {num[-4:]}"
    if len(num) == 20:
        return f"{str(parts[0])} **{num[-4:]}"
    else:
        print("Что-то непонятное")
        return None

