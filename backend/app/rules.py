import datetime

class FLAGS:
    GREEN = 1
    AMBER = 2
    RED = 0
    MEDIUM_RISK = 3  # display purpose only
    WHITE = 4  # data is missing for this field


# This is already written for your reference
def latest_financial_index(data: dict):
    for index, financial in enumerate(data.get("financials")):
        if financial.get("nature") == "STANDALONE":
            print(index)
            return index
    return 0


def total_revenue(data: dict, financial_index: int) -> float:
    financials = data["financials"][financial_index]
    try:
        return financials["pnl"]["lineItems"]["net_revenue"]
    except KeyError:
        print("net_revenue key not found")
        return 0


def total_borrowing(data: dict, financial_index: int) -> float:
    financials = data["financials"][financial_index]
    
    # Use .get() to safely access 'longTermBorrowing' and provide a default of 0 if it's missing
    long_term_borrowing = financials["bs"]["liabilities"].get("long_term_borrowings")
    short_term_borrowing = financials["bs"]["liabilities"].get("short_term_borrowings")

    total_borrowing = long_term_borrowing + short_term_borrowing
    print(long_term_borrowing,short_term_borrowing,'khhhkhj')
    return total_borrowing


def iscr(data: dict, financial_index: int) -> float:
    financials = data["financials"][financial_index]
    profit_before_interest_tax = financials["pnl"]["lineItems"]["profit_before_tax"]
    depreciation = financials["pnl"]["lineItems"].get("depreciation", 0)
    interest_expenses = financials["pnl"]["lineItems"].get("interest", 0)
    
    return (profit_before_interest_tax + depreciation + 1) / (interest_expenses + 1)


def iscr_flag(data: dict, financial_index: int):
    iscr_value = iscr(data, financial_index)
    if iscr_value >= 2:
        return FLAGS.GREEN
    return FLAGS.RED


def total_revenue_5cr_flag(data: dict, financial_index: int):
    revenue = total_revenue(data, financial_index)
    if revenue >= 50_000_000:
        return FLAGS.GREEN
    return FLAGS.RED


def borrowing_to_revenue_flag(data: dict, financial_index: int):
    total_borrowings_value = total_borrowing(data, financial_index)
    total_revenue_value = total_revenue(data, financial_index)
    print(total_borrowings_value,total_revenue_value)

    if total_revenue_value == 0:
        print("Total revenue is zero, cannot calculate borrowing to revenue ratio.")
        return FLAGS.RED  # Return RED flag since no revenue means a higher risk.

    ratio = total_borrowings_value / total_revenue_value
    print(ratio)

    if ratio <= 0.25:
        return FLAGS.GREEN
    return FLAGS.AMBER

