import streamlit as st
import numpy as np



# Title of program
st.title("CHARACTERIZING AND PREDICTING RESERVOIR FACIES USING MACHINE LEARNING APPROACH, IN THE NIGER DELTA BASIN, NIGERIA")
st.sidebar.title('Inputs')

# Taking input from slider
k = st.sidebar.slider('Permeability(mD)', min_value = 10, max_value = 200, value = 100)

mu = st.sidebar.slider('Porosity', min_value = 10, max_value = 50, value = 15)

q = st.sidebar.slider('Flowrate(STB/day)', min_value = 100, max_value = 500, value = 200)


# Taking inputs from number inputs 

re = st.sidebar.number_input('Rock Eval Pyrolysis', min_value = 100, max_value = 10000, value = 3000)

rw = st.sidebar.number_input('Total Organic Carbon (TOC)', min_value = 1, max_value = 10, value = 1)

pe = st.sidebar.number_input('Palynomorph', min_value = 100, max_value = 10000, value = 4000)

B = st.sidebar.number_input('Scan Electrode Microscopy (SEM)', min_value = 2, max_value = 500, value = 30)

h = st.sidebar.number_input('Net pay thickness of Reservoir (feet)', min_value = 2, max_value =500, value =30)

r = np.linspace(re,re,500)

p = pe - (141.2 * q * mu * B * (np.log(re/r))/k/h)

# y_min = P[np.where(r==rw)]

b = st.button("Show AI's Prediction")

#What will happen if user clicks the b button

if b:
   
    plt.figure(figsize = (8,6))
    fig,ax = plt.subplots()
    ax.plot(r,p,linewidth = 4)
    ax.grid(True)
    ax.axhline(y_min,linewidth=3,color = 'red')
    ax.set_xlabel('radius(feet)')
    ax.set_ylabel('Pressure at radius r, (PSI)')
    ax.set_title('Pressure Profile')
    ax.set_ylim(0,5000)
    
    #Plot
    st.pyplot(fig)





