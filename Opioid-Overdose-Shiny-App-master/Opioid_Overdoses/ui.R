#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  #titlePanel("Opioid Overdose Deaths in the United States 2015-2017"),
  
  headerPanel("DEEP GEEKS PROJECT FOR HACKATHON SPRING 2018"),
  sidebarPanel(
      
      
      radioButtons("odType", "Choose type of Opioid Overdose:",
                   c("Opioids (T40.0-T40.4,T40.6)" = "Opioids (T40.0-T40.4,T40.6)", 
                     "Heroin (T40.1)" = "Heroin (T40.1)",
                     "Cocaine (T40.5)" = "Cocaine (T40.5)",
                     "Number of Deaths" = "Number of Deaths",
                     "Psychostimulants with abuse potential (T43.6)" = "Psychostimulants with abuse potential (T43.6)" )),
      radioButtons("statType", "Choose Statistic:",
                         c("DataValue" = "DataValue", 
                           "PercentComplete" = "PercentComplete",
                           "PercentPendingInvestigation" = "PercentPendingInvestigation")),
      h3(tableOutput("tableYear")),
      htmlOutput('myTable')
      ),
      
  mainPanel(
     h1("Hackathon 2018 by DeepGeeks"),
    h2("Opioid OverdosePredictive Model Description"),
     p("This app shows the analysis of Opioid Overdose Death Statistics in U.S."),
     
     sliderInput("Year", "Select Year to be displayed:",
                  min = 2015, max =2017, value = 2015, step = 1,
                  animate = TRUE, sep = "", width = 500 ),
     h3(textOutput("mapYear")),
     htmlOutput("choropleth"),
     helpText( p("Note: States which appear green on the map represent unavailable data for that year/overdose type"),
               a("Centers for Disease Control and Prevention: Opioid Overdoses", 
                 href = "https://www.cdc.gov/drugoverdose/index.html", target ="_blank" ))
  )
  
 
))
