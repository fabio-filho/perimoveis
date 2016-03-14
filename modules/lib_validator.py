# -*- coding: utf-8 -*-


class IS_MONEY(object):
    def __init__(self, format=True, error_message='Digite o valor!'):
        self.format = format
        self.error_message = error_message
    def __call__(self, value):


            d=str(value)

            d = d.replace('.','')

            d = d.replace(',','.')

            #return (value, valor[-3:-2])
            try:
                return (d, None)
            except:
                return (d,str(d)+'o valor digitado não é um número válido')

    def formatter(self, value):
            value  = str(value)
            c = []
            for d in value:
               if d.isdigit():
                   c.append(d)
            value = str(''.join(c))
            l = len(value) #10 = 1000000000 = 10.000.000,00
            i = l - 2 #8
            p = i / 3 #2
            r = (l % 3) #2
            #p = 3
            pf = i-1
            if l == 1:
                formatado = '0,0'+value

            elif l == 2:
                formatado = '0,'+value
            elif l > 2:
                d = ','+value[-2:]
                s = ''
                n = r+1
                s += value[0:r+1]
                if i > 3:
                    while n < i:
                        pt = n + 3
                        s += '.'+ value[n:pt]
                        n = pt

                formatado = s+d
            else:
                formatado = value
            return formatado



class IS_CPF_OR_CNPJ(object):

    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message
    def __call__(self, value):
        try:
            #return (value, 'cpf incorreto'+str(value))
            #return (value, 'cpf incorreto'+str(cl))
            c = []
            for d in value:
               if d.isdigit():
                   c.append(d)
            cl = str(''.join(c))
            #return (value, 'cpf incorreto'+str(cl))
            if  len(cl) == 11:
                cpf = cl
                cnpj = None
            elif  len(cl) == 14:
                cpf = None
                cnpj = cl
            else:
                return (value, 'Número de dígitos incorreto para CPF ou CNPJ')

            #return(cpf,'aquiok'+str(len(cpf)==11))
            if cpf:

                def valida(value):

                    def calcdv(numb):

                        result = int()
                        seq = reversed(((range(9, id_type[1], -1)*2)[:len(numb)]))
                        #return (value,'to fundo1')
                        for digit, base in zip(numb, seq):
                            result += int(digit)*int(base)

                        dv = result % 11
                        #return (value,'to fundo1'+str(dv))
                        return (dv-10) and dv or 0

                    id_type = ['CPF', -1]


                    numb, xdv = value[:-2], value[-2:]

                    dv1 = calcdv(numb)
                    #return (value,'entrei'+str(dv1))
                    dv2 = calcdv(numb + str(dv1))
                    return (('%d%d' % (dv1, dv2) == xdv and True or False), id_type[0])


                try:
                    cpf=str(value)
                    #return(cpf,'aquiok'+str(len(cpf)==11))
                    if len(cpf)>=11:

                        #return (value, 'cpf acima de 11')
                        c = []
                        for d in cpf:
                           if d.isdigit():
                               c.append(d)
                        cl = str(''.join(c))
                        #return (value, 'cpf incorreto'+str(cl))
                        if  len(cl) == 11:
                            if valida(cl)[0] == True:
                                return(value,None)
                            else:
                                return (value, 'cpf inválido')
                        elif  len(cl) < 11:
                            return (value, 'cpf incompleto')
                        else:
                            return (value, 'cpf tem mais de 11 dígitos')
                        if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-' :
                            return (value, 'cpf deve estar no formato 000.000.000-00'+cpf[11])
                    else:
                        return (value, 'cpf deve estar no formato 000.000.000-00')
                    #return(cpf,'aquiok'+str(len(cpf)==11))
                except:
                    return (value, 'algum erro'+str(value))
            elif cnpj:

                   """ Pega apenas os 12 primeiros dígitos do CNPJ e gera os 2 dígitos que faltam """
                   inteiros = map(int, cnpj)
                   novoCnpj = inteiros[:12]

                   prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
                   while len(novoCnpj) < 14:
                      r = sum([x*y for (x, y) in zip(novoCnpj, prod)]) % 11
                      if r > 1:
                         f = 11 - r
                      else:
                         f = 0
                      novoCnpj.append(f)
                      prod.insert(0, 6)
                   #return(str(novoCnpj),'aquiok')
                   """ Se o número gerado coincidir com o número original, é válido """
                   if novoCnpj == inteiros:
                      #cnpj = ''.join(novoCnpj)

                      return(str(cnpj),None)

                   else:
                      return (value, 'CNPJ não é válido')



        except:
            return (value, 'algum erro'+str(value))
    def formatter(self, value):
            if len(value)==11:
                formatado = value[0:3]+'.'+value[3:6]+'.'+value[6:9]+'-'+value[9:11]
            elif len(value)==14:
                formatado = value[0:2]+'.'+value[2:5]+'.'+value[5:8]+'/'+value[8:12]+'-'+value[12:14]
            else:
                formatado = value
            return formatado





