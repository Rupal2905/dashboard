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
    'PSUBNKBEES.NS', 'HDFCPVTBAN.NS', 'GSEC10ABSL.NS', 'SETFNIFBK.NS', 'BFSI.NS',
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
    monthly_returns = ((monthly_data['last'] - monthly_data['first']) / monthly_data['first']) * 100
    
    data['Year'] = data.index.year  
    yearly_data = data['Close'].resample('Y').agg(['first', 'last']) 
    yearly_returns = ((yearly_data['last'] - yearly_data['first']) / yearly_data['first']) * 100

    data['Cumulative_Return'] = (data['Close'] / data['Close'].iloc[0]) * 100 - 100
    dates = data.index

    last_6_months_return = (data['Close'].iloc[-1] - data['Close'].iloc[-126]) / data['Close'].iloc[-126] * 100
    last_3_months_return = (data['Close'].iloc[-1] - data['Close'].iloc[-63]) / data['Close'].iloc[-63] * 100
    annual_return = (data['Close'].iloc[-1] - data['Close'].iloc[-252]) / data['Close'].iloc[-252] * 100

    years = (data.index[-1] - data.index[0]).days / 365
    cagr = (data['Close'].iloc[-1] / data['Close'].iloc[0]) ** (1 / years) - 1

    rolling_max = data['Close'].cummax()
    drawdown = (data['Close'] - rolling_max) / rolling_max
    max_drawdown = drawdown.min() * 100

    average_annual_return = (data['Close'].iloc[-1] / data['Close'].iloc[-252]) - 1
    calmar_ratio = average_annual_return / abs(max_drawdown)

    daily_returns = data['Close'].pct_change()
    sharpe_ratio = daily_returns.mean() / daily_returns.std() * (252 ** 0.5)

    data['Daily_Return'] = data['Close'].pct_change()

    VaR_95 = np.percentile(data['Daily_Return'].dropna(), 5)
    Expected_Shortfall = (data['Daily_Return'][data['Daily_Return'] <= VaR_95].mean()) * 100

    color = color_palette[i % len(color_palette)]  
    monthly_fig.add_trace(go.Bar(x=monthly_returns.index, 
                                 y=monthly_returns, 
                                 name=f'{etf} Monthly Returns',
                                 marker=dict(color=color), 
                                 opacity=0.7))

    yearly_fig.add_trace(go.Bar(x=yearly_returns.index, 
                                y=yearly_returns, 
                                name=f'{etf} Yearly Returns',
                                marker=dict(color=color),
                                opacity=0.7))
    
    cumulative_returns_fig.add_trace(go.Scatter(
        x=dates, 
        y=data['Cumulative_Return'], 
        name=f'{etf} Cumulative Return',
        mode='lines', 
        line=dict(color=color, width=2)
    ))
    st.write('Performance Metrics')
    col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Last 6M Return", value=f"{last_6_months_return:.2f}%", delta="")
    st.metric(label="Annual Return", value=f"{annual_return:.2f}%", delta="")

with col2:
    st.metric(label="CAGR", value=f"{cagr * 100:.2f}%", delta="")
    st.metric(label="Max Drawdown", value=f"{max_drawdown:.2f}%", delta="")

with col3:
    st.metric(label="Last 3M Return", value=f"{last_3_months_return:.2f}%", delta="")
    st.metric(label="Calmar Ratio", value=f"{calmar_ratio:.2f}", delta="")

with col4:
    st.metric(label="Sharpe Ratio", value=f"{sharpe_ratio:.2f}", delta="")
    st.metric(label="Expected Shortfall", value=f"{Expected_Shortfall:.2f}%", delta="")

    
        
monthly_fig.update_layout(
    title=f"Monthly Returns for Selected ETFs ({start_date} to {end_date})",
    xaxis_title='Month',
    yaxis_title='Monthly Return (%)',
    xaxis_tickformat="%b %Y", 
    barmode='group', 
    template="plotly_dark",
)

yearly_fig.update_layout(
    title=f"Yearly Returns for Selected ETFs ({start_date} to {end_date})",
    xaxis_title='Year',
    yaxis_title='Yearly Return (%)',
    xaxis_tickformat="%Y", 
    barmode='group', 
    template="plotly_dark", 
)

cumulative_returns_fig.update_layout(
    title=f"Cumulative Returns for Selected ETFs ({start_date} to {end_date})",
    xaxis_title='Date',
    yaxis_title='Cumulative Return (%)',
    xaxis_tickformat="%b %Y",  
    template="plotly_dark",  
    showlegend=True,  
)

st.plotly_chart(monthly_fig)
st.plotly_chart(yearly_fig)
st.plotly_chart(cumulative_returns_fig)

# Create a DataFrame to hold the metrics
metrics_data = {
    "Metric": [
        "Last 6 Months Return", "Last 3 Months Return", "Annual Return", "CAGR", "Max Drawdown", "Calmar Ratio", "Sharpe Ratio"
    ],
    "Value": [
        f"{last_6_months_return:.2f}%", f"{last_3_months_return:.2f}%", f"{annual_return:.2f}%", f"{cagr * 100:.2f}%",
        f"{max_drawdown:.2f}%", f"{calmar_ratio:.2f}", f"{sharpe_ratio:.2f}"
    ]
}

# Create a DataFrame
metrics_df = pd.DataFrame(metrics_data)

# Display the table
st.subheader("Performance Metrics Table")
st.table(metrics_df)

