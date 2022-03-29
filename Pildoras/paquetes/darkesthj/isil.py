def isil(ep1,ep2,parcial,ep3,ep4,final):
        notaEP = ((ep1+ep2+ep3+ep4)/4)*0.4
        notaParcial = parcial*0.3
        notaFinal = final*0.3
        promedioFinal = notaEP+notaParcial+notaFinal
        print(f'Su nota final es: {promedioFinal}')
