import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# List of available ETF symbols
etf_symbols = ['MAXHEALTH.NS', 'NIF10GETF.NS', 'MOQUALITY.NS', 'MOSMALL250.NS', 'MONIFTY500.NS', 'MOHEALTH.NS', 'HDFCLOWVOL.NS', 
    'SMALLCAP.NS', 'HEALTHADD.NS', 'PHARMABEES.NS', 'HEALTHY.NS', 'HEALTHIETF.NS', 'HDFCQUAL.NS',
    'SBIETFCON.NS', 'GSEC5IETF.NS', 'METALIETF.NS', 'OILIETF.NS', 'HDFCSML250.NS',
    'NIFTYQLITY.NS', 'SDL24BEES.NS', 'FMCGIETF.NS', 'SETF10GILT.NS', 'HDFCNEXT50.NS', 'NIFMID150.NS',
    'LICNETFN50.NS', 'AXISHCETF.NS', 'GSEC10IETF.NS', 'NV20.NS', 'MOMOMENTUM.NS', 'NV20.NS',
    'MOM100.NS', 'LOWVOL.NS', 'LICNETFGSC.NS', 'PSUBANK.NS', 'SETFNN50.NS', 'ABSLBANETF.NS',
    'MAFANG.NS', 'ALPHA.NS', 'CONS.NS', 'MOM30IETF.NS', 'HDFCMID150.NS', 'LICNFNHGP.NS', 'BSLSENETFG.NS',
    'MOVALUE.NS', 'FINIETF.NS', 'SBINEQWETF.NS', 'ABSLPSE.NS', 'NETF.NS', 'MID150BEES.NS', 'MAKEINDIA.NS',
    'BSE500IETF.NS', 'NIF5GETF.NS', 'COMMOIETF.NS', 'QUAL30IETF.NS', 'NIFTYBETF.NS', 'SENSEXIETF.NS',
    'MOMENTUM.NS', 'IT.NS', 'MASPTOP50.NS', 'TOP100CASE.NS', 'MID150CASE.NS', 'NIFTY1.NS', 'DIVOPPBEES.NS',
    'SBIETFQLTY.NS', 'LOWVOLIETF.NS', 'NIF100BEES.NS', 'HDFCMOMENT.NS', 'GROWWEV.NS', 'NEXT50.NS',
    'HDFCGROWTH.NS', 'HDFCNIFTY.NS', 'MIDCAPIETF.NS', 'SENSEXETF.NS', 'MIDCAP.NS', 'CONSUMIETF.NS',
    'AXISTECETF.NS', 'AUTOBEES.NS', 'UTINEXT50.NS', 'AUTOIETF.NS', 'GSEC10YEAR.NS', 'BSLGOLDETF.NS',
    'CPSEETF.NS', 'INFRABEES.NS', 'MOM50.NS', 'HDFCBSE500.NS', 'BSLNIFTY.NS', 'TECH.NS', 'EQUAL50ADD.NS',
    'EBBETF0425.NS', 'SETFNIF50.NS', 'GOLDCASE.NS', 'AXISNIFTY.NS', 'HDFCVALUE.NS', 'IDFNIFTYET.NS',
    'LOWVOL1.NS', 'NIF100IETF.NS', 'ESG.NS', 'MIDCAPETF.NS', 'JUNIORBEES.NS', 'ICICIB22.NS', 'MOGSEC.NS',
    'MIDQ50ADD.NS', 'SHARIABEES.NS', 'NIFTYIETF.NS', 'LTGILTBEES.NS', 'HDFCNIF100.NS', 'UTISXN50.NS',
    'NEXT50IETF.NS', 'INFRAIETF.NS', 'EVINDIA.NS', 'ABSLNN50ET.NS', 'MIDSMALL.NS', 'NIFTYETF.NS',
    'QNIFTY.NS', 'UTISENSETF.NS', 'GILT5YBEES.NS', 'TNIDETF.NS', 'EBBETF0431.NS', 'EBBETF0430.NS',
    'NPBET.NS', 'ALPL30IETF.NS', 'LIQUIDCASE.NS', 'NIFTYBEES.NS', 'LIQUIDSHRI.NS', 'LIQUID1.NS',
    'LIQUIDADD.NS', 'NIFTY50ADD.NS', 'HDFCLIQUID.NS', 'LIQUIDIETF.NS', 'LIQUIDSBI.NS', 'ALPHAETF.NS',
    'LIQUIDETF.NS', 'IVZINNIFTY.NS', 'LIQUIDBEES.NS', 'AXISILVER.NS', 'LIQUID.NS', 'ABGSEC.NS',
    'LIQUIDBETF.NS', 'ABSLLIQUID.NS', 'NIFITETF.NS', 'TATAGOLD.NS', 'BBETF0432.NS', 'SILVER1.NS',
    'SDL26BEES.NS', 'LICMFGOLD.NS', 'BBNPNBETF.NS', 'GOLDETFADD.NS', 'IVZINGOLD.NS', 'CONSUMBEES.NS',
    'MIDSELIETF.NS', 'NV20BEES.NS', 'ITETF.NS', 'ITETFADD.NS', 'AXISGOLD.NS', 'GOLDETF.NS', 'GOLDSHARE.NS',
    'HDFCSENSEX.NS', 'LICNETFSEN.NS', 'TATSILV.NS', 'QGOLDHALF.NS', 'NV20IETF.NS', 'AXISCETF.NS',
    'EGOLD.NS', 'MON100.NS', 'HDFCGOLD.NS', 'AXISBPSETF.NS', 'AXSENSEX.NS', 'HDFCNIFBAN.NS', 'BANKBETF.NS',
    'GOLD1.NS', 'NAVINIFTY.NS', 'HDFCNIFIT.NS', 'BBNPPGOLD.NS', 'GOLDBEES.NS', 'MAHKTECH.NS', 'SILVERADD.NS',
    'ITBEES.NS', 'SENSEXADD.NS', 'LICNMID100.NS', 'ITIETF.NS', 'UTIBANKETF.NS', 'BANKNIFTY1.NS',
    'PSUBANKBEES.NS', 'HDFCPVTBAN.NS', 'GSEC10ABSL.NS', 'SETFNIFBK.NS', 'BFSI.NS',
    'AXISBNKETF.NS', 'SBIETFIT.NS', 'BANKBEES.NS', 'SILVRETF.NS', 'PSUBNKIETF.NS', 'HDFCPSUBK.NS',
    'EBBETF0433.NS', 'BANKETFADD.NS', 'SBIETFPB.NS', 'PVTBANIETF.NS', 'GOLDIETF.NS', 'PVTBANKADD.NS',
    'BANKETF.NS', 'SILVERIETF.NS', 'PSUBANKADD.NS', 'HNGSNGBEES.NS', 'BANKIETF.NS', 'ESILVER.NS',
    'SILVERETF.NS', 'MONQ50.NS', 'SILVER.NS', 'HDFCSILVER.NS', 'SILVERBEES.NS', 'SBISILVER.NS',
    'MOREALTY.NS', 'MNC.NS'
]

