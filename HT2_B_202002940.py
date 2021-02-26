numero_usuario = int(input("Por favor, ingrese un número: "))  
  
if numero_usuario > 1:  
   for i in range(2,numero_usuario):  
       if (numero_usuario % i) == 0:  
           print(numero_usuario,"No es un número primo")  
           break  
   else:  
       print(numero_usuario,"Es un número primo")  
         
else:  
   print(numero_usuario,"No es un número primo")  