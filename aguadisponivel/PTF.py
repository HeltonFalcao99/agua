class Oliveira:

    def oliveira(self, T_ARE, SILT, ARG, SOLO):
        if(T_ARE == None or SILT == None or ARG == None or SOLO == None):
            retorno = None
        else:
            retorno = ((-0.000021 * T_ARE) + (0.000203 * SILT) +
                       (0.000054 * ARG) + (0.021656 * SOLO))
            retorno = round(retorno, 3)
        return retorno


class BarrosSimplificada:

    def BS_logalpha(self, ARG):
        logalpha = (-1.07329) + (-1.59578 * (ARG/1000))
        logalpha = round(logalpha, 3)
        return logalpha

    def BS_alpha(self, log):
        alpha = 10**log
        alpha = round(alpha, 3)
        return alpha

    def BS_n(self, t_are, silt):
        N = (1.134153) + (0.722216*(t_are/1000)) + (0.39574*(silt/1000))
        N = round(N, 3)
        return N

    def BS_thetar(self, t_are, arg):
        thetar = (0.128617) + (-0.14836*(t_are/1000)) + (0.35705*(arg/1000))
        thetar = round(thetar, 3)
        return thetar

    def BS_thetas(self, t_are, silt):
        thetas = (0.434714) + (-0.114177*(t_are/1000)) + (0.117845*(silt/1000))
        thetas = round(thetas, 3)
        return thetas

    def BS_zu(self, alpha, n, thetar, thetas):
        bs_zu = thetar + ((thetas-thetar) / ((1+(alpha*10)**n)**(1-(1/n))))
        bs_zu = round(bs_zu, 3)
        return bs_zu

    def BS_tt(self, alpha, n, thetar, thetas):
        bs_tt = thetar + ((thetas-thetar) / ((1+(alpha*33)**n)**(1-(1/n))))
        bs_tt = round(bs_tt, 3)
        return bs_tt

    def BS_pc(self, alpha, n, thetar, thetas):
        bs_pc = thetar + ((thetas-thetar) / ((1+(alpha*1500)**n)**(1-(1/n))))
        bs_pc = round(bs_pc, 3)
        return bs_pc

    def bar_ad(self, tt, pc):
        AD = tt - pc
        AD = round(AD, 3)
        return AD


class Barros:
    # alfa de barros
    def bar_alpha(self, T_ARE, ARG, SOLO):
        A1 = 0.8118 + (0.8861 * (T_ARE / 1000)) + (-1.1907 *
                                                   (ARG / 1000)) + (-0.001514 * (SOLO / 0.001))
        ALPHA = 10**A1
        ALPHA = round(ALPHA, 3)
        return ALPHA
    # n de barros

    def bar_n(self, T_ARE, SILT, M_ORG):
        N = (1.1527 + (0.7427*(T_ARE/1000)) +
             (0.4135*(SILT/1000)) + (-5.5341*(M_ORG/1000)))
        N = round(N, 3)
        return N
    # theta r de barros

    def bar_thetar(self, T_ARE, ARG, M_ORG, SOLO):
        THETAR = 0.0858 + (-0.1671*(T_ARE/1000)) + (0.3516*(ARG/1000)) + \
            (1.1846*(M_ORG*0.001)) + (0.000029*(SOLO/0.001))
        THETAR = round(THETAR, 3)
        return THETAR
    # theta s de barros

    def bar_thetas(self, SOLO):
        THETAS = 1 + (-0.00037 * (SOLO/0.001))
        THETAS = round(THETAS, 3)
        return THETAS

    def bar_zu(self, alpha, n, thetar, thetas):
        B_ZU = thetar + ((thetas-thetar) / ((1+(alpha*10)**n)**(1-(1/n))))
        B_ZU = round(B_ZU, 3)
        return B_ZU

    def bar_tt(self, alpha, n, thetar, thetas):
        B_TT = thetar + ((thetas-thetar) / ((1+(alpha*33)**n)**(1-(1/n))))
        B_TT = round(B_TT, 3)
        return B_TT

    def bar_pc(self, alpha, n, thetar, thetas):
        B_PC = thetar + ((thetas-thetar) / ((1+(alpha*1500)**n)**(1-(1/n))))
        B_PC = round(B_PC, 3)
        return B_PC

    def bar_ad(self, tt, pc):
        AD = tt - pc
        AD = round(AD, 3)
        return AD


class Tomasella:

    def tom_thetas(self, agro, afin, silt, solo, c_org):
        ThetaS = (91.6203 - (30.0046 * solo) + (1.5925*c_org) + (0.0022*agro*silt) -
                  (0.0036 * agro * afin) - (0.0018*agro*agro) - (0.001*afin*afin))/100
        ThetaS = round(ThetaS, 3)
        return ThetaS

    def tom_thetar(self, agro, afin, silt, solo, arg):
        ThetaR = (23.3867 + (0.1103*arg) + (-4.7949*solo) + (0.0047*silt*arg) +
                  (-0.0027*(agro**2)) + (-0.0022 * (afin**2)) + (-0.0048*(silt**2)))/100
        ThetaR = round(ThetaR, 3)
        return ThetaR

    def tom_N(self, agro, afin, silt, arg):
        N = ((168.8617 + (-0.0258*agro*silt) + (-0.0261*afin*arg) +
              (0.0093*(afin**2)) + (-0.0077 * (silt**2)))/100)
        N = round(N, 3)
        return N

    def tom_alpha(self, agro, afin, silt, solo, arg):
        alpha = (2.71828**((183.2601 + (-2.556*silt) + (-0.1329 * arg) + (-247.4904*solo) +
                            (-0.0189*agro*afin) + (0.1177*agro*silt) + (0.0517*afin*arg) + (0.0617*(agro**2)))/100))
        alpha = round(alpha, 3)
        return alpha

    def tom_zu(self, alpha, n, thetar, thetas):
        T_ZU = thetar + ((thetas-thetar) / ((1+(alpha*10)**n)**(1-(1/n))))
        T_ZU = round(T_ZU, 3)
        return T_ZU

    def tom_tt(self, alpha, n, thetar, thetas):
        T_TT = thetar + ((thetas-thetar) / ((1+(alpha*33)**n)**(1-(1/n))))
        T_TT = round(T_TT, 3)
        return T_TT

    def tom_pc(self, alpha, n, thetar, thetas):
        T_PC = thetar + ((thetas-thetar) / ((1+(alpha*1500)**n)**(1-(1/n))))
        T_PC = round(T_PC, 3)
        return T_PC

    def tom_ad(self, tt, pc):
        ad = tt - pc
        ad = round(ad, 3)
        return ad
