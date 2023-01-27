def get_tax_rate(income, number_of_children):

    income_in_k = income/1000  # more readable in thousands
    p_a         = 12.5         # personal allowance is £12.5k 
    b_r         = 0.20         # base rate is 20% 

    # implementation strategy: divide into income_tax_rate and 'benefit_tax_rate '

    tax_thresholds      = [0,   p_a,  50,   145]  
    tax_rates           = [0.0, b_r, 0.40, 0.45] # let's always use .0 for precentages

    clawback_windows     = [(50, 60), (100, 120)]  # treat child benefit and personal allowance in the same way

    child_benefit_rates = [0.0, 0.12, 0.17] 
    child_benefit_rate  = child_benefit_rates[number_of_children] # ouch! no input validation

    personal_allowance_rate = (p_a*b_r)/(clawback_windows[1][1]-clawback_windows[1][0])
    print(personal_allowance_rate)
    clawback_rates        = (child_benefit_rate, personal_allowance_rate)

    income_tax_rate = 0.0  # yay! by default, no tax

    for threshold, rate in zip(tax_thresholds[::-1], 
                               tax_rates[::-1]):
        if income_in_k>threshold:
            income_tax_rate = rate
            break

    clawback_rate= 0
    for threshold, rate in zip(clawback_windows, clawback_rates):
        if income_in_k > threshold[0] and income_in_k < threshold[1]:
            print(f"adding {rate} at {threshold[0]}")
            clawback_rate += rate
    total_tax_rate = income_tax_rate + clawback_rate

    return total_tax_rate*100