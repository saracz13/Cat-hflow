import matplotlib.pyplot as plt
import matplotlib.dates as mpb_dates
import numpy as np
from catshflow.reports.service import reports_service

def graphics():
    print("""
          _____________________
          1. Balance movements
          2. Classification
          ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
          """
          )
    graphic = input("Enter the corresponding number:")
    if graphic == "1":
        print("""
            _____________________  
                FRECUENCY
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            1. WEEKLY
            2. MONTHLY
            3. HALF-YEARLY          
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            """
            )
        frecuency = input("Enter the corresponding number:")
        if frecuency in ["1","2","3"]:
            result,validation = reports_service.balance_movements(frecuency)

            fechas = []
            saldos = []
            for item in result:
                fechas.append(item[0])
                saldos.append(item[1]) 
            plt.style.use('_mpl-gallery')
            fig, ax = plt.subplots()
            ax.plot(fechas, saldos, marker='o', linestyle='-')

            ax.xaxis.set_major_formatter(mpb_dates.DateFormatter('%Y-%m-%d'))
            fig.autofmt_xdate()

            ax.set_xlabel("Date")
            ax.set_ylabel("Total balance")
            ax.set_title("Daily balance evolution")
            print(result)
            print(validation)
            plt.show()
        else:
            return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
    elif graphic == "2":
        print("""
              _______________
              1. CATEGORIES
              2. FUNDS
              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
              """)
        classification = input("Enter the corresponding number:")
        if classification == "1":
            print("""
                ______________
                [1]INCOME
                [2]EXPENDITURE
                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                """)
            transaction_type = input("Enter the corresponding number:")
            print("""
            _____________________  
                FRECUENCY
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            1. WEEKLY
            2. MONTHLY
            3. HALF-YEARLY          
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            """
            ) 
            frecuency = input("Enter the corresponding number:")
            if frecuency in ["1","2","3"]:
                if transaction_type == "1":
                    result,validation = reports_service.category_income(frecuency)

                    labels = list(result.keys())   
                    values = list(result.values())        

                    plt.style.use('_mpl-gallery-nogrid')

                    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))

                    fig, ax = plt.subplots()
                    ax.pie(values, colors=colors, radius=3, center=(4, 4),
                    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

                    ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

                    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                    ylim=(0, 8), yticks=np.arange(1, 8))

                    print(result)
                    print(validation)
                    plt.show()
                elif transaction_type == "2":
                    result,validation = reports_service.category_expenditure(frecuency)

                    labels = list(result.keys())   
                    values = list(result.values())        

                    plt.style.use('_mpl-gallery-nogrid')

                    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))

                    fig, ax = plt.subplots()
                    ax.pie(values, colors=colors, radius=3, center=(4, 4),
                    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

                    ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

                    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                    ylim=(0, 8), yticks=np.arange(1, 8))

                    print(result)
                    print(validation)
                    plt.show()
                else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
            else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
        elif classification == "2":
            print("""
                ______________
                [1]SAVING
                [2]WITHDRAWAL
                ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                """)
            transaction_type = input("Enter the corresponding number:")
            print("""
            _____________________  
                FRECUENCY
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            1. WEEKLY
            2. MONTHLY
            3. HALF-YEARLY          
            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            """
            )
            frecuency = input("Enter the corresponding number:")
            if frecuency in ["1","2","3"]:
                if transaction_type == "1":
                    result,validation = reports_service.fund_savings(frecuency)

                    labels = list(result.keys())   
                    values = list(result.values())        

                    plt.style.use('_mpl-gallery-nogrid')

                    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))

                    fig, ax = plt.subplots()
                    ax.pie(values, colors=colors, radius=3, center=(4, 4),
                    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

                    ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

                    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                    ylim=(0, 8), yticks=np.arange(1, 8))

                    print(result)
                    print(validation)
                    plt.show()
                elif transaction_type == "2":
                    result,validation = reports_service.fund_withdrawal(frecuency)

                    labels = list(result.keys())   
                    values = list(result.values())        

                    plt.style.use('_mpl-gallery-nogrid')

                    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))

                    fig, ax = plt.subplots()
                    ax.pie(values, colors=colors, radius=3, center=(4, 4),
                    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

                    ax.legend(labels, loc='center left', bbox_to_anchor=(1, 0.5))

                    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
                    ylim=(0, 8), yticks=np.arange(1, 8))

                    print(result)
                    print(validation)
                    plt.show()
                else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
            else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
        else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}
    else:
                    return {"Type": "ERROR",
                            "Message": "Please choose a valid option!",
                            "Status code": 400}   
        
        
        

       