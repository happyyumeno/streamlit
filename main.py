import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 入門')

st.write('ただの文字')

# df = pd.DataFrame({
#     '1':[1,2,3],
#     '2':[10,20,None]
    
# })

#st.area_chart(df)
#st.line_chart(df)
#st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
    
# )

# st.map(df)

st.write('プログレスバー')
'start!'

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'done!'
    # print(i)
    # time.sleep(1)

st.write('interactive')

left_column, right_column=st.columns(2)
button=left_column.button('右に表示')
if button:
    right_column.write('right')

ex=st.expander('call')
ex.write('text')

text=st.text_input('あなたの趣味')
cond=st.slider('調子は？',0,100,50)

# text=st.sidebar.text_input('あなたの趣味')
# cond=st.sidebar.slider('調子は？',0,100,50)
'あなたの趣味',text
'調子は',cond



st.write('image')

option=st.selectbox(
    '好きな数字',
    list(range(1,11))
)

'好きな数字は',option,'です'


# if st.checkbox('Show Image'):
#     img=Image.open('aaa.png')
#     st.image(img,caption='aaa',use_column_width=True)

#st.table(df)
#st.dataframe(df.style.highlight_min(axis=1),width=500,height=500)
#st.write(df.fillna(''))

"""
# syou
## setu
### kou

```python
import 
```
"""