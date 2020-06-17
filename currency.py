def count_currency(total_amount=2100, currency_list=[500,50, 20, 10]):
	currency_list.sort(reverse=True)
	final_dict = dict()
	for bill in currency_list:
		final_dict[bill] = 0
		if total_amount >= bill:
			bill_count = total_amount // bill
			total_amount = total_amount - bill_count * bill 
			final_dict[bill] = bill_count
	print (final_dict)
	return (final_dict)
count_currency(2100, [500, 50, 20, 10])
