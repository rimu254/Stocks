import streamlit as st

def run():
    st.header('Welcome to Stockly!')
    st.markdown(
        """
        Stockly is a web application that allows you to see the growth of the companies for the past years according to 
        to your specification and the predictions of the growth of the companies for the next 5 years.
        **👈 Select Predictions or Company Charts from the sidebar** to see more!
        ### What can I do with Stockly?
        - See the predictions of the growth of the companies for the next 5 years.
        - See the growth of the companies for the past 5 years.
        - Compare the growth of the companies against each other.
        - Download the pictures of the charts.
        ### Want to learn more about these companies?
        Check out their websites!
        Links in the sidebar.
     
    """
    )
    tsl_icon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu4gCl3HPHeVBLIHxoaXHRTM-keB4s7j-N0Q&usqp=CAU"
    ggl_icon = "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
    amzn_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1200px-Amazon_logo.svg.png"
    aapl_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/1200px-Apple_logo_black.svg.png"
    nflx_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Netflix_2015_logo.svg/1200px-Netflix_2015_logo.svg.png"
    msft_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/768px-Microsoft_logo.svg.png?20210729021049"
    twtr_icon = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Twitter-logo.svg/768px-Twitter-logo.svg.png?20220821125553"
    meta_icon = "https://signsalad.com/wp-content/uploads/2021/11/Screenshot-2021-11-03-at-12.14.11.png"

    st.subheader('Tesla')
    col1, col2 = st.columns([1,1])
    with col1:
        st.image(tsl_icon, width=275, caption="Tesla Inc")
    with col2:
        st.markdown("""
        Tesla, Inc. is an American electric vehicle and clean energy company. Tesla's current products include electric cars, battery energy storage from home to grid scale, solar panels and solar roof tiles, as well as other related products and services.
        - Founded: 2003
        - Headquarters: Austin, Texas, United States
        - CEO: Elon Musk
        - Revenue: 81.46 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Apple')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(aapl_icon, width=150, caption="Apple Inc")
    with col2:
        st.markdown("""
        Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software, and online services. It is one of the world's largest technology companies by revenue and profit, and is widely recognized as one of the most innovative and successful companies in history.
        - Founded: 1976
        - Headquarters: Cupertino, California, United States
        - CEO: Tim Cook
        - Revenue: 117.2 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Netflix')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(nflx_icon, width=300, caption="Netflix Inc")
    with col2:
        st.markdown("""
        Netflix, Inc. is an American multinational entertainment company founded on August 29, 1997, in Scotts Valley, California, by Reed Hastings and Marc Randolph. It specializes in and provides streaming media and video-on-demand online and DVD by mail.
        - Founded: 1997
        - Headquarters: Los Gatos, California, United States
        - CEO: Ted Sarandos
        - Revenue: 31.6 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Amazon')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(amzn_icon, width=300, caption="Amazon Inc")
    with col2:
        st.markdown("""
        Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence. It's retail website, Amazon.com, is the world's largest online retailer and it's main source of revenue.
        - Founded: 1994
        - Headquarters: Bellevue, Washington, United States
        - CEO: Andy Jassy
        - Revenue: 514 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Google')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(ggl_icon, width=300, caption="Google Inc")
    with col2:
        st.markdown("""
        Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. It is one of the most used search engines in the world with over 80% market share.
        - Founded: 1998
        - Parent Organization: Alphabet Inc.
        - Headquarters: Mountain View, California, United States
        - CEO: Sundar Pichai
        - Revenue: 282.8 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Meta')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(meta_icon, width=275, caption="Meta Inc")
    with col2:
        st.markdown("""
        Meta, formally known as FaceBook, is an American technology company that specializes in Internet-related services and products, which include online social media and social networking services, Internet search, and online advertising. It is one of the world's largest social media companies. It recently diversified into virtual reality and augmented reality.
        - Founded: 2004
        - Headquarters: Menlo Park, California, United States
        - CEO: Mark Zuckerberg
        - Revenue: 116.61 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Twitter')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(twtr_icon, width=250, caption="Twitter Inc")
    with col2:
        st.markdown("""
        Twitter, Inc. is an American micro-blogging and social networking service on which users post and interact with messages known as "tweets". Registered users can post, like, and retweet tweets, but unregistered users can only read them.
        - Founded: 2006
        - Headquarters: San Francisco, California, United States
        - CEO: Elon Musk
        - Revenue: 3.72 billion USD (2022)
        """, unsafe_allow_html=True)

    st.subheader('Microsoft')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(msft_icon, width=250, caption="Microsoft Inc")
    with col2:
        st.markdown("""
        Microsoft Corporation is an American multinational technology company. It develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services.
        - Founded: 1975
        - Headquarters: Redmond, Washington, United States
        - CEO: Satya Nadella
        - Revenue: 198.27 billion USD (2022)
        """, unsafe_allow_html=True)


    st.sidebar.header('Company Websites 🌐')
    st.sidebar.markdown("""
            - [Tesla](https://www.tesla.com/about)
            - [Apple](https://www.apple.com/business/)
            - [Netflix](https://ir.netflix.net/ir-overview/profile/default.aspx)
            - [Amazon](https://www.aboutamazon.com/)
            - [Google](https://about.google/)
            - [Meta](https://www.meta.com/)
            - [Twitter](https://about.twitter.com/en)
            - [Microsoft](https://www.microsoft.com/en-us/about)
        """, unsafe_allow_html=True)
