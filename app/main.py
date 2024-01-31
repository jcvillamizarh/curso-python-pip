import utils
import read_csv
import charts
import pandas as pd

'''
def draw_country_population_bar():
  data = read_csv.read_csv('./data.csv')
  country = input('Type Country to get data => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


def draw_world_population_percetages_pie():
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries, percentages = utils.world_population_percentage(data)
  charts.generate_pie_chart(countries, percentages)
'''

def draw_pie_char():
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('./data.csv')
  country = input('Type Country to get data => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


def run():
  draw_pie_char()
  '''
  draw_world_population_percetages_pie()
  draw_country_population_bar()
  '''

if __name__ == '__main__':
  run()
