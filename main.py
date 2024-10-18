import random


#
# print("************************************")
# print("-------------1 uzd.----------------")
#
#
# def sum_int(num1, num2):
#     print(num1 + num2)
#
#
# sum_int(5, 4)
#
# print("************************************")
# print("-------------2 uzd.----------------")
#
#
# def piSq():
#     return 9.8596
#
#
# print(piSq())
#
# print("************************************")
# print("-------------3 uzd.----------------")
#
#
# def multiply_int(num1, num2):
#     return num1 * num2
#
#
# print(multiply_int(5, 4))
#
# print("************************************")
# print("-------------4 uzd.----------------")
#
#
# def print_array(arr):
#     for a in arr:
#         print(f"{a} ", end="")
#
#
# print_array(["labas", "krabas", "kebabas"])
#
# print("************************************")
# print("-------------5 uzd.----------------")
#
#
# def generate_random_number(num1, num2):
#     min = num1 if num1 < num2 else num2
#     max = num2 if num2 > num1 else num1
#     return random.randint(min, max)
#
#
# print(generate_random_number(10, 2))
#
# print("************************************")
# print("-------------6 uzd.----------------")
#
#
# def generate_random_int_numbers(min, max, length):
#     numbers = []
#     for i in range(length):
#         numbers.append(random.randint(min, max))
#     return numbers
#
#
# print(generate_random_int_numbers(2, 12, 10))
#
# print("************************************")
# print("-------------7 uzd.----------------")
#
#
# def sum_int_numbers(int_numbers):
#     sum = 0
#     for n in int_numbers:
#         sum += n
#     return sum
#
#
# print(sum_int_numbers(generate_random_int_numbers(2, 5, 5)))
#
# print("************************************")
# print("-------------8 uzd.----------------")
#
#
# def calculate_average(int_numbers):
#     sum = 0
#     for n in int_numbers:
#         sum += n
#     return sum / len(int_numbers)
#
#
# print(f"Vidurkis: {calculate_average(generate_random_int_numbers(2, 5, 5))}")
#
# print("************************************")
# print("-------------9 uzd.----------------")
#
#
# def draw_rectangle(height, width):
#     rec = ""
#     for i in range(height):
#         for j in range(width):
#             rec += "*"
#         rec += "\n"
#     print(rec)
#
#
# draw_rectangle(5, 5)
#
# print("************************************")
# print("------------10 uzd.----------------")
#
#
# def count_letters_and_spaces(sentence):
#     print(f"Raidziu is viso: {len(sentence)}")
#     print(f"Tarpu is viso: {sentence.count(' ')}")
#     count = 0
#     for s in sentence:
#         if s == " ":
#             count += 1
#     print(f"Antras budas. Tarpu is viso: {count}")
#
#
# count_letters_and_spaces("Šiandien labai graži diena")
#
# print("************************************")
# print("------------11 uzd.----------------")
#
#
# def encode_sentence(sentence):
#     encoded_sentence = ""
#     for i in range(len(sentence) - 1, -1, -1):
#         encoded_sentence += sentence[i]
#     print(f"Uzkoduotas sakinys: {encoded_sentence}")
#
#
# encode_sentence("Šiandien labai graži diena")

