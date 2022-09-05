from concurrent.futures import ThreadPoolExecutor
from db_ops.configs import TXT_ROOT
import subprocess


def task(py_file):
    # print("task")
    a = subprocess.Popen(py_file.split())  # 没有指定PIPE
    print(a.communicate())  # 打印输出结果和输入参数
    print(py_file)


tgt_path = str(TXT_ROOT)
# tgt_path = "/mnt/z/qtData/windtxt/equity"

commands = [
    "python  start.py   -t AShareFinancialderivative	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareTTMHis	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareMarginTrade 	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AIndexValuation  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AIndexFinancialderivative	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AshareConseption	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareSalesSegment	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareCompRestricted  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareANNFinancialIndicator  	-st	20070101	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t ChinaHedgeFundNAV  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t ChinaHedgeFundDescription  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t ChinaMutualFundNAV  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t ChinaMutualFundDescription  	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py   -t AShareDescription	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareConsensusRollingData	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareEODDerivativeIndicator	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareEXRightDividendRecord	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareFinancialIndicator	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareHolderNumber	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIncome	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIndustriesClass_CITICS	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIndustriesClass_CS	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIndustriesClass_GICS	-st	20190112	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIndustriesClass_SW	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIndustriesClass_WIND	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareIssuingDatePredict	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareL2Indicators	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareMarginTrade	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareMoneyFlow	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareProfitExpress	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareProfitNotice	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareST	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareStockRatingConsus	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareTechIndicators	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareTradingSuspension	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareYield	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ASWSIndexEOD	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CBondEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CBondFuturesEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CBondFuturesPositions	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CCommodityFuturesEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CCommodityFuturesPositions	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesCalendar	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesContPro	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesContProChange	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesDescription	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesInstock	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesMarginRatio	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CFuturesWarehouseStocks	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ChinaOptionCalendar	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ChinaOptionContpro	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ChinaOptionDescription	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ChinaOptionEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t ChinaOptionIndexEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CIndexFuturesEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t CIndexFuturesPositions	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t COptionContProChange	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t COptionDescriptionChange	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t SHSCMembers	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t SZSCMembers	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexAlternativeMembers	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexEODPrices	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexFreeWeight	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexIndustriesEODCITICS	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexMembers	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AIndexMembersCITICS	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareBalanceSheet	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareBlockTrade	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareCalendar	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareCashFlow	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py	-t AShareConsensusData	-st	20191012	-md	append	--fu 3 --otp	%s" % tgt_path,
    "python  start.py  -t ChinaMutualFundAssetPortfolio -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ChinaMutualFundStockPortfolio -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t QDIISecuritiesPortfolio -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CMFIndexEOD -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareInsideHolder -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareinstHolderDerData -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareManagementHoldReward -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIndustriesCode -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareTTMandMRQ -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareDividend -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AIndexCSI500weight -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AIndexHS300closeweight -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t SHSCChannelholdings -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CBIndexEODPrices -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CFuturesContractMapping -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareISActivity -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareISParticipant -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareISQA -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AIndexWindIndustriesEOD -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIncDescription -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIllegality -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareManagement -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareInvestmentIncome -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareEquityPledgeInfo -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareOwnership -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ASharePledgeProportion -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareEquityRelationships -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CFundWindIndexMembers -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ChinaMutualFundDescription -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ChinaMutualFundIssue -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CGBBenchmark -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ChinaClosedFundEODPrice -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ChinaMutualFundSeatTrading -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareConseption -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIndustriesClass_SWN -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareDevaluationPreparation -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareBankIndicator -st 20191012 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareMJRHolderTrade -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t ASharePlanTrade -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIPO -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareEarningEst -st 20070101 -md append --fu 3 --otp %s" % tgt_path,

    "python  start.py  -t AShareANNInf -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareANNColumn -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareTrustInvestmentTOT -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareRelatedClaimsDebets -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t Top5ByOperatingIncome -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareSalesSegment -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIBrokerIndicator -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareInsuranceIndicator -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareAuditOpinion -st 20070101 -md append --fu 3 --otp %s" % tgt_path,

    "python  start.py  -t AShareStrangeTradeDetial -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareMajorEvent -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareRegInv -st 20070101 -md append --fu 3 --otp %s" % tgt_path,

    "python  start.py  -t AShareProsecution -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t MergerEvent -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareRDexpenditure -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t CBondNegativeCreditEvent -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareFreeFloatCalendar -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareIntroduction -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareRegional -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AIndexMembersWind -st 20220620 -md append --fu 3 --otp %s" % tgt_path,

    "python  start.py  -t AShareIncome_op -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareBalanceSheet_op -st 20070101 -md append --fu 3 --otp %s" % tgt_path,
    "python  start.py  -t AShareCashFlow_op -st 20220620 -md append --fu 3 --otp %s" % tgt_path,
]

if __name__ == "__main__":
    print('Pool Start')
    with ThreadPoolExecutor(4) as pool:
        results = pool.map(task, commands)
    print('Pool Done')
