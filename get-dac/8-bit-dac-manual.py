import RPi.GPIO as GPIO

dac_bits = [22, 27, 17, 26, 25, 21, 20, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_bits, GPIO.OUT)

dynamic_range = 3.17

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    
    binary_str = format(number, '08b')
    
    bits_for_print = [int(bit) for bit in binary_str]
    
    bits_for_gpio = [int(bit) for bit in reversed(binary_str)]
    
    for i in range(8):
        GPIO.output(dac_bits[i], bits_for_gpio[i])
    
    print(f"Число на вход ЦАП: {number}, биты: {bits_for_print}")

try:
    while True:
        try:
            line = input("Введите напряжение в Вольтах: ")
           
            
            voltage = float(line)
            
            number = voltage_to_number(voltage)
            number_to_dac(number)
            print("") 

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()