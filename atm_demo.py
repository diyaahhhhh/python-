balance_amount=1000
while True:
    print('1. \tCheck the balance')
    print('2. \tDeposit money')
    print('3. \tWithdraw money')
    print('4. \tExit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        print(f'Current balance amount: ${balance_amount}')
    elif choice==2:
        deposit=float(input('Enter the amount to be deposited: '))
        balance_amount+=deposit
        print(f'${balance_amount} successfully deposited!\nCurrent balance:',balance_amount)
    elif choice==3:
          withdraw=float(input('Enter the amount to be withdrawn:'))
          if withdraw>1000:
              print('Insufficient balance!')
          else:
              balance_amount -= withdraw
              print(withdraw,'successfully withdrawn! \nCurrent balance: $',balance_amount)
    else:
        break