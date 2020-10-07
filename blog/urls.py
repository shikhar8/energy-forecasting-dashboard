from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^cost$',views.cost,name='cost'),
    url(r'^consumer_demand_map$',views.consumer_demand_map,name='consumer_demand_map'),
    url(r'^prosumer_supply$',views.prosumer_supply,name='prosumer_supply'),
    url(r'^conventional_energy_generated$',views.conventional_energy_generated,name='conventional_energy_generated'),
    url(r'^accuracy_of_forecasting_models$',views.accuracy_of_forecasting_models,name='accuracy_of_forecasting_models'),
    url(r'^scheduling_decision_report$',views.scheduling_decision_report,name='scheduling_decision_report'),
    url(r'^contact_us$',views.contact_us,name='contact_us'),
    url(r'^load_power_accuracy$', views.load_power_accuracy, name='load_power_accuracy'),
    url(r'^solar_power_accuracy$', views.solar_power_accuracy, name='solar_power_accuracy'),
    url(r'^wind_power_accuracy$', views.wind_power_accuracy, name='wind_power_accuracy'),
    url(r'^cost_accuracy$', views.cost_accuracy, name='cost_accuracy'),
]