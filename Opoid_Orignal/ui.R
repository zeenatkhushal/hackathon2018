#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#


library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  #titlePanel(""),
  titlePanel("Deep Geeks Project for Hackathon Spring 2018"),
  shinythemes::themeSelector(),
  theme = "bootstrap.css",
  
#headerPanel("Hackathon Spring 2018"),
  #headerPanel("Opioid Overdose Deaths in 2015-2018"),
  sidebarPanel(
      
      
    checkboxGroupInput("odType", "Choose type of Opioid Overdose / Total Deaths:",
                 c("Percent with drugs specified" = "Percent with drugs specified", 
                   "Heroin (T40.1)" = "Heroin (T40.1)",
                   "Methadone (T40.3)" = "Methadone (T40.3)",
                   "Natural & semi-synthetic opioids (T40.2)" = "Natural & semi-synthetic opioids (T40.2)",
                   "Opioids (T40.0-T40.4,T40.6)" = "Opioids (T40.0-T40.4,T40.6)",
                   "Number of Deaths" = "Number of Deaths",
                   "Psychostimulants with abuse potential (T43.6)" = "Psychostimulants with abuse potential (T43.6)",
                   "Synthetic opioids, excl. methadone (T40.4)" = "Synthetic opioids, excl. methadone (T40.4)",
                   "Number of Drug Overdose Deaths" = "Number of Drug Overdose Deaths",
                   "Opioids (T40.0-T40.4,T40.6)" = "Opioids (T40.0-T40.4,T40.6)",
                   "Psychostimulants with abuse potential (T43.6)" = "Psychostimulants with abuse potential (T43.6)")),
      radioButtons("statType", "Choose Statistic:",
                         c("Total Deaths and/or Overdoses" = "DataValue")),
      h3(tableOutput("tableYear")),
      htmlOutput('myTable')
      ),
  
  mainPanel(
     h2("Opioid Overdose Deaths in 2015-2018"),
     p("The below graph shows the Opioid Overdose and/or Deaths in different states of US for the year 2015, 2016 and 2017.The slider bar shows the year from 2015-2018. The grey color in the graph shows the no data is available"),
     
     sliderInput("Year", "Select Year to be displayed:",
                  min = 2015, max =2018, value = 2015, step = 1,
                  animate = TRUE, sep = "", width = 500 ),
     h3(textOutput("mapYear")),
     htmlOutput("choropleth"),
     helpText( p("DataSet Link Provided for Use Case "),
               a("Centers for Disease Control and Prevention: Opioid Overdoses", 
                 href = "https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm", target ="_blank" ))
  )
  
 
))
