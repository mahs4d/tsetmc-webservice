from datetime import date
from os import path
from typing import List

import pandas as pd

from .client import WebserviceClient, Flow


def generate_pack(client: WebserviceClient, from_date: date, to_date: date, out_dir: str):
    total = 30
    cur = 0

    cur += 1
    print(f'{cur}/{total}')
    try:
        company = _iterate_flows(client.company)
        _save_data_to_csv(company, 'company', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        instrument = _iterate_flows(client.instrument)
        _save_data_to_csv(instrument, 'instrument', out_dir)
    except Exception as ex:
        instrument = []
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        client_type = client.client_type()
        _save_data_to_csv(client_type, 'client_type', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        option = client.option()
        _save_data_to_csv(option, 'option', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        share_changes = _iterate_flows(client.share_change)
        _save_data_to_csv(share_changes, 'share_changes', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        market_activity_last = _iterate_flows(client.market_activity_last)
        _save_data_to_csv(market_activity_last, 'market_activity_last', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        power_instruments = client.power_instrument()
        _save_data_to_csv(power_instruments, 'power_instruments', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        adj_prices = _iterate_flows(client.adj_price)
        _save_data_to_csv(adj_prices, 'adj_prices', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        nsc_start = client.nsc_start()
        _save_data_to_csv(nsc_start, 'nsc_start', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        inst_affect = client.inst_affect()
        _save_data_to_csv(inst_affect, 'inst_affect', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        instruments_state = _iterate_flows(client.instruments_state)
        _save_data_to_csv(instruments_state, 'instruments_state', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        top = _iterate_flows(client.top)
        _save_data_to_csv(top, 'theoretical_open_price', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        msg = client.msg()
        _save_data_to_csv(msg, 'msg', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        sub_sector = client.sub_sector()
        _save_data_to_csv(sub_sector, 'sub_sector', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        static_thresholds = _iterate_flows(client.static_thresholds)
        _save_data_to_csv(static_thresholds, 'static_thresholds', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        best_limits_all_ins = _iterate_flows(client.best_limits_all_ins)
        _save_data_to_csv(best_limits_all_ins, 'best_limits_all_ins', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        inst_with_best_limit = _iterate_flows(client.inst_with_best_limit)
        _save_data_to_csv(inst_with_best_limit, 'inst_with_best_limit', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        index_b1_last_day_last_data = _iterate_flows(client.index_b1_last_day_last_data)
        _save_data_to_csv(index_b1_last_day_last_data, 'index_b1_last_day_last_data', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        sector = client.sector()
        _save_data_to_csv(sector, 'sector', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        board = client.board()
        _save_data_to_csv(board, 'board', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        trade_last_day = _iterate_flows(client.trade_last_day)
        _save_data_to_csv(trade_last_day, 'trade_last_day', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        future_information = _iterate_date(from_date, to_date, client.future_information)
        _save_data_to_csv(future_information, 'future_information', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        sector_state = _iterate_date(from_date, to_date, client.sector_state)
        _save_data_to_csv(sector_state, 'sector_state', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        index_b2 = _iterate_date(from_date, to_date, client.index_b2)
        _save_data_to_csv(index_b2, 'index_b2', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        index_b2 = _iterate_date(from_date, to_date, client.index_b2)
        _save_data_to_csv(index_b2, 'index_b2', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        trade_one_day = _iterate_date(from_date, to_date, _iterate_flows, fl_func=client.trade_one_day)
        _save_data_to_csv(trade_one_day, 'trade_one_day', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        trade_one_day_all = _iterate_date(from_date, to_date, _iterate_flows, fl_func=client.trade_one_day_all)
        _save_data_to_csv(trade_one_day_all, 'trade_one_day_all', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        instrument_filter_by_date = _iterate_date(from_date, to_date, _iterate_flows,
                                                  fl_func=client.instrument_filter_by_date)
        _save_data_to_csv(instrument_filter_by_date, 'instrument_filter_by_date', out_dir)
    except Exception as ex:
        print(ex)

    cur += 1
    print(f'{cur}/{total}')
    try:
        market_activity_daily = client.market_activity_daily(from_date, to_date)
        _save_data_to_csv(market_activity_daily, 'market_activity_daily', out_dir)
    except Exception as ex:
        print(ex)

    best_limit_one_ins = []
    for inst in instrument:
        code = inst['InsCode']
        try:
            arr = client.best_limit_one_ins(instrument_code=code)
            for a in arr:
                a['InsCode'] = code
            best_limit_one_ins.extend(arr)
        except Exception as ex:
            print(ex)
    _save_data_to_csv(best_limit_one_ins, 'best_limit_one_ins', out_dir)

    cur += 1
    print(f'{cur}/{total}')
    inst_trade = []
    for inst in instrument:
        code = inst['InsCode']
        try:
            arr = client.inst_trade(instrument_code=code, from_date=from_date, to_date=to_date)
            for a in arr:
                a['InsCode'] = code
            inst_trade.extend(arr)
        except Exception as ex:
            print(ex)
    _save_data_to_csv(inst_trade, 'inst_trade', out_dir)


def _iterate_date(from_date, to_date, func, **kwargs):
    arr = []
    for d in pd.date_range(from_date, to_date):
        try:
            temp_arr = func(date=d, **kwargs)
            for t in temp_arr:
                t['date'] = d

            arr.extend(temp_arr)
        except Exception as ex:
            print(ex)

    return arr


def _iterate_flows(fl_func, **kwargs):
    arr = []
    try:
        arr.extend(fl_func(**kwargs, flow=Flow.BOURSE))
    except Exception as ex:
        print(ex)

        arr = []
        try:
            arr.extend(fl_func(**kwargs, flow=Flow.FARABOURSE))
        except Exception as ex:
            print(ex)
    arr = []
    try:
        arr.extend(fl_func(**kwargs, flow=Flow.ATI))
    except Exception as ex:
        print(ex)

    return arr


def _save_data_to_csv(data: List[dict], file_name: str, out_dir: str):
    df = pd.DataFrame(data)
    df.to_csv(path.join(out_dir, f'{file_name}.csv'))
