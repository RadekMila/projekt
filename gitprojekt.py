# Mapa świata

import matplotlib as mat
import cartopy.crs as ccrs
import cartopy.feature as cft
import matplotlib.pyplot as plt


def wybor():
    print("Możesz wybrać czy chcesz zobaczyć mape/kraje europy czy ich statystyki.")
    user = input("Chcesz zobaczyć mape danego kraju w europie czy statystyki.M/S\n:").capitalize()
    if user == "M":
        Mapa_europy()
    elif user == "S":
        Statystyki_europy()


def Statystyki_europy():
    user = input("Wybierz jakie kraju chcesz zobaczyć statystyki,chyba ze chcesz zobaczyc wszystkie wpisz \"Wszystkie\".Jak chcesz zobaczyć srednią europy wpisz \"srednia\":").capitalize()

    statystyki_krajów_ludność = {
        "Polska": 38,
        "Niemcy": 83,
        "Fracja": 67,
        "Hiszpania": 47,
        "Włochy": 60,
        "Czechy": 10.5,
        "Słowacja": 5.4,
        "Austria": 9.1,
        "Węgry": 9.6,
        "Rumunia": 19.0,
        "Norwegia": 5.5,
        "Szwecja": 10.5,
        "Finlandia": 5.6,
        "Dania": 5.9,
        "Irlandia": 5.3,
        "Portugalia": 10.2,
        "Belgia": 11.8,
        "Holandia": 17.5,
        "Szwajcaria": 8.8,
        "Litwa": 2.8,
        "Łotwa": 1.8,
        "Estonia": 1.3,
        "Grecja": 10.3,
        "Bułgaria": 6.4,
        "Chorwacja": 3.8
    }

    srednia = sum(statystyki_krajów_ludność.values()) / len(statystyki_krajów_ludność)
    statystyki_krajów_ludność["Srednia"] = round(srednia, 2)


    statystyki_krajów_PKB = {
        "Polska": 809,
        "Niemcy": 4526,
        "Francja": 3052,
        "Hiszpania": 2301,
        "Włochy": 1620,
        "Czechy": 360,
        "Słowacja": 130,
        "Austria": 520,
        "Węgry": 210,
        "Rumunia": 320,
        "Norwegia": 550,
        "Szwecja": 660,
        "Finlandia": 320,
        "Dania": 460,
        "Irlandia": 590,
        "Portugalia": 290,
        "Belgia": 600,
        "Holandia": 1100,
        "Szwajcaria": 830,
        "Litwa": 75,
        "Łotwa": 45,
        "Estonia": 39,
        "Grecja": 300,
        "Bułgaria": 100,
        "Chorwacja": 80
    }
    srednia2 = sum(statystyki_krajów_PKB.values()) / len(statystyki_krajów_PKB)
    statystyki_krajów_PKB["Srednia"] = round(srednia2, 2)

    statystyki_krajów_powierzchnia = {
        "Polska": 312696,
        "Niemcy": 357022,
        "Francja": 643801,
        "Hiszpania": 505370,
        "Włochy": 301340,
        "Czechy": 78865,
        "Słowacja": 49035,
        "Austria": 83871,
        "Węgry": 93028,
        "Rumunia": 238397,
        "Norwegia": 385207,
        "Szwecja": 450295,
        "Finlandia": 338424,
        "Dania": 42933,
        "Irlandia": 70273,
        "Portugalia": 92212,
        "Belgia": 30528,
        "Holandia": 41543,
        "Szwajcaria": 41285,
        "Litwa": 65300,
        "Łotwa": 64589,
        "Estonia": 45227,
        "Grecja": 131957,
        "Bułgaria": 110994,
        "Chorwacja": 56594
    }
    srednia3 = sum(statystyki_krajów_powierzchnia.values()) / len(statystyki_krajów_powierzchnia)
    statystyki_krajów_powierzchnia["Srednia"] = round(srednia3, 2)

    statystyki_krajów_PKB_per_capita = {
        "Polska": 17391,
        "Niemcy": 44337,
        "Francja": 639117,
        "Hiszpania": 28570,
        "Włochy": 34088,
        "Czechy": 34000,
        "Słowacja": 24000,
        "Austria": 57000,
        "Węgry": 22000,
        "Rumunia": 17000,
        "Norwegia": 100000,
        "Szwecja": 63000,
        "Finlandia": 57000,
        "Dania": 77000,
        "Irlandia": 115000,
        "Portugalia": 28000,
        "Belgia": 51000,
        "Holandia": 63000,
        "Szwajcaria": 96000,
        "Litwa": 27000,
        "Łotwa": 25000,
        "Estonia": 30000,
        "Grecja": 28000,
        "Bułgaria": 16000,
        "Chorwacja": 21000
    }
    srednia4 = sum(statystyki_krajów_PKB_per_capita.values()) / len(statystyki_krajów_PKB_per_capita)
    statystyki_krajów_PKB_per_capita["Srednia"] = round(srednia4, 2)


    if user in statystyki_krajów_ludność:
        plt.figure(figsize=(9, 4.5))
        plt.bar(user, statystyki_krajów_ludność[user], color="orange",width=0.3)
        plt.title("Liczba ludności w danym kraju")
        plt.ylabel("Liczba ludności w (mln)")
        plt.xlabel("KRAJ")
        plt.grid(axis='y')
        plt.xlim(-1,1)


        plt.figure(figsize=(9, 4.5))
        plt.bar(user, statystyki_krajów_PKB[user], color="orange", width=0.3)
        plt.title("PKB (Produkt krajowy brutto)")
        plt.ylabel("Liczba PKB w (mld)(USD)")
        plt.xlabel("KRAJ")
        plt.grid(axis='y')
        plt.xlim(-1, 1)


        plt.figure(figsize=(9,4.5))
        plt.bar(user, statystyki_krajów_powierzchnia[user], color="orange", width=0.3)
        plt.title("Powierzchnia")
        plt.ylabel("(Podana w km²)")
        plt.xlabel("KRAJ")
        plt.grid(axis='y')
        plt.xlim(-1, 1)


        plt.figure(figsize=(9,4.5))
        plt.bar(user,statystyki_krajów_PKB_per_capita[user],color="orange", width=0.3)
        plt.title("PKB PER CAPITA")
        plt.ylabel("Podanew w USD")
        plt.xlabel("KRAJ")
        plt.grid(axis='y')
        plt.xlim(-1,1)
        plt.show()


    else:
        print("Nie ma podanego kraju w słowniku.")


