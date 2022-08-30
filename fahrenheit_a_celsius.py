import os;

if __name__ == "__main__":
    # os.system("clear"); # comando que solo funciona en linux
    os.system("cls"); # comando que solo funciona para windows

    temperaturaFahrenheit = 32;
    temperaturaCelsius = 0;

    print("=========================");
    print("Conversión de temperatura");
    print("=========================");
    print("Fahrenheit a Celsius\n");
    while (temperaturaFahrenheit <= 40):
        temperaturaCelsius = float((temperaturaFahrenheit - 32) * 5 / 9);
        print(f"{temperaturaFahrenheit}°F -> {round(temperaturaCelsius, 2)}°C");
        temperaturaFahrenheit += 1;

    input("\n!!Presione enter para continuar...");