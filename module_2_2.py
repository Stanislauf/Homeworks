primo = input("Inserire il primo numero: ")
secondo = input("Inserire il secondo numero: ")
terzo = input('Inserire il terzo numero: ')
#if primo == secondo and primo == terzo and secondo == terzo:
if primo == secondo == terzo:
    print(3)
#elif primo == secondo or primo == terzo or secondo == terzo:
elif primo != secondo != terzo:
    print(0)
else:
    print(2)