# # ******************************* Sudetingesnes ***************************************************
# print("************************************")
# print("-------------1 uzd.----------------")
#
#
# def print_message(text):
#     print(f"---{text}---")
#
#
# print_message("labas")
# print_message("hello")
#
# print("************************************")
# print("-------------2 uzd.----------------")
#
#
# def generate_rnd_str(length):
#     symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
#     text = ""
#     for i in range(length):
#         text += symbols[random.randint(0, len(symbols) - 1)]
#     return text
#
#
# random_characters = generate_rnd_str(20)
# print(random_characters)
# chars = re.findall("[0-9]+|[a-zA-Z]", random_characters)
# for c in chars:
#     if c.isdigit():
#         if len(c) > 1:
#             print(f"[{c}]")
#         else:
#             print(f"[ {c} ]")
#     else:
#         print(c)
#
# print("************************************")
# print("-------------3 uzd.----------------")
#
#
def count_divisors(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    return count
#
#
# print(f"Skaiciaus dalikliai: {count_divisors(10)}")
# print(f"Skaiciaus dalikliai: {count_divisors(20)}")
#
# print("************************************")
# print("-------------4 uzd.----------------")
# array = []
#
#
# def generate_sorted_array():
#     for i in range(100):
#         num = random.randint(33, 78)
#         array.append([num, count_divisors(num)])
#         sorted_array = sorted(array, key=lambda x: x[1], )
#     # print(sorted_array)
#     return [row[0] for row in sorted_array]
#
#
# print(f"Isrusiuotas masyvas: {generate_sorted_array()}")
#
# print("************************************")
# print("-------------5 uzd.----------------")
#
#
# def generate_numbers():
#     array = []
#     for i in range(100):
#         array.append(random.randint(333, 778))
#     return array
#
#
# count = 0
# array = generate_numbers()
# print(array)
# for i in array:
#     if count_divisors(i) == 0:
#         count += 1
# print(f"Is viso pirminiu skaiciu yra: {count}")

print("************************************")
print("-------------6 uzd.----------------")


def append_and_return(arr, element):
    arr.append(element)
    return arr


def generate_numbers_and_array(times, count):
    num_and_arrays = []
    count += 1
    # length = random.randint(10, 20)
    length = 4
    for i in range(length):
        num = random.randint(0, 11)
        num_and_arrays.append(num)
    if count == times:
        num_and_arrays.append(0)
        return num_and_arrays
    else:
        return append_and_return(num_and_arrays, generate_numbers_and_array(times, count))


# print(f"{generate_numbers_and_array(3, 0)}")
# print(f"{generate_numbers_and_array(random.randint(10, 31), 0)}")

print("************************************")
print("-------------7 uzd.----------------")


def sum_numbers(arr, sum):
    for i in range(len(arr)):
        if i != len(arr) - 1:
            sum += arr[i]
        elif arr[-1] == 0:
            return sum
        else:
            return sum_numbers(arr[i], sum)


arr = generate_numbers_and_array(4, 0)
print(arr)
print(f"Suma: {sum_numbers(arr, 0)}")

print("************************************")
print("-------------8 uzd.----------------")


def generate_array():
    arr = []
    for i in range(3):
        arr.append(random.randint(1, 34))
    return arr


def add_additional_number(arr):
    count = 0
    for i in range(len(arr) - 3, len(arr)):
        if count_divisors(arr[i]) > 0:
            count += 1
    if count > 0:
        arr.append(random.randint(1, 34))
        return add_additional_number(arr)
    else:
        return arr


print(f"{add_additional_number(generate_array())}")

print("************************************")
print("-------------9 uzd.----------------")


def generate_two_dimensional_array():
    arr1 = []
    for i in range(10):
        arr2 = []
        for j in range(10):
            arr2.append(random.randint(1, 101))
        arr1.append(arr2)
    return arr1


arr = generate_two_dimensional_array()
print(arr)


def make_additional_operations():
    sum = 0
    count = 0
    for i in arr:
        for j in i:
            if count_divisors(j) > 0:
                sum += j
                count += 1
    average = sum / count
    if average < 70:
        min_element = min([min(r) for r in arr])
        index = [(i, arr2.index(min_element)) for i, arr2 in enumerate(arr) if min_element in arr2]
        arr[index[0][0]][index[0][1]] += + 3
        return make_additional_operations()
    else:
        return average


print(f"Galutinis vidurkis: {make_additional_operations()}")

# # ******************************* PDF ***************************************************
# print("************************************")
# print("-------------1 uzd.----------------")
#
#
# def combine_personal_info():
#     name = "Rasa"
#     reason = "I liked programming stuff"
#     print(f"{name}. {reason}")
#
#
# combine_personal_info()
# combine_personal_info()
# combine_personal_info()
#
# print("************************************")
# print("-------------2 uzd.----------------")
#
#
# def print_poem():
#     line1 = "Pat-a-cake, pat-a-cake, baker’s man"
#     line2 = "Bake me a cake as fast as you can."
#     line3 = "Roll it, and pat it,"
#     line4 = "And mark it with B,"
#     line5 = "And put it in the oven for baby and me."
#     print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")
#
#
# print_poem()
# print_poem()
# print_poem()
# print_poem()
# print_poem()
#
# print("************************************")
# print("-------------3 uzd.----------------")
#
#
# def print_text():
#     print("Text")
#
#
# def print_some_text():
#     print("Some text")
#
#
# def print_another_text():
#     print("Another text")
#
#
# print_text()
# print_some_text()
# print_another_text()
#
# print("************************************")
# print("-------------4 uzd.----------------")
#
#
# def make_first_text_line():
#     return "First text line"
#
#
# def make_second_text_line():
#     return "Second text line"
#
#
# def make_text():
#     return make_first_text_line() + "\n" + make_second_text_line()
#
#
# print(make_text())
#
# print("************************************")
# print("-------------5 uzd.----------------")
#
#
# def sum_random_numbers():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(10, 20)
#     total = num1 + num2
#     print(f"{num1} + {num2} = {total}")
#
#
# sum_random_numbers()
# sum_random_numbers()
# sum_random_numbers()
#
# print("************************************")
# print("-------------6 uzd.----------------")
#
#
# def print_info_about_policeman():
#     name = "Petras"
#     last_name = "Augutis"
#     age = 25
#     salary = 1500
#     emp_status = "pilnas"
#     specialization = "kriminalistas"
#     print(f"Policininkas vardu {name} ir pavarde {last_name}. Jam yra {age} metai. Uždirba {salary} eurų.")
#     print(f"Etatas yra {emp_status}. Specializacija: {specialization}")
#
#
# print_info_about_policeman()
#
# print("************************************")
# print("-------------7 uzd.----------------")
#
#
# def print_random_numbers():
#     for i in range(10):
#         print(random.randint(1, 10), end=" ")
#     print()
#     print()
#
#
# print_random_numbers()
# print_random_numbers()
# print_random_numbers()
# print_random_numbers()
# print_random_numbers()
#
# print("************************************")
# print("-------------8 uzd.----------------")
#
#
# def generate_random_num():
#     print(random.randint(1, 10))
#
#
# for i in range(10):
#     generate_random_num()
#
# print("************************************")
# print("-------------9 uzd.----------------")
#
#
# def print_hello_message(name):
#     print("Labas " + name)
#
#
# def print_goodbye_message(name):
#     print("Viso gero " + name)
#
#
# name = "Petras"
# print_hello_message(name)
# print_goodbye_message(name)
#
# print("************************************")
# print("------------10 uzd.----------------")
#
#
# def print_bigger_number_message(num1, num2):
#     print("Didesnis skaicius yra: ", end="")
#     print(num1 if num1 > num2 else num2 if num2 > num1 else "skaičiai lygūs")
#
#
# print_bigger_number_message(1, 5)
# print_bigger_number_message(19, 3)
# print_bigger_number_message(17, 17)
#
# print("************************************")
# print("------------11 uzd.----------------")
#
#
# def print_car_info(brand, model, year, displacement):
#     print(f"Automobilio marke: {brand}, modelis: {model}, metai: {year}, darbinis turis: {displacement}", end="")
#     print()
#
#
# print_car_info("Toyota", "Yaris", "2021", "1490")
# print_car_info("Kia", "Soul", "2019", "1591")
#
# print("************************************")
# print("------------12 uzd.----------------")
#
#
# def sum_numbers(num1, num2):
#     print(f"{num1} + {num2} = {num1 + num2}")
#
#
# def subtract_numbers(num1, num2):
#     print(f"{num1} - {num2} = {num1 - num2}")
#
#
# def multiply_numbers(num1, num2):
#     print(f"{num1} * {num2} = {num1 * num2}")
#
#
# def divide_numbers(num1, num2):
#     print(f"{num1} / {num2} = {num1 / num2}")
#
#
# def perform_math_operations():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     sum_numbers(num1, num2)
#     subtract_numbers(num1, num2)
#     multiply_numbers(num1, num2)
#     divide_numbers(num1, num2)
#
#
# perform_math_operations()
# perform_math_operations()
# perform_math_operations()
#
# print("************************************")
# print("------------13 uzd.----------------")
#
#
# def print_words(words):
#     for w in words:
#         print(f"{w} - {len(w)}")
#
#
# words = ["hey", "hello", "hi"]
# print_words(words)
#
# print("************************************")
# print("------------14 uzd.----------------")
#
#
# def print_numbers(numbers):
#     for n in numbers:
#         print(f"{n} - {n ** 2} - {n / 2}")
#
#
# numbers1 = [5, 6, 8]
# numbers2 = [4, 2, 8, 6]
#
# print_numbers(numbers1)
# print_numbers(numbers2)
#
# print("************************************")
# print("------------15 uzd.----------------")
#
#
# def print_student_info(grades, full_name):
#     print(f"Vardas/pavardė: {full_name}")
#     print(f"Pažymiai: {grades}")
#     total = 0
#     for g in grades:
#         total += g
#     print(f"Vidurkis: {total / len(grades)}")
#
#
# name = "Ignas Ignauskas"
# grades = [7, 2, 10]
# print_student_info(grades, name)
#
# print("************************************")
# print("------------16 uzd.----------------")
#
#
# def find_max_number(numbers):
#     max = numbers[0]
#     for num in numbers:
#         if num > max:
#             max = num
#     print(f"Didziausias skaicius: {max}")
#
#
# def append_random_numbers(numbers, count):
#     for i in range(count):
#         numbers.append(random.randint(1, 10))
#
#
# numbers1 = []
# numbers2 = []
# numbers3 = []
#
# append_random_numbers(numbers1, 5)
# append_random_numbers(numbers2, 6)
# append_random_numbers(numbers3, 7)
#
# print(numbers1)
# print(numbers2)
# print(numbers3)
#
# find_max_number(numbers1)
# find_max_number(numbers2)
# find_max_number(numbers3)
#
# print("************************************")
# print("------------17 uzd.----------------")
#
#
# def get_my_favorite_sentence():
#     return "Pasaulis gražus"
#
#
# print(get_my_favorite_sentence())
#
# print("************************************")
# print("------------18 uzd.----------------")
#
#
# def get_random_number():
#     return random.randint(1, 10)
#
#
# print(f"Skaicius: {get_random_number()}")
# print(f"Skaicius: {get_random_number()}")
# print(f"Skaicius: {get_random_number()}")
#
# print("************************************")
# print("------------19 uzd.----------------")
#
#
# def generate_student_info_message(name, average):
#     return "Studentas " + name + " turi vidurkį " + str(average)
#
#
# print(generate_student_info_message("Giedrius", 6.4))
# print(generate_student_info_message("Paulius", 8.3))
# print(generate_student_info_message("Vilius", 9.4))
#
# print("************************************")
# print("------------20 uzd.----------------")
#
#
# def find_lowest_divisor(num):
#     for i in range(2, num + 1):
#         if num % i == 0:
#             return i
#
#
# for i in range(10, 31):
#     print(f"{i} - {find_lowest_divisor(i)}")
#
# print("************************************")
# print("------------21 uzd.----------------")
#
#
# def find_prime_number(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
#
# for i in range(2, 15):
#     print(f"{i} {str(find_prime_number(i)).lower()}")
#
# print("************************************")
# print("------------22 uzd.----------------")
#
#
# def sum_numbers(num1, num2, num3=0):
#     return num1 + num2 + num3
#
#
# def subtract_numbers(num1, num2, num3=0):
#     return num1 - num2 - num3
#
#
# def multiply_numbers(num1, num2, num3=1):
#     return num1 * num2 * num3
#
#
# def divide_numbers(num1, num2, num3=1):
#     return num1 / num2 / num3
#
#
# # def perform_math_operations():
# #     num1 = random.randint(1, 10)
# #     num2 = random.randint(1, 10)
# #     print(f"{num1} + {num2} = {sum_numbers(num1, num2)}")
# #     print(f"{num1} - {num2} = {subtract_numbers(num1, num2)}")
# #     print(f"{num1} * {num2} = {multiply_numbers(num1, num2)}")
# #     print(f"{num1} / {num2} = {divide_numbers(num1, num2)}")
#
#
# def perform_math_operations():
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     num3 = random.randint(1, 10)
#     print(f"{num1} + {num2} + {num3} = {sum_numbers(num1, num2, num3)}")
#     print(f"{num1} - {num2} - {num3} = {subtract_numbers(num1, num2, num3)}")
#     print(f"{num1} * {num2} * {num3} = {multiply_numbers(num1, num2, num3)}")
#     print(f"{num1} / {num2} / {num3} = {divide_numbers(num1, num2, num3)}")
#
#
# perform_math_operations()
#
# print("************************************")
# print("------------23 uzd.----------------")
#
#
# def sum_arr_numbers(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n
#     return sum
#
#
# numbers1 = [4, 8, 2]
# numbers2 = [2, 3, 1]
#
# sum1 = sum_arr_numbers(numbers1)
# sum2 = sum_arr_numbers(numbers2)
# print(sum1)
# print(sum2)
# print(f"Didesne suma: ", end="")
# print(sum1 if sum1 > sum2 else sum2 if sum2 > sum1 else "sumos vienodos")
#
# print("************************************")
# print("------------24 uzd.----------------")
#
#
# def find_longest_word(words):
#     max = len(words[0])
#     word = words[0]
#     for w in words:
#         if len(w) > max:
#             max = len(w)
#             word = w
#     return word, max
#
#
# words = ["labas", "kebabas", "krabas"]
# word, length = find_longest_word(words)
# print(f"Ilgiausias zodis: {word}. Ji sudaro {length} raides.")
#
# print("************************************")
# print("------------25 uzd.----------------")
#
#
# def is_every_grade_positive(grades):
#     count = 0
#     for g in grades:
#         if g > 4:
#             count += 1
#     return count == len(grades)
#
#
# def print_grades_message(grades):
#     if is_every_grade_positive(grades):
#         print("visi studento pažymiai teigiami")
#     else:
#         print("studentas turi bent vieną neigiamą pažymį")
#
#
# print_grades_message([8, 9, 5, 6, 7])
# print_grades_message([4, 5, 2, 8, 9])
#
# # 26 uzduotis -> 22 uzduotis
