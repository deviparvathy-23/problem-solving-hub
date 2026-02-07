def birthdayCakeCandles(candles):
    count=0
    m=max(candles)
    for i in candles:
        if i==m:
            count+=1
    return count
