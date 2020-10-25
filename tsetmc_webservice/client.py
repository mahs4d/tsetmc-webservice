from datetime import date
from decimal import Decimal
from enum import Enum
from typing import List

import zeep


class Flow(Enum):
    GENERAL = 0
    BOURSE = 1
    FARABOURSE = 2
    ATI = 3
    PAYE_BOURSE = 4
    PAYE_FARABOURSE = 5


class WebserviceClient:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

        self._soap_service = zeep.Client(wsdl='http://service.tsetmc.com/webservice/TsePublicV2.asmx?WSDL') \
            .bind('TsePublicV2', 'TsePublicV2Soap12')

    def client_type(self) -> List[dict]:
        """
        ClientType
        اطلاعات معاملات به تفکیک حقیقی و حقوقی
        """

        result = self._soap_service.ClientType(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1'][1]['_value_1']:
            resco = val['Data']
            ret.append(_element_to_dict(resco))

        return ret

    def option(self) -> List[dict]:
        """
        option
        اختیار معامله
        """

        result = self._soap_service.Option(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['Option']
            ret.append(_element_to_dict(resco))

        return ret

    def nsc_start(self) -> List[dict]:
        """
        NSCStart
        اطلاعات 20 روز آخری که بازار باز بوده است را ارائه می کند.
        """

        result = self._soap_service.NSCStart(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseNSCStart']
            ret.append(_element_to_dict(resco))

        return ret

    def inst_affect(self) -> List[dict]:
        """
        InstAffect
        اطلاعات تاثیر نمادها در شاخص را ارائه مي کند.
        """

        result = self._soap_service.InstAffect(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstAffectList']
            ret.append(_element_to_dict(resco))

        return ret

    def power_instrument(self) -> List[dict]:
        """
        PowerInstrument
        فهرست نمادهای فعال بازار برق را ارائه مي کند.
        """

        result = self._soap_service.PowerInstrument(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['Instrument']
            ret.append(_element_to_dict(resco))

        return ret

    def msg(self) -> List[dict]:
        """
        Msg
        پیغامهای ناظر بازار را ارائه مي کند.
        """

        result = self._soap_service.Msg(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseMsg']
            ret.append(_element_to_dict(resco))

        return ret

    def sub_sector(self) -> List[dict]:
        """
        SubSector
        اطلاعات زیر گروه هاي صنعت را ارائه مي کند.
        """

        result = self._soap_service.SubSector(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['SubSector']
            ret.append(_element_to_dict(resco))

        return ret

    def sector(self) -> List[dict]:
        """
        Sector
        اطلاعات گروه هاي صنعت را ارائه مي کند.
        """

        result = self._soap_service.Sector(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseSectorList']
            ret.append(_element_to_dict(resco))

        return ret

    def board(self) -> List[dict]:
        """
        Board
        ليست تابلوها را ارائه مي کند.
        """

        result = self._soap_service.Board(UserName=self._username, Password=self._password)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseBoardList']
            ret.append(_element_to_dict(resco))

        return ret

    def market_value(self) -> Decimal:
        """
        MarketValue
        آخرین ارزش بازار را ارائه مي کند.
        """

        result = self._soap_service.MarketValue(UserName=self._username, Password=self._password)
        return result

    def company(self, flow: Flow) -> List[dict]:
        """
        Company
        اطلاعات مربوط به شرکتها را ارائه مي کند.
        """

        result = self._soap_service.Company(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseCompanyName']
            ret.append(_element_to_dict(resco))

        return ret

    def instrument(self, flow: Flow) -> List[dict]:
        """
        Instrument
        اطلاعات مربوط به نمادها را ارائه مي کند.
        """

        result = self._soap_service.Instrument(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseInstruments']
            ret.append(_element_to_dict(resco))

        return ret

    def share_change(self, flow: Flow) -> List[dict]:
        """
        ShareChange
        فهرست افزایش سرمایه ها
        """

        result = self._soap_service.ShareChange(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseShare']
            ret.append(_element_to_dict(resco))

        return ret

    def adj_price(self, flow: Flow) -> List[dict]:
        """
        AdjPrice
        اطلاعات تعدیل قیمت نمادها را ارائه مي کند.
        """

        result = self._soap_service.AdjPrice(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseAdjPrice']
            ret.append(_element_to_dict(resco))

        return ret

    def market_activity_last(self, flow: Flow) -> List[dict]:
        """
        MarketActivityLast
        اطلاعات آمار معاملات را آخرین روز را ارائه مي کند.
        """

        result = self._soap_service.MarketActivityLast(UserName=self._username, Password=self._password,
                                                       Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['MarketOverview']
            ret.append(_element_to_dict(resco))

        return ret

    def instruments_state(self, flow: Flow) -> List[dict]:
        """
        InstrumentsState
        اطلاعات وضعیت نمادها را ارائه می کند. در صورتی که نمادی در این متود وجود نداشته باشد به معنی باز بودن نماد است.
        """

        result = self._soap_service.InstrumentsState(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstrumentsSTates']
            ret.append(_element_to_dict(resco))

        return ret

    def top(self, flow: Flow) -> List[dict]:
        """
        TOP
        اطلاعات قیمت تئوریک گشایش
        """

        result = self._soap_service.TOP(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseTop']
            ret.append(_element_to_dict(resco))

        return ret

    def static_thresholds(self, flow: Flow) -> List[dict]:
        """
        StaticThresholds
        کمینه و بیشینه قیمت مجاز نمادها
        """

        result = self._soap_service.StaticThresholds(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['StaticThresholds']
            ret.append(_element_to_dict(resco))

        return ret

    def best_limits_all_ins(self, flow: Flow) -> List[dict]:
        """
        BestLimitsAllIns
        تقاضاهاي برتر خريد و فروش همه نمادها را ارائه مي کند.
        """

        result = self._soap_service.BestLimitsAllIns(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstBestLimit']
            ret.append(_element_to_dict(resco))

        return ret

    def inst_with_best_limit(self, flow: Flow) -> List[dict]:
        """
        InstWithBestLimit
        اطلاعات آمار معاملات را در يک بازه زماني در تابلويي خاص ارائه مي کند.
        """

        result = self._soap_service.InstWithBestLimit(UserName=self._username, Password=self._password,
                                                      Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstNames']
            ret.append(_element_to_dict(resco))

        return ret

    def index_b1_last_day_last_data(self, flow: Flow) -> List[dict]:
        """
        IndexB1LastDayLastData
        اطلاعات آخرين روز شاخص ها را ارائه مي کند.
        """

        result = self._soap_service.IndexB1LastDayLastData(UserName=self._username, Password=self._password,
                                                           Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['IndexB1LastDayLastData']
            ret.append(_element_to_dict(resco))

        return ret

    def trade_last_day(self, flow: Flow) -> List[dict]:
        """
        TradeLastDay
        اطلاعات معاملات آخرين روز را ارائه مي کند.
        """

        result = self._soap_service.TradeLastDay(UserName=self._username, Password=self._password, Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TradeLastDay']
            ret.append(_element_to_dict(resco))

        return ret

    def market_value_by_date(self, date: date) -> Decimal:
        """
        MarketValueByDate
        ارزش بازار در یک تاریخ مشخص را ارائه مي کند.
        """

        result = self._soap_service.MarketValueByDate(UserName=self._username, Password=self._password,
                                                      DEven=_date_to_int(date))
        return result

    def future_information(self, date: date) -> List[dict]:
        """
        FutureInformation
        اطلاعات بازار آتی را ارائه مي کند.
        """

        result = self._soap_service.FutureInformation(UserName=self._username, Password=self._password,
                                                      DEven=_date_to_int(date))

        ret = []
        for val in result['_value_1'][1]['_value_1']:
            resco = val['TseAlert']
            ret.append(_element_to_dict(resco))

        return ret

    def sector_state(self, date: date) -> List[dict]:
        """
        SectorState
        اطلاعات وضعیت گروه هاي صنعت را ارائه مي کند.
        """

        result = self._soap_service.SectorState(UserName=self._username, Password=self._password,
                                                DEven=_date_to_int(date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['SectorState']
            ret.append(_element_to_dict(resco))

        return ret

    def index_b2(self, date: date) -> List[dict]:
        """
        IndexB2
        اطلاعات سابقه شاخص ها را ارائه مي کند.
        """

        result = self._soap_service.IndexB2(UserName=self._username, Password=self._password, DEven=_date_to_int(date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TseIndexB2']
            ret.append(_element_to_dict(resco))

        return ret

    def trade_one_day(self, flow: Flow, date: date) -> List[dict]:
        """
        TradeOneDay
        5اطلاعات معاملات روزانه را ارائه مي کند.
        """

        result = self._soap_service.TradeOneDay(UserName=self._username, Password=self._password, Flow=flow.value,
                                                SelDate=_date_to_int(date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TradeSelectedDate']
            ret.append(_element_to_dict(resco))

        return ret

    def trade_one_day_all(self, flow: Flow, date: date) -> List[dict]:
        """
        TradeOneDayAll
        اطلاعات معاملات روزانه را ارائه مي کند.
        """

        result = self._soap_service.TradeOneDayAll(UserName=self._username, Password=self._password, Flow=flow.value,
                                                   SelDate=_date_to_int(date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TradeSelectedDateAll']
            ret.append(_element_to_dict(resco))

        return ret

    def instrument_filter_by_date(self, flow: Flow, date: date) -> List[dict]:
        """
        InstrumentFilterByDate
        اطلاعات مربوط به نمادهای جدید و یا تغییر یافته از یک تاریخ به بعد را ارائه مي کند.
        """

        result = self._soap_service.InstrumentFilterByDate(UserName=self._username, Password=self._password,
                                                           DEven=_date_to_int(date),
                                                           Flow=flow.value)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['Instrument']
            ret.append(_element_to_dict(resco))

        return ret

    def market_activity_daily(self, from_date: date, to_date: date) -> List[dict]:
        """
        MarketActivityDaily
        اطلاعات آمار معاملات را در يک بازه زماني ارائه مي کند.
        """

        result = self._soap_service.MarketActivityDaily(UserName=self._username, Password=self._password,
                                                        DateFrom=_date_to_int(from_date), DateTo=_date_to_int(to_date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['LastDayTrade']
            ret.append(_element_to_dict(resco))

        return ret

    def best_limit_one_ins(self, instrument_code: int) -> List[dict]:
        """
        BestLimitOneIns
        5 تقاضاي برتر خريد و فروش يک نماد را ارائه مي کند.
        """

        result = self._soap_service.BestLimitOneIns(UserName=self._username, Password=self._password,
                                                    InsCode=instrument_code)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstBestLimit']
            ret.append(_element_to_dict(resco))

        return ret

    def inst_trade(self, instrument_code: int, from_date: date, to_date: date) -> List[dict]:
        """
        InstTrade
        اطلاعات آمار معاملات يک نماد را در يک بازه زماني را ارائه مي کند.
        """

        result = self._soap_service.InstTrade(UserName=self._username, Password=self._password, Inscode=instrument_code,
                                              DateFrom=_date_to_int(from_date), DateTo=_date_to_int(to_date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['TradeSelectedDate']
            ret.append(_element_to_dict(resco))

        return ret

    def instruments_state_change(self, instrument_code: int, date: date) -> List[dict]:
        """
        InstrumentsStateChange
        تغییر وضعیت نماد
        """

        result = self._soap_service.InstrumentsStateChange(UserName=self._username, Password=self._password,
                                                           Inscode=instrument_code, DEven=_date_to_int(date))

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstrumentsStateChange']
            ret.append(_element_to_dict(resco))

        return ret

    def index_b1_last_day_one_inst(self, index_code: int, flow: Flow) -> List[dict]:
        """
        IndexB1LastDayOneInst
        اطلاعات آخرين روز شاخص ها را ارائه مي کند.
        """

        result = self._soap_service.IndexB1LastDayOneInst(UserName=self._username, Password=self._password,
                                                          Flow=flow.value, IdxCode=index_code)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['IndexB1LastDay']
            ret.append(_element_to_dict(resco))

        return ret

    def index_instrument(self, index_code: int, flow: Flow) -> List[dict]:
        """
        IndexInstrument
        اطلاعات نمادهاي هر شاخص را ارائه مي کند.
        """

        result = self._soap_service.IndexInstrument(UserName=self._username, Password=self._password,
                                                    Flow=flow.value, IdxCode=index_code)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['IndexB1LastDay']
            ret.append(_element_to_dict(resco))

        return ret

    def auction(self, offset: int) -> List[dict]:
        """
        Auction
        حراج بازار فیزیکی
        """

        result = self._soap_service.Auction(UserName=self._username, Password=self._password, **{'from': offset})

        ret = []
        for val in result['_value_1'][1]['_value_1']:
            resco = val['Data']
            ret.append(_element_to_dict(resco))

        return ret

    def power_instrument_history(self, offset: int) -> List[dict]:
        """
        PowerInstrumentHistory
        تاریخچه  فهرست نمادهای فعال و غیر فعال بازار برق را ارائه مي کند.
        """

        result = self._soap_service.PowerInstrumentHistory(UserName=self._username, Password=self._password,
                                                           From=offset)

        ret = []
        for val in result['_value_1']['_value_1']:
            resco = val['InstrumentHistory']
            ret.append(_element_to_dict(resco))

        return ret


def _element_to_dict(element) -> dict:
    ret = {}
    for name, _ in type(element)._xsd_type.elements:
        ret[name] = element[name]

    return ret


def _date_to_int(d: date) -> int:
    return int(f'{d.year:04}{d.month:02}{d.day:02}')
