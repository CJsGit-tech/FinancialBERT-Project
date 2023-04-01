import streamlit as st
import pandas as pd 
import numpy as np

@st.cache_data
def read_data(path):
    df = pd.read_csv(path,encoding_errors='ignore')
    cols = list(df.columns)
    return df, cols

# App Title
st.title('Text Data Label Inspector Application')

upload_data = st.file_uploader(label='Upload CSV:')
if upload_data is None:
    st.stop()
df,cols = read_data(upload_data)


# Num Rows Display
if 'num_row' not in st.session_state:
    st.session_state['num_row'] = 5

# Create Buttons
with st.expander("Check Entire Dataframe"):
    st.subheader("Show DataFrame")
    col1, col2 = st.columns([2,0.4])

    with col1:
        incre = st.button('add row')

    with col2:
        decre = st.button('minus row')

    if incre:
        st.session_state['num_row'] +=1

    if decre:
        st.session_state['num_row'] -= 1

    st.dataframe(df.head(st.session_state['num_row']))

###################################################################################
if 'text_idx' not in st.session_state:
    st.session_state['text_idx'] = 0

st.subheader('Data Inspection')
prev_button,nxt_button = st.columns([3,0.6],gap='small')

with nxt_button:
    incre = st.button('Next Record',key='text')

with prev_button:
    decre = st.button('Previous Record',key='labels')

if incre and (st.session_state['text_idx'] <= len(df)):
    st.session_state['text_idx'] +=1

if decre and (st.session_state['text_idx'] > 0):
    st.session_state['text_idx'] -= 1


st.markdown(f":green[Current Index:] {st.session_state['text_idx']}")
text, labels = st.columns([3,1],gap='small')
record = df.iloc[st.session_state['text_idx']]
with text:
    st.write(record['text'])
with labels:
    st.write(":red[Sentiment Label:]\n\n" + record['sentiment'])
    st.write(":blue[Topic Label:]\n\n" + record['topics'])

###########################################################################
st.subheader('Adding Index for Modification')

if 'modification' not in st.session_state:
    st.session_state['modification'] = []
if 'indexes' not in st.session_state:
    st.session_state['indexes'] = []

add_idx_button,clear_idx_button = st.columns([3,0.6],gap='small')
drop, sentiment_change, topics_change = st.columns([1,1,1])

with add_idx_button:
    with drop:
        drop_or_not = st.radio('Drop Index', options = ['drop','keep'], index=0)
    with sentiment_change:
        sentiment = st.radio('Change Sentiment', options = list(df.sentiment.unique()), index=0)
    with topics_change:
        topic = st.radio('Change Topics', options = list(df.topics.unique()),index=0)

    add_idx = st.button(label = 'Add index')

with clear_idx_button:
    clear_idx = st.button(label = 'Clear index')

if add_idx and (st.session_state['text_idx'] not in st.session_state['indexes']):

    change_dict = {
        'index': st.session_state['text_idx'],
        'drop': drop_or_not,
        'sentiment':sentiment,
        'topic': topic
    }

    st.session_state['modification'].append(change_dict) 
    st.session_state['indexes'].append(change_dict['index'])

if clear_idx and (len(st.session_state['indexes']) >0):
    st.session_state['modification'].clear()
    st.session_state['indexes'].clear()

st.text("Indexes For Modification:\n\n" + str(st.session_state['indexes']))
###########################################################################

if len(st.session_state['indexes']) <= 0:
    st.stop()

st.subheader("Execute and Modify Dataframe")
mod_df = df.copy()
execute_modification = st.button(label='Execute')


if execute_modification:
    idx2drop = []
    for idx, item in enumerate(st.session_state['modification']):
        data_index = item['index']
        data_drop = item['drop']
        data_sent = item['sentiment']
        data_topic = item['topic']

        if data_drop == 'drop':
            idx2drop.append(data_index)
        else:
            mod_df.loc[int(data_index),'sentiment'] = data_sent
            mod_df.loc[int(data_index),'topics'] = data_topic
    st.info('Dropping Unwanted Indexes and Resetting Index')
    
    if len(idx2drop) > 0:
        mod_df = mod_df.drop(idx2drop,axis=0)
    
    mod_df = mod_df.reset_index(drop=True)

def clear_indexes():
    st.session_state['indexes'].clear()
    st.session_state['modification'].clear()

st.subheader("Download the Modified Dataframe")
download = st.download_button(label = "Download", on_click = clear_indexes,
                              data = mod_df.to_csv(index=0).encode('utf-8'), file_name = 'modified_df.csv',mime='text/csv')