def Mapa_europy():
    user = input("Wybierz Państwo w europie,lub wpisz europa:").capitalize()

    kraje_slownik = {
        "Polska": [13.5, 24.5, 48.5, 55.5],
        "Czechy": [12.0, 19.0, 48.0, 51.5],
        "Słowacja": [16.5, 23.0, 47.5, 50.5],
        "Francja": [-5.0, 8.5, 41.0, 51.5],
        "Niemcy": [5.5, 15.5, 47.0, 55.0],
        "Włochy": [6.5, 18.5, 36.0, 47.5],
        "Hiszpania": [-9.5, 4.5, 36.0, 44.0],
        "Austria": [9.0, 17.0, 46.0, 49.5],
        "Węgry": [16.0, 23.0, 45.5, 48.5],
        "Rumunia": [20.0, 30.0, 43.0, 48.5],
        "Norwegia": [4.0, 31.0, 57.5, 71.5],
        "Szwecja": [11.0, 24.5, 55.0, 69.5],
        "Finlandia": [20.0, 32.0, 59.5, 70.5],
        "Dania": [8.0, 13.0, 54.5, 58.0],
        "Irlandia": [-11.0, -5.0, 51.0, 55.5],
        "Portugalia": [-10.0, -6.0, 36.5, 42.5],
        "Belgia": [2.5, 6.5, 49.5, 51.7],
        "Holandia": [3.0, 7.5, 50.5, 53.7],
        "Szwajcaria": [5.5, 10.5, 45.5, 47.8],
        "Litwa": [20.5, 27.0, 53.8, 56.5],
        "Łotwa": [21.0, 28.0, 55.5, 58.2],
        "Estonia": [21.5, 28.5, 57.0, 59.8],
        "Grecja": [19.0, 28.5, 34.5, 42.0],
        "Bułgaria": [22.0, 28.5, 41.0, 44.5],
        "Chorwacja": [13.0, 20.0, 42.0, 47.0],
        "Europa":  [-25.0, 45.0, 34.0, 72.0]
    }

    plt.figure(figsize=(13, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(kraje_slownik[user])

    ax.add_feature(cft.BORDERS, linewidth=1)
    ax.add_feature(cft.COASTLINE)
    ax.add_feature(cft.OCEAN, facecolor="lightblue")

    ax.text(21.01, 52.23, "Warszawa", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(21.01, 52.23, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(14.4378005, 50.0755381, "Praga", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(14.4378005, 50.0755381, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(17.11, 48.15, "Bratysława", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(17.11, 48.15, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(13.40, 52.52, "Berlin", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(13.40, 52.52, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(2.35, 48.85, "Paryż", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(2.35, 48.85, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(12.48, 41.89, "Rzym", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(12.48, 41.89, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(-3.70, 40.42, "Madryt", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(-3.70, 40.42, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(16.37, 48.21, "Wiedeń", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(16.37, 48.21, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(19.04, 47.50, "Budpeszt", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(19.04, 47.50, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(26.10, 44.43, "Bukareszt", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(26.10, 44.43, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(10.75, 59.91, "Oslo", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(10.75, 59.91, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(18.06, 59.33, "Sztokholm", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(18.06, 59.33, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(24.94, 60.17, "Helsinki", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(24.94, 60.17, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(12.57, 55.68, "Kopenhaga", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(12.57, 55.68, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(-6.26, 53.35, "Dublin", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(-6.26, 53.35, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(-9.14, 38.72, "Lizbona", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(-9.14, 38.72, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(4.35, 50.85, "Bruksela", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(4.35, 50.85, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(4.90, 52.37, "Amsterdam", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(4.90, 52.37, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(7.45, 46.95, "Berno", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(7.45, 46.95, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(25.28, 54.68, "Wilno", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(25.28, 54.68, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(24.10, 56.95, "Ryga", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(24.10, 56.95, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(24.75, 59.44, "Tallin", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(24.75, 59.44, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(23.72, 37.98, "Ateny", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(23.72, 37.98, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(23.32, 42.70, "Sofia", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(23.32, 42.70, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    ax.text(15.98, 45.81, "Zagrzeb", fontsize="9", transform=ccrs.PlateCarree())
    ax.plot(15.98, 45.81, marker="o", color="blue", markersize="3", transform=ccrs.PlateCarree())

    # ax.gridlines(draw_labels=True)

    plt.show()


wybor()
