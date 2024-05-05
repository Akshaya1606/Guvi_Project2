import pandas as pd
import streamlit as st
import mysql.connector
import plotly.express as px



mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="new_password",
 auth_plugin='mysql_native_password'

)

print(mydb)
mycursor = mydb.cursor(buffered=True)
mycursor.execute("USE project2")
#engine=create_engine('mysql+mysqlconnector://root:@localhost:3306/project2')


def display_chart(n):
    if n==1:
        fig = px.choropleth_mapbox(df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Transaction_count',
        mapbox_style="stamen-terrain", opacity=0.8,
        color_continuous_scale=px.colors.sequential.RdPu,
        zoom=3.5, center={"lat": 21.7679, "lon": 78.8718},
        hover_data=['State','Quater','Year','Transaction_count','Transaction_amount'])

        fig.update_geos(fitbounds="locations",visible=False)
        fig.update_layout(height=800)
        fig.update_layout(width=800)
        st.plotly_chart(fig,use_container_width=True)
    else:
        fig = px.choropleth_mapbox(df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color='Registered_Users',
        mapbox_style="stamen-terrain", opacity=0.8,
        color_continuous_scale=px.colors.sequential.ice_r,
        zoom=3.5, center={"lat": 21.7679, "lon": 78.8718},
        hover_data=['State','Quater','Year','Registered_Users'])

        fig.update_geos(fitbounds="locations",visible=False)
        fig.update_layout(height=800)
        fig.update_layout(width=800)
        st.plotly_chart(fig)

def displaycol3details(n):
    if n==1:
        container = st.container(height=800)
        with container:
                st.header('Transaction')
                st.write('All PhonePe transactions (UPI + Cards + Wallets)')
                st.write(transaction_count)
                st.write('Total payment value=',transaction_amount)
                st.write('Avg. transaction value',transaction_amountavg)
                st.header('Catogories')
                st.write(f'Recharge & bill payments: ',recharge)
                st.write(f'Peer-to-peer payments: ',peer)
                st.write(f'Merchant payments: ',merchant)
                st.write(f'Financial Services: ',finser)
                st.write(f'Others: ',other)

                button1 = st.button("State")
                button2 = st.button("District")
                button3 = st.button("Pincode")

                if button1:
                    st.dataframe(df1,hide_index=True)
                if  button2:
                    st.dataframe(df2,hide_index=True)
                if button3:
                    st.dataframe(df3,hide_index=True)
                
    else:
        container = st.container(height=800)
        with container:
                st.header('Users')
                st.write('Registered PhonePe Users till the required quater and year')
                st.write(rcount)
                st.write('Registered App Opens till the required quater and year')
                st.write(f"{app}")
                button1 = st.button("State")
                button2 = st.button("District")
                button3 = st.button("Pincode")

                if button1:
                    st.dataframe(df1,hide_index=True)
                if  button2:
                    st.dataframe(df2,hide_index=True)
                if button3:
                    st.dataframe(df3,hide_index=True)



    

st.set_page_config(
        page_title="PhonePe Pulse",
        layout="wide",
    )
image_url=r"C:\Users\Akshaya\Downloads\png-clipart-phonepe-india-unified-payments-interface-india-purple-violet.png"
st.markdown(f'<h1 style="text-align: center;"><img src="{image_url}" width="10">Phonepe Pulse Data Visualization and Exploration</h1>', unsafe_allow_html=True)

# Display the title and image
st.image(r"C:\Users\Akshaya\Downloads\png-clipart-phonepe-india-unified-payments-interface-india-purple-violet.png", width=50) 

phonepe = [':house: HOME', ':spiral_note_pad: ABOUT',':earth_asia: EXPLORE DATA', ':iphone: INSIGHTS']

# Create the tabs
tabs = st.tabs(phonepe)

# Add content to each tab
with tabs[0]:
    st.header('''Welcome to the Phonepe Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly ''')
    col1, col2= st.columns(2)

    with col1:
        st.header("Introduction")
        st.image(r"C:\Users\Akshaya\Documents\Phonepe_logo\Phonepe_logo\RGB\4x\PhonePe_white_horizontal.png")
        st.markdown("""
**The Indian digital payments story has truly captured the world's imagination.
From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet, and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government.
Founded in December 2015, PhonePe has been a strong beneficiary of the API-driven digitization of payments in India.
When we started, we were constantly looking for granular and definitive data sources on digital payments in India.
PhonePe Pulse is our way of giving back to the digital payments ecosystem.**
""")
        st.markdown('''**India’s digital transformation is a testament to the power of innovation to propel massive economic growth. From a cash-is-king mindset to walking into a store with a smartphone and the PhonePe app, India has transitioned to making payments digitally, almost overnight. As per the PhonePe Pulse – BCG report, merchant payments are expected to increase from 
                 20% in value today to 65% by 2026, further underscoring 
                 the role of the ubiquitous merchant in this transformation.**''')
        

    with col2:
        st.header("Innovation leading to accelerated growth")
        st.video(r"C:\Users\Akshaya\Downloads\WhatsApp Video 2024-05-01 at 18.08.05_1d4808a6.mp4")
        st.image(r"C:\Users\Akshaya\Downloads\Pulse-Insight-Header-Pulse-Bytes-Size.webp")
        