st.title("ETF Analysis Dashboard")
selected_etfs = st.multiselect("Select ETFs", etf_symbols, default=['BANKBEES.NS'])

start_date = st.date_input("Start Date", pd.to_datetime('2020-01-01'))
end_date = st.date_input("End Date", pd.to_datetime('today'))

monthly_fig = go.Figure()  
yearly_fig = go.Figure()
cumulative_returns_fig = go.Figure()

color_palette = ["#636EFA", "#EF553B", "#00CC96", "#AB63A1", "#FFA15C", "#19D3F3", "#FF6692", "#B6E880", "#F4CBF5"]

for i, etf in enumerate(selected_etfs):

    data = yf.download(etf, start=start_date, end=end_date)
    
    data['Month'] = data.index.to_period('M')  
    monthly_data = data['Close'].resample('M').agg(['first', 'last'])
    
    # Flatten columns to access 'first' and 'last'
    monthly_data.columns = ['_'.join(col).strip() for col in monthly_data.columns.values]
    
    monthly_returns = ((monthly_data['Close_first'] - monthly_data['Close_last']) / monthly_data['Close_first']) * 100

    data['Year'] = data.index.year  
    yearly_data = data['Close'].resample('Y').agg(['first', 'last']) 
    
    # Flatten columns for yearly data
    yearly_data.columns = ['_'.join(col).strip() for col in yearly_data.columns.values]
    
    yearly_returns = ((yearly_data['Close_first'] - yearly_data['Close_last']) / yearly_data['Close_first']) * 100

    monthly_fig.add_trace(go.Scatter(x=monthly_returns.index, y=monthly_returns, mode="lines", name=etf, line=dict(color=color_palette[i])))
    yearly_fig.add_trace(go.Scatter(x=yearly_returns.index, y=yearly_returns, mode="lines", name=etf, line=dict(color=color_palette[i])))
    cumulative_returns_fig.add_trace(go.Scatter(x=data.index, y=(data['Close'] / data['Close'].iloc[0] - 1) * 100, mode="lines", name=etf, line=dict(color=color_palette[i])))

monthly_fig.update_layout(title="Monthly Returns", xaxis_title="Date", yaxis_title="Returns (%)", xaxis_rangeslider_visible=False)
yearly_fig.update_layout(title="Yearly Returns", xaxis_title="Date", yaxis_title="Returns (%)", xaxis_rangeslider_visible=False)
cumulative_returns_fig.update_layout(title="Cumulative Returns", xaxis_title="Date", yaxis_title="Returns (%)", xaxis_rangeslider_visible=False)

st.plotly_chart(monthly_fig)
st.plotly_chart(yearly_fig)
st.plotly_chart(cumulative_returns_fig)


