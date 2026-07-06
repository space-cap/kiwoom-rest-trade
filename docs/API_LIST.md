# 키움증권 REST API 매핑 및 지원 목록 (API_LIST.md)

본 문서는 `kiwoom-rest-trade` SDK가 지원하는 전체 **337개 API**와 파이썬 메서드 간의 1대1 매핑 인덱스 가이드입니다.

| 대분류 | 중분류 | 키움 API ID | 파이썬 호출 메서드 | API 기능명 | HTTP 요청 |
|---|---|---|---|---|---|
| OAuth 인증 | 접근토큰발급 | `au10001` | `client.auth.au10001` | 접근토큰 발급 | `POST /oauth2/token` |
| OAuth 인증 | 접근토큰폐기 | `au10002` | `client.auth.au10002` | 접근토큰폐기 | `POST /oauth2/revoke` |
| 국내주식 | 계좌 | `ka00001` | `client.domestic.ka00001` | 계좌번호조회 | `POST /api/dostk/acnt` |
| 국내주식 | 종목정보 | `ka00198` | `client.domestic.ka00198` | 실시간종목조회순위 | `POST /api/dostk/stkinfo` |
| 국내주식 | 관심종목 | `ka01300` | `client.domestic.ka01300` | 관심종목 그룹 리스트 조회 | `POST /api/dostk/watchlist` |
| 국내주식 | 관심종목 | `ka01301` | `client.domestic.ka01301` | 관심종목 그룹 상세 조회 | `POST /api/dostk/watchlist` |
| 국내주식 | 계좌 | `ka01690` | `client.domestic.ka01690` | 일별잔고수익률 | `POST /api/dostk/acnt` |
| 국내주식 | 종목정보 | `ka10001` | `client.domestic.ka10001` | 주식기본정보요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10002` | `client.domestic.ka10002` | 주식거래원요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10003` | `client.domestic.ka10003` | 체결정보요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 시세 | `ka10004` | `client.domestic.ka10004` | 주식호가요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10005` | `client.domestic.ka10005` | 주식일주월시분요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10006` | `client.domestic.ka10006` | 주식시분요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10007` | `client.domestic.ka10007` | 시세표성정보요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 기관/외국인 | `ka10008` | `client.domestic.ka10008` | 주식외국인종목별매매동향 | `POST /api/dostk/frgnistt` |
| 국내주식 | 업종 | `ka10010` | `client.domestic.ka10010` | 업종프로그램요청 | `POST /api/dostk/sect` |
| 국내주식 | 시세 | `ka10011` | `client.domestic.ka10011` | 신주인수권전체시세요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 종목정보 | `ka10013` | `client.domestic.ka10013` | 신용매매동향요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 공매도 | `ka10014` | `client.domestic.ka10014` | 공매도추이요청 | `POST /api/dostk/shsa` |
| 국내주식 | 종목정보 | `ka10015` | `client.domestic.ka10015` | 일별거래상세요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10016` | `client.domestic.ka10016` | 신고저가요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10017` | `client.domestic.ka10017` | 상하한가요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10018` | `client.domestic.ka10018` | 고저가근접요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10019` | `client.domestic.ka10019` | 가격급등락요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10020` | `client.domestic.ka10020` | 호가잔량상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10021` | `client.domestic.ka10021` | 호가잔량급증요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10022` | `client.domestic.ka10022` | 잔량율급증요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10023` | `client.domestic.ka10023` | 거래량급증요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 종목정보 | `ka10024` | `client.domestic.ka10024` | 거래량갱신요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10025` | `client.domestic.ka10025` | 매물대집중요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10026` | `client.domestic.ka10026` | 고저PER요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10027` | `client.domestic.ka10027` | 전일대비등락률상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 종목정보 | `ka10028` | `client.domestic.ka10028` | 시가대비등락률요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10029` | `client.domestic.ka10029` | 예상체결등락률상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10030` | `client.domestic.ka10030` | 당일거래량상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10031` | `client.domestic.ka10031` | 전일거래량상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10032` | `client.domestic.ka10032` | 거래대금상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10033` | `client.domestic.ka10033` | 신용비율상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10034` | `client.domestic.ka10034` | 외인기간별매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10035` | `client.domestic.ka10035` | 외인연속순매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10036` | `client.domestic.ka10036` | 외인한도소진율증가상위 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10037` | `client.domestic.ka10037` | 외국계창구매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10038` | `client.domestic.ka10038` | 종목별증권사순위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10039` | `client.domestic.ka10039` | 증권사별매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10040` | `client.domestic.ka10040` | 당일주요거래원요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 순위정보 | `ka10042` | `client.domestic.ka10042` | 순매수거래원순위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 종목정보 | `ka10043` | `client.domestic.ka10043` | 거래원매물대분석요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 시세 | `ka10044` | `client.domestic.ka10044` | 일별기관매매종목요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10045` | `client.domestic.ka10045` | 종목별기관매매추이요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10046` | `client.domestic.ka10046` | 체결강도추이시간별요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10047` | `client.domestic.ka10047` | 체결강도추이일별요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | ELW | `ka10048` | `client.domestic.ka10048` | ELW일별민감도지표요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka10050` | `client.domestic.ka10050` | ELW민감도지표요청 | `POST /api/dostk/elw` |
| 국내주식 | 업종 | `ka10051` | `client.domestic.ka10051` | 업종별투자자순매수요청 | `POST /api/dostk/sect` |
| 국내주식 | 종목정보 | `ka10052` | `client.domestic.ka10052` | 거래원순간거래량요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10053` | `client.domestic.ka10053` | 당일상위이탈원요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 종목정보 | `ka10054` | `client.domestic.ka10054` | 변동성완화장치발동종목요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10055` | `client.domestic.ka10055` | 당일전일체결량요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10058` | `client.domestic.ka10058` | 투자자별일별매매종목요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10059` | `client.domestic.ka10059` | 종목별투자자기관별요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 차트 | `ka10060` | `client.domestic.ka10060` | 종목별투자자기관별차트요청 | `POST /api/dostk/chart` |
| 국내주식 | 종목정보 | `ka10061` | `client.domestic.ka10061` | 종목별투자자기관별합계요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10062` | `client.domestic.ka10062` | 동일순매매순위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 시세 | `ka10063` | `client.domestic.ka10063` | 장중투자자별매매요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 차트 | `ka10064` | `client.domestic.ka10064` | 장중투자자별매매차트요청 | `POST /api/dostk/chart` |
| 국내주식 | 순위정보 | `ka10065` | `client.domestic.ka10065` | 장중투자자별매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 시세 | `ka10066` | `client.domestic.ka10066` | 장마감후투자자별매매요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 대차거래 | `ka10068` | `client.domestic.ka10068` | 대차거래추이요청 | `POST /api/dostk/slb` |
| 국내주식 | 대차거래 | `ka10069` | `client.domestic.ka10069` | 대차거래상위10종목요청 | `POST /api/dostk/slb` |
| 국내주식 | 계좌 | `ka10072` | `client.domestic.ka10072` | 일자별종목별실현손익요청_일자 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `ka10073` | `client.domestic.ka10073` | 일자별종목별실현손익요청_기간 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `ka10074` | `client.domestic.ka10074` | 일자별실현손익요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `ka10075` | `client.domestic.ka10075` | 미체결요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `ka10076` | `client.domestic.ka10076` | 체결요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `ka10077` | `client.domestic.ka10077` | 당일실현손익상세요청 | `POST /api/dostk/acnt` |
| 국내주식 | 시세 | `ka10078` | `client.domestic.ka10078` | 증권사별종목매매동향요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 차트 | `ka10079` | `client.domestic.ka10079` | 주식틱차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka10080` | `client.domestic.ka10080` | 주식분봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka10081` | `client.domestic.ka10081` | 주식일봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka10082` | `client.domestic.ka10082` | 주식주봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka10083` | `client.domestic.ka10083` | 주식월봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 종목정보 | `ka10084` | `client.domestic.ka10084` | 당일전일체결요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 계좌 | `ka10085` | `client.domestic.ka10085` | 계좌수익률요청 | `POST /api/dostk/acnt` |
| 국내주식 | 시세 | `ka10086` | `client.domestic.ka10086` | 일별주가요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka10087` | `client.domestic.ka10087` | 시간외단일가요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 계좌 | `ka10088` | `client.domestic.ka10088` | 미체결 분할주문 상세 | `POST /api/dostk/acnt` |
| 국내주식 | 차트 | `ka10094` | `client.domestic.ka10094` | 주식년봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 종목정보 | `ka10095` | `client.domestic.ka10095` | 지정종목 정보요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 순위정보 | `ka10098` | `client.domestic.ka10098` | 시간외단일가등락율순위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 종목정보 | `ka10099` | `client.domestic.ka10099` | 종목정보 리스트 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10100` | `client.domestic.ka10100` | 종목정보 조회 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10101` | `client.domestic.ka10101` | 업종코드 리스트 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka10102` | `client.domestic.ka10102` | 회원사 리스트 | `POST /api/dostk/stkinfo` |
| 국내주식 | 기관/외국인 | `ka10131` | `client.domestic.ka10131` | 기관외국인연속매매현황요청 | `POST /api/dostk/frgnistt` |
| 국내주식 | 계좌 | `ka10170` | `client.domestic.ka10170` | 당일매매일지요청 | `POST /api/dostk/acnt` |
| 국내주식 | 조건검색 | `ka10171` | `client.domestic.ka10171` | 조건검색 목록조회 | `POST /api/dostk/websocket` |
| 국내주식 | 조건검색 | `ka10172` | `client.domestic.ka10172` | 조건검색 요청 일반 | `POST /api/dostk/websocket` |
| 국내주식 | 조건검색 | `ka10173` | `client.domestic.ka10173` | 조건검색 요청 실시간 | `POST /api/dostk/websocket` |
| 국내주식 | 조건검색 | `ka10174` | `client.domestic.ka10174` | 조건검색 실시간 해제 | `POST /api/dostk/websocket` |
| 국내주식 | 업종 | `ka20001` | `client.domestic.ka20001` | 업종현재가요청 | `POST /api/dostk/sect` |
| 국내주식 | 업종 | `ka20002` | `client.domestic.ka20002` | 업종별주가요청 | `POST /api/dostk/sect` |
| 국내주식 | 업종 | `ka20003` | `client.domestic.ka20003` | 전업종지수요청 | `POST /api/dostk/sect` |
| 국내주식 | 차트 | `ka20004` | `client.domestic.ka20004` | 업종틱차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka20005` | `client.domestic.ka20005` | 업종분봉조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka20006` | `client.domestic.ka20006` | 업종일봉조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka20007` | `client.domestic.ka20007` | 업종주봉조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka20008` | `client.domestic.ka20008` | 업종월봉조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 업종 | `ka20009` | `client.domestic.ka20009` | 업종현재가일별요청 | `POST /api/dostk/sect` |
| 국내주식 | 차트 | `ka20019` | `client.domestic.ka20019` | 업종년봉조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 대차거래 | `ka20068` | `client.domestic.ka20068` | 대차거래추이요청(종목별) | `POST /api/dostk/slb` |
| 국내주식 | ELW | `ka30001` | `client.domestic.ka30001` | ELW가격급등락요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30002` | `client.domestic.ka30002` | 거래원별ELW순매매상위요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30003` | `client.domestic.ka30003` | ELWLP보유일별추이요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30004` | `client.domestic.ka30004` | ELW괴리율요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30005` | `client.domestic.ka30005` | ELW조건검색요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30009` | `client.domestic.ka30009` | ELW등락율순위요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30010` | `client.domestic.ka30010` | ELW잔량순위요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30011` | `client.domestic.ka30011` | ELW근접율요청 | `POST /api/dostk/elw` |
| 국내주식 | ELW | `ka30012` | `client.domestic.ka30012` | ELW종목상세정보요청 | `POST /api/dostk/elw` |
| 국내주식 | ETF | `ka40001` | `client.domestic.ka40001` | ETF수익율요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40002` | `client.domestic.ka40002` | ETF종목정보요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40003` | `client.domestic.ka40003` | ETF일별추이요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40004` | `client.domestic.ka40004` | ETF전체시세요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40006` | `client.domestic.ka40006` | ETF시간대별추이요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40007` | `client.domestic.ka40007` | ETF시간대별체결요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40008` | `client.domestic.ka40008` | ETF일자별체결요청 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40009` | `client.domestic.ka40009` | ETF시간대별NAV현황 | `POST /api/dostk/etf` |
| 국내주식 | ETF | `ka40010` | `client.domestic.ka40010` | ETF시간대별수급현황 | `POST /api/dostk/etf` |
| 국내주식 | 시세 | `ka50010` | `client.domestic.ka50010` | 금현물체결추이 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka50012` | `client.domestic.ka50012` | 금현물일별추이 | `POST /api/dostk/mrkcond` |
| 국내주식 | 차트 | `ka50079` | `client.domestic.ka50079` | 금현물틱차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka50080` | `client.domestic.ka50080` | 금현물분봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka50081` | `client.domestic.ka50081` | 금현물일봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka50082` | `client.domestic.ka50082` | 금현물주봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka50083` | `client.domestic.ka50083` | 금현물월봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 시세 | `ka50087` | `client.domestic.ka50087` | 금현물예상체결 | `POST /api/dostk/mrkcond` |
| 국내주식 | 차트 | `ka50091` | `client.domestic.ka50091` | 금현물당일틱차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 차트 | `ka50092` | `client.domestic.ka50092` | 금현물당일분봉차트조회요청 | `POST /api/dostk/chart` |
| 국내주식 | 시세 | `ka50100` | `client.domestic.ka50100` | 금현물 시세정보 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka50101` | `client.domestic.ka50101` | 금현물 호가 | `POST /api/dostk/mrkcond` |
| 국내주식 | 기관/외국인 | `ka52301` | `client.domestic.ka52301` | 금현물투자자현황 | `POST /api/dostk/frgnistt` |
| 국내주식 | 테마 | `ka90001` | `client.domestic.ka90001` | 테마그룹별요청 | `POST /api/dostk/thme` |
| 국내주식 | 테마 | `ka90002` | `client.domestic.ka90002` | 테마구성종목요청 | `POST /api/dostk/thme` |
| 국내주식 | 종목정보 | `ka90003` | `client.domestic.ka90003` | 프로그램순매수상위50요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `ka90004` | `client.domestic.ka90004` | 종목별프로그램매매현황요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 시세 | `ka90005` | `client.domestic.ka90005` | 프로그램매매추이요청 시간대별 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka90006` | `client.domestic.ka90006` | 프로그램매매차익잔고추이요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka90007` | `client.domestic.ka90007` | 프로그램매매누적추이요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 시세 | `ka90008` | `client.domestic.ka90008` | 종목시간별프로그램매매추이요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 순위정보 | `ka90009` | `client.domestic.ka90009` | 외국인기관매매상위요청 | `POST /api/dostk/rkinfo` |
| 국내주식 | 시세 | `ka90010` | `client.domestic.ka90010` | 프로그램매매추이요청 일자별 | `POST /api/dostk/mrkcond` |
| 국내주식 | 대차거래 | `ka90012` | `client.domestic.ka90012` | 대차거래내역요청 | `POST /api/dostk/slb` |
| 국내주식 | 시세 | `ka90013` | `client.domestic.ka90013` | 종목일별프로그램매매추이요청 | `POST /api/dostk/mrkcond` |
| 국내주식 | 계좌 | `kt00001` | `client.domestic.kt00001` | 예수금상세현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00002` | `client.domestic.kt00002` | 일별추정예탁자산현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00003` | `client.domestic.kt00003` | 추정자산조회요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00004` | `client.domestic.kt00004` | 계좌평가현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00005` | `client.domestic.kt00005` | 체결잔고요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00007` | `client.domestic.kt00007` | 계좌별주문체결내역상세요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00008` | `client.domestic.kt00008` | 계좌별익일결제예정내역요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00009` | `client.domestic.kt00009` | 계좌별주문체결현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00010` | `client.domestic.kt00010` | 주문인출가능금액요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00011` | `client.domestic.kt00011` | 증거금율별주문가능수량조회요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00012` | `client.domestic.kt00012` | 신용보증금율별주문가능수량조회요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00013` | `client.domestic.kt00013` | 증거금세부내역조회요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00015` | `client.domestic.kt00015` | 위탁종합거래내역요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00016` | `client.domestic.kt00016` | 일별계좌수익률상세현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00017` | `client.domestic.kt00017` | 계좌별당일현황요청 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt00018` | `client.domestic.kt00018` | 계좌평가잔고내역요청 | `POST /api/dostk/acnt` |
| 국내주식 | 주문 | `kt10000` | `client.domestic.kt10000` | 주식 매수주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt10001` | `client.domestic.kt10001` | 주식 매도주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt10002` | `client.domestic.kt10002` | 주식 정정주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt10003` | `client.domestic.kt10003` | 주식 취소주문 | `POST /api/dostk/ordr` |
| 국내주식 | 신용주문 | `kt10006` | `client.domestic.kt10006` | 신용 매수주문 | `POST /api/dostk/crdordr` |
| 국내주식 | 신용주문 | `kt10007` | `client.domestic.kt10007` | 신용 매도주문 | `POST /api/dostk/crdordr` |
| 국내주식 | 신용주문 | `kt10008` | `client.domestic.kt10008` | 신용 정정주문 | `POST /api/dostk/crdordr` |
| 국내주식 | 신용주문 | `kt10009` | `client.domestic.kt10009` | 신용 취소주문 | `POST /api/dostk/crdordr` |
| 국내주식 | 종목정보 | `kt20016` | `client.domestic.kt20016` | 신용융자 가능종목요청 | `POST /api/dostk/stkinfo` |
| 국내주식 | 종목정보 | `kt20017` | `client.domestic.kt20017` | 신용융자 가능문의 | `POST /api/dostk/stkinfo` |
| 국내주식 | 주문 | `kt50000` | `client.domestic.kt50000` | 금현물 매수주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt50001` | `client.domestic.kt50001` | 금현물 매도주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt50002` | `client.domestic.kt50002` | 금현물 정정주문 | `POST /api/dostk/ordr` |
| 국내주식 | 주문 | `kt50003` | `client.domestic.kt50003` | 금현물 취소주문 | `POST /api/dostk/ordr` |
| 국내주식 | 계좌 | `kt50020` | `client.domestic.kt50020` | 금현물 잔고확인 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt50021` | `client.domestic.kt50021` | 금현물 예수금 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt50030` | `client.domestic.kt50030` | 금현물 주문체결전체조회 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt50031` | `client.domestic.kt50031` | 금현물 주문체결조회 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt50032` | `client.domestic.kt50032` | 금현물 거래내역조회 | `POST /api/dostk/acnt` |
| 국내주식 | 계좌 | `kt50075` | `client.domestic.kt50075` | 금현물 미체결조회 | `POST /api/dostk/acnt` |
| 미국주식 | 순위정보 | `usa01980` | `client.overseas.usa01980` | 미국주식 실시간 종목 조회 순위 | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa01990` | `client.overseas.usa01990` | 미국주식 관심종목 등록 상위 | `POST /api/us/rkinfo` |
| 미국주식 | 차트 | `usa06010` | `client.overseas.usa06010` | 미국주식 틱 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06011` | `client.overseas.usa06011` | 미국주식 분 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06012` | `client.overseas.usa06012` | 미국주식 일 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06013` | `client.overseas.usa06013` | 미국주식 주 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06014` | `client.overseas.usa06014` | 미국주식 월 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06015` | `client.overseas.usa06015` | 미국주식 년 차트 | `POST /api/us/chart` |
| 미국주식 | 차트 | `usa06016` | `client.overseas.usa06016` | 미국주식 분기 차트 | `POST /api/us/chart` |
| 미국주식 | 종목정보 | `usa10098` | `client.overseas.usa10098` | 미국주식 거래소구분 조회 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10099` | `client.overseas.usa10099` | 미국주식 종목리스트 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10100` | `client.overseas.usa10100` | 미국주식 종목 조회 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10101` | `client.overseas.usa10101` | 미국주식 업종리스트 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10102` | `client.overseas.usa10102` | 미국지수 리스트 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10104` | `client.overseas.usa10104` | 미국 ETF,ETN 리스트 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa10105` | `client.overseas.usa10105` | 미국 ETF 카테고리 리스트 | `POST /api/us/stkinfo` |
| 미국주식 | 시세 | `usa20100` | `client.overseas.usa20100` | 미국주식 현재가 종목정보 | `POST /api/us/mrkcond` |
| 미국주식 | 시세 | `usa20101` | `client.overseas.usa20101` | 미국주식 현재가 10호가 | `POST /api/us/mrkcond` |
| 미국주식 | 시세 | `usa20150` | `client.overseas.usa20150` | 미국주식 상세 체결내역 | `POST /api/us/mrkcond` |
| 미국주식 | 시세 | `usa20151` | `client.overseas.usa20151` | 미국주식 일별 체결내역 | `POST /api/us/mrkcond` |
| 미국주식 | 관심종목 | `usa20200` | `client.overseas.usa20200` | 미국주식 관심종목 그룹 리스트 조회 | `POST /api/us/watchlist` |
| 미국주식 | 관심종목 | `usa20201` | `client.overseas.usa20201` | 미국주식 관심종목 그룹 상세 조회 | `POST /api/us/watchlist` |
| 미국주식 | 조건검색 | `usa20280` | `client.overseas.usa20280` | 미국주식 조건검색 목록조회 | `POST /api/us/websocket` |
| 미국주식 | 조건검색 | `usa20281` | `client.overseas.usa20281` | 미국주식 조건검색 요청 일반 | `POST /api/us/websocket` |
| 미국주식 | 조건검색 | `usa20290` | `client.overseas.usa20290` | 미국주식 조건검색 요청 실시간 | `POST /api/us/websocket` |
| 미국주식 | 조건검색 | `usa20291` | `client.overseas.usa20291` | 미국주식 조건검색 실시간 해제 | `POST /api/us/websocket` |
| 미국주식 | 순위정보 | `usa20510` | `client.overseas.usa20510` | 미국주식 기간별 등락률상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20511` | `client.overseas.usa20511` | 미국주식 기간별 등락률상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20512` | `client.overseas.usa20512` | 미국주식 기간별 등락률상위(관심종목) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa20520` | `client.overseas.usa20520` | 미국주식 거래량급등락(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20521` | `client.overseas.usa20521` | 미국주식 거래량급등락(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 순위정보 | `usa20530` | `client.overseas.usa20530` | 미국주식 당일 거래량 상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20531` | `client.overseas.usa20531` | 미국주식 당일 거래량 상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20540` | `client.overseas.usa20540` | 미국주식 당일 거래대금 상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20541` | `client.overseas.usa20541` | 미국주식 당일 거래대금 상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20550` | `client.overseas.usa20550` | 미국주식 시가총액상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20551` | `client.overseas.usa20551` | 미국주식 시가총액상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa20570` | `client.overseas.usa20570` | 미국주식 가격대별주가(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20571` | `client.overseas.usa20571` | 미국주식 가격대별주가(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 시세 | `usa20590` | `client.overseas.usa20590` | 미국주식 일별주가 | `POST /api/us/mrkcond` |
| 미국주식 | 순위정보 | `usa20880` | `client.overseas.usa20880` | 키움 거래 상위 종목(미국주식) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20881` | `client.overseas.usa20881` | 키움 거래 상위 종목(미국 ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20910` | `client.overseas.usa20910` | 미국주식 전일대비 등락률상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20911` | `client.overseas.usa20911` | 미국주식 전일대비 등락률상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20920` | `client.overseas.usa20920` | 미국주식 시가대비 등락률상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20921` | `client.overseas.usa20921` | 미국주식 시가대비 등락률상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20922` | `client.overseas.usa20922` | 미국주식 시가대비 등락률상위(관심종목) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa20930` | `client.overseas.usa20930` | 미국주식 가격급등락(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20931` | `client.overseas.usa20931` | 미국주식 가격급등락(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20932` | `client.overseas.usa20932` | 미국주식 가격급등락(관심종목) | `POST /api/us/stkinfo` |
| 미국주식 | 순위정보 | `usa20940` | `client.overseas.usa20940` | 미국주식 누적 등락률 상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20941` | `client.overseas.usa20941` | 미국주식 누적 등락률 상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20960` | `client.overseas.usa20960` | 미국주식 전일 거래상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa20961` | `client.overseas.usa20961` | 미국주식 전일 거래상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa20970` | `client.overseas.usa20970` | 미국주식 고가/저가 접근(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20971` | `client.overseas.usa20971` | 미국주식 고가/저가 접근(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa20972` | `client.overseas.usa20972` | 미국주식 고가/저가 접근(관심종목) | `POST /api/us/stkinfo` |
| 미국주식 | 계좌 | `usa21670` | `client.overseas.usa21670` | 미국주식 일별계좌수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `usa21680` | `client.overseas.usa21680` | 미국주식 월별계좌수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `usa21690` | `client.overseas.usa21690` | 미국주식 연도별계좌수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `usa21730` | `client.overseas.usa21730` | 미국주식 일별종목수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `usa21731` | `client.overseas.usa21731` | 미국주식 월별종목수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `usa21732` | `client.overseas.usa21732` | 미국주식 연도별종목수익률현황 | `POST /api/us/acnt` |
| 미국주식 | 업종 | `usa23000` | `client.overseas.usa23000` | 미국주식 업종별 기간별 수익률 조회 | `POST /api/us/sect` |
| 미국주식 | 업종 | `usa23100` | `client.overseas.usa23100` | 미국주식 업종별 등락률 상위/하위 조회 | `POST /api/us/sect` |
| 미국주식 | 종목정보 | `usa23400` | `client.overseas.usa23400` | 미국주식 거래량갱신(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa23401` | `client.overseas.usa23401` | 미국주식 거래량갱신(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa23402` | `client.overseas.usa23402` | 미국주식 거래량갱신(관심종목) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24100` | `client.overseas.usa24100` | 미국주식 신고가/신저가(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24101` | `client.overseas.usa24101` | 미국주식 신고가/신저가(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 순위정보 | `usa24110` | `client.overseas.usa24110` | 미국주식 최고최저가대비 상승하락(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24111` | `client.overseas.usa24111` | 미국주식 최고최저가대비 상승하락(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24120` | `client.overseas.usa24120` | 미국주식 특정일자 상승/하락 (주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24121` | `client.overseas.usa24121` | 미국주식 특정일자 상승/하락(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa24140` | `client.overseas.usa24140` | 미국주식 갭상승/갭하락(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24141` | `client.overseas.usa24141` | 미국주식 갭상승/갭하락(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 순위정보 | `usa24150` | `client.overseas.usa24150` | 미국주식 회전율 상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24151` | `client.overseas.usa24151` | 미국주식 회전율 상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24160` | `client.overseas.usa24160` | 미국주식 연속상승/하락 순위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24161` | `client.overseas.usa24161` | 미국주식 연속상승/하락 순위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24162` | `client.overseas.usa24162` | 미국주식 연속상승/하락 순위(관심종목) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24200` | `client.overseas.usa24200` | 미국주식 호가잔량상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24201` | `client.overseas.usa24201` | 미국주식 호가잔량상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 종목정보 | `usa24210` | `client.overseas.usa24210` | 미국주식 잔량률급증(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24211` | `client.overseas.usa24211` | 미국주식 잔량률급증(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24220` | `client.overseas.usa24220` | 미국주식 매물대집중(주식/업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa24221` | `client.overseas.usa24221` | 미국주식 매물대집중(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 순위정보 | `usa24290` | `client.overseas.usa24290` | 미국주식 주간거래 괴리율 상위(주식/업종) | `POST /api/us/rkinfo` |
| 미국주식 | 순위정보 | `usa24291` | `client.overseas.usa24291` | 미국주식 주간거래 괴리율 상위(ETF) | `POST /api/us/rkinfo` |
| 미국주식 | 투자정보 | `usa24300` | `client.overseas.usa24300` | 미국주식 리서치(미국주식/ETF) | `POST /api/us/invtinfo` |
| 미국주식 | 종목정보 | `usa26410` | `client.overseas.usa26410` | 미국주식 연도별 등락률(종목) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa26411` | `client.overseas.usa26411` | 미국주식 연도별 업종별 종목등락률 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa26412` | `client.overseas.usa26412` | 미국주식 연도별 ETF 카테고리별 종목등락률 | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa26413` | `client.overseas.usa26413` | 미국주식 연도별 등락률(업종) | `POST /api/us/stkinfo` |
| 미국주식 | 종목정보 | `usa26414` | `client.overseas.usa26414` | 미국주식 연도별 등락률(ETF) | `POST /api/us/stkinfo` |
| 미국주식 | 주문 | `ust20000` | `client.overseas.ust20000` | 미국주식 매수 주문 | `POST /api/us/ordr` |
| 미국주식 | 주문 | `ust20001` | `client.overseas.ust20001` | 미국주식 매도 주문 | `POST /api/us/ordr` |
| 미국주식 | 주문 | `ust20002` | `client.overseas.ust20002` | 미국주식 정정 주문 | `POST /api/us/ordr` |
| 미국주식 | 주문 | `ust20003` | `client.overseas.ust20003` | 미국주식 취소 주문 | `POST /api/us/ordr` |
| 미국주식 | 계좌 | `ust21050` | `client.overseas.ust21050` | 미국주식 원장 미체결 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21070` | `client.overseas.ust21070` | 미국주식 원장잔고확인 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21100` | `client.overseas.ust21100` | 미국주식 거래내역 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21110` | `client.overseas.ust21110` | 해외주식 예수금 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21111` | `client.overseas.ust21111` | 원화출금가능 금액 조회(원화대용 포함) | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21120` | `client.overseas.ust21120` | 통화별 예수금 및 증권 평가금현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21121` | `client.overseas.ust21121` | 해외증권 원장 평가금액현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21131` | `client.overseas.ust21131` | 해외증권 특정일 평가금액 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21132` | `client.overseas.ust21132` | 특정일 통화별 예수금 및 증권 평가금 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21150` | `client.overseas.ust21150` | 미국주식 일별 주문체결내역 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21160` | `client.overseas.ust21160` | 미국주식 예수금 상세 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21170` | `client.overseas.ust21170` | 미국주식 당일 종목별 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21180` | `client.overseas.ust21180` | 미국주식 기간별 주문내역 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21510` | `client.overseas.ust21510` | 미국주식 당일 주문체결 확인 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21530` | `client.overseas.ust21530` | 미국주식 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21610` | `client.overseas.ust21610` | 미국주식 당일매매 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21620` | `client.overseas.ust21620` | 미국주식 당일매매정리 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21630` | `client.overseas.ust21630` | 미국주식 당일 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21640` | `client.overseas.ust21640` | 미국주식 일별 종목별 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21650` | `client.overseas.ust21650` | 미국주식 기간별 수익률 현황 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21660` | `client.overseas.ust21660` | 미국주식 일별 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 계좌 | `ust21661` | `client.overseas.ust21661` | 미국주식 월별 실현손익 | `POST /api/us/acnt` |
| 미국주식 | 환전 | `ust31300` | `client.overseas.ust31300` | 환전 예상 금액 조회 | `POST /api/us/exchange` |
| 미국주식 | 환전 | `ust31301` | `client.overseas.ust31301` | 환율 조회 | `POST /api/us/exchange` |
| 미국주식 | 환전 | `ust31302` | `client.overseas.ust31302` | 환전 신청 | `POST /api/us/exchange` |
| 미국주식 | 주문 | `ust31490` | `client.overseas.ust31490` | 미국주식 주문가능수량(종목/증거금률별) | `POST /api/us/ordr` |
| 국내주식 | 실시간시세 | `00` | `client.domestic.tr_00` | 주문체결 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `04` | `client.domestic.tr_04` | 잔고 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0A` | `client.domestic.tr_0A` | 주식기세 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0B` | `client.domestic.tr_0B` | 주식체결 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0C` | `client.domestic.tr_0C` | 주식우선호가 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0D` | `client.domestic.tr_0D` | 주식호가잔량 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0E` | `client.domestic.tr_0E` | 주식시간외호가 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0F` | `client.domestic.tr_0F` | 주식당일거래원 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0G` | `client.domestic.tr_0G` | ETF NAV | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0H` | `client.domestic.tr_0H` | 주식예상체결 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0I` | `client.domestic.tr_0I` | 국제금환산가격 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0J` | `client.domestic.tr_0J` | 업종지수 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0U` | `client.domestic.tr_0U` | 업종등락 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0g` | `client.domestic.tr_0g` | 주식종목정보 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0m` | `client.domestic.tr_0m` | ELW 이론가 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0s` | `client.domestic.tr_0s` | 장시작시간 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0u` | `client.domestic.tr_0u` | ELW 지표 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `0w` | `client.domestic.tr_0w` | 종목프로그램매매 | `POST /api/dostk/websocket` |
| 국내주식 | 실시간시세 | `1h` | `client.domestic.tr_1h` | VI발동/해제 | `POST /api/dostk/websocket` |
| 미국주식 | 실시간시세 | `F4` | `client.overseas.F4` | 미국주식 실시간 주문 확인 | `POST /api/us/websocket` |
| 미국주식 | 실시간시세 | `F5` | `client.overseas.F5` | 미국주식 실시간 체결 | `POST /api/us/websocket` |
| 미국주식 | 실시간시세 | `FE` | `client.overseas.FE` | 미국주식 실시간 체결가 | `POST /api/us/websocket` |
| 미국주식 | 실시간시세 | `FT` | `client.overseas.FT` | 미국주식 10호가 | `POST /api/us/websocket` |