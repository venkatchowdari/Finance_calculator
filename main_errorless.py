'''
⁜ This a program calculate the finace of person on there expence

'''

def calaculate_finance(monthly_salary: float, tax_rate: float, gym_membership:float, rent:float, food: float, currency: str)->None:
    monthly_tax_rate: float = monthly_salary * (tax_rate/100)
    monthly_expense: float = gym_membership + rent  + food 
    monthly_net_income: float = monthly_salary - (monthly_expense + monthly_tax_rate) 
    yearly_salary: float = monthly_salary * 12
    yearly_expense : float  = monthly_expense * 12
    yearly_tax_rate: float = yearly_salary * monthly_tax_rate
    yearly_net_income:float = monthly_net_income * 12
    
    print('\n-----------------------------------------------------------\n')
    
    print(f'Monthly income : {currency}{monthly_salary:,.2f}')    
    print(f'Monthly Expense : {currency}{monthly_expense:,.2f}')
    print(f'Monthly Net income : {currency}{monthly_net_income:,.2f}')
    print(f'Yearly Salary : {currency}{yearly_salary:,.2f}')
    print(f'Yearly Tax Rate : {currency}{yearly_tax_rate:,.2f}')
    print(f'Your per year income : {currency}{yearly_expense:,.2f}')
    print(f'Yearly Net income : {currency}{yearly_net_income:,.2f}\n')
    
    print('-----------------------------------------------------------')
    

def main():
    try:
        monthly_salary = float(input("Enter the monthly salary : "))
        tax_rate = float(input("Enter the tax rate in your region : "))
        gym_membership = float(input("Enter the price gym membership for month : "))
        rent = float(input("Enter your house rent : "))
        currency = input("Enter your currency : ")
        food = float(input("Enter your expense for food : "))
    
        calaculate_finance(monthly_salary, tax_rate, gym_membership, rent, food, currency)
    except ValueError as e:
        print(f'Error : {e}')
    
    
if __name__ == '__main__':
    main()
    
    