with tabs[1]:
    st.header("Phonepe Pulse")
    st.write('''**Pulse is PhonePe’s way of giving back to the ecosystem by creating an open data source that 
             showcases how India transacts in the digital payments landscape. Discover the latest data-driven insights and 
             deep dive into payment and insurance trends.**''')
    col1, col2= st.columns(2)
    with col1:
        st.image(r"C:\Users\Akshaya\Downloads\PhonePe.webp")
        
        st.image(r"C:\Users\Akshaya\Downloads\pulse-2.png")
        
    with col2:
        st.markdown("**The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.**")
        
        st.markdown("""**When PhonePe started 5 years back, we were constantly looking for definitive data sources on digital payments in India. Some of the questions we were seeking answers to were - 
                    How are consumers truly using digital payments? What are the top cases? Are kiranas across Tier 2 and 3 getting a facelift with the penetration of QR codes?**""")



        st.markdown("""**This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.**""")


        st.markdown("""**This year, as we crossed 2000 Cr. transactions and 30 Crore registered users, we thought as India's largest digital payments platform with 46% UPI market share, we have a ring-side view of how India sends, spends, manages and grows its money. So it was time to demystify and share the what, why and how of digital payments in India.**""")
        
        
        st.markdown("""**PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.**""")
        st.video(r"C:\Users\Akshaya\Downloads\WhatsApp Video 2024-05-01 at 18.08.04_03739f20.mp4")
    with tabs[2]:
        st.header('Explore Data of the PhonePe in terms of Transaction and User details')
        #st.markdown("<p style='font-family: Arial; font-size: 18px; color: blue;'>Customized text</p>", unsafe_allow_html=True)
        col1,col2,col3=st.columns([0.8,3.5,1.2])
        with col1:
         add_selectbox1 = st.selectbox("select",('Transactions','Users'))
         add_selectbox2 = st.selectbox("year",('2018','2019','2020','2021','2022','2023'))
         add_selectbox3 = st.selectbox("quater",('1','2','3','4'))
        with col2:
            if add_selectbox1=='Transactions':
                mycursor.execute(f"SELECT * from Map_Total_Transaction_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                df=pd.DataFrame(out,columns=['State','Year','Quater','Transaction_count','Transaction_amount'])
                display_chart(1)
            if add_selectbox1=='Users':
                mycursor.execute(f"SELECT * from Map_Total_User_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                df=pd.DataFrame(out,columns=['State','Year','Quater','Registered_Users'])
                display_chart(2)

        with col3:
            if add_selectbox1=='Transactions':
                mycursor.execute(f"SELECT sum(Transaction_count) from Aggregate_Transaction_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                transaction_count=f'₹{out[0][0]:,.0f}'
                mycursor.execute(f"SELECT sum(Transaction_amount) from Aggregate_Transaction_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                transaction_amount=f'₹{out[0][0]:,.0f}'
                mycursor.execute(f"SELECT avg(Transaction_count) from Aggregate_Transaction_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                transaction_amountavg=f'₹{out[0][0]:,.0f}'
                mycursor.execute(f"SELECT  sum(Transaction_count) from project2.aggregate_transaction_details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'  and Transaction_type='Recharge & bill payments'")
                out=mycursor.fetchall()
                recharge=f'{out[0][0]}'
                mycursor.execute(f"SELECT  sum(Transaction_count) from project2.aggregate_transaction_details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'  and Transaction_type='Peer-to-peer payments'")
                out=mycursor.fetchall()
                peer=f'{out[0][0]}'
                mycursor.execute(f"SELECT  sum(Transaction_count) from project2.aggregate_transaction_details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'  and Transaction_type='Merchant payments'")
                out=mycursor.fetchall()
                merchant=f'{out[0][0]}'
                mycursor.execute(f"SELECT sum(Transaction_count) from project2.aggregate_transaction_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}'  and Transaction_type='Financial Services'")
                out=mycursor.fetchall()
                finser=f'{out[0][0]}'
                mycursor.execute(f"SELECT sum(Transaction_count) from project2.aggregate_transaction_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}'  and Transaction_type='Others'")
                out=mycursor.fetchall()
                other=f'{out[0][0]}'
                mycursor.execute(f"SELECT  State, sum(District_amount) as sum1 from project2.top_transaction_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}' group by state order by sum1 desc limit 10 ")
                out=mycursor.fetchall()
                df1=pd.DataFrame(out,columns=['Top_States',''])
                mycursor.execute(f"SELECT  District, District_amount  from project2.top_transaction_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}'  order by District_amount desc limit 10 ")
                out=mycursor.fetchall()
                df2=pd.DataFrame(out,columns=['Top_Districts',''])
                mycursor.execute(f"SELECT  Pincode, District_amount  from project2.top_transaction_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}' order by District_amount desc limit 10 ")
                out=mycursor.fetchall()
                df3=pd.DataFrame(out,columns=['Top_Pincodes',''])
                displaycol3details(1)

            if add_selectbox1=='Users':
                mycursor.execute(f"SELECT sum(Registered_Users) from Map_User_Details where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out1=mycursor.fetchall()
                mycursor.execute(f"SELECT Distinct sum(Appopens) from Aggregate_User_Details1 where Year='{add_selectbox2}' and Quater='{add_selectbox3}'")
                out=mycursor.fetchall()
                rcount=f"{out1[0][0]}"
                app=f"{out[0][0]}"
                mycursor.execute(f"SELECT  State, sum(Registered_Users) as sum1 from project2.top_user_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}' group by state order by sum1 desc limit 10 ")
                out=mycursor.fetchall()
                df1=pd.DataFrame(out,columns=['Top_States',''])
                mycursor.execute(f"SELECT  District, Registered_Users  from project2.top_user_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}'  order by Registered_Users desc limit 10 ")
                out=mycursor.fetchall()
                df2=pd.DataFrame(out,columns=['Top_Districts',''])
                mycursor.execute(f"SELECT  Pincode, REgistered_Users  from project2.top_user_details where Year='{add_selectbox2}'and Quater='{add_selectbox3}' order by Registered_Users desc limit 10 ")
                out=mycursor.fetchall()
                df3=pd.DataFrame(out,columns=['Top_Pincodes',''])
                displaycol3details(2)
    with tabs[3]:
        st.header('Here are the valuable insights based on the detils of the Transaction and User details')
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     type=st.selectbox('Select Typr',('Transaction','User'))
        #     if type=='Transaction':
        #         transaction= st.selectbox('Select Transaction type',
        #                                     ('Recharge & bill payments', 'Peer-to-peer payments',
        #                                      'Merchant payments', 'Financial Services', 'Others'))

        # with col2:
        #     year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
        # with col3:
        #     quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
        selectquerybox=st.selectbox('Select the insights',('1.District wise representation of the usage','2.Brand wise hierarchy in PhonePe Usage','3.Which type of transaction has highest usage','4.State VS Transaction type visualization based on Transaction Amount','5.City wise hierarchy of highest transaction','6.What is the average transaction in each State in the selected quater','7 What is the trend of transaction in the particular year','8.What is the trend of the registered Users in the selected year','9.Top states liking the selected Type of Transaction in the selected Quater','10.Total App opening in the selected year and quater'))
        if selectquerybox=='1.District wise representation of the usage':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"SELECT * from project2.Map_User_Details where Year='{year}' and Quater='{quater}'")
            out=mycursor.fetchall()
            detail=pd.DataFrame(out,columns=['District','State', 'Year','Quater','Registered_Users'])
            fig = px.sunburst(detail, path=['State', 'District'], values='Registered_Users',color='Registered_Users',color_continuous_scale='teal_r')
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='2.Brand wise hierarchy in PhonePe Usage':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"Select Brand_Usage ,sum(Registered_Users) from project2.Aggregate_User_Details01 where Year='{year}' and Quater='{quater}' group by Brand_Usage")
            out=mycursor.fetchall()
            detail=pd.DataFrame(out,columns=['Brand_the_User_use','Registered_Users'])
            fig =px.pie(detail, values='Registered_Users', names='Brand_the_User_use', title='Brandwise spread of Registered Users',color_discrete_sequence=px.colors.sequential.Plasma_r)
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='3.Which type of transaction has highest usage':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"Select  Transaction_type,sum(Transaction_count) from project2.Aggregate_Transaction_Details where Year='{year}' and Quater='{quater}' group by Transaction_type")
            out=mycursor.fetchall()
            detail=pd.DataFrame(out,columns=['Transaction_type','Transaction_count'])
            fig = px.bar(detail, x="Transaction_count", y="Transaction_type", orientation='h',color='Transaction_type',color_discrete_sequence=px.colors.sequential.Rainbow_r,)
            fig.update_layout(legend={'traceorder': 'normal'})
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            fig.update_layout(title="States", xaxis_title_standoff=20)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='4.State VS Transaction type visualization based on Transaction Amount':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"Select State,Transaction_type,Transaction_amount from project2.Aggregate_Transaction_Details where Year='{year}' and Quater='{quater}'")
            out=mycursor.fetchall()
            detail=pd.DataFrame(out,columns=['State','Transaction_type','Transaction_amount'])
            fig = px.bar(detail, x="State", y="Transaction_amount", color="Transaction_type",color_discrete_sequence=['#da6bff','#6b6bff','#ff6b6b','#CAB2D6','#FFFF99'])
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='5.City wise hierarchy of highest transaction':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"SELECT * from project2.Map_Transaction_Details where Year='{year}' and Quater='{quater}'")
            out=mycursor.fetchall()
            detail=pd.DataFrame(out,columns=['District','State', 'Year','Quater', 'Transaction_count', 'Transaction_amount'])
            fig = px.sunburst(detail, path=['State', 'District'], values='Transaction_count',color='Transaction_count',color_continuous_scale='haline_r')
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='6.What is the average transaction in each State in the selected quater':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"Select  State,avg(Transaction_amount) from project2.Aggregate_Transaction_Details where Year='{year}' and Quater='{quater}' group by State")
            out=mycursor.fetchall()
            details=pd.DataFrame(out,columns=['State','Average_Transaction'])
            fig = px.bar(details, x="State", y="Average_Transaction", orientation='v',color='Average_Transaction',color_continuous_scale='Pinkyl')
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='7 What is the trend of transaction in the particular year':
            year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            mycursor.execute(f"select quater, transaction_type,sum(Transaction_count) AS TotalTransactionCount FROM project2.aggregate_transaction_details WHERE year='{year}' GROUP BY quater, transaction_type")
            out=mycursor.fetchall()
            details=pd.DataFrame(out,columns=['Quater','Transaction_type','Transaction_count'])
            fig = px.line(details, x="Quater", y="Transaction_count", color="Transaction_type",color_discrete_sequence=['#ffdd1a','#00ffff','#ff6b6b','#ff33cc','#33ff33'])
            fig.update_traces(textposition="bottom right")
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='8.What is the trend of the registered Users in the selected year':
            year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            mycursor.execute(f"select quater, sum(Registered_users) AS Total_registers FROM project2.aggregate_user_details WHERE year='{year}' GROUP BY quater")
            out=mycursor.fetchall()
            details=pd.DataFrame(out,columns=['Quater','Registered_users'])
            fig = px.line(details, x="Quater", y="Registered_users")
            fig.update_traces(textposition="bottom right")
            fig.update_layout(height=780)
            fig.update_layout(width=780)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='9.Top states liking the selected Type of Transaction in the selected Quater':
            col1, col2, col3 = st.columns(3)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            with col3:
                transaction= st.selectbox('Select Type of transaction',('Recharge & bill payments', 'Peer-to-peer payments','Merchant payments', 'Financial Services', 'Others'))
            mycursor.execute(f"select State,Transaction_amount FROM project2.aggregate_transaction_details WHERE year='{year}' and quater='{quater}' and transaction_type='{transaction}' order by Transaction_amount desc limit 10")
            out=mycursor.fetchall()
            details=pd.DataFrame(out,columns=['State','Transaction_amount'])
            fig = px.bar(details, x="Transaction_amount", y="State", orientation='h',color='Transaction_amount',color_continuous_scale='Blues')
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
        if selectquerybox=='10.Total App opening in the selected year and quater':
            col1,col2=st.columns(2)
            with col1:
                year = st.selectbox('Select Year', ('2018', '2019', '2020', '2021', '2022','2023'))
            with col2:
                quater = st.select_slider('Select Quarter', ('1', '2', '3', '4'))
            mycursor.execute(f"Select State,Appopens,Brand_Usage,Registered_users FROM project2.aggregate_user_details01 WHERE year='{year}' and quater='{quater}'")
            out=mycursor.fetchall()
            details=pd.DataFrame(out,columns=['State','Appopens','Brand_Usage','Registered_users'])
            fig = px.bar(details, x="Appopens", y="State", orientation='h',color='Brand_Usage',color_continuous_scale='Reds')
            fig.update_layout(height=780)
            fig.update_layout(width=800)
            st.plotly_chart(fig,use_container_width=True)
css = '''
<style>
.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 2rem;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)
