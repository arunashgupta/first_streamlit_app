import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 and Bluberry Oatmean')
streamlit.text('🥗Kale Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-range Eggs')
streamlit.text('🥑🍞 Avocado Toast')




streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


# Display the table on the page.
#New Section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

# using json normalizer funciton from pandas library to flatten or normalize data fruityvice_normalized using pandas taking th json version to normalize the data it would be showing in 
# table? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# below code will bring the above data in a datafrima like a table output it the screen as a table?
streamlit.dataframe(fruityvice_normalized)
#removing line of raw json from the app
# below code would display new code with header and choice of fruit in fruit_choice variable and its writtening the fruit-choce using write and then using get
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())






