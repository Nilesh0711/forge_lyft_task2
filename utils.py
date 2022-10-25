def add_years_to_date(original_date, year_to_add):
    result = original_date.replace(year=original_date.year+year_to_add)
    return result
