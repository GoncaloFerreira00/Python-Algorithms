def func(i):
    nums  = []
    nums.append(0)
    nums.append(1)
    for x in range(i):
       endlist = nums[-1]
       endendlist = nums[-2] 
       nums.append(endendlist + endlist)
    print(nums[i])

print("Para terminar digite um numero negativo.")
try:
    while True:
        n = int(input("Digite um numero: "))
        if n<0:
            break
            print("Apenas numeros positivos.")
        
        func(n)
except:
  print("An exception occurred")
    