class IS_TELEFONE(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message
    def __call__(self, value):
        try:
            telefone=str(value)
            #return(cpf,'aquiok'+str(len(cpf)==11))
            if len(telefone)>=10:
                #return (value, 'cpf acima de 11')
                c = []
                for d in telefone:
                   if d.isdigit():
                       c.append(d)
                cl = str(''.join(c))
                #return (value, 'cpf incorreto'+str(cl))
                if  len(cl) == 10:
                    return(str(cl),None)
                elif  len(cl) < 10:
                    return (value, 'telefone incompleto')
                else:
                    return (value, 'o telefone tem mais de 10 dígitos')
                if cpf[2] != '-' or cpf[7] != '-':
                    return (value, 'o telefone deve estar no formato 00-0000-0000')
            else:
                return (value, 'O telefone deve estar no formato 00-0000-0000')
            #return(cpf,'aquiok'+str(len(cpf)==11))
        except:
            return (value, 'algum erro'+str(value))
    def formatter(self, value):
            if len(value) == 10:
                formatado = value[0:2]+'-'+value[2:6]+'-'+value[6:10]
            else:
                formatado = value
            return formatado



class IS_CPF(object):
    def __init__(self, format=True, error_message='Digite apenas os números!'):
        self.format = format
        self.error_message = error_message
    def __call__(self, value):

        def valida(value):

            def calcdv(numb):

                result = int()
                seq = reversed(((range(9, id_type[1], -1)*2)[:len(numb)]))
                #return (value,'to fundo1')
                for digit, base in zip(numb, seq):
                    result += int(digit)*int(base)

                dv = result % 11
                #return (value,'to fundo1'+str(dv))
                return (dv-10) and dv or 0

            id_type = ['CPF', -1]


            numb, xdv = value[:-2], value[-2:]

            dv1 = calcdv(numb)
            #return (value,'entrei'+str(dv1))
            dv2 = calcdv(numb + str(dv1))
            return (('%d%d' % (dv1, dv2) == xdv and True or False), id_type[0])


        try:
            cpf=str(value)
            #return(cpf,'aquiok'+str(len(cpf)==11))
            if len(cpf)>=11:

                #return (value, 'cpf acima de 11')
                c = []
                for d in cpf:
                   if d.isdigit():
                       c.append(d)
                cl = str(''.join(c))
                #return (value, 'cpf incorreto'+str(cl))
                if  len(cl) == 11:
                    if valida(cl)[0] == True:
                        return(value,None)
                    else:
                        return (value, 'cpf inválido')
                elif  len(cl) < 11:
                    return (value, 'cpf incompleto')
                else:
                    return (value, 'cpf tem mais de 11 dígitos')
                if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-' :
                    return (value, 'cpf deve estar no formato 000.000.000-00'+cpf[11])
            else:
                return (value, 'cpf deve estar no formato 000.000.000-00')
            #return(cpf,'aquiok'+str(len(cpf)==11))


        except:
            return (value, 'algum erro'+str(value))
    def formatter(self, value):

            formatado = value[0:3]+'.'+value[3:6]+'.'+value[6:9]+'-'+value[9:11]
            #formatado = value
            return formatado
