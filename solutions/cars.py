def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    old_car = start_price_old
    new_car = start_price_new
    monthly = 0
    percent = percent_loss_by_month/100
    
    if monthly+old_car>=new_car:
        left = monthly+old_car-new_car
        return [0,left]
    
    for i in range(0,100):
        if monthly+old_car>=new_car:
            left = monthly-new_car+old_car
            left = round(left)
            month = i+1
            break
        old_car-= old_car*percent
        new_car-= new_car*percent
        monthly+=saving_per_month
        if i%2==0:
            percent+=0.005
        if monthly+old_car>=new_car:
            left = monthly-new_car+old_car
            left = round(left)
            month = i+1
            break
    return [month,left]
