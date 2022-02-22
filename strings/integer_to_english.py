def integer_to_eng(number):
    to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
    tens = "Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety".split()
    big_nums = {1000000000 : "Billion", 1000000: "Million", 1000: "Thousand" }
    
    def convert(num):
        if num < 20:
            return to19[num-1:num]
        if num < 100:
            return [tens[num//10-2]] + convert(num%10)
        if num < 1000:
            return [to19[num//100-1]] + ["Hundred"] + convert(num%100)
        else:
            for i in [1000000000, 1000000, 1000]:
                if num // i > 0:
                    return convert(n//i) + [big_nums[i]] + convert(n%i)


    return ' '.join(convert(number)) or "Zero"

number = 123
print("Converting {} into {}".format(number, integer_to_eng(number)))
