import csv

#get the return and inflation data
with open('returnst.csv', 'r') as f:
	reader = csv.reader(f)
	RETURNS_T = list(reader)

TSM_R = RETURNS_T[0]
SCB_R = RETURNS_T[1]
WOR_R = RETURNS_T[2]
LTT_R = RETURNS_T[3]
GLD_R = RETURNS_T[4]
BIL_R = RETURNS_T[5]
INF_R = RETURNS_T[6]

YEARS = len(TSM_R)

#starting withdrawal rate
WR = 4

#set initial asset allocation
TSM_S = 20
SCB_S = 20
WOR_S = 0
LTT_S = 20
GLD_S = 20
BIL_S = 20

while(1):

	HGY = 0
	GOLD_YEAR = 0
	TTW = 0;
	WR += .1

	for START_YEAR in range( 0, YEARS ):
		TSM_P = TSM_S
		SCB_P = SCB_S
		WOR_P = WOR_S
		LTT_P = LTT_S
		GLD_P = GLD_S
		BIL_P = BIL_S

                #just a little check for how quickly gold runs out
		if( GOLD_YEAR > HGY ):
			HGY = GOLD_YEAR
		GOLD_YEAR = 0

		for YEAR in range(START_YEAR, YEARS):
		
			#print( "TSM is " + str(TSM_P) + ", return is " + str(TSM_R[YEAR]) + ", infl. is " + str(INF_R[YEAR]) )
	
			#spending pattern (enable or disable): spend GLD first
			if(0):
				if( GLD_P >= WR ):
					GLD_P -= WR
					GOLD_YEAR += 1
				elif(BIL_P >= WR ):
					BIL_P -= WR
				elif(LTT_P >= WR ):
					LTT_P -= WR
				elif(WOR_P >= WR ):
					WOR_P -= WR
				elif(SCB_P >= WR ):
					SCB_P -= WR
				elif(TSM_P >= WR ):
					TSM_P -= WR
				else:
					print("FAIL YEAR=" + str(YEAR))
					exit()


                        #spending pattern (enable or disable): spend BIL first
			if(0):
				if(BIL_P >= WR ):
					BIL_P -= WR
				elif( GLD_P >= WR ):
					GLD_P -= WR
					GOLD_YEAR += 1
				elif(LTT_P >= WR ):
					LTT_P -= WR
				elif(WOR_P >= WR ):
					WOR_P -= WR
				elif(SCB_P >= WR ):
					SCB_P -= WR
				elif(TSM_P >= WR ):
					TSM_P -= WR
				else:
					print("FAIL YEAR=" + str(YEAR))
					exit()
					
			#spending pattern (enable or disable): spend GLT+LTT+BIL first
			if(1):
				if( GLD_P >= WR/3 and LTT_P >= WR/3 and BIL_P >= WR/3):
					GLD_P -= WR/3
					LTT_P -= WR/3
					BIL_P -= WR/3
				elif( GLD_P >= WR ):
					GLD_P -= WR
				elif(LTT_P >= 4 ):
					LTT_P -= WR
				elif(BIL_P >= WR):
                                        BIL_P -= WR
				elif(WOR_P >= WR ):
					WOR_P -= WR
				elif(SCB_P >= WR ):
					SCB_P -= WR
				elif(TSM_P >= WR ):
					TSM_P -= WR
				else:
					print("FAIL YEAR=" + str(YEAR))
					exit()

			#spending pattern (enable or disable): spend GLT+LTT first
			if(0):
				if( GLD_P >= WR/2 and LTT_P >= WR/2 ):
					GLD_P -= WR/2
					LTT_P -= WR/2
				elif( GLD_P >= WR ):
					GLD_P -= WR
				elif(LTT_P >= 4 ):
					LTT_P -= WR
				elif(BIL_P >= WR):
                                        BIL_P -= WR
				elif(WOR_P >= WR ):
					WOR_P -= WR
				elif(SCB_P >= WR ):
					SCB_P -= WR
				elif(TSM_P >= WR ):
					TSM_P -= WR
				else:
					print("FAIL YEAR=" + str(YEAR))
					exit()

			#spending pattern (enable or disable): equal spend
			if(0):
				if( TSM_P + SCB_P + WOR_P + LTT_P + GLD_P >= WR ):
                                        T_WEALTH = TSM_P + SCB_P + WOR_P + LTT_P + GLD_P + BIL_P
                                        GLD_P -= GLD_P*WR/T_WEALTH
                                        LTT_P -= LTT_P*WR/T_WEALTH
                                        WOR_P -= WOR_P*WR/T_WEALTH
                                        SCB_P -= SCB_P*WR/T_WEALTH
                                        TSM_P -= TSM_P*WR/T_WEALTH
                                        BIL_P -= BIL_P*WR/T_WEALTH
				else:
					print("FAIL YEAR=" + str(YEAR))
					exit()

			TSM_P *= (100-float(INF_R[YEAR])+float(TSM_R[YEAR]))/100
			SCB_P *= (100-float(INF_R[YEAR])+float(SCB_R[YEAR]))/100
			WOR_P *= (100-float(INF_R[YEAR])+float(WOR_R[YEAR]))/100
			LTT_P *= (100-float(INF_R[YEAR])+float(LTT_R[YEAR]))/100
			GLD_P *= (100-float(INF_R[YEAR])+float(GLD_R[YEAR]))/100
			BIL_P *= (100-float(INF_R[YEAR])+float(BIL_R[YEAR]))/100

                        #annual rebalance (enable or disable)
			if(0):
				T_WEALTH = TSM_P + SCB_P + WOR_P + LTT_P + GLD_P + BIL_P
				TSM_P = T_WEALTH*TSM_S/100
				SCB_P = T_WEALTH*SCB_S/100
				WOR_P = T_WEALTH*WOR_S/100
				LTT_P = T_WEALTH*LTT_S/100
				GLD_P = T_WEALTH*GLD_S/100
				BIL_P = T_WEALTH*BIL_S/100

			#print( str(YEAR) + "\t" + str(round(TSM_P)) + "\t" + str(round(SCB_P)) + "\t" + str(round(WOR_P)) + "\t" + str(round(LTT_P)) + "\t" + str(round(GLD_P)) )
			#input()

		T_WEALTH = TSM_P + SCB_P + WOR_P + LTT_P + GLD_P + BIL_P
		TTW += T_WEALTH
		#print( "\t" + str(round(TSM_P)) + "\t" + str(round(SCB_P)) + "\t" + str(round(WOR_P)) + "\t" + str(round(LTT_P)) + "\t" + str(round(GLD_P)) + "\t" + str(round(BIL_P)))
		#input()
		
	print( str(round(WR,2)) + " ATW = " + str(round(TTW/(YEARS+1))) + ", HGY=" + str(HGY))